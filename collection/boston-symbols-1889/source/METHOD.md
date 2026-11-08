# Boston Symbols 1889

Original native JP2 leaves, source URLs, hashes and rights evidence are retained under reference/. Crop coordinates, masks and tracing parameters are in tracing.json; coverage is recorded in inventory.json and the central Boston Cuts inventory.

Symbols are separated using ink-row whitespace and individually reviewed against the native scan. The technical table has unequal column spacing. Catalogue numbers, fractions, ordinary letters and numeral samples are excluded. Separately printed size variants retain their observed differences. The map plate contributes the isolated construction types; labelled map and building demonstrations are retained in the source as compositions of those types.

Local paper correction uses a 25-pixel maximum filter with a radius-4 Gaussian estimate, then divides the scanned gray values by the paper estimate. Three thresholds and exact PathOps differences produce disjoint primary, secondary and tertiary vector regions at opacities 1, 0.55 and 0.25. The tones interpret scanned ink strength and are not claims of separately coloured printing inks. No missing strokes are invented.

The longest ink dimension fits 1800 units in the 2048-unit em, with 64-unit bearings and uniform scaling. Potrace 1.16 fits cubic curves for the canonical CFF master. Normal builds use source/font.ttx without the network or tracing tools. Original project work is copyright Harold Lehmann and uses the repository MIT license.

The 460 exports include 417 technical-table symbols, 17 crochet patterns, 10 small commercial symbols and 16 map types. Monochrome thresholds start from per-crop Otsu separation on locally corrected paper, then receive reviewed overrides for sun faces (180), fine map rules (200), faint at signs (230), crochet frames and counters (160–225), pale hairlines and astronomical signs (230), and the tiny 6-point percentage mark (200). Final thresholds, not a fresh automatic estimate, are committed in tracing.json. Small scans retain their printed gaps; faint lines are not reconstructed.

`measure_thresholds.py` prints candidate values for comparison without editing the authoritative recipe. Review the source and both tonal and monochrome proofs before adopting any candidate; global thresholding cannot faithfully resolve every pale hairline and tiny white counter at once.

`sign-classification.json` records historical functional names supplied by the
explicit legends on [printed page 18 of the GPO 1904 specimen](https://archive.org/details/123459_1904/page/n34/mode/1up).
The retained source clarifies conjunction, opposition, trine, quartile, sextile,
the lunar nodes, Pallas, Ceres, Juno, Vesta, geometrical proportion and several trade
and apothecary signs. The lower-loop node is the Dragon’s Head; the upper-loop
node is the Dragon’s Tail. These semantic correspondences do not assert that
different point sizes or foundries used identical matrices. Classification changes alone preserve the drawings, metrics and Private Use assignments.

## Preferred matching sign impressions

Twenty-one Boston six-point astronomical identities use matching impressions from the GPO 1904 specimen, printed page 18 (PDF page and archive leaf 34). The native comparison resolves fine loops, terminals and rays obscured by the earlier soft scan interpretation. The supplying GPO forms have no printed point-size label; the six-point names identify their original Boston context. Design correspondence does not establish shared physical matrices.

`gpo-witness-review.json` records both source locators, the previous metadata and recipes, selected crops, measured outline limits and the reasons for each source choice. Glyph overrides preserve the original master as a baseline and every advance width. Uniform scaling fits each new outline within that advance. Tiny source irregularities remain; no ideal curves, artificial symmetries or missing strokes are substituted.

The GPO crops use native grayscale without paper normalization. Monochrome thresholds are 215 except the Sun with a face and Ceres (195), and Venus (225). Disjoint primary/secondary/tertiary thresholds are 215/220/225, or 195/205/225 for the two lighter forms. The shared frame threshold is 225. The [source comparison proof](../specimens/gpo-sign-witness-review.pdf) retains both historical crops and both monochrome interpretations alongside the selected tonal vector.

Two further matching GPO witnesses clarify the curled per/each sign and the
degree ring. The per/each drawing uses the labelled six-point commercial row;
its original Boston five-and-a-half-point context remains in the name. The
degree-ring legend has no printed point size. Thresholds 215 and 195 respectively
retain the observed open counters; native asymmetry remains. Both source crops,
old recipes and original advances are retained in `gpo-witness-review.json`.
The [commercial and degree comparison](../specimens/gpo-commercial-witness-review.pdf)
shows the original and selected drawings in monochrome and tones.

Nine further matching witnesses preserve complete pound-weight bowls and feet,
the per/each oval, the fine cent joins, nearly uniform plus arms, the complete
division dots, radical stroke contrast and the pointed prime. The original
Boston names and recipes remain in `gpo-witness-review.json`. The supplying
GPO point sizes are independent of the names' Boston size context. All advances
are unchanged. The hooked algebraic radical is classified by its repeated
position in the algebraic rows and the labelled radical legend; its individual
impression has no printed caption. The pound ligature also has commercial use.

The [matched-witness proof](../specimens/gpo-matched-witness-review.pdf) compares
both native sources and the old/new monochrome and tonal paths. Vector differences
separate nested ink contours. The larger plus uses tone thresholds 205/215/225
to exclude pale paper flecks; monochrome uses 225. No analytic geometric redraw,
invented join or unmeasured straightening is applied.

The thin square and nine-point triangle use complete matching twelve-point GPO
impressions. The triangle's crop excludes an isolated paper fleck well to its
left, preserving the complete outline. Thresholds 195/205/215 retain the native
ink without the square's pale interior paper mark. The original and selected
sources and monochrome/tonal drawings appear in the
[geometric comparison](../specimens/gpo-geometric-witness-review.pdf).
The original advances and Boston size contexts remain unchanged.

A matching ten-point GPO commercial impression improves the large pound-weight
ligature while retaining its Boston identity and advance. The complete native
bowl requires threshold 225; the lower-threshold trial drops its hairline.
[The source comparison](../specimens/gpo-pound-witness-review.pdf) retains both
historical impressions and monochrome/tonal interpretations. The GPO medical
legend also identifies the seven-point open barred round form as a scruple.
