"""Readability transform retaining every layout rule and all its operands."""
from pathlib import Path
import json
R=Path(__file__).resolve().parent;d=json.loads((R/'decoded-layout.json').read_text());lines=[]
def js(v):return json.dumps(v,separators=(',',':'))
def anch(x):
 if x is None:return None
 assert x['format']==1
 return x['xy']
for tag in ['GSUB','GPOS']:
 v=d[tag];lines.append(tag+' SCRIPTS '+js(v['scripts'])+' FEATURES '+js(v['features']))
 for look in v['lookups']:
  lines.append(tag+' L'+str(look['index'])+' type='+str(look['type'])+' flag='+str(look['flag']))
  for sub in look['subtables']:
   t=dict(sub)
   if 'pairs' in t:
    t['pairs']=[[a,b,list(v1.items()),list(v2.items())] for a,b,v1,v2 in t['pairs']]
   if 'marks' in t:t['marks']=[[g,c,anch(a)] for g,c,a in t['marks']]
   if 'bases' in t:t['bases']=[[g,[anch(a) for a in anchors]] for g,anchors in t['bases']]
   # Pairs have fixed value-field sets within each subtable; name these once.
   if 'pairs' in t and t['pairs']:
    key1=[k for k,v in t['pairs'][0][2]];key2=[k for k,v in t['pairs'][0][3]]
    assert all([k for k,v in pair[2]]==key1 and [k for k,v in pair[3]]==key2 for pair in t['pairs'])
    t['pairValueFields']=[key1,key2];t['pairs']=[[a,b,[v for k,v in v1],[v for k,v in v2]] for a,b,v1,v2 in t['pairs']]
   lines.append(js(t))
lines.append('GDEF '+js(d['GDEF']));lines.append('kern '+js(d['kern']))
(R/'layout.read.txt').write_text('\n'.join(lines)+'\n')
print('bytes', (R/'layout.read.txt').stat().st_size)
