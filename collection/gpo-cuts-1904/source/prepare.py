"""Trace the GPO recipes with the shared exact accelerated mask preparation.

Optional preparation requires NumPy 1.26.4, SciPy 1.11.4 and Potrace 1.16.
Release builds use the committed canonical master, without retracing.
"""
import importlib.util
import json
import sys
from pathlib import Path

if __name__ == '__main__':
    shared = Path(__file__).resolve().parents[2] / 'baltimore-cuts-1832/source/prepare.py'
    spec = importlib.util.spec_from_file_location('gpo_shared_prepare', shared)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    from trace_regions import trace_regions
    trace = module.tracing.trace

    def trace_monochrome(image, entry, potrace):
        if entry.get('mono_threshold_regions'):
            return trace_regions(image, entry, potrace, module.tracing)
        return trace(image, entry, potrace)

    module.tracing.trace = trace_monochrome
    assemble = module.tracing.assemble

    def assemble_direct(family, drawings, aliases, output, features, settings, extra):
        # Dense engravings do not need the expensive optional CFF operator optimizer.
        # Keep the fitted contours and coordinates exactly as prepared.
        for drawing in [*drawings.values(), *extra.values()]:
            drawing['preserve_commands'] = True
        # Private tonal contours are delivered as SVG, not encoded characters.
        # Keep them as individual paths rather than materializing their enormous
        # CFF operand arrays together. stage_master.py restores these exact paths
        # as ordinary glyph overrides over named empty slots in the baseline.
        layers = output.with_suffix('.layers')
        layers.mkdir(parents=True, exist_ok=True)
        for name, drawing in extra.items():
            (layers / (name + '.json')).write_text(json.dumps(drawing, indent=2) + '\n')
        slots = {name: {'path': '', 'advance_width': drawing['advance_width']}
                 for name, drawing in extra.items()}
        print('Assembling', len(drawings), 'encoded drawings;', len(extra),
              'full-detail tone paths retained in', layers, flush=True)
        return assemble(family, drawings, aliases, output, features, settings, slots)

    module.tracing.assemble = assemble_direct
    module.tracing.main()
