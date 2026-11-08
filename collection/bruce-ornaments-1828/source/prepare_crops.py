"""Reproduce the retained reading crops from the native full-page images.

Run this optional preparation script before trace_specimen.py. Normal font builds
use font.ttx and require neither image processing nor Potrace.
"""
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageDraw

FAMILY = Path(__file__).resolve().parents[1]


def prepare():
    records = json.loads((FAMILY / "source/crops.json").read_text())["crops"]
    for record in records:
        image = Image.open(FAMILY / record["source_file"]).convert("L")
        turn = record["source_rotation_counterclockwise"]
        if turn:
            image = image.rotate(turn, expand=True)
        crop = image.crop(record["box"])
        draw = ImageDraw.Draw(crop)
        for rectangle in record["erase_before_rotation"]:
            draw.rectangle(rectangle, fill=255)
        angle = record["deskew_counterclockwise_degrees"]
        if angle:
            crop = crop.rotate(angle, resample=Image.Resampling.BICUBIC,
                               expand=True, fillcolor=255)
        output = FAMILY / record["output"]
        output.parent.mkdir(parents=True, exist_ok=True)
        crop.save(output)
        if hashlib.sha256(output.read_bytes()).hexdigest() != record["sha256"]:
            raise ValueError(f"Reading crop differs from its retained hash: {output}")
    print(f"Reproduced {len(records)} native reading crops.")


if __name__ == "__main__":
    prepare()
