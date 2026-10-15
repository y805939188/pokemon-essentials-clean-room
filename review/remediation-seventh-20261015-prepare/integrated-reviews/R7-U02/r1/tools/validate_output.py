import hashlib, json, os, re, subprocess
from pathlib import Path
R=Path(__file__).resolve().parents[1]
B='e646432c644dec04d306842cc5a559a29c718fbc'
MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
P='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U02/r1/'
def git(*a):return subprocess.check_output(['git',*a])
d=json.loads((R/'per-id.json').read_bytes())
assert {x['id'] for x in d['records']}=={'GR7-M04-301','GR7-M06-002','GR7-D06-001'}
vec=[]
for record in d['records']:
 assert record['verdict']=='PASS_SCOPED_ACTUAL_INTEGRATION'
 assert record['MI']==MI and not record['ACCEPTED'] and not record['CLOSED']
 for c in record['actual_clauses']:
  data=git('show',MI+':'+c['path']);a,b=c['lines_inclusive']
  assert hashlib.sha256(data).hexdigest()==c['whole_file_identity']['sha256']
  assert hashlib.sha256(b''.join(data.splitlines(keepends=True)[a-1:b])).hexdigest()==c['clause_identity_including_LF']['sha256']
 for v in record['vectors']:
  assert v['execution']=='NOT_EXECUTED' and v['independent_static_reason'] and v['common_premises']
  data=git('show',MI+':'+v['actual_catalog']).splitlines(keepends=True)[v['actual_line']-1]
  assert hashlib.sha256(data).hexdigest()==v['actual_line_identity']['sha256']
  vec.append(v['id'])
assert len(vec)==len(set(vec))==51
receipt=json.loads((R/'review-input-receipt.json').read_bytes())
assert len(receipt['mandatory_actual_full_read'])==14 and len(receipt['all_restored_inputs'])==219
assert len(receipt['limits'])==14
assert receipt['actual_thread_id']==os.environ['CODEX_THREAD_ID']
dispatch=git('show','c64774c60d91e522cb515ef71e3e9d4ea6b4712c:review/remediation-seventh-20261015-prepare/integration/wave2/v1/dispatch/R7-U02-R7IR.md').decode()
assert receipt['actual_thread_id'] not in dispatch
assert git('rev-parse','HEAD:deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
changes=git('diff','--name-only',B).decode().splitlines()
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
assert all(x.startswith(P) for x in changes+untracked)
assert git('branch','--show-current').decode().strip()=='codex/r7-ir-u02-20261015-r1'
assert len(json.loads((R/'scope-validation.json').read_bytes())['clause_checks'])==56
print(json.dumps(dict(three_scoped_verdicts=True,vectors=51,all_vectors_NOT_EXECUTED=True,mandatory_full_files=14,restored=219,L01_L14=14,write_scope=P,formal_output_tree_unchanged=True,independent_visible_ID=True,configuration='UNVERIFIED')))
