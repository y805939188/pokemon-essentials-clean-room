import hashlib,json
from pathlib import Path
r=Path(__file__).resolve().parents[1]
rows=[]
for p in sorted(r.rglob('*')):
 if not p.is_file() or p.name=='artifact-manifest.json':continue
 assert '__pycache__' not in str(p)
 d=p.read_bytes();rows.append(dict(path=str(p.relative_to(r)),bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()))
(r/'artifact-manifest.json').write_text(json.dumps(dict(schema='r7.u02.actual-review-artifacts.v1',root='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U02/r1/',files=rows,self_binding='Manifest itself and all files are externally bound by final immutable commit/tree and exhaustive remote HTTP/Git byte readback; no recursive self-hash',qualification='Identities and tool I/O do not replace semantic review; all behavior NOT_EXECUTED'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(nonself_files=len(rows),nonself_bytes=sum(x['bytes'] for x in rows))))
