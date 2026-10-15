"""Bind every nonself reviewer artifact; the result Git tree binds the manifest."""
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
repo=root.parents[4]
files=[]
for p in sorted(root.rglob('*')):
    if not p.is_file() or p.name=='artifact-manifest.json':continue
    assert not p.is_symlink()
    d=p.read_bytes()
    files.append(dict(path=p.relative_to(repo).as_posix(),bytes=len(d),sha256=hashlib.sha256(d).hexdigest(),git_blob=hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest(),git_mode='100644'))
data=dict(schema='r7-u03-r2.artifact-manifest.v1',branch='codex/r7-u03-reviewer-20261015-r2',base_commit='e646432c644dec04d306842cc5a559a29c718fbc',allowed_prefix='candidates/R7-U03/evidence/reviewer/r2/',files=files,file_count_excluding_self=len(files),bytes_excluding_self=sum(r['bytes'] for r in files),self_binding='This file and all actual additions are bound by the final result commit/tree and exhaustive external final HTTP readback. No recursive self-hash claimed.',execution='TOOL_VALIDATION only')
(root/'artifact-manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(files_excluding_manifest=len(files),bytes_excluding_manifest=data['bytes_excluding_self'])))
