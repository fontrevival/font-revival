"""Closed contour clipping with exact cubic subdivision, retaining winding."""
from fontTools.misc.bezierTools import splitCubicAtT,solveCubic
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.svgLib.path import parse_path

def contours(svg):
 rec=RecordingPen();parse_path(svg,rec);out=[];segments=[];point=None;start=None
 for op,args in rec.value:
  if op=='moveTo':point=start=args[0]
  elif op=='lineTo':segments.append((point,args[0]));point=args[0]
  elif op=='curveTo':
   assert len(args)==3
   segments.append((point,*args));point=args[-1]
  elif op in ['closePath','endPath']:
   if point!=start:segments.append((point,start))
   if segments:out.append(segments)
   segments=[];point=start=None
  else:raise ValueError(op)
 assert not segments
 return out

def clip_plane(segments,axis,bound,sign):
 kept=[]
 for s in segments:
  if len(s)==2:
   a,b=s[0][axis],s[1][axis]
   roots=[(bound-a)/(b-a)]if a!=b and 0<(bound-a)/(b-a)<1 else []
   if roots:
    t=roots[0];q=tuple(x+(y-x)*t for x,y in zip(*s));pieces=[(s[0],q),(q,s[1])]
   else:pieces=[s]
  else:
   p,q,r,t=[p[axis]for p in s]
   roots=sorted(set(v for v in solveCubic(-p+3*q-3*r+t,3*p-6*q+3*r,-3*p+3*q,p-bound)if 1e-10<v<1-1e-10))
   pieces=splitCubicAtT(*s,*roots)if roots else [s]
  for piece in pieces:
   middle=(piece[0][axis]+piece[-1][axis])/2 if len(piece)==2 else sum(p[axis]*w for p,w in zip(piece,[1,3,3,1]))/8
   if sign*(middle-bound)>=-1e-8:kept.append(piece)
 if not kept:return []
 closed=[];last=kept[-1][-1]
 for s in kept:
  if last!=s[0]:closed.append((last,s[0]))
  closed.append(s);last=s[-1]
 return closed

def clip(contour_list,box):
 x0,y0,x1,y1=box;pen=SVGPathPen(None)
 for original in contour_list:
  segments=original
  for axis,bound,sign in [(0,x0,1),(0,x1,-1),(1,y0,1),(1,y1,-1)]:
   segments=clip_plane(segments,axis,bound,sign)
   if not segments:break
  if not segments:continue
  pen.moveTo(segments[0][0])
  for s in segments:
   if len(s)==2:pen.lineTo(s[1])
   else:pen.curveTo(*s[1:])
  pen.closePath()
 return pen.getCommands()
