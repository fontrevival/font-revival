# Historical source preparation

The retained native JP2 leaves provide source context. `crops.json` records exact native rectangles, quarter-turns, subsequent rotations and any measured quadrilateral correction. The lossless PNG crops retain the resulting geometry. `tracing.json` specifies the final threshold, component filtering, small-hole cleanup, crop erasures and uniform scale for Potrace 1.16. `drawings.json` preserves the reviewed fitted paths. The imported CFF master is canonical.

Rectangular frames are corrected only from their observed corners. Recorded local threshold regions recover faint printed rules without drawing new content. Border units are separated at reviewed repeat boundaries. Isolated surrounding caption and neighbouring-sort fragments are excluded; faint detail absent from the scan is not invented. Source wear that cannot be resolved remains visible.

`inventory.json` records the historical settings, canonical duplicate IDs, composition components and source-quality gaps. Repeated impressions and historical body sizes do not create extra offerings. Permanent IDs and codepoints identify the distinct designs.

## Font delivery

The densest engravings retain their complete fitted curves through default OpenType `ccmp` shaping. `font-parts.json` fingerprints each canonical outline and lists its registered pieces in `font-parts/`. Each piece fits CFF and TrueType renderer limits; only the last advances. Stable character codes and original spacing are retained. The actual released fonts are compared with the canonical outlines, including fine hatching and inscriptions. Applications without shaping use the binary compatibility drawings in `truetype-glyphs/`; these lose fine detail and should be replaced by the SVG for large artwork. Other recorded font approximations retain the prior display-size review. SVG and tonal artwork preserve the full canonical paths. See the [icon workflow](../../../docs/ICONS.md) for preparation and format checks.
