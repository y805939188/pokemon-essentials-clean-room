#!/usr/bin/env python3
"""Reconcile attributed independent decisions, not author classifications."""
from pathlib import Path
import collections,hashlib,json,re,subprocess
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];E=OUT/'evidence';A=OUT/'agents'
NEW='5666b7b912e2fb79b5119283ee6a37401a7071db';OLD='d62b41f4d620e50bb04c80a7505374bd284d8210';PRIOR='a0352c7fba38391afc535525988245701d5ce202'
SRC='planning/implementation-routing/r8-20261017';FORMAL='deliverables/final-specification-set/'
def load(p):return json.loads(p.read_text())
def save(n,d):(OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def jb(c,p):return json.loads(subprocess.check_output(['git','show',c+':'+p],cwd=ROOT))
def verdict(x):return x.get('verdict',x.get('new_verdict',x.get('overall_verdict')))
def idof(x):return x.get('finding_id',x.get('id'))
def owner(path):
 rel=path.removeprefix(FORMAL);group=rel.split('/')[0]
 if group=='test-catalog':
  name=rel.split('/')[-1]
  if name=='README.md':return'demo'
  if name.startswith('combat-requirements'):return'combat'
  if name.startswith('creature-rpg'):return'creature'
  if name.startswith('generic-kernel'):return'kernel'
  if name.startswith('pokemon-rules'):return'pokemon'
  if name.startswith(('engine-overworld','user-interface')):return'world-ui'
  if name.startswith('demo-dx'):return'demo'
  raise ValueError(path)
 return {'combat-requirements':'combat','creature-rpg':'creature','generic-kernel':'kernel','pokemon-rules':'pokemon','engine-overworld':'world-ui','user-interface':'world-ui','demo-dx':'demo'}.get(group,'demo')
m=load(ROOT/SRC/'routing-manifest.json');coverage=load(ROOT/SRC/'section-coverage.json');formal=load(E/'formal-coverage.json')
old=jb(OLD,SRC+'/routing-manifest.json');old_by={f['feature_id']:f for f in old['features']};active_by={f['feature_id']:f for f in m['features']};retired_by={f['feature_id']:f for f in m['retired_features']}
prior=jb(PRIOR,'review/r8-disposition-independent-d62b41f-20261017/feature-results.json');prior_by={f['feature_id']:f for f in prior['features']}
prior_findings=jb(PRIOR,'review/r8-disposition-independent-d62b41f-20261017/findings.json')['findings'];prior_findings_by={x['id']:x for x in prior_findings}
old_results=[];active_results=[];metadata_results=[];finding_results=[];new_findings=[];domains={};readers={};catalog=[]
for domain in ['combat','creature','kernel','pokemon','world-ui','demo']:
 data=load(A/(domain+'-results.json'));domains[domain]=data
 for field,dest in [('old_feature_results',old_results),('active_feature_results',active_results),('finding_results',finding_results)]:
  for index,x in enumerate(data[field]):
   record=dict(x);record['verdict']=verdict(x);record['reviewer']=domain;record['review_evidence']=f'agents/{domain}-results.json#/{field}/{index}';dest.append(record)
 for index,x in enumerate(data['retired_metadata_results']):
  mid=x.get('metadata_id',x.get('unit_id')if x.get('unit_type')=='metadata_record'else None)
  if mid:
   metadata_results.append(dict(x)|{'metadata_id':mid,'verdict':verdict(x),'reviewer':domain,'review_evidence':f'agents/{domain}-results.json#/retired_metadata_results/{index}'})
 for index,x in enumerate(data['reading_ledger']):
  path=x['path']
  if owner(path)==domain:
   assert path not in readers,path
   readers[path]={'reader':domain,'ledger':x,'review_evidence':f'agents/{domain}-results.json#/reading_ledger/{index}'}
 for x in data.get('new_findings',[]):new_findings.append(dict(x)|{'id':idof(x),'title':x.get('title','7项持久/战斗/音频依赖仍遗漏或误接'),'verdict':'FAIL','reviewer':domain,'review_evidence':f'agents/{domain}-results.json#/new_findings'})
 for field in ['catalog_section_results','catalog_consumer_navigation_results']:
  for x in data.get(field,[]):catalog.append({'reviewer':domain,**x})
root=load(OUT/'root-findings.json');finding_results.extend(dict(x)|{'reviewer':'root','review_evidence':'root-findings.json#/finding_results'}for x in root['finding_results']);new_findings.extend(dict(x)|{'reviewer':'root','review_evidence':'root-findings.json#/new_findings'}for x in root['new_findings'])
def unique(rows,key,expected):
 ids=[x[key]for x in rows];assert len(ids)==len(set(ids)),[x for x,n in collections.Counter(ids).items()if n!=1]
 assert set(ids)==set(expected),{'missing':sorted(set(expected)-set(ids)),'extra':sorted(set(ids)-set(expected))}
unique(old_results,'feature_id',old_by);unique(active_results,'feature_id',active_by);unique(metadata_results,'metadata_id',{x['metadata_id']for x in m['metadata_records']})
unique(finding_results,'finding_id',prior_findings_by)
assert len(old_results)==721 and len(active_results)==736 and len(metadata_results)==32 and len(finding_results)==44
all_prior_nonpass=[]
for row in old_results:
 fid=row['feature_id'];old_verdict=prior_by[fid]['verdict'];decl=row.get('prior_verdict',row.get('old_verdict'));assert decl==old_verdict,(fid,decl,old_verdict)
 assert row['verdict']in ['PASS','FAIL','待查'];row['prior_verdict']=old_verdict;row['current_state']='active'if fid in active_by else'retired'
 current=active_by.get(fid,retired_by.get(fid));assert current['source']==old_by[fid]['source']
 if fid in retired_by:assert {k:v for k,v in current.items()if k!='retirement'}==old_by[fid]
 row['fixed_source']=current['source'];row['candidate_pointer']=('/features/'+str(m['features'].index(current)))if fid in active_by else('/retired_features/'+str(m['retired_features'].index(current)))
 row['identity_preserved']='PASS'
 if old_verdict!='PASS':all_prior_nonpass.append(row)
for row in active_results:
 f=active_by[row['feature_id']];row.update({'is_new':row['feature_id']not in old_by,'fixed_source':f['source'],'functional_scope':f['functional_scope'],'current_applicability':f['current_applicability'],'candidate_pointer':'/features/'+str(m['features'].index(f))})
 assert row['verdict']in ['PASS','FAIL','待查']
for row in metadata_results:
 r=next(x for x in m['metadata_records']if x['metadata_id']==row['metadata_id']);row['fixed_source']=r['source'];row['candidate_pointer']='/metadata_records/'+str(m['metadata_records'].index(r))
for row in finding_results:
 original=prior_findings_by[row['finding_id']];row['original_title']=original['title'];row['original_severity']=original['severity'];row['prior_evidence_commit']=PRIOR
 assert row['verdict']in ['PASS','FAIL','待查']
save('feature-results.json',{'candidate_commit':NEW,'prior_review_commit':PRIOR,'old_feature_results':sorted(old_results,key=lambda x:x['feature_id']),'active_feature_results':sorted(active_results,key=lambda x:x['feature_id']),'retired_metadata_results':sorted(metadata_results,key=lambda x:x['metadata_id']),'scope':'Feature verdict is own classification/dependency/current disposition; incoming catalog and common readable-view defects have separate findings, not implicit failures of every referenced feature.'})
save('finding-results.json',{'candidate_commit':NEW,'original_finding_count':44,'finding_results':sorted(finding_results,key=lambda x:x['finding_id']),'qualification':'PASS may close the original facet while separately identified new propagation remains; all exact cases and reasons preserved in linked domain results.'})
# Deduplicate the reverse-catalog issue independently reported by two domain owners.
reverse=[x for x in new_findings if x['id']in ['WU-R1-N01','POK-R1-CATALOG-002']]
assert len(reverse)==2
new_findings=[x for x in new_findings if x not in reverse]
new_findings.append({'id':'R1-CATALOG-WP-COLLISION','severity':'P3','verdict':'FAIL','title':'反向Pokémon目录仍以同WP编号误连Fishing/Slot/Mining','old_finding_roots':['WORLD-CATALOG-F01'],'candidate_file':SRC+'/section-coverage.json','candidate_pointers':[f'/sections/{i}/feature_refs'for i in range(2277,2293)],'corroborating_reviews':reverse,'why':'目录明确对应Berry/Voltorb/Lottery等规则正文，16节却连不同体系Fishing/Slot/Mining；两个领域独立核同一根因，合并计一项。','required_fix':'按目录真实对应正文/具名后继修复消费者，不改来源、不逐向量新增ID。'})
new_findings.sort(key=lambda x:(x['severity'],x['id']))
save('findings.json',{'candidate_commit':NEW,'findings':new_findings,'count':len(new_findings),'counts_by_severity':dict(collections.Counter(x['severity']for x in new_findings)),'deduplication':'WU-R1-N01 and POK-R1-CATALOG-002 are one reverse-WP-collision root. Original44 groups are separately reconciled; groups/cases/feature failures are different denominators.'})
assert set(readers)=={x['path']for x in formal['documents']},{'missing':sorted({x['path']for x in formal['documents']}-set(readers)),'extra':sorted(set(readers)-{x['path']for x in formal['documents']})}
reading=[]
for doc in formal['documents']:
 path=doc['path'];reader=readers[path];old_read=jb(PRIOR,'review/r8-disposition-independent-d62b41f-20261017/reading-coverage.json');prior_doc=next(x for x in old_read['documents']if x['path']==path)
 assert prior_doc['sha256']==doc['source']['sha256']
 reading.append({'path':path,'source_identity':doc['source'],'current_identity':doc['current'],'source_lines':doc['source_lines'],'current_lines':doc['current_lines'],'source_headings':doc['source_headings'],'source_changed_at_current':doc['current_changed'],'prior_full_reading_identity_match':True,'prior_reading_commit':PRIOR,'prior_full_reading_record':prior_doc,'current_review':reader,'qualification':'Prior full reading of identical bytes is retained only for unaffected facets; new/changed/nonPASS/same-root facets have attributed fresh source-unit review. This is not131 fresh whole-file reads.'})
save('reading-coverage.json',{'documents':reading,'count':len(reading),'source_headings':formal['source_heading_count'],'current_headings':formal['current_heading_count'],'unassigned_documents':[],'unreviewed_known_nonpass_ids':[],'current_changed_document_readers':['kernel','pokemon'],'reading_mode':'Full prior identity-bound reading credit + complete revised-row reconciliation + targeted fresh reading of affected complete source units and necessary consumers. See each ledger for actual fresh ranges; no current908 credit from B8 worktree.'})
sections=[]
for i,section in enumerate(coverage['sections']):
 path=section['path'];reviewer=readers[path];sections.append({'section_index':i,'candidate_pointer':f'/sections/{i}','source_commit':m['source_baseline']['commit'],'current_snapshot':m['current_snapshot']['commit'],**section,'identity_and_heading_fields':'PASS','attributed_semantic_review':reviewer['reader'],'reading_evidence':reviewer['review_evidence'],'review_qualification':'Review covers heading and source body via documented current/prior ranges; exact metadata/consumer defects are reported separately in findings. Structural coverage is not automatic semantic PASS.'})
save('section-results.json',{'candidate_commit':NEW,'sections':sections,'count':len(sections),'catalog_review_details':catalog,'scope':'All actual formal headings; each metadata/case outcome stays in the attributed domain or root findings. No heading-count-only acceptance.'})
counts={'documents':len(reading),'source_bytes':sum(x['source_identity']['bytes']for x in reading),'current_bytes':sum(x['current_identity']['bytes']for x in reading),'source_lines':sum(x['source_lines']for x in reading),'current_lines':sum(x['current_lines']for x in reading),'source_headings':len(sections),'old_features':dict(collections.Counter(x['verdict']for x in old_results)),'active_features':dict(collections.Counter(x['verdict']for x in active_results)),'retired_metadata':dict(collections.Counter(x['verdict']for x in metadata_results)),'original_finding_groups':dict(collections.Counter(x['verdict']for x in finding_results)),'old_nonpass_recheck':dict(collections.Counter(x['verdict']for x in all_prior_nonpass)),'old_pass_propagation':dict(collections.Counter(x['verdict']for x in old_results if x['prior_verdict']=='PASS')),'new_feature_verdicts':dict(collections.Counter(x['verdict']for x in active_results if x['is_new'])),'new_findings_by_severity':dict(collections.Counter(x['severity']for x in new_findings)),'new_findings':len(new_findings),'by_domain':{d:{'owned_documents':sum(owner(x['path'])==d for x in formal['documents']),'old':dict(collections.Counter(x['verdict']for x in old_results if x['reviewer']==d)),'active':dict(collections.Counter(x['verdict']for x in active_results if x['reviewer']==d))}for d in domains}}
assert sum(counts['old_nonpass_recheck'].values())==273 and sum(counts['old_pass_propagation'].values())==448
assert sum(counts['new_feature_verdicts'].values())==47
counts['no_unreviewed_row_claim']=not any(x['verdict']=='待查'for x in old_results+active_results+metadata_results+finding_results)
save('result.json',{'candidate_commit':NEW,'verdict':'FAIL','scope':'Fixed-source R1 rough routing only; not final R8 remediation, target compatibility, implementation or acceptance. Execution configuration remains UNVERIFIED.','counts':counts,'root_old_tool_groups':'PASS','tool_validation':'PASS_TOOL_VALIDATION_ONLY','accepted_source_rows':17,'pending_bound_rows':174,'no_prototypes_executed':True,'remaining_gates':['Repair listed routing/dependency/metadata/view defects and re-review exact successor SHA','Authoritative actual ultra/default execution telemetry or qualification confirmation unavailable','User scope/phase decisions','Fixed-target capture/items/escape/in-battle-growth behavioral prototypes','Remaining upstream accepted payload backfill and final cumulative independent acceptance']})
print(json.dumps(counts,ensure_ascii=False))
