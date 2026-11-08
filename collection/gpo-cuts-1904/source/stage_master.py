"""Stage the compact CFF master and its full-detail private tone overrides.

The preparation OTF contains complete encoded monochrome artwork and named
empty tone slots. Its companion .layers directory retains every fitted tonal
contour without constructing enormous unused CFF operand arrays in memory.
"""
import argparse
import importlib.util
import json
from pathlib import Path

from fontTools.ttLib import TTFont

FAMILY = Path(__file__).resolve().parent.parent
ROOT = FAMILY.parent.parent


def stage(source, output):
    metadata = json.loads((FAMILY / 'font.json').read_text())
    names = {layer['glyph'] for icon in metadata['icons']
             for layer in icon['multitone_layers']}
    layers = source.with_suffix('.layers')
    if {p.stem for p in layers.glob('*.json')} != names:
        raise ValueError('Prepared tone paths must match every named layer.')
    with TTFont(source, recalcTimestamp=False) as font:
        widths = {name: font['hmtx'][name][0] for name in names}
    for name in names:
        drawing = json.loads((layers / (name + '.json')).read_text())
        if not drawing['path'] or drawing['advance_width'] != widths[name]:
            raise ValueError('Invalid prepared tone path: ' + name)

    helper = ROOT / 'collection/baltimore-cuts-1832/source/stage_master.py'
    spec = importlib.util.spec_from_file_location('shared_stage_master', helper)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.stage(FAMILY, source, output)
    for name in sorted(names):
        drawing = json.loads((layers / (name + '.json')).read_text())
        item = {'glyph': name, **drawing, 'preserve_commands': True,
                'notes': 'Full native-resolution historical tracing, restored through the standard '
                         'glyph-edit mechanism over the compact CFF baseline. Private tone layers '
                         'have named empty baseline slots; encoded icons have complete outlines. '
                         'This full-detail drawing is authoritative for vector artwork.'}
        (FAMILY / 'source/glyphs' / (name + '.json')).write_text(
            json.dumps(item, ensure_ascii=False, indent=2) + '\n')
    print('Staged', len(names), 'complete private tone paths', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    stage(args.source, args.output)
