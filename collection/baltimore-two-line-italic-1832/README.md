# Baltimore Two Line Italic 1832

Bold sloping display capitals with fine serifs and a curled Q tail.

![Baltimore Two Line Italic 1832 specimen](specimens/preview.png)

**1832 · Regular · Version 1.000 · 108 characters · Capitals only · MIT**

[OTF](fonts/BaltimoreTwoLineItalic1832-Regular.otf) · [TTF](fonts/BaltimoreTwoLineItalic1832-Regular.ttf) · [WOFF2](web/BaltimoreTwoLineItalic1832-Regular.woff2) · [PDF specimen](specimens/specimen.pdf) · [Changes](CHANGELOG.md)

## Use

Install either desktop format. For websites, copy `web/`, include `font.css`,
and use `font-family: "Baltimore Two Line Italic 1832"`. Designed for display sizes.

## Design

**Designer:** Unidentified in the historical specimen

**Foundry:** Baltimore Type Foundry; F. Lucas, Jr., agent

**Observed:** Observed capitals ABCDEFGHIJKLMNOPQRSTUVWXYZÆŒ from Two Lines Minion Italic, one-based PDF page 73 of the unpaginated 1832 volume.

**Reconstructed:** Figures are companion adaptations of the observed Two Lines Brevier Roman figures on PDF page 73; sheared to accompany the italic capitals. Punctuation and other symbols are explicit new MIT project drawings. Lowercase input aliases capitals. Digital spacing is new. No lowercase or figures are claimed to be printed in this alphabet.

## Sources

1. [A specimen of printing types and ornaments from the Baltimore Type Foundry (1832), Two Lines Minion Italic; unnumbered leaf, PDF page 73, Internet Archive leaf 72](https://archive.org/details/ldpd_12198261_000/page/n72/mode/1up) — 1832 US publication, public domain by age. Columbia University Libraries scan; the DPLA catalogue records Public domain. Exact native JP2 and institutional evidence retained locally. [Rights basis](https://dp.la/item/c773fb687c8cc1c610a04becf6baf8e2).

Source images are in `reference/`; the source record is [font.json](font.json).
Historical reference material retains the rights status recorded there.
Copyright (c) 2026 Harold Lehmann. The digital revival is released under the included [MIT License](LICENSE).

## Build or improve

From the repository root:

```sh
python scripts/fontrevival.py build baltimore-two-line-italic-1832
python scripts/fontrevival.py check baltimore-two-line-italic-1832
```

Edit `source/font.ttx` or export an individual glyph with
`python scripts/fontrevival.py glyph baltimore-two-line-italic-1832 j`.
Follow the shared [revival workflow](../../docs/WORKFLOW.md) for additions and revisions.
