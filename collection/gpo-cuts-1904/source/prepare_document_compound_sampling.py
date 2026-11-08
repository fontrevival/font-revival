"""Reproduce the native context samples for Document Division compound rules."""
from pathlib import Path
import json
from PIL import Image


def prepare(family):
    review = json.loads((family / 'source/document-compound-rule-review.json').read_text())
    native = Image.open(family / review['native_file']).convert('L')
    for entry in review['entries']:
        crop = native.crop(entry['context_box'])
        factor = entry['sampling_factor']
        crop.resize((crop.width * factor, crop.height * factor),
                    Image.Resampling.BILINEAR).save(family / entry['recipe']['file'])


if __name__ == '__main__':
    prepare(Path(__file__).resolve().parents[1])
