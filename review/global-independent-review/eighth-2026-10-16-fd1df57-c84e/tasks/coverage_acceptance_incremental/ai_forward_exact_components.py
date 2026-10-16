"""Own exact AI carrier components. Every definition and ordered binding must
still be read. Data reconstruction only; no reviewed-source code execution.
"""
import json,hashlib,datetime,re,traceback
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent.parent;start=datetime.datetime.now(datetime.timezone.utc).isoformat()
try:
 r=json.loads((P/'reading-ledger.json').read_text())['snapshot_payloads'][40];raw=(B/r['snapshot']).read_bytes();assert len(raw)==r['bytes'] and hashlib.sha256(raw).hexdigest()==r['sha256'];j=json.loads(raw);families=[];operations=[];keys=[]
 def ix(a,v):
  if v not in a:a.append(v)
  return a.index(v)
 def regid(s):
  if s is None:return None
  m=re.fullmatch('REG([0-9]{4})',s);assert m and s=='REG'+m[1];return int(m[1])
 def rid(n):return None if n is None else 'REG'+str(n).zfill(4)
 def factnums(a):
  result=[]
  for s in a:
   m=re.fullmatch('AIU([0-9]{3})',s);assert m;result.append(int(m[1]))
  return result
 def factids(a):return ['AIU'+str(n).zfill(3) for n in a]
 a=j['registration_index'];assert [x['id'] for x in a]==[rid(i) for i in range(1,787)];common={k:a[0][k] for k in ['reader','actual_source_read','semantic_qualification','business_execution']};assert all(all(x[k]==v for k,v in common.items()) for x in a)
 regrows=[[x['source_index'],x['range'],ix(families,x['family']),ix(operations,x['operation']),[ix(keys,s) for s in x['keys']],factnums(x['source_fact_units'])] for x in a];decoded=[dict(common,id=rid(i+1),source_index=x[0],range=x[1],family=families[x[2]],operation=operations[x[3]],keys=[keys[n] for n in x[4]],source_fact_units=factids(x[5])) for i,x in enumerate(regrows)];assert decoded==a
 exp=j['expanded_registration_bindings'];exprows=[[regid(x['registration_id']),ix(families,x['family']),ix(keys,x['key']),ix(operations,x['operation']),regid(x['source_registration_id']),regid(x['prior_effective_registration']),x['effective_write'],factnums(x['source_fact_units'])] for x in exp];assert [{'registration_id':rid(x[0]),'family':families[x[1]],'key':keys[x[2]],'operation':operations[x[3]],'source_registration_id':rid(x[4]),'prior_effective_registration':rid(x[5]),'effective_write':x[6],'source_fact_units':factids(x[7])} for x in exprows]==exp
 methods=j['method_index'];mc={k:methods[0][k] for k in ['read_status','index_qualification']};assert all(all(x[k]==v for k,v in mc.items()) for x in methods);mrows=[[x['source_index'],x['definition_line'],x['signature'],factnums(x['source_fact_units'])] for x in methods];assert [dict(mc,source_index=x[0],definition_line=x[1],signature=x[2],source_fact_units=factids(x[3])) for x in mrows]==methods
 old=json.loads((P/'ai-forward-current-final-field-dictionary-view.json').read_text());mt=old['complete_current_fields']['manual_units'];table=mt['$exact_top_record_field_table'];assert [{k:table['field_value_dictionaries'][k][n] for k,n in zip(table['columns'],row) if n!=-1} for row in table['rows_in_original_order']]==j['manual_units']
 view={'schema':'gr8-AI-complete-exact-components/v1','qualification':'Every full manual unit dictionary value and all ordered bindings, every family/operation/key literal and all786 registration/786expanded/134method rows require actual reading. REG numbers decode exact REG+4zero-padded decimal; AIU numbers decode exact AIU+3zero-padded decimal. No source body, actual caller or atomic acceptance inferred.','source':{k:r[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','captured_utc']},'all_other_root_fields':{k:v for k,v in j.items() if k not in ['manual_units','registration_index','expanded_registration_bindings','method_index']},'families':families,'operations':operations,'key_columns':['index','exact_key_literal'],'key_dictionary':[[i,s] for i,s in enumerate(keys)],'manual_units_complete_fields':mt,'registration_common_fields':common,'registration_columns':['source_index','range','family_index','operation_index','key_indices_in_original_order','AIU_numbers_in_original_order'],'registration_row_id':'Original row0→REG0001; inclusive786 rows exact IDs checked','registration_rows':regrows,'expanded_columns':['REG_number','family_index','key_index','operation_index','source_REG_number_or_null','prior_effective_REG_number_or_null','effective_write','AIU_numbers_in_original_order'],'expanded_rows':exprows,'method_common_fields':mc,'method_columns':['source_index','definition_line','literal_signature','AIU_numbers_in_original_order'],'method_rows':mrows}
 def emit(v,d=0,compact=False):
  if isinstance(v,dict):return '{\n'+',\n'.join(' '*(d+1)+json.dumps(k,ensure_ascii=False)+': '+emit(x,d+1,k in ['key_dictionary','registration_rows','expanded_rows','method_rows','rows_in_original_order'] or d>3 and isinstance(x,list)) for k,x in v.items())+'\n'+' '*d+'}'
  if isinstance(v,list):
   if not v:return '[]'
   if compact:return '[\n'+',\n'.join(' '*(d+1)+(json.dumps(x,ensure_ascii=False,separators=(',',':')) if len(json.dumps(x,ensure_ascii=False))<1800 else emit(x,d+1)) for x in v)+'\n'+' '*d+']'
   if all(not isinstance(x,(dict,list)) for x in v):return json.dumps(v,ensure_ascii=False)
   return '[\n'+',\n'.join(' '*(d+1)+emit(x,d+1) for x in v)+'\n'+' '*d+']'
  return json.dumps(v,ensure_ascii=False)
 data=(emit(view)+'\n').encode();assert json.loads(data)==view;name='ai-forward-complete-exact-components-view.json';assert not(P/name).exists();(P/name).write_bytes(data);g={'begin_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':0,'source_index':40,'source_sha256':r['sha256'],'output':name,'bytes':len(data),'lines':len(data.splitlines()),'sha256':hashlib.sha256(data).hexdigest(),'all_current_fields_exact_reconstruction':True,'generation_reading_credit':0,'source_credit':0,'business':'NOT_EXECUTED'};(P/'ai-forward-complete-exact-components-generation.json').write_text(json.dumps(g,indent=2)+'\n');print(json.dumps(g))
except Exception:
 (P/'ai-forward-component-generation-failure.json').write_text(json.dumps({'begin_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':1,'traceback':traceback.format_exc(),'reading_credit':0},indent=2)+'\n');raise
