# Epitaph 1889: source and method

The historical Epitaph page is printed p. 172, PDF page 178,
Internet Archive leaf 178. Retain the native JP2 and institutional metadata;
`font.json` records the source and public-domain evidence.

`rows.json` records visually inspected transcriptions and preview coordinates.
The final `tracing.json` records native-pixel crop rectangles, thresholds,
cleanup, target heights and bearings. Larger impressions have priority; smaller
ones provide missing sorts. Scaling is uniform within each row, retaining
observed proportions. The Q tail is measured below its neighbours' baseline.
Point-size-specific features are not interpreted as a complete alternate set.

`companions.json` separates all inferred and newly drawn glyphs from the crops.
Its explicit font-unit paths are sufficient to repeat preparation without the
working notebooks. Lowercase aliases the capitals. Spacing is new digital work.
The year in the name dates the specimen rather than a claimed first issue.

Use Python 3.12, the pinned repository dependencies and Potrace 1.16:

```sh
python scripts/trace_specimen.py epitaph-1889 --output workspace/Epitaph1889-Regular.otf
python scripts/fontrevival.py import epitaph-1889 workspace/Epitaph1889-Regular.otf
python scripts/fontrevival.py sizecheck epitaph-1889
python scripts/fontrevival.py build epitaph-1889
```

Normal release builds use the canonical `font.ttx`, not this tracing recipe.
Inspect the source comparison, full inventory and words at several sizes.

Optional selection review uses `requirements-display.txt` and the local `select.py` wrapper. It writes candidate crops to a working directory only; inspect them before changing the final tracing recipe. The committed native crops and explicit companion paths remain sufficient for preparation.

## Additional specimen impressions

`016JX` follow the additional historical impressions listed in `font.json`.
Their native crops, row transcriptions, cap-body scale anchors, baseline positions
and cleanup are recorded in `tracing.json`. Each crop uses a uniform scale;
small optical-size differences remain visible. These forms replace companion
drawings or coarser traces. The corresponding entries are removed from
`companions.json`; editable final paths are in `glyphs/`. Normal builds apply
those paths over `font.ttx`.

Digital advances are retained except where the source-proportioned outline
needs additional sidebearings, as recorded per glyph. Compare the retained
source crops with `../specimens/source-review.pdf` and the revision with
`../specimens/specimen-restoration-review.pdf`.
