import json,pathlib,subprocess,hashlib,datetime,collections,sys
out=pathlib.Path(__file__).resolve().parent
base='review/remediation-sixth-20261014-prepare/'
reg='d35356005f79b9fdffc5a4202a0b39e9255a36fa'
actual='86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
packet='229260cfd5177581bb88bafd84770ceb1c11b117'
clock=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
receipt={'start_utc':clock(),'identity_reads':[],'failures':[],'checks':[]}
cache={}
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def read(ref,path):
 spec=ref+':'+path
 if spec in cache:return cache[spec]
 start=clock();r=subprocess.run(['git','show',spec],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if r.returncode:
  receipt['failures'].append({'input':spec,'start_utc':start,'end_utc':clock(),'exit':r.returncode,'stderr':r.stderr.decode()});raise RuntimeError(spec+' unavailable')
 cache[spec]=r.stdout;receipt['identity_reads'].append({'input':spec,'start_utc':start,'end_utc':clock(),'exit':0,**identity(r.stdout),'qualification':'Whole byte identity/JSON structure; semantic credit limited to separately displayed fields/ranges. No source behavior execution.'});return r.stdout
def get(ref,path):return json.loads(read(ref,path))
def ptr(o,p):
 for k in p.strip('/').split('/'):o=o[int(k)] if isinstance(o,list) else o[k]
 return o
def check(name,condition,details=None):
 receipt['checks'].append({'name':name,'pass':bool(condition),'details':details});assert condition,name
try:
 inp=get(packet,base+'integration/final-acceptance-audit-20261014/input.json')
 dep=get(reg,inp['dependency_status']['path']);check('dependency exact bytes',identity(read(reg,inp['dependency_status']['path']))==inp['dependency_status']['identity'])
 ai=get(actual,inp['actual_input']['path']);check('actual input exact bytes',identity(read(actual,inp['actual_input']['path']))=={k:inp['actual_input'][k] for k in ['bytes','sha256','git_blob']})
 graph=get(reg,dep['fixed_graph_path']);check('original graph identity',identity(read(reg,dep['fixed_graph_path']))==dep['fixed_graph_identity']);check('original graph unchanged vs preparation',read(reg,dep['fixed_graph_path'])==read(ai['preparation_commit'],dep['fixed_graph_path']))
 check('original 110 edges no omission/addition/reordering/core rewrite',len(graph['edges'])==len(dep['edges'])==110 and all(e['index']==n and {k:e[k] for k in old}==old for n,(old,e) in enumerate(zip(graph['edges'],dep['edges']))))
 nodes=set(x for e in graph['edges'] for x in [e['from'],e['to']]);check('original100 nodes',len(nodes)==dep['nodes_count']==100)
 counts=collections.Counter(e['status'] for e in dep['edges']);check('108 static/process and2 future gates',counts['SATISFIED_FOR_STATIC_CONTENT']==108 and len(counts)==3 and all(e['status'].startswith('PENDING_') for e in dep['edges'][108:]))
 batch={b['batch']:b for b in ai['batches']};reports={r['group']:r for r in inp['five_independent_actual_reports']};check('14 current primary batches',len(batch)==14)
 files={f['path']:f for f in ai['files']};structured={}
 for group,r in reports.items():
  check('group '+group+' root report identity',identity(read(r['report_commit'],r['report_path']))==r['report_identity'])
  check('group '+group+' structured identity',identity(read(r['report_commit'],r['structured_verdict_path']))==r['structured_verdict_identity']);structured[group]=get(r['report_commit'],r['structured_verdict_path'])
  check('group '+group+' bound finite actual',r['bound_actual_commit']==actual and r['bound_actual_formal_tree']==inp['frozen_formal_tree'] and r['content_minimum_repairs']==0 and r['effective_configuration']=='UNVERIFIED' and r['global_configuration_certificate'] is False)
 for b in batch.values():
  r=b['independent_review'];report=read(r['review_commit'],r['report_path']);check(b['batch']+' candidate PASS receipt identity',identity(report)==r['report_identity'])
  # U04's original metadata intentionally has no required_repairs scalar.
  # Its exact fixed report L1-3 and132-136 were separately read; do not invent it.
  repairs_ok=r['required_repairs']==0 if 'required_repairs' in r else b['batch']=='R6-U04' and r['state']=='CANDIDATE_PASS' and '本固定候选无必要实质修订' in report.decode()
  check(b['batch']+' finite candidate signature binding',r['candidate_published_commit']==b['candidate_published_commit'] and r['scope_ids']==b['required_ids'] and repairs_ok and r['effective_configuration']=='UNVERIFIED',{'declared_required_repairs':r.get('required_repairs','FIELD_ABSENT_IN_ORIGINAL_METADATA'),'absent_field_qualification':'U04 exact fixed report explicit no required substantive repair; no source scalar filled in.' if 'required_repairs' not in r else None})
 edges=[]
 for n,e in enumerate(dep['edges']):
  tests=[];proof=e['evidence'];kind=e['kind']
  if kind in ['candidate_review','candidate_acceptance']:
   bid=e['from'][:6];b=batch[bid];r=b['independent_review'];tests.append(proof['candidate_PASS_review']==r['review_commit'])
   if kind=='candidate_review':tests.append(proof['candidate']==b['candidate_published_commit'])
   else:tests.extend([proof['actual_commit']==actual,'distinct from formal acceptance' in proof['meaning']])
  elif kind=='shared_candidate_receive':
   b=batch[e['from']];path=proof['path'];cp=base+'candidates/'+b['batch']+'/mirror/'+path
   cand=read(b['candidate_published_commit'],cp);cur=read(actual,path);original=read(ai['fixed_main'],path)
   tests.extend([path in b['all_candidate_allowlist_paths'],proof['candidate_commit']==b['candidate_published_commit'],identity(cand)==proof['candidate_identity'],identity(cur)==proof['actual_identity'],proof['actual_commit']==actual])
   changed=cand!=original;tests.append((proof['mode']=='CHANGED_CONTRIBUTION_RECEIVED')==changed)
   contributors=[c for c in files.get(path,{}).get('contributions',[]) if c['batch']==b['batch']]
   if changed:tests.append(len(contributors)==1 and contributors[0]['candidate_commit']==b['candidate_published_commit'] and contributors[0]['candidate_path']==cp and contributors[0]['identity']==identity(cand))
   else:tests.append(not contributors and proof['mode']=='NO_CANDIDATE_DELTA_BASELINE_OR_READONLY_RECEIVER')
   expected_groups={m['actual_primary_group'] for m in inp['required_mapping'] if m['primary_batch']==b['batch']};tests.append(set(proof['formal_review_primary_groups'])==expected_groups)
  elif kind=='actual_integrated_non_author_global_review':tests.extend([proof['actual_commit']==actual,proof['unique_ids']==56,proof['groups']==list('ABCDE'),proof['configuration_certificate'] is False])
  elif kind=='formal_acceptance':tests.extend([proof['independent_registry_PASS'] is None,proof['formal_acceptance']==0,e['status']=='PENDING_EXACT_FINAL_REGISTRY_AUDIT_THEN_FORMAL_ACCEPTANCE'])
  elif kind=='final_registration_after_all_dependencies':tests.extend([proof['CLOSED']==0,proof['all_required_OPEN']==56,e['status']=='PENDING_FORMAL_ACCEPTANCE_THEN_FINAL_CLOSED_REGISTRATION'])
  else:tests.append(False)
  check('edge '+str(n)+' exact disposition binding',all(tests))
  edges.append({'index':n,'original_pointer':'/edges/'+str(n),'original_edge':graph['edges'][n],'from':e['from'],'to':e['to'],'kind':kind,'registered_status':e['status'],'audit_condition_verdict':'PASS','qualified_disposition':'STATIC_OR_PROCESS_SATISFIED' if n<108 else 'FUTURE_GATE_CORRECTLY_PENDING','evidence_binding_pass':all(tests),'scope':'No new original edge; source/material/unchanged receiver not promoted to new implementation/execution.'})
 shared=[e for e in dep['edges'] if e['kind']=='shared_candidate_receive'];check('all original prospective batch/path pairs preserved',{(e['from'],e['evidence']['path']) for e in shared}=={(b['batch'],p) for b in batch.values() for p in b['all_candidate_allowlist_paths']})
 modecounts=collections.Counter(e['evidence']['mode'] for e in shared);check('76 changed contributions plus3 readonly pairs',modecounts=={'CHANGED_CONTRIBUTION_RECEIVED':76,'NO_CANDIDATE_DELTA_BASELINE_OR_READONLY_RECEIVER':3})
 ids=[];projection=json.loads((out/'contract-and-condition-projection.json').read_text())
 for n,m in enumerate(inp['required_mapping']):
  d=ptr(dep,m['dependency_item_pointer']);s=ptr(get(reg,m['contract_path']),m['contract_pointer']);r=reports[m['actual_primary_group']];v=ptr(structured[r['group']],m['report_per_id_pointer']);review=d['primary_actual_review']
  check(m['id']+' contract exact identity',identity(read(reg,m['contract_path']))==m['contract_identity'])
  check(m['id']+' original deps/consumers pointer and primary preserved',d['id']==s['id']==v['id']==m['id'] and d['original_dependencies']==s['dependencies_and_receivers']['original_dependencies'] and d['necessary_consumers_pointer']==m['contract_pointer']+'/bidirectional_evidence/necessary_consumers' and d['primary_batch']==m['primary_batch']==s['dependencies_and_receivers']['primary_batch'] and d['actual_group']==m['actual_primary_group'])
  ptr(get(reg,m['contract_path']),d['necessary_consumers_pointer'])
  check(m['id']+' actual signature exact binding',review['review_commit']==r['report_commit'] and review['report_path']==r['report_path'] and review['report_identity']==r['report_identity'] and review['actual_commit']==actual and review['actual_formal_tree']==inp['frozen_formal_tree'] and review['id']==m['id'] and review['per_id_pointer']==m['report_per_id_pointer'] and m['id'] in r['required_ids'])
  check(m['id']+' static conditions and future gates truthful',d['static_actual_conditions_satisfied'] and d['formal_acceptance'] is None and d['closed'] is False and d['remaining_gates']==['independent exact public registry/dependency audit','formal acceptance','final CLOSED registration'])
  check(m['id']+' candidate one primary receipt',m['id'] in batch[m['primary_batch']]['required_ids'])
  verdict=v.get('verdict',v.get('actual_verdict',v.get('qualified_result','')));check(m['id']+' structured finite PASS', 'PASS' in verdict and all(v.get(k) in [None,0,[],False] for k in ['required_repairs','necessary_repairs','blocking_failures','minimum_substantive_changes','required_minimum_content_revision']))
  ids.append({'id':m['id'],'primary_batch':m['primary_batch'],'actual_primary_group':m['actual_primary_group'],'original_contract_path':m['contract_path'],'original_contract_pointer':m['contract_pointer'],'necessary_consumers_pointer':d['necessary_consumers_pointer'],'dependency_status_pointer':m['dependency_item_pointer'],'original_dependency_fields_exact':True,'consumer_pointer_resolves':True,'single_primary_actual_signature_bound':True,'current_candidate_receipt_bound':True,'static_dependency_condition_verdict':'PASS','minimum_registry_fix':None,'original_dependencies':d['original_dependencies'],'existing_limits_preserved':True,'eligible_for_scoped_formal_acceptance_dependency_dimension':True,'remaining_gates':['root composite exact public registry/dependency audit','R6-I scoped formal acceptance','R6-I final CLOSED registration'],'formal_acceptance':0,'CLOSED':False})
 check('56 unique IDs and primary groups11/9/19/9/8',len(ids)==len({r['id'] for r in ids})==56 and collections.Counter(r['actual_primary_group'] for r in ids)==dict(zip('ABCDE',[11,9,19,9,8])))
 check('severity39P2/17P3',collections.Counter(m['severity'] for m in inp['required_mapping'])=={'P2':39,'P3':17})
 expected=[{'id':'GR6-F-002','primary_group':'E','supplement_groups':['D'],'satisfied_content_only':True,'counted_required_once':True},{'id':'GR6-F-V004','primary_group':'E','supplement_groups':['B'],'satisfied_content_only':True,'counted_required_once':True}]
 check('F002 E/D andArena E/B counted once',dep['qualified_joint_interfaces'][:2]==expected)
 joint=dep['qualified_joint_interfaces'][2];check('U14 A primary/C finite supplements',joint['primary_group']=='A' and joint['supplement_groups']==['C'] and joint['ids']==batch['R6-U14']['required_ids'])
 receipt.update(end_utc=clock(),exit=0,registration_commit=reg,actual_semantic_commit=actual,graph_nodes=100,original_edges=110,static_or_process_satisfied=108,future_gates_correctly_pending=2,shared_pair_modes=dict(modecounts),required_ids=56,condition_result='DEPENDENCY_REGISTRY_PASS_SCOPED_STATIC',eligible_for_scoped_formal_acceptance_dependency_dimension=True,minimum_registry_fixes=[],configuration='UNVERIFIED',formal_acceptance=0,CLOSED=0,OPEN=56,new_source_behavior_model_host_save_execution=0)
 (out/'edge-conditions.json').write_text(json.dumps(edges,ensure_ascii=False,indent=2)+'\n');(out/'per-id-conditions.json').write_text(json.dumps(ids,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:v for k,v in receipt.items() if k not in ['identity_reads','checks','failures']},ensure_ascii=False,indent=2));print('checks',len(receipt['checks']),'identities',len(receipt['identity_reads']))
except Exception as e:
 receipt.update(end_utc=clock(),exit=1,error=repr(e));print(json.dumps({'exit':1,'error':repr(e),'failures':receipt['failures']},ensure_ascii=False,indent=2));raise
finally:(out/'identity-and-conditions-audit.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
