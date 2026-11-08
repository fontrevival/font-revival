"""Recreate documented fitting crops; interpolation adds no scan detail."""
from pathlib import Path
import json
from PIL import Image
FAMILY = Path(__file__).resolve().parent.parent
if __name__ == "__main__":
    review = json.loads((FAMILY / "source/leader-review.json").read_text())
    for entry in review["entries"]:
        with Image.open(FAMILY / entry["native_file"]) as image:
            crop = image.convert("L").crop(entry["context_box"])
            factor = entry["sampling"]["factor"]
            crop.resize((crop.width * factor, crop.height * factor), Image.Resampling.BILINEAR).save(FAMILY / entry["working_file"])
