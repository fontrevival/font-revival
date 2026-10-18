# Boston Cuts 1832

The source is *Specimen of printing types from the Boston Type & Stereotype
Foundry* (1832), John G. Rogers, agent, printed by Samuel N. Dickinson. The
Library of Congress scan is distributed as Internet Archive item
`specimenofprinti00bost`. Its retained metadata states that the Library is unaware
of any copyright restrictions. The 1832 US publication is public domain by age;
the MIT license covers original project work.

## Source coverage

The inventory covers newspaper ornaments on PDF page 199 and every numbered cut
on PDF pages 201–391. These leaves have no printed folios. One-based PDF page and
Internet Archive leaf numbers coincide in this range; `reference/scandata.xml`
records the original leaf map. Native JP2 files and lossless grayscale PNG
conversions retain the page orientation and resolution. Acquisition records
identify their archive members, dimensions and SHA256 hashes.

`inventory.json` records 757 individual impressions: 391 distinct additions,
364 references to existing collection items and two repeated impressions of
new artwork. The existing families retain their original files, names,
codepoints and drawings. A shared design is referenced even when the books use
different catalogue numbers. Differences in impression strength alone do not
create another icon; distinct compositions, engraving variants and integrated
lettering remain distinguishable designs.

The main numbering reaches 606. Nos. 81, 135, 539 and 544 are absent from their
printed sequences. An unnumbered steamboat and large tree frame occupy the
vicinity of Nos. 95 and 481; their identifiers describe the observed source
without inventing printed numbers. No. 128 contains 25 Primer panels, all
already represented by Baltimore No. 357. No. 450 contains 12 almanac panels;
No. 500 contains 83 separate Primer pictures across three pages. Separate
members of other small sets have letter suffixes. Connected compositions remain
whole illustrations. Initial alphabets and earlier border specimens are outside
this numbered-cut inventory.

## Tracing

`tracing.json` records native pixel crops, counterclockwise quarter turns and
explicit erasure rectangles. Erasures remove separate catalogue/sample type or
detached fragments from adjacent items. Lettering belonging to an illustration
and observed engraver signatures remain. No missing letter, illustration detail
or border segment is drawn. A few source impressions meet the historical scan
edge; the inventory identifies those limitations.

Direct grayscale thresholds 105, 135 and 155 separate observed ink strengths.
No. 438 uses 145 for its lightest band to exclude the shaded page gutter.
The middle threshold supplies the monochrome drawing. The darker paper in this
scan requires lower thresholds than the Baltimore volume. Local paper
normalization is disabled to preserve broad solid strokes. A 0.3-pixel blur and
minimum component area of three native pixels suppress isolated scan noise;
no holes are filled. Potrace 1.16 fits cubic curves at tolerance 0.15.

All three tones use `native-mask-bands`: nested masks are separated at the native
scan resolution before curve fitting. This avoids expensive whole-outline
boolean operations on dense engravings. Each fitted region shares the same
coordinate frame. The default opacities 1, 0.55 and 0.25 interpret scan strength;
they are not evidence of three printing inks. Artwork contains vector contours,
not an embedded bitmap.

Each impression scales uniformly into an 1800-unit maximum dimension in a
2048-unit em, with 64-unit sidebearings and vertical centring. Aspect ratios
remain historical. Private Use assignments are permanent and local to this
family. A blank quarter-em space is the only newly constructed character.

## Reproduction and delivery

Normal releases use `font.ttx` and the standard `source/glyphs/` overrides.
Install the repository requirements, this directory's optional requirements,
and Potrace 1.16 for intentional retracing. From the repository root:

```sh
python collection/boston-cuts-1832/source/prepare.py boston-cuts-1832 \
  --output workspace/BostonCuts1832-Regular.otf --potrace /path/to/potrace \
  --jobs 1 --cache workspace/boston-1832-trace-cache
python collection/baltimore-cuts-1832/source/prepare_truetype.py boston-cuts-1832 \
  workspace/BostonCuts1832-Regular.otf --potrace /path/to/potrace
python collection/boston-cuts-1832/source/stage_master.py \
  workspace/BostonCuts1832-Regular.otf workspace/boston-1832-baseline.otf
python scripts/fontrevival.py import boston-cuts-1832 \
  workspace/boston-1832-baseline.otf --binary-charstrings
python collection/baltimore-cuts-1832/source/review_sizing.py boston-cuts-1832 \
  workspace/BostonCuts1832-Regular.otf
python scripts/fontrevival.py sizecheck boston-cuts-1832
python scripts/fontrevival.py build boston-cuts-1832
python scripts/fontrevival.py check boston-cuts-1832
```

The shared preparation helpers accept the family argument and read this family's
own recipes. They do not modify the Baltimore family. Importing an existing
master requires an intentional `--replace` operation.
Preparation retains fitted commands directly, without the optional operator
optimizer. The prepared OTF contains every complete monochrome cut and named
empty slots for private tones; its companion `.layers` directory retains all
1173 full-detail tonal paths. Staging places those exact paths in the standard
glyph overrides. This avoids constructing enormous unused CFF operand arrays
for all tones simultaneously. The contours, coordinates and shared frames are
unchanged. Native trace caches use source, recipe, layer and tool signatures;
verified cached tone paths can be staged through the same representation.

Seventy-nine monochrome drawings receive documented downloadable-font
approximations because their contour or control-point counts exceed renderer
limits. Nos. 427, 487–489, 501, 555, 575, 579 and 596, and the unnumbered tree
frame, use the shared `coverage-screen` method to retain their apparent shading
at display sizes. Its fine diagonal screening is a modern font-format
interpretation, not historical engraved linework. The other 312 encoded cuts
retain their full traced outlines in every font. Their JSON files retain the original
outline hash, unchanged advance, point counts, preparation settings and measured
bounds allowance. Full-detail canonical artwork remains in the master and glyph
overrides, and is delivered as SVG and tonal PNG. Desktop and webfonts contain
only encoded monochrome drawings and space. CFF programs are split losslessly
into subroutines below 60,000 bytes for browser compatibility. The comparison
proofs show source crops, full-detail artwork and font drawings at display sizes.

SVG sprites and web bundles are divided into manageable parts. Source previews
in the PDF use bounded JPEG images; native reference PNGs remain lossless and
vector artwork retains its complete contours. `sizing.json` records reviewed
source proportions and any bounds allowance for font approximations.
