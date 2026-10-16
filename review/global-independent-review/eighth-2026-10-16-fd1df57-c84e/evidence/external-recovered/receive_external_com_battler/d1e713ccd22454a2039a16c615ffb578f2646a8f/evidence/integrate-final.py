"""Integrate already-read qualified contributions; integrity checks are not review votes."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

T = Path(__file__).resolve().parents[1]
REPO = T.parents[4]
REL = T.relative_to(REPO).as_posix()
BASE = '7cfb409ab4c0e5978ff5c4079a00c01ccb7f3a0b'
STATUS = 'READY_FOR_ROOT_TASK_FINAL_ACCEPTANCE'
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args): return subprocess.check_output(['git','-C',str(REPO),*args])
def read(p): return json.loads((T/p).read_text())
def write(p, x): (T/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def sha(b): return hashlib.sha256(b).hexdigest()
assert git('rev-parse','HEAD').decode().strip() == BASE
assert git('branch','--show-current').decode().strip() == 'codex/r8-receive-com-battler-20261016'
forward=read('inputs/target-5cf9503a/forward-mapping.json')
reverse=read('inputs/target-5cf9503a/reverse-mapping.json')
compounds={c['id']:c for c in forward['compounds']}
rev={s['id']:s for g in reverse['clause_groups'] for s in g['subassertions']}
g1=read('evidence/recovered-groups/g1/reception.json')
g2=read('evidence/recovered-groups/g2/reception.json')
groups={
 'group1_recovery':dict(commit='fa83704fec0389a4f9f50595e94eeb235b92cb3a', actual_context='01a144f1-2a91-709b-972d-b7945c0b001b', original_context='01a14489-4f84-70f3-be6b-d423160cc02b', src='recovery_battler_g1',dst='g1'),
 'group2_recovery':dict(commit='d55395055e862f3a2cb3b30d25469c1864fdef45', actual_context='01a144ee-00e5-739f-a972-9be4a7bc2006', original_context='01a14489-30d3-71b8-b1fa-99d8f482b029', src='recovery_battler_g2',dst='g2')}
for name,g in groups.items():
    prefix=REL.rsplit('/',1)[0]+'/'+g['src']
    rows=git('ls-tree','-r',g['commit'],'--',prefix).decode().splitlines()
    receipts=[]
    for row in rows:
        info,path=row.split('\t');mode,typ,blob=info.split()
        raw=git('show',g['commit']+':'+path)
        dest='evidence/recovered-groups/'+g['dst']+'/'+path.removeprefix(prefix+'/')
        assert (T/dest).read_bytes()==raw
        receipts.append(dict(original_path=path,local_path=dest,mode=mode,blob=blob,bytes=len(raw),sha256=sha(raw)))
    assert len(receipts)==6
    g.update(workspace_tree=git('rev-parse',g['commit']+'^{tree}').decode().strip(),source_task_tree=git('rev-parse',g['commit']+':'+prefix).decode().strip(),files=receipts,
        identity_binding='actual recovery context supplied by parent dispatch; own child opaque UUID/config remains UNVERIFIED',
        old_summary_reading_credit=0,new_votes=0,dedup='Same logical group; exact child/facet ID wins once. Later original outputs cannot add a vote or denominator.')

primary={}
for i,c in enumerate(g1['primary']):
    original=compounds[c['id']]
    assert [x['id'] for x in original['children']]==c['child_ids']
    assert original['unit']==c['unit'] and original['source']['evidence_id']==c['source_ref']['evidence_id']
    assert original['source']['ranges']==c['source_ref']['ranges']
    assert c['comparison'] in g1['manual_comparisons']
    primary[c['id']]=dict(group='group1_recovery',comparison_pointer='/primary/'+str(i),reason_pointer='/manual_comparisons/'+c['comparison'])
for i,c in enumerate(g2['forward']):
    original=compounds[c['id']]
    assert [(x['id'],x['assertion']) for x in original['children']]==[(x['id'],x['assertion']) for x in c['children']]
    assert original['source']==c['source']
    assert c['id'] not in primary
    primary[c['id']]=dict(group='group2_recovery',comparison_pointer='/forward/'+str(i))
assert len(primary)==262
reverse_new={}
for i,x in enumerate(g1['reverse_local_facets']):
    assert x['id']in rev
    assert x['support_children']==[child for f in rev[x['id']]['primary_facets'] for child in f['child_ids']]
    reverse_new[x['id']]=dict(group='group1_recovery',comparison_pointer='/reverse_local_facets/'+str(i))
for i,x in enumerate(g2['reverse']):
    assert x['assertion']==rev[x['id']]['assertion']
    assert x['id'] not in reverse_new
    reverse_new[x['id']]=dict(group='group2_recovery',comparison_pointer='/reverse/'+str(i))
assert len(reverse_new)==124

# These reasons are the receiver's actual comparison of the complete business
# assertions and the necessary interfaces, not results computed from coverage.
joins=[
 ('FC20-HP.03',['HEAL'], 'heal_HP/status/PP各自拒蛋；完整heal按HP→status→PP后清进化准备。HP与PP单项不自动等同完整治疗。战斗recover的canHeal/同步另由C0162/C0166及R03给出。'),
 ('FC20-ITEM.03',['END','CATCH','WORLD_END'], '正常终局先记录/接收捕获，再显示终战、取消未用选择/离场能力；仅pbParty(0)当前索引逐项Peer终战及I还原。满队送存先Peer/毒计数/Mega清理再删除，平移I及记录；加入捕获者写末槽I。伙伴世界后置治疗及自身持物错配边界不改写成全原队快照。CATCH仅存储完整入口与捕获成功分支，不授全捕获算法信用。'),
 ('FC43-ACCURACY.03',['ACCURACY','ABILITY_CALLBACKS','ITEM_CALLBACKS'], '默认命中前门Telekinesis/世代Minimize/base0；用户/盟友/目标能力与双方物品分别有效门，只有目标能力受mode门。重力×5/3，Micle在修正阶段清标并×1.2；后续base0返回仍已消费标记。七阶级夹限、倍率各round、evasion至少1、随机严格小于threshold；affection另减10。NoGuard与全部此处必要注册体已读，不概括双方任一必经同门。'),
 ('FC48-SPEEDWEIGHT.03',['ABILITY_CALLBACKS'], 'QuickFeet视为任一异常×1.5；Unburden须标记且当前无物×2，普通能力有效性来自调用者。R01完整优先序贡献绑定计算/档/随机缓存；增量重算不重抽既有同速随机数，回合末另重新pbCalculatePriority。'),
 ('FC42-CONSUMERS.01',['EOR'], 'EOR入口重算后只取得一次priority(true)速度序；Weather/治愈/残余/期限/形态/持续检查复用该数组，逐点重读对象与有效性；替补/具体回调可改变对象，但并不把每个残余子步骤改为全重排。'),
 ('FC22-MEGA.01',['OTHER','COMMAND','ACTION'], '禁止开关、Battler.hasMega含Transform、野生先拒；debug才早于SkyDrop/环/额度。业主环与side/owner额度-1不同于裸个体资格；菜单提供toggle，取消unregister。执行仅绑定UseMove和登记，pbMegaEvolve再查对象/个体/资格与已Mega；写形态/刷新/展示/额度-2后才旧失去、新获得及可选增量排序。'),
 ('FC67-DISPLAY.03',['SCENE','DATABOX'], 'sendOut优先Illusion，野生初始化仍真实bitmap；普通shiny经Illusion，而super_shiny来自自身，双设置门决定公共闪光。DataBox直接显示字段不重算统计；仅静态调用/等待与字节接收，像素、音频、运行时资源和真实时长未执行。'),
 ('FC45-INDIRECT.02',['EOR'], '正weatherDuration先减，0则结束并可启默认天气，只有仍有天气才持续/天气回调及伤害。Grass恢复在后段期限减计前，故terrain1仍恢复再结束。天气残余有fainted/专用伤害门；通用MagicGuard与液体污泥、ShadowHyper实际路径分开。'),
 ('FC47-CONTROL.01',['CONTROL','DRAIN','BEAK','NO_RETREAT','ACTION'], 'Bind/MeanLook/Octolock/JawLock/FairyLock建立守卫与计数来源不同；NoRetreat/Ingrain另有本体前门。AfterYou/Quash查已动与选择，Round首合格盟友MoveNext，Instruct黑名单/多轮/准备动作/最后同ID真实槽/PP0且总正门后仅置Instruct。ShellTrap/BeakBlast先充能标志，Grudge/同命建立和动作清理各自入口；主使用消费者由组3完整实读接合。钢光束ceil、MindBlown round且Damp、爆炸等自损点不统一成recoil或所有失败均同一提交。'),
 ('FC41-TRAP.02',['SWITCH','RUN','ABILITY_CALLBACKS','ITEM_CALLBACKS','COMMAND'], '换入蛋/所有权/倒下/在场及重复选择门，换出倒下早真、certain switching/鬼型先于原trapped。ArenaTrap接地、MagnetPull钢、ShadowTag对手非有效同能力；ShedShell只换出，RunAway/SmokeBall逃跑。实际pbRun训练家/forfeit、canRun、duringBattle与pbCanRun区别保留；速率用raw speed，不套pbSpeed。菜单取消-1与组合注册分开。'),
 ('FC42-GROWTH.01',['EXP','SWITCH'], 'pbUpdateParticipants记录队伍索引由入场参与记录刷新；GainExp先internal/expGain、对侧、participants非空、倒下或captured；计数仅能战且业主、分配遍历玩家队伍，ExpShare可看当前/I，ExpAll不越空participants前门。EV/Exp物品默认差异沿H01已更正。'),
 ('FC42-GROWTH.02',['EXP'], '最大Exp只calc_stats早返，不必场上刷新；初算<=0/最终<=0早返。正常逐段先写exp再条，level/统计/场上pbUpdate(false)/窗口/逐级学招顺序；Shadow单独存储门。满槽取消无新槽但不回滚先前经验；替换新Move及战斗副本，追加/替换后形态检查，Transform五值/类型/能力副本仍保持。'),
 ('FC46-DRAIN.01',['DRAIN'], '三完整族均先实际damageState.hpLost>0；半量用/2.0 round，DreamEater另睡眠资格，3/4用×0.75 round，再传真实target至中央drain。中央LiquidOoze允许倒下、直接反损及HP物品；普通canHeal/BigRoot和无统一尾濒死由C0163保持。'),
 ('FC42-CONSUMERS.03',['EOR','SWITCH','EXP'], 'EOR完整781行及完整pbEORSwitch/成长必要体实读；个人/侧/场/terrain/self/末回调、GainExp、形态、替补、位置、持续检查与明列尾清理次序成立。主方法在Perish后、GainExp后、EORSwitch后三个显式退出跳过后续，不虚构finally清mode。替补前pbJudge与双方选择/野生逃跑入口分别有门。只签这些必要阶段，不接全能力/物品注册库。'),
 ('FC21-FORM.01',[], '六个完整CREA有限记录中C21-R015夜/倒下/冻结→0否则nil，不是白天强制1；R020持久hasMoveSecretSword→1否则0。战斗状态/招式改变分支仍由C0172/C0173独立判断；原记录actual_reader与其余caller未接资格保留。'),
 ('FC21-FORM.02',[], '只接C0174/C0175实际涉及的Castform/Cherrim有效能力、Eiscue原身份标记、Darmanitan/Minior/Wishiwashi/Zygarde原身份及Morpeko有效身份/时点。全物种表仍由CREA_C主责；此反向子项的Battler facet已完整接收，不将外域整表改记本任务FULL。'),
 ('FC21-COMMIT.02',[], '六完整CREA对象均保留form写/能力缓存清在hook前，取消或异常只保已达前缀。Rotom可同ID删空、Kyurem遍历内compact跳项、Necrozma旧/新>2早返及删除后学CONFUSION、Calyrex基础表过滤及后学；拒绝/取消不回滚form或此前删除。g2已补读WP21 210–234，不把185–209截断当完整。'),
 ('FC22-MEGA.02',['WORLD_END','FACILITY_END','CONTEST_END','CATCH','END'], '普通换出无统一unmega，首次濒死才按持久Mega/Primal解除。世界after_battle全玩家party逐项解除，伙伴另治疗+解除；设施完整入口前治疗、存items，后双方治疗/解除/还原items且自身独立decision；竞赛startover治疗解除。捕获成功分支与送存前清理各自入口，不能以Battle普通终局替代所有世界/设施边界。'),
 ('FC67-DISPLAY.01',['SCENE','DATABOX','ANIMATION_BASE','SPLASH_ANIMATION','EXP'], 'HP写入前后关系接C0161/162；HP条旧新相同不启动，otherwise1秒插值等待不受showAnims关闭。EXP段先写，条仅存在battler/非零范围且可展示才启动；1.75秒乘比例、满条0.2秒闪后清临时字段。能力条设置门/同侧替换/8帧appear/disappear及dispose，收回/倒下独立循环等待。DataBox动画读值不反写HP/EXP。原生像素声音真实时钟/资源未执行，全UI域不转入本任务。'),
 ('FC42-CONSUMERS.02',['EOR'], 'Octolock仅存活且sourceindex>=0触发，分别无来源查询/降防与特防，再降阶物；未传模式重置。ECB001完整非作者反证支持true时-1/-1、false时Contrary+1/+1控制，不新增候选/投票。'),
 ('FC47-TRANSFER.02',['TRANSFER','GIFT'], '偷食守卫双方存活、unaffected/substitute、树果/不可失去、StickyHold/mode；先Belch/移除目标，再外来强制触发及使用者共生。Fling先缓存willFail，具体目标替身/ShieldDust及强制/特殊异常不同，尾仅当前仍有物时消费且禁Belch参数；NaturalGift不受Unnerve、需有效树果/flag，尾同样重读当前物。已达移除/消息不因后异常回滚。'),
 ('FC50-BERRY.03',['ITEM_CALLBACKS'], 'MentalHerb六效任一成立才真，分别清Attract/Taunt/Encore及EncoreMove/Torment/Disable/HealBlock，不清DisableMove。Leppa扫描持久招的空/部分PP，普通须空，forced才可首部分；Ripen20、夹持久PP后同槽战斗PP直接同步，不套SetPP三门。WhiteHerb负阶直接归0并升轮标，非普通升阶/Contrary链。helper真才消费后置。'),
 ('FC40-TURN.01',['OTHER','SWITCH','RUN','ITEM_ACTION','COMMAND','ACTION'], 'Call注册与可行动命令门、换人组合资格/注册、物品菜单CanUse和注册先扣包/取消返包、Mega菜单/业主额度及动作执行体均接合；动作先Call→Switch→决定退出→Items→决定退出→Mega→Moves。各生效入口与pbProcessTurn普通/special/skip分层，不能从任意四元数组推合法可达。')
]
assert len(joins)==23 and len({x[0]for x in joins})==23
sources=read('evidence/final-finite-sources.json')
source_ids={x['id']for x in sources['records']}
for _,ids,_ in joins: assert set(ids)<=source_ids
join_records=[dict(id=ident, status='FINITE_BATTLER_SOURCE_FACING_JOIN_RECEIVED',
    original_assertion=rev[ident]['assertion'], original_complete_object_pointer='/clause_groups/'+str(next(i for i,g in enumerate(reverse['clause_groups'])if any(x['id']==ident for x in g['subassertions'])))+'/subassertions/'+str(next(i for g in reverse['clause_groups']for i,x in enumerate(g['subassertions'])if x['id']==ident)),
    source_bundle='evidence/final-finite-sources.json', necessary_source_ids=ids,
    complete_foreign_definition_receipts='splits/R01,R02,R03,H01/result/reception-ledger.json and evidence/crea-six-form-records.json as applicable; original reader/scope preserved',
    receiver_comparison=why, full_foreign_domain_accepted=False, business='NOT_EXECUTED', root_task_final_acceptance=False)
    for ident,ids,why in joins]
write('evidence/final-finite-interface-joins.json',dict(schema='r8-battler-finite-cross-domain-joins/v1',utc=NOW,records=join_records,count=23,
 scope='Exact 23 necessary source-facing foreign facets; not all foreign source, formal group ownership, history universe or native execution.',UPDATE_NOT_STARTED=True))

ledger=read('reception-ledger.json')
already={x['id'] for x in ledger['source_child_statuses'] if x['status']!='OPEN'}
incoming={ch['id']for c in compounds.values()if c['id']in primary for ch in c['children']}
assert len(already)==183 and len(incoming)==627 and not already&incoming
for x in ledger['source_child_statuses']:
    cid=x['id'].rsplit('.',1)[0]
    if cid in primary:x.update(status='RECEIVED_QUALIFIED_CONTRIBUTION',recovery_contribution=primary[cid],source_body_read_credit='Actual recovery group; parent received complete assertions/comparison, no repeated SOURCE_FULL')
assert len(ledger['source_child_statuses'])==810 and all(x['status']!='OPEN'for x in ledger['source_child_statuses'])
join_index={x['id']:i for i,x in enumerate(join_records)}
for x in ledger['reverse_child_statuses']:
    if x['id']in reverse_new:x['recovery_contribution']=reverse_new[x['id']]
    x.update(status='RECEIVED_COMPLETE_ASSIGNED_PRIMARY_FACET_AND_NECESSARY_FINITE_JOINS',root_task_final_acceptance=False)
    if x['id']in join_index:x['finite_interface_join_pointer']='/records/'+str(join_index[x['id']]); x['finite_interface_join_file']='evidence/final-finite-interface-joins.json'
for x in ledger['facts']:x['final_consumer_join']='ALL_ASSIGNED_PRODUCERS_AND_QUALIFIED_FINITE_DEFINITION_JOINED';x['root_task_final_acceptance']=False
ledger.update(status=STATUS,complete_producer_children_received=810,complete_selected_formal_children_received=160,assigned_reverse_primary_facets_received=160,
 complete_compounds_received=289,necessary_foreign_facets_received=23,complete_central_finite_interfaces_received=4,final_finite_consumer_joins_received=24,
 remaining_source_child_ids=[],remaining_reverse_primary_child_ids=[],available_not_received='No remaining necessary source-facing task population. Native execution and whole foreign domains remain separately qualified.',
 reverse_count_qualification='160 complete assigned source-facing contributions plus all23 necessary finite joins; no whole-foreign-domain or root-final PASS.',
 recovery_object_pointer_correction='g1 original object_pointer uses /primary_compounds/N, while exact target key is /compounds/N. Original bytes preserved; cumulative links use original_pointer and exact IDs. Pure navigation correction, no new finding.',
 dedup='382 g1 recovery +245 g2 recovery +183 group3=810; 61+63+36=160. Original g1/g2 summary credit0; recovery never an extra vote.')
ledger['received_groups'].update(groups)
write('reception-ledger.json',ledger)

interfaces=read('interfaces.json')
for x in interfaces['cumulative_finite_fact_joins']:
    x['received_producer_compound_ids']=x['all_producer_compound_ids'][:]
    x['missing_producer_compound_ids']=[]
    x['status']='ALL_ASSIGNED_PRODUCERS_AND_FINITE_DEFINITION_JOINED'
    x['root_task_final_acceptance']=False
for x in interfaces['four_full_original_interfaces']:
    assert set(x['local_compound_ids'])<=set(compounds)
    x['prior_reception_snapshot']=x['reception'];x['reception']='COMPLETE_ASSIGNED_FINITE_INTERFACE_RECEIVED_ROOT_FINAL_PENDING'
    x['received_compound_ids']=x['local_compound_ids'][:]
    x['received_source_child_ids']=[ch['id']for cid in x['local_compound_ids']for ch in compounds[cid]['children']]
    x['finite_join_file']='evidence/final-finite-interface-joins.json'
    x['root_task_final_acceptance']=False
for x in interfaces['additional_history_join']:
    x['reception']='BOUNDED_EXISTING_DISPOSITIONS_AND_COMPLETE_COUNTERS_RECEIVED'
    x['qualification']='ECB001/002 existing bounded NO_REQUIRED and COM001 existing corroboration only. Global accepted-history absence/equivalence/canonical decisions remain root responsibility; no missing all-history read reclassified as PASS.'
interfaces['presentation_IF04'].update(status='FINITE_HP_EXP_COMMIT_TO_DISPLAY_INTERFACE_RECEIVED',static_join='FC67-DISPLAY.01/.02/.03; EXP and DataBox full necessary definitions in final-finite-sources.json; all native/media/time observations NOT_EXECUTED',root_task_final_acceptance=False)
interfaces['cross_group_pending']=dict(source_primary_ids=[],reverse_primary_ids=[],foreign_facet_ids=[],RX_CORE_ENTRY='Resolved by actual group4 R01 E039316–423; former missing group3 manifest row retained as history',qualification='All necessary finite edges joined. Whole foreign domains/native/history universe are not this task denominator.')
interfaces.update(status='FOUR_ASSIGNED_FINITE_INTERFACES_AND_24_FACT_JOINS_COMPLETE_ROOT_FINAL_PENDING',final_finite_interface_joins='evidence/final-finite-interface-joins.json',finite_interface_count=4,finite_fact_join_count=24)
for e in interfaces['cumulative_group3_edges']:
    e['status']='HISTORICAL_GROUP3_EDGE_NOW_INCLUDED_IN_FINAL_ALL_GROUP_JOIN'
    e['scope']='Original group3 contribution kept; final authoritative joins are cumulative_finite_fact_joins and four_full_original_interfaces.'
write('interfaces.json',interfaces)

reading=read('reading-ledger.json')
reading['final_recovery_reception']=dict(utc=NOW,groups=groups,complete_assertions_received=627,complete_reverse_primary_facets_received=124,
 parent_literal_read='All627 original assertion values; g1 all41 family reasons with per-compound mapping; g2 all102 hand comparisons; all61+63 reverse business assertions and qualification reasons; all74 unique original formal relations via complete14 reason dictionary and complete relation table.',
 truncation_repairs=['g1 C0033–0056 repaired separately (C0056 alias separately); g1 C0095–0160 full','original74 formal relations initial output truncated; all74 re-presented with full14 reason dictionary and exact per-relation fields','prior broad interfaces preview truncation receives no new semantic credit; already read original business reused, ID arrays navigation only'],
 source_full_credit='Actual g1 recovery1102 lines, g2 recovery1766 lines, g3 original1778 lines; total10 parents4646 lines. Parent receipt does not impersonate their source reading.',
 necessary_new_source_literal_read='All units in evidence/final-finite-sources.json were literally presented in this context; EOR complete781, Exp complete271, DataBox1–413 and Splash418–506, bounded complete specific callers/callbacks. CATCH captured branch is intentionally bounded, not full throw algorithm.',
 six_crea_records='All child meanings, premises, failure/cancel prefixes, actual receiver and remaining qualifications literally received; actual source reader preserved.',
 old_original_summary_credit=0,new_votes=0,recovered_helpers_executed=0,model_or_game_execution=0)
reading['counts'].update(complete_primary_child_reception=810,complete_reverse_child_reception=160,complete_central_interface_reception=4,complete_finite_fact_joins=24)
reading['capacity_remaining']='No further split required for this task. Parent root task-final acceptance remains pending; no new dispatch.'
write('reading-ledger.json',reading)
progress=read('progress.json')
progress.update(utc=NOW,status=STATUS,remaining=dict(necessary_source_children=0,necessary_reverse_children=0,necessary_finite_interfaces=0,root_task_final_acceptance='PENDING_PARENT',native_execution='NOT_EXECUTED',whole_foreign_domains='ORIGINAL_OWNER_SCOPE_RETAINED'),
 next='Parent lead reviews this concrete cumulative delivery and performs root task-final acceptance. No remediation/merge/main change.',
 capacity_handoff='All four actual groups received; recovery replaces stalled same-group credit by exact IDs. Frozen split-dispatch generation statuses remain historical.',
 final_counts=dict(primary_files=10,source_lines=4646,compounds=289,source_children=810,reverse_children=160,finite_foreign_facets=23,finite_definitions=24,finite_fact_joins=24,central_finite_interfaces=4,bounded_history_interfaces=1,presentation_finite_interface=1))
progress['completed'].update(progress['final_counts'])
progress['failure_and_correction_log'].append(dict(stage='additional finite source freeze',failure='Two preliminary helper invocations rejected overestimated endpoint numbers before writing output (Healing695, Items470; other endpoints preflight corrected).',correction='Read exact boundaries and fixed ranges; final freeze completed against pinned Git. No rejected output credited as review or execution.'))
progress['actual_recovery_deliveries']=groups
write('progress.json',progress)
publication=read('publication.json')
publication.update(schema='r8-com-battler-qualified-ready-publication/v1',task_status=STATUS,current_cumulative_reception='ALL_FOUR_GROUPS_AND_NECESSARY_FINITE_INTERFACES_RECEIVED',
 completed_scope='289 compounds /810 source children /160 reverse assigned primary facets;23 finite foreign joins;24 definitions/fact joins;4 finite central interfaces;IF04 and bounded history qualifications.',
 remaining_scope='Parent root task-final acceptance; no remaining necessary finite source-facing task gaps. Native business NOT_EXECUTED; whole foreign domains/history universe retained with their owners.',
 final_binding='This file cannot contain its own successor hash. Exact ordinary pushed tip/workspace tree/task tree/full blob readback are supplied in external final receipt and final response.',
 final_recovery_groups=groups,final_utc=NOW)
write('publication.json',publication)
validation=read('validation.json')
validation.update(result='PASS_TOOL_INTEGRITY_ONLY_SEMANTIC_RECEPTION_RECORDED_SEPARATELY',final_validation=dict(utc=NOW,source_partition=[382,245,183],reverse_partition=[61,63,36],overlap=0,complete_compounds=289,source_children=810,reverse_children=160,finite_joins=23,finite_fact_joins=24,finite_interfaces=4,unchanged_recovery_files=12,unchanged_prior_group_files=81,semantic_credit_from_tools=0,game_executions=0))
write('validation.json',validation)
write('evidence/final-reception-validation.json',dict(schema='r8-battler-final-reception-integrity/v1',utc=NOW,groups=groups,
 frozen_catalog_unchanged=sha((T/'frozen-denominator.json').read_bytes())==sha(git('show',BASE+':'+REL+'/frozen-denominator.json')),
 source_ids=len({x['id']for x in ledger['source_child_statuses']}),reverse_ids=len({x['id']for x in ledger['reverse_child_statuses']}),
 full_original_objects='unchanged10 inputs; active cumulative ledgers use exact original pointers',
 recovery_scripts='Preserved as inert original bytes; not executed', root_final=False,semantic_credit=0,UPDATE_NOT_STARTED=True))
print('INTEGRATED: 289 compounds /810 source children /160 reverse facets /23 finite joins /24 facts /4 finite interfaces; root final pending')
