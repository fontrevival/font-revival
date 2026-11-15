# Historical source preparation

Native JP2 leaves preserve the complete historical context. `crops.json` records source coordinates, quarter-turns, explicit removal of neighbouring captions, and measured rigid deskew. The lossless crop and `tracing.json` retain each accepted threshold and Potrace 1.16 setting. Uniform scaling preserves the engraved proportions; no missing image content is reconstructed.

`drawings.json` retains the fitted paths; the imported CFF XML is the build master. Repeated impressions are linked to stable collection IDs in `inventory.json`. Better complete impressions revise those existing IDs rather than create duplicate offerings. Distinct recuts remain separate. Composed borders are recorded through their constituent pieces.

The book has 298 scan images, including 142 historical printed faces and 156 blank or copy-material images. The 296-page access PDF excludes the first and last scan images. These unpaginated leaves use explicit PDF positions and null printed-page numbers. `type-coverage.json` records observed alphabets and exact source gaps; incomplete text faces are not issued.

## Font delivery

The densest engravings retain their complete fitted curves through default OpenType `ccmp` shaping. `font-parts.json` fingerprints each canonical outline and lists its registered pieces in `font-parts/`. Each piece fits CFF and TrueType renderer limits; only the last advances. Stable character codes and original spacing are retained. The actual released fonts are compared with the canonical outlines, including fine hatching and inscriptions. Applications without shaping use the binary compatibility drawings in `truetype-glyphs/`; these lose fine detail and should be replaced by the SVG for large artwork. Other recorded font approximations retain the prior display-size review. SVG and tonal artwork preserve the full canonical paths. See the [icon workflow](../../../docs/ICONS.md) for preparation and format checks.
