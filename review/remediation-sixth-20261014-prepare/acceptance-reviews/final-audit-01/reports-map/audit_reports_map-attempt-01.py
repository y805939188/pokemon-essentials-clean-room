from pathlib import Path
from collections import Counter
import subprocess,sys,json,hashlib,datetime,time
ROOT=Path('/workspace/pokemon-essentials-clean-room');OUT=Path(__file__).resolve().parent;P='review/remediation-sixth-20261014-prepare/'
ENTRY='229260cfd5177581bb88bafd84770ceb1c11b117';REGISTER='d35356005f79b9fdffc5a4202a0b39e9255a36fa';ACT='86bbc99b28d93db4ed9d6897daf5f3725ccd1808';PREP='469a268b92daed7b4d28d7fd0da75520cbb7228f';FORMAL='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
start=datetime.datetime.now(datetime.timezone.utc).isoformat();commands=[];identities=[];cache={};errors=[]
def command(*args):
 t=datetime.datetime.now(datetime.timezone.utc).isoformat();q=subprocess.run(['git',*args],cwd=ROOT,capture_output=True);commands.append({'argv':['git',*args],'start_utc':t,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':q.returncode,'stdout_bytes':len(q.stdout),'stdout_sha256':hashlib.sha256(q.stdout).hexdigest(),'stderr':q.stderr.decode()});assert q.returncode==0,q.stderr.decode();return q.stdout
def payload(c,p):
 key=(c,p)
 if key not in cache:cache[key]=command('show',c+':'+p)
 return cache[key]
def identity(c,p,expected=None):
 b=payload(c,p);ent=command('ls-tree',c,'--',p).decode().strip();parts=ent.split(None,3);assert len(parts)==4 and parts[0]=='100644' and parts[1]=='blob',ent
 got={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()};assert got['git_blob']==parts[2]
 match=expected is None or all(got[k]==expected[k] for k in got);assert match,(c,p,got,expected)
 identities.append({'commit':c,'path':p,'mode':parts[0],'type':parts[1],**got,'declared_match':match});return got
def pointer(j,ptr):
 assert ptr.startswith('/'),ptr
 for x in ptr.split('/')[1:]:
  x=x.replace('~1','/').replace('~0','~');j=j[int(x)] if isinstance(j,list) else j[x]
 return j
def canonical(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def empty(x):return x is None or x==[] or x==0 or x is False
checks={};i=json.loads(payload(ENTRY,P+'integration/final-acceptance-audit-20261014/input.json'));identity(ENTRY,P+'integration/final-acceptance-audit-20261014/input.json');identity(ENTRY,P+'integration/final-acceptance-audit-20261014/prompt.md')
checks['registration_commit_tree_exact']=command('rev-parse',REGISTER+'^{tree}').decode().strip()==i['frozen_registration_workspace_tree']
checks['actual_and_registration_formal_tree_same']=command('rev-parse',ACT+':deliverables/final-specification-set').decode().strip()==command('rev-parse',REGISTER+':deliverables/final-specification-set').decode().strip()==FORMAL
for f in i['frozen_read_set']:identity(REGISTER,f['path'],f)
identity(ACT,i['actual_input']['path'],i['actual_input']);a=json.loads(payload(ACT,i['actual_input']['path']));checks['all_declared_frozen_read_set_and_actual_input_bytes_modes']=True
reports={};verdicts={};signatures=[];raw_signed=[];primary_owner={}
for g in i['five_independent_actual_reports']:
 group=g['group'];c=g['report_commit'];di=g['report_path'].rsplit('/',1)[0]
 assert command('rev-parse',c+'^{tree}').decode().strip()==g['report_workspace_tree'];assert command('rev-parse',c+':'+di).decode().strip()==g['report_directory_tree']
 ri=identity(c,g['report_path'],g['report_identity']);vi=identity(c,g['structured_verdict_path'],g['structured_verdict_identity']);text=payload(c,g['report_path']).decode();v=json.loads(payload(c,g['structured_verdict_path']));reports[group]=g;verdicts[group]=v
 assert ACT in text and FORMAL in text and 'UNVERIFIED' in text
 key={'A':'records','B':'ids','C':'rows','D':'per_id','E':'per_id'}[group];rows=v[key];ids=[x['id'] for x in rows];assert len(rows)==g['required_count'];assert len(set(ids))==len(ids);assert set(ids)==set(g['required_ids']);raw_signed+=ids
 for x in rows:primary_owner.setdefault(x['id'],[]).append(group)
 repairs={k:v[k] for k in ['required_repairs','necessary_content_revisions'] if k in v};assert all(empty(z) for z in repairs.values())
 assert v.get('formal_acceptance') in [False,None];assert v.get('CLOSED') is False
 signatures.append({'group':group,'required_count':len(rows),'commit':c,'workspace_tree':g['report_workspace_tree'],'directory_tree':g['report_directory_tree'],'report_path':g['report_path'],'report_identity':ri,'structured_verdict_path':g['structured_verdict_path'],'structured_verdict_identity':vi,'bound_actual_commit':ACT,'bound_formal_tree':FORMAL,'original_result':g['original_result'],'content_minimum_repairs':0,'effective_configuration':'UNVERIFIED','public_sync_pending_phrases':'Historical report-stage conditions, not new source/runtime acceptance gates','signature_qualification_checked':'Complete root report newly read; structured root/item identity and required verdict fields checked. No behavior re-review.'})
checks['five_report_and_structured_identity_tree_bindings']=True;checks['five_required_raw_lists_unique_and56_total']=len(raw_signed)==len(set(raw_signed))==56
mapping=i['required_mapping'];raw_mapping=[x['id'] for x in mapping];assert len(raw_mapping)==len(set(raw_mapping))==56;assert Counter(raw_mapping)==Counter(raw_signed);checks['one_primary_actual_group_per56']=all(len(v)==1 for v in primary_owner.values())
raw_batch=[]
for b in a['batches']:raw_batch+=b['required_ids']
assert len(raw_batch)==len(set(raw_batch))==56;assert Counter(raw_batch)==Counter(raw_mapping);checks['one_primary_current_batch_per56']=True
assert Counter(x['severity'] for x in mapping)=={'P2':39,'P3':17};checks['severities39P2_17P3']=True
syncpath=P+'integration/public-sync-20261014/sync-input.json';deppath=P+'integration/public-sync-20261014/dependency-status.json';ledgerpath=P+'ledger.json'
sync=json.loads(payload(REGISTER,syncpath));dep=json.loads(payload(REGISTER,deppath));ledger=json.loads(payload(REGISTER,ledgerpath));assert len(ledger['required'])==56 and len(set(x['id'] for x in ledger['required']))==56;currentledger={x['id']:x for x in ledger['required']};assert len(sync['items'])==len(dep['per_id'])==56
contracts={};selected=[];used=[]
for m in mapping:
 id=m['id'];group=m['actual_primary_group'];g=reports[group];v=verdicts[group];node=pointer(v,m['report_per_id_pointer']);assert node['id']==id;assert m['report_commit']==g['report_commit'] and m['report_path']==g['report_path'];used.append((group,m['report_per_id_pointer']))
 assert primary_owner[id]==[group];batches=[b for b in a['batches'] if id in b['required_ids']];assert len(batches)==1;b=batches[0];assert b['batch']==m['primary_batch'] and b['contract_path']==m['contract_path']
 path=m['contract_path']
 if path not in contracts:
  identity(ACT,path,m['contract_identity']);identity(PREP,path,m['contract_identity']);assert payload(ACT,path)==payload(PREP,path);contracts[path]=json.loads(payload(ACT,path))
 con=contracts[path];scope=pointer(con,m['contract_pointer']);assert scope['id']==id;assert scope['identity_and_verdict']['severity']==m['severity'];assert scope['dependencies_and_receivers']['primary_batch']==m['primary_batch'];assert id in con['required_ids']
 n_batch=node.get('batch',node.get('primary_batch',m['primary_batch']));assert n_batch==m['primary_batch'];assert node.get('actual_commit',v.get('actual_commit',ACT))==ACT
 n_severity=node.get('severity',node.get('priority',m['severity']));assert n_severity==m['severity'];n_verdict=node.get('actual_verdict',node.get('verdict',node.get('qualified_result',node.get('actual_content_verdict'))));assert 'PASS' in n_verdict
 nrep={k:node[k] for k in ['required_repairs','necessary_repairs','blocking_failures','minimum_substantive_changes','required_minimum_content_revision'] if k in node};assert nrep and all(empty(x) for x in nrep.values())
 if group=='B':
  assert node['contract']['path']==path and node['contract']['identity']==m['contract_identity'] and node['contract']['scope_pointer']==m['contract_pointer']
  for cell in node['seven_groups']:assert pointer(con,cell['json_pointer'])==scope[cell['group']] and canonical(scope[cell['group']])==cell['canonical_value_sha256']
 if group=='C':
  assert node['contract']['path']==path and node['contract']['pointer']==m['contract_pointer'];assert all(node['contract'][k]==m['contract_identity'][k] for k in ['bytes','sha256','git_blob'])
 if group=='D':
  for cell in node['seven_groups'].values():assert cell['contract_path']==path and cell['contract_identity']==m['contract_identity'];assert pointer(con,cell['contract_pointer']) is not None
 reg=pointer(sync,m['public_registry_item_pointer']);d=pointer(dep,m['dependency_item_pointer']);l=currentledger[id];assert reg['id']==d['id']==l['id']==id;assert reg['primary_batch']==d['primary_batch']==l['primary_batch']==m['primary_batch'];assert reg['actual_group']==d['actual_group']==group
 assert reg['contract_pointer']==d['contract_pointer']==m['contract_pointer'];assert reg['contract_path']==path and reg['contract_identity']==m['contract_identity'];assert reg['original_dependencies']==d['original_dependencies']==scope['dependencies_and_receivers']['original_dependencies'];assert pointer(con,d['necessary_consumers_pointer'])==scope['bidirectional_evidence']['necessary_consumers']
 for rr in [reg['actual_content_review'],d['primary_actual_review'],l['integrated_pass']]:
  assert rr['group']==group and rr['review_commit']==g['report_commit'] and rr['report_path']==g['report_path'] and rr['report_identity']==g['report_identity'];assert rr['verdict_path']==g['structured_verdict_path'] and rr['verdict_identity']==g['structured_verdict_identity'];assert rr['per_id_pointer']==m['report_per_id_pointer'];assert rr['actual_commit']==ACT and rr['actual_formal_tree']==FORMAL;assert rr['necessary_content_revisions']==0 and rr['effective_configuration']=='UNVERIFIED';assert rr['formal_acceptance'] is None and rr['CLOSED'] is False
 assert reg['formal_acceptance'] is None and reg['closed'] is False and d['formal_acceptance'] is None and d['closed'] is False and l['formal_acceptance'] is None and l['closed'] is False;assert d['static_actual_conditions_satisfied'] is True
 selected.append({'id':id,'severity':m['severity'],'primary_batch':m['primary_batch'],'current_candidate_commit':b['candidate_published_commit'],'actual_primary_group':group,'report_commit':g['report_commit'],'report_path':g['report_path'],'pointer_target_path':g['structured_verdict_path'],'report_per_id_pointer':m['report_per_id_pointer'],'pointer_target_kind':'Structured verdict JSON, not Markdown report','resolved_id':node['id'],'resolved_verdict':n_verdict,'required_repairs':nrep,'complete_target_record_canonical_sha256':canonical(node),'contract_path':path,'contract_identity':m['contract_identity'],'contract_pointer':m['contract_pointer'],'complete_contract_record_canonical_sha256':canonical(scope),'public_registry_target_path':syncpath,'public_registry_item_pointer':m['public_registry_item_pointer'],'dependency_target_path':deppath,'dependency_item_pointer':m['dependency_item_pointer'],'necessary_consumers_pointer':d['necessary_consumers_pointer'],'original_dependencies':d['original_dependencies'],'public_rule_summary':reg['rule_summary'],'case_controls':reg['case_controls'],'remaining_gates':d['remaining_gates'],'formal_acceptance':None,'CLOSED':False,'condition_result':'PASS_REPORT_IDENTITY_SIGNATURE_OWNER_AND_POINTER_MAP_ONLY'})
checks['all56_structured_pointers_exact_unique_and_not_markdown']=len(used)==len(set(used))==56
checks['all56_contract_id_severity_batch_pointers_match']=True;checks['all56_public_dependency_ledger_primary_review_pointers_match']=True;checks['all56_report_content_minimum_repairs_zero']=True;checks['all56_accepted0_closed0_open56']=True
checks['F002_E_primary_D_interface_once']=primary_owner['GR6-F-002']==['E'];checks['Arena_E_primary_B_interface_once']=primary_owner['GR6-F-V004']==['E'];checks['U14six_A_primary_C_interface_only']=all(primary_owner[id]==['A'] for id in next(b['required_ids'] for b in a['batches'] if b['batch']=='R6-U14'))
checks['group_counts11_9_19_9_8']=Counter(m['actual_primary_group'] for m in mapping)=={'A':11,'B':9,'C':19,'D':9,'E':8}
namespace=[{'batch':b['batch'],'candidate_commit':b['candidate_published_commit'],'required_ids':b['required_ids'],'contract_path':b['contract_path']} for b in a['batches']]
Ajoins=[{'actual_path':f['path'],'current_candidate_contributors':[{'batch':c['batch'],'commit':c['candidate_commit'],'path':c['candidate_path'],'identity':c['identity']} for c in f['contributions']]} for f in a['files'] if any(x in f['path'] for x in ['wp10-migration','wp34-inherit','wp62-pokedex','wp13-map','wp60-fishing','engine-overworld-wp11','pokemon-rules-wp53'])]
result={'reader':'/root/history_payload','start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cwd':str(ROOT),'argv':sys.argv,'runtime':sys.version,'entry_commit':ENTRY,'registration_commit':REGISTER,'actual_commit':ACT,'formal_tree':FORMAL,'checks':checks,'all_checks_pass':all(checks.values()),'identity_bindings':identities,'group_signature_qualification':signatures,'per56_pointer_results':selected,'current14_batch_namespace':namespace,'A_historical_shorthand_vs_current_selected_contributors':Ajoins,'semantic_boundary':'Complete five root reports newly read for signature/qualification; full structured bytes parsed and exact necessary pointers resolved. No new behavior/source review, no full contract/large history semantics repeated.','configuration':'UNVERIFIED','execution':{'author_scripts':0,'reference_source':0,'behavior_model':0,'host_Demo_real_save':0,'new_spawn':0,'CLI_config_probe':0},'formal_acceptance_count':0,'CLOSED_count':0,'OPEN_count':56,'commands':commands}
(OUT/'reports-map-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');(OUT/'per56-pointer-results.json').write_text(json.dumps(selected,ensure_ascii=False,indent=2)+'\n');(OUT/'five-report-signatures.json').write_text(json.dumps(signatures,ensure_ascii=False,indent=2)+'\n');(OUT/'current14-batch-map.json').write_text(json.dumps(namespace,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'all_checks_pass':result['all_checks_pass'],'checks':checks,'identity_count':len(identities),'required_count':len(selected),'group_counts':dict(Counter(x['actual_primary_group'] for x in selected))},ensure_ascii=False));assert result['all_checks_pass']
