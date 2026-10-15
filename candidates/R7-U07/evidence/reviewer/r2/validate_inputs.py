"""Independent fixed-byte, scope, binding and preservation checks only."""
import datetime,difflib,hashlib,json,subprocess
from pathlib import Path
ROOT=Path('/workspace/r7-u07-reviewer-r2'); E=Path(__file__).resolve().parent
R=Path('/workspace/r7-context/R7-U07-reviewer');F=Path('/workspace/r7-review-bootstrap/R7-U07-r2')
C=Path('/workspace/r7-review-input/R7-U07-r2-2649ed2bd2cc3afdfa636cd643fc1975de5eae32/candidate')
B='e646432c644dec04d306842cc5a559a29c718fbc';A='2649ed2bd2cc3afdfa636cd643fc1975de5eae32'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def ident(d):return {'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()}
def check(d,row):
 a=ident(d)
 for k,v in a.items():
  ek='git_blob_content_id' if k=='git_blob' and 'git_blob_content_id' in row else k
  if ek in row:assert v==row[ek],(ek,v,row[ek])
 return a
freeze=json.loads((F/'candidate-input.json').read_bytes())
assert git('rev-parse',A+'^{tree}').decode().strip()==freeze['candidate_tree']
assert git('rev-parse','aa369555b0e8b6c8b077f964b54ed63d3b924f26^{tree}').decode().strip()=='08bd0f362c74ef7645b5bbd70b557489c122ae29'
assert git('rev-parse',B+':deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
checks=[]
for name,commit,path,local in [('tool','658488c81f1f3181a488298ab27850c8af951d73','tools/restore_container_context.py',Path('/workspace/r7-bootstrap/R7-U07-reviewer/tools/restore_container_context.py')),('original-plan','658488c81f1f3181a488298ab27850c8af951d73','recovery/batches/R7-U07.json',Path('/workspace/r7-bootstrap/R7-U07-reviewer/recovery/batches/R7-U07.json')),('dispatch','c64774c60d91e522cb515ef71e3e9d4ea6b4712c','review-rechecks/R7-U07/r2/reviewer-dispatch.md',F/'reviewer-dispatch.md')]:
 d=local.read_bytes();assert d==git('show',commit+':review/remediation-seventh-20261015-prepare/'+path);checks.append({'name':name,'commit':commit,'path':path,**ident(d)})
for name in ['candidate-input.json','candidate-restore/R7-U07.json','mirror-diffs.patch','remote-readback.json']:
 d=(F/name).read_bytes();assert d==git('show','aa369555b0e8b6c8b077f964b54ed63d3b924f26:review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U07/'+name);checks.append({'name':name,**ident(d)})
original_plan=json.loads(Path('/workspace/r7-bootstrap/R7-U07-reviewer/recovery/batches/R7-U07.json').read_bytes()); original=[]
for key in ['artifacts','evidence','fixed_read_inputs']:
 for row in original_plan[key]:original.append({'local_path':row['local_path'],**check((R/row['local_path']).read_bytes(),row)})
files=freeze['candidate_and_author_evidence_file_identities']; candidate=[]
actual_tree={}
for record in git('ls-tree','-r','-z',A,'candidates/R7-U07').split(b'\0'):
 if not record:continue
 meta,path=record.split(b'\t');mode,kind,blob=meta.decode().split();actual_tree[path.decode()]=(mode,kind,blob)
assert set(actual_tree)=={x['path'] for x in files}
for row in files:
 path=row['path'];d=(C/path).read_bytes();mode,kind,blob=actual_tree[path]
 assert mode==row['git_mode']=='100644' and kind=='blob' and blob==row['git_blob']
 assert d==git('show',A+':'+path);candidate.append({'path':path,'mode':mode,**check(d,row)})
diff=[tuple(x.split('\t',1)) for x in git('diff','--name-status',B,A).decode().splitlines()]
assert diff==[(x['status'],x['path']) for x in freeze['complete_diff_against_B']]
assert all(s=='A' and p.startswith('candidates/R7-U07/') for s,p in diff)
changes=[]
for row in files:
 if row['role']!='candidate_mirror':continue
 target=row['formal_target'];before=git('show',B+':'+target);after=(C/row['path']).read_bytes()
 assert before==(R/'inputs/project'/target).read_bytes()
 check(before,row['base_B_identity_or_explicit_new_file'])
 a=before.decode().splitlines(True);b=after.decode().splitlines(True)
 ops=[list(x) for x in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes() if x[0]!='equal']
 changes.append({'target':target,'before':ident(before),'after':ident(after),'opcodes':ops})
 patch=''.join(difflib.unified_diff(a,b,fromfile='a/'+target,tofile='b/'+target))
 (E/('wp55-diff.patch' if 'combat-requirements/wp55-' in target else 'catalog-diff.patch')).write_text(patch)
 if 'combat-requirements/wp55-' in target:assert [(x[0],x[1],x[2]) for x in ops]==[('replace',92,93),('replace',123,124)]
 else:
  assert ops==[['insert',103,103,103,116]]
  assert a==b[:103]+b[116:]
# Validate all references whose original payload is actually in this bounded plan.
raw={p.stem:p.read_bytes() for p in (R/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs').glob('*.raw')}
normalized=json.loads((R/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_bytes())['records'][14]
refs={};metadata_refs={}
def walk(v):
 if isinstance(v,dict):
  if 'raw_member_byte_offsets' in v and 'input_sha256' in v:
   key=(v['input_sha256'],tuple(v['raw_member_byte_offsets']),v.get('json_pointer',''))
   (refs if v['input_sha256'] in raw else metadata_refs)[key]=v
  for x in v.values():walk(x)
 elif isinstance(v,list):
  for x in v:walk(x)
walk(normalized); walk(json.loads((R/'dispatch/delegation/contracts/R7-U07.json').read_bytes()))
ref_results=[]
for key,v in refs.items():
 data=raw[v['input_sha256']];lo,hi=v['raw_member_byte_offsets'];part=data[lo:hi]
 assert len(part)==v['raw_member_bytes'] and hashlib.sha256(part).hexdigest()==v['raw_member_sha256']
 obj=json.loads(data)
 for seg in v['json_pointer'].split('/')[1:]:
  seg=seg.replace('~1','/').replace('~0','~');obj=obj[int(seg)] if isinstance(obj,list) else obj[seg]
 assert json.loads(part)==obj
 canonical=json.dumps(obj,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
 assert hashlib.sha256(canonical).hexdigest()==v['canonical_sha256'],v['json_pointer']
 ref_results.append({'binding_id':v.get('binding_id'),'pointer':v['json_pointer'],'input_sha256':v['input_sha256'],'byte_range':[lo,hi],'raw_sha256':v['raw_member_sha256'],'canonical_sha256':v['canonical_sha256']})
# Author manifest identity declarations, never author semantic validation.
manifest=json.loads((C/'candidates/R7-U07/evidence/author/artifact-manifest.json').read_bytes())
manifest_checks=[]
for row in manifest['files']:
 p=C/row['path']; assert p.is_file()
 manifest_checks.append({'path':row['path'],**check(p.read_bytes(),row['after'])})
 if row.get('before'):
  check(git('show',B+':'+row['baseline_path']),row['before'])
assert len(manifest_checks)==31
assert {x['path'] for x in manifest_checks}==set(actual_tree)-{'candidates/R7-U07/evidence/author/artifact-manifest.json'}
log_summaries=[]
for p in sorted((C/'candidates/R7-U07/evidence/author/logs').glob('*.json')):
 v=json.loads(p.read_bytes());log_summaries.append({'path':str(p.relative_to(C)),'exit_code':v.get('exit_code'),'argv':v.get('argv'),'start_utc':v.get('start_utc'),'end_utc':v.get('end_utc'),'identity':ident(p.read_bytes()),'has_stdin':'stdin' in v,'stdout_bytes':len(v.get('stdout','').encode()),'stderr':v.get('stderr','')})
result={'schema':'r7.u07.r2.input-tool-validation.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'qualification':'TOOL_VALIDATION_ONLY_NO_BEHAVIOR_EXECUTION','fixed_byte_inputs':checks,'original_files':original,'candidate_files':candidate,'candidate_files_count':len(candidate),'candidate_bytes':sum(x['bytes'] for x in candidate),'complete_diff':diff,'changes':changes,'bound_raw_refs_verified':ref_results,'upstream_metadata_refs_not_reread':[{ 'input_sha256':k[0],'pointer':k[2],'qualification':'Not required semantic source; metadata only. No new semantic credit or blanket material limit.'} for k in metadata_refs],'author_manifest_checked_declarations':manifest_checks,'author_command_log_summaries':log_summaries,'reference_host_model_Demo_native_media_real_save_replay_execution':0}
(E/'input-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'result':'BYTE_SCOPE_AND_RAW_BINDING_CHECKS_MATCH','original_files':len(original),'original_bytes':sum(x['bytes'] for x in original),'candidate_files':len(candidate),'candidate_bytes':sum(x['bytes'] for x in candidate),'raw_references_verified':len(ref_results),'author_manifest_identity_declarations_checked':len(manifest_checks),'author_log_failures':[(x['path'],x['exit_code']) for x in log_summaries if x['exit_code'] not in [0,None]],'changes':changes},ensure_ascii=False,indent=2))
