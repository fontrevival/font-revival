"""Make source, figure-feature and punctuation proofs from retained evidence."""
from pathlib import Path
import argparse,json
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.reportLabPen import ReportLabPen
from fontTools.svgLib.path import parse_path
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

class CanvasPen(ReportLabPen):
    def _closePath(self):self.path.close()

def review(family,font_path,output):
    font=TTFont(font_path);gs=font.getGlyphSet();cmap=font.getBestCmap()
    record=json.loads((family/'source/figure-punctuation-review.json').read_text())
    lining={'0':'zero.tall','1':'one.lining','2':'two.lining','5':'five.lining','7':'seven.lining','9':'nine.lining'}
    c=canvas.Canvas(str(output),pagesize=(612,792),invariant=1);c.setTitle('De Vinne 18pt: lining figures and poster punctuation');c.setAuthor('Harold Lehmann')
    def title(text,subtitle):
        c.setFont('Helvetica-Bold',16);c.drawString(24,760,text)
        c.setFont('Helvetica',9);c.drawString(24,739,subtitle)
    def glyph(name,x,y,size,path=None):
        c.saveState();c.translate(x,y);c.scale(size/1000,size/1000);p=c.beginPath()
        if path is None:gs[name].draw(CanvasPen(gs,p))
        else:parse_path(path,CanvasPen(None,p))
        c.drawPath(p,fill=1,stroke=0);c.restoreState()
    def text(line,x,y,size,feature=None):
        for ch in line:
            name=lining.get(ch,cmap[ord(ch)]) if feature=='lnum' else 'zero.tall' if feature=='ss01' and ch=='0' else cmap[ord(ch)]
            glyph(name,x,y,size);x+=font['hmtx'][name][0]*size/1000
    def native(e,x,y,w,h):
        im=Image.open(family/e['native_file']).convert('RGB').crop(e['native_box']);factor=min(w/im.width,h/im.height)
        c.drawImage(ImageReader(im),x,y,width=im.width*factor,height=im.height*factor)
    def notes(lines,y):
        c.setFont('Helvetica',9)
        for line in lines:c.drawString(24,y,line);y-=15
    title('Observed lining figures','GPO 1904, printed page 124 / archive leaf 140. Native crops enlarged independently.')
    for i,e in enumerate(r for r in record['selected'] if r['alternate']):
        x=24+i*94;c.setFont('Helvetica-Bold',10);c.drawString(x,709,e['glyph'])
        native(e,x,585,76,110);glyph(e['glyph'],x,470,110)
        c.setFont('Helvetica',8);c.drawString(x,447,'Threshold 150')
    c.setFont('Helvetica-Bold',10);c.drawString(24,413,'Default figures');text('0123456789',24,350,64)
    c.setFont('Helvetica-Bold',10);c.drawString(24,305,'lnum: observed lining set');text('0123456789',24,240,64,'lnum')
    notes(['Five new lining alternatives join the improved zero.tall. Existing 3, 4, 6 and 8 serve both settings.',
           'Each native row retains its measured baseline and rigid rotation at one fixed page scale.',
           'Source differences in figure height and overshoot remain; no numeral is stretched to a common top.',
           'The selected zero is an intact repeated impression. The damaged central zero is comparison only.',
           'All earlier encoded outlines and advances remain unchanged.'],175)
    c.showPage()
    title('Tall zero: clearer source impression','The ss01 substitution and 555-unit advance are preserved. The short zero remains encoded.')
    prior=record['prior_handy_zero'];current=next(r for r in record['selected'] if r['glyph']=='zero.tall')
    for x,label,e in [(60,'Earlier Handy source, page 338',prior['source']),(340,'Selected GPO source, page 124',current)]:
        c.setFont('Helvetica-Bold',10);c.drawString(x,708,label);native(e,x+25,520,125,165)
    glyph(None,90,330,190,prior['drawing']['path']);glyph('zero.tall',370,330,190)
    c.setFont('Helvetica',9);c.drawString(60,303,'Version 1.001 outline');c.drawString(340,303,'Version 1.002 outline')
    c.setStrokeColorRGB(.7,.75,.8);c.line(60,330,548,330)
    text('760 1000 1900 0.00',24,240,36,'ss01');text('760 1000 1900 0.00',24,190,24,'ss01')
    notes(['The larger GPO witness supplies a more even intact oval and counter without filling printing defects.',
           'Thirteen common capitals establish poster scale; 47 matched header centers transfer it to this page.',
           'The zero retains its measured row position. Its advance is preserved by horizontal centering only.',
           'Four-times Lanczos sampling and threshold 150 retain one outer contour and one counter.'],135)
    c.showPage()
    title('Observed poster punctuation','GPO 1904, printed page 120 / archive leaf 136. Fixed page scale and measured row baselines.')
    for i,e in enumerate(r for r in record['selected'] if not r['alternate']):
        x=24+i*144;c.setFont('Helvetica-Bold',10);c.drawString(x,710,f'U+{ord(e["character"]):04X}')
        native(e,x,565,90,125);glyph(cmap[ord(e['character'])],x,485,95)
    y=430
    for size in [36,24,18,12,8]:
        c.setFont('Helvetica',8);c.drawString(24,y+14,f'{size}pt')
        text('Oh, lunch: late lunch;',76,y,size);y-=size*1.3+5
        text('I’m late; will I jump?',76,y,size);y-=size*1.3+22
    notes(['Colon and semicolon retain two components; the question mark retains its separate dot.',
           'The apostrophe is U+2019. No straight apostrophe alias or opening quote is inferred.'],40)
    c.showPage()
    title('Figure settings at several sizes','Default and lnum use the same size and baseline; the 3, 4, 6 and 8 outlines are shared.')
    y=680
    for size in [36,24,18,12,8]:
        for feature in [None,'lnum']:
            c.setFont('Helvetica',8);c.drawString(24,y,f'{size}pt '+(feature or 'default'))
            text('0123456789 1904 12,345.67',105,y,size,feature);y-=size*1.35+14
        y-=16
    notes(['Figure alternatives remain unencoded and are selected through OpenType substitutions.',
           'ss01 selects the tall zero alone; lnum selects the six alternate forms as one complete lining set.',
           'All six alternatives and both features are checked in OTF, TTF, WOFF and WOFF2.'],110)
    c.save();font.close()

if __name__=='__main__':
    family=Path(__file__).resolve().parent.parent;m=json.loads((family/'font.json').read_text())
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font',type=Path,default=family/'fonts'/(m['postscript_name']+'.otf'))
    parser.add_argument('--output',type=Path,default=family/'specimens/figure-punctuation-review.pdf')
    args=parser.parse_args();review(family,args.font,args.output)
