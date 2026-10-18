"""Flatten only independently verified remote-cache objects; preserve failed transport evidence."""
from pathlib import Path
import datetime,hashlib,json,os,shutil,stat,subprocess
REPO=Path('/workspace/pokemon-essentials-clean-room');RR=REPO/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e';PUB=RR/'publication';IO=PUB/'checkpoint-34-io'
COMMIT='81cc98eec7cc81706e51c8b274e9ff7042c0868b';NAME='r8-four-receivers-and-metadata-readback-34';BASE='publication/r8-qualified-primary21-and-recoveries-readback-33.json'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def file_sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1048576):h.update(b)
 return h.hexdigest()
def put(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
events=[]
def run(args,label,allow_failure=False):
 a=utc();p=subprocess.run(args,capture_output=True);b=utc();(IO/(label+'.stdout')).write_bytes(p.stdout);(IO/(label+'.stderr')).write_bytes(p.stderr)
 e={'args':args,'start_utc':a,'end_utc':b,'exit':p.returncode,'stdout':'publication/checkpoint-34-io/'+label+'.stdout','stderr':'publication/checkpoint-34-io/'+label+'.stderr','stdout_bytes':len(p.stdout),'stdout_sha256':sha(p.stdout),'stderr_bytes':len(p.stderr),'stderr_sha256':sha(p.stderr)};put(IO/(label+'.operation.json'),e);events.append(e)
 if not allow_failure:assert p.returncode==0,e
 return p
base_raw=(RR/BASE).read_bytes();base=json.loads(base_raw);assert base['status']=='VERIFIED' and base['commit']=='c7fec918d511a0ead8ab325c934e9346d7c43cac'
seed=Path(base['isolated_git_dir']).resolve();flat=Path('/workspace/scratch/checkpoint-34-flat-verified-c33/remote.git');assert not flat.exists()
old27=PUB/'r8-finite-adjudications-and-minimal-closure-readback-27.json';old27raw=old27.read_bytes();scope27=json.loads(old27raw)['cache_scope'];assert scope27['allowed_commit_closure']=='fd1df570cad987dc3852a3b958f03916e317f7fe' and scope27['actual_pack_object_ids_equal_exact_B8_closure'] is True
fixed_input=Path('/workspace/scratch/r8-finite-adjudications-and-minimal-closure-readback-27/input-object-cache')
fixed_b8_objects=Path(scope27['cache'])/'objects'
b8files={x['name']:x for x in scope27['pack_files']}
sources=[];todo=[seed/'objects'];seen=set()
while todo:
 obj=todo.pop().resolve()
 if obj in seen:continue
 seen.add(obj);assert str(obj).startswith('/workspace/scratch/') and (obj.name=='objects' or obj==fixed_input) and obj.is_dir(),obj
 assert obj!=REPO/'.git/objects' and REPO/'.git' not in obj.parents
 alt=obj/'info/alternates';nexts=[]
 if alt.exists():
  for s in alt.read_text().splitlines():
   if s.strip():
    q=Path(s.strip());q=q if q.is_absolute() else obj/q;nexts.append(str(q.resolve()));todo.append(q)
 if obj==fixed_input:
  assert (obj/'pack').resolve()==(fixed_b8_objects/'pack').resolve()
  nexts.append(str(fixed_b8_objects.resolve()));todo.append(fixed_b8_objects)
 sources.append({'object_directory':str(obj),'alternates':nexts,'alternates_sha256':sha(alt.read_bytes()) if alt.exists() else None})
flat.parent.mkdir(parents=True,exist_ok=True);run(['git','init','--bare',str(flat)],'flat-seed-init')
copies=[];duplicates=0
for s in sources:
 src=Path(s['object_directory'])
 for p in sorted(src.rglob('*')):
  if not p.is_file():continue
  rel=p.relative_to(src)
  valid=(len(rel.parts)==2 and len(rel.parts[0])==2 and all(c in '0123456789abcdef' for c in rel.parts[0]) and len(rel.parts[1])==38 and all(c in '0123456789abcdef' for c in rel.parts[1])) or (len(rel.parts)==2 and rel.parts[0]=='pack' and (rel.parts[1].startswith('pack-') or (src in [fixed_input,fixed_b8_objects] and p.name in b8files)) and p.suffix in ['.pack','.idx','.rev','.bitmap','.promisor'])
  if not valid:continue
  if src in [fixed_input,fixed_b8_objects]:
   e=b8files[p.name];assert p.stat().st_size==e['bytes'] and file_sha(p)==e['sha256']
  assert stat.S_ISREG(p.lstat().st_mode) and not p.is_symlink()
  dst=flat/'objects'/rel;dst.parent.mkdir(parents=True,exist_ok=True)
  if dst.exists():
   assert p.stat().st_size==dst.stat().st_size
   if p.stat().st_ino!=dst.stat().st_ino:assert file_sha(p)==file_sha(dst)
   duplicates+=1;continue
  try:os.link(p,dst);method='SAME_DEVICE_HARDLINK_IMMUTABLE_REMOTE_OBJECT';assert p.stat().st_dev==dst.stat().st_dev and p.stat().st_ino==dst.stat().st_ino
  except OSError:shutil.copyfile(p,dst);method='EXACT_BYTE_COPY';assert file_sha(p)==file_sha(dst)
  copies.append({'source':str(p),'destination':str(dst),'bytes':p.stat().st_size,'method':method})
assert not (flat/'objects/info/alternates').exists()
run(['git','-C',str(flat),'cat-file','-e',base['commit']+'^{commit}'],'flat-seed-baseline-present')
assert run(['git','-C',str(flat),'rev-parse',base['commit']+':review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'],'flat-seed-baseline-tree').stdout.decode().strip()==base['report_tree']
absent=run(['git','-C',str(flat),'cat-file','-e',COMMIT+'^{commit}'],'flat-seed-target-absent',True);assert absent.returncode!=0
run(['git','-C',str(flat),'fsck','--connectivity-only','--no-reflogs',base['commit']],'flat-seed-baseline-connectivity')
failed=Path('/workspace/scratch')/NAME/'remote.git';saved=failed.parent/'attempt-01-alternates-too-deep-remote.git';assert failed.is_dir() and not saved.exists();failed.rename(saved)
receipt={'schema':'gr8-checkpoint34-verified-remote-baseline-flattening/v1','utc':utc(),'status':'FLAT_REMOTE_BASELINE_PLUS_EXACT_FIXED_B8_INPUT_READY_TARGET_ABSENT','original_baseline_receipt':BASE,'original_baseline_receipt_sha256':sha(base_raw),'baseline_commit':base['commit'],'baseline_report_tree':base['report_tree'],'original_isolated_seed':str(seed),'flat_seed':str(flat),'source_object_stores':sources,'copied_object_files':copies,'duplicate_same_object_files':duplicates,'object_bytes':sum(x['bytes'] for x in copies),'qualified_fixed_B8_input_pack_provenance':{'receipt':'publication/'+old27.name,'bytes':len(old27raw),'sha256':sha(old27raw),'cache_scope':scope27,'qualification':'Original ancestor-only B8 pack originally derived from fixed old input, not current report target; all3originalpack bytes/SHA independently rechecked. Other seed objects from verified remote report caches.'},'failed_attempt_original_location':str(failed),'failed_attempt_preserved_location':str(saved),'no_current_working_root_git_objects_read_or_used_as_target_source':True,'target_C34_absent_before_fresh_fetch':True,'flat_seed_has_no_alternates':True,'events':events,'semantic_credit':'NONE transport-only; original baseline file, original seed and failed evidence not modified/deleted'}
proof=PUB/'checkpoint-34-flat-seed-provenance.json';put(proof,receipt)

# Exact trusted verifier clone: only seed resolution, explicit transport logging and provenance change.
trusted=PUB/'incremental-remote-readback.py';source=trusted.read_text();trusted_sha=sha(trusted.read_bytes())
old="seed=Path(base['isolated_git_dir']);bare=Path('/workspace/scratch')/name/'remote.git'"
new="original_seed=Path(base['isolated_git_dir']);seed=Path('/workspace/scratch/checkpoint-34-flat-verified-c33/remote.git');bare=Path('/workspace/scratch')/name/'remote.git'"
assert source.count(old)==1;source=source.replace(old,new)
old="p=subprocess.run(['git','init','--bare',str(bare)],capture_output=True);assert p.returncode==0"
new="init_start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(['git','init','--bare',str(bare)],capture_output=True);events.append(dict(args=['init','--bare',str(bare)],git_dir=str(bare.parent),start_utc=init_start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),exit=p.returncode,stdout=p.stdout.decode(errors='replace'),stderr=p.stderr.decode(errors='replace')));assert p.returncode==0"
assert source.count(old)==1;source=source.replace(old,new)
old="raw=subprocess.check_output(['git','-C',str(where),'ls-tree','-r','-z',c,'--',prefix])"
new="raw=run(where,'ls-tree','-r','-z',c,'--',prefix).stdout"
assert source.count(old)==1;source=source.replace(old,new)
old="destination=r/'publication'/f'{name}.json';destination.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\\n')"
new="out.update(baseline_flattening_receipt='publication/checkpoint-34-flat-seed-provenance.json',baseline_flattening_receipt_sha256=hashlib.sha256((r/'publication/checkpoint-34-flat-seed-provenance.json').read_bytes()).hexdigest(),original_baseline_isolated_git_dir=str(original_seed),actual_flat_remote_only_seed=str(seed),original_trusted_verifier_source_sha256='"+trusted_sha+"',verifier_adaptation='Only remote-only seed flattening, init/tree command logging and explicit provenance; all exact commit/tree/delta/blob/116gzip checks retained. No worktree root.git target as independent source.');destination=r/'publication'/f'{name}.json';destination.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\\n')"
assert source.count(old)==1;source=source.replace(old,new)
clone=PUB/'checkpoint-34-adapted-incremental-readback.py';clone.write_text(source)
adapt={'schema':'gr8-checkpoint34-trusted-verifier-transport-adaptation/v1','utc':utc(),'original_source':str(trusted.relative_to(RR)),'original_source_bytes':trusted.stat().st_size,'original_source_sha256':trusted_sha,'adapted_source':str(clone.relative_to(RR)),'adapted_source_bytes':clone.stat().st_size,'adapted_source_sha256':sha(clone.read_bytes()),'changes':['Use flat copy of exactly original baseline remote-cache transitive object stores; original baseline receipt bytes/sha preserved.','Capture bare init and full ls-tree command I/O/UTC/exit.','Record flattening and original/adapted verifier provenance.'],'all_original_blob_tree_delta_gzip_assertions_retained':True,'semantic_or_business_credit':'NONE'}
put(PUB/'checkpoint-34-verifier-adaptation.json',adapt)
assert not failed.exists()
q=run(['python',str(clone),COMMIT,NAME,BASE],'publish-fresh-remote-readback-retry')
remote=PUB/(NAME+'.json');rb=json.loads(remote.read_bytes());assert rb['status']=='VERIFIED' and rb['commit']==COMMIT and rb['compressed_original_count']==116
push=json.loads((PUB/'checkpoint-34-push-receipt.json').read_bytes());assert rb['report_tree']==push['report_tree']
done={'schema':'gr8-checkpoint34-complete-publication-status/v1','utc':utc(),'status':'COMMIT_PUSH_AND_FRESH_REMOTE_READBACK_VERIFIED','commit':COMMIT,'workspace_tree':push['workspace_tree'],'report_tree':rb['report_tree'],'remote_ref':push['remote_ref'],'push_receipt':'publication/checkpoint-34-push-receipt.json','readback_receipt':{'path':'publication/'+remote.name,'bytes':remote.stat().st_size,'sha256':sha(remote.read_bytes())},'flat_seed_provenance':'publication/checkpoint-34-flat-seed-provenance.json','verifier_adaptation':'publication/checkpoint-34-verifier-adaptation.json','first_failed_attempt_preserved':str(saved),'remote_files':rb['count'],'remote_bytes':rb['bytes'],'full_new_remote_blob_count':rb['full_new_remote_blob_count'],'reused_verified_blob_count':rb['reused_verified_blob_count'],'compressed_original_count':rb['compressed_original_count'],'compressed_original_bytes':rb['compressed_original_bytes'],'frozen_registry_count':27,'new_contexts':0,'new_votes':0,'new_semantic_credit':0,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'whole_review_complete':False,'whole_required':None,'whole_history_canonical':'UNFROZEN','proof_files_created_after_commit':'Own C34 receipt/IO/readback are local successors, not claimed inside same commit.'}
put(PUB/'checkpoint-34-completed.json',done);print(json.dumps(done,ensure_ascii=False))
