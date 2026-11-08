"""Recreate the fourfold grayscale sample from the retained native page."""
from pathlib import Path
from PIL import Image

def prepare(family=None):
    family=Path(family) if family else Path(__file__).resolve().parents[1]
    page=Image.open(family/'reference/gpo-document-1904-leaf-85.png').convert('L')
    crop=page.crop((1205,3192,1418,3385))
    crop.resize((crop.width*4,crop.height*4),Image.Resampling.BILINEAR).save(family/'reference/document-wreath-sampling-4.png')

if __name__=='__main__':
    prepare()
