# Six-point De Vinne Condensed

The GPO census specimen, printed page 16 (archive leaf 33), shows complete
six-point capitals, lowercase and ten figures, labelled case 14. Matching
impressions in the 1897 New York ATF specimen, page 329 (leaf 397), the BYU
1897 Handy Book, page 359 (leaf 361), and Pacific 1896, page 418 (leaf 422),
supply clearer forms. The year identifies the complete retained alphabet,
not the first appearance of the design. Every outline belongs to this size.

Seven native pages are retained. Cornell Handy 1897 page 191, Desk 1898
page 297 and collective ATF 1896 page 281 provide further comparisons.
The collective page credits Central Type Foundry, St. Louis, for the design;
no individual punch or matrix is identified. `source-inventories.json`
records exact transcriptions, source-local omissions and 13 mapped rows.
All 426 mapped impressions were visually reviewed. Joined Co/ce samples
remain comparison evidence only. Dollar, hyphen and further punctuation
require clearer same-size witnesses.

`selection.json` locates 63 default visible forms and one named alternative.
BYU A and M use clearer repeat impressions. New York supplies complete
figures, G, straight R and g/m/n/p/s/u. Pacific h has an open arch, unlike
the bridged BYU impressions. The selected a preserves two closed counters,
visible in independent small ATF impressions. The census a has a broken
lower cross-stroke; a modern aperture is not drawn into either source.
Less spread same-cut ink remains a source-quality question.

The default straight R agrees with the census construction. Three R
impressions on each of the BYU and Pacific pages have sweeping legs.
`source-quality.json` records all 13 R witnesses and measured positions.
The BYU sweeping form is retained as unencoded `R.sweeping`, selected with
stylistic set `ss01` (Sweeping R). For CSS, use
`font-feature-settings: "ss01" 1`. No additional Unicode assignment is made.
`review_alternates.py` compares the native source, default and alternative,
then shows feature settings at four sizes. `verify_alternates.py` checks the
mapping, label, bounds, advance and contours in all four font formats.

Every selected crop is sampled four times with Pillow LANCZOS.
`reference/crops.json` records 64 derivatives, native coordinates and exact
pixel/file hashes. New York's raw image rotates exactly 90 degrees clockwise;
Pacific rotates 270 degrees clockwise. The BYU image is already oriented.
`resample_crops.py` verifies these derivatives and recreates them with
`--regenerate`. Pillow 12.3.0 defines the sampling; no new source detail is
introduced. ATF outlines use threshold 155; the 13 selected Census forms
use 170. This retains faint native strokes, including K's upper arm and
Q's upper bowl. All use paper radius 48, blur 1.2 and tolerance 0.8,
corresponding to native radius 12, blur 0.3 and tolerance 0.2.
No holes are filled or strokes drawn. Dotted i/j keep two components;
other selected forms keep one. No crop-relative ink erasure is needed.

Theil–Sen baselines and median caplines establish one uniform scale per
physical source. Text and numeral rows have independent baselines. Rigid
rotations remove measured scan skew. Threshold-specific recipes retain the
original measured source scale and baseline. There is no shear, width
stretching or per-glyph height normalization. `measurements.json` records
anchors, scales, rotations and the selected fitted bounds.

`prepare.py --output PATH --potrace PATH` verifies crops, traces default
and alternate recipes, and assembles the OTF with `features.fea`. An optional
`--cache PATH` saves fitted paths. Import the OTF with the repository command;
release builds use `font.ttx`. Generic tracing alone omits the alternative.

The em is 1000, nominal cap height 700, modern sidebearings 35 and space 300.
Coverage is complete A–Z, a–z and 0–9, plus the observed comma and modern
word space. Other punctuation is not invented. `sizing.json` and
`alternate-limits.json` retain explicit reviewed bounds; there are no
sizing advisories.
