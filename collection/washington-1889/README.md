# Washington 1889

Broad high-contrast display letters with triangular entry serifs and a lively historical lowercase.

![Washington 1889 specimen](specimens/preview.png)

**1889 · Regular · Version 1.000 · 104 characters · MIT**

[OTF](fonts/Washington1889-Regular.otf) · [TTF](fonts/Washington1889-Regular.ttf) · [WOFF2](web/Washington1889-Regular.woff2) · [PDF specimen](specimens/specimen.pdf) · [Changes](CHANGELOG.md)

## Use

Install either desktop format. For websites, copy `web/`, include `font.css`,
and use `font-family: "Washington 1889"`. Designed for display sizes.

## Design

**Designer:** Unidentified in the consulted historical specimen

**Foundry:** Boston and Central Type Foundries

**Observed:** Directly traced characters: 12345678ABCDEFGHIKLMNOPRSTUXYacdegilnoprstvx. Printed page 184, PDF page 190. Larger impressions anchor the master; smaller sizes supply additional characters. Original crops are also retained for separately labelled reconstructions.

**Reconstructed:** Inferred companion letters and figures: JQVZjkqy. Punctuation and remaining symbols are new project drawings. Both historical cases are retained. Spacing and harmonisation of optical sizes are modern choices. The 1889 suffix dates the source, not a claim of first release. Characters redrawn in place of coarse small-size traces: 09Wbfhmuwz; see companions.json for the construction of each.

## Sources

1. [Specimen book from the Boston type foundry (1889), Washington; printed p. 184, one-based PDF page 190, Internet Archive leaf 190](https://archive.org/details/specimenbookfrom00unse/page/n190/mode/1up) — 1889 US publication, public domain under the maximum historical 95-year term. Library of Congress scan hosted by Internet Archive; retained institutional metadata says the Library is unaware of copyright restrictions. Original native JP2 leaf; no modern digital typeface used. [Rights basis](https://archive.org/metadata/specimenbookfrom00unse).

Source images are in `reference/`; the source record is [font.json](font.json).
Historical reference material retains the rights status recorded there.
Copyright (c) 2026 Harold Lehmann. The digital revival is released under the included [MIT License](LICENSE).

## Build or improve

From the repository root:

```sh
python scripts/fontrevival.py build washington-1889
python scripts/fontrevival.py check washington-1889
```

Edit `source/font.ttx` or export an individual glyph with
`python scripts/fontrevival.py glyph washington-1889 j`.
Follow the shared [revival workflow](../../docs/WORKFLOW.md) for additions and revisions.
