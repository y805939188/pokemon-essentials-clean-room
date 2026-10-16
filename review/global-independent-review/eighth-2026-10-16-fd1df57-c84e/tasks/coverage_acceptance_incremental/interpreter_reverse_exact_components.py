"""Inert exact field decomposition of the interpreter reverse mapping.
Every reverse assertion remains literal. Repeated source-fact-ID arrays are
represented by exact ordered source-unit bindings against an already received
frozen forward carrier, never as source or atomic acceptance. Decode equality
is mechanical integrity only; all component values still require actual reading.
"""
import json,hashlib,datetime
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent
begin=datetime.datetime.now(datetime.timezone.utc).isoformat()
l=json.loads((P/'reading-ledger.json').read_text())
def get(i):
 r=l['snapshot_payloads'][i];raw=(B/r['snapshot']).read_bytes();assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'];return r,json.loads(raw)
r,j=get(247);fr,f=get(244);ids={u['id']:[x['id'] for x in u['facts']] for u in f['units']}
paths=list(dict.fromkeys(c['spec']['path'] for c in j['clauses']))
q='The listed complete source units were read and compared; group crosslinks do not establish extra unlisted claims.'
rows=[]
for c in j['clauses']:
 exp=[v for u in c['source_units'] for v in ids[u]]
 assert c['execution']=='NOT_EXECUTED'
 assert set(c)=={'id','spec','subassertions','premises','source_units','status','execution'}
 assert set(c['spec'])=={'path','lines'}
 assertions=[]
 for n,s in enumerate(c['subassertions'],1):
  assert set(s)=={'id','assertion','source_fact_ids','support_qualification'}
  assert s['id']==c['id']+'.'+str(n) and s['source_fact_ids']==exp and s['support_qualification']==q
  assertions.append(s['assertion'])
 rows.append([c['id'],paths.index(c['spec']['path']),c['spec']['lines'],c['premises'],c['source_units'],c['status'],assertions])
root={k:v for k,v in j.items() if k!='clauses'}
rebuilt=dict(root,clauses=[])
for a,path,lines,premises,sourceunits,status,assertions in rows:
 rebuilt['clauses'].append({'id':a,'spec':{'path':paths[path],'lines':lines},'premises':premises,'source_units':sourceunits,'status':status,'execution':'NOT_EXECUTED','subassertions':[{'id':a+'.'+str(n),'assertion':text,'source_fact_ids':[v for u in sourceunits for v in ids[u]],'support_qualification':q} for n,text in enumerate(assertions,1)]})
assert rebuilt==j
idrules={}
for u,values in ids.items():
 assert values==[u+'.'+str(i) for i in range(1,len(values)+1)]
 idrules[u]={'suffix_inclusive':[1,len(values)]}
view={'schema':'gr8-interpreter-reverse-complete-exact-components/v1','source':{k:r[k] for k in ['original_path','bytes','sha256','git_blob','captured_utc']},'qualified_prior_forward_component':{k:fr[k] for k in ['original_path','bytes','sha256','git_blob','captured_utc']},'exact_binding_rule':'Each subassertion ID = row id + dot + one-based assertion position. Each subassertion source_fact_ids = ordered concatenation of the source_units exact fact IDs below. Each support_qualification = the shared literal. All1007 checked exactly. These are declared broad provider crosslinks, not proof that every source fact supports each assertion.','shared_support_qualification':q,'execution_for_each_clause':'NOT_EXECUTED','spec_paths_by_index':paths,'prior_forward_fact_id_exact_ordered_ranges':idrules,'complete_root_fields_except_clauses':root,'columns':['clause_id','spec_path_index','inclusive_spec_lines','premises','source_units_in_order','provider_status','all_literal_subassertion_texts_in_order'],'rows':rows,'qualification':'All current values exactly reconstruct the frozen reverse carrier using explicit already received forward fact IDs. Generation is0reading. Complete component reading, source/body/formal/consumer acceptance are distinct.'}
def emit(v,d=0):
 pad=' '*d
 if isinstance(v,dict):return '{\n'+',\n'.join(' '*(d+1)+json.dumps(k,ensure_ascii=False)+': '+emit(x,d+1) for k,x in v.items())+'\n'+pad+'}'
 if isinstance(v,list):
  if v and all(isinstance(x,list) and len(x)==7 for x in v):return '[\n'+',\n'.join(' '*(d+1)+json.dumps(x,ensure_ascii=False,separators=(',',':')) for x in v)+'\n'+pad+']'
  if all(not isinstance(x,(dict,list)) for x in v):return json.dumps(v,ensure_ascii=False)
  return '[\n'+',\n'.join(' '*(d+1)+emit(x,d+1) for x in v)+'\n'+pad+']'
 return json.dumps(v,ensure_ascii=False)
out=P/'interpreter-reverse-complete-exact-component-view.json';assert not out.exists();data=(emit(view)+'\n').encode();assert json.loads(data)==view;out.write_bytes(data)
proof={'begin_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'output':out.name,'bytes':len(data),'lines':len(data.splitlines()),'sha256':hashlib.sha256(data).hexdigest(),'source_index':247,'source_sha256':r['sha256'],'all1007_sourcefactarrays_exact_forward_flatten':True,'all_subassertion_ids_exact_ordered_suffix':True,'full_decode_equals_original':True,'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'}
(P/'interpreter-reverse-exact-components-generation.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
