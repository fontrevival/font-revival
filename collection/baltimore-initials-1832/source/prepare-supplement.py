"""Retrace supplementary period impressions and append/replace their stable sorts.

Original Baltimore glyphs and tone layers are retained from the canonical master.
Normal release builds use font.ttx and do not run this optional Potrace tool.
"""
import argparse
import json
import sys
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.svgLib.path import parse_path
from fontTools.ttLib import TTFont

FAMILY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FAMILY.parents[1] / 'scripts'))
import fontrevival as fr
import trace_specimen as tr


def prepare(output, potrace):
    tr.require_potrace(potrace)
    recipe = json.loads((FAMILY / 'source/supplemental-tracing.json').read_text())
    font = TTFont(recalcTimestamp=False)
    font.importXML(FAMILY / 'source/font.ttx')
    top = font['CFF '].cff.topDictIndex[0]
    order = font.getGlyphOrder()
    drawings = {}
    for ch, entry in recipe['glyphs'].items():
        drawing = tr.prepare_entry((FAMILY / entry['file'], entry, [], '', None, potrace, f'U+{ord(ch):04X}'))['solid']
        name = f'uni{ord(ch):04X}'
        pen = T2CharStringPen(drawing['advance_width'], None)
        parse_path(drawing['path'], pen)
        top.CharStrings[name] = pen.getCharString(private=top.Private, globalSubrs=top.GlobalSubrs)
        if name not in order:
            order.append(name)
        bounds = BoundsPen(None)
        parse_path(drawing['path'], bounds)
        font['hmtx'][name] = drawing['advance_width'], round(bounds.bounds[0])
        for table in font['cmap'].tables:
            if table.isUnicode():
                table.cmap[ord(ch)] = name
        drawings[ch] = drawing
    top.charset = order
    font.setGlyphOrder(order)
    font['maxp'].numGlyphs = len(order)
    fr.normalize(font, fr.metadata(FAMILY))
    output.parent.mkdir(parents=True, exist_ok=True)
    font.save(output)
    fr.write_json(output.with_suffix('.paths.json'), drawings)
    print(f'Prepared {len(drawings)} supplementary impressions in {output}.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--potrace', default='potrace')
    args = parser.parse_args()
    prepare(args.output, args.potrace)
