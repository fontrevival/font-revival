# Facade 1889: source and method

The historical Facade page is printed p. 191, PDF page 197,
Internet Archive leaf 197. The native JP2 and institutional metadata are
retained in `reference/`; `font.json` records the source and rights evidence.

`rows.json` records reviewed transcriptions and preview coordinates. Selection
requires one segmented impression per transcribed character. `selections.json`
records the chosen sorts; `tracing.json` records the final native-pixel crops,
cleanup, target heights and bearings. Larger impressions take priority; smaller
ones supply additional letters. All scaling within an impression is uniform.
Differences between optical sizes remain visible. The tiny punctuation samples
are excluded; punctuation comes from explicit MIT project drawings.

Lowercase input aliases the capitals; the consulted page supplies capitals only.

`companions.json` separates inferred letters and figures from observed crops.
Each companion records its construction. K is reconstructed from its tiny
impression; the observed larger I establishes the stem and terminal weight. Explicit font-unit paths are sufficient
to repeat preparation without working notebooks. Spacing is new digital work.
The year in the name dates the specimen rather than a claimed first issue.

Use Python 3.12, the pinned repository dependencies and Potrace 1.16:

```sh
python scripts/trace_specimen.py facade-1889 --output workspace/Facade1889-Regular.otf
python scripts/fontrevival.py import facade-1889 workspace/Facade1889-Regular.otf
python scripts/fontrevival.py sizecheck facade-1889
python scripts/fontrevival.py build facade-1889
```

Normal release builds use the canonical `font.ttx`, not the tracing recipe.
Inspect source comparisons, the full inventory and words at several sizes.
