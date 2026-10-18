# Doric 1889

Heavy display letters with bracketed slab serifs, rounded bowls and a substantial historical lowercase.

![Doric 1889 specimen](specimens/preview.png)

**1889 · Regular · Version 1.000 · 104 characters · MIT**

[OTF](fonts/Doric1889-Regular.otf) · [TTF](fonts/Doric1889-Regular.ttf) · [WOFF2](web/Doric1889-Regular.woff2) · [PDF specimen](specimens/specimen.pdf) · [Changes](CHANGELOG.md)

## Use

Install either desktop format. For websites, copy `web/`, include `font.css`,
and use `font-family: "Doric 1889"`. Designed for display sizes.

## Design

**Designer:** Unidentified in the consulted historical specimen

**Foundry:** Boston and Central Type Foundries

**Observed:** Directly traced characters: 0123456789ABCDEFGHILMNOQRSTUVYacdehiklmnoqrstuv. Printed page 138, PDF page 144. Larger impressions anchor the master; smaller optical sizes supply additional characters. Crops are retained for separately labelled small-source reconstructions as well.

**Reconstructed:** Inferred companion letters and figures: JKXZbfgjpwxyz. Punctuation and remaining symbols are new project drawings. Both historical cases are retained. Spacing and harmonisation of optical sizes are modern choices. The 1889 suffix dates the source, not a claim of first release. Characters redrawn in place of coarse smaller-size traces: PW; see companions.json for the construction of each.

## Sources

1. [Specimen book from the Boston type foundry (1889), Doric; printed p. 138, one-based PDF page 144, Internet Archive leaf 144](https://archive.org/details/specimenbookfrom00unse/page/n144/mode/1up) — 1889 US publication, public domain under the maximum historical 95-year term. Library of Congress scan hosted by Internet Archive; retained institutional metadata says the Library is unaware of copyright restrictions. Original native JP2 leaf; no modern digital typeface used. [Rights basis](https://archive.org/metadata/specimenbookfrom00unse).

Source images are in `reference/`; the source record is [font.json](font.json).
Historical reference material retains the rights status recorded there.
Copyright (c) 2026 Harold Lehmann. The digital revival is released under the included [MIT License](LICENSE).

## Build or improve

From the repository root:

```sh
python scripts/fontrevival.py build doric-1889
python scripts/fontrevival.py check doric-1889
```

Edit `source/font.ttx` or export an individual glyph with
`python scripts/fontrevival.py glyph doric-1889 j`.
Follow the shared [revival workflow](../../docs/WORKFLOW.md) for additions and revisions.
