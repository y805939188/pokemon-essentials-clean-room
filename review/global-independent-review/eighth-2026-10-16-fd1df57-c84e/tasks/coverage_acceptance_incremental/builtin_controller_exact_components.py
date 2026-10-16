"""Exact static display of257 built-in controller-data records and119 patterns.
Reconstruct each raw literal from its actual GUID/name/ordered fields only after
checking byte-exact equality. This executes no executable/native consumer and
grants no program, registration, platformselection or gamebridge acceptance.
"""
import json,hashlib,datetime
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;begin=datetime.datetime.now(datetime.timezone.utc).isoformat();r=json.loads((P/'reading-ledger.json').read_text())['snapshot_payloads'][11];raw=(B/r['snapshot']).read_bytes();assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'];j=json.loads(raw)
patterns=j['patterns'];names=j['names'];records=j['records'];pattern_of={};name_of={}
assert [v['pattern'] for v in patterns]==list(range(len(patterns)))
for i,v in enumerate(patterns):
 assert set(v)=={'pattern','records','ordered_fields'}
 for n in v['records']:
  assert n not in pattern_of;pattern_of[n]=i
for i,v in enumerate(names):
 assert set(v)=={'name','records'}
 for n in v['records']:
  assert n not in name_of;name_of[n]=i
assert set(pattern_of)==set(name_of)==set(range(len(records)))
pattern_rows=[]
for v in patterns:
 for pair in v['ordered_fields']:assert len(pair)==2 and all(isinstance(s,str) and ',' not in s and ':' not in s for s in pair)
 literal=','.join(k+':'+val for k,val in v['ordered_fields'])
 assert [x.split(':') for x in literal.split(',')]==v['ordered_fields']
 pattern_rows.append([v['pattern'],v['records'],literal])
record_rows=[]
for i,v in enumerate(records):
 assert set(v)=={'record','pointer_slot','start','end','sha256','guid','name','ordered_fields','raw_text'}
 assert v['record']==i and names[name_of[i]]['name']==v['name'] and patterns[pattern_of[i]]['ordered_fields']==v['ordered_fields']
 literal=v['guid']+','+v['name']+','+','.join(k+':'+val for k,val in v['ordered_fields'])+','
 assert literal==v['raw_text']
 record_rows.append([i,v['pointer_slot'],v['start'],v['end'],v['sha256'],v['guid'],name_of[i],pattern_of[i]])
rebuilt=dict(j,records=[])
for i,slot,start,end,sha,guid,ni,pi in record_rows:
 pairs=patterns[pi]['ordered_fields'];name=names[ni]['name'];rebuilt['records'].append({'record':i,'pointer_slot':slot,'start':start,'end':end,'sha256':sha,'guid':guid,'name':name,'ordered_fields':pairs,'raw_text':guid+','+name+','+','.join(k+':'+val for k,val in pairs)+','})
assert rebuilt==j
view={'schema':'gr8-builtin-controller-complete-exact-components/v1','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'qualification':'Literal data-field reception only. Each record raw_text exactly GUID, comma, selected name, comma, selected ordered pattern, trailingcomma; equality checked for all257. Every actual GUID/name/pattern and every name/pattern/record binding still requires actual reading. No nativecode/platform/registration/host/gamebridge approval; generation0reading.','complete_root_fields_except_records_patterns_names':{k:v for k,v in j.items() if k not in ['records','patterns','names']},'pattern_columns':['pattern','records_in_original_order','ordered_fields_literal_eachcomma_pair_split_once_at_colon'],'patterns':pattern_rows,'name_columns':['name','records_in_original_order'],'names':[[v['name'],v['records']] for v in names],'record_columns':['record','pointer_slot','start','end','sha256','guid','name_index','pattern_index'],'records':record_rows}
lines=['{']
for n,(k,v) in enumerate(view.items()):
 suffix=',' if n<len(view)-1 else ''
 if k in ['patterns','names','records']:lines+=[' '+json.dumps(k)+': [']+['  '+json.dumps(row,ensure_ascii=False,separators=(',',':'))+(',' if i<len(v)-1 else '') for i,row in enumerate(v)]+[' ]'+suffix]
 else:lines+=[' '+json.dumps(k)+': '+json.dumps(v,ensure_ascii=False)+suffix]
lines+=['}'];data=('\n'.join(lines)+'\n').encode();assert json.loads(data)==view;out=P/'builtin-controller-complete-exact-components-view.json';assert not out.exists();out.write_bytes(data)
proof={'begin_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':11,'source_sha256':r['sha256'],'output':out.name,'bytes':len(data),'lines':len(data.splitlines()),'sha256':hashlib.sha256(data).hexdigest(),'all257_raw_literals_exact_component_equality':True,'all_records_patterns_names_exact_decode':True,'generation_reading_credit':0,'source_program_credit':0,'business':'NOT_EXECUTED'};(P/'builtin-controller-exact-components-generation.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
