"""New complete JSON/typed-value reconstruction bookkeeping; not behavior evidence."""
import sys;sys.dont_write_bytecode=True
import pathlib,json,hashlib,importlib.util
D=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location('reader',D/'read_documents.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
docs=json.loads((D/'reading-documents.json').read_text());values=json.loads((D/'reading-values.json').read_text());results=[];failures=[];seen={};duplicates=[]
def value(vi):
 x=values[vi];di,loc=x['first'];v=m.document_value(di)
 for k in loc:v=v[k]
 if 'segment' in x:v=v[x['segment'][0]:x['segment'][1]]
 return v
for di,dm in enumerate(docs):
 raw=m.show(dm['commit'],dm['path']);obj=m.transform(raw,dm);nodes=json.loads((D/dm['nodes_file']).read_text());n=0
 def check(x,loc):
  global n
  node=nodes[n];n+=1
  if node[0]!=loc:failures.append([di,n,'location'])
  if isinstance(x,dict):
   if node[1:]!=['object',list(x)]:failures.append([di,n,'ordered_object'])
   for k,v in x.items():check(v,loc+[k])
  elif isinstance(x,list):
   if node[1:]!=['array',len(x)]:failures.append([di,n,'array'])
   for k,v in enumerate(x):check(v,loc+[k])
  else:
   vi=node[2];typ=type(x).__name__;enc=json.dumps(x,ensure_ascii=False,separators=(',',':')).encode();record=values[vi]
   if node[1]!=typ or record['type']!=typ or record['sha256']!=hashlib.sha256(enc).hexdigest():failures.append([di,n,'typed_scalar'])
   if vi in seen and seen[vi]!=(typ,enc):failures.append([di,n,'exact_reuse_collision'])
   seen[vi]=(typ,enc)
 check(obj,[])
 if n!=len(nodes):failures.append([di,n,'extra_nodes'])
 if dm['format']=='json':
  def pairs(kvs):
   keys=[k for k,v in kvs]
   if len(keys)!=len(set(keys)):duplicates.append(di)
   return dict(kvs)
  json.loads(raw,object_pairs_hook=pairs)
 results.append({'doc_index':di,'commit':dm['commit'],'path':dm['path'],'raw_hash_match':hashlib.sha256(raw).hexdigest()==dm['sha256'],'nodes':n,'mapping_exact':not any(x[0]==di for x in failures),'duplicate_JSON_keys':di in duplicates})
mixed=json.loads((D/'mixed-string-reconstruction-map.json').read_text());segments=[]
for r in mixed['records']:
 original=value(r['parent_value_id']);parts=[value(z['value_id']) for z in r['segments']];ok=''.join(parts)==original and all(original[z['start']:z['end']]==value(z['value_id']) for z in r['segments']);segments.append({'parent_value_id':r['parent_value_id'],'exact_typed_concatenation':ok})
result={'scope':'Complete structural/type/order/identity/reconstruction validation only; model semantic consumption is separately recorded.','documents':results,'scalar_value_count':len(values),'original_value_contexts_checked':len(seen),'failures':failures,'duplicate_JSON_key_documents':duplicates,'mixed_strings':segments,'all_structures_exact':not failures and not duplicates and all(x['raw_hash_match'] for x in results) and all(x['exact_typed_concatenation'] for x in segments)}
(D/'typed-map-verification.json').write_text(json.dumps(result,indent=2)+'\n');print('Documents',len(results),'failures',len(failures),'duplicate key documents',len(set(duplicates)),'mixed reconstruction failures',sum(not x['exact_typed_concatenation'] for x in segments),'all_structures_exact',result['all_structures_exact'])
