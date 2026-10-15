"""Seal only reviewer deliverables; validate scope and identities, not game behavior."""
import hashlib
import json
from pathlib import Path
import subprocess

OUT=Path(__file__).resolve().parents[1]
REPO=Path(__file__).resolve().parents[6]
PREFIX='candidates/R7-U05/evidence/reviewer/r1/'
B='e646432c644dec04d306842cc5a559a29c718fbc'
def git(*args): return subprocess.check_output(['git',*args],cwd=REPO)
def ident(data):
 return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())
assert git('branch','--show-current').decode().strip()=='codex/r7-u05-reviewer-20261015-r1'
changed=set(git('diff','--name-only',B).decode().splitlines())|set(git('ls-files','--others','--exclude-standard').decode().splitlines())
assert changed and all(p.startswith(PREFIX) for p in changed)
assert not git('diff',B,'--','deliverables','planning','audit','AGENTS.md','review','reference')
review=json.loads((OUT/'per-id.json').read_bytes());receipt=json.loads((OUT/'review-input-receipt.json').read_bytes())
assert review['result']=='PASS_SCOPED_CANDIDATE' and len(review['vectors'])==9
assert not review['findings_requiring_revision'] and not review['missing_input_or_independence_blockers']
assert not any(review[k] for k in ['integrated_PASS','ACCEPTED','CLOSED'])
assert all(v['execution']=='NOT_EXECUTED' for v in review['vectors'])
assert review['reviewer_context']['actual_thread_id']!=review['author_context']
assert all(x=='UNVERIFIED' for x in review['configuration']['effective'].values())
candidate=Path('/workspace/r7-review-input/R7-U05-3acf3e23fd79c3bed1b98d23873bc1f2fd25cafa/candidate')
for row in receipt['candidate_files']:
 assert ident((candidate/row['path']).read_bytes())=={k:row[k] for k in ['bytes','sha256','git_blob']}
for row in receipt['candidate_anchors']:
 data=(candidate/row['path']).read_bytes();a,b=row['byte_offsets']
 assert hashlib.sha256(data[a:b]).hexdigest()==row['sha256']
 assert data.splitlines(keepends=True)[row['line']-1]==data[a:b]
files=[]
for path in sorted(OUT.rglob('*')):
 if path.is_file():
  assert not path.is_symlink()
  if path==OUT/'artifact-manifest.json': continue
  files.append(dict(path=str(path.relative_to(REPO)),**ident(path.read_bytes()),git_mode='100644'))
manifest=dict(schema='r7.u05.independent-reviewer-artifact-manifest.v1',batch_id='R7-U05',record_id='GR7-M07-002',
              result=review['result'],reviewer_context=review['reviewer_context']['actual_thread_id'],
              branch='codex/r7-u05-reviewer-20261015-r1',base_commit=B,allowed_prefix=PREFIX,files=files,
              self_exclusion={'path':PREFIX+'artifact-manifest.json','reason':'Self identity and final result commit/tree bound externally by actual complete remote readback; no recursive self hash.'},
              count_excluding_self=len(files),bytes_excluding_self=sum(r['bytes'] for r in files),
              phase='TOOL_VALIDATION_ONLY_NO_NEW_SEMANTIC_OR_EXECUTION_CREDIT')
(OUT/'artifact-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='REVIEWER_SCOPE_MANIFEST_AND_INPUT_RETENTION_VERIFIED',files_excluding_manifest=len(files),
                     bytes_excluding_manifest=manifest['bytes_excluding_self'],candidate_files_rechecked=14,
                     formal_changes=0,behavior_execution='NOT_EXECUTED'),indent=2))
