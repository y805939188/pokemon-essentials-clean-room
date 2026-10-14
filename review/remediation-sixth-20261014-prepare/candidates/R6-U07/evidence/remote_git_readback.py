#!/usr/bin/env python3
"""Fresh remote Git-object readback, no existing object cache or worktree."""
import sys, json, hashlib, subprocess
from pathlib import Path
from datetime import datetime, timezone

commit, directory, receipt_directory = sys.argv[1:]
remote = Path(directory).resolve()
out = Path(receipt_directory).resolve()
assert str(remote).startswith('/tmp/r6-u07-remote-') and not remote.exists()
base = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
branch = 'codex/remediation-sixth-r6-u07-author-20261014'
prefix = 'review/remediation-sixth-20261014-prepare/candidates/R6-U07'
start = datetime.now(timezone.utc).isoformat()
calls = []

def run(argv, cwd=None):
    t=datetime.now(timezone.utc).isoformat()
    p=subprocess.run(argv,cwd=cwd,capture_output=True)
    calls.append({'argv':argv,'cwd':str(cwd or Path.cwd()),'utc_start':t,
                  'utc_end':datetime.now(timezone.utc).isoformat(),'exit_code':p.returncode,
                  'stdout_bytes':len(p.stdout),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),
                  'stderr':p.stderr.decode(errors='replace')})
    assert p.returncode==0,(argv,p.stderr.decode(errors='replace'))
    return p.stdout

run(['git','init','--bare',str(remote)])
run(['git','remote','add','origin','https://github.com/y805939188/pokemon-essentials-clean-room.git'],remote)
run(['git','fetch','--filter=blob:none','--depth=1','origin',branch],remote)
tip=run(['git','rev-parse','FETCH_HEAD'],remote).decode().strip()
assert tip==commit,(tip,commit)
tree=run(['git','rev-parse',commit+'^{tree}'],remote).decode().strip()
assert tree==subprocess.check_output(['git','rev-parse',commit+'^{tree}'],text=True).strip()
subtree=run(['git','rev-parse',commit+':'+prefix],remote).decode().strip()
entries={}
for row in run(['git','ls-tree','-r',commit,prefix],remote).decode().splitlines():
    meta,path=row.split('\t');mode,kind,sha=meta.split();entries[path]=(mode,kind,sha)
paths=subprocess.check_output(['git','diff','--name-only',base,commit],text=True).splitlines()
assert all(x.startswith(prefix+'/') for x in paths)
rows=[]
for path in paths:
    b=run(['git','cat-file','blob',commit+':'+path],remote)
    expected=subprocess.check_output(['git','cat-file','blob',commit+':'+path])
    mode,kind,sha=entries[path]
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    assert b==expected and blob==sha and mode=='100644' and kind=='blob',path
    rows.append({'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
                 'git_blob':blob,'mode':mode,'type':kind,'full_remote_bytes_equal':True})
ref=run(['git','ls-remote','--heads','origin',branch]).decode().strip()
assert ref.split()[0]==commit,ref
receipt={'commit':commit,'tree':tree,'candidate_directory_tree':subtree,'remote_ref':ref,
         'fresh_remote_object_database':str(remote),'initial_object_database_absent':True,
         'fetch_filter':'blob:none; each changed payload fully fetched on read, not inventory-only',
         'utc_start':start,'utc_end':datetime.now(timezone.utc).isoformat(),'argv':sys.argv,
         'cwd':str(Path.cwd()),'changed_payload_count':len(rows),'payloads':rows,'calls':calls,
         'undeclared_diff':[],'exit_code':0,'independent_review':'PENDING','source_or_host_execution':False}
out.mkdir(parents=True,exist_ok=True)
p=out/'remote-git-readback.json';assert not p.exists();p.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['commit','tree','candidate_directory_tree','changed_payload_count','exit_code']},ensure_ascii=False))
