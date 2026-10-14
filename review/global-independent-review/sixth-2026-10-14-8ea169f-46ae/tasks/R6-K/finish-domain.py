from pathlib import Path
import json,re,hashlib,datetime,collections
P=Path(__file__).parent;BASE=P.parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
U=json.loads((P/'named-review-units.json').read_text());by={x['id']:x for x in U}
L=[json.loads(x) for x in (P/'reading-ledger.jsonl').read_text().splitlines()]
R=[json.loads(x) for x in (P/'reverse-formal-matrix.jsonl').read_text().splitlines()]
F=[json.loads(x) for x in (P/'forward-source-matrix.jsonl').read_text().splitlines()]
# Explicit per-vector consumer domains, authored after reading all row conditions.
mapids={}
def bind(prefix,ids,parents,reason):
 for n in ids:mapids[f'{prefix}{n:02d}']=(['K-U'+str(k).zfill(3) for k in parents],reason)
bind('BE',[1,2,3,4,5,6,15,34],[142,143],'registered condition identity/parameter and common predicate guard; selected target is distinct from successful submission')
bind('BE',[7,8,9,10],[143,83,86],'shared egg/Shadow/Everstone/BattleBond guard with item caller acceptance/consumption separately conditioned')
bind('BE',[11,12,13,14,16,17,18,21,22,23,24,25,36,37],[144,83,86],'actual evolution scene cancel/normal-submit order, owned item caller and postaction/clone dependencies; pixels/audio remain derived under host prerequisites')
bind('BE',[19,20],[144,52,122],'persistent species setter cache/forcedform and target-data defaults; dynamic display is not a blanket form-zero normalization')
bind('BE',[26,27,28],[144,147],'current O world end-notification scan and UI cancellation/submit, after normal C terminal return')
bind('BE',[29,30,31,32,33],[147,149],'K/D producer and persistent readiness to actual event check; ability-party snapshot and no eventID consumption')
bind('BE',[35],[148,144],'received creature shared guard/trade postaction and actual scene cleanup/final party replacement')
bind('CX',[1,2,3,4,5,6,7,8],[146,151,152],'check-time world/map/weather/nonEgg party inputs, short-circuit and exact context literal relations; no demo reachability claim')
bind('CX',range(9,26),[147,143],'C exact critical/actual HP-loss/faint/capture producers plus O start/normal end arrays and current-party scan; prior writes survive exception')
bind('CX',[26,27,28,29],[149,147],'single versus whole-able-party event entry, hit return versus evolution commit and cancel/retry')
bind('CX',[30,31,32,33,34,35],[148,143,144],'actual trade receive-side predicate, old-object Everstone, uncancellable transaction and two cleanup invocations; second native disposal outcome unknown')
bind('CX',[36],[72,147],'specific storage healing preserves readiness versus general heal clearing; current UI guard/selector fact separate from K/D storage')
bind('CX',[37,38],[144,147],'postaction appended member changes later current-party scan; normal cancel returns and clears arrays, exception does not guarantee clearing')
bind('CX',[39,40,41,42],[147,72,69,64],'actual capacity/selection and catch array shifts, merged participant identity versus shared player identity and terminal initial-item restore')
bind('RM',[1,2,3,4,5,6,7,8,10,12,29,33,36],[158],'current O full roam228, own Settings/config/strict encounter type and candidate/temporary association gates')
bind('RM',[9,11],[158,60,62,126,129],'persistent roam creature joins actual C terminal effective-ability dispatch/Peerleave and own NaturalCure/Regenerator callbacks; HP/PP use guarded writes')
bind('RM',[13,14,15,16,17,18,19,20,21,22,23,27,30,31,32,37],[159,158],'own full Radar267 plus current O encounter/modifier/wrapper facts, own bicycle600–609; no safe fallback for nil candidate')
bind('RM',[24],[158,159,160],'actual named-handler registration order: roam advance/reset then radar cancellation with raw-old/display-new map-name gate')
bind('RM',[25,34,35],[158,160,53],'current O public wrapper/temporary and persistent generation/notifications and actual skip/return chain; literal infection probability is a variant premise')
bind('RM',[26],[160,46,47,49],'owned complete save registrations/conversions and current load receipt; temporary radar excluded, migration terminal placeholder fails after completed prefix')
bind('RM',[28],[160,158],'own complete debugroamer461–548 and actual settings/routes; branch-local clear versus preserved already flag, finite retry no must-change guarantee')
# Guard against stale parent IDs; keep formal expected as a derived requirement, not execution.
cp=Path('deliverables/final-specification-set/test-catalog/pokemon-rules-wp31-32-37-38.md')
rows=[]
for ln,s in enumerate(cp.read_text().splitlines(),1):
 m=re.match(r'^\| ((?:BE|CX|RM)\d{2}) \| (.*?) \| (.*?) \|$',s)
 if not m:continue
 vid,pre,exp=m.groups();parents,reason=mapids[vid]
 pp=[by[x] for x in parents]
 rb=next(x for x in R if x['path']==str(cp) and x['start_line']<=ln<=x['end_line'])
 refs=list({(r['path'],r['start_line'],r['end_line']):r for u in pp for r in u['source_refs']+u['necessary_consumer_refs']}.values())
 rows.append({'id':vid,'formal_path':str(cp),'formal_line':ln,'formal_block_id':rb['id'],'row_sha256':hashlib.sha256(s.encode()).hexdigest(),'stated_preconditions':pre,'derived_expected':exp,'manual_consumer_join':reason,'primary_unit_ids':parents,'parent_fact_artifact':str(P/'named-review-units.json'),'parent_facts':[{'id':u['id'],'name':u['name'],'status':u['status'],'fact':u['new_fact'],'consumer_receipts':u.get('consumer_receipts',[]),'prerequisites':u['prerequisites']} for u in pp],'source_and_necessary_consumer_refs':refs,'fresh_formal_read_logs':rb['fresh_read_logs'],'evidence':'SOURCE_STATIC_OWN_PLUS_CURRENT_IMPORTED_CONSUMERS / DERIVED_VECTOR','reference_vector_execution':'NOT_EXECUTED','native_ui_execution':0,'own_imported_source_read_credit':0,'qualification':'Exact row inputs retained. Current source static relations do not certify native timing/pixels/saves/default demo reachability; imported references keep their author scope. Root proposal decisions separate.'})
assert len(rows)==116 and len({x['id'] for x in rows})==116 and set(mapids)=={x['id'] for x in rows}
(P/'context-116-joins.json').write_text(json.dumps({'utc':now,'task':'R6-K','counts':dict(collections.Counter(x['id'][:2] for x in rows)),'vectors':rows,'unbound_vectors':[],'source_read_credit_from_mapping':0,'execution_credit_from_mapping':0},ensure_ascii=False,indent=2)+'\n')
# Validate current persisted ranges/log recoverability, not model semantic proof.
badrefs=[]
for u in U:
 for r in u['source_refs']+u['necessary_consumer_refs']:
  p=Path(r['path'])
  if not p.exists() or not (1<=r['start_line']<=r['end_line']<=len(p.read_text().splitlines())):badrefs.append({'unit':u['id'],'ref':r})
active=json.loads((P/'active-inventory.json').read_text());missing=[]
for kind in ['source','formal']:
 for inv in active[kind]:
  rr=[x for x in L if x['path']==inv['path'] and x.get('acquisition_log') and (P/'logs'/x['acquisition_log']).exists()]
  cv={n for x in rr for n in range(x['start_line'],x['end_line']+1)}
  gap=[n for n in range(1,inv['lines']+1) if n not in cv]
  if gap:missing.append({'path':inv['path'],'kind':kind,'lines':gap})
old=json.loads((P/'logs/matrix-validation.json').read_text())
with (P/'logs/matrix-validation-history.jsonl').open('a') as w:w.write(json.dumps(old,ensure_ascii=False)+'\n')
checks={'unique_formal_blocks':len({x['id'] for x in R})==len(R),'all_blocks_have_named_unit':all(x['unit_ids'] for x in R),'all_blocks_actual_read_union_complete':all(x['actual_read_range_union_complete'] for x in R),'all_current_reverse_logs_exist':all((P/'logs'/s).exists() for x in R for s in x['fresh_read_logs']),'active_inventory_actual_logged_contiguous_union_complete':not missing,'all_source_segments_named_disposition':all(x['consumer_and_formal_unit_ids'] or x['foreign_disposition_ids'] for x in F),'source_refs_existing_valid':not badrefs,'116_vectors_named_current_parent_bindings':len(rows)==116 and all(all('PENDING' not in by[i]['status'] for i in x['primary_unit_ids']) for x in rows)}
result={'utc':now,'evidence':'TOOL_VALIDATION_ADMINISTRATIVE_ONLY','checks':checks,'missing_actual_logged_ranges':missing,'invalid_refs':badrefs,'units':len(U),'formal_blocks':len(R),'source_read_segments':len(F),'initial_acquisition_log_gaps':'See initial-acquisition-gap-remediation.json; actual subsequent full fresh rereads supply current ranges. Original time/log not fabricated.','reference_functions_executed_by_validation':0,'does_not_establish_semantic_pass':True}
(P/'logs/matrix-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
pending=[{'id':u['id'],'formal_path':u['formal_path'],'lines':[u['start_line'],u['end_line']],'status':u['status']} for u in U if 'PENDING' in u['status']]
(P/'pending-consumer-bindings.json').write_text(json.dumps({'utc':now,'pending_consumer_units':pending,'count':len(pending),'root_adjudications_reserved':['GR6-K-001','GR6-K-002','GR6-K-003','GR6-UI-BAG-001'],'named_host_unknowns_are_not_source_dependency_pending':True},ensure_ascii=False,indent=2)+'\n')
status=json.loads((P/'task-status.json').read_text());status.update({'timestamp':now,'status':'IN_PROGRESS','phase':'DOMAIN_STATIC_REVIEW_COMPLETE_GLOBAL_COUNTER_IN_PROGRESS','bidirectional_consumer_proof_complete':not pending and all(checks.values()),'named_review_units':len(U),'matrix_coverage':json.loads((P/'matrix-coverage.json').read_text()),'pending_consumer_units':pending,'pending_consumer_unit_count':len(pending),'context_vectors_bound':116,'context_vectors_unbound':0,'global_counter_started':True,'domain_work_complete':not pending and all(checks.values()),'remaining_work':['Independent global coverage counter: R432/formal131/20379/supp116/binary/history recoverable proof and residuals','Root non-proposer adjudication of three K proposals; proposer does not mark final required'],'source_unit_count_definition':'181 actual continuous acquisition segments and213 manually authored fact/formal units; not an exhaustive Ruby declaration count'})
(P/'task-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':checks,'vectors':len(rows),'pending':len(pending),'source_segments':len(F),'invalid_refs':badrefs,'missing':missing},ensure_ascii=False))
