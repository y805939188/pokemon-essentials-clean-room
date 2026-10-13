#!/usr/bin/env python3
"""Reconstruct the proposed specification bytes from immutable B5; no engine execution."""
import argparse, hashlib, json, subprocess
from pathlib import Path

p=argparse.ArgumentParser()
p.add_argument('--repo',required=True)
p.add_argument('--out',required=True)
a=p.parse_args()
repo=Path(a.repo).resolve();dest=Path(a.out).resolve();here=Path(__file__).resolve().parent
if not str(dest).startswith('/tmp/') or dest==Path('/tmp'):
    raise SystemExit('Use a dedicated /tmp scratch output; live formal writes are forbidden.')
ops=json.loads((here/'operations.json').read_text())
manifest=json.loads((here/'candidate-manifest.json').read_text())
expected={r['path']:r for r in manifest['prospective_formal_files']}
for target in sorted(expected):
    raw=subprocess.check_output(['git','show',ops['b5_commit']+':'+target],cwd=repo)
    baseline=manifest['unchanged_B5_identities'][target]
    assert hashlib.sha256(raw).hexdigest()==baseline['sha256'],target
    text=raw.decode('utf-8')
    for op in ops['operations']:
        if op['target_path']!=target:continue
        anchor=op['b5_anchor'];assert text.count(anchor)==1,(target,op['operation_id'])
        replacement=op['payload']+anchor if op['kind']=='insert_before' else op['payload']
        text=text.replace(anchor,replacement,1)
    data=text.encode('utf-8');r=expected[target]
    assert len(data)==r['bytes'] and hashlib.sha256(data).hexdigest()==r['sha256'],target
    blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    assert blob==r['git_blob'],target
    out=dest/target;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(data)
print(json.dumps({'paths':len(expected),'output':str(dest),'result':'TOOL_VALIDATION_OK','reference_execution':0}))
