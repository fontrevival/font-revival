"""Recreate the bilinear grayscale working crop used for the fine waved rule.

The exact native JP2 and its lossless PNG remain the historical evidence.
Interpolation permits subpixel fitting and does not recover additional detail.
Run before source/prepare.py when reproducing the original tracing.
"""
from pathlib import Path
from PIL import Image
FAMILY = Path(__file__).resolve().parent.parent
if __name__ == '__main__':
    with Image.open(FAMILY / 'reference/leaf-32.png') as image:
        crop = image.convert('L').crop((704, 2896, 765, 2916))
        crop.resize((488, 160), Image.Resampling.BILINEAR).save(
            FAMILY / 'reference/waved-rule-sampling-8.png')
