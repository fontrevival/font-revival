"""Trace all observed forms, including named alternatives, with Potrace 1.16.

Run from any directory with --output PATH and optionally --potrace PATH.
The output is an importable CFF master plus disposable path audits.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sys

ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / 'scripts/trace_specimen.py').is_file())
sys.path.insert(0, str(ROOT / 'scripts'))
import trace_specimen as ts
from resample_crops import verify_crops


def prepare(family, output, potrace='potrace', cache=None):
    ts.require_potrace(potrace)
    verify_crops(family)
    manifest = json.loads((family / 'source/tracing.json').read_text())
    alternatives = json.loads((family / 'source/alternates.json').read_text())
    companions = json.loads((family / 'source/companions.json').read_text())
    assert not companions['aliases'], 'This source has no inferred aliases.'
    assert all('from' not in e for e in companions['glyphs'].values())
    tool_hash = hashlib.sha256(Path(__file__).read_bytes()
                              + Path(ts.__file__).read_bytes()
                              + (ROOT/'scripts/outline_geometry.py').read_bytes()
                              + (family/'source/resample_crops.py').read_bytes()).hexdigest()
    if cache:
        cache.mkdir(parents=True, exist_ok=True)
    hashes, drawings, extra = {}, {}, {}
    for entries, destination in [(manifest['glyphs'], drawings), (alternatives['glyphs'], extra)]:
        for name, entry in entries.items():
            file = family / entry['file']
            if file not in hashes:
                hashes[file] = hashlib.sha256(file.read_bytes()).hexdigest()
            signature = json.dumps([tool_hash, hashes[file], entry], sort_keys=True)
            cached = cache / (hashlib.sha256(signature.encode()).hexdigest()+'.json') if cache else None
            result = ts.prepare_entry((file, entry, [], signature, cached, potrace, name))
            assert not result['tones']
            destination[name] = result['solid']
    drawings.update(companions['glyphs'])
    features = (family / 'source/features.fea').read_text()
    ts.assemble(family, drawings, {}, output, features,
                manifest.get('font_metrics'), extra_drawings=extra)
    ts.fontrevival.write_json(output.with_suffix('.paths.json'), drawings)
    ts.fontrevival.write_json(output.with_suffix('.alternates.paths.json'), extra)
    print(f'Prepared {output}: {len(drawings)} encoded forms and {len(extra)} named alternatives.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--potrace', default='potrace')
    parser.add_argument('--cache', type=Path)
    args = parser.parse_args()
    prepare(Path(__file__).resolve().parent.parent, args.output, args.potrace, args.cache)
