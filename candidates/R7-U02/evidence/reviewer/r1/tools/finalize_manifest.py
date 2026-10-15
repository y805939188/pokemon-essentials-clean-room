"""Bind every non-self artifact; commit/tree and final readback bind this manifest."""
import datetime,hashlib,json,pathlib
root=pathlib.Path(__file__).resolve().parents[1]
rows=[]
for p in sorted(root.rglob('*')):
 if not p.is_file() or p.name=='artifact-manifest.json':continue
 assert not p.is_symlink()
 d=p.read_bytes();rows.append({'path':p.relative_to(root).as_posix(),'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest(),'mode':'100644'})
x={'schema':'r7.u02.reviewer-artifact-manifest.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'branch':'codex/r7-u02-reviewer-20261015-r1','base_commit':'e646432c644dec04d306842cc5a559a29c718fbc','write_prefix':'candidates/R7-U02/evidence/reviewer/r1/','files':rows,'nonself_files':len(rows),'nonself_bytes':sum(r['bytes'] for r in rows),'self_binding':'Own bytes are bound by actual result commit/tree and external final complete remote readback; no recursive self-hash.','qualification':'Candidate evidence only; no actual integrated PASS/ACCEPTED/CLOSED.'}
(root/'artifact-manifest.json').write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest_files_excluding_self':len(rows),'nonself_bytes':x['nonself_bytes']}))
