# Baltimore Two Line Italic 1832: source and method

The alphabet is **Two Lines Minion Italic**, Baltimore 1832, unnumbered PDF page 73.
The original JP2 is retained unchanged; source URLs and rights are in `../font.json`.
`rows.json` records the visual transcription and preview coordinates;
`tracing.json` records native pixel rectangles, cleanup and metric choices.

The page is read after a 90-degree counterclockwise rotation. Each alphabet
is scaled around a 700-unit cap height, preserving relative widths and the
below-baseline Q tail. Italic component selection isolates the connected letter
and excludes fragments of neighbouring serifs in its rectangular crop.

The specimen supplies all 26 capitals, Æ and Œ. It supplies no digits for this
alphabet. `companions.json` contains explicit digital figure adaptations from
this project's observed Two Lines Brevier Roman on PDF page 73. They are sheared 0.30 to accompany the italic; these are not historical italic figures.
Punctuation is new MIT project work. Lowercase and æ/œ are capital aliases.
Word spacing and bearings are digital choices.

Prepare the master with the repository's pinned tracing/display requirements:

```sh
python collection/baltimore-two-line-italic-1832/source/select.py workspace/baltimore-two-line-italic-1832-selection
python scripts/trace_specimen.py baltimore-two-line-italic-1832 --output workspace/baltimore-two-line-italic-1832.otf
python scripts/fontrevival.py import baltimore-two-line-italic-1832 workspace/baltimore-two-line-italic-1832.otf
python scripts/fontrevival.py sizecheck baltimore-two-line-italic-1832
python scripts/fontrevival.py build baltimore-two-line-italic-1832
```

The normal build reads `source/font.ttx`. Retracing is an intentional preparation
step. Review the complete character inventory, source comparison and word proofs.
