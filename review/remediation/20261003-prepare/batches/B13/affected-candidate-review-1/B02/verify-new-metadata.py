import subprocess, json, hashlib, pathlib, re, collections
ROOT=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel']).decode().strip())
BASE='8e67f780c204d593d89f364f585d2c6c2fe74631'
CAND='5845e8084ced280e51c51a4081ec8583a9c2ca39'
PUB='1dc5cc80854e02965b9bb7a02c00a7c40d392f89'
PERMIT='2b23c82947bcecec4ab059d63048f9b67586575b'
R='review/remediation/20261003-prepare/batches/B13/'
cache={}
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def read(ref,path):
 key=(ref,path)
 if key not in cache:cache[key]=git('show',ref+':'+path)
 return cache[key]
def js(ref,path):return json.loads(read(ref,path))
def ident(ref,path):
 b=read(ref,path);return {'commit':ref,'path':path,'git_blob':git('rev-parse',ref+':'+path).decode().strip(),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def binding(x):
 a=ident(x['commit'],x['path']);ok=all(a[k]==x[k] for k in ['git_blob','sha256','bytes']);assert ok,(x,a);return a
out={'role':'INDEPENDENT_AFFECTED_CANDIDATE_METADATA_ONLY','FIX_BASE':BASE,'reviewed_candidate':CAND,'publication':PUB,'scope_permission':PERMIT,'identity_checks':{},'no_reference_or_behavior_or_historical_program_execution':True}
for ref,tree in [(BASE,'ae2f491294eb4f97be6b75f75706c16279f9bf46'),(CAND,'23f92a9c446f5f0fbcee44df2f57d85df4dd0e3c'),(PUB,'0c3c5b8235dad94152d08bc0490e6778dd7adfe9')]:
 actual=git('rev-parse',ref+'^{tree}').decode().strip();assert actual==tree;out['identity_checks'][ref]=actual
out['author_remote_ref']=git('ls-remote','--exit-code','origin','refs/heads/codex/cloud-dot-B13-author-1-20261010').decode().strip();assert out['author_remote_ref'].split()[0]==PUB
full=git('diff','--binary','--no-ext-diff','--no-textconv',BASE,CAND)
pathlib.Path('/tmp/B13-affected-exact-base-to-candidate.full.patch').write_bytes(full)
receipt=js(PUB,R+'candidate-1/scope-applied-1/publication-receipt.json')
fi={'command':['git','diff','--binary','--no-ext-diff','--no-textconv',BASE,CAND],'bytes':len(full),'sha256':hashlib.sha256(full).hexdigest(),'git_blob':hashlib.sha1(('blob '+str(len(full))+'\0').encode()+full).hexdigest(),'paths_filtered':False}
for k in ['bytes','sha256','git_blob']:assert fi[k]==receipt['whole_unfiltered_base_to_candidate'][k],(k,fi[k],receipt['whole_unfiltered_base_to_candidate'][k])
out['complete_unfiltered_diff']=fi
changes=[line.split('\t',1) for line in git('diff','--no-renames','--name-status',BASE,CAND).decode().splitlines()]
formal=js(CAND,R+'author-draft-1/scope-applied-1/all-11-output-identities.json')['records']
allowed={r['path'] for r in formal};assert len(allowed)==11
sections=re.split(br'(?m)^diff --git ',full)[1:];out['all_changed_paths']=[]
assert len(sections)==len(changes)==69
for (status,p),section in zip(changes,sections):
 assert p.encode() in section.splitlines()[0]
 kind='FORMAL_OUTPUT' if p in allowed else 'B13_ADDED_REPORT_OR_CANDIDATE_MATERIAL'
 assert p in allowed or (status=='A' and (p.startswith(R+'author-draft-1/') or p.startswith(R+'candidate-1/'))),(status,p)
 b=read(CAND,p)
 if p.endswith('.json'):json.loads(b)
 out['all_changed_paths'].append(dict(status=status,path=p,classification=kind,identity=ident(CAND,p),diff_section_sha256=hashlib.sha256(b'diff --git '+section).hexdigest()))
assert {p for s,p in changes if s=='M'}==allowed
out['all11_outputs']=[]
for r in formal:
 p=r['path'];a=ident(BASE,p);z=ident(CAND,p)
 assert all(a[k]==r['formal_input'][k] for k in ['git_blob','sha256','bytes'])
 assert all(z[k]==r['output'][k] for k in ['git_blob','sha256','bytes'])
 assert read(PUB,p)==read(CAND,p)
 if r['kind']=='APPROVED_FINAL':assert read('d4bfb88e461383d689f0e2db5d08c5f143b1e5f5',p)==read(CAND,p)
 out['all11_outputs'].append({'kind':r['kind'],'before':a,'candidate':z,'publication_equal':True})
grant_path=R+'scope-amendment-1/scope-amendment.json'
grant=js(PERMIT,grant_path)
assert read(PERMIT,grant_path)==read(CAND,R+'author-draft-1/scope-applied-1/scope-amendment.json')
out['permission_identity']=ident(PERMIT,grant_path)
out['exact_four_original_scope']=[]
for r in grant['records']:
 binding(r['before']);binding(r['after_to_apply'])
 assert read(BASE,r['path'])==read(r['before']['commit'],r['before']['path'])
 assert read(CAND,r['path'])==read(r['after_to_apply']['commit'],r['after_to_apply']['path'])
 out['exact_four_original_scope'].append({'path':r['path'],'before':r['before'],'after':r['after_to_apply'],'allowed_clauses':r['allowed_clauses'],'matches':True})
binding(grant['source_whole_patch'])
original_diff=git('diff','--binary','--no-ext-diff','--no-textconv',BASE,CAND,'--',*grant['allowed_original_write_paths'])
approved_patch=read(grant['source_whole_patch']['commit'],grant['source_whole_patch']['path'])
def normalized_patch(b):
 lines=[]
 for line in b.splitlines():
  if line.startswith((b'diff --git ',b'index ')):continue
  if line.startswith(b'@@'):line=re.sub(br'^(@@.*?@@).*$',br'\1',line)
  lines.append(line)
 return b'\n'.join(lines)
assert normalized_patch(original_diff)==normalized_patch(approved_patch)
out['original_patch_sha256']=hashlib.sha256(approved_patch).hexdigest()
out['original_git_diff_sha256']=hashlib.sha256(original_diff).hexdigest()
out['original_patch_format']='Approved difflib unified patch: Git diff/index headers and hunk function-context suffix differ; all hunks/context/before/after bytes independently equal.'
ctrl_path=R+'author-draft-1/original-and-acceptance-controls.json';ctrl=js(CAND,ctrl_path)
assert read(CAND,ctrl_path)==read('e8caada4ab919e48e3dc817f0638ce595fde449c',R+'refreeze-after-B12-C-1/original-and-acceptance-controls.json')
out['all8_control_bindings']=[]
for c in ctrl['controls']:
 row={'id':c['id'],'primary':c['primary'],'canonical_state':c['canonical_state']}
 for name,kind in [('whole_original_object','whole_original_object_binding'),('whole_approved_acceptance_object','whole_approved_acceptance_binding')]:
  x=c[kind];binding(x);obj=js(x['commit'],x['path'])
  for part in x['pointer'].strip('/').split('/'):
   part=part.replace('~1','/').replace('~0','~');obj=obj[int(part)] if isinstance(obj,list) else obj[part]
  assert obj==c[name],(c['id'],name)
  row[kind]={**x,'whole_object_equal':True}
 assert c['complete_current_control_fields']=={k:c['whole_approved_acceptance_object'][k] for k in c['complete_current_control_fields']}
 row['complete_effective_control_fields_equal']=True;out['all8_control_bindings'].append(row)
assert len(out['all8_control_bindings'])==8 and sum(x['primary'] for x in out['all8_control_bindings'])==5
out['planned52_input_identities']=[binding(r['input']) for r in js(CAND,R+'author-draft-1/planned-inputs-52.json')['records']];assert len(out['planned52_input_identities'])==52
st='review/remediation/20261003-prepare/batches/B12/acceptance-stage-1/completion-statistics-successor.json'
assert read(BASE,st)==read(CAND,st);stats=js(BASE,st)
out['all_prior_accepted_contributions']={'stats_identity':ident(BASE,st),'candidate_byte_equal':True,'accepted_batches':stats['accepted_batches'],'accepted_contribution_count':len(stats['accepted_contribution_receipts']),'receipts':stats['accepted_contribution_receipts'],'not_read_or_reapproved_history':True}
assert len(stats['accepted_contribution_receipts'])==232
out['protected_paths']={'all_existing_paths_outside_exact11_unchanged':True,'no_deleted_or_renamed_paths':True,'no_reference_changes':True,'no_public_or_main_registration_changes':True,'no_other_owner_changes':True,'publication_followup_changes':git('diff','--no-renames','--name-status',CAND,PUB).decode().splitlines()}
for l in out['protected_paths']['publication_followup_changes']:assert l.startswith('A\t'+R+'candidate-1/scope-applied-1/')
def rows(data):
 ans=[];series=None
 for line in data.decode().splitlines():
  m=re.match(r'## (QC|WS|PA|RC|EG|EN|FC|MG|TT)[:：]',line)
  if m:series=m.group(1)
  m=re.match(r'^\|\s*((?:[QWP]\d+[a-z]?)|(?:[A-Z]{2}-\d+))\s*\|',line)
  if m:ans.append((series,m.group(1),line))
 return ans
out['catalog_independent_checks']=[]
for p in ['deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md','deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md']:
 old,new=rows(read(BASE,p)),rows(read(CAND,p));okeys=[r[:2] for r in old];nkeys=[r[:2] for r in new];assert len(set(okeys))==len(okeys);assert len(set(nkeys))==len(nkeys)
 assert [k for k in nkeys if k in set(okeys)]==okeys
 nd={r[:2]:r[2] for r in new};changed=[{'series':s,'id':i,'before':text,'after':nd[(s,i)]} for s,i,text in old if text!=nd[(s,i)]]
 if 'creature-rpg-' in p:assert [(x['series'],x['id']) for x in changed]==[('FC','FC-10')];assert nkeys==okeys
 else:assert {tuple((x['series'],x['id'])) for x in changed}=={('QC','Q32'),('QC','Q36'),('QC','Q37'),('QC','Q38'),('QC','Q40'),('QC','Q41'),('PA','P19'),('PA','P20'),('PA','P22'),('RC','W22b')}
 out['catalog_independent_checks'].append({'path':p,'old_counts':dict(collections.Counter(s for s,i,t in old)),'new_counts':dict(collections.Counter(s for s,i,t in new)),'old_ID_order_and_multiplicity_preserved':True,'changed_old_rows':changed,'added_rows':[dict(series=s,id=i,text=t) for s,i,t in new if (s,i) not in set(okeys)],'unchanged_old_rows':len(old)-len(changed),'other_owner_rows_byte_equal':True,'runtime_tests_executed':0})
map_path=R+'author-draft-1/affected-interface-map.json';out['potential_owner_interface_bindings']=[]
for v in js(CAND,map_path)['potential_interfaces']:
 row={'owner':v['accepted_batch'],'inputs':[]}
 for x in v['current_accepted_inputs_consumed_by_author']+v['reverse_declared_reader_inputs']:
  binding(x);row['inputs'].append({'base':x,'candidate':ident(CAND,x['path']),'unchanged':read(BASE,x['path'])==read(CAND,x['path'])})
 row['shared_control_IDs']=v['shared_control_IDs'];out['potential_owner_interface_bindings'].append(row)
extra=[('B09','combat-requirements/wp41-switching-positioning-and-escape.md'),('B11','combat-requirements/wp47-b-switching-control-and-item-changes.md'),('B11','pokemon-rules/wp50-held-item-triggers-and-consumption.md'),('B11','combat-requirements/wp49-ability-phase-triggers.md')]
out['independently_found_current_interfaces']=[]
for owner,p in extra:
 p='deliverables/final-specification-set/'+p;assert read(BASE,p)==read(CAND,p)
 out['independently_found_current_interfaces'].append({'owner':owner,'base':ident(BASE,p),'candidate':ident(CAND,p),'unchanged':True})
pathlib.Path('/tmp/B13-affected-shared-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'complete_stream':fi,'changes':len(changes),'formal_outputs':len(formal),'scope_patch_equal':True,'full_controls':len(out['all8_control_bindings']),'planned_input_identities':len(out['planned52_input_identities']),'accepted_contributions_preserved':len(stats['accepted_contribution_receipts']),'catalogs':[{k:v[k] for k in ['path','old_counts','new_counts','unchanged_old_rows']} for v in out['catalog_independent_checks']]},ensure_ascii=False,indent=2))
