# Eight-point De Vinne Condensed

The GPO census specimen, printed page 16 (archive leaf 33), shows complete
eight-point capitals, lowercase and ten figures, labelled case 15. Matching
impressions in the 1897 New York ATF specimen, page 329 (leaf 397), the BYU
1897 Handy Book, page 359 (leaf 361), and Pacific 1896, page 418 (leaf 422),
supply clearer forms. The year identifies the complete retained alphabet,
not the first appearance of the design. Every outline belongs to this size.
The six-point cut has its own outlines and proportions; selected measurements
of both sizes are retained in `source-quality.json`.

Eleven native pages are retained. Cornell Handy 1897 page 191, Desk 1898
page 297 and collective ATF 1896 page 281 provide further comparisons.
The collective page credits Central Type Foundry, St. Louis, for the design;
no individual punch or matrix is identified. `source-inventories.json`
records exact transcriptions, source-local omissions and mapped source rows.
All 366 alphabet and figure impressions were visually reviewed. The Handy poster page supplies the observed punctuation documented below.
Other companions still require source review.

`selection.json` locates 76 default visible forms and one named alternative.
BYU supplies most clearer letters, including intact g and m. New York h/n
have open arches; L avoids native BYU wear, T has its complete left serif,
and all ten figures retain complete contours. Pacific G avoids native BYU
wear. The selected a preserves two closed counters, visible in independent
small ATF impressions. A modern aperture is not drawn into the source;
less spread same-cut ink remains a source-quality question.

The default sweeping R agrees with the census construction. Two R
impressions on each of the BYU and Pacific pages have straight legs.
`source-quality.json` records all nine R witnesses and measured positions.
The BYU straight form is retained as unencoded `R.straight`, selected with
stylistic set `ss01` (Straight R). For CSS, use
`font-feature-settings: "ss01" 1`. No additional Unicode assignment is made.
`review_alternates.py` compares the native source, default and alternative,
then shows feature settings at four sizes. `verify_alternates.py` checks the
mapping, label, bounds, advance and contours in all four font formats.

Every selected crop is sampled four times with Pillow LANCZOS.
`reference/crops.json` records 77 derivatives, native coordinates and exact
pixel/file hashes. New York's raw image rotates exactly 90 degrees clockwise;
Pacific rotates 270 degrees clockwise. The BYU image is already oriented.
`resample_crops.py` verifies these derivatives and recreates them with
`--regenerate`. Pillow 12.3.0 defines the sampling; no new source detail is
introduced. ATF alphabet outlines use threshold 155; the 12 selected Census forms
use 170. This retains faint native strokes, including the full X/Z/k/w
and q's upper bowl. All use paper radius 48, blur 1.2 and tolerance 0.8,
corresponding to native radius 12, blur 0.3 and tolerance 0.2.
No holes are filled or strokes drawn. Dotted i/j keep two components;
other alphabet forms keep one. Double quotes and the hyphen keep two components. No crop-relative ink erasure is needed.

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
Coverage is complete A–Z, a–z and 0–9, with modern word space and the observed
poster punctuation and stacked fractions documented below. Unsupported companions are not invented.
`sizing.json` and `alternate-limits.json` retain explicit
reviewed bounds; there are no sizing advisories.


## Observed poster punctuation

The 1897 Handy Book labels the corresponding optical size on printed page 341
(archive leaf 360). The index correctly locates this poster section at 340–341;
the ordinary Condensed pages cite 332–333 in error. Those pages contain
Title Black and Boston Black and are excluded from this family’s evidence.

Twenty-three shared capitals and lowercase forms were compared at one uniform
cap scale. Their proportions and characteristic shapes agree with this cut;
the printed straight R agrees with its retained named alternative. The
poster letters themselves are comparison evidence. Existing alphabet and
figure outlines, spacing and stylistic substitution remain unchanged.

The poster punctuation is traced from its native image at four-times Lanczos
sampling. `punctuation-review.json` records selections and threshold trials;
`measurements.json` retains robust row baselines and the heading-cap scale.
Each mark keeps its position relative to its own text row. There is no
independent character-height normalization, invented outline, filled counter
or unsupported alias. Exact source crops are included in `reference/crops.json`.

The double-bar hyphen is encoded as hyphen-minus by its printed function.
Threshold 70 excludes the gray right-edge printing bridge while preserving
two native black bars. Thresholds 90–170 join those bars; 50 narrows them.
The opening and closing double quotations retain their different printed
vertical positions. A sharper matching witness remains a quality task.


## Observed stacked fractions

The Handy Book poster and fraction chart, printed pages 341 and 40, show the
corresponding named optical size. Twenty adjacent poster figures were compared
across the eight- and ten-point samples; their scale agrees with the existing
fonts. The poster fractions retain that heading-cap scale and the baseline
measured from figures 1, 4 and 7. A robust fit through the fraction bars removes
row skew. These bars sit below cap midheight, and denominators extend below
the figure baseline; neither position is normalized.

One uniform chart scale is fitted from seven common whole-fraction widths and
heights. The worn seven-eighths is excluded from this fit. The chart barline is
aligned using the observed poster bar-to-baseline distance. `fraction-review.json`
and `measurements.json` record these fits, threshold comparisons and selections.
Every addition is a complete traced impression, with no substituted numerator,
denominator or analytically drawn fraction bar. The tiny printed four can have
a solid counter; clearer matching impressions remain source-quality tasks.

The 1898 Desk fraction page has filled detail; the 1906 American Line page has
soft small detail. Both are comparison sources. The latter prints folio 698
on archive leaf 646. Provider metadata is four pages behind here: leaf 650
actually prints Roycroft folio 702. Native folios establish these citations.

Eight-point seven-eighths remains unencoded because both Handy impressions
have a broken numerator. Three-eighths uses threshold 170 to retain its pale
upper denominator loop. The native joins and unequal counters are preserved.
