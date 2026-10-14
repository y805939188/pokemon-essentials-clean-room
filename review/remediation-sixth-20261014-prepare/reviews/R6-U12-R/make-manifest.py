import hashlib,json,sys,datetime
from pathlib import Path
root=Path(__file__).resolve().parent
records=[]
for p in sorted(root.rglob('*')):
 if not p.is_file() or p.name=='package-manifest.json':continue
 data=p.read_bytes();records.append({'path':str(p.relative_to(Path.cwd())),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),'mode':'100644','type':'blob'})
result={'schema':'r6.u12.review-finite-core-manifest.v1','written_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'candidate_commit':'caa090d8e396c08b09fb2d4d5067aa00f4d6c3cb','candidate_tree':'8f29be65173bb29d160aed74dbb6f7378fa81c2a','payloads':records,'payload_count_excluding_manifest':len(records),'bytes_excluding_manifest':sum(x['bytes'] for x in records),'self_excluded':'package-manifest.json; its actual bytes/blob and containing core commit/tree are checked externally','publication_tail':'Future actual core commit/push/readback receipts are a finite later tail. Final publication commit/tree and complete payload readback are external tool/final-response bindings.'}
root.joinpath('package-manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest_payloads':len(records),'bytes':result['bytes_excluding_manifest']}))
