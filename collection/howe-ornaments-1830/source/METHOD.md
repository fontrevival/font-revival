# Historical source preparation

Native JP2 leaves preserve the complete historical context. `crops.json` records source coordinates, quarter-turns, explicit removal of neighbouring captions, and measured rigid deskew. The lossless crop and `tracing.json` retain each accepted threshold and Potrace 1.16 setting. Uniform scaling preserves the engraved proportions; no missing image content is reconstructed.

`drawings.json` retains the fitted paths; the imported CFF XML is the build master. Repeated impressions are linked to stable collection IDs in `inventory.json`. Better complete impressions revise those existing IDs rather than create duplicate offerings. Distinct recuts remain separate. Composed borders are recorded through their constituent pieces.

The book has 298 scan images, including 142 historical printed faces and 156 blank or copy-material images. The 296-page access PDF excludes the first and last scan images. These unpaginated leaves use explicit PDF positions and null printed-page numbers. `type-coverage.json` records observed alphabets and exact source gaps; incomplete text faces are not issued.

## Dense font delivery

`font-parts.json` records default OpenType `ccmp` pieces for uniE05C. The complete fitted outline is split at overlapping boundaries so each piece fits renderer limits. Only the final piece advances; the encoded icon and overall spacing remain unchanged. `truetype-glyphs/` retains a simplified compatibility outline for applications without shaping. Downloadable fonts contain encoded monochrome icons and private assembly pieces; the complete tone layers remain in the canonical master and SVG artwork.
