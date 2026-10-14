from pathlib import Path
import json,collections,datetime
P=Path(__file__).parent;B=P.parents[2];REF='reference/pokemon-essentials/'
def get(n):return json.loads((B/n).read_text())
cache={}
def pay(p):
 if p not in cache:cache[p]=[json.loads(x)for x in p.read_text().splitlines()if x.strip()]if p.suffix=='.jsonl'else json.loads(p.read_text())
 return cache[p]
def ptr(j,sp):
 for k in sp.split('/')[1:]:
  k=k.replace('~1','/').replace('~0','~');j=j[int(k)]if isinstance(j,list)else j[k]
 return j
fk=['new_fact','named_fact','fact','semantic_read_record','behavior','behavioral_fact','meaning','assessment','new_review_evidence','explicit_semantic_records','linked_fact_ids','core_source_fact_records','human_fact_ids']
ck=['necessary_consumer_refs','necessary_consumer','necessary_consumers','consumer','consumers','consumer_locations','consumer_clauses','formal','formal_path','formal_clauses','formal_destination','consumer_and_formal_unit_ids','foreign_disposition_ids','source_fact_receiver','primary','explicit_semantic_records','formal_clause']
points=get('tasks/R6-K/global-coverage-counter/source-pointer-index.json');group=collections.defaultdict(list)
for x in points:
 if 'reading-ledger'in x['artifact']:continue
 j=pay(B/x['artifact']);sp=x['json_pointer'];chosen=None
 while True:
  q=ptr(j,sp)
  if isinstance(q,dict)and any(q.get(k)for k in fk)and any(q.get(k)for k in ck):chosen={'artifact':x['artifact'],'source_pointer':x['json_pointer'],'parent_fact_pointer':sp,'source_range':x['range'],'fact_fields':{k:q[k]for k in fk if q.get(k)},'consumer_formal_fields':{k:q[k]for k in ck if q.get(k)},'actual_semantics_not_verified_by_script':True};break
  if not sp:break
  sp=sp.rsplit('/',1)[0]
 if chosen and len(group[x['path']])<4:group[x['path']].append(chosen)
# compressed bulk and binary have exact bounded author/resource receipts, not bogus prose citations.
specialcounts=get('tasks/R6-K/global-coverage-counter/finite-contract-special-path-counts.json');bulkcounts=get('tasks/R6-K/global-coverage-counter/finite-contract-bulk-path-counts.json');localcounts=get('tasks/R6-K/global-coverage-counter/finite-contract-local-path-counts.json');bins={x['path']:x for x in get('tasks/R6-K/global-coverage-counter/binary18-scope-bindings.json')};ranges={x['path']:x for x in get('tasks/R6-K/global-coverage-counter/range-results.json')};owners={REF+x['path']:x['primary_reader']for x in get('control/source-primary-ownership.json')};out=[];unbound=[]
for x in get('inventory/reference.json'):
 path=REF+x['path'];chain=group[path];kind='EXACT_CURRENT_SOURCE_UNIT_FACT_CONSUMER_FORMAL_POINTERS'
 if path in specialcounts:kind='FINITE_ALL_SPECIAL_RECORD_FIELD_RULE_CONSUMER_FORMAL_BINDING';chain=[{'record_field_units':specialcounts[path],'artifact':'tasks/R6-D/source-to-spec-matrix.jsonl','manual_rules':'tasks/R6-D/manual-rule-catalog.json','rule_consumer_counter':'tasks/R6-K/global-coverage-counter/finite-contract-summary.json'}]+chain
 if path in bulkcounts:kind='FINITE_ALL_RECORD_AUTHOR_RULE_CONSUMER_FORMAL_BINDING';chain=[{'records':bulkcounts[path],'artifact':'tasks/R6-D/pbs-bulk/source-to-spec-matrix.json.gz','decode_receipt':'tasks/R6-D/pbs-bulk/source-to-spec-matrix.json','rule_consumer_counter':'tasks/R6-K/global-coverage-counter/finite-contract-summary.json'}]+chain
 if x['path']in localcounts:kind='ALL_CURRENT_LOCALIZATION_BODY_UNIT_ACCEPTANCE_FACT_CONSUMER_FORMAL';chain=[{'records':localcounts[x['path']],'artifact':'tasks/R6-D/localization/source-to-formal.json','unit_acceptance_counter':'tasks/R6-K/global-coverage-counter/finite-contract-summary.json'}]+chain
 if path in bins:kind='NAMED_BINARY_FINITE_STRUCTURE_PROGRAM_OR_NATIVE_LIMIT_DISPOSITION';chain=[bins[path]]
 if x['path']in ['.gitignore','.rubocop.yml','README.md','LICENSE','Essentials Engine wiki.url']:
  kind='FULL_CURRENT_METADATA_PURPOSE_TYPE_DISPOSITION';chain=[{'artifact':'tasks/R6-B/controller-meta/forward-matrix.json','report':'tasks/R6-B/report.md:25','scope':'Metadata full current text purpose only, no game rule/legal/external URL result','actual_range_receipts':ranges[path]['current_range_receipts']}]
 if not chain:unbound.append(path)
 rr=ranges[path];out.append({'path':path,'primary_reader':owners[path],'input_sha256':x['sha256'],'type_disposition':kind,'actual_range_receipts_artifact':'tasks/R6-K/global-coverage-counter/range-results.json','actual_text_gap_ranges':rr['actual_read_gap_ranges'],'structural_all_gap_ranges':rr['all_declared_range_gap_ranges'],'recoverable_source_fact_consumer_formal_or_named_disposition':chain,'not_independent_global_behavior_PASS':True})
(P/'source432-chain-recovery.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');s={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reference_files':len(out),'named_source_chain_or_finite_type_disposition':len(out)-len(unbound),'unbound_files':unbound,'classification_counts':dict(collections.Counter(x['type_disposition']for x in out)),'all_source_bodies_not_newly_reread_by_K_counter':True};(P/'source-chain-summary.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n');print(json.dumps(s,ensure_ascii=False))
