"""Inventory every existing reviewer deliverable except this self-referential manifest."""
import pathlib,json,hashlib,datetime
H=pathlib.Path(__file__).resolve().parents[1];R=H.parents[4]
files=[]
for p in sorted(H.rglob('*')):
 if not p.is_file() or p==H/'artifact-manifest.json':continue
 d=p.read_bytes();files.append(dict(path=str(p.relative_to(R)),bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest(),git_mode='100644'))
manifest=dict(schema='r7-u03-r1.reviewer-artifact-manifest.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),branch='codex/r7-u03-reviewer-20261015-r1',base_commit='e646432c644dec04d306842cc5a559a29c718fbc',write_root='candidates/R7-U03/evidence/reviewer/r1/',files=files,self_binding='artifact-manifest.json excludes its own identity; actual result commit/tree and complete final remote readback bind every file including this manifest outside the commit.',qualification='Reviewer evidence only; candidate and formal files are not transported in this branch.')
(H/'artifact-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(nonself_files=len(files),nonself_bytes=sum(r['bytes'] for r in files))))
