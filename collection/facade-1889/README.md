# Facade 1889

Tall condensed display capitals with rising crossbars, fine serifs and narrow oval bowls.

![Facade 1889 specimen](specimens/preview.png)

**1889 · Regular · Version 1.001 · 104 characters · Capitals only · MIT**

[OTF](fonts/Facade1889-Regular.otf) · [TTF](fonts/Facade1889-Regular.ttf) · [WOFF2](web/Facade1889-Regular.woff2) · [PDF specimen](specimens/specimen.pdf) · [Changes](CHANGELOG.md)

## Use

Install either desktop format. For websites, copy `web/`, include `font.css`,
and use `font-family: "Facade 1889"`. Designed for display sizes.

## Design

**Designer:** Unidentified in the consulted historical specimen

**Foundry:** Boston and Central Type Foundries

**Observed:** Directly sampled characters: 12356789ABCDEFGHILMNOPQRSTUVWXY. Printed page 191, PDF page 197. Larger impressions anchor the master; smaller sizes supply additional characters. The tiny K impression informs a separately documented reconstruction. Additional directly traced impressions supply 4. Exact editions, pages, crops, scale anchors and cleanup are recorded in source/tracing.json and reference/specimen-restoration-sources.json.

**Reconstructed:** Inferred companion letters and figures: JZ0. K is redrawn from its tiny impression, using the larger I to restore stem weight and flared terminals. Punctuation and remaining symbols are new project drawings. Lowercase input aliases the capitals. Spacing and harmonisation of optical sizes are modern choices. The 1889 suffix dates the source, not a claim of first release.

## Sources

1. [Specimen book from the Boston type foundry (1889), Facade; printed p. 191, one-based PDF page 197, Internet Archive leaf 197](https://archive.org/details/specimenbookfrom00unse/page/n197/mode/1up) — 1889 US publication, public domain under the maximum historical 95-year term. Library of Congress scan hosted by Internet Archive; retained institutional metadata says the Library is unaware of copyright restrictions. Original native JP2 leaf; no modern digital typeface used. [Rights basis](https://archive.org/metadata/specimenbookfrom00unse).
2. [ATF 1898, leaf 346](https://archive.org/details/deskbookofprinti00amer/page/n346/mode/1up) — 1898 US publication, public domain by age. Historical scan and institutional metadata retained; no modern digital font used. Native JP2 page. [Rights basis](https://archive.org/metadata/deskbookofprinti00amer).

Source images are in `reference/`; the source record is [font.json](font.json).
Historical reference material retains the rights status recorded there.
Copyright (c) 2026 Harold Lehmann. The digital revival is released under the included [MIT License](LICENSE).

## Build or improve

From the repository root:

```sh
python scripts/fontrevival.py build facade-1889
python scripts/fontrevival.py check facade-1889
```

Edit `source/font.ttx` or export an individual glyph with
`python scripts/fontrevival.py glyph facade-1889 j`.
Follow the shared [revival workflow](../../docs/WORKFLOW.md) for additions and revisions.
