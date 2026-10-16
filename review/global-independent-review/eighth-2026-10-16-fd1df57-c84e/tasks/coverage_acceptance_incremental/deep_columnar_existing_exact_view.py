"""Reversible JSON display factoring nested common fields of same-shape rows.
No target code is imported or executed. This only preserves JSON values in a
shorter reading aid. The decoder equality check grants no reading/semantic credit.
"""
import json,datetime,hashlib,sys,re
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent
relative=sys.argv[1];index='OWN_EXACT_COMPONENT_VIEW';label=sys.argv[2];assert re.fullmatch('[a-z0-9-]+',label)
start=datetime.datetime.now(datetime.timezone.utc).isoformat();src=P/relative;assert src.resolve().is_relative_to(P);raw=src.read_bytes();r={'original_path':relative,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'git_blob':'N/A_OWN_EXACT_COMPONENT_VIEW','captured_utc':'N/A_DERIVED_VIEW_IDENTITY_NOT_ORIGINAL_CAPTURE'};original=json.loads(raw)
def canonical(v):return json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def encode(v):
 if isinstance(v,dict):
  assert '$exact_nested_table' not in v and '$exact_varying_column' not in v
  return {k:encode(x) for k,x in v.items()}
 if isinstance(v,list):
  if len(v)>=2 and all(isinstance(x,dict) and set(x)==set(v[0]) for x in v):
   paths=[]
   def template(vs,path=()):
    if all(canonical(x)==canonical(vs[0]) for x in vs):return encode(vs[0])
    if all(isinstance(x,dict) and set(x)==set(vs[0]) for x in vs):return {k:template([x[k] for x in vs],path+(k,)) for k in vs[0]}
    col=len(paths);paths.append(path);return {'$exact_varying_column':col}
   t=template(v)
   def at(x,path):
    for k in path:x=x[k]
    return x
   return {'$exact_nested_table':{'template_common_fields_apply_to_every_row':t,'columns_exact_paths':[list(path) for path in paths],'rows_in_original_order':[[encode(at(x,path)) for path in paths] for x in v]}}
  return [encode(x) for x in v]
 return v
def decode(v):
 if isinstance(v,dict):
  if set(v)=={'$exact_nested_table'}:
   t=v['$exact_nested_table']
   def fill(x,row):
    if isinstance(x,dict):
     if set(x)=={'$exact_varying_column'}:return decode(row[x['$exact_varying_column']])
     if set(x)=={'$exact_nested_table'}:return decode(x)
     return {k:fill(y,row) for k,y in x.items()}
    if isinstance(x,list):return [fill(y,row) for y in x]
    return x
   return [fill(t['template_common_fields_apply_to_every_row'],row) for row in t['rows_in_original_order']]
  return {k:decode(x) for k,x in v.items()}
 if isinstance(v,list):return [decode(x) for x in v]
 return v
encoded=encode(original);assert decode(encoded)==original
view={'schema':'gr8-exact-nested-common-json-reading-view/v1','qualification':'Each template literal applies to every row. A varying marker selects the declared row cell, whose exact JSON value follows. Full decode equals original. Generation0reading/source/atomic/task credit.','source':{k:r[k] for k in ['original_path','bytes','sha256','git_blob','captured_utc']},'value':encoded}
def emit(v,d=0,compact=False):
 pad=' '*d
 if isinstance(v,dict):return '{\n'+',\n'.join(' '*(d+1)+json.dumps(k,ensure_ascii=False)+': '+emit(x,d+1,k=='rows_in_original_order') for k,x in v.items())+'\n'+pad+'}'
 if isinstance(v,list):
  if not v:return '[]'
  if compact:return '[\n'+',\n'.join(' '*(d+1)+(json.dumps(x,ensure_ascii=False,separators=(',',':')) if len(json.dumps(x,ensure_ascii=False))<1800 else emit(x,d+1)) for x in v)+'\n'+pad+']'
  if all(not isinstance(x,(list,dict)) for x in v):return json.dumps(v,ensure_ascii=False)
  return '[\n'+',\n'.join(' '*(d+1)+emit(x,d+1) for x in v)+'\n'+pad+']'
 return json.dumps(v,ensure_ascii=False)
out=P/(label+'-deep-columnar-view.json');assert not out.exists();data=(emit(view)+'\n').encode();assert json.loads(data)==view;out.write_bytes(data)
proof={'begin_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':index,'source_sha256':r['sha256'],'output':out.name,'bytes':len(data),'lines':len(data.splitlines()),'sha256':hashlib.sha256(data).hexdigest(),'exact_decode_equals_original':True,'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'}
(P/(label+'-deep-columnar-generation.json')).write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
