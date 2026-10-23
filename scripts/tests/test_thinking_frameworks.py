"""Thinking-framework references stay generated, scoped and idempotent."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('thinking_frameworks', REPO / 'scripts/thinking_frameworks.py')
tf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tf)

CARD = {'id': 'five-whys', 'group': 'think', 'name': '5 Whys', 'kind': 'widely used', 'firm_source': '',
        'used_by': [], 'what': 'Ask why until the cause is fixable.', 'when': 'Something broke.',
        'ordered_steps': True, 'steps': ['State the problem.', 'Ask why.'], 'habit': 'Use it in post-mortems.',
        'example': 'Late proposal.', 'watch_out': '', 'origin': 'Taiichi Ohno.',
        'sources': [{'title': 'Lean', 'url': 'https://www.lean.org/lexicon-terms/5-whys/'}], 'situations': ['problem']}
SKILL = ('---\nname: demo\ndescription: Demo.\nmetadata:\n  departments: General\n---\n\n# Demo\n\n'
         '```markdown\n## Anti-patterns\n```\n\n## Method\n\n1. Work.\n\n## Anti-patterns\n\n- None.\n')


class ThinkingFrameworks(unittest.TestCase):
    def make_root(self, folder, skills=None):
        root = Path(folder)
        (root / tf.SOURCE).mkdir(parents=True)
        data = {'source': {'title': 'Guide', 'format': 'HTML', 'checked': 'Checked.', 'marks': 'Marks.'},
                'groups': {'think': {'label': 'Think', 'purpose': 'x'}}, 'situations': {}, 'frameworks': [CARD]}
        (root / tf.SOURCE / 'frameworks.json').write_text(json.dumps(data), encoding='utf-8')
        mapping = {'excluded_plugins': {'legal': 'upstream'}, 'excluded_skills': {},
                   'skills': skills if skills is not None else
                   {'demo-plugin/demo': {'anchor': '## Anti-patterns',
                                         'frameworks': [{'id': 'five-whys', 'use': 'Step 1: ask why.'}]}}}
        (root / tf.SOURCE / 'skill-map.json').write_text(json.dumps(mapping), encoding='utf-8')
        skill = root / 'plugins/demo-plugin/skills/demo'
        skill.mkdir(parents=True)
        (skill / 'SKILL.md').write_text(SKILL, encoding='utf-8')
        other = root / 'plugins/demo-plugin/skills/other'
        other.mkdir(parents=True)
        (other / 'SKILL.md').write_text('# Other\n', encoding='utf-8')
        return root, skill, other

    def test_generate_check_and_idempotence(self):
        with tempfile.TemporaryDirectory() as folder:
            root, skill, other = self.make_root(folder)
            with self.assertRaises(ValueError):
                tf.sync(root, check=True)
            self.assertEqual((skill / 'SKILL.md').read_text(encoding='utf-8'), SKILL)
            self.assertEqual(tf.sync(root), 1)
            text = (skill / 'SKILL.md').read_text(encoding='utf-8')
            # Inserted before the real heading, not the fenced example.
            self.assertLess(text.index('```\n\n## Method'), text.index(tf.START))
            self.assertLess(text.index(tf.END), text.rindex('## Anti-patterns'))
            self.assertIn('references/thinking-frameworks.md', text)
            self.assertIn('**In this skill:** Step 1: ask why.', (skill / tf.REF).read_text(encoding='utf-8'))
            self.assertEqual(tf.sync(root, check=True), 1)
            tf.sync(root)
            self.assertEqual((skill / 'SKILL.md').read_text(encoding='utf-8'), text)
            self.assertEqual(tf.strip_block(text), SKILL)
            self.assertEqual((other / 'SKILL.md').read_text(encoding='utf-8'), '# Other\n')
            self.assertFalse((other / 'references').exists())

    def test_rejects_unknown_ids_style_and_excluded_plugins(self):
        bad = [{'demo-plugin/demo': {'anchor': None, 'frameworks': [{'id': 'nope', 'use': 'x'}]}},
               {'demo-plugin/demo': {'anchor': None, 'frameworks': [{'id': 'five-whys', 'use': 'a; b'}]}},
               {'demo-plugin/demo': {'anchor': '## Missing', 'frameworks': [{'id': 'five-whys', 'use': 'x'}]}},
               {'legal/demo': {'anchor': None, 'frameworks': [{'id': 'five-whys', 'use': 'x'}]}}]
        for skills in bad:
            with tempfile.TemporaryDirectory() as folder:
                root, skill, _ = self.make_root(folder, skills)
                with self.assertRaises(ValueError):
                    tf.sync(root)
                self.assertEqual((skill / 'SKILL.md').read_text(encoding='utf-8'), SKILL)

    def test_standalone_intro_preserves_attribution_and_default(self):
        with tempfile.TemporaryDirectory() as folder:
            root, skill, _ = self.make_root(folder)
            data, mapping = tf.load(root)
            default = tf.render_reference('demo', mapping['skills']['demo-plugin/demo']['frameworks'], data)
            self.assertIn('Selected from the Guide. Checked.', default)
            mapping['skills']['demo-plugin/demo']['reference_intro'] = 'Self-contained public introduction.'
            (root / tf.SOURCE / 'skill-map.json').write_text(json.dumps(mapping))
            tf.sync(root)
            reference = (skill / tf.REF).read_text()
            self.assertIn('Self-contained public introduction.', reference)
            self.assertNotIn('Selected from the Guide', reference)
            self.assertIn('**Origin:** Taiichi Ohno.', reference)
            self.assertIn('https://www.lean.org/', reference)
            tf.sync(root, check=True)

    def test_invalid_intro_does_not_write_generated_files(self):
        for value in ['', '   ', 42, []]:
            with tempfile.TemporaryDirectory() as folder:
                root, skill, _ = self.make_root(folder)
                _, mapping = tf.load(root)
                mapping['skills']['demo-plugin/demo']['reference_intro'] = value
                (root / tf.SOURCE / 'skill-map.json').write_text(json.dumps(mapping))
                with self.assertRaisesRegex(ValueError, 'reference_intro'):
                    tf.sync(root)
                self.assertEqual((skill / 'SKILL.md').read_text(), SKILL)
                self.assertFalse((skill / tf.REF).exists())

    def test_reports_orphans_without_deleting(self):
        with tempfile.TemporaryDirectory() as folder:
            root, skill, other = self.make_root(folder)
            (other / 'references').mkdir()
            (other / tf.REF).write_text('leftover', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, 'remove it manually'):
                tf.sync(root)
            self.assertEqual((other / tf.REF).read_text(encoding='utf-8'), 'leftover')

    def test_reject_symlink_destination(self):
        with tempfile.TemporaryDirectory() as folder:
            root, skill, _ = self.make_root(folder)
            outside = root / 'outside'
            outside.mkdir()
            (skill / 'references').symlink_to(outside, target_is_directory=True)
            with self.assertRaises(ValueError):
                tf.sync(root)
            self.assertFalse(list(outside.iterdir()))

    def test_repository_content_current(self):
        self.assertEqual(tf.sync(REPO, check=True), 1)


if __name__ == '__main__':
    unittest.main()
