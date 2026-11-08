"""Generate the native-source and named-alternate comparison PDF."""
from pathlib import Path
import argparse
import json
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.reportLabPen import ReportLabPen
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


class CanvasPen(ReportLabPen):
    def _closePath(self):
        self.path.close()


def review(family, font_path, output):
    font = TTFont(font_path)
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    alternatives = json.loads((family/'source/alternates.json').read_text())['glyphs']
    selections = {e['glyph_name']:e for e in json.loads((family/'source/selection.json').read_text())
                  if 'glyph_name' in e}
    measurements = json.loads((family/'source/measurements.json').read_text())['rows']
    substitutions = {}
    for record in font['GSUB'].table.FeatureList.FeatureRecord:
        mapping = {}
        for index in record.Feature.LookupListIndex:
            for subtable in font['GSUB'].table.LookupList.Lookup[index].SubTable:
                mapping.update(subtable.mapping)
        substitutions[record.FeatureTag] = mapping
    c = canvas.Canvas(str(output), pagesize=(612,792), invariant=1)
    c.setTitle('De Vinne 12pt 1897 — observed source alternatives')
    c.setAuthor('Harold Lehmann')

    def glyph(name, x, y, scale):
        c.saveState();c.translate(x,y);c.scale(scale,scale)
        path = c.beginPath();glyphs[name].draw(CanvasPen(glyphs,path))
        c.drawPath(path,fill=1,stroke=0);c.restoreState()

    def text(line, x, y, size, features=()):
        for ch in line:
            name = cmap[ord(ch)]
            for tag in features: name = substitutions[tag].get(name,name)
            glyph(name,x,y,size/1000)
            x += font['hmtx'][name][0]*size/1000

    for i,(name,entry) in enumerate(alternatives.items()):
        if i % 2 == 0:
            c.setFont('Helvetica-Bold',15);c.drawString(24,762,'De Vinne 12pt: observed alternatives')
            c.setFont('Helvetica',9);c.drawString(24,744,'Uniform source scale; default and alternate share a baseline. No inferred complete figure set.')
        y = 468 if i%2 == 0 else 138
        selected = selections[name]
        ch = selected['character']
        feature = next(tag for tag,m in substitutions.items() if name in m.values())
        c.setFont('Helvetica-Bold',12);c.drawString(24,y+238,f'{name}  ({feature})')
        c.setFont('Helvetica',8);c.drawString(24,y+222,selected['selected'])
        c.drawString(24,y+202,'Native source');c.drawString(225,y+202,'Default');c.drawString(400,y+202,'Alternate')
        crop = Image.open(family/entry.get('native_file', entry['file'])).crop(entry.get('native_box', entry['box'])).convert('RGB')
        scale = measurements[selected['row']]['scale']*.16
        c.drawImage(ImageReader(crop),24,y+180-crop.height*scale,width=crop.width*scale,height=crop.height*scale)
        c.saveState();c.setStrokeColorRGB(.65,.72,.8);c.line(220,y+30,585,y+30);c.restoreState()
        glyph(cmap[ord(ch)],230,y+30,.16);glyph(name,410,y+30,.16)
        text(ch*3,230,y-25,24);text(ch*3,410,y-25,24,[feature])
        if i%2 == 1 or i == len(alternatives)-1: c.showPage()
    c.setFont('Helvetica-Bold',15);c.drawString(24,762,'Figure stylistic sets at text and display sizes')
    c.setFont('Helvetica',9);c.drawString(24,744,'ss01: census M; ss02: 1897 figures 0/1/3/5/9; ss03: job-room figures 2/4.')
    y = 705
    for size in [36,24,16,11]:
        for features in [(),('ss01',),('ss02',),('ss03',),('ss01','ss02','ss03')]:
            c.setFont('Helvetica',8);c.drawString(24,y,str(size)+'pt '+('/'.join(features) or 'default'))
            text('MIM 0123456789 1435',145,y,size,features)
            y -= size*1.3
        y -= 20
    c.save()


if __name__ == '__main__':
    family = Path(__file__).resolve().parent.parent
    meta = json.loads((family/'font.json').read_text())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font',type=Path,default=family/'fonts'/(meta['postscript_name']+'.otf'))
    parser.add_argument('--output',type=Path,default=family/'specimens/alternates-review.pdf')
    args = parser.parse_args()
    review(family,args.font,args.output)
