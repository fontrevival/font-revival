# The revival workflow

For ornament and cut families, also follow [the icon workflow](ICONS.md). It uses
the same CFF master and maintenance commands, with Private Use coverage and
generated SVG, sprite and CSS delivery alongside the desktop and web fonts.

Original project work uses Harold Lehmann's copyright notice and the repository
MIT license. Keep historical designer credits and source rights distinct from
copyright ownership.

## 1. Start from evidence

Put working scans, images, or PDFs in `workspace/`. Identify the typeface,
date, designer, foundry, and useful specimen pages. Record a public-domain rights
basis using the [source policy](SOURCES.md). Keep the exact reference images used
in `collection/<id>/reference/` so future work does not depend on live websites.

## 2. Add a family

```sh
python scripts/fontrevival.py new example-1890 --name "Example 1890" --year 1890
```

Complete the generated `font.json`. Trace the historical forms, clean scan damage,
set consistent metrics and spacing, and draw any missing companions. Record which
forms are reconstructed. Build or export a static OpenType/CFF master with at
least printable Basic Latin, then import it:

```sh
python scripts/fontrevival.py import example-1890 workspace/Example1890-Regular.otf
python scripts/fontrevival.py sizecheck example-1890
python scripts/fontrevival.py build example-1890
```

The imported XML master preserves the outlines, character map, spacing, kerning,
and OpenType features. It is the common source for every release format. Additional
tracing scripts and measurements can live alongside it under `source/`.

For an intentionally limited revival, `font.json` may instead declare the exact
encoded characters in `character_set`, with an explanation in
`character_set_notes`. Include spaces and aliases explicitly. Preparation and
validation reject both missing and extra characters; ordinary text families
still require printable Basic Latin. Omit unsupported figures and symbols when
the revival is limited to observed source forms. Generated specimens show only
supported characters.

For sources suitable for crop-based tracing, the optional [repeatable tracing
tool](TRACING.md) records measurements and explicit companion drawings, then prepares
the OTF for `import`. The build uses those records to generate a historical-source
comparison proof for visual review.

## 3. Improve an existing family

Save the current font before editing. For example:

```sh
cp collection/nero-1888/fonts/Nero1888-Regular.ttf workspace/nero-before.ttf
python scripts/fontrevival.py glyph nero-1888 j
```

If that glyph already has an edit file, edit the existing file. Change the SVG path
and advance width in `source/glyphs/j.json`. Coordinates use the font's units per
em, with positive y upwards. The `notes` field records the design rationale.
Check related accented forms too; a `j` change may also require `jcircumflex`.
Run `python scripts/fontrevival.py sizecheck <id>` on the editable source before
building. Review flagged proportions against the scan; record intended size ranges
in `source/sizing.json` so `check` can reject future regressions in every format.
See [character sizing](SIZING.md) for rules, measurement reports and limitations.
For broader changes, edit `source/font.ttx`, or intentionally replace it with
`import ... --replace`. Existing glyph edits continue to apply over a replaced master;
review them when replacing it.

Increase `font.json`'s version (for example `1.001` → `1.002`) and describe the
change in `CHANGELOG.md`. Rebuild, then generate a focused review proof:

```sh
python scripts/fontrevival.py build nero-1888
python scripts/fontrevival.py compare nero-1888 --before workspace/nero-before.ttf \
  --text "j ij ji fj ja jo ju aj enjoyment ĵ" \
  --output collection/nero-1888/specimens/j-review.pdf
python scripts/fontrevival.py build nero-1888
```

The final build includes the review PDF in the checksums. Use a meaningful filename
and keep review proofs that explain design decisions. Git preserves previous masters
and releases; a revision should be a focused commit.

## 4. Check and share

```sh
python scripts/fontrevival.py check
python -m unittest discover -s tests
python -m http.server 8000
```

Inspect the gallery at <http://localhost:8000>, the specimen PDF (including its full
character inventory), and any review proofs. Compare against the historical sources.
Check counters, overlaps, baseline, descenders, spacing, and words containing the changed
forms. Commit the editable sources and regenerated outputs together.

Documentation-only changes need a diff review and `git diff --check`; they do
not require rebuilding unchanged fonts.

The `Check collection` workflow compares each push or pull request with the last
successful check on its target branch. It validates and packages affected
families, checks generated gallery files when their inputs change, and runs the
tests for code or collection changes. Shared build tools, pinned dependencies,
the license, or the checking workflow trigger a full audit. A manual workflow
run also audits the complete collection; a missing successful baseline defaults
to that full audit. Each selected family is rebuilt once before packaging.
The uploaded packages contain only the families selected for that run.

### Gallery publication

The `Publish gallery` workflow (`.github/workflows/pages.yml`) publishes pushes
to `main` that change site inputs. Documentation-only and test-only pushes skip
publication. Pushes to other branches do not publish the gallery.

After pushing a site change to `main`, find the run for that commit with
`gh run list --workflow pages.yml --commit <commit-sha>` and monitor it with
`gh run watch <run-id> --exit-status`. Retry the lookup if the run has not appeared
yet. Check failed logs before retrying a deployment, and verify the expected
update on the [live gallery](https://font-revival.com/) after a successful run.

Pages receives a complete site artifact. To keep preparation fast, the workflow
starts with a sparse partial checkout and fetches only files the gallery embeds.
Download links are checked against the committed Git tree without fetching the
archival files. Prepared pages and their dependencies are cached by their Git
blob IDs and assembler configuration. Unchanged pages can be reused without
fetching their large source files. The compiled editor is reused when its pinned
commit, configuration and catalogue inputs match. Pages receives a complete
snapshot assembled from cached and changed files; an unchanged snapshot skips
the upload and deployment. Changes only to externally hosted downloads therefore
need no new Pages deployment. Local assembly with `python3 scripts/build_site.py`
uses the full checkout and needs no cache.

### Editor distribution

The published site includes a proprietary editor built from the separate private
repository pinned in `site/editor-release.json`. Only its compiled browser assets
and proprietary and third-party notices are distributed with the site. The
collection's MIT license applies to this repository's work; it does not license
the editor. Editor source and build configuration are maintained separately.

## Repeatability

`build` discovers families automatically and derives OTF, TTF, WOFF, WOFF2, specimen
PDF/PNG, CSS, family README, checksums, and the gallery from committed inputs.
TTF curves are derived from the cubic master with a maximum conversion error of
0.5 font units. The build applies the MIT metadata and unrestricted embedding.

`check` verifies character coverage, nonempty outlines, spacing across formats,
reviewed character sizing limits, license metadata, checksums, and a clean rebuild
in a temporary directory. It also prints advisory size outliers for visual review.
Python 3.12 and `requirements.txt` define the reference environment used by CI.
Rendering may differ with platform font rasterizers; use the Linux CI environment
for byte-for-byte comparisons. Source files and outputs are committed together.
