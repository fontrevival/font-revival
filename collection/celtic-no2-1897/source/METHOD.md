# Celtic No. 2: twelve-point source method

This revival contains the complete capitals and figures of the labelled
**twelve-point** Celtic No. 2 cut. The 1904 document specimen explicitly credits
Farmer. The date suffix identifies the earliest source used here, not the
first appearance of the historical design.

The 1897 alphabet at printed page 25, native archive leaf 59, supplies QUVWXYZ.
The 1900 census alphabet at printed page 1, native leaf 3, supplies the finer
A–P and all ten figures. The document specimen at printed page 39, native
leaf 83, supplies RST and the printed period. `selection.json` records every
chosen impression. The smaller and larger labelled sizes remain separate
comparison sources; their forms are not used to complete this cut.

The exact original JP2 files and institutional metadata are retained in
`reference/`. Printed pages are read from the scans. Provider page labels in
the 1897 scan metadata disagree with the visible footers and must not be
substituted for those printed locators.

`tracing.json` is reproducible with the shared Potrace 1.16 preparation tool.
Local paper illumination is normalised with a 12-pixel radius, followed by
0.35-pixel blur. Source-specific thresholds retain the observed light strokes:
200 for the census, 180 for the 1897 alphabet and 175 for the document specimen.
Only the largest connected letter component is retained. No holes are filled,
and no letter, figure or punctuation outlines are constructed as companions.
The only companion is an empty 300-unit word space.

Capline and baseline regressions over ordinary flat capitals determine one
uniform scale and one rigid rotation per source row. `measurements.json`
retains those anchors, slopes, fitted native bounds and correction angles.
The nominal cap height is 700 units in a 1000-unit em. Curved overshoots and
the descending Q and R tails remain as printed. Rotation is applied to the
vector trace, leaving the original source image intact. There is no shear or
independent width adjustment.

Sidebearings of 35 units and proportional advances are modern spacing choices.
Lowercase and unsupported punctuation are not encoded. The full supported
character set is explicit in `font.json`; `sizing.json` preserves the reviewed
individual proportions through conversion to the delivery formats.

The assembled card in the job-room specimen, printed page 39, native leaf 55,
supplies the observed ampersand. Its twelve-point setting is identified by matching
letter construction and physical cap heights against the labelled samples on
the same page. `card-source-review.json` retains that evidence and the threshold
comparison. Threshold 175 preserves the complete printed form. Its scale and
rigid rotation come from the surrounding capitals; it is not independently
fitted to a modern punctuation height. The earlier capitals, figures, period
and spacing remain unchanged.

The family is a single scalable offering based on its selected complete alphabet and figures. Other prepared historical sizes remain editable source witnesses in specimen-cuts, with their exact character coverage and source records. The index records punctuation outside the current selection for future compatibility review. Those optical cuts are source evidence rather than separate point-size font products.
