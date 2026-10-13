"""Select crops from explicitly transcribed, visually reviewed specimen rows.

Optional source-preparation tool; see requirements-display.txt.
A count mismatch is never assigned letters. Outputs always go to an explicit
working directory; review them before changing a family recipe.
"""
import argparse
import json
import string
from pathlib import Path
from statistics import median

import numpy as np
from scipy import ndimage
from PIL import Image, ImageDraw, ImageFont



def select(rows, name, reference_root, output):
    output.mkdir(parents=True, exist_ok=True)
    selected, candidates, errors = {}, [], []
    images = {}
    native_widths = {}
    rotations = {}
    for ri, row in enumerate(rows):
        file = row['file']
        if any(ch in string.ascii_lowercase for ch in row['text']) and not all(
                field in row for field in ('baseline', 'cap_height')):
            raise ValueError('Mixed-case rows need an explicit measured baseline and cap height.')
        if row.get('rotation', 0) not in (0, 90):
            raise ValueError('Row selection currently supports only 0 or 90 degree rotation.')
        if not row['text'] or len(row['box']) != 4:
            raise ValueError('Each row needs a nonempty transcription and a four-coordinate box.')
        if file in rotations and rotations[file] != row.get('rotation',0):
            raise ValueError('One source file must have one reading orientation per run.')
        rotations[file] = row.get('rotation',0)
        if file not in images:
            with Image.open(reference_root / file) as source:
                native_widths[file] = source.width
                im = source.convert('L')
            if row.get('rotation'):
                im = im.rotate(row['rotation'], expand=True)
            images[file] = im
        im = images[file]
        scale = im.width / row.get('preview_width', 1000)
        box = [round(v * scale) for v in row['box']]
        if not (0 <= box[0] < box[2] <= im.width and 0 <= box[1] < box[3] <= im.height):
            raise ValueError('Row rectangle is outside the oriented reference: ' + str(box))
        crop = im.crop(box)
        mask = np.asarray(crop) < row.get('threshold', 150)
        labels, count = ndimage.label(mask)
        areas = np.bincount(labels.ravel())
        keep = areas >= row.get('min_area', max(4, round(scale * scale * .35)))
        keep[0] = False
        mask = keep[labels]
        if row.get('components'):
            parts = ndimage.find_objects(labels)
            spans = sorted((s[1].start, s[1].stop) for i, s in enumerate(parts, 1)
                           if s and areas[i] >= row.get('letter_area', scale * scale * 10))
        else:
            active = mask.sum(axis=0) >= max(1, round(scale * .4))
            edges = np.diff(np.r_[False, active, False].astype(int))
            spans = list(zip(np.where(edges == 1)[0], np.where(edges == -1)[0]))
            spans = [(a, b) for a, b in spans if b - a >= scale * .45]
        span_keeps = [1] * len(spans)
        if row.get('merge_components'):
            if not row.get('components') or 'cuts' in row:
                raise ValueError('Component groups require component selection without cuts.')
            groups = row['merge_components']
            used = [index for group in groups for index in group]
            if (len(used) != len(set(used)) or any(not group for group in groups)
                    or any(index < 0 or index >= len(spans) for index in used)):
                raise ValueError('Component groups must contain distinct, valid component indices.')
            grouped = [(min(spans[i][0] for i in group),
                        max(spans[i][1] for i in group), len(group)) for group in groups]
            grouped += [(a, b, 1) for i, (a, b) in enumerate(spans) if i not in used]
            grouped.sort()
            spans = [(a, b) for a, b, _ in grouped]
            span_keeps = [n for _, _, n in grouped]
        if 'cuts' in row:
            edges = [round(v * scale) - box[0] for v in row['cuts']]
            spans = list(zip(edges, edges[1:]))
            span_keeps = [1] * len(spans)
        if len(spans) != len(row['text']):
            errors.append((ri, len(spans), len(row['text']), row['text']))
            debug = crop.convert('RGB')
            draw = ImageDraw.Draw(debug)
            for i, (a, b) in enumerate(spans):
                draw.rectangle((int(a), 0, int(b)-1, crop.height-1), outline='red', width=2)
                draw.text((int(a)+1, 1), str(i), fill='blue', font=ImageFont.load_default(size=16))
            debug.save(output / f'{name}-row-{ri}.png')
            continue
        local = []
        for ci, (ch, (a, b)) in enumerate(zip(row['text'], spans)):
            letter_mask = mask[:, a:b]
            if row.get('single_component', True) and (ch.isalnum() or ch in 'ÆŒ&$'):
                glyph_labels, glyph_count = ndimage.label(letter_mask)
                glyph_areas = np.bincount(glyph_labels.ravel()); glyph_areas[0] = 0
                # Connected italic sorts can overlap a neighbour's rectangular
                # crop. In component mode the single selected component is the
                # letter; neighbouring serif fragments must not set its bounds.
                glyph_keep = (np.isin(np.arange(len(glyph_areas)),
                                      np.argsort(glyph_areas)[-span_keeps[ci]:])
                              if row.get('components') else
                              glyph_areas >= max(4, glyph_areas.max() * .015))
                glyph_keep[0] = False
                letter_mask = glyph_keep[glyph_labels]
            ys, xs = np.where(letter_mask)
            bounds = [box[0]+int(a+xs.min()), box[1]+int(ys.min()),
                      box[0]+int(a+xs.max())+1, box[1]+int(ys.max())+1]
            local.append((ch, bounds, ci))
        heights = [b[3]-b[1] for ch,b,_ in local if ch in string.ascii_uppercase.replace('Q','') + string.digits]
        cap = row.get('cap_height', median(heights)/scale if heights else 1) * scale
        for ch, bounds, ci in local:
            if ch == '※':
                continue
            # Preserve Q's tail; the ordinary capitals/figures share a baseline.
            height = round((bounds[3]-bounds[1])*700/cap)
            if row.get('baseline') is not None:
                baseline = row['baseline'] * scale
                baseline += row.get('baseline_slope', 0) * ((bounds[0]+bounds[2])/2-box[0])
                bottom = round((baseline-bounds[3])*700/cap)
            elif ch == 'Q':
                nearby = sorted((abs((b[0]+b[2])-(bounds[0]+bounds[2])), b[3])
                                for c,b,_ in local if c in string.ascii_uppercase.replace('Q',''))[:4]
                bottom = round((median(b for _,b in nearby)-bounds[3])*700/cap)
            else:
                bottom = round((700-height)/2) if ch.isalnum() or ch in 'ÆŒ' else row.get('y_min', 0)
            padded = [bounds[0]-2, bounds[1]-2, bounds[2]+2, bounds[3]+2]
            if row.get('rotation') == 90:
                # Upright = native.rotate(90); x' = y, y' = width - x.
                native_width = native_widths[file]
                x0,y0,x1,y1 = padded
                padded = [native_width-y1, x0, native_width-y0, x1]
            e = dict(character=ch, row=ri, index=ci, file=file, box=padded,
                     rotation=row.get('rotation', 0), height=height, y_min=bottom,
                     bearings=row.get('bearings', [35,35]), blur=.45,
                     threshold=row.get('threshold',150), fill_holes=row.get('fill_holes',40),
                     component_min_area=row.get('component_min_area', max(4, round(scale*scale*.25))),
                     tolerance=.25,
                     notes=f'Observed impression; transcribed row {ri}, sort {ci}. Pixel measurements retained in source/rows.json.')
            if row.get('components'):
                del e['component_min_area']
                e['keep_components'] = span_keeps[ci]
            if row.get('measure_advances') and ci + 1 < len(local):
                e['advance_width'] = round((local[ci+1][1][0]-bounds[0])*700/cap)
                e['notes'] += ' Advance follows the next impression’s ink origin in this reviewed row.'
            candidates.append(e)
            if ch not in selected or ch in row.get('prefer_characters',''):
                selected[ch] = e
    for e in errors:
        print(name, 'MISMATCH', *e)
    print(name, 'observed', ''.join(sorted(selected)), 'missing', ''.join(c for c in string.ascii_uppercase+string.digits if c not in selected))
    (output / f'{name}-selected.json').write_text(json.dumps(selected, indent=2)+'\n')
    (output / f'{name}-candidates.json').write_text(json.dumps(candidates, indent=2)+'\n')
    out = Image.new('RGB',(1400, max(1, (len(selected)+9)//10)*180), '#f4f0e7')
    draw=ImageDraw.Draw(out)
    for i,(ch,e) in enumerate(sorted(selected.items())):
        im=images[e['file']]
        b=e['box']
        if e['rotation']==90:
            nw=native_widths[e['file']]
            b=[b[1],nw-b[2],b[3],nw-b[0]]
        im=im.crop(b)
        im.thumbnail((130,140));x=i%10*140;y=i//10*180
        out.paste(im,(x,y+30));draw.text((x+5,y+4),f'{ch} r{e["row"]}',fill='black',font=ImageFont.load_default(size=20))
    out.save(output/f'{name}-selected.jpg',quality=95)
    return not errors


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('family',type=Path,help='Family directory containing source/rows.json')
    parser.add_argument('--output',type=Path,required=True,help='Disposable review directory, outside the family')
    args=parser.parse_args()
    family=args.family.resolve()
    output=args.output.resolve()
    if output.is_relative_to(family):
        parser.error('Use a working output directory outside the family.')
    manifest=json.loads((family/'source/rows.json').read_text())
    if manifest.get('schema_version') != 1:
        parser.error('Unsupported row manifest schema.')
    good=select(manifest['rows'],family.name,family,output)
    raise SystemExit(0 if good else 1)
