"""Own inert exact field-component aid; all values/bindings still need reading."""
import datetime,hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;begin=datetime.datetime.now(datetime.timezone.utc).isoformat();l=json.loads((P/'reading-ledger.json').read_text());r=l['snapshot_payloads'][192];raw=(B/r['snapshot']).read_bytes();assert hashlib.sha256(raw).hexdigest()==r['sha256'];d=json.loads(raw)
def canon(x):return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def it(x,a):
 if x not in a:a.append(x)
 return a.index(x)
assert set(d)=={'schema','record_count','top_level_record_semantics','rows'};assert d['record_count']==len(d['rows'])==2400
sources=[];gates=[];statuses=[];contracts=[];tokens=[];values=[];templates=[];noncupheaders=[];noncupfields=[];cupgroups=[];cuppools={k:[] for k in ['Species','Item','Nature','EVs','Moves']};cupbind=[];recordnames=[]
def val(x):
 assert isinstance(x,str);seq=[it(s,tokens) for s in x.split(',')];idx=it(seq,values);assert ','.join(tokens[z] for z in values[idx])==x;return idx
for i,x in enumerate(d['rows']):
 assert set(x)=={'record_pointer','source','record','line','activation_gate','fields','fact_consumer_formal_ref','status'} and x['record_pointer']==f'records.json#/records/{i}'
 si=it(x['source'],sources);ga=it(x['activation_gate'],gates);st=it(x['status'],statuses);co=it(x['fact_consumer_formal_ref'],contracts)
 isc=bool(x['fields']) and x['fields'][0]['fact_contract']=='CUP'
 if isc:
  keys=list(cuppools);fs=x['fields'];assert [f['field'] for f in fs[:5]]==keys;rawvals=[f['value'] for f in fs[:5]]
  vs=[]
  for k,s in zip(keys,rawvals):vs.append(it(val(s),cuppools[k]))
  expected=[{'field':k,'position':j,'line':x['line'],'value':s,'fact_contract':'CUP','field_semantics_ref':'field-semantics.json#/fields/CUP/'+k} for j,(k,s) in enumerate(zip(keys,rawvals))]
  for k,field,sourceval in [('EV','EVs',rawvals[3]),('Move','Moves',rawvals[4])]:
   for j,s in enumerate(sourceval.split(',')):expected.append({'field':f'{k}[{j}]','value':None if s=='' else s,'fact_contract':'CUP','subfield':True,'field_semantics_ref':'field-semantics.json#/fields/CUP/'+field})
  assert expected==fs and x['record']==f'line:{x["line"]}',{'ordinal':i,'expected':expected,'actual':fs,'record':x['record'],'line':x['line']}
  if not cupgroups or cupgroups[-1]['source_index']!=si:cupgroups.append({'source_index':si,'original_record_start':i,'count':0,'line_formula':'3+positionWithinThisGroup','gate_index':ga,'status_index':st,'contract_index':co})
  g=cupgroups[-1];pos=g['count'];g['count']+=1;assert (g['original_record_start']+pos,3+pos,g['gate_index'],g['status_index'],g['contract_index'])==(i,x['line'],ga,st,co);cupbind.append(vs)
 else:
  header=[i,si,it(x['record'],recordnames),x['line'],ga,st,co];noncupheaders.append(header);enc=[]
  for f in x['fields']:
   assert 'value'in f;template={k:v for k,v in f.items() if k not in ['line','value']};ti=it(template,templates);delta=f['line']-x['line'] if 'line'in f else None;vi=val(f['value']);enc.append([ti,delta,vi]);back={**templates[ti],'value':','.join(tokens[z] for z in values[vi])}
   if delta is not None:back['line']=x['line']+delta
   assert back==f
  noncupfields.append(enc)
view={'qualification':'Complete current192 field values and bindings, exact reconstruction checked. All literal tokens, ordered comma sequences and2400recordbindings require actual reading. Comma join preserves every empty token/order/duplicates, no trimming/normalization. Broad contract refs are currentcarrier assertions, not independent sources/behaviors/atomic/taskacceptance. Generation0read/sourcecredit.','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'complete_root_metadata':{k:v for k,v in d.items() if k!='rows'},'sources':sources,'activation_gates':gates,'statuses':statuses,'consumer_formal_contract_refs':contracts,'complete_literal_value_tokens':tokens,'complete_value_sequences_comma_join':values,'noncup_field_complete_templates':templates,'noncup_record_literal_names':recordnames,'noncup_header_encoding':'Each512 header=[originalGlobalRecordOrdinal,sourceIdx,recordNameIdx,line,gateIdx,statusIdx,contractIdx]. record_pointer exact records.json#/records/ordinal. Matching512ordered field arrays=[templateIdx,lineDeltaOrNull,valueSequenceIdx]; reconstruct alltemplatekeys+value commajoin+line whenpresent. Nofieldomitted.','complete512_noncup_headers':noncupheaders,'complete512_noncup_ordered_fields':noncupfields,'cup_complete_groups':cupgroups,'cup_field_order':list(cuppools),'cup_complete_value_dictionaries':cuppools,'cup_exact_field_shape':'First5fields Species/Item/Nature/EVs/Moves have field,position0..4,line=recordline,value,fact_contractCUP,field_semantics_ref field-semantics.json#/fields/CUP/name. Then EV[ordinal] all EVcomma tokens inlistedorder, thenMove[ordinal] all Movescomma tokens inlistedorder; eachsubfield object field,value,fact_contractCUP,subfieldtrue,field_semantics_ref sameEVs/Moves. Alloriginal13292subfieldobjects matched exactly; originalsubfield value is null for rawempty token (strictchecked eachobject), rawcomma string retains all empty tokens; no EV/move order, duplicate or position elision. CUPrecord literal line:n and record_pointer globalordinal retained bygroup formulas.','complete1888_cup_ordered_bindings':cupbind}
lines=['{'];ks=list(view)
for k in ks:
 v=view[k]
 if isinstance(v,list):
  lines.append(canon(k)+':[')
  for j,z in enumerate(v):lines.append(canon(z)+(','if j+1<len(v)else''))
  lines.append(']'+(','if k!=ks[-1]else''))
 elif k=='cup_complete_value_dictionaries':
  lines.append(canon(k)+':{');sk=list(v)
  for z in sk:
   lines.append(canon(z)+':'+canon(v[z])+(','if z!=sk[-1]else''))
  lines.append('}'+(','if k!=ks[-1]else''))
 else:lines.append(canon(k)+':'+canon(v)+(','if k!=ks[-1]else''))
lines.append('}');data=('\n'.join(lines)+'\n').encode();assert json.loads(data)==view;out=P/'pbs192-complete-exact-components-view.json';out.write_bytes(data);m={'begin_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':192,'source_sha256':r['sha256'],'output':out.name,'bytes':len(data),'lines':len(lines),'sha256':hashlib.sha256(data).hexdigest(),'literal_tokens':len(tokens),'complete_comma_sequences':len(values),'noncup_field_templates':len(templates),'noncup_records':len(noncupheaders),'cup_records':len(cupbind),'all_current_objects_exactly_reconstructed':True,'generation_reading_credit':0};(P/'pbs192-complete-components-generation.json').write_text(json.dumps(m,indent=2)+'\n');print(json.dumps(m))
