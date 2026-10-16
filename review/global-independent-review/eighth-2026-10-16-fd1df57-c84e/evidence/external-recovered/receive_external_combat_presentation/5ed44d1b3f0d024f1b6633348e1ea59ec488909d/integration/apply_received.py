"""Integrate actual independently authored contributions. No child script/source is executed."""
from pathlib import Path
import json,hashlib,subprocess,datetime,os,collections
I=Path(__file__).resolve().parent;T=I.parent;ROOT=T.parents[1];REPO=Path('/workspace/pokemon-essentials-clean-room');PREFIX=str(T.relative_to(REPO));BASE='35d85e4484b892ebc32542346861440638d2183c';utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
def load(p):return json.loads(p.read_text())
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def old(n):return json.loads(subprocess.check_output(['git','show',BASE+':'+PREFIX+'/'+n]))
def ident(p):
 b=p.read_bytes();return {'path':str(p.relative_to(T)),'mode':'100644','bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
frozen=load(T/'frozen-denominator.json');f_by={r['id']:r for r in frozen['objects']};jobs=load(T/'continuation-contracts.json');expected={r['id']:set(r['ids'])for r in jobs['jobs']};children=load(I/'received-identities.json')['children'];providers={r['job']:r for r in children};received={};reverse=collections.defaultdict(list);interfaces=collections.defaultdict(list);qitems=[];field_checked=0;unit_proofs={};read_io={'02_ball_base_fields':['73f14f','853470','e62a7f','9dfb4c','e674a8','c5587f'],'03_fixed_choreography':['c1c3eb','833779','f60e08','3e3a0f'],'04_author_player':['c1c3eb','4e33d6','d64b6b','3e3a0f'],'05_capture_debug':['76bbda','fdd797','362781','60a4f4','c5587f']}
for job,provider in providers.items():
 P=I/'received'/job/provider['commit'];d=load(P/'reception-ledger.json');rs=d.get('objects',d.get('records',d.get('primary')));assert rs is not None
 assert {r['id']for r in rs}==expected[job]
 for r in rs:
  rid=r['id'];assert rid not in received;o=f_by[rid]
  original=r.get('original_complete_object',r.get('original_complete'))
  if original is not None:assert original==o,(job,rid,'original object differs from frozen contract')
  else:
   assert r['origin_file']==o['origin_file']and r['origin_pointer']==o['origin_pointer']
   if o['population']=='manual':assert r['original_assertion']==o['meaning']['assertion']
   elif o['population']=='RGB_field':assert r['received_meaning']['rgb']==o['meaning']['rgb'];field_checked+=1
   else:assert r['value']==o['meaning']['value']and r['received_meaning']['exact_value']==o['meaning']['value']and r['index']==o['meaning']['index']and r['field']==o['meaning']['field'];field_checked+=1
  meaning=r.get('received_meaning',r.get('current_effective_meaning',r.get('accepted_complete_meaning')));assert meaning is not None
  received[rid]={'job':job,'provider':provider,'original':o,'record':r,'meaning':meaning,'payload':ident(P/'reception-ledger.json'),'pointer':('/objects/'if 'objects'in d else'/records/'if 'records'in d else'/primary/')+str(rs.index(r))}
 if job.startswith('02'):
  assert len(rs)==618 and not d['remaining']['necessary_unread_objects']and not d['remaining']['necessary_unreceived_units'];qitems += [{'job':job,**q}for q in d['qualifications']]
 elif job.startswith('03'):assert d['counts']['exact_source_objects_unread']==d['counts']['necessary_units_unreceived']==0
 elif job.startswith('04'):
  assert d['primary_unreceived']==0 and d['necessary_units_unreceived']==[];q=load(P/'qualifications.json');qitems += [{'job':job,'id':'CP04-Q%02d'%(i+1),'objects':r['ids'],'received_meaning':r['meaning']}for i,r in enumerate(q['evidence_only_clarifications'])]
 elif job.startswith('05'):assert d['unread_primary']==d['necessary_unreceived']==0
 fd=load(P/'interfaces.json');proof={'job':job,'commit':provider['commit'],'context':provider['context_parent_supplied'],'payload':ident(P/'interfaces.json')}
 if job.startswith('02'):
  orig={x['id']:x for x in fd['reverse_group']['subassertions']}
  for i,r in enumerate(fd['reverse_receipts']):reverse[r['id']].append({**proof,'pointer':'/reverse_receipts/'+str(i),'original':orig[r['id']],'status':r['status'],'meaning':r['producer_join'],'raw_receipt':r})
 elif job.startswith('03'):
  for i,r in enumerate(d['reverse_receipts']):reverse[r['id']].append({**proof,'payload':ident(P/'reception-ledger.json'),'pointer':'/reverse_receipts/'+str(i),'original':r['original_subassertion'],'status':r['independent_status'],'meaning':r['independent_reason'],'raw_receipt':r})
 elif job.startswith('04'):
  for i,r in enumerate(fd['reverse_current_contribution']):reverse[r['id']].append({**proof,'pointer':'/reverse_current_contribution/'+str(i),'original':r['original_complete'],'status':r['status'],'meaning':r['accepted_meaning_and_reason'],'raw_receipt':r})
 else:
  for i,g in enumerate(fd['reverse']):
   for j,r in enumerate(g['checks']):reverse[r['original']['id']].append({**proof,'pointer':f'/reverse/{i}/checks/{j}','original':r['original'],'status':r['status'],'meaning':r['received_meaning_and_join'],'raw_receipt':r})
 irs=fd.get('selected_reverse_interfaces',fd.get('records'))
 for i,r in enumerate(irs):
  orig=r.get('original',r.get('original_complete',r.get('original_complete_interface')));rid=orig['id'];interfaces[rid].append({**proof,'pointer':('/records/'if job.startswith('03')else'/selected_reverse_interfaces/')+str(i),'original':orig,'status':r.get('status',r.get('independent_status')),'meaning':r.get('meaning',r.get('producer_consumer_join',r.get('received_meaning',r.get('independent_join')))),'raw_receipt':r})
 rd=load(P/'reading-ledger.json');unit_proofs[job]={'commit':provider['commit'],'reader_context':provider['context_parent_supplied'],'context_authority':'Parent actual dispatch and fixed result handoff; child02/03 opaque self-echo remains UNVERIFIED. No inferred model configuration.','reading_ledger':ident(P/'reading-ledger.json'),'units':rd.get('units',rd.get('reads',rd.get('records'))),'own_read_credit':'Provider alone; root direct source intervals unchanged.','integration_io':read_io[job]}
qitems += [
 {'job':'03_fixed_choreography','id':'CP03-EVIDENCE-001','objects':['EXTCP-F052.A03'],'received_meaning':'对方排列条正确坐标(248-bitmap.width,114)，球(174,84)；width248时条X0而非-248。保留原错误，不新增正式必修。'},
 {'job':'03_fixed_choreography','id':'CP03-EVIDENCE-002','objects':['EXTCP-F051.A03'],'received_meaning':'floor(W/2)初始相对动作与floor(-W/2)后续增量分列，第二值不是最终偏移；W513原X0先256后-1，偶宽512终0。静态推导。'},
 {'job':'03_fixed_choreography','id':'CP03-EVIDENCE-003','objects':['EXTCP-F058.A02'],'received_meaning':'捕获trainer是battle.pbPlayer即player[0]、手位player_1，不是目标owner或任意席位owner；普通派出另按席位owner。'},
 {'job':'05_capture_debug','id':'CP05-Q01','objects':['EXTCP-F078.A08'],'received_meaning':'255上限只限FAST/LEVEL/LURE/HEAVY/LOVE/MOON六个具名出口；HEAVY另有率0早返和非零下限1。Timer输入率100第10轮可400，不能整族先钳255。'},
 {'job':'05_capture_debug','id':'CP05-Q02','objects':['EXTCP-F066.A02','EXTCP-F079.A03'],'received_meaning':'异兽非BEAST前置或非异兽BEAST除十保留输入数值类型：正常整数率45→4；显式浮点依该类型，不把内部类型自动变未来API。'},
 {'job':'05_capture_debug','id':'CP05-Q03','objects':['EXTCP-F064.A01','EXTCP-F064.A02','EXTCP-F064.A03'],'received_meaning':'caught/seen包装受internalBattle门，直接owned/shadow写无该门；图鉴页能力读全局player，而owned查询/写入接收battle.pbPlayer。正常同一对象，不外推任意副本。'},
 {'job':'05_capture_debug','id':'CP05-Q04','objects':['EXTCP-F076.A01','EXTCP-F076.A02'],'received_meaning':'handler只有nil回退，false/0保持；raw add不转id，查找/trigger才转换合格非Symbol对象，空子类无registry解析。通知不等统一领域成功/消费。'},
 {'job':'05_capture_debug','id':'CP05-Q05','objects':['EXTCP-F062.A05'],'received_meaning':'调试非在场候选不保证可换入，caller再验；空集nil，非空最多50次让渡。controlPlayer=true真实模拟走AI旁路，不能由直接辅助move缺失推整个模拟失败。'},
 {'job':'05_capture_debug','id':'CP05-Q06','objects':['EXTCP-F065.A06'],'received_meaning':'重选后的投掷用新battler.index，藏球仍传最初idxBattler；入口1倒下/同伴3存活时投3、隐藏框参数1。只核参数链，不授必隐藏重选框或新正式finding。'},
 {'job':'05_capture_debug','id':'CP05-Q07','objects':['EXTCP-F065.A07'],'received_meaning':'first-ball失败标志只在非4且到达末尾时更新；挡球早返/nil目标/更早异常不自动更新或计失败；直接投球不自带背包扣减，已登记消耗需此前提。'}
]
dump(I/'mandatory-qualifications.json',{'schema':'gr8-cp-integrated-qualifications/v1','records':qitems,'original_qualified_sources':'Full immutable provider reports/ledgers retained; no new product policy or required edit.','reverse_credit_restrictions':['R015.4 and R019.4 source supplement only, not literal formal-detail coverage','R019.6 formal locator must include WP67-A9.4 lines267/271'],'UPDATE_NOT_STARTED':True})
assert len(received)==879 and field_checked==512
legacy=frozen['reverse_population']['objects'];all_rev={r['id']:r for g in legacy['clauses']for r in g['subassertions']};all_ir={r['id']:r for r in legacy['selected_interface_assertions']}
for rid,proofs in reverse.items():assert all(p['original']==all_rev[rid]for p in proofs)
for rid,proofs in interfaces.items():assert all(p['original']==all_ir[rid]for p in proofs)
assert len(reverse)==55 and sum(map(len,reverse.values()))==66
assert len(interfaces)==20 and sum(map(len,interfaces.values()))==30
# Narrow rather than overwrite broader raw evidence. Both provider receipts remain recoverable.
reverse_matrix=[]
for rid,original in all_rev.items():
 ps=reverse.get(rid,[]);status='FINITE_CONTRIBUTION_RECEIVED'if ps else'PENDING_01_OR_06_ACTUAL_RESULT'
 if rid in ['EXTCP-R015.4','EXTCP-R019.4']and ps:status='SOURCE_SUPPLEMENT_RECEIVED_NOT_LITERAL_FORMAL_COVERAGE'
 if rid=='EXTCP-R019.6'and ps:status='FINITE_CONTRIBUTION_RECEIVED_WITH_FORMAL_LOCATOR_CORRECTION_9_4'
 reverse_matrix.append({'id':rid,'original':original,'status':status,'actual_receipts':ps,'count_credit':1 if ps else 0,'claim':'No full parent formal/domain approval from locator arrays.'})
interface_matrix=[]
for rid,original in all_ir.items():
 ps=interfaces.get(rid,[]);status='ROOT_SCOPE_PRECISION_DECISION_OPEN'if rid=='EXTCP-IR012'else'FINITE_FACT_JOIN_RECEIVED'
 interface_matrix.append({'id':rid,'original':original,'status':status,'actual_receipts':ps,'unique_disposition_credit':1,'primary_atom_credit_from_interface':0,'whole_foreign_domain_credit':0})
prior=old('reception-ledger.json');out=[]
for oldr in prior['objects']:
 rid=oldr['id'];r=dict(oldr)
 if rid in received:
  item=received[rid];p=item['provider'];raw=item['record'];r['prior_35d85e4_status']=oldr['status'];r['original_target_meaning']=oldr['actual_complete_meaning'];r['actual_complete_meaning']=item['meaning'];r['status']='COMPLETE_FINITE_CONTRIBUTION_RECEIVED';r['reader']=p['context_parent_supplied'];r['integrator_context']=os.environ.get('CODEX_THREAD_ID','UNVERIFIED');r['receipt_basis']={'commit':p['commit'],'checkout_tree':p['checkout_tree'],'task_tree':p['task_tree'],'payload':item['payload'],'pointer':item['pointer'],'provider_decision':raw.get('receipt',raw.get('independent_decision',raw.get('decision',raw.get('status')))),'actual_provider_reads':unit_proofs[item['job']]['reading_ledger'],'root_contribution_read_io':read_io[item['job']],'no_duplicate_source_review':'Per parent instruction, actual provider contribution/qualification integrated; source whole-file read credit remains provider only.'}
  r['reason']=raw.get('comparison_reason',raw.get('verification_reason',raw.get('reason',item['meaning'])));r['formal_reception']=raw.get('formal_value_coverage',raw.get('formal_credit',raw.get('current_formal_locator','FINITE_CURRENT_FORMAL_JOIN_AS_PROVIDER_RECORD')));r['mandatory_received_qualifications']=[q for q in qitems if rid in q.get('objects',[])];r['direct_source_read_here_at_prior_checkpoint']=rid in {x['id']for x in prior['objects']if x['source_read_io']};r['necessary_unreceived_in_this_finite_contribution']=[]
 out.append(r)
assert sum(x['status']=='COMPLETE_FINITE_CONTRIBUTION_RECEIVED'for x in out)==879
pending=[x['id']for x in out if x['status']!='COMPLETE_FINITE_CONTRIBUTION_RECEIVED'];assert set(pending)==expected['01_scene_input_objects']
rec={**prior,'schema':'gr8-cp-independent-reception/v2','updated_utc':utc,'status':'INCOMPLETE_WAITING_ACTUAL_01_06_RESULTS','source_checked':680,'source_checked_scope':'Original root direct source checks only; unchanged by delegated receipts.','source_available_unread':166,'source_available_unread_scope':'Current semantic objects lacking actual independent reception; not root direct source lines.','complete_finite_receptions':879,'remaining_final_receptions':166,'received_current_effective_objects':879,'root_direct_source_checked_at_initial_checkpoint':680,'objects':out,'pending_object_ids':pending,'pending_auxiliary_job':'06_qualifications_interfaces','old_three_subset_of_02_not_added_again':True,'independent_receipts':[{k:v for k,v in p.items()if k!='files'}for p in children],'root_task_final':'OPEN_MAIN_REVIEWER_ONLY','UPDATE_NOT_STARTED':True}
dump(T/'reception-ledger.json',rec)
iface=old('interfaces.json');iface.update(schema='gr8-cp-independent-interfaces/v2',status='INCOMPLETE_WAITING_ACTUAL_01_06_RESULTS',unique_legacy_reverse_subassertions_received=55,legacy_reverse_subassertions_pending=95,raw_reverse_receipt_occurrences=66,selected_interface_unique_dispositions_received=20,selected_interface_finite_fact_joins=19,selected_interface_root_scope_pending=['EXTCP-IR012'],raw_selected_interface_receipt_occurrences=30,reverse_matrix=reverse_matrix,selected_interface_matrix=interface_matrix,IF06_finite_contribution=load(I/'received/04_author_player/a19dcfcaba117a746545760e888e224695b1bbe9/interfaces.json')['IF06'],whole_original_named_interface_final_signatures='No expansion from these finite facts; remaining global/history/provider joins remain06/root.');dump(T/'interfaces.json',iface)
proposal=old('proposal-counters.json');q04=load(I/'received/04_author_player/a19dcfcaba117a746545760e888e224695b1bbe9/qualifications.json')
for r in proposal['records']:
 if r['id']=='GR8-EXTCP-H001':
  r['status']='INDEPENDENT_NONPROPOSER_COUNTEREVIDENCE_RECEIVED_NO_REQUIRED_SUPPORTED_ROOT_CANONICAL_PENDING';r['independent_source_verification']=q04['H001'];r['source_commit']='a19dcfcaba117a746545760e888e224695b1bbe9';r['root_decision']='Main reviewer only; original withdrawal/error preserved.'
 else:r['received_additional_evidence']={'02':providers['02_ball_base_fields']['commit'],'03':providers['03_fixed_choreography']['commit'],'04':providers['04_author_player']['commit'],'scope':'Complete finite cry/source joins and strongest scope arguments received; overall precision/ownership and actual ELR receipt stay main reviewer. No new required/optional/policy adopted.'}
proposal['status']='INCOMPLETE_WAITING_ACTUAL_01_06_RESULTS';dump(T/'proposal-counters.json',proposal)
reading=old('reading-ledger.json');reading['schema']='gr8-cp-actual-reading-ledger/v2';reading['updated_utc']=utc;reading['prior_direct_read_checkpoint']=BASE;reading['received_independent_contributions']=unit_proofs;reading['current_effective_semantic_receipts']={'objects':879,'manual':367,'release_fields':224,'capture_fields':272,'RGB_fields':16,'pending_primary':166,'new_direct_reference_or_business_execution':0,'credit':'Actual four different provider contexts; no root duplicate source reading claim.'};reading['integration_truncation_repairs']=[{'io':'187dc2','repair':'05 entire50 necessary scope purposes/ranges repaired c5587f;02 full25 already before truncation. No direct source credit.'},{'io':'833779','incident':'Metadata preview TypeError None due04 keyprimary; header slices locator-only; no acceptance inferred from failure.','repair':'04 body67 rows4e33d6/d64b6b;03 semantic decisions833779/f60e08 complete.'},{'io':'f60e08','repair':'NewH001 proof4e33d6;embedded original CP002 proven same frozen original and already read earlier; repeated wrapper not new semantic credit.'},{'io':'962abc','repair':'03 reverse18/currentinterfaces16 and04 reverse21/interfaces3 reproduced without repeated identity metadata3e3a0f.'}];dump(T/'reading-ledger.json',reading)
progress=old('progress.json');progress.update(utc=utc,state='INCOMPLETE_WAITING_ACTUAL_01_06_RESULTS',complete_finite_receptions=879,remaining_final_receptions=166,source_available_unread=166,source_checked=680,source_checked_scope='Root direct historical checks, not provider sum',received_independent_jobs=4,pending_actual_jobs=['01_scene_input_objects','06_qualifications_interfaces'],child_jobs_created=0,CP002='OPEN_MAIN_REVIEWER',H001='ACTUAL_NONPROPOSER_COUNTEREVIDENCE_RECEIVED');progress['initial_core_commit']=progress.pop('core_commit',None);progress['initial_core_remote_full_bytes_verified']=progress.pop('core_remote_full_bytes_verified',False);progress['integration_core_binding']='integration/publication.json';progress['actual_contexts_created_by_parent']=6;progress['contexts_spawned_by_integrator']=0;dump(T/'progress.json',progress)
# Original frozen six contracts and old failed/raw evidence remain immutable.
summary={'schema':'gr8-cp-integration-receipt/v1','utc':utc,'state':'INCOMPLETE_WAITING_ACTUAL_01_06_RESULTS','instruction':'Direct actual contribution integration; no new reviewer or repeated whole primary source review.','integrator':os.environ.get('CODEX_THREAD_ID','UNVERIFIED'),'providers':children,'unique_received_objects':879,'pending_primary_objects':166,'pending_auxiliary':['06_qualifications_interfaces'],'old_finite3_subset_not_added':True,'field_values_identical_to_previous_actually_read_values':512,'unique_reverse_subassertions':55,'reverse_occurrences_not_denominator':66,'unique_selected_interface_dispositions':20,'finite_selected_joins':19,'scope_pending':['EXTCP-IR012/GR8-EXTCP-002 main reviewer'],'source_group_or_foreign_credit_from_locator_arrays':0,'new_required':0,'new_optional':0,'new_policy_adopted':0,'business_execution':'NOT_EXECUTED','new_contexts_spawned_by_integrator':0,'root_task_final':'OPEN_MAIN_REVIEWER_ONLY','UPDATE_NOT_STARTED':True}
dump(I/'current-reception.json',summary)
print(json.dumps({k:summary[k]for k in ['state','unique_received_objects','pending_primary_objects','unique_reverse_subassertions','reverse_occurrences_not_denominator','unique_selected_interface_dispositions','finite_selected_joins']}))
