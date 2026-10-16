"""Lossless additional finite original-qualification reading, not verdict transfer."""
from pathlib import Path
import json,hashlib,re,collections
P=Path(__file__).resolve().parent
old=json.loads((P/'semantic-atlas/associations.json').read_text())
seen={json.dumps(g['value'],ensure_ascii=False,sort_keys=True):g['id'] for g in old['groups']}
source=json.loads((P/'originals/r5-quarantined-scope.json').read_text())
skip={'source_baseline','specification_baseline','source_anchors','spec_anchors','affected_files','reviewer','canonical_input','source_path','path','commit','sha256','git_blob','bytes','line_ranges','lines','pointer','record_sha256','original_object','original_source'}
groups={};admin=[];reuse=[]
def walk(v,p='',ignored=False):
 if isinstance(v,dict) and v:
  for k,x in v.items():walk(x,p+'/'+str(k).replace('~','~0').replace('/','~1'),ignored or k in skip)
 elif isinstance(v,list) and v:
  for i,x in enumerate(v):walk(x,p+'/'+str(i),ignored)
 else:
  key=json.dumps(v,ensure_ascii=False,sort_keys=True)
  if ignored or isinstance(v,str) and re.fullmatch(r'[0-9a-f]{8,64}',v):admin.append(p)
  elif key in seen:reuse.append({'pointer':p,'exact_read_group':seen[key]})
  else:groups.setdefault(key,{'value':v,'pointers':[]})['pointers'].append(p)
walk(source)
out=P/'nonmandatory-reads';out.mkdir(exist_ok=True)
chunks=[];pieces=[];weight=0
for i,g in enumerate(groups.values()):
 g['id']=f'N{i+1:04d}';s=g['id']+' '+g['pointers'][0]+'\n'+json.dumps(g['value'],ensure_ascii=False)+'\n\n';w=sum(1 if ord(c)>127 else .25 for c in s)
 if pieces and weight+w>5500:chunks.append(pieces);pieces=[];weight=0
 pieces.append(s);weight+=w
if pieces:chunks.append(pieces)
manifest=[]
for i,c in enumerate(chunks):
 b=''.join(c).encode();name=f'chunk-{i+1:02d}.txt';(out/name).write_bytes(b);manifest.append({'file':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'status':'UNREAD'})
(out/'associations.json').write_text(json.dumps({'source':'originals/r5-quarantined-scope.json','groups':list(groups.values()),'same_context_exact_reuse':reuse,'identity_inventory_pointers':admin,'credit':'Only after exact values and context are actually read'},ensure_ascii=False,indent=2)+'\n')
(out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'new_values':len(groups),'exact_already_read':len(reuse),'identity_routes':len(admin),'chunks':len(chunks),'bytes':sum(r['bytes'] for r in manifest)}))
