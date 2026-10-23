"""Regressions for names, filesystem compatibility and renamed resources."""
import hashlib
import ast
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('portability', ROOT/'scripts/portability.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class PortabilityTests(unittest.TestCase):
    def test_name_budget_includes_namespace(self):
        self.assertIsNone(p.invocation_error('example-workflows', 'x'*46))
        self.assertIsNotNone(p.invocation_error('example-workflows', 'x'*47))

    def test_repository_skill_limit_is_separate_from_invocation_limit(self):
        self.assertIsNone(p.skill_name_error('x'*40))
        self.assertIsNotNone(p.skill_name_error('x'*41))
        self.assertIsNone(p.invocation_error('example-workflows', 'x'*40))
        self.assertIsNotNone(p.invocation_error('plugin-'+'x'*20, 'x'*40))

    def test_filename_and_relative_budgets_have_exact_utf16_boundaries(self):
        filename = 'a'*57+'.md'
        self.assertEqual(p.utf16_units(filename), 60)
        self.assertEqual(p.path_errors(['refs/'+filename]), [])
        self.assertTrue(any('Filename' in error for error in p.path_errors(['refs/x'+filename])))
        unicode_filename = '😀'*28+'x.md'
        self.assertEqual(p.utf16_units(unicode_filename), 60)
        self.assertEqual(p.path_errors(['refs/'+unicode_filename]), [])
        self.assertTrue(any('Filename' in error for error in p.path_errors(['refs/x'+unicode_filename])))
        relative = 'a'*50+'/'+'b'*50+'/'+'c'*35+'.md'
        self.assertEqual(p.utf16_units(relative), 140)
        self.assertEqual(p.path_errors([relative]), [])
        self.assertTrue(any('repository limit is 140' in error for error in p.path_errors(['x'+relative])))
        # The filename policy applies to the leaf, not every directory component.
        self.assertEqual(p.path_errors(['x'*61+'/file.md']), [])

    def test_full_paths_include_destination_root_and_separator(self):
        root = 'C:/'+'r'*251
        self.assertEqual(p.utf16_units(root+'/a.md'), 259)
        self.assertEqual(p.path_errors(['a.md'], root), [])
        self.assertTrue(any('Full path has 260' in error for error in p.path_errors(['a.md'], root+'r')))
        self.assertEqual(p.path_errors(['a.md'], root+'/'), [])
        with self.assertRaisesRegex(ValueError, 'absolute target root'):
            p.path_errors(['a.md'], 'relative/root')

    def test_report_is_measured_sorted_and_does_not_access_target(self):
        with patch.object(Path, 'exists', side_effect=AssertionError('No destination access')):
            report = p.path_report(['a.md', 'references/details.md'], 'C:/hypothetical/checkout')
        self.assertEqual(report['files'], 2)
        self.assertEqual(report['limits']['relative_utf16'], 140)
        self.assertEqual(report['limits']['filename_utf16'], 60)
        self.assertEqual(report['checkout_root_budget_utf16'], 118)
        self.assertEqual(report['max_relative_utf16'], len('references/details.md'))
        self.assertEqual(report['max_full_utf16'], len('C:/hypothetical/checkout/references/details.md'))
        self.assertEqual(report['longest'][0]['path'], 'references/details.md')
        self.assertEqual(report['errors'], [])

    def test_windows_names_and_directory_collisions(self):
        for name in ['assets/CON.md', 'assets/lpt1.txt', 'aux/file.md',
                     'assets/file:stream', 'assets/trailing.',
                     'assets/trailing ', 'a/'+'x'*179, '../escape']:
            with self.subTest(name=name):
                self.assertTrue(p.path_errors([name]))
        self.assertTrue(p.path_errors(['Refs/a.md', 'refs/b.md']))
        self.assertTrue(p.path_errors(['café/a.md', 'cafe\u0301/b.md']))
        self.assertEqual(p.path_errors(['assets/console.md', 'references/évidence.md']), [])

    def test_name_migrations_resolve_and_resources_retain_bytes(self):
        migration = json.loads((ROOT/'docs/skill-name-migration.json').read_text(encoding='utf-8'))
        for record in migration.values():
            if 'new_path' in record:
                target = ROOT/record['new_path']
                self.assertTrue(target.is_file(), target)
                self.assertEqual(target.parent.name, record['name'])
        resources = json.loads((ROOT/'docs/resource-path-migration.json').read_text(encoding='utf-8'))
        for record in resources:
            target = ROOT/record['path']
            self.assertFalse((ROOT/record['previous_path']).exists())
            self.assertEqual(hashlib.sha256(target.read_bytes()).hexdigest(), record['sha256'])


if __name__ == '__main__':
    unittest.main()
