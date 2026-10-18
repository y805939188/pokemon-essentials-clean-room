"""Fresh no-alternates remote byte readback of this review prefix only."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[5]
PREFIX='review/remediation-eighth-20261016-prepare/reviews/final-ultra/r1/'
BINDING='8ab43a609e60430492b219f0dce14ef4fdb8e47f'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--commit',required=True)
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    logs=[]
    remote=subprocess.check_output(['git','-C',str(ROOT),'remote','get-url','origin'],text=True).strip()
    branch=subprocess.check_output(['git','-C',str(ROOT),'branch','--show-current'],text=True).strip()
    env=os.environ.copy()
    for name in ['GIT_ALTERNATE_OBJECT_DIRECTORIES','GIT_OBJECT_DIRECTORY','GIT_DIR','GIT_WORK_TREE']:
        env.pop(name,None)
    def run(argv):
        start=datetime.now(timezone.utc).isoformat()
        p=subprocess.run(argv,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        logs.append({'argv':[x.replace(remote,'REMOTE_ORIGIN') for x in argv],'utc':start,'exit':p.returncode,
            'stdout_bytes':len(p.stdout),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),
            'stderr':p.stderr.decode(errors='replace').replace(remote,'REMOTE_ORIGIN')})
        if p.returncode:raise RuntimeError(json.dumps(logs[-1]))
        return p.stdout
    def tree(repo):
        raw=run(['git','-C',str(repo),'ls-tree','-rz',a.commit,'--',PREFIX])
        rows=[]
        for line in raw.split(b'\0'):
            if not line:continue
            left,path=line.split(b'\t',1); mode,kind,blob=left.decode().split()
            assert kind=='blob' and mode=='100644'
            rows.append((path.decode(),mode,blob))
        return rows
    expected=tree(ROOT)
    changed=run(['git','-C',str(ROOT),'diff','--name-only','-z',BINDING,a.commit]).split(b'\0')
    assert all(not x or x.decode().startswith(PREFIX) for x in changed)
    before=run(['git','-C',str(ROOT),'ls-remote','origin','refs/heads/'+branch]).decode().split()[0]
    assert before==a.commit
    records=[]
    with tempfile.TemporaryDirectory(prefix='r8-final-fresh-',dir='/tmp') as tmp:
        fresh=Path(tmp)/'remote.git'
        run(['git','init','--bare',str(fresh)])
        assert not (fresh/'objects/info/alternates').exists()
        run(['git','-C',str(fresh),'fetch','--no-tags',remote,'refs/heads/'+branch])
        assert run(['git','-C',str(fresh),'rev-parse','FETCH_HEAD']).decode().strip()==a.commit
        assert tree(fresh)==expected
        for path,mode,blob in expected:
            # Full blob bytes are consumed and compared, never just a hash list.
            b=run(['git','-C',str(fresh),'cat-file','blob',blob])
            local=(ROOT/path).read_bytes()
            assert b==local, path
            records.append({'path':path,'mode':mode,'blob':blob,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'remote_complete_bytes_equal_worktree':True})
        assert not (fresh/'objects/info/alternates').exists()
    after=run(['git','-C',str(ROOT),'ls-remote','origin','refs/heads/'+branch]).decode().split()[0]
    assert after==a.commit
    result={'schema':'r8-final-review-fresh-remote-readback/v1','verified_utc':datetime.now(timezone.utc).isoformat(),
        'review_commit':a.commit,'branch':branch,'remote_ref_before':before,'remote_ref_after':after,
        'fresh_bare_no_alternates':True,'complete_review_prefix':PREFIX,'files':len(records),'bytes':sum(v['bytes'] for v in records),
        'all_complete_remote_bytes_equal':True,'all_commit_changes_confined_to_own_prefix':True,'records':records,'commands':logs,
        'qualification':'Readback of a real preceding commit; no self futurehash. Final successor receipt is itself fully read back before external finalSHA delivery. No main merge or source/business execution.'}
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['review_commit','files','bytes','all_complete_remote_bytes_equal']}))

if __name__=='__main__':main()
