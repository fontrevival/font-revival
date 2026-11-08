"""Recreate the two documented corner fitting crops from the native page."""
from pathlib import Path
import json
from PIL import Image, ImageDraw
FAMILY = Path(__file__).resolve().parent.parent
if __name__ == "__main__":
    review = json.loads((FAMILY / "source/corner-review.json").read_text())
    for entry in review["entries"]:
        with Image.open(FAMILY / entry["native_file"]) as image:
            box = entry["native_box"]
            crop = image.convert("L").crop(box)
            draw = ImageDraw.Draw(crop)
            for x0, y0, x1, y1 in entry["native_neighbor_erases"] + entry["native_paper_erases"]:
                draw.rectangle([x0-box[0], y0-box[1], x1-box[0], y1-box[1]], fill=255)
            factor = entry["sampling"]["factor"]
            crop.resize((crop.width*factor, crop.height*factor), Image.Resampling.BILINEAR).save(FAMILY / entry["working_file"])
