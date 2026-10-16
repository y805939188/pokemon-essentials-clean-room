"""Recover an exact immutable input in a fresh bare repository. No input is executed."""
import datetime, hashlib, json, pathlib, subprocess
T=pathlib.Path(__file__).resolve().parent
P=T.parents[1]
C='a96ec67a948e3fc86b25ad407cd977b6752e2d77'
S=P/'delegation/readsets/receive_external_h_r6_effective_contracts.complete.json'
D=json.loads(S.read_text())
J=T/'runtime/remote.git'
O=T/'recovered'
assert not J.exists() and not O.exists()
(T/'inputs').mkdir(exist_ok=True)
(T/'inputs/readset.complete.json').write_bytes(S.read_bytes())
(T/'runtime').mkdir(exist_ok=True)
E=[]
def run(args):
 t=datetime.datetime.now(datetime.timezone.utc).isoformat()
 p=subprocess.run(args,capture_output=True)
 E.append(dict(args=args,start_utc=t,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit=p.returncode,stdout=p.stdout.decode(errors='backslashreplace'),stderr=p.stderr.decode(errors='backslashreplace')))
 (T/'recovery-events.json').write_text(json.dumps(E,ensure_ascii=False,indent=2)+'\n')
 assert p.returncode==0
 return p.stdout
run(['git','init','--bare',str(J)])
run(['git','--git-dir='+str(J),'fetch','--no-tags','--depth=1','https://github.com/y805939188/pokemon-essentials-clean-room.git',C])
g=['git','--git-dir='+str(J)]
assert run(g+['rev-parse',C+'^{tree}']).decode().strip()==D['target_checkout_tree']
prefix='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/external_h_r6_effective_contracts/'
listing=run(g+['ls-tree','-r','-z',C,'--',prefix])
a={}
for line in listing.split(b'\0'):
 if not line: continue
 m,p=line.split(b'\t',1); mode,kind,oid=m.decode().split(); assert kind=='blob'
 a[p.decode()]=(mode,oid)
assert set(a)=={f['remote_path_at_target_commit'] for f in D['files']}
assert len(a)==D['input_file_count']
O.mkdir()
R=[]
for f in D['files']:
 r=pathlib.PurePosixPath(f['relative_to_target_task'])
 assert not r.is_absolute() and '..' not in r.parts
 assert a[f['remote_path_at_target_commit']]==(f['mode'],f['git_blob'])
 b=subprocess.check_output(g+['cat-file','blob',f['git_blob']])
 assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256']
 assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==f['git_blob']
 q=O/r; q.parent.mkdir(parents=True,exist_ok=True); q.write_bytes(b)
 R.append(dict(f,local_path=str(q.relative_to(T)),disposition='EXACT_IDENTITY_RECOVERED_SEMANTIC_CREDIT_0'))
assert sum(x['bytes'] for x in R)==D['input_bytes']
result=dict(schema='receive-exact-remote-recovery/v1',status='VERIFIED',target_commit=C,checkout_tree=D['target_checkout_tree'],target_task_tree=run(g+['rev-parse',C+':'+prefix.rstrip('/')]).decode().strip(),count=len(R),bytes=sum(x['bytes'] for x in R),files=R,semantic_credit=0,restored_code_executed=False)
(T/'recovery-manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='files'}))
