"""Exact inert per-record field sharing, no source or reading credit."""
import json,hashlib,datetime
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;begin=datetime.datetime.now(datetime.timezone.utc).isoformat();r=json.loads((P/'reading-ledger.json').read_text())['snapshot_payloads'][80];raw=(B/r['snapshot']).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256'];j=json.loads(raw)
def canon(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
records=[]
for row in j['records']:
 anchors={k:row[k] for k in ['source_parameter_data','behavior'] if len(canon(row[k]))>=40}
 def enc(x,path=()):
  for k,v in anchors.items():
   if path!=(k,) and canon(x)==canon(v):return {'$exact_same_row_field':k}
  if isinstance(x,dict):
   assert '$exact_same_row_field' not in x
   return {k:enc(v,path+(k,)) for k,v in x.items()}
  if isinstance(x,list):return [enc(v,path+(i,)) for i,v in enumerate(x)]
  return x
 encoded=enc(row)
 def dec(x):
  if isinstance(x,dict):
   if set(x)=={'$exact_same_row_field'}:return row[x['$exact_same_row_field']]
   return {k:dec(v) for k,v in x.items()}
  if isinstance(x,list):return [dec(v) for v in x]
  return x
 assert dec(encoded)==row;records.append(encoded)
encoded=dict(j,records=records)
view={'schema':'gr8-stage-exact-same-record-field-components/v1','source':{k:r[k] for k in ['original_path','bytes','sha256','git_blob','captured_utc']},'binding_rule':'Within each one of114 record objects, $exact_same_row_field names source_parameter_data or behavior in that same record. Read its full literal anchor once and each use binding. Every replaced whole value exactly equal; no inference from source/operation names. All remaining values literal. Decoder equality verified; generation0reading.','value':encoded}
out=P/'stage-table-same-record-components.json';assert not out.exists();data=(json.dumps(view,ensure_ascii=False,indent=1)+'\n').encode();out.write_bytes(data);proof={'begin_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'output':out.name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'lines':len(data.splitlines()),'all114_exact_decode_equals_original':True,'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'};(P/'stage-table-same-record-components-generation.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
