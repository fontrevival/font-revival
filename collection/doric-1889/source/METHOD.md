# Doric 1889: source and method

The historical Doric page is printed p. 138, PDF page 144,
Internet Archive leaf 144. The native JP2 and institutional metadata are
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
python scripts/trace_specimen.py doric-1889 --output workspace/Doric1889-Regular.otf
python scripts/fontrevival.py import doric-1889 workspace/Doric1889-Regular.otf
python scripts/fontrevival.py sizecheck doric-1889
python scripts/fontrevival.py build doric-1889
```

Normal release builds use the canonical `font.ttx`, not the tracing recipe.
Inspect source comparisons, the full inventory and words at several sizes.

## Measurements and reconstructed companions

Ordinary cap bodies provide the scale of each row. The measured baseline and
page slope preserve the position of lowercase descenders and the Q tail. The
exact row settings and selected native crops are retained for independent review.
Differences in width and contrast between metal sizes remain visible.

The original crops for `PW` are retained as evidence, but their coarse
small-size outlines are replaced by explicit drawings. Each entry in
`companions.json` explains its construction. Source comparisons label these
letters and figures as redrawn. Missing letters are inferred separately.

The figure 1 has closed ink-break pinholes in its stem. The tracing recipe fills
those small regions; the source sort has no intentional counter there. The observed GPO 48-point g has a double-storey construction, a flat lower
terminal and an ear just above the main lowercase body.

## Additional specimen impressions

`JKbfgj` follow the additional historical impressions listed in `font.json`.
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
