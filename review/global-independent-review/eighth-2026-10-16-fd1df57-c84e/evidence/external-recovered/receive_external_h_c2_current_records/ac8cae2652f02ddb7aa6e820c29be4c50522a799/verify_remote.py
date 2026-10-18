"""Read every report blob from a separately fetched remote-only bare repository.

The bare repository must have no alternates. No payload is imported or executed.
Exact unchanged files may use this same bare's earlier remote-downloaded objects.
"""
import argparse, datetime, gzip, hashlib, json, subprocess
from pathlib import Path

T=Path(__file__).resolve().parent
REPO=T.parents[4]
PREFIX=str(T.relative_to(REPO))
def digest(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('commit');ap.add_argument('--output',required=True);ap.add_argument('--bare',default='/tmp/r8-receive-h-c2-remote.git');a=ap.parse_args();bare=Path(a.bare)
    assert not (bare/'objects/info/alternates').exists()
    def remote(*args):return subprocess.check_output(['git','--git-dir='+str(bare),*args],stderr=subprocess.PIPE)
    def local(*args):return subprocess.check_output(['git','-C',str(REPO),*args],stderr=subprocess.PIPE)
    remote_tree=remote('rev-parse',a.commit+'^{tree}').decode().strip();assert remote_tree==local('rev-parse',a.commit+'^{tree}').decode().strip()
    task_tree=remote('rev-parse',a.commit+':'+PREFIX).decode().strip();assert task_tree==local('rev-parse',a.commit+':'+PREFIX).decode().strip()
    rt=remote('ls-tree','-r','-z',a.commit+':'+PREFIX);lt=local('ls-tree','-r','-z',a.commit+':'+PREFIX);assert rt==lt
    rows=[]
    for entry in rt.split(b'\0'):
        if not entry:continue
        header,path=entry.split(b'\t');mode,kind,blob=header.decode().split();assert kind=='blob';p=path.decode()
        # Promisor fetch retrieves a missing blob from the configured remote,
        # never the local author object database.
        data=remote('cat-file','blob',blob);own=local('cat-file','blob',blob);assert data==own
        identity=digest(data);assert identity['git_blob']==blob
        r={'path':p,'mode':mode,**identity,'remote_full_blob_read':True,'local_equal':True}
        if p.endswith('.gz'):
            d=gzip.decompress(data);od=gzip.decompress(own);assert d==od;r['decoded']=digest(d);r['decoded_identity_verified']=True
        rows.append(r)
        if len(rows)%10==0:print('remote files verified',len(rows),flush=True)
    progress=json.loads(remote('show',a.commit+':'+PREFIX+'/progress.json'))
    out={'schema':'gr8.report.remote-readback/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':a.commit,'checkout_tree':remote_tree,'task_tree':task_tree,'bare':str(bare),'alternates':False,'exact_path_mode_blob_collection_equal':True,'files':rows,'file_count':len(rows),'bytes':sum(r['bytes'] for r in rows),'semantic_credit':0,'task_semantic_status':progress['status'],'update_started':progress['update_started']}
    Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='files'}),flush=True)
if __name__=='__main__':main()
