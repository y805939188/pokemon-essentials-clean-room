"""Own complete static JSON field dictionaries for top-level record tables.
Every unique complete field value and every original row binding requires actual
reading. Exact reconstruction asserts data preservation, grants0reading/approval.
"""
import json,hashlib,datetime,re,sys
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;n=int(sys.argv[1]);label=sys.argv[2];assert re.fullmatch('[a-z0-9-]+',label);start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=json.loads((P/'reading-ledger.json').read_text())['snapshot_payloads'][n];raw=(B/r['snapshot']).read_bytes();assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'];original=json.loads(raw);assert isinstance(original,dict);out={};rebuilt={}
for k,v in original.items():
 if isinstance(v,list) and v and all(isinstance(x,dict) for x in v):
  keys=list(dict.fromkeys(f for x in v for f in x));pool={f:[] for f in keys};look={f:{} for f in keys};rows=[]
  for x in v:
   row=[]
   for f in keys:
    if f not in x:row.append(-1);continue
    sig=json.dumps(x[f],ensure_ascii=False,sort_keys=True,separators=(',',':'))
    if sig not in look[f]:look[f][sig]=len(pool[f]);pool[f].append(x[f])
    row.append(look[f][sig])
   rows.append(row)
  table={'qualification':'-1 means original field absent, not null. Other integers select complete value in same-named field dictionary. Every dictionary definition and every ordered row binding requires actual reading. No source/formal/atomiccredit.','columns':keys,'field_value_dictionaries':pool,'rows_in_original_order':rows};out[k]={'$exact_top_record_field_table':table};rebuilt[k]=[{f:pool[f][i] for f,i in zip(keys,row) if i!=-1} for row in rows]
 else:out[k]=v;rebuilt[k]=v
assert rebuilt==original
view={'schema':'gr8-exact-top-record-field-dictionaries/v1','qualification':'Complete carrier field values retained once per exact same-named value; all original row bindings retained. Equality is mechanical only, no reading/source/atomic acceptance.','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'complete_current_fields':out}
def emit(v,d=0,compact=False):
 if isinstance(v,dict):return '{\n'+',\n'.join(' '*(d+1)+json.dumps(k,ensure_ascii=False)+': '+emit(x,d+1,k=='rows_in_original_order' or d>3 and isinstance(x,list)) for k,x in v.items())+'\n'+' '*d+'}'
 if isinstance(v,list):
  if not v:return '[]'
  if compact:return '[\n'+',\n'.join(' '*(d+1)+(json.dumps(x,ensure_ascii=False,separators=(',',':')) if len(json.dumps(x,ensure_ascii=False))<=1800 else emit(x,d+1)) for x in v)+'\n'+' '*d+']'
  if all(not isinstance(x,(dict,list)) for x in v):return json.dumps(v,ensure_ascii=False)
  return '[\n'+',\n'.join(' '*(d+1)+emit(x,d+1) for x in v)+'\n'+' '*d+']'
 return json.dumps(v,ensure_ascii=False)
data=(emit(view)+'\n').encode();assert json.loads(data)==view;name=label+'-field-dictionary-view.json';assert not(P/name).exists();(P/name).write_bytes(data);g={'begin_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':n,'source_sha256':r['sha256'],'output':name,'bytes':len(data),'lines':len(data.splitlines()),'sha256':hashlib.sha256(data).hexdigest(),'all_current_fields_exact_decode':True,'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'};(P/(label+'-field-dictionary-generation.json')).write_text(json.dumps(g,indent=2)+'\n');print(json.dumps(g))
