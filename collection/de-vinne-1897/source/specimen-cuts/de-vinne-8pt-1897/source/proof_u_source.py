"""Generate the retained-source and before/after U quality proof."""
from pathlib import Path
import json
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.reportLabPen import ReportLabPen
from fontTools.svgLib.path import parse_path
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

F=Path(__file__).resolve().parent.parent
m=json.loads((F/'font.json').read_text())
review=json.loads((F/'source/u-source-review.json').read_text())
fonts={ext:TTFont(F/folder/(m['postscript_name']+'.'+ext))
       for folder,ext in [('fonts','otf'),('fonts','ttf'),('web','woff'),('web','woff2')]}
font=fonts['otf']
pdf=F/'specimens/u-source-review.pdf'
c=canvas.Canvas(str(pdf),pagesize=(1200,1000),invariant=1)
c.setTitle('De Vinne eight point: clearer whole U source');c.setAuthor('Harold Lehmann')
class CanvasPen(ReportLabPen):
    def _closePath(self):self.path.close()
def label(s,x,y,size=12,bold=False):
    c.setFont('Helvetica-Bold' if bold else 'Helvetica',size);c.setFillColorRGB(0,0,0);c.drawString(x,y,s)
def glyph(f,name,x,y,size,before=False):
    c.saveState();c.translate(x,y);c.scale(size/1000,size/1000);c.setFillColorRGB(0,0,0)
    p=c.beginPath();pen=CanvasPen(f.getGlyphSet(),p)
    if before and name=='U':parse_path(review['previous']['drawing']['path'],pen)
    else:f.getGlyphSet()[name].draw(pen)
    c.drawPath(p,fill=1,stroke=0);c.restoreState()
def text(line,x,y,size,before=False,f=font):
    for ch in line:
        name=f.getBestCmap()[ord(ch)];glyph(f,name,x,y,size,before)
        advance=review['previous']['drawing']['advance_width'] if before and name=='U' else f['hmtx'][name][0]
        x+=advance*size/1000
    assert x<1180,(line,size,x)
def baseline(x,y,w):
    c.setStrokeColorRGB(.65,.72,.8);c.setLineWidth(.5);c.line(x,y,x+w,y)
def native(e,x,y,w,h):
    im=Image.open(F/e['native_file']).convert('RGB').crop(e['native_box']);scale=min(w/im.width,h/im.height)
    c.drawImage(ImageReader(im),x,y,width=im.width*scale,height=im.height*scale)

label('Clearer whole U, preserving the observed construction',25,955,23,True)
label('Native crops enlarged independently. Before and after outlines share one font scale and baseline.',25,925)
for e,x,title in [(review['previous']['recipe'],25,'Previous Census source'),(review['selected'],270,'Selected BYU poster source')]:
    label(title,x,875,15,True);native(e,x,600,205,245)
for before,x,title in [(True,620,'Before / advance 707'),(False,905,'After / advance 744')]:
    label(title,x,875,15,True);baseline(x,600,255);glyph(font,'U',x,600,300,before)
label('BYU printed page 598, archive leaf 600: U in PUBLIC. Threshold 130; no filled holes or drawn repair.',25,550)
label('Eleven non-U/S/M capitals: 13.4163876 units/native pixel. Fifteen serif feet: baseline 2694, zero robust slope.',25,526)
label('Maximum baseline residual: 2 native pixels. Current U ink: -18.84 to 696.96. Modern sidebearings remain 35 units.',25,502)
im=Image.open(F/review['selected']['native_file']).convert('RGB').crop([610,2627,2375,2710])
c.drawImage(ImageReader(im),25,385,width=1150,height=im.height/im.width*1150)
for i,before in enumerate([True,False]):
    y=285-i*130;label('Before' if before else 'After',25,y+6,15,True);baseline(160,y,990)
    text('PUBLIC USUAL COURT HOUSE',160,y,48,before)
    text('PUBLIC USUAL COURT HOUSE',160,y-48,24,before)
c.showPage()

label('The clearer U in all four font formats',25,955,23,True)
label('All other glyphs, advances, encoded coverage and feature mappings are preserved.',25,925)
for row,(ext,f) in enumerate(fonts.items()):
    y=750-row*205;label(ext.upper(),25,y+95,18,True);baseline(150,y,1000)
    glyph(f,'U',160,y,200);text('PUBLIC USUAL',400,y,60,f=f);text('COURT HOUSE',400,y-48,24,f=f)
c.showPage()

label('Before and after U in words',25,955,23,True)
label('Only U changes. The slightly wider source is preserved without independent horizontal compression.',25,925)
for row,size in enumerate([48,24,8]):
    y=805-row*240;label(str(size)+' pt / before',25,y+5,13,True);baseline(160,y,990)
    text('PUBLIC USUAL COURT HOUSE',160,y,size,True)
    label('After',25,y-80+5);baseline(160,y-80,990);text('PUBLIC USUAL COURT HOUSE',160,y-80,size)
label('The former Census recipe and drawing remain in u-source-review.json for repeatable comparison.',25,105)
label('Minor native edge variation is retained. No extra U alternate or cross-size substitution is introduced.',25,80)
c.showPage();c.save()
for f in fonts.values():f.close()
print(pdf)
