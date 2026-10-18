# Altona 1889: source and method

The historical Altona page is printed p. 170, PDF page 176,
Internet Archive leaf 176. The native JP2 and institutional metadata are
retained in `reference/`; `font.json` records the source and rights evidence.

`rows.json` records reviewed transcriptions and preview coordinates. Selection
requires one segmented impression per transcribed character. `selections.json`
records the chosen sorts; `tracing.json` records the final native-pixel crops,
cleanup, target heights and bearings. Larger impressions take priority; smaller
ones supply additional letters. All scaling within an impression is uniform.
Differences between optical sizes remain visible. In particular, o and several
other lowercase letters supplied by the 36-point cut are wider than the 48-point
c/e. The reviewed sizing profile preserves this difference. The tiny punctuation samples
are excluded; punctuation comes from explicit MIT project drawings.

The historical lowercase is retained, including dots and descenders. The page mixes
plain and descending terminals for several capitals and lowercase letters. The
master selects one observed sort per character; it does not invent a full set of
alternates. Measured baselines keep extensions out of the body-height estimate.

`companions.json` separates inferred letters and figures from observed crops.
Each companion records its construction. Explicit font-unit paths are sufficient
to repeat preparation without working notebooks. Spacing is new digital work.
The year in the name dates the specimen rather than a claimed first issue.

Use Python 3.12, the pinned repository dependencies and Potrace 1.16:

```sh
python scripts/trace_specimen.py altona-1889 --output workspace/Altona1889-Regular.otf
python scripts/fontrevival.py import altona-1889 workspace/Altona1889-Regular.otf
python scripts/fontrevival.py sizecheck altona-1889
python scripts/fontrevival.py build altona-1889
```

Normal release builds use the canonical `font.ttx`, not the tracing recipe.
Inspect source comparisons, the full inventory and words at several sizes.
