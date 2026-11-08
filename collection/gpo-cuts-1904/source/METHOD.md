# GPO Cuts 1904

The source is the U.S. Government Printing Office's *Job room type faces*
(1904), also catalogued as the Job Room specimen book and catalogue. The GPO
contributed and sponsored Internet Archive scan `123459_1904`; GovInfo
provides the corresponding PDF. The publication is public domain by age.
The historical title-page copyright note does not establish a surviving
copyright in this 1904 publication.

## Coverage and design identity

`inventory.json` records each reviewed impression, selected witness, repeat
and match to an existing collection design. Its scope includes Index Cuts,
Flags, Eagle Cuts, Public Buildings, Steam and Sailing Vessels, Miscellaneous
Cuts, Check Ends, Seals, Post Old Style Ornaments, and the unnumbered new GPO building frontispiece. Printed page, one-based
PDF page and archive leaf are separate locators. The retained scan map confirms
these relationships; a matching number is not assumed to identify the same page.

Design identity depends on the engraved forms. A new size, ink weight or
rotation does not by itself create another icon. Vessel No. 45 repeats No. 38;
flags Nos. 1 and 2 repeat No. 3; the two No. 6 flags share one composition.
Treasury No. 87 reproduces No. 81 with softer tonal detail. The selected No. 81
preserves its fine ruled engraving. All repeat impressions remain on the full
reference pages and in the inventory.

Check Ends contains 44 impressions and 41 distinct complete compositions.
T1/T2 repeat N1/N2, and D3 repeats D1. Different integral labels remain part of
their respective compositions. B1 and B2 are separate vines with natural stem
endings; the enclosing typeset check does not join them into one ornament.
The complete wordmarks are icons, not evidence for complete text alphabets.

Post Old Style Ornaments contains 43 numbered impressions and 25 complete
designs. Eighteen impressions repeat the same compositions at different sizes.
The selected witnesses preserve clear internal lines and complete contours;
the larger eagle No. 26 is softer than the selected No. 7. The torch pair
Nos. 39 and 43 retains its observed opposite handedness. Unidentified people
remain described by their dress and pose, without speculative personal names.

The seal inventory distinguishes agency inscriptions, complete compositions
and engraving variants. A different agency name is part of a different seal;
a smaller or heavier impression alone does not establish another design.
Uncertain witnesses retain their comparison candidates without receiving new
codepoints. Outer borders, lettering, feathers and hatching supply the evidence
for distinct variants. Integral reply instructions remain with their seals.
Justice Nos. 34 and 109 have different head and wing construction and shield
ruling. The independent 1897 No. 28 impression confirms the No. 34 construction.

Matching impressions in *Specimens of job and display types in use in the
Government Printing Office* (1897) supply clearer witnesses for seals Nos. 35,
75, 79 and 110. `earlier-seal-witnesses.json` preserves both source selections,
the previous recipes and the reasons for choosing the earlier impressions.
Their permanent identities and advances are unchanged. The retained 1897
leaves use visually read printed folios: the provider's page-number labels
on these leaves do not reproduce the printed folios. A matching engraving
does not establish use of the same physical printing block.

Several hands and eagles also appear in the Boston and Baltimore collections.
The inventory links their permanent identities and records preferred witnesses;
those drawings belong to their existing families. Hand Nos. 21, 22 and 24 share
one design. No. 21 supplies its clearer raised-finger contour, while its stable
ID retains the number assigned during the initial comparison with No. 24.
Independent optical engravings remain separate when finger shapes, cuffs or
hatching differ. Agricultural allegory No. 67 resembles Baltimore No. 267, but
its face, drapery, fruit, trees and mill are independently engraved.

Names describe observed subjects. Eagle Cut No. 21 is a phoenix rising from a
burning pyre. `building-identifications.json` and
`miscellaneous-identifications.json` and `seal-identifications.json` distinguish documented subject evidence
from visual inference. The portrait labels do not assert an unidentified
engraver or photographic model. Integral lettering, historical banners and
engraved signatures remain part of the artwork. PLYMOUTH, NORTH WEST and
UNITED STATES are observed vessel lettering, not independent ship attributions.

## Native preparation and correction

`reference/acquisition.json` records original JP2 members, SHA256 hashes,
dimensions and lossless grayscale PNG conversions. Native scans retain detail
that can be absent from segmented PDF images. `tracing.json` records native-pixel
crops with exclusive right and bottom edges. Rotated page compositions receive
a documented quarter-turn to restore their reading orientation. Separate
captions and page furniture are excluded; integral lettering is retained.
Measured blank-paper masks remove adjacent captions or detached scan specks
without reconstructing the engraving.

Recipes retain their individual monochrome and three-tone thresholds. The
vessel section principally uses 110, 155 and 190; many other sections use
110, 155 and 210. Miscellaneous cuts principally use 145, 185 and 220.
Most check ends use 145, 195 and 230; A–C use 110, 155 and 210 to avoid
tracing paper texture. Individual recipes retain exceptions. For example, fine
hand contours use monochrome threshold 195 and the small flag uses 215 to retain
its observed stripes, staff and finial. Small hand No. 25 retains breaks present
in its printed index-finger line. Check-end E2 retains faint and broken outside
flourishes in the available witness. Missing linework is not invented.

A 0.3-pixel Gaussian blur and a minimum connected-component area of two or three
native pixels suppress isolated scan noise. No holes are filled and no local
paper normalization is applied. Potrace 1.16 fits cubic outlines at tolerance
0.15. Native masks are separated before fitting tonal regions
(`native-mask-bands`). Default opacities are 1, 0.55 and 0.25; they do not imply
historical printing in three inks.

Each composition scales uniformly to an 1800-unit maximum dimension inside a
2048-unit em, with vertical centring and default 64-unit sidebearings. Replacement
witnesses are centred within the previously assigned advances. Wide scenes retain
their proportions. `straightening.json` records measured architectural frame
axes and affine corrections applied equally to monochrome and tonal contours.
Native pixels are not warped. Illustrated perspective and inclined masts belong
to the art and are not automatically treated as scan defects. A blank quarter-em
space is the only newly drawn character; Private Use assignments are permanent.

`post-ornament-alignment.json` records outer-rule measurements for seven Post
Old Style panels. Four panels receive a small shared affine correction about
the unchanged advance centre; the other three retain directions under 0.2
degrees. The same transform applies to monochrome and all tone layers. Explicit
crop masks remove detached exterior paper marks from the potted rose and the
left-branch torch without removing internal engraved marks. The owl's filled
wing and faint medallion centre remain as observed in the available impressions.

The Art Strokes, Markers and Embellishers on printed page 132 retain separately
observed handed forms and differences in contour proportions. Twenty smaller
motif impressions link to clearer larger witnesses; this does not identify
their physical matrices as identical. Two small striped wedges remain
unassigned because filled white cuts prevent a reliable comparison of their
division counts. Rows of four stars or tabs and the page border are recorded
as compositions of existing components, with each border component located
on the retained page.

`stroke-alignment.json` records robust fits to fourteen deliberately straight
edges. Seven directions between 0.207 and 0.326 degrees receive rigid vector
rotations about the unchanged advance centre. The same transform applies to
monochrome and all tone layers. Designed curves and smaller measured angles
retain their source directions. Two caption masks and six exterior paper masks
exclude neighboring material. Broken hairlines and small white printing defects
remain visible where the available witnesses do not establish a repair.

Printed page 133 contains 86 numbered slots with 97 separately shown
impressions. Eighty distinct ornaments are retained, including one isolated
flag-shaped component from Capital No. 3. Twelve rotated impressions refer
to their selected counterparts. Wave No. 3 matches the existing Boston
triple-wave motif; the apparent weights of Wave Nos. 2 and 4 remain unresolved.
Capital No. 15 repeats two periods of No. 14. Protean No. 4 is an arrangement
of eight ordinary dots. The inventory records these compositions and the
ordinary panel rules without adding duplicate icons. Names describe observed
geometry and subjects; the small white centre of Art No. 17 is not assigned
an unsupported symbolic meaning.

`ornament-page133-alignment.json` retains twenty horizontal and five vertical
edge measurements. Seven rigid rotations of approximately 0.234–0.819 degrees
apply equally to monochrome and tonal paths. Short or inconsistent edges retain
their native directions. Protean No. 12's nearly upright sides and lower edge
do not justify warping the whole square to match its slightly sloping top.

Twenty-six page-133 ornaments have individually reviewed monochrome thresholds.
Wave Nos. 5, 8 and 10 combine faint rules and darker dotted lines. Their
`mono_threshold_regions` use measured rectangles in blank gutters to select
lower thresholds for dots while retaining the surrounding rules. The optional
`trace_regions.py` helper combines these native masks before tracing; it neither
draws missing ink nor changes the tonal recipes. Remaining ink bridges, broken
rules and faint petal tips stay visible pending clearer matching impressions.
Four caption masks in the page inventory, including three on selected drawings,
three neighboring-component masks and two exterior paper masks exclude material
outside the selected drawings.

Printed page 134 supplies 21 Job and Word ornaments from 72 numbered impressions
and eight repeated border rosettes. Size comparisons establish design identity
without asserting that the physical matrices are identical. The 36-point Job
and 24-point Word impressions usually provide the clearest contours. Word No. 4
uses its 12-point impression because both outer curls survive; the larger
impressions have broken curls or a white petal defect. Word No. 11 uses its
18-point impression with a complete round lower dot. Job Nos. 7 and 8 are
opposite-handed shell scrolls and retain separate identities. The eight page
rosettes repeat Word No. 12; ordinary paired rules and the assembled frame are
recorded as page furniture.

`ornament-page134-alignment.json` records thirteen measured straight edges.
Word No. 5 receives a 0.319-degree rigid rotation shared by all tone layers.
Independent edges of Job No. 4 and Word Nos. 1 and 2 disagree, so their printed
irregularities are retained. Seven monochrome thresholds preserve faint rays,
curls and stems. One caption mask and five exterior masks remove unrelated ink.
Word No. 7's tiny detached lower mark remains: its alignment with the stem tip
does not establish that it is paper debris. The small white cut in Job No. 2,
weak petal tip in Job No. 6 and softness of the smaller Word No. 4 impression
remain source-quality limitations.

## Unique and Flame Borders

Printed page 135 supplies fourteen distinct Unique Border motifs and two Flame
Border components. The inventory locates all 638 Unique impressions, including
twenty appearances of No. 205 that repeat Art Ornament No. 19. Its larger isolated
impression on printed page 133 remains the preferred source. Sixteen composed
examples are retained as context; two groups of ordinary vertical rules are
recorded separately. Rotated placements retain their component identity.

Five monochrome thresholds and three tonal threshold sets preserve fine petals,
veins and rays. Unique No. 145 uses the eleventh bottom impression after comparison
of all 78 witnesses; its small source still leaves some petal separations soft.
`border-page135-alignment.json` records seven native edge measurements. Unique
Nos. 180 and 214 receive small rigid rotations of −0.380 and −0.518 degrees,
respectively. The irregular maze tiles retain their observed geometry.

The Flame strip repeats six differing curves over 175 native pixels. All four
runs confirm that period; replacing it with a single generic flame would lose
observed differences. The four diagonal corners match under quarter-turns.
`border-page135-components.json` records the measured repeat rectangle and a
phase selected through solid joining ink. Three-period monochrome and tonal
proofs preserve the seam. A recurring broken fine tip remains visible in the
source; no speculative closure is drawn. Final delivery uses the measured tile
for continuous composition, while the font retains its ordinary sidebearings.

## Art Borders

Printed page 136 contains 354 impressions of two fleur-de-lis designs: outlined
“Open” and filled “Tint.” The 12-, 18- and 24-point examples share the same
construction. The diagonal corner placements are rotations of the upright
motifs. The inventory retains all seven composed frames and each repeated
impression, including the outer page surround.

The two 24-point top-row witnesses preserve the petals, tied bars, lower curls
and tails most clearly. Native asymmetry is retained; short curved features
provide no reliable basis for affine correction. Monochrome and tonal proofs
preserve the fine loops without contour simplification.

## Old English Borders and Elzevir Bands

Printed page 137 contains five assembled frames and two isolated roses. Its
651 component records resolve to nine designs and 642 repeated witnesses.
Old English No. 9 has two handed flower-and-serrated-leaf forms and a separate
diagonal bud corner. No. 10 uses the same layered five-petal rose throughout,
including the two isolated impressions. No. 25 repeats three outlined rounded
triangles and a solid dot; its staggered corner placements reuse that unit.

Elzevir Nos. 111 and 105 each have a straight repeat and a distinct corner.
The No. 111 corner includes the small diagonal star, both adjoining large
flowers and their modified scroll join. Those two flowers belong to the corner
record rather than the straight run. The inventory locates 62 straight periods
and four corner modules for No. 111, and 54 periods and four corners for No. 105.

The selected No. 111 period spans 93 native pixels. No. 105 uses a 77-pixel
period, phased through the interval after the lozenge flower so its interstitial
scroll remains complete. `border-page137-components.json` retains the measured
repeat rectangles. Three-period source, monochrome and tonal proofs document
the joins. The font keeps ordinary sidebearings; continuous composition uses
the recorded repeat rectangle. Small weaknesses in the printed lower line
remain source evidence, rather than being replaced with invented straight ink.

The second top-row No. 25 impression avoids a neighboring mark in the first.
The tiny No. 9 bud uses a lower monochrome threshold within its measured native
region to preserve the white petal divisions. Its paler leaves retain a separate
threshold, and the mask outside the bud region is unchanged. No contours are
drawn to replace missing ink. Five straight-reference measurements, retained in
`border-page137-alignment.json`, do not support a consistent skew correction;
native proportions and asymmetry are preserved.

## Caxton and Contour Borders

Printed page 138 contains eight frames assembled from 784 component impressions.
The solid Caxton and outlined Contour designs each have a straight repeat,
an outward corner and an inward corner at both 12 and 18 points. Twelve-point
straight and inward-corner loops close; the corresponding eighteen-point curls
remain open throughout the page. The smaller leaf tips are shorter and less
swept. These consistent differences identify distinct size engravings. Inward
straight runs are rotated impressions of the outward repeat, while their corner
construction is separate. The inventory records twelve new components and 772
repeats, with every corner and straight impression located individually.

Native crops retain the complete leaves and curls. The top-right 12-point
Contour inward corner supplies a clearer vine junction than the top-left
impression; a quarter-turn gives it the common corner orientation. One narrow
mask removes an adjoining leaf fragment beside the 18-point Contour inward
corner, below its retained vine. No absent ink is reconstructed. Curved leaf
edges and deliberate asymmetry are preserved without arbitrary squaring.

`border-page138-components.json` records native straight-repeat pitches of
58 and 87 pixels and their vector coordinate transforms. Repetition preserves
the small printing gaps at some joins. Corner placement uses the source frame
and its joining phase, independently of the isolated icon's font advance.

## Rounded rules

Printed page 139 shows 22 isolated parts and 22 corner or junction placements
in four frames. Eight forms account for those 44 witnesses: two heavy and two
fine handed long rules, a tight quarter-circle corner, a curved three-way
junction, and broader four-point and fine two-point corners. Three- and
six-point tight corners share the same construction at different scales, as
do the two junction sizes. Rotations retain their canonical identity.

The long rules preserve their complete observed endpoints. Four- and two-point
frame corners are separated just beyond measured tangencies, with short flat
joining margins. These crop boundaries do not establish physical joints in
the original printing material. The fine long rules and two-point corners
share a bend construction but retain their distinct complete endpoint layouts.
Twenty-five ordinary connecting runs remain located composition evidence.
Geometric fits compare radius-to-stroke proportions; the revival traces the
native ink rather than replacing it with ideal circles. Selected long stems
measure less than 0.15 degrees from vertical, so no affine correction is applied.
`border-page139-components.json` retains the geometry and source selections.
When composing frames, restore relative source stroke widths independently of
each icon's normalized display size.

## Reproduction and delivery

Normal builds use `font.ttx` and standard glyph overrides. Optional retracing
requires this directory's pinned requirements and Potrace 1.16:

```sh
python collection/gpo-cuts-1904/source/prepare.py gpo-cuts-1904 \
  --output workspace/GPOCuts1904-Regular.otf --potrace /path/to/potrace \
  --jobs 2 --cache workspace/gpo-trace-cache
python collection/baltimore-cuts-1832/source/prepare_truetype.py gpo-cuts-1904 \
  workspace/GPOCuts1904-Regular.otf --potrace /path/to/potrace
python collection/gpo-cuts-1904/source/stage_master.py \
  workspace/GPOCuts1904-Regular.otf workspace/gpo-baseline.otf
python scripts/fontrevival.py import gpo-cuts-1904 workspace/gpo-baseline.otf
python collection/baltimore-cuts-1832/source/review_sizing.py gpo-cuts-1904 \
  workspace/GPOCuts1904-Regular.otf
python scripts/fontrevival.py sizecheck gpo-cuts-1904
python scripts/fontrevival.py build gpo-cuts-1904
python scripts/fontrevival.py check gpo-cuts-1904
```

Replacing an existing master requires an intentional `--replace`. Shared
preparation helpers read this family's recipes without editing other families.
Staging retains all full-detail private tone paths as ordinary glyph overrides
over named empty CFF slots. The full-detail monochrome master and tonal vectors
remain authoritative for SVG and PNG.

Dense engravings can exceed font-renderer point or contour limits. Paths in
`truetype-glyphs/` record the canonical outline hash, unchanged advance, method,
counts and bounds allowance. Downloadable fonts use these reviewed reductions;
SVG and tonal PNG preserve full detail. CFF programs are split losslessly into
subroutines below 60,000 bytes. The sizing profile records source proportions
and measured allowance for format conversion.

Vessel Nos. 41 and 44 use the documented `coverage-screen` font approximation
to retain apparent shading that ordinary binary reduction loses. Its diagonal
screen is a modern font-format interpretation, not historical engraved linework.
Use full-detail SVGs for enlarged artwork. Source, vector and final font-format
proofs are distinct review stages; a recorded tracing is not by itself evidence
that all downloadable formats have passed review.

The interior front matter and section dividers retain 486 located ornamental placements in `frontmatter-components.json`. Three complete designs are traced: an oak/acorn sprig, a swallowtail ribbon and a three-leaf spiral spray. Facing six-triangle clusters decompose into two existing Old English 25 pieces; they are not additional icons. The property pattern repeats Unique 59 and the floral divider repeats both handed Old English 9 pieces and their common corner. Native source comparisons retain the existing lamp, spiral, radiating star, eagle and rounded-rule drawings. A clearer lower sepal on one divider corner comes with more plugged upper sepals, so that witness does not replace the complete prior tracing. The ribbon's separate typeset imprint is masked inside the blank field and retained in the complete source composition. No letters are reconstructed from these short headings.

The ribbon uses monochrome threshold 215 to retain its faint left tail. Measured rigid rotations level the ribbon by approximately −0.259 degrees and correct the leaf-spray page tilt by approximately +2.419 degrees. `frontmatter-alignment.json` retains the native edge measurements, uncertainty and shared vector transforms.

The binding uses one interlaced square meander corner in four rotations. Eight front/back-cover witnesses are recorded in `binding-components.json`; the front lower-left corner has the least scuff and glare. `separate_cover_gold.py` derives a native-size grayscale tracing signal as `255 - clip(3 * (green - blue), 0, 255)`, separating yellow gold from red leather and neutral reflections. The original colour JPEG2000 remains authoritative evidence. Extraction retains both complete loops and four joining rules in each arm; it does not infer physical stamp boundaries. Native gilt texture remains. Ordinary side rules and the outer rectangle stay composition context.

Eight measured rule directions support a rigid correction of approximately -0.319 degrees after the corner is turned upright. `binding-alignment.json` records the independent fits and common transform. The native variation among individual rules is retained. The thin binding strokes are intended for enlarged use, with a recommended minimum display size of 256 pixels.

Brass circles are isolated individually from four nested numbered groups on printed page 17. `brass-circle-isolation.json` records broad blank-paper masks, separate caption rectangles and two paper-mark exclusions. `isolate_brass_circles.py` reproduces the native-pixel derivatives; the full original leaf remains authoritative. No circle is replaced by ideal geometry. Diameter-specific stroke and spacing proportions distinguish the numbered forms from uniform rescalings.

The 24 brass brace impressions supply 13 distinct proportioned forms and 11 rotated witnesses. The opposed No.11 specimens differ in length and curvature, so both remain. Complete observed braces are turned horizontally with their middle point upward. `brass-brace-alignment.json` records endpoint measurements; three corrections over 0.15 degrees are applied rigidly, without changing aspect ratio or imposing lobe symmetry. Native printing gaps remain where a complete matching impression does not supply stronger evidence. Instructional binding diagrams and ordinary tables on printed pages 15 and 19 are documented separately in `technical-components.json`.

The signs on printed page 18 are catalogued impression by impression in
`sign-components.json`, with 141 main specimens and 81 explanatory-legend forms.
The legend supplies historical names, including integration, difference,
equivalence, versicle and the astronomical labels. Those source readings are
kept separate from modern Unicode assignments. Unlabelled curved signs retain
descriptive names. All 460 Boston symbol source crops and 27 related moon and
prescription cuts were compared at native resolution. Twenty-two distinct
complete forms are retained; four repeat witnesses supply additional evidence.
The ten- and twelve-point four-dot proportion specimens share one drawing,
while the wider, closer and fine-dot forms have different dot/spacing ratios.
Because and therefore share one triangle of dots under a half-turn.
The native ink is traced without substituting ideal circles, dots or straight
lines. Further unassigned sign comparisons remain explicit in the inventory.

The prescription signs include two distinct R constructions with a cross stroke
extending below the baseline. The broad form occurs both as recipe and as
ecclesiastical response; one canonical drawing serves both contexts. The narrow
ounce and drachm have different head and bowl proportions from the Boston
medical specimens. The upright-stem and high-wedge radicals differ from the
hooked check-shaped form already represented in Boston Symbols. Two unlabelled
angled algebraic signs retain descriptive names. Their printed row sizes remain
source context, without an inferred modern operator assignment.

Further counterpart review links 42 sign impressions to existing Boston designs
and seven impressions to the eight additional GPO drawings. `sign-components.json`
retains exact crops, correspondence reasons and the unresolved source questions.

The [medical and algebraic source proof](../specimens/signs-medical-algebraic-review.pdf) compares the selected native crops with monochrome and tonal vectors. These eight small signs use vector differences between fitted nested thresholds to avoid beads caused by separately fitting one-pixel tonal bands. The flared twelve-point angle retains a small native break near the end of its lower hairline; no inferred line segment is substituted.

Native geometry also links 36 further impressions to existing Boston symbols.
Closely spaced equality uses a center-separation/length ratio near0.21;
triangle, square, rectangle and comparison-angle references preserve observed
proportions. A right-pointing angle is recorded as a 180-degree use of its
left-pointing counterpart. Paper flecks and weak strokes remain evidence of the
impression and do not create additional icon identities. Exact locators and
correspondence reasons remain in `sign-components.json` and `sign-witness-review.json`.

Three further geometrical-proportion forms have nearly square dot grids with
center pitches approximately 0.31, 0.44 and 0.54 of the bar length. Native Boston
counterparts have different horizontal/vertical pitch proportions. A tall
outlined triangle is shared by the algebraic and astronomical settings and
legends; its complete algebraic impression is preferred. Pixel measurements
in `sign-geometry-review.json` support correspondence decisions only. All four
drawings trace native ink; no idealized geometry replaces their contours.

The [geometric source proof](../specimens/signs-geometric-review.pdf) shows the
four distinct constructions in native, monochrome and tonal form at large and
small display sizes.

The document-division GPO specimen supplies independent sign witnesses on
printed page 53 (archive leaf 111). `sign-crossbook-review.json` records exact
comparisons and retained crops. The narrow italic percent, plain-ended scruple,
widely separated equality strokes, broad comparison angle, detached-bar plus-minus
and narrow acute angle use complete native jobroom impressions. Weak joins and
broken arcs elsewhere remain source gaps; they are not reconstructed. Plain
minus lengths and small-dot ink spread do not create duplicate identities.

The two-point waved rule on printed page 16 is retained as three consecutive
complete periods. The original JP2 and full grayscale PNG are preserved. Its
fine stroke spans about two native pixels; `prepare_wave_sampling.py` creates an
explicitly labelled eightfold bilinear working crop for subpixel fitting. This
interpolation adds no source detail. Threshold 225 retains the connected stroke;
215, 225 and 235 define the disjoint tone regions. The smooth Potrace corner
threshold of 1.334 avoids introducing sharp corners at native pixel steps.
A rigid rotation of +0.1613215 degrees corrects the measured whole-strip drift.
No sinusoid, mirrored period, stretched axis or filled gap replaces the printing.
The observed variation and unequal terminal sections remain visible; this strip
is not a perfected seamless tile. `waved-rule-review.json` records the exact
native crop, derivation, measurements and comparisons to existing wave designs.

Four unequal double-rule faces preserve the observed line-weight and gap
proportions of the labelled four-, six-, ten- and twelve-point specimens.
The four- and twelve-point drawings use the clearer 1897 printed page 80;
the six- and ten-point drawings use 1904 printed page 16. Full native scans
and both later matching impressions remain in the source inventory.
The mixed-rule-review.json record gives the source choice and rigid rotation.
A 48-pixel local paper normalization supports the earlier unevenly lit page.
The complete strips retain uniform scale and source edge variation. The small
break in the twelve-point lower hairline and its slight bow are preserved;
no invented rectangles or filled gaps replace the historical impression.
At small display sizes these long, fine strips lose their separate lines;
the recommended minimum is 512 pixels for the four- and twelve-point strips
and 256 pixels for the six- and ten-point strips. Printed point sizes describe
the historical rule bodies, rather than the normalized digital em.

Four leader patterns preserve compact dots and three distinct hyphen-to-gap
relationships. The specimens show many arbitrary stock lengths and metal body
sizes; these remain individual witnesses of the same repeated constructions.
The leader-review.json record accounts for 33 impressions from the 1897, 1900
and 1904 GPO books, with native width, pitch and baseline measurements.
Four consecutive dots and three consecutive hyphens per pattern retain the
native mark variation. The original 1904 page supplies the clearest selected
runs. The wider-spaced strip uses three cleaner later marks from the twelve-point
specimen, avoiding an uneven ink shoulder in an earlier trial run.
Eightfold bilinear grayscale sampling supports subpixel fitting without adding
scan detail. The prepare_leader_sampling.py script reproduces every derived
crop. The tracing recipes retain exact thresholds and one rigid rotation from
the complete run's measured baseline. No copied marks, synthetic circles or
rectangles, independent-axis stretching or filled gaps replace the source.
The 64-pixel minimum preserves useful mark separation. Repeated layout still
needs the observed native phase; the stripped glyph bearings do not themselves
encode a seamless tiling interval.

The half-blunt and single-rule corners retain the complete long-armed shapes
printed under their respective brass-rule headings. Eleven existing Boston
components and signs provide comparison evidence in corner-review.json; their
relative weights and proportions differ from these two printing faces.
Fourfold bilinear grayscale sampling avoids the pointed ends and width jumps
introduced by tracing one-pixel masks. It adds no source detail. Explicit masks
remove neighboring stock lengths and one isolated paper cloud above the single
rule; they do not touch either arm. The reproducible sampling helper and full
native page preserve those decisions.
Two fitted native directions establish a small global scan correction, making
the axes perpendicular while preserving length along each direction. Local ink
variation remains. The single-rule corner has a small printed gap at its join;
no synthetic connecting line replaces it. A matching intact witness remains
the preferred basis for improving that join. Recommended minimum sizes are
128 pixels for the half-blunt corner and 256 pixels for the finer corner.

The beveled leader-body diagram comes from the explicitly labeled BODY column,
beside the hyphen printing faces. It is a technical illustration of the metal
body. The six-, eight- and ten-point examples remain separate source witnesses
of that construction, including their native curvature and aspect variations.
One canonical diagram uses the six-point impression, which has less internal
ink loss than the larger examples. The related Baltimore space rules have
different thin strokes and turned ends and are not used as replacement sources.
The body-diagram-review.json record preserves these comparisons and source boxes.
The outline retains uniform native proportions and receives one rigid rotation
from a robust fit to the straight shank edges. The 64-pixel minimum component
area removes disconnected paper specks without filling holes inside the body.
No analytic rectangle, wedge or replacement end contour substitutes for the
observed illustration. The recommended minimum display size is 128 pixels.

The Document Division specimen supplies ten ornamental dash constructions from
eleven named impressions on printed page 66. A and H share a diamond-and-bead
center; their different outer line lengths remain separate source witnesses.
The more continuous H impression supplies that drawing. Comparisons distinguish
solid from hollow centers, the proportions of the compact diamond, rounded beads,
flared shoulders, and the different collar and wedge sequences. The complete
native source and close comparison records are in document-dash-review.json.
Fourfold bilinear grayscale sampling supports subpixel tracing without adding
source detail. A 48-sample-pixel paper normalization precedes thresholding.
Each complete dash receives one rigid rotation from a robust grayscale fit to
both outer plain arms. Source proportions, minor edge variation and remaining
weak ink are retained. No synthetic lines, mirrored ends or copied beads replace
the observed printing. The B impression retains a small left-arm gap. The four
more intricate collar and wedge designs have a 512-pixel recommended minimum;
the other six have a 256-pixel minimum. Smaller renderings lose fine distinctions.

Document Division brass rules 20 and 21 on printed page 66 provide two compound
printing faces. No. 20 places a shallow wave above a straight hairline. No. 21
places a filled scalloped band above a fine waved line. Each drawing preserves
three consecutive observed periods, selected clear of the attached metal-body
illustration. The source context, repeat phase and comparisons are retained in
document-compound-rule-review.json. Fourfold bilinear sampling and local paper
normalization support subpixel tracing. One rigid rotation follows the lower
straight rule of No. 20 or the straight bottom edge of No. 21's upper band.
Native proportions, uneven ink and minor edge wear remain. The recommended
minimum sizes are 64 pixels for No. 20 and 128 pixels for No. 21.

Document Division rules 18, 19, 22 and 23 retain four paired printing-face
profiles. No. 18 is a wider-spaced fine pair; No. 19 has a modestly heavier
upper stroke; Nos. 22 and 23 pair a heavier upper stroke with a fine lower
stroke at different relative separations. Measurements at three positions and
native-detail comparisons distinguish these profiles from the existing pairs.
The revived interior segments preserve the complete two-stroke construction.
Their cropped ends are not presented as isolated historical terminals; full
face/body context remains on the retained page. Fourfold bilinear sampling and
one rigid rotation retain native proportions and edge variation. See
document-paired-rule-review.json for source boxes and comparison evidence.
Document rule 24 is a further witness of the existing Job Room six-point
profile, despite its eight-point body label. The clearer Job Room drawing
remains preferred. Recommended minimum display size for the four new segments
is 128 pixels.

The plain-rule construction review retains 230 GPO source impressions: 198
printing faces, stock lengths and plain dashes, and 32 rectangular body-width
illustrations. These use the elementary straight rectangular construction
already represented by the Boston Series E rules. The correspondence is at
construction level; it does not equate source proportions, optical weights,
physical matrices or technical purpose. Body illustrations remain identified as
metal-width diagrams, separately from their printing faces. Historical lengths,
face classes, body labels and native comparison rectangles remain in
`plain-rule-construction-review.json`. The retained source images preserve their
original proportions and attached joins. Existing artwork is retained; these
comparison rectangles are not replacement tracing crops. The review PDF shows
representative native contexts and the existing Boston and Baltimore rules.

`rule-composition-review.json` resolves the component relationships in 43 brass-
rule demonstrations: 35 printing-face/metal-body comparisons, four Job Room
stock arrangements, three nested Document Division frames and their stock
layout. Each face and body remains a separate source record, with the native
caption and any joined boundary retained in context. Frame geometry records
three measured positions on each of the twelve straight edges. The frames use
existing plain-rule construction; their joined corners are not assumed to be
impressions of the isolated Job Room casting. Visible inner-frame corner gaps
remain evidence. The composition review adds no extra glyph for stock lengths,
body dimensions or nested frame sizes. Its proof preserves the original native
arrangements, and every component link identifies the supplying inventory.

The unnumbered wreath below the Document Division Celtic specimens on printed
page 40 retains eighteen three-bladed leaf groups and two separate dots. It is
recorded as one complete ornament: this page does not establish separate movable
leaf pieces. Native comparisons against wreaths, circular ornaments and rotated
visual candidates found no matching complete design or isolated leaf unit.
The retained scan is soft. Threshold 225 preserves the faint inner blades;
three disjoint regions use 200/225/230 after local paper normalization. A tighter
crop excludes a detached paper mark to the right. No leaf was copied, no gap
filled and no oval reshaped. A rigid rotation of +0.174271758 degrees aligns
the two measured dot centroids. See document-wreath-review.json for source
boxes, comparisons, measurements and the continuing sharper-witness search.
The recommended minimum display size is 256 pixels.

The Celtic No. 2 business card on Job Room printed page 39 is an assembled
example of six identified type settings and four plain rules. Each rule links
to the existing Boston E3 unornamented construction, with original dimensions,
orientation and measured native width retained. This correspondence does not
assert shared metal stock or identical isolated terminals. The left joins have
small native gaps; the right joins are softer and largely connected. Neither
establishes a new corner design. No frame icon, redrawn joint or replacement
outline is added. Source axes, profiles, type-family links and native corners
are retained in celtic-card-frame-review.json and its review proof.

Selected matching Bruce1828 impressions improve engraving detail. The exact native crop rectangles, previous and selected witnesses, thresholds and reasons are retained in bruce1828-quality-revisions.json. The glyph overrides preserve each stable ID, codepoint and advance, including all tone regions where applicable. Previous sources remain in reference/. No absent content is reconstructed.

The compact font outlines for Capitol Nos. 29, 31 and 32 are bound to the current aligned masters. Nos. 29 and 32 use the documented coverage-screen method to preserve faint borders and apparent shading; this screening is a modern font-format interpretation. No. 31 uses ordinary binary reduction. `capitol-font-format-review.json` and `specimens/capitol-format-review.pdf` record the comparisons at 48, 96, 192 and 384 pixels. Full-detail master and SVG drawings, identifiers and advances are preserved.
