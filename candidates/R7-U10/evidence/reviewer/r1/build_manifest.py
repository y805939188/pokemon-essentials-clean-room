"""Bind every non-self reviewer artifact; commit/tree and final remote receipt bind self."""
import datetime, hashlib, json, pathlib
root=pathlib.Path.cwd()
p=pathlib.Path(__file__).parent
rows=[]
for f in sorted(p.rglob('*')):
    if not f.is_file() or f.name=='artifact-manifest.json':continue
    assert not f.is_symlink()
    b=f.read_bytes()
    rows.append({'path':str(f.relative_to(root)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'mode':'100644'})
d={'schema':'r7.u10.reviewer.artifact-manifest.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'sole_branch':'codex/r7-u10-reviewer-20261015-r1','base_commit':'e646432c644dec04d306842cc5a559a29c718fbc','exact_write_prefix':'candidates/R7-U10/evidence/reviewer/r1/','files':rows,'nonself_file_count':len(rows),'nonself_bytes':sum(r['bytes'] for r in rows),'self_binding':'Own bytes are bound by actual final Git commit/tree and complete remote byte readback; no self-hash cycle. Any postcommit publication receipt is a later evidence commit, never an amend/force.','qualification':'Three content PASS_SCOPED_CANDIDATE; overall WAIT_INPUT_OR_INDEPENDENCE due disclosed no-subtask workflow deviation. No formal acceptance or closure.'}
(p/'artifact-manifest.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'nonself_files':len(rows),'nonself_bytes':d['nonself_bytes']}))
