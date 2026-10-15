"""Bind every review evidence file except this manifest's own recursive identity."""
import datetime
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
repo=root.parents[4]
assert repo==Path('/workspace/r7-u13-reviewer-checkout')
rows=[]
for path in sorted(root.rglob('*')):
    if not path.is_file() or path==root/'artifact-manifest.json': continue
    data=path.read_bytes()
    assert '__pycache__' not in path.parts
    assert path.parent==root or root/'tools' in path.parents
    rows.append(dict(path=str(path.relative_to(repo)),base='NEW_REVIEWER_EVIDENCE',bytes=len(data),
                     sha256=hashlib.sha256(data).hexdigest(),git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest(),git_mode='100644'))
manifest=dict(schema='r7-u13-reviewer-artifact-manifest.v1',observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    batch_id='R7-U13',review_round='r1',reviewer_thread='01a13ff1-4e91-74b4-ac83-5838dbb59018',
    branch='codex/r7-u13-reviewer-20261015-r1',base_commit='e646432c644dec04d306842cc5a559a29c718fbc',
    dispatch_commit='95c260d8f3fb4a171675dde877137fcd4c2f1c8d',freeze_commit='aa369555b0e8b6c8b077f964b54ed63d3b924f26',
    candidate_commit='5635c73ea14adc278961da0e3917c2d00d580a25',candidate_tree='e2c261a77a7268a5eb07e7e364ac257d9fed3e31',
    verdict='PASS_SCOPED_CANDIDATE',artifacts=rows,nonself_files=len(rows),nonself_bytes=sum(x['bytes'] for x in rows),
    self_binding='Manifest itself and final publish tail bound by actual result commit/tree and full detached remote readback; no recursive self-hash claimed.',
    qualifications=dict(effective_configuration='UNVERIFIED',behavior_vectors='NOT_EXECUTED',reference_host_Demo_native_media_real_save_replay=0,integrated_PASS=False,ACCEPTED=False,CLOSED=False))
(root/'artifact-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='REVIEWER_MANIFEST_FINALIZED',files_including_manifest=len(rows)+1,nonself_bytes=manifest['nonself_bytes'],only_scope='candidates/R7-U13/evidence/reviewer/r1/')))
