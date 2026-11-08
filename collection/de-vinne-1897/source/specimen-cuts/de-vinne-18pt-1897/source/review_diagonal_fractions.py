"""Render native fraction evidence and the declared modern placement in text."""
from pathlib import Path
import argparse,json
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.reportLabPen import ReportLabPen
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

class CanvasPen(ReportLabPen):
    def _closePath(self):self.path.close()

def review(family,font_path,output):
    f=TTFont(font_path);gs=f.getGlyphSet();cmap=f.getBestCmap()
    record=json.loads((family/'source/diagonal-fractions-review.json').read_text())
    c=canvas.Canvas(str(output),pagesize=(612,792),invariant=1)
    c.setTitle('De Vinne 18pt: diagonal fractions and symbols');c.setAuthor('Harold Lehmann')
    def title(line,subtitle):
        c.setFont('Helvetica-Bold',15);c.drawString(24,760,line)
        c.setFont('Helvetica',9);c.drawString(24,739,subtitle)
    def text(line,x,y,size,lining=False):
        mapping={'0':'zero.tall','1':'one.lining','2':'two.lining','5':'five.lining','7':'seven.lining','9':'nine.lining'}
        for ch in line:
            name=mapping.get(ch,cmap[ord(ch)]) if lining else cmap[ord(ch)]
            c.saveState();c.translate(x,y);c.scale(size/1000,size/1000);p=c.beginPath()
            gs[name].draw(CanvasPen(gs,p));c.drawPath(p,fill=1,stroke=0);c.restoreState()
            x+=f['hmtx'][name][0]*size/1000
        assert x<590,(line,size,'proof overflow')
    images={}
    for start in range(0,len(record['selected']),4):
        title('Whole observed fractions and symbols','Native crops enlarged independently; font outlines retain their source physical proportions.')
        for j,e in enumerate(record['selected'][start:start+4]):
            y=665-j*155
            c.setFont('Helvetica-Bold',10);c.drawString(24,y,f'U+{ord(e["character"]):04X} / '+e['book'])
            c.setFont('Helvetica',9);c.drawString(24,y-16,f'Printed {e["printed_page"]}; archive {e["archive_leaf"]}; threshold {e["threshold"]}')
            native=e['native_file']
            if native not in images:
                im=Image.open(family/native).convert('RGB');rotation=e['native_rotation_clockwise']
                images[native]=im.rotate(-rotation,expand=True) if rotation else im
            im=images[native].crop(e['native_box']);scale=min(120/im.width,108/im.height)
            c.drawImage(ImageReader(im),40,y-132,width=im.width*scale,height=im.height*scale)
            text(e['character'],230,y-115,110)
            c.setFont('Helvetica',9);c.drawString(375,y-65,f'{e["expected_components"]} ink components')
            c.drawString(375,y-82,f'{e["expected_counters"]} counters')
        c.setFont('Helvetica',9);c.drawString(24,32,'No assembled fractions, filled holes, stretched forms or drawn repairs.');c.showPage()
    title('Modern mid-cap placement at source size','Row centers at 350 units. The historical charts do not establish a co-set text baseline.')
    y=665
    for size in [36,24,18,12,8]:
        c.setFont('Helvetica',8);c.drawString(24,y,f'{size}pt')
        for line in ['H 12½ inches; 3¾ pounds H','20¢ 50% ¼⅓⅔⅛⅜⅝⅞']:
            c.setStrokeColorRGB(.80,.83,.86);c.line(85,y,588,y)
            c.setStrokeColorRGB(.91,.92,.93);c.line(85,y+size*.7,588,y+size*.7)
            text(line,85,y,size);y-=size*1.6+18
    c.setFont('Helvetica',9);c.drawString(24,110,'Each complete row receives one rigid rotation and one translation; no glyph is height-normalized.')
    c.drawString(24,94,'The full-size fractions extend above capitals and below baseline within existing vertical metrics.')
    c.showPage()
    title('Fractions with both figure settings','Whole fraction forms retain source proportions beside observed figure variants.')
    y=680
    for size in [36,24,18,12,8]:
        for lining in [False,True]:
            c.setFont('Helvetica',8);c.drawString(24,y,f'{size}pt '+('lnum' if lining else 'default'))
            text('12½ 3¾ 20¢ 50% 1⅛ 7⅞',105,y,size,lining);y-=size*1.5+18
        y-=12
    c.setFont('Helvetica',9);c.drawString(24,60,f'Nine whole diagonal fractions plus cent and percent; {len(gs)-len(cmap)-1} figure alternatives remain unencoded.')
    c.save();f.close()

if __name__=='__main__':
    family=Path(__file__).resolve().parent.parent;m=json.loads((family/'font.json').read_text())
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font',type=Path,default=family/'fonts'/(m['postscript_name']+'.otf'))
    parser.add_argument('--output',type=Path,default=family/'specimens/diagonal-fractions-review.pdf')
    args=parser.parse_args();review(family,args.font,args.output)
