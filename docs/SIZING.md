# Character sizing review

Use the repository's pinned Python environment. No additional tools are required.

```sh
python scripts/fontrevival.py sizecheck remington-1888
python scripts/fontrevival.py sizecheck remington-1888 --json > workspace/remington-sizes.json
python scripts/fontrevival.py sizecheck
```

`sizecheck` measures the canonical CFF master **with glyph overrides applied**, so
it can catch a mistake before a build. JSON output lists every encoded character's
glyph name, top, bottom, ink width, ink height and advance width, in font units.
It measures actual curve extrema and resolves composite outlines. Ink dimensions
matter: a tiny letter can still have the correct advance width, especially in a
monospaced font. Spaces have zero ink dimensions.

## Automatic review warnings

The audit compares capital tops, figure tops, lowercase body tops and ascender
tops with their group medians, flagging differences greater than 20%. It compares
`c/e/o` ink widths with a 25% tolerance and checks that `t` extends above the body
when the family has distinct ascenders. Groups need at least three usable members.
Lowercase checks are skipped for `character_style: "capitals-only"` or a cmap that
aliases the entire lowercase alphabet to capitals. Top coordinates are measured
separately from total height, so descenders and Q tails do not inflate the target.

Warnings request visual review; they do not certify that a letter is wrong.
Ornamental extensions, oldstyle figures, narrow letters and historical irregularity
can be deliberate. Default warnings are advisory in both `sizecheck` and `check`.
`sizecheck --strict` exits unsuccessfully on warnings as well as rule violations.

## Reviewed family limits

Add `source/sizing.json` after inspecting the historical source and proofs:

```json
{
  "schema_version": 1,
  "notes": "Explain the source, design targets and review evidence.",
  "rules": [
    {
      "characters": "t",
      "y_max": [685, 715],
      "y_min": [-10, 10],
      "ink_width": [380, 400],
      "notes": "This family's historical t reaches its 700-unit ascenders."
    }
  ]
}
```

Rules accept `y_min`, `y_max`, `ink_width`, `ink_height` and `advance_width` as
inclusive `[minimum, maximum]` ranges in font units. Each rule requires a reason in
`notes`. `characters` is a string of encoded characters; `"*"` selects all of them,
including spaces. Multiple rules on a character all apply. Missing characters,
unknown keys, invalid ranges and nonfinite values fail validation. Allow enough
room for curve conversion, rounding and appropriate optical overshoot. Give
intentional exceptions their own ranges; do not widen a whole group to hide a defect.

Rule violations fail `sizecheck`, `check` and packaging. `check` measures all four
release formats and runs in CI. A family without a profile gets only heuristic
warnings. Remington's [sizing profile](../collection/remington-1888/source/sizing.json)
provides an example covering letters, figures and fixed advances.
JSON reports include how many characters have at least one reviewed rule; this
does not imply every dimension of those characters is covered.

## Visual review

Bounds cannot judge stroke weight, counters, perceived size, or the body beneath
an accent. A letter can fit the numerical limits and need an optical adjustment.
Inspect words at several sizes, full character inventories, PNG/PDF specimens
and the gallery. Review accented derivatives and related forms whenever their
base changes. Save a before/after PDF with `compare`.
