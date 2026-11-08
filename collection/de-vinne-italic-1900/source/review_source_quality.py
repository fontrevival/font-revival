"""Reproduce native evidence, threshold and delivery-format proofs for this family."""
from pathlib import Path
import json,textwrap
from PIL import Image,ImageDraw
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from fontTools.ttLib import TTFont
from fontTools.pens.basePen import BasePen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.svgLib.path import parse_path

F=Path(__file__).resolve().parent.parent
meta=json.loads((F/'font.json').read_text())
review=json.loads((F/'source/italic-quality-review.json').read_text())
selected=review['selected'];pt=review['point_size'];target=selected['character']
fonts={ext:TTFont(F/('fonts' if ext in ('otf','ttf') else 'web')/(meta['postscript_name']+'.'+ext)) for ext in ('otf','ttf','woff','woff2')}
output=F/'specimens/source-quality-review.pdf'
c=Canvas(str(output),pagesize=(612,792),invariant=1)
c.setTitle(meta['name']+' source-quality review');c.setAuthor('Harold Lehmann')

class OutlinePen(BasePen):
    def __init__(self,path):super().__init__(None);self.p=path
    def _moveTo(self,p):self.p.moveTo(*p)
    def _lineTo(self,p):self.p.lineTo(*p)
    def _curveToOne(self,a,b,c):self.p.curveTo(*a,*b,*c)
    def _closePath(self):self.p.close()
    def _endPath(self):pass

def label(x,y,text,size=9):
    c.setFont('Helvetica',size);c.setFillColorRGB(0,0,0);c.drawString(x,y,text)

def paragraph(text,x,y,width=91,size=9):
    for line in textwrap.wrap(text,width):label(x,y,line,size);y-=13
    return y

def heading(title,note):
    label(36,756,title,15);paragraph(note,36,735)

def glyph(font,ch):
    gs=font.getGlyphSet();name=font.getBestCmap()[ord(ch)];pen=SVGPathPen(gs);gs[name].draw(pen)
    return dict(path=pen.getCommands(),advance_width=font['hmtx'][name][0])

def draw(shape,x,y,size=72,colour=(0,0,0),stroke=False):
    c.saveState();c.translate(x,y);c.scale(size/1000,size/1000)
    c.setFillColorRGB(*colour);c.setStrokeColorRGB(*colour);c.setLineWidth(8)
    p=c.beginPath();parse_path(shape['path'],OutlinePen(p));c.drawPath(p,fill=int(not stroke),stroke=int(stroke));c.restoreState()

def words(text,font,x,y,size,old=False):
    for ch in text:
        shape=review['previous_drawing'] if old and ch==target else glyph(font,ch)
        draw(shape,x,y,size);x+=shape['advance_width']*size/1000

def source_image(box,x,y,width,height):
    with Image.open(F/selected['native_file']) as im:crop=im.convert('RGB').crop(box)
    scale=min(width/crop.width,height/crop.height);w,h=crop.width*scale,crop.height*scale
    c.drawImage(ImageReader(crop),x,y+height-h,w,h)

heading(meta['name']+' / native source',f'Version {meta["version"]}; printed page {selected["printed_page"]}, archive leaf {selected["archive_leaf"]}.')
paragraph(review['source']['rights'],36,701)
source_image(review['setting_context_box'],36,545,540,123)
label(36,526,'Complete point-labelled setting; prices are excluded from character coverage.')
source_image(selected['native_box'],36,287,220,210)
label(36,267,'Native crop; neighbouring ink remains visible.')
draw(glyph(fonts['otf'],target),345,315,180)
label(300,267,f'Observed {target}; threshold {selected["threshold"]}; advance {selected["drawing"]["advance_width"]}')
paragraph(selected['decision'],36,231)
paragraph('The complete glyph is traced from one impression. No holes are filled, strokes drawn, outlines assembled from parts, or widths stretched. One measured scale and rigid rotation preserve source proportions and the historical italic slant.',36,135)
c.showPage()

fit=selected['accepted_physical_scale']
heading('Independent capital comparison','Black: retained canonical capitals. Red outline: source impressions at one uniform scale.')
label(36,703,f'{fit["dimension_pairs"]//2} capitals; scale {fit["scale"]:.6f}; RMS {fit["rms_residual_font_units"]:.2f} font units.')
group=[e for e in review['comparisons'] if e['role']=='capital-scale-comparison']
for i,e in enumerate(group):
    x=36+i%4*140;y=590-i//4*190;label(x,y+77,e['character']+' / '+e['id'],8)
    draw(glyph(fonts['otf'],e['character']),x,y,90);draw(e['drawing'],x,y,90,(.8,.05,.05),True)
paragraph(review['identity_limit'],36,61)
c.showPage()

heading('Threshold and contour comparison','Each trial uses the same independent capital scale and measured text-row baseline.')
group=sorted([e for e in review['comparisons'] if e['role']=='quality-candidate'],key=lambda e:(e['id'],e['threshold']))
columns=5 if pt==8 else 3;step=112 if pt==8 else 190
for i,e in enumerate(group):
    x=36+i%columns*step;y=556-i//columns*245
    label(x,y+111,e['id'],7);label(x,y+95,'Threshold '+str(e['threshold']),8)
    if review['previous_drawing']:
        draw(review['previous_drawing'],x,y,105);draw(e['drawing'],x,y,105,(.8,.05,.05),True)
    else:draw(e['drawing'],x+20,y,112)
    label(x,y-39,str(len(e['white_island_areas']))+' closed counters',8)
paragraph('The black comparison outline is the retained census g; red outlines are Ryan impressions.' if pt==8 else 'The lowest threshold breaks the lower contour. The selected threshold 155 retains two apertures and the observed bar and terminal extents.',36,169)
paragraph('Selected: '+selected['id']+', threshold '+str(selected['threshold'])+'. '+review['identity_limit'],36,125)
c.showPage()

heading('Desktop and web format comparison',f'Whole observed {target}; same source position and advance in all four delivery formats.')
samples=['Stars $2468','Honor $25'] if pt==6 else ['Tumbling Vaulting','gags and giggling']
if review['previous_drawing']:
    label(36,698,'Previous census g in the same text and spacing',9);words(samples[0],fonts['otf'],36,663,25,old=True)
for i,(ext,font) in enumerate(fonts.items()):
    y=590-i*130;label(36,y+42,ext.upper(),10)
    words(samples[0],font,36,y,30);words(samples[1],font,36,y-35,18)
    words(samples[0],font,345,y-35,12)
paragraph('Existing advances and feature mappings are preserved. '+('This font adds one observed dollar.' if pt==6 else 'Only g is replaced; the lining R remains available through ss01.'),36,56)
c.showPage()

heading('Native text baseline','Red: measured baseline through independent whole-letter anchors. Source pixels are enlarged for inspection.')
row=selected['accepted_row'];group=[e for e in review['comparisons'] if e['id'] in row['anchor_ids']]
for i,e in enumerate(group):
    x=36+i%5*112;y=450-i//5*225
    label(x,y+210,e['id'],7);label(x,y+196,e['character'],10)
    with Image.open(F/e['native_file']) as im:
        box=e['box'];crop=im.convert('RGB').crop(box);mag=4;crop=crop.resize((crop.width*mag,crop.height*mag),Image.Resampling.NEAREST)
        pen=ImageDraw.Draw(crop)
        pen.line([(0,(row['baseline_intercept']+row['slope']*box[0]-box[1])*mag),(crop.width-1,(row['baseline_intercept']+row['slope']*box[2]-box[1])*mag)],fill=(220,0,0),width=1)
    scale=min(102/crop.width,170/crop.height);w,h=crop.width*scale,crop.height*scale
    c.drawImage(ImageReader(crop),x,y+175-h,w,h)
paragraph(f'{len(group)} anchors; slope {row["slope"]:.8f}; baseline intercept {row["baseline_intercept"]:.6f} native pixels. The target glyph does not determine its own vertical placement.',36,123)
paragraph('A rigid rotation corrects scan skew. No shear or individual width adjustment is applied. Source overshoots and printing differences remain visible.',36,75)
c.showPage();c.save()
for font in fonts.values():font.close()
print('Wrote',output)
