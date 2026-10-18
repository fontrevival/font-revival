# Repeatable specimen tracing

`scripts/trace_specimen.py` converts documented crops of historical specimens
into a static OpenType/CFF font. It reads local reference images and writes an
OTF plus a `.paths.json` file for inspecting the traced outlines. Import the
reviewed OTF as `source/font.ttx`, the editable master used by release builds.

## Requirements

Use Python 3.12, the pinned `requirements.txt`, and **Potrace 1.16**. The reference
Linux tool packages are Ubuntu 24.04 `potrace=1.16-2build1` and
`libpotrace0=1.16-2build1`. Potrace is required for tracing; release builds and
checks use the committed master without retracing. The script checks the
Potrace version. Use `--potrace /path/to/potrace` to select an installation.

## Prepare a master

Prepare the font in `workspace/`, inspect the OTF and its adjacent `.paths.json`,
then import it and build the release formats:

```sh
python scripts/trace_specimen.py trinal-1888 --output workspace/Trinal1888-Regular.otf
python scripts/fontrevival.py import trinal-1888 workspace/Trinal1888-Regular.otf
python scripts/fontrevival.py build trinal-1888
```

To replace a family's master, use `import --replace`. This replaces the outlines
and OpenType features in `source/font.ttx`; the build applies `source/glyphs/`
overrides to the imported master. Review those overrides when replacing it.
Edits to the TTX master do not update the tracing recipe.

## Recipe files

Each family prepared with the tracer keeps:

- `source/tracing.json`: exact reference filenames and crop boxes `[left, top,
  right, bottom]` in original image pixels, with y down and right/bottom exclusive.
  It records target outline height, baseline offset, sidebearings and any cleanup
  settings. Read `source/METHOD.md` before changing them.
  An optional `rotation` is an exact counterclockwise quarter turn (0, 90, 180
  or 270 degrees), applied after cropping and before cleanup. Erasure rectangles
  use coordinates in that rotated crop. Historical comparison proofs show the
  same upright orientation without applying the tracing cleanup to the scan.
- `source/companions.json`: explicit SVG paths in font units with y up, or
  transforms referencing a traced character or preceding companion. These supply
  companion characters and documented repairs. An entry for a traced character
  replaces that trace.
- `source/features.fea`: optional OpenType features for the prepared master.
- `reference/`: exact local scans plus acquisition and rights evidence.

## Crop cleanup and outline fitting

The tracer caches each decoded image, works on small crops, blurs by 0.55 pixels,
thresholds at 135, retains the largest connected ink component, and fills enclosed
white specks of at most eight pixels. Per-glyph settings override these defaults.
For detached dots and ornaments, set `keep_components` to retain the largest N
components, or `component_min_area` to retain all components above a pixel-area
threshold. Inspect the result: pale hairlines may require a higher `threshold`
and less `blur`. `ink_erosion` shrinks ink by an integer pixel radius before
component selection; use it only to compensate for documented impression spread.

Potrace fits cubic outlines with `alphamax=1`, `opttolerance=0.35`, `turdsize=0`
and `unit=10`. The script reads its y-up paths, scales uniformly to the documented
height, moves them to the recorded baseline and sidebearing, and rounds to font
units. Draw missing characters explicitly and identify them as reconstructions
in `font.json`, following the [source policy](SOURCES.md).

An entry may set `advance_width` and `center` for a fixed-width cell. The recipe's
`font_metrics` can set `cap_height`, `x_height`, `win_ascent`, `win_descent` and
`monospaced`; fixed-pitch masters must give every drawing the same advance,
including spaces and punctuation.
The assembler carries fixed-pitch metadata into CFF and TrueType outputs.
`ink_width` sets an explicit horizontal outline extent and takes precedence over
`width_scale`.

## Reviewing display rows

For a manually transcribed display specimen, the optional row selector records
candidate crops and a contact sheet before tracing:

```sh
python -m pip install -r requirements-display.txt
python scripts/select_display_rows.py collection/baltimore-bold-1832 \
  --output workspace/baltimore-bold-row-review
```

The family's `source/rows.json` records each reference file, reading rotation,
preview width, row rectangle and exact transcription. A `※` marks a separator
excluded from the alphabet. A count mismatch rejects the entire row and writes
a diagnostic image. Review character assignments even when counts agree,
especially around disconnected strokes, dots and clipped characters. The
selector preserves significant disconnected pieces when measuring bounds.
Its output consists of candidate crops and review images; it does not modify
`tracing.json`, `companions.json` or the TTX master.

Connected-sort selection (`components: true`) can isolate overlapping italic
serif fragments. Only use it for visually confirmed connected letters. Explicit
`merge_components` groups join zero-based component indices before assigning
characters, for example the dot and stem of an i or two detached parts of an M.
The generated candidate records how many components to keep. Inspect the crop and
the fitted outline: count agreement alone cannot identify a letter or a dot.
Mixed-case rows require a measured `baseline` and cap height; an optional
`baseline_slope` records page tilt relative to the row's left edge. These are
measurements of the specimen, not automatic letter-size normalisation.
`measure_advances` uses the next impression’s ink origin for advance widths;
review this in words, especially for italic overhangs. The final sort in a row
uses explicit bearings because it has no following origin to measure.

`requirements-display.txt` pins NumPy 1.26.4 and SciPy 1.11.4 for this optional
preparation step. Normal builds and checks do not require either package.

## Revising selected glyphs

`scripts/trace_revisions.py` prepares candidate glyph overrides for an existing
family. Set `mode` to `glyph-revision` in
`source/tracing.json`, record the selected crops and `notes`, and use
`review_characters`/`review_words` to focus the historical proof.

```sh
python scripts/trace_revisions.py nero-1888 --output workspace/nero-edits
```

This command reads `source/font.ttx` without applying glyph overrides,
preserves its glyph names and advances, and writes candidate edits only to the
specified directory. It rejects a recipe that changes an advance. Review and
copy the desired files into `source/glyphs/`, following the version, changelog,
before/after and verification steps in [WORKFLOW.md](WORKFLOW.md).

A `replace_bases` mapping may list dependent glyph names, such as Cacute for C.
The helper requires an exact match for the original base contours (apart from
equivalent explicit/implicit closing lines), replaces them with the new drawing,
and keeps all other contours in place. A mismatch fails preparation. This is
appropriate for flattened CFF accents sharing the same original body; translated
or otherwise altered bases require separate reviewed edits. Revision recipes
do not require `companions.json`; their output is a set of glyph override files.

## Vector construction

Optional vector construction uses `requirements-tracing.txt`, which additionally
pins skia-pathops 0.9.0. `scripts/outline_geometry.py` resolves contour overlaps and
constructs translated silhouette differences without a raster step. The Hades
family's `source/derive.py` uses it to prepare a registered companion to Erebus.
These tools are not required by normal builds or checks.

## Comparison proofs

For typeface families with `source/tracing.json`, `build` generates
`specimens/source-review.pdf`. It pairs capitals and figures with their
historical crops, labels inferred drawings, and shows words at four sizes.
Mixed-case families include lowercase comparisons. Recipes can select the
characters and words with `review_characters` and `review_words`.

`specimens/specimen.pdf` contains the full encoded character inventory. Review
both proofs, including punctuation and spacing, before accepting a master.
Document lowercase aliases for capitals-only designs in the metadata, README
and gallery.

## Icon tracing

See [ICONS.md](ICONS.md) for icon manifests, tone layers and delivery formats.

`--jobs 4` prepares independent crops in parallel while preserving manifest order.
`--cache workspace/trace-cache` reuses prepared paths only when the source bytes,
recipe, layer metadata and preparation code match. The cache can be discarded
without affecting the committed master or release builds.

Icon recipes may set `max_ink_dimension` and `center_vertical` to fit wide or tall
artwork uniformly in a common frame. `frame_threshold` uses the lightest retained
trace to measure that frame before applying the same transform to solid and tonal
paths. It prevents pale extremities from clipping without stretching the drawing.

### Tonal region separation

Multi-tone tracing fits contours at each recorded grayscale threshold and uses
vector subtraction to separate the tone regions. The boolean-operation helper
checks results against the operands' fill rules on a deterministic 64 × 64 point
grid. It retries failed operations in rotated or reflected coordinate frames
and with subdivided Bezier curves. Boundary tolerances range from 0.05 to one
font unit. See [the geometry implementation](../scripts/outline_geometry.py)
for the retry sequence. These sampled checks require visual confirmation in
the source proofs.

By default, tone separation starts with integer-rounded input contours. On
failure it retries with unrounded contours, then quadratic curves with a maximum
conversion error of 0.05 font units. Finished regions are rounded to integer
font coordinates. Two recipe options control this process:

- `multitone.round_inputs: false` tries unrounded contours first. This can avoid
  artificial tangencies caused by rounding nested threshold contours. Baltimore
  recipes use this setting with direct grayscale thresholds.
- `multitone.separation: "native-mask-bands"` separates the threshold masks at
  native resolution before fitting contours. Use it for engravings whose vector
  intersections cannot be resolved, and document the reason. The raster bands
  are disjoint, but fitted and rounded edges can meet. Baltimore No. 363 is an
  example of this method.

### PNG rendering

Icon families with `font_export_glyphs: "encoded"` or a
`source/truetype-glyphs/` directory use Cairo 1.18.0 (`libcairo2` on Ubuntu 24.04)
for full-detail tonal PNGs. Cairo renders the master's vector contours with
nonzero winding and antialiasing, supporting outlines that exceed font-renderer
limits. Other icon families use FreeType.

### Caption cleanup and orientation

`post_trace_remove_contours` lists rectangles in font coordinates. After fitting,
preparation removes complete contours whose control bounds lie inside a
rectangle. Contours crossing a rectangle are preserved. Review these measured
regions against the source and retain the evidence for each removal.

For a reviewed orientation correction, `post_trace_transform` contains six affine
coefficients in positive-up font coordinates. It runs after fitting and caption
cleanup, with the same matrix for the solid drawing and every tone. Coordinates
are stored on a 1/64-unit grid; `preserve_coordinates: true` in a glyph override
keeps that precision when compiling CFF. Advances and contour order are retained.
Use measured frame edges or other reliable references and compare the complete
drawing before accepting a rotation; a historical pose or tapered edge is not a
reason to straighten an object.
