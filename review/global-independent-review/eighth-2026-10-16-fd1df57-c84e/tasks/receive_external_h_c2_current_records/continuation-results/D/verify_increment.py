"""Read only this D directory's fixed remote increment through an isolated partial bare."""
from pathlib import Path
import argparse
import datetime
import gzip
import hashlib
import json
import subprocess

P=Path(__file__).resolve().parent
ROOT=next(x for x in P.parents if (x/'.git').is_dir())
REL=P.relative_to(ROOT).as_posix()
BARE=P/'private/readback.git'
def git(args,remote=False):
    cmd=['git','--git-dir='+str(BARE)] if remote else ['git','-C',str(ROOT)]
    return subprocess.check_output(cmd+args,stderr=subprocess.PIPE)
def ident(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
      'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
def entries(commit,remote=False):
    lines=git(['ls-tree','-rz',commit,REL],remote).split(b'\0')
    result={}
    for line in lines:
        if not line:continue
        meta,path=line.decode().split('\t'); mode,kind,blob=meta.split()
        assert kind=='blob' and mode=='100644'
        result[path]=(mode,blob)
    return result
def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--commit',required=True);a.add_argument('--base',required=True)
    a.add_argument('--output',required=True)
    args=a.parse_args(); destination=P/args.output
    assert destination.resolve().is_relative_to(P.resolve())
    assert not (BARE/'objects/info/alternates').exists()
    expected=entries(args.commit)
    actual=entries(args.commit,True)
    assert expected==actual
    all_delta=git(['diff','--name-only',args.base,args.commit]).decode().splitlines()
    assert all(x.startswith(REL+'/') for x in all_delta)
    rows=[]
    for path,(mode,blob) in sorted(actual.items()):
        # Lazy fetch obtains the full promised blob from origin. Existing bytes
        # in this bare are only prior remotely verified D publication objects.
        data=git(['cat-file','blob',blob],True)
        local=git(['show',args.commit+':'+path])
        assert data==local
        details=ident(data);assert details['git_blob']==blob
        row={'path':path,'mode':mode,**details,'fixed_remote_commit':args.commit,
          'in_this_increment':path in all_delta,'byte_equal':True}
        if path.endswith('.json.gz'):
            decoded=gzip.decompress(data);json.loads(decoded)
            row['decoded']=ident(decoded)
        rows.append(row)
    tree=git(['rev-parse',args.commit+'^{tree}'],True).decode().strip()
    assert tree==git(['rev-parse',args.commit+'^{tree}']).decode().strip()
    dtree=git(['rev-parse',args.commit+':'+REL],True).decode().strip()
    assert dtree==git(['rev-parse',args.commit+':'+REL]).decode().strip()
    branch='refs/heads/codex/r8-c2-reception-d-20261016'
    live=git(['ls-remote','origin',branch]).decode().split()[0]
    assert live==args.commit
    result={'schema':'gr8-hc2-d-own-increment-remote-readback/v1',
      'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':args.commit,
      'base':args.base,'workspace_tree':tree,'D_directory':REL,'D_tree':dtree,
      'remote_branch':branch,'remote_ref_equal':True,'isolated_bare_no_alternates':True,
      'transport':'Git HTTPS partial bare; full bytes of every own D member, no old repository payload body download',
      'exact_set_and_all_mode_blob_bytes_SHA_equal':True,'files':rows,
      'files_count':len(rows),'total_bytes':sum(x['bytes'] for x in rows),
      'increment_paths':all_delta,'semantic_credit':0,'semantic_status':'INCOMPLETE',
      'behavior_execution':0,'UPDATE_NOT_STARTED':True}
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['commit','workspace_tree','D_tree','files_count','total_bytes','exact_set_and_all_mode_blob_bytes_SHA_equal','semantic_status']}))
if __name__=='__main__':main()
