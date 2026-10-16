"""Synchronize task-local WIP counters/references. Counts do not grant semantic acceptance."""
from pathlib import Path
import collections
import datetime
import hashlib
import json

BASE=Path(__file__).resolve().parent
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(name): return json.loads((BASE/name).read_text())
def write(name,value): (BASE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
atoms=read('manual-atomic-clauses.json');stats=read('wp06-stats-directory-manual-field-atoms.json')['records'];sid={x['id'] for x in stats};atoms['records']=[x for x in atoms['records'] if x['id'] not in sid]+stats;write('manual-atomic-clauses.json',atoms)
CHILDREN=len(atoms['records'])
old=read('old-locator-disposition.json');consumer=read('consumer-candidate-dispositions.json');facts=read('sourcefact-consumer-receptions.json');ledger=read('reading-ledger.json')
full={x['path'] for x in ledger['records'] if x.get('repo')=='R' and x.get('status')=='FULL_READ' and not x['path'].startswith('PBS/')}
LOCAL=consumer['summary']['RECEIVED_LOCAL_STATIC_DOWNSTREAM_OPEN']; NAMED=consumer['summary']['RECEIVED_NAMED_BOUNDED_CONTRIBUTION_DOWNSTREAM_OPEN']; OPEN=consumer['summary']['OPEN_NOT_YET_SEMANTICALLY_RECEIVED']
PURPOSE=sum(v for k,v in consumer['summary'].items() if k not in ('RECEIVED_LOCAL_STATIC_DOWNSTREAM_OPEN','RECEIVED_NAMED_BOUNDED_CONTRIBUTION_DOWNSTREAM_OPEN','OPEN_NOT_YET_SEMANTICALLY_RECEIVED')); DISCOVERED=len(consumer.get('additional_discovered_lexical_candidates',[]))
OWN_R_FULL=len(full)
bound=sum(bool(x.get('explicit_manual_child_ids') or x.get('manual_child_assertions')) for x in old['records'])
assert len(old['records'])==2219 and len(facts['records'])==135 and len(consumer['records'])==714 and OWN_R_FULL>=77
assert len({x['id'] for x in atoms['records']})==CHILDREN
actual_receipts=[
 ('CREA-8','received/creature-a-kernel-consumer-reception.json',8),
 ('CREA-OBTAIN-2','received/crea-obtain-addendum-reception.json',2),
 ('CORE-6','received/core-kernel-reception.json',6),
 ('UI-COMPLETE-105','received/ui-complete-finite-reception.json',105),
 ('UI-DEX-CORRECTION-11','received/ui-correction-dex-reception.json',11),
 ('MEDIA-MESSAGES-17','received/media-messages-finite-reception.json',17),
 ('MEDIA-ENCODING-4','received/media-serialized-encoding-87f3db06-reception.json',4),
 ('ROOT-LOTTERY-3-GROUPS-11-ASSERTIONS','received/root-lottery-finite-reception.v1.json',11),
 ('CREA-LIFECYCLE-18','received/crea-lifecycle-ef79b21e-reception.json',18),
 ('CREA-SETTINGS-4','received/crea-lifecycle-settings-c777c711-reception.json',4),
 ('CORE-ATTACK-5','received/core-attack-settings-0a708ab7-reception.json',5),
 ('DEVELOPER-NAMES-2','received/developer-names-reception.json',2),
 ('FACILITY-STATS-6','received/facility-four-stats-reception.v1.json',6),
 ('CORE-EOR-CAPTURE-8','received/core-eor-capture-finite-reception.v1.json',8),
 ('CORE-FIELD-9','received/core-field-settings-finite-reception.v1.json',9),
 ('ROOT-ENCOUNTER-BOUNDED-1','received/root-encounter-finite-reception.v1.json',1),
 ('CORE-SFB-11-20','received/core-sourcefacts11-20-finite-reception.v1.json',10),
]
received=[]
for identity,path,count in actual_receipts:
 raw=(BASE/path).read_bytes();received.append({'id':identity,'complete_finite_reception':path,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'finite_units_or_facts':count,'credit':'Actual complete selected contribution read; exact scope/reader/premises in receipt. No whole-domain or extra sourceFULL granted.'})
ledger['received_complete_finite_contributions_current']=received
for path,ranges,unit,evidence in [
 ('Data/Scripts/012_Overworld/007_Overworld_DayCare.rb',[[172,213]],'inherit_IVs complete173–212','io/crea-unit-boundary-supplement-actual-source.json'),
 ('Data/Scripts/020_Debug/003_Debug menus/007_Debug_PokemonCommands.rb',[[1007,1048]],'set_egg complete handler1007–1048','io/crea-unit-boundary-supplement-actual-source.json'),
]:
 found=next((x for x in ledger['records'] if x.get('path')==path),None)
 entry={'path':path,'repo':'R','status':'PARTIAL_READ_COMPLETE_NAMED_UNITS','reader':'/root/kernel_atomic_reception','actual_read_ranges':ranges,'complete_units':[unit],'whole_file_read':False,'reading_evidence':evidence}
 if not found:ledger['records'].append(entry)
 elif found.get('status')!='FULL_READ':
  found['actual_read_ranges']=sorted(set(tuple(x) for x in found.get('actual_read_ranges',[]))|set(tuple(x) for x in ranges));found['complete_units']=sorted(set(found.get('complete_units',[])+[unit]));found.setdefault('later_read_evidence',[]).append(evidence)
ledger['own_reference_full_read_non_PBS']=OWN_R_FULL;ledger['updated_utc']=NOW;write('reading-ledger.json',ledger)
for name,path,count in actual_receipts:
 found=next((x for x in facts.get('named_contributions',[]) if x['id']==name),None)
 if found is None:
  found={'id':name};facts.setdefault('named_contributions',[]).append(found)
 found.update(reception_path=path,complete_finite_count=count,source_credit='Original actual named reader retained; no whole-domain approval',whole_domain_received=False)
for x in facts['records']:
 if x['fact_id']=='KER-F077':x['manual_atom_links']=sorted(set(x.get('manual_atom_links',[])+[r['id'] for r in stats if r['id'].endswith('-DECLARATION') or r['id'].endswith('-INITIAL')]))
facts['updated_utc']=NOW;write('sourcefact-consumer-receptions.json',facts)
progress=read('progress.json');progress.update(updated_utc=NOW,own_reference_full_read=OWN_R_FULL,own_reference_full_read_measure='Non-PBS actual own FULL source paths; original start77 complete. PBS counted separately.',own_reference_full_read_non_PBS=OWN_R_FULL,explicit_manual_atom_subset=CHILDREN,consumer_candidate_dispositions=consumer['summary'],old_locators_with_explicit_partial_child_binding=bound,additional_method_candidates_received_local=1,additional_method_candidates_received_named=7,additional_method_candidates_unreceived=0,checkpoint_review_written_utc=NOW,named_crea_lifecycle_facts_received=18,named_crea_lifecycle_settings_facts_received=4,named_core_attack_facts_received=5,named_media_encoding_facts_received=4,named_developer_complete_units_received=2,named_root_lottery_complete_assertions_received=11);write('progress.json',progress)
gaps=read('coverage-gaps.json');gaps['updated_utc']=NOW;gaps['current_unreceived_lexical_candidates']=[x for x in consumer['records'] if x['status']=='OPEN_NOT_YET_SEMANTICALLY_RECEIVED'];gaps['current_unreceived_lexical_candidate_count']=len(gaps['current_unreceived_lexical_candidates']);gaps['current_additional_method_candidates']=consumer['additional_method_config_candidates'];gaps['manual_subset_not_denominator']=CHILDREN;gaps['partial_old_locator_bindings_not_completed']=bound
pbs_full=sorted(x['path'] for x in ledger['records'] if x.get('repo')=='R' and x.get('status')=='FULL_READ' and x['path'].startswith('PBS/'))
pbs_all=set(gaps['PBS_full_read_paths'])|set(gaps['PBS_remaining_paths'])
assert len(pbs_all)==73 and len(pbs_full)>=32
PBS_FULL=len(pbs_full);PBS_REMAINING=len(pbs_all)-PBS_FULL
gaps['PBS_full_read_paths']=pbs_full;gaps['PBS_remaining_paths']=sorted(pbs_all-set(pbs_full))
for group in gaps['primary_formal']:
 path=group['path'];matching=[x for x in old['records'] if x['path']==path];group['manual_child_records']=sum(x.get('formal',{}).get('path')==path for x in atoms['records']);group['partial_child_bound_old_ids']=[x['old_locator_id'] for x in matching if x.get('explicit_manual_child_ids') or x.get('manual_child_assertions')];group['still_without_named_child_binding_old_ids']=[x['old_locator_id'] for x in matching if not (x.get('explicit_manual_child_ids') or x.get('manual_child_assertions')) and not x['disposition'].startswith(('LAYOUT_','TABLE_'))];group['semantic_exhaustiveness']='NOT_FROZEN; exact child status and per-locator remainder control'
gaps['historical_receipts']={'HTTP':'Original complete canonical/counterreview/5 actual criteria plus qualified record26 actually read. Original raw probe/probe-v1/probe-result-v2 not yet received.','Timer':'Original complete canonical/counterreview/6 actual criteria actually read. Original raw probe still unreceived.','fixed_object_recovery':'io/history-fixed-object-recovery.json records own isolated bare fetch timeout45s, zero semantic credit; no permanent unavailability inferred.'};write('coverage-gaps.json',gaps)
interfaces=read('interfaces.json');interfaces['updated_utc']=NOW
for x in interfaces['interfaces']:
 if x['id']=='KAR-I-CONFIG':x['accepted']=f'714 original census:{LOCAL} local reached candidates,{NAMED} complete named finite candidates,{PURPOSE} comment/declaration uses; extra8 method locations=1local+7named. Each exact ID retains actual reader and complete premise.';x['open']=f'{OPEN} exact original lexical candidates remain semantically unreceived, listed with path/line/symbol; dynamic/transitive discovery not frozen. No all-config approval.'
 if x['id']=='KAR-I-INTL-MEDIA':x['status']='PROVIDER_CONFIRMED_COMPLETE_FINITE_RECEPTION_IN_PARENT_MESSAGES';x['accepted']='Recipient confirmed exact12facts plus navigation correction,15producer/shared contracts plus Trainer identity addendum; original source FULL remains this provider. Confirmation message is not a separately read remote receipt.'
interfaces['current_complete_finite_receptions']=received
interfaces['new_source_units_and_semantic_edges']={'GamePlayer':'14fact frozen packet received by root; all7 named stats/3 Settings candidates now local-static. Root receipt navigation from message not itself re-read yet.','Time':'131 explicit hand-authored children join wallclock/uptime/phone/tone/timer/step/dungeon/AntiRandom/recorded RNG with their exact prefixes; Game_Map fog3 consumers separately actual received.','Diagnostics':'132 explicit hand-authored IO/DP children join helper-local catch sets, state machines, caller continuation and warning parameter channels.','ROOT-decisions':'GR8-KER001/002/003 complete exact canonical and original counter contracts actually read; bounded root decisions only. MapSave triage-only and emergency no-new-required records actually read. Hash candidate full root counterreceived NO_REQUIRED_BOUNDED_SCOPE; no new vote.'};write('interfaces.json',interfaces)
inp=read('input-identities.json');inp['updated_utc']=NOW;inp['late_complete_finite_reception_identities']=received;inp['source_full_read_count_does_not_imply_semantic_PASS']=True;write('input-identities.json',inp)
nextstep=read('next-dispatch.json');nextstep['updated_utc']=NOW;nextstep['current_work']=f'All13F/2219 old locator meanings or explicit layout purposes reconstructed; no remainder without a named meaning/purpose. Seventy previously generic sourcefact OPEN records now have individually authored finite source/purpose/consumer/boundary dispositions, with originals preserved;62 other local-subset facts, F101 rejection and F134/135 navigation rejection remain separately scoped. Refine final unique atomic denominator and complete{PBS_REMAINING} actual PBS and{OPEN} lexical candidates plus necessary successors. No split transferred responsibility.';nextstep['current_remaining_consumer_ids']=[x['id'] for x in gaps['current_unreceived_lexical_candidates']];write('next-dispatch.json',nextstep)
io=[]
for file in sorted((BASE/'io').glob('*.json')):
 try:obj=json.loads(file.read_text())
 except (json.JSONDecodeError,UnicodeError):continue
 if 'underlying_exit_code' in obj:io.append({'path':str(file.relative_to(BASE)),'started_utc':obj.get('started_utc'),'ended_utc':obj.get('ended_utc'),'underlying_exit_code':obj['underlying_exit_code'],'read_credit':'I/O enumeration only; actual full/partial reading governed by source/contribution ledger'})
execution=read('execution-ledger.json');execution['updated_utc']=NOW;execution['current_captured_read_IO']=io;execution['fixed_historical_object_fetch']='io/history-fixed-object-recovery.json';execution['complete_direct_command_timestamps']='NOT_ALL_CAPTURED: older direct metadata/edit commands retain platform evidence only; no backfilled UTC';execution['target_business_execution']='NOT_EXECUTED';execution['update_status']='UPDATE_NOT_STARTED';write('execution-ledger.json',execution)
report=f'''KERNEL第八轮独立审查仍在进行，尚无全域、章节或全部旧定位的语义通过结论。当前状态为 RUNNING_INCOMPLETE_NO_GLOBAL_PASS；UPDATE_NOT_STARTED；目标业务、游戏宿主及Demo均NOT_EXECUTED。实际记录时点：{NOW}。

固定B8为fd1df570cad987dc3852a3b958f03916e317f7fe，R为8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。请求gpt-6.1-sol/ultra/default普速/Fast off，实际字段均UNVERIFIED。工作仅写本任务目录及root另明授权的三个有限反证独占目录。原完整合同、全局提示、AGENTS、review-SKILL及135原事实全字段已实际读；2.9MB readset的全部元数据仍非本人逐字段视觉全文读，结构解析不冒充全文语义接收。

本人13个primary正式全文均已读；原77起点源及后续{OWN_R_FULL-77}个非PBS源共{OWN_R_FULL}路径实际全文（含同一实际上下文有限反证中真正完整的源，不增独立票）。另{PBS_FULL}个精确PBS路径全文，{PBS_REMAINING}个仍可得而待接，不列材料缺失。新必要partial单位分别记实际范围，完整贡献保原reader，不变成本人源FULL或独立第二票。

人工工作子记录现{CHILDREN}：初始44、WP02配置169、WP03 347、WP04 208、WP05 117、WP06统计296/时间131、WP07 132、WP08 214、WP09 232、WP10 240、首目录625（181case596子义＋29共享）、次目录812（206case782子义＋30共享），以及已手工残余1077（WP02 195/WP03 243/WP04 164/WP05+Stats+DP 141/Time102/IO133/Intl99）。它们含仍需细分的更新类别、scope/history与精确OPEN，未冻结最终原子分母。2219旧定位中{bound}仅有具名部分子义接合；其余496处有明确版式用途，全部2219现无未具名实义且非版式用途的定位。旧FULL_READ_CHILD_ASSERTIONS_NOT_EXHAUSTIVELY_DECOMPOSED等原状态保留为后续唯一分母精修提示，不能据其字面把本轮新增接合漏掉。版式用途不批准相邻复合意义。

714原词法候选现{LOCAL}local/{NAMED}具名有限接受/{OPEN}未接/{PURPOSE}注释或声明用途。额外8个方法配置位置已1local+7有限接收；仍不证明动态或传递消费者穷尽。完整具名包及实际前提见sourcefact-consumer-receptions.json、interfaces.json及received/；完整payload从CRE、CORE、UI、媒体、Developer和root有限事实取得，原reader/源身份/失败前缀与OPEN全部保留。CORE后继9fact/18对象全414L已实际收，Terrain缺end516用自身完整定义补齐；其30候选逐手工事实接合，原parent FULL不移转。

当前重点接合包括：17值保存机制和整对象边界；GamePlayer四向/跳跃/对角、step通知与早写统计；电话墙钟逐次减1与帧delta；tone缓存；变量墙钟销毁式查询；AntiRandom条件概率；录像索引缺项；文件catch集合/内存流状态/整数byte协议；HTTP构造与host/落盘的捕获边界；诊断0标记被Main忽略以及弃用警告每调用发出。旧70条generic OPEN现在逐fact手写59379B表及具体接收字段，包括F008旧范围勘误、F016读取出处用途、F023忽略尾项不必转换、F070窄begin也包日志/push、F072墙钟日历与uptime累计（Stats lastsave也在play_time域），70条原record全部保留。旧KER-F101的callsite录制部分不受支持，保明确拒收，不转成新formal缺陷；F134/135源事实局部确认而旧WP10导航拒接，WP75 owner完整有限接合待收。

既有GR8-KER001/002/003完整canonical与原counter契约已实际全文接收，只保各自狭窄范围。MapSave仍TRIAGE_ONLY，emergency仍NO_NEW_REQUIRED；不挂到KER003。新完整Hash提案1原件保留，root真实非提出者完整反证已实际全文接收并接受NO_REQUIRED_BOUNDED_SCOPE，新增required/optional均0；条件source事实保留。本人追加既有不同context的after-all-hits有限反证另目录交root，结论NO_REQUIRED_BOUNDED_SCOPE；Slot七角色8节反证43448B＋915Bextent澄清已交root并获消息指引有限requiredP3（root9536B完整8节回执已本人全文实收，有限history OPEN/0新票保留），均0新增context/票。Bag注册图像另50187B完整必要sourcehint只保9facts/18units与外部inventory对象17有限接收，不新finding或扩大Slot范围。EggGroup15严格成员域8节独立有限counter另目录16224B交root，另4318B mandatory补完整generic4–68，原65185B保留。root14620B七组完整裁决已本人实际全文接收，有限requiredP3 GR8-PBS-EGGGROUP-DOMAIN-001，只承接15作者身份域；等价已明确纳入表可撤回/合并，全历史去重OPEN，不改正确繁殖算法，0重复根/新增context/票；HTTP/Timer原完整第四审查合同、反证和实际criteria已读；rawprobe未读，固定对象获取超时45s的真实失败已保留0信用，不推出永久缺失，不升级当前执行证明。

两目录全部387case已逐行手工复合子义，467目录旧定位有具名语义或精确版式用途；全部13F/2219旧定位均已逐意义或明确用途处置，核剩余非版式且无具名子义为0。新增ribbons401/trainer_types401/trainers118实际全文三fixture172records/39members已冻302011B，该时点PBS累计32路径；跨完整物种/招式/物品与native编译成功未授。Items新增四源3420行与Move77已本人全文，Pokemon36个必要完整方法为partial源接收；15手工事实/4receiver事实/55候选在207554B有限完整包保存，固定Git与实际I/O核验。五遭遇fixture各311L已实际全文，95record/260method/1100slot完整原值与12手工事实、10Settings实际消费冻985522B有限包；WildEncounters469L是新增本人FULL，lead/Dex必要完整方法保partial。root7540B反证+46363B必要全文+8224B原提案已实际接收，当前WP36§3.1/WP62§5.3已明文覆盖版本枚举差异，有限NO_REQUIRED，不把GR7-M04-001误作遭遇alias（root已核为紧急保存optional，54870B canonical完整视图与26632B operative原root /records/3已全文实际收、含原提案及R7-C04完整裁决并与四旧formal必要上下文核验；只保紧急保存optionalP3而非Encounter alias，全历史仍OPEN）。另四Reflection/Modifiers/Spriteset完整349L＋8手工facts/12候选已冻41287B；AI item220全源＋必要登记/消费/worthwhile完整receiver已冻30898B/5手工facts/17候选，区分配置class-load估值、实际选择、choices早写和道具消费前缀，source错拼/错表未裁新finding。Safari196/Rules323/Generator211再新增本人FULL3，11旧候选9真实设置读取与2注释用途逐意义接合，完整42527B包；SafariStart46实际配置复制漏于旧714另列新增已接词法候选{DISCOVERED}，不把原census说成穷尽。另应root明指完成参与者更新点独立8节counter13839B，当前42638B/13R+4F完整实收并核固定Git、自补9完整必要单位，root16581B完整有限终裁已实际接收NO_REQUIRED_BOUNDED_SCOPE；不增context/票。GameScreen134/Picture166再本人FULL2，7完整时钟意义/明确条件及保存outer图谱29791B已冻，play_time getter副作用与rotation uptime分域、zero-tone旧timer保原事实不新finding。五代abilities五物理4505L/1122整record/2256显式字段完整读完并冻1476662B，五手工意义保schema/flags/default/原名与描述、消息producer和hatch flag有限receiver，文字描述不授全部战斗效果。其后Roaming228/Phone706完整新FULL2及8事实/9候选62044B，Interpreter必要完整方法/6事实/8候选36800B，额外distance_moved getter另列discovered。MapTransition138/Contest441新FULL2及微更新/dispatch/超时三门完整有限47166B，3旧候选；超时仍保native uptime/inner compatibility。Shadow三PBS42/213/525和RegionalDex212全字段全文已冻395905B，4Items/18Moves/131Shadow全471原字段、两Dex151+256有序身份绑定；条件类型/default和make/update/replace完整方法保原前提，备份非自动启用，PBS现{PBS_FULL}路径、余{PBS_REMAINING}。CORE F011–020完整93306B及3强制伴件、22内嵌正文/27固定身份已真正接收，有限10facts不机械清其余候选。下一步为全部工作子记录唯一分母人工归并细分、135原事实完整适用支持、{PBS_REMAINING}PBS和{OPEN}候选及实际必要动态后继。可得未读/未审是待完成工作。四个分片仍PROPOSED_NOT_APPLIED_0START，未真实移交，全部13F/2219责任仍在本人。本checkpoint齐全不代表任务完成。
'''
(BASE/'review.md').write_text(report)
print(json.dumps({'utc':NOW,'working_children':CHILDREN,'partial_old_bindings':bound,'candidate_summary':consumer['summary'],'extra_methods_unreceived':0,'own_nonPBS_FULL':OWN_R_FULL,'report_bytes':len(report.encode()),'captured_IO_records':len(io)}))
