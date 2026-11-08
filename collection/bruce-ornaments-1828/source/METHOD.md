# Source and method

The 45 dash designs come from the **Ornamental Dashes** section of George Bruce’s
1828 specimen, PDF pages 169, 171, 173 and 175. The leaves are unnumbered;
`printed_page` is null. The Internet Archive copy uses zero-based leaves
168, 170, 172 and 174 for the corresponding pages.

The New York Public Library copy digitized by Google is distributed through
[HathiTrust](https://hdl.handle.net/2027/nyp.33433006349736). The complete PDF
was obtained from the [Circuitous Root mirror](https://circuitousroot.com/images/artifice/letters/press/noncomptype/typography/bruce/bruce-1828-specimen-hathi-nyp-33433006349736.pdf).
`reference/acquisition.json` identifies the container and native page images
by SHA256. `pdfimages -png` extracts the embedded pixels without upsampling.
Full native pages remain in `reference/`; this is historical printed artwork,
not a modern font or modern redrawing.

## Design identity

The inventory accounts for 93 specimen impressions: 91 single designs and two
compositions containing three separately movable pieces each. Of the 97 atomic
records, 45 supply this family, eight repeat those new designs and 44 refer to
existing Baltimore or Boston artwork. The clipped long-horn fragment remains
partial source evidence. References preserve existing IDs and codepoints.

Historical size names identify source settings. They do not automatically create
separate digital icons. Geometrically equivalent impressions share one selected
source; minor coil-length differences remain recorded witnesses. Different
centres, end pieces and solid or shaded treatments are retained when the printed
construction is distinct. The lion-mask scroll differs from Baltimore’s related
human-mask scroll. The round grinning mask differs from the bearded mask and
the later Boston jester face. A horizontally mirrored long cornucopia refers to
the existing Boston drawing with its orientation recorded.

The shaded graduated coil retains the canonical ID first assigned from Long
Primer No. 12. Its outline uses the clearer Brevier No. 8 impression, whose
interior highlights survive more fully. The manifest cites the actual supplying
page and setting; the stable ID is an identifier rather than a current citation.

## Extraction

`crops.json` records native rectangles after the page quarter-turn, explicit
removal of neighbouring marks and rigid deskew angles. Most corrections use the
median ink centres at the two ends of a horizontal divider. The grinning mask
uses a 2.8-degree clockwise correction of the nearby heading’s page tilt.
The optional `prepare_crops.py` reproduces these images and checks their hashes.
No crop is stretched, symmetrized or reconstructed from an unrelated design.

For dashes, `tracing.json` records monochrome tracing at threshold 135, a 0.4-pixel blur,
an eight-pixel minimum isolated component and no hole filling. Small enclosed
white details and disconnected ornament pieces are preserved. Potrace 1.16 fits
cubic contours with tolerance 0.15; fontTools rounds to the font-unit grid.
The monochrome scan does not support a meaningful three-ink interpretation.
For thin dividers, recorded erasure rectangles also remove isolated scan specks
entirely outside the principal horizontal ink band. They preserve every observed
piece within the ornament, including its small beads and arrowheads.

Each icon retains its proportions, fits within a maximum 1800-unit ink dimension
and is centred vertically in a 2048-unit em with 64-unit side bearings.
Names, search tags, Private Use assignments and digital metrics are modern
project work. No pictorial elements have been invented. Fine engraving details
lost in the historical scan remain limits of the source.

The optional preparation command is:

```sh
python scripts/trace_specimen.py bruce-ornaments-1828 --output workspace/BruceOrnaments1828-Regular.otf
```

Normal release builds use the canonical CFF XML master, `font.ttx`.


## Flowers and Borders

One hundred and fifty-three border repeats, corners and floral motifs come from
unnumbered PDF pages 177–235. `border-inventory.json` accounts for all 309 printed
settings, including 95 settings repeated on seven later pages. The 254 component
reviews resolve to 153 distinct drawings, 84 references to existing artwork,
15 repeated components, one composed corner using an identified floral tile,
and one obscured flower awaiting a clearer source. Seven ordinary rule settings
are retained as provenance without additional icons. Historical size headings
are not separate digital products.

`border-crops.json` records native rectangles and 123 measured quadrilaterals.
The latter follow tilted type-block edges; bilinear rectification uses the mean
length of each pair of opposing edges for the output dimensions. It removes
scan skew without forcing flowers into circles or changing their measured aspect.
The five small grayscale crops from PDF235 use fourfold working interpolation
so the curve fit can preserve their thin strokes. This adds no source detail;
the native page, quadrilateral, working scale and output dimensions remain recorded.
Complete repeat intervals were measured against the native runs and inspected
in joined proofs. The trefoil corner retains its printed double-border
arrangement, including the inward return.

The less compressed Hathi images retain clearer contours than the archive JP2
representation in the reviewed examples. Border tracing uses a 0.4-pixel blur,
no hole filling and cubic fitting tolerance 0.15. Recorded thresholds of 135,
110 or 85 follow bounded source comparisons. Reduced corner smoothing retains
straight geometric edges in the recipes that declare it. Six pixels is the usual minimum
isolated component area; the diagonal fan corner, ringed terminal and oval
flower instead retain their explicitly counted connected pieces. The terminal
preserves both its outer block and central disk. Separate neighbouring fragments
and scan specks are excluded only where recorded by the tracing recipe.

Fine hatching already closed or indistinct in the scan remains a source
limitation. The small round and lozenge flowers on PDF199 are filled in both
available scan representations; their obscured details are not reconstructed.
A later clearer impression can replace these drawings under the same IDs.
The flower used as Great Primer No. 1 and as an end on PDF205 is too
obscured to identify confidently; it has no additional digital drawing.
A curled flower cross and a pierced square terminal recur turned 45 degrees;
these settings reference their existing drawings. The separate star at the left
end of Small Pica No. 2 on PDF213 supplies its complete tips; the No. 1 row
joins those tips with diagonal rules. Mirrored leaf repeats also appear turned
90 degrees. These arrangements retain their component links. The isolated flower at the
left of Pearl No. 1 on PDF235 supplies the complete flower repeated in No. 7.
The small concave diamond retains both the black surround and central disk.
The repeated pages 219–231 preserve the same fine defects and filled interiors
as pages 205–217 and provide no additional engraved detail.

`prepare_border_crops.py` reproduces the reading images and verifies their
hashes. `prepare_borders.py` optionally retraces only the border entries and
retains every earlier dash outline and metric from the canonical master:

```sh
python collection/bruce-ornaments-1828/source/prepare_border_crops.py
python collection/bruce-ornaments-1828/source/prepare_borders.py --output workspace/BruceOrnaments1828-Regular.otf
```

Selected matching Bruce1828 impressions improve engraving detail. The exact native crop rectangles, previous and selected witnesses, thresholds and reasons are retained in bruce1828-quality-revisions.json. The glyph overrides preserve each stable ID, codepoint and advance, including all tone regions where applicable. Previous sources remain in reference/. No absent content is reconstructed.
