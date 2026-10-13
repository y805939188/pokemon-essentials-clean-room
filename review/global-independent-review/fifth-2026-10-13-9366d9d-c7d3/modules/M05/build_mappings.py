"""Assemble already completed semantic judgments into the requested projections."""
import review_state as s
from pathlib import Path
import json,re
P='deliverables/final-specification-set/'
coverage=s.load('reading-coverage')
log=json.loads((s.ROOT/'shared-review-log.json').read_text())['comparisons']
by_name={Path(x['path']).name:x for x in log}

def src(patterns):
 ret=[]
 for q in coverage['sources']:
  if not any(t in q['path'] for t in patterns):continue
  for seg in q['semantic_segments']:
   a={'path':q['path'],'version':s.R,'lines':seg['lines'],'entry':seg['entries']}
   if 'actual_semantic_line_ranges' in seg:a['actual_semantic_line_ranges']=seg['actual_semantic_line_ranges']
   if a not in ret:ret.append(a)
 return ret
def specpaths(tokens):
 out=[]
 for token in tokens:
  fs=list((s.REPO/'deliverables/final-specification-set').glob('*/'+token+'*.md'))
  for f in fs:
   path=str(f.relative_to(s.REPO));q=next((q for q in log if q['path']==path),None)
   primary=next((x for x in s.load('spec-to-source')['specifications'] if x['path']==path and x.get('kind')=='formal'),None)
   if not q and not primary:continue
   ranges=q['actual_semantic_ranges'] if q else [x['lines'] for x in primary['sections']]
   out.append({'path':path,'version':s.B,'sections':'M05 relevant clauses; exact semantic ranges in spec-to-source.json','reviewed_line_ranges':ranges})
 return out

# One identity per behavioral contract. References to the same capability are projections.
# id,title,status,source patterns,spec tokens,judgment,classification,finding ids
rows=[
 ('player.identity','玩家/训练家身份、语言与资源','supported',['001_Trainer.rb','004_Player.rb','014_TrainerType.rb','017_PlayerMetadata.rb','016_Metadata.rb','001_Utilities.rb','PBS/metadata.txt','PBS/trainer_types.txt'],['wp24'],'姓名/公开与私有身份/外来判断、资源整数校验夹限、literal-true徽章、初始化与PBS默认差异均有合同。','Creature-RPG',[]),
 ('trainer.load-partner','训练家装载、检查、伙伴登记与参战资源','supported',['002_Trainer_LoadAndNew.rb','015_Trainer.rb','001_Overworld_BattleStarting.rb','PBS/trainers.txt'],['wp24','wp39'],'完整训练家字段构建/默认、未知类型与缺资料入口、伙伴ID用于版本读取、参与合并与独立items已承接。','Creature-RPG',[]),
 ('player.profile-resources','角色/装束、训练家卡与逻辑资源选择','supported',['003_Trainer_Sprites.rb','012_UI_TrainerCard.rb','003_Utilities_BattleAudio.rb','017_PlayerMetadata.rb'],['wp24','wp15','wp39'],'登记门、装束/基础图回退、BGM/胜利/捕获三个预置及最后非空候选、卡片持久首次开始时间等业务投影支持；媒体未证。','Engine / Overworld Integration',[]),
 ('party.membership','队伍集合、查询、选员和移除守卫','supported',['001_Trainer.rb','002_Utilities_Pokemon.rb','005_UI_Party.rb'],['wp24','wp25','wp26','wp66-a'],'全体/非蛋/可战集合、资格选择与取消写变量、删除最后可战成员返回false等区分成立；调用方可忽略false，不能加强成原子保证。','Creature-RPG',[]),
 ('party.storage','储存域、地区、盒子和界面业务操作','supported',['004_PokemonStorage.rb','017_UI_PokemonStorage.rb','019_UI_PC.rb','004_Battle_Peers.rb'],['wp25','wp66-b','wp38'],'复制/移动/当前盒/满盒满队、暂持源删除、释放/邮件限制、墙纸读取写回、地区缓存及负下标入口已对照。借用选择器的融合问题只作N002消费者投影。','Creature-RPG',[]),
 ('creature.acquisition','获得、赠送、蛋、外来个体与脚本交换','supported',['002_Utilities_Pokemon.rb','005_UI_Trading.rb','004_UI_Evolution.rb','023_UI_PurifyChamber.rb','002_BugContest.rb'],['wp26','wp25','wp31','wp32'],'六入口容量/昵称/Dex/所有者/治疗区别，交换先统计/演出与进化后最终替换、竞赛/净化消费者有界支持；Demo未知。','Creature-RPG',[]),
 ('item.data','物品内容身份、标志、缺省与可用属性','unresolved',['006_Item.rb','PBS/items','backup/items'],['wp03','wp27','wp28','wp29','wp47-a-attributes','wp47-b-control','wp50-held-item-effect'],'全部物品业务字段和备选差异已审；旗标/路由/价格/消耗大部支持，缺省与ShowQuantity的合同覆盖观察N006保留。literal名字/描述非M05文字准确性审查。','Generic Kernel',['GR5-M05-006']),
 ('inventory.container','背包/PC容器、纯预检与部分执行','supported',['008_PokemonBag.rb','018_UI_ItemStorage.rb','019_UI_PC.rb','016_Metadata.rb'],['wp27','wp66-c'],'全部查询/数量/槽界/replace不合并/999×999PC/惰性播种与存取删加断言、重要整叠区别支持。','Creature-RPG',[]),
 ('inventory.selection-registration','过滤、游标、排序、登记与快捷菜单','supported',['008_PokemonBag.rb','007_UI_Bag.rb','016_UI_ReadyMenu.rb','001_UI_PauseMenu.rb'],['wp27','wp28','wp65','wp66-c'],'过滤与无过滤初始袋/恢复、排序即时保存索引、可登记/图标/登记集合/实际持有候选分层和确认执行返回支持。事件变量适配另N007。','User Interface',[]),
 ('item.active-dispatch','主动处理器、缺失默认、数量与调用分流','supported',['001_Item_Utilities.rb','005_Event_Handlers.rb','007_UI_Bag.rb','005_UI_Party.rb'],['wp28','wp27','wp40'],'全部十家族/直接优先和条件顺序/复制在当时绑定/缺省值、0/1/2和数量初1、真效果才按传入量耗、前缀不回滚逐段支持。','Creature-RPG',[]),
 ('item.battle-consumption','战斗选择、执行、消费身份与退款','supported',['006_Battle_ActionUseItem.rb','003_Item_BattleEffects.rb','009_Battle_CommandPhase.rb','003_Scene_ChooseCommands.rb','002_Battle_StartAndEnd.rb'],['wp28','wp40','wp42','wp67-a'],'登记扣除/业主资源/家族复检差异、Direct5缺效果仍耗、失败退款保身份和同轮终局再退款已有精确合同。','Combat Requirements',[]),
 ('item.field-tools','全部野外主动工具与业务接点','supported',['002_Item_Effects.rb','001_Item_Utilities.rb','005_Overworld_Fishing.rb','004_Overworld_FieldMoves.rb','008_Game_Player.rb'],['wp28','wp12','wp59','wp60-fishing','wp61'],'喷雾/笛/蜜/逃脱绳/三车/三竿/探测仪全部别名/地图/盒等工具分流及次数/不耗/失效但返回真按入口支持。','Engine / Overworld Integration',[]),
 ('item.radar','雷达全生命周期','supported',['005_Item_PokeRadar.rb','003_Overworld_WildEncounters.rb','008_Game_Player.rb'],['wp37','wp24'],'门序/袋预检与实际执行、四环、闪光两次取整、续链与100次改选、八种取消与电量独立支持。','Pokémon Rules',[]),
 ('item.active-healing','主动HP、状态、复活和全部PP效果','supported',['001_Item_Utilities.rb','002_Item_Effects.rb','003_Item_BattleEffects.rb','005_UI_Party.rb'],['wp28','wp20','wp30','wp66-a'],'所有直接/复制/条件治疗身份、两重平衡档、场外/战斗濒死PP资格、单招与全招同步、复活取整、圣灰与友好减量支持。','Pokémon Rules',[]),
 ('item.active.ev','维生素、羽毛与降EV树果','partial',['001_Item_Utilities.rb','002_Item_Effects.rb'],['wp28','wp19','wp30'],'252/510/可选100门、最大量/逐次友好和合并降EV支持；18身份六stat完整对应未承接，N004。','Pokémon Rules',['GR5-M05-004']),
 ('item.active.ability','薄荷、特性道具与糖果','partial',['001_Item_Utilities.rb','002_Item_Effects.rb','001_Pokemon.rb'],['wp28','wp19','wp30','wp21'],'Nature全表足以确定薄荷结果；糖果大小/多份/上限/取消已承接；胶囊/补丁普通/隐藏索引与ZYGARDE精确排除缺口N004。','Pokémon Rules',['GR5-M05-004']),
 ('item.active.battle-stat','战斗增益、X系列、聚气/白雾/逃离','partial',['003_Item_BattleEffects.rb'],['wp28','wp44','wp41'],'全部X别名/固定档/MAXMUSHROOMS/白雾与娃娃等支持；DIREHIT资格阈值1/2/3与赋值2/2/3未精确分列N004。','Combat Requirements',['GR5-M05-004']),
 ('item.learning','机器/导师、通用教学与重学','supported',['001_Item_Utilities.rb','001_Utilities.rb','022_UI_MoveRelearner.rb','005_UI_Party.rb','006_UI_Summary.rb'],['wp28','wp30','wp20','wp66-a'],'TM/HM/TR重要/消耗、入口统计与初始记录差异、PP保留开关、导师movelist注解与执行差别、空重学首次失败等已明列。','Creature-RPG',[]),
 ('item.fusion','形态工具、融合/拆分与借用选员','partial',['002_Item_Effects.rb','005_UI_Party.rb','001_FormHandlers.rb','001_Trainer.rb','017_UI_PokemonStorage.rb'],['wp28','wp21','wp25','wp66-a','wp66-b'],'全部工具/八融合身份普通门及换招参数支持；SPECIAL存放 retained base 后移除最后可战失败仍融合，N002。','Pokémon Rules',['GR5-M05-002']),
 ('creature.held-items','持物、邮件耦合和战斗四份记录','supported',['001_Pokemon.rb','006_Battler_AbilityAndItem.rb','001_Battle_Battler.rb','001_Battle.rb'],['wp20','wp47-b','wp50','wp42'],'当前物/还原/回收/拾取记录、按位置读与写穿/局部id区分，邮件不匹配读取自清有正确主合同；PC调用违反结果另N001。','Creature-RPG',[]),
 ('item.passive-calculation','持物计算及直接战斗查询','supported',['009_Battle_ItemEffects.rb','003_Move_UsageCalculations.rb','001_Battle_Battler.rb','004_Battle_ActionAttacksPriority.rb'],['wp50','wp43','wp40','wp45'],'速度/重量/命中/会心/伤害/经验EV/天气期限全部具体参数及直接查询消费者支持，空族默认不虚构效果。','Combat Requirements',[]),
 ('item.passive-lifecycle','被动物品触发、强制食用与消费','supported',['009_Battle_ItemEffects.rb','006_Battler_AbilityAndItem.rb','007_Battler_UseMove.rb','010_Battler_UseMoveTriggerEffects.rb','011_Battle_EndOfRoundPhase.rb','008_Battle_AbilityEffects.rb'],['wp50','wp49','wp42','wp44','wp45'],'全部32族196登记身份逐体对照；HP阈值/强制/熟成/颊囊/共生/紧张感，Micle反向、Leppa异招PP及当前物重读有合同。','Combat Requirements',[]),
 ('item.move-operations','偷取、交换、回收、移除、强吃和投掷','supported',['011_MoveEffects_Items.rb','008_MoveEffects_MoveAttributes.rb','006_Battler_AbilityAndItem.rb','007_Battler_UseMove.rb'],['wp47-a','wp47-b','wp46','wp50'],'各操作前门/持久性/记录非对称和NaturalGift/Fling空持物异常已明确，全部Fling/NaturalGift默认数据支持。','Combat Requirements',[]),
 ('item.capture-balls','全部球处理器与捕获接收物品投影','supported',['010_Battle_PokeBallEffects.rb','005_Battle_CatchAndStoreMixin.rb','004_Battle_Peers.rb','003_Item_BattleEffects.rb'],['wp38','wp25','wp42'],'四族全部球修正/默认/成功效果、护符和目标/容量门、已扣不退款、伙伴合并集合还原错配已有精确合同；捕获概率整体主责M06。','Pokémon Rules',[]),
 ('mail.transfer','写信、给予、取回、信箱与快照','partial',['006_Item_Mail.rb','019_UI_PC.rb','001_Item_Utilities.rb','005_UI_Party.rb','006_UI_Summary.rb','017_UI_PokemonStorage.rb','001_Pokemon.rb'],['wp64','wp20','wp66-a','wp66-b'],'写信/取回/内容删除/容量/部分提交多数组合支持；信箱Give失败N001、盒中/暂持摘要的player-party索引快照N003。','Creature-RPG',['GR5-M05-001','GR5-M05-003']),
 ('gift.mystery','礼物作者、下载、接收与领取','supported',['024_UI_MysteryGift.rb','003_HTTP_Utilities.rb','004_Player.rb','002_Utilities_Pokemon.rb','008_PokemonBag.rb'],['wp64','wp26','wp27','wp07'],'四元数据、作者唯一/下载重复、取消保存/编码失败、首未领ID、物品预检和个体先变更后获得逐入口支持；未联网。','Creature-RPG',[]),
 ('shop.transactions','金钱和BP买卖/兑换及价格覆盖','supported',['020_UI_PokeMart.rb','021_UI_BattlePointShop.rb','003_Interpreter.rb','006_Item.rb','004_Player.rb'],['wp29','wp27','wp24','wp66-c'],'购买逐份/回退量非槽事务、卖先钱后删/实际增量、BP半价显示全价扣、赠球、原库存删除和退出清覆盖支持。','Creature-RPG',[]),
 ('phone.contacts','电话完整业务与旧兼容入口','supported',['004_Item_Phone.rb','010_UI_Phone.rb','021_PhoneMessage.rb','PBS/phone.txt'],['wp63','wp24','wp77'],'全部注册/隐藏/可见重排/计时/再战/消息替换和18旧入口，类级缺查找/旧参数错位/失败前新增等已有正确合同。','Creature-RPG',[]),
 ('item.field-consumers','野生、繁殖、进化和种植中的物品消费者','supported',['003_Overworld_WildEncounters.rb','007_Overworld_DayCare.rb','007_Evolution.rb','001_FormHandlers.rb','006_Overworld_BerryPlants.rb','007_BerryPlant.rb'],['wp36','wp33','wp34','wp31','wp32','wp21','wp60-berry'],'全部物品相关完整函数/注册已读并按各自主域对照；洁净/护符/遗传/持物进化/四肥料与选择消耗时序支持。','Pokémon Rules',[]),
 ('item.ai','AI道具决策、评级、效用与其它预测消费者','supported',['003_AI_UseItem.rb','008_AI_Utilities.rb','007_AI_MoveEffects_Items.rb','010_AIBattler.rb','011_AIMove.rb','002_AI_Switch.rb','AI_MoveEffects','AI_ChooseMove'],['wp51','wp52'],'主动偏好与实际效果分离，完整基础评级/直接复制条件评级、强食用效用、查封/转移估值与误差、其它持物预测参数支持；非AI整模块全审。','Combat Requirements',[]),
 ('item.facility-replay','设施/模拟/录像与恢复的物品交界','supported',['Challenge_Data.rb','Challenge_EntryRestrictions.rb','Challenge_Battles.rb','ChallengeGenerator','BattlePalaceBattle.rb','RecordedBattle.rb'],['wp54','wp56','wp58','wp76'],'禁物/重复、按位置恢复与异常出口、宫殿只讲究带局部门、回放扣实时包、生成候选/模拟有物评分支持。','Combat Requirements',[]),
 ('inventory.other-consumers','卡片、小游戏奖励与其他资源消费者','supported',['Minigame_TripleTriad.rb','Minigame_Mining.rb','Minigame_SlotMachine.rb','Minigame_VoltorbFlip.rb'],['wp68-triple','wp69-slot-machine','wp69-voltorb-flip','wp70-mining'],'卡仓独立却共用数量助手，card买卖顺序、挖矿逐件发、代币上限/净差或实时奖额区别支持；非小游戏全审。','Creature-RPG',[]),
 ('item.shadow','香、时之笛及净化物品交界','supported',['002_ShadowPokemon_Other.rb','023_UI_PurifyChamber.rb','Shadow Pokémon backup/items_shadow'],['wp23','wp28','wp64'],'全部额外主动注册/心量与友好/Hyper二层门、可选数据无Scent的默认阻断、净化室转移边界已承接。','Pokémon Rules',[]),
 ('item.authoring','物品/训练家数据编辑、写回与转换','partial',['001_EditorScreens.rb','002_Editor_DataTypes.rb','001_Editor_Utilities.rb','003_Editor_Listers.rb','001_GameData.rb','Compiler_CompilePBS.rb','Compiler_WritePBS.rb','Compiler_MapsAndEvents.rb'],['wp73-a','wp03','wp04','wp75','wp24','wp28'],'常规schema/身份/价格/机器/物品池重复/转换读写支持；手写name/lose_text错字段丢文本N005。','Demo / Developer Experience',['GR5-M05-005']),
 ('item.debug','调试资源、成员、持物/邮件与业务直接入口','supported',['Debug_MenuCommands.rb','Debug_PokemonCommands.rb','Debug_BattlePkmnCommands.rb','Debug_Menus.rb'],['wp72','wp73-a','wp24','wp25','wp64'],'已有调试资源/填包填盒/删除绕门/邮件同步与NPC物品编辑具体合同；不执行开发者工具。','Demo / Developer Experience',[]),
 ('item.persistence','玩家/背包/存储持久单元与物品迁移','supported',['Game_SaveValues.rb','Game_SaveConversions.rb'],['wp09','wp10','wp24','wp27'],'仅已读M05登记与背包/笛迁移投影支持，不重签整个保存引导或其它迁移。','Generic Kernel',[]),
 ('item.event-tools','事件物品选择与变量转换工具','partial',['001_Item_Utilities.rb','001_Utilities.rb'],['wp27','wp66-c','wp13-map','wp77'],'底层过滤与游标已给；返回/变量NONE和nil、列表重复/首匹配/转换失败前清空的精确覆盖待裁决N007，源读取已完成。','Demo / Developer Experience',['GR5-M05-007'])
]

extra_sources={
 'player.identity':['005_Pokemon_Owner.rb','001_Pokemon.rb'],
 'trainer.load-partner':['005_Pokemon_Owner.rb','001_Pokemon.rb'],
 'creature.acquisition':['005_Pokemon_Owner.rb','001_Pokemon.rb'],
 'item.radar':['005_Overworld_RoamingPokemon.rb'],
 'player.profile-resources':['007_Item_Sprites.rb'],
 'item.data':['001_Settings.rb','002_BattleSettings.rb'],
 'item.battle-consumption':['010_Battle_AttackPhase.rb'],
 'item.passive-calculation':['001_Battle_Move.rb','005_Move.rb','003_Battle_ExpAndMoveLearning.rb','007_Battle_ActionRunning.rb','008_Battle_ActionOther.rb'],
 'item.passive-lifecycle':['004_Battler_Statuses.rb','003_Battler_ChangeSelf.rb','009_Battler_UseMoveSuccessChecks.rb','002_Battler_Initialize.rb','005_Battle_ActionSwitching.rb'],
 'item.move-operations':['005_MoveEffects_Misc.rb','010_MoveEffects_Healing.rb','002_Move_Usage.rb','013_MoveEffects_SwitchingActing.rb','004_Move_BaseEffects.rb'],
 'item.capture-balls':['001_SafariBattle.rb','002_BugContestBattle.rb','001_SafariZone.rb'],
 'item.fusion':['PBS/pokemon.txt','PBS/pokemon_forms.txt'],
 'item.ai':['001_Battle_AI.rb'],
 'gift.mystery':['013_UI_Load.rb'],
 'item.authoring':['021_Compiler/001_Compiler.rb']
}
rows.append(('item.acquisition','地面道具/普通接收与库存写入','supported',['001_Overworld.rb','024_UI_MysteryGift.rb'],['wp27','wp28','wp64'],'地面拾取/消息接收按直接add返回显示成功或空间不足，不自动补统一预检；大数量可有部分写入。神秘礼物另先预检，二者不合并。','Creature-RPG',[]))
rows=[(i,t,st,sp+extra_sources.get(i,[]),wp+(['wp53'] if i=='item.capture-balls' else ['wp18'] if i in ['player.identity','trainer.load-partner','creature.acquisition'] else []),r,cl,f) for i,t,st,sp,wp,r,cl,f in rows]

d=s.load('source-to-spec');d['capabilities']=[]
for id,title,status,sp,wp,result,cls,findings in rows:
 d['capabilities'].append({'id':id,'title':title,'status':status,'classification':cls,'evidence_level':'supported_static' if status=='supported' else 'static_semantic_review','support_boundary':'Fixed R source and B5 text only; static consumer projections; no reference/model/host/Demo execution.','source_anchors':src(sp),'spec_anchors':specpaths(wp),'comparison_result':result,'shared_contract':id,'related_findings':findings,'in_scope_reading_complete':True})
d['counting_rule']='Unique behavioral capability identities only. Registrations, aliases, data rows, vectors and consumer projections do not increase capability count.'
d['coverage_index_notice']='Entry indexes below locate already manually reviewed bodies. Text search, parsing and count equality are not semantic evidence.'
s.save('source-to-spec',d)

# Bind current shared-contract clauses to bounded source segments actually read.
st=s.load('spec-to-source')
for q in log:
 path=q['path'];ls=(s.REPO/path).read_text().splitlines()
 anchors=src(q['source_patterns'])
 sections=[]
 for a,b in q['actual_semantic_ranges']:
  b=min(b,len(ls));clauses=[]
  for n in range(a,b+1):
   t=ls[n-1]
   if not t.strip() or t.startswith('#') or re.match(r'^\|\s*[-:]+',t) or t.strip() in ['---','```']:continue
   clauses.append({'line':n,'kind':'table_row' if t.startswith('|') else 'clause','spec_text':t,'judgment_reference':q['comparison_result']})
  sections.append({'lines':[a,b],'section':'bounded current contract projection','source_anchors':anchors,'comparison_result':q['comparison_result'],'status':q['status'],'evidence_level':q['evidence_level'],'clauses_and_table_rows':clauses})
 # Main seven specs retain their more precise existing section/row mapping.
 if any('/'+n in path for n in ['wp24-','wp25-','wp26-','wp27-','wp28-','wp29-','wp64-']):continue
 rec={'path':path,'version':s.B,'kind':'shared_contract_projection','line_count':len(ls),'material_availability':'available','sections':sections,'effective_supplements':[],'scope_boundary':q['scope']}
 st['specifications']=[x for x in st['specifications'] if x['path']!=path]+[rec]

# Replace provisional section judgments only with their now completed comparisons.
updates={
 ('wp26',122):'supported_static：竞赛奖品/净化室/捕获与直接获赠边界完成有界caller对照；无统一事务保证。',
 ('wp28',1):'partial：路由支持；身份参数缺口GR5-M05-004，字段缺省覆盖GR5-M05-006。',
 ('wp28',79):'supported_static：全部野外业务caller已补核；钓鱼/地图/Honey按各入口返回与效果分层。',
 ('wp28',123):'supported_static：退款残留→同轮终局/下一命令/失能清理完整链已对照WP40/42。',
 ('wp28',135):'partial：全部直接/复制/条件登记已实审并逐身份索引；参数缺口见GR5-M05-004。',
 ('wp28',221):'partial：通用EV/友好/薄荷/糖果算法支持；stat身份全集及能力药精确条件见GR5-M05-004。',
 ('wp28',309):'partial：世代/数量/消耗已有明确规则；Item缺省与ShowQuantity覆盖观察GR5-M05-006（裁决未定）。',
 ('wp64',79):'supported_static：礼物下载/解析/接收与HTTP真实静态便利包装已对照；未访问远端。'
}
for q in st['specifications']:
 for sec in q['sections']:
  for (prefix,a),value in updates.items():
   if q.get('kind')=='formal' and Path(q['path']).name.startswith(prefix+'-') and sec['lines'][0]==a:sec['comparison_result']=value

# Sources that have completed local counterevidence get a final comparison rather than a stale TODO.
for q in coverage['sources']:
 for seg in q['semantic_segments']:
  seg['source_review_complete_for_range']=True
  linked=[x['id'] for x in d['capabilities'] if any(a['path']==q['path'] and a['lines']==seg['lines'] for a in x['source_anchors'])]
  seg['capability_ids']=linked
  old=seg['comparison_result']
  if any(t in old for t in ['待','pending','反查中','线索','补全逐条','主责']) or (old.startswith('context_only') and linked):
   seg['preliminary_comparison']=old
   seg['comparison_result']='静态源段比较完成；最终判断见所列唯一能力记录（含partial/unresolved），不继承初读pending或历史PASS。'
  if not linked:seg['comparison_result']='context_only：已读以界定M05调用边界，不作该外模块完整支持结论。'
s.save('reading-coverage',coverage)
s.save('spec-to-source',st)

# Interface identity is the same as the capability identity, with producer/consumer projections.
it=s.load('shared-interfaces');it['contracts']=[]
for c in d['capabilities']:
 it['contracts'].append({'id':c['id'],'title':c['title'],'classification':c['classification'],'status':c['status'],'evidence_level':c['evidence_level'],'support_boundary':c['support_boundary'],'rule_owners':[a['path'] for a in c['spec_anchors']],'producer_and_consumer_anchors':c['source_anchors'],'comparison_result':c['comparison_result'],'related_findings':c['related_findings'],'unique_capability_identity':c['id'],'ownership_boundary':'M05 owns assigned player/item business; shared module clauses are consumer projections only. M06 capture/growth and M10 rendering/input retain their independent review ownership.','execution_status':'not_executed'})
it['identity_aliases']={'mail.snapshot':'mail.transfer','held-item.give':'mail.transfer','trainer.authoring':'item.authoring','M05.player.identity':'player.identity','M05.trainer.load':'trainer.load-partner','M05.bag.choose-cursors':'inventory.selection-registration'}
it['counting_rule']=d['counting_rule']
s.save('shared-interfaces',it)
