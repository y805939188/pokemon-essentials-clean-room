#!/usr/bin/env python3
"""Fetch independent remote metadata and reread every selected UTF-8 payload."""
import concurrent.futures, datetime, hashlib, json, pathlib, subprocess, sys, urllib.parse, urllib.request

OWN=pathlib.Path(__file__).resolve().parent
REPO=OWN.parents[3]
commit,branch,prefix,outname=sys.argv[1:]
url='https://github.com/y805939188/pokemon-essentials-clean-room.git'
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
commands=[]
def run(argv,cwd):
    t=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.run(argv,cwd=cwd,capture_output=True,timeout=120)
    commands.append(dict(argv=argv,cwd=str(cwd),started_utc=t,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit=p.returncode,stdout=p.stdout.decode(),stderr=p.stderr.decode()))
    if p.returncode:raise RuntimeError(p.stderr.decode())
    return p.stdout
try:
    refs=run(['git','ls-remote','--heads',url,'refs/heads/'+branch],REPO).decode().split()
    assert refs and refs[0]==commit,(commit,refs)
    bare=pathlib.Path('/tmp/r6-u08-review-remote-'+commit[:12])
    run(['git','init','--bare',str(bare)],REPO)
    run(['git','fetch','--filter=blob:none','--depth=1',url,commit],bare)
    remote_commit=run(['git','rev-parse','FETCH_HEAD'],bare).decode().strip()
    assert remote_commit==commit
    workspace_tree=run(['git','rev-parse',commit+'^{tree}'],bare).decode().strip()
    directory_tree=run(['git','rev-parse',commit+':'+prefix.rstrip('/')],bare).decode().strip()
    remote_tree=run(['git','ls-tree','-rz',commit,'--',prefix],bare)
    local_tree=subprocess.check_output(['git','ls-tree','-rz',commit,'--',prefix],cwd=REPO)
    assert remote_tree==local_tree
    entries=[]
    for e in remote_tree.split(b'\0'):
        if not e:continue
        meta,path=e.decode().split('\t');mode,typ,blob=meta.split();entries.append((path,mode,typ,blob))
    def read(entry):
        path,mode,typ,blob=entry
        t=datetime.datetime.now(datetime.timezone.utc).isoformat()
        raw='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path,safe='/')
        with urllib.request.urlopen(raw,timeout=45) as response:
            data=response.read();status=response.status
        local=subprocess.check_output(['git','show',commit+':'+path],cwd=REPO)
        actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        assert status==200 and data==local and actual==blob and typ=='blob'
        data.decode('utf-8')
        return dict(path=path,mode=mode,git_type=typ,git_blob=blob,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),type='UTF-8 text',http_status=status,full_bytes_equal=True,started_utc=t,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        rows=list(pool.map(read,entries))
    result=dict(schema='r6-u08-r.remote-readback.v1',result='REMOTE_FULL_READBACK_MATCH',repository=url,commit=commit,branch=branch,workspace_tree=workspace_tree,directory_tree=directory_tree,path_prefix=prefix,payload_count=len(rows),payloads=rows,remote_tree_equal_local=True,started_utc=started,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),argv=sys.argv,cwd=str(REPO),commands=commands,level='TOOL_VALIDATION_ONLY',source_execution=False)
except Exception as exc:
    result=dict(result='READBACK_FAILURE',error=repr(exc),started_utc=started,ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),commands=commands)
    (OWN/outname).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    raise
(OWN/outname).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['result','commit','workspace_tree','directory_tree','payload_count']},ensure_ascii=False))
