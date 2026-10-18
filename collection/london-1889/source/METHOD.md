# London 1889: source and method

The historical London page is printed p. 179, PDF page 185,
Internet Archive leaf 185. The native JP2 and institutional metadata are
retained in `reference/`; `font.json` records the source and rights evidence.

`rows.json` records reviewed transcriptions and preview coordinates. Selection
requires one segmented impression per transcribed character. `selections.json`
records the chosen sorts; `tracing.json` records the final native-pixel crops,
cleanup, target heights and bearings. Larger impressions take priority; smaller
ones supply additional letters. All scaling within a traced impression is uniform. Baselines include measured
page slope; the London 6/7 also have a local correction at the curled row end.
Differences between optical sizes remain visible. The tiny punctuation samples
are excluded; punctuation comes from explicit MIT project drawings.

Lowercase input aliases the capitals. The London capital alphabet includes
descending stems; measured baselines preserve these extensions.

`companions.json` separates inferred letters and figures from observed crops.
Each companion records its construction. Explicit font-unit paths are sufficient
to repeat preparation without working notebooks. Spacing is new digital work.
The year in the name dates the specimen rather than a claimed first issue.

Use Python 3.12, the pinned repository dependencies and Potrace 1.16:

```sh
python scripts/trace_specimen.py london-1889 --output workspace/London1889-Regular.otf
python scripts/fontrevival.py import london-1889 workspace/London1889-Regular.otf
python scripts/fontrevival.py sizecheck london-1889
python scripts/fontrevival.py build london-1889
```

Normal release builds use the canonical `font.ttx`, not the tracing recipe.
Inspect source comparisons, the full inventory and words at several sizes.

London occupies the lower half of the retained page. The Teniers specimens above
it are a separate face and do not supply letterforms for this revival.
