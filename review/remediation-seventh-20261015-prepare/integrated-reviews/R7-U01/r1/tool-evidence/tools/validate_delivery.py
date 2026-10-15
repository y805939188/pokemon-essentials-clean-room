import hashlib,json,pathlib,subprocess
C=pathlib.Path('/workspace/r7-ir-R7-U01/checkout');P='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U01/r1/';D=C/P;B='e646432c644dec04d306842cc5a559a29c718fbc'
j=json.loads((D/'artifact-manifest.json').read_text());paths=set()
for x in j['files']:
 p=D/x['path'];b=p.read_bytes();assert len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'];assert hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()==x['git_blob'];paths.add(x['path'])
actual={str(p.relative_to(D)) for p in D.rglob('*') if p.is_file()};assert paths|{'artifact-manifest.json'}==actual
for p in D.rglob('*.json'):json.loads(p.read_bytes())
for p in D.rglob('*.jsonl'):
 for line in p.read_text().splitlines():json.loads(line)
v=json.loads((D/'per-id.json').read_text());assert {r['id'] for r in v['records']}=={'GR7-M01-001','GR7-J01-001'}
assert all(r['conclusion']=='PASS_SCOPED_ACTUAL_INTEGRATION' and r['ACCEPTED'] is False and r['CLOSED'] is False for r in v['records'])
vectors=[x for r in v['records'] for x in r['vectors']];assert len(vectors)==len({x['id'] for x in vectors})==20
assert all(x['behavior_execution']=='NOT_EXECUTED' for x in vectors)
assert len(json.loads((D/'review-input-receipt.json').read_text())['mandatory_full_actual_documents'])==16
staged=subprocess.check_output(['git','diff','--cached','--name-status',B],cwd=C).decode().splitlines()
assert staged and all(x.startswith('A\t'+P) for x in staged),staged
assert {x.split('\t')[1][len(P):] for x in staged}==actual
r=subprocess.run(['git','diff','--cached','--check'],cwd=C,capture_output=True,text=True);assert r.returncode==0,(r.stdout,r.stderr)
print(json.dumps({'status':'DELIVERY_IDENTITIES_JSON_SCOPE_AND_WHITESPACE_VERIFIED','files':len(actual),'vectors':20,'mandatory_full_actual_documents':16,'only_added_under':P,'qualification':'Artifact integrity only; content decision by actual reviewer, no behavioral execution.'},ensure_ascii=False,indent=2))
