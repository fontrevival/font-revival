"""Create the source, format and setting proof for descending three and four."""
from pathlib import Path
import json
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.reportLabPen import ReportLabPen
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

F=Path(__file__).resolve().parent.parent
m=json.loads((F/'font.json').read_text())
review=json.loads((F/'source/descending-figures-review.json').read_text())
fonts={ext:TTFont(F/folder/(m['postscript_name']+'.'+ext))
       for folder,ext in [('fonts','otf'),('fonts','ttf'),('web','woff'),('web','woff2')]}
font=fonts['otf']
image=Image.open(F/review['selected'][0]['native_file']).convert('RGB')
pdf=F/'specimens/descending-figures-review.pdf'
c=canvas.Canvas(str(pdf),pagesize=(1200,1000),invariant=1)
c.setTitle('De Vinne eighteen point: observed descending three and four')
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
    p=c.beginPath()
    f.getGlyphSet()[name].draw(CanvasPen(f.getGlyphSet(),p))
    c.drawPath(p,fill=1,stroke=0)
    c.restoreState()

def text(line,x,baseline,size,feature=None,f=font):
    mapping={}
    if feature:
        table=f['GSUB'].table
        record=next(r for r in table.FeatureList.FeatureRecord if r.FeatureTag==feature)
        mapping={k:v for i in record.Feature.LookupListIndex for sub in table.LookupList.Lookup[i].SubTable
                 for k,v in sub.mapping.items()}
    for ch in line:
        name=f.getBestCmap()[ord(ch)]
        name=mapping.get(name,name)
        glyph(f,name,x,baseline,size)
        x+=f['hmtx'][name][0]*size/1000
    assert x<1180,(line,size,x)

def baseline(x,y,width):
    c.setStrokeColorRGB(.65,.72,.8)
    c.setLineWidth(.5)
    c.line(x,y,x+width,y)

label('Whole source impressions and observed positions',25,955,23,True)
label('ATF Desk Book, NYPL copy, printed523 / archive540. Native crops enlarged independently.',25,928)
label('One capital scale; nine text anchors; one rigid row rotation. Existing default outlines are preserved.',25,907)
for i,e in enumerate(review['selected']):
    x=25+i*590
    label(e['character']+' / '+e['glyph'],x,865,17,True)
    crop=image.crop(e['native_box'])
    factor=min(170/crop.width,260/crop.height)
    c.drawImage(ImageReader(crop),x,565,width=crop.width*factor,height=crop.height*factor)
    label('Native',x,540)
    label('Current default',x+200,540)
    label('Observed descending',x+390,540)
    baseline(x+195,640,370)
    glyph(font,font.getBestCmap()[ord(e['character'])],x+200,640,280)
    glyph(font,e['glyph'],x+390,640,280)
    label('Ink bounds: '+str(round(e['expected_bounds']['y_min'],2))+' to '+str(round(e['expected_bounds']['y_max'],2)),x,510)
    label('Advance: '+str(e['advance_width'])+'; contours: '+str(e['expected_contours'])+'; threshold:110',x,490)
context=image.crop([652,2730,5695,3020])
c.drawImage(ImageReader(context),25,360,width=1150,height=context.height/context.width*1150)
label('Source setting: nected them with another, and 234',25,330)
label('Scale:3.3783237 units/native pixel. Text rotation:-0.1061622 degrees. Maximum baseline residual:1.23 pixels.',25,302)
label('Both source forms remain intact at thresholds90/110/130; the selected threshold is110.',25,280)
label('Small native edge irregularities remain; no holes are filled or contours drawn to replace missing ink.',25,258)
for y,size in [(195,72),(113,36),(58,18)]:
    label(str(size)+' pt',25,y+4)
    baseline(115,y,1035)
    text('and 234; 34 43 3344',115,y,size,'onum')
c.showPage()

label('Desktop and web outline comparison',25,955,23,True)
label('Both alternatives at the same 200-point scale. Baselines and native size differences are preserved.',25,925)
for row,(ext,f) in enumerate(fonts.items()):
    y=750-row*205
    label(ext.upper(),25,y+100,18,True)
    baseline(160,y,990)
    glyph(f,'three.oldstyle',165,y,200)
    glyph(f,'four.oldstyle',340,y,200)
    text('and 234',570,y,72,'onum',f)
    text('34 43 234',570,y-55,24,'onum',f)
c.showPage()

label('Default, oldstyle and lining figure settings',25,955,23,True)
label('onum and ss02 select descending3/4. The other oldstyle positions use the existing defaults.',25,925)
for row,(title,feature) in enumerate([('Default',None),('Oldstyle (onum)','onum'),('Descending three and four (ss02)','ss02'),('Lining (lnum)','lnum')]):
    y=800-row*155
    label(title,25,y+78,17,True)
    baseline(25,y,1140)
    text('0123456789 234 34',25,y,72,feature)
label('Text samples with oldstyle figures',25,255,17,True)
for y,size,line in [(193,36,'Another 234 members; 34 years.'),(135,24,'Our independence; 234 and 43.'),(87,18,'34 43 234 3344; 12½ inches, 20¢.'),(48,14,'The complete alphabets and existing punctuation remain unchanged; 234.')]:
    baseline(25,y,1140)
    text(line,25,y,size,'onum')
c.showPage()
c.save()
for f in fonts.values():
    f.close()
print(pdf)
