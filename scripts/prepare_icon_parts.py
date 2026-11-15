"""Prepare full-detail icon pieces without flattening their fitted curves.

Authoring step: inspect the generated font proofs before accepting these pieces.
Builds read the saved JSON paths and never repeat the clipping operation.
"""
import argparse
import hashlib
import json
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.svgLib.path import parse_path

import fontrevival as fr
from font_parts import outline_limits
from outline_partition import contours, clip


def compact_coordinates(svg):
    pen = SVGPathPen(None, ntos=lambda v: format(round(v * 64) / 64, '.6f').rstrip('0').rstrip('.')
                     if round(v * 64) else '0')
    parse_path(svg, pen)
    return pen.getCommands()


def prepare(family, names, overlap=4):
    m = fr.metadata(family)
    if m.get('kind') != 'icons' or m.get('font_export_glyphs') != 'encoded':
        raise ValueError('Decomposition is for encoded-only icon delivery fonts.')
    font = fr.load_source(family, m, encoded_only=True)
    glyphs = font.getGlyphSet()
    manifest = family / 'source/font-parts.json'
    data = json.loads(manifest.read_text()) if manifest.exists() else {
        'schema_version': 1, 'feature': 'ccmp', 'glyphs': {}}
    folder = family / 'source/font-parts'
    folder.mkdir(exist_ok=True)
    for name in names:
        if name not in font.getBestCmap().values():
            raise ValueError('Select an encoded icon glyph.')
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        original = pen.getCommands()
        fingerprint = hashlib.sha256(original.encode()).hexdigest()
        if data['glyphs'].get(name, {}).get('master_sha256') == fingerprint:
            print('Retained', name, flush=True)
            continue
        source, pieces = contours(original), []
        advance = font['hmtx'][name][0]

        def divide(box, depth=0):
            x0, y0, x1, y1 = box
            drawing = compact_coordinates(clip(source, (x0-overlap, y0-overlap,
                                                         x1+overlap, y1+overlap)))
            quadratic, cubic, count = outline_limits(drawing)
            if not quadratic:
                return
            if max(quadratic, cubic) <= 30000 and count < 4000:
                pieces.append({'path': drawing, 'clip_box': list(box),
                               'quadratic_points': quadratic, 'cubic_points': cubic})
                return
            if depth >= 10:
                raise ValueError(f'{name}: clipping cannot meet renderer limits.')
            if x1-x0 >= y1-y0:
                mid = (x0+x1)/2
                divide((x0, y0, mid, y1), depth+1)
                divide((mid, y0, x1, y1), depth+1)
            else:
                mid = (y0+y1)/2
                divide((x0, y0, x1, mid), depth+1)
                divide((x0, mid, x1, y1), depth+1)

        divide((0, font['hhea'].descent, advance, font['hhea'].ascent))
        if len(pieces) < 2:
            print('Fits one renderer glyph; no decomposition:', name, flush=True)
            continue
        refs = []
        for index, piece in enumerate(pieces):
            private = f'{name}.part{index+1:02}'
            piece.update(glyph=private, advance_width=advance if index == len(pieces)-1 else 0,
                         notes='Exact cubic subdivision and rectangular clipping; 1/64-unit storage. '
                               'Overlapping boundaries avoid antialias seams; complete union retains the original ink.')
            file = folder / (private + '.json')
            fr.write_json(file, piece)
            refs.append({'glyph': private, 'file': file.relative_to(family).as_posix()})
        data['glyphs'][name] = {'master_sha256': fingerprint, 'advance_width': advance,
                               'overlap_font_units': overlap, 'parts': refs,
                               'notes': 'Default OpenType ccmp expands this icon into registered outline pieces. '
                                        'Only the final piece advances; the encoded character and total spacing remain unchanged. '
                                        'The base outline is a compatibility fallback for software without shaping.'}
        fr.write_json(manifest, data)
        print('Prepared', name, len(pieces), 'pieces; visual review required', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('family')
    parser.add_argument('--glyph', nargs='+', required=True)
    args = parser.parse_args()
    prepare(fr.family_dir(args.family), args.glyph)
