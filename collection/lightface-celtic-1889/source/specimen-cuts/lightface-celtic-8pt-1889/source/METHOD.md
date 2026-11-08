# Lightface Celtic: eight-point source method

This family preserves the complete uppercase, lowercase and ten figures of the
labelled eight-point Light-face Celtic cut. Period, comma, semicolon, hyphen,
em dash and right apostrophe are observed. The empty word space is a modern
layout advance. No visible form is invented or borrowed from another size.

The Boston and Central 1889 specimen supplies an earlier named witness. ATF's
1896 collective specimen calls it Lightface Celtic No. 40. The date suffix
identifies an inspected source, not the design's first release; its designer is
unidentified. Five matching specimen books support the revival. The differently
labelled eight-point Celtic types in the 1904 document specimen are separate.

The eight-point cut has broader lowercase than the twelve-point cut at a common
cap reference. The difference recurs in native 1897 and census impressions at
several thresholds. In the fitted outlines a/e/n/o are about 14–23 percent wider.
The optical comparison proof shows both cuts; weight alone was not used to
distinguish them.

Native scans, exact locators, acquisition hashes and source metadata are retained
in `reference/`. Census impressions supply A–R, a–r except i/j, and all figures.
The 1897 alphabet supplies V/X/Z and i/j/x/z. Job-room text supplies S/T/U/W/Y,
s/t/u/v/w/y and punctuation; Boston supplies the apostrophe. The heavily inked
ATF page remains comparison evidence. `selection.json` records every crop and
decision; `source-inventories.json` records exact source-local coverage.

The census i/j are joined and excluded. Separate 1897 impressions are used.
Manual source review corrected the automatic 1897 b–g assignments, where a split
b and overlapping f/g had concealed errors despite equal character counts.
No joined impression was divided by an invented cut.

`tracing.json` reproduces the outlines with Potrace 1.16. Local illumination uses
radius 10 and a 0.35-pixel blur. Census threshold is 155, except f/m at 165, b/n
at 175 and q at 195. The 1897 letters use 165, except x at 175. Job-room forms use
165, except u at 175 and em dash at 185. Boston apostrophe uses 205. Repeated s
impressions were compared; the s in “worse” retains both arms clearly at 165.
No holes are filled. Dots and semicolon components remain separate.

Capline and baseline regressions determine one uniform physical scale per page
and rigid rotation per row. The cap reference is 700 in a 1000-unit em. Lowercase
retains native proportions. Figures use a local baseline from 1/4/7 rather than
extrapolation across page curvature. The em dash's measured ink-column centreline
has a local tilt: a rigid rotation squares it while preserving its row-relative
vertical centre. The measured columns and correction are in `selection.json`.
No shear, width stretching or analytic stroke replacement is applied.

Modern sidebearings are 35 units and the word space is 300. Individual reviewed
limits in `sizing.json` preserve bounds through format conversion.
`source-quality.json` records source decisions and rejected trace settings.
