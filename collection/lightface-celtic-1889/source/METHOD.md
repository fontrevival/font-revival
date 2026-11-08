# Lightface Celtic: twelve-point source method

This revival preserves the complete uppercase and lowercase of the labelled
**twelve-point** Light-face Celtic cut, with its ten figures, period, comma,
hyphen and right apostrophe. The only new companion is an empty word space.
The date suffix refers to the inspected 1889 Boston specimen, not a claim of
first release. The designer is unidentified. The Boston and Central specimen
names the type; the GPO document specimen prints the attribution “American.”
The ATF 1896 collective specimen labels the design Lightface Celtic No. 40.

The original native scans and institutional metadata are retained in
`reference/`. Printed pages were read from the visible footers; provider labels
for the 1897 scan can disagree. `selection.json` identifies every selected
character and exact crop. `source-inventories.json` records source-local
coverage, keeping differently named and differently sized samples separate.

The census impressions provide larger matching letters and all figures. The
1897 alphabet supplies complete twelve-point forms missing from the census
sample. Selected job-room and document impressions improve clarity or supply
punctuation. Boston and ATF remain comparison and provenance witnesses. The
larger ATF scan is more heavily printed and is not the preferred outline source.

`tracing.json` reproduces the outlines with the shared Potrace 1.16 preparation
tool. Local paper illumination is normalised with radius 12, followed by a
0.35-pixel blur. Thresholds are recorded per character: 155 for the census,
150 for the selected 1897 forms except Q at 170, 165 for the document, and 155
for the job-room except n/r/q at 170 and comma/apostrophe at 185. The i and j
retain their two native components. Other letters retain the complete connected
body; no holes are filled. Overlapping horizontal extents were isolated from
separate native components, without slicing the f/g or i/j overhangs.

The lighter thresholds exclude scan fringe; they were rejected wherever a
hairline or component disappeared. A second job-room w supplies a complete
impression at the selected weight. `source-quality.json` records those choices.
Contour counts are an additional check: they do not prove stroke completeness.

Capline and baseline regressions determine one uniform physical scale per page
and a rigid rotation per row. Lowercase uses the same page scale as capitals
and its own measured baseline; its proportions are not independently fitted to
a generic x-height. The nominal cap height is 700 units in a 1000-unit em. Native
overshoots, descenders and the Q tail remain. There is no shear, separate width
scaling, reconstructed stroke or substitution from another point size.

Sidebearings of 35 units and a 300-unit space are modern spacing choices.
`sizing.json` preserves the reviewed individual bounds through format conversion.
Unsupported symbols are omitted and the exact encoded set is in `font.json`.

The family is a single scalable offering based on its selected complete alphabet and figures. Other prepared historical sizes remain editable source witnesses in specimen-cuts, with their exact character coverage and source records. The index records punctuation outside the current selection for future compatibility review. Those optical cuts are source evidence rather than separate point-size font products.
