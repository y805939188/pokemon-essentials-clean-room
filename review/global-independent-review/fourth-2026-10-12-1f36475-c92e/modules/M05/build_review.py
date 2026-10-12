from pathlib import Path
import json, subprocess, re
from datetime import datetime, timezone
ROOT=Path.cwd()
OUT=ROOT/'review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/M05'
REF=Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
B='1f36475d22120a0d1175967d5b17d71fe8311d88'
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BASE={'commit':B,'tree':'d696e23ce4a0eae12b0bb2a5e74bf9cd4c74764a','identity_navigation':'delivery/2026-10-12/formal-identities.json'}
RBASE={'commit':R,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','root':str(REF),'readiness':'PARTIAL_READY (共享 baseline.json；未重核整仓)'}
REVIEWER={'module':'M05','thread_id':'01a12fdc-b1dc-7f62-8311-aa6a002b9432','pid':64300,'role':'由父会话启动的独立 CLI 审者','parent_thread_id':'01a12fc2-e8c0-7e43-a721-ccfe659d75c8','identity_source':'../../tasks/M05-launch.json','requested_model':'gpt-6-astra','requested_reasoning_effort':'ultra','requested_service_tier':'default','fast':False,'actual_echo':'UNVERIFIED'}
S={
 'trainer':'Data/Scripts/015_Trainers and player/001_Trainer.rb',
 'loadtrainer':'Data/Scripts/015_Trainers and player/002_Trainer_LoadAndNew.rb',
 'player':'Data/Scripts/015_Trainers and player/004_Player.rb',
 'dex':'Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb',
 'trainerdata':'Data/Scripts/010_Data/002_PBS data/015_Trainer.rb',
 'playermeta':'Data/Scripts/010_Data/002_PBS data/017_PlayerMetadata.rb',
 'mapmeta':'Data/Scripts/010_Data/002_PBS data/018_MapMetadata.rb',
 'itemdata':'Data/Scripts/010_Data/002_PBS data/006_Item.rb',
 'storage':'Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb',
 'pkmn':'Data/Scripts/014_Pokemon/001_Pokemon.rb',
 'acq':'Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb',
 'util':'Data/Scripts/019_Utilities/001_Utilities.rb',
 'world':'Data/Scripts/012_Overworld/001_Overworld.rb',
 'battle_start':'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',
 'field':'Data/Scripts/012_Overworld/004_Overworld_FieldMoves.rb',
 'bag':'Data/Scripts/013_Items/008_PokemonBag.rb',
 'itemutil':'Data/Scripts/013_Items/001_Item_Utilities.rb',
 'effects':'Data/Scripts/013_Items/002_Item_Effects.rb',
 'battleeffects':'Data/Scripts/013_Items/003_Item_BattleEffects.rb',
 'mail':'Data/Scripts/013_Items/006_Item_Mail.rb',
 'shadow':'Data/Scripts/014_Pokemon/001_Pokemon-related/002_ShadowPokemon_Other.rb',
 'trade':'Data/Scripts/016_UI/001_Non-interactive UI/005_UI_Trading.rb',
 'partyui':'Data/Scripts/016_UI/005_UI_Party.rb',
 'bagui':'Data/Scripts/016_UI/007_UI_Bag.rb',
 'storageui':'Data/Scripts/016_UI/017_UI_PokemonStorage.rb',
 'pc':'Data/Scripts/016_UI/019_UI_PC.rb',
 'mart':'Data/Scripts/016_UI/020_UI_PokeMart.rb',
 'bp':'Data/Scripts/016_UI/021_UI_BattlePointShop.rb',
 'gift':'Data/Scripts/016_UI/024_UI_MysteryGift.rb',
 'ready':'Data/Scripts/016_UI/016_UI_ReadyMenu.rb',
 'loadui':'Data/Scripts/016_UI/013_UI_Load.rb',
 'playerworld':'Data/Scripts/004_Game classes/008_Game_Player.rb',
 'interpreter':'Data/Scripts/003_Game processing/003_Interpreter.rb',
 'battleuse':'Data/Scripts/011_Battle/001_Battle/006_Battle_ActionUseItem.rb',
 'command':'Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb',
 'choose':'Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb',
 'end':'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb',
 'settings':'Data/Scripts/001_Settings.rb',
 'save':'Data/Scripts/002_Save data/004_Game_SaveValues.rb',
}
F='deliverables/final-specification-set/'
P={k:F+'creature-rpg/'+v for k,v in {
 '24':'wp24-player-trainers-partners.md','25':'wp25-party-and-storage.md','26':'wp26-acquisition-gifts-and-script-trade.md','27':'wp27-bag-and-item-storage.md','28':'wp28-item-use-and-training.md','29':'wp29-shops-and-exchanges.md','64':'wp64-mail-and-mystery-gift.md','18':'wp18-creature-identity-species-ownership.md','20':'wp20-hp-status-moves-helditem.md'}.items()}
P.update({'t1':F+'test-catalog/creature-rpg-wp18-20-24-25-26.md','t2':F+'test-catalog/creature-rpg-wp27-28-29-30-33.md','t3':F+'test-catalog/creature-rpg-wp35-36-57-64-68.md','40':F+'combat-requirements/wp40-commands-obedience-and-action-order.md','42':F+'combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md','51':F+'combat-requirements/wp51-ai-action-selection-and-skill.md','50':F+'pokemon-rules/wp50-held-item-triggers-and-consumption.md','67b':F+'user-interface/wp67-b-lifecycle-presentations-and-history.md','67a':F+'user-interface/wp67-a-battle-interaction-and-presentation.md','13':F+'engine-overworld/wp13-map-events-npc-followers.md','scope':F+'scope-statement.md'})
def src(key,loc,fact):return {'path':S.get(key,key),'commit':R,'lines_or_symbol':loc,'fact':fact}
def spec(key,loc,fact):return {'path':P.get(key,key),'commit':B,'lines_or_symbol':loc,'fact':fact}
def write(name,obj): (OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
caps=[]
def cap(desc,ss,ps,entry,branches,limits,notchecked,status='supported',findings=None,history=None,owner='M05',classification=None,reason=None):
 n=len(caps)+1
 caps.append({'capability_id':f'GR4-CAP-M05-{n:03d}','module':'M05','description':desc,'source_anchors':ss,'spec_anchors':ps,'entry_and_preconditions':entry,'configuration_data_host_limits':limits,'reviewer':REVIEWER,'checked_branches_boundaries':branches,'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],'execution_status':'NOT_EXECUTED','material_availability':{'source':'available_read_only','formal':'available_fixed_baseline','host_demo':'not_available_as_complete_runnable_game'},'status':status,'reason':reason or 'supported 仅表示本项所列分支的 supported_static；不表示全文件、全部组合或运行通过。','related_findings':findings or [],'history_links':history or [],'not_checked':notchecked,'primary_owner':owner,'projection':'本域主责' if owner=='M05' else 'M05 的直接消费/回归投影；不代主域全审','classification':classification or ['Creature-RPG']})
cap('训练家标识、玩家资源域及许可初态',
 [src('trainer','18–39,169–175','名字标记与标识双半；外来 ID 排除自身。'),src('player','38–107','资源初值、四类整数写入钳位、布尔徽章计数。'),src('settings','49–55','四种资源上限。'),src('PBS/metadata.txt','[0],4–7','初始金钱 3000，初始 PC 道具 POTION，仓库制作者身份。')],
 [spec('24','§3.1–3.2/§4.1–4.3','标识、资源及许可消费者。'),spec('t1','PT-01/02','负金钱钳0与非法 soot 类型。')],
 '有效训练家类型/玩家；只比较资源写入入口，不把初始元数据写入当成同一校验入口。',
 ['普通整数写入；money=-5→0；coins 超上限→99999；soot 字符串拒绝；功能标记初始 false。'],
 '金钱/BP/coins/soot 上限可配置；宿主语言仅定位调用，未读真实系统语言。',['战斗奖惩金钱整链、徽章/许可的真实事件写入、初始化非法元数据。'])
cap('玩家元数据按编号回退与字符集后备链',
 [src('playermeta','43–87','缺编号回退1；行走/奔跑/骑行/水上等逐级后备。'),src('player','60–74','直写先提交再刷新；训练家类型取元数据。'),src('PBS/metadata.txt','[1],15–23','具名玩家各动作资源键。')],
 [spec('24','§3.2–3.3','回退、原编号保存及资源链。'),spec('t1','PT-04/05','未登记编号与原始直写边界。')],
 '元数据1有效，查询编号99；直接字段变化在地图角色可为空时。',['99未登记→内容取1；同值字段早退；缺动作资源字段按链式后备。'],
 '资源键可得，图像实际缺失；这里只审内容选择，不签显示结果。',['初始命名系统用户名、包装切换的全部事件调用、套装媒体。'])
cap('NPC 训练家装载、缺失与默认个体数据',
 [src('loadtrainer','4–10,70–123','类型未知报错/记录缺失空；调试和非调试检查分离。'),src('trainerdata','115–177','按类型/名称/版本生成、外来ID、条目字段与默认IV/EV。')],
 [spec('24','§5.1–5.3/§8','装载、检查和编辑分层。'),spec('18','§5.3表 NPC训练家队伍,197','默认IV/EV与个体字段覆盖。'),spec('t1','PT-17/18/32/33','未知类型、名字替换与调试拒绝。')],
 '已登记类型，存在或缺失指定版本；正常扩展点不额外修改。',['记录不存在空返回；非调试检查直接放行；调试拒新增后 false；默认招式与显式招式分支。'],
 'PBS/trainers.txt 与 trainer_types.txt 可读，但本次未遍历全部训练家配置。',['所有NPC变体、调试创建写盘/编译、Shadow生成全部覆盖次序。'])
cap('伙伴注册、参与谓词及战后资源清理',
 [src('world','637–651','取消载具在装载前；存身份ID而非版本；注销单槽。'),src('battle_start','125–201,306–328','伙伴参与次序、按存储ID再查道具、战后治疗。')],
 [spec('24','§6.1–6.3','准确区分初始版本与再查ID；独立 can_lose 门。'),spec('t1','PT-19–28','参与、注册部分失败和清理。')],
 '有效世界和伙伴记录；讨论普通战斗创建/正常返回。',['未知类型时未取消载具；类型合法记录缺失时已取消载具；敌方>1先于显式单打；noPartner先拒；有伙伴但未参与仍触治疗。'],
 '载具具体清理依 WP12；随机ID再查可能命中另一版本。',['设施/竞赛/漫游/雷达组合、战后中断、真实伙伴事件。'],classification=['Creature-RPG','Combat Requirements'])
cap('队伍过滤、移除和最后可用成员',
 [src('trainer','57–164','非蛋、可战斗两口径；按索引移除要求另有可用者。')],
 [spec('24','§3.1','队伍查询归属。'),spec('25','§4.1/§5','成员删除与界面守卫分离。')],
 '合法紧凑队伍，成员含蛋/濒死/存活者。',['非蛋HP0计 pokemon_count 不计 able_count；移除唯一可用者失败；越界索引拒绝；有其它可用者则删除。'],
 'MAX_PARTY_SIZE=6；不把界面最后成员守卫扩大到全部容器直写。',['稀疏或非法队伍对象；训练家各查询全部组合。'])
cap('基础盒容器同对象搬运、容量及存入治疗',
 [src('storage','4–77,120–263','容量随数组长度；复制同引用；入队追加；存储先当前盒再全盒。'),src('settings','220–225','6人/40盒/存入治疗世代门。')],
 [spec('25','§3.1–3.2/§4.1/§6–8','容器不变量与失败时先治疗。'),spec('t1','PS-01–13/23–24/29–31/37–38','有区分力的容器向量。')],
 '合法来源个体；基础储存；明确治疗配置；无回调改容量。',['队伍[A]显式目标0或5都追加B；盒目标可覆盖；删除队伍压缩、盒留空；clear长度0且空/满都真；当前盒满时从盒0扫描；全满且治疗开先治再返回-1。'],
 '默认40×30，治疗当前代8关、7及以前开。',['UI演出中断、任意负盒号/非法索引、所有自定义容量组合。'])
cap('仓库 UI 的拿起、存入、放下、交换及释放守卫',
 [src('storageui','1705–1879','最后成员/邮件/不可存放/不可释放守卫按入口不同；释放默认否。'),src('pc','163–205（菜单守卫）','PC存入与整理入口分离。')],
 [spec('25','§4.2/§5','按目标和是否持有分层。'),spec('t1','PS-15–22','蛋、邮件、队伍空格与持有位对照。')],
 '正常仓库UI操作；初始仅1可用A另有蛋B；无宿主故障。',['整理模式存B不触最后可用守卫；PC存入入口另按整队拦截；带邮件持有者可放回队伍空格但不可放盒；释放蛋/邮件/禁止释放者拒绝。'],
 '源逻辑可得、Graphics/Audio缺；同引用搬运按容器规则。',['墙纸读取兼容/资源、拖拽动画、全部输入竞争；UI主域全覆盖。'])
cap('地区储存的缓存、可得性与代理异常',
 [src('storage','269–288,291–369','按地图缓存地区；地区移动只复制；删除/墙纸代理异常。'),src('util','380–384','地图位置首分量，无值默认-1。'),src('save','pokemon_storage new_game_value (101)','默认创建基础储存。')],
 [spec('25','§3.3/§8','明确不是默认启用且代理并非等价。'),spec('t1','PS-25–27','同引用双位、删除失败及缺地区。')],
 '显式使用地区储存的合法静态调用；不声称普通UI已经启用。',['同图使用缓存；换图才重解；无地图/地区拒绝；地区移动保留源，基础移动删源。'],
 '所有脚本检索未定位默认实例化；动态/插件使用未知。',['地区化真实地图与UI组合、失败后的外层恢复。'])
cap('普通/静默/仅入队/外来/蛋的获得入口',
 [src('acq','4–175','容量预检、命名/图鉴/初始招式写入及队伍/盒分派。')],
 [spec('26','§3.1–3.3/§7','入口差异和多次容量复检。'),spec('t1','AQ-01–18/31–36','获得正常、满队、全满、昵称和缺省等级。')],
 '已有合法普通个体或明确合法物种/等级；图鉴与基础储存存在。',['初始满队但盒有位普通赠送入盒、外来/仅队伍拒；全满在构造前拒；静默仅入队无显式seen调用；拒命名保留昵称，进入输入再空文清昵称；外来空昵称参数不改原名。'],
 '图鉴登记内部与构造形态例外只作为共享条款，不全审；存入治疗代际承接。',['事件等待改容量的实际可达性、蛋创建形态全链、捕获/竞赛/寄养/净化消费者全审。'])
cap('脚本交换准备、演出后替换及选择器',
 [src('trade','27–54,157–211,217–243','先统计与拥有者/首招；图鉴在前、最终队伍替换在后。'),src('partyui','1172–1201,1534–1559','默认交换选择器筛选与变量输出；allowIneligible为另一个工具输入。')],
 [spec('26','§4/§7','实例与物种输入、无回滚及选择器。'),spec('67b','§3.3/§5','新图鉴条件页两处收尾，宿主重复释放未证。'),spec('t1','AQ-19–27','正常替换和非法输入统计已写。')],
 '使用默认物种交换包装；另传已有合法个体；演出正常返回。',['新物种沿旧成员等级，实例保留招式；未登记物种报错但计数已+1；最终同队伍槽替换；有图鉴条件页的重复收尾已被共享条款承接。'],
 '脚本交换调用者地图事件缺失；宿主重复释放结果未知。',['自定义连续交换进化、允许不合格选择工具变体、演出资源和时序。'])
cap('背包与共享容器的部分写入/全有全无及替换',
 [src('bag','19–164,237–301','无限口袋单次长度+1扫描；add/remove可部分；all入口预检；替换不跨袋。'),src('world','656–749','拾取/收到/奖品均直接add，提示差异。')],
 [spec('27','§3/§7','预检和执行分离、三个接收消费者。'),spec('t2','BG-01–16','1500空袋对照与跨槽删除。')],
 '合法道具、默认空无限口袋或具名有限容量；正常元数据。',['空袋1500预检false不写、直接add存999后false、add_all不写；总数5删10返回false并清空；replace跨口袋参数不搬迁；clear保留登记和最后口袋。'],
 '每槽999；自动排序只在成功添加后。',['所有槽排列/空洞及未知复杂插件容器、迁移实际数据。'])
cap('PC 道具存取、数量选择与懒初始化',
 [src('bag','170–229','999槽×999，元数据初始物品；严格道具查询。'),src('bagui','604–702','先接收方预检、删源再加目标；重要物品整叠但显示1。'),src('pc','4–53','懒创建与空态。')],
 [spec('27','§4','固定容器与UI数值分流。'),spec('t2','BG-14/17–21','PC种子/容量拒绝/重要物品。')],
 'PC或背包正常选择，数量来自当前库存；接收方预检稳定。',['POTION种子只在有效数据下加入；预检失败不删源；重要物品多份不弹数量并整叠搬运；PC丢弃重要物品拒。'],
 '默认数据POTION，未运行序列化/存档或窗口。',['多键竞争完整比较、异常回调改变库存、真实PC事件。'])
cap('快捷登记、候选过滤与游标恢复',
 [src('bag','138–156','直接登记只验证ID且去重。'),src('bagui','479–542,590–600','登记菜单与给予非蛋门，过滤选择恢复游标。'),src('ready','287–329','快捷收集只看持有，确认只在快捷路径。')],
 [spec('27','§4.3/§5','登记三层、过滤游标和仅蛋/濒死非蛋对照。'),spec('t2','BG-22–31','直接登记无处理器、用尽保留登记、给予菜单。')],
 '合法物品与有效背包；正常返回过滤选择。',['合法无处理器物品可直接登记；未持有不进快捷，持有后可进；普通无图标不等于无登记；仅蛋无Give，增加濒死非蛋则有Give。'],
 '快捷按键完整宿主映射未审；注册身份与场景消费分开。',['全部隐藏招式资格、排序/输入竞争、异常时游标恢复。'])
cap('装备给予、取回与邮件取消后的库存状态',
 [src('itemutil','781–853','普通持物回包/替换；邮件先取、容量门和取消部分提交。'),src('mail','20–32,100–125','信箱转移与写信返回。')],
 [spec('64','§3.2–3.3','背包容量先于信箱询问；取消造成普通X入包保留。'),spec('t3','MG-04–08','存信箱/满/销毁/写信取消。')],
 '合法可持道具X和邮件M，成员非蛋；背包容量已明确，消息正常返回。',['普通取回先预检袋；给蛋拒；已持X改给M后取消写信：成员仍X、M回袋、袋X净+1；先存旧信箱后取消新邮件不回滚。'],
 '保留参考异常事实，不决定未来是否修正。',['Box Link持物快照完整连续链（仅导航第三轮M10）、全部持物/战斗消耗效果。'])
cap('主动道具的四入口、返回值与库存扣减时点',
 [src('itemutil','16–126,644–776','数量门、回退处理器、最后路径返回、非战斗成功才扣、直接工具无库存守卫。'),src('itemdata','171–198','TM/HM/Key重要不消费，TR属性控制。')],
 [spec('28','§3.1–3.4/§6–7','入口分流、野外0/1/-1和消费。'),spec('t2','IU-40–43','仅蛋、用过再取消、直接库存0。')],
 '合法默认道具；无未知插件处理器；需要时队伍含非蛋。',['成功使用一份再取消返回0而已扣仍保留；Direct无背包handler可落野外；返回2只关袋；野外效果false不自动补通用失败消息；库存0直接调用不单独拒。'],
 '一次多量配置控制上限，普通UI持有量与直接工具保证分开。',['处理器注册容器底层全部优先级/动态重绑定、所有组合特殊道具。'])
cap('主动HP、状态、复活的世代与上下文差异',
 [src('effects','412–455,525–630','回复量与重平衡分支；非战斗全治不含战斗混乱。'),src('itemutil','333–362','封顶与实际增量。'),src('battleeffects','66–79,119–153,333–374,429–466','战斗仅混乱全治可用；复活半血至少1。')],
 [spec('28','§5.1表/§8','精确请求量和全治战斗混乱例外。'),spec('t2','IU-01–06/51–53','HP封顶与SITRUS101/105。')],
 '非蛋非Hyper；HP/状态合法；战斗非Embargo；正常注册/执行。',['POTION缺30补20；HP满/0拒；SITRUS HP1/101→26；REVIVE最大101→50；全治满血NONE混乱3战斗消费并清混乱、非战斗拒；重平衡真/假60/50等。'],
 '当前代8；只静态请求/数值，不认证动画和音效。',['所有别名逐一执行、苦药完整友好算术、异常重入。'],classification=['Pokémon Rules','Creature-RPG'])
cap('PP 补给按上下文的濒死资格、选招与消费',
 [src('battleeffects','155–186,501–533','战斗ETHER族和ELIXIR族先要求目标可战斗，别名同门。'),src('effects','632–684','非战斗恢复只看招式PP条件，无存活门。'),src('itemutil','367–382,644–686,710–775','恢复PP封顶、外层成功扣减；非战斗通用门不拒濒死。'),src('command','100–137','战斗资格失败不登记不消费。'),src('choose','239–285','非蛋目标可进入招式选择，拒绝回成员循环。'),src('pkmn','264–270','可战斗要求非蛋且HP>0。'),src('PBS/items.txt','3294–3333;5242–5250','默认五种PP恢复道具的场外/战斗用途。'),src('PBS/moves.txt','[TACKLE]5326–5336','总PP35。')],
 [spec('28','§5.2,202–206/§3.5','仅给PP门与同步，未给战斗存活门。'),spec('t2','IU-07,51','向量未分濒死上下文。'),spec('51','§4,104–108','AI缺索引异常不是人手PP资格表。'),spec('67a','§5.2–5.3,126–139','目标选择及通用资格框架，具体道具门引用WP28。')],
 '正常玩家队伍[A存活,B濒死]；B非蛋非Shadow非Hyper，TACKLE0/35；对应道具1；普通内部战斗与非战斗独立初态。',
 ['战斗ETHER选择B和TACKLE后失败、不登记，PP0/35、库存1；场外同输入恢复到10/35、HP仍0、库存0；B改存活则两入口都可恢复。','MAXETHER/LEPPA和ELIXIR/MAXELIXIR均同存活门；全PP满/取消另行拒；不把持有LEPPA当主动使用。'],
 '默认PBS与现存handler足以构造；完整游戏UI未运行。',['目标在登记后濒死的全部战斗演化、被动LEPPA/AI全策略、Gen5–7数据替换执行。'],status='partial',findings=['GR4-M05-001'],classification=['Creature-RPG','Pokémon Rules','Combat Requirements'],reason='已有PP量值/同步/消费框架，但五种主动PP补给的战斗存活门和场外反向对照未承接。')
cap('EV培养数量层、100阈值和部分成功消费',
 [src('itemutil','388–502','EV额度、上限、逐份友好及布尔返回；薄荷只改计算性格。'),src('effects','714–784','维生素与羽毛数量注册及WING复制。'),src('settings','233–253','当前多量与无100阈值配置。')],
 [spec('28','§5.3/§6.2/§8','三层数量、世代条件及按qty扣减。'),spec('t2','IU-09–18/49','上限与部分成功反例。')],
 '合法EV受限状态与稳定库存；多量开/关分设；无友好额外加成时。',['HPUP EV100当前代→110、旧阈值开则失败；羽毛EV250持5最大2；若直接qty3仅两份可加仍整体真并按qty扣；POMEG EV250/h255选25→EV0。'],
 '252/510是增量门，不定义一切存储硬上限。',['全部友好代际/软上限、设施EV255创建、全21薄荷映射。'],classification=['Pokémon Rules','Creature-RPG'])
cap('TM/HM/TR教学入口与最初招式记录',
 [src('effects','75–90','背包机器教学把TR传为一次性教学。'),src('util','452–486','成功统计并在一次性教学时追加最初招式。'),src('itemutil','710–730','队伍直接学习并按属性扣，不走包装统计/初始招式追加。'),src('PBS/items.txt','[TM57]4654–4663','显示名TM57但用途TR与CHARGEBEAM。')],
 [spec('28','§5.4,224–229','按数据身份及入口区分。'),spec('t2','IU-20–23/58','TR两入口对照。')],
 '可兼容非蛋非Shadow目标、招式有空槽，用户同意，学习正常返回。',['背包TR成功才追加最初记录并统计；队伍入口成功也扣1但不追加/计包装统计；TM/HM重要不扣；取消不学不扣。'],
 '本项验证记录消费者区别，学习本体和PP保留完整规则属WP30。',['完整教学遗忘输入循环、默认兼容清单穷尽、TR全身份。'])
cap('野外喷雾、HONEY和离洞工具消费',
 [src('effects','27–62,100–226','关袋延后、喷雾计数/冰面不减、蜂蜜无条件真、离洞许可。'),src('field','791–820','天气/无遭遇可使香甜气息不战斗。'),src('playerworld','38–47','具名跟随许可要求followers空。'),src('itemutil','755–762','效果成功才按属性消费。')],
 [spec('28','§3.3/§7','期望遭遇未发生仍可能消费；离洞失败不扣。'),spec('13','§6.2','跟随者守卫只属特定调用入口。'),spec('t2','IU-35/37/38','天气、喷雾叠加和无逃脱点。')],
 '世界对象与道具有效；正常请求返回；喷雾计步通知到达。',['喷雾100/200/250，已有剩余拒叠；冰面不扣步；HONEY天气阻止仍真并扣；离洞无逃脱点或有跟随者拒；成功取消载具/转移后清逃脱点。'],
 '完整普通遭遇/地图传送/钓竿时序属共享域。',['自行车/钓鱼/黑白笛全部消费下游、真实地图、喷雾续用UI。'],classification=['Creature-RPG','Engine / Overworld Integration'])
cap('金钱商店购买回退、出售钳位和球赠品',
 [src('mart','68–95,598–715,722–748','价格、逐件添加回退、先钱后物出售、赠品及原地库存过滤。'),src('player','78–81','金钱钳位。'),src('settings','257','赠品世代门。')],
 [spec('29','§3/§6–9','入口化守卫与状态次序。'),spec('t2','SH-01–11/18–19/27','购买、失败、出售实增与默认量。')],
 '正常商店合法stock；普通道具数量用户明确；有限袋容量只作独立边界。',['200×3从1000→400；只放2/3时撤2且不扣；卖100钱包999950→999999统计49；购买25任意球当前代尝试2纪念球，旧配置仅普通球1；已持重要项原地从stock删且退出不恢复。'],
 '重要物品不能出售；正常库存由缺失事件提供，未假造demo商店。',['全部真实价格经济、输入同轮竞争、音效失败/异常回滚。'])
cap('BP商店、显示半价与会话价格覆盖',
 [src('bp','68–75,332–346,446–525','同买覆盖，数量显示先单价整除2，确认/扣全价，退出清价格。'),src('interpreter','440–452','买正值、卖非负双倍写、旧覆盖保留。'),src('itemdata','119–138','数据售出价默认半价/BP默认1。')],
 [spec('29','§4–5/§8','价格数据/显示/实扣区分。'),spec('t2','SH-12–17/20–28','买卖覆盖算术、BP正常、奇数半价。')],
 '合法道具、足够BP、选定数量3、无异常；覆盖存在与缺失分别。',['BP价21数量3：显示30、扣63；价格0不除0且最大999；卖参数60有效价120；买250覆盖同时影响BP；负/缺省参数不清旧覆盖；会话结束才清映射。'],
 '数据格式/编译的价格上限本次仅读schema，不认证全部PBS编译。',['半价显示宿主观察、所有价格数据输入格式、写入异常恢复。'])
cap('邮件快照、信箱容量与同对象流转',
 [src('mail','4–32,100–125','250字、快照后2/后1/本人，信箱容量10。'),src('pc','58–105','阅读、入袋先加后删除信箱、Give委托。')],
 [spec('64','§2–3/§8–9','快照/转移/容量。'),spec('t3','MG-01–14','快照、邮箱和既有持物对照。')],
 '正常邮件与成员对象、消息/显示正常返回。',['写作空文并停止不创建邮件；容量9→10成功，10拒；入袋成功才删除信箱；阅读逻辑不改邮件内容；IconMail由数据标记。'],
 '邮件卡片/图标素材缺失；Give最终队伍窗口本次只定位委托。',['全部12邮件身份、实际展示、信箱Give嵌套操作全链。'])
cap('神秘礼物解锁、下载候选过滤与重复ID',
 [src('loadui','298–327','有存档且解锁才出下载命令。'),src('gift','241–325,331–349','下载解码、与初始队列过滤、逐条入未领取队列、非空解码错误外传。')],
 [spec('64','§4–5/§8–9','作者唯一ID与下载重复ID分开，下载非领取。'),spec('t3','MG-14–17/27–28','入口、过滤及重复载荷。')],
 '合法已解码静态载荷夹具；已有队列有效；不发网络请求。',['既有同ID已领取/未领取均排除；载荷内两ID7都可入候选；选第一不重新过滤第二；接收只入队列不发物品；非空解码没有本地兜底。'],
 '网络运输仅借共享合同；示例URL未访问，序列化载荷未执行。',['HTTP实现/响应类型全路径、消息掉落动画、真实线上礼物。'],classification=['Creature-RPG','Generic Kernel'])
cap('神秘礼物领取的容量与提交先后',
 [src('gift','354–428','查首未领取；个体先改来源再调用静默获得；物品先can_add；成功才[id]。'),src('acq','78–90','静默赠送容量初检与放置。')],
 [spec('64','§6/§8–9','个体失败保留字段改写、物品预检失败不改队列。'),spec('t3','MG-18–24/28','领取正常/满/查无/重复。')],
 '合法待领个体或数量>0物品；玩家与有效数据；容量明确。',['满队满盒个体领取false但PID/时间/来源等已改且仍待领；物品容量不足不添加不标记；POTION3成功入袋并改单ID标记；两份同ID按首个未领依次发。'],
 '随机值/系统时间仅角色，未获取真实抽样；图鉴画面依资源。',['畸形载荷全部输入、真实配送员事件、领取中断保存恢复。'])
cap('礼物作者侧创建、管理会话与共享个体',
 [src('gift','17–218','创建写主文件；Edit/Delete仅会话；Receive共享同个体；导出写另文件。')],
 [spec('64','§7/§8','四层状态与Receive后Edit取消仍改队伍。'),spec('t3','MG-25–26/29–32','ID0、创建取消别名、管理重进。')],
 '合法静态主文件和已加载玩家夹具；不真实读写礼物或联网。',['0 ID为取消确认非可提交；同会话Receive→Edit先改obtain_text后取消仍影响入队同个体；Delete/Edit不写主文件；Export与Create落盘目标不同。'],
 '作者工具副作用按源静态描述；本轮未调用任何作者写盘。',['重复Receive跨多相同队列别名组合、文件失败实际恢复。'],classification=['Creature-RPG','Demo / Developer Experience'])
cap('探测仪的矩形窗口、平局、方向和三路响应',
 [src('itemutil','556–576','同图hiddenitem子串、排除A、矩形、Manhattan及先枚举平局。'),src('effects','318–355','次数先增、无/脚下/附近三路均真、别名。'),src('PBS/items.txt','6262–6278','两个默认工具Direct/KeyItem。')],
 [spec('28','§3.3-R01,87–103','完整候选与响应合同。'),spec('t2','U03-IF01–11,224–240','阈值7/5对照8/6、脚下/无响应。')],
 '有效玩家/地图/事件/自开关/内容，正常请求返回，无额外回调且方向未锁；锁定对照单列。',['(5,5)到(7,5)/(5,7)等距保先枚举；dx7/dy5可入8/6排；分量相等朝垂直；无候选仍计数+1效果真；脚下4次0.2请求+0.3后提示，不拾取不写A。'],
 '等待是请求值，真实秒数/文字刷新/音效未认证。',['全部真实地图事件排列、宿主方向/媒体/按键表现。'],history=['GR3-M05-002 / U03，详见regression.json'],classification=['Creature-RPG','Engine / Overworld Integration','User Interface'])
cap('个体毫米尺寸数学辅助',
 [src('acq','243–271','原始IV低位、PID低字节、15区段和两次整数阶段。')],
 [spec('18','§7.4,280–308','全部分段与默认段65410起点。'),spec('24','§3.1,54','尺寸引用归个体。'),spec('t1','U03-SZ01–05/B01–B15,250–282','位输入和分段两端。')],
 '合法32位PID与原始IV、整数H高度；只审可得辅助，不称默认玩法启用。',['H7/IV0/P0→203mm、P2304→209、P2560→210；s113→280而非281；默认65410..65535仍T65510；EV/Nature/强化IV不参与。'],
 '静态全脚本仅定义无普通caller；不排除动态/插件调用。',['真实用途、非法字段恢复、宿主执行。'],history=['GR3-M05-001 / U03，详见regression.json'],owner='M04',classification=['Pokémon Rules','Demo / Developer Experience'])
cap('战斗消费登记、失败退款残留与后续清理',
 [src('battleuse','34–148','登记扣、复检失败退但不清身份；成功清身份。'),src('command','5–22,174–181','取消退并清、下轮可出命令直接清。'),src('end','499–510','正常终局逐对象取消选择。')],
 [spec('28','§3.5–3.5.1,112–131','残留及同轮终局消费投影。'),spec('40','§4.2–4.2.1,97–112','上游命令合同。')],
 '合法已登记物品与稳定足够退款容量，使用者存活；只查消费/清理消费者。',['资格复检失败退款后身份仍在；同轮正常终局可再次退；进入下轮仅清不退；效果正常返回不论布尔值都清身份。'],
 '本次重读共享关键消费者；未重演U04完整毒伤裁判链，保持原历史CLOSED。',['战斗全阶段/AI业主/毒伤终局可达性重新全审、所有退款容量竞争。'],owner='M07',history=['GR3-M07-001 / U04（相关消费投影，不重开）'],classification=['Combat Requirements','Creature-RPG'])
write('capabilities.json',caps)
# 全套正式文件反证：机器只作搜索记录，不构成语义执行。
formal=sorted((ROOT/F).rglob('*.md'))
assert len(formal)==131
queries=[('pp_identities',r'ETHER|ELIXIR|LEPPABERRY'),('pp_aliases',r'以太|回复.?PP|恢复.?PP|PP.?回复|PP.?恢复|活力块|活力碎片|苹野|LEPPA'),('pp_fainted',r'PP.{0,30}(濒死|失能|不可行动|可行动|可战斗)|(濒死|失能|不可行动|可行动|可战斗).{0,30}PP')]
searchlog=[]
for name,pattern in queries:
 hits=[]
 for p in formal:
  nums=[i for i,l in enumerate(p.read_text().splitlines(),1) if re.search(pattern,l,re.I)]
  if nums:hits.append({'path':str(p.relative_to(ROOT)),'lines':nums})
 searchlog.append({'name':name,'query':pattern,'scope':F,'files_searched':131,'method':'全目录逐行不区分大小写正则；与本次rg检索互证','hits':hits})
negative={'searches':searchlog,'contexts_read':[spec('28','§3.2–3.5/§5.2/§7','通用门未拒所有濒死；PP段只列PP条件。'),spec('20','§3.2/§5.4–5.5','恢复底层/同步不替代使用资格。'),spec('40','§4.2','资格家族框架和引用，不列PP存活门。'),spec('67a','§5.2–5.3','非蛋目标和资格回调，不自动过滤全部濒死。'),spec('51','§4,104–108','AI存活示例及缺索引异常不定义人工选目标的反向资格，也未给ELIXIR族门。'),spec('50','§4 LEPPABERRY,90','持有触发是不同消费者，不能替代主动资格。'),spec('t2','IU-07/26–28','PP正常向量和POTION复检不提供PP濒死场景。')], 'result':'未找到五种主动PP道具的战斗HP>0门及场外濒死可恢复对照；保留已有通用资格、同步、被动果与AI条款，不以无英文词命中单独判缺失。','source_countersearch':{'scope':'固定参考全部312脚本','queries':[':ETHER|:MAXETHER|:ELIXIR|:MAXELIXIR|:LEPPABERRY','pbCanUseItemOnPokemon|triggerCanUseInBattle|pbItemMenu'],'result':'资格注册/复制集中Item_BattleEffects155–186；非战斗632–684；其它命中为被动持物、AI估值、迁移身份与拾取表，不覆写该资格。Shadow覆写163–178对本例非Hyper成员不增加或撤销此门。'}}
write('negative-evidence.json',negative)
finding={
 'id':'GR4-M05-001','title':'PP补给未区分战斗中的濒死拒绝与非战斗可恢复','module':'M05','severity':'P2','disposition':'REQUIRED','status':'OPEN','reviewer':REVIEWER,'category':'实现信息不足','classification':['Creature-RPG','Pokémon Rules','Combat Requirements'],
 'source_baseline':RBASE,'source_anchors':caps[16]['source_anchors']+[src('shadow','163–178','非Hyper普通目标不改变通用资格返回；不抵消PP家族存活门。'),src('itemdata','119–138,171–198','五物品非重要、默认消费；LEPPA此处只审主动入口。')],
 'specification_baseline':BASE,'spec_anchors':caps[16]['spec_anchors']+[spec('20','§5.4–5.5,159–165','PP恢复辅助及战斗同步存在，但不承接战斗道具的存活前提。'),spec('40','§4.2,99–104','通用资格框架回指WP28。')],
 'expected_reference_behavior':'ETHER/MAXETHER/主动LEPPABERRY以及ELIXIR/MAXELIXIR的战斗资格先要求目标非蛋且HP>0；濒死者即使PP有缺口仍拒绝，不登记、不扣背包。非战斗对同一非蛋非Hyper濒死者可恢复PP：ETHER/LEPPA所选招+10封顶，MAXETHER回满；ELIXIR逐招+10、MAXELIXIR逐招回满，至少有恢复才成功并由外层扣1。HP保持0。',
 'current_spec_behavior':'WP28§5.2列ETHER选招、总PP>0、当前未满和ELIXIR总增量门，并单列战斗同步；§3.5只给通用资格家族调用。未写这五种PP补给战斗额外存活门。IU-07未指明上下文和HP状态。WP51的存活AI/缺索引异常不是这份人手使用资格合同。',
 'gap':'独立实现者不能由正式合同唯一判断对濒死成员的战斗PP使用应拒绝、但场外应成功；沿用一套PP缺口条件会在战斗中错误恢复并消费，沿用统一存活门又会错误拒绝场外使用。',
 'preconditions':['默认Gen8、默认五物品和TACKLE数据，正常内部战斗，玩家有可行动使用者A与非场上濒死B，避免全队濒死无法进入战斗。','B为普通非蛋非Shadow非Hyper合法个体，HP0/100，TACKLE当前0/总35、PP提升0，无额外效果或插件；ETHER库存1，背包/场景正常。','场外对照独立重置同一字段，不从战斗结算恢复后取状态；目标/招式选择正常确认，无取消、重入或宿主异常。'],
 'minimal_counterexample':{'input':'普通内部战斗，A发起使用ETHER，选择濒死后备B，再选TACKLE0/35。','expected':'显示无效果并留成员选择循环；尚未登记UseItem，ETHER仍1，B仍HP0、PP0/35。','nonbattle_reverse':'相同独立初态从普通背包对B选同招：恢复到10/35，HP仍0，效果成功后ETHER1→0。'},
 'normal_case':'仅把B改为HP1/100且仍后备、PP0/35：两上下文均可恢复到10/35；战斗在登记扣1、执行前资格保持时完成效果。',
 'failure_or_boundary_case':['HP0且PP有缺口：战斗五种均拒；场外五种按各自量值可恢复。','目标存活但全部PP已满则仍按既有无效果规则不消费；ETHER取消招式选择不消费。','MAXETHER和MAXELIXIR回满35；ETHER/LEPPA/ELIXIR在唯一TACKLE槽的例子为10；这些数值是未执行静态向量。'],
 'impact_on_independent_implementation':'影响普通合法战斗中的可选择动作、目标PP和背包库存；属于有界事实合同缺口，不是要求实现某个源类或特定API。',
 'negative_evidence_search':negative,
 'proposed_spec_change':'在WP28§5.2以战斗/非战斗两列补五物品的资格差异和别名集合，明确战斗拒绝位于登记扣减之前；保留原恢复量、同步与退款规则。为IU目录增HP0战斗拒、HP0场外成功、HP>0正常及满PP/取消反向向量；WP40/WP67-A可引用，不必复制成多条根因。',
 'acceptance_criteria':[{'kind':'static','criterion':'正文独立给出五种主动PP补给的战斗非蛋且HP>0门，并明确场外无该存活门；不扩大为所有道具统一门。'},{'kind':'static','criterion':'按上述夹具可唯一推出战斗库存1/PP0/HP0、场外库存0/PP10/HP0，且MAX两种和别名量值明确。'},{'kind':'static','criterion':'补存活、PP满、取消对照；引用WP20恢复/同步、WP40登记与WP67-A拒绝返回层不冲突；AI/被动LEPPA不混入。'},{'kind':'runtime','criterion':'本轮不要求运行；静态向量标NOT_EXECUTED。未来如做宿主验证须另记录工具/输入/输出/副作用，不以本次审查签运行通过。'}],
 'affected_files':[P['28'],P['t2']], 'shared_contracts':[{'path':P['20'],'role':'PP状态和恢复量/同步，保持既有合同'},{'path':P['40'],'role':'登记前资格门/扣减'},{'path':P['67a'],'role':'拒绝回成员选择'},{'path':P['51'],'role':'AI消费者区分，非本问题修复目标'},{'path':P['50'],'role':'被动LEPPA区别'}],
 'dependencies':['WP20 非蛋/HP和PP定义','WP27库存','WP28主动使用','WP40战斗登记','WP67-A目标选择'],
 'related_capabilities':['GR4-CAP-M05-017'],'related_findings':[],'root_cause_group':'PP_RECOVERY_CONTEXT_ELIGIBILITY','history_links':{'relation':'new','third_round':None,'second_round':None,'note':'不是GR3-M05-001/002或GR3-M07-001。第二轮同根ID未作猜测；本轮只判当前固定正式材料缺口。'},
 'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],'execution_status':'NOT_EXECUTED','confidence':'HIGH','unknowns':['真实媒体、按键、宿主UI运行未证。','未穷举插件覆写与全部世代数据替换；缺口在固定默认数据已成立。'],
 'excluded_claims':['不认为底层PP恢复本身拒绝濒死。','不声称全部战斗道具不能对濒死使用，复活道具另有相反资格。','不将AI缺索引异常、被动树果或执行退款残留算成本问题。','不要求修改参考，也不提供框架实现。'],
 'user_decision_needed':False,'review_resolution':{'reviewer_verdict':'CONFIRMED_STATIC_GAP','next':'待另一独立审者按共同任务书针对性反证/去重；本审不修规格、不关闭历史项。'}
}
write('findings.json',{'schema_version':'1.0','findings':[finding]})
# 历史固定引用；只读取本域两项，不继承旧签名。
UCOM='08fc8828229c14ab4a540db417d08194ba194a31'
UPATH='review/remediation-third-20261012-prepare/U03/actual-integration/independent-review/attempt-01/per-id-verdicts.json'
ACOM='c2eb74c7cbcf8a190d5e902d871fbce44904efd6'
APATH='review/remediation-third-20261012-prepare/registration/U03-formal-acceptance.json'
regs=[]
for n,idx in [('001',27),('002',26)]:
 c=caps[idx]
 regs.append({'id':'GR3-M05-'+n,'reviewer':REVIEWER,'current_baseline':BASE,'current_file_anchors':c['spec_anchors'],'source_anchors':c['source_anchors'],'old_acceptance_fixed_reference':[{'commit':UCOM,'path':UPATH,'pointer':'/verdicts/'+('1' if n=='001' else '2'),'use':'原验收标准与静态PASS范围；本轮重新比当前正文与参考。'},{'commit':ACOM,'path':APATH,'use':'本批精确实际接受；该时点final_CLOSED=false，不混同后来的最终关闭。'}],'criteria_checked':c['checked_branches_boundaries'],'consumer_checked':('WP24仅转引，固定脚本pbSize仅定义；未将其当默认玩法。' if n=='001' else 'WP28场外消费折叠与默认KeyItem；隐藏事件拾取仍独立，不由探测自动写A。'),'result':'supported','result_meaning':'SUPPORTED_STATIC_NO_REGRESSION_IN_CHECKED_CRITERIA','historical_status':'CLOSED (保持原身份；本轮未执行关闭动作)','limits':c['not_checked']+['不将旧PASS转授完整本域，不代替本轮其它能力样本。'],'evidence_level':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR'],'execution_status':'NOT_EXECUTED'})

for reg in regs:
 reg['old_acceptance_fixed_reference'].append({'commit':'98e49a592c9e82b1e53d3f1fd403ba2ad0935983','path':'review/remediation-third-20261012-prepare/registration/final-closure-acceptance.json','use':'最终激活关闭；导航为当前B的delivery/2026-10-12/current-status.json，保留effective_CLOSED23。'})
write('regression.json',regs)
# 每份正式文件均盘点；只有列出的局部合同产生正向支持。
coverage=[]
for p in formal:
 rel=str(p.relative_to(ROOT)); cs=[c for c in caps if any(a['path']==rel for a in c['spec_anchors'])]
 primary=rel in [P[k] for k in ['24','25','26','27','28','29','64']]
 tests=rel in [P['t1'],P['t2'],P['t3']]
 if cs:
  anchors=[]
  for c in cs:
   for a in c['source_anchors']:
    if a not in anchors: anchors.append(a)
  checked=[]
  for c in cs:
   for a in c['spec_anchors']:
    if a['path']==rel:checked.append({'locus':a['lines_or_symbol'],'contract':a['fact'],'capability_id':c['capability_id']})
  positive=[c['capability_id'] for c in cs if c['status']=='supported']
  coverage.append({'path':rel,'baseline':BASE,'role':'primary' if primary else 'test_catalog' if tests else 'shared_projection','contracts_checked':checked,'source_anchors':anchors,'status':'partial' if rel in [P['28'],P['t2']] or not positive else 'supported','support_evidence':{'meaning':'所列合同supported_static，不是整文件通过','capabilities':positive,'levels':['SOURCE_STATIC','SPEC_STATIC','DERIVED_VECTOR']},'dependencies':sorted({a['path'] for c in cs for a in c['spec_anchors'] if a['path']!=rel}),'unsupported_assertions':['GR4-M05-001：PP战斗濒死门未承接'] if rel in [P['28'],P['t2']] else [],'not_checked':sorted({v for c in cs for v in c['not_checked']})+['本文件未在contracts_checked列出的章节、附表行与测试行不签语义通过；测试从未执行。']})
 else:
  coverage.append({'path':rel,'baseline':BASE,'role':'scope' if rel==P['scope'] else 'inventoried_dependency_or_other_module','contracts_checked':(['§2–§5：材料、静态证据与运行限制；历史公共状态不重审'] if rel==P['scope'] else []),'source_anchors':[],'status':'not_reviewed','support_evidence':{'meaning':'仅文件盘点或别名搜索命中，不等于正文语义核对'},'dependencies':[],'unsupported_assertions':[],'not_checked':['正文、附表、测试未作本域语义验收；命中词也不作为全文件阅读。']})
write('spec-coverage.json',coverage)
# 参考全432 tracked路径盘点 + 本域文本候选检索；无哈希重验/无二进制解码。
tracked=subprocess.check_output(['git','-C',str(REF),'ls-files','-z'],text=True).split('\0')[:-1]
pattern=r'ItemHandlers::|\$bag\.(?:add|remove|can_add|add_all|remove_all|replace_item)|pb(?:AddPokemon|AddToParty|AddForeignPokemon|GenerateEgg|StartTrade|StorePokemon|RegisterPartner)|mystery_gifts|mailbox|RegionalStorage|PokemonStorage|PokemonBag|PCItemStorage|mart_prices'
source_entries=[]
for path in tracked:
 p=REF/path; semantic=[]
 for c in caps:
  for a in c['source_anchors']:
   if a['path']==path and a['lines_or_symbol'] not in semantic:semantic.append(a['lines_or_symbol'])
 # 反证专项source读
 for a in finding['source_anchors']:
  if a['path']==path and a['lines_or_symbol'] not in semantic:semantic.append(a['lines_or_symbol'])
 hits=[]
 if path.startswith('Data/Scripts/') and path.endswith('.rb'):
  hits=[i for i,l in enumerate(p.read_text().splitlines(),1) if re.search(pattern,l)]
 related=bool(semantic or hits or path.startswith('Data/Scripts/013_Items/') or path.startswith('Data/Scripts/015_Trainers and player/') or (path.startswith('PBS/') and Path(path).name in ['items.txt','items_shadow_pkmn.txt','trainers.txt','trainer_types.txt','metadata.txt','map_metadata.txt','moves.txt','pokemon.txt','pokemon_forms.txt']) or path.startswith('Text_english_core/'))
 source_entries.append({'path':path,'commit':R,'role':'semantic_sample' if semantic else 'domain_candidate_or_consumer' if related else 'outside_selected_M05_scope','status':'read_semantically' if semantic else 'inventoried_only','ranges_read_semantically':semantic,'discovery_hit_lines':hits,'not_checked':'列出范围外均未审；存在/词命中不证明支持、可解析或可运行。' if semantic else '仅路径/文本词级盘点；未审语义、未解析或执行。'})
write('source-scope.json',{'schema_version':'1.0','reviewer':REVIEWER,'reference_baseline':RBASE,'inventory_method':'基于固定参考git ls-files全部tracked路径；从核心目录与全脚本文本消费者反查，不重做共享逐字readiness。','discovery_query':pattern,'formal_discovery':'spec-coverage.json列出完整131文件；各主域正文、附表/测试与共享合同逐项限定。','counts':{'tracked':len(source_entries),'scripts':sum(x['path'].startswith('Data/Scripts/') for x in source_entries),'pbs':sum(x['path'].startswith('PBS/') for x in source_entries),'semantic_sample_files':sum(x['status']=='read_semantically' for x in source_entries),'domain_candidates_and_samples':sum(x['role']!='outside_selected_M05_scope' for x in source_entries)},'entries':source_entries,'unavailable':['Graphics/Audio完整素材','Data/Map*.rxdata与完整Demo事件数据库','已成立的游戏宿主运行'],'inventoried_not_parsed':['Data/Scripts.rxdata','Data/messages_core.dat','所有翻译目录文本只盘点，未逐条语义核对','Gen5–8/Shadow备份只盘点与少量身份定位，未验证启用组合']})
write('execution.json',{'actual_executions':(json.loads((OUT/'execution.json').read_text())['actual_executions'] if (OUT/'execution.json').exists() else []),'not_executed':[{'kind':'EXECUTED_REFERENCE','reason':'未执行参考程序或抽取的参考路径；全部语义结论是SOURCE_STATIC。'},{'kind':'EXECUTED_MODEL','reason':'未运行独立行为模型；反例与向量为DERIVED_VECTOR。'},{'kind':'EXECUTED_HOST_OR_DEMO','reason':'缺完整地图/媒体/宿主；未运行游戏、UI、战斗或真实Demo。'},{'kind':'network_or_authoring','reason':'没有下载礼物、访问示例URL、真实存档、编译、作者写盘或账户。'}],'read_only_tool_activity':'常规rg/nl/git show/文件盘点仅为证据读取；不登记为行为测试。最终产物JSON/引用验证将另记TOOL_VALIDATION。'})
write('reviewer-identity.json',{'schema_version':'1.0','reviewer':REVIEWER,'formal_baseline':BASE,'source_baseline':RBASE,'authorization':'仅本M05目录可写；未创建其它agent、未改正式/参考/全局矩阵/历史、未commit或push。','model_verification':'CLI launch仅证明请求，不证明实际后端模型/推理档位/服务档位。'})
print(json.dumps({'capabilities':len(caps),'formal_inventory':len(coverage),'reference_inventory':len(source_entries),'findings':1,'regressions':len(regs)},ensure_ascii=False))
