from pathlib import Path
import re,json,datetime,hashlib
o=Path(__file__).resolve().parent;ids=json.loads((o/'identities.json').read_text());sem=json.loads((o/'semantic-units.json').read_text());rev=json.loads((o/'reverse-mapping.json').read_text())
units=sem['units'];regs=[];methods=[];unmapped=[]
def support(si,a,b):return [u['id'] for u in units if u['source']==si and u['range'][0]<=b and u['range'][1]>=a]
for x in ids['files']:
 if x['kind']!='reference':continue
 lines=(Path(x['repo'])/x['path']).read_text().splitlines()
 for i,l in enumerate(lines):
  m=re.search(r'Battle::AI::Handlers::(\w+)\.(addIf|add|copy)\(',l)
  if m:
   family,action=m.groups();j=i
   if action=='copy':
    while not lines[j].rstrip().endswith(')'):j+=1
   else:
    while lines[j].strip()!=')':j+=1
   header='\n'.join(lines[i:j+1]);args=header[header.index('(')+1:]
   keys=re.findall(r'"([^"\n]+)"|(?<!\w):([A-Za-z_]\w*)',args if action=='copy' else args.split(',',1)[0]);keys=[a or b for a,b in keys]
   if not keys:raise ValueError((x['path'],i+1))
   su=support(x['index'],i+1,j+1)
   if not su:unmapped.append((x['index'],i+1,j+1))
   regs.append({'id':f'REG{len(regs)+1:04d}','source_index':x['index'],'range':[i+1,j+1],'family':family,'operation':action,'keys':keys,'source_fact_units':su,'reader':'/root/com_ai','actual_source_read':'FULL_CONTINUOUS_PRIMARY_FILE; COMPLETE_CALL_READ','semantic_qualification':'Manual semantic facts in cited units; this generated inventory is only a post-read binding/completeness crosscheck. No registration count or pointer grants acceptance.','business_execution':'NOT_EXECUTED'})
  if re.match(r'\s*def\s',l):
   su=support(x['index'],i+1,i+1)
   if not su:unmapped.append((x['index'],i+1,'method'))
   methods.append({'source_index':x['index'],'definition_line':i+1,'signature':l.strip(),'source_fact_units':su,'read_status':'ACTUAL_FULL_FILE_STRUCTURAL_READ','index_qualification':'Locator only, full method facts in manual units; no source execution.'})
state={};occ=[];anomalies=[]
for r in regs:
 fam=r['family'];action=r['operation'];keys=r['keys']
 if action=='addIf':continue
 if action=='add':targets=keys[:1]
 else:targets=keys[1:]
 for key in targets:
  ident=(fam,key);prior=state.get(ident);source=state.get((fam,keys[0])) if action=='copy' else r['id']
  item={'registration_id':r['id'],'family':fam,'key':key,'operation':action,'source_registration_id':source,'prior_effective_registration':prior,'effective_write':bool(source),'source_fact_units':r['source_fact_units']}
  if source:state[ident]=source
  if prior or not source:anomalies.append(item)
  occ.append(item)
census={'registration_statements':len(regs),'add_copy_statements':sum(r['operation']!='addIf' for r in regs),'conditional_statements':sum(r['operation']=='addIf' for r in regs),'expanded_direct_occurrences':len(occ),'different_seen_direct_keys':len(set((r['family'],r['key']) for r in occ)),'effective_direct_keys':len(state),'conditional_item_identities':57,'effective_locatable_keys':len(state)+57,'source_files_with_registrations':len(set(r['source_index'] for r in regs)),'method_definitions_indexed':len(methods)}
assert census['registration_statements']==786,census
assert census['expanded_direct_occurrences']==786,census
assert census['effective_direct_keys']==782,census
assert not unmapped,unmapped
facts=[]
for u in units:
 rr=[r['id'] for r in rev['records'] if u['id'] in r['source_fact_units']]
 vv=[r['id'] for r in rev['vectors'] if u['id'] in r['source_fact_units']]
 facts.append({**u,'formal_manual_clause_groups':rr,'formal_static_vectors':vv,'full_file_identity':'identities.json#reference/'+str(u['source']),'consumer':u.get('consumer',u.get('consumers','Existing AI query families; named formal caller and actual local phase, with real receivers separately scoped in interfaces.json')),'premises':'Actual called AI phase/flags/family; valid accessed objects unless the unit explicitly describes invalid/sparse/empty input. Numeric/local helper result is not real action success.','mapping_assessment':'MANUALLY_READ_LOCAL_FACTS_MAPPED; NAMED_EXTERNAL_RECEIVERS_REMAIN_OPEN','structural_entries':[r['id'] for r in regs if u['id'] in r['source_fact_units']]})
payload={'schema':'gr8-com-ai-forward-mapping/v1','reviewer':'/root/com_ai','updated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'B8_commit':ids['B8_commit'],'R_commit':ids['R_commit'],'status':'PRIMARY_AI_LOCAL_FACT_MAPPING_COMPLETE_WITH_EXTERNAL_RECEPTION_OPEN','method':'Actual20fullfile continuous read and manually authored65unit facts precede structural census. Generated declaration/method locators audit completeness only; no search/count/pointer/previousPASS replaces semantic or consumer acceptance.','manual_units':facts,'manual_fact_count':sum(len(x['facts']) for x in units),'registration_index':regs,'expanded_registration_bindings':occ,'effective_binding_anomalies':anomalies,'method_index':methods,'mechanical_census':census,'unmapped_structural_locators':unmapped,'primary_unread_files':0,'primary_unread_lines':0,'external_reception':'interfaces.json: scoped6/open4, not globalAI acceptance','business_execution':'NOT_EXECUTED','new_behavior_runs':0,'update_started':False}
(o/'forward-mapping.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(census))
