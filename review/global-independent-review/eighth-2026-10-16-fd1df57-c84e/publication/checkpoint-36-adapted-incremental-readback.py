"""Transport-only exact successor verification, reusing a fully verified baseline."""
from pathlib import Path
import subprocess,sys,json,hashlib,datetime,gzip

repo=Path('/workspace/pokemon-essentials-clean-room')
prefix='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
r=repo/prefix
commit,name,baseline_receipt=sys.argv[1:]
proof_path=r/baseline_receipt
proof_raw=proof_path.read_bytes();base=json.loads(proof_raw)
assert base['status']=='VERIFIED'
seed=Path(base['isolated_git_dir']);bare=Path('/workspace/scratch')/name/'remote.git'
assert not bare.exists()
events=[]
def run(where,*args,allow_failure=False):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 p=subprocess.run(['git','-C',str(where),*args],capture_output=True)
 events.append(dict(args=list(args),git_dir=str(where),start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit=p.returncode,stdout=p.stdout.decode(errors='replace'),stderr=p.stderr.decode(errors='replace')))
 if not allow_failure:assert p.returncode==0,events[-1]
 return p
assert run(seed,'cat-file','-e',commit+'^{commit}',allow_failure=True).returncode!=0
bare.parent.mkdir(parents=True,exist_ok=True)
init_start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(['git','init','--bare',str(bare)],capture_output=True);events.append(dict(args=['init','--bare',str(bare)],git_dir=str(bare.parent),start_utc=init_start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit=p.returncode,stdout=p.stdout.decode(errors='replace'),stderr=p.stderr.decode(errors='replace')));assert p.returncode==0
(bare/'objects/info/alternates').write_text(str((seed/'objects').resolve())+'\n')
assert run(bare,'cat-file','-e',commit+'^{commit}',allow_failure=True).returncode!=0
assert run(bare,'rev-parse',base['commit']+':'+prefix).stdout.decode().strip()==base['report_tree']
run(bare,'update-ref','refs/heads/verified-baseline',base['commit'])
run(bare,'fetch','--no-tags','--no-write-fetch-head','https://github.com/y805939188/pokemon-essentials-clean-room.git',commit)
assert run(bare,'cat-file','-e',commit+'^{commit}').returncode==0
run(bare,'merge-base','--is-ancestor',base['commit'],commit)
delta=run(bare,'diff','--name-only','-z',base['commit'],commit).stdout.split(b'\0')
assert all(not p or p.decode().startswith(prefix+'/')for p in delta)
assert run(bare,'rev-parse',commit+':deliverables/final-specification-set').stdout.decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
def tree(where,c):
 raw=run(where,'ls-tree','-r','-z',c,'--',prefix).stdout
 result={}
 for row in raw.split(b'\0'):
  if not row:continue
  meta,path=row.split(b'\t',1);mode,typ,blob=meta.decode().split()
  assert mode=='100644'and typ=='blob'
  result[path.decode()]=(mode,typ,blob)
 return result
remote_tree=tree(bare,commit);local_tree=tree(repo,commit);assert remote_tree==local_tree
baseline_tree=tree(bare,base['commit']);baseline_files={x['path']:x for x in base['files']}
assert set(baseline_tree)==set(baseline_files)
for p,t in baseline_tree.items():
 row=baseline_files[p];assert t==(row['mode'],row['type'],row['blob'])
def batch(where):return subprocess.Popen(['git','-C',str(where),'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
remote_batch=batch(bare);local_batch=batch(repo)
def blob(proc,oid):
 proc.stdin.write((oid+'\n').encode());proc.stdin.flush();header=proc.stdout.readline().decode().split();assert header[0]==oid and header[1]=='blob'
 data=proc.stdout.read(int(header[2]));assert len(data)==int(header[2])and proc.stdout.read(1)==b'\n'
 return data
rows=[];changed=[];reused=0
try:
 for path,(mode,typ,oid) in sorted(remote_tree.items()):
  if baseline_tree.get(path)==(mode,typ,oid):
   old=baseline_files[path];row=dict(old,readback='REUSED_EXACT_VERIFIED_BASELINE_MODE_BLOB_SHA_BYTES');reused+=1
  else:
   rb=blob(remote_batch,oid);lb=blob(local_batch,oid);assert rb==lb
   assert hashlib.sha1(b'blob '+str(len(rb)).encode()+b'\0'+rb).hexdigest()==oid
   row=dict(path=path,mode=mode,type=typ,blob=oid,bytes=len(rb),sha256=hashlib.sha256(rb).hexdigest(),readback='FULL_NEW_REMOTE_BLOB_BYTES_VERIFIED');changed.append(path)
  rows.append(row)
 by_path={x['path']:x for x in rows};restored=[]
 manifest_path=prefix+'/publication/compressed-artifacts.json'
 if manifest_path in by_path:
  mb=blob(remote_batch,by_path[manifest_path]['blob']);manifest=json.loads(mb)
  for original in manifest['artifacts']:
   container=prefix+'/'+original['container_path'];entry=by_path[container]
   assert entry['blob']==original['container_git_blob']and entry['mode']==original['container_mode']
   packed=blob(remote_batch,entry['blob'])
   assert len(packed)==original['container_bytes']and hashlib.sha256(packed).hexdigest()==original['container_sha256']
   assert original['original_bytes']<250000000
   raw=gzip.decompress(packed)
   assert len(raw)==original['original_bytes']and hashlib.sha256(raw).hexdigest()==original['original_sha256']
   assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==original['original_git_blob']
   restored.append(dict(original_path=original['original_path'],mode=original['original_mode'],bytes=len(raw),sha256=original['original_sha256'],git_blob=original['original_git_blob'],container_path=original['container_path'],readback='REMOTE_CONTAINER_DECODED_EXACT_ORIGINAL_BYTES_VERIFIED'))
finally:
 for proc in [remote_batch,local_batch]:proc.stdin.close();assert proc.wait()==0
tree_oid=run(bare,'rev-parse',commit+':'+prefix).stdout.decode().strip()
out=dict(schema='gr8-remote-incremental-readback/v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='VERIFIED',commit=commit,report_tree=tree_oid,remote='https://github.com/y805939188/pokemon-essentials-clean-room.git',isolated_git_dir=str(bare),baseline_receipt=baseline_receipt,baseline_receipt_sha256=hashlib.sha256(proof_raw).hexdigest(),baseline_commit=base['commit'],baseline_report_tree=base['report_tree'],seed_policy='Explicit verified baseline remote object cache; target absent before actual exact-SHA fetch. Unchanged mode/type/blob/path entries reuse its previously full-byte-verified SHA/length. Every changed/new blob independently read from fresh fetched target and compared with local committed blob bytes; no live worktree comparison.',count=len(rows),bytes=sum(x['bytes']for x in rows),full_new_remote_blob_count=len(changed),reused_verified_blob_count=reused,deleted_paths=sorted(set(baseline_tree)-set(remote_tree)),files=rows,compressed_originals=restored,compressed_original_count=len(restored),compressed_original_bytes=sum(x['bytes']for x in restored),events=events,semantic_credit='NONE: transport only; no reading/semantic/task-final approval',UPDATE_NOT_STARTED=True,verifier_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
out.update(original_trusted_verifier_source_sha256='c7993a3be2b3d0a4dfefd464e086a274c8bccc27f13dffa96a1647627c4d46ba',baseline_flattening_receipt='publication/checkpoint-34-flat-seed-provenance.json',baseline_flattening_receipt_sha256='51449150b024fac59fd168ae28b7443d868b0c16598d070eaace808c6e5d41d5',c36_seed_policy='C35 verified remote cache backed by C34 then flat C33 remote caches; no legacy deep alternate chain and no current worktree object source.',verifier_adaptation='Only init/tree command logging and provenance; original exact commit/tree/delta/changed-blob/116gzip assertions retained.');destination=r/'publication'/f'{name}.json';destination.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:out[k]for k in ['status','commit','report_tree','count','bytes','full_new_remote_blob_count','reused_verified_blob_count','compressed_original_count','compressed_original_bytes']},ensure_ascii=False))
