"""Seal explicit bounded D judgments and exact outstanding scopes; no blanket PASS."""
from pathlib import Path
import datetime
import gzip
import hashlib
import json
import os
import subprocess

P=Path(__file__).resolve().parent
REPO=next(x for x in P.parents if (x/'.git').is_dir())
TASK=P.parents[1]
CONTRACT='64cfde5aa3f6b25adc7291b2c2e880d87baf1ebd'
BASE='1b46a33526f086241c765b700155c5406a86f65e'
TARGET='967b90fac83a6b0c3313087d8871312b4eac18b9'
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
CTX=os.environ.get('CODEX_THREAD_ID','UNVERIFIED')
UTC=datetime.datetime.now(datetime.timezone.utc).isoformat()
def write(name,x):
    (P/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def load(name):return json.loads((P/name).read_text())
def sha(data):return hashlib.sha256(data).hexdigest()
def js(x):return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
readset=json.loads((TASK/'continuation-v2/D.complete.json').read_text())
originals=load('original-recovery.json')['files']
legacy=json.loads((P/'originals/6').read_text())

# Every statement below was written after the corresponding complete record view
# was displayed. Text reception and source/consumer acceptance are separate axes.
notes={
'R6-CM-FB-01':('合法作者数据可命中已有但不能构造效果的绑定；名称缺席才进入无实现回退。Physical40与Status0均先遇构造边界，Metronome外层已提交前缀不自动回滚。','现WP43的缺席前提及旧缺席向量仍正确；未来不必复制常量空间/构造方式。可选精度补充不能升级默认401绑定损坏。','源工厂57–70、数据schema/初始化22–57、无实现失败门10–18及simple调用136–149已新读。编译全部准入、完整Metronome及外层PP/历史链、B8 WP43/catalog尚未完整接收。'),
'UI-ST-002':('单纯持有导航跳过自动马赛克；成功交换可独立重启效果，刷新读取当前暂持对象。交换后的Q=X/held=Y不因BACK回滚。','当前§9位于暂持跨页上下文，不能截句推成所有成功交换都冻结。保留optional/P3，不认证像素。','完整pbSetMosaic、场景pbSwap、pbUpdateOverlay、screen pbSwap及B8暂持跨页条款新读；入口全链/其它列出的向量与旧反证实际原件仍未完整接收。'),
'GR6-F-003':('18键选择性快照不保存开场地形/持续和默认场地；正常准备Electric/-1与回放新场地None/0的对照须排除入场再设地形。','精确18键与不完整状态声明已蕴含该缺失；可选具名兼容向量，不新计重复必修。旧隔离源观察仅保原资格，不计D执行。','完整RecordedBattle、ActiveField、默认setter、prepare_battle、设施包装及当前WP58有关条款/向量未新接收。'),
'GR6-F-G001':('当前根目录缺STICK/VICEGRIP时，FARFETCHD空持物、CRAWDAUNT丢该招并保三幸存招式顺序；显式Gen5目录可保身份。','通用未知物品nil/未知招式跳过规则已有正确合同；备份不自动生效，不新增别名或强制语料修订。GR6-F-010只是原别名。','准确PBS节、解析/编译/反写完整定义与设施消费者、B8 WP76/catalog尚未实质接收。'),
'R6-D-FONT-C01':('三档只按本档默认及显式有序候选查询；全部未中交空名，显式设置未中再试本档默认。格式化标记的Arial分支另列。','原文未承诺遍历八字体或跨档自动替代；文件存在不能代宿主Font.exist结果。保留同根GR7-M18-001和optional。','完整MessageConfig/DrawText必要定义与窗口消费者及当前WP17有关条款未新接收。'),
'R6-D-PBS-C08':('0=None编辑标签与通用Shadow/0路径请求是不同观察层；人工0资源存在且加载成功时才可谈请求结果，不能推实际阴影像素。','当前资源选择通用分支正确；没有证实真实Graphics/0素材，不要求创造资源或升级必修。','SpeciesMetrics、shadow_filename/bitmap、场景对象及B8 WP73-B/WP15必要定义和条款未新接收。'),
'R6-DX-AN-007::FLOAT_RECURRENCE':('一般N逐次浮点累加的端点位级误差为独立可选精度facet；不混入默认点数值的必修父根。','父项关闭不选择该facet，不要求未来保留同一浮点递推或声称像素等价。','原AN-007完整默认/一般N两输入域及其当前消费者尚未新接收。'),
'BAG-04':('旧registeredItems/index的nil跳过与false分别变[]/[0,0,1]；choices非nil会clone，各分支独立。','当前正常列表/三元索引域不承诺任意错型旧档。旧浏览位置大小写清理缺陷另由B8 WP10正确保留，不能把本项两字段的清理扩为全部字段。','完整207–230转换及B8 WP10目录行、WP65快捷游标完整有关段新读；完整迁移生命周期/存档往返未新接收。'),
'UTIL-03':('首尾片段含n=0/越长尾取整串、blank空白判定与旧ASCII数值谓词分别保留；旧“尾随空白均拒绝”须服从末尾LF的后继资格。','PBS解析不等于此helper；GR7-H14-001是同一旧policy的事实资格facet，未选择兼容，不另加必修或新policy根。','完整first/last/blank/numeric定义新读；C17后继完整文字由父file23用途接收关联。末LF旧实际1进程10输入只保历史，不记本次执行。'),
'UTIL-05':('对称差去重，左独有值后接右独有值，保各侧首次出现顺序；[A,A,B]与[B,C,C]给[A,C]。','没有默认caller不能抹去事实，也不能由数组算符存在要求未来公开同名API。policy未选择。','完整Array对称差方法新读；B8 WP03schema完整有关表已读，未宣称此业务表定义全部通用集合兼容。'),
'UTIL-11':('旧常量辅助各自的nil/false/0、异常捕获阶段和原样返回分别保留；反查别名按给定枚举首遇，非稳定优先。','GameData领域严格/宽容查询不等于这套反射旧输入域；未选兼容，不强制未来常量/类结构。','完整isConst?/hasConst?/getConst/getID/两反查方法104–152已新读；无新默认调用存在性或全工程负证据结论。'),
'UTIL-12':('set保参数集合引用；execute优先显式回调、以当次参数数组为上下文，set之前遍历参数可先失败。','WP05显式事件参数不等于隐式上下文；事实保留与未来是否提供兼容能力分开，不要求instance_eval。','完整CallbackWrapper构造/set/execute335–361和B8 WP05相关参数合同新读；外域动态扩展未新核。'),
'UTIL-13':('摄氏先对9C/5舍入再加32；华氏对5(F−32)/9整体舍入；负半值不能交换顺序。','当前时间/天气域未承诺统一物理温度服务；数学可判定不等于必须引入未来API。policy未选择。','完整两温度转换63–71及B8 WP06目的/范围1–18新读；未执行向量。'),
'GR6-POL-001':('三个可读旧宿主数据库剖面分别保构造默认/反序列化/覆写边界，344类方法与988字段是原有限静态分母。','当前活动consumer不会自动选全部旧剖面；原生版本/后端选择未知，未来先选有限兼容域。','本次只接完整历史policy文字；三个剖面和当前活动消费者本体未新接收。'),
'R6-UI-PARTY-004':('完整旧提案的Entry0→空Summary故障链是已反证历史；当前根NO_REQUIRED_REVISION及相反旧实证资格保持，BACK正常nil。','command在loop块内条件赋值不能借上轮Entry0直接推出本轮Summary；B8失败首错误后继续/留画面合同保留，不重开原必修。','多选完整方法1051–1139及B8§4.6/§9完整有关条款新读。旧实证完整I/O、规则域及其它Summary消费者未全部新接收，绝不冒本次运行证明。'),
}
for n,x in enumerate(legacy['limits']):
    notes[x['id']]=(x['title']+'：'+x['r6_available_and_reviewed']+' 未知：'+x['unknown_scope'],
      '这是原R6有限已审/未知/恢复条件文字；不授R8源/程序/宿主新批准，不把D可得缺读塞入此limit。',
      '完整原记录及原恢复条件已读；原evidence目标本体没有因记录引用取得D阅读信用。')

text_events={
 'optional/0':['cb5b71'], 'optional/2':['3182b4'],
 'optional/3':['337302'], 'optional/4':['337302','db09ce'],
 'optional/5':['db09ce','bf6944 (80–130补读21token截断)'],
 'optional/6':['bf6944'], 'FLOAT/0':['28f2da'],
 'policy/0':['d50036'], 'policy/1':['d50036'], 'policy/2':['d50036'], 'policy/3':['d50036'],
 'policy/4':['28f2da'], 'policy/5':['28f2da'], 'policy/6':['28f2da'],
 'no_required/0':['4803e1'],
}
receipts=[]
for x in readset['semantic_objects']:
    k,n=x['kind'],x['index']; value=legacy[k][n]; meaning,counter,join=notes[x['id']]
    receipts.append({'kind':k,'index':n,'id':x['id'],'pointer':f'file6#/{k}/{n}',
       'original_payload':originals[6], 'exact_value_sha256':sha(js(value)),
       'record_text_reading':'COMPLETE_ALL_ORIGINAL_FIELDS_AND_PROPOSAL_WITH_EXACT_VALUE_ASSOCIATIONS',
       'reading_events':text_events.get(f'{k}/{n}',['ded47c']),
       'bounded_reception':'HISTORICAL_RECORD_TEXT_RECEIVED; CURRENT_SOURCE_AND_CONSUMER_ACCEPTANCE_NOT_AUTOMATIC',
       'meaning':meaning,'strongest_no_required_counter':counter,'join_and_remaining':join,
       'retained_classification':k,'adoption':'NOT_SELECTED_OR_NOT_APPLICABLE',
       'execution':'NOT_EXECUTED','full_frozen_semantic_reception':'NOT_COMPLETE'})
write('reception-ledger.json',{'schema':'gr8-hc2-d-bounded-receptions/v1','utc':UTC,'actual_context':CTX,
 'status':'INCOMPLETE','legacy_text_receipts':receipts,'all_29_text_read':True,
 'all_29_full_current_source_consumer_acceptance':False,'new_canonical_body_reading_credit':0,
 'old_27_reopened':False,'UPDATE_NOT_STARTED':True})

common={'contract_commit':CONTRACT,'base_report_commit':BASE,'target_commit':TARGET,
 'target_tree':readset['target_checkout_tree'],'target_task_tree':readset['target_task_tree_observed_from_fixed_commit'],
 'B8':B8,'R':R,'actual_context':CTX,'parent_context':'01a14465-f204-7783-a526-9b43e91ea005',
 'original_author_context':readset['target_author_actual_context'],'spawned':0,
 'actual_configuration':dict.fromkeys(['model','effort','tier','speed','Fast'],'UNVERIFIED')}
assert CTX not in (common['parent_context'],common['original_author_context'],'UNVERIFIED')
write('independence.json',dict(common,thread_and_session_echo_equal=CTX==os.environ.get('CODEX_SESSION_ID'),
 evidence='244f1f: only CODEX_THREAD_ID/CODEX_SESSION_ID read; no credentials/quota probes',
 requested_configuration={'model':'gpt-6.1-sol','effort':'ultra','tier':'default','speed':'normal','Fast':False}))
write('frozen-denominator.json',dict(common,schema='gr8-hc2-d-frozen-denominator/v1',
 own_legacy_objects=readset['semantic_objects'],original_purpose_indices=readset['original_purpose_indices'],
 shared_root_field_scope=readset['shared_root_field_scope'],required_current_structures=readset['required_current_structures'],
 full_input_file_count=45,transport_only_bytes=5862414,
 independent_populations={'legacy31':{'optional':8,'FLOAT':1,'policy':7,'limits':14,'no_required':1},
 'canonical37':{'required':27,'optional':7,'no_required_revision':1,'policy':2},'optional_navigation_facets':2},
 root_reserved_accepted_in_BASE=readset['root_reserved'],prior_accepted=readset['already_received'],
 no_combined_PASS_denominator=True,semantic_generation_credit=0))

full_purpose_text={5:'完整历史资格文字，四报告和完整非必修外围字段；current56的56项为指针/状态/案例计数用途，不接其所指源正文。',
 6:'只限D29完整历史记录文字，另两条由固定BASE父接收范围关联。必要当前源/消费者仍逐项开放。',
 11:'完整发布绑定文字及33/21824成员字段的身份用途；不冒D重新远端读取旧19GB包。',
 19:'完整九入口资格、323派生用途的所有分类/处置/状态值及原字段用途；当前指向正文不自动通过。',
 20:'5732行完整字段类型/身份用途及全部共用资格/18anchor-overlay关联；无事实body信用。',
 21:'25001行及1072准确接收override字段用途/全部disposition；DL-F015无formal-range保留；无条款body信用。',
 22:'736行全部程序locator/引用字段用途及所有kind/status/premise值；不读目标程序、不授执行。'}
purpose=[]
for i in readset['original_purpose_indices']:
    status='OPEN_AVAILABLE_NOT_COMPLETELY_RECEIVED'
    if i in full_purpose_text:status='BOUNDED_TEXT_OR_TYPED_PURPOSE_READ; NECESSARY_TARGET_BODY_CREDIT_ZERO'
    if i in (0,1,15,16,18):status='SHARED_ROOT_FIELDS_READ; ASSIGNED_PER_RECORD_BODIES_EXCLUDED_AND_OPEN_BY_RECEIVER'
    purpose.append({'index':i,'identity':originals[i],'status':status,
      'scope':full_purpose_text.get(i,'仅已显示的共享根字段或探索性局部；不据此签整份用途。'),
      'all_required_semantic_interfaces_received':False})
write('reading-ledger.json',{'schema':'gr8-hc2-d-actual-reading/v1','utc':UTC,'actual_context':CTX,
 'instructions':{'AGENTS':'full 6328B read 562fcd/43c35f','global_prompt':'full 241 lines 43c35f/e6f397',
  'task_prompt_and_skill':'full 4ffff3; skill explicitly excludes audit reports; no formal revision',
  'original45_readset':'full compact 3fca81; D complete supplemented 543621/b9dfdf',
  'contract_equality':'3fca81: all three D contract files equal64cfde5'},
 'purposes':purpose,'legacy_receipts':'reception-ledger.json#/legacy_text_receipts',
 'shared_root_events':['3e9085 (0/1)','cfd37b (15/18)','scope16 complete following 683e7d parent exact receipt'],
 'typed_purpose_events':['scope20/21/22 complete raw output','scope19 1–370 and371–737 complete raw outputs','scope11 complete raw output'],
 'prior_receipts':{'commit':BASE,'objects':'canonical0/15/16/35, legacy optional1/7, original purposes2/3/4/7/8/17/23/24',
 'use':'Only exact stated historical/text/identity bounds from complete parent report/additional-receptions read in683e7d; no D new credit'},
 'exploratory_truncation_zero_missing_text_credit':['140fa0','0d3ff7 material-inventory print/list.items failure','3e9085','8d9b84','85427c H11'],
 'supplemented_truncations':{'D_complete':'543621+b9dfdf+3fca81','optional5':'bf6944 80–130','H11':'full subsequent raw display'},
 'source_and_formal_readings':'source-readings.json','generation_grants_reading_credit':False,
 'formal_full_file_credit':0,'global_PASS':False,'UPDATE_NOT_STARTED':True})

source_spans=[
 ('R','Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb',[[1,70]],'完整构造与from_pokemon_move；末尾其它片段不计完整方法'),
 ('R','Data/Scripts/010_Data/002_PBS data/005_Move.rb',[[1,57]],'完整schema/initialize；其它函数截断不计'),
 ('R','Data/Scripts/011_Battle/003_Move/004_Move_BaseEffects.rb',[[1,18]],'完整Unimplemented whole-use门'),
 ('R','Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',[[136,149]],'完整pbUseMoveSimple；未签外层完整use链'),
 ('R','Data/Scripts/001_Technical/002_RubyUtilities.rb',[[1,87],[330,361]],'完整必要字符串/集合方法与CallbackWrapper；未签其余工具'),
 ('R','Data/Scripts/019_Utilities/001_Utilities.rb',[[1,152]],'完整组合/温度/常量辅助；后续TimeEvent截断不计'),
 ('R','Data/Scripts/002_Save data/005_Game_SaveConversions.rb',[[207,230]],'完整bag注册转换；不签全迁移链'),
 ('R','Data/Scripts/016_UI/005_UI_Party.rb',[[1051,1139]],'完整多选方法，旧Entry0前提反核'),
 ('R','Data/Scripts/016_UI/017_UI_PokemonStorage.rb',[[1064,1070],[1131,1149],[1418,1479],[1813,1843]],'完整必要mosaic/swap/overlay/领域swap；周边截断函数不计'),
 ('B8','deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md',[[264,275]],'完整暂持跨页有关条款；后续搜索表未计'),
 ('B8','deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md',[[126,136],[230,242]],'多选/返回/失败必要完整条款'),
 ('B8','deliverables/final-specification-set/generic-kernel/wp10-migration-failure-recovery.md',[[70,99]],'完整转换目录和bag前提；其它表未获全读'),
 ('B8','deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md',[[130,158]],'完整有关schema结构表'),
 ('B8','deliverables/final-specification-set/generic-kernel/wp05-events-extensions-plugins.md',[[1,45]],'完整目的/参数原语/命名表有关条款'),
 ('B8','deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md',[[1,18]],'目的/范围，非温度服务声明'),
 ('B8','deliverables/final-specification-set/user-interface/wp65-title-load-options-pause-and-pc.md',[[207,239]],'快捷候选/游标/取消/消费/持久完整有关条款'),
]
sources=[]
for repo,path,spans,scope in source_spans:
    gitroot=REPO if repo=='B8' else Path('/workspace/pokemon-essentials')
    commit=B8 if repo=='B8' else R
    data=subprocess.check_output(['git','-C',str(gitroot),'show',commit+':'+path])
    # Verify exact fixed bytes at the actual source location; hashing is identity only.
    assert (gitroot/path).read_bytes()==data
    sources.append({'repository':str(gitroot),'commit':commit,'path':path,'bytes':len(data),'sha256':sha(data),
      'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest(),
      'actual_complete_relevant_ranges':spans,'scope':scope,'evidence_level':'SOURCE_STATIC_OR_FORMAL_STATIC',
      'full_file_semantic_credit':False,'execution':'NOT_EXECUTED'})
write('source-readings.json',{'readings':sources,'truncation_rule':'Only listed complete relevant units receive credit; partial neighbouring methods and truncated first formal composite are excluded.',
 'behavior_execution':0,'runtime_equivalence':False})

interfaces=[
 ('D-I01','31 inherited record containers','D29 text + parent2','BOUNDED_TEXT_RECEIVED','31/37、FLOAT/facet及policy数量分列；不升级源事实/执行。'),
 ('D-I02','canonical/findings/C13/C19 shared root fields','consumer records in A/B/C/root','OPEN_OTHER_RECEIVER_BODY','完整shared资格可读；未收到33个canonical的实际非作者完整接收，不签其body或接口。'),
 ('D-I03','old UTIL-03 numeric wording','GR7-H14-001 / C17 successor qualification','BOUNDED_HISTORY_QUALIFICATION','末LF后继限定与旧字段生成时点并存；不另选policy。'),
 ('D-I04','5732/25001/736 locators','source-fact/clause/program targets','TYPED_IDENTITY_PURPOSE_ONLY','全部字段用途保留；指针不授目标本体信用；E009/E010撤销与DL-F015例外保持。'),
 ('D-I05','13 batch author candidates','50 shared receivers /48 conflicts /R7-I/R7-IR','OPEN_AVAILABLE_NOT_FULLY_READ','assignment27→13和firstwave13已读；全候选scope/边条件/冲突贡献尚未完整接收。'),
 ('D-I06','handoff control prose + manifest semantic/task strata','manual update and parent task-final','OPEN_AVAILABLE_NOT_FULLY_READ','不得由v2状态或工具成功授权启动；87/31任务资格及其它业务字段仍待完整实读。'),
 ('D-I07','B8 publication binding text','old transport identities / original qualification','BOUNDED_HISTORICAL_TEXT_AND_TYPED_IDS','33/21824成员身份用途完整处置，不称D新取回旧整包或源正文。'),
]
write('interfaces.json',{'schema':'gr8-hc2-d-interfaces/v1','interfaces':[dict(zip(['id','producer','consumer','status','reason'],x)) for x in interfaces],
 'unreceived_producer_cannot_sign_consumer':True,'root_task_final':'EXCLUSIVE_PARENT_MAIN_REVIEWER'})
write('proposal-counters.json',{'schema':'gr8-hc2-d-counter-attempts/v1','actual_non_author':CTX,
 'new_required_proposals':[],'new_required_confirmed':0,
 'legacy_counters':[{'id':x['id'],'pointer':x['pointer'],'strongest_counter':x['strongest_no_required_counter'],
 'scope':'Bounded D reasoning; final legacy classification retained, no new global verdict'} for x in receipts],
 'GR8-HIST-C2-001':{'status':'PARENT_RESERVED_NOT_REPEATED','parent_receipt':BASE+':tasks/receive_external_h_c2_current_records/counterreview-hist-c2-001.md',
 'rule':'D不把父最强反证冒作D原创或根裁决。'},'new_proposer_independence_votes':0,
 'missing_reads_are_not_NO_REQUIRED':True,'UPDATE_NOT_STARTED':True})

remaining=[]
for i in (9,10,12,13,14):
    remaining.append({'kind':'ORIGINAL_PURPOSE_INCOMPLETE','index':i,'identity':originals[i],
       'pointer':'file'+str(i)+'#','exact_scope':'完整当前非canonical新增值及必要依赖/消费者。已显示的局部不免除此整份用途的剩余。',
       'available':True,'cause':'AVAILABLE_NOT_COMPLETELY_READ_OR_RECEIVED','host_limit':False})
for x in receipts:
    value=legacy[x['kind']][x['index']]
    remaining.append({'kind':'NECESSARY_CURRENT_FACT_JOIN_NOT_FULLY_CERTIFIED','id':x['id'],'pointer':x['pointer'],
      'exact_scope':x['join_and_remaining'],'original_source_formal_and_consumers':value.get('bidirectional_evidence',
        {'source':value.get('source_anchors',value.get('source',[])),'formal':value.get('current_contract_anchors',[]),'evidence':value.get('evidence',[])}),
      'available_materials_not_host_limit':True,'execution_not_required_for_static_reads':True})
write('unread.json',{'schema':'gr8-hc2-d-exact-remaining/v1','status':'INCOMPLETE','items':remaining,
 'cross_scope_excluded_records':{'ids_by_partition':json.loads((TASK/'continuation-v2/manifest.json').read_text())['partitions'][:3],
 'state':'Their actual new receipts are not present in BASE; D grants no body/duplicate credit.'},
 'other_target_transport_inputs':'45 identities verified, but only instructions, declared record text/purpose and specifically listed helper source reads get semantic credit. Untouched scripts, tool I/O and unreviewed target claim evidence remain identity-only, not all45 FULL_READ.',
 'missing_materials':[],'permission_blockers':[],'material_or_host_limit_used_to_hide_unread':False,
 'READY_FOR_PARENT_RECEPTION':False,'UPDATE_NOT_STARTED':True})

# Preserve the exact projections used for displayed records and root purposes.
# Unopened projections remain explicitly uncredited, and are excluded here.
evidence_names=[f'optional-{i}.json' if i==0 else f'optional-{i}.factored.json' for i in (0,2,3,4,5,6)]
evidence_names += ['no_required-0.factored.json','FLOAT-0.factored.json']
evidence_names += [f'policy-{i}.factored.json' for i in range(7)]
evidence_names += [f'limits-{i}.factored.json' for i in range(14)]
evidence_names += [f'scope-{i}.json' for i in (0,1,15,18,16,5,19,20,21,22,11)]
blob=js({'schema':'gr8-hc2-d-displayed-projections/v1','rule':'Generation is not reading; ledger/events determine actually displayed scopes.',
 'files':{n:(P/'views'/n).read_text() for n in evidence_names},
 'legacy_value_associations':load('value-associations.json'),
 'scope_associations':load('scope-associations.json')})
(P/'reading-evidence.json.gz').write_bytes(gzip.compress(blob,mtime=0))
write('reading-evidence.identity.json',{'decoded_bytes':len(blob),'decoded_sha256':sha(blob),
 'encoded_bytes':(P/'reading-evidence.json.gz').stat().st_size,'encoded_sha256':sha((P/'reading-evidence.json.gz').read_bytes()),
 'rule':'Bounded gzip decode JSON only; never execute restored sources. Unopened projections do not get credit.'})
write('progress.json',dict(common,status='INCOMPLETE',utc=UTC,legacy_record_texts_read=29,
 remaining_original_purposes=[9,10,12,13,14],current_source_consumer_joins_not_blanket_certified=29,
 new_reference_behavior_execution=0,UPDATE_NOT_STARTED=True))
print(json.dumps({'legacy_texts':len(receipts),'remaining_purposes':5,'status':'INCOMPLETE','actual_context':CTX}))
