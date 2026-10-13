"""Safeguards for optional historical row selection, without tracing fonts."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
AVAILABLE = all(importlib.util.find_spec(name) for name in ('numpy', 'scipy'))
if AVAILABLE:
    import select_display_rows as selection


@unittest.skipUnless(AVAILABLE, 'Optional display preparation dependencies are not installed')
class DisplayRowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.output = self.root / 'review'

    def run_selection(self, image, text, **kwargs):
        image.save(self.root / 'scan.png')
        row = dict(file='scan.png', preview_width=image.width,
                   box=[0, 0, image.width, image.height], text=text, **kwargs)
        with contextlib.redirect_stdout(io.StringIO()):
            good = selection.select([row], 'test', self.root, self.output)
        data = json.loads((self.output / 'test-selected.json').read_text())
        return good, data

    def test_count_mismatch_cannot_assign_letters(self):
        image = Image.new('L', (100, 80), 255)
        d = ImageDraw.Draw(image)
        d.rectangle((10, 10, 30, 65), fill=0)
        d.rectangle((50, 10, 70, 65), fill=0)
        good, selected = self.run_selection(image, 'ABC')
        self.assertFalse(good)
        self.assertEqual(selected, {})
        self.assertTrue((self.output / 'test-row-0.png').exists())

    def test_disconnected_halves_survive_glyph_bounds(self):
        image = Image.new('L', (100, 100), 255)
        d = ImageDraw.Draw(image)
        # Two large disconnected halves with overlapping x projections. The
        # largest-component-only approach incorrectly discarded half a capital.
        d.rectangle((20, 15, 75, 40), fill=0)
        d.rectangle((20, 50, 75, 80), fill=0)
        d.rectangle((45, 1, 46, 2), fill=0)  # Small unrelated paper mark.
        good, selected = self.run_selection(image, 'M')
        self.assertTrue(good)
        self.assertEqual(selected['M']['box'], [18, 13, 78, 83])

    def test_rotated_crop_maps_back_to_native_pixels(self):
        image = Image.new('L', (120, 80), 255)
        d = ImageDraw.Draw(image)
        d.rectangle((20, 15, 75, 60), fill=0)
        image.save(self.root / 'scan.png')
        row = dict(file='scan.png', rotation=90, preview_width=80,
                   box=[0, 0, 80, 120], text='A')
        with contextlib.redirect_stdout(io.StringIO()):
            good = selection.select([row], 'test', self.root, self.output)
        selected = json.loads((self.output / 'test-selected.json').read_text())
        self.assertTrue(good)
        self.assertEqual(selected['A']['box'], [18, 13, 78, 63])

    def test_component_rows_exclude_overlapping_neighbour_fragments(self):
        image = Image.new('L', (100, 90), 255)
        d = ImageDraw.Draw(image)
        d.polygon([(30, 10), (39, 10), (19, 70), (10, 70)], fill=0)
        d.polygon([(55, 10), (64, 10), (44, 70), (35, 70)], fill=0)
        good, selected = self.run_selection(image, 'AB', components=True,
                                           measure_advances=True)
        self.assertTrue(good)
        self.assertEqual(selected['A']['box'], [8, 8, 42, 73])
        self.assertEqual(selected['B']['box'], [33, 8, 67, 73])
        # Tracing these rectangles by area alone would include the adjacent
        # sloping stem at a corner. The recipe explicitly isolates one sort.
        self.assertEqual(selected['A']['keep_components'], 1)
        self.assertNotIn('component_min_area', selected['A'])
        self.assertEqual(selected['A']['advance_width'], round(25*700/61))
        self.assertNotIn('advance_width', selected['B'])

    def test_reviewed_groups_keep_a_letter_and_its_detached_mark(self):
        image = Image.new('L', (100, 90), 255)
        d = ImageDraw.Draw(image)
        d.rectangle((30, 10, 40, 19), fill=0)
        d.rectangle((30, 30, 40, 70), fill=0)
        good, selected = self.run_selection(image, 'i', components=True,
                                           merge_components=[[0, 1]], baseline=70,
                                           cap_height=60)
        self.assertTrue(good)
        self.assertEqual(selected['i']['box'], [28, 8, 43, 73])
        self.assertEqual(selected['i']['keep_components'], 2)


if __name__ == '__main__':
    unittest.main()
