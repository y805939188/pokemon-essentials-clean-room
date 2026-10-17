#!/usr/bin/env python3
"""Reconcile attributed semantic verdicts; never infer classification from keywords."""
from pathlib import Path
from collections import Counter
import json,subprocess,hashlib
O=Path(__file__).resolve().parent; R=O.parents[1]; A=O/'agents'; E=O/'evidence'
C='a32873d2860b15d9f5e27727db8f131f4ec433b6'; P='8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8'; PC='5666b7b912e2fb79b5119283ee6a37401a7071db'; D='d62b41f4d620e50bb04c80a7505374bd284d8210'; I='a0352c7fba38391afc535525988245701d5ce202'; CURRENT='908273093e1f6b27fc58249417675dd62d146224'
S='planning/implementation-routing/r8-20261017'; PRE='review/r8-disposition-r1-independent-5666b7b-20261017'; INIT='review/r8-disposition-independent-d62b41f-20261017'
def load(p):return json.loads(p.read_text())
def jb(c,p):return json.loads(subprocess.check_output(['git','show',c+':'+p],cwd=R))
def save(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def v(x):return x.get('verdict',x.get('new_verdict'))
def ident(x):return x.get('id',x.get('finding_id',x.get('issue_id')))
def owner(path):
 rel=path.removeprefix('deliverables/final-specification-set/');group=rel.split('/')[0];name=rel.split('/')[-1]
 if group=='test-catalog':
  if name.startswith('combat-requirements'):return 'combat'
  if name.startswith('creature-rpg'):return 'creature'
  if name.startswith('generic-kernel'):return 'kernel'
  if name.startswith(('pokemon-rules','engine-overworld','user-interface')):return 'pokemon-world'
  return 'demo'
 return {'combat-requirements':'combat','creature-rpg':'creature','generic-kernel':'kernel','pokemon-rules':'pokemon-world','engine-overworld':'pokemon-world','user-interface':'pokemon-world','demo-dx':'demo'}.get(group,'demo')
m=jb(C,S+'/routing-manifest.json'); cov=jb(C,S+'/section-coverage.json'); formal=load(E/'formal-coverage.json')
oldm=jb(D,S+'/routing-manifest.json'); oldids={x['feature_id'] for x in oldm['features']}; active={x['feature_id']:x for x in m['features']}; retired={x['feature_id']:x for x in m['retired_features']}; meta={x['metadata_id']:x for x in m['metadata_records']}
r1=jb(P,PRE+'/feature-results.json'); prev={x['feature_id']:x for x in r1['old_feature_results']}; prevactive={x['feature_id']:x for x in r1['active_feature_results']}; prevmeta={x['metadata_id']:x for x in r1['retired_metadata_results']}; prevgroups={x['finding_id']:x for x in jb(P,PRE+'/finding-results.json')['finding_results']}; previssues={x['id']:x for x in jb(P,PRE+'/findings.json')['findings']}
originalgroups={x['id']:x for x in jb(I,INIT+'/findings.json')['findings']}; oldreading={x['path']:x for x in jb(P,PRE+'/reading-coverage.json')['documents']}
oldrows=[];actrows=[];metarows=[];groups=[];issues=[];findings=[];readers={};domains={}; catalogs=[]
for domain in ['combat','creature','demo','kernel','pokemon-world','source']:
 data=load(A/(domain+'-results.json'));domains[domain]=data
 assert data['candidate_commit']==C
 for field,dest in [('old_feature_results',oldrows),('active_feature_results',actrows),('issue_results',issues),('original_group_results',groups)]:
  for i,x in enumerate(data[field]):
   z=dict(x);z.update(verdict=v(x),reviewer=domain,review_evidence=f'agents/{domain}-results.json#/{field}/{i}');dest.append(z)
 for i,x in enumerate(data['retired_metadata_results']):
  if x.get('unit_type') and not x['unit_type'].startswith('metadata'):continue
  z=dict(x);z.update(verdict=v(x),reviewer=domain,review_evidence=f'agents/{domain}-results.json#/retired_metadata_results/{i}');metarows.append(z)
 if domain!='source':
  for i,x in enumerate(data['reading_ledger']):
   path=x['path']
   if owner(path)==domain:
    assert path not in readers,path
    readers[path]={'reader':domain,'ledger':x,'review_evidence':f'agents/{domain}-results.json#/reading_ledger/{i}'}
 for i,x in enumerate(data['new_findings']):findings.append(dict(x)|{'id':ident(x),'verdict':'FAIL','reviewer':domain,'review_evidence':f'agents/{domain}-results.json#/new_findings/{i}'})
 for field in ['catalog_section_results','catalog_consumer_results','catalog_results','section_metadata_results']:
  for i,x in enumerate(data.get(field,[])):catalogs.append({'reviewer':domain,'review_evidence':f'agents/{domain}-results.json#/{field}/{i}',**x})
# Root common-tool original facets were fixed; newly introduced current-source rules fail.
for gid,why,refs in [('ROOT-TOOL-01','Original historical unresolved/blank-heading checks pass; newly added current coverage schema/backfill and exemption fail.', ['SOURCE-R2-002','SOURCE-R2-003']),('ROOT-TOOL-02','Original known batch/event and source-range checks pass; later receipt-current content identity can bypass acceptance.', ['SOURCE-R2-001'])]:
 groups.append({'finding_id':gid,'verdict':'FAIL','original_case_verdict':'PASS','current_scope_verdict':'FAIL','r1_verdict':prevgroups[gid]['verdict'],'reviewer':'root','reason':why,'finding_refs':refs,'review_evidence':'agents/source-results.json#/new_findings','original_case_evidence':'evidence/tool-replay-summary.json'})
issues.append({'issue_id':'ROOT-R1-VIEW-01','r1_verdict':'FAIL','verdict':'PASS','reviewer':'root','reason':'All36 explicit parents,39 child anchors/39edges, original29 subset and new67→769 are present, unique and reachable in the scope column; all736 rows and33meta/8cells independently projected.','cases':'evidence/independent-view-projection.json','review_evidence':'evidence/independent-view-projection.json'})
def exact(rows,key,expected):
 ids=[x[key]for x in rows];assert len(ids)==len(set(ids)),Counter(ids);assert set(ids)==set(expected),{'missing':sorted(set(expected)-set(ids)),'extra':sorted(set(ids)-set(expected))}
exact(oldrows,'feature_id',oldids);exact(actrows,'feature_id',active);exact(metarows,'metadata_id',meta);exact(groups,'finding_id',originalgroups);exact(issues,'issue_id',previssues);assert len(oldrows)==721 and len(actrows)==736 and len(metarows)==33 and len(groups)==44 and len(issues)==12
for x in oldrows:
 fid=x['feature_id'];assert x['r1_verdict']==prev[fid]['verdict'],fid; current=active.get(fid,retired.get(fid));x.update(fixed_source=current['source'],identity_preserved='PASS',current_state='active'if fid in active else 'retired',candidate_pointer=('/features/'+str(m['features'].index(current)))if fid in active else('/retired_features/'+str(m['retired_features'].index(current))))
for x in actrows:
 fid=x['feature_id']; f=active[fid];assert x['r1_verdict']==(prevactive[fid]['verdict']if fid in prevactive else 'NEW'),(fid,x['r1_verdict'])
 x.update(fixed_source=f['source'],functional_scope=f['functional_scope'],current_applicability=f['current_applicability'],candidate_pointer='/features/'+str(m['features'].index(f)),classification_verdict='PASS',dependency_verdict=x.get('dependency_verdict','FAIL'if x['verdict']=='FAIL'else'PASS'),is_original721=fid in oldids,is_R1_new=fid not in oldids and fid in prevactive,is_R2_new=fid not in prevactive)
for x in metarows:
 f=meta[x['metadata_id']];x.update(fixed_source=f['source'],candidate_pointer='/metadata_records/'+str(m['metadata_records'].index(f)))
for x in groups:
 gid=x['finding_id'];x['r1_verdict']=prevgroups[gid]['verdict'];x['original_case_verdict']=x.get('original_case_verdict',v(x));x['current_scope_verdict']=x.get('current_scope_verdict',v(x));x['verdict']=x['current_scope_verdict'];x.update(original_title=originalgroups[gid]['title'],original_severity=originalgroups[gid]['severity'])
 # COMBAT domain preserved original-case PASS separately in final output.
for x in oldrows+actrows+metarows+issues+groups:assert x['verdict']in ['PASS','FAIL','待查'],x
assert {x['path']for x in formal['documents']}==set(readers)
reading=[]
for d in formal['documents']:
 path=d['path'];p=oldreading[path];assert d['source']==p['source_identity'] and d['current']==p['current_identity'],path
 reading.append({'path':path,'source_identity':d['source'],'current_identity':d['current'],'source_lines':d['source_lines'],'current_lines':d['current_lines'],'headings':d['headings'],'r1_identity_and_semantic_credit':p,'r2_review':readers[path],'qualification':'Full identity-bound prior read credit only for unchanged and unaffected facets. R2 new/nonPASS/same-root units and consumers have fresh ranges in attributed ledgers; no claim of131 freshly read complete files.'})
sections=[]
for i,s in enumerate(cov['sections']):
 rd=readers[s['path']];sections.append({'section_index':i,'candidate_pointer':f'/sections/{i}',**s,'identity_and_heading_verdict':'PASS','semantic_review_owner':rd['reader'],'reading_evidence':rd['review_evidence'],'qualification':'Source body review uses inherited/full and fresh affected-unit ranges. Semantic dependency defects stay linked to exact feature findings; coverage count alone is not PASS.'})
counts={'documents':len(reading),'historical_headings':len(sections),'current908_headings':formal['current908_headings'],'prepared_only_headings':2704,'source_bytes':formal['source_bytes'],'current_bytes':formal['current_bytes'],'old_features':dict(Counter(x['verdict']for x in oldrows)),'active_features':dict(Counter(x['verdict']for x in actrows)),'classification_facets':dict(Counter(x['classification_verdict']for x in actrows)),'metadata':dict(Counter(x['verdict']for x in metarows)),'original_case_groups':dict(Counter(x['original_case_verdict']for x in groups)),'current_scope_groups':dict(Counter(x['current_scope_verdict']for x in groups)),'r1_remaining_issues':dict(Counter(x['verdict']for x in issues)),'r1_old28_recheck':dict(Counter(x['verdict']for x in oldrows if x['r1_verdict']=='FAIL')),'r1_old693_propagation':dict(Counter(x['verdict']for x in oldrows if x['r1_verdict']=='PASS')),'r1_47_new_active':dict(Counter(x['verdict']for x in actrows if x['is_R1_new'])),'r2_new769':dict(Counter(x['verdict']for x in actrows if x['is_R2_new'])),'r1_18_failed_active_survivors':dict(Counter(x['verdict']for x in actrows if x['feature_id']in prevactive and prevactive[x['feature_id']]['verdict']=='FAIL')),'r1_18_failed_active_disposition':dict(Counter(x['verdict']for x in oldrows if x['feature_id']in prevactive and prevactive[x['feature_id']]['verdict']=='FAIL')),'r1_10_failed_metadata':dict(Counter(x['verdict']for x in metarows if x['metadata_id']in prevmeta and prevmeta[x['metadata_id']]['verdict']=='FAIL')),'r1_22_pass_metadata':dict(Counter(x['verdict']for x in metarows if x['metadata_id']in prevmeta and prevmeta[x['metadata_id']]['verdict']=='PASS')),'r1_nine_failed_original_groups':dict(Counter(x['original_case_verdict']for x in groups if x['r1_verdict']=='FAIL')),'findings':len(findings),'findings_by_severity':dict(Counter(x['severity']for x in findings)),'by_domain':{d:{'documents':sum(owner(x['path'])==d for x in reading),'old':dict(Counter(x['verdict']for x in oldrows if x['reviewer']==d)),'active':dict(Counter(x['verdict']for x in actrows if x['reviewer']==d))}for d in domains if d!='source'}}
assert counts['old_features']=={'PASS':706,'FAIL':15} and counts['active_features']=={'PASS':708,'FAIL':28},counts
assert counts['metadata']=={'PASS':33} and counts['classification_facets']=={'PASS':736}
assert counts['original_case_groups']=={'PASS':43,'FAIL':1} and counts['current_scope_groups']=={'PASS':39,'FAIL':5},counts
assert counts['r1_remaining_issues']=={'PASS':11,'FAIL':1}
save('feature-results.json',{'candidate_commit':C,'r1_review_commit':P,'old_feature_results':sorted(oldrows,key=lambda x:x['feature_id']),'active_feature_results':sorted(actrows,key=lambda x:x['feature_id']),'retired_metadata_results':sorted(metarows,key=lambda x:x['metadata_id']),'qualification':'Every row gets overall verdict. Classification/responsibility/scope facets can pass while wrong outgoing dependency makes overallFAIL. Incoming wrong references do not fail target rows.'})
save('finding-results.json',{'candidate_commit':C,'finding_results':sorted(groups,key=lambda x:x['finding_id']),'counts':{'original_cases':counts['original_case_groups'],'current_scope':counts['current_scope_groups']},'qualification':'Historical reports unchanged. Original specific-case repair and expanded same-root current-scope verdict are separate; top-level verdict is current_scope.'})
save('issue-results.json',{'candidate_commit':C,'issue_results':sorted(issues,key=lambda x:x['issue_id']),'count':12})
save('findings.json',{'candidate_commit':C,'findings':sorted(findings,key=lambda x:(x['severity'],x['id'])),'count':len(findings),'counts_by_severity':counts['findings_by_severity'],'qualification':'Two creature findings split remaining3cases from additional2cases; one root same dependency family. Counts are issue groups, not feature rows. No duplicate cross-domain counting.'})
save('reading-coverage.json',{'candidate_commit':C,'documents':reading,'count':131,'unassigned_documents':[],'reading_mode':'Inherited131 exact-identity full semantic records + complete changes and same-root effective-unit/consumer rereads. Additional38 source-diff documents and21 proposed heading mappings are separately attributed; no new131-full-reread claim.','source_preparation_evidence':'agents/source-results.json#/reading_ledger'})
save('section-results.json',{'candidate_commit':C,'sections':sections,'count':len(sections),'catalog_and_metadata_results':catalogs,'prepared_21_heading_results':domains['source']['source_heading_results'],'prepared_qualification':'21 proposed only, never counted in current2683.'})
save('result.json',{'candidate_commit':C,'verdict':'FAIL','scope':'Fixed908 R2 rough routing and actual future-tool code only; not final cumulative source or behavioral acceptance.','counts':counts,'current_snapshot':CURRENT,'current_events':2,'accepted_bound_rows':17,'pending_bound_rows':174,'source_183_original_bindings':'Preserved; later split expansion191 total bound, not183 closed.','actual_execution_configuration':'UNVERIFIED; no authoritative echo for actual model/ultra/default/Fast or cloud UUID.','static_command_stage':'r2-fixed-source seven commands exit0; no semantic acceptance transfer.','future5_and2704':'NOT_EXECUTED_AWAITING_U04','remaining_gates':['Repair28 dependency rows and3 future-tool defects; freeze successor and independently re-review','U04 formal receipt pending user confirmation/publication, do not manufacture','Apply accepted cumulative source, backfill and independently review actual full headings and binding tests','All destination compatibility and four behavioral prototypes remain pending','User scope/phase decisions remain pending','Authoritative execution configuration telemetry remains unavailable']})
print(json.dumps(counts,ensure_ascii=False))
