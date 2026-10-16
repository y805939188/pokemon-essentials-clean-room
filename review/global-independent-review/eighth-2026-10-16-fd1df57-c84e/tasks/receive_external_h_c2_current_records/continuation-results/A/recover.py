"""Inert byte restoration only; never execute any restored program."""
from pathlib import Path
import subprocess, json, gzip, hashlib, os
T=Path(__file__).resolve().parent
REPO=T.parents[6]
C='967b90fac83a6b0c3313087d8871312b4eac18b9'
C2='4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
def run(*a): return subprocess.check_output(a)
def ident(b): return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
def save(p,v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def main():
    work=T/'.work';work.mkdir(exist_ok=True)
    bare=work/'remote.git'
    if not bare.exists():
        run('git','init','--bare',str(bare))
        (bare/'objects/info/alternates').write_text(str(REPO/'.git/objects')+'\n')
    io=[]
    for c in [C,C2]:
        p=subprocess.run(['git','--git-dir='+str(bare),'fetch','--no-tags','https://github.com/y805939188/pokemon-essentials-clean-room.git',c],capture_output=True,text=True)
        io.append(dict(commit=c,exit=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0
    def git(*args): return run('git','--git-dir='+str(bare),*args)
    readset=json.loads((T.parent.parent/'continuation-v2/A.complete.json').read_text())
    receipts=[]
    out=work/'target';out.mkdir(exist_ok=True)
    for f in readset['files']:
        path=f['remote_path_at_target_commit'];b=git('show',C+':'+path);actual=ident(b)
        assert all(actual[k]==f[k] for k in actual)
        assert git('ls-tree',C,'--',path).decode().split()[0]==f['mode']
        p=out/f['relative_to_target_task'];p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
        receipts.append(dict(input=f,actual=actual,credit=0))
    inv=json.loads((out/'material-inventory.json').read_text());originals=work/'originals';originals.mkdir(exist_ok=True);orig=[]
    for f in inv:
        path=f.get('transport_path',f['path']);encoded=git('show',C2+':'+path);b=gzip.decompress(encoded) if f.get('transport_path') else encoded
        actual=ident(b);assert actual['bytes']==f['bytes'] and actual['sha256']==f['sha256'] and actual['git_blob']==f.get('git_blob',f.get('actual_git_blob'))
        (originals/str(f['index'])).write_bytes(b);orig.append(dict(input=f,actual=actual,encoded=ident(encoded),credit=0))
    save(T/'recovery.json',dict(target=C,original_commit=C2,cache='own bare with read-only alternates to this workspace clone; ordinary exact HTTPS fetch',io=io,target_files=receipts,originals=orig,reading_credit=0))
    save(T/'independence.json',dict(target_author='01a143b2-b02d-7094-808b-a4e9de51301b',parent_receiver='01a14465-f204-7783-a526-9b43e91ea005',actual_context=os.environ.get('CODEX_THREAD_ID','UNVERIFIED'),session=os.environ.get('CODEX_SESSION_ID','UNVERIFIED'),model='UNVERIFIED',effort='UNVERIFIED',tier='UNVERIFIED',speed='UNVERIFIED',Fast='UNVERIFIED',spawned=0))
    print('recovered',len(receipts),sum(x['actual']['bytes'] for x in receipts),'target bytes;',len(orig),'C2 originals; reading credit 0')
if __name__=='__main__':main()
