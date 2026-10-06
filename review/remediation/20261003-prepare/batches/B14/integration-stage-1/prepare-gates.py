"""New B14-G bounded reader/actual-request metadata only; does not dispatch or approve."""
import bookkeeping as k
import pathlib,json,re,copy,csv,hashlib,subprocess
G=k.G;B=k.B;A=k.A;C=k.C;P='review/remediation/20261003-prepare/';BP=P+'batches/B14/'
con=k.obj(A,k.CONTRACT);planned=[]
def fixed(commit,path,binding):return k.identity(k.git(commit,path),path,binding,commit)
def current(p):return k.identity(pathlib.Path(p).read_bytes(),p,'INTENDED_G_SNAPSHOT_AWAIT_EXTERNAL_ACT')
for r in con['planned_reads']:
 p=r['path'];old=r['accepted_current_input'];cm=old.get('commit',A);before=fixed(cm,p,'ACCEPTED_INPUT_OR_FIXED_HISTORICAL')
 for f in ['git_blob','sha256','bytes']:assert before[f]==old[f],(p,f)
 if r['planned_index'] in [47,48]:
  assert cm==B['fixed_originalREPORT'];now=fixed(cm,p,'IMMUTABLE_ORIGINAL_REPORT_HISTORICAL_INPUT_NOT_CURRENT_TREE')
 else:now=current(p)
 planned.append(dict(planned_index=r['planned_index'],path=p,before=before,current=now,changed=before['git_blob']!=now['git_blob'],reading_role='Contract refreeze; semantic coverage separately recorded in reading-log.json'))
assert len(planned)==72
additional={};owners={}
for rr in B['report_bindings']:
 if rr['owner']=='FULL':continue
 paths={};man=k.obj(rr['report_commit'],rr['directory']+'input-identities.json')
 def walk(v):
  if isinstance(v,dict):
   p=v.get('path')
   if isinstance(p,str) and p.startswith(('deliverables/final-specification-set/','specs/')) and pathlib.Path(p).is_file():paths[p]=current(p)
   for w in v.values():walk(w)
  elif isinstance(v,list):
   for w in v:walk(w)
 walk(man)
 gate=next(x for x in con['accepted_reverse_review_gates'] if x['accepted_batch']==rr['owner'])
 ctrlpaths=[]
 # Exact immutable accepted owner registration and source limits; no old program execution.
 for name in ['finding-registration.json','current-readers.json','integration-manifest.json','source-limits.json']:
  p=P+'batches/'+rr['owner']+'/integration-stage-1/'+name
  if pathlib.Path(p).is_file():ctrlpaths.append(fixed(A,p,'ACCEPTED_OWNER_CONTROL_HISTORY'))
 for p,x in paths.items():additional[p]=x
 owners[rr['owner']]=dict(accepted_gate=gate,current_reader_identities=list(paths.values()),accepted_owner_control_inputs=ctrlpaths,candidate_receipt=fixed(rr['report_commit'],rr['directory']+'review-manifest.json','FIXED_C3_CANDIDATE_RECEIPT'),full_report_directory=rr['paths'],semantic_scope='Only complete named affected interfaces/owner controls; no unrelated domain reapproval')
management=[fixed(A,P+'batches/B09/acceptance-stage-1/'+s,'ACCEPTED_B09_C_MANAGEMENT') for s in ['acceptance-manifest.json','completion-statistics-successor.json','B14-downstream-contract.json','readiness-and-conflicts.json','report-corrections-successor.json','downstream-handshake.json']]
public=[current(p) for p in B['public_paths']]
current_G_registration_inputs=[current((G/name).as_posix()) for name in ['finding-registration.json','clause-location-bindings.json','pre-freeze-navigation-correction.json']]
formal=[current(p) for p in B['formal_paths']]
extra=[current(x['path']) for x in con['additional_current_B09_normative_inputs']]
catalogs=[current(p) for p in B['formal_paths'] if '/test-catalog/' in p]
k.save('current-readers.json',dict(stage='B14-G',accepted_predecessor=A,exact_passed_C3=C,actual_identity=B['actual_identity'],planned_total=72,planned=planned,current_public_inputs=public,formal12=formal,both_whole_catalogs=catalogs,additional_current_B09_normative_inputs=extra,affected_owner_scopes=owners,additional_affected_current_inputs=list(additional.values()),current_management_inputs=management,current_G_registration_inputs=current_G_registration_inputs,fixed_original_and_acceptance=[con['fixed_original_findings'],con['fixed_approved_acceptance']],binding_rule='Two global report inputs explicitly retain originalREPORT history. Current filesystem content is an intended G snapshot only until exact external ACT binding. Immutable dated history is not resnapshotted; no recursive self-hashes.',semantic_coverage='See separate reading log; hash/refreeze does not prove behavior.'))
# Existing five-column schema, necessary current paths only, excluding this file/new-record self recursion.
identities={}
for x in [r['current'] for r in planned]+public+formal+extra+catalogs+list(additional.values())+management+current_G_registration_inputs:
 identities[(x['path'],x['binding'])]=x
for owner in owners.values():
 for x in owner['accepted_owner_control_inputs']:identities[(x['path'],x['binding'])]=x
rows=['path\tgit_blob\tsha256\tbytes\tbinding\n']
for x in identities.values():rows.append('\t'.join(str(x[f]) for f in ['path','git_blob','sha256','bytes','binding'])+'\n')
(G/'current-hashes.tsv').write_text(''.join(rows))
repro=dict(actual_commit=None,actual_tree=None,actual_parents=None,identity_status='AWAIT_EXTERNAL_COORDINATOR_MECHANICAL_FREEZE',endpoint_rule='ACT is the externally supplied full commit, never a branch HEAD or report label.',flags=['--no-ext-diff','--no-textconv','--no-renames','--binary','--full-index','--no-color'],path_filter=None,predecessor_to_ACT=dict(from_commit=A,to_commit=None,complete_diff=None,sha256=None,bytes=None,status='MUST_ACQUIRE_COMPLETE_UNFILTERED_AFTER_EXTERNAL_ACT',command='git diff --no-ext-diff --no-textconv --no-renames --binary --full-index --no-color '+A+' <EXTERNAL_ACT_SHA>'),C3_to_ACT=dict(from_commit=C,to_commit=None,complete_diff=None,sha256=None,bytes=None,status='MUST_ACQUIRE_COMPLETE_UNFILTERED_AFTER_EXTERNAL_ACT',command='git diff --no-ext-diff --no-textconv --no-renames --binary --full-index --no-color '+C+' <EXTERNAL_ACT_SHA>'),identity_commands=['git show --no-patch --format=%H%n%T%n%P <EXTERNAL_ACT_SHA>','git ls-tree -r <EXTERNAL_ACT_SHA>'],required_read='Read both complete unfiltered streams before owner segmentation, every public/traceability/control difference and exact changed clause/caller/data/condition evidence. Equal blobs/prior PASS do not discharge any gate. Current source/report formatting hashes cannot substitute for another stream.',single_payload_policy='One G payload freeze. No mandatory evidence-only child or recursive self-hash backfill. Coordinator supplies identity externally; exact diff output may be consumed from external freeze without mutating this payload.')
k.save('diff-and-freeze.json',dict(stage='B14-G',status='PREPARED_AWAIT_EXTERNAL_ACT',reproduction=repro,reviewed_candidate_tree=B['candidate_tree'],original_REPORT=B['fixed_originalREPORT'],PLAN=B['fixed_PLAN'],source_copy_manifest=G.as_posix()+'/copy-identities.json',current_reader_manifest=G.as_posix()+'/current-readers.json',actual_gates_pending=8,acceptance=False))
requests=[]
impact=k.obj(C,BP+'candidate-1/reverse-impact-packages.json');impact_by={p['accepted_owner']:p for p in impact['accepted_owner_packages']}
for rr in B['report_bindings']:
 owner=rr['owner'];name='actual-request-'+owner+'.json';scope=impact['full_R_B14'] if owner=='FULL' else impact_by[owner]['own_bounded_impact_analysis']
 if owner=='FULL':
  scope=copy.deepcopy(scope)
  scope['instructions']='Independently inspect all24 local contributions, complete current qualifications/effective conditions/root extensions and acceptance controls, all12 exact formal paths (five original and seven final, including the authorized WP16 original/final splash repair), positive/reverse unexecuted designs and source limits. Inspect the exact public-integrated ACT, complete unfiltered accepted-predecessor→ACT and C3→ACT differences. Author bookkeeping, equal blobs and candidate PASS do not supply actual acceptance.'
  scope['current_formal_scope']=dict(original=5,final=7,total=12)
  scope['candidate_status']='EIGHT_EXACT_C3_CANDIDATE_RECEIPTS_SUPPLIED_CANDIDATE_ONLY'
  scope['historical_scope_note']='The early immutable candidate-1 reverse-impact package described six final files at its own input; current G scope includes seven final targets. Frozen proposal bytes remain unchanged.'
 package=dict(run_id=B['run_id'],stage='B14-G',gate='FULL_R_B14_ACTUAL' if owner=='FULL' else 'SEPARATE_AFFECTED_'+owner+'_ACTUAL',status='PENDING_EXTERNAL_ACT_AND_INDEPENDENT_REVIEW',reviewer='R-B14' if owner=='FULL' else 'R-'+owner,requested_configuration=dict(model='gpt-6.1-sol',effort='ultra',service_tier='default=Standard',backend_effective='UNVERIFIED under approved Plan A',admission='Future task not dispatched; supplied requested profile is not an effective certificate'),exact_actual_identity=B['actual_identity'],accepted_public_predecessor=A,passed_C3=C,passed_C3_tree=B['candidate_tree'],all_applicable_candidate_receipts=B['report_bindings'],own_candidate_receipt=rr,full_original_controls=dict(original=con['fixed_original_findings'],qualified_acceptance=con['fixed_approved_acceptance'],full24_local=G.as_posix()+'/finding-registration.json',current_owner_controls=owners.get(owner,{}),precedence='Read complete current qualifications, effective second-review/root/extension conditions; historical raw prose cannot override.'),current_input_manifest=G.as_posix()+'/current-readers.json',current_hash_table=G.as_posix()+'/current-hashes.tsv',formal_targets12=B['formal_paths'],public_registration10=B['public_paths'],bounded_interface=scope,positive_reverse_unexecuted_designs=[fixed(rr['report_commit'],rr['directory']+'static-designs.json','INDEPENDENT_C3_UNEXECUTED_DESIGNS'),fixed(C,BP+'candidate-2/fix-response.json','AUTHOR_OVERLAYS_UNEXECUTED'),fixed(C,BP+'candidate-3/scope-proposal-1/static-designs.json','C3_UNEXECUTED')],complete_unfiltered_diffs=repro,mandatory_reviewer_actions=['Bind same exact externally supplied ACT SHA/tree/parents and compare all intended formal/public/reader identities.','Read both full unfiltered predecessor→ACT and C3→ACT streams including all current public/traceability/control differences before segmentation.','Inspect exact affected changed-clause/caller/data/condition evidence, qualified positive/reverse designs and protected owner clauses.','Provide independent pending quality disposition; only the independent exact reviewer may support NOT_AFFECTED with full comparison. Writer cannot certify it.','Keep all source/data/runtime/media/Demo/plugin/config limits; do not inherit candidate PASS or accept/close canonical findings.'],fresh_full_WP39_WP40_required=owner in ['FULL','B09'],B09_report_only_corrections=fixed(A,P+'batches/B09/acceptance-stage-1/report-corrections-successor.json','ACCEPTED_REPORT_ONLY_CORRECTIONS'),historical_full_C3_evidence_qualifications=fixed(B['report_bindings'][0]['report_commit'],BP+'review-round-3/findings.json','HISTORICAL_REPORT_ONLY_QUALIFICATION'),all_gates_required_before_AREG_C=['FULL','B02','B03','B04','B06','B07','B08','B09'],B10='Blocked until all actual gates plus B14-C, then all53 reads/eight writes/contract refreeze; later WP46 reverse B14 gates remain as applicable.',runtime_observations=0,proven_Demo_chains=0,behavior_vectors_executed=0,writer_actual_verdict=None,acceptance=False,dispatch=False)
 package['current_G_registration_inputs']=current_G_registration_inputs
 package['current_input_manifest_binding']=current((G/'current-readers.json').as_posix())
 package['current_hash_table_binding']=current((G/'current-hashes.tsv').as_posix())
 package['current_clause_bindings']=G.as_posix()+'/clause-location-bindings.json'
 package['pre_freeze_metadata_correction']=G.as_posix()+'/pre-freeze-navigation-correction.json'
 package['formal_scope_counts']=dict(original=5,final=7,total=12)
 k.save(name,package);requests.append(dict(owner=owner,path=G.as_posix()+'/'+name,status=package['status']))
k.save('gate-requests.json',dict(stage='B14-G',actual_identity=B['actual_identity'],separate_packages=requests,total=8,status='ALL_PENDING',dispatches=0,writer_actual_PASS=False,parent_C='NOT_PERFORMED'))
print('Refroze72 planned inputs,12 formal,10public,2whole catalogs; additional affected readers',len(additional),'current-hashes entries',len(identities),'actual packages8.')
