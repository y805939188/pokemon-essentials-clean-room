"""Read every published task blob from a separate Git object store."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import subprocess

T=Path(__file__).resolve().parent
REPO=T.parents[4]
PREFIX=str(T.relative_to(REPO))
def git(repo,*args):
    return subprocess.check_output(['git','--git-dir='+str(repo),*args])
def listing(repo,commit):
    rows={}
    for entry in git(repo,'ls-tree','-rz',commit,'--',PREFIX).split(b'\0'):
        if not entry:continue
        attrs,path=entry.split(b'\t',1)
        mode,kind,blob=attrs.decode().split()
        assert kind=='blob' and mode=='100644'
        rows[path.decode()]=(mode,blob)
    return rows
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--remote-git-dir',required=True)
    ap.add_argument('--commit',required=True)
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    remote=Path(args.remote_git_dir)
    assert remote.resolve()!=(REPO/'.git').resolve()
    assert not (remote/'objects/info/alternates').exists()
    expected=listing(REPO/'.git',args.commit)
    actual=listing(remote,args.commit)
    assert actual==expected
    rows=[]
    for path,(mode,blob) in sorted(expected.items()):
        local_data=git(REPO/'.git','cat-file','blob',blob)
        remote_data=git(remote,'cat-file','blob',blob)
        assert remote_data==local_data
        rows.append({'path':path,'mode':mode,'git_blob':blob,'bytes':len(remote_data),'sha256':hashlib.sha256(remote_data).hexdigest(),'complete_bytes_read':True,'exact':True})
    tree=git(remote,'rev-parse',args.commit+'^{tree}').decode().strip()
    local_tree=git(REPO/'.git','rev-parse',args.commit+'^{tree}').decode().strip()
    assert tree==local_tree
    tasktree=git(remote,'rev-parse',args.commit+':'+PREFIX).decode().strip()
    assert tasktree==git(REPO/'.git','rev-parse',args.commit+':'+PREFIX).decode().strip()
    changed=[x.decode() for x in git(REPO/'.git','diff-tree','--no-commit-id','--name-only','-r','-z','40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232',args.commit).split(b'\0') if x]
    assert set(changed)==set(actual)
    published_ledger=json.loads(git(remote,'show',args.commit+':'+PREFIX+'/reception-ledger.json'))
    out={'schema':'gr8-elr-complete-remote-publication-readback/v3','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':args.commit,'checkout_tree':tree,'task_tree':tasktree,'task_prefix':PREFIX,'remote_git_dir':str(remote),'collection_exact':True,'full_bytes_mode_blob_sha_exact':True,'all_changed_paths_in_exclusive_write_set':True,'files':rows,'count':len(rows),'bytes':sum(x['bytes'] for x in rows),'cache_boundary':'Previously fetched fixed contract/report objects retained only to negotiate history; current report fetched from GitHub after ordinary push; no alternates/shared object access. Every current task payload read in full again.','semantic_credit':'NONE_TRANSPORT_ONLY','task_state':published_ledger['status'],'root_final_signed':published_ledger.get('root_final_signed',False),'UPDATE_NOT_STARTED':True}
    Path(args.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='files'},ensure_ascii=False))
if __name__=='__main__':main()
