# Celtic No. 2: eight-point source method

This revival preserves the complete observed capitals, ten figures and declared
punctuation of the eight-point Celtic No. 2 cut. The document specimen
credits Farmer. The date suffix identifies an inspected historical source,
not the design's first appearance. No visible forms are invented or borrowed
from another optical size; the empty word space is a modern layout advance.


The native comparisons distinguish the optical cuts by recurring proportions
across books, independently of impression weight. `optical-comparison.json`
retains the source crops and three-threshold measurements. Its trial traces
are comparison evidence; some lose fine strokes and are not approved outlines.
The selected source decisions are in `source-quality.json` and `selection.json`.

Selected impressions:

- `reference/leaf-3.jp2`: ABCDEFGHKLMNOPQSTUVXYZ09
- `reference/gpo-job-1897-leaf-59.jp2`: IJRW12345678
- `reference/gpo-document-1904-leaf-83.jp2`: .
- `reference/gpo-jobroom-1904-leaf-55.jp2`: ’

Exact historical JP2 files, acquisition hashes and institutional metadata are
retained in `reference/`. Printed pages were read from the scans; archive leaves
and printed page numbers are distinct locators. In particular, the 1897 provider
page labels disagree with some visible footers.

The shared Potrace 1.16 preparation tool reproduces `tracing.json`. Local paper
illumination uses a 12-pixel radius and 0.35-pixel blur. The largest connected
printed component is retained, with no filled holes. Reviewed thresholds are:

- 175: ABCDEFGHIKLMNOPQRSTUVXYZ’
- 185: JW04569
- 195: 12378.

Capline and baseline regressions determine one uniform physical scale and rigid
rotation per source row. The cap reference is 700 units in a 1000-unit em.
Separated figure groups use a local baseline from the feet of 1/4/7 at the same
physical scale; this avoids extrapolating page curvature across blank space.
There is no shear, independent width fitting or analytic stroke repair.

Modern sidebearings are 35 units and the word space is 300. Individual limits
in `sizing.json` preserve the reviewed bounds through format conversion.
Small historical impressions retain minor print irregularities visible in the
native evidence. Native crops, large outlines and words at 16–96 pixels were
reviewed for complete strokes, counters, spacing and baseline alignment.
