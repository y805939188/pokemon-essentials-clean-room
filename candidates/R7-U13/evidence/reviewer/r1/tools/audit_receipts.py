"""Inspect frozen author evidence as data; never import or execute author code."""
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

ROOT=Path('/workspace/pokemon-essentials-clean-room')
OUT=Path(__file__).resolve().parent
AUTHOR=Path('/workspace/r7-review-input/R7-U13-r1-5635c73ea14adc278961da0e3917c2d00d580a25/candidate/candidates/R7-U13/evidence/author')
ORIG=Path('/workspace/r7-context/R7-U13-reviewer')
BOOT=Path('/workspace/r7-review-bootstrap/R7-U13-r1')
B='e646432c644dec04d306842cc5a559a29c718fbc'

def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT)
def identity(data): return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())
def load(path): return json.loads(path.read_bytes())

files=[]
for path in sorted(AUTHOR.iterdir()):
    data=path.read_bytes()
    if path.suffix=='.json': json.loads(data)
    if path.suffix=='.jsonl':
        for line in data.decode().splitlines(): json.loads(line)
    files.append(dict(path=path.name,**identity(data),qualification='Frozen author evidence read as data; no new author-tool execution'))
assert len(files)==20

manifest=load(AUTHOR/'artifact-manifest.json')
diffs=[]
for row in manifest['artifacts']:
    old=git('show',B+':'+row['original_path'])
    new=(AUTHOR.parents[1]/row['original_path']).read_bytes()
    diffs.append(''.join(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),fromfile='B/'+row['original_path'],tofile=row['candidate_path'],n=0)))
assert '\n'.join(diffs).encode() == (AUTHOR/'changes.patch').read_bytes()

record=load(ORIG/'evidence/tasks/R7-C13/inputs/delta-j16/findings.json')['records'][30]
counter=load(ORIG/'evidence/tasks/R7-C13/inputs/evidence/received-final-proposals/GR7-D07-001/counter-review.json')['findings'][0]
proposal=load(BOOT/'supplemental/tasks/R7-D07/findings.json')['findings'][0]
assert record['original_proposal']==proposal
assert record['independent_adjudication']['decision_record']==counter
assert record['counter_payload_not_author_update']['current_record']==counter
late=load(ORIG/'evidence/tasks/R7-C13/inputs/late-reception/evidence/late-author-payload-receptions.json')['records'][3]
assert late['id']=='GR7-D07-001'

receipts=[]
for name in ['recovery-receipt-20261015T122419706899Z.json','recovery-receipt-20261015T123124935145Z.json']:
    value=load(AUTHOR/name)
    assert value['files_verified']==21 and value['bytes_verified']==16814642
    assert value['status']=='BOUNDED_RESTORE_BYTES_VERIFIED'
    for row in value['files']:
        mapped=ORIG/row['local_path']
        assert all(identity(mapped.read_bytes())[k]==row[k] for k in identity(mapped.read_bytes()))
    receipts.append(dict(name=name,start_utc=value['start_utc'],end_utc=value['end_utc'],plan_identity=value['plan_identity'],statuses=sorted({x['status'] for x in value['files']}),files=21,bytes=16814642))

first=load(AUTHOR/'first-push-readback.json')
assert first['commit']=='3dd59f45ad39e4a87a535c41137b9478f553f031'
for row in first['files']:
    actual=identity(git('show',first['commit']+':'+row['path']))
    assert row['full_byte_equal'] and actual==row['remote']==row['local_commit_identity']
assert len(first['files'])==first['files_read_back']==23
assert sum(x['remote']['bytes'] for x in first['files'])==first['bytes_read_back']==825028

commands=[json.loads(x) for x in (AUTHOR/'commands.jsonl').read_text().splitlines()]
history=[dict(start_utc=x['start_utc'],end_utc=x['end_utc'],argv=x['argv'],exit_code=x['exit_code'],stdout_identity=identity(x['stdout'].encode()),stderr_identity=identity(x['stderr'].encode())) for x in commands]
assert sum(x['exit_code']!=0 for x in commands)==2
shared=[]
for batch in ['R7-U01','R7-U02','R7-U03','R7-U10','R7-U11','R7-U12']:
    path='review/remediation-seventh-20261015-prepare/delegation/contracts/'+batch+'.json'
    data=git('show','f622356f3beb9e84ea8cff9db07c7fb382565d3f:'+path)
    contract=json.loads(data)
    shared.append(dict(batch=batch,path=path,**identity(data),shared_scopes=[row for row in contract['paths'] if row['path'] in ['audit/source-traceability.md','planning/feature-matrix.md','deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md']]))
summary=dict(schema='r7-u13-reviewer-author-evidence-audit.v1',observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    author_evidence=files,all_20_evidence_received=True,author_patch_recomputed_exact=True,
    root_original_and_counter_embeds_equal=True,late_C11_not_author_mutation=late,
    author_recovery_receipts=receipts,author_first_push=dict(commit=first['commit'],tree=first['tree'],files=23,bytes=825028,qualification='Historical first author push only; current 24-file candidate separately verified'),
    author_commands=history,author_logged_failures=2,additional_precommit_failure=load(AUTHOR/'precommit-check-failure.json'),
    shared_contracts=shared,semantic_PASS=False,reference_or_author_code_executed=0)
(OUT/'author-evidence-audit.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='AUTHOR_EVIDENCE_DATA_AND_SCOPE_CHECKED',files=len(files),author_patch_exact=True,author_logged_commands=len(commands),author_logged_failures=2,first_author_receipt_files=23,shared_contracts=len(shared),reference_or_author_code_executed=0)))
