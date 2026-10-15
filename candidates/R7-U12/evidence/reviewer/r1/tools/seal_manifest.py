"""Bind all actual reviewer evidence except this manifest's own recursive hash."""
import datetime
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
rows=[]
for path in sorted(root.rglob('*')):
    if not path.is_file() or path==root/'artifact-manifest.json':continue
    assert not path.is_symlink()
    data=path.read_bytes()
    rows.append({'path':'candidates/R7-U12/evidence/reviewer/r1/'+path.relative_to(root).as_posix(),
                 'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                 'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest(),'mode':'100644',
                 'baseline':'ABSENT_AT_FIXED_B'})
obj={'schema':'r7.u12.reviewer-artifact-manifest.v1','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'baseline_commit':'e646432c644dec04d306842cc5a559a29c718fbc','branch':'codex/r7-u12-reviewer-20261015-r1',
     'write_set':'candidates/R7-U12/evidence/reviewer/r1/ only','files_except_manifest_self':rows,
     'nonself_count':len(rows),'nonself_bytes':sum(r['bytes'] for r in rows),
     'self_binding':'Final actual commit/tree plus exhaustive remote file readback bind this manifest. No recursive/future self hash.',
     'transport_policy':'First ordinary evidence push and full readback may be followed only by evidence receipt/manifest additions. Final readback is returned outside its own commit to avoid recursion.',
     'effective_model_configuration':'UNVERIFIED','integrated_PASS':False,'ACCEPTED':False,'CLOSED':False}
(root/'artifact-manifest.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest_nonself_count':len(rows),'manifest_nonself_bytes':obj['nonself_bytes']}))
