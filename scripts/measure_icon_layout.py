#!/usr/bin/env python3
"""Propose catalogue border recipes; inspect repeat proofs before accepting.

Run from the repository root with requirements-display.txt installed. This is
source preparation, not part of the release build. It replaces icon-layout.json;
reviewed hand adjustments are reapplied from icon-layout-overrides.json.
"""
import json,sys,math,xml.etree.ElementTree as ET
from pathlib import Path
sys.path.insert(0,'scripts')
from fontTools.svgLib.path import parse_path
from fontTools.pens.boundsPen import BoundsPen
from outline_raster import rasterize
from PIL import Image,ImageDraw
import numpy as np
icons=json.load(open('icons.json'))['icons'];layout={};measurements=[]
for it in icons:
 tags=it['tags'];key=it['id'];border=it['type']=='ornaments' and any(t in tags for t in ['border','corner','repeat','frame']);extra=('p255-11pt-' in key or 'shipped' in it['name'].lower() or key in ['baltimore-1832-p127-62','baltimore-1832-p127-63','baltimore-1832-p67-eight-line-pica-oak-leaf-a','boston-1889-p237-art72-a'])
 if not (border or extra):continue
 f=Path('collection')/it['collection'];paths=[];boxes=[]
 for j,el in enumerate(ET.parse(it['multitone']['svg']).iter('{http://www.w3.org/2000/svg}path')):
  name=it['multitone_layers'][j]['glyph'];override=f/'source/glyphs'/f'{name}.json';p=json.load(open(override))['path'] if override.exists() else el.attrib['d'];paths.append(p);pen=BoundsPen(None);parse_path(p,pen)
  if pen.bounds:boxes.append(pen.bounds)
 x0=min(b[0] for b in boxes);x1=max(b[2] for b in boxes);y0=min(b[1] for b in boxes);y1=max(b[3] for b in boxes);box=[math.floor(x0),-math.ceil(y1),math.ceil(x1)-math.floor(x0),math.ceil(y1)-math.floor(y0)]
 kind='corner' if 'corner' in tags or '-corner' in key else 'frame' if '-frame' in key or (key.startswith('baltimore') and it['pdf_page'] in [131,167,169]) or '-composition' in key else 'repeat' if ('repeat' in tags or 'tile' in tags or '-unit' in key or 'check-' in key or '-3pt-border-' in key or key.endswith(('floriated-16','floriated-17','grimaldi-4','grimaldi-8','grimaldi-11','grimaldi-12'))) else 'motif'
 entry={'kind':kind,'inkBox':box}
 if kind=='repeat':
  # A complete strip carries end treatments; measure a central repeating span.
  tile=list(box);continuous=True
  if 'strip' in tags or 'check-' in key:
   width=3600;scale=width/box[2];height=max(4,math.ceil(box[3]*scale));mask=rasterize(paths[0],width,height,scale,(-box[0]*scale,-box[1]*scale));a=np.asarray(mask,dtype=float)/255
   # Reject the end treatments and use mean vertical ink, robust to a small skew.
   v=a.sum(axis=0);v=v[width//8:-width//8];lo=max(5,round(height*.18));hi=min(len(v)//3,max(lo+1,round(height*5)));scores=[]
   for p in range(lo,hi):
    aa=v[:-p];bb=v[p:];den=np.mean(aa*aa+bb*bb)+1e-9;scores.append((float(np.mean((aa-bb)**2)/den),p))
   # Earliest strong local minimum avoids selecting a multi-period harmonic.
   minima=[(s,p) for k,(s,p) in enumerate(scores) if 0<k<len(scores)-1 and s<=scores[k-1][0] and s<scores[k+1][0]]
   if minima:
    best=min(s for s,p in minima);score,period=next(((s,p) for s,p in minima if s<=max(.035,best*1.45)),min(minima))
    period/=scale;count=max(1,round(box[3]/period));span=period*count
    center=box[0]+box[2]/2;tile=[round(center-span/2,3),box[1],round(span,3),box[3]]
    measurements.append({'id':key,'period':round(period,3),'cycles':count,'score':round(score,4),'tile':tile})
  # Round or isolated sorts are evenly spaced rather than cut at mitres.
  if '-unit' in key or any(t in tags for t in ['rosette','medallion']) and box[2]/box[3]<1.3:continuous=False
  entry.update(tile=tile,join='continuous' if continuous else 'spaced')
 layout[key]=entry
overrides=json.load(open('site/icon-layout-overrides.json'))['icons']
for key,value in overrides.items():
 if key not in layout:raise ValueError('Unknown override '+key)
 layout[key].update(value['layout'])
print('measured',len(layout),'icons,',len(measurements),'strips',flush=True)
Path('site/icon-layout.json').write_text(json.dumps({'schema_version':1,'coordinate_system':'SVG viewBox; x, y, width, height. Layout crops do not alter the historical master.','icons':layout},indent=2)+'\n')
Path('site/icon-layout-measurements.json').write_text(json.dumps(measurements,indent=2)+'\n')
