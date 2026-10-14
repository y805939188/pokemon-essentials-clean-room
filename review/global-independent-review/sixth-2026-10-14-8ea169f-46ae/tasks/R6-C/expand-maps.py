import json
from pathlib import Path
root=Path(__file__).parent; source='reference/pokemon-essentials/Data/Scripts/011_Battle/';formal='deliverables/final-specification-set/'
wp={'45':'combat-requirements/wp45-weather-terrain-side-and-position-effects.md','48':'pokemon-rules/wp48-ability-calculation-modifiers.md','49':'combat-requirements/wp49-ability-phase-triggers.md','50':'pokemon-rules/wp50-held-item-triggers-and-consumption.md','67':'user-interface/wp67-a-battle-interaction-and-presentation.md'}
data=[]
def add(p,a,z,u,f,w,x,y,q='SOURCE_MATCH_BOUNDED'):
 data.append({'source':{'path':source+p,'start':a,'end':z},'unit':u,'fact':f,'consumer':{'path':formal+wp[w],'start':x,'end':y,'clause':u},'preconditions':'固定快照有效输入；具名入口实际守卫及依赖正常返回；未保证其它入口相同。','evidence':'SOURCE_STATIC','disposition':'MAPPED_NEW_READ','qualification':q,'aggregate_pass':False})
B='001_Battle/';T='002_Battler/';S='004_Scene/';O='007_Other battle code/'
add(O+'001_PBEffects.rb',1,178,'有界效果标识库存','117个人/9位置/22side/13field标识；审计身份不要求未来复制数字表示。','45',102,145)
add(B+'005_Battle_ActionSwitching.rb',425,468,'入场危害','boots门→rock→spikes→poison spikes吸收/毒→web，伤害和倒下时点阻后段。','45',178,191)
add(B+'005_Battle_ActionSwitching.rb',394,424,'位置治愈/新月舞','位置旗在可恢复/状态/PP与当前代判断后清；替换不自动丢位置旗。','45',199,203)
add(B+'011_Battle_EndOfRoundPhase.rb',120,133,'Wish位置期限','positive递减到0后，当前成员canHeal才恢复保存量与消息。','45',195,197)
add(B+'011_Battle_EndOfRoundPhase.rb',78,118,'延迟攻击消费','原source未在场可用临时dummy；special与当前天气执行后复原，非ordinaryPP保证。','45',205,211)
add(B+'001_Battle.rb',602,641,'Shift位置效果','交换battler/choice/sprite及索引指向，position效果保持。','45',213,217)
add(T+'001_Battle_Battler.rb',344,455,'能力/物品有效性','abilityfaint/GastroAcid/gas/unstoppable；itemfaint/Klutz/embargo/room/corrosion，当前身份与unlosable分开。','48',11,34)
add(T+'001_Battle_Battler.rb',248,292,'速度/重量管线','阶级→能力/物品→侧/状态/徽章→round+min1；重量先临时值后能力物品，单位0.1kg。','48',36,54)
add(T+'006_Battler_AbilityAndItem.rb',116,169,'免疫奖励helper','silent查询不写stat/HP奖励；提示和提交资格分别读取，真实入口source/target门保留。','48',169,177)
add(T+'006_Battler_AbilityAndItem.rb',5,211,'生命周期核心','switch/faint/gasend/trace/cure/gainloss有不同存活/忽略门；gain入场标志false。','49',19,41)
add(T+'010_Battler_UseMoveTriggerEffects.rb',5,86,'每击消费者','contact/ability/item条件与顺序；倒下不总skip受击，替身和本体门分开。','49',126,155)
add(T+'010_Battler_UseMoveTriggerEffects.rb',87,176,'招后第一段','DestinyBond、能力/useritem/targetitem/forceSwitch顺序，侧全灭跳boost不等跳全部。','49',157,169)
add(T+'010_Battler_UseMoveTriggerEffects.rb',177,207,'招后第二段','有效SheerForce附效门可skipBerserk等，第三段不沿用统一skip。','49',171,181)
add(T+'007_Battler_UseMove.rb',541,581,'舞者消费','收集快到慢而反向使用；先暴走+1后资格，拒绝未到恢复分支；dancerflag防递归。','49',219,223)
add(T+'003_Battler_ChangeSelf.rb',156,296,'形态直接生命周期','状态/moves/weather/endround形态检查独立；实际变形提交而非真实像素观察。','49',225,246)
add(T+'006_Battler_AbilityAndItem.rb',212,296,'消耗/共生','berry/pinch门；remove/consume记录recycle/initial/Belch/Pickup再symbiosis；外来物品ownitem分开。','50',13,31)
add(T+'006_Battler_AbilityAndItem.rb',297,476,'持物分族调用','hp/status/endmove/stat/terrain/drop/forced/EOR各alive与命中门；handler成功才消费后置。','50',13,31)
add(O+'009_Battle_ItemEffects.rb',218,259,'速度重量物品','ChoiceScarf/Macho/iron/quickpowder倍率门；FloatStone重量，管线最后round。','50',35,53)
add(O+'009_Battle_ItemEffects.rb',631,721,'priority/accuracy物品','QuickClaw/Custap门，Lagging；BlunderPolicy miss与Zoom/Wide/Micle命中，标记与消费分开。','50',35,53)
add(O+'009_Battle_ItemEffects.rb',722,1268,'damage/critical物品','userpower/attack/final、targetdefense/resistberry与会心；gem先标后消费，targetcritical空族默认。','50',55,70)
add(O+'009_Battle_ItemEffects.rb',260,630,'HP/状态治愈持物','HP/Ripen/随机星桃/性格果；MentalHerb清timer留identity；EjectPack先consume后select。','50',72,92,'C002_LOCAL_FACT_CORRECT_CONSUMER_JOIN')
add(O+'009_Battle_ItemEffects.rb',1269,1575,'每击与target招后物品','contact/SheerForce/击中等守卫，Jabo回血和续击identity、Eject/RedCard选择/消费/anchor后门。','50',94,121)
add(T+'010_Battler_UseMoveTriggerEffects.rb',5,86,'反伤与续击消费者','每击反伤后自动治疗/共生可换物；续击读当前identity/HP，非统一快照。','50',113,121)
add(O+'009_Battle_ItemEffects.rb',1576,1692,'招后持物与PP','LifeOrb/ShellBell/ThroatSpray；Leppa写持久槽再同步战斗槽；WhiteHerb与强制消费独立。','50',123,130)
add(O+'009_Battle_ItemEffects.rb',1693,1948,'场域成长EOR持物','Exp/EV、weather/terrain/seeds、EORheal/orbs/shedshell/roomservice/Intimidate/escape分族。','50',132,149)
add(T+'001_Battle_Battler.rb',421,455,'物品保护查询','有效性与species/form不可丢失门分开，显式消耗不总查询unlosable。','50',151,167)
add(S+'002_Scene_Initialize.rb',1,191,'构造与资源','sprite/window初始化、背景/平台fallback、wild可见和trainerframes；资源缺失保留宿主scope。','67',30,58)
add(S+'003_Scene_ChooseCommands.rb',6,140,'命令/战斗输入','四格游标保存与wrap、run/cancel/Call模式，Mega/Shift及PP显示。','67',60,87)
add(S+'005_Battle_Scene_Menus.rb',1,551,'菜单呈现消费者','图形/文字command/fight/target，nil/empty姓名、near许可/高亮、PP颜色/Mega状态；登记另由选择单位。','67',60,130)
add(S+'003_Scene_ChooseCommands.rb',196,332,'背包UI','Bag游标保留、battleUse效果门、party/moves/ball目标；取消不登记，消费在上层。','67',134,162)
add(S+'003_Scene_ChooseCommands.rb',141,195,'PartyUI','显示序与实际party索引转换；lax/cancel模式，选择与替补/接收上层区别。','67',166,189)
add(S+'003_Scene_ChooseCommands.rb',447,474,'学招/命名/图鉴UI','forget返回槽、name返回text、species图鉴入口；业务提交由上游。','67',193,207)
add(S+'004_Scene_PlayAnimations.rb',221,312,'HP/EXP/升级UI','逐目标damage/HP表现集合与等待；EXP框结束后等级窗口。','67',193,207)
add(S+'004_Scene_PlayAnimations.rb',331,389,'CaptureUI','shake/critical与result，成功ME3.5秒、hide1秒；trainer挡球独立动画。','67',211,232)
add(S+'001_Battle_Scene.rb',169,312,'消息确认','ordinary/brief/paused等待输入各异；defaultcancel负值不能Back。','67',236,242)
add(S+'006_Battle_Scene_Objects.rb',1,413,'DataBox时序','HP/EXP按uptime、bar整数阈值和图标；EXPflashRGBA64/200/248/192，未观测像素。','67',244,252,'STATIC_PROPERTIES_ONLY_FLASH_WORDING_UI_REVIEW_PENDING')
add(S+'006_Battle_Scene_Objects.rb',418,698,'Sprite/Abilitybar','个体species/form/shadowmetrics定位、底origin与bob/flash；目标高亮和能力条侧身份。','67',244,262)
add(S+'004_Scene_PlayAnimations.rb',5,220,'开场/发送/召回','blocking与queue、每发送completion、能力条show/hide/replace。','67',254,262)
add(S+'008_Battle_Scene_Animations.rb',1,849,'硬编码动画','intro/lineup/sendout/recall/faint/shake/deflect轨道和临时资源寿命，完成与UI恢复依赖。','67',254,262)
add(S+'007_Battle_Scene_BaseAnimation.rb',1,823,'轨道/球burst','全轨结束下一update才done；临时资源处置，装饰随机不决定捕获。','67',254,270)
add(S+'004_Scene_PlayAnimations.rb',390,579,'招式动画查找播放','身份左右查找→类型类别默认→TACKLE回退；commonmissing返回；变换/影子复原在正常返回。','67',264,298)
add(O+'007_BattleAnimationPlayer.rb',1,844,'数据库动画播放','实际播放elapsed20fps、路径变换/SE/flash/sprite复原；数据属性不当像素声音观测。','67',264,298)
add(S+'009_Battle_DebugScene.rb',1,106,'Debug替身','无视觉固定/随机返回与拼写query异常；非ordinary真实UI验证。','67',300,313)
# Validate every range before mutating maps; previous interrupted append's complete prefix is retained.
for r in data:
 for k in ['source','consumer']:
  q=r[k];n=len(Path(q['path']).read_text().splitlines());assert 1<=q['start']<=q['end']<=n,(q,n)
existing=[json.loads(x)for x in(root/'forward-map.jsonl').read_text().splitlines()]
assert not any(r['unit']=='有界效果标识库存'for r in existing),'already expanded'
for i,r in enumerate(data,start=len(existing)+1):r['fact_id']=f'R6-C-F{i:03d}'
with(root/'forward-map.jsonl').open('a')as f,(root/'reverse-map.jsonl').open('a')as g:
 for r in data:
  f.write(json.dumps(r,ensure_ascii=False)+'\n');g.write(json.dumps({'clause':r['consumer'],'source':r['source'],'fact_id':r['fact_id'],'preconditions':r['preconditions'],'verification':r['qualification'],'evidence':'SOURCE_STATIC','aggregate_pass':False},ensure_ascii=False)+'\n')
print('Added',len(data),'facts; exact ranges validated; no blanketPASS')
