# Caslon Compressed 1841

Narrow Roman capitals with fine hairlines, flat serifs and a recurved Q tail.

![Caslon Compressed 1841 specimen](specimens/preview.png)

**1841 · Regular · Version 1.000 · 77 characters · Capitals only · MIT or SIL OFL 1.1**

[OTF](fonts/CaslonCompressed1841-Regular.otf) · [TTF](fonts/CaslonCompressed1841-Regular.ttf) · [WOFF2](web/CaslonCompressed1841-Regular.woff2) · [PDF specimen](specimens/specimen.pdf) · [Changes](CHANGELOG.md)

## Use

Install either desktop format. For websites, copy `web/`, include `font.css`,
and use `font-family: "Caslon Compressed 1841"`. Designed for display sizes.

## Design

**Designer:** Unidentified in the historical specimen

**Foundry:** Henry Caslon, London

**Observed:** Complete capitals from Two-Line Pica; compatible Great Primer supplies figures, punctuation and OE ligature.

**Reconstructed:** No inferred visible characters. Spaces and digital spacing are new; lowercase input aliases the corresponding capitals.

## Sources

1. [Specimen of printing types, Henry Caslon (1841), archive leaf 13, PDF page 14](https://archive.org/details/bub_gb_LVsJAAAAQAAJ/page/n13/mode/1up) — 1841 British publication, public domain by age. Internet Archive metadata supplies Public Domain Mark 1.0; historical scan retained. [Rights basis](https://archive.org/details/bub_gb_LVsJAAAAQAAJ).

Source images are in `reference/`; the source record is [font.json](font.json).
Historical reference material retains the rights status recorded there.
Copyright (c) 2026 Harold Lehmann. The fonts and editable font source data are available under your choice of the [MIT License](LICENSE) or [SIL Open Font License 1.1](OFL.txt) (`MIT OR OFL-1.1`), with no Reserved Font Names. See [font licensing](FONT-LICENSES.txt) for the scope and notices. Other original project files, including standalone artwork, code and documentation, use MIT.

## Build or improve

From the repository root:

```sh
python scripts/fontrevival.py build caslon-compressed-1841
python scripts/fontrevival.py check caslon-compressed-1841
```

Edit `source/font.ttx` or export an individual glyph with
`python scripts/fontrevival.py glyph caslon-compressed-1841 j`.
Follow the shared [revival workflow](../../docs/WORKFLOW.md) for additions and revisions.
