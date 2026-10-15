"""Independent transport, preservation and link checks; no behavioral execution."""
import datetime,difflib,hashlib,json,os,pathlib,re,subprocess
R=pathlib.Path('/workspace/r7-ir-R7-U01');P='/workspace/pokemon-essentials-clean-room'
B='e646432c644dec04d306842cc5a559a29c718fbc';MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
def git(*a):return subprocess.check_output(['git',*a],cwd=P)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
j=json.loads((R/'actual-input/integration/applied-clauses.json').read_bytes())
plan=json.loads((R/'actual-plans/R7-U01.json').read_bytes())
context=os.environ.get('CODEX_THREAD_ID');session=os.environ.get('CODEX_SESSION_ID')
excluded=re.findall(r'01a[0-9a-f-]{33}',(R/'bootstrap/R7-U01-R7IR.md').read_text())
assert context and context==session and context not in excluded
identity={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'CODEX_THREAD_ID':context,'CODEX_SESSION_ID':session,'opaque_context_id':'NOT_EXPOSED','opaque_task_id':'NOT_EXPOSED','tool_pid':os.getpid(),'excluded_visible_identifiers':sorted(set(excluded)),'distinct_from_all_exclusions':True,'child_tasks_created':0,'effective_configuration':{x:'UNVERIFIED' for x in ['model','effort','service_tier','speed']},'qualification':'Visible runtime identifier comparison only; no creation API return/effective configuration or opaque-ID equivalence inferred.'}
dump(R/'tool-evidence/identity-observation.json',identity)
raws={p.stem:p for p in (R/'original').rglob('*.raw')}
c=json.loads((R/'original/dispatch/delegation/contracts/R7-U01.json').read_bytes());refs={}
def walk(x):
 if isinstance(x,dict):
  if 'raw_member_byte_offsets' in x and x.get('input_sha256') in raws:refs[(x['input_sha256'],x['json_pointer'])]=x
  for v in x.values():walk(v)
 elif isinstance(x,list):
  for v in x:walk(v)
walk(c);bindings=[]
for (sha,pointer),row in sorted(refs.items()):
 b=raws[sha].read_bytes();assert hashlib.sha256(b).hexdigest()==sha
 a,z=row['raw_member_byte_offsets'];span=b[a:z]
 assert len(span)==row['raw_member_bytes'] and hashlib.sha256(span).hexdigest()==row['raw_member_sha256']
 x=json.loads(b)
 for token in pointer.split('/')[1:] if pointer else []:x=x[int(token)] if isinstance(x,list) else x[token.replace('~1','/').replace('~0','~')]
 assert x==json.loads(span)
 canonical=json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
 assert hashlib.sha256(canonical).hexdigest()==row['canonical_sha256']
 bindings.append({'input_sha256':sha,'pointer':pointer,'raw_span':[a,z],**ident(span),'canonical_sha256':row['canonical_sha256'],'matched':True})
old=R/'actual-input/prior-candidate/candidates/R7-U01';new=R/'actual-input/candidate/candidates/R7-U01'
mirrors=[p.relative_to(new) for p in new.rglob('*.md') if str(p.relative_to(new)).startswith(('deliverables/','audit/','planning/'))]
delta=[]
for rel in mirrors:
 a=(old/rel).read_bytes();b=(new/rel).read_bytes()
 ops=[{'operation':tag,'old_zero_based':[i,k],'new_zero_based':[v,w]} for tag,i,k,v,w in difflib.SequenceMatcher(None,a.splitlines(keepends=True),b.splitlines(keepends=True),autojunk=False).get_opcodes() if tag!='equal']
 if rel.name=='wp03-content-identity-and-schema.md':assert ops==[{'operation':'replace','old_zero_based':[57,58],'new_zero_based':[57,58]}]
 elif rel.name=='generic-kernel-wp02-03-04.md':
  assert a==b''.join(b.splitlines(keepends=True)[:223])
  assert ops==[{'operation':'insert','old_zero_based':[223,223],'new_zero_based':[223,236]}]
 else:assert a==b
 delta.append({'path':str(rel),'old':ident(a),'new':ident(b),'operations':ops})
old_per=json.loads((old/'evidence/author/per-id.json').read_bytes());new_per=json.loads((new/'evidence/author/per-id.json').read_bytes())
assert all(x['vectors']==y['vectors'] for x,y in zip(old_per['records'],new_per['records']))
shared=[]
for row in plan['shared_preservation_checks']:
 f=next(x for x in j['files'] if x['path']==row['path']);hs=[h for h in f['hunks'] if h['batch_id']==row['other_batch']];assert hs
 for h in hs:
  a,z=h['actual_final_line_indices_half_open'];current=git('show',MI+':'+f['path']).decode().splitlines(keepends=True)
  assert ''.join(current[a:z])==h['added_text']
 root=R/'actual-input/shared-candidate-review'/row['other_batch'];report=(root/'report.md').read_bytes()
 for name in ['report.md','per-id.json','review-input-receipt.json']:
  b=(root/name).read_bytes();actual=git('show',row['candidate_review_commit']+':'+f"candidates/{row['other_batch']}/evidence/reviewer/r1/{name}");assert b==actual
 assert row['candidate_commit'] in report.decode() and 'PASS_SCOPED_CANDIDATE' in report.decode()
 shared.append({**row,'approved_hunk_count':len(hs),'actual_spans':[h['actual_final_line_indices_half_open'] for h in hs],'approved_bytes_preserved':True,'review_report':ident(report),'qualification':'Other-ID approval provenance/preservation only, no new semantic PASS.'})
err=next(x for x in j['files'] if x['path'].endswith('current-navigation-errata.json'))
before=json.loads(err['hunks'][0]['added_text']);after=json.loads(git('show',MI+':'+err['path']));err_delta={k:{'before':before[k],'after':after[k]} for k in before if before[k]!=after[k]}
assert set(err_delta)=={'status','reception'}
assert after['status']=='INTEGRATED_PENDING_INDEPENDENT_ACTUAL_REVIEW'
assert after['reception']['ACCEPTED'] is False and after['reception']['CLOSED'] is False
assert after['reception']['actual_integration_review']==before['reception']['actual_integration_review']
pub=json.loads((R/'actual-input/integration/public-reception.json').read_bytes());links=[]
for s in pub['source_bindings']:
 b=git('show',s['candidate_freeze_commit']+':'+s['candidate_input_path']);x=json.loads(b)
 assert s['candidate_commit'] in json.dumps(x)
 links.append({'batch':s['id'],'freeze':s['candidate_freeze_commit'],'path':s['candidate_input_path'],**ident(b),'candidate_reference_matched':True})
assert git('show',MI+':review/remediation-seventh-20261015-prepare/integration/wave2/v1/public-reception.json')==(R/'actual-input/integration/public-reception.json').read_bytes()
ui=next(x for x in j['files'] if 'test-catalog/user-interface-' in x['path'])
ub=git('show',MI+':'+ui['path']);up=R/'supplemental-input'/ui['path'];up.parent.mkdir(parents=True,exist_ok=True);up.write_bytes(ub)
ui_ranges=[{'batch':h['batch_id'],'base':h['base_line_indices_half_open'],'actual':h['actual_final_line_indices_half_open'],'added':h['added_identity']} for h in ui['hunks']]
for name in ['original','actual-input']:
 for p in (R/name).rglob('*'):
  if p.is_file():p.chmod(0o444)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'original_raw_bindings':bindings,'r1_to_r2_mirrors':delta,'original_16_vectors_preserved':True,'shared_nine':shared,'errata_only_changed_field':err_delta,'public_reception_fixed_input_links':links,'UI_full_file':{'path':ui['path'],**ident(ub),'hunks':ui_ranges},'restored_files_now_read_only':True,'qualification':'TOOL_VALIDATION only. Content reasoning separately recorded by reviewer.'}
dump(R/'tool-evidence/supplemental-audit.json',out)
print(json.dumps({'raw_bindings':len(bindings),'r1_to_r2':delta,'shared_checks':len(shared),'errata_delta':err_delta,'UI_hunks':ui_ranges,'fixed_links':len(links)},ensure_ascii=False,indent=2))
