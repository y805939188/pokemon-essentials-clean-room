#!/usr/bin/env python3
"""Fresh remote Git-object readback, independent of the worktree object database."""
from pathlib import Path
import argparse,datetime,hashlib,json,subprocess,tempfile
p=argparse.ArgumentParser();p.add_argument('commit');p.add_argument('--output',required=True);args=p.parse_args()
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
prefix=OUT.relative_to(ROOT).as_posix()+'/'
remote='https://github.com/y805939188/pokemon-essentials-clean-room.git'
records=[]
def run(argv,cwd):
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    r=subprocess.run(argv,cwd=cwd,capture_output=True)
    records.append({'argv':argv,'cwd':str(cwd),'started_utc':started,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':r.returncode,'stdout':r.stdout.decode(errors='replace'),'stderr':r.stderr.decode(errors='replace')})
    if r.returncode:raise RuntimeError(records[-1])
    return r.stdout
def tree(data):
    entries=[]
    for row in data.decode().splitlines():
        meta,path=row.split('\t',1);mode,kind,sha=meta.split()
        entries.append((path,mode,kind,sha))
    return entries
local=tree(run(['git','ls-tree','-r',args.commit,'--',prefix],ROOT))
result={'schema':'r8-disposition-review-fresh-remote-readback.v1','verified_commit':args.commit,'reviewed_candidate':'d62b41f4d620e50bb04c80a7505374bd284d8210','remote':remote,'scope':prefix,'fresh_object_database':True,'no_local_object_alternates':True}
try:
    with tempfile.TemporaryDirectory(prefix='r8-disposition-remote-') as tmp:
        fresh=Path(tmp)/'objects.git'
        run(['git','init','--bare',str(fresh)],ROOT)
        run(['git','remote','add','origin',remote],fresh)
        run(['git','fetch','--depth=1','--filter=blob:none','--no-tags','origin',args.commit],fresh)
        remote_entries=tree(run(['git','ls-tree','-r',args.commit,'--',prefix],fresh))
        assert local==remote_entries, 'remote review tree mismatch'
        blobs=sorted({sha for _,_,kind,sha in remote_entries if kind=='blob'})
        # Prime all selected blobs in one network round trip, using the same
        # reachable-object request used by partial clone lazy fetching.
        run(['git','fetch','--no-tags','origin',*blobs],fresh)
        checks=[]
        for path,mode,kind,sha in remote_entries:
            assert kind=='blob', (path,kind)
            data=subprocess.check_output(['git','cat-file','blob',sha],cwd=fresh)
            local_data=subprocess.check_output(['git','show',args.commit+':'+path],cwd=ROOT)
            assert data==local_data, path
            checks.append({'path':path,'git_mode':mode,'git_blob':sha,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'remote_bytes_equal_local_committed_bytes':True})
        result.update(result='PASS_FRESH_REMOTE_ALL_REVIEW_BYTES',files=checks,file_count=len(checks),bytes=sum(x['bytes'] for x in checks),remote_refs=run(['git','ls-remote','origin','refs/heads/main','refs/heads/codex/r8-disposition-tagging-20261017','refs/heads/codex/r8-disposition-review-d62b41f-20261017'],fresh).decode())
except Exception as exc:
    result.update(result='FAIL',error=str(exc));raise
finally:
    result['commands']=records
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['files','commands']},ensure_ascii=False))
