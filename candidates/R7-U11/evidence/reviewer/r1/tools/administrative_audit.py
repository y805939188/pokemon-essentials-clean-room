"""Check author manifest declarations and retain administrative limitations."""
import hashlib,json,pathlib,datetime
out=pathlib.Path(__file__).resolve().parents[1];root=pathlib.Path('/workspace/r7-review-input/R7-U11-r1-f151a507bb43e8c936845c7408ab4bc14138caf0/candidate');author=root/'candidates/R7-U11/evidence/author'
manifest=json.loads((author/'artifact-manifest.json').read_bytes());rows=[]
for r in manifest['files']:
 b=(root/r['path']).read_bytes();new=r['new']
 if new is None:
  assert r['kind']=='manifest' and r['path'].endswith('/artifact-manifest.json');continue
 assert len(b)==new['bytes'] and hashlib.sha256(b).hexdigest()==new['sha256'] and hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()==new['git_blob_content_id'];rows.append(r['path'])
assert len(rows)==56 and len(manifest['files'])==57
logs=[]
for p in sorted((author/'logs').glob('*.json')):
 r=json.loads(p.read_bytes()); stdout=(p.parent/r['stdout']).read_bytes();stderr=(p.parent/r['stderr']).read_bytes();logs.append({'name':p.name,'start_utc':r['start_utc'],'end_utc':r['end_utc'],'child_pid':r['child_pid'],'exit_code':r['exit_code'],'stdout_bytes':len(stdout),'stderr_bytes':len(stderr)})
ctx=json.loads((author/'context.json').read_bytes());assert ctx['platform_thread_id_from_CODEX_THREAD_ID']=='01a13f80-12b3-72ef-ab3d-8ba6a20af008'
d={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'manifest_entries':57,'individual_identity_matches':56,'self_manifest_bound_by_frozen_candidate_git_tree_and_independent_byte_audit':True,'author_thread_id':ctx['platform_thread_id_from_CODEX_THREAD_ID'],'author_separate_task_context_model_PID':{'task':ctx['separate_task_id'],'context':ctx['separate_context_id'],'model_process_pid':ctx['agent_model_process_pid']},'author_effective_configuration':ctx['effective_configuration'],'author_command_logs':logs,'retained_failures':['003-input-audit exit1: named input absent before supplemental restore','006-candidate-validation exit1: overbroad invariant in author validator, corrected before007','initial xxd unavailable127 as stated in author report; no backfilled independent process log'],'initial_logging_qualification':ctx['initial_tool_log_qualification'],'qualification':'Administrative and identity verification only. Author tool results/self-assessments do not grant reviewer semantic PASS.'}
(out/'author-administrative-audit.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'manifest_entries':57,'declared_identity_matches':56,'author_log_exit_codes':[r['exit_code'] for r in logs],'author_configuration':'UNVERIFIED'}))
