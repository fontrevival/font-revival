"""Prepare conservative positive kern candidates; inspect in words before import.

Run after an initial TTF build. This only writes to a requested workspace file;
it never changes the canonical master. Pixel profiles use Pillow/FreeType at
200 px, with a 15-font-unit minimum gap, rounded to 5 font units. This fills in
unsafe pairs when the source's next-ink-origin advances meet a different letter.
"""
import argparse
from pathlib import Path
import string

import numpy as np
from PIL import ImageFont
from fontTools.ttLib import TTFont

family = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
args = parser.parse_args()
if args.output.resolve().is_relative_to(family):
    parser.error('Use a workspace output; review before copying into source/.')
font_path = family / 'fonts/BaltimoreBlackSlope1832-Regular.ttf'
font = ImageFont.truetype(str(font_path), 200)
profiles = {}
for character in string.ascii_letters + string.digits:
    mask, offset = font.getmask2(character, anchor='ls')
    pixels = np.asarray(mask).reshape((mask.size[1], mask.size[0]))
    profile = {}
    for y, row in enumerate(pixels):
        ink = np.where(row > 180)[0]
        if len(ink):
            profile[y + offset[1]] = (ink.min() + offset[0], ink.max() + offset[0])
    profiles[character] = profile
with TTFont(font_path) as source:
    cmap = source.getBestCmap()
lines = ['# New digital collision spacing; not historical kerning measurements.',
         'languagesystem DFLT dflt;', 'languagesystem latn dflt;', 'feature kern {']
for left in sorted(profiles):
    for right in sorted(profiles):
        shared = profiles[left].keys() & profiles[right].keys()
        needed = max((profiles[left][y][1] - profiles[right][y][0] + 3
                      for y in shared), default=0)
        adjustment = round((needed - font.getlength(left))) * 5
        if adjustment > 0:
            lines.append(f'  pos {cmap[ord(left)]} {cmap[ord(right)]} {adjustment};')
lines.append('} kern;')
args.output.write_text('\n'.join(lines) + '\n')
print(f'Prepared {len(lines)-5} positive kern candidates; inspect before import.')
