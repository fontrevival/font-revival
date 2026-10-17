#!/usr/bin/env python3
"""Proof every catalogue repeat at a common height, retaining a review PDF.

Run from the repository root. Optional first argument is the PNG output folder.
"""
import json,sys,xml.etree.ElementTree as ET,math
from pathlib import Path
sys.path.insert(0,'scripts')
from outline_raster import rasterize
from PIL import Image,ImageDraw
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
out=Path(sys.argv[1] if len(sys.argv)>1 else "workspace/border-review");out.mkdir(parents=True,exist_ok=True)
icons={i['id']:i for i in json.load(open('icons.json'))['icons']};layouts=json.load(open('site/icon-layout.json'))['icons'];rows=[]
for key,e in layouts.items():
 if e['kind']!='repeat':continue
 it=icons[key];paths=[]
 for i,el in enumerate(ET.parse(it['multitone']['svg']).iter('{http://www.w3.org/2000/svg}path')):
  f=Path('collection')/it['collection']/'source/glyphs'/(it['multitone_layers'][i]['glyph']+'.json');paths.append(json.load(open(f))['path'] if f.exists() else el.attrib['d'])
 x,y,w,h=e['tile'];sc=55/h;tw=max(1,round(w*sc));tile=Image.new('RGBA',(tw,55))
 for p,opacity in zip(paths,[1,.55,.25]):
  mask=rasterize(p,tw,55,sc,(-x*sc,-y*sc)).point(lambda a:round(a*opacity));ink=Image.new('RGBA',tile.size);ink.putalpha(mask);tile=Image.alpha_composite(tile,ink)
 row=Image.new('RGB',(460,95),'#fffaf0');d=ImageDraw.Draw(row);d.text((5,3),key.replace('baltimore-1832-','').replace('boston-1889-',''),fill='black')
 for x in range(4,455,tw):row.paste(tile,(x,25),tile)
 rows.append(row)
pdf=Canvas("docs/border-repeat-review.pdf",pagesize=(828,798),invariant=1)
for start in range(0,len(rows),42):
 chunk=rows[start:start+42];sheet=Image.new('RGB',(1380,math.ceil(len(chunk)/3)*95),'#fffaf0')
 for j,row in enumerate(chunk):sheet.paste(row,((j%3)*460,(j//3)*95))
 sheet.save(out/f'joins-{start//42+1}.png')
 pdf.drawImage(ImageReader(sheet),0,798-sheet.height*.6,width=828,height=sheet.height*.6);pdf.showPage()
pdf.save()
print(len(rows),'repeat previews; docs/border-repeat-review.pdf')
