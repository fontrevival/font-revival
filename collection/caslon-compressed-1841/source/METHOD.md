# Historical source preparation

The retained native JP2 leaf comes from Henry Caslon’s 1841 specimen. The PNG is an exact quarter-turn for reading. `rows.json` records the manually transcribed settings and native crop selection. `measurements.json` retains source dimensions, fitted baselines, cap scale and the small rigid rotation applied to each drawing. Every glyph uses uniform scaling; widths are not stretched.

`tracing.json` records threshold 150, blur 0.35 pixels, connected-component selection and Potrace 1.16 curve fitting. Detached punctuation marks keep their observed components. The whole visible alphabet and ten figures are sourced; no missing character is reconstructed. Spaces and digital spacing are new. Lowercase input aliases the observed capitals.

Historical point sizes identify source witnesses for one scalable design. Two-Line Pica supplies the capitals and AE ligature. The compatible Great Primer setting supplies figures, punctuation and OE; its separate calibration is retained in `calibration.json`. The smaller Pica setting remains a source witness.
