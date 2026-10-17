#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,subprocess
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
C='d62b41f4d620e50bb04c80a7505374bd284d8210'
prefix=OUT.relative_to(ROOT).as_posix()+'/'
changed=subprocess.check_output(['git','diff','--name-only',C],cwd=ROOT,text=True).splitlines()
assert all(p.startswith(prefix) for p in changed),changed
for entry in json.loads((OUT/'evidence/candidate-identities.json').read_text())['entries']:
    assert hashlib.sha256((ROOT/entry['path']).read_bytes()).hexdigest()==entry['sha256'],entry['path']
files=[]
for path in sorted(OUT.rglob('*')):
    if not path.is_file() or path.name=='output-file-manifest.json':continue
    assert '__pycache__' not in path.parts, path
    b=path.read_bytes()
    files.append({'path':path.relative_to(ROOT).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':subprocess.check_output(['git','hash-object','--stdin'],input=b,cwd=ROOT).decode().strip(),'git_mode':'100755' if path.stat().st_mode & 0o111 else '100644'})
manifest={'schema':'r8-disposition-review-output-files.v1','reviewed_candidate':C,'self_identity':'This file is excluded from its own hashes; the enclosing Git commit is supplied externally. A publication-proof, when present, verifies its explicitly named prior payload commit, never a future/self commit.','file_count_excluding_self':len(files),'files':files}
(OUT/'output-file-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files_excluding_self':len(files),'bytes_excluding_self':sum(x['bytes'] for x in files)}))
