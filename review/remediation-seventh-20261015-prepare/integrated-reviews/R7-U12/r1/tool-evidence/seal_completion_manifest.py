"""Bind every nonself artifact of the completed review; no recursive self hash."""
from pathlib import Path
import hashlib
import json

root = Path(__file__).resolve().parent.parent
manifest = root/'artifact-manifest.json'
files=[]
for path in sorted(root.rglob('*')):
    if not path.is_file() or path==manifest:
        continue
    data=path.read_bytes()
    files.append(dict(path=path.relative_to(root).as_posix(),bytes=len(data),
        sha256=hashlib.sha256(data).hexdigest(),
        git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
        mode='100644'))
manifest.write_text(json.dumps(dict(schema='r7.u12.completed-actual-review-manifest.v1',
    files=files,count_nonself=len(files),bytes_nonself=sum(x['bytes'] for x in files),
    scope='Only integrated-reviews/R7-U12/r1 evidence. Two completed finite static actual '
        'verdicts; historical WAIT and original tooling remain historical. No MI body or '
        'candidate mirror and no acceptance/closure.',
    self_binding='Manifest itself is bound by real immutable result commit/tree and '
        'exhaustive remote-byte readback produced after publication.'),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(nonself_files=len(files),nonself_bytes=sum(x['bytes'] for x in files))))
