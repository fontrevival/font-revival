# Baltimore Initials 1832

Historical decorated initials from Baltimore 1832, with matching impressions from Boston 1832, Howe 1830 and Bruce 1828, plus the leafy-descender Oak Leaf R from the complete alphabet sheet.

![Historical scan beside the vector revival](specimens/preview.png)

**66 icon(s) · Version 1.002 · MIT**

[SVG files](svg/) · [SVG sprite](web/icons.svg) · [OTF](fonts/BaltimoreInitials1832-Regular.otf) · [TTF](fonts/BaltimoreInitials1832-Regular.ttf) · [WOFF2](web/BaltimoreInitials1832-Regular.woff2) · [Comparison and size proof](specimens/specimen.pdf) · [Icon manifest](icons.json) · [Changes](CHANGELOG.md)

[Three-tone SVGs](svg/multitone/) · [Three-tone sprite](web/icons-multitone.svg) · [Transparent three-tone PNGs](png/multitone/)

## Use in HTML

[Download the web bundle (ZIP)](downloads/baltimore-initials-1832-web.zip), unzip it, and place
the extracted `collection` folder beside your HTML file. Keep its subfolders
together. The examples below then work as written; adjust the paths if you move
the folder elsewhere. The bundle contains SVGs, PNGs, fonts, CSS, instructions
and the license. No JavaScript or font installation is needed for SVG use.

### Three-tone image — works from disk too

The individual SVG displays all three tones at their default strengths, with a
transparent background. Change `height` to resize it; the proportions are retained.

```html
<img src="collection/baltimore-initials-1832/svg/multitone/baltimore-1832-p59-six-line-pica-ornamented-m.svg"
     alt="Six Line Pica Ornamented letter M" height="96">
```

An `<img>` has its own colour context: page CSS cannot recolour its internal
regions. For a decorative image beside a text label, use `alt=""` instead.

### Three-tone sprite — customise every tone

Copy `web/icons-multitone.svg` and use the following complete example on an
HTTP(S) page served from the same origin as the sprite. It draws dark primary ink
and two strengths of red. Each colour and opacity can be changed independently.

```html
<style>
  .revival-cut {
    display: inline-block;
    font-size: 96px;
    height: 1em;
    width: 0.941406em;
    vertical-align: middle;
    --fr-primary-color: #24251f;
    --fr-secondary-color: #a5422c;
    --fr-tertiary-color: #a5422c;
    --fr-primary-opacity: 1;
    --fr-secondary-opacity: 0.55;
    --fr-tertiary-opacity: 0.25;
  }
</style>
<svg class="revival-cut" role="img" aria-label="Six Line Pica Ornamented letter M">
  <use href="collection/baltimore-initials-1832/web/icons-multitone.svg#baltimore-1832-p59-six-line-pica-ornamented-m"></use>
</svg>
```

Use the same secondary and tertiary colour and opacity for a two-tone appearance.
The defaults are primary 100%, secondary 55% and tertiary 25%; these are separate
vector regions, not a gradient. The tone assignments interpret the historical
impression. A transparent PNG of the default tones is also provided.

External SVG sprites can be blocked on `file://` pages. To customise tones on a
page opened from disk, open the individual SVG in a text editor, copy its complete
`<svg>…</svg>` markup into your HTML, and add `class="revival-cut"` to that SVG.
The same CSS above then applies to its inline paths. Keep its `viewBox` and paths.
The gallery itself uses inline SVG so its previews work directly from disk.

### Monochrome icon font

Copy the whole `web/` folder, including CSS and webfonts. Standard icon fonts show
the solid artwork; use the SVG examples above for three-tone artwork.

```html
<link rel="stylesheet" href="collection/baltimore-initials-1832/web/icons.css">
<span class="fr-icon fr-baltimore-1832-p59-six-line-pica-ornamented-m" aria-hidden="true"
      style="font-size:96px;color:#a5422c"></span>
<span>Six Line Pica Ornamented letter M</span>
```

The example hides a decorative icon from screen readers and supplies visible
text. For an icon that conveys meaning on its own, use `role="img"` and an
`aria-label` instead of `aria-hidden`. Font size and colour use ordinary CSS.

Install the OTF or TTF for desktop use. The manifest lists each icon's Private Use
codepoint and recommended minimum display size. These codepoints are not ordinary
text characters; IDs and codepoints are permanent within this collection.
The example above uses U+E000 and is recommended from
64 px. The 16–192 pt proofs show how detail holds up at different sizes.
Keep the included LICENSE with redistributed assets.

## Evidence and editing

**Foundry:** Baltimore Type Foundry; F. Lucas, Jr., agent

**Designer:** Baltimore Type Foundry; individual engravers generally unidentified (signed large cuts credited in the source inventory)

**Observed:** 38 original Baltimore impressions plus 27 matching period impressions (21 letters and six punctuation marks), and the complete-sheet Oak Leaf R: 66 items. Both R forms are retained separately. All letters and punctuation of the Boston MINT! GOLD. specimen are included, alongside the original Baltimore PRINT LUCAS letters. Every item has an exact scan crop and source citation; the standalone sheet uses an explicit location instead of a PDF page.

**Interpreted or new:** No inferred letters or new pictorial content. Thresholding, crop cleanup, cubic curve fitting and font-unit rounding interpret the observed impressions. Source identifiers, Private Use assignments, uniform scale and bearings are digital metadata and metrics. Original 38 items retain their existing monochrome and three-tone drawings, including reviewed 1.001 alignment. The 28 supplementary impressions are monochrome.

- [A specimen of printing types and ornaments from the Baltimore Type Foundry (1832), unnumbered leaf; PDF page 59, Internet Archive leaf 58](https://archive.org/details/ldpd_12198261_000/page/n58/mode/1up) — 1832 US publication, public domain by age; Columbia University Libraries historical scan, distributed through Internet Archive. DPLA item c773fb687c8cc1c610a04becf6baf8e2 records Public domain. No modern digital font or redrawing was used. The MIT license applies to original project work, not ownership of the historical design. [Rights basis](https://dp.la/item/c773fb687c8cc1c610a04becf6baf8e2).
- [A specimen of printing types and ornaments from the Baltimore Type Foundry (1832), unnumbered leaf; PDF page 65, Internet Archive leaf 64](https://archive.org/details/ldpd_12198261_000/page/n64/mode/1up) — 1832 US publication, public domain by age; Columbia University Libraries historical scan, distributed through Internet Archive. DPLA item c773fb687c8cc1c610a04becf6baf8e2 records Public domain. No modern digital font or redrawing was used. The MIT license applies to original project work, not ownership of the historical design. [Rights basis](https://dp.la/item/c773fb687c8cc1c610a04becf6baf8e2).
- [A specimen of printing types and ornaments from the Baltimore Type Foundry (1832), unnumbered leaf; PDF page 67, Internet Archive leaf 66](https://archive.org/details/ldpd_12198261_000/page/n66/mode/1up) — 1832 US publication, public domain by age; Columbia University Libraries historical scan, distributed through Internet Archive. DPLA item c773fb687c8cc1c610a04becf6baf8e2 records Public domain. No modern digital font or redrawing was used. The MIT license applies to original project work, not ownership of the historical design. [Rights basis](https://dp.la/item/c773fb687c8cc1c610a04becf6baf8e2).
- [A specimen of printing types and ornaments from the Baltimore Type Foundry (1832), unnumbered leaf; PDF page 69, Internet Archive leaf 68](https://archive.org/details/ldpd_12198261_000/page/n68/mode/1up) — 1832 US publication, public domain by age; Columbia University Libraries historical scan, distributed through Internet Archive. DPLA item c773fb687c8cc1c610a04becf6baf8e2 records Public domain. No modern digital font or redrawing was used. The MIT license applies to original project work, not ownership of the historical design. [Rights basis](https://dp.la/item/c773fb687c8cc1c610a04becf6baf8e2).
- [Specimen of printing types from the Boston Type & Stereotype Foundry (1832), unpaginated; PDF page 133, archive leaf 133](https://archive.org/details/specimenofprinti00bost/page/n133/mode/1up) — 1832 US publication, public domain by age. Library of Congress scan; the retained archive record states that the Library is unaware of copyright restrictions. [Rights basis](https://archive.org/details/specimenofprinti00bost).
- [Specimen of printing types and ornaments, J. Howe & Co. (1830), unpaginated; PDF page 133, archive leaf 133](https://archive.org/details/specimenofprinti00jhow/page/n133/mode/1up) — 1830 US publication, public domain by age. Library of Congress scan; the retained archive record states that the Library is unaware of copyright restrictions. [Rights basis](https://archive.org/details/specimenofprinti00jhow).
- [Specimen of printing types from the Boston Type & Stereotype Foundry (1832), unpaginated; PDF page 145, archive leaf 145](https://archive.org/details/specimenofprinti00bost/page/n145/mode/1up) — 1832 US publication, public domain by age. Library of Congress scan; the retained archive record states that the Library is unaware of copyright restrictions. [Rights basis](https://archive.org/details/specimenofprinti00bost).
- [A specimen of printing types, and ornaments cast in the letterfoundry of George Bruce (1828), unpaginated; PDF page 137, archive leaf 136](https://archive.org/details/bub_gb_C41QAAAAYAAJ/page/n136/mode/1up) — 1828 US publication; Internet Archive marks this Google Books scan Public Domain Mark 1.0. The archive contributor field does not identify the holding library. [Rights basis](https://archive.org/details/bub_gb_C41QAAAAYAAJ).
- [Specimen of printing types from the Boston Type & Stereotype Foundry (1832), unpaginated; PDF page 139, archive leaf 139](https://archive.org/details/specimenofprinti00bost/page/n139/mode/1up) — 1832 US publication, public domain by age. Library of Congress scan; the retained archive record states that the Library is unaware of copyright restrictions. [Rights basis](https://archive.org/details/specimenofprinti00bost).
- [Specimen of printing types from the Boston Type & Stereotype Foundry (1832), unpaginated; PDF page 141, archive leaf 141](https://archive.org/details/specimenofprinti00bost/page/n141/mode/1up) — 1832 US publication, public domain by age. Library of Congress scan; the retained archive record states that the Library is unaware of copyright restrictions. [Rights basis](https://archive.org/details/specimenofprinti00bost).
- [Oak Leaf complete alphabet sheet, hosted by Luc Devroye; attributed to Baltimore Type Foundry, 1832](https://luc.devroye.org/BaltimoreTypeFoundry--OakLeaf-1832.png) — The underlying Oak Leaf design is documented in the 1832 Baltimore specimen and is public domain by age. The complete reproduction is hosted by Luc Devroye; its intermediate publication and reproduction history are unidentified. The attribution is the working basis for this revival. The project MIT license covers original digital work and does not assert ownership of the reference sheet. [Rights basis](https://archive.org/details/ldpd_12198261_000/page/n66/mode/1up).

Copyright (c) 2026 Harold Lehmann. Historical public-domain material retains its status.
Read [the method](source/METHOD.md), [inventory](source/inventory.json) and
[icon workflow](../../docs/ICONS.md). The canonical master is `source/font.ttx`;
SVGs, sprite, fonts and manifests are generated from it with glyph edits applied.

```sh
python scripts/fontrevival.py build baltimore-initials-1832
python scripts/fontrevival.py sizecheck baltimore-initials-1832
python scripts/fontrevival.py check baltimore-initials-1832
python scripts/fontrevival.py glyph baltimore-initials-1832 uniE000
```
