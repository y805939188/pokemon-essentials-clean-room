"""Read-only independent R3 JSON/Git audit; writes only pokemon-world review outputs."""
import collections, copy, difflib, hashlib, json, re, subprocess, unicodedata
from pathlib import Path

C = 'c0f62d973180679134f2eb1a488c1dc359c8658f'
CUR = '5f87743293290de2e219ecdd6c19e88280f60c9a'
R2 = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
RR = '0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add'
OLD = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
B = 'planning/implementation-routing/r8-20261017/'
RP = 'review/r8-disposition-r2-independent-a32873d-20261017/'
OUT = Path(__file__).parent
cache = {}
def sha(b): return hashlib.sha256(b).hexdigest()
def git(c, p):
    if (c,p) not in cache: cache[c,p] = subprocess.check_output(['git','show',c+':'+p])
    return cache[c,p]
def read(c,p): return json.loads(git(c,p))
def ident(c,p):
    b=git(c,p)
    return dict(commit=c,path=p,bytes=len(b),sha256=sha(b),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),lines=len(b.splitlines()))
def body(c,p,ranges):
    ls=git(c,p).splitlines(keepends=True)
    return b''.join(b''.join(ls[a-1:b]) for a,b in ranges)
def merge(rs):
    result=[]
    for a,b in sorted(rs):
        if result and a<=result[-1][1]+1: result[-1][1]=max(result[-1][1],b)
        else: result.append([a,b])
    return result
def pointer(rows,key,value): return '/'+str(next(i for i,x in enumerate(rows) if x[key]==value))

m=read(C,B+'routing-manifest.json'); prev=read(R2,B+'routing-manifest.json'); orig=read(OLD,B+'routing-manifest.json')
f={x['feature_id']:x for x in m['features']}; pf={x['feature_id']:x for x in prev['features']}; of={x['feature_id']:x for x in orig['features']}
ret={x['feature_id']:x for x in m['retired_features']}; meta={x['metadata_id']:x for x in m['metadata_records']}
r2=read(RR,RP+'agents/pokemon-world-results.json'); rg=read(RR,RP+'feature-results.json')
own={x['feature_id'] for x in r2['active_feature_results']}; oldids={x['feature_id'] for x in r2['old_feature_results']}; mids={x['metadata_id'] for x in r2['retired_metadata_results']}; docs={x['path'] for x in r2['reading_ledger']}
pa={x['feature_id']:x for x in r2['active_feature_results']}; po={x['feature_id']:x for x in r2['old_feature_results']}
assert (len(own),len(oldids),len(mids),len(docs))==(353,333,12,62)
assert own=={x['feature_id'] for x in m['features'] if any('/'+d+'/' in x['source']['document'] for d in ['pokemon-rules','engine-overworld','user-interface'])}
for field,key,ids in [('old_feature_results','feature_id',oldids),('active_feature_results','feature_id',own),('retired_metadata_results','metadata_id',mids)]:
    glob={x[key]:x for x in rg[field]}
    assert all(x['verdict']==glob[x[key]]['verdict'] for x in r2[field])

mandatory={}
for path in ['REPORT.md','findings.json','finding-results.json','feature-results.json','issue-results.json','reading-coverage.json','section-results.json','agents/pokemon-world-report.md','agents/pokemon-world-results.json','agents/pokemon-world-evidence.json']:
    b=git(RR,RP+path); data=json.loads(b) if path.endswith('.json') else None
    mandatory[path]={**ident(RR,RP+path),'consumption':'FULL_PROSE_READ' if data is None else 'COMPLETE_STRUCTURED_PARSE_AND_OWN_SCOPE_RECONCILIATION','array_lengths':{k:len(v) for k,v in data.items() if isinstance(v,list)} if isinstance(data,dict) else None}

evidence={}; direct_changed=[]
for i in sorted(own):
    x=f[i]; loc=x['current_applicability']['locator']; p=x['source']['document']; s=x['source']; cb=git(CUR,p)
    assert x['current_applicability']['snapshot_commit']==CUR
    assert sha(body(CUR,p,loc['line_ranges']))==loc['unit_sha256']
    assert sha(cb)==loc['file_sha256'] and ident(CUR,p)['git_blob']==loc['file_git_blob']
    assert sha(body(s['commit'],p,s['line_ranges']))==s['unit_sha256']
    assert sha(git(s['commit'],p))==s['file_sha256']
    assert s==pf[i]['source']
    if i in of: assert s==of[i]['source']
    historical_effective=sha(body(B8,p,x['functional_scope']['line_ranges']))
    changed=historical_effective!=loc['unit_sha256']
    if changed: direct_changed.append(i)
    changed_fields=[k for k in x if x[k]!=pf[i].get(k)]
    targets=[t for t in x['dependencies']['feature_refs'] if f[t]['current_applicability']['locator']['unit_sha256']!=pf[t]['current_applicability']['locator']['unit_sha256'] or f[t]['future_plan']!=pf[t]['future_plan']]
    evidence[i]={'candidate_pointer':'/features'+pointer(m['features'],'feature_id',i),'changed_fields_from_r2':changed_fields,'source_preserved':True,'current_locator_hashes_recomputed':True,'baseline_effective_sha256':historical_effective,'current_effective_sha256':loc['unit_sha256'],'direct_source_changed':changed,'current_source':{'commit':CUR,'document':p,**loc},'r2_object_sha256':sha(json.dumps(pf[i],ensure_ascii=False,sort_keys=True).encode()),'r3_object_sha256':sha(json.dumps(x,ensure_ascii=False,sort_keys=True).encode()),'affected_outgoing_targets':targets}

# Fresh semantic reads recorded exactly; complete diffs were read for all changed primary files.
fresh=collections.defaultdict(list)
def ranges(path,rs): fresh['deliverables/final-specification-set/'+path]+=rs
ranges('engine-overworld/wp11-map-topology-transfer.md',[[23,179],[187,196]])
ranges('engine-overworld/wp12-terrain-movement-vehicles.md',[[92,186]])
ranges('engine-overworld/wp13-map-events-npc-followers.md',[[74,151]])
ranges('engine-overworld/wp13-interpreter-command-matrix.md',[[21,154],[169,172]])
ranges('engine-overworld/wp14-random-dungeons.md',[[23,105],[220,263],[282,288]])
ranges('engine-overworld/wp15-resource-matching-and-audio.md',[[20,50],[92,130]])
ranges('engine-overworld/wp16-world-rendering-and-visual-transitions.md',[[21,253]])
ranges('engine-overworld/wp59-world-time-weather-field-moves.md',[[102,180]])
ranges('pokemon-rules/wp19-attributes-ability-and-stats.md',[[126,181],[223,234]])
ranges('pokemon-rules/wp23-shadow-data-and-vectors.md',[[61,238]])
ranges('pokemon-rules/wp23-shadow-hyper-and-purification.md',[[74,85],[132,164]])
ranges('pokemon-rules/wp31-basic-evolution.md',[[237,250],[263,271]])
ranges('pokemon-rules/wp34-inheritance-and-offspring.md',[[22,51],[145,166]])
ranges('pokemon-rules/wp37-roaming-and-poke-radar.md',[[95,95]])
ranges('pokemon-rules/wp43-types-accuracy-and-damage.md',[[163,163]])
ranges('pokemon-rules/wp50-held-item-effect-coverage.md',[[30,31]])
ranges('pokemon-rules/wp50-held-item-triggers-and-consumption.md',[[167,167]])
ranges('pokemon-rules/wp53-safari-and-bug-catching-contest.md',[[44,48],[128,136],[234,243]])
ranges('pokemon-rules/wp60-berry-plants.md',[[20,51],[70,70],[84,88],[107,134]])
ranges('pokemon-rules/wp61-field-passive-effects-and-blackout.md',[[22,57],[139,146]])
ranges('pokemon-rules/wp62-pokedex-records-regions-and-content.md',[[147,178]])
ranges('pokemon-rules/wp69-voltorb-flip.md',[[47,60]])
ranges('user-interface/wp65-title-load-options-pause-and-pc.md',[[23,101],[148,176],[206,233]])
ranges('user-interface/wp66-a-party-and-summary-ui.md',[[134,169]])
ranges('user-interface/wp66-b-storage-and-pokedex-ui.md',[[88,134]])
ranges('user-interface/wp66-c-bag-item-storage-and-shop-ui.md',[[13,23]])
ranges('user-interface/wp67-a-battle-interaction-and-presentation.md',[[28,107],[193,317],[341,355]])
ranges('user-interface/wp67-b-lifecycle-presentations-and-history.md',[[139,147]])
ranges('user-interface/wp69-slot-machine.md',[[17,125]])
ranges('test-catalog/engine-overworld-wp11-15-59-60.md',[[18,20],[740,822]])
ranges('test-catalog/pokemon-rules-wp19-21-22-23-34.md',[[340,356]])
ranges('generic-kernel/wp03-content-identity-and-schema.md',[[277,338]])
ranges('generic-kernel/wp08-localization.md',[[44,98]])
ranges('generic-kernel/wp10-migration-failure-recovery.md',[[230,247]])
ranges('creature-rpg/wp18-creature-identity-species-ownership.md',[[47,106]])
ranges('creature-rpg/wp25-party-and-storage.md',[[103,168]])
ranges('creature-rpg/wp24-player-trainers-partners.md',[[240,275]])
ranges('creature-rpg/wp28-item-use-and-training.md',[[47,78],[105,111],[135,140]])
ranges('creature-rpg/wp30-growth-learning-and-friendship.md',[[79,159],[183,222]])
ranges('creature-rpg/wp33-daycare-and-breeding-session.md',[[107,158]])
ranges('combat-requirements/wp39-battle-context-and-participants.md',[[167,182]])
ranges('combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md',[[59,96]])
for p in list(fresh):
    end=len(git(CUR,p).splitlines());fresh[p]=[[a,min(b,end)] for a,b in fresh[p] if a<=end]

repairdata=read(C,B+'revisions/r3/dependency-repairs.json')
repairs=[x for x in repairdata['records'] if x['feature_id'] in own]
assert len(repairs)==20
cases=[]
for r in repairs:
    i=r['feature_id']; x=f[i]; oldrefs=set(pf[i]['dependencies']['feature_refs']); now=set(x['dependencies']['feature_refs'])
    removed=oldrefs-now; added=now-oldrefs
    expected={t['target_feature_id'] for t in r['removed_edges']}
    assert removed==expected
    cases.append({'feature_id':i,'r2_verdict':'FAIL','verdict':'PASS','candidate_pointer':evidence[i]['candidate_pointer']+'/dependencies/feature_refs','source':evidence[i]['current_source'],'removed_refs':sorted(removed),'added_refs':sorted(added),'retained_refs':sorted(now&oldrefs),'reason':r['rationale'],'targets':[{ 'feature_id':t,'source':evidence[t]['current_source'] if t in evidence else {'commit':CUR,'document':f[t]['source']['document'],**f[t]['current_applicability']['locator']}} for t in sorted(now)],'same_root_check':'All current own outgoing feature refs enumerated; extra 751/760→355 and 664→159/160/161 removed; positive controls kept.'})

bad={'FR-000456','FR-000596'}
finding_for={'FR-000456':'R3-EV-BOUNDARY-001','FR-000596':'R3-SOURCE-ATTRIBUTION-001'}
newcases=[]
for i,why,expected,counter in [
 ('FR-000456','The accepted source says HP255/ATK255 totals510; the new annotation calls this over-total EV. The violation is per-stat252, not total510.','Describe per-stat excess with total510 unchanged; preserve the first negative remainder failure and unaffected routing.','The default two-stat template totals255+255=510, yet already fails at HP single-stat upper bound252−255=−3. A total-excess explanation is false.'),
 ('FR-000596','The new annotation attributes negative step-probability/floor-accumulator behavior to WP61§3. The actual full B8→5f file delta only repairs L56 Repel comparison-member selection.','Replace the copied probability summary with default first non-Egg (including fainted) versus alternate first able Repel comparison, and retain WP36 consumer ownership.','Party first non-Egg fainted L50, next healthy L10, wild L20: the default comparison blocks on L50; first-able alternative compares L10 and permits. Probability floor arithmetic cannot describe or distinguish this accepted correction.')]:
    idx=next(j for j,x in enumerate(read(C,B+'revisions/r3/feature-source-deltas.json')['records']) if x['feature_id']==i)
    file_rows=read(C,B+'revisions/r3/source-file-reassessment.json')['records']; fi=next(j for j,x in enumerate(file_rows) if x['document']==f[i]['source']['document'])
    patch_rows=read(C,B+'revisions/r3/source-refinement-patch.json')['records']; pj=next(j for j,x in enumerate(patch_rows) if x['feature_id']==i); pk=next(j for j,x in enumerate(patch_rows[pj]['field_changes']) if x['pointer']=='/differences')
    newcases.append({'feature_id':i,'finding_id':finding_for[i],'verdict':'FAIL','facet':'current_calibration','candidate_pointer':evidence[i]['candidate_pointer']+'/differences/1','candidate_text':f[i]['differences'][1],'supporting_author_record_pointer':'/records/'+str(idx)+'/source_fact_delta','supporting_author_file':B+'revisions/r3/feature-source-deltas.json','source_file_reassessment_pointer':'/records/'+str(fi)+'/source_fact_reassessment','source_refinement_patch_pointer':'/records/'+str(pj)+'/field_changes/'+str(pk)+'/after/1','source':evidence[i]['current_source'],'effective_source_ranges':f[i]['current_applicability']['locator']['line_ranges'],'distinguishing_counterexample':counter,'reason':why,'minimum_fix':expected})

delta_reason={r['feature_id']:r['source_fact_delta'] for r in read(C,B+'revisions/r3/feature-source-deltas.json')['records']}
delta_reason['FR-000456']='HP/ATK255 is per-stat excess at total510. Recalculation preserves it; normal growth fails at first invalid single-stat interval before EV/EXP writes. Candidate annotation incorrectly labels total excess.'
delta_reason['FR-000596']='Only Repel comparison member changes: default first non-Egg incl fainted versus configured first able. Parent keeps encounter gate input; 762 retains count/UI selector. Candidate annotation mistakenly describes probability accumulator.'
active=[]
for i in sorted(own):
    x=f[i]; e=evidence[i]; repaired=i in {r['feature_id'] for r in repairs}; affected=e['direct_source_changed'] or bool(e['affected_outgoing_targets']) or repaired or x['dependencies']!=pf[i]['dependencies']
    reason=(delta_reason[i] if e['direct_source_changed'] else next((r['rationale'] for r in repairs if r['feature_id']==i),'R2 complete attributed source/target semantics retained only for unchanged effective clauses; current referenced targets and incoming source changes checked for nonimpact.'))
    active.append({'feature_id':i,'r2_verdict':pa[i]['verdict'],'verdict':'FAIL' if i in bad else 'PASS','classification_verdict':'PASS','responsibility_verdict':'PASS','scope_verdict':'PASS','dependency_verdict':'PASS','current_calibration_verdict':'FAIL' if i in bad else 'PASS','current_state':{'source_snapshot':CUR,'destination_verification':x['destination_verification']['status'],'implementation':x['implementation']['status'],'acceptance':x['implementation']['acceptance_status'],'stage':x['future_plan']['stage'],'stage_approval':x['future_plan']['stage_approval']},'method':'FIXED_R2_SEMANTIC_CREDIT_PLUS_FRESH_CHANGED_CLAUSE_AND_EFFECTIVE_SOURCE_TARGET_REVIEW' if affected else 'IDENTITY_BOUND_R2_SEMANTIC_CREDIT_WITH_EXPLICIT_NONIMPACT','reason':reason,'r2_reason':pa[i]['reason'],'source_document':x['source']['document'],'functional_scope':x['functional_scope'],'current_source':e['current_source'],'identity':e,'inheritance_limits':'Preservation/hashes are evidence of identity, not dependency semantics. Changed source/target, repairs, refinements and source calibration evaluated separately; no target compatibility inherited.','finding_refs':[finding_for[i]] if i in bad else []})
ar={x['feature_id']:x for x in active}
old=[]
for i in sorted(oldids):
    retired=i in ret; x=ret[i] if retired else f[i]
    assert x['source']==of[i]['source']
    if retired: assert {k:v for k,v in x.items() if k!='retirement'}==of[i]
    old.append({'feature_id':i,'r2_verdict':po[i]['verdict'],'verdict':'FAIL' if i in bad else 'PASS','disposition':'retired' if retired else 'active','current_state':'COMPLETE_ORIGINAL_HISTORY_PRESERVED_AS_METADATA' if retired else ar[i]['current_state'],'classification_verdict':'PASS','dependency_verdict':'PASS','current_calibration_verdict':'FAIL' if i in bad else 'PASS','source_document':x['source']['document'],'immutable_source_preserved':True,'complete_retired_history_preserved':True if retired else None,'reason':'Full original body equals d62 excluding retirement; metadata and consumers remain valid.' if retired else ar[i]['reason'],'method':'COMPLETE_HISTORY_FIELD_COMPARISON_AND_CONSUMER_NAVIGATION' if retired else ar[i]['method'],'finding_refs':[finding_for[i]] if i in bad else []})
metas=[]
for prior in r2['retired_metadata_results']:
    i=prior['metadata_id']; x=meta[i]; previous=next(v for v in prev['metadata_records'] if v['metadata_id']==i)
    assert x==previous
    history=[]
    for fid in x['retired_feature_ids']:
        assert {k:v for k,v in ret[fid].items() if k!='retirement'}==of[fid]
        history.append({'feature_id':fid,'complete_original_body_equal':True,'original_body_sha256':sha(json.dumps(of[fid],ensure_ascii=False,sort_keys=True).encode()),'retirement':ret[fid]['retirement']})
    metas.append({**copy.deepcopy(prior),'r2_verdict':prior['verdict'],'verdict':'PASS','history_proof':history,'current_navigation':'Existing metadata→parent→excluded_child_refs→child and direct links retained; changed consumers reviewed separately.','identity_equal_to_r2':True})

ledger=[]
for prior in r2['reading_ledger']:
    p=prior['path']; ci=ident(CUR,p); hist=ident(B8,p); oldcur=prior['commit']; pi=ident(oldcur,p)
    diff=subprocess.check_output(['git','diff','--no-ext-diff','--no-color',B8,CUR,'--',p]); changed=hist['sha256']!=ci['sha256']; hunks=[]
    for a,ac,b,bc in re.findall(rb'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@',diff,re.M):hunks.append({'old_range':[int(a),int(a)+int(ac or b'1')-1],'current_range':[int(b),int(b)+int(bc or b'1')-1]})
    ledger.append({'path':p,'historical_identity':hist,'r2_current_identity':pi,'current_identity':ci,'candidate_formal_identity':ident(C,p),'source_changed_from_B8':changed,'source_changed_from_R2':pi['sha256']!=ci['sha256'],'fresh_read_ranges':merge(fresh[p]+[h['current_range'] for h in hunks if h['current_range'][0]<=h['current_range'][1]]),'full_cumulative_diff_read':changed,'complete_diff_sha256':sha(diff) if changed else None,'diff_hunks':hunks,'inherited_r2_reading':prior,'credit':'Full fixed prior attributed body plus all current changed clauses and exact unchanged portions; fresh ranges are listed, not claimed as a new full-file read.','inheritance_limits':'Only unchanged clauses/facets retain prior semantic credit. Full changed effective source/consumer units reread where listed; command matrix unchanged table portions retain prior exact-identity credit.'})

units=[]
assert set(direct_changed)=={r['feature_id'] for r in read(C,B+'revisions/r3/feature-source-deltas.json')['records'] if r['feature_id'] in own}
for i in sorted(direct_changed):units.append({'feature_id':i,'source_fact_verdict':'PASS','source_to_routing_classification_verdict':'PASS','source_to_routing_responsibility_verdict':'PASS','current_calibration_verdict':'FAIL' if i in bad else 'PASS','source':evidence[i]['current_source'],'reason':delta_reason[i],'finding_refs':[finding_for[i]] if i in bad else []})

headings=[]; incoming_headings=[]
for row in read(C,B+'revisions/r3/new-heading-mappings.json')['accepted_mappings']:
    p=row['document']; ownrefs=sorted(set(row['feature_refs'])&own)
    if p not in docs and not ownrefs:continue
    ls=git(CUR,p).splitlines(keepends=True); a,b=row['line_ranges'][0]; raw=ls[a-1]; text=raw.decode().strip(); title=re.sub(r'^#{1,6}\s+','',text)
    assert title==row['title'] and sha(title.encode())==row['source_identity']['heading_sha256']
    assert sha(raw)==row['source_identity']['raw_markdown_heading_sha256']
    assert sha(body(CUR,p,row['line_ranges']))==row['source_identity']['unit_sha256']
    record={'document':p,'title':row['title'],'current_ranges':row['line_ranges'],'current_identity':ident(CUR,p),'feature_refs':row['feature_refs'],'metadata_refs':row['metadata_refs'],'owned_feature_refs':ownrefs,'verdict':'PASS','classification_verdict':'PASS','current_calibration_verdict':'PASS','identity_recomputed':True,'reason':row['basis'],'semantic_basis':'Final source defines existing parent contract, static vector, or named consumer; new heading does not establish a new owner. Consumer effective scopes and existing parent-child navigation retained. NOT_EXECUTED is preserved.'}
    (headings if p in docs else incoming_headings).append(record)

dependencies=[]
for i in sorted(own):
    refs=f[i]['dependencies']['feature_refs']
    if not refs:continue
    dependencies.append({'feature_id':i,'verdict':'PASS','feature_refs':refs,'r2_feature_refs':pf[i]['dependencies']['feature_refs'],'source':evidence[i]['current_source'],'targets':[{'feature_id':t,'document':f[t]['source']['document'],'effective_current_ranges':f[t]['current_applicability']['locator']['line_ranges'],'unit_sha256':f[t]['current_applicability']['locator']['unit_sha256']} for t in refs],'affected_targets':evidence[i]['affected_outgoing_targets'],'reason':next((r['rationale'] for r in repairs if r['feature_id']==i), '645/647 explicitly consume330 terminal motion; 699/703 explicitly consume440 language and352/354 resource identity/load failures.' if i in {'FR-000645','FR-000647','FR-000699','FR-000703'} else 'Actual prerequisite/shared/consumer or named exclusion contract retained from complete R2 semantic review; changed effective targets separately reconciled, without demanding a repeated smallest ID.'),'positive_control':i in {'FR-000744','FR-000753','FR-000681'}})

groups=[]
for g in r2['original_group_results']:
    n=copy.deepcopy(g); n['r2_verdict']=g['verdict'];n['r2_current_scope_verdict']=g.get('current_scope_verdict',g['verdict']);n['verdict']='PASS';n['original_case_verdict']='PASS';n['current_scope_verdict']='FAIL' if g['finding_id']=='POK-S05' else 'PASS';n['finding_refs']=['R3-SOURCE-ATTRIBUTION-001'] if n['current_scope_verdict']=='FAIL' else [];n['reason']='Original classification/split/retirement cases remain PASS. R2 dependency issue repaired; new current-source annotation error is separately scoped to456/596, with596 in POK-S05.';n['r2_full_result']=copy.deepcopy(g);groups.append(n)

prior_issues=copy.deepcopy(r2['issue_results'])
for r in prior_issues:r['r2_verdict']=r['verdict'];r['verdict']='PASS';r['method']='R2 exact repaired catalog mappings plus final source/consumer nonimpact reconciliation; original16 catalog removals and724 addition preserved.'
issue={'issue_id':'POK-WORLD-R2-DEP-001','r2_verdict':'FAIL','verdict':'PASS','cases':cases,'same_root_propagation':'20 source rows, all replacements,664 extra159/160/161 and751/760 extra355 examined;744 trainer-card,735 exclusion and753 diagnostics remain valid.'}
incoming=[]
for x in m['features']:
    i=x['feature_id']
    if i in own:continue
    a=set(x['dependencies']['feature_refs'])&own;b=set(pf[i]['dependencies']['feature_refs'])&own
    if a!=b:incoming.append({'producer_id':i,'added_own_refs':sorted(a-b),'removed_own_refs':sorted(b-a),'source':{'commit':CUR,'document':x['source']['document'],**x['current_applicability']['locator']},'verdict':'PASS','reason':'397 exact author egg-group domain points to508 parent/offspring role consumer. This is not a new rule or a transfer of offspring generation to the catalog.'})

results={'schema_version':'r3-independent-pokemon-world.v1','candidate_commit':C,'current_snapshot_commit':CUR,'r2_candidate_commit':R2,'r2_review_commit':RR,'outcome':'FAIL','configuration':{k:'UNVERIFIED' for k in ['model','effort','service_tier','speed','Fast','cloud_uuid']},'counts':{'primary_documents':len(docs),'changed_primary_documents':sum(x['source_changed_from_B8'] for x in ledger),'original_ids':len(old),'active_rows':len(active),'active_PASS':sum(x['verdict']=='PASS' for x in active),'active_FAIL':len(bad),'classification_PASS':len(active),'responsibility_PASS':len(active),'scope_PASS':len(active),'dependency_PASS':len(active),'current_calibration_FAIL':len(bad),'retired_metadata':len(metas),'original_groups':len(groups),'repaired_R2_cases':len(cases),'direct_changed_units':len(units),'owned_new_headings':len(headings),'external_new_headings_with_own_consumers':len(incoming_headings),'nonempty_outgoing_feature_ref_rows':len(dependencies),'outgoing_feature_ref_edges':sum(len(x['feature_refs']) for x in dependencies)},'old_feature_results':old,'active_feature_results':active,'retired_metadata_results':metas,'issue_results':[issue]+prior_issues,'original_group_results':groups,'reading_ledger':ledger,'extra_consumer_reading':[{'path':p,'current_identity':ident(CUR,p),'fresh_read_ranges':merge(rs),'role':'EXTRA_CONSUMER_NOT_PRIMARY'} for p,rs in fresh.items() if p not in docs],'new_heading_results':headings,'external_new_heading_consumer_results':incoming_headings,'changed_source_results':units,'changed_file_results':[{'document':x['path'],'current_identity':x['current_identity'],'complete_diff_sha256':x['complete_diff_sha256'],'hunks':x['diff_hunks'],'source_acceptance_verdict':'DELEGATED_TO_ROOT_SOURCE_RECEIPT_AUDIT','source_semantic_verdict':'PASS','classification_calibration_verdict':'PASS','annotation_calibration_verdict':'FAIL' if any(r['feature_id'] in bad and r['source']['document']==x['path'] for r in units) else 'PASS','affected_units':[u['feature_id'] for u in units if u['source']['document']==x['path']]} for x in ledger if x['source_changed_from_B8']],'outgoing_dependency_results':dependencies,'incoming_dependency_results':incoming,'mandatory_r2_inputs':mandatory,'refinement_results':[{'feature_id':i,'verdict':'PASS','reason':'Normal motion/collision timer is independent from jump timer; production and consumption gates, message early return, micro-update exclusion and failed prefix are not merged.' if i in ['FR-000645','FR-000647'] else 'Seven SCRIPT_TEXTS image roles choose game then core per request; actual H affects reel timing; empty translation/load/frame-prefix and object/random/sound/financial prefixes stay separate.'} for i in ['FR-000645','FR-000647','FR-000699','FR-000703']],'extra_refinement_results':[{'feature_id':'FR-000397','owned_primary':False,'verdict':'PASS','reason':'15 exact author egg-group IDs incl Water1/Water2/Water3, extension-sensitive strict domain, base/form defaults, WP33 Undiscovered-first/Ditto/intersection and WP34 generation roles remain distinct. Direct refs target real B8 parent anchors; added current child anchor is not misrepresented as B8.'}],'new_findings':[{'id':'R3-SOURCE-ATTRIBUTION-001','severity':'P3','verdict':'FAIL','title':'Two new source-calibration annotations misstate the accepted effective source','candidate_file':B+'routing-manifest.json','cases':newcases,'minimum_fix':'Correct only the two current-source difference summaries and corresponding delta evidence. Preserve category, responsibilities, scopes, current/upstream identities and repaired dependencies.'}],'limits':['No Ruby/game/business/host/Showdown/framework execution; static JSON/Git/Python only.','Root owns global receipts, tool defect replay, whole-tree protection and final reconciliation. This scope does not independently award source acceptance.','Classifications are coarse proposals; destination compatibility, user scope/stage approval, implementation and acceptance remain pending.','Full prior source credit is identity-bound to R2/R1/original attributed reading. Fresh current ranges and full changed diffs are explicit; no truncated output earns unread credit.']}
results['new_findings']=[{'id':fid,'severity':'P3','verdict':'FAIL','title':'Accepted EV input boundary mislabeled as total excess' if fid=='R3-EV-BOUNDARY-001' else 'Accepted source delta attributed to the wrong effective contract','candidate_file':B+'routing-manifest.json','cases':[c for c in newcases if c['finding_id']==fid],'root_merge_qualification':'Canonical issue ID assigned by root; this domain supplies only456 or596. Other domain cases are independently owned and not counted again here.','minimum_fix':'Correct the affected manifest differences and current delta/file evidence, patch after-values and generator strings; regenerate derived view and identity summaries. Preserve source, routing category, responsibilities, scope and repaired dependencies.'} for fid in ['R3-EV-BOUNDARY-001','R3-SOURCE-ATTRIBUTION-001']]
independent_repair_reasons={348:'The tile-mapping result is a three-layer map consumed by364;346/347 produce layout and324 transfers it.355 only owns audio.',372:'366 owns the exact type-change, noninterruptible fixed weather transition and camera-follow consumer;324/325 retain genuine map lifecycle inputs.',373:'Nine weather identities, particle/tile/tone inputs and Storm flash reach366.33 is battle abort and358 a different pre-battle system.',487:'The complete Shadow6.1 body supplies actual growth/EV inputs to29/204, setter and friendship boundaries to205/208, with held effects578 and purification748 retained.',608:'The complete Pokedex visibility/search/forms unit reaches665/666/667 UI consumers.670 is the unrelated bag-selector interface.',664:'Storage UI writes invoke164–167 container/operation/guard/persistence contracts and162 capacity.157–161 instead concern partner and trainer/player contracts.',681:'29/204/205/206/207 and739 own growth and persistent/battle move synchronization.735 is explicitly labeled an exclusion comparison, not the teaching executor.',682:'The full capture queue/name/full-party/source-removal UI consumes528–531 and162/164 container acceptance. Partner participation/treatment do not implement it.',749:'Purification uses the storage selector and same-object move/replace rules, matching164/166/662/664 and690. No NPC trade, owner rewrite or Pokedex forms browsing occurs.',751:'The one-line shake request→list-write→0.5-second wait needs365 world animation and425 runtime time. Any animation SE is indirect inside365; no751 direct audio-family call is specified.',754:'The two handler directory rows are actual EXP/EV modifiers consumed by204/29 with578 held-item rules; switching-failure25 has no role.',755:'World EXP.SHARE and bonus inputs join204/29 growth,31 end state,148 held state and153 wallet, retaining578. They do not invoke25 switching failure.',756:'Map-scene-only return sets transfer and dismounts, matching324 plus326 map-state/persistence boundary navigation. The separate trainer-card scene650 does not take part.',757:'Monotonic425 timer and625/626 messages/choices are reached by645 pause micro-updates.650 has no timer or micro-update responsibility.',759:'Save/Quit/Safari/contest pause entries consume643/645 and444/446 persistent-save contracts;580/582 remain the mode state inputs.650 is unrelated.',760:'Only the map display tick, plant image identity/direction and stage flash were split here.325,352 and365 match those effects; save, pre-battle transitions and generic audio do not.',761:'The interaction actually selects filtered fertilizer/berry items through670, changes177 inventory and590 plant state, and asks626 confirmation.186 battle pre-deduction/refund is a different entry.',762:'Repel depletion explicitly calls ordinary183 item use and670 flagged selector.327/330 movement,355 BGM,625 messages and626 confirmation keep their specific real uses.',764:'The written recovery transfer/dismount/refresh is324 with326 map-state lifecycle navigation and153 money. It does not open650 trainer card.',766:'The ordered cell reveal/explosion/board reveal/collection stages use625 confirmation/messages.699 Slot reel slip/stop has no shared contract.'}
for c in cases:
    c['author_rationale_under_review']=c['reason'];c['reason']=independent_repair_reasons[int(c['feature_id'][3:])]
for d in dependencies:
    n=int(d['feature_id'][3:])
    if n in independent_repair_reasons:d['reason']=independent_repair_reasons[n]
source_r2=read(RR,RP+'agents/source-results.json')
results['mandatory_r2_inputs']['agents/source-results.json']={**ident(RR,RP+'agents/source-results.json'),'consumption':'COMPLETE_STRUCTURED_PARSE; full source diff/new-heading reading credit used only by exact identity','reading_qualification':source_r2['reading_qualification']}
prior_heads={(x['document'],x['anchor']):x for x in source_r2['source_heading_results']}
for rec in incoming_headings:
    prior=next(v for (p,a),v in prior_heads.items() if p==rec['document'] and v['title']==rec['title'])
    expected=body('0eee6d141f33758eda34bd8ebad94a3e2b617f5a',rec['document'],prior['ranges'])
    assert expected==body(CUR,rec['document'],rec['current_ranges'])
    rec['reading_method']='EXACT_R2_PREPARED_FULL_NEW_BODY_CREDIT_PLUS_FINAL_OWNED_CONSUMER_REASSESSMENT'
    rec['identity_bound_prior_body']={'commit':'0eee6d141f33758eda34bd8ebad94a3e2b617f5a','ranges':prior['ranges'],'sha256':sha(expected),'review_commit':RR,'review_record':prior}

# Whole owned heading projection: structural alignment is kept distinct from semantic credit.
historical=read(C,B+'section-coverage.json'); old_historical=read(R2,B+'section-coverage.json')
assert historical==old_historical
current_coverage=read(C,B+'current-section-coverage.json'); current_index={(s['path'],s['anchor']):s for s in current_coverage['sections']}
def slug(t):
    t=re.sub(r'<[^>]*>','',t);t=re.sub(r'\[([^]]+)\]\([^)]*\)',r'\1',t).lower()
    return ''.join(c for c in t if c in ' -_' or unicodedata.category(c)[0] in 'LN').replace(' ','-')
def headings_of(p,c=CUR):
    ls=git(c,p).splitlines(keepends=True); found=[]; used=collections.Counter(); fence=None
    for n,line in enumerate(ls,1):
        text=line.decode();fm=re.match(r'^\s{0,3}(`{3,}|~{3,})',text)
        if fm:
            mark=fm.group(1)[0];fence=None if fence==mark else mark if fence is None else fence;continue
        if fence is not None:continue
        hm=re.match(r'^(#{1,6})\s+(.+?)\s*$',text)
        if not hm:continue
        lev=len(hm.group(1));title=hm.group(2);stem=slug(title);anchor=stem+('-'+str(used[stem]) if used[stem] else '');used[stem]+=1
        found.append({'line_start':n,'level':lev,'title':title,'anchor':anchor,'heading_sha256':sha(line)})
    for j,h in enumerate(found):
        h['line_end']=next((k['line_start']-1 for k in found[j+1:] if k['level']<=h['level']),len(ls))
    return found
section_results=[]
for p in sorted(docs):
    for h in headings_of(p):
        s=current_index[p,h['anchor']]
        assert all(s[k]==h[k] for k in ['line_start','line_end','level','title','heading_sha256'])
        assert all(i in f for i in s['feature_refs']) and all(i in meta for i in s['metadata_refs'])
        section_results.append({'path':p,**h,'verdict':'PASS','classification_navigation_verdict':'PASS','feature_refs':s['feature_refs'],'metadata_refs':s['metadata_refs'],'method':'FINAL_GIT_HEADING_RECOMPUTE_PLUS_PRIOR_IDENTITY_BOUND_SEMANTICS_AND_FRESH_CHANGED_SOURCE_REVIEW','limit':'Heading/JSON alignment alone is not a fresh whole-body semantic read; source-calibration annotation findings remain separate.'})
results['section_results']=section_results
results['catalog_section_results']=[s for s in section_results if '/test-catalog/' in s['path']]
results['counts']['owned_current_headings']=len(section_results)
results['counts']['owned_catalog_headings']=len(results['catalog_section_results'])
results['historical_section_coverage_preserved']=True
direct_results=[]
anchor_cache={}
for i in sorted(own):
    entries=[]
    for d in f[i]['dependencies']['direct_refs']:
        p=d['document'];key=(B8,p)
        if key not in anchor_cache:
            hh=headings_of(p,B8);anchor_cache[key]={h['anchor']:[h['line_start'],h['line_end']] for h in hh}
            for a in re.findall(r'<a\s+id=[\"\x27]([^\"\x27]+)[\"\x27]',git(B8,p).decode()):anchor_cache[key].setdefault(a,None)
        assert d['anchor'] in anchor_cache[key], (i,p,d['anchor'])
        entries.append({'document':p,'anchor':d['anchor'],'B8_anchor_exists':True,'B8_effective_heading_range':anchor_cache[key][d['anchor']],'reason':d['reason'],'current_document_identity':ident(CUR,p)})
    direct_results.append({'feature_id':i,'verdict':'PASS','refs':entries,'semantic_credit':'Existing explicit shared/consumer contracts preserve R2 semantic credit only for unchanged clauses; changed source/target and four owned refinements freshly reconciled. Anchor existence is only a separate structural check.'})
results['direct_reference_results']=direct_results
results['counts']['direct_reference_edges']=sum(len(x['refs']) for x in direct_results)

affected_incoming=[]
for x in m['features']:
    i=x['feature_id'];targets=sorted(set(x['dependencies']['feature_refs'])&own)
    if i in own or not targets:continue
    producer_changed=x['current_applicability']['locator']['unit_sha256']!=pf[i]['current_applicability']['locator']['unit_sha256'] or x['dependencies']!=pf[i]['dependencies'] or x['future_plan']!=pf[i]['future_plan']
    target_changed=any(evidence[t]['direct_source_changed'] or f[t]['dependencies']!=pf[t]['dependencies'] or f[t]['future_plan']!=pf[t]['future_plan'] for t in targets)
    if producer_changed or target_changed:affected_incoming.append({'producer_id':i,'producer_current_source':{'commit':CUR,'document':x['source']['document'],**x['current_applicability']['locator']},'targets':[{'feature_id':t,'effective_current_source':evidence[t]['current_source'],'classification_verdict':'PASS','responsibility_verdict':'PASS','current_calibration_verdict':ar[t]['current_calibration_verdict']} for t in targets],'producer_changed':producer_changed,'target_changed':target_changed,'target_scope_verdict':'PASS','producer_dependency_verdict':'RECONCILE_WITH_PRODUCER_DOMAIN_RESULT','reason':'No incoming edge transfers producer duties into target or provides target compatibility. Effective target contracts are the displayed ranges; producer semantics are reconciled by its allocated domain reviewer.'})
results['affected_incoming_results']=affected_incoming
results['counts']['affected_incoming_producers']=len(affected_incoming)
corrections=[]
newtext={'FR-000456':'正常设施模板HP/攻击EV各255、其余0、总量510，是单项越额；重算不规范化。该样本条件化进入普通成长时，先在HP单项负余量处失败，早于本接收者EV/经验写入；其它越额形态仍按各自单项/总量余量门判断。','FR-000596':'Repel遭遇门默认比较首个非蛋成员（含濒死）；替代配置才比较首位可战成员，实际允许门仍由WP36负责；本行保留步进通知次序与计数交界。'}
for c in newcases:
    i=c['feature_id'];suffix=f[i]['differences'][1].split('；当前已接受源细化上述行为',1)[1]
    corrections.append({'finding_id':c['finding_id'],'feature_id':i,'manifest':{'path':B+'routing-manifest.json','pointer':c['candidate_pointer'],'before':c['candidate_text'],'proposed_after':newtext[i]+'；当前已接受源细化上述行为'+suffix},'source_delta':{'path':B+'revisions/r3/feature-source-deltas.json','pointer':c['supporting_author_record_pointer'],'proposed_after':newtext[i]},'file_reassessment':{'path':B+'revisions/r3/source-file-reassessment.json','pointer':c['source_file_reassessment_pointer'],'proposed_after':newtext[i]},'unified_patch_after_value':{'path':B+'revisions/r3/source-refinement-patch.json','pointer':c['source_refinement_patch_pointer'],'proposed_after':newtext[i]+'；当前已接受源细化上述行为'+suffix},'regeneration_sources':[{'path':B+'revisions/r3/build-author-evidence.py','key':'wp19-attributes-ability-and-stats.md' if i=='FR-000456' else 'wp61-field-passive-effects-and-blackout.md'}],'derived_consumers':[B+'views/pokemon-rules.md'],'qualified_updates':'Update final hashes/diff summaries and patch reconstruction proof after concrete author edits. Preserve R1/R2 history, accepted source bytes, archived application receipts and source/current/upstream identities.'})
(OUT/'pokemon-world-calibration-corrections.json').write_text(json.dumps({'role':'REVIEW_ONLY_CONCRETE_MINIMUM_CORRECTION_PROPOSAL_NOT_APPLIED','candidate_commit':C,'records':corrections},ensure_ascii=False,indent=2)+'\n')
(OUT/'pokemon-world-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
(OUT/'pokemon-world-evidence.json').write_text(json.dumps({'candidate':C,'current':CUR,'rows':evidence,'mandatory_inputs':mandatory,'counts':results['counts'],'assertions_passed':True},ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results['counts'],ensure_ascii=False,indent=2))
