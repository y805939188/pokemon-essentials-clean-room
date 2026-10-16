"""Own reversible text dictionary plus nested-common display of static JSON.
Every literal definition and every ordered binding still requires actual reading.
No source code is imported/evaluated. Generation grants0 reading/acceptance.
"""
import json,hashlib,datetime,re,sys
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;index=int(sys.argv[1]);label=sys.argv[2];assert re.fullmatch('[a-z0-9-]+',label);start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=json.loads((P/'reading-ledger.json').read_text())['snapshot_payloads'][index];raw=(B/r['snapshot']).read_bytes();assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'];original=json.loads(raw);texts=[];lookup={}
def encstrings(v):
 if isinstance(v,str):
  if v not in lookup:lookup[v]=len(texts);texts.append(v)
  return {'$literal_string_index':lookup[v]}
 if isinstance(v,dict):
  assert '$literal_string_index' not in v and '$exact_nested_table' not in v and '$exact_varying_column' not in v
  return {k:encstrings(x) for k,x in v.items()}
 if isinstance(v,list):return [encstrings(x) for x in v]
 return v
def canonical(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def encode(v):
 if isinstance(v,dict):return {k:encode(x) for k,x in v.items()}
 if isinstance(v,list):
  if len(v)>=2 and all(isinstance(x,dict) and set(x)==set(v[0]) for x in v):
   paths=[]
   def template(vs,path=()):
    if all(canonical(x)==canonical(vs[0]) for x in vs):return encode(vs[0])
    if all(isinstance(x,dict) and set(x)==set(vs[0]) for x in vs):return {k:template([x[k] for x in vs],path+(k,)) for k in vs[0]}
    col=len(paths);paths.append(list(path));return {'$exact_varying_column':col}
   t=template(v)
   def at(x,path):
    for k in path:x=x[k]
    return x
   return {'$exact_nested_table':{'template_common_fields_apply_to_every_row':t,'columns_exact_paths':paths,'rows_in_original_order':[[encode(at(x,path)) for path in paths] for x in v]}}
  return [encode(x) for x in v]
 return v
def decode(v):
 if isinstance(v,dict):
  if set(v)=={'$literal_string_index'}:return texts[v['$literal_string_index']]
  if set(v)=={'$exact_nested_table'}:
   t=v['$exact_nested_table']
   def fill(x,row):
    if isinstance(x,dict):
     if set(x)=={'$exact_varying_column'}:return decode(row[x['$exact_varying_column']])
     if set(x)=={'$exact_nested_table'} or set(x)=={'$literal_string_index'}:return decode(x)
     return {k:fill(y,row) for k,y in x.items()}
    if isinstance(x,list):return [fill(y,row) for y in x]
    return x
   return [fill(t['template_common_fields_apply_to_every_row'],row) for row in t['rows_in_original_order']]
  return {k:decode(x) for k,x in v.items()}
 if isinstance(v,list):return [decode(x) for x in v]
 return v
encoded=encode(encstrings(original));assert decode(encoded)==original
view={'schema':'gr8-exact-literal-string-dictionary-nested-table/v1','qualification':'Every exact literal string and every ordered binding requires actual reading. Literal string index markers select texts listed once below; nested common fields apply to every row and varying cells follow declared paths. Complete exact decode equals original. Generation0reading/source/formal/semanticcredit.','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'literal_string_columns':['index','exact_original_string'],'literal_strings':[[i,s] for i,s in enumerate(texts)],'complete_field_bindings':encoded}
def emit(v,n=0,compact=False):
 if isinstance(v,dict):return '{\n'+',\n'.join(' '*(n+1)+json.dumps(k,ensure_ascii=False)+': '+emit(x,n+1,k in ['literal_strings','rows_in_original_order']) for k,x in v.items())+'\n'+' '*n+'}'
 if isinstance(v,list):
  if not v:return '[]'
  if compact:return '[\n'+',\n'.join(' '*(n+1)+(json.dumps(x,ensure_ascii=False,separators=(',',':')) if len(json.dumps(x,ensure_ascii=False))<1400 else emit(x,n+1)) for x in v)+'\n'+' '*n+']'
  if all(not isinstance(x,(dict,list)) for x in v):return json.dumps(v,ensure_ascii=False)
  return '[\n'+',\n'.join(' '*(n+1)+emit(x,n+1) for x in v)+'\n'+' '*n+']'
 return json.dumps(v,ensure_ascii=False)
data=(emit(view)+'\n').encode();assert json.loads(data)==view;name=label+'-exact-dictionary-view.json';assert not(P/name).exists();(P/name).write_bytes(data);proof={'begin_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':index,'source_sha256':r['sha256'],'output':name,'bytes':len(data),'lines':len(data.splitlines()),'sha256':hashlib.sha256(data).hexdigest(),'unique_literal_strings':len(texts),'all_current_JSON_fields_exact_reconstruction':True,'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'};(P/(label+'-exact-dictionary-generation.json')).write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
