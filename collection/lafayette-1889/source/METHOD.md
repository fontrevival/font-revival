# Lafayette 1889: source and method

The historical Lafayette page is printed p. 185, PDF page 191,
Internet Archive leaf 191. The native JP2 and institutional metadata are
retained in `reference/`; `font.json` records the source and rights evidence.

`rows.json` records reviewed transcriptions and preview coordinates. Selection
requires one segmented impression per transcribed character. `selections.json`
records the chosen sorts; `tracing.json` records the final native-pixel crops,
cleanup, target heights and bearings. Larger impressions take priority; smaller
ones supply additional letters. All scaling within a traced impression is uniform. Baselines include measured
page slope.
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
python scripts/trace_specimen.py lafayette-1889 --output workspace/Lafayette1889-Regular.otf
python scripts/fontrevival.py import lafayette-1889 workspace/Lafayette1889-Regular.otf
python scripts/fontrevival.py sizecheck lafayette-1889
python scripts/fontrevival.py build lafayette-1889
```

Normal release builds use the canonical `font.ttx`, not the tracing recipe.
Inspect source comparisons, the full inventory and words at several sizes.

## Small-source reconstructions

The following original crops are retained for comparison, but their enlarged
scan outlines are replaced with explicit drawings: `x`. Each entry
in `companions.json` explains its source relationships and inferred details.
The source-comparison proof labels these as redrawn.

The uncial capital W is an observed historical form, not a lowercase alias. The
observed 24-point lowercase w preserves that double-bowl construction.
The dotted i/j are shorter than the spurred h/k/l ascenders in the large source.

## Additional specimen impressions

`KVbfw` follow the additional historical impressions listed in `font.json`.
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
