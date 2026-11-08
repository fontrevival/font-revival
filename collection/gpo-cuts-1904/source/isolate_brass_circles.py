"""Reproduce native circle crops while excluding labels and neighbouring rings.

The radial intervals are broad masks in blank paper, not replacement outlines.
All surviving pixels come unchanged from the retained native grayscale scan.
"""
import json
from pathlib import Path

import numpy as np
from PIL import Image

FAMILY = Path(__file__).resolve().parents[1]


def isolate(record, source):
    box = record['box']
    pixels = np.array(source.crop(box))
    yy, xx = np.indices(pixels.shape)
    cx, cy = record['mask']['native_centre']
    radius = np.hypot(xx + box[0] - cx, yy + box[1] - cy)
    low, high = record['mask']['radial_interval']
    pixels[(radius < low) | (radius > high)] = 255
    for field in ['native_caption_erases', 'native_paper_erases']:
        for x0, y0, x1, y1 in record['mask'][field]:
            pixels[max(0, y0-box[1]):max(0, y1-box[1]),
                   max(0, x0-box[0]):max(0, x1-box[0])] = 255
    return Image.fromarray(pixels)


def main():
    records = json.loads((FAMILY/'source/brass-circle-isolation.json').read_text())
    source = Image.open(FAMILY/records['source_file']).convert('L')
    for record in records['circles']:
        output = FAMILY/record['derived_file']
        output.parent.mkdir(parents=True, exist_ok=True)
        isolate(record, source).save(output)
    print(f"Reproduced {len(records['circles'])} native circle crops.")


if __name__ == '__main__':
    main()
