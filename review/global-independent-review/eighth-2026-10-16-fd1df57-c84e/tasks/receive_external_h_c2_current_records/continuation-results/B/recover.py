"""Inert fixed-commit restoration. Never execute recovered scripts or game code."""
from pathlib import Path
import subprocess,json,gzip,hashlib,datetime,os
T=Path(__file__).resolve().parent
P=T.parent.parent
REPO=next(p for p in T.parents if (p/'.git').is_dir())
W=T/'.work'; W.mkdir(exist_ok=True)
C='967b90fac83a6b0c3313087d8871312b4eac18b9'
C2='4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
def identity(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def run(a):return subprocess.check_output(a,cwd=REPO)
bare=W/'target.git'
if not bare.exists():
 run(['git','init','--bare',str(bare)])
 (bare/'objects/info/alternates').write_text(str(REPO/'.git/objects')+'\n')
fetch=['git','--git-dir='+str(bare),'fetch','--no-tags','https://github.com/y805939188/pokemon-essentials-clean-room.git',C]
p=subprocess.run(fetch,cwd=REPO,capture_output=True)
assert p.returncode==0,p.stderr.decode()
readset=json.loads((P/'continuation-v2/B.complete.json').read_text())
rows=[]
for f in readset['files']:
 path=f['remote_path_at_target_commit']; data=run(['git','--git-dir='+str(bare),'show',C+':'+path]); actual=identity(data)
 mode,kind,blob=run(['git','--git-dir='+str(bare),'ls-tree',C,'--',path]).decode().split('\t')[0].split()
 assert kind=='blob' and mode==f['mode'] and blob==f['git_blob']
 assert all(actual[k]==f[k] for k in actual)
 q=W/'target'/f['relative_to_target_task'];q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(data)
 rows.append(dict(input=f,actual=actual,semantic_credit=0))
actualset=run(['git','--git-dir='+str(bare),'ls-tree','-r','--name-only',C,'--',str(Path(readset['files'][0]['remote_path_at_target_commit']).parent)]).decode().splitlines()
assert set(actualset)=={r['remote_path_at_target_commit'] for r in readset['files']}
original=[]
for f in json.loads((W/'target/material-inventory.json').read_text()):
 path=f.get('transport_path',f['path']);raw=run(['git','show',C2+':'+path]);mode,kind,blob=run(['git','ls-tree',C2,'--',path]).decode().split('\t')[0].split()
 assert mode==f['mode'] and kind=='blob'
 if 'transport_path' in f:
  enc=f['encoded_identity'];a=identity(raw)
  assert a==dict(bytes=enc['transport_bytes'],sha256=enc['transport_sha256'],git_blob=enc['transport_git_blob_content_id']) and blob==a['git_blob']
  data=gzip.decompress(raw)
 else:data=raw
 a=identity(data);assert a==dict(bytes=f['bytes'],sha256=f['sha256'],git_blob=f.get('git_blob',f.get('actual_git_blob')))
 q=W/'originals'/str(f['index']);q.parent.mkdir(exist_ok=True);q.write_bytes(data)
 original.append(dict(input=f,encoded=identity(raw),decoded=a,semantic_credit=0))
save(T/'recovery.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),target=C,target_tree=run(['git','--git-dir='+str(bare),'rev-parse',C+'^{tree}']).decode().strip(),fetch=dict(args=fetch,exit=p.returncode,stdout=p.stdout.decode(),stderr=p.stderr.decode()),cache='Exact Git objects reused through disclosed local alternates; exact remote fetch still performed',target_files=rows,original_commit=C2,original_files=original,source_behavior_executed=False))
print('45 target / 25 C2 original payloads verified; reading credit 0')
