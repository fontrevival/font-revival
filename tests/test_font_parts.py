"""Keep dense icon decomposition faithful, registered and bound to its source."""
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest

from fontTools.fontBuilder import FontBuilder
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.svgLib.path import parse_path
from fontTools.ttLib import TTFont
from PIL import Image, ImageChops, ImageDraw, ImageFont, features

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from font_parts import add_parts, load_parts, substitution_parts, validate_parts
from fontrevival import to_truetype
from outline_partition import contours, clip
from outline_raster import rasterize


DRAWING = ('M100 100C0 400 100 800 450 900C800 800 900 400 800 100Z '
           'M300 300L600 300L600 650L300 650Z')


def fixture_font():
    fb = FontBuilder(1000, isTTF=False)
    order = ['.notdef', 'space', 'uniE000']
    fb.setupGlyphOrder(order)
    fb.setupCharacterMap({32: 'space', 0xE000: 'uniE000'})
    drawings = {}
    for name in order:
        pen = T2CharStringPen(950, None)
        if name == 'uniE000':
            parse_path(DRAWING, pen)
        drawings[name] = pen.getCharString()
    fb.setupCFF('PartsTest', {'FullName': 'Parts Test', 'FamilyName': 'Parts Test',
                            'Weight': 'Regular'}, drawings, {})
    fb.setupHorizontalMetrics({name: (950, 0) for name in order})
    fb.setupHorizontalHeader(ascent=1000, descent=0)
    fb.setupNameTable({'familyName': 'Parts Test', 'styleName': 'Regular',
                      'psName': 'PartsTest', 'fullName': 'Parts Test'})
    fb.setupOS2(sTypoAscender=1000, sTypoDescender=0, usWinAscent=1000, usWinDescent=0)
    fb.setupPost()
    return fb.font


class FontPartsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.family = Path(self.temp.name)
        folder = self.family / 'source/font-parts'
        folder.mkdir(parents=True)
        self.font = fixture_font()
        pen = SVGPathPen(self.font.getGlyphSet())
        self.font.getGlyphSet()['uniE000'].draw(pen)
        original = pen.getCommands()
        refs = []
        for index, box in enumerate([(0, 0, 479, 1000), (471, 0, 950, 1000)]):
            name = f'uniE000.part{index+1:02}'
            file = folder / (name + '.json')
            file.write_text(json.dumps({'glyph': name, 'advance_width': 950 if index else 0,
                                        'path': clip(contours(original), box)}))
            refs.append({'glyph': name, 'file': file.relative_to(self.family).as_posix()})
        manifest = {'schema_version': 1, 'feature': 'ccmp', 'glyphs': {'uniE000': {
            'master_sha256': hashlib.sha256(original.encode()).hexdigest(),
            'advance_width': 950, 'parts': refs, 'notes': 'Source-bound test pieces.'}}}
        (self.family / 'source/font-parts.json').write_text(json.dumps(manifest))

    def tearDown(self):
        self.temp.cleanup()

    def test_clipping_preserves_curves_and_winding_through_a_hole(self):
        parts = load_parts(self.family, self.font)['uniE000']
        # Render their combined winding once: the overlapping clip boundaries
        # cancel inside the original hole rather than filling it.
        expected = rasterize(DRAWING, 1000, 1000, 1, (0, 1000))
        actual = rasterize(' '.join(p['path'] for p in parts), 1000, 1000, 1, (0, 1000))
        difference = ImageChops.difference(expected, actual)
        # Cairo's flattening changes subpixel coverage at newly subdivided
        # curves; no fully inked pixel may turn into paper or vice versa.
        self.assertFalse(any(abs(a-b) == 255 for a, b in zip(expected.tobytes(), actual.tobytes())))
        self.assertLess(sum(difference.tobytes()), sum(expected.tobytes()) * .0001)
        self.assertEqual(actual.getpixel((450, 500)), 0)
        self.assertIn('C', parts[0]['path'])

    def test_parts_round_trip_and_default_shaping_retains_direction_and_advance(self):
        parts = load_parts(self.family, self.font)
        add_parts(self.font, parts)
        self.assertEqual(substitution_parts(self.font)['uniE000'],
                         ['uniE000.part01', 'uniE000.part02'])
        for font in [self.font, to_truetype(self.font, preserve_origins=True)]:
            stream = io.BytesIO()
            font.save(stream)
            stream.seek(0)
            with TTFont(stream) as restored:
                validate_parts(restored, parts)
        if not features.check('raqm'):
            self.skipTest('Pillow needs RAQM to test default OpenType shaping.')
        stream.seek(0)
        face = ImageFont.truetype(stream, 500, layout_engine=ImageFont.Layout.RAQM)
        images = []
        for direction in ['ltr', 'rtl']:
            self.assertEqual(face.getlength('\ue000', direction=direction), 475)
            image = Image.new('L', (600, 600))
            ImageDraw.Draw(image).text((20, 550), '\ue000', font=face, anchor='ls',
                                       direction=direction, fill=255)
            images.append(image)
        self.assertIsNone(ImageChops.difference(*images).getbbox())
        self.assertEqual(images[0].getpixel((245, 300)), 0)

    def test_source_changes_and_unregistered_part_advances_are_rejected(self):
        file = self.family / 'source/font-parts/uniE000.part01.json'
        part = json.loads(file.read_text())
        part['advance_width'] = 950
        file.write_text(json.dumps(part))
        with self.assertRaisesRegex(ValueError, 'registered spacing'):
            load_parts(self.family, self.font)
        part['advance_width'] = 0
        file.write_text(json.dumps(part))
        manifest = self.family / 'source/font-parts.json'
        data = json.loads(manifest.read_text())
        data['glyphs']['uniE000']['master_sha256'] = 'old-source'
        manifest.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'stale font decomposition'):
            load_parts(self.family, self.font)


if __name__ == '__main__':
    unittest.main()
