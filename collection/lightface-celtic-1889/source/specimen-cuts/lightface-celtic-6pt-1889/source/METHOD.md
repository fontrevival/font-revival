# Lightface Celtic: six-point source method

This family preserves the complete uppercase and lowercase of the labelled
six-point Light-face Celtic cut, all ten figures, period, comma, hyphen, right
apostrophe and both double quotation marks. The empty word space is a modern
layout advance. No visible character is invented or borrowed from another size.

The 1889 Boston and Central specimen provides the earlier named witness. The
ATF 1896 collective specimen calls the design Lightface Celtic No. 40; the GPO
document specimen attributes it to “American.” The date suffix identifies an
inspected source, not the first release of the type. The designer is unidentified.

The six-point cut has wider lowercase letters than the twelve-point cut at the
same cap reference. This is visible in both the 1897 and census impressions,
including a/e/n/o/x, and remains after fitting the outlines. The difference is
not solely ink weight. The optical comparison proof shows both source cuts.

Original native scans, metadata, exact locators and acquisition hashes are in
`reference/`. The census supplies A–X, a–x and all figures. The document supplies
Y/Z/y/z, apostrophe and quotation marks. Job-room text supplies period, comma
and hyphen. The smaller 1897 and Boston samples and heavily printed ATF sample
remain comparison and provenance sources. `selection.json` identifies every
selected impression and crop; `source-inventories.json` records source-local
coverage across the six matching samples.

`tracing.json` reproduces the outlines with Potrace 1.16 and the shared tracing
tool. Local paper illumination uses radius 8 and a 0.35-pixel blur. Thresholds
are 155 for census letters and figures except B/d/m/n at 165, b/p/q at 175 and a
at 185. Document letters use 175; apostrophe and opening quotation mark use 205;
the closing quotation mark uses 215. Job-room punctuation uses 165. These
settings retain native hairlines and punctuation tails that lower thresholds
drop. No holes are filled. Dots and paired quotation marks remain separate
components. Overlapping f/g projections are isolated from their native bodies.

Capline and baseline regressions determine one uniform physical scale per
source page and a rigid rotation per row. The cap reference is 700 units in a
1000-unit em. Lowercase retains its native proportions at the same page scale.
The figures use a locally measured baseline from 1/4/7: extrapolating from the
far-left capitals would introduce an error from page curvature. No shear,
horizontal stretching or analytic stroke repair is applied.

Modern sidebearings are 35 units and the word space is 300 units. Individual
limits in `sizing.json` preserve reviewed bounds through format conversion.
`source-quality.json` records source choices and rejected trace settings.
