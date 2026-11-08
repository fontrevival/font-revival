# Boston Ornaments 1889

Original JP2 leaves from the 1889 Boston specimen are retained unchanged. Acquisition URLs, archive members and hashes are in reference/acquisition.json. The requested Boston survey is tracked centrally in ../../boston-cuts-1889/source/inventory.json.

Individual word ornaments and border components are isolated from catalogue numbers, prices and sample text. Repeated compositions demonstrate the same parts and are retained on full source pages. Native crop coordinates, explicit erase rectangles and all preparation settings are in tracing.json. PUA assignments are stable within this font family; icon IDs are globally unique.

Potrace 1.16 fits cubic curves after optional local paper correction: a 25-pixel maximum filter and radius-4 Gaussian estimate paper illumination; each native gray value is divided by that estimate. This does not add strokes or close gaps. Three thresholds make nested masks; exact PathOps differences create disjoint primary, secondary and tertiary regions. Opacities are 1, 0.55 and 0.25. These tones are modern interpretations of the scanned impressions.

Uniform scaling retains source aspect ratios, fits the longest ink dimension within 1800 units of the 2048-unit em, and centres short ornaments vertically. Sidebearings are 64 units. Paper and neighbouring labels are removed only with recorded crop boundaries or explicit rectangles. No pictorial content is invented. Normal builds use the committed CFF TTX master and do not need Potrace or the network.

Prepare with scripts/trace_specimen.py boston-ornaments-1889 --jobs 4 --cache workspace/boston-expansion/trace-cache, then import and build through scripts/fontrevival.py.

The 715 exports cover printed pp. 258–270. Complete frames and separable printing components retain their distinct uses. Connected repeats that cannot be isolated without slicing artwork are recorded in inventory.json and preserved in the complete frame. Recorded threshold overrides preserve thin K-series curls, fine corner lines and engraved counters. The repeated publisher emblem is exported once from p. 258.

## Border boundary review

`border-cleanup.json` records native source crops and measured cleanup regions.
They remove neighbouring-cut fragments or isolated paper flecks after the existing
alignment transform, without changing the normalisation or advance. This revision
removes only complete disconnected contours from the right edge of Corner 119; the corner itself is unchanged. Historical worn impressions
and shared joins are retained. `specimens/border-review.pdf` records before/after
proofs. Layout recipes in `site/icon-layout.json` distinguish printing components
from complete frames and strips.

Native group context distinguishes the fine-and-heavy bracket pairs in Word
Ornaments Nos. 10 and 11 from ordinary parallel hairlines. Each pair remains one
complete historical specimen. Combination Ornament L2 and Santa Claus border
component 2 each contain three strokes, with a heavier middle stroke. Combination
Ornaments K2 and K3 retain their left- and right-curled ball terminals. These
six descriptions and their subject tags follow the observed shapes; the IDs,
character assignments, component grouping, source contours and spacing remain
unchanged. `rule-classification.json` retains the previous descriptions and the
source evidence, with a native-context review PDF.

The four straight strokes in Series E, specimens 1–4 on printed page 260,
carry straight and horizontal subject tags. They have no curled terminals.
`plain-rule-classification.json` retains the former tags and source evidence;
artwork, character assignments, names and spacing remain unchanged.

## OpenType drawing-program limits

The downloadable OTF divides drawing programs longer than 60,000 bytes into
shallow CFF subroutines using the shared builder. Drawing instructions and their
operands remain exact; no contour is simplified. The editable master, SVGs,
TrueType and webfont outlines, spacing, and character assignments are unchanged.
This prevents strict font sanitizers from rejecting a drawing program exceeding
the CFF length limit.
