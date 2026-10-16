"""Fetch a dedicated report branch into an independent /tmp object store.

Read every report blob fully and compare path/mode/blob/bytes/SHA256/tree against
the local fixed commit. This validates report transfer, not review semantics.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import subprocess
import tempfile

ap=argparse.ArgumentParser()
ap.add_argument('--commit',required=True)
ap.add_argument('--output',required=True)
args=ap.parse_args()
SPEC=pathlib.Path('/workspace/pokemon-essentials-clean-room')
TASK='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/external_pbs_creature_backups'
BRANCH='codex/r8-external-pbs-creature-backups-20261016'
URL='https://github.com/y805939188/pokemon-essentials-clean-room.git'
TMP=pathlib.Path(tempfile.mkdtemp(prefix='r8-xpcb-remote-',dir='/tmp'))
logs=[]

def run(cwd,argv,timeout=55):
    begin=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.run(argv,cwd=cwd,capture_output=True,timeout=timeout)
    logs.append(dict(cwd=str(cwd),argv=argv,stdout=p.stdout.decode(errors='replace'),stderr=p.stderr.decode(errors='replace'),
                     exit_code=p.returncode,start_utc=begin,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
    if p.returncode: raise RuntimeError('Command failed: '+repr(argv))
    return p.stdout

def entries(repo,commit):
    out=run(repo,['git','ls-tree','-r','-z',commit,'--',TASK])
    result=[]
    for row in out.split(b'\0'):
        if not row: continue
        meta,path=row.split(b'\t',1)
        mode,kind,blob=meta.decode().split()
        if kind!='blob': raise RuntimeError('Unexpected non-blob report object')
        result.append((path.decode(),mode,blob))
    return result

def read_all_blobs(repo,rows):
    # Exact raw blob bytes are consumed, not printed, then independently hashed.
    begin=datetime.datetime.now(datetime.timezone.utc).isoformat()
    proc=subprocess.Popen(['git','cat-file','--batch'],cwd=repo,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    answer=[]
    for path,mode,blob in rows:
        proc.stdin.write((blob+'\n').encode()); proc.stdin.flush()
        header=proc.stdout.readline().decode().strip().split()
        if len(header)!=3 or header[0]!=blob or header[1]!='blob':
            proc.kill(); raise RuntimeError('Bad cat-file header '+repr(header))
        size=int(header[2]); data=proc.stdout.read(size)
        if len(data)!=size or proc.stdout.read(1)!=b'\n':
            proc.kill(); raise RuntimeError('Incomplete blob '+path)
        actual_blob=hashlib.sha1(b'blob '+str(size).encode()+b'\0'+data).hexdigest()
        answer.append(dict(path=path,mode=mode,blob=blob,bytes=size,sha256=hashlib.sha256(data).hexdigest(),
                           full_bytes_read=True,git_blob_recomputed=(actual_blob==blob)))
    proc.stdin.close()
    stderr=proc.stderr.read().decode(errors='replace')
    code=proc.wait()
    logs.append(dict(cwd=str(repo),argv=['git','cat-file','--batch'],stdout='Binary blob stream consumed in full; identities recorded per payload.',
                     stderr=stderr,exit_code=code,blob_count=len(answer),raw_binary_stdout_not_duplicated=True,
                     start_utc=begin,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
    if code or not all(x['git_blob_recomputed'] for x in answer): raise RuntimeError('Blob validation failed')
    return answer

start=datetime.datetime.now(datetime.timezone.utc).isoformat()
result=dict(schema='r8-task-remote-readback/v1',start_utc=start,branch=BRANCH,commit=args.commit,
            remote_url=URL,independent_store=str(TMP),alternates_used=False,evidence_level='TOOL_TRANSMISSION_VALIDATION_ONLY',semantic_credit_added=0)
try:
    run(TMP,['git','init','--quiet'])
    run(TMP,['git','remote','add','origin',URL])
    run(TMP,['git','fetch','--quiet','--no-tags','--filter=blob:none','--depth=1','origin','refs/heads/'+BRANCH])
    actual=run(TMP,['git','rev-parse','FETCH_HEAD']).decode().strip()
    if actual!=args.commit: raise RuntimeError('Remote tip differs from requested fixed commit')
    if (TMP/'.git/objects/info/alternates').exists(): raise RuntimeError('Unexpected alternates')
    result['commit_tree']=run(TMP,['git','rev-parse',args.commit+'^{tree}']).decode().strip()
    result['report_tree']=run(TMP,['git','rev-parse',args.commit+':'+TASK]).decode().strip()
    localtree=run(SPEC,['git','rev-parse',args.commit+':'+TASK]).decode().strip()
    localroot=run(SPEC,['git','rev-parse',args.commit+'^{tree}']).decode().strip()
    remote_rows=entries(TMP,args.commit)
    local_rows=entries(SPEC,args.commit)
    if remote_rows!=local_rows: raise RuntimeError('Report path/mode/blob list mismatch')
    remote=read_all_blobs(TMP,remote_rows)
    local=read_all_blobs(SPEC,local_rows)
    if remote!=local or localtree!=result['report_tree'] or localroot!=result['commit_tree']:
        raise RuntimeError('Full blob identity/tree mismatch')
    result.update(status='PASS_FULL_REMOTE_BYTES',payload_count=len(remote),total_bytes=sum(r['bytes'] for r in remote),
                  payloads=remote,all_path_mode_blob_bytes_sha256_match=True,report_tree_match=True,commit_tree_match=True)
except Exception as exc:
    result.update(status='FAIL',error=repr(exc))
result.update(end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),io=logs)
pathlib.Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('io','payloads')},ensure_ascii=False))
raise SystemExit(0 if result['status']=='PASS_FULL_REMOTE_BYTES' else 1)
