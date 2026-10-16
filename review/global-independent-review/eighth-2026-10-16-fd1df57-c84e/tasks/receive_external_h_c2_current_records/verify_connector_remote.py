"""Verify exact-commit connector bytes plus prior independent remote-only bytes.
Transport data is never executed. Every new/changed blob requires complete base64
at the fixed published commit. Unchanged blobs reuse the earlier no-alternates
bare; no local object borrowing or silent lazy fetch. Git commit metadata, all
ancestor trees and recursive task tree bind the exact path/mode/blob collection.
Reading/hashing grants zero semantic credit.
"""
import argparse, base64, datetime, gzip, hashlib, json, os, subprocess
from pathlib import Path
T=Path(__file__).resolve().parent
REPO=T.parents[4]
PREFIX=str(T.relative_to(REPO))
def digest(b):
    return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
def tree_hash(entries):
    rows=sorted(entries,key=lambda r:r['path'].encode()+(b'/' if r['type']=='tree' else b''))
    raw=b''.join((r['mode'].lstrip('0')+' ').encode()+r['path'].encode()+b'\0'+bytes.fromhex(r['sha']) for r in rows)
    return hashlib.sha1(b'tree '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('bundle');ap.add_argument('--base',required=True);ap.add_argument('--output',required=True);ap.add_argument('--bare',default='/tmp/r8-receive-h-c2-remote.git');a=ap.parse_args();bare=Path(a.bare)
    assert not (bare/'objects/info/alternates').exists()
    b=json.loads(Path(a.bundle).read_text());commit=b['commit']['sha']
    def git(*args):return subprocess.check_output(['git','-C',str(REPO),*args],stderr=subprocess.PIPE)
    def remote(*args):
        env=dict(os.environ,GIT_NO_LAZY_FETCH='1',GIT_TERMINAL_PROMPT='0')
        return subprocess.check_output(['git','--git-dir='+str(bare),*args],env=env,stderr=subprocess.PIPE)
    assert b['branch']['object']['sha']==commit
    assert b['commit']['tree']['sha']==git('rev-parse',commit+'^{tree}').decode().strip()
    ancestors={r['path']:r['tree'] for r in b['ancestors']}
    assert ancestors['']['sha']==b['commit']['tree']['sha']
    parts=PREFIX.split('/')
    for depth in range(len(parts)):
        p='/'.join(parts[:depth]);tree=ancestors[p]
        assert not tree.get('truncated') and tree_hash(tree['tree'])==tree['sha']
        child=next(r for r in tree['tree'] if r['path']==parts[depth])
        expected=ancestors['/'.join(parts[:depth+1])]['sha'] if depth+1<len(parts) else b['task_tree']['sha']
        assert child['type']=='tree' and child['mode']=='040000' and child['sha']==expected
    task=b['task_tree'];assert not task['truncated']
    assert task['sha']==git('rev-parse',commit+':'+PREFIX).decode().strip()
    local={}
    for entry in git('ls-tree','-r','-z',commit+':'+PREFIX).split(b'\0'):
        if entry:
            header,path=entry.split(b'\t');mode,kind,sha=header.decode().split();local[path.decode()]=(mode,kind,sha)
    received={r['path']:(r['mode'],r['type'],r['sha']) for r in task['tree'] if r['type']!='tree'}
    assert received==local
    all_rows=task['tree'];tree_ids={'':task['sha'],**{r['path']:r['sha'] for r in all_rows if r['type']=='tree'}}
    for p,sha in tree_ids.items():
        prefix=p+'/' if p else ''
        children=[dict(r,path=r['path'][len(prefix):]) for r in all_rows if r['path'].startswith(prefix) and '/' not in r['path'][len(prefix):]]
        assert tree_hash(children)==sha
    changed=set(git('diff','--name-only',a.base,commit,'--',PREFIX).decode().splitlines())
    supplied={r['path']:r for r in b['changed_files']}
    assert len(supplied)==len(b['changed_files']) and set(supplied)==changed
    prior={}
    for entry in remote('ls-tree','-r','-z',a.base+':'+PREFIX).split(b'\0'):
        if entry:
            header,path=entry.split(b'\t');mode,kind,sha=header.decode().split();prior[path.decode()]=(mode,kind,sha)
    rows=[]
    for p,(mode,kind,sha) in sorted(local.items()):
        full=PREFIX+'/'+p;own=git('cat-file','blob',sha)
        if full in supplied:
            r=supplied[full];assert r['encoding']=='base64' and r['sha']==sha
            data=base64.b64decode(''.join(r['content'].split()),validate=True);origin='exact-commit GitHub connector full base64 file'
        else:
            assert prior[p]==(mode,kind,sha)
            data=remote('cat-file','blob',sha);origin='prior independent remote-only bare exact unchanged blob'
        identity=digest(data);assert data==own and identity['git_blob']==sha
        entry=next(r for r in all_rows if r['path']==p);assert entry['size']==len(data)
        row=dict(path=p,mode=mode,**identity,remote_full_blob_read=True,local_equal=True,transport_origin=origin)
        if p.endswith('.gz'):
            decoded=gzip.decompress(data);assert decoded==gzip.decompress(own);row['decoded']=digest(decoded);row['decoded_identity_verified']=True
        rows.append(row)
    out=dict(schema='gr8.report.connector-remote-readback/v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),commit=commit,checkout_tree=b['commit']['tree']['sha'],task_tree=task['sha'],branch=b['branch']['ref'],branch_head=commit,base_remote_cache_commit=a.base,bare=str(bare),alternates=False,exact_remote_commit_and_ancestor_tree_chain=True,all_remote_trees_reconstructed=True,exact_path_mode_blob_collection_equal=True,connector_full_changed_file_count=len(supplied),prior_remote_unchanged_file_count=len(rows)-len(supplied),files=rows,file_count=len(rows),bytes=sum(r['bytes'] for r in rows),git_https_authentication='FAILED_AFTER_SUCCESSFUL_ORDINARY_CORE_PUSH; GitHub connector fallback succeeded',semantic_credit=0,task_semantic_status='INCOMPLETE',update_started=False)
    Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='files'},ensure_ascii=False))
if __name__=='__main__':main()
