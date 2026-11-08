# Six-point De Vinne

The 1897 Government Printing Office specimen, printed page 50 (archive leaf 109),
supplies complete six-point capitals, lowercase and figures. Its stock mark
reads Keystone–10. Matching witnesses occur in the census specimen, printed
page 17 (leaf 35), the 1904 job-room specimen, printed page 69 (leaf 85), and the
document specimen, printed page 30 (leaf 65). Three retained JP2s supply selected
forms; the document page is comparison evidence. The year identifies an inspected
specimen; no first-casting, designer, punch or matrix attribution is inferred.

`selection.json` locates every chosen impression and derived crop.
`source-inventories.json` retains all 23 native rows and exact transcriptions.
The job-room heading reads YALUKI. Its damaged I in RIVER is excluded from
baseline and capline anchors and from outline selection. The census lowercase
crop extends far enough to retain the complete z. Adjacent projections and pale
printing bridges are separated at reviewed native body boundaries; disconnected
r, O and y parts are grouped without drawing connections. Every native mapping
was visually reviewed.

Clearer job-room letters replace many weaker alphabet impressions. Census a/w
preserve their open apertures. Matching 1897 D/I/W retain stronger edges and
junctions, and its short zero retains a closed counter. No holes are filled,
strokes drawn or outlines borrowed from another point size.

The complete census numeral row defines the default design sequence: short
0/1/2, descending 3/4 and near-cap lining 5/6/7/8/9. Cleaner matching job-room
five/nine and 1897 zero preserve their source-relative positions. Six named
alternatives have no additional Unicode assignments:

- `ss01`, Census M: shallow central join and thin left stem.
- `ss02`, 1897 figure variants (5, 7, 9): descending five, seven and nine.
- `ss03`, Lining figure variants (0, 1): tall job-room zero and one.

These are observed substitutions, not complete alternate figure sets.
For example, CSS `font-feature-settings: "ss01" 1, "ss03" 1` selects the census
M and tall zero/one. `alternates-review.pdf` compares native crops, default
outlines and alternatives, followed by feature combinations at several sizes.
`review_alternates.py` regenerates it; `verify_alternates.py` checks all six
unencoded forms and their mappings, labels, bounds and contours in four formats.

Each original crop is sampled four times with Pillow LANCZOS before paper
correction and tracing. This interpolates existing pixels without adding source
detail. `reference/crops.json` records 71 native coordinates and exact pixel/file
hashes. `resample_crops.py` verifies the derived images against the retained JP2s
and can recreate them with `--regenerate`. Pillow 12.3.0 defines these derivatives.

`prepare.py` is the complete preparation entry point: pass `--output PATH` and
`--potrace PATH`, with an optional `--cache PATH`. It verifies the crops, traces
`tracing.json` and `alternates.json`, then assembles an OTF with `features.fea`.
Import that OTF with the repository command. Release builds use `font.ttx`;
generic preparation alone does not include the named alternatives.

Four-times paper radius 48, blur 1.2 and tolerance 0.8 correspond to native
radius 12, blur 0.3 and tolerance 0.2. Thresholds are 155 for census/job-room
and 170 for 1897, with no per-glyph override. Dotted i/j and the double-bar
hyphen retain two components. The hyphen has 346/345 black pixels in its two
bars and no enclosed white island; it is encoded as hyphen-minus. No equals
operator or unsupported punctuation is inferred.

Theil–Sen flat-bottom baselines and median caplines establish one uniform scale
per physical page. Fitted bounds are converted back to native coordinates before
measurement. Lowercase and text rows have independent baselines, as do the
distant 1897 and census numeral blocks. No shear, separate width stretching or
individual glyph-height normalization is used. `measurements.json` records every
anchor, rotation and scale; `source-quality.json` compares six/eight/ten point.

The em is 1000, nominal cap height 700, modern sidebearings 35 and word space 300.
Coverage is complete A–Z, a–z, 0–9 plus observed period, comma and double-bar hyphen.
Two figure-top advisories for 6/8 preserve the observed mixed figure heights.
`sizing.json` and `alternate-limits.json` retain explicit reviewed proportions.


6 whole observed diagonal fractions, cent and percent are retained from matched ATF
assortments. `diagonal-fractions-review.json` identifies each complete impression,
its native page, exact oriented crop, threshold and component/counter inventory.
No numerator, denominator or slash is borrowed from another form or point size.
Clearer whole impressions avoid printed bridges and pale defects; no missing
ink is drawn, and no enclosed holes are filled in these additions.

The retained Handy common-capital page establishes a single physical scale by
least-squares comparison with existing same-size capitals. Repeated footer type
transfers that scale to its fraction chart. Corresponding whole fraction widths
and heights then transfer scale to the other selected books. All fitted common
forms and residuals are recorded. No fraction is compressed to cap height, and
matching construction does not establish identical physical punches or matrices.

The charts do not supply a co-set text baseline. An explicit modern convention
centers each printed fraction row at mid-cap, 350 units. One rigid rotation and
one vertical translation apply to a row, preserving relative differences among
its forms. Row skew is measured from whole-form ink-box centers at threshold 150.
Shorter cent and percent forms do not determine the fraction-row fit;
they retain their native positions under the same row transform. A matching
historical setting with letters or ordinary figures remains desirable evidence
for vertical placement. The modern convention is not a historical-baseline claim.

The additions use four-times Lanczos sampling, normalization radius 48, blur 1.2,
Potrace 1.16 tolerance 0.8 and minimum component area 16 (one native pixel).
The main comparison used thresholds 110/130/150/170/190. Finer BYU windows
from 50 to 120 were also reviewed: 539 distinct threshold trials across 98
whole impressions (540 displayed evaluations include one cached confirmation). The retained recipes specify
the selected threshold for each whole form. Exact quarter-turn orientation
precedes cropping for the New York and American Line raw scans.
`resample_crops.py` verifies derived pixels and hashes against retained native
pages; `prepare.py` includes that audit before tracing. The focused
`diagonal-fractions-review.pdf` shows native impressions and mixed text at
several sizes, including the existing figure variants. Earlier letter and figure
outlines, metrics and OpenType mappings remain unchanged.

The accepted Handy chart scale is 37.708684721 font units per
native pixel. Selected companion ink spans approximately -130.4 to
817.1 units, within the existing font metrics.

The selected three-quarters is printed under the seven-point label on BYU
printed page 637. The retained six/seven pairs show matching native physical
size and construction; `paired_label_evidence` records all eleven paired forms
on that page. The clearer seven-labelled impression uses the same physical page
scale as the six-labelled forms, without a seven-to-six resizing factor. Its
original printed label is retained in the source inventory, recipe and proof.
This does not establish that the historical pieces share a punch or matrix.

Quarter, half, one-third, cent and percent use BYU six-labelled impressions at
threshold 150. Two-thirds uses threshold 130. Three-quarters uses the clearer
seven-labelled impression at 110; the six-labelled alternative has a ragged
slash foot at lower thresholds and a bar/four contact at 100. Seven-eighths
uses the six-labelled impression at 80, preserving all four ink parts and both
counters; a lower threshold damages the stroke, while 90 joins the lower bar
to the eight. No individual fraction height is normalized.

One-eighth (U+215B), three-eighths (U+215C) and five-eighths (U+215D) remain
unencoded source-quality gaps. The compared whole impressions contain unresolved
slash/figure contacts or broken strokes at usable thresholds. Their exact
tradeoffs are recorded in `source_quality_gaps`; no separation is invented.


## Observed poster punctuation

Matching 6-point Poster De Vinne settings supply the semicolon and right single quotation mark used as an apostrophe.
The LOC Desk Book, printed page 108 (leaf 130), supplies the semicolon.
The NYPL Desk Book, printed page 523 (leaf 540), supplies the apostrophe.

Shared capitals and lowercase forms support the same optical cut. This is not
an identification of physical punches or matrices. Each setting uses one scale
measured from independent common capitals; whole flat-footed n/h/m/i/r/l forms
anchor its text-row baseline. A rigid rotation corrects the measured scan slope.
Each mark retains its printed vertical position, with modern 35-unit sidebearings.

Four-times Lanczos sampling, normalization radius 48, blur 1.2 and Potrace
tolerance 0.8 preserve the whole native marks. No hole filling, drawn repair,
independent stretching or source-part assembly is used. Colon and semicolon
retain two separate components; the apostrophe retains one. Selected thresholds,
exact crops, baseline anchors, common-form comparisons and rejected witnesses
are retained in `punctuation-review.json`. `punctuation-review.pdf` shows native
evidence, word settings and all four delivery formats.

Joined native projections remain unsliced and are excluded from single-character
measurements. Two pale comparison m impressions retain both visible stem
components; their accidental initial component filtering was corrected before
acceptance. Existing alphabet, figure, fraction, spacing and feature data are
preserved. Unsupported punctuation and aliases remain unencoded. Processed NYPL
apostrophes retain their visible stepped edges; cleaner matching witnesses remain
a source-quality task.
