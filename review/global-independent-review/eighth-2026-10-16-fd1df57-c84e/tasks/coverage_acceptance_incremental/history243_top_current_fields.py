"""Own partial carrier aid, deliberately excludes three explicit nested fields.

All top-level ledger metadata and all other per-record fields are exact. A
partial reception can never mark original137 complete or inherit historical
source/candidate/semantic approval from this index.
"""
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;begin=datetime.datetime.now(datetime.timezone.utc).isoformat();l=json.loads((P/'reading-ledger.json').read_text());r=l['snapshot_payloads'][137];raw=(B/r['snapshot']).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256'];d=json.loads(raw);excluded=['administrative_dispositions','semantic_range','current_same_value_associations'];records=[{k:v for k,v in x.items() if k not in excluded} for x in d['records']];columns=list(dict.fromkeys(k for x in records for k in x));pools={k:[] for k in columns};look={k:{} for k in columns};bindings=[]
for x in records:
 row=[]
 for k in columns:
  if k not in x:row.append(-1);continue
  s=json.dumps(x[k],ensure_ascii=False,separators=(',',':'))
  if s not in look[k]:look[k][s]=len(pools[k]);pools[k].append(x[k])
  row.append(look[k][s])
 bindings.append(row)
assert [{k:pools[k][idx] for k,idx in zip(columns,row) if idx!=-1} for row in bindings]==records
lines=['{"source_index":137,"qualification":"PARTIAL137 ONLY. Explicitly excluded per-record fields:administrative_dispositions,semantic_range,current_same_value_associations; all remain OPEN. -1 means absent; other row fields reference exact same-named pool, all zero-based. Complete original243-record top-field projection reconstructs exactly; no historical source/task/approval credit from generation.",','"exact_root_metadata":'+json.dumps({k:v for k,v in d.items() if k!='records'},ensure_ascii=False,separators=(',',':'))+',','"columns":'+json.dumps(columns,separators=(',',':'))+',','"pools":{']
for a,k in enumerate(columns):
 lines.append(json.dumps(k)+':[')
 for i,v in enumerate(pools[k]):lines.append(json.dumps(v,ensure_ascii=False,separators=(',',':'))+(',' if i+1<len(pools[k]) else ''))
 lines.append(']'+(',' if a+1<len(columns) else ''))
lines.append('},"ordered243bindings":[')
for i,row in enumerate(bindings):lines.append(json.dumps(row,separators=(',',':'))+(',' if i+1<len(bindings) else ''))
lines.append(']}');data=('\n'.join(lines)+'\n').encode();json.loads(data);out=P/'h243-top-current-fields-PARTIAL-view.json';out.write_bytes(data);m={'begin_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':137,'source_sha256':r['sha256'],'output':out.name,'bytes':len(data),'lines':len(lines),'sha256':hashlib.sha256(data).hexdigest(),'top_projection_exact':True,'excluded_nested_fields':excluded,'generation_reading_credit':0,'source_credit':0,'whole137_complete':False};(P/'h243-top-current-fields-PARTIAL-generation.json').write_text(json.dumps(m,indent=2)+'\n');print(json.dumps(m))
