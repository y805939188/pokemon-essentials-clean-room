#!/usr/bin/env python3
"""Serialize manually reviewed finite reception; never execute reference business code."""
from pathlib import Path
import json, hashlib, datetime, collections

base = Path(__file__).resolve().parent
rr = base.parent.parent
utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(name): return json.loads((base/name).read_text())
def put(name, obj):
    (base/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
def binding(path):
    p = rr/path
    raw = p.read_bytes()
    return {'path':path, 'bytes':len(raw), 'sha256':hashlib.sha256(raw).hexdigest()}

backup = 'evidence/external-recovered/receive_external_pbs_creature_backups/96ee9a69e24d5e2063be7ebcf8de0fdb2e019510/'
facts = [
 {'id':'AI-DATA-01', 'facet':'activation', 'facts':[
  '普通发现只枚举PBS顶层txt，按最长基名匹配确名或下划线后缀；四代及Shadow子目录存在不使它们活化。facility显式文件请求是另一入口。',
  '选用备份要求作者显式选择/提升相容输入、有效引用和此前步骤正常；Generation字段是物种描述，MECHANICS_GENERATION及其类载入派生默认不随备份路径或运行时赋值自动重算。',
  '四代数据分别依自己的基础锚点解释，不混代或从同名/同hash推导组合兼容。Shadow四文件还要求显式激活及有效SHADOW/Move/Species依赖。'],
  'provider_objects':['PB01/PB06/PB09','KERNEL SFR01/SFR06','BACKUP IF01/CD-I06','PCR common_premises.backup'],
  'AI_consumers':['AITrainer40–52','AIMove/BattleMove category and data-dependent handler setup'],
  'preserved':'WP51/52技能、加权和真实命令范围不变；无所有代际组合支持或当前已编译产品认证。'},
 {'id':'AI-DATA-02', 'facet':'author fields, identities and defaults', 'facts':[
  'PBS_BATTLE已合格21路径7704路径记录字段/省略合同由原实际读者承担；本接收者实际读field-contracts全部及PB01–20完整逻辑对象，不重新记本人7704原始记录全文。其own11/同byte关联5、CREB原raw4/关联1归属保留。',
  'Move的Type/Target及Item的Move走当前依赖枚举；FunctionCode是原作者文本，不在编译时统一查实现存在。Status正威力拒绝，物理/特殊零威力警告后转Status；未知合法效果走真实factory回退，与独立AI handler缺省不同。',
  'Move缺省power0/categoryStatus/typeNONE/accuracy100/PP5/TargetNone/priority0/effectChance0/Flags空分别保留；构造默认不等作者可用枚举批准。power1、accuracy0、总PP0、目标数0各有独立消费者。',
  'Type弱/抗/免疫关系保留原先后，generic相性乘积不自行去重全部参数；普通Battler类型收集另去重。Gen5无FAIRY且STEEL抗DARK/GHOST，后代数据/分类设置与当前机制分开。',
  'Ability/Item名称与描述为显示数据；身份及实际Flags、当前有效能力/持物和各caller gate才影响已审AI查询。物品主动BattleUse、被动持有、can_hold、important和消费规则分开；不由描述推callback或激活。',
  'Gen5 VICEGRIP与当前VISEGRIP无自动别名；SheerCold、DarkVoid、HiddenPower、Teleport等四代原字段/效果码差异按各自输入保留，不称一键旧规则切换。'],
  'provider_objects':['PBS_BATTLE field-contracts all families; PB01–20','existing CRE-B record and handler receipts'],
  'AI_consumers':['AIMove full563','AI_ChooseMove full393','AI utilities full898','all nine effect source files'],
  'preserved':'所有原始长列表/名称/描述逐记录全文信用仍归合格producer，不授本人与整740/267callback复审信用。'},
 {'id':'AI-DATA-03', 'facet':'current and backup creature fields', 'facts':[
  'PCR原11路径2178记录26936显式字段及所需字段/默认语义归/root/pbs_creature_current_cloud；本接收者实际收共同前提及26原manual groups，加经52325B强制伴件纠正的species.mega，合27组有限含义。',
  'BACKUP的6712路径记录/89067绑定/75313省略继承由四个实际独立主读者与原Encounter/metrics接收者承担，完整已合格输入贡献可用；此处不重读或重记6712、212atoms、12全域接口。与PCR/PBS_BATTLE重叠人口不相加。',
  'Species base/form身份、选中形态、普通/simple/forced写入及能力缓存清理分开。Types uniq、数值/数组/逐成员克隆、缺失或空Moves/Evolutions、三野生持物池全缺才共同继承各按所属代基础处理。Tutor重复保留；个体reset_moves只对合级Moves去重取最新后末4。',
  'BaseStats按PBS Stat次序，成长/性别/幸福/体重/能力及学习列表的字段默认分别进入当前Pokemon个体或缓存；battle副本可随后独立改变。Legendary/Mythical/UltraBeast标志以Species大小写不敏感查询进入实际AITrainer野生技能32分支。',
  'Mega候选按当前simple形态匹配并取首个满足持正确石 OR 知道所需MegaMove的记录；另持任意Mega石不单独否决招式分支。裸query不同实际ring/配额/换人/Shadow/执行许可。',
  'Shadow字段、目标/效果、metrics和遭遇只接字段→所述查询/生成/快照请求，不引入游戏触发、UI成功或宿主保证。旧Encounter谓词成功必reset句不采用；独立reset入口和后继调用者另列。'],
  'provider_objects':['PCR common_premises/manual_groups + mandatory Mega/token/locator/weight/Shadow scope companions','BACKUP report current1–34 and IF01/02/09/CD-I06 complete objects; necessary-provider corrections'],
  'AI_consumers':['AITrainer40–52','AIBattler current Pokemon/Battler queries','AIMove rough power/type and direct real-method queries','AI switch roster/ability/item/type analysis'],
  'preserved':'接收有限完整字段含义与已合格原值贡献；整外域formal、native、所有回调/事件和各原reader个人未读不清零。'},
 {'id':'AI-DATA-04', 'facet':'trainer construction and AI snapshot', 'facts':[
  'PCR72 TrainerType/20 Trainer完整字段与15完整手写consumer meanings已实际接收。TrainerType缺省gender2、base_money30、skill取有效base_money（包括0）、flags空；编辑器9999不是通用解析上限。',
  'Trainer runtime skill/flags facade可读当前TrainerType，但AITrainer构造复制当时skill及flags，随后依32/48/100门补flags并按精确大小写Anti前缀去除；表重载不自动重建已存在AITrainer。',
  'TrainerType.has_flag?大小写不敏感不同AI skill flag精确include。nil-trainer野生技能从实际初始side battler的Species标志读取，旧ZERO_ABLE/MIXED_ORDER范围保持。',
  '普通trainer数据按type/name/version精确查，无版本回退；to_trainer复制items并有序创建Pokemon后施加Move/ability/gender/IV/EV/Shadow等覆写。已有对象/新造对象、登记/选择/实际执行和保存值分层，正常前序门及失败前缀保留。'],
  'provider_objects':['PCR trainertype.fields/trainer.fields','trainer92 manual_consumer_meanings all15','Developer TRAINER-DATA for construction subset'],
  'AI_consumers':['own AITrainer1–100 originalFULL + resumed reread','own TrainerType originalFULL + resumed77–134'],
  'preserved':'Developer单句gender0默认不采用，实际源码101–112与PCR更精确合同为gender2；不是新formal差异或新proposal。'},
 {'id':'AI-DATA-05', 'facet':'parse/register/compile/write failure prefixes', 'facts':[
  '普通BOM/注释/第一#删除、CSV/q/可选位/重复字段/严格枚举各按真实parser顺序；有效未知属性可忽略，不据此保证任意畸形输入。',
  '直接register替换；generic compiler先clear、逐记录转换/校验、重复拒绝、登记，再全表终检/save。后项失败可保留此前内存登记，早先table文件也可已写；不存在跨表统一回滚。',
  '完整编译按types→abilities→moves→items→species/forms/依赖者，ordinary startup Compiler.main为debug gate并检查缺PBS/import/必需输出/整秒最大mtime/force，触发可先删列出产品再进入compile_all。',
  '直接compile_all(true)执行内容阶段/动画/训练师事件/消息，不继承startup检查、predelete或outer rescue；Reset/SystemExit传播，普通诊断/删除步骤也可能提前失败，各前缀分别保留。',
  'Writer输出来自当前登记值/schema/后缀分组或专用路径；PBS文本写出与archive保存分开，后写失败不回滚先前登记/盘写。导出也不证明缓存失效或完整字节roundtrip。'],
  'provider_objects':['KERNEL SFR02/04–10 + mandatory Compiler1117','Developer COMP-CSV/LIFECYCLE/PBS-GENERIC/SPECIES/TRAINER and registry','PBS_BATTLE PB02/03/16/18'],
  'AI_consumers':['data available to newly constructed trainers/Pokemon/BattleMove and current registry lookups'],
  'own_source_checks':['Compiler001924–1117 complete named rewrite/discovery/compile_pbs_files/compile_all/main definitions'],
  'preserved':'KERNEL SFR05旧full1010必须按mandatory改1117；此处本人只新增所示194行有限区间，不冒本人Compiler全文。'},
 {'id':'AI-DATA-06', 'facet':'startup, cache and reload', 'facts':[
  'Main先messages/plugins/Compiler.main再Game.initialize；后者建立新Game_Temp并GameData.load_all替换各DATA。普通Game.load(saved_values)装存档及地图，不再编译或load_all。',
  'GameData整体save/load不归一化内层业务图，也不更新旧record引用。Pokemon::Move保存ID/PP/PPUp，字段及总PP按当前表读取；Battle::Move创建时保存name/function/power/type/category/accuracy/target/priority/effectChance并克隆Flags。',
  'Battle::Move总PP有正数显式覆盖才优先，否则可委托realMove；AI包装现存battleMove及其当前阶段calcType/moldBreaker，而非重构PBS。现有招式快照和AITrainer技能快照不因registry reload统一刷新。',
  '四个Game_Temp数据cache和MapFactoryHelper的class缓存不同。pbClearData显式清四cache及connection/dimension，并条件setup encounters/loadTilesets；直接compile_all不调用它。新Game_Temp本身不清独立MapFactory缓存。',
  '显示name/description/getter、当前语言消息、资源选择与真实像素/音频分开；表或文本落盘不证明界面/实例/资源立刻同步。真实dat/native save-reload为0次。'],
  'provider_objects':['Developer CACHE-TEMP/CACHE-CONNECTION/GAME-START/REGISTRY','PBS_BATTLE PB16–18','PCR TRAINER-TYPE-LIVE/RELOAD'],
  'own_source_checks':['MiscPBSData1–64 FULL','GameStart1–126 FULL','BattleMove1–201 FULL','PokemonMove1–77 FULL','AITrainer1–100 reread'],
  'AI_consumers':['AIMove setup/get_base_power/type/priority/accuracy/damage','AITrainer cached skill and sanitized flags','AIBattler current live delegates'],
  'preserved':'全部SOURCE_STATIC/具名事实接收；不授宿主成功、native编解码、任意存档迁移或插件兼容。'}
]

# These exact logical objects were actually displayed and read in this context.
excluded = {'REC_BACKUP_ATOM_SHAPE'} # truncated exploratory sample; repaired sample is separately retained
receipts=[]
for f in sorted((base/'io').glob('REC_*.json')):
    o=json.loads(f.read_text())
    if o.get('exit_code')!=0:
        continue
    entry={'io':str(f.relative_to(base)), 'start_utc':o.get('start_utc'),'end_utc':o.get('end_utc'),
           'original_exit_code':o.get('exit_code'),'original_identity':o.get('identity'),
           'credit':'EXPLORATORY_TRUNCATED_NO_ACCEPTANCE_CREDIT' if f.stem in excluded else 'ACTUAL_COMPLETE_SELECTED_OBJECT_OR_SOURCE_INTERVAL_READING'}
    if o.get('operation')=='STATIC_JSON_OBJECT_READ_NOT_BUSINESS_EXECUTION':
        payload=json.loads(o['stdout']);entry['provider_path']=payload['path']
        entry['complete_object_selectors']=[x['selector'] for x in payload['selected']]
    else:entry.update({'path':o.get('path'),'range':[o.get('start_line'),o.get('end_line')]})
    if f.stem=='REC_PCR_FRONTIER':entry['credit']='ACTUAL_COMPLETE_1–277_PLUS_SEPARATE_TAIL_REPAIR278–301'
    receipts.append(entry)

rootpaths=['adjudication/root-pbs-current-task-final-acceptance.v1.json','adjudication/root-kernel-task-final-acceptance.v1.json','adjudication/root-developer-task-final-acceptance.v1.json','adjudication/root-pbs-backups-task-final-acceptance.v1.json']
packet={'schema':'gr8-com-ai-pbs-reload-reception/v1','utc':utc,'receiver':'/root/com_ai',
 'same_actual_context':True,'new_contexts':0,'new_independent_votes':0,
 'fixed_B8':'fd1df570cad987dc3852a3b958f03916e317f7fe','fixed_R':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
 'interface':'IF-COMAI-DEFAULT-PBS-RELOAD','status':'ACCEPTED_COMPLETE_NECESSARY_FINITE_AI_DATA_INTERFACE',
 'basis':'Actual complete finite meanings/common premises and own original20R9F consumer reading. Root status/hash/provenance alone is not acceptance.',
 'qualified_provider_populations':[{'provider':'/root/pbs_battle','population':'21 paths/7704 path-records','personal_raw_credit_transferred':False},
  {'provider':'/root/pbs_creature_current_cloud','population':'11 paths/2178 records/26936 explicit fields','personal_raw_credit_transferred':False},
  {'provider':'four generation readers + original backup receiver','population':'6712 path-records/89067 bindings/75313 omission dispositions','contribution_commit':'96ee9a69e24d5e2063be7ebcf8de0fdb2e019510','root_acceptance':rootpaths[3],'personal_raw_credit_transferred':False},
  {'provider':'/root/kernel_atomic_reception','scope':'SFR01/02/04–10 finite declarations/registry/parser/compiler/cache, actual original qualified reader retained'},
  {'provider':'/root/developer_full_cloud','scope':'Compiler startup/direct/cache and selected constructor/registry complete facts'}],
 'manual_semantic_facets':facts,'actual_read_receipts':receipts,'root_qualification_bindings':[binding(p) for p in rootpaths],
 'necessary_available_unread':0,'necessary_consumer_unreceived':0,
 'not_accepted':['Entire foreign formal domains or whole6712/7704/2178 rereading by this context','Any source/game/native/UI/media/disk behavior execution','All plugins/dynamic registrations/all arbitrary generation combinations','Global history dedup/equivalent directory/B8 compliance or whole review PASS'],
 'mandatory_corrections':['MegaMove OR condition; arbitrary held MegaStone not an extra bare query gate','Species Types-only uniq; Tutor repetitions preserved','Encounter trigger true separate from reset callers','Compiler1117/complete compile_pbs_files993–1018; no invented EOF lines','TrainerType gender default2; flags case-insensitive only in Species/TrainerType predicate, AI membership exact','Eight audit JSON lexeme tokens vs compiled integer values distinct'],
 'tool_boundaries':{'reference_business_runs':0,'independent_business_model_runs':0,'native_or_serialized_load_runs':0,'source_or_formal_changes':0,'UPDATE_NOT_STARTED':True,'actual_configuration':'UNVERIFIED'},
 'retained_tool_failures':['io/REC_PCR_SCOPE_END.json KeyError scope exit1, exact successful selector retry separately retained','Metadata inventory SyntaxError closing parenthesis exit1: original platform output preserved; no reading credit; corrected inventory exit0; exact failure UTC not separately echoed UNVERIFIED'],
 'truncation_repairs':['REC_PCR_FRONTIER actual continuous1–277 then REC_PCR_FRONTIER_TAIL278–301','REC_BACKUP_ATOM_SHAPE exploratory truncated sample grants no blanket atoms credit; FC01 form/consumer separately read in REC_BACKUP_FIELDS_RETRY']}
put('pbs-reload-reception.v1.json',packet)

interfaces=read('interfaces.json')
old=interfaces['open_interfaces']
assert len(old)==1 and old[0]['id']==packet['interface']
new={'id':packet['interface'],'receiver':'/root/com_ai','providers':['/root/pbs_battle','/root/pbs_creature_current_cloud','four actual backup generation readers + named receiver','/root/kernel_atomic_reception','/root/developer_full_cloud'],
 'status':packet['status'],'evidence_level':['SOURCE_STATIC','RECEIVED_QUALIFIED_COMPLETE_PRODUCER_FACTS'],
 'complete_finite_contract':'Original outstanding AI default/alternate author fields/defaults/activation → parser/schema/registration/compiler/export → startup/load/cache/ordinary-save distinction → existing/new AI consumers.',
 'manual_facts':'pbs-reload-reception.v1.json#/manual_semantic_facets AI-DATA-01–06 all complete meanings',
 'actual_object_read_receipts':'pbs-reload-reception.v1.json#/actual_read_receipts',
 'facts':[f['facts'] for f in facts],'scope_qualification':packet['not_accepted'],
 'necessary_available_unread':0,'necessary_consumer_unreceived':0,'execution':'NOT_EXECUTED','new_contexts_or_votes':0,'UPDATE_NOT_STARTED':True}
interfaces['accepted_scoped'].append(new)
interfaces.update({'updated_utc':utc,'open_interfaces':[],'accepted_scoped_count':15,'open_interface_count':0,
 'status':'PRIMARY_AND_CURRENT_NECESSARY_FINITE_AI_INTERFACES_COMPLETE_AWAIT_ROOT_ACCEPTANCE',
 'previous_open_interface_retained_in_reception_record':old,
 'personal_foreign_unread_not_erased':'unread-and-boundaries.v2.json',
 'not_accepted_global':['Whole COM-BATTLER/COM-MOVE/COM-ABILITY-ITEM/CRE/PBS/UI/FAC formal domains beyond named finite receipts','Native serialized artifacts or executed compile/game/save/reload','All arbitrary generation combinations/plugins/current host state','Global history/equivalent dedup and B8 compliance PASS']})
put('interfaces.json',interfaces)

inventory=read('remaining-reception/readset.json')
rows=[]
for i,x in enumerate(inventory['records']):
    path=x['identity']['path']
    if i<=20: group='PBS_BATTLE qualified21 fields/defaults + existing CRE-B'
    elif i<=31: group='PBS_CURRENT qualified11 record fields/defaults/common premises'
    elif i<=47: group='BACKUP qualified four generation producer contribution'
    else: group='KERNEL/DEVELOPER/PCR complete named source facts and own finite checks'
    rows.append({'path':path,'identity':x['identity'],'prior_personal_or_named_reading_disposition':x['current_AI_receiver_status'],
      'current_necessary_AI_reception':'COMPLETE_FINITE_INTERFACE_RECEIVED','basis':group,
      'own_raw_full_added_by_this_receipt':False,'qualification':'Prior personal raw reading scope remains exact. Qualified producer reception does not rewrite this path to personal FULL or transfer whole foreign task.'})
boundary={'schema':'gr8-com-ai-unread-and-boundaries/v2','utc':utc,'actual_context':'/root/com_ai','new_contexts':0,
 'primary':{'reference_files':20,'formal_files':9,'full':29,'unread_files':0,'unread_lines':0},
 'original_outer_navigation_path_count':62,'path_inventory_is_not_new_primary_denominator':True,
 'necessary_AI_available_unread':0,'necessary_AI_consumer_unreceived':0,
 'prior_personal_disposition_counts_preserved':dict(collections.Counter(x['prior_personal_or_named_reading_disposition'] for x in rows)),
 'paths':rows,'actual_new_own_source_reading':[{'path':'Data/Scripts/021_Compiler/001_Compiler.rb','range':[924,1117],'scope':'complete named units only, not full1117'},
  {'path':'Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb','range':[1,64],'scope':'FULL'},
  {'path':'Data/Scripts/003_Game processing/001_StartGame.rb','range':[1,126],'scope':'FULL'},
  {'path':'Data/Scripts/011_Battle/003_Move/001_Battle_Move.rb','range':[1,201],'scope':'FULL'},
  {'path':'Data/Scripts/014_Pokemon/004_Pokemon_Move.rb','range':[1,77],'scope':'FULL'}],
 'rereads_without_new_unique_source_credit':['AITrainer1–100 originalFULL','TrainerType77–134 originalFULL'],
 'global_and_personal_not_closed':packet['not_accepted'],'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'actual_configuration':'UNVERIFIED'}
put('unread-and-boundaries.v2.json',boundary)
put('remaining-reception/disposition.v2.json',{'utc':utc,'original_readset':'readset.json','original_prompt':'prompt.md','status':'CLOSED_NECESSARY_FINITE_AI_RECEPTION_DO_NOT_REDISPATCH_OLD62_PROMPT','reception':'../pbs-reload-reception.v1.json','personal_scope':'../unread-and-boundaries.v2.json','new_contexts':0,'new_votes':0,'qualification':'Original navigation/readset bytes retained. No new62foreign full-body layer; qualified actual source/record readers and necessary selected meanings received.'})

p=read('progress.json')
p['previous_delivery_end_utc']=p['end_utc']
p.update({'status':'REVIEW_COMPLETE_WITH_REQUIRED_CHANGE_HANDOFF_UPDATE_NOT_STARTED','updated_utc':utc,'end_utc':utc,
 'accepted_interfaces':15,'unreceived_interfaces':0,'mapping':'65manualsourceunits196facts;72manualformalgroup273branches;285catalogrows;15necessaryfiniteinterfacescomplete.',
 'remaining_receiver_prompt':'remaining-reception/disposition.v2.json','remaining_receiver_readset':'unread-and-boundaries.v2.json',
 'resume_same_context_new_contexts':0,'current_necessary_available_unread':0,'current_necessary_consumer_unreceived':0,
 'final_reception':'pbs-reload-reception.v1.json','final_manifest':'completion-manifest.v2.json','validation':'validation.v2.json'})
put('progress.json',p)
l=read('reading-ledger.json');l.update({'updated_utc':utc,'named_scoped_interfaces':15,'outer_data_interfaces_unreceived':0,
 'same_context_followup_reception':'pbs-reload-reception.v1.json','personal_external_scope_preserved':'unread-and-boundaries.v2.json','new_contexts_from_followup':0})
put('reading-ledger.json',l)
f=read('forward-mapping.json');f.update({'updated_utc':utc,'status':'PRIMARY_AI_LOCAL_MAPPING_AND_NECESSARY_FINITE_CONSUMER_JOINS_COMPLETE',
 'external_reception':'interfaces.json15scopedreceipts/0necessaryunreceived; pbs-reload-reception.v1.json six manually accepted finite facets; whole foreign domain PASS not granted'})
put('forward-mapping.json',f)
v=read('reverse-mapping.json');v.update({'updated_utc':utc,'status':'PRIMARY_AI_MANUAL_MAPPING_AND_NECESSARY_FINITE_CONSUMER_JOINS_COMPLETE',
 'method':'Original manual72groups273branches/285rows remain. Necessary finite source/data consumers now received in interfaces.json15; foreign whole formal domains/history/native are not granted.'})
put('reverse-mapping.json',v)

review='''COM-AI的固定20R/9formal、65人工源单元196事实、72正式组273分支及285目录行已完成实际全文阅读与双向有限语义核对。15个必要有限接口现已接收，当前必要可得未读0、必要消费者未接收0，交root既定签收。实际审者仍为`/root/com_ai`；本次续审新增context和独立票均为0。

B8为`fd1df570cad987dc3852a3b958f03916e317f7fe`，workspace tree `751dfde81048c81390f89a65ca1d1a565ba8e1ca`、formal tree `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R为`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。29份primary共829654bytes，身份及连续区间保留在identities/reading-ledger；后继报告HEAD不替代冻结输入。

`semantic-units.json`、`forward-mapping.json`和`reverse-mapping.json`保留全部实际手写事实与分支判据；登记/方法计数只是实读后的结构核验。285目录行包括AI37、AE57、BE86、CE59、AB31、R7-U06-SE15，均保留完整输入、局部预期、源判断及未执行资格。额外完整源、跨域原读者和有限scope见supplementary/received-source/received-creature/shared-ab各原台账。

两项提案维持既定有限裁决：GR8-AI-001为required P3，补Conversion现存可直调目标评分定义；普通User0不消费该handler必须保留，不改技能/权重或接线。GR8-AI-002仅optional计数字样，root severity=null。完整合同、非提出者com_facility反证和root既有裁决入口在proposals.json；本次新增candidate/required/optional均0，不新增全史去重声称。

`interfaces.json`的原14项有限接收保持命令/行动集合、Palace/Arena、HandlerHash、Move/Battler/AbilityItem及主动/被动物品各自具体边界。新增第15项`IF-COMAI-DEFAULT-PBS-RELOAD`由`pbs-reload-reception.v1.json`六个完整人工语义facet支持：

- 接收已合格PBS_BATTLE21路径7704记录、PCR11路径2178记录及四代备份6712记录的相关完整作者字段/默认/继承贡献；原实际完整读者及同字节关联资格保留，重叠人口不相加。
- 四代/Shadow备份须显式选择、相容依赖及正常先前步骤；目录存在或MECHANICS_GENERATION不自动活化。Types-only去重、三持物池全缺继承、Mega石OR招式和Encounter谓词/独立reset等精确规则保留。
- Compiler普通启动检查/预删除/诊断与直接compile_all分开；clear、逐记录校验/登记、终检/save及后续输出失败可留前缀，无跨表/全图事务。
- Game.initialize装载当前注册表，普通存档Game.load不重新编译/load_all。Pokemon::Move动态查询、Battle::Move字段快照、AITrainer技能/flags快照及各独立cache分开；直接编译不清全部cache，不刷新全部旧实例。

接收依据是实际读过的完整目标对象/共同前提和原20R/9F消费者审读，根签status/hash本身不授接受。KERNEL/Developer/PCR强制伴件、Mega更正、Compiler1117定位、八个JSON词元/compiled整数区分均同用。本人补读Compiler924–1117完整具名方法、MiscPBSData64、GameStart126、BattleMove201、PokemonMove77及AITrainer/TrainerType原已读区间；前者不称本人Compiler全文。原stdout/stderr/exit/UTC和精确selector在io/REC_*，失败及截断修复独立保留。

`unread-and-boundaries.v2.json`逐一保留原62导航路径的个人/具名阅读处置；必要有限接收完成没有把这些外域个人原文未读或部分读批量改为FULL。原62readset/prompt保留字节，现行disposition禁止按旧缺口再派无限整外域复审。整外国formal域、全6712/7704/2178的本人复读、所有动态插件/代际组合、native/资源/当前宿主状态、全局历史与B8合规结论仍不获本任务批准。

证据为SOURCE_STATIC、具名合格完整贡献接收和原DERIVED_VECTOR。参考业务、独立业务模型、游戏/UI/媒体/native、实际dat与存档保存重载均0次、NOT_EXECUTED。静态字节/JSON/引用校验不计行为执行。请求gpt-6.1-sol/ultra/default普速/Fast关闭；实际model/effort/tier/speed/Fast及opaque平台ID逐字段UNVERIFIED。

唯一写集tasks/com_ai/；未改source/formal/planning/audit/历史，未commit/push、安装或整改。UPDATE_NOT_STARTED。completion-manifest.v2.json给本次最终交付hash；全局整合与既定root签收仍由主审承担。
'''
(base/'review.md').write_text(review)
print(json.dumps({'utc':utc,'interface':packet['interface'],'status':packet['status'],'accepted':15,'necessary_unreceived':0,'facets':len(facts),'captured_read_receipts':len(receipts),'business':'NOT_EXECUTED'},ensure_ascii=False))
