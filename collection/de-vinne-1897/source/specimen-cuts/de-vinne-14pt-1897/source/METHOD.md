# Fourteen-point De Vinne

The 1897 Government Printing Office specimen, printed page 50 (archive leaf
109), supplies complete fourteen-point capitals and lowercase, plus figures
1–8. Its stock mark reads Keystone–10. The census specimen, printed page 18
(leaf 37), and the 1904 job-room specimen, printed page 68 (leaf 84), provide
matching fourteen-point letters, all ten figures and punctuation. The year in
the family name identifies an inspected specimen, not a first casting date.
No designer, punch or matrix identity is asserted.

`selection.json` identifies every chosen impression. The larger census scan
supplies several clearer letters; the job-room paragraph supplies sharper
matching impressions and punctuation. Remaining letters come from the complete
1897 alphabets. Original JP2 scans, archive locators, member names and hashes
are retained. Source transcriptions are in `source-inventories.json`.

At a common 700-unit nominal cap height, the fourteen-point cut has different
relative widths and counters from the eighteen-point cut, including narrower
M and m. The figure forms also differ. No outline is borrowed across sizes.
Measured comparisons are retained in `source-quality.json`.

The default figures come from the complete census row. Their mixed heights
and descenders are preserved: 2/4/5/7 have lower tops, and 4/5/7 descend.
The corpus also shows six distinct alternatives, retained without additional
Unicode assignments:

- `ss01`, Census M: shallow central join, thin left stem and heavy right stem.
- `ss02`, 1897 figure variants (1, 3): short serifed one and descending three.
- `ss03`, Job-room figure variants (2, 4, 5): tall two and baseline four/five.

These sets describe the observed substitutions; neither figure set claims a
complete alternate ten-figure design. For example, CSS
`font-feature-settings: "ss01" 1, "ss03" 1` selects the census M and the three
job-room figure variants. `alternates-review.pdf` compares each source crop,
default and alternate, and shows the combinations at several sizes.

`prepare.py` is the complete source-preparation entry point. It uses the shared
Potrace 1.16 tracer for `tracing.json` and the named recipes in `alternates.json`,
then assembles all forms with `features.fea`. Run it with `--output PATH` and
`--potrace PATH`; an optional `--cache PATH` caches source/code/recipe hashes.
It writes the importable OTF and two disposable path audits. Import that OTF
with the normal repository import command. Release builds use `font.ttx`.
The generic preparation command alone does not include the named alternatives.

Paper normalization uses radius 12, blur 0.3 pixel, threshold 155 for census
and job-room or 170 for 1897, and Potrace tolerance 0.2. Connected-body selection
isolates neighbouring ink where crop extents overlap. Dotted i/j and the
historical hyphen retain both components. The two horizontal hyphen bars are
encoded as hyphen-minus; no equals operator is inferred. Only the measured
two-pixel enclosed pale blemish in B is filled; both intended counters and the
outer contour are unchanged.

Theil–Sen baseline slopes and median caplines determine one uniform scale per
physical source page. Lowercase and paragraph rows use their own measured
baselines. The distant census numeral block also has its own rigid transform:
baseline figures 1/2/3/6/8/0 agree within 0.24 native pixel, while extrapolating
the capital block would raise all figures. This corrects the gently bowed
source line without changing relative numeral positions. No shear, width
stretching or individual glyph-height normalization is applied.

The em is 1000, nominal cap height 700, modern sidebearings 35 and word space
300. `sizing.json` retains the encoded proportions. Four peer-height warnings
for 2/4/5/7 describe intentional source differences. `alternate-limits.json`
records the six unencoded forms; `verify_alternates.py` checks them and their
GSUB substitutions in all four formats. `review_alternates.py` regenerates the
alternate-source PDF from the release OTF. The encoded inventory is complete
for A–Z, a–z and 0–9, with observed period, comma and hyphen. Unsupported
punctuation and symbols are omitted.


Nine whole diagonal fractions, cent and percent are retained from matched ATF
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
Shorter American cent and percent forms do not determine the fraction-row fit;
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

The accepted Handy chart scale is 16.082321425 font units per
native pixel. Selected companion ink spans approximately -114.9 to
811.3 units, within the existing font metrics.
