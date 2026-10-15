"""Validate this review's serialization and enumerate all deliverable byte identities."""
import hashlib
import json
from pathlib import Path
import subprocess

TOOLS=Path(__file__).resolve().parent
OUT=TOOLS.parent
REPO=TOOLS.parents[5]
PREFIX='candidates/R7-U04/evidence/reviewer/r1/'
def identity(data):return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())
per_id=json.loads((OUT/'per-id.json').read_bytes())
assert [r['id'] for r in per_id['records']]==['GR7-M03-001','GR7-M03-002']
for r in per_id['records']:
    assert r['verdict']=='PASS_SCOPED_CANDIDATE' and not r['required_revisions']
    assert not r['formal_ACCEPTED'] and not r['CLOSED'] and not r['actual_integrated_PASS']
    assert r['execution']['behavior_vectors']=='NOT_EXECUTED'
    assert len(r['vectors'])==6
    for v in r['vectors']:
        a=v['candidate_anchor']
        data=(Path('/workspace/r7-review-input/R7-U04-242e1f9fb2fbdf7d609bcdb6de0a95547f9f4c6a/candidate')/a['path']).read_bytes()
        lo,hi=a['byte_offsets_half_open']
        assert identity(data)==a['file_identity'] and identity(data[lo:hi])==a['span_identity']
        assert v['execution']=='NOT_EXECUTED'
for p in OUT.rglob('*'):
    assert not p.is_symlink()
    if p.is_file() and p.suffix=='.json':json.loads(p.read_bytes())
    if p.is_file() and p.suffix=='.jsonl':
        for line in p.read_text().splitlines():json.loads(line)
diff=subprocess.check_output(['git','diff','--name-only','e646432c644dec04d306842cc5a559a29c718fbc'],cwd=REPO).decode().splitlines()
untracked=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=REPO).decode().splitlines()
assert all(p.startswith(PREFIX) for p in diff+untracked)
validation=dict(schema='r7.u04.r1.deliverable-validation.v1',status='DOCUMENT_IDENTITIES_AND_SCOPE_CHECKED',vector_count=12,record_count=2,json_and_jsonl_parse=True,candidate_span_identities=True,reviewer_only_scope=True,domain_execution='NOT_EXECUTED',semantic_credit_from_this_tool=0,formal_ACCEPTED=False,CLOSED=False)
(TOOLS/'review-validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n')
files=[p for p in OUT.rglob('*') if p.is_file() and p!=OUT/'artifact-manifest.json']
rows=[dict(path=str(p.relative_to(REPO)),git_mode='100644',**identity(p.read_bytes())) for p in sorted(files)]
manifest=dict(schema='r7.u04.r1.reviewer-artifact-manifest.v1',batch_id='R7-U04',branch='codex/r7-u04-reviewer-20261015-r1',base='e646432c644dec04d306842cc5a559a29c718fbc',allowed_prefix=PREFIX,files=rows,file_count_excluding_self=len(rows),bytes_excluding_self=sum(r['bytes'] for r in rows),self_binding='This manifest is excluded from its own identities; final external Git commit/tree and full remote readback bind it.',domain_execution='NOT_EXECUTED',formal_ACCEPTED=False,CLOSED=False)
(OUT/'artifact-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
for row in rows:assert identity((REPO/row['path']).read_bytes())=={k:row[k] for k in ['bytes','sha256','git_blob']}
print(json.dumps(dict(status='ARTIFACT_MANIFEST_MATCH',files=len(rows)+1,bytes=sum(r['bytes'] for r in rows)+(OUT/'artifact-manifest.json').stat().st_size,domain_execution='NOT_EXECUTED')))
