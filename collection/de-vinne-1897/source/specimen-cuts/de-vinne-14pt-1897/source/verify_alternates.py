"""Check observed unencoded alternatives and their features in every format."""
from pathlib import Path
import json
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen


def verify(family):
    meta=json.loads((family/'font.json').read_text())
    limits=json.loads((family/'source/alternate-limits.json').read_text())['glyphs']
    expected={'ss01':{'M':'M.census'},'ss02':{'one':'one.oldstyle','three':'three.oldstyle'},
              'ss03':{'two':'two.lining','four':'four.lining','five':'five.lining'}}
    labels={'ss01':'Census M','ss02':'1897 figure variants (1, 3)',
            'ss03':'Job-room figure variants (2, 4, 5)'}
    results=[]
    for folder,ext in [('fonts','otf'),('fonts','ttf'),('web','woff'),('web','woff2')]:
        path=family/folder/(meta['postscript_name']+'.'+ext)
        font=TTFont(path)
        assert set(font.getBestCmap())==set(map(ord,meta['character_set'])),path
        assert len(font.getGlyphOrder())==len(meta['character_set'])+len(limits)+1,path
        assert not set(limits)&set(font.getBestCmap().values()),'Alternatives must remain unencoded.'
        table=font['GSUB'].table
        mappings={}
        for record in table.FeatureList.FeatureRecord:
            mapping={}
            for index in record.Feature.LookupListIndex:
                lookup=table.LookupList.Lookup[index]
                assert lookup.LookupType==1
                for subtable in lookup.SubTable: mapping.update(subtable.mapping)
            mappings[record.FeatureTag]=mapping
            label=font['name'].getDebugName(record.Feature.FeatureParams.UINameID)
            assert label==labels[record.FeatureTag],(path,record.FeatureTag,label)
        assert mappings==expected,(path,mappings)
        scripts={r.ScriptTag:r.Script for r in table.ScriptList.ScriptRecord}
        for tag in ['DFLT','latn']:
            assert set(scripts[tag].DefaultLangSys.FeatureIndex)==set(range(3)),(path,tag)
        gs=font.getGlyphSet()
        for name,rule in limits.items():
            bp=BoundsPen(gs);gs[name].draw(bp);assert bp.bounds,(path,name)
            x0,y0,x1,y1=bp.bounds
            measures=dict(y_min=y0,y_max=y1,ink_width=x1-x0,ink_height=y1-y0)
            for key,value in measures.items():
                low,high=rule['bounds'][key]
                assert low<=value<=high,(path,name,key,value,[low,high])
            assert font['hmtx'][name][0]==rule['advance'],(path,name,'advance')
            pen=RecordingPen();gs[name].draw(pen)
            assert sum(op=='moveTo' for op,args in pen.value)==rule['contours'],(path,name,'contours')
        results.append(dict(format=ext,alternates=len(limits),substitutions=6,features=3,
                            exact_coverage=True,unencoded=True,bounds_advances_contours='pass'))
        font.close()
    return results


if __name__=='__main__':
    print(json.dumps(verify(Path(__file__).resolve().parent.parent),indent=2))
