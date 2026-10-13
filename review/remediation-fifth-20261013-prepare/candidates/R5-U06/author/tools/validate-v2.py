#!/usr/bin/env python3
"""Check the three revised criteria and preservation identities; no game execution."""
import hashlib,json,subprocess
from fractions import Fraction
from pathlib import Path
root=Path(__file__).resolve().parents[1]
repo=next(p for p in root.parents if (p/'AGENTS.md').exists() and (p/'.git').exists())
prefix=str(root.relative_to(repo))+'/'
old='bc2b9f77fffe81e618bf7ef0ca2573fc7816e8a7'
def prior(name):return json.loads(subprocess.check_output(['git','show',old+':'+prefix+name],cwd=repo))
def read(name):return json.loads((root/name).read_text())
def digest(obj):return hashlib.sha256(json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
revision=read('revision-v2.json');manifest=read('candidate-manifest.json')
vectors=read('static-vectors.json')['vectors'];old_vectors=prior('static-vectors.json')['vectors']
changed={'U06-M10-003-D','U06-M10-003-E','U06-M10-011-C'}
assert {v['id'] for v in vectors}=={v['id'] for v in old_vectors} and len(vectors)==106
for old_v in old_vectors:
 new_v=next(v for v in vectors if v['id']==old_v['id'])
 if new_v['id'] not in changed:assert new_v==old_v
for vid in ['U06-M10-003-D','U06-M10-003-E']:
 v=next(v for v in vectors if v['id']==vid)
 assert v['stimulus']['T'] is None
 assert v['premises'].startswith('B为有效字符串；T存在时为有效字符串，不存在时为null')
v=next(v for v in vectors if v['id']=='U06-M10-011-C');assert v['stimulus']['times']==[.48,.725]
assert int((.475-.375)/(2/20))==0
assert Fraction.from_float(.475-.375)/Fraction.from_float(2/20)==Fraction(3602879701896396,3602879701896397)
assert int((.48-.375)/(2/20))==1 and int((.725-.375)/(2/20))==3
assert all(v['execution_status']=='NOT_EXECUTED' for v in vectors)
edits=read('edits.json');changed_edits={'U06-E021','U06-E040'}
for old_e in prior('edits.json'):
 new_e=next(e for e in edits if e['edit_id']==old_e['edit_id'])
 if new_e['edit_id'] not in changed_edits:assert new_e==old_e
response=read('finding-responses.json')['findings'];failed={'GR5-M10-003/C03','GR5-M10-011/C01','GR5-M10-011/C04'}
for old_f in prior('finding-responses.json')['findings']:
 new_f=next(f for f in response if f['id']==old_f['id'])
 if old_f['id'] not in {'GR5-M10-003','GR5-M10-011'}:assert new_f==old_f
 for old_c in old_f['mandatory_criteria']:
  new_c=next(c for c in new_f['mandatory_criteria'] if c['criterion_id']==old_c['criterion_id'])
  if old_c['criterion_id'] not in failed:assert new_c==old_c
  else:assert new_c['status']=='AUTHOR_STATIC_REVISED_V2_WAIT_LIMITED_RECHECK' and not new_c['independent_signature']
old_targets={r['target']:r for r in prior('candidate-manifest.json')['proposed_targets']}
different=[r['target'] for r in manifest['proposed_targets'] if r['proposed_sha256']!=old_targets[r['target']]['proposed_sha256']]
assert len(different)==2 and len(revision['unchanged_proposed_targets'])==22
for row in revision['unchanged_finding_records']:assert row['same_record']
assert (root/'regression-results.json').read_bytes()==subprocess.check_output(['git','show',old+':'+prefix+'regression-results.json'],cwd=repo)
assert revision['existing303_rows_literal_preserved'] and len(read('regression-results.json')['unchanged_existing_vector_rows'])==303
for p in ['deliverables','specs','audit','reference','review/remediation-fifth-20261013-prepare/contracts','review/remediation-fifth-20261013-prepare/registration','review/remediation-fifth-20261013-prepare/reviews']:
 assert not subprocess.check_output(['git','diff','--name-only',old,'--',p],cwd=repo),p
print(json.dumps(dict(status='TOOL_VALIDATION_OK',limited_criteria=3,changed_vectors=3,unchanged_vectors=103,unchanged_criteria=142,unchanged_findings=16,unchanged_edits=41,unchanged_targets=22,old_literal_rows=303,new_behavior_executions=0)))
