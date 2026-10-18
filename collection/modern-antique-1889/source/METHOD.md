# Modern Antique 1889: source and method

The historical Modern Antique page is printed p. 141, PDF page 147,
Internet Archive leaf 147. The native JP2 and institutional metadata are
retained in `reference/`; `font.json` records the source and rights evidence.

`rows.json` records reviewed transcriptions and preview coordinates. Selection
requires one segmented impression per transcribed character. `selections.json`
records the chosen sorts; `tracing.json` records the final native-pixel crops,
cleanup, target heights and bearings. Larger impressions take priority; smaller
ones supply additional letters. All scaling within an impression is uniform.
Differences between optical sizes remain visible. The tiny punctuation samples
are excluded; punctuation comes from explicit MIT project drawings.

The historical lowercase is retained, including dots and descenders. Measured
baselines preserve ascenders and descenders independently of the body height.

`companions.json` separates inferred letters and figures from observed crops.
Each companion records its construction. Explicit font-unit paths are sufficient
to repeat preparation without working notebooks. Spacing is new digital work.
The year in the name dates the specimen rather than a claimed first issue.

Use Python 3.12, the pinned repository dependencies and Potrace 1.16:

```sh
python scripts/trace_specimen.py modern-antique-1889 --output workspace/ModernAntique1889-Regular.otf
python scripts/fontrevival.py import modern-antique-1889 workspace/ModernAntique1889-Regular.otf
python scripts/fontrevival.py sizecheck modern-antique-1889
python scripts/fontrevival.py build modern-antique-1889
```

Normal release builds use the canonical `font.ttx`, not the tracing recipe.
Inspect source comparisons, the full inventory and words at several sizes.

## Measurements and reconstructed companions

Ordinary cap bodies provide the scale of each row. The measured baseline and
page slope preserve the position of lowercase descenders and the Q tail. The
exact row settings and selected native crops are retained for independent review.
Differences in width and contrast between metal sizes remain visible.

The original crops for `03Qp` are retained as evidence, but their coarse
small-size outlines are replaced by explicit drawings. Each entry in
`companions.json` explains its construction. Source comparisons label these
letters and figures as redrawn. Missing letters are inferred separately.
