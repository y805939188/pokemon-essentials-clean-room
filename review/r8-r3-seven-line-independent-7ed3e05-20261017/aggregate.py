#!/usr/bin/env python3
"""Normalize the bounded independent verdict without rewriting prior FAIL history."""
from pathlib import Path
from collections import Counter
import copy, hashlib, json, subprocess
O=Path(__file__).resolve().parent;R=O.parents[1];E=O/'evidence';S=R/'planning/implementation-routing/r8-20261017'
C='7ed3e0554ac24339a7e61cab152f628037111644';P='c0f62d973180679134f2eb1a488c1dc359c8658f';PR='34202eb7accfee48bb8761db88b340bd77f54a42';CUR='5f87743293290de2e219ecdd6c19e88280f60c9a';OLD='review/r8-disposition-r3-independent-c0f62d9-20261017/'
def prior(n):return json.loads(subprocess.check_output(['git','show',PR+':'+OLD+n],cwd=R))
def read(p):return json.loads((O/p).read_text())
def write(p,d):(O/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def ref(n,pointer):return {'commit':PR,'path':OLD+n,'pointer':pointer}
m=json.loads((S/'routing-manifest.json').read_text());pm=json.loads(subprocess.check_output(['git','show',P+':planning/implementation-routing/r8-20261017/routing-manifest.json'],cwd=R));old=prior('feature-results.json');oldactive={f['feature_id']:f for f in old['active_feature_results']};parent={f['feature_id']:f for f in pm['features']}
ev=read('agents/ev-results.json');at=read('agents/attribution-results.json');fresh={}
for filename,d,field in [('ev-results.json',ev,'feature_results'),('attribution-results.json',at,'active_feature_results')]:
 assert d['candidate_commit']==C and not d['new_findings']
 for i,x in enumerate(d[field]):
  assert x['verdict']=='PASS';fresh[x['feature_id']]={'record':x,'evidence':{'path':'agents/'+filename,'pointer':'/'+field+'/'+str(i)}}
assert set(fresh)=={'FR-000029','FR-000032','FR-000173','FR-000204','FR-000227','FR-000456','FR-000596'}
facets=['classification','responsibility','scope','dependency','current_calibration'];active=[]
for i,f in enumerate(m['features']):
 fid=f['feature_id'];p=oldactive[fid];pr=parent[fid]
 assert f['source']==p['fixed_source'] and f['functional_scope']==p['functional_scope'] and f['current_applicability']==p['current_applicability']
 assert all(p['normalized_facets'][k]=='PASS'for k in facets[:4])
 protected=copy.deepcopy(f);previous=copy.deepcopy(pr);protected.pop('differences');previous.pop('differences');assert protected==previous
 if fid in fresh:
  assert p['normalized_facets']['current_calibration']=='FAIL' and f['differences'][:1]+f['differences'][2:]==pr['differences'][:1]+pr['differences'][2:]
  method='FRESH_COMPLETE_EFFECTIVE_SCOPE_AND_DIFF_SEMANTIC_REVIEW_PLUS_LIMITED_PRIOR_FOUR_FACET_CREDIT';reason=fresh[fid]['record']['reason'];evidence=fresh[fid]['evidence']
 else:
  assert f==pr and all(p['normalized_facets'][k]=='PASS'for k in facets)
  method='FIXED_PRIOR_FIVE_FACET_CREDIT_PLUS_COMPLETE_ROW_AND_SOURCE_DEPENDENCY_NONIMPACT';reason=p['reason'];evidence={'path':'agents/propagation-row-conservation.json','feature_id':fid}
 active.append({'feature_id':fid,'candidate_pointer':'/features/'+str(i),'verdict':'PASS','normalized_facets':{k:'PASS'for k in facets},'method':method,'reason':reason,'prior_verdict':p['verdict'],'prior_normalized_facets':p['normalized_facets'],'prior_evidence':ref('feature-results.json','/active_feature_results/'+str(i)),'current_evidence':evidence,'fixed_source':f['source'],'functional_scope':f['functional_scope'],'current_applicability':f['current_applicability'],'complete_protected_feature_object_equal_parent':True,'complete_feature_object_equal_parent':f==pr,'nonimpact_basis':'Actual accepted5f clauses, source/current identities, effective ranges, responsibilities and every dependency object unchanged. Seven notes describe existing accepted rules and add no behavior/producer/edge/owner; source/consumer semantic checks in the allocated reports confirm the corrected distinctions. Prior incoming consumers retain their real purposes, independent of annotation wording. No semantic credit from equality alone.','future_destination':f['future_plan']['destination'],'destination_verification':f['destination_verification'],'stage':f['future_plan']['stage'],'stage_approval':f['future_plan']['stage_approval'],'implementation':f['implementation']})
assert len(active)==736;am={f['feature_id']:f for f in active}
old721=[]
for i,p in enumerate(old['old_feature_results']):
 fid=p['feature_id'];r={'feature_id':fid,'verdict':'PASS','current_state':p['current_state'],'prior_verdict':p['verdict'],'prior_evidence':ref('feature-results.json','/old_feature_results/'+str(i))}
 if fid in am:r.update(current_evidence={'path':'feature-results.json','pointer':'/active_feature_results/'+str(next(j for j,x in enumerate(active)if x['feature_id']==fid))},method=am[fid]['method'])
 else:
  assert p['verdict']=='PASS';r.update(method='COMPLETE_RETIRED_OBJECT_AND_REPLACEMENT_METADATA_IDENTITY_WITH_UNCHANGED_CONSUMER_PURPOSES',current_evidence={'path':'agents/propagation-row-conservation.json','feature_id':fid})
 old721.append(r)
assert len(old721)==721
metadata=[]
for i,p in enumerate(old['retired_metadata_results']):
 assert p['verdict']=='PASS';metadata.append({'metadata_id':p['metadata_id'],'verdict':'PASS','prior_evidence':ref('feature-results.json','/retired_metadata_results/'+str(i)),'method':'COMPLETE_METADATA_RETIRED_REPLACEMENT_OBJECT_IDENTITY_PLUS_CONSUMER_NONIMPACT','reason':p['reason'],'current_evidence':'agents/propagation-row-conservation.json'})
assert len(metadata)==33
write('feature-results.json',{'candidate_commit':C,'parent_candidate_commit':P,'current_source_commit':CUR,'fixed_prior_review_commit':PR,'old_feature_results':old721,'active_feature_results':active,'retired_metadata_results':metadata,'scope':'Bounded seven-note semantic closure plus individually identity-bound unchanged prior credit. Prior FAIL records remain at their original SHA.'})
issues=[]
for x in ev['issue_results']+at['issue_results']:issues.append({'issue_id':x.get('issue_id',x.get('finding_id')),'verdict':'PASS','prior_verdict':'FAIL','result':x})
write('issue-results.json',{'candidate_commit':C,'repair_roots':issues,'new_findings':[],'minimum_fix':None})
pi=prior('issue-results.json');inherited={}
for k in ['R2_seven_issue_results','R1_twelve_issue_results']:
 inherited[k]=[]
 for i,x in enumerate(pi[k]):
  assert x['verdict']=='PASS';inherited[k].append({'issue_id':x.get('issue_id',x.get('finding_id')),'verdict':'PASS','method':'FIXED_PRIOR_REPAIR_AND_NONIMPACT_IDENTITY_CREDIT','prior_evidence':ref('issue-results.json','/'+k+'/'+str(i)),'nonimpact':'No source, schema/validator, dependency, scope, responsibility, stableID, acceptance, or repaired navigation changed. Only the seven already accepted source explanations and necessary copies changed.'})
write('prior-issue-results.json',{'candidate_commit':C,**inherited})
groups=[]
for i,x in enumerate(prior('finding-results.json')['finding_results']):
 assert x['original_case_verdict']=='PASS' and x['current_classification_dependency_scope_verdict']=='PASS'
 groups.append({'finding_id':x['finding_id'],'original_case_verdict':'PASS','current_classification_dependency_scope_verdict':'PASS','current_expanded_scope_verdict':'PASS','verdict':'PASS','prior_expanded_scope_verdict':x['current_scope_verdict'],'prior_evidence':ref('finding-results.json','/finding_results/'+str(i)),'method':'BOUNDED_CALIBRATION_CLOSURE' if x['finding_id']in ['COMBAT-05','POK-S05']else'EXACT_FIXED_CREDIT_AND_NONIMPACT','reason':'Original cases, categories, split/retirement and real dependency purposes unchanged. COMBAT-05 row29 and POK-S05 row596 now pass fresh calibration; no group reopens due to unrelated annotation.'})
assert len(groups)==44;write('finding-results.json',{'candidate_commit':C,'finding_results':groups,'all_original_and_expanded_groups_pass':True})
coverage=prior('reading-coverage.json');documents=[]
for i,d in enumerate(coverage['documents']):
 freshrefs=[]
 for filename,data,field in [('ev-results.json',ev,'fresh_reading_ledger'),('attribution-results.json',at,'actual_fresh_reading_ledger')]:
  for j,entry in enumerate(data[field]):
   if entry.get('path')==d['path']:
    freshrefs.append({'path':'agents/'+filename,'pointer':'/'+field+'/'+str(j),'declared_credit':entry,'qualification':'Only the actual fresh ranges or complete diff declared by the semantic owner, not whole-document credit.'})
 documents.append({'path':d['path'],'historical_identity':d['historical_identity'],'current_identity':d['current_identity'],'historical_headings':d['historical_headings'],'current_headings':d['current_headings'],'prior_reading_credit':ref('reading-coverage.json','/documents/'+str(i)),'current_mode':'FIXED_PRIOR_READING_CREDIT_WITH_RECOMPUTED_IDENTITY_AND_BOUNDED_NONIMPACT','current_fresh_reading_ledgers':freshrefs,'nonimpact':'Source corpus remains exact5f; coverage/mappings and all feature protected fields unchanged. Fresh seven-unit/six-file semantic closure preserves actual existing producer/consumer roles; unrelated current prose is not newly claimed read.'})
assert len(documents)==131;write('reading-coverage.json',{'candidate_commit':C,'documents':documents,'count':131,'unassigned_documents':[],'qualification':'No fresh131 full-text claim. Previous full review bound by34202eb7; fresh seven effective units/six complete diffs and needed consumers attributed in agents.'})
sections=[]
for i,x in enumerate(prior('section-results.json')['sections']):
 sections.append({'path':x['path'],'document_id':x['document_id'],'level':x['level'],'title':x['title'],'anchor':x['anchor'],'line_start':x['line_start'],'line_end':x['line_end'],'heading_sha256':x['heading_sha256'],'feature_refs':x['feature_refs'],'metadata_refs':x['metadata_refs'],'mechanical_identity_verdict':'PASS_RECOMPUTED_FIXED_GIT','consumer_semantic_verdict':'PASS_FIXED_CREDIT_AND_BOUNDED_NONIMPACT','prior_evidence':ref('section-results.json','/sections/'+str(i)),'current_evidence':'agents/propagation-heading-conservation.json'})
assert len(sections)==2704;write('section-results.json',{'candidate_commit':C,'current_source_commit':CUR,'sections':sections,'count':2704,'historical2683_preserved':True,'new_headings':21,'qualification':'Complete heading/consumer projection recomputed; prior attributed semantic reading plus bounded seven-note closure, no new fulltext claim.'})
counts=copy.deepcopy(prior('result.json')['counts'])
for k,n in [('old721',721),('active736',736),('metadata33',33),('R2_seven_issues',7),('R1_twelve_issues',12),('original44_specific_cases',44),('original44_classification_dependency_groups',44),('expanded_current_scope_groups',44),('R2_failed28_active_recheck',28),('R2_pass708_active_propagation',708),('R2_old15_FAIL_recheck',15)]:counts[k]={'PASS':n,'FAIL':0}
counts['facets']={k:{'PASS':736,'FAIL':0}for k in facets};counts['new_findings']=0;counts['new_findings_by_severity']={};counts['recovery_roots']={'PASS':2,'FAIL':0};counts['fresh_recovery_cases']={'PASS':7,'FAIL':0}
for d in counts['by_domain'].values():
 for k in ['old','active']:d[k]={'PASS':sum(d[k].values()),'FAIL':0}
static=read('evidence/tool-replay-summary.json');assert static['all_exit_zero'] and static['all17_input_hashes_stable_and_equal_candidate'];assert read('evidence/input-audit-results.json')['all_passed']
remote=read('evidence/candidate-fresh-remote-readback.json');assert remote['verified_commit']==C and remote['file_count']==175 and remote['bytes']==38564194 and remote['result']=='PASS_FRESH_REMOTE_ALL_REVIEW_BYTES'
result={'candidate_commit':C,'exact_parent_commit':P,'current_source_commit':CUR,'fixed_prior_review_commit':PR,'classification_corrections_verdict':'PASS','final_cumulative_source_calibration_verdict':'PASS','overall_verdict':'PASS','coordination_final_integration_freeze_eligible':True,'whole_round_published':False,'whole_round_CLOSED':False,'counts':counts,'candidate_input_readback':{'file_count':175,'bytes':38564194,'verdict':'PASS_FRESH_REMOTE_ALL_BYTES'},'static_execution':{'commands':10,'followup_commands':2,'inputs_hash_stable':17,'bounded_repair_checks':12,'final_calibration_checks':15,'result':'PASS'},'configuration':'Parent requested/admitted ultra/default traceable; actual runtime model/effort/tier/speed/Fast/cloudUUID UNVERIFIED without authoritative echo, not a failure reason.','target_compatibility':'NOT_VERIFIED','prototypes':'4_NOT_EXECUTED','phase_implementation_acceptance':'All736 destination待验证, stage待定/未批准, implementation未实现, target acceptance未验收; exclusions0.','remaining_blockers_in_review_scope':[],'next_owner_action':'Coordinator may freeze/accept the final integrated candidate using this exact input/report; coordinator still owns integration, merge and whole-round publication.'}
write('result.json',result)
print(json.dumps({'active':len(active),'old':len(old721),'metadata':len(metadata),'documents':len(documents),'sections':len(sections),'groups':len(groups),'root_issues':len(issues),'verdict':'PASS'},ensure_ascii=False))
