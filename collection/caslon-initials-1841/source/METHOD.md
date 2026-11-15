# Historical source preparation

Native JP2 leaves preserve the original context. `crops.json` records native rectangles, quarter-turns, erasures and any measured quadrilateral correction. The lossless PNG crops are the exact tracing inputs. Any local pixel adjustments applied during preparation are retained with the crop record. `tracing.json` records Potrace 1.16 thresholds, component filtering and fitted-curve settings. Monochrome-only adaptive or regional thresholds recover observed faint ink; tonal masks and the sizing frame use the retained grayscale crop. Measured `post_trace_transform` matrices rotate fitted paths without resampling the scan.

`drawings.json` preserves the reviewed monochrome paths; `glyphs/` preserves three disjoint tonal bands at opacities 1, 0.55 and 0.25. The imported CFF master is canonical. Recorded source wear remains where no observed repair is possible. Font units are uniformly scaled, retaining each design’s proportions.

`inventory.json` distinguishes source settings from design identities. Repeated body sizes and compositions refer to their canonical components, including explicit gaps where hidden foldouts or weak impressions prevent extraction. Unresolved identities are preserved without speculative duplicate claims. Standalone decorated letters are illustration assets rather than partial text fonts.
