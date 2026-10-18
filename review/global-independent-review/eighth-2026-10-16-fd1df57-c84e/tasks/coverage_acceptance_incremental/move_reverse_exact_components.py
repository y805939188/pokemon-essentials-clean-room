"""Own static exact components of MOVE reverse carrier, preserving every
literal assertion/context/vector/data object and every binding. No source eval.
"""
import json,hashlib,datetime,re,traceback
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;start=datetime.datetime.now(datetime.timezone.utc).isoformat()
try:
 r=json.loads((P/'reading-ledger.json').read_text())['snapshot_payloads'][78];raw=(B/r['snapshot']).read_bytes();assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'];j=json.loads(raw);paths=[];contexts=[];sf=[];just=[];ar=[]
 def ix(a,v):
  if v not in a:a.append(v)
  return a.index(v)
 common={k:j['assertions'][0][k] for k in ['reviewer','support','evidence_level','execution','premises']};assert all(all(a[k]==v for k,v in common.items()) for a in j['assertions'])
 for a in j['assertions']:
  m=re.fullmatch(r'(.*):L([0-9]+):A([0-9]+)',a['id']);assert m and a['formal']=={'payload':'B8:'+m[1],'line':int(m[2])}
  ci=ix(contexts,[ix(paths,m[1]),a['formal']['line'],m[2],a['formal_full_context']]);ar.append([ci,m[3],a['assertion'],ix(sf,a['source_facts']),ix(just,a['justification'])])
 rebuilt=[]
 for ci,ad,assertion,si,ji in ar:
  pi,line,ld,text=contexts[ci];rebuilt.append(dict(common,id=paths[pi]+':L'+ld+':A'+ad,formal={'payload':'B8:'+paths[pi],'line':line},formal_full_context=text,assertion=assertion,source_facts=sf[si],justification=just[ji]))
 assert rebuilt==j['assertions']
 groupdefs=[];sfr=[]
 for groups in sf:
  assert isinstance(groups,list);sfr.append([ix(groupdefs,x) for x in groups])
 assert [[groupdefs[i] for i in row] for row in sfr]==sf
 vectors=j['vectors'];vc={k:vectors[0][k] for k in ['primary','reviewer','owner','support','evidence_level','execution'] if all(v[k]==vectors[0][k] for v in vectors)};vk=[k for k in vectors[0] if k not in vc];vd={k:[] for k in vk};vr=[]
 for v in vectors:assert set(v)==set(vectors[0]);vr.append([ix(vd[k],v[k]) for k in vk])
 assert [dict(vc,**{k:vd[k][n] for k,n in zip(vk,row)}) for row in vr]==vectors
 admin=j['administrative_dispositions'];ac={k:admin[0][k] for k in admin[0] if all(v[k]==admin[0][k] for v in admin)};ak=[k for k in admin[0] if k not in ac];av=[[v[k] for k in ak] for v in admin];assert [dict(ac,**dict(zip(ak,row))) for row in av]==admin
 checks=j['data_checks'];cells=checks['blacklist_cells'];cc={'equal':True};assert all(v['equal'] is True and set(v)=={'line','effect','entry','asserted','actual','equal'} for v in cells);entries=[];cr=[[v['line'],v['effect'],ix(entries,v['entry']),v['asserted'],v['actual']] for v in cells];assert [dict(cc,line=v[0],effect=v[1],entry=entries[v[2]],asserted=v[3],actual=v[4]) for v in cr]==cells
 view={'schema':'gr8-MOVE-reverse-complete-exact-components/v1','qualification':'Every literal definition and each ordered assertion/context/group/vector/data binding requires actual reading. id is exactly path:Ldigits:Adigits with original zeroes retained; formal.payload exactly B8:+path and line integer checked. No source/fullF/atomic approval by reconstruction.','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'all_other_root_fields':{k:v for k,v in j.items() if k not in ['assertions','vectors','data_checks','administrative_dispositions']},'assertion_common_fields':common,'formal_path_dictionary':paths,'formal_context_columns':['path_index','line_integer','original_L_decimal_digits','complete_literal_context'],'formal_context_rows':contexts,'complete_source_fact_group_dictionary':groupdefs,'source_fact_lists_original_ordered_group_indices':sfr,'complete_justification_dictionary':just,'assertion_columns':['formal_context_index','original_A_decimal_digits','literal_assertion','source_fact_list_index','justification_index'],'assertion_rows':ar,'vector_common_fields':vc,'vector_field_columns':vk,'vector_complete_field_dictionaries':vd,'vector_rows':vr,'administrative_common_fields':ac,'administrative_columns':ak,'administrative_rows':av,'blacklist_common_fields':cc,'blacklist_entry_dictionary':entries,'blacklist_columns':['line','effect','entry_index','asserted','actual'],'blacklist_rows':cr,'all_other_complete_data_checks':{k:v for k,v in checks.items() if k!='blacklist_cells'}}
 def emit(v,d=0,compact=False):
  if isinstance(v,dict):return '{\n'+',\n'.join(' '*(d+1)+json.dumps(k,ensure_ascii=False)+': '+emit(x,d+1,k.endswith('_rows') or k=='source_fact_lists_original_ordered_group_indices' or d>1 and isinstance(x,list)) for k,x in v.items())+'\n'+' '*d+'}'
  if isinstance(v,list):
   if not v:return '[]'
   if compact:return '[\n'+',\n'.join(' '*(d+1)+(json.dumps(x,ensure_ascii=False,separators=(',',':')) if len(json.dumps(x,ensure_ascii=False))<1800 else emit(x,d+1)) for x in v)+'\n'+' '*d+']'
   if all(not isinstance(x,(dict,list)) for x in v):return json.dumps(v,ensure_ascii=False)
   return '[\n'+',\n'.join(' '*(d+1)+emit(x,d+1) for x in v)+'\n'+' '*d+']'
  return json.dumps(v,ensure_ascii=False)
 data=(emit(view)+'\n').encode();assert json.loads(data)==view;name='move-reverse-complete-exact-components-view.json';assert not(P/name).exists();(P/name).write_bytes(data);g={'begin_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':78,'source_sha256':r['sha256'],'output':name,'bytes':len(data),'lines':len(data.splitlines()),'sha256':hashlib.sha256(data).hexdigest(),'all_current_fields_exact_reconstruction':True,'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'};(P/'move-reverse-complete-exact-components-generation.json').write_text(json.dumps(g,indent=2)+'\n');print(json.dumps(g))
except Exception:
 (P/'move-reverse-component-generation-failure.json').write_text(json.dumps({'begin_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':1,'traceback':traceback.format_exc(),'reading_credit':0},indent=2)+'\n');raise
