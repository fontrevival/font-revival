"""Verify or regenerate the recorded four-times source crops from native JP2s."""
from pathlib import Path
import argparse
import hashlib
import json
from PIL import Image


def verify_crops(family, regenerate=False):
    manifest=json.loads((family/'reference/crops.json').read_text())
    acquisition=json.loads((family/'reference/acquisition.json').read_text())
    native_hashes={e['file']:e['sha256'] for e in acquisition}
    sources={}
    records=manifest['crops']
    assert len({e['file'] for e in records})==len(records)
    for e in records:
        native=e['native_file']
        if native not in sources:
            path=family/native
            assert hashlib.sha256(path.read_bytes()).hexdigest()==native_hashes[native],native
            sources[native]=Image.open(path).convert('RGB')
        assert e['sampling_scale']==4 and e['resampling']=='Pillow LANCZOS'
        image=sources[native]
        rotation=e.get('native_rotation_clockwise',0)
        assert rotation in (0,90,180,270)
        if rotation:image=image.transpose({90:Image.Transpose.ROTATE_270,180:Image.Transpose.ROTATE_180,270:Image.Transpose.ROTATE_90}[rotation])
        crop=image.crop(e['native_box'])
        crop=crop.resize((crop.width*4,crop.height*4),Image.Resampling.LANCZOS)
        assert crop.mode==e['mode'] and list(crop.size)==e['size'],e['id']
        assert hashlib.sha256(crop.tobytes()).hexdigest()==e['pixel_sha256'],e['id']
        path=family/e['file']
        if regenerate:
            path.parent.mkdir(parents=True,exist_ok=True)
            crop.save(path)
        assert hashlib.sha256(path.read_bytes()).hexdigest()==e['file_sha256'],e['id']
        retained=Image.open(path)
        assert retained.mode==crop.mode and retained.size==crop.size,e['id']
        assert retained.tobytes()==crop.tobytes(),e['id']
    return dict(native_sources=len(sources),derived_crops=len(records),exact_pixels=True,exact_files=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--regenerate',action='store_true')
    args=parser.parse_args()
    print(json.dumps(verify_crops(Path(__file__).resolve().parent.parent,args.regenerate),indent=2))
