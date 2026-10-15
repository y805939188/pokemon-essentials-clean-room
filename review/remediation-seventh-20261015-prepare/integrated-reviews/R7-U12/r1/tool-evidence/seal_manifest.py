"""List every result file; self is bound by immutable Git commit/tree externally."""
from pathlib import Path
import hashlib
import json

root=Path(__file__).resolve().parent.parent
manifest=root/'artifact-manifest.json'
rows=[]
for p in sorted(root.rglob('*')):
    if not p.is_file() or p==manifest:continue
    data=p.read_bytes()
    rows.append(dict(path=p.relative_to(root).as_posix(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
        git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),mode='100644'))
manifest.write_text(json.dumps(dict(schema='r7.u12.actual-review-artifact-manifest.v1',files=rows,
    count_nonself=len(rows),bytes_nonself=sum(r['bytes'] for r in rows),
    self_binding='No recursive self hash. Final actual immutable result commit/tree, exhaustive Git file table and full remote-byte readback bind this manifest.',
    scope='Only integrated-reviews/R7-U12/r1 evidence; WAIT for both required IDs; no MI body or author mirror.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(nonself_files=len(rows),nonself_bytes=sum(r['bytes'] for r in rows))))
