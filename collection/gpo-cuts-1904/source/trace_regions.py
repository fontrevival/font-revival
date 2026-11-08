"""Trace separately inked regions in one native monochrome mask.

Some ornaments combine faint hairlines with much darker dots. The measured
``mono_threshold_regions`` rectangles select a different threshold only for
the encoded monochrome drawing. Coordinates are half-open native crop pixels
after quarter-turn rotation, before the shared four-pixel tracing margin.
Tone layers and the common coordinate frame retain their own recipes.
"""
from PIL import Image
from fontTools.pens.roundingPen import RoundingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen


def region_mask(image, entry, clean):
    mask = clean(image, entry).copy()
    width, height = mask.width - 8, mask.height - 8
    for region in entry['mono_threshold_regions']:
        x0, y0, x1, y1 = region['box']
        threshold = region['threshold']
        if not (0 <= x0 < x1 <= width and 0 <= y0 < y1 <= height
                and 0 < threshold < 256):
            raise ValueError('Invalid monochrome threshold region: ' + str(region))
        rectangle = (x0 + 4, y0 + 4, x1 + 4, y1 + 4)
        try:
            local = clean(image, dict(entry, threshold=threshold))
        except ValueError as error:
            if not str(error).startswith(('No ink in crop:', 'No components survive')):
                raise
            local = Image.new('L', mask.size, 255)
        mask.paste(local.crop(rectangle), rectangle[:2])
    return mask


def trace_regions(image, entry, potrace, tracing):
    mask = region_mask(image, entry, tracing.clean_crop)
    record = tracing.trace_mask(mask, entry, potrace)
    frame = dict(entry, threshold=entry['frame_threshold'],
                 erase=entry.get('erase', []) + entry.get('multitone', {}).get('erase', []))
    reference = tracing.trace_mask(tracing.clean_crop(image, frame), frame, potrace)
    transform, advance = tracing.trace_transform(reference, entry)
    pen = SVGPathPen(None)
    record.replay(TransformPen(RoundingPen(pen), transform))
    return {'path': pen.getCommands(), 'advance_width': advance}
