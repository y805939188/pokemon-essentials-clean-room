#!/usr/bin/env python3
"""Read one immutable necessary file, validating whole bytes; never execute it."""
import argparse, hashlib, json, subprocess, urllib.request, urllib.parse
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('batch',choices=['R5-U0'+str(i) for i in range(1,9)]);p.add_argument('kind',choices=['source','formal','evidence']);p.add_argument('path');p.add_argument('--cache-root',default='/tmp/fifth-input-cache');args=p.parse_args()
root=Path(__file__).resolve().parents[1];repo=root.parents[1]
c=json.loads((root/'contracts'/args.batch/'contract.json').read_text())
key={'source':'source_readset','formal':'formal_readset','evidence':'original_evidence_readset'}[args.kind]
row=next((x for x in c[key] if x['path']==args.path),None)
if row is None:raise SystemExit('Path not in this primary readset; consult exact shared/negative-evidence anchors and report additional read need.')
repository='Maruno17/pokemon-essentials' if args.kind=='source' else 'y805939188/pokemon-essentials-clean-room'
commit=row['commit'];cache=Path(args.cache_root).resolve()
if not (str(cache).startswith('/tmp/') or str(cache).startswith('/workspace/')):raise SystemExit('Cache must be an authorized scratch directory.')
if cache==repo or repo in cache.parents or root in cache.parents or cache==root:raise SystemExit('Use scratch cache; frozen package cannot be overwritten.')
name=Path(row['path'])
if name.is_absolute() or '..' in name.parts:raise SystemExit('Invalid repository path.')
out=cache/repository/commit/name
if out.exists():data=out.read_bytes();source='cached full bytes'
else:
 data=None
 if args.kind!='source':
  r=subprocess.run(['git','cat-file','blob',commit+':'+row['path']],cwd=repo,capture_output=True)
  if r.returncode==0:data=r.stdout;source='local immutable Git object'
 if data is None:
  url='https://raw.githubusercontent.com/'+repository+'/'+commit+'/'+urllib.parse.quote(row['path'],safe='/')
  with urllib.request.urlopen(url,timeout=30) as f:data=f.read()
  source='fresh immutable raw GitHub file'
gitblob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest();sha=hashlib.sha256(data).hexdigest()
if gitblob!=row['git_blob'] or ('bytes' in row and len(data)!=row['bytes']) or ('sha256' in row and sha!=row['sha256']):raise SystemExit('Frozen input identity mismatch; no write.')
out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(data)
print(json.dumps({'path':str(out),'repository':repository,'commit':commit,'bytes':len(data),'sha256':sha,'git_blob':gitblob,'source':source,'execution':False,'evidence_level':'TOOL_VALIDATION'},ensure_ascii=False))
