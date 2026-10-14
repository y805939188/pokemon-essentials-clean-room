from pathlib import Path
from collections import Counter
import datetime,difflib,hashlib,json,subprocess,sys
ROOT=Path('/workspace/pokemon-essentials-clean-room');OUT=Path(__file__).resolve().parent
ACT='86bbc99b28d93db4ed9d6897daf5f3725ccd1808';CAND='9971fe84896786645cdcda3ab45e5caf7785cabc';PREP='469a268b92daed7b4d28d7fd0da75520cbb7228f';MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6';REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX='review/remediation-sixth-20261014-prepare/';INPUT=PREFIX+'integration/U01-U14-final-composite-20261014/actual-review-input.json'
start=datetime.datetime.now(datetime.timezone.utc).isoformat();commands=[];cache={};errors=[]
def git(*args):
 p=subprocess.run(['git',*args],cwd=ROOT,capture_output=True);commands.append({'argv':['git',*args],'exit':p.returncode,'stderr':p.stderr.decode()})
 if p.returncode:raise RuntimeError(p.stderr.decode())
 return p.stdout
def blob(c,p):
 key=(c,p)
 if key not in cache:cache[key]=git('show',c+':'+p)
 return cache[key]
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def canon(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def check_identity(c,p,decl,role):
 b=blob(c,p);got=ident(b);entry=git('ls-tree',c,'--',p).decode().strip();parts=entry.split(None,3)
 return {'role':role,'commit':c,'path':p,'declared':decl,'observed':got,'entry':entry,'match':all(got[k]==decl[k] for k in got if k in decl),'mode_type_ok':len(parts)>=3 and parts[0]=='100644' and parts[1]=='blob' and parts[2]==got['git_blob']}
def schema(x,p='',dst=None):
 dst={} if dst is None else dst;dst.setdefault(p,Counter())[type(x).__name__]+=1
 if isinstance(x,dict):
  for k,v in x.items():schema(v,p+'/'+k,dst)
 elif isinstance(x,list):
  for v in x:schema(v,p+'/*',dst)
 return dst
j=json.loads(blob(ACT,INPUT));checks={};treechecks=[]
for c,t,role in [(ACT,'67e8c55d520fa8cad2928cb4b95e24c3ed602d5a','actual workspace'),(MAIN,j['fixed_main_workspace_tree'],'fixed main workspace'),(REF,j['fixed_reference_tree'],'fixed reference'),(j['pre_integration_commit'],j['delta_from_prior_actual']['base_workspace_tree'],'prior actual workspace')]:
 got=git('rev-parse',c+'^{tree}').decode().strip();treechecks.append({'commit':c,'role':role,'expected':t,'observed':got,'match':got==t})
for c,t,role in [(ACT,'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c','actual formal'),(MAIN,j['fixed_formal_tree'],'fixed main formal'),(j['pre_integration_commit'],j['delta_from_prior_actual']['base_formal_tree'],'prior formal')]:
 got=git('rev-parse',c+':deliverables/final-specification-set').decode().strip();treechecks.append({'commit':c,'role':role,'expected':t,'observed':got,'match':got==t})
checks['fixed_workspace_formal_reference_trees_match']=all(x['match'] for x in treechecks)
identities=[];bt=[];non_E_membership_not_checked=[]
E_BATCHES={'R6-U02','R6-U05','R6-U10','R6-U11','R6-U13'}
for b in j['batches']:
 identities.append(check_identity(ACT,b['contract_path'],b['contract_identity'],b['batch']+' current contract metadata'))
 if b['batch'] not in E_BATCHES:
  non_E_membership_not_checked.append({'batch':b['batch'],'candidate_commit':b['candidate_published_commit'],'report_commit':b['independent_review']['review_commit'],'scope':'Full input metadata structurally read; fixed candidate/report membership not independently checked by E. No E defect or new semantic signature inferred.'})
  continue
 r=b['independent_review'];identities.append(check_identity(r['review_commit'],r['report_path'],r['report_identity'],b['batch']+' necessary shared independent report'))
 for c,expr,expected,role in [(b['candidate_published_commit'],'^{tree}',b['candidate_workspace_tree'],'candidate workspace'),(b['candidate_published_commit'],':'+PREFIX+'candidates/'+b['batch']+'/mirror',b['candidate_mirror_tree'],'candidate mirror')]:
  got=git('rev-parse',c+expr).decode().strip();bt.append({'batch':b['batch'],'commit':c,'role':role,'expected':expected,'observed':got,'match':got==expected})
 if 'review_workspace_tree' in r:
  got=git('rev-parse',r['review_commit']+'^{tree}').decode().strip();bt.append({'batch':b['batch'],'role':'review workspace','expected':r['review_workspace_tree'],'observed':got,'match':got==r['review_workspace_tree']})
 if 'review_directory_tree' in r:
  got=git('rev-parse',r['review_commit']+':'+r['report_path'].rsplit('/',1)[0]).decode().strip();bt.append({'batch':b['batch'],'role':'review directory','expected':r['review_directory_tree'],'observed':got,'match':got==r['review_directory_tree']})
checks['all14_current_contract_and5_E_report_tree_identities_match']=all(x['match'] and x['mode_type_ok'] for x in identities) and all(x['match'] for x in bt)
non_E_contributions_declarative=[]
for f in j['files']:
 for c,key,role in [(MAIN,'baseline','fixed baseline'),(j['pre_integration_commit'],'previous_actual','prior actual'),(ACT,'actual','frozen actual')]:identities.append(check_identity(c,f['path'],f[key],role))
 for x in f['contributions']:
  selected=x['batch']=='R6-U13' or (f['path'].endswith('wp40-commands-obedience-and-action-order.md') and x['batch'] in ['R6-U02','R6-U05']) or (f['path'].endswith('pokemon-rules-wp53-60-61-62-69-70.md') and x['batch']=='R6-U11') or (f['path'].endswith('wp66-a-party-and-summary-ui.md') and x['batch']=='R6-U10')
  if selected:identities.append(check_identity(x['candidate_commit'],x['candidate_path'],x['identity'],x['batch']+' selected E candidate contribution'))
  else:non_E_contributions_declarative.append({'formal_path':f['path'],'declaration':x,'scope':'Metadata declaration only; E does not verify nonselected fixed membership or semantic contribution.'})
checks['all53_formal_metadata_and_E_selected_contribution_identities_match']=all(x['match'] and x['mode_type_ok'] for x in identities)
contribution_count=sum(len(f['contributions']) for f in j['files']);allids=[x for b in j['batches'] for x in b['required_ids']]
checks['53_paths_76_contributions_14_batches_56_unique_ids']=len(j['files'])==53 and contribution_count==76 and len(j['batches'])==14 and len(allids)==len(set(allids))==56 and set(allids)==set(j['required_ids']) and j['required_count']==56
all_actual_paths=set(git('diff','--name-only',MAIN,ACT,'--','deliverables/final-specification-set').decode().splitlines());checks['actual53_changed_paths_equal_declared_set']=all_actual_paths=={f['path'] for f in j['files']}
checks['pending_state_no_integrated_closed_runtime_claim']=j['state']=='ACTUAL_COMPOSITION_PENDING_INDEPENDENT_REVIEW' and j['INTEGRATED_PASS'] is None and j['formal_acceptance'] is None and j['CLOSED'] is False and all(j[k]==0 for k in ['new_source_execution','new_independent_behavior_model_execution','host_Demo_real_save_execution']) and j['administrative_sync']['state']=='DEFERRED_UNTIL_INDEPENDENT_ACTUAL_REVIEW'
cp=PREFIX+'contracts/R6-U13.json';oldb=blob(PREP,cp);candb=blob(CAND,cp);actualb=blob(ACT,cp);old=json.loads(oldb);actual=json.loads(actualb)
prompt=blob(PREP,PREFIX+'prompts/R6-U13-A.md').decode();block=prompt.split('```json\n',1)[1].split('\n```',1)[0].encode();checks['U13_exact_old_candidate_actual_contract_and_prompt_binding']=oldb==candb==actualb and block==oldb.rstrip(b'\n') and json.loads(block)==actual
seven=['identity_and_verdict','bidirectional_evidence','premises_and_counterexample','minimum_revision_contract','acceptance_and_regression','independent_adjudication','dependencies_and_receivers'];groups=[]
for a,b in zip(old['scope_contracts'],actual['scope_contracts']):
 groups.append({'id':b['id'],'whole_record_equal':a==b,'whole_record_canonical_sha256':canon(b),'seven_groups':{k:{'complete_present':k in b,'equal':a[k]==b[k],'canonical_sha256':canon(b[k])} for k in seven}})
checks['all8_complete7group_records_and_headers_equal']=old==actual and len(groups)==8 and all(x['whole_record_equal'] and all(z['complete_present'] and z['equal'] for z in x['seven_groups'].values()) for x in groups)
contractbinding={'old':ident(oldb),'candidate':ident(candb),'actual':ident(actualb),'canonical_sha256':canon(actual),'full_header_keys':[k for k in actual if k!='scope_contracts'],'parsed_full_objects_equal':old==actual,'seven_group_records':groups,'root_character_count_correction':{'characters':len(oldb.decode()),'bytes':len(oldb),'meaning':'354597 was character count; exact specified old/new contract bytes did not change.'}}
# All E-selected candidate edit blocks must occur at the exact joined postimage.
selected=[]
for f in j['files']:
 for x in f['contributions']:
  if x['batch']=='R6-U13' or (f['path'].endswith('wp40-commands-obedience-and-action-order.md') and x['batch'] in ['R6-U02','R6-U05']) or (f['path'].endswith('pokemon-rules-wp53-60-61-62-69-70.md') and x['batch']=='R6-U11') or (f['path'].endswith('wp66-a-party-and-summary-ui.md') and x['batch']=='R6-U10'):
   base=blob(MAIN,f['path']).decode().splitlines();candidate=blob(x['candidate_commit'],x['candidate_path']).decode().splitlines();post=blob(ACT,f['path']).decode().splitlines();sm=difflib.SequenceMatcher(None,base,candidate,autojunk=False);blocks=[]
   for tag,a,b,c,d in sm.get_opcodes():
    if tag=='equal':continue
    newblock=candidate[c:d];positions=[i+1 for i in range(len(post)-len(newblock)+1) if post[i:i+len(newblock)]==newblock] if newblock else []
    blocks.append({'operation':tag,'baseline_span':[a+1,b],'candidate_span':[c+1,d],'candidate_postimage_lines':newblock,'actual_occurrence_starts':positions,'exact_nonempty_postimage_retained':bool(newblock) and bool(positions)})
   selected.append({'batch':x['batch'],'formal_path':f['path'],'candidate_commit':x['candidate_commit'],'candidate_path':x['candidate_path'],'candidate_identity':ident(blob(x['candidate_commit'],x['candidate_path'])),'actual_identity':ident(blob(ACT,f['path'])),'whole_file_equal':blob(x['candidate_commit'],x['candidate_path'])==blob(ACT,f['path']),'blocks':blocks})
checks['all8U13_and4_sibling_contribution_blocks_preserved']=all(all(z['exact_nonempty_postimage_retained'] for z in x['blocks']) for x in selected)
# Root receiver payload exact line is the applied delta while U10 Summary edits remain.
r=j['receiver_delta'];payload=json.loads(blob(r['payload_commit'],r['payload_path']));post=blob(ACT,r['formal_path']).decode().splitlines();oldpost=blob(j['pre_integration_commit'],r['formal_path']);line=payload['proposed_full_line'];positions=[i+1 for i,x in enumerate(post) if x==line]
receiver={'commit':ACT,'formal_path':r['formal_path'],'actual_identity':ident(blob(ACT,r['formal_path'])),'origin_payload_commit':r['payload_commit'],'origin_payload_path':r['payload_path'],'payload_identity':ident(blob(r['payload_commit'],r['payload_path'])),'postimage_occurrence_lines':positions,'base_line_match':payload['old_full_line'] in blob(MAIN,r['formal_path']).decode().splitlines(),'exact_postimage':line,'old_proposed_state_is_historical':payload['status'],'current_receiver_record':r,'prior_actual_full_bytes_unchanged':blob(ACT,r['formal_path'])==oldpost}
checks['true_WP66_receiver_delta_applied_exactly_once']=r['applied'] is True and r['U13_old_bundle_received'] is False and r['counts_as_additional_candidate_PASS'] is False and r['INTEGRATED_PASS'] is False and positions and len(positions)==1 and receiver['base_line_match'] and receiver['prior_actual_full_bytes_unchanged']
resolution_checks=[]
for x in j['resolutions']:
 b=blob(ACT,x['path']).decode()
 if 'actual_line' in x:resolution_checks.append({'path':x['path'],'actual_line_present':x['actual_line'] in b.splitlines()})
 else:resolution_checks.append({'path':x['path'],'scope':'U10/U12 append metadata identity verified only; own group E does not sign their semantic join.','pending_semantics_owner':'D'})
checks['root_resolution_exact_postimage_present']=all(x.get('actual_line_present',True) for x in resolution_checks)
changed=git('diff','--name-only',j['pre_integration_commit'],ACT,'--','deliverables/final-specification-set').decode().splitlines();checks['delta8_before_after_and_unchanged45_match']=set(changed)=={x['path'] for x in j['delta_from_prior_actual']['changed_formal_paths']} and len(changed)==8 and len(j['delta_from_prior_actual']['unchanged_prior_formal_paths'])==45 and all(blob(ACT,p)==blob(j['pre_integration_commit'],p) for p in j['delta_from_prior_actual']['unchanged_prior_formal_paths']) and all(ident(blob(j['pre_integration_commit'],x['path']))==x['before'] and ident(blob(ACT,x['path']))==x['after'] for x in j['delta_from_prior_actual']['changed_formal_paths'])
checks['WP21_unchanged_prospective_baseline']=all(ident(blob(ACT,x['path']))==x['identity'] and blob(ACT,x['path'])==blob(MAIN,x['path']) for x in j['unchanged_prospective_paths'])
h0=json.loads(blob(CAND,PREFIX+'candidates/R6-U13/evidence/historical-regression.json'));h1=json.loads(blob(ACT,PREFIX+'candidates/R6-U13/evidence/historical-regression.json'));checks['old74_historical_evidence_exact_byte_binding']=blob(CAND,PREFIX+'candidates/R6-U13/evidence/historical-regression.json')==blob(ACT,PREFIX+'candidates/R6-U13/evidence/historical-regression.json') and len(h1['affected_path_navigation'])==74
# Prefix preservation against all shared current content is new evidence, not old PASS transfer.
wp40='deliverables/final-specification-set/combat-requirements/wp40-commands-obedience-and-action-order.md';addon='Arena 裁判调用同一完整取消：只清列明持续招，回复期为正时保留当前招身份；裁判后的存活未替代者仍受下一轮回复门约束（WP56 §3.2），败者倒下/补位清效另算。'.encode();w=blob(ACT,wp40);prior=blob(j['pre_integration_commit'],wp40)
checks['WP40_prior_U02_U05_all_bytes_preserved_after_only_U13_addition']=w.count(addon)==1 and w.replace(addon,b'')==prior
pt='deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md';checks['pokemon_shared_nonSF_U11_suffix_equals_prior_actual']=blob(ACT,pt).split('## BP：'.encode(),1)[1]==blob(j['pre_integration_commit'],pt).split('## BP：'.encode(),1)[1]
checks['U13_SF_prefix_complete_equals_selected_candidate']=blob(ACT,pt).split('## BP：'.encode(),1)[0]==blob(CAND,PREFIX+'candidates/R6-U13/mirror/'+pt).split('## BP：'.encode(),1)[0]
result={'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cwd':str(ROOT),'argv':sys.argv,'runtime':sys.version,'actual_commit':ACT,'input_identity':ident(blob(ACT,INPUT)),'complete_recursive_input_schema':{k:dict(v) for k,v in schema(j).items()},'checks':checks,'tree_bindings':treechecks,'batch_trees':bt,'all_declared_payload_identity_bindings':identities,'declared_count':len(identities),'contribution_count':contribution_count,'non_E_membership_not_checked':non_E_membership_not_checked,'non_E_contributions_declarative':non_E_contributions_declarative,'contract_binding':contractbinding,'selected_groupE_contributions':selected,'WP66_receiver':receiver,'root_resolution_checks':resolution_checks,'historical_qualification_scope':'Exact original74 evidence byte reuse; new actual selected clauses/shared contribution preservation independently checked. No full R1-R5 or other groups semantic verdict transfer.','new_source_execution':0,'author_script_execution':0,'host_real_save_execution':0,'model_config':'UNVERIFIED','all_checks_pass':all(checks.values()),'commands':commands}
(OUT/'independent-actual-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'contract-binding.json').write_text(json.dumps(contractbinding,ensure_ascii=False,indent=2)+'\n');(OUT/'selected-contribution-spans.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2)+'\n');(OUT/'WP66-actual-receiving.json').write_text(json.dumps(receiver,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'all_checks_pass':result['all_checks_pass'],'checks':checks,'declared_identities':len(identities),'53paths':len(j['files']),'14batches':len(j['batches']),'76contributions':contribution_count,'selected_E_contributions':len(selected),'input_schema_nodes':len(result['complete_recursive_input_schema']),'contract_bytes':len(actualb),'contract_characters':len(actualb.decode()),'exact_contract_unchanged':oldb==actualb,'wp66_actual_line':positions},ensure_ascii=False))
