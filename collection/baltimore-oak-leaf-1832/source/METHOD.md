# Baltimore Oak Leaf 1832: complete sheet

All 26 capitals, the ampersand, period, comma and exclamation are traced from
`reference/oak-leaf-complete.png`, the complete alphabet hosted by Luc Devroye.
The retained PNG is unchanged. `complete-sheet-acquisition.json` records its
URL, hash and dimensions. Its filename attributes Oak Leaf to Baltimore, 1832;
the intermediate publication and page remain unidentified. This attribution is
the working basis for the complete-sheet revival.

The Baltimore 1832 PRINT LUCAS page and Boston 1832 MINT! GOLD. page remain as
historical context. The R on the complete sheet has a different leafy lower leg
from the Baltimore PRINT impression. This font follows the complete sheet's R
and its other letters consistently; Baltimore Initials preserves both R forms as separate impressions.

## Drawing and coverage

`tracing.json` records exact native-pixel crops, a threshold of 160, 0.25-pixel
blur, a two-pixel minimum ink component and no filled holes. Potrace 1.16 fits
cubic curves at tolerance 0.15. Disconnected engraved details are retained.
Each glyph is uniformly fitted with 40-unit sidebearings; capitals have a
700-unit total ink height. Q retains its tail below the baseline. Period and
comma are fitted to their relative size on the sheet; comma descends.

There are no inferred visible characters. A-Z, & . , ! and blank spaces are
encoded. Lowercase keys alias the capitals. Figures and unsupported punctuation
are omitted. The explicit `character_set` in font.json lets validation enforce
this exact coverage, rather than filling gaps with invented drawings.

`companions.json` contains only the blank word space and aliases. The canonical
master is `font.ttx`; ordinary builds need no tracing tool. To retrace and import:

```sh
python scripts/trace_specimen.py baltimore-oak-leaf-1832 \
  --output workspace/BaltimoreOakLeaf1832-Regular.otf --potrace /path/to/potrace
python scripts/fontrevival.py import baltimore-oak-leaf-1832 \
  workspace/BaltimoreOakLeaf1832-Regular.otf --replace
python scripts/fontrevival.py sizecheck baltimore-oak-leaf-1832
python scripts/fontrevival.py build baltimore-oak-leaf-1832
```

Original digital work is Copyright (c) 2026 Harold Lehmann, MIT licensed.
Historical source status and attribution are recorded separately in font.json.
