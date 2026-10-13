"""Integrate manual scope assessments and exact fresh evidence, preserving incomplete gates."""
from current_evidence import *
D=json.loads((HERE/'regression-legacy-scope.json').read_text());A=json.loads((HERE/'scope-assessments.json').read_text())['records'];O=json.loads((HERE/'original-comparison-joins.json').read_text());S=json.loads((HERE/'fresh-source-ledger.json').read_text());H=json.loads((HERE/'history-relations.json').read_text())
progress={}
for m in ['M01','M02','M03','M04','M05','M06','M07','M08','M09','M10','M11','M12','M12B','C00']:
 p=HERE.parent/m/'progress.json'
 if not p.exists():continue
 raw=p.read_bytes();d=json.loads(raw);ready=d.get('complete',d.get('status')=='complete') is True
 if m=='C00':ready=d.get('own_semantic_fields_complete',False) is True
 progress[m]={'file':str(p.relative_to(ROOT)),'sha256':digest(raw),'primary_complete':d.get('complete'),'bounded_current_field_gate_satisfied':ready,'qualification':'C00 own semantic fields only; remaining global integration not borrowed' if m=='C00' else 'Primary completion retained; candidate partial/missing/unresolved are findings, not unread scope'}
def owner(path):
 n=Path(path).name
 if n in ['README.md','scope-statement.md']:return 'C00'
 mat=re.match(r'wp(\d+)',n)
 if not mat:return 'C00'
 wp=int(mat[1])
 if wp in [1]:return 'C00'
 if wp in [2,3,4,8]:return 'M01'
 if wp in [5,6,7,9,10]:return 'M02'
 if wp in [11,12,13,14,59,60,61]:return 'M03'
 if wp in [15,16,17,65,66,67]:return 'M10'
 if wp in range(18,24):return 'M04'
 if wp in [24,25,26,27,28,29,64]:return 'M05'
 if wp in range(30,39):return 'M06'
 if wp in [39,40,41,42,45]:return 'M07' if wp!=45 else 'M08'
 if wp in [43,44,46,47,48,49,50]:return 'M08'
 if wp in range(51,59):return 'M09'
 if wp in [62,63,68,69,70,71]:return 'M11'
 if wp==75:return 'M12'
 return 'M12B'
orig_byformal={}
for i,r in enumerate(O['records']):
 if r['current_formal']:orig_byformal.setdefault(r['current_formal'],[]).append((i,r))
admin={('B01','GIR-FD82-001'),('B01','WP80-B02-R02'),('B02','GIR-FD82-A017'),('B18','GIR-FD82-001'),('B18','WP80-INTAKE-R02'),('B21','GIR-FD82-001'),('B21','GIR-FD82-A017'),('B21','WP80-B02-R02'),('B21','WP80-INTAKE-C01'),('B21','WP80-INTAKE-R02')}
for r in D['contributions']:
 key=r['record_key'];cr=r['current_R5_semantic_review'];nav=r['current_B5_navigation'];a=A[key];qual_only=(r['batch_owner'],r['id']) in admin
 paths=list(dict.fromkeys(x['path'] for x in nav['clause_candidates'] if x['path'].startswith('deliverables/') and '/test-catalog/' not in x['path']))
 primary=sorted(set(owner(p) for p in paths)) or (['C00'] if qual_only else [])
 if r['batch_owner']=='B21':primary=sorted(set(primary+['C00']))
 original=[];pending=[]
 for p in paths:
  if Path(p).name in ['README.md','scope-statement.md']:continue
  candidates=orig_byformal.get(p,[])
  if not candidates:pending.append({'status':'not_reviewed','path':p,'reason':'Exact current-to-original receiver join not yet available; not missing_material.'})
  for i,o in candidates:
   original.append({'file':'original-comparison-joins.json','pointer':f'/records/{i}','original':o['original'],'primary_evidence':o['primary_evidence'],'result':o['status'],'boundary':'Detailed fresh original-to-current disposition reviewed; not inherited original approval.'})
   if o['status']=='not_reviewed':pending.append({'status':'not_reviewed','path':o['original'],'reason':'Fresh original comparison not closed'})
 for m in primary:
  if not progress.get(m,{}).get('bounded_current_field_gate_satisfied'):pending.append({'status':'not_reviewed','module':m,'path':progress.get(m,{}).get('file',str((HERE.parent/m/'progress.json').relative_to(ROOT))),'reason':'Primary exact evidence mapping/completion gate pending; actual available scoped comparison retained, NOT missing_material.'})
 if not cr['fresh_evidence_joins'] and not cr.get('current_qualification_evidence'):pending.append({'status':'not_reviewed','record_key':key,'reason':'No exact fresh inverse or current-qualification record joined'})
 if not qual_only and not cr.get('fresh_source_fact_refs'):pending.append({'status':'not_reviewed','record_key':key,'reason':'Required current source fact/ledger join pending'})
 cr.update({'status':'not_reviewed' if pending else a['status'],'evidence_level':a['evidence_level'],'manual_scope_comparison':a['current_behavior_comparison'],'scope_boundary':a['qualified_scope_boundary'],'manual_assessment_pointer':'scope-assessments.json#/records/'+esc(key) if 'esc' in globals() else 'scope-assessments.json#/records/'+key.replace('/','~1'),'source_review_method':'REG actual direct finite source/spec review for GR3/GR4; legacy scopes tied to current primary source-first semantic records, with difference rereads logged. Never historic verdict transfer.','current_primary_owners':primary,'primary_progress_gates':[progress[m] for m in primary if m in progress],'original_comparison_joins':original,'pending_joins':pending,'mapping_complete':not pending,'scope_review_complete':True,'scope_kind':'qualified_navigation_or_historical_identity_control' if qual_only else 'qualified_behavioral_contribution','not_product_capability':True,'execution_status':'NOT_EXECUTED_BY_REG','related_current_findings':[h['finding_id'] for h in H['records'] if any(x['record_key']==key for x in h['qualified_contributions'])]})
 cr['reason']='All explicitly qualified local behaviors/current clauses and fresh source evidence joined; supported_static is finite only.' if not pending else 'Explicit pending joins remain; manual bounded comparison is not promoted into a complete main-module signature.'
 a['evidence_join_complete']=not pending
# Central role may consume other contributions, but never transfer their old acceptance.
bykey={r['record_key']:r for r in D['contributions']}
for r in D['contributions']:
 if r['batch_owner']!='B21' or (r['batch_owner'],r['id']) in admin:continue
 cr=r['current_R5_semantic_review']
 for j in r.get('delegated_consumer_contributions',[]):
  other=bykey[j['record_key']]['current_R5_semantic_review']
  if not other['mapping_complete']:cr['pending_joins'].append({'status':'not_reviewed','record_key':j['record_key'],'pointer':j['pointer'],'reason':'Current R5 consumer projection still has exact pending joins; no transitive historical acceptance.'})
 cr['mapping_complete']=not cr['pending_joins'];cr['status']=A[r['record_key']]['status'] if cr['mapping_complete'] else 'not_reviewed'
for c in D['controls']:
 subs=[(i,r) for i,r in enumerate(D['contributions']) if r['id']==c['id']];pending=[{'record_key':r['record_key'],'pointer':f'/contributions/{i}','pending_joins':r['current_R5_semantic_review']['pending_joins']} for i,r in subs if not r['current_R5_semantic_review']['mapping_complete']]
 states={r['current_R5_semantic_review']['status'] for i,r in subs};status='not_reviewed' if pending else ('partial' if 'partial' in states else ('unresolved' if 'unresolved' in states else 'supported'))
 c['current_R5_semantic_review'].update({'status':status,'evidence_level':'supported_static' if status=='supported' else 'STATIC_SCOPE_REVIEW','mapping_complete':not pending,'qualified_scope_rollup':[{'record_key':r['record_key'],'pointer':f'/contributions/{i}','status':r['current_R5_semantic_review']['status']} for i,r in subs],'pending_joins':pending,'reason':'All scoped contributions must join current evidence; whole control never inherits a single local acceptance. Navigation/admin constraints are not product features.','related_current_findings':[h['finding_id'] for h in H['records'] if any(x['id']==c['id'] for x in h['legacy_controls'])]})
D['complete']=False;D['mapping_complete']=all(c['current_R5_semantic_review']['mapping_complete'] for c in D['controls']);D['primary_evidence_snapshots']='fresh-evidence-snapshots.json';D['source_ledger_snapshots']='fresh-source-ledger.json';D['manual_scope_assessments']='scope-assessments.json';D['original_comparisons']='original-comparison-joins.json';D['history_relationships']='history-relations.json';D['qualification_preservation']='All original ID/batch/candidate/actual/acceptance references, whole original/approved controls, local scope and READ_ONLY/NOT_AFFECTED qualification retained. Parent CURRENT resolves retired admin status. No old verdict transfer.'
save('regression-legacy-scope.json',D)
Ad=json.loads((HERE/'scope-assessments.json').read_text());Ad['records']=A;Ad['matrix_complete']=True;Ad['complete']=False;save('scope-assessments.json',Ad)
for fn in ['original-comparison-joins.json','history-relations.json']:
 x=json.loads((HERE/fn).read_text());x['matrix_complete']=x.get('matrix_complete',x['complete']);x['complete']=False;save(fn,x)
from collections import Counter
print('Contributions',dict(Counter(r['current_R5_semantic_review']['status'] for r in D['contributions'])))
print('Controls',dict(Counter(r['current_R5_semantic_review']['status'] for r in D['controls'])))
print('Pending distinct', sorted(set((p.get('module',''),p.get('path',''),p.get('reason','')) for r in D['contributions'] for p in r['current_R5_semantic_review']['pending_joins'] if 'record_key' not in p)))
