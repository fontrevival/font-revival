# Source and method

The numbered cuts on unnumbered PDF pages 237–289 (odd-numbered pages) of George Bruce’s 1828 specimen supply these 354 drawings. Native embedded page images from the New York Public Library copy retain the source evidence. All page citations are one-based PDF positions; archive leaves are separate zero-based positions.

A 270-degree counterclockwise quarter-turn restores the printed page orientation. Exact native rectangles are recorded in `crops.json`; tools retain their deliberate oblique poses. The master uses uniform scaling without stretching, thresholded source masks and Potrace cubic fitting. The original impressions limit fine detail; no hidden engraving has been invented.

`inventory.json` links duplicate impressions to existing stable IDs. A standalone eagle and a figure beside houses retain their complete printed compositions and record related motifs. The filled small steamboat (No.171) and long gun (No.224) remain source gaps rather than uncertain additions. The reclining animal is deliberately described without an unverified species.

To reproduce the optional source preparation, run `scripts/trace_specimen.py bruce-cuts-1828` with Potrace 1.16 and the repository requirements, then import the resulting OTF. The canonical editable master is `font.ttx`.

The complete twelve-panel zodiac is retained as twelve distinct pictorial cuts. The fine engraving and pale frame edges require recorded per-cut thresholds; no absent hatching is reconstructed. Isolated captions, neighboring fragments and paper specks are excluded by crop-local erasures. Tools retain deliberate angles, and the skate is identified from its footplate, straps and upturned blade. Two tapered implements and several mammals retain descriptive names until a labelled witness establishes a more specific identity.

Fish, insects and animal engravings retain their original proportions and deliberate angles. Crop review extends clipped extremities to the complete printed design; per-cut thresholds balance pale lines against filled engraving. Explicit erasures remove only neighboring caption fragments and isolated paper specks. Fine hatching below native scan resolution is not invented. Ambiguous species and tool subtypes retain descriptive names.

The household and natural-history cuts on PDF pages 261–267 retain full extremities and native proportions. No523 is identified from its cloth folds as a draped monument. Faint cage wires and pyramid lines use individually reviewed thresholds; source gaps in fine engraving are retained.

The later small cuts on PDF pages 269–289 retain thin plant, insect and animal outlines with individually reviewed thresholds. Native crops preserve complete extremities. The camel with pyramids and portrait medallion are observed engraved variants of related compositions; no lost detail is reconstructed. Explicit erase rectangles remove detached paper marks and neighbouring captions.

The illustrated panels on PDF pages 291–339 include framed narratives, natural history, ships and emblems. Eleven tilted frames are rectified from measured opposing edges, preserving their mean dimensions and complete surrounding flourishes. The exact quadrilaterals and output dimensions are retained in crops.json. The mouse No.534 is a separate engraving with a curved tail and different ground from No.395. Related compositions and repeated pages remain linked in the inventory.

Selected matching Bruce1828 impressions improve engraving detail. The exact native crop rectangles, previous and selected witnesses, thresholds and reasons are retained in bruce1828-quality-revisions.json. The glyph overrides preserve each stable ID, codepoint and advance, including all tone regions where applicable. Previous sources remain in reference/. No absent content is reconstructed.

The final illustrated leaves, PDF 341–403, contribute 64 distinct complete designs. Two rectangular illustrations are squared from measured edge coordinates in crops.json. Repeated, matching and clipped impressions remain explicit in inventory.json, with native reference pages retained. Catalogue numbering is transcribed as printed even when a number is reused for a different engraving. Cut 1136 lacks the upper horse contour and 1139 lacks a wingtip and upper rays in both repeated impressions; neither is reconstructed.

Dense engravings can exceed signed renderer point or contour limits. Reviewed source/truetype-glyphs paths retain the original advance and a bounded outline difference; their SHA256 binds them to the full-detail master. All downloadable font formats use those compatible drawings. The editable master and SVG preserve unrestricted detail. See source/truetype-review.json and specimens/format-comparison.pdf for the display-size proof.

Three extremely dense cuts (1092, 1093 and 1135) use a coverage-preserving diagonal screen in downloadable fonts. This is a modern format interpretation of apparent shading, not replacement historical engraving. The source/truetype-settings.json file selects the method; per-glyph records retain its pixel scale, blur, screen period and outline fingerprint. Native source and unrestricted SVG remain available for detailed reproduction. The optional preparation command is `python collection/baltimore-cuts-1832/source/prepare_truetype.py bruce-cuts-1828 --potrace PATH`.

The combined proof PDF embeds grayscale source previews at a maximum of 500 pixels and JPEG quality 85 to keep the complete 499-design comparison distributable. Native reference images and individual comparison PNGs are retained at their original recorded resolution. This setting affects PDF previews only.

Encoded-only font delivery keeps the gallery connected to the full generated SVG contours while the reviewed compact outlines serve desktop and webfont rendering. The PDF proof draws the same delivered TrueType outlines as reusable vector forms.
