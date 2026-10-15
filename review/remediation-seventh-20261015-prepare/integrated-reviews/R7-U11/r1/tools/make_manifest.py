"""Final manifest excludes only itself; final immutable commit/tree binds itself."""
import hashlib
import json
from pathlib import Path
OUT=Path(__file__).resolve().parent.parent
REPO=Path('/workspace/r7-ir-R7-U11/review-checkout')
rows=[]
for p in sorted(OUT.rglob('*')):
    if not p.is_file() or p==OUT/'artifact-manifest.json':continue
    b=p.read_bytes()
    rows.append({'path':p.relative_to(REPO).as_posix(),'bytes':len(b),
                 'sha256':hashlib.sha256(b).hexdigest(),
                 'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest(),
                 'git_mode':'100644'})
(OUT/'artifact-manifest.json').write_text(json.dumps({
    'schema':'r7.u11.actual-review-artifact-manifest.r1.v1',
    'files':rows,'nonself_files':len(rows),'nonself_bytes':sum(x['bytes'] for x in rows),
    'self_binding':'Excluded only this manifest; immutable final commit/tree and full remote file-byte readback bind it externally',
    'qualification':'Transport identities, not semantic/runtime/model configuration proof'
},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest_files':len(rows),'nonself_bytes':sum(x['bytes'] for x in rows)}))
