"""Create the whole-source, format and setting proof for the broad S."""
from pathlib import Path
import json
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.reportLabPen import ReportLabPen
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

F = Path(__file__).resolve().parent.parent
m = json.loads((F/'font.json').read_text())
review = json.loads((F/'source/broad-s-review.json').read_text())
fonts = {ext:TTFont(F/folder/(m['postscript_name']+'.'+ext))
         for folder,ext in [('fonts','otf'),('fonts','ttf'),('web','woff'),('web','woff2')]}
font = fonts['otf']
pdf = F/'specimens/broad-s-review.pdf'
c = canvas.Canvas(str(pdf), pagesize=(1200,1000), invariant=1)
c.setTitle('De Vinne ten point: observed broad S')
c.setAuthor('Harold Lehmann')

class CanvasPen(ReportLabPen):
    def _closePath(self):
        self.path.close()

def label(text,x,y,size=12,bold=False):
    c.setFont('Helvetica-Bold' if bold else 'Helvetica',size)
    c.setFillColorRGB(0,0,0)
    c.drawString(x,y,text)

def glyph(f,name,x,baseline,size):
    c.saveState()
    c.translate(x,baseline)
    c.scale(size/1000,size/1000)
    c.setFillColorRGB(0,0,0)
    p = c.beginPath()
    f.getGlyphSet()[name].draw(CanvasPen(f.getGlyphSet(),p))
    c.drawPath(p,fill=1,stroke=0)
    c.restoreState()

def text(line,x,baseline,size,features=(),f=font):
    substitutions = {}
    table = f['GSUB'].table
    for tag in features:
        record = next(r for r in table.FeatureList.FeatureRecord if r.FeatureTag==tag)
        substitutions.update({k:v for i in record.Feature.LookupListIndex
                              for sub in table.LookupList.Lookup[i].SubTable
                              for k,v in sub.mapping.items()})
    for ch in line:
        name = f.getBestCmap()[ord(ch)]
        name = substitutions.get(name,name)
        glyph(f,name,x,baseline,size)
        x += f['hmtx'][name][0]*size/1000
    assert x<1180, (line,size,x)

def baseline(x,y,width):
    c.setStrokeColorRGB(.65,.72,.8)
    c.setLineWidth(.5)
    c.line(x,y,x+width,y)

def native(e,x,y,w,h):
    im = Image.open(F/e['native_file']).convert('RGB').crop(e['native_box'])
    scale = min(w/im.width,h/im.height)
    c.drawImage(ImageReader(im),x,y,width=im.width*scale,height=im.height*scale)

label('Two observed ten-point S forms',25,955,23,True)
label('Native crops are enlarged independently. Default and alternate outlines use one common font scale.',25,925)
selected = review['selected'][0]
for e,x,title in [(review['comparison_impressions'][0],25,'Handy narrow S'),
                  (selected,245,'Poster broad S, selected'),
                  (review['comparison_impressions'][1],465,'Handy co-set broad S')]:
    label(title,x,875,15,True)
    native(e,x,625,180,220)
label('Default',730,875,15,True)
label('ss04 / S.broad',945,875,15,True)
baseline(715,625,455)
glyph(font,'S',730,625,280)
glyph(font,'S.broad',945,625,280)
label('Handy printed page 189 / archive 208; selected poster: printed page 339 / archive 358.',25,590)
label('Both forms are co-set in MUSCLES on page 189. The narrow default is preserved.',25,568)
im = Image.open(F/review['comparison_impressions'][0]['native_file']).convert('RGB').crop([835,1441,1262,1487])
c.drawImage(ImageReader(im),25,420,width=1150,height=im.height/im.width*1150)
label('Eleven non-S poster capitals: 25.9377641 units/native pixel. Eight serif feet: no common rotation.',25,385)
label('Maximum baseline residual: 1 native pixel. S.broad ink: -1.86 to 706.62; advance: 722.',25,363)
label('Threshold 110, no hole filling or drawn repair. Modern 35-unit sidebearings; source edge variation retained.',25,341)
for y,size in [(250,72),(155,36),(95,24),(48,10)]:
    label(str(size)+' pt / ss04',25,y+6)
    baseline(160,y,990)
    text('MUSCLES SAMPLES',160,y,size,('ss04',))
c.showPage()

label('Desktop and web outline comparison',25,955,23,True)
label('Narrow default and broad alternate share the same 200-point scale and baseline.',25,925)
for row,(ext,f) in enumerate(fonts.items()):
    y = 750-row*205
    label(ext.upper(),25,y+100,18,True)
    baseline(160,y,990)
    glyph(f,'S',165,y,200)
    glyph(f,'S.broad',340,y,200)
    text('MUSCLES SALE',570,y,60,('ss04',),f)
    text('MUSCLES SALE',570,y-55,24,('ss04',),f)
c.showPage()

label('Default and broad S in words',25,955,23,True)
label('ss04 selects only S.broad. The census M and existing figure stylistic sets remain available.',25,925)
for row,size in enumerate([72,48,24,10]):
    y = 805-row*175
    label(str(size)+' pt / default',25,y+6,13,True)
    baseline(160,y,990)
    text('MUSCLES SAMPLES',160,y,size)
    label('ss04',25,y-65+6,11)
    baseline(160,y-65,990)
    text('MUSCLES SAMPLES',160,y-65,size,('ss04',))
label('Combined ss01 / ss02 / ss03 / ss04',25,145,15,True)
text('MS 0123456789 ¼½¾',25,98,48,('ss01','ss02','ss03','ss04'))
text('Samples of type, 10½ inches. Sales of 20¢.',25,45,24,('ss04',))
c.showPage()
c.save()
for f in fonts.values():
    f.close()
print(pdf)
