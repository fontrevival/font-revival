"""Reproduce border reading crops from retained native page pixels."""
import hashlib
import json
from pathlib import Path
from PIL import Image

FAMILY = Path(__file__).resolve().parents[1]


def prepare():
    records = json.loads((FAMILY / 'source/border-crops.json').read_text())['crops']
    for record in records:
        image = Image.open(FAMILY / record['source_file']).convert('L')
        turn = record['source_rotation_counterclockwise']
        if turn:
            image = image.rotate(turn, expand=True)
        if 'quadrilateral_native_ul_ur_lr_ll' in record:
            ul, ur, lr, ll = record['quadrilateral_native_ul_ur_lr_ll']
            quad = tuple(value for point in [ul, ll, lr, ur] for value in point)
            crop = image.transform(tuple(record['output_dimensions']), Image.Transform.QUAD,
                                   quad, resample=Image.Resampling.BICUBIC, fillcolor=255)
        else:
            crop = image.crop(record['box'])
        output = FAMILY / record['output']
        crop.save(output)
        if hashlib.sha256(output.read_bytes()).hexdigest() != record['sha256']:
            raise ValueError(f'Border crop differs from retained hash: {output}')
    print(f'Reproduced {len(records)} native border reading crops.')


if __name__ == '__main__':
    prepare()
