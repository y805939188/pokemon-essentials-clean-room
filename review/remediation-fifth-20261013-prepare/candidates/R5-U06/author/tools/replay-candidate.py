#!/usr/bin/env python3
"""Reproduce specification text in scratch; do not run reference or a game model."""
import argparse,difflib,hashlib,json,subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--out',default='/tmp/r5-u06-replay');a=p.parse_args()
out=Path(a.out).resolve()
if not str(out).startswith('/tmp/'):raise SystemExit('Output must be a /tmp scratch directory.')
root=Path(__file__).resolve().parents[1]
repo=next(x for x in root.parents if (x/'AGENTS.md').exists() and (x/'.git').exists())
manifest=json.loads((root/'candidate-manifest.json').read_text())
edits=json.loads((root/'edits.json').read_text());base=manifest['fixed_inputs']['B5']['commit']
original={};current={}
for row in edits:
 target=row['target']
 if target not in original:
  original[target]=subprocess.check_output(['git','show',base+':'+target],cwd=repo).decode()
  current[target]=original[target]
 if current[target].count(row['before'])!=1:raise SystemExit('Anchor mismatch: '+row['edit_id'])
 current[target]=current[target].replace(row['before'],row['after'],1)
patch=[]
for target in manifest['target_order']:
 text=current[target]
 patch.extend(difflib.unified_diff(original[target].splitlines(True),text.splitlines(True),fromfile='a/'+target,tofile='b/'+target,n=0))
 f=out/target;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(text)
 row=next(r for r in manifest['proposed_targets'] if r['target']==target)
 data=text.encode()
 if hashlib.sha256(data).hexdigest()!=row['proposed_sha256']:raise SystemExit('Proposed bytes mismatch: '+target)
 if row['mode']=='direct_mirror' and (repo/row['candidate_path']).read_bytes()!=data:raise SystemExit('Mirror mismatch: '+target)
if ''.join(patch)!=(root/'formal-diff.patch').read_text():raise SystemExit('Patch mismatch.')
for row in manifest['artifacts']:
 data=(repo/row['path']).read_bytes()
 h=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
 if len(data)!=row['bytes'] or hashlib.sha256(data).hexdigest()!=row['sha256'] or h!=row['git_blob']:raise SystemExit('Artifact mismatch: '+row['path'])
print(json.dumps(dict(status='TOOL_VALIDATION_OK',targets=len(current),edits=len(edits),output=str(out),behavior_executions=0)))
