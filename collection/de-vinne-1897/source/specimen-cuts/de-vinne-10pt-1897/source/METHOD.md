# Ten-point De Vinne

The 1897 Government Printing Office specimen, printed page 50 (archive leaf
109), supplies complete ten-point capitals, lowercase and figures. Its stock
mark reads Keystone–10. Matching witnesses appear in the census specimen,
printed page 17 (leaf 35), the 1904 job-room specimen, printed page 69 (leaf 85),
and the document specimen, printed page 30 (leaf 65). All four retained JP2s
provide selected forms. The family year identifies an inspected specimen,
not a first casting date. No designer, punch or matrix identity is asserted.

`selection.json` identifies each chosen native impression and derived crop.
Larger census and clearer job-room/document impressions improve matching
letters. Census F, 1897 Q and document S avoid damaged competing witnesses
without drawn repairs. Complete 1897 forms supply the remaining letters.
`source-inventories.json` records exact transcriptions and reviewed segmentation.
In the document text, 80 and oo share pale printing bridges, while two o
impressions have disconnected projection groups. Their corrected crop bounds
retain the observed letters; no missing stroke is invented.

The ten-point cut preserves heavier small-cut strokes and different widths,
Q tail and figures from twelve and fourteen point at equal nominal cap height.
Measured comparisons are retained in `source-quality.json`. No outline is
borrowed across sizes.

Default figures follow the complete census row, with a clearer matching
job-room four: 0/2 are short, 1 is tall, 3/4/5 are lining, 6/8 reach cap height,
and 7/9 descend. Eight observed alternatives have no extra Unicode assignments:

- `ss01`, Census M: shallow central join and thin left stem.
- `ss02`, 1897 figure variants (1, 3, 4, 5): short serifed one and descending
  three/four/five.
- `ss03`, Lining figure variants (0, 7): tall document zero and baseline
  job-room seven.
- `ss04`, Broad S: wider body and flatter diagonal, from the Handy poster.

These labels describe the observed substitutions; they do not claim complete
alternate figure sets. CSS `font-feature-settings: "ss01" 1, "ss03" 1` selects
the census M and two lining figure variants. `alternates-review.pdf` compares
the original native crops with default and alternate outlines, followed by
feature combinations at several sizes.

Small serifs are retained by sampling each original crop four times with
Pillow LANCZOS before paper correction and tracing. The enlargement interpolates
existing pixels; it creates no new source detail. `reference/crops.json`
records all 73 native crop coordinates and derived pixel/file hashes.
`resample_crops.py` verifies each derived image against the retained JP2 and
can recreate the files with `--regenerate`. It checks exact native hashes,
dimensions, modes, pixels and PNG bytes. Pillow 12.3.0 defines these derivatives.

`prepare.py` is the complete preparation entry point. Run with `--output PATH`
and `--potrace PATH`; optional `--cache PATH` caches source/code/recipe hashes.
It verifies the derived crops, traces `tracing.json` and `alternates.json`,
and assembles the OTF with `features.fea`. Import that OTF with the normal
repository command. Release builds use `font.ttx`; generic preparation alone
does not include the named alternatives.

At four-times sampling, paper correction radius 48, blur 1.2 and Potrace
tolerance 0.8 correspond to native radius 12, blur 0.3 and tolerance 0.2.
Thresholds are 155 for census/job-room/document and 170 for 1897. The selected
hyphen uses 120 to exclude a pale end bridge, leaving two separate black
components. Its two bars are encoded as hyphen-minus; no equals operator is
inferred. The em dash after valor is separately observed. Dotted i/j retain
both components. No holes are filled and no outline is drawn or repaired.

Theil–Sen flat-bottom baseline fits and median caplines establish one uniform
scale per physical page. Fitted coordinates are converted back to native
pixels before measurement. Lowercase and paragraph rows have independent
baselines. The distant 1897 and census numeral blocks also have independent
rigid transforms; their baseline-anchor residuals are below 0.32 and 1.67 native
pixels respectively. Relative figure positions remain intact. No shear,
independent width stretching or individual glyph-height normalization is used.

The em is 1000, nominal cap height 700, modern sidebearings 35 and word space 300.
`sizing.json` retains encoded proportions; the short zero advisory is
intentional. `alternate-limits.json` records eight unencoded forms, checked
with their GSUB mappings in all four formats by `verify_alternates.py`.
`review_alternates.py` regenerates their source comparison PDF. Coverage is
complete for A–Z, a–z and 0–9, with observed period, comma, hyphen and em dash.
Unsupported punctuation, symbols and aliases are omitted.


8 whole observed diagonal fractions, cent and percent are retained from matched ATF
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
its forms. Row skew is measured from whole-form ink-box centers at threshold 150, except the fainter LOC row at 190.
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

The accepted Handy chart scale is 25.961500020 font units per
native pixel. Selected companion ink spans approximately -191.8 to
896.3 units, within the existing font metrics.

The common-capital scale fit excludes the broader, flatter Handy S. Its
comparison remains recorded as a distinct source variant; the existing S is unchanged.

Source-quality gaps remain for U+215E (⅞).

Ten-point NY lower thresholds break numerator7 or8, while usable thresholds merge upper slash/8; American has the same tradeoff. BYU and LOC rows omit this form; Handy and NYPL are heavily joined. Seek an intact same-size whole impression before encoding.

The Handy Book of Specimens, printed page 189 (leaf 208), sets both narrow and
broad S in the ten-point word MUSCLES. The first S agrees with the narrow default;
the final S has a wider body and flatter diagonal. A complete broad form repeats
in SPEAKING on printed page 339 (leaf 358). `S.broad`, selected by `ss04`
(Broad S), retains this smoother poster impression. The default S and all
previous outlines, advances and feature mappings remain unchanged.

Eleven non-S poster capitals provide 22 width/height measurements for one
isotropic scale of 25.9377641 font units per native pixel. Eight independent
stem-foot windows establish a median native baseline of 1310 with zero robust
slope and a maximum residual of one native pixel. No common rotation is applied.
The standard setting is separately fitted to ten non-S capitals (20 dimensions)
at 25.6977148 units per pixel; seven foot windows establish baseline 1478 with
zero robust slope and maximum residual one pixel. Baselines use the lower ink
edge, the last black pixel row plus one. S is excluded from both scale fits.

`broad-s-review.json` retains the selected whole impression, common-capital
measurements, native foot windows and comparison witnesses. Fifteen trials
compare five thresholds for each of three whole S impressions. Poster threshold
110 preserves complete terminals and open apertures with smoother bowls than
the heavier trials and the rougher standard broad repeat. Four-times Lanczos
sampling, normalization radius 48, blur 1.2 and Potrace tolerance 0.8 use no hole
filling or drawn repair. Modern sidebearings are 35 units. Minor native edge
variation remains a clearer-witness task; no geometry is borrowed from other
point sizes. Optical agreement does not prove identical punches or matrices.
`broad-s-review.pdf` compares sources, all four formats and feature settings at
several sizes. The named-alternate proof filters selection records by glyph
name so fraction provenance records remain compatible.


## Observed poster punctuation

Matching 10-point Poster De Vinne settings supply the colon, semicolon and right single quotation mark used as an apostrophe.
The LOC Desk Book, printed page 108 (leaf 130), supplies the semicolon.
The NYPL Desk Book, printed page 523 (leaf 540), supplies the apostrophe.
The BYU Handy Book, printed page 598 (leaf 600), supplies the colon.

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
