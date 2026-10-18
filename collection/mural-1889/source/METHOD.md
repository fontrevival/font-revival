# Mural 1889: source and method

The historical Mural page is printed p. 190, PDF page 196,
Internet Archive leaf 196. The native JP2 and institutional metadata are
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
Each companion records its construction. X and Y are reconstructed from the tiny
six-point impressions; their stroke contrast follows the larger N and I, avoiding
the disproportionately heavy result of scaling those coarse scan pixels. The
six-point zero is similarly rebuilt from the larger O at the figure width. Explicit font-unit paths are sufficient
to repeat preparation without working notebooks. Spacing is new digital work.
The year in the name dates the specimen rather than a claimed first issue.

Use Python 3.12, the pinned repository dependencies and Potrace 1.16:

```sh
python scripts/trace_specimen.py mural-1889 --output workspace/Mural1889-Regular.otf
python scripts/fontrevival.py import mural-1889 workspace/Mural1889-Regular.otf
python scripts/fontrevival.py sizecheck mural-1889
python scripts/fontrevival.py build mural-1889
```

Normal release builds use the canonical `font.ttx`, not the tracing recipe.
Inspect source comparisons, the full inventory and words at several sizes.

## Additional specimen impressions

`1247J` follow the additional historical impressions listed in `font.json`.
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
