"""Verify thin successor member/metadata pointers only."""
from pathlib import Path
import collections,datetime,hashlib,json
OUT=Path(__file__).resolve().parent;BASE=OUT.parent;RR=BASE.parents[2]
def sha(b):return hashlib.sha256(b).hexdigest()
def read(n):return json.loads((OUT/n).read_bytes())
def put(n,d):(OUT/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
start=datetime.datetime.now(datetime.timezone.utc).isoformat();ins=read('inputs.json')['inputs'];docs={}
for x in ins:
 p=RR/x['path'];raw=p.read_bytes();assert len(raw)==x['bytes'] and sha(raw)==x['sha256'],x['path'];docs[x['path']]=json.loads(raw)
def resolve(n,p):
 d=docs[n]
 for k in p.split('/')[1:]:
  k=k.replace('~1','/').replace('~0','~');d=d[int(k)]if isinstance(d,list)else d[k]
 return d
checks=collections.Counter()
for x in read('pointer-bindings.json')['bindings']:
 v=resolve(x['artifact'],x['pointer']);assert sha(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())==x['value_sha256_canonical_JSON'];checks['bound_record_or_field_pointers']+=1
for name in ['paths-563.json','overrides-33.json','catalog-readers-17.json','root-receipts-current.json']:
 d=read(name)
 def w(v):
  if isinstance(v,dict):
   if 'artifact'in v and 'pointer'in v and v['artifact']in docs:
    value=resolve(v['artifact'],v['pointer']);checks['all_exported_metadata_pointer_refs']+=1
    if 'original_value'in v:assert value==v['original_value'];checks['exact_exported_original_values']+=1
   for x in v.values():w(x)
  elif isinstance(v,list):
   for x in v:w(x)
 w(d)
thin=read('paths-563.json');ov=read('overrides-33.json')['rows'];cat=read('catalog-readers-17.json')['rows'];reg=read('root-receipts-current.json')
assert len(thin['rows'])==563 and len({(x['kind'],x['path'])for x in thin['rows']})==563
assert len(ov)==33 and len({(x['kind'],x['path'])for x in ov})==33
assert len(cat)==17 and len({x['path']for x in cat})==17
assert reg['count']==len(reg['receipts'])==29
assert sum('resource_scope'in x for x in thin['rows'])==18
assert all(x['semantic_PASS']is None and not x['personal_FULL_added']for x in thin['rows'])
ids=set();domains=set();reader_instances=collections.Counter()
for o in ov:
 if not o['path'].startswith('Text_english_core/'):continue
 domain=Path(o['path']).stem;domains.add(domain)
 for b in o['actual_reader_bindings']:
  actor=resolve(b['actor_pointer']['artifact'],b['actor_pointer']['pointer']);assert actor==b['actor_original']
  records=resolve(b['reading_array_pointer']['artifact'],b['reading_array_pointer']['pointer']);nav=0
  for a,z in b['exact_array_index_runs']:
   for i in range(a,z+1):
    x=records[i];assert x['domain']==domain
    if 'reader_context'in x:assert x['reader_context']==actor
    assert x['id']not in ids,x['id'];ids.add(x['id']);reader_instances[actor]+=1;nav+=1
  assert nav==b['navigation_pair_count_not_atoms'];checks['exact_original_reader_domain_ID_bindings']+=nav
assert len(domains)==18 and len(ids)==10697
for o in ov:
 for b in o['actual_reader_bindings']:
  if 'raw_path_pointer'in b:assert resolve(b['raw_path_pointer']['artifact'],b['raw_path_pointer']['pointer'])==o['path'];checks['trainer_rawpath_to_full_lossless_view_joins']+=1
for c in cat:
 p=c['actual_original_text_reading']['record_pointer'];n=c['actual_original_text_reading']['artifact'];x=resolve(n,p)
 original=x.get('path',x.get('payload',x.get('identity_path',x.get('identity',{}).get('path'))));assert original==c['path'];checks['catalog_exact_path_original_reader_joins']+=1
 assert c['reader_fields_original']
 for r in c['reader_fields_original']:assert isinstance(r['original_value'],str) and r['original_value'].startswith('/root/')
manifest=docs['tasks/com_move/integration-membership/delivery-manifest.json']
for x in manifest['files']:
 raw=(BASE/x['path']).read_bytes();assert len(raw)==x['bytes']and sha(raw)==x['sha256']
out={'schema':'gr8-thin-final-current-full-mechanical-verification/v1','start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0,'input_identities_exact':len(ins),'fixed_paths':563,'overrides':33,'catalogs':17,'root_receipts':29,'checks':dict(checks),'localization_original_reader_partition_counts_navigation_only':dict(reader_instances),'old50payloads_unchanged':True,'unknown':len(read('unknown.json')['unknown']),'new_contexts':0,'new_votes':0,'new_source_or_semantic_reading_credit':0,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'global_PASS_granted':False}
put('mechanical-verification.json',out);print(json.dumps(out,ensure_ascii=False))
