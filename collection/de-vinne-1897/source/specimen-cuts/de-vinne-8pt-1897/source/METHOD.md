# Eight-point De Vinne

The 1897 Government Printing Office specimen, printed page 50 (archive leaf 109),
supplies complete eight-point capitals, lowercase and figures. Its stock mark
reads Keystone–10. Matching witnesses occur in the census specimen, printed
page 17 (leaf 35), the 1904 job-room specimen, printed page 69 (leaf 85), and the
document specimen, printed page 30 (leaf 65). All four retained JP2s supply
selected forms. The year identifies an inspected specimen; no first-casting,
designer, punch or matrix attribution is inferred.

`selection.json` locates every chosen impression and derived crop.
`source-inventories.json` retains all 22 native rows and exact transcriptions.
Adjacent job-room re/ro/ry projections have separate connected bodies. The
ta pair in Hystaspes has a pale printing bridge; lower-threshold contours locate
its crop boundary. A document n has disconnected stem and arch projections,
reunited without drawing a connection. Every native mapping was visually reviewed.

Clearer job-room letters replace many weaker alphabet impressions. The 1897 J
retains its complete hook; the census R has a closed bowl; another job-room m
preserves both open arches. Document L/S remain selected. Cleaner matching 1897
zero/six/eight/nine avoid the chipped zero and rougher census edges. No holes
are filled, strokes drawn or outlines borrowed from another point size.

The complete census numeral row defines the default design sequence: short 0,
tall 1/2/4/6/7/8 and descending 3/5/9. The matching 1897 replacements preserve
their own source-relative positions. Seven named alternatives have no additional
Unicode assignments:

- `ss01`, Census M: shallow central join and thin left stem.
- `ss02`, 1897 figure variants (1, 2, 4, 7): short one/two and descending four/seven.
- `ss03`, Lining figure variant (3): baseline document three.
- `ss04`, Broad S: wider body and flatter diagonal, from the BYU poster.

These are observed substitutions, not complete alternate figure sets.
For example, CSS `font-feature-settings: "ss01" 1, "ss03" 1` selects the census
M and lining three. `alternates-review.pdf` compares native crops, default
outlines and alternatives, followed by feature combinations at several sizes.
`review_alternates.py` regenerates it; `verify_alternates.py` checks all seven
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
radius 12, blur 0.3 and tolerance 0.2. Thresholds are 155 for census/job-room/document
and 170 for 1897, with no per-glyph override. Dotted i/j and the selected double-bar
hyphen retain two components. The hyphen has 611/608 black pixels in its two bars
and no enclosed white island; it is encoded as hyphen-minus. No equals operator
or unsupported punctuation is inferred.

Theil–Sen flat-bottom baselines and median caplines establish one uniform scale
per physical page. Fitted bounds are converted back to native coordinates before
measurement. Lowercase and text rows have independent baselines, as do the
distant 1897 and census numeral blocks. No shear, separate width stretching or
individual glyph-height normalization is used. `measurements.json` records every
anchor, rotation and scale; `source-quality.json` compares eight/ten/twelve point.

The em is 1000, nominal cap height 700, modern sidebearings 35 and word space 300.
Coverage is complete A–Z, a–z, 0–9 plus observed period, comma and double-bar hyphen.
Three peer-height advisories for 0/5/9 preserve the observed mixed figure heights.
`sizing.json` and `alternate-limits.json` retain explicit reviewed proportions.


7 whole observed diagonal fractions, cent and percent are retained from matched ATF
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
its forms. Row skew is measured from whole-form ink-box centers at threshold 150, except the fainter LOC row at 170.
Shorter cent and percent forms do not determine the fraction-row fit;
they retain their native positions under the same row transform. A matching
historical setting with letters or ordinary figures remains desirable evidence
for vertical placement. The modern convention is not a historical-baseline claim.

The additions use four-times Lanczos sampling, normalization radius 48, blur 1.2,
Potrace 1.16 tolerance 0.8 and minimum component area 16 (one native pixel).
Initial thresholds 110/130/150/170/190 were compared, followed by finer windows
where counters or separate strokes changed. The review record gives the total
trial count and the selected recipes retain their exact thresholds. The retained recipes specify
the selected threshold for each whole form. Exact quarter-turn orientation
precedes cropping for the New York and American Line raw scans.
`resample_crops.py` verifies derived pixels and hashes against retained native
pages; `prepare.py` includes that audit before tracing. The focused
`diagonal-fractions-review.pdf` shows native impressions and mixed text at
several sizes, including the existing figure variants. Earlier letter and figure
outlines, metrics and OpenType mappings remain unchanged.

The accepted Handy chart scale is 29.335353618 font units per
native pixel. Selected companion ink spans approximately -150.4 to
843.8 units, within the existing font metrics.

Source-quality gaps remain for U+2154 (⅔), U+215D (⅝).

Eight-point whole impressions retain slash/figure contacts at usable thresholds. NY lower thresholds break numerator or denominator; BYU numerator also has a pale notch. LOC176 still breaks the denominator and177already joins lower slash/numerator. No intact four-part whole witness selected.

Eight-point Handy and BYU merge both slash ends. New York joins the upper slash to the eight at usable thresholds. American Line has a broken five until the slash ends join. The LOC upper counter remains open through threshold 174 and closes only after a slash contact forms. Seek an intact same-size whole impression.

The BYU copy of the 1897 ATF specimen, printed page 598 (leaf 600), sets both
forms in `PUBLIC SPEAKING IN THE COURT HOUSE`: the S in SPEAKING is broad and
flat, while HOUSE has the narrower form matching the default. Four S impressions
in the BYU series page 356 (leaf 358) and the NYPL poster CONVENTIONS also match
the narrow form. `S.broad`, selected by `ss04` (Broad S), retains the complete
BYU broad impression. The default S and all earlier outlines and advances remain
unchanged. The broad letter is not substituted from another point size.

Eleven common capitals provide 22 width/height measurements for one isotropic
scale of 13.4163876 font units per native pixel. U, M and both S forms are
excluded. Fifteen stem-foot windows in P/B/L/I/K/N/T/H/E establish a Theil-Sen
slope and median baseline. Their lower ink edges use the final black pixel row
plus one. The measured slope is zero; no common rotation is applied. The maximum
anchor residual is two native pixels, at the first P. The broad S retains its
small baseline overshoot without independent height adjustment.

`broad-s-review.json` retains common-capital measurements, foot windows and the
whole-impression comparison. Five thresholds of each co-set S were reviewed.
Threshold 150 retains the complete broad form and open apertures with smooth
main curves. Four-times Lanczos sampling, normalization radius 48, blur 1.2 and
Potrace tolerance 0.8 use no hole filling or drawn repair. Modern sidebearings
are 35 units. Optical agreement does not prove identical punches or matrices.
`broad-s-review.pdf` compares both forms, all four formats and feature settings
at several sizes. The original named-alternate proof filters selection records
by glyph name, so fraction provenance records remain compatible.

The whole U in PUBLIC on BYU printed page 598 (leaf 600) supplies clearer flared
heads, right stem and bowl than the pale Census source. Five GPO and five BYU
whole impressions share the asymmetric construction. Raising the Census
threshold changes the fine stem and width substantially; its lowest trial loses
the right stem. The evidence supports a source-quality improvement rather than
a separate U design. The processed NYPL witness has rougher stepped edges.

The accepted poster U uses the same independent eleven-capital scale and fifteen
native serif-foot baseline anchors as the broad S. U, S and M are excluded from
the scale fit. Threshold 130 retains both complete stems, open interior and
smooth main curves. Five poster thresholds were reviewed, followed by before
and after word settings at 8, 24 and 48 points. Four-times Lanczos sampling,
normalization radius 48, blur 1.2, no hole filling and tolerance 0.8 match the
documented source pipeline. No independent stretch or drawn repair is used.

The new source width gives advance 744, formerly 707, with unchanged modern
35-unit sidebearings. Its measured baseline overshoot is retained. Every other
outline, advance, encoded character and feature mapping is preserved.
`u-source-review.json` retains the previous source recipe and drawing, accepted
comparison and baseline evidence. `u-source-review.pdf` compares whole sources,
before and after settings, and all four formats. Minor native edge variation
remains; future sharper matching impressions may support further improvement.


## Observed poster punctuation

Matching 8-point Poster De Vinne settings supply the colon, semicolon and right single quotation mark used as an apostrophe.
The LOC Desk Book, printed page 108 (leaf 130), supplies the semicolon.
The BYU Handy Book, printed page 598 (leaf 600), supplies colon and apostrophe.

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
