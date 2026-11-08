# GPO Cuts 1897

The source is *Specimens of job and display types in use in the Government
Printing Office* (1897), Internet Archive identifier `specimensofjobdi00unit`.
The historical publication is public domain by age. Native JP2 pages and
lossless grayscale conversions are retained with acquisition hashes.

## Coverage and identity

The inventory records all 37 numbered impressions on printed pages 91–94.
Fourteen complete compositions have new permanent identities. Twenty-two
impressions match designs retained in GPO Cuts 1904; four supply clearer
witnesses for those existing identities. Agriculture No. 23 repeats No. 22.
Its smaller size and heavier printing do not establish a distinct design.

Design comparisons use lettering, border construction and engraved forms.
Agriculture No. 22 combines outlined lettering, a shaded star field and a
ruled shield. The 1904 variants have different lettering or an open shield.
The two Marine Hospital seals have independently constructed lettering.
The Ordnance seals retain their different integral inscriptions. The Life
Saving Service emblem has a different oar and gaff arrangement from the
1904 versions. The Smithsonian seal has a draped, stippled profile bust;
the 1904 portrait has a different shoulder and engraving treatment.

The Agricultural Society seal includes its institution name and 1852 date.
Its unlettered relative in the 1904 specimen remains a separate composition.
Names describe observed subjects without assigning unidentified engravers.
Related witnesses do not prove reuse of the same physical printing block.
Complete engraved wordings are part of their icons, not text alphabets.

Printed folios are read from the scans. They differ from the provider's
page-number labels on these leaves. Printed pages, one-based access PDF
pages and archive leaves are retained as separate fields.

## Preparation

`tracing.json` records native-pixel crops, measured blank-paper masks and
individual monochrome and tone thresholds. Crop right and bottom edges are
exclusive. Masks exclude detached specimen numbers or scan specks while
preserving integral inscriptions and decoration. No missing linework is
invented, no holes are filled and no local paper normalization is applied.

The default preparation uses a 0.3-pixel Gaussian blur, a minimum component
area of two native pixels and Potrace 1.16 at tolerance 0.15. Tonal masks are
separated before curve fitting. Opacities 1, 0.55 and 0.25 interpret scanned
ink strength; they do not imply three historical printing inks.

Each composition scales uniformly to an 1800-unit maximum dimension within
a 2048-unit em, with vertical centring and 64-unit sidebearings. Source
proportions are retained. The only new character drawing is a blank space.
The Private Use assignments and names are project metadata.

Optional preparation uses the pinned requirements in this directory and
the shared native tracing implementation:

```sh
python collection/gpo-cuts-1897/source/prepare.py gpo-cuts-1897 \
  --output workspace/GPOCuts1897-Regular.otf --potrace /path/to/potrace \
  --jobs 2 --cache workspace/gpo-trace-cache
python collection/gpo-cuts-1897/source/stage_master.py \
  workspace/GPOCuts1897-Regular.otf workspace/gpo-1897-baseline.otf
python scripts/fontrevival.py import gpo-cuts-1897 workspace/gpo-1897-baseline.otf
```

Normal builds use the canonical `font.ttx` and standard glyph overrides.
Named private tone paths are retained as editable overrides over empty CFF
slots. Full-detail artwork remains authoritative; any font-format reduction
requires a separate comparison with that artwork. See the shared collection
workflow for sizing, format checks, specimen review and publication.
