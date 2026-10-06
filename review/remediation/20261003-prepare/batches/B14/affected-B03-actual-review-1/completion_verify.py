"""Own full native/document/type/reuse verification; never executes reviewed code."""
import completion_read as R
import json,collections,hashlib,re,pathlib,sys
idx=R.gzload('completion-reading-index.json.gz');claims=idx['claims'];log=json.loads((R.OUT/'completion-consumption.json').read_text());done=set(log['read_claims']);groups=collections.defaultdict(list)
for occ in idx['occurrences']+idx.get('native_scalar_supplement_occurrences',[]):groups[occ[1]].append(occ)
def pairs(items):
 d={}
 for k,v in items:
  assert k not in d,'Duplicate native JSON key'
  d[k]=v
 return d
def no_constant(v):raise AssertionError('Nonstandard native JSON constant')
structs=[];checked=0;values={};doc_results=[]
for di,d in enumerate(idx['documents']):
 b=R.git(d['commit'],d['path']);assert len(b)==d['bytes'] and R.h(b)==d['sha256']
 try:full=json.loads(b,object_pairs_hook=pairs,parse_constant=no_constant)
 except json.JSONDecodeError:full={'literal_lines':b.decode().splitlines(keepends=True)}
 o={s:R.at(full,R.parts(s)) for s in d['selection']} if d['selection'] is not None else full
 scalar=dict(R.scalars(o));nodes=[]
 def graph(v,p=''):
  if isinstance(v,dict):
   nodes.append({'pointer':p,'type':'dict','ordered_keys':list(v),'length':len(v),'empty':not v})
   for k,x in v.items():graph(x,p+'/'+k.replace('~','~0').replace('/','~1'))
  elif isinstance(v,list):
   nodes.append({'pointer':p,'type':'list','length':len(v),'empty':not v})
   for n,x in enumerate(v):graph(x,p+'/'+str(n))
 graph(o);structs.append({'document':di,'identity':{k:d[k] for k in ['commit','path','sha256','bytes']},'native_source_selection':d['selection'],'ordered_containers_and_empty_values':nodes,'scalar_count':len(scalar)})
 hashes={p:R.vh(v) for p,v in scalar.items()};seen=set()
 for occ in groups[di]:
  ci,_,ptr,steps,typ,sha=occ;key=(ci,ptr,json.dumps(steps,separators=(',',':')))
  if key in seen:continue
  seen.add(key);v=scalar[ptr];assert type(v).__name__==typ and hashes[ptr]==sha
  v=R.derive(v,steps);assert type(v).__name__==claims[ci]['type'] and R.vh(v)==claims[ci]['value_sha256'];checked+=1
  if ci in values:assert type(v)==type(values[ci]) and (v==values[ci])
  else:values[ci]=v
 for ci,c in enumerate(claims):
  if c['first']['document']!=di:continue
  r=c['first'];v=R.derive(scalar[r['selector']],r['steps']);assert R.vh(v)==c['value_sha256'];values[ci]=v
 doc_results.append({'document':di,'all_scalar_types_values_contexts_and_transformations_reconstructed':True,'ordered_containers':len(nodes),'native_scalar_count':len(scalar),'unique_occurrence_checks':len(seen),'JSON_duplicate_keys':0})
 print('NATIVE_VERIFIED',di,d['path']) if di%50==0 else None
assert len(values)==len(claims)
reuse=[]
for ci,c in enumerate(claims):
 for field in ['exact_ordered_sentence_spans','exact_ordered_table_text_spans']:
  if field in c:
   v=values[ci];rr=c[field];assert ''.join(v[a:z] for a,z,j in rr)==v
   for a,z,j in rr:assert type(values[j])==str and v[a:z]==values[j]
 p=c['prior_consumed']
 if p and p.get('kind')=='exact_body_substring_already_consumed':
  parent=p['parent_claim'];a,z=p['exact_span']
  assert type(values[ci])==str and values[parent][a:z]==values[ci],('REUSE_LINK',ci,parent,[a,z],len(str(values[ci])),len(str(values[parent])),R.vh(values[ci]),R.vh(values[parent]))
  assert parent in done or claims[parent]['prior_consumed'];reuse.append(ci)
 if p and p.get('kind')=='same_task_consumed_parent':assert p['parent_claim'] in done
remainder=[n for n,c in enumerate(claims) if not c['metadata_only'] and not c['prior_consumed'] and n not in done];assert not remainder
snapshot=json.loads((R.OUT/'preliminary-turn-1/snapshot-manifest.json').read_text())
for d in snapshot['files']:
 b=(R.OUT/'preliminary-turn-1'/d['path']).read_bytes();assert R.h(b)==d['sha256'] and len(b)==d['bytes']
for n,h in [('independent-first-judgment.md','4d281d2f2b849df89d3ece67356d38c5bbb42957cf252eb60020fad0208bc393'),('first-judgment-receipt.json','1708eedfbd1b2f721385df94be7b99714636c510edb7a7875d8144599b7a701b')]:assert R.h((R.OUT/n).read_bytes())==h
R.save('completion-native-structures.json.gz',structs)
result={'documents':doc_results,'unique_claims':len(claims),'complete_occurrence_checks':checked,'all_native_scalar_types_values_and_contexts_verified':True,'all_native_ordered_containers_and_empty_values_retained':True,'all_lossless_span_concatenations_verified':True,'exact_body_reuse_checked':reuse,'semantic_remainder':[],'semantic_reading_basis':'Same-review model consumption recorded by immutable initial receipt and subsequent acknowledged stable claim IDs; reconstruction is separate bookkeeping, not behavior evidence.','preliminary_snapshot_26_exact_bytes_preserved':True,'first_judgment_and_receipt_exact_bytes_preserved':True,'runtime_observations':0,'proven_Demo':0,'behavior_vectors_executed':0,'historical_or_reference_program_execution':0}
R.save('completion-native-verification.json.gz',result);log['complete']=True;log['native_verification']='completion-native-verification.json.gz';log['literal_programs_read']=idx['program_documents'];R.save('completion-consumption.json',log);print('COMPLETE_NATIVE_RECONSTRUCTION',len(claims),checked)
