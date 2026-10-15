import json,hashlib,subprocess,os,datetime,sys
from pathlib import Path
OUT=Path(__file__).parent.parent;PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U08/r1/';B='e646432c644dec04d306842cc5a559a29c718fbc'
def git(*a):return subprocess.check_output(['git',*a])
def load(p):return json.loads(p.read_text())
r=load(OUT/'per-id.json');assert [x['record_id'] for x in r['records']]==['GR7-M13-001','GR7-J16-001','GR7-J16-002','GR7-J16-003'];assert all(x['verdict']=='PASS_SCOPED_ACTUAL_INTEGRATION' and not x['formal_ACCEPTED'] and not x['CLOSED'] for x in r['records']);assert sum(len(x['vectors']) for x in r['records'])==17
for x in r['records']:
 for v in x['vectors']:assert v['execution']=='NOT_EXECUTED' and v['premises'] and v['independent_static_reason_and_expected_prefix']
 for c in x['actual_clauses']:
  b=git('show',c['commit']+':'+c['path']);a,z=c['byte_offsets_half_open'];assert b[a:z].decode()==c['actual_text'];assert hashlib.sha256(b[a:z]).hexdigest()==c['clause_identity']['sha256'];assert hashlib.sha256(b).hexdigest()==c['whole_file_identity']['sha256']
assert all(v=='UNVERIFIED' for v in r['configuration'].values());assert len(load(OUT/'review-input-receipt.json')['full_actual_reads'])==12
assert git('branch','--show-current').decode().strip()=='codex/r7-ir-u08-20261015-r1';assert git('merge-base',B,'HEAD').decode().strip()==B
assert git('rev-parse','HEAD:deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
for p in git('diff','--name-only',B).decode().splitlines():assert p.startswith(PREFIX),p
for row in git('status','--porcelain','--untracked-files=all').decode().splitlines():assert row[3:].startswith(PREFIX),row
for p in OUT.rglob('*.json'):load(p)
if '--manifest' in sys.argv:
 m=load(OUT/'artifact-manifest.json');actual={p.relative_to(OUT).as_posix() for p in OUT.rglob('*') if p.is_file() and p.name!='artifact-manifest.json'};assert actual=={x['path'] for x in m['files']}
 for x in m['files']:
  b=(OUT/x['path']).read_bytes();assert len(b)==x['bytes'] and hashlib.sha256(b).hexdigest()==x['sha256'] and hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()==x['git_blob']
print(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool_pid':os.getpid(),'result':'JSON_CLAUSES_17_STATIC_VECTORS_AND_EXCLUSIVE_WRITE_SCOPE_MATCH','manifest_checked':'--manifest' in sys.argv,'formal_subtree_at_result':'B_UNCHANGED','semantic_PASS_from_tool':False,'behavior_execution':0,'configuration':'UNVERIFIED'}))
