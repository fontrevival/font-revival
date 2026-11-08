"""Reproduce native reading crops from retained historical pages."""
from pathlib import Path
import json,hashlib
from PIL import Image
root=Path(__file__).resolve().parents[1]
records=json.loads((root/'source/crops.json').read_text())['crops']
for record in records:
 im=Image.open(root/record['source_file']).convert('L')
 turn=record['source_rotation_counterclockwise']
 if turn:im=im.rotate(turn,expand=True)
 crop=im.crop(record['box'])
 angle=record.get('deskew_counterclockwise_degrees',0)
 if angle:crop=crop.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True,fillcolor=255)
 target=root/record['output'];crop.save(target)
 assert hashlib.sha256(target.read_bytes()).hexdigest()==record['sha256'],record['id']
print(f'Reproduced {len(records)} native reading crops with identical hashes.')
