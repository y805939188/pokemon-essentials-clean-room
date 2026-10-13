import review_state as s
from pathlib import Path
import re
P='deliverables/final-specification-set/'
SRC={
 'bag':'013_Items/008_PokemonBag.rb','util':'013_Items/001_Item_Utilities.rb','effect':'013_Items/002_Item_Effects.rb','beffect':'013_Items/003_Item_BattleEffects.rb','mail':'013_Items/006_Item_Mail.rb','item':'010_Data/002_PBS data/006_Item.rb','metadata':'010_Data/002_PBS data/016_Metadata.rb','settings':'001_Settings.rb',
 'acq':'019_Utilities/002_Utilities_Pokemon.rb','over':'012_Overworld/001_Overworld.rb','trade':'016_UI/001_Non-interactive UI/005_UI_Trading.rb','party':'016_UI/005_UI_Party.rb','storage':'014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb','boxes':'016_UI/017_UI_PokemonStorage.rb','bagui':'016_UI/007_UI_Bag.rb','pcitem':'016_UI/018_UI_ItemStorage.rb','ready':'016_UI/016_UI_ReadyMenu.rb','pc':'016_UI/019_UI_PC.rb','mart':'016_UI/020_UI_PokeMart.rb','bp':'016_UI/021_UI_BattlePointShop.rb','gift':'016_UI/024_UI_MysteryGift.rb','battleitem':'011_Battle/001_Battle/006_Battle_ActionUseItem.rb','player':'015_Trainers and player/004_Player.rb','trainer':'015_Trainers and player/001_Trainer.rb','pokemon':'014_Pokemon/001_Pokemon.rb'}
def anchors(*args):
 ret=[]
 for key,a,b in args:ret.append({'path':'Data/Scripts/'+SRC.get(key,key),'version':s.R,'lines':[a,b]})
 return ret
# All of these sections were read as full body text, tables, examples and failure clauses.
# Grouped annotations below are judgments from those reads, not inferred from heading extraction.
DATA={
'wp26-acquisition-gifts-and-script-trade.md':[
(1,44,'§1–2范围/定义',anchors(('acq',1,231),('trade',193,243)),'supported_static：入口和所有者/静默分工；非运行证明'),
(45,60,'§3.1六入口对照全部行',anchors(('acq',77,231)),'supported_static：普通/静默/仅入队/外来/蛋的容量与返回差异'),
(61,83,'§3.2逐入口全部顺序与UNOWN边界',anchors(('acq',77,231)),'supported_static：图鉴显式/构造隐式分开；M06创造/形态投影'),
(84,92,'§3.3命名/存储三工具',anchors(('acq',1,76),('storage',241,324)),'supported_static：复检/昵称空值/送盒治疗与直接追加'),
(93,121,'§4.1–4.3交换输入/提交/失败',anchors(('trade',1,243),('party',1533,1560)),'supported_static：统计先写、等级/招式物种与实例差异、演出后替换；演出未执行'),
(122,142,'§5交界矩阵全部行',anchors(('acq',1,231),('gift',360,428),('party',1504,1560)),'partial：主入口吻合；竞赛/净化间消费者尚待补读，未把表引用当全证'),
(143,155,'§6九项不变量',anchors(('acq',1,231),('trade',193,243)),'supported_static：已提交前缀不回滚；仅入队并非无条件最终位置保证'),
(156,176,'§7全部失败与A/B/C反例',anchors(('acq',1,231),('trade',193,243)),'supported_static：初检/消息等待/命名与最终存储分层'),
(177,207,'§8–11配置/向量/依赖/未决',anchors(('settings',126,169),('settings',215,225),('acq',1,231)),'supported_static限定；脚本事件/demo不可得未证明')],
'wp27-bag-and-item-storage.md':[
(1,44,'§1–2概念表所有行',anchors(('bag',1,301),('settings',259,282)),'supported_static容器、槽位、游标和登记三层'),
(45,55,'§3.1查询/容量表',anchors(('bag',28,83)),'supported_static未知/负要求与游标下界边界'),
(56,67,'§3.2变更表',anchors(('bag',84,164)),'supported_static：逐个/全有全无分开、同袋替换不合并'),
(68,77,'§3.3助手全部算法',anchors(('bag',232,301)),'supported_static贪心预检纯性、执行部分保留、无限袋仅增一槽扫描'),
(78,86,'§4.1PC储存',anchors(('bag',166,231),('metadata',59,79),('pc',136,146)),'supported_static：固定999×999、已有记录的播种每项1、默认空与文本POTION分开'),
(87,99,'§4.2存取/丢弃/信箱全部表行',anchors(('pcitem',247,376),('pc',58,105)),'supported_static：预检及删加顺序；重要物品整叠/单数显示；信箱Move to Bag不同于Give候选'),
(100,109,'§4.3界面业务',anchors(('bagui',421,704),('party',927,936)),'supported_static：过滤/初始袋与退出恢复按WP66-C补充解释；给予非蛋而非存活门'),
(110,120,'§5登记与快捷',anchors(('bag',137,164),('ready',180,331),('util',121,128)),'supported_static：可登记、直接登记、图标、快捷收集资格不合并'),
(121,142,'§6–7不变量/失败全部条目',anchors(('bag',1,301),('over',653,750),('gift',388,425),('pcitem',247,376)),'supported_static：1500入空无限袋留下999、消息差；不擅加全消费者事务'),
(143,174,'§8–11配置/向量/依赖/未决',anchors(('settings',259,282),('bag',1,301),('metadata',59,79)),'supported_static默认；世代备选不是运行自动切换')],
'wp28-item-use-and-training.md':[
(1,46,'§1–2范围/概念表',anchors(('util',1,128),('item',171,202)),'partial：分流与名义覆盖成立；具体身份参数缺失待候选'),
(47,68,'§3.1十家族/复制/条件/默认',anchors(('util',1,128),('003_Game processing/005_Event_Handlers.rb',144,198)),'supported_static家族组合与缺处理器默认'),
(69,78,'§3.2背包',anchors(('util',640,707),('bagui',450,559)),'supported_static：最大量/库存/循环与最后取消返回'),
(79,86,'§3.3野外',anchors(('util',750,777),('effect',26,379)),'supported_static入口层；远端地图/钓鱼功能投影待补'),
(87,104,'§3.3-R01探测仪',anchors(('util',552,578),('effect',289,355)),'supported_static全搜索/方向/响应；U03-IF逐向量另核'),
(105,111,'§3.4个体/教学统计',anchors(('util',710,748),('party',1394,1405)),'supported_static：背包包装与队伍直接使用统计/最初招式区别'),
(112,122,'§3.5战斗',anchors(('battleitem',1,149),('beffect',1,328),('011_Battle/001_Battle/009_Battle_CommandPhase.rb',100,138)),'supported_static：登记/资格/目标/球、效果缺席Direct5'),
(123,134,'§3.5.1退款残留与终局',anchors(('battleitem',1,149),('011_Battle/001_Battle/002_Battle_StartAndEnd.rb',405,512)),'partial：退款函数已核；最终循环完整调用链待消费范围补核'),
(135,165,'§4覆盖表全身份族',anchors(('effect',1,1524),('beffect',1,712)),'partial：已完整源读全部登记/复制/条件，表“主要”目录不能代完整参数；具体缺口继续反证'),
(166,201,'§5.1治疗复活/完整HP表及MILKDRINK',anchors(('effect',403,627),('beffect',66,154),('beffect',329,500),('util',329,347),('party',1278,1323)),'supported_static全部HP数值/配置/状态上下文与实际增量'),
(202,220,'§5.2五PP/成长/全部边界',anchors(('effect',628,713),('beffect',155,182),('beffect',501,532),('util',348,383)),'supported_static场外濒死可回复/战斗登记前拒、有效槽同步与PP成长'),
(221,234,'§5.3培养/薄荷/特性/经验',anchors(('effect',714,1121),('util',129,328),('util',384,500),('pokemon',420,545),('pokemon',929,969)),'partial：通用培养算法/友好/薄荷/糖果已承接；六stat身份映射、能力药具体索引和ZYGARDE名缺失'),
(235,243,'§5.4机器与石',anchors(('effect',380,402),('util',579,639),('util',644,656),('util',710,731),('party',1083,1164)),'supported_static：TM/HM/TR、两个入口最初招式/统计差异、不可取消石进化'),
(244,254,'§5.5战斗增益族',anchors(('beffect',214,328),('beffect',533,712)),'partial：X六属性/蘑菇/Mist/娃娃/笛支持；DIREHIT资格阈值1与写入2未精確承接'),
(255,278,'§5.6形态/八融合表全行',anchors(('effect',1122,1524),('party',746,800),('party',1204,1218),('trainer',116,125)),'partial：普通路径支持；GR5-M05-002盒子重入反例推翻全称移出/取消状态承诺'),
(279,308,'§6–7不变量/失败',anchors(('util',640,854),('battleitem',1,149),('effect',1,1524),('beffect',1,712)),'partial：多数通用门支持；融合的未撤销嵌套队伍改变按N002限定'),
(309,346,'§8–11配置/59向量/依赖/未决',anchors(('settings',231,257),('item',119,137),('002_BattleSettings.rb',54,68)),'partial：世代开关与消耗分流支持；字段默认/数量显示待全相关合同反查')],
'wp29-shops-and-exchanges.md':[
(1,44,'§1–2概念/范围',anchors(('mart',1,748),('bp',1,525)),'supported_static三价/库存/赠品/覆盖'),
(45,52,'§3.1入口可见性',anchors(('mart',722,748)),'supported_static：传入库存原地移重要品、cantsell，退出清价格'),
(53,64,'§3.2购买步骤',anchors(('mart',598,671),('bag',84,115)),'supported_static：逐份添加、已加回退，数量与钱包复检；回退总量并非槽分布事务'),
(65,71,'§3.3全部赠球配置',anchors(('mart',640,667),('settings',254,257)),'supported_static两配置与逐份能放才统计'),
(72,85,'§3.4出售/默认量/统计',anchors(('mart',673,718),('player',58,64)),'supported_static：售零/重要拒、价格覆盖、实际钱包增量计收入'),
(86,107,'§4BP全步骤及显示三量',anchors(('bp',1,45),('bp',360,382),('bp',446,525)),'supported_static：展示qty×floor(unit/2)、确认实扣unit×qty；与money槽共享覆盖'),
(108,126,'§5数据价/两事件覆盖入口',anchors(('mart',1,78),('bp',1,45),('003_Game processing/003_Interpreter.rb',433,449),('item',119,137)),'supported_static：买>0卖>=0/卖参数×2/非正保留'),
(127,151,'§6资源域与顺序表',anchors(('player',58,81),('mart',598,718),('bp',446,509),('item',25,70)),'supported_static：文本非负不钱包上限，编辑器界限与运行setter分离'),
(152,177,'§7–8全部不变量/失败',anchors(('mart',598,748),('bp',446,525),('bag',84,115)),'supported_static：支持已有明确正常未变状态前提；不把清覆盖与取消写资源合并'),
(178,208,'§9–12配置/向量/依赖/未决',anchors(('settings',48,57),('settings',254,282),('item',119,137)),'supported_static：默认商店规则；真实事件库存留未知')],
'wp64-mail-and-mystery-gift.md':[
(1,24,'§1范围/分类/非目标',anchors(('mail',1,125),('gift',1,428)),'supported_static声明静态与事件/HTTP/媒体边界'),
(25,34,'§2.1–2.2邮件字段/快照/写信',anchors(('mail',1,18),('mail',100,125),('boxes',1247,1260),('016_UI/006_UI_Summary.rb',1195,1229)),'partial：普通队伍快照/取消支持，盒子Summary索引源缺口GR5-M05-003'),
(35,40,'§2.3信箱',anchors(('mail',20,32)),'supported_static懒建、容量10、移同对象、caller另清item'),
(41,59,'§3.1–3.2阅读/取回/信箱全部行',anchors(('mail',34,99),('pc',58,105),('party',938,956),('util',821,854),('pokemon',585,599)),'partial：PC Give成功承诺与mail读取自清冲突GR5-M05-001；其它表行支持'),
(60,70,'§3.3两给予部分提交案例',anchors(('util',781,854),('party',1408,1431)),'supported_static：取消返新邮件不撤旧物入包；先取后给不回滚'),
(71,78,'§4礼物载体/默认持久',anchors(('gift',1,170),('player',10,57)),'supported_static：四元/作者唯一与下载不唯一/编码分层'),
(79,87,'§5下载/候选/接收',anchors(('gift',241,338)),'supported_static本地接收与解码错误；HTTP实现细节待工具正文补核'),
(88,100,'§6.1礼物个体领取写序',anchors(('gift',354,386),('acq',118,151)),'supported_static：先重摇/来源/招式/能力/静默获得、成功才标记；构造与Dex副作用归M06'),
(101,111,'§6.2–6.3物品领取/查无',anchors(('gift',354,428),('bag',58,115)),'supported_static：预检失败不加，成功后标记首未领ID，不清同ID其它条目'),
(112,120,'§7作者编辑/管理/导出',anchors(('gift',1,240)),'supported_static：ID0/缺文件/损坏传播/现有个体别名；非运行测试'),
(121,141,'§8–9不变量与全部边界',anchors(('mail',1,125),('gift',1,428),('party',938,956)),'partial：同对象转移需排除Give失败N001；其它重复/失败/作者保存范围支持'),
(142,161,'§10–12依赖/32向量/未知',anchors(('gift',1,428),('mail',1,125)),'supported_static范围限定；不据占位URL推任何连通性')]
}
for filename,rows in DATA.items():
 path=P+'creature-rpg/'+filename
 d=s.load('spec-to-source');d['specifications']=[q for q in d['specifications'] if q['path']!=path];s.save('spec-to-source',d)
 s.spec(path,rows)
# Add explicit per-clause/per-table-row projection under each semantic section.
d=s.load('spec-to-source')
for q in d['specifications']:
 if q['kind']!='formal' or 'creature-rpg/wp' not in q['path']:continue
 ls=(s.REPO/q['path']).read_text().splitlines()
 for section in q['sections']:
  a,b=section['lines'];clauses=[]
  for n in range(a,min(b,len(ls))+1):
   t=ls[n-1]
   if not t.strip() or t.startswith('#') or re.match(r'^\|\s*[-:]+',t) or t.strip()=='---':continue
   clauses.append({'line':n,'kind':'table_row' if t.startswith('|') else 'clause','spec_text':t,'source_anchors':section['source_anchors'],'judgment_reference':section['section']})
  section['clauses_and_table_rows']=clauses
s.save('spec-to-source',d)
