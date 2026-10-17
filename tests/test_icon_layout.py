"""Catalogue layout data stays numeric, source-relative and safe to consume."""
import json,math,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class IconLayoutTests(unittest.TestCase):
 def test_recipes_refer_to_real_collection_assets_and_have_finite_geometry(self):
  recipes=json.loads((ROOT/'site/icon-layout.json').read_text())['icons']
  ids={i['id'] for f in (ROOT/'collection').glob('*/font.json') for i in json.loads(f.read_text()).get('icons',[])}
  self.assertTrue(set(recipes)<=ids)
  for key,r in recipes.items():
   self.assertIn(r['kind'],['repeat','frame','corner','motif'],key)
   for name in ['inkBox','tile']:
    if name not in r:continue
    box=r[name];self.assertEqual(len(box),4,key);self.assertTrue(all(isinstance(v,(int,float)) and math.isfinite(v) for v in box),key);self.assertGreater(box[2],0,key);self.assertGreater(box[3],0,key)
   if r['kind']=='repeat':
    self.assertIn(r['join'],['continuous','spaced']);self.assertIn('tile',r)
    x,y,w,h=r['inkBox'];a,b,c,d=r['tile'];self.assertTrue(x-.01<=a and y-.01<=b and a+c<=x+w+.01 and b+d<=y+h+.01,key)
