"""Exact five raw-binding dependencies discovered while auditing the two selected records."""
import datetime,gzip,hashlib,importlib.util,json,subprocess
from pathlib import Path
E=Path(__file__).resolve().parent
C2='4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
pre='review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/'
bootstrap=Path('/workspace/r7-bootstrap/R7-U11-author')
spec=importlib.util.spec_from_file_location('restore',bootstrap/'tools/restore_container_context.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
rows=json.loads((bootstrap/'missing-bindings.json').read_bytes())
index=json.loads(subprocess.check_output(['git','show',C2+':'+pre+'payload-index.json']))
lookup={r['logical_path']:r for r in index['logical_files']}
objects={r['transport_path']:r for r in index['compressed_objects']}
receipt={'start_utc':m.utc(),'commit':C2,'selection':'Exact logical_path lookups only; no whole-package semantic scan','rows':[]}
for row in rows:
 logical='tasks/R7-C13/'+row['c13_snapshot']; r=lookup[logical]; obj=objects[r['transport_path']]
 assert r['bytes']==row['bytes'] and r['sha256']==row['sha256'] and r['git_blob_content_id']==row['content_git_blob']
 transport,io=m.fetch({'repository':'y805939188/pokemon-essentials-clean-room','commit':C2,'path':pre+r['transport_path']},{'bytes':obj['transport_bytes'],'sha256':obj['transport_sha256'],'git_blob_content_id':obj['transport_git_blob_content_id']})
 decoded=gzip.decompress(transport); actual=m.verify(decoded,r)
 dest=bootstrap/'supplemental'/(row['sha256']+'.raw');dest.parent.mkdir(parents=True,exist_ok=True)
 if dest.exists():assert dest.read_bytes()==decoded
 else:dest.write_bytes(decoded)
 receipt['rows'].append({'binding_id':row['binding_id'],'logical_path':logical,'transport_path':r['transport_path'],'local_path':str(dest),**actual,'transport':io,'qualification':row['qualification']})
receipt['end_utc']=m.utc();(E/'supplemental-restoration.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'EXACT_ADDITIONAL_BINDINGS_RESTORED','count':len(receipt['rows']),'bytes':sum(r['bytes'] for r in receipt['rows']),'semantic_credit':False}))
