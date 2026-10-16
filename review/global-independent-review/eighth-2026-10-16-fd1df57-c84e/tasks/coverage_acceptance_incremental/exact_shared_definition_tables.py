"""Exact reversible factoring of shared-definition dictionaries, no reading credit."""
import collections, datetime, hashlib, json, sys
from pathlib import Path
OWN=Path(__file__).resolve().parent
relative,label=sys.argv[1:]
assert '/' not in label and '..' not in label
src=OWN/relative;assert src.resolve().is_relative_to(OWN)
start=datetime.datetime.now(datetime.timezone.utc).isoformat();raw=src.read_bytes();original=json.loads(raw)
assert 'shared_definitions' in original

def canonical(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def enc(x):
 if isinstance(x,dict):
  assert '$exact_definition_table_groups' not in x and '$dictionary_order' not in x
  return {k:enc(v) for k,v in x.items()}
 if isinstance(x,list):return [enc(v) for v in x]
 return x

def factor(defs):
 groups=collections.OrderedDict();singles={}
 for k,v in defs.items():
  if isinstance(v,dict):groups.setdefault(tuple(v),[]).append((k,v))
  else:singles[k]=enc(v)
 tables=[]
 for fields,rows in groups.items():
  if len(rows)<2:
   for k,v in rows:singles[k]=enc(v)
   continue
  common={f:rows[0][1][f] for f in fields if all(canonical(v[f])==canonical(rows[0][1][f]) for _,v in rows)}
  columns=[f for f in fields if f not in common]
  tables.append({'common_fields_for_every_definition':enc(common),'varying_columns_after_definition_key':columns,'rows':[[k]+[enc(v[f]) for f in columns] for k,v in rows]})
 return {'$exact_definition_table_groups':tables,'single_definitions':singles,'$dictionary_order':list(defs)}

encoded=enc(original);encoded['shared_definitions']=factor(original['shared_definitions'])
def dec(x):
 if isinstance(x,dict):
  if set(x)=={'$exact_definition_table_groups','single_definitions','$dictionary_order'}:
   values={k:dec(v) for k,v in x['single_definitions'].items()}
   for t in x['$exact_definition_table_groups']:
    common=dec(t['common_fields_for_every_definition'])
    for row in t['rows']:values[row[0]]=dict(common,**dict(zip(t['varying_columns_after_definition_key'],[dec(v) for v in row[1:]])))
   return {k:values[k] for k in x['$dictionary_order']}
  return {k:dec(v) for k,v in x.items()}
 if isinstance(x,list):return [dec(v) for v in x]
 return x
assert dec(encoded)==original

def emit(v,d=0,rows=False):
 pad=' '*d
 if isinstance(v,dict):
  if not v:return '{}'
  return '{\n'+',\n'.join(' '*(d+1)+json.dumps(k,ensure_ascii=False)+': '+emit(w,d+1,k=='rows') for k,w in v.items())+'\n'+pad+'}'
 if isinstance(v,list):
  if not v:return '[]'
  if rows:return '[\n'+',\n'.join(' '*(d+1)+(json.dumps(w,ensure_ascii=False,separators=(',',':')) if len(canonical(w))<=2400 else emit(w,d+1)) for w in v)+'\n'+pad+']'
  if all(not isinstance(w,(dict,list)) for w in v):return json.dumps(v,ensure_ascii=False)
  return '[\n'+',\n'.join(' '*(d+1)+emit(w,d+1) for w in v)+'\n'+pad+']'
 return json.dumps(v,ensure_ascii=False)

out=OWN/(label+'-definition-tables-view.json');assert not out.exists()
text=emit(encoded)+'\n';assert json.loads(text)==encoded;out.write_text(text)
proof={'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0,'input':relative,'input_bytes':len(raw),'input_sha256':hashlib.sha256(raw).hexdigest(),'output':out.name,'bytes':len(text.encode()),'lines':len(text.splitlines()),'sha256':hashlib.sha256(text.encode()).hexdigest(),'all_decode_equals_input':True,'generation_reading_credit':0,'source_semantic_credit':0,'business':'NOT_EXECUTED'}
(OWN/(label+'-definition-tables-generation.json')).write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
