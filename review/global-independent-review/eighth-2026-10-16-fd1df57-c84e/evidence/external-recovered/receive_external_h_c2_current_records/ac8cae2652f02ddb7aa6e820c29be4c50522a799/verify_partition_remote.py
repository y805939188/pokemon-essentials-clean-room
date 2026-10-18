"""Receiver-owned full remote subtree verifier; imports no partition scripts."""
import argparse, datetime, gzip, hashlib, json, subprocess
from pathlib import Path
T=Path(__file__).resolve().parent
REPO=T.parents[4]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('commit');ap.add_argument('--prefix',required=True);ap.add_argument('--bare',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
    assert not (Path(a.bare)/'objects/info/alternates').exists()
    def remote(*args):return subprocess.check_output(['git','--git-dir='+a.bare,*args],stderr=subprocess.PIPE)
    def local(*args):return subprocess.check_output(['git','-C',str(REPO),*args],stderr=subprocess.PIPE)
    def identity(data):return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())
    tree=remote('rev-parse',a.commit+'^{tree}').decode().strip();assert tree==local('rev-parse',a.commit+'^{tree}').decode().strip()
    subtree=remote('rev-parse',a.commit+':'+a.prefix).decode().strip();assert subtree==local('rev-parse',a.commit+':'+a.prefix).decode().strip()
    entries=remote('ls-tree','-r','-z',a.commit+':'+a.prefix);assert entries==local('ls-tree','-r','-z',a.commit+':'+a.prefix)
    rows=[]
    for entry in entries.split(b'\0'):
        if not entry:continue
        header,path=entry.split(b'\t');mode,kind,blob=header.decode().split();assert kind=='blob'
        data=remote('cat-file','blob',blob);assert data==local('cat-file','blob',blob);ids=identity(data);assert ids['git_blob']==blob
        row=dict(path=path.decode(),mode=mode,**ids,full_remote_bytes_equal=True)
        if path.endswith(b'.gz'):row['decoded']=identity(gzip.decompress(data))
        rows.append(row)
        if len(rows)%20==0:print('partition remote files verified',len(rows),flush=True)
    out=dict(schema='gr8.partition.receiver-full-remote-readback/v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),commit=a.commit,checkout_tree=tree,subtree=subtree,prefix=a.prefix,bare=a.bare,alternates=False,exact_path_mode_blob_collection_equal=True,files=rows,file_count=len(rows),bytes=sum(r['bytes'] for r in rows),semantic_credit=0)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True);Path(a.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='files'}),flush=True)
if __name__=='__main__':main()
