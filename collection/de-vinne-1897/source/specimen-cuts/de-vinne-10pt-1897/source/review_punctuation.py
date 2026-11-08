"""Render native punctuation evidence, settings and four-format comparisons."""
from pathlib import Path
import json
import sys
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.reportLabPen import ReportLabPen
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'scripts/fontrevival.py').is_file())
sys.path.insert(0,str(ROOT/'scripts'))
import fontrevival as fr

class ClosedPen(ReportLabPen):
    def _closePath(self):self.path.close()

def text_vector(c,font,text,x,y,size):
    gs=font.getGlyphSet();cmap=font.getBestCmap()
    c.saveState();c.translate(x,y);c.scale(size/1000,size/1000)
    for ch in text:
        name=cmap[ord(ch)];path=c.beginPath();gs[name].draw(ClosedPen(gs,path));c.drawPath(path,fill=1,stroke=0)
        c.translate(font['hmtx'][name][0],0)
    c.restoreState()

def review(family):
    read=lambda p:json.loads(p.read_text())
    m=read(family/'font.json');evidence=read(family/'source/punctuation-review.json');pt=evidence['point_size']
    f=TTFont(family/'fonts'/(m['postscript_name']+'.otf'))
    output=family/'specimens/punctuation-review.pdf'
    c=canvas.Canvas(str(output),pagesize=(1200,1000),invariant=1)
    c.setTitle(m['name']+' | Whole observed punctuation');c.setAuthor('Harold Lehmann')
    def title(t,sub):
        c.setFont('Helvetica-Bold',20);c.drawString(28,960,m['name']+' | '+t)
        c.setFont('Helvetica',12);c.drawString(28,935,sub)
    title('Native sources and fitted outlines','Whole impressions; one measured setting scale and native row baseline. Source crops enlarged independently for inspection.')
    for j,e in enumerate(evidence['selected']):
        x=25+j*390
        c.setFont('Helvetica-Bold',14);c.drawString(x,890,f'U+{ord(e["character"]):04X}  {e["glyph_name"]}')
        c.setFont('Helvetica',11);c.drawString(x,868,e['book'])
        c.drawString(x,850,f'Printed {e["printed_page"]}, leaf {e["archive_leaf"]}, threshold {e["threshold"]}')
        im=Image.open(family/e['native_file']).convert('RGB').crop(e['native_box'])
        scale=min(150/im.width,240/im.height)
        c.drawImage(ImageReader(im),x+10,570,width=im.width*scale,height=im.height*scale)
        c.setStrokeColorRGB(.7,.76,.82);c.line(x+180,580,x+355,580);c.setStrokeColorRGB(0,0,0)
        text_vector(c,f,e['character'],x+195,580,240)
        c.setFont('Helvetica',11);c.drawString(x,535,f'Advance {e["recipe"]["advance_width"]}; baseline shown at right')
        c.drawString(x,513,f'Native box {e["native_box"]}')
        c.drawString(x,491,f'Scale {e["accepted_row"]["scale"]:.6f}; row rotation {e["accepted_row"]["rotation_degrees"]:.4f} degrees')
    c.setFont('Helvetica',13)
    for i,line in enumerate([
        'Capital comparisons establish physical scale; whole flat-footed lowercase forms establish each text-row baseline.',
        'Colon and semicolon retain two components. The apostrophe retains one. No filled holes or assembled parts.',
        'Four-times Lanczos sampling, normalization radius 48, blur 1.2 and tolerance 0.8; modern 35-unit sidebearings.',
        'Processed NYPL apostrophes retain stepped native edges. Cleaner matching impressions remain a quality task.',
        'The source evidence supports matching optical forms; it does not identify physical punches or matrices.'
    ]):c.drawString(28,390-i*26,line)
    c.showPage()
    title('Punctuation in words','Source size and enlarged settings; source-relative descenders and upper punctuation positions retained.')
    lines=['nature’s God; public sale','Well improved; orchard’s fruit']
    if pt!=6:lines+=['House at 7:23 o’clock','A.M. and 3:15 P.M.']
    assert set(''.join(lines))<=set(m['character_set'])
    y=885
    for size in [pt,16,28,48]:
        c.setFont('Helvetica',12);c.drawString(28,y,f'{size} point setting');y-=size+14
        for line in lines:
            text_vector(c,f,line,28,y,size);y-=size*1.35+3
        y-=20
    assert y>35,('word page overflow',pt,y)
    c.showPage()
    title('Observed character coverage','Existing letters, figures, fractions, advances and feature substitutions are preserved.')
    before='nature’s God; public sale';base='natures God public sale'
    c.setFont('Helvetica',14);c.drawString(28,875,'Previously available base text')
    for size,y in [(64,770),(32,690),(16,640)]:text_vector(c,f,base,28,y,size)
    c.setFont('Helvetica',14);c.drawString(28,530,'Observed punctuation added')
    for size,y in [(64,425),(32,345),(16,295)]:text_vector(c,f,before,28,y,size)
    c.setFont('Helvetica',13);c.drawString(28,180,'No unsupported ASCII apostrophe, opening single quote or other companion is inferred.')
    c.showPage()
    title('Four delivery formats','Each format preserves the selected whole contours, advances and source-relative position.')
    text='n; n’ n' if pt==6 else 'n: n; n’ 7:23 o’clock'
    for j,(folder,ext) in enumerate([('fonts','otf'),('fonts','ttf'),('web','woff'),('web','woff2')]):
        g=TTFont(family/folder/(m['postscript_name']+'.'+ext));y=850-j*195
        c.setFont('Helvetica-Bold',14);c.drawString(28,y,ext.upper())
        c.setStrokeColorRGB(.7,.76,.82);c.line(28,y-98,1165,y-98);c.setStrokeColorRGB(0,0,0)
        text_vector(c,g,text,28,y-98,78)
        text_vector(c,g,lines[0],28,y-145,24)
        g.close()
    c.showPage();c.save();f.close()
    print(output)

if __name__=='__main__':
    review(Path(__file__).resolve().parent.parent)
