import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

spec=importlib.util.spec_from_file_location('skill_bundle',Path(__file__).parents[1]/'skill_bundle.py')
bundle=importlib.util.module_from_spec(spec);spec.loader.exec_module(bundle)

class BundleTests(unittest.TestCase):
    def fixture(self,root):
        skill=root/'plugins/example/skills/example';skill.mkdir(parents=True)
        (skill/'SKILL.md').write_text('---\nname: example\ndescription: Test export behavior.\nmetadata:\n  departments: General\n---\n\nUse references/details.md.\n', encoding='utf-8')
        (skill/'references').mkdir();(skill/'references/details.md').write_text('Required details', encoding='utf-8')
        (root/'docs').mkdir();(root/'docs/departments.json').write_text('{"example":["General"]}', encoding='utf-8')
        (root/'README.md').write_text('# Example\n', encoding='utf-8');(root/'plugins/example/README.md').write_text('# Example\n', encoding='utf-8')
        (root/'plugins/example/.claude-plugin').mkdir();(root/'plugins/example/.claude-plugin/plugin.json').write_text('{"name":"example"}', encoding='utf-8')
        (root/'plugins/example/plugin.json').write_text(json.dumps({'$schema':'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json','name':'example'}), encoding='utf-8')
        return skill

    def test_export_preserves_resources_and_excludes_private_files(self):
        with tempfile.TemporaryDirectory(dir=Path.cwd()) as tmp:
            root=Path(tmp).resolve();skill=self.fixture(root)
            (skill/'.secret').mkdir();(skill/'.secret/never-read.txt').write_text('private fixture', encoding='utf-8')
            (skill/'.env').write_text('fixture', encoding='utf-8');(skill/'config.local.json').write_text('{}', encoding='utf-8')
            try:
                (skill/'outside-link').symlink_to(root/'README.md')
            except OSError:
                pass  # Optional filesystem capability; dedicated tests cover link rejection.
            with patch.object(bundle,'ROOT',root):
                bundle.export('example',None,os.path.relpath(root/'out'))
                with zipfile.ZipFile(root/'out/example.zip') as z:
                    self.assertEqual(set(z.namelist()),{'example/SKILL.md','example/references/details.md'})
                    self.assertEqual(z.read('example/references/details.md'),b'Required details')
                with self.assertRaisesRegex(ValueError,'overwrite'):bundle.export('example',None,os.path.relpath(root/'out'))

    def test_unicode_fingerprint_survives_windows_newlines(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp).resolve();skill=self.fixture(root)
            resource=skill/'references/details.md'
            resource.write_bytes('Résumé — 中文\n'.encode('utf-8'))
            before=bundle.digest(skill)
            resource.write_bytes('Résumé — 中文\r\n'.encode('utf-8'))
            self.assertEqual(before,bundle.digest(skill))
            resource.write_bytes('Changed résumé\r\n'.encode('utf-8'))
            self.assertNotEqual(before,bundle.digest(skill))

    def test_ambiguous_yaml_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp).resolve();skill=self.fixture(root)
            p=skill/'SKILL.md'
            p.write_text(p.read_text(encoding='utf-8').replace('name: example', 'name: example\nname: second'),encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'duplicate YAML field'):bundle.front(p)

    def test_export_rejects_protected_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp).resolve();self.fixture(root)
            with patch.object(bundle,'ROOT',root):
                with self.assertRaisesRegex(ValueError,'Protected output'):bundle.export('example',None,'.secret/output')

    def test_resource_edit_invalidates_both_readmes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp).resolve();skill=self.fixture(root)
            with patch.object(bundle,'ROOT',root):
                bundle.render();bundle.validate()
                before=(root/'README.md').read_text(encoding='utf-8');plugin_before=(root/'plugins/example/README.md').read_text(encoding='utf-8')
                (skill/'references/details.md').write_text('Changed behavior', encoding='utf-8')
                with self.assertRaisesRegex(ValueError,'Documentation out of date'):bundle.render(check=True)
                bundle.render();bundle.validate()
                self.assertNotEqual(before,(root/'README.md').read_text(encoding='utf-8'))
                self.assertNotEqual(plugin_before,(root/'plugins/example/README.md').read_text(encoding='utf-8'))

    def test_invalid_name_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp).resolve();skill=self.fixture(root)
            p=skill/'SKILL.md';p.write_text(p.read_text(encoding='utf-8').replace('name: example','name: Bad Name'), encoding='utf-8')
            with patch.object(bundle,'ROOT',root):
                with self.assertRaisesRegex(ValueError,'invalid name'):bundle.validate()

    def test_host_path_in_reference_blocks_bundle_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp).resolve();skill=self.fixture(root)
            p=skill/'references/details.md';p.write_text('Read `/Users/example/process.md`.\n', encoding='utf-8')
            with patch.object(bundle,'ROOT',root):
                bundle.render()
                with self.assertRaisesRegex(ValueError,'Workspace routing errors'):bundle.validate()

    def test_nested_protected_entrypoints_are_never_validated_or_catalogued(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp).resolve();skill=self.fixture(root)
            protected=skill/'.secret';protected.mkdir()
            (protected/'SKILL.md').write_text('Invalid fixture that must be excluded', encoding='utf-8')
            top_protected=root/'plugins/.secret';top_protected.mkdir()
            (top_protected/'SKILL.md').write_text('Invalid top-level fixture that must be excluded', encoding='utf-8')
            with patch.object(bundle,'ROOT',root):
                bundle.render();bundle.validate()
                self.assertEqual(len(bundle.skills()),1)

if __name__=='__main__':unittest.main()
