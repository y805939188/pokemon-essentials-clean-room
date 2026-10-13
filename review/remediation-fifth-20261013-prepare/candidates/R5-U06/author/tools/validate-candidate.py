#!/usr/bin/env python3
"""Check coverage, scopes, bytes, and exact arithmetic; no behavioral simulator."""
import hashlib,json,subprocess
from fractions import Fraction
from pathlib import Path
root=Path(__file__).resolve().parents[1]
repo=next(x for x in root.parents if (x/'AGENTS.md').exists() and (x/'.git').exists())
contract=json.loads(subprocess.check_output(['git','show','22fba7786b0090a1955ce6211315b0036cddfbcd:review/remediation-fifth-20261013-prepare/contracts/R5-U06/contract.json'],cwd=repo))
response=json.loads((root/'finding-responses.json').read_text())
edits=json.loads((root/'edits.json').read_text())
vectors=json.loads((root/'static-vectors.json').read_text())['vectors']
required=set(contract['required_ids']);assert {r['id'] for r in response['findings']}==required
assert len(response['findings'])==18 and len(vectors)==len({v['id'] for v in vectors})
assert all(v['execution_status']=='NOT_EXECUTED' and v['evidence_level']=='DERIVED_VECTOR' for v in vectors)
assert all(not f['closed'] and not f['formal_acceptance'] and not any(x['independent_signature'] for x in f['mandatory_criteria']) for f in response['findings'])
assert all(set(f['consumer_sync_paths'])==set(contract['per_finding_formal_permissions'][f['id']]) for f in response['findings'])
for fid in required:
 es=[e for e in edits if fid in e['finding_ids']]
 assert {e['target'] for e in es}==set(contract['per_finding_formal_permissions'][fid]),fid
 assert any(v['finding_id']==fid for v in vectors)
for e in edits:
 for fid in e['finding_ids']:assert e['target'] in contract['per_finding_formal_permissions'][fid]
sample=next(v for v in vectors if v['id']=='U06-M10-001-A')['stimulus']['text']
assert sample=='A\nB\nC' and sample.count('\n')==2 and '\\n' not in sample
assert Fraction(8,20)==Fraction(2,5)
assert (Fraction(625,1000)-Fraction(375,1000))//Fraction(5,20)%4==1
assert Fraction(625,1000)//Fraction(5,20)%4==2
assert Fraction(1,2)//Fraction(1,20)==10 and Fraction(11,20)//Fraction(1,20)==11
assert Fraction(1,8)*2==Fraction(1,4)
assert [Fraction(640)*t//48 for t in [Fraction(1,100),Fraction(2,100),Fraction(1,5),Fraction(1,4)]]==[0,0,2,3]
assert 100+(0-100)*Fraction(1,2)==50 and 20+100*Fraction(1,2)==70
reg=json.loads((root/'regression-results.json').read_text())
assert all(r['candidate_same_literal_row'] for r in reg['unchanged_existing_vector_rows'])
for path in ['deliverables','specs','audit','reference','review/remediation-fifth-20261013-prepare/contracts','review/remediation-fifth-20261013-prepare/registration','review/remediation-fifth-20261013-prepare/frozen-input']:
 assert not subprocess.check_output(['git','diff','--name-only','93524fe5cf396de2bd01f3c5c1e08ba4b874bc68','--',path],cwd=repo),path
assert subprocess.check_output(['git','rev-parse','HEAD:deliverables/final-specification-set'],cwd=repo,text=True).strip()==contract['fixed_inputs']['B5']['formal_tree']
print(json.dumps(dict(status='TOOL_VALIDATION_OK',required=18,criteria=sum(len(r['mandatory_criteria']) for r in response['findings']),vectors=len(vectors),existing_literal_rows=len(reg['unchanged_existing_vector_rows']),behavior_executions=0)))
