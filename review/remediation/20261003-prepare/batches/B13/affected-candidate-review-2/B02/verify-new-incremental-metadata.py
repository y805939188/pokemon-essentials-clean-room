import subprocess, pathlib, hashlib, json, re, collections
ROOT=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel']).decode().strip())
BASE='8e67f780c204d593d89f364f585d2c6c2fe74631'
OLD='5845e8084ced280e51c51a4081ec8583a9c2ca39'
NEW='db9e6ed1997efe5bf94dac952aad44fd3b9ebd21'
PUB='dbabf68ec00e7e368d594dfb49497ba5a9cbf578'
SCOPE='231c9f25df4dd64961fb9290ff52302782a9fdb8'
PRIOR='4a75ca146e10062e469a42a9610bc3026861a34c'
R='review/remediation/20261003-prepare/batches/B13/'
cache={}
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
def read(ref,p):
 if (ref,p) not in cache:cache[(ref,p)]=git('show',ref+':'+p)
 return cache[(ref,p)]
def obj(ref,p):return json.loads(read(ref,p))
def ident(ref,p):
 b=read(ref,p);return {'commit':ref,'path':p,'git_blob':git('rev-parse',ref+':'+p).decode().strip(),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
def binding(x):
 z=ident(x['commit'],x['path']);assert all(z[k]==x[k] for k in ['git_blob','sha256','bytes']);return z
prior=obj(PRIOR,R+'affected-candidate-review-1/B02/shared-audit.json')
out={'role':'INDEPENDENT_INCREMENTAL_AFFECTED_CANDIDATE_METADATA_ONLY','FIX_BASE':BASE,'OLD':OLD,'reviewed_NEW':NEW,'publication':PUB,'scope_amendment2':SCOPE,'prior_own_report':PRIOR}
out['identities']={}
for ref,t in [(BASE,'ae2f491294eb4f97be6b75f75706c16279f9bf46'),(OLD,'23f92a9c446f5f0fbcee44df2f57d85df4dd0e3c'),(NEW,'d7e8953fb0f3eff949c3dbee1f9361b0b8f71804'),(PUB,'d17afab3b727253a0dc147b9d9a40d0869fed363')]:
 assert git('rev-parse',ref+'^{tree}').decode().strip()==t;out['identities'][ref]=t
assert git('rev-parse',PUB+'^').decode().strip()==NEW
out['author_remote_ref']=git('ls-remote','--exit-code','origin','refs/heads/codex/cloud-dot-B13-author-1-20261010').decode().strip();assert out['author_remote_ref'].split()[0]==PUB
receipt=obj(PUB,R+'candidate-1/two-findings-scope-applied-1/publication-receipt.json')
out['complete_unfiltered_streams']={}
for label,start in [('OLD_to_NEW',OLD),('FIX_BASE_to_NEW',BASE)]:
 b=git('diff','--binary','--no-ext-diff','--no-textconv',start,NEW)
 meta={'command':['git','diff','--binary','--no-ext-diff','--no-textconv',start,NEW],'paths_filtered':False,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(('blob '+str(len(b))+'\0').encode()+b).hexdigest()}
 for k in ['bytes','sha256','git_blob']:assert meta[k]==receipt['whole_unfiltered_diff_streams'][label][k]
 if label=='OLD_to_NEW':assert b==read(PUB,R+'candidate-1/two-findings-scope-applied-1/OLD-to-NEW.full.patch')
 pathlib.Path('/tmp/B13-affected2-'+label+'.full.patch').write_bytes(b);out['complete_unfiltered_streams'][label]=meta
formal=[x['candidate']['path'] for x in prior['all11_outputs']]
changed=[x.split('\t',1) for x in git('diff','--no-renames','--name-status',OLD,NEW).decode().splitlines()]
expected={'deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md','deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md','specs/combat/wp58-battle-recording-and-playback.md'}
assert {p for s,p in changed if s=='M'}==expected
assert all(p in expected or (s=='A' and (p.startswith(R+'author-draft-1/') or p.startswith(R+'candidate-1/'))) for s,p in changed)
out['all_changed_paths']=[]
for s,p in changed:
 b=read(NEW,p)
 if p.endswith('.json'):json.loads(b)
 out['all_changed_paths'].append({'status':s,**ident(NEW,p),'kind':'FORMAL_DELTA' if p in expected else 'OWN_ADDED_METADATA_OR_FROZEN_EVIDENCE'})
out['all11_outputs']=[]
submitted=obj(NEW,R+'author-draft-1/two-findings-scope-applied-1/all-11-formal-output-identities.json')['outputs'];assert len(submitted)==11
assert {x['path'] for x in submitted}==set(formal)
for x in submitted:
 p=x['path'];z=ident(NEW,p);assert all(z[k]==x['output'][k] for k in ['git_blob','sha256','bytes']);assert read(PUB,p)==read(NEW,p)
 out['all11_outputs'].append({'before_OLD':ident(OLD,p),'reviewed_NEW':z,'unchanged_from_OLD':read(OLD,p)==read(NEW,p),'publication_equal':True})
grant_path=R+'scope-amendment-2/scope-amendment.json';grant=obj(SCOPE,grant_path);out['scope2_binding']=ident(SCOPE,grant_path)
assert read(SCOPE,grant_path)==read(NEW,R+'author-draft-1/two-findings-scope-applied-1/scope-inputs/scope-amendment.json')
assert grant['allowed_original_write_paths']==['specs/combat/wp58-battle-recording-and-playback.md']
g=grant['records'][0];binding(g['before']);binding(g['after_to_apply']);binding(grant['source_whole_patch'])
assert read(OLD,g['path'])==read(g['before']['commit'],g['before']['path'])
assert read(NEW,g['path'])==read(g['after_to_apply']['commit'],g['after_to_apply']['path'])
def section(b):
 pre,rest=b.split('### 5.2 换人序列\n\n'.encode(),1);mid,post=rest.split('### 5.3 模式差异'.encode(),1);return pre,mid,post
a,b=section(read(OLD,g['path'])),section(read(NEW,g['path']));assert a[0]==b[0] and a[2]==b[2]
assert a[1].decode().strip()==g['exact_before_clause'] and b[1].decode().strip()==g['exact_after_clause']
def norm(b):
 return b'\n'.join(re.sub(br'^(@@.*?@@).*$',br'\1',l) if l.startswith(b'@@') else l for l in b.splitlines() if not l.startswith((b'diff --git ',b'index ')))
patch=read(grant['source_whole_patch']['commit'],grant['source_whole_patch']['path'])
assert norm(patch)==norm(git('diff','--binary','--no-ext-diff','--no-textconv',OLD,NEW,'--',g['path']))
out['scope2_exact_application']={'before':g['before'],'after':ident(NEW,g['path']),'whole_patch':grant['source_whole_patch'],'entire_before_after_equal':True,'all_outside_5_2_bytes_equal':True,'hunks_context_equal_only_Git_headers_and_function_suffix_normalized':True,'quality_PASS_from_permission':False}
out['frozen_evidence_reused_unchanged']=[]
for p in ['AGENTS.md']+[R+'author-draft-1/'+n for n in ['original-and-acceptance-controls.json','B13-downstream-contract.json','planned-inputs-52.json','source-reading-log.json','source-limits.json','inherited-source-limits.json','source-audit-successor.json','catalog-preservation.json','catalog-locks.json','static-transition-traces.json','scope-applied-1/finding-dispositions-successor.json','scope-applied-1/affected-interface-scope-successor.json','independent-review-requirements.json']]:
 assert read(OLD,p)==read(NEW,p);out['frozen_evidence_reused_unchanged'].append(ident(NEW,p))
out['prior_own_identity_audit']=ident(PRIOR,R+'affected-candidate-review-1/B02/shared-audit.json')
out['all8_controls_and_52_input_prior_identity_verification_reused']=True
out['all_current_owner_interfaces']=[]
for row in prior['potential_owner_interface_bindings']:
 outrow={'owner':row['owner'],'shared_control_IDs':row['shared_control_IDs'],'current_inputs':[]}
 for x in row['inputs']:
  p=x['base']['path'];outrow['current_inputs'].append({'before_OLD':ident(OLD,p),'reviewed_NEW':ident(NEW,p),'unchanged':read(OLD,p)==read(NEW,p)})
 out['all_current_owner_interfaces'].append(outrow)
out['additional_current_interfaces']=[]
for x in prior['independently_found_current_interfaces']:
 p=x['candidate']['path'];assert read(BASE,p)==read(OLD,p)==read(NEW,p);out['additional_current_interfaces'].append({'owner':x['owner'],'identity_NEW':ident(NEW,p),'same_as_OLD_FIX_BASE':True})
out['new_evidence_index_bindings']=[]
for x in obj(NEW,R+'author-draft-1/two-findings-scope-applied-1/current-evidence-index.json')['references']:
 binding(x);assert read(x['commit'],x['path'])==read(NEW,x['path']);out['new_evidence_index_bindings'].append({'bound':x,'equals_NEW':True})
out['old_review_input_copies']=[]
rb=obj(NEW,R+'author-draft-1/two-findings-repair-1/review-input-bindings.json')
# Review-copy identity fields are checked generically without executing any old program.
def copied_bindings(x):
 if isinstance(x,dict):
  if all(k in x for k in ['commit','path','git_blob','sha256','bytes']):
   if x['commit']==PRIOR:
    z=binding(x);out['old_review_input_copies'].append(z)
  for v in x.values():copied_bindings(v)
 elif isinstance(x,list):
  for v in x:copied_bindings(v)
copied_bindings(rb)
out['all7_frozen_review_copy_checks']=[]
for x in rb['inputs']:
 z=ident(NEW,x['copy']);assert all(z[k]==x[k] for k in ['git_blob','sha256','bytes'])
 if x['commit']==PRIOR:assert read(PRIOR,x['path'])==read(NEW,x['copy'])
 out['all7_frozen_review_copy_checks'].append({'source_binding':x,'copy_NEW':z,'matches_source_blob_sha256_bytes':True,'own_prior_original_commit_byte_comparison':x['commit']==PRIOR,'quality_signature_transferred':False})
def dispositions(ref,path):
 x=obj(ref,path)
 return next(v for v in x.values() if isinstance(v,list) and len(v)==8 and all(isinstance(y,dict) and 'id' in y for y in v))
old_disp=dispositions(OLD,R+'author-draft-1/scope-applied-1/finding-dispositions-successor.json')
new_disp=dispositions(NEW,R+'author-draft-1/two-findings-scope-applied-1/finding-dispositions-successor.json')
assert [x['id'] for x in old_disp]==[x['id'] for x in new_disp]
out['all8_disposition_control_preservation']=[]
for a,b in zip(old_disp,new_disp):
 fields=['whole_control','original_required_fields','current_required_fields','approved_acceptance_gate','whole_extensions_and_root_adjudications']
 for k in fields:assert a[k]==b[k],(a['id'],k)
 out['all8_disposition_control_preservation'].append({'id':a['id'],'original_current_root_extension_acceptance_fields_equal':True,'canonical_state':b['canonical_state']})
stats=prior['all_prior_accepted_contributions']['stats_identity']['path'];assert read(BASE,stats)==read(OLD,stats)==read(NEW,stats)
out['all232_accepted_contributions_preserved']={'identity_NEW':ident(NEW,stats),'old_verified_receipts_reused':prior['all_prior_accepted_contributions']['accepted_contribution_count'],'whole_bytes_unchanged_BASE_OLD_NEW':True,'historical_reapproval':False}
def rows(b):
 ans=[];family=None
 for line in b.decode().splitlines():
  m=re.match(r'## (QC|WS|PA|RC|EG|EN|FC|MG|TT)[:：]',line)
  if m:family=m.group(1)
  m=re.match(r'^\|\s*((?:[QWP]\d+[a-z]?)|(?:[A-Z]{2}-\d+))\s*\|',line)
  if m:ans.append((family,m.group(1),line))
 return ans
out['catalog_checks']=[]
for p in ['deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md','deliverables/final-specification-set/test-catalog/creature-rpg-wp35-36-57-64-68.md']:
 a,b=rows(read(OLD,p)),rows(read(NEW,p));ak=[x[:2] for x in a];bk=[x[:2] for x in b];assert len(set(ak))==len(ak) and len(set(bk))==len(bk)
 assert [x for x in bk if x in set(ak)]==ak
 bd={x[:2]:x[2] for x in b};delta=[{'series':s,'id':i,'before':t,'after':bd[s,i]} for s,i,t in a if t!=bd[s,i]];added=[{'series':s,'id':i,'text':t} for s,i,t in b if (s,i) not in set(ak)]
 if 'combat-requirements' in p:
  assert [(x['series'],x['id']) for x in delta]==[('WS','W35')];assert [(x['series'],x['id']) for x in added]==[('RC','W26')]
 else:assert read(OLD,p)==read(NEW,p) and not delta and not added
 out['catalog_checks'].append({'path':p,'OLD_counts':dict(collections.Counter(x[0] for x in a)),'NEW_counts':dict(collections.Counter(x[0] for x in b)),'changed_old_rows':delta,'new_rows':added,'unchanged_old_rows':len(a)-len(delta),'all_OLD_ID_order_multiplicity_preserved':True,'W16_W24_W25_W28_W29_retained':True,'executed_designs':0})
formal_check=subprocess.run(['git','diff','--check',OLD,NEW,'--',*sorted(expected)],cwd=ROOT,capture_output=True);assert formal_check.returncode==0
whole_check=subprocess.run(['git','diff','--check',OLD,NEW],cwd=ROOT,capture_output=True);diagnostics=whole_check.stdout.decode();paths=sorted(set(l.split(':',1)[0] for l in diagnostics.splitlines() if l.startswith(R)))
assert whole_check.returncode==2 and paths and all(p.endswith('.patch') for p in paths)
out['diff_check']={'formal_delta':'PASS','whole_unfiltered_exit':2,'diagnostic_paths':paths,'diagnostics_sha256':hashlib.sha256(whole_check.stdout).hexdigest(),'classification':'Serialized patch context whitespace only, not formal-output defect; exact full diff bytes preserved, not trimmed.'}
out['protection']={'all_existing_paths_outside_exact3_unchanged':True,'no_delete_rename':True,'reference_main_public_all_other_owner_and_old_reports_unchanged':True,'no_runtime_reference_vectors_or_historical_program_execution':True}
out['NEW_to_publication']=git('diff','--no-renames','--name-status',NEW,PUB).decode().splitlines();assert all(l.startswith('A\t'+R+'candidate-1/two-findings-scope-applied-1/') for l in out['NEW_to_publication'])
pathlib.Path('/tmp/B13-affected2-shared-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'streams':out['complete_unfiltered_streams'],'changed_paths':len(changed),'formal_changed':len(expected),'all11_verified':len(out['all11_outputs']),'accepted_receipts_preserved':232,'catalogs':[{k:x[k] for k in ['path','OLD_counts','NEW_counts','unchanged_old_rows']} for x in out['catalog_checks']],'scope2':'EXACT_MATCH; QUALITY_SEPARATE','diff_check':out['diff_check']},ensure_ascii=False,indent=2))
