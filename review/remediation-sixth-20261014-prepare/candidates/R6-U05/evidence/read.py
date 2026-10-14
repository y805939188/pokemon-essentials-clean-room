#!/usr/bin/env python3
import sys,json,hashlib,datetime,subprocess
from pathlib import Path
e=Path(__file__).resolve().parent
r=e.parents[2]
kind,path,start,end=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
inputs=json.loads((r/'inputs/frozen-inputs.json').read_text())
commit=inputs['reference_commit'] if kind=='source' else '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
if kind=='source':
 p=Path('/tmp/r6-u05-frozen/Maruno17/pokemon-essentials')/commit/path
elif kind=='formal': p=r.parents[1]/path
else: p=r/'inputs/evidence'/path
b=p.read_bytes(); lines=b.decode().splitlines()
id={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
if kind in ['source','formal']:
 row=next(x for x in inputs['source_materials' if kind=='source' else 'formal_materials'] if x['path']==path)
 assert all(row[k]==id[k] for k in id)
else:
 index=json.loads((r/'inputs/evidence/index.json').read_text())
 rows=index.values() if isinstance(index,dict) else index
 # Evidence identity is separately validated in input-validation.json.
assert 1<=start<=end<=len(lines),(path,start,end,len(lines))
rec={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'kind':kind,'path':path,'commit':commit,'identity':id,'range':[start,end],'line_count':len(lines),'level':'SOURCE_STATIC','emitted_complete_range':True}
with (e/'reading-ledger.jsonl').open('a') as f: f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(kind,path,str(start)+'-'+str(end))
for i in range(start,end+1): print(str(i)+': '+lines[i-1])
