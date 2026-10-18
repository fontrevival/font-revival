#!/usr/bin/env python3
"""Prepare Washington's documented source and weight revisions for review.

Requires requirements-tracing.txt and Potrace 1.16. Release builds consume the
committed glyph overrides and do not invoke this optional preparation script.
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FAMILY = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

import pathops
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.svgLib.path import parse_path
from PIL import Image

from outline_geometry import _path, _svg, boolean_op
from trace_specimen import glyph_name, require_potrace, trace


def bounds(svg):
    pen = BoundsPen(None)
    parse_path(svg, pen)
    return pen.bounds


def transform(svg, matrix):
    pen = SVGPathPen(None)
    parse_path(svg, TransformPen(pen, matrix))
    return pen.getCommands()


def refine(drawing, radius):
    result = drawing.copy()
    old = bounds(result['path'])
    silhouette = _path(result['path'])
    band = pathops.Path(silhouette)
    band.stroke(2 * radius, pathops.LineCap.BUTT_CAP, pathops.LineJoin.MITER_JOIN, 4)
    inset = boolean_op(silhouette, band, pathops.PathOp.DIFFERENCE)
    # Rounding offset intersections can leave a closed point or retraced line.
    # Discard only those zero-area contours, never counters or ink components.
    rounded = _path(_svg(inset))
    clean = pathops.Path()
    clean.fillType = rounded.fillType
    for contour in rounded.contours:
        if contour.area > 0.01:
            clean.addPath(contour)
    svg = _svg(clean)
    new = bounds(svg)
    sx = (old[2] - old[0]) / (new[2] - new[0])
    sy = (old[3] - old[1]) / (new[3] - new[1])
    result['path'] = transform(svg, (sx, 0, 0, sy, old[0] - new[0] * sx, old[1] - new[1] * sy))
    result['notes'] += (
        f' Display-weight refinement: inset the ink boundary by {radius} font units '
        'with mitered corners, then restore its measured bounds. This opens '
        'counters and reduces the smaller optical size’s stroke weight against '
        'the larger d/o/n reference; retain the historical construction.')
    return result


def prepare(output, potrace):
    if output.resolve().is_relative_to(FAMILY):
        raise ValueError('Write candidates outside the family; review before installing.')
    require_potrace(potrace)
    recipe = json.loads((FAMILY / 'source/tracing.json').read_text())
    settings = json.loads((FAMILY / 'source/weight-refinement.json').read_text())
    drawings, images = {}, {}
    for ch in settings['traced_characters']:
        entry = recipe['glyphs'][ch]
        if entry['file'] not in images:
            with Image.open(FAMILY / entry['file']) as image:
                images[entry['file']] = image.convert('L')
        drawings[ch] = trace(images[entry['file']], entry, potrace) | {
            'glyph': glyph_name(ch), 'notes': entry['notes']}
    raw_v = drawings['V'].copy()
    for ch, radius in settings['inset_radius'].items():
        drawings[ch] = refine(drawings[ch], radius)
    v = settings['v']
    source = refine(raw_v, v['source_inset_radius'])
    scale = v['scale']
    drawings['v'] = {
        'glyph': 'v', 'advance_width': v['advance_width'],
        'path': transform(source['path'], (scale, 0, 0, scale,
                          (v['advance_width'] - raw_v['advance_width'] * scale) / 2,
                          v['y_shift'])),
        'notes': 'Display-size reconstruction from the observed V at 72% scale, '
                 'with a separate 12-unit capital-scale weight correction to match '
                 'the lowercase. The small 1889 v establishes the fork and foot; '
                 'the larger y corroborates the flared right entry. Preserve the original advance.'}
    width = settings['q']['advance_width']
    drawings['q'] = {
        'glyph': 'q', 'advance_width': width,
        'path': transform(drawings['p']['path'], (-1, 0, 0, 1, width, 0)),
        'notes': 'Inferred q reflects the weight-refined 48-point p bowl and stem. '
                 'No q impression has been located; the reflected entry and exit terminals remain reconstructed.'}
    output.mkdir(parents=True, exist_ok=True)
    for drawing in drawings.values():
        (output / (drawing['glyph'] + '.json')).write_text(json.dumps(drawing, indent=2) + '\n')
    print(f'Prepared {len(drawings)} glyphs in {output}; review before installing.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--potrace', default='potrace')
    args = parser.parse_args()
    prepare(args.output, args.potrace)
