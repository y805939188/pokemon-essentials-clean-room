"""Publish only this authorized evidence branch, then independently fetch its B bytes.

Usage: publish.py core COMMIT (writes publication.json after ordinary push/readback)
       publish.py final COMMIT (verifies final tip; prints receipt, no recursive write)
No alternates in the readback repository. No old task helper or reference execution.
"""
from pathlib import Path
import argparse, datetime, hashlib, json, subprocess

T=Path(__file__).resolve().parent
REPO=Path('/workspace/pokemon-essentials-clean-room')
PREFIX=T.relative_to(REPO).as_posix()
BRANCH='codex/r8-c2-reception-b-20261016'
BASE='1b46a33526f086241c765b700155c5406a86f65e'
URL='https://github.com/y805939188/pokemon-essentials-clean-room.git'
READBACK=T/'.work/publication-readback'
ap=argparse.ArgumentParser();ap.add_argument('phase',choices=['core','final']);ap.add_argument('commit');a=ap.parse_args()
logs=[]
def run(args,cwd=REPO,input=None):
    r=subprocess.run(args,cwd=cwd,input=input,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    logs.append(dict(args=args,cwd=str(cwd),exit=r.returncode,stdout=r.stdout.decode(errors='replace'),stderr=r.stderr.decode(errors='replace')))
    if r.returncode:raise RuntimeError(json.dumps(logs[-1],ensure_ascii=False))
    return r.stdout
def g(*x,cwd=REPO):return run(['git',*x],cwd)
def enc(x):return json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()
def sha(b):return hashlib.sha256(b).hexdigest()
assert g('branch','--show-current').decode().strip()==BRANCH
assert g('rev-parse','HEAD').decode().strip()==a.commit
changes=g('diff','--name-only',BASE,a.commit).decode().splitlines()
assert changes and all(p.startswith(PREFIX+'/') for p in changes)
g('merge-base','--is-ancestor',BASE,a.commit)
assert not g('status','--porcelain').strip(), 'Commit all authorized B report files first'
g('push','origin',a.commit+':refs/heads/'+BRANCH)
advertised=g('ls-remote',URL,'refs/heads/'+BRANCH).decode().split()
assert advertised==[a.commit,'refs/heads/'+BRANCH]
if not READBACK.exists():
    READBACK.mkdir(parents=True)
    g('init',cwd=READBACK)
    g('remote','add','origin',URL,cwd=READBACK)
assert not (READBACK/'.git/objects/info/alternates').exists()
g('fetch','--no-tags','--depth=1','--filter=blob:none','origin',a.commit,cwd=READBACK)
g('sparse-checkout','init','--no-cone',cwd=READBACK)
run(['git','sparse-checkout','set','--no-cone','--stdin'],READBACK,('/'+PREFIX+'/\n').encode())
g('checkout','--detach',a.commit,cwd=READBACK)
assert g('rev-parse','HEAD',cwd=READBACK).decode().strip()==a.commit
assert g('rev-parse',a.commit+':'+PREFIX)==g('rev-parse',a.commit+':'+PREFIX,cwd=READBACK)
local=g('ls-tree','-rz',a.commit,'--',PREFIX).split(b'\0')
remote=g('ls-tree','-rz',a.commit,'--',PREFIX,cwd=READBACK).split(b'\0')
assert local==remote
files=[]
for ent in local:
    if not ent:continue
    meta,rawpath=ent.split(b'\t',1);mode,kind,blob=meta.decode().split();p=rawpath.decode()
    assert mode=='100644' and kind=='blob'
    expected=subprocess.check_output(['git','show',a.commit+':'+p],cwd=REPO)
    actual=(READBACK/p).read_bytes()
    assert expected==actual
    assert hashlib.sha1(b'blob '+str(len(actual)).encode()+b'\0'+actual).hexdigest()==blob
    files.append(dict(path=p,mode=mode,git_blob=blob,bytes=len(actual),sha256=sha(actual)))
receipt=dict(schema='r8.B.publication.v1',phase=a.phase,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),branch=BRANCH,base=BASE,commit=a.commit,commit_tree=g('rev-parse',a.commit+'^{tree}').decode().strip(),B_tree=g('rev-parse',a.commit+':'+PREFIX).decode().strip(),ordinary_push=True,force=False,remote_branch_exact=True,readback='Fresh isolated shallow filtered repository, NO alternates; only B sparse files materialized. Exact commit fetched from remote, all B mode/blob/bytes/SHA/collection checked',all_changed_paths=changes,files=files,file_count=len(files),collection_sha256=sha(enc(files)),semantic_credit_from_transport=0,reference_behavior_executed=False,logs=logs)
if a.phase=='core':
    receipt['final_binding']='This receipt is appended in the next authorized evidence-only commit; its exact final tip is independently fetched and verified with phase final, and returned to parent without self-ID recursion.'
    (T/'publication.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
else:
    prior=json.loads((T/'publication.json').read_text());assert prior['commit']!=a.commit
    receipt['core_receipt_commit']=prior['commit']
    receipt['final_increment']=g('diff','--name-only',prior['commit'],a.commit).decode().splitlines()
    # Full receipt is kept locally under ignored work; final tool output records digest.
    (T/'.work/final-publication-readback.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['phase','commit','commit_tree','B_tree','file_count','collection_sha256','ordinary_push','remote_branch_exact']},ensure_ascii=False))
