# Twelve-point De Vinne

The 1897 Government Printing Office specimen, printed page 50 (archive leaf
109), supplies complete twelve-point capitals, lowercase and figures. Its stock
mark reads Keystone–10. The census specimen, printed page 18 (leaf 37), and the
1904 job-room specimen, printed page 68 (leaf 84), provide matching letters,
figures and punctuation. The document specimen, printed page 30 (leaf 65), is
a comparison witness; it supplies no selected outline. The family year names
an inspected specimen, not a first casting date. No designer, punch or matrix
identity is asserted.

`selection.json` identifies every chosen impression. Larger census and sharper
job-room impressions replace poorer matching letters. Remaining forms come
from the complete 1897 rows. Original JP2 scans, archive locators, member names
and hashes are retained. Exact transcriptions are in `source-inventories.json`.
The census lowercase reads `abddefghijklmnop`: its third and fourth letters
are both d, and c is absent. The chosen d is the fourth impression.

At a common 700-unit nominal cap height, the twelve-point cut preserves broader,
heavier small-cut proportions than fourteen and eighteen point, including M/m,
and different Q and figure forms. No outline is borrowed across sizes.
`source-quality.json` records measured comparisons and the remaining scope for
sharper matching twelve-point witnesses.

The complete census figure row is the default. Its 2 is short and 4/7 descend;
3/5/9 are lining, unlike some adjacent optical cuts. Nine distinct observed
alternatives are retained without additional Unicode assignments:

- `ss01`, Census M: shallow central join, thin left stem and heavy right stem.
- `ss02`, 1897 figure variants (0, 1, 3, 5, 9): short round zero, short serifed
  one, and descending three/five/nine.
- `ss03`, Job-room figure variants (2, 4): tall two and baseline four.
- `ss04`, Broad S: wider body and flatter diagonal, from the BYU poster.

These labels name the observed substitutions; they do not claim complete
alternate figure sets. CSS `font-feature-settings: "ss01" 1, "ss03" 1` selects
the census M and the two job-room figures. `alternates-review.pdf` compares
source crops, default forms and alternatives, with feature examples at several
sizes.

`prepare.py` is the complete source-preparation entry point. It uses the shared
Potrace 1.16 tracer for `tracing.json` and the named recipes in `alternates.json`,
then assembles all forms with `features.fea`. Run with `--output PATH` and
`--potrace PATH`; optional `--cache PATH` caches source/code/recipe hashes. It
writes an importable OTF and two disposable path audits. Import that OTF with
the normal repository import command. Release builds use `font.ttx`. The
generic preparation command alone does not include the named alternatives.

Paper normalization uses radius 12, blur 0.3 pixel, threshold 155 for census
and job-room or 170 for 1897, and Potrace tolerance 0.2. Connected-body selection
isolates neighbouring ink where crops overlap. Both components of dotted i/j
and the double-bar hyphen remain. The selected hyphen is the third job-room
impression, in man-ner, whose bars are separated. It is encoded as hyphen-minus;
no equals operator is inferred. No holes are filled and no visible outline is
drawn or repaired.

Theil–Sen baseline slopes and median caplines give one uniform scale per
physical source page. Lowercase and paragraph rows have their own measured
baselines. Both distant numeral blocks also use independent rigid transforms:
1897 baseline anchors agree within 0.28 native pixel and census anchors within
0.82 pixel. Relative figure heights and positions remain intact. There is no
shear, independent width stretching or individual glyph-height normalization.

The em is 1000, nominal cap height 700, modern sidebearings 35 and word space
300. `sizing.json` preserves encoded proportions; three peer-height advisories
for 2/4/7 are intentional. `alternate-limits.json` records nine unencoded
forms; `verify_alternates.py` checks their outlines, advances and GSUB features
in all four formats. `review_alternates.py` regenerates the alternate-source
PDF. Coverage is complete for A–Z, a–z and 0–9, with observed period, comma,
right single quotation mark and hyphen. Unsupported punctuation and symbols,
including an ASCII apostrophe alias, are omitted.


Nine whole diagonal fractions, cent and percent are retained from matched ATF
assortments. `diagonal-fractions-review.json` identifies each complete impression,
its native page, exact oriented crop, threshold and component/counter inventory.
No numerator, denominator or slash is borrowed from another form or point size.
Clearer whole impressions avoid printed bridges and pale defects; no missing
ink is drawn, and no enclosed holes are filled in these additions.

The retained Handy common-capital page establishes a single physical scale by
least-squares comparison with eleven existing same-size capitals. The broader
Handy S is retained as comparison evidence and excluded from the scale fit.
Repeated footer type transfers that scale to its fraction chart. Corresponding whole fraction widths
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
Five thresholds 110/130/150/170/190 were compared. The retained recipes specify
the selected threshold for each whole form. Exact quarter-turn orientation
precedes cropping for the New York and American Line raw scans.
`resample_crops.py` verifies derived pixels and hashes against retained native
pages; `prepare.py` includes that audit before tracing. The focused
`diagonal-fractions-review.pdf` shows native impressions and mixed text at
several sizes, including the existing figure variants. Earlier letter and figure
outlines, metrics and OpenType mappings remain unchanged.

The accepted Handy chart scale is 19.532025124 font units per
native pixel. Selected companion ink spans approximately -134.0 to
845.2 units, within the existing font metrics.

The BYU copy of the 1897 ATF specimen, printed page 598 (leaf 600), sets both
narrow and broad S in `EXECUTOR’S SALE`. The narrow form agrees with the default;
the broad form repeats in the Handy specimen, printed page 339 (leaf 358).
`S.broad`, selected by `ss04` (Broad S), retains the complete clearer BYU impression.
The default S and all earlier outlines and advances remain unchanged.

Eleven non-S capitals provide 22 width/height measurements for one isotropic
scale of 8.7829378 font units per native pixel. Both S forms are excluded from
the fit. Seven serif-foot windows in E/X/E/T/A/L/E establish a Theil–Sen slope
and median baseline. Their lower ink edges use the final black pixel row plus
one; curved overshoots and the R tail are excluded. The rigid rotation is
0.0617411 degrees; maximum anchor residual is 0.914 native pixel. The broad S
retains its small baseline overshoot without independent height adjustment.

`broad-s-review.json` retains the common-capital measurements, foot windows and
whole-impression comparisons. Five thresholds of each of three S impressions
were reviewed. BYU threshold 150 preserves the whole broad form with less edge
irregularity than the softer Handy repeat. Four-times Lanczos sampling,
normalization radius 48, blur 1.2 and Potrace tolerance 0.8 use no hole filling
or drawn repair. Modern sidebearings are 35 units. Optical agreement does not
prove identical punches or matrices. `broad-s-review.pdf` compares the source,
both forms, all four formats and feature settings at several sizes.
