# Baltimore Black Slope 1832: source and method

The source is **English Black Slope**, unnumbered PDF page 81 (Internet Archive
leaf 80). It is a Roman with a backslant, not a blackletter. The title, observed
letters and public-domain evidence are recorded in `../font.json`.

`rows.json` records inspected words and the complete printed capital/figure rows.
The connected components are grouped explicitly for the separated M stem and
for i/j dots. Bounding rectangles may include neighbouring serif fragments;
the tracing recipe retains only the reviewed number of principal components.
Linear baselines fitted to the bottoms of non-descending letters compensate
for the tilted scan, without removing the historical backslant. Capitals use
700 font units; the measured lowercase x-height is about 460. Relative widths,
ascenders and descenders are retained. Advances follow the next observed ink
origin in each reviewed word/alphabet row; this permits the bounding boxes of
backslanted neighbours to overlap as they do in print. Last sorts and new
companions receive explicit digital bearings. `features.fea` adds positive kern
adjustments where changed neighbours would collide. `review_spacing.py` retains
the measurement method; its output is a candidate for visual review, not a
normal build step. These are new digital adjustments, not historical kerning.

The Baltimore source supplies capitals A–X, lining figures, $, æ and all lowercase
except k/w/y/z. Boston's 1832 English Back Slope supplies Y/Z/k/w/y/z, completing
the observed alphabet. The matching Latin passage, backslant, capital curls and
figure forms establish the connection between these differently titled showings. Punctuation is new MIT project work. Each drawing
and its rationale is explicit in `companions.json`. No capital aliases substitute
for the lowercase.

Use the pinned tracing/display requirements and Potrace 1.16:

```sh
python collection/baltimore-black-slope-1832/source/select.py workspace/black-slope-selection
python scripts/trace_specimen.py baltimore-black-slope-1832 --output workspace/black-slope.otf
python scripts/fontrevival.py import baltimore-black-slope-1832 workspace/black-slope.otf
python scripts/fontrevival.py sizecheck baltimore-black-slope-1832
python scripts/fontrevival.py build baltimore-black-slope-1832
```

Normal builds use `font.ttx`. Inspect the source comparison, lowercase words,
complete character inventory and gallery when revising these forms.

## Additional specimen impressions

`YZkwyz` follow the additional historical impressions listed in `font.json`.
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
