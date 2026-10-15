"""Verify deliverable structure, input invariants and manifest declarations."""
import hashlib,json,pathlib,subprocess,sys,datetime
root=pathlib.Path(__file__).resolve().parents[1];prefix='candidates/R7-U02/evidence/reviewer/r1/'
p=json.loads((root/'per-id.json').read_bytes());assert [r['record_id'] for r in p['records']]==['GR7-M04-301','GR7-M06-002','GR7-D06-001']
assert all(r['verdict']=='PASS_SCOPED_CANDIDATE' and not r['blocking_findings'] for r in p['records'])
assert sum(len(r['vectors']) for r in p['records'])==51
assert all(v['execution']=='NOT_EXECUTED' for r in p['records'] for v in r['vectors'])
for file in root.rglob('*.json'):json.loads(file.read_bytes())
assert not list(root.rglob('*.rb')) and not list(root.rglob('*.exe'))
assert subprocess.check_output(['git','rev-parse','HEAD']).decode().strip()=='e646432c644dec04d306842cc5a559a29c718fbc'
assert not subprocess.check_output(['git','diff','--name-only'])
assert subprocess.check_output(['git','rev-parse','HEAD:deliverables/final-specification-set']).decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
assert all(x.startswith(prefix) for x in subprocess.check_output(['git','ls-files','--others','--exclude-standard']).decode().splitlines())
if '--manifest' in sys.argv:
 m=json.loads((root/'artifact-manifest.json').read_bytes());actual={str(q.relative_to(root)) for q in root.rglob('*') if q.is_file() and q.name!='artifact-manifest.json'}
 assert actual=={r['path'] for r in m['files']}
 for row in m['files']:
  d=(root/row['path']).read_bytes();assert len(d)==row['bytes'] and hashlib.sha256(d).hexdigest()==row['sha256']
  assert hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()==row['git_blob']
print(json.dumps({'status':'REVIEW_ARTIFACTS_VALID','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'required_ids':3,'static_vectors':51,'executed_vectors':0,'formal_tree_unchanged':True,'only_reviewer_r1_writes':True,'manifest_checked':'--manifest' in sys.argv}))
