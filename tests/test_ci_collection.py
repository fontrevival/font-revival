import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock

SPEC = importlib.util.spec_from_file_location('ci_collection', Path(__file__).resolve().parents[1] / 'scripts/ci_collection.py')
ci = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ci)


class CollectionSelectionTests(unittest.TestCase):
    families = ['first-1880', 'second-1890']

    def test_proof_revision_checks_only_its_family(self):
        plan = ci.select_checks(['collection/first-1880/specimens/specimen.pdf',
                                 'collection/first-1880/SHA256SUMS.txt'], self.families)
        self.assertEqual(plan, {'full': False, 'families': ['first-1880'], 'gallery': False, 'tests': True})

    def test_shared_tools_and_manual_audits_select_every_family(self):
        for path in ('scripts/fontrevival.py', 'scripts/svg_paths.py', 'requirements.txt',
                     'LICENSE', '.github/workflows/check.yml'):
            with self.subTest(path=path):
                plan = ci.select_checks([path], self.families)
                self.assertTrue(plan['full'])
                self.assertTrue(plan['gallery'])
                self.assertEqual(plan['families'], self.families)
        self.assertTrue(ci.select_checks([], self.families, full=True)['full'])

    def test_gallery_edits_do_not_rebuild_unaffected_fonts(self):
        for path in ('site/shared.css', 'icons/example.html', 'catalog.json'):
            with self.subTest(path=path):
                plan = ci.select_checks([path], self.families)
                self.assertEqual(plan['families'], [])
                self.assertTrue(plan['gallery'])

    def test_family_metadata_and_font_changes_also_check_gallery(self):
        for name in ('font.json', 'fonts/font.otf', 'svg/icon.svg', 'downloads/bundles.json'):
            with self.subTest(name=name):
                plan = ci.select_checks(['collection/first-1880/' + name], self.families)
                self.assertEqual(plan['families'], ['first-1880'])
                self.assertTrue(plan['gallery'])

    def test_deleted_and_renamed_families_check_gallery(self):
        plan = ci.select_checks(['collection/removed-1880/font.json',
                                 'collection/second-1890/font.json'], self.families)
        self.assertEqual(plan['families'], ['second-1890'])
        self.assertTrue(plan['gallery'])

    def test_docs_and_editor_pins_need_no_collection_rebuild(self):
        plan = ci.select_checks(['README.md', 'docs/WORKFLOW.md', 'site/editor-release.json'], self.families)
        self.assertEqual(plan, {'full': False, 'families': [], 'gallery': False, 'tests': False})
        plan = ci.select_checks(['tests/test_site.py', 'scripts/build_site.py'], self.families)
        self.assertEqual(plan, {'full': False, 'families': [], 'gallery': False, 'tests': True})

    def test_missing_successful_baseline_falls_back_to_full_audit(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for family in self.families:
                path = root / 'collection' / family
                path.mkdir(parents=True)
                (path / 'font.json').write_text('{}')
            with mock.patch.object(ci.subprocess, 'check_output', return_value='a' * 40):
                self.assertTrue(ci.plan(root)['full'])
            with mock.patch.object(ci.subprocess, 'check_output', side_effect=[
                subprocess.CalledProcessError(128, 'git'), 'a' * 40]):
                self.assertTrue(ci.plan(root, 'b' * 40)['full'])

    def test_uses_successful_baseline_including_changes_from_failed_pushes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            family = root / 'collection/first-1880'
            family.mkdir(parents=True)
            (family / 'font.json').write_text('{}')
            with mock.patch.object(ci.subprocess, 'check_output', side_effect=[
                b'collection/first-1880/source/glyphs/A.json\0README.md\0', 'a' * 40]) as git:
                plan = ci.plan(root, 'b' * 40)
            self.assertEqual(git.call_args_list[0].args[0][-2:], ['b' * 40, 'HEAD'])
            self.assertEqual(plan['families'], ['first-1880'])
