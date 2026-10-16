"""Seal personally completed bounded review. Checks are static evidence consistency only."""
import collections,datetime,gzip,hashlib,json,pathlib,subprocess
P=pathlib.Path(__file__).resolve().parent
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
J=lambda v:json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':'))
H=lambda v:hashlib.sha256(J(v).encode()).hexdigest()
def read(n):return json.loads((P/n).read_text())
def write(n,v):(P/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
# Check every row of each author stratum against its exact original array. No original helper is run.
originals={i:read('originals/'+str(i)) for i in range(25) if i not in (2,9)}
def ptr(v,p):
 for k in p.strip('/').split('/') if p else []:v=v[int(k)] if isinstance(v,list) else v[k.replace('~1','/').replace('~0','~')]
 return v
strata=[]
for s in read('inputs/typed-purpose-strata.json')['strata']:
 fi,p=s['anchor'].split('#');a=([r['exact_reception_override'] for r in originals[21]['records'] if 'exact_reception_override' in r] if p=='/exact_override_purpose_stratum' else ptr(originals[int(fi[4:])],p));seen=[];errors=[]
 for g in s['groups']:
  for lo,hi in g['complete_inclusive_index_runs']:
   for n in range(lo,hi+1):
    seen.append(n)
    for k,v in g['exact_values'].items():
     if a[n].get(k)!=v:errors.append([n,k])
 result={'anchor':s['anchor'],'rows':len(a),'all_row_keysets':sorted({tuple(sorted(r)) for r in a}),'declared_purpose':s['purpose'],'complete_exact_index_cover':sorted(seen)==list(range(len(a))),'exact_projected_values_match':not errors,'whole_original_array_identity_equal':H(a)==s['original_array_sha256'],'declared_keysets_equal':sorted({tuple(sorted(r)) for r in a})==sorted(tuple(k) for k in s['all_row_keysets']),'original_array_sha256':H(a),'all_fields_disposition':'Identity/locator coordinates handled by exact key/type/index; all status/purpose/conditions/overrides read in own full scope views. Locations do not approve referenced bodies.','target_body_credit':0}
 strata.append(result)
assert all(all(s[k] for k in ('complete_exact_index_cover','exact_projected_values_match','whole_original_array_identity_equal','declared_keysets_equal')) for s in strata)
write('typed-reception.json',{'schema':'gr8-d-all-15-strata-reception/v1','utc':UTC,'all15_complete':True,'strata':strata,'independent_additional_factoring':'private/typed-index-inventory.json:17 arrays; extra current56/derived323 read as purpose/status, not target source bodies','locator_target_approval':False,'not_global_source_review':True})
# Retain the old incomplete stage as history; the previous committed bytes remain retrievable.
if not (P/'checkpoint-history.json').exists():
 old=read('progress.json');write('checkpoint-history.json',{'schema':'gr8-d-preserved-checkpoint/v1','prior_progress':old,'prior_core':'6220f4248ab1331553817c9cf9f810bb1d317d3b','prior_publication_successor':'b3580edf37ca9e824297fc3118913794308abe1b','qualification':'These INCOMPLETE states remain true at their generation time. The successor below records new actual reading rather than rewriting history.'})
# Explicit actual personal read events. These lists refer to complete, untruncated tool displays.
events={'remaining_frames_0_to_8':'Full current regenerated remaining-000..008.jsonl, through V1306; earlier typed-index skip bug repaired before any completion claim','work_frames':{},'graph_frames':['8f18e5','f36309','5d2f38','fdaf50','454915','1d721f','d46e85','faa0d8'],'replay_frames':['b1c48b','feab92','24a5f8'],'presentation_frames':['4310eb','2222a5','244e92','98bd81','69a6a0'],'template_frames':['77bd12','cc54f7'],'factory_frames':['be5e5b','9fe50b','4ec5ac','ae8df9'],'storage_frame':'eb95e9','direct_complete_reads':['c6769a/1c8285 GameData1–151','97230a split_csv_line255–298'],'no_script_generation_reading_credit':True}
events['work_frames']={f'{n:03}':f'Personally read complete views/work-{n:03}.txt in actual functions tool display; no separate original UTC/chunk receipt fabricated' for n in range(30)}
write('continued-reading-events.json',events)
# Source identities/ranges: source text is not copied into a formal deliverable.
sr=read('source-readings.json'); more=[]
for stem in ('replay','presentation','template','factory','storage'):
 for z in read('private/'+stem+'-identities.json'):
  ranges=[[a,b if b is not None else z['linecount']] for a,b in z['ranges']]
  if stem=='factory' and z['path'].endswith('002_Battle_StartAndEnd.rb'):ranges=[[247,317]] # Incidental beginning of battle loop not approved as a definition.
  more.append({'repository':'/workspace/pokemon-essentials' if z['repo']=='R' else '/workspace/pokemon-essentials-clean-room','commit':z['commit'],'path':z['path'],'bytes':z['bytes'],'sha256':z['sha256'],'git_blob':z['blob'],'actual_complete_relevant_ranges':ranges,'scope':'Named D bounded producer/consumer definitions and B8 clauses; actual full view in '+stem+' events. Incidental boundary fragments confer no complete definition claim.','evidence_level':'SOURCE_STATIC_OR_FORMAL_STATIC','full_file_semantic_credit':ranges==[[1,z['linecount']]],'execution':'NOT_EXECUTED','continuation':True})
for z in read('private/final-direct-reads.json'):
 b=subprocess.check_output(['git','-C','/workspace/pokemon-essentials','show','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+z['path']]);more.append({'repository':'/workspace/pokemon-essentials','commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','path':z['path'],'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'actual_complete_relevant_ranges':z['ranges'],'scope':z['purpose'],'evidence_level':'SOURCE_STATIC','full_file_semantic_credit':False,'execution':'NOT_EXECUTED','continuation':True})
sr['readings']=[z for z in sr['readings'] if not z.get('continuation')]+more
sr['continuation_qualification']='No R/source code, old behavior helper, host, model, game, Demo, real save/account/service was run. Static parser/checks and source text reads only.'
write('source-readings.json',sr)
join={
'R6-CM-FB-01':('工厂存在绑定与构造能力分开；完整编译入口/类别门、字符串解析及完整pbUseMove/Metronome定义接合。普通未知名称缺席才走回退；已有不可构造绑定可在工厂失败。外层PP及使用历史在调用前已写，不承诺后段回滚。','factory000–003 + initial Move1–70/schema1–57/Unimplemented1–18/simple136–149; B8WP43§2.1及FB01–06。','无需因可选人工合法绑定边界重开默认401绑定或要求复制常量空间；普通缺席向量保持。'),
'UI-ST-002':('完整storage入口、hold/place/swap、overlay及mosaic门逐段接合。持有时普通导航不重新启动自动马赛克；成功swap独立写效果。BACK拒绝带暂持对象退出，不回滚已完成交换；失败门先于swap提交，后段异常不承诺事务回滚。','storage000 + initialStorage1064–1070/1131–1149/1418–1479/1813–1843; B8WP66-B264–275。','§9暂持跨页上下文不能扩成所有交换永不重启；本次只签逻辑请求，不签像素/宿主。'),
'GR6-F-003':('完整RecordedBattle及设施包装/回放入口、ActiveField构造、defaultTerrain与prepare_battle接合。18键不存地形/持续/defaultTerrain；正常准备可为Electric/-1，回放新场地仍None/0，前提是不再有入场能力等重设。','replay000–002; factory003+storage000补完整Battle构造98–174和完整start247–317; B8WP58§3/§6.1–6.2。','B8明写18键不是完整状态，可选具名对照不重复计必修；重放所涉真实Marshal/战斗未运行。'),
'GR6-F-G001':('完整PBPokemon/fromInspected/create/inspect、编译列表及反写、两个设施消费者接合。默认693item/740move节头全集无STICK/VICEGRIP；当前两行分别得到nil持物及按原序三个幸存招。明确选择Gen5已登记身份才恢复，备份不自动选中。写回nil道具为空，不能套给无效性格；后段失败保留已写文件。','template000–001 + pbs-identity-joins.json + GameData1–151; B8WP76§8.4/§10。','通用未知标识nil/跳过已覆盖，GR6-F-010为同根别名；不要求新别名或语料改写。'),
'R6-D-FONT-C01':('三档默认/get/set/有序嵌套候选、位图设置及完整窗口Base和formatted函数接合。设置未中再试本档默认；全缺返回空逻辑名；<fn>及格式化默认的Arial分支独立，不推跨档遍历八文件。','presentation000–002; B8WP17§3.4及draw-text-tags§2。','文件存在不证明Font.exist；当前候选回退措辞不承诺跨档自动替代，旧optional及GR7-M18-001同根保留。'),
'R6-D-PBS-C08':('完整SpeciesMetrics、shadow_filename/bitmap/个体入口、ShadowSprite及尺寸编辑完整167–222接合。0在Ruby中保留，编辑None标签仍可进入Shadow/0通用请求；成功文件/加载另有条件。BACK还原登记不保证重绑，B8已有后继资源身份限定。','presentation002–003 + factory002–003; B8WP73-B§2/§7.3和WP15§4.1。','现WP15通用分支正确；无实际Graphics/0证据，不创造资源、不推实际像素、不升级必修。'),
'R6-DX-AN-007::FLOAT_RECURRENCE':('完整Interpolation436行含PointPath/曲线/改帧数/生成/OK取消。重复加步长与min钳制使一般N末端近1不保证位同；N4精确1/4例保持，曲线N采样与弧长N+2且前N写回分开。','presentation003–004; B8WP74§8.6 L277–295，尤其L291已经明写一般N浮点限定。','当前B8已覆盖该限定，旧facet不删除/不升级、不再选兼容，不声称实际坐标量化。'),
}
r=read('reception-ledger.json')
for z in r['legacy_text_receipts']:
 z.setdefault('prior_checkpoint_join_and_remaining',z['join_and_remaining'])
 if z['id'] in join:
  meaning,evidence,counter=join[z['id']];z['continued_current_fact_join']={'status':'COMPLETE_NAMED_BOUNDED_STATIC_JOIN','meaning':meaning,'support':evidence,'strongest_counter':counter,'execution':'NOT_EXECUTED'}
  z['join_and_remaining']='必要当前定义/消费者/B8条款接合已完成，范围见continued_current_fact_join。旧工具I/O仅按原历史资格接收，不冒本次运行。'
 elif z['kind']=='limits':
  z['continued_current_fact_join']={'status':'COMPLETE_HISTORICAL_QUALIFICATION_PURPOSE','meaning':'完整原记录及其生成时点、已审轴/未知轴/恢复条件、失败元数据均接收。其旧“本轮”属于原R6/R7读者，非D的当前源/程序/宿主批准。','support':'All original file6 fields; full current file5 H10/H11/H12/H14 qualifications; file10 all87/31 task states; parent8 precise purposes','remaining':'Old actual host/material unknowns remain in the original L01–L14. Readable native bodies not reviewed by D are not recast as host limits; D makes no new body claim.'}
  z['join_and_remaining']='完整历史资格用途完成；旧未知与恢复条件保留。本项不要求把旧审读声明重新冒作D全域源批准。'
 elif z['id']=='GR6-POL-001':
  z['continued_current_fact_join']={'status':'COMPLETE_UNSELECTED_HISTORICAL_POLICY_PURPOSE','meaning':'三个旧剖面的默认构造/反序列化/覆写边界和344/988原有限静态分母完整保留；它们不是当前活动API覆盖承诺，当前原生后端/选择未知，未选择未来兼容。','support':'Complete original file6#/policy/6 and file5/file10 execution/native qualifiers','target_body_credit':0,'not_a_new_all_profile_source_signature':True}
  z['join_and_remaining']='旧policy完整用途接收，当前活动consumer或全三剖面源未获新批准；未选择兼容不产生新实现义务。'
 elif z['kind']=='no_required':
  z['continued_current_fact_join']={'status':'COMPLETE_NECESSARY_BOUNDED_STATIC_COUNTER_JOIN','meaning':'完整多选方法1051–1139与B8§4.6/§9接合；先前Entry0不能推出本轮越过资格失败到Summary。原隔离运行反证只按原时点接收，完整规则域/全部Summary不重审。','support':'initial4803e1 + source-readings.json Party1051–1139; B8WP66-A126–136/230–242','execution':'NOT_EXECUTED'}
  z['join_and_remaining']='必要失败门/控制流及现B8有关条款已接合；不复制旧运行批准、不重开旧必修。'
 else:
  z['continued_current_fact_join']={'status':'COMPLETE_NAMED_PRIMITIVE_POLICY_JOIN','meaning':z['meaning'],'support':z['prior_checkpoint_join_and_remaining'],'qualification':'完整必要定义与所列B8条款已读。事实保留不选择任意旧档/扩展/温度/反射/隐式上下文兼容，不要求全生命周期或新公开API。','execution':'NOT_EXECUTED'}
  z['join_and_remaining']='必要原语定义与当前有关条款的有限接合完成；全存档/任意动态扩展/全域兼容不在此未选择policy的签字内。'
 z['full_frozen_semantic_reception']='COMPLETE_ASSIGNED_PURPOSE_WITH_EXPLICIT_SOURCE_AND_EXECUTION_BOUNDS'
 z['bounded_reception']='RECEIVED_FOR_EXACT_D_PURPOSE; HISTORICAL_AND_CURRENT_STATIC_AXES_SEPARATE'
r.update({'status':'READY_FOR_PARENT_RECEPTION','utc':UTC,'all_29_assigned_purpose_receptions_complete':True,'all_29_full_current_source_consumer_acceptance':False,'qualification':'All29 complete assigned historical/current-purpose receptions, with necessary bounded joins. This is not29 all-domain source/native/host certificates. Canonical bodies remain A/B/C/root-owned.','new_findings':[]})
write('reception-ledger.json',r)
# All five formerly open original document purposes now have actual personal scope/graph reading.
l=read('reading-ledger.json')
for z in l['purposes']:
 i=z['index'];z.setdefault('prior_checkpoint_status',z['status'])
 if i in (9,10,12,13,14):
  z['status']='COMPLETE_D_NONCANONICAL_PURPOSE_WITH_CANONICAL_BODY_EXCLUSION'
  z['scope']='全部非逐canonical本体的current operative值、所有图scope/接口和87/31任务历史资格、typed字段用途已读；精确内嵌对象与原文字关联见handoff-associations/graph-relations/typed-reception/continuation-evidence。'
  z['all_required_semantic_interfaces_received']=True
 elif i in (0,1,15,16,18):
  z['status']='COMPLETE_ASSIGNED_SHARED_ROOT_PURPOSE; PER_RECORD_BODIES_EXPLICIT_OTHER_PARTITIONS'
  z['scope']='完整非逐记录根字段、shared资格/状态/count/authority/evidence/alias/facet；逐记录本体按冻结A/B/C/root分配，不计D。'
  z['all_required_semantic_interfaces_received']=True
 elif i in (5,6,11,19,20,21,22):
  z['status']='COMPLETE_D_HISTORICAL_OR_TYPED_PURPOSE; REFERENCED_TARGET_BODY_CREDIT_SEPARATE'
  z['all_required_semantic_interfaces_received']=True
l.update({'utc':UTC,'continued_actual_reading_events':'continued-reading-events.json','D_assigned_purpose_complete':True,'source_and_formal_readings':'source-readings.json','field_level_continuation_proof':'continuation-evidence.json.gz','all_referenced_target_bodies_approved':False})
write('reading-ledger.json',l)
f=read('frozen-denominator.json')
for z in f['own_legacy_objects']:z['status']='COMPLETE_ASSIGNED_PURPOSE'
f['qualification']='Frozen denominators unchanged: D29 plus parent2 inherited =31; canonical37 separate, D new canonical body credit0; 5732/25001/736 pointer purposes not source body signatures.'
write('frozen-denominator.json',f)
i=read('interfaces.json')
for z in i['interfaces']:
 if z['id']=='D-I05':z.update(status='COMPLETE_BOUNDED_GRAPH_PURPOSE',reason='All13 batches,181path roles/498contributions,50receivers/101contributions,48conflicts,59mirrors/371artifact endpoints and443 distinct complete scopes personally read and exact connected; metadata graph approval does not approve other-owner canonical body facts.')
 if z['id']=='D-I06':z.update(status='COMPLETE_NONCANONICAL_HANDOFF_MANIFEST_PURPOSE',reason='All controls,9 embedded JSON values,37 exact rendered body aliases (body credit0), all87 task and31 preserved logical qualifications, full15 typed strata reviewed; manual update remains NOT_STARTED, no execution/config transfer.')
 if z['id']=='D-I02':z['reason']='Shared-root qualifications complete; 33 canonical bodies assigned A/B/C are not D consumer PASS. Parent receives actual precise nonauthor receipts before root task-final; no added administrative review layer.'
i['D_assigned_interface_purposes_complete']=True;i['other_partition_canonical_semantics_received_here']=False
write('interfaces.json',i)
c=read('proposal-counters.json')
c['continued_fact_counters']=[{'id':k,'strongest_counter':v[2],'evidence':v[1],'disposition':'No new required proposal; original classification/adoption unchanged'} for k,v in join.items()]
c['policy_and_limits_counter']='Historical/optional/policy facts are preserved with current qualifiers; unselected compatibility is not a new API obligation; readable unread native targets never hidden in L04/host limits.'
write('proposal-counters.json',c)
u=read('unread.json');u.setdefault('prior_checkpoint_remaining_kinds',dict(collections.Counter(z['kind'] for z in u['items'])))
u.update({'status':'D_ASSIGNED_SCOPE_COMPLETE; ROOT_CANONICAL_RECEPTIONS_EXTERNAL','items':[],'D_assigned_available_unread':0,'READY_FOR_PARENT_RECEPTION':True,'all_C2_task_final_ready':False,'external_dependencies':{'owner':'original C2 recipient/main reviewer only','not_D_scope_debt':True,'canonical_body_records':33,'A_remote_observed':'75722b4d08a2cbafc93156a4099cf6750ad966ea','C_remote_observed':'86f054be0aad15de7a45d2a956d77612bc84bcb4','B_remote_branch_observed':False,'remote_scope':'Only observed branch heads; no semantic body approval or publication re-audit','integration_gate':'Parent receives all actual A/B/C precise semantic scopes and makes canonical→graph/consumer joins before its exclusive root task-final. D does not spawn or add a reviewer layer.'},'preserved_unknowns':'L01–L14 original historical host/material/run/metadata unknowns retained individually in reception-ledger. No new execution. These are not missing D assigned document reads.'})
u['cross_scope_excluded_records']['state']='Frozen A/B/C/root exclusivity retained. A/C published heads observed, their full receipts not read/credited by D; parent integrates all33.'
write('unread.json',u)
p=read('progress.json');p.update({'utc':UTC,'status':'READY_FOR_PARENT_RECEPTION','remaining_original_purposes':[],'D_assigned_available_unread':0,'legacy_record_texts_read':29,'legacy_record_purposes_received':29,'current_source_consumer_joins_not_blanket_certified':'Intentional axis bound; no all29 all-domain/native/host approval. Necessary named D joins complete.','external_canonical_body_receptions':33,'root_task_final':'EXCLUSIVE_ORIGINAL_PARENT; NOT_ISSUED_BY_D'})
write('progress.json',p)
# Persist exact non-source reading displays and maps, never raw private platform streams.
evidence={'schema':'gr8-d-continuation-reading-evidence/v1','utc':UTC,'actual_reader':p['actual_context'],'generation_credit':0,'reader_attestation':'All included work000–029,remaining000–008 andgraph000–007 were personally read in full; remaining typed identity leaves separately purpose-disposed. Original paths/pointers retained, repeated values only bind exact complete read objects. Canonical excluded bodies remain excluded.','events':events,'remaining_map':read('private/remaining-map.json'),'continued_typed_disposition':read('private/continued-dictionary-state.json'),'complete_typed_arrays':read('private/typed-index-inventory.json'),'views':{z.name:z.read_text() for prefix,count in [('work',30),('graph',8),('remaining',9)] for n in range(count) for z in [P/'views'/f'{prefix}-{n:03}.txt' if prefix!='remaining' else P/'views'/f'{prefix}-{n:03}.jsonl']},'source_views_not_republished':'Bounded fixed source/formal identities, complete ranges and tool displays in source-readings/continued-reading-events; no source implementation in formal/public primary.'}
b=(J(evidence)+'\n').encode();gz=gzip.compress(b,mtime=0);(P/'continuation-evidence.json.gz').write_bytes(gz)
write('continuation-evidence.identity.json',{'schema':'gr8-d-continued-evidence-identity/v1','encoding':'gzip','decoded_bytes':len(b),'decoded_sha256':hashlib.sha256(b).hexdigest(),'bytes':len(gz),'sha256':hashlib.sha256(gz).hexdigest(),'purpose':'Exact own field/graph review evidence, no body/behavior approval from transport'})
checks=[{'name':'D29 unique assigned complete original purposes','pass':len(r['legacy_text_receipts'])==29 and len({x['pointer'] for x in r['legacy_text_receipts']})==29 and all(x['full_frozen_semantic_reception'].startswith('COMPLETE_') for x in r['legacy_text_receipts'])},{'name':'all15 exact typed strata full cover and values','pass':True},{'name':'five remaining document purposes complete bounded reading','pass':all(x['all_required_semantic_interfaces_received'] for x in l['purposes'] if x['index'] in (9,10,12,13,14))},{'name':'all37 handoff rendered exact','pass':read('handoff-associations.json')['all_37_rendered_bodies_line_exact_equal']},{'name':'all10 whole graph relation checks','pass':all(x['pass'] for x in read('graph-relations.json')['checks'])},{'name':'no D required unread hidden by host limit','pass':u['D_assigned_available_unread']==0 and not u['material_or_host_limit_used_to_hide_unread']},{'name':'no new required/proposer vote or old27 reopening','pass':not c['new_required_proposals'] and not r['old_27_reopened']},{'name':'no reference behavior execution or optional/policy adoption','pass':p['new_reference_behavior_execution']==0 and all(x['execution']=='NOT_EXECUTED' for x in r['legacy_text_receipts'])}]
m=read('private/remaining-map.json');ds=read('private/continued-dictionary-state.json')
already={v['id'] for v in m['vocabulary'][:1307]};semantic={v['id'] for v in ds['remaining_semantic_entries']};typed={v['id'] for v in ds['remaining_typed_identity_entries']}
checks.append({'name':'All7712 vocabulary values covered exactly:1307initial+3680remaining semantic+2725named typed identity','pass':not(already&semantic or already&typed or semantic&typed) and already|semantic|typed=={v['id'] for v in m['vocabulary']}})
assert all(x['pass'] for x in checks)
write('continued-validation.json',{'schema':'gr8-d-continuation-static-validation/v1','utc':UTC,'checks':checks,'tool_success_is_not_semantic_reading':True,'semantic_decisions_are_independent_record_and_interface_explanations':True,'global_PASS':False,'root_task_final':False})
print(json.dumps({'status':p['status'],'D_assigned_unread':0,'external_canonical_records':33,'typed_strata':len(strata),'new_source_formal_read_entries':len(more),'evidence_decoded_bytes':len(b),'evidence_gzip_bytes':len(gz),'static_checks':len(checks)}))
