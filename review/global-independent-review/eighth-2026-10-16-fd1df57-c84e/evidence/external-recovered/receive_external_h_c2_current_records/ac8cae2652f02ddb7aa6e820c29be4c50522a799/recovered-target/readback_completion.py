"""Fresh filtered bare remote fetch, then full byte read of every task member."""
from pathlib import Path
import json,subprocess,hashlib,gzip,datetime,os,argparse
T=Path(__file__).parent;W=T/'.publication-work';REPO=T.parents[4]
URL='https://github.com/y805939188/pokemon-essentials-clean-room.git'
ap=argparse.ArgumentParser();ap.add_argument('phase',choices=['core','binding']);a=ap.parse_args()
expected=json.loads((W/f'completion-{a.phase}.json').read_text())
dest=W/f'completion-remote-{a.phase}.git'
assert not dest.exists() and not dest.is_symlink()
logs=W/f'remote-{a.phase}-logs';logs.mkdir(exist_ok=False)
env=os.environ.copy()
for key in ('GIT_DIR','GIT_WORK_TREE','GIT_INDEX_FILE','GIT_OBJECT_DIRECTORY','GIT_ALTERNATE_OBJECT_DIRECTORIES'):
    env.pop(key,None)
receipts=[]
def run(args,stdin=None,timeout=55):
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.run(args,input=stdin,capture_output=True,env=env,timeout=timeout)
    n=len(receipts);out=logs/f'{n:03d}.stdout';err=logs/f'{n:03d}.stderr';out.write_bytes(p.stdout);err.write_bytes(p.stderr)
    receipts.append(dict(argv=args,start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit_code=p.returncode,stdout=str(out),stderr=str(err)))
    (logs/'commands.json').write_text(json.dumps(receipts,ensure_ascii=False,indent=2)+'\n')
    assert p.returncode==0,(args,p.returncode,p.stderr.decode(errors='replace'))
    return p.stdout
run(['git','init','--bare',str(dest)])
run(['git','-C',str(dest),'remote','add','origin',URL])
run(['git','-C',str(dest),'config','remote.origin.promisor','true'])
run(['git','-C',str(dest),'config','remote.origin.partialclonefilter','blob:none'])
run(['git','-C',str(dest),'fetch','--no-tags','--depth=1','--filter=blob:none','origin',expected['branch']])
assert not (dest/'objects/info/alternates').exists()
commit=run(['git','-C',str(dest),'rev-parse','FETCH_HEAD']).decode().strip();assert commit==expected['commit']
workspace=run(['git','-C',str(dest),'rev-parse',commit+'^{tree}']).decode().strip();assert workspace==expected['workspace_tree']
reporttree=run(['git','-C',str(dest),'rev-parse',commit+':'+expected['report_path']]).decode().strip();assert reporttree==expected['report_tree']
tree={}
for row in run(['git','-C',str(dest),'ls-tree','-r','-z',commit,'--',expected['report_path']]).split(b'\0'):
    if not row:continue
    meta,path=row.split(b'\t',1);mode,kind,blob=meta.decode().split();assert kind=='blob'
    tree[path.decode()]=(mode,blob)
assert set(tree)=={x['path'] for x in expected['payloads']}
# Fetch explicit report blobs in one negotiation from this new remote object store.
unique=sorted({x['blob'] for x in expected['payloads']})
run(['git','-C',str(dest),'-c','fetch.negotiationAlgorithm=noop','fetch','--no-tags','--no-write-fetch-head','origin',*unique])
read=[]
for row in expected['payloads']:
    assert tree[row['path']]==(row['mode'],row['blob'])
    data=run(['git','-C',str(dest),'cat-file','blob',row['blob']])
    blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
    assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'] and blob==row['blob']
    read.append(dict(path=row['path'],mode=row['mode'],blob=blob,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),status='FULL_REMOTE_BYTES_READ_MATCH'))
    if row['path'].endswith('/exact-reading-evidence.json.gz'):
        decoded=gzip.decompress(data);assert isinstance(json.loads(decoded),dict)
        bundle=dict(bytes=len(decoded),sha256=hashlib.sha256(decoded).hexdigest())
refs=run(['git','ls-remote',URL,expected['branch'],'refs/heads/main','refs/tags/delivery/seventh-round-closed-final-20261016']).decode()
rr={x.split('\t')[1]:x.split('\t')[0] for x in refs.splitlines()}
assert rr[expected['branch']]==commit
for ref in ('refs/heads/main','refs/tags/delivery/seventh-round-closed-final-20261016'):
    assert rr[ref]=='fd1df570cad987dc3852a3b958f03916e317f7fe'
assert run(['git','-C',str(REPO),'rev-parse','HEAD']).decode().strip()=='fd1df570cad987dc3852a3b958f03916e317f7fe'
result=dict(status='FULL_FRESH_REMOTE_TASK_BYTES_READBACK_MATCH',phase=a.phase,commit=commit,workspace_tree=workspace,report_tree=reporttree,
    report_path=expected['report_path'],files=len(read),bytes=sum(x['bytes'] for x in read),payloads=read,
    byte_origin='Fresh bare repository without alternates; remote tree then explicit remote blob fetch; every task blob fully cat-file read, no local publication-byte cache reused',
    decoded_evidence_bundle=bundle,protected_remote_refs=rr,original_worktree_HEAD_unchanged=True,ordinary_push_confirmed=True,
    root_semantic_reception='NOT_RECEIVED',new_behavior_execution='NOT_EXECUTED',update_status='UPDATE_NOT_STARTED',
    utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),command_receipts=str(logs/'commands.json'))
(W/f'completion-{a.phase}-remote-readback.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='payloads'},ensure_ascii=False,indent=2))
