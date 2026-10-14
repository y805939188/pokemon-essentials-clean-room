import json
from pathlib import Path
b=Path(__file__).parent;D='deliverables/final-specification-set/';R='reference/pokemon-essentials/Data/Scripts/011_Battle/';rows=[]
def s(p,a,z):return{'path':R+p,'start':a,'end':z}
B='001_Battle/';T='002_Battler/';O='007_Other battle code/';U='004_Scene/'
w39='combat-requirements/wp39-battle-context-and-participants.md';w40='combat-requirements/wp40-commands-obedience-and-action-order.md';w41='combat-requirements/wp41-switching-positioning-and-escape.md';w42='combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md';w45='combat-requirements/wp45-weather-terrain-side-and-position-effects.md';w48='pokemon-rules/wp48-ability-calculation-modifiers.md';w49='combat-requirements/wp49-ability-phase-triggers.md';w50='pokemon-rules/wp50-held-item-triggers-and-consumption.md';w67='user-interface/wp67-a-battle-interaction-and-presentation.md'
def add(p,a,z,src,reason,status='REPEATED_BOUNDED_CONTRACT_SOURCE_JOIN',owner='R6-C'):
 rows.append({'path':D+p,'start':a,'end':z,'source_units':src,'disposition':status,'responsible_domain':owner,'semantic_assessment':reason,'preconditions':'同主文具名入口/合法参数/依赖正常返回；完整事实含提前拒绝、已写前缀和作用域；不作真实宿主执行保证。','evidence':'SOURCE_STATIC','aggregate_pass':False})
add(w39,294,294,[s(B+'001_Battle.rb',98,116)],'构造空参与队伍前门直接报错；不从个体存活数量推构造空集合。')
add(w39,298,299,[s(B+'002_Battle_StartAndEnd.rb',16,104),s(B+'002_Battle_StartAndEnd.rb',247,350),s(B+'002_Battle_StartAndEnd.rb',519,568)],'人数/多owner尺寸校验与中止/调试100轮后裁定来自不同门，返回0不等完整正常终局。')
add(w40,49,49,[s(B+'002_Battle_StartAndEnd.rb',322,350)],'三阶段与每阶段后的decision截断直接核。')
add(w40,305,314,[s(B+'009_Battle_CommandPhase.rb',5,265),s(B+'006_Battle_ActionUseItem.rb',34,149),s(B+'010_Battle_AttackPhase.rb',16,201),s(T+'007_Battler_UseMove.rb',154,581),s(T+'008_Battler_UseMoveTargeting.rb',5,203)],'重复不变量逐项接主消费者：可出示/退物/先后顺序/续招PP/目标重定向/空槽动作清理，不共享统一执行资格。')
add(w40,318,321,[s(T+'007_Battler_UseMove.rb',154,215),s(T+'007_Battler_UseMove.rb',369,402),s(T+'009_Battler_UseMoveSuccessChecks.rb',10,100)],'前门或无PP早退、身份清理与后段无目标失败分开；choice锁失源自清、特殊与普通记录不等。')
add(w40,322,323,[s(T+'008_Battler_UseMoveTargeting.rb',5,35),s(T+'007_Battler_UseMove.rb',455,500)],'抢夺/反射真实user及旧target清理分支已全读；无目标反射直接empty、实际效果在coater对侧。CM counter-C-P01确认默认效果无额外可见反例，不从结构调用差别升缺陷。')
add(w40,324,324,[s(B+'004_Battle_ActionAttacksPriority.rb',136,279)],'部分排序保持既定平局随机序，TrickRoom反向不覆盖优先级字段。')
add(w40,325,325,[s(B+'002_Battle_StartAndEnd.rb',322,350)],'debug100按时裁定源已核；Palace独立source/results归F。','FRESH_VARIANT_JOIN_RECEIVED','R6-C/R6-F')
add(w40,326,326,[s(T+'007_Battler_UseMove.rb',5,59)],'K新读ShadowOther196–220真实Hyper/obedience绑定与C普通processTurn接合，替换choice清而不执行。','FRESH_EXTERNAL_SHADOW_JOIN_RECEIVED','R6-C/R6-K')
add(w40,327,327,[s(O+'006_Battle_Clauses.rb',11,51),s(O+'006_Battle_Clauses.rb',248,269)],'selfKO平局、爆炸false和suddendeath数字结果不按注释重解释，F工厂设置另审。')
add(w40,336,336,[s(T+'009_Battler_UseMoveSuccessChecks.rb',241,297),s(B+'010_Battle_AttackPhase.rb',102,175),s(O+'008_Battle_AbilityEffects.rb',3030,3058)],'代8分支当前参数已由MainSettings17绑定；各代码guard遵真实entry，不按世代8注释造全部行为。')
add(w40,339,341,[s(T+'009_Battler_UseMoveSuccessChecks.rb',107,182),s(B+'008_Battle_ActionOther.rb',67,134),s(B+'009_Battle_CommandPhase.rb',28,34)],'徽章界/环flag/noMega输入跟caller资格分开；Shadow绑定K所有，不从裸false实现假定无Shadow。')
add(w41,35,42,[s(B+'005_Battle_ActionSwitching.rb',9,112),s(B+'005_Battle_ActionSwitching.rb',142,219),s(B+'001_Battle.rb',602,641),s(B+'007_Battle_ActionRunning.rb',5,159)],'概念与真实move/replace/swap/run类别对应，slot/source关系重映射不等持久个体替换。')
add(w41,177,190,[s(B+'005_Battle_ActionSwitching.rb',206,375),s(T+'008_Battler_UseMoveTargeting.rb',5,203)],'实际执行consumer已全读；Teleport/Pivot/Roar/DragonTail/PartingShot特定producer由CM全量review整合，待其逐族事实接合。','CROSS_DOMAIN_MOVE_PRODUCER_JOIN_PENDING','R6-CM')
add(w41,196,205,[s(B+'005_Battle_ActionSwitching.rb',9,219),s(B+'005_Battle_ActionSwitching.rb',220,468),s(B+'007_Battle_ActionRunning.rb',5,159),s(B+'001_Battle.rb',602,641)],'十项重复规则核：switch+swap区别，rawspeed整数逃率，登记与直接替补分开，真实entry顺序、target关系清单，随机替补和AI最佳不统一。拖出producer补依CM。')
add(w41,209,212,[s(B+'005_Battle_ActionSwitching.rb',9,112),s(B+'005_Battle_ActionSwitching.rb',142,219)],'无后备/duplicate/nonowner/egg/faint各自guard及消息；别名直接call不共享UI按钮门。')
add(w41,213,214,[s(B+'005_Battle_ActionSwitching.rb',206,219)],'末段合法候选negative的core consumer已核；move野生/训练家/substitute/anchor gates等待CM对应族。','CROSS_DOMAIN_MOVE_PRODUCER_JOIN_PENDING','R6-CM')
add(w41,215,217,[s(B+'008_Battle_ActionOther.rb',5,27),s(B+'007_Battle_ActionRunning.rb',5,159),s(B+'009_Battle_CommandPhase.rb',150,265)],'Shiftcentre/size/owner拒和runquery/ordinary/duringBattle门分开，debugCancel-1被命令循环消费。')
add(w41,225,229,[s(B+'005_Battle_ActionSwitching.rb',142,205),s(B+'005_Battle_ActionSwitching.rb',38,90),s(B+'005_Battle_ActionSwitching.rb',394,468)],'实际switchStyle、trap/escape、代差position/hazard消费者，值来源worldprepare O或config，输入存在不即执行成功。')
add(w42,28,31,[s(B+'001_Battle.rb',329,443),s(B+'003_Battle_ExpAndMoveLearning.rb',5,85),s(B+'001_Battle.rb',98,174),s(O+'003_Battle_DamageState.rb',1,61)],'输入/持久和临时层及资格整队集合直接核；伙伴参与集合和玩家普通经验接收区别，不把UI/调用完成当写入同时性。')
add(w42,267,272,[s(B+'003_Battle_ExpAndMoveLearning.rb',5,271),s(B+'011_Battle_EndOfRoundPhase.rb',597,781),s(B+'002_Battle_StartAndEnd.rb',352,516)],'当前配置、五阶段边界、写入前缀、学习取消不回滚与可更新initial实际consumer核；世界Pickup权表/external通知仍O/K。','REPEATED_CORE_CONTRACT_WITH_WORLD_OWNER_BOUNDARY','R6-C/R6-O/R6-K')
add(w45,25,28,[s(O+'002_Battle_ActiveField.rb',1,88),s(O+'001_PBEffects.rb',117,178),s(B+'001_Battle.rb',694,815)],'13/22/9 scopes与default/current/duration语义核，默认-1同时current而非stack；天气/terrain身份目录data由D/O，战斗建立与世界不同。')
add(w49,13,15,[s(T+'001_Battle_Battler.rb',344,455),s(B+'001_Battle.rb',444,504),s(B+'004_Battle_ActionAttacksPriority.rb',264,279),s(B+'011_Battle_EndOfRoundPhase.rb',597,630)],'真实alive集合与speedcache读取非TrickRoom、index与个体重初始化区别；状态真实/视为不统一；触发真假与提交不统一。')
add(w49,260,262,[s(O+'008_Battle_AbilityEffects.rb',299,3208),s(T+'006_Battler_AbilityAndItem.rb',5,211),s(T+'004_Battler_Statuses.rb',219,275),s(T+'005_Battler_StatStages.rb',9,300)],'重复生命期/倍率/概率/消息边界从全处理器及中央query/commit核；代8与abilitySplash为配置前提；不扩大到host。')
add('pokemon-rules/wp38-capture-and-receiving.md',7,7,[s(O+'005_Battle_CatchAndStoreMixin.rb',5,262),s(B+'006_Battle_ActionUseItem.rb',34,59)],'五层标题接各实际consumer，不把menu与capture判定合并。')
add('pokemon-rules/wp38-capture-and-receiving.md',128,130,[],'明确外域/媒体边界；F已完成Safari/Bug完整新review接收，K负责Shadow，C场景完整新读只描述属性与轨道，host无观测。','FRESH_NAMED_SCOPE_BOUNDARY','R6-F/R6-K/R6-C')
add(w48,235,235,[s(O+'008_Battle_AbilityEffects.rb',69,298),s(T+'006_Battler_AbilityAndItem.rb',116,169),s(T+'007_Battler_UseMove.rb',154,215)],'defaultinput/boolean wrapper与查询/奖励/PP提交不同，silent吸收奖励本地边界已有具名事实。')
add('pokemon-rules/wp50-held-item-effect-coverage.md',42,42,[s(O+'009_Battle_ItemEffects.rb',1269,1450),s(O+'009_Battle_ItemEffects.rb',1831,1948)],'同identity多族计数事实，以静态registry exactrows和完整handler读合成，不推196unique物品。')
add('pokemon-rules/wp50-held-item-effect-coverage.md',71,71,[s(O+'009_Battle_ItemEffects.rb',1,217),s(T+'006_Battler_AbilityAndItem.rb',212,476),s(T+'001_Battle_Battler.rb',421,455)],'全script canonicalItemEffects add/copy搜索唯一文件009；32族含两empty，本轮原族core和外registryconsumer均新核；unknownplugins保持scope。')
add(w50,173,173,[s(O+'009_Battle_ItemEffects.rb',218,444)],'HI34–36定位与新全目录核，floatstone实际1/2、active与held量分别，196文字核对另标签。','TEST_CATALOG_CROSS_REFERENCE_NEW_READ')
add(w67,17,26,[s(U+'001_Battle_Scene.rb',79,312),s(U+'003_Scene_ChooseCommands.rb',6,446),s(B+'009_Battle_CommandPhase.rb',5,265),s(U+'004_Scene_PlayAnimations.rb',5,579),s(U+'009_Battle_DebugScene.rb',1,106)],'概念分别核窗/choice/firstAction/cancel/游标/动画block；accept与execute区分，target初选不合法USE可登记例另已有合同；不将未来Scene API设计写入。')
add(w67,325,328,[s(O+'005_Battle_CatchAndStoreMixin.rb',112,150),s(B+'001_Battle.rb',98,174),s(B+'002_Battle_StartAndEnd.rb',16,104),s(U+'003_Scene_ChooseCommands.rb',196,332),s(B+'005_Battle_ActionSwitching.rb',142,219)],'capture空target最早字段失败、构造empty、bagempty和无后备消费者核；Arena自动递增另F完成receipt，正常输入仍依其source。')
add(w67,329,329,[s(B+'003_Battle_ExpAndMoveLearning.rb',229,270),s(U+'003_Scene_ChooseCommands.rb',447,459)],'C已核空槽battle直接learn与满槽forget的前提；摘要详情0槽/空重学首绘由UI primary，不能以C source代审。','CROSS_DOMAIN_SHARED_DETAILS_JOIN_PENDING','R6-UI')
add(w67,330,332,[s(U+'004_Scene_PlayAnimations.rb',412,567),s(B+'003_Battle_ExpAndMoveLearning.rb',229,270),s(U+'001_Battle_Scene.rb',230,266)],'教学取消循环、missingidentity/type/TACKLE动画回退及paused结束标志实际门，normal return与异常处置分开。')
add(w67,333,333,[s(U+'009_Battle_DebugScene.rb',1,106)],'Cdebug替身全读；回放paused转ordinary及自动target例外，F已完成RecordedBattle fullreceipt，仍以其精确source审。','FRESH_VARIANT_JOIN_RECEIVED','R6-C/R6-F')
for q in rows:
 for x in q['source_units']:assert 1<=x['start']<=x['end']<=len(Path(x['path']).read_text().splitlines()),x
(b/'manual-clause-joins.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n'for q in rows));print('manualgroups',len(rows))
