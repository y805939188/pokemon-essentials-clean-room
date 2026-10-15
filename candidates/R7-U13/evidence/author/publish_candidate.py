"""Ordinary push to the sole authorized branch; full pinned remote byte readback.

Initial delivery records a receipt for the subsequent evidence-only commit.
Final delivery prints its detached receipt and performs no filesystem writes.
"""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT=Path(__file__).resolve().parents[4]
E=Path(__file__).parent
B='e646432c644dec04d306842cc5a559a29c718fbc'
BRANCH='codex/r7-u13-author-20261015-wave1'
PREFIX='candidates/R7-U13/'
parser=argparse.ArgumentParser()
parser.add_argument('--phase',choices=['initial','final'],required=True)
args=parser.parse_args()
operations=[]

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()

def run(argv,check=True):
    start=utc();p=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True)
    operations.append({'start_utc':start,'end_utc':utc(),'cwd':str(ROOT),'argv':argv,'stdout':p.stdout,'stderr':p.stderr,'exit_code':p.returncode})
    if check and p.returncode:raise RuntimeError(json.dumps(operations[-1],ensure_ascii=False))
    return p.stdout.strip()

def ident(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob_content_id':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

start=utc()
assert run(['git','branch','--show-current'])==BRANCH
assert run(['git','remote','get-url','origin'])=='https://github.com/y805939188/pokemon-essentials-clean-room.git'
assert run(['git','status','--porcelain=v1'])=='','publish requires clean committed candidate'
commit=run(['git','rev-parse','HEAD']);tree=run(['git','rev-parse','HEAD^{tree}'])
assert re.fullmatch('[0-9a-f]{40}',commit)
changed=run(['git','diff','--name-only',B,commit]).splitlines()
assert changed and all(p.startswith(PREFIX) for p in changed)
parent=run(['git','rev-parse','HEAD^'])
remote_before=run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH])
if args.phase=='initial':
    assert parent==B
    assert not remote_before or remote_before.split()[0]==commit,'existing differing remote candidate must be protected'
else:
    first=json.loads((E/'first-push-readback.json').read_text())
    assert parent==first['commit']
    assert remote_before.split()[0] in [parent,commit],'remote advanced outside this author; stop without force'
    evidence_delta=run(['git','diff','--name-only',parent,commit]).splitlines()
    assert evidence_delta and all(p.startswith(PREFIX+'evidence/author/') for p in evidence_delta)
run(['git','push','origin','HEAD:refs/heads/'+BRANCH])
run(['git','fetch','--no-tags','origin','refs/heads/'+BRANCH])
assert run(['git','rev-parse','FETCH_HEAD'])==commit
assert run(['git','rev-parse','FETCH_HEAD^{tree}'])==tree
remote_after=run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH])
assert remote_after.split()[0]==commit

entries=[]
for raw in subprocess.check_output(['git','ls-tree','-rz',commit,'candidates/R7-U13'],cwd=ROOT).split(b'\0'):
    if not raw:continue
    meta,path=raw.split(b'\t',1);mode,kind,blob=meta.decode().split();path=path.decode()
    assert mode=='100644' and kind=='blob' and path.startswith(PREFIX)
    entries.append((path,blob))
assert set(changed)=={p for p,b in entries},'every new file must be fully read back'

def readback(item):
    path,blob=item
    local=subprocess.check_output(['git','show',commit+':'+path],cwd=ROOT)
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
    attempts=[]
    for attempt in range(1,4):
        began=utc()
        try:
            request=urllib.request.Request(url,headers={'User-Agent':'R7-U13-author-full-pinned-readback','Cache-Control':'no-cache'})
            with urllib.request.urlopen(request,timeout=40) as response:
                data=response.read(len(local)+1);status=response.status
            actual=ident(data)
            assert data==local and actual['git_blob_content_id']==blob
            attempts.append({'attempt':attempt,'start_utc':began,'end_utc':utc(),'http_status':status,'full_bytes_read':True})
            return {'path':path,'url':url,'expected_blob_from_committed_tree':blob,'remote':actual,'local_commit_identity':ident(local),'full_byte_equal':True,'attempts':attempts}
        except (urllib.error.URLError,TimeoutError) as error:
            attempts.append({'attempt':attempt,'start_utc':began,'end_utc':utc(),'error':str(error)})
            if isinstance(error,urllib.error.HTTPError) and error.code not in [429,500,502,503,504]:raise
            if attempt==3:raise
            time.sleep(attempt)

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    files=list(pool.map(readback,entries))
assert run(['git','status','--porcelain=v1'])==''
receipt={'schema':'r7-u13-author-remote-readback.v1','phase':args.phase,'start_utc':start,'end_utc':utc(),
 'status':'CANDIDATE_READY_NOT_REVIEWED','branch':BRANCH,'base':B,'commit':commit,'tree':tree,'parent':parent,
 'ordinary_push_only':True,'remote_before':remote_before,'remote_after':remote_after,'git_operations':operations,
 'files':files,'files_read_back':len(files),'bytes_read_back':sum(x['remote']['bytes'] for x in files),
 'all_remote_full_bytes_sha256_blob_equal':True,'worktree_clean_before_detached_receipt':True,
 'configuration':'UNVERIFIED','independent_review':'NOT_STARTED_BY_AUTHOR','game_host_Demo_native_media_real_save_replay':0,
 'qualification':'Git/HTTP transport and byte identity only; no semantic acceptance. The final commit/tree receipt is detached platform tool output to avoid circular self-hashing.'}
if args.phase=='initial':
    path=E/'first-push-readback.json'
    assert not path.exists()
    path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'phase':'initial','commit':commit,'tree':tree,'files_read_back':len(files),'bytes_read_back':receipt['bytes_read_back'],'all_remote_full_bytes_sha256_blob_equal':True,'receipt_path':str(path),'status':receipt['status']},ensure_ascii=False,indent=2))
else:
    print(json.dumps(receipt,ensure_ascii=False,indent=2))
