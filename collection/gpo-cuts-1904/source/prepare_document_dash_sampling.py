"""Reproduce fourfold grayscale samples for the Document Room dashes.

Run with the repository's pinned Pillow environment. Sampling preserves each
complete native crop and adds no source detail. Paper correction and tracing
remain in source/tracing.json.
"""
from pathlib import Path
import json
from PIL import Image


def prepare(family):
    review = json.loads((family / 'source/document-dash-review.json').read_text())
    native = Image.open(family / review['native_file']).convert('L')
    for entry in review['entries']:
        crop = native.crop(entry['native_box'])
        factor = entry['sampling_factor']
        crop.resize((crop.width * factor, crop.height * factor),
                    Image.Resampling.BILINEAR).save(family / entry['recipe']['file'])


if __name__ == '__main__':
    prepare(Path(__file__).resolve().parents[1])
