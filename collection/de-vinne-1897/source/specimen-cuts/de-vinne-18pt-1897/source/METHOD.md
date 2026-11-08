# Eighteen-point De Vinne

The 1897 Government Printing Office specimen, printed page 50 (archive leaf
109), supplies complete capitals and lowercase with figure 2. Its stock mark
reads Keystone–10. The census specimen, printed page 18 (leaf 37), and the
1904 job-room specimen, printed page 68 (leaf 84), show matching eighteen-point
letters. Common forms were compared at one uniform scale per source page.
The date in the family name identifies an inspected specimen, not an asserted
first casting date or designer attribution.

`selection.json` records each chosen impression. Larger census letters and
clearer job-room letters replace softer matching impressions where available.
The complete 1897 alphabet supplies the remaining letters. Original JP2 scans,
archive URLs, exact container members, printed locators and hashes are retained.

The census sets lowercase j before i. The character map follows the visible
forms. The job-room hyphen has two horizontal bars; both are retained in
hyphen-minus. No equals operator is inferred. Its short zero is selected from
VALUE OF MICA 760. The optional tall zero uses a sharper intact impression
from the 1904 GPO figure page, printed page 124 (archive leaf 140). The softer
1897 Handy witness, page 338 (leaf 357), and damaged Census zero remain
comparison sources. `ss01`, named Tall zero, selects this one alternative;
`lnum` selects the observed lining set. The default figures retain their
printed unequal heights and descenders.

`tracing.json` reproduces 80 visible encoded glyphs using the shared Potrace 1.16
tracer. The earlier alphabet, figures and punctuation use local paper
normalization with radius 12, blur 0.3 pixel and threshold
155 for census/job-room or 170 for the selected 1897 forms. The tolerance is
0.2. The connected letter body isolates neighbouring fragments in overlapping
capital crops; no letter boundary is sliced. Dotted i/j and the double-bar
hyphen each retain two components. Enclosed pale printing pinholes of one,
two and four native pixels in L, 9 and comma are removed, respectively.
The exact changed pixels are recorded; no outer-edge pixel or intended
counter is affected. Cleaner observed b and y impressions avoid their earlier
blemishes without drawing replacements.

`measurements.json` retains fitted native bounds and baseline anchors.
Theil–Sen baseline slopes and median caplines determine a uniform scale per
source page and a rigid rotation per row. Lowercase uses that same physical
scale and its own observed baseline. There is no shear, width stretching,
individual glyph-height normalization or substitution from another point size.
The nominal cap height is 700 in a 1000-unit em. Modern spacing uses 35-unit
sidebearings and a 300-unit space. `sizing.json` preserves the reviewed
proportions through format conversion.

The encoded inventory contains all capitals, lowercase and figures, plus the
observed period, comma, hyphen, colon, semicolon, question mark and right
apostrophe. Unsupported characters are omitted. The
source comparison and word proofs show the actual coverage and optical forms.

The GPO poster, printed page 120 (leaf 136), provides thirteen common capitals
for a least-squares isotropic scale of 11.3005486 font units per native pixel.
Forty-seven matching header-glyph centers transfer this scale to the figure
page: 11.3137425 units per pixel. One scale applies to both figure rows;
their heights are never independently normalized. Header fits at several
thresholds establish stability. Optical correspondence does not establish
identical historical punches or matrices.

`figure-punctuation-review.json` records these comparisons, row measurements
and ten selected whole impressions. Figures 1, 2, 5, 7 and 9 have unencoded
lining alternatives; the existing 3, 4, 6 and 8 serve both settings. The tall
zero is shared by `lnum` and `ss01`. Its 555-unit advance is preserved with
centered sidebearings rounded to the shared 1/64-unit grid. Each figure row
has its own measured baseline and rigid rotation. Small source differences
in figure height and overshoot remain.

Four punctuation characters come from the poster text. Six distributed
flat-bottom lowercase letters determine each row's baseline by Theil–Sen
slope and median intercept. Their maximum residual is under 0.65 native
pixel. The four punctuation forms retain these baseline positions and the
same page scale as the capitals. The right apostrophe is U+2019; no straight
apostrophe or mirrored opening quote is inferred.

The additions use four-times Lanczos sampling, paper normalization radius 48,
blur 1.2 pixels, threshold 150 and tolerance 0.8. Five thresholds were reviewed
for seventeen figure impressions and four punctuation impressions. All chosen
forms are complete whole traces, without hole filling or drawn repairs. The
centered figure-row zero has a right-stroke printing hole; an intact repeated
zero supplies the alternate. `tall-zero-review.json` retains the earlier Handy
selection as historical comparison evidence.

`reference/crops.json` and `resample_crops.py` verify derived crops against
the retained native pages, including the earlier comparison crop.
`source/prepare.py` rebuilds encoded and alternate outlines;
`verify_alternates.py` checks features and alternate geometry in all four formats.

The ATF fraction assortments supply nine diagonal fractions, cent and percent.
New York printed page 436 (leaf 506) supplies quarter, half, three-quarters,
one-third and cent; the Handy book page 40 (leaf 59) supplies percent. The BYU
copy page 637 (leaf 639) supplies two-thirds and the four eighth fractions.
All are whole printed forms, with no assembled numerators or reconstructed
slashes. Deliberate diagonal interruptions and all counters remain intact.

`diagonal-fractions-review.json` records source choices, threshold comparisons,
physical scales and row geometry. The Handy fraction page scale is 13.3314558
font units per native pixel, transferred from its measured eighteen-point
capitals through repeated footer type. Whole-form width and height comparisons
transfer this scale to New York (9.7813652) and BYU (5.7983809). No fraction is
compressed to the nominal cap height: the source forms are about 970 units tall.
These comparisons support grouping, without establishing identical matrices.

The charts contain no co-set text baseline. Fraction rows therefore use an
explicit modern placement: the median ink-box center lies at mid-cap, 350 units.
One rigid rotation and one vertical translation apply to an entire printed row;
inter-form height differences are preserved. Row skew comes from the ink-box
centers at threshold 150, independently of the selected outline threshold.
The resulting ink range is about -144 to 842, within the existing font metrics.
A matching historical setting with letters or ordinary figures remains desirable
evidence for placement. This convention is not claimed as a historical baseline.

The fraction traces use four-times Lanczos sampling, normalization radius 48,
blur 1.2, tolerance 0.8 and component minimum area 16 (one native pixel).
Thresholds from 110 through 190 were compared across 22 complete impressions.
No enclosed holes are filled. New York half at 170 retains pale slash ink;
BYU three-eighths at 190 and five-eighths at 170 avoid print-edge notches and
spurious pale pinholes; seven-eighths at 110 avoids a small lower-slash spur.
The other selected fractions and cent use 150; the intact Handy percent uses
130. The New York percent has a broken upper connection, and lower-resolution
Handy eighths merge strokes that remain separate in the sharper BYU source.
Exact quarter-turn orientation precedes the recorded New York crop coordinates.
`diagonal-fractions-review.pdf` compares the native impressions, outlines and
mixed text at several sizes. Earlier glyph outlines, spacing and features remain
unchanged.

The NYPL copy of the 1898 Desk Book, printed page 523 (leaf 540), sets descending
3 and 4 beside lowercase text and a short 2. Complete impressions provide
`three.oldstyle` and `four.oldstyle`, selected by `onum` or `ss02` (Descending
three and four). The other default figures already have the corresponding
oldstyle positions. Existing defaults, the lining mappings and tall zero remain
unchanged. The additions are source-supported alternatives, not translated copies
of the current default outlines.

Twenty-two common capitals provide 44 width/height measurements for one isotropic
page scale of 3.3783237 font units per native pixel. Nine flat-footed n/h/m/i/r
impressions on the figure line determine a Theil–Sen slope and median baseline;
curved t feet, round forms and figures are excluded. The rigid row rotation is
-0.1061622 degrees; the maximum anchor residual is 1.23 native pixels. The figure
positions come from this co-set text, with no independent size or baseline fit.

`descending-figures-review.json` records the measurements and whole-witness
comparison. NYPL thresholds 90, 110 and 130 preserve the open 3 and single-counter
4. Threshold 110 is selected for both. Five thresholds of the softer Handy page
338 figures confirm their geometry and descending setting. The retained NYPL
image has a processed gray background; its small edge irregularities remain.
There is no filled counter, synthetic smoothing or assembled replacement.
Four-times Lanczos sampling, normalization radius 48, blur 1.2 and tolerance 0.8
match the recorded recipes. Native source dimensions are retained under one
uniform scale. Sidebearings are modern 35-unit layout choices. Optical matching
does not establish identical punches or matrices.
