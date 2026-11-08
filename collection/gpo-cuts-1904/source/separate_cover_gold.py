"""Separate yellow gold from the retained burgundy binding scans.

This optional source-preparation step requires the family's pinned NumPy and
Pillow dependencies. It preserves the native pixel dimensions. The difference
between green and blue suppresses red leather and neutral glare; threshold tracing
then uses the resulting dark-on-white signal. No lines are reconstructed.
"""
from pathlib import Path
import numpy as np
from PIL import Image

FAMILY = Path(__file__).resolve().parent.parent

def separate(leaf):
    original = FAMILY / 'reference' / f'leaf-{leaf}.jp2'
    with Image.open(original) as image:
        rgb = np.asarray(image.convert('RGB'), dtype=np.int16)
    gold = np.clip(3 * (rgb[:, :, 1] - rgb[:, :, 2]), 0, 255)
    result = Image.fromarray(np.uint8(255 - gold), mode='L')
    output = FAMILY / 'reference' / f'leaf-{leaf}-gold.png'
    result.save(output)
    return output

if __name__ == '__main__':
    for leaf in [1, 208]:
        print(separate(leaf))
