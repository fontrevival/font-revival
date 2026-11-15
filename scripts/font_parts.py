"""Full-detail icon outlines decomposed by default OpenType shaping.

The editable master stays intact. Reviewed clipping pieces are added only to
delivery fonts; one encoded icon expands to registered, overlapping pieces.
"""
import hashlib
import json

from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.svgLib.path import parse_path


def outline_limits(path):
    pen = TTGlyphPen(None)
    parse_path(path, Cu2QuPen(pen, .5, reverse_direction=True))
    glyph = pen.glyph()
    rec = RecordingPen()
    parse_path(path, rec)
    # Conservative cubic count includes repeated closing endpoints.
    cubic = sum(len(points) for op, points in rec.value
                if op in ('moveTo', 'lineTo', 'curveTo'))
    return len(glyph.coordinates), cubic, glyph.numberOfContours


def load_parts(family, font):
    manifest = family / 'source/font-parts.json'
    if not manifest.exists():
        return {}
    data = json.loads(manifest.read_text())
    if data.get('schema_version') != 1 or data.get('feature') != 'ccmp':
        raise ValueError('Unsupported font decomposition manifest.')
    glyphs = font.getGlyphSet()
    encoded = set(font.getBestCmap().values())
    result, used = {}, set(font.getGlyphOrder())
    for name, entry in data['glyphs'].items():
        if name not in encoded or not entry.get('notes'):
            raise ValueError(f'{name}: invalid decomposed icon.')
        path = SVGPathPen(glyphs)
        glyphs[name].draw(path)
        fingerprint = hashlib.sha256(path.getCommands().encode()).hexdigest()
        advance = font['hmtx'][name][0]
        if entry.get('master_sha256') != fingerprint:
            raise ValueError(f'{name}: stale font decomposition.')
        if entry.get('advance_width') != advance or len(entry['parts']) < 2:
            raise ValueError(f'{name}: invalid decomposition spacing or part count.')
        parts = []
        for index, ref in enumerate(entry['parts']):
            file = family / ref['file']
            if not file.resolve().is_relative_to((family / 'source/font-parts').resolve()):
                raise ValueError('Font part must be inside source/font-parts.')
            part = json.loads(file.read_text())
            private = ref['glyph']
            if (part.get('glyph') != private or private in used
                    or not private.startswith(name + '.part')):
                raise ValueError(f'{name}: invalid or repeated part name.')
            expected = advance if index == len(entry['parts']) - 1 else 0
            if part.get('advance_width') != expected or not part.get('path'):
                raise ValueError(f'{private}: invalid registered spacing or empty outline.')
            quadratic, cubic, contours = outline_limits(part['path'])
            if quadratic > 32763 or cubic > 32767 or contours >= 4095:
                raise ValueError(f'{private}: part exceeds renderer limits.')
            used.add(private)
            parts.append(part)
        result[name] = parts
    return result


def add_parts(font, parts):
    """Add private pieces and default substitutions to a delivery CFF font."""
    if not parts:
        return
    if 'GSUB' in font:
        raise ValueError('Icon decomposition requires a font without existing GSUB rules.')
    top = font['CFF '].cff.topDictIndex[0]
    order = font.getGlyphOrder()[:]
    rules = ['languagesystem DFLT dflt;', 'languagesystem latn dflt;', 'feature ccmp {']
    for name, drawings in sorted(parts.items()):
        names = []
        for drawing in drawings:
            private, width = drawing['glyph'], drawing['advance_width']
            pen = T2CharStringPen(width, None, roundTolerance=0)
            parse_path(drawing['path'], pen)
            charstring = pen.getCharString(private=top.Private, globalSubrs=top.GlobalSubrs,
                                          optimize=False)
            if top.CharStrings.charStringsAreIndexed:
                top.CharStrings.charStrings[private] = len(top.CharStrings.charStringsIndex)
                top.CharStrings.charStringsIndex.append(charstring)
            else:
                top.CharStrings.charStrings[private] = charstring
            bounds = BoundsPen(None)
            parse_path(drawing['path'], bounds)
            font['hmtx'][private] = (width, round(bounds.bounds[0]))
            order.append(private)
            names.append(private)
        rules.append('sub ' + name + ' by ' + ' '.join(names) + ';')
    font.setGlyphOrder(order)
    top.charset = order[:]
    rules.append('} ccmp;')
    addOpenTypeFeaturesFromString(font, '\n'.join(rules))


def substitution_parts(font):
    """Return only default ccmp multiple substitutions, for proofs and checks."""
    if 'GSUB' not in font:
        return {}
    table = font['GSUB'].table
    indices = {index for feature in table.FeatureList.FeatureRecord
               if feature.FeatureTag == 'ccmp' for index in feature.Feature.LookupListIndex}
    result = {}
    for index in sorted(indices):
        lookup = table.LookupList.Lookup[index]
        if lookup.LookupType == 2:
            for subtable in lookup.SubTable:
                result.update({name: list(parts) for name, parts in subtable.mapping.items()})
    return result


def validate_parts(font, expected):
    actual = substitution_parts(font)
    for name, parts in expected.items():
        names = [part['glyph'] for part in parts]
        if actual.get(name) != names:
            raise ValueError(f'{name}: missing or changed default decomposition.')
        if sum(font['hmtx'][private][0] for private in names) != font['hmtx'][name][0]:
            raise ValueError(f'{name}: decomposition changes text advance.')
        glyphs = font.getGlyphSet()
        for private in names:
            pen = SVGPathPen(glyphs)
            glyphs[private].draw(pen)
            quadratic, cubic, contours = outline_limits(pen.getCommands())
            if (('glyf' in font and quadratic > 32763)
                    or ('CFF ' in font and cubic > 32767) or contours >= 4095):
                raise ValueError(f'{private}: delivered piece exceeds renderer limits.')
