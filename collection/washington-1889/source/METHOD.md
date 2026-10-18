# Washington 1889: source and method

The historical Washington page is printed p. 184, PDF page 190,
Internet Archive leaf 190. The native JP2 and institutional metadata are
retained in `reference/`; `font.json` records the source and rights evidence.

`rows.json` records reviewed transcriptions and preview coordinates. Selection
requires one segmented impression per transcribed character. `selections.json`
records the chosen sorts; `tracing.json` records the final native-pixel crops,
cleanup, target heights and bearings. Larger impressions take priority; smaller
ones supply additional letters. All scaling within a traced impression is uniform. Baselines include measured
page slope.
Differences between optical sizes remain visible. The tiny punctuation samples
are excluded; punctuation comes from explicit MIT project drawings.

The historical lowercase is retained, including dots and descenders. Measured
baselines preserve ascenders and descenders independently of the body height.

## Supplemental impressions

`supplemental-rows.json` records additional Washington lines from three books:

| Source | Location | Selected impressions |
| --- | --- | --- |
| Central/Boston, *Popular Designs for Artistic Printers*, 1892 | Unnumbered leaves 78–79, PDF pages 79–80 | 54-point `k` in “Drink”; 42-point `u` in “Buckles”; 36-point `m` in “Luminous” |
| ATF, *Collective Specimen Book*, 1895/1896 | Printed p. 460 | 54-point `5` in “Not 5 Fit”; 48-point `7p` in “Hid 7 Tip”; 42-point `g` in “Pig”; 30-point `w` in “Show”; 24-point `V` in “Violets” |
| ATF, *A desk book of printing types*, 1898 | Printed pp. 444–445, native leaves 446–447 | 54-point `h` in “March”; 48-point `y4` in “Monday 4”; 42-point `W` in “Washers”; 30-point `b` and `9` in “Abundance $89” |

The retained native leaves and lossless ATF 1896 crop are described in
`reference/supplemental-sources.json`. Institutional metadata and source links
are retained with them. The ATF 1896 crop excludes the modern facsimile's
introductory material. `tracing.json` selects the exact individual impressions
and records cleanup, height, baseline, and advance. The new entries refer to
zero-based row numbers in `supplemental-rows.json`.

The larger `g` and `p` impressions establish the contours and stroke contrast. The
new `q` reflects the refined `p`; its terminals remain inferred. The small 1889 `v`
establishes the fork and foot, while its display-size reconstruction uses the
newly observed `V` at 72% scale. The larger `y` corroborates the flared right
entry. The lowercase `v` has its own weight correction. The `y` itself is traced from the 48-point impression, including its
continuous descending curve, rather than composed from separate branches.

Uniform scaling establishes the proportions of each new trace. Advances are
retained except for `hkmw`: their former reconstructed cells were too narrow
for the observed outlines. These four receive 35-unit sidebearings. No accents
in this family's character map depend on these bases; encoding and OpenType
features are retained.

## Display weight

The smaller optical sizes are heavier than the 60-point anchor letters even
when their scans are clean. `weight-refinement.json` records the individual
corrections to `457Vbgmpw`: a narrow band around the traced boundary is removed
using vector operations, and the original measured bounds are restored. The
insets range from 2 to 17 font units; they were reviewed against the larger
`d`, `o`, and `n`, in words and at several sizes. These are modern weight
adjustments to observed forms. The source proof labels them as redrawn.

The `q` inherits the refined `p`. The `v` uses a separate correction before
lowercase scaling, so thinning the capital `V` does not over-lighten its
lowercase companion. Additional blur in the 1892 `kmu` crops smooths the
enlarged scan's pixel steps before fitting curves. It does not change the
historical construction.

With the pinned `requirements-tracing.txt` dependencies and Potrace 1.16,
prepare candidate overrides outside the family for review:

```sh
python collection/washington-1889/source/prepare_revisions.py \
  --output workspace/washington-revisions
```

`source/glyphs/` contains the release overrides over the original CFF master.
The trace recipe and companion paths also describe the revised drawings, so
re-preparing a master does not restore the superseded forms. The before/after
proof is `specimens/weight-and-forms-review.pdf`.

`companions.json` separates inferred letters and figures from observed crops.
Each companion records its construction. Explicit font-unit paths are sufficient
to repeat preparation without working notebooks. Spacing is new digital work.
The year in the name dates the specimen rather than a claimed first issue.

Use Python 3.12, the pinned repository dependencies and Potrace 1.16:

```sh
python scripts/trace_specimen.py washington-1889 --output workspace/Washington1889-Regular.otf
python scripts/fontrevival.py import washington-1889 workspace/Washington1889-Regular.otf
python scripts/fontrevival.py sizecheck washington-1889
python scripts/fontrevival.py build washington-1889
```

Normal release builds use the canonical `font.ttx`, not the tracing recipe.
Inspect source comparisons, the full inventory and words at several sizes.

## Remaining reconstructions

The following original crops are retained for comparison, but their enlarged
scan outlines are replaced with explicit drawings: `0fvz`. Each entry
in `companions.json` explains its source relationships and inferred details.
The source-comparison proof labels these as redrawn, as it does the documented
display-weight refinements above.

The consulted Washington pages do not supply `JQZjq`. Those forms remain
inferred; a complete historical alphabet is not claimed. The initial-alphabet
books from Bruce (1828), Howe (1830), Boston (1832), Figgins (1834), and Caslon
(1841) supplied no additional Washington evidence. The later Lindsay (1890)
and Ryan (1894) specimen searches also supplied no selected Washington forms.

The existing vertical font metrics retain sufficient room for the descenders.
The `g`, `p`, and `y` depths follow the selected larger impressions.
