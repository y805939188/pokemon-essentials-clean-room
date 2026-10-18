"""Own inert exact lexical components for125 MOVE carrier objects.
Tables preserve every original field and ordered binding. Source/formal literal
bodies are not imported or executed. Exact equality grants0 reading/acceptance.
"""
import json,hashlib,datetime,re
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;start=datetime.datetime.now(datetime.timezone.utc).isoformat();r=json.loads((P/'reading-ledger.json').read_text())['snapshot_payloads'][74];raw=(B/r['snapshot']).read_bytes();assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'];j=json.loads(raw);units=j['units'];constant={k:units[0][k] for k in units[0] if all(x[k]==units[0][k] for x in units)};fields=[k for k in units[0] if k not in constant];assert fields==['id','source','definition','main_contract','fact','consumer_chain','reception_owner','reception_status','reverse_consumers','formal_locator'];assert all(x['id']=='RUNIT:'+x['definition'] for x in units)
keys=['main_contract','consumer_chain','reception_owner','reception_status','reverse_consumers','formal_locator'];d={k:[] for k in keys};payloads=[];rows=[]
def idx(values,value):
 if value not in values:values.append(value)
 return values.index(value)
for v in units:
 assert set(v['source'])=={'payload','lines'}
 rows.append([v['definition'],idx(payloads,v['source']['payload']),v['source']['lines'],v['fact']]+[idx(d[k],v[k]) for k in keys])
paths=[];reverse=[]
for a in d['reverse_consumers']:
 z=[]
 for s in a:
  m=re.fullmatch(r'(.*):L([0-9]+):A([0-9]+)',s);assert m
  z.append([idx(paths,m[1]),m[2],m[3]])
 reverse.append(z)
d['reverse_consumers']=reverse
rebuilt=[]
for row in rows:
 definition,pi,lines,fact,*v=row;u=dict(constant,id='RUNIT:'+definition,source={'payload':payloads[pi],'lines':lines},definition=definition,fact=fact)
 for key,i in zip(keys,v):
  u[key]=d[key][i] if key!='reverse_consumers' else [paths[a]+':L'+l+':A'+n for a,l,n in d[key][i]]
 rebuilt.append(u)
assert rebuilt==units
out={'schema':'gr8-nested-move-exact-field-components/v1','qualification':'Literal complete carrier fields only. Every ordered row and dictionary definition requires actual reading. Reverse triples preserve exact path:Ldecimal:Adecimal strings including digits. id exactly RUNIT:+definition checked all125. No underlying source/formal/atomic/consumer acceptance.','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'all_other_root_fields':{k:v for k,v in j.items() if k not in ['units','source_groups']},'common_unit_fields':constant,'source_payload_dictionary':payloads,'reverse_locator_paths':paths,'unit_field_dictionaries':d,'unit_columns':['definition','source_payload_index','source_lines','fact']+[k+'_index' for k in keys],'unit_rows':rows,'complete_source_groups':j['source_groups']}
def emit(v,n=0,compact=False):
 if isinstance(v,dict):return '{\n'+',\n'.join(' '*(n+1)+json.dumps(k,ensure_ascii=False)+': '+emit(x,n+1,k=='unit_rows') for k,x in v.items())+'\n'+' '*n+'}'
 if isinstance(v,list):
  if not v:return '[]'
  if compact:return '[\n'+',\n'.join(' '*(n+1)+json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in v)+'\n'+' '*n+']'
  if all(not isinstance(x,(dict,list)) for x in v):return json.dumps(v,ensure_ascii=False)
  return '[\n'+',\n'.join(' '*(n+1)+emit(x,n+1) for x in v)+'\n'+' '*n+']'
 return json.dumps(v,ensure_ascii=False)
data=(emit(out)+'\n').encode();assert json.loads(data)==out;name='nested-move-forward-complete-components-view.json';assert not (P/name).exists();(P/name).write_bytes(data);proof={'begin_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':74,'source_sha256':r['sha256'],'output':name,'bytes':len(data),'lines':len(data.splitlines()),'sha256':hashlib.sha256(data).hexdigest(),'all125_units_exact_reconstruction':True,'all_other_root_and_source_groups_exact':True,'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'};(P/'nested-move-forward-complete-components-generation.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
