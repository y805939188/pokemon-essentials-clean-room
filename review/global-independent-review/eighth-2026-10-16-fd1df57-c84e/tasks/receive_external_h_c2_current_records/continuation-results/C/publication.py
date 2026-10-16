"""Independent remote readback of this C directory only, without object alternates."""
from pathlib import Path
import argparse,datetime,hashlib,json,subprocess
T=Path(__file__).resolve().parent;ROOT=Path('/workspace/pokemon-essentials-clean-room');W=T/'.work';BASE='1b46a33526f086241c765b700155c5406a86f65e';BRANCH='codex/r8-c2-reception-c-20261016';URL='https://github.com/y805939188/pokemon-essentials-clean-room.git';PREFIX=str(T.relative_to(ROOT))
def run(args,**kw):return subprocess.check_output(args,stderr=subprocess.PIPE,**kw)
def local(*a):return run(['git','-C',str(ROOT),*a])
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('commit');ap.add_argument('--receipt');a=ap.parse_args();c=a.commit
 advertised=run(['git','ls-remote','--heads',URL,'refs/heads/'+BRANCH]).decode().strip();assert advertised.split()[0]==c,(c,advertised)
 bare=W/'publication-remote.git'
 if not bare.exists():
  run(['git','init','--bare',str(bare)])
  for key,val in [('remote.origin.url',URL),('remote.origin.promisor','true'),('remote.origin.partialclonefilter','blob:none'),('extensions.partialclone','origin')]:run(['git','--git-dir='+str(bare),'config',key,val])
 assert not (bare/'objects/info/alternates').exists()
 def remote(*x):return run(['git','--git-dir='+str(bare),*x])
 remote('fetch','--no-tags','--depth=1','--filter=blob:none','origin',c)
 changed=local('diff','--name-only',BASE,c).decode().splitlines();assert changed and all(p.startswith(PREFIX+'/') for p in changed)
 rawtree=local('ls-tree','-rz',c,'--',PREFIX);remote_tree=remote('ls-tree','-rz',c,'--',PREFIX);assert rawtree==remote_tree
 entries=[]
 for x in rawtree.split(b'\0'):
  if not x:continue
  header,path=x.split(b'\t',1);mode,kind,blob=header.decode().split();assert kind=='blob';entries.append((mode,blob,path.decode()))
 # Explicitly request only this publication's blobs from the remote. No baseline blobs read.
 remote('fetch','--no-tags','--no-write-fetch-head','origin',*sorted({b for _,b,_ in entries}))
 files=[]
 for mode,blob,path in entries:
  b=remote('cat-file','blob',blob);expected=local('show',c+':'+path);assert b==expected;assert ident(b)['git_blob']==blob
  files.append({'path':path,'mode':mode,**ident(b)})
 ct=remote('rev-parse',c+'^{tree}').decode().strip();st=remote('rev-parse',c+':'+PREFIX).decode().strip()
 out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'COMPLETE_REMOTE_READBACK_OWN_INCREMENT_ONLY','remote':URL,'branch':BRANCH,'advertised_branch_line':advertised,'commit':c,'checkout_tree':ct,'C_subtree':st,'base':BASE,'changed_paths':changed,'readback_file_count':len(files),'readback_bytes':sum(f['bytes'] for f in files),'files':files,'isolation':'New partial bare, no alternates; commit/trees fetched from remote and exactly this C-directory blob set requested/read; parent/reference/other report blobs not read back.','credit':'TRANSPORT_IDENTITY_ONLY; no semantic/runtime credit'}
 if a.receipt:(T/a.receipt).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ['files','changed_paths']},ensure_ascii=False))
if __name__=='__main__':main()
