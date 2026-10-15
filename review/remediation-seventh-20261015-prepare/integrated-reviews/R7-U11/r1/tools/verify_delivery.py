"""Check only this review's scope, identities, structured output and evidence links."""
import hashlib
import json
import subprocess
from pathlib import Path

OUT=Path(__file__).resolve().parent.parent
REPO=Path('/workspace/r7-ir-R7-U11/review-checkout')
ROOT=REPO.parent
PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U11/r1/'
B='e646432c644dec04d306842cc5a559a29c718fbc'
def git(*args): return subprocess.check_output(['git',*args],cwd=REPO)
def read(p):return json.loads(p.read_bytes())
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
assert git('branch','--show-current').decode().strip()=='codex/r7-ir-u11-20261015-r1'
changed=set(git('diff','--name-only',B,'--').decode().splitlines())
changed.update(git('ls-files','--others','--exclude-standard').decode().splitlines())
assert changed and all(p.startswith(PREFIX) for p in changed),sorted(changed)
assert git('rev-parse','HEAD:deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
for name in ['report.md','per-id.json','review-input-receipt.json','content-review-progress.json']:
    assert (OUT/name).is_file()
records=read(OUT/'per-id.json')
assert [x['record_id'] for x in records['records']]==['GR7-M16-001','GR7-M17-002']
assert all(x['verdict']=='PASS_SCOPED_ACTUAL_INTEGRATION' for x in records['records'])
assert records['ACCEPTED'] is False and records['CLOSED'] is False
spans=0
for record in records['records']:
    for f in record['actual_files']:
        assert all(identity((ROOT/'actual-input/actual'/f['path']).read_bytes())[k]==f[k] for k in ['bytes','sha256','git_blob'])
    for s in record['actual_clauses']:
        content=(ROOT/'actual-input/actual'/s['path']).read_bytes()
        a,b=s['byte_offsets_zero_based_half_open']
        assert identity(content[a:b])=={k:s[k] for k in ['bytes','sha256','git_blob']}
        c,d=s['lines_one_based_inclusive']
        assert b''.join(content.splitlines(keepends=True)[c-1:d])==content[a:b]
        spans+=1
    for v in record['vectors']:
        assert v['behavior_execution']=='NOT_EXECUTED'
        assert v['premise'] and v['independent_static_reason']
assert len(records['records'][1]['vectors'])==12
ledger=read(OUT/'content-review-progress.json')
assert len(ledger['mandatory_primary_files'])==14
assert all(x['complete_content_read'] for x in ledger['mandatory_primary_files'])
receipt=read(OUT/'review-input-receipt.json')
assert receipt['effective_configuration']==dict.fromkeys(['model','effort','tier','speed'],'UNVERIFIED')
assert read(OUT/'original-binding-audit.json')['normalized_U11_references']==217
assert len(read(OUT/'shared-approval-audit.json')['rows'])==8
reconstruction=read(OUT/'clause-reconstruction.json')['files']
assert len(reconstruction)==24 and sum(len(x['hunks']) for x in reconstruction)==56
assert sum(x['exact_reconstruction'] for x in reconstruction)==23
assert read(OUT/'context-observation.json')['AI_auxiliary_tasks_created']==0
for p in OUT.rglob('*.json'):
    json.loads(p.read_bytes())
assert not any(p.is_symlink() for p in OUT.rglob('*'))
subprocess.run(['git','diff','--check',B,'--',PREFIX,
                ':(exclude)'+PREFIX+'publication-evidence/*.stdout',
                ':(exclude)'+PREFIX+'publication-evidence/*.stderr'],cwd=REPO,check=True)
print(json.dumps({'authorized_review_paths':len(changed),'actual_clause_spans_verified':spans,
                  'primary_full_read_records':14,'all_behavior_vectors':'NOT_EXECUTED',
                  'formal_B_subtree_unchanged':True,'structured_delivery':'VALID',
                  'whitespace_scope':'New authored text, excluding retained raw publication stdout/stderr; complete cached check023 exit2 preserved'},ensure_ascii=False))
