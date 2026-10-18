# London 1889

Ornamental capitals with swelling strokes, flared terminals and selectively descending stems.

![London 1889 specimen](specimens/preview.png)

**1889 · Regular · Version 1.001 · 104 characters · Capitals only · MIT**

[OTF](fonts/London1889-Regular.otf) · [TTF](fonts/London1889-Regular.ttf) · [WOFF2](web/London1889-Regular.woff2) · [PDF specimen](specimens/specimen.pdf) · [Changes](CHANGELOG.md)

## Use

Install either desktop format. For websites, copy `web/`, include `font.css`,
and use `font-family: "London 1889"`. Designed for display sizes.

## Design

**Designer:** Unidentified in the consulted historical specimen

**Foundry:** Boston and Central Type Foundries

**Observed:** Directly traced characters: 5678ACDEFGHIKLMNOPRSTUVW. Printed page 179, PDF page 185. Larger impressions anchor the master; smaller sizes supply additional characters. Original crops are also retained for separately labelled reconstructions. Additional directly traced impressions supply 4QY. Exact editions, pages, crops, scale anchors and cleanup are recorded in source/tracing.json and reference/specimen-restoration-sources.json.

**Reconstructed:** Inferred companion letters and figures: BJXZ01239. Punctuation and remaining symbols are new project drawings. Lowercase input aliases the capitals. Spacing and harmonisation of optical sizes are modern choices. The 1889 suffix dates the source, not a claim of first release.

## Sources

1. [Specimen book from the Boston type foundry (1889), London; printed p. 179, one-based PDF page 185, Internet Archive leaf 185](https://archive.org/details/specimenbookfrom00unse/page/n185/mode/1up) — 1889 US publication, public domain under the maximum historical 95-year term. Library of Congress scan hosted by Internet Archive; retained institutional metadata says the Library is unaware of copyright restrictions. Original native JP2 leaf; no modern digital typeface used. [Rights basis](https://archive.org/metadata/specimenbookfrom00unse).
2. [ATF 1898, leaf 444](https://archive.org/details/deskbookofprinti00amer/page/n444/mode/1up) — 1898 US publication, public domain by age. Historical scan and institutional metadata retained; no modern digital font used. Native JP2 page. [Rights basis](https://archive.org/metadata/deskbookofprinti00amer).

Source images are in `reference/`; the source record is [font.json](font.json).
Historical reference material retains the rights status recorded there.
Copyright (c) 2026 Harold Lehmann. The digital revival is released under the included [MIT License](LICENSE).

## Build or improve

From the repository root:

```sh
python scripts/fontrevival.py build london-1889
python scripts/fontrevival.py check london-1889
```

Edit `source/font.ttx` or export an individual glyph with
`python scripts/fontrevival.py glyph london-1889 j`.
Follow the shared [revival workflow](../../docs/WORKFLOW.md) for additions and revisions.
