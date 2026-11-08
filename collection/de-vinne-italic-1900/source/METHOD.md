# De Vinne Italic

This is one scalable offering. The eight-point witness supplies a coherent italic alphabet, the clearer accepted g, and the observed lining-R option. Source point sizes identify specimens, not recommended or required digital sizes.

The default alphabet, metrics and named alternatives are unchanged from the selected master. Supplementary whole characters preserve combined coverage without invented forms; their exact donors and unchanged coordinates are recorded in `consolidation.json`. Different source-size drawings and earlier proofs remain under `specimen-cuts/` as archival evidence. They are not separate font products.

The following detailed method describes the selected alphabet source and its earlier additions. Its source-size comparisons do not assert that supplementary characters came from the same physical casting.

# Eight-point De Vinne Italic

The GPO census specimen, printed page 15 (archive leaf 31), shows complete
eight-point capitals, lowercase and ten figures, labelled case 7. Matching
impressions in the 1897 New York ATF specimen, page 335 (leaf 403), and the
BYU 1897 Handy Book, page 365 (leaf 367), supply clearer letters and figures.
The year identifies the complete retained alphabet, not the first appearance
of the design. Six-point and eight-point cuts have separate proportions;
neither supplies outlines for the other.

Eight native pages are retained. Pacific 1896 page 429, Cornell Handy 1897
page 197, Desk 1898 page 303 and collective ATF 1896 page 286 provide further
comparisons. The collective page credits Central Type Foundry, St. Louis,
for the design; no individual punch or matrix is identified.
`source-inventories.json` records exact transcriptions, omissions and
15 native rows, with selected additional forms documented in `italic-quality-review.json`.
Joined ro samples remain comparison evidence only.

`selection.json` locates 62 default visible forms and the named alternative.
New York K replaces the cracked census K; New York C avoids a census pinhole.
BYU m retains all three stems, unlike the broken census impression.
Census a preserves its open upper aperture, and census five avoids a New York
pinhole. New York G avoids an upper printing bridge, New York U and zero avoid
damaged competing impressions, and BYU S has its complete upper stroke.
The Ryan g in Tumbling supplies a clearer loop junction with both counters
retained. The census impression remains available for comparison.

The default census R has a descending leg. Two R impressions on each of the
BYU and Pacific pages have lining legs. `source-quality.json` records all
five witnesses and measured positions. The BYU R is retained as unencoded
`R.lining`, selected with stylistic set `ss01` (Lining R). For CSS, use
`font-feature-settings: "ss01" 1`. No additional Unicode assignment is made.
`review_alternates.py` compares the native source, default and alternative,
then shows feature settings at four sizes. `verify_alternates.py` checks the
mapping, label, bounds, advance and contours in all four font formats.

Every selected crop is sampled four times with Pillow LANCZOS.
`reference/crops.json` records 64 derivatives, including the retained census g
comparison, with native coordinates and exact
pixel/file hashes. New York's raw image receives an exact clockwise
quarter-turn before cropping; the BYU image is already oriented.
`resample_crops.py` verifies these derivatives and recreates them with
`--regenerate`. Pillow 12.3.0 defines the sampling; no new source detail is
introduced. Selected outlines use threshold 155, except Ryan g at 175,
with paper radius 48,
blur 1.2 and tolerance 0.8, corresponding to native radius 12, blur 0.3 and
tolerance 0.2. No holes are filled or strokes drawn.

Two recorded crop-relative rectangles isolate census j from neighbouring
i/k ink. Its native dot and complete hook are retained. Dotted i/j keep
two components; other selected forms keep one.

Theil–Sen baselines and median caplines establish one uniform scale per
physical source. Text and numeral rows have independent baselines. Rigid
rotations remove measured scan skew while preserving the italic slant.
There is no shear, width stretching or per-glyph height normalization.
`measurements.json` records anchors, source scales and rotations.

`prepare.py --output PATH --potrace PATH` verifies crops, traces default
and alternate recipes, and assembles the OTF with `features.fea`. An optional
`--cache PATH` saves fitted paths. Import the OTF with the repository command;
release builds use `font.ttx`. Generic tracing alone omits the alternative.

The em is 1000, nominal cap height 700, modern sidebearings 35 and space 300.
The revised g retains its 733-unit
advance and 35-unit left bearing; its right bearing follows the observed width.
Coverage is complete A–Z, a–z and 0–9, plus modern word space. Punctuation
requires clearer source evidence and is not invented. `sizing.json` and
`alternate-limits.json` retain explicit reviewed bounds; there are no
sizing advisories.

## Whole-form source comparison

The eight-point g is taken whole from Tumbling in the John Ryan Foundry
1894 specimen, printed page 69 (archive leaf 75). Threshold 175 retains both
counters and the complete loop junction. Eight common capital impressions
supply 16 dimensions for uniform scale 23.509621; nine whole flat-footed
letters establish the text baseline. Weak A/N/I strokes are excluded from
scale fitting. The Vaulting g has a broken upper bowl at 175 and is retained
only as comparison evidence. The existing 733-unit g advance is preserved.

`italic-quality-review.json` retains native boxes, measured rows, threshold
trials and rejected impressions. Four-times Lanczos sampling, paper radius 48,
blur 1.2 and tolerance 0.8 follow the existing method. No holes are filled,
strokes drawn, parts assembled, or widths stretched. Common-form agreement
supports the same optical design, without identifying a punch or matrix.

`review_source_quality.py` regenerates `source-quality-review.pdf`: native
evidence, common-capital comparisons, threshold trials, desktop/web word
settings and the independent native baseline anchors.
