"""Publish the authorized review branch and read every review blob from remote."""
import datetime, hashlib, json, pathlib, subprocess, sys

ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
REL='review/remediation-sixth-20261014-prepare/reviews/R6-U10-R'
OUT=ROOT/REL
BRANCH='codex/remediation-sixth-r6-u10-review-20261014'
BASE='d3554f9479fadcd1255cf8103b19e4aa88e1825b'
mode=sys.argv[1]
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
commands=[]
def run(argv,cwd=ROOT):
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.Popen(argv,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout,stderr=p.communicate()
    commands.append(dict(argv=argv,cwd=str(cwd),pid=p.pid,started_utc=start,
        ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit_code=p.returncode,
        stdout_bytes=len(stdout),stdout_sha256=hashlib.sha256(stdout).hexdigest(),
        stderr=stderr.decode('utf-8',errors='replace'),
        stdout_text=stdout.decode('utf-8',errors='replace') if len(stdout)<10000 and argv[-2:-1]!=['blob'] else 'COMPLETE_BYTES_CONSUMED_DIGEST_RECORDED'))
    if p.returncode: raise RuntimeError(stderr.decode('utf-8',errors='replace'))
    return stdout
try:
    local_commit=run(['git','rev-parse','HEAD']).decode().strip()
    assert run(['git','branch','--show-current']).decode().strip()==BRANCH
    diff=run(['git','diff','--name-only',BASE,local_commit]).decode().splitlines()
    assert diff and all(p.startswith(REL+'/') for p in diff),diff
    remote='https://github.com/y805939188/pokemon-essentials-clean-room.git'
    before=run(['git','ls-remote','origin','refs/heads/'+BRANCH]).decode().strip()
    push=run(['git','push','origin','HEAD:refs/heads/'+BRANCH]).decode()
    bare=OUT/('remote-readback-'+mode+'.git')
    assert not bare.exists(), 'Fresh remote object store required for each publication phase'
    run(['git','init','--bare','--quiet',str(bare)])
    run(['git','--git-dir='+str(bare),'remote','add','origin',remote])
    run(['git','--git-dir='+str(bare),'fetch','--no-tags','--depth=1','--filter=blob:none','origin','refs/heads/'+BRANCH])
    cmd=['git','--git-dir='+str(bare)]
    remote_commit=run(cmd+['rev-parse','FETCH_HEAD']).decode().strip()
    assert remote_commit==local_commit,(remote_commit,local_commit)
    local_tree=run(['git','rev-parse',local_commit+'^{tree}']).decode().strip()
    remote_tree=run(cmd+['rev-parse',remote_commit+'^{tree}']).decode().strip()
    assert remote_tree==local_tree
    directory_tree=run(cmd+['rev-parse',remote_commit+':'+REL]).decode().strip()
    local_rows=run(['git','ls-tree','-r',local_commit,'--',REL]).decode().splitlines()
    remote_rows=run(cmd+['ls-tree','-r',remote_commit,'--',REL]).decode().splitlines()
    assert remote_rows==local_rows
    assert set(diff)=={line.split('\t',1)[1] for line in remote_rows}
    rows=[]
    for line in remote_rows:
        meta,path=line.split('\t',1); file_mode,file_type,blob=meta.split()
        local=run(['git','cat-file','blob',blob])
        received=run(cmd+['cat-file','blob',blob])
        assert local==received and file_mode=='100644' and file_type=='blob'
        assert hashlib.sha1(b'blob '+str(len(received)).encode()+b'\0'+received).hexdigest()==blob
        rows.append(dict(path=path,mode=file_mode,type=file_type,git_blob=blob,bytes=len(received),
            sha256=hashlib.sha256(received).hexdigest(),full_bytes_match=True))
    result=dict(kind='FULL_REMOTE_REVIEW_PAYLOAD_READBACK',mode=mode,commit=remote_commit,tree=remote_tree,
        review_directory_tree=directory_tree,branch=BRANCH,remote=remote,candidate=BASE,
        actual_remote_tip_before_push=before or 'ABSENT',normal_push_confirmed=True,
        fresh_independent_object_store=str(bare),alternates=False,paths=rows,payload_count=len(rows),
        payload_bytes=sum(r['bytes'] for r in rows),complete_declared_difference=True,
        all_full_bytes_sha256_blob_mode_type_path_match=True,started_utc=started,
        ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),cwd=str(ROOT),argv=sys.argv,
        independent_exit_code=0,commands=commands,
        scope='Git publication and byte verification only; no source/model/host behavior execution')
except Exception as e:
    result=dict(kind='PUBLICATION_FAILURE_PRESERVED',mode=mode,error=str(e),started_utc=started,
        ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),commands=commands)
    target=OUT/'local-evidence'/('publication-failure-'+mode+'.json')
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
    sys.exit(1)
target=OUT/('core-remote-readback.json' if mode=='core' else 'local-evidence/final-remote-readback.json')
target.parent.mkdir(exist_ok=True)
target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['commit','tree','review_directory_tree','payload_count','payload_bytes','all_full_bytes_sha256_blob_mode_type_path_match']},ensure_ascii=False,indent=2))
