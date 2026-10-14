import json, hashlib, subprocess
from pathlib import Path

OUT=Path(__file__).resolve().parent
report=json.loads((OUT/'review-findings.json').read_text())
vectors=json.loads((OUT/'derived-vector-review.json').read_text())
ids=['R6-B-001','R6-B-002','R6-DX-E001','R6-DX-E002']
groups=['identity_and_verdict','bidirectional_evidence','premises_and_counterexample',
 'minimum_revision_contract','acceptance_and_regression','independent_adjudication','dependencies_and_receivers']
assert report['decision']=='PASS' and report['decision_state']=='CANDIDATE_PASS'
assert [r['id'] for r in report['records']]==ids
assert [r['identity_and_verdict']['severity'] for r in report['records']]==['P3','P2','P2','P3']
assert all(all(g in r for g in groups) for r in report['records'])
assert all(r['identity_and_verdict']['verdict']=='PASS' for r in report['records'])
assert not report['required_additional_revisions'] and not report['candidate_semantic_blockers']
assert vectors['vector_count']==22 and vectors['execution_count']==0
assert len({r['id'] for r in vectors['rows']})==22
assert all(r['execution']=='NOT_EXECUTED' and r['result']=='SUPPORTED_STATIC' for r in vectors['rows'])
assert all(n==0 for n in report['execution_counts'].values())
assert all(all(v=='UNVERIFIED' for v in r['independent_adjudication']['effective'].values()) for r in report['records'])
for f in report['records'][0]['independent_adjudication']['candidate_files']:
 data=subprocess.check_output(['git','show',report['candidate_commit']+':'+f['candidate_path']])
 assert len(data)==f['bytes'] and hashlib.sha256(data).hexdigest()==f['sha256']
 assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==f['git_blob']
for p in OUT.glob('*.json'): json.loads(p.read_text())
for p in OUT.glob('*.jsonl'):
 for line in p.read_text().splitlines():json.loads(line)
print(json.dumps({'result':'PASS','semantic_scope':'artifact consistency only; no source/vector execution',
 'four_records_seven_groups':True,'22_manual_vectors':True,'bound_candidate_bytes':True,
 'configuration_unverified':True,'all_owned_JSON_valid':True}))
