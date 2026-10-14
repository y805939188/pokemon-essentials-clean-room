"""Read-only structural audit of explicitly bound historical administrative JSON.
Parses complete blobs recursively, emits shape/leaf inventory and row identity
projections. Never executes repository scripts or labels game semantics passed.
"""
import subprocess,json,pathlib,hashlib,collections,datetime
BASE=pathlib.Path(__file__).resolve().parent
MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
FIFTH='f49d870c6fd616ab6736754a218a4553b5acac7f'
P='review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/'
INPUTS=[
 (MAIN,'delivery/2026-10-11/accepted-history-index.json'),
 (MAIN,'review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/all341-public-source-map.json'),
 (MAIN,'review/remediation/20261003-prepare/FINAL-closure/registration-cloud-20261011-1/all229-closure-records.json'),
 (MAIN,'review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/accepted-341-scope.json'),
 (MAIN,'review/remediation-third-20261012-prepare/registration/final-closure-acceptance.json'),
 (FIFTH,P+'regression-third-23.json'),
 (FIFTH,P+'regression-legacy-scope.json'),
 (MAIN,'review/remediation-fifth-20261013-prepare/integration/R5-U08/candidate-01/historical-regression-input.json')]
objs=[]; inventories=[]
for rev,path in INPUTS:
 b=subprocess.check_output(['git','show',rev+':'+path]);d=json.loads(b);objs.append(d)
 shape=collections.Counter();leaves=[]
 def walk(v,p):
  shape[(p,type(v).__name__)]+=1
  if isinstance(v,dict):
   for k,x in v.items():walk(x,p+'/'+k)
  elif isinstance(v,list):
   for x in v:walk(x,p+'/*')
  else:leaves.append(v)
 walk(d,'')
 inv={'revision':rev,'path':path,'bytes':len(b),'lines':len(b.splitlines()),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':subprocess.check_output(['git','rev-parse',rev+':'+path]).decode().strip(),'root_keys':list(d),'complete_recursive_shape':[{'path':p,'type':t,'occurrences':n} for (p,t),n in sorted(shape.items())],'leaf_count':len(leaves),'mode':'STRUCTURE_FULL_NOT_SEMANTIC_PASS'}
 inventories.append(inv)
 with (BASE/'reading-ledger.jsonl').open('a') as f:f.write(json.dumps({k:v for k,v in inv.items() if k not in ['complete_recursive_shape','root_keys']}|{'range':[1,inv['lines']],'semantic_review':'NOT_CLAIMED','evidence_level':'TOOL_VALIDATION','time':datetime.datetime.now(datetime.timezone.utc).isoformat()})+'\n')
(BASE/'structural-inventory.json').write_text(json.dumps(inventories,indent=2))
index,source,closed,accepted,gr3,reg3,legacy,current=objs
keys=lambda r:tuple(r['exact_identity_key'].get(k) for k in ['batch','id','candidate','actual','independent_report'])
src=source['records'];acc=accepted['full_mapping']
checks={'evidence_level':'TOOL_VALIDATION','not_game_semantic_approval':True,'all341_count':len(src),'all341_unique_tuple_count':len(set(map(keys,src))),'all341_unique_batch_id':len({r['record_key'] for r in src}),'third341_count':len(acc),'third341_exact_tuple_set_equal':set(map(keys,src))==set(map(keys,acc)),'third341_full_row_prefix_equal':all(all(r[k]==s[k] for k in s) for r,s in zip(acc,src)),'229_count':len(closed['records']),'229_distinct_ID_count':len({r.get('id') for r in closed['records']}),'21_batches_count':len(index['batch_records']),'21_sum_contributions':sum(r['contribution_records'] for r in index['batch_records']),'341_by_batch':dict(sorted(collections.Counter(r['exact_identity_key']['batch'] for r in src).items())),'23_active_count':len(gr3['activated_required_ids23']),'23_active_unique_count':len(set(gr3['activated_required_ids23'])),'R3_regression_count':len(reg3['records']),'R3_denominator':reg3['denominator'],'R2_legacy_controls_count':len(legacy['controls']),'R2_legacy_contributions_count':len(legacy['contributions']),'R2_legacy_denominators':legacy['denominators'],'historical_current_records_count':len(current['records'])}
(BASE/'structural-checks.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,ensure_ascii=False,indent=2))
with (BASE/'r2-341-tuples.tsv').open('w') as f:
 f.write('record_index\trecord_key\tbatch\tid\tcandidate\tactual\tindependent_report\tapproval_row\ttraceability_row\tclosure_pointer\n')
 for i,r in enumerate(src):f.write('\t'.join(map(str,[i,r['record_key'],*keys(r),r['approval_data_row_1based'],r['traceability_data_row_1based'],r['current_closure_binding']]))+'\n')
def fields(d):return {k:v for k,v in d.items() if not isinstance(v,(dict,list))}
projection={'regression3_top':{k:v for k,v in reg3.items() if k!='records'},'R3_records':[],'R2_top':{k:v for k,v in legacy.items() if k not in ['controls','contributions','canonical_history_relations']},'R2_controls':[],'R2_contributions':[]}
for i,r in enumerate(reg3['records']):projection['R3_records'].append({'index':i,'scalar_fields':fields(r),'keys':list(r),'denominator':r.get('criteria_count'),'criterion_scalars':[fields(c) for c in r.get('criteria',[])],'identity_scope_reuse':r.get('historical_identity_scope_reuse')})
for i,r in enumerate(legacy['controls']):projection['R2_controls'].append({'index':i,'scalar_fields':fields(r),'keys':list(r),'identity_scope_reuse':r.get('historical_identity_scope_reuse')})
for i,r in enumerate(legacy['contributions']):projection['R2_contributions'].append({'index':i,'scalar_fields':fields(r),'keys':list(r),'identity_scope_reuse':r.get('historical_identity_scope_reuse')})
(BASE/'qualification-projection.json').write_text(json.dumps(projection,ensure_ascii=False,indent=2))
