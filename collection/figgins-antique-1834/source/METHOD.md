# Historical source preparation

Figgins Antique combines complementary impressions of the heavy Antique design.
The Double Pica setting on archive leaf 161 supplies the complete capitals,
figures and 23 lowercase letters. The heavy Long Primer setting on leaf 163
supplies whole observed g, j and q. The lighter English setting was compared
and rejected as a donor. These physical sizes are source labels for one scalable
font. No missing character is reconstructed.

The exact JP2 sources and the lossless quarter-turn of leaf 161 are retained.
`measurements.json` records independently measured page rotations, transcribed
rows, source-coordinate transformations, native cap heights and local baselines.
Flat capitals determine uniform scale; descenders retain their measured extent.
The g baseline follows the adjacent lowercase x-height; j uses the neighbouring
a baseline. No nonuniform stretching is used.

`rows.json` records the original source windows and explicit separation of
touching printed serifs. Their transformed boundaries are retained in
`measurements.json`. A separate V in Votes and i in in avoid adjoining serif
fragments. The Long Primer alphabet omits V; the main Double Pica alphabet
supplies it.

`tracing.json` records every accepted crop and cleanup setting. Potrace 1.16
traces native grayscale masks after a 0.2-pixel blur, using threshold 100
(or 85 for j to preserve its visible dot gap), no counter filling and a curve
tolerance of 0.15. Detached dots and paired quotation marks are preserved.
Spaces, sidebearings and digital metrics are new; the ASCII quotation mark
aliases the observed closing double quotation mark.
