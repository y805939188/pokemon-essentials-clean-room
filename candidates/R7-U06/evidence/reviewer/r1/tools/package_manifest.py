"""List the exact reviewer payload. Manifest self-identity comes from Git/readback."""
import datetime
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
checkout=root.parents[4]
rows=[]
for p in sorted(root.rglob('*')):
    if not p.is_file() or p==root/'artifact-manifest.json':continue
    assert not p.is_symlink()
    data=p.read_bytes()
    rows.append({'path':str(p.relative_to(checkout)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
                 'git_blob_content_id':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest(),'git_mode':'100644'})
manifest={'schema':'r7.u06.reviewer-artifact-manifest.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'fixed_B':'e646432c644dec04d306842cc5a559a29c718fbc','branch':'codex/r7-u06-reviewer-20261015-r1',
          'candidate_commit':'fd0c1e6f50587331846921d446d893f1c1e84f3d','candidate_tree':'113069992c0d13f80c41312c26f2143a9e31c15f',
          'reviewer_thread_id':'01a13ff0-6000-748c-a2ed-b6965f662032','files':rows,
          'self_identity_rule':'Manifest excluded from own hash list; final commit/tree and exhaustive immutable remote readback include it.',
          'configuration':'Effective model/effort/tier/speed UNVERIFIED','behavior_vectors':'NOT_EXECUTED',
          'verdict':'PASS_SCOPED_CANDIDATE for both required IDs only','integrated_PASS':False,'ACCEPTED':False,'CLOSED':False}
(root/'artifact-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'nonself_files':len(rows),'nonself_bytes':sum(r['bytes'] for r in rows),'manifest_self':'BOUND_EXTERNALLY_BY_COMMIT_TREE_AND_READBACK'}))
