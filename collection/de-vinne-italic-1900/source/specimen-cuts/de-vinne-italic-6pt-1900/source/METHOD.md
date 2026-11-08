# Six-point De Vinne Italic

The GPO census specimen, printed page 15 (archive leaf 31), shows complete
six-point capitals, lowercase and all ten figures, labelled case 6. Matching
impressions in the 1897 New York ATF specimen, page 335 (leaf 403), and the
BYU copy of the 1897 Handy Book, page 365 (leaf 367), supply clearer letters
and figures. The year identifies the retained complete alphabet, not the
first appearance of the design.

Eight native pages are retained. The Pacific 1896 page 429, Cornell Handy
1897 page 197, Desk 1898 page 303 and collective ATF 1896 page 286 provide
comparison evidence. The collective page credits Central Type Foundry,
St. Louis, for the design; it does not identify an individual punch or matrix.
`source-inventories.json` records exact sample transcriptions and omissions,
15 native rows and their coordinates; selected additional forms are documented
in `italic-quality-review.json`. Joined ct/ru/ta samples remain comparison evidence.

`selection.json` locates all 63 selected visible forms. Clearer BYU letters
and New York letters/figures supplement the complete census alphabet.
Census a, n and i avoid printing bridges in competing witnesses. New York g
preserves both counters, its two has a complete foot, and BYU F avoids a
census ink pinhole. The census m retains a small printed shoulder notch;
a sharper matching witness may improve it without changing its design.

The Q threshold is 165 to retain its faint native lower bowl junction.
Larger Q contexts corroborate the closed bowl but supply no outlines.
The census j threshold is 135; two explicit rectangles in its sampled crop
remove neighbouring i/k ink while retaining the complete hook and separate
dot. Other selected outlines use threshold 155. No holes are filled and no
strokes are drawn. Dotted i/j retain two components; other glyphs retain one.

`reference/crops.json` records 63 exact four-times RGB LANCZOS derivatives,
native source hashes, oriented crop coordinates and derivative hashes.
New York's raw camera image receives an exact clockwise quarter-turn before
cropping. The BYU image is already oriented and receives no rotation.
`resample_crops.py` verifies every pixel and file, or recreates derivatives
with `--regenerate`. Pillow 12.3.0 defines the sampling. Interpolation adds
no source detail. Paper radius 48, blur 1.2 and tolerance 0.8 correspond to
native radius 12, blur 0.3 and tolerance 0.2.

Theil–Sen baselines and median caplines establish one uniform scale per
physical source. Text and numeral rows have independent measured baselines.
Rigid rotations remove scan skew while preserving the historical italic
slant. No shear, width stretching or individual glyph-height normalization
is used. `measurements.json` records the anchors and transformations.

`prepare.py --output PATH --potrace PATH` verifies the retained crops and
traces the complete source recipes. An optional `--cache PATH` saves fitted
paths. Import the resulting OTF with the repository import command; release
builds use `font.ttx`. No named alternatives are accepted for this cut.

The em is 1000, nominal cap height 700, modern sidebearings 35 and word space
300. Coverage is complete A–Z, a–z and 0–9, plus the observed dollar and modern
space advance. There is no invented punctuation or alias. The clearer LOC
six-point dollar is used; the filled collective impression remains comparison evidence.
`sizing.json` records reviewed bounds for every
encoded character; there are no sizing advisories.

## Whole-form source comparison

The six-point dollar is taken whole from the LOC Desk Book, printed page 349
(archive leaf 357), before 2468. Threshold 155 retains both apertures and the
printed bar and terminal extents. Twelve common capitals supply 24 dimensions
for one uniform scale 21.840752; ten whole flat-footed letters establish the
text baseline. Its measured scan slope is corrected by a rigid
rotation; the italic slant is preserved. The dollar has modern 35-unit
sidebearings and advance 650.

`italic-quality-review.json` retains native boxes, measured rows, threshold
trials and rejected impressions. Four-times Lanczos sampling, paper radius 48,
blur 1.2 and tolerance 0.8 follow the existing method. No holes are filled,
strokes drawn, parts assembled, or widths stretched. Common-form agreement
supports the same optical design, without identifying a punch or matrix.

`review_source_quality.py` regenerates `source-quality-review.pdf`: native
evidence, common-capital comparisons, threshold trials, desktop/web word
settings and the independent native baseline anchors.
