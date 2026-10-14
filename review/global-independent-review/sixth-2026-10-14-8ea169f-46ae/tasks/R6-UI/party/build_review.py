"""Generate audit records from manually reviewed facts; no reference code execution."""
import json, re, subprocess, hashlib
from pathlib import Path
from datetime import datetime, timezone
ROOT=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT=Path(__file__).resolve().parent
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
FORMAL='deliverables/final-specification-set/'
UI=FORMAL+'user-interface/'
SPEC=UI+'wp66-a-party-and-summary-ui.md'
TEXTSPEC=UI+'wp17-messages-windows-input.md'
CAT=FORMAL+'test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md'
R='reference/pokemon-essentials/'
S=R+'Data/Scripts/'
PARTY=S+'016_UI/005_UI_Party.rb'
SUMMARY=S+'016_UI/006_UI_Summary.rb'
RELEARN=S+'016_UI/022_UI_MoveRelearner.rb'
TEXT=S+'016_UI/025_UI_TextEntry.rb'
ITEM=S+'013_Items/001_Item_Utilities.rb'
MAIL=S+'013_Items/006_Item_Mail.rb'
POKE=S+'014_Pokemon/001_Pokemon.rb'
SPRITE=S+'014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb'
FORMS=S+'014_Pokemon/001_Pokemon-related/001_FormHandlers.rb'
WINDOW=S+'007_Objects and windows/005_SpriteWindow_text.rb'
EDIT=S+'007_Objects and windows/012_TextEntry.rb'
HELPER=S+'016_UI/018_UI_ItemStorage.rb'
STORAGE=S+'016_UI/017_UI_PokemonStorage.rb'
EFFECTS=S+'013_Items/002_Item_Effects.rb'
TUTOR=S+'019_Utilities/001_Utilities.rb'
RULES=S+'018_Alternate battle modes/002_Battle Frontier rules/002_Challenge_Rulesets.rb'
DRAW=S+'007_Objects and windows/010_DrawText.rb'
MENU=S+'003_Game processing/006_Event_HandlerCollections.rb'
now=datetime.now(timezone.utc).isoformat()
def frozen(path):
    repo=ROOT/'reference/pokemon-essentials' if path.startswith(R) else ROOT
    rev=REF if path.startswith(R) else MAIN
    rel=path[len(R):] if path.startswith(R) else path
    return subprocess.check_output(['git','-C',str(repo),'show',rev+':'+rel])
def ev(path,a,b):return {'path':path,'start_line':a,'end_line':b}
def link(a,b=None,path=SPEC):return ev(path,a,a if b is None else b)
def dump(name,obj):(OUT/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def jsonl(name,rows):(OUT/name).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
units=[]
def u(path,a,b,label,fact,refs,consumers=(),verdict='STATIC_SUPPORTED',note=''):
    idx=len([x for x in units if x['source']['path']==path])+1
    fid={'005_UI_Party.rb':'P','006_UI_Summary.rb':'S','022_UI_MoveRelearner.rb':'R','025_UI_TextEntry.rb':'T'}[path.split('/')[-1]]+f'{idx:03d}'
    units.append({'unit_id':'R6-UI-party-'+fid,'source':ev(path,a,b),'classification':'User Interface','review_level':'semantic' if verdict!='STRUCTURE_ONLY' else 'structure','fact':fact,'label':label,'formal_links':refs,'necessary_consumer_evidence':list(consumers),'assessment':verdict,'note':note,'reference_execution':'NOT_EXECUTED','host_demo':'UNKNOWN'})
# The intervals are manually chosen semantic units and partition every assigned source line.
u(PARTY,1,103,'确认与取消按钮','普通队伍仅取消，多选有确认和取消；选中态改变背景；尺寸与坐标来自当前资源约定。',[link(35,37)],verdict='STATIC_SUPPORTED')
u(PARTY,104,131,'命令颜色','蓝色命令标签与普通文字分开；构造阶段会消费并改写内部命令数组，未来不要求保留该容器实现。',[link(70)])
u(PARTY,132,160,'空槽','空槽只显示空面板，不接受选中、预选和换位标记；其它视觉属性可更新。',[link(35,37)])
u(PARTY,161,244,'成员面板建立及释放','首位圆角、其它矩形；成员、持物、状态和HP资源在开场请求，资源实际存在与释放异常未验证。',[link(35,38),link(263)], [ev(SPRITE,85,140)])
u(PARTY,245,295,'刷新触发与缓存','成员/注解改变会重画文字；选择、预选、换位状态只触发对应显示刷新；显示读取可能填缓存或提交动态形态。',[link(38),link(225)], [ev(POKE,147,179),ev(SPRITE,124,140)])
u(PARTY,296,321,'面板状态优先级','选中时来源预选优先于换位、换位优先于濒死；未选中时来源预选优先于濒死。',[link(37)])
u(PARTY,322,337,'HP背景可见门','蛋或非空注解隐藏HP背景；换位相关背景优先于濒死背景。',[link(38)])
u(PARTY,338,361,'成员与持物图标','球图跟随选择；成员图标跟随成员与位置；持物提示在更新中重新消费当前持物。',[link(38)], [ev(SPRITE,85,202),ev(S+'013_Items/007_Item_Sprites.rb',116,157)])
u(PARTY,362,444,'文字与状态绘制','蛋不显示等级/性别/HP/状态/闪光；非空注解同时隐藏HP与状态图。存活才画HP前景，比例偶数舍入；濒死、异常、感染期状态按优先级。',[link(38,39)], [ev(POKE,244,250)],note='正文只明确注解替代HP区域，未明确状态图一起隐藏；零HP前景门未明写，见覆盖观察 O-PT-01。')
u(PARTY,445,473,'面板更新','文字重画有刷新缓存，动态图标继续更新；不能把未触发重画解释为所有个体读取只读。',[link(38),link(225)], [ev(SPRITE,184,202)])
u(PARTY,474,527,'队伍开场','建立最多配置数量的面板；初始选择0；多选另设确认、取消；存储许可参数决定提示文字与快捷桥。',[link(29),link(35),link(132)], [ev(S+'001_Settings.rb',207,225)])
u(PARTY,528,555,'普通消息','消息忙时USE调用恢复，已全显时USE或BACK关闭；不把BUSY暂停当作返回。',[link(242)], [ev(WINDOW,300,387),ev(WINDOW,526,580)])
u(PARTY,556,587,'局部确认','默认Yes；只有消息不忙时才受理BACK或USE恢复；三行两行窗中间暂停可使循环持续更新而不能返回。',[link(242)], [ev(WINDOW,300,387),ev(WINDOW,526,580)])
u(PARTY,588,617,'命令选择','默认首项；窗口先更新，再BACK优先于USE，BACK返回-1，USE返回当前索引。',[link(70,72),link(54,56)],note='同轮出口是本地命令入口合同，不借用光标命名优先序。')
u(PARTY,618,639,'数量与注解','按件数量委托共享输入；注解按槽更新，存在性只检查首面板文本是否为空值。',[link(95),link(104),link(226)], [ev(HELPER,276,325)])
u(PARTY,640,703,'选中与换位演出','预选保留来源位置；换位演出分别离场/入场，结束清换位标记并刷新；异常无确保回退保证。',[link(62,64),link(223)])
u(PARTY,704,744,'摘要与内嵌背包','摘要关闭后刷新原队伍；给予列表过滤可携带；使用列表过滤处理器/机器、Hyper香类、已知与不兼容机器。',[link(78),link(90,95)], [ev(ITEM,125,127),ev(S+'010_Data/002_PBS data/006_Item.rb',184,198)])
u(PARTY,745,800,'成员选择输入','方向同轮覆盖优先UP/LEFT/RIGHT/DOWN；然后SPECIAL、ACTION、BACK、USE互斥裁决。快捷目标禁桥且ACTION取消；菜单目标桥仍可用。',[link(54,64)], [ev(STORAGE,1500,1509),ev(STORAGE,1650,1661)],note='本条方向优先序为源事实；正文未列组合查询，真实物理组合仍未知。')
u(PARTY,801,853,'方向转移','左右按相邻索引，向上一般同列减2；按钮间与队伍边缘按特定分支移动；DOWN落空即到按钮，不是统一跳到下一非空。多选7 UP到6、6 DOWN到7。',[link(41,48)],note='导航文字为概括；不能代替完整多选按钮转移矩阵。')
u(PARTY,854,874,'从盒返回重建','注解按旧槽保存，旧有效选中索引保留，超出剩余长度夹末位，无旧有效槽落取消；不保留预选来源对象。',[link(29),link(60),link(239)])
u(PARTY,875,903,'普通刷新','普通刷新重读各面板原引用，单槽刷新只重读相应引用；硬重建才按当前队伍重建容器。',[link(78),link(95),link(225)])
u(PARTY,904,925,'借用场景入口','一般借用入口不传存储许可；选人可设置帮助文本；多席位参数在此入口未使用。',[link(23,26),link(257)])
u(PARTY,926,957,'给予入口','给予选人后执行给物并返回成功；取消为false。邮箱给予先提示后挂邮件，再读取会因无匹配持物清邮件，后续取物身份失败，未删邮箱。',[link(21,22),link(107)], [ev(ITEM,781,854),ev(POKE,573,599)])
u(PARTY,958,989,'转发接口','屏幕转发显示、确认、命令与刷新；引用同一场景；不要求未来保留这些源接口。',[link(13)],verdict='STRUCTURE_ONLY')
u(PARTY,990,1011,'未调用的重复限制工具','定义了相同物种与重复持物检查，但本文件未用；不能推出普通队伍界面强制这些限制。',[],verdict='INVENTORY_ONLY')
u(PARTY,1012,1021,'换位提交','不同来源/目标时，在离场演出后按旧位置交换引用，再入场刷新；来源失效也不重验，不回滚已写队伍。',[link(62,64),link(223)], [ev(PARTY,672,696)])
u(PARTY,1022,1034,'简单选招列表','现有招式按当前/总PP显示，总PP非正用占位；借用普通命令取消合同。',[link(26)],note='此入口与摘要遗忘画面不是同一入口。')
u(PARTY,1035,1049,'资格注解显式刷新','只有存在注解时逐成员重算；清注解独立；进化石成功后调用此显式刷新。',[link(95),link(131),link(226)], [ev(EFFECTS,380,409)])
u(PARTY,1050,1139,'多选入场','前置有效队伍门；资格与位次数组保留；Entry/No Entry重排；满最大人数新增后选确认；校验失败首错误，取消nil。',[link(25),link(132),link(236)], [ev(RULES,1,78),ev(RULES,127,220),ev(TUTOR,1,47),ev(S+'018_Alternate battle modes/002_Battle Frontier rules/003_Challenge_EntryRestrictions.rb',254,268),ev(S+'018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb',38,49)],verdict='CONFLICT',note='R6-UI-PARTY-004；校验失败后未跳回选择器，旧菜单命令0可误入不存在的第6位摘要。')
u(PARTY,1140,1170,'资格选择','开场仅求一次资格并缓存；拒不合格留循环；允许不合格绕过拒绝；BACK -1。',[link(23),link(131),link(226)])
u(PARTY,1171,1203,'带资格交易选择','传入处理器先求值，再叠加蛋/Shadow/不可交易；缓存结果，允许不合格可接受。',[link(24),link(131)])
u(PARTY,1204,1257,'主菜单与会话桥','开场求存储三门，主菜单按注册条件排序追加Cancel，已知场地招插固定位置，非蛋才插入。',[link(19,20),link(29),link(70)], [ev(MENU,80,116),ev(S+'012_Overworld/004_Overworld_FieldMoves.rb',1,48)])
u(PARTY,1258,1287,'奶招连续循环','用量至少1且等于总HP整除5；来源HP须大于用量；拒自己/蛋/濒死/满血；每次来源扣固定量，目标恢复受上限夹限，保留原来源身份和位置。',[link(82),link(64),link(240)], [ev(ITEM,333,338),ev(POKE,244,250)])
u(PARTY,1288,1313,'场地招提交与FLY取消','可用性、确认通过后关屏；FLY取目的地才写字段并返回；地图取消重建不传存储许可，选择重置0；其它场地招返回由调用者执行。',[link(81),link(238)], [ev(S+'016_UI/001_UI_PauseMenu.rb',166,185),ev(S+'012_Overworld/004_Overworld_FieldMoves.rb',1,48)])
u(PARTY,1314,1330,'Summary注册','Summary总有并打开摘要，返回更新帮助与队伍面板。',[link(70),link(78)])
u(PARTY,1331,1339,'Debug注册','Debug仅调试；细节排除正常范围。',[link(70),link(79)])
u(PARTY,1340,1351,'Switch注册','多成员才有命令；保留来源旧索引，目标选择使用菜单模式；按USE才尝试交换。',[link(59,64),link(80),link(233)])
u(PARTY,1352,1373,'邮件命令','非蛋且有效邮件才有Mail；子菜单Read/Take/Cancel，Read不重拍快照，Take成功才刷新。',[link(70),link(83,84),link(127)], [ev(MAIL,34,98),ev(ITEM,825,854),ev(POKE,586,599)])
u(PARTY,1374,1393,'物品父菜单','非蛋且无有效邮件才有Item；菜单条件每次重新计算、末尾Cancel，负/末尾选择不执行。',[link(70,72)], [ev(MENU,80,116)])
u(PARTY,1394,1407,'Use子命令','内嵌过滤选择后对原成员使用；取消不调用领域处理；返回单槽刷新。',[link(85),link(93),link(103,104),link(210)], [ev(ITEM,710,752)])
u(PARTY,1408,1420,'Give子命令','内嵌选择可携带物品，成功给予才单槽刷新；原持物与邮件的前序变化由领域入口决定。',[link(86),link(101)], [ev(ITEM,781,823)])
u(PARTY,1421,1431,'Take子命令','有持物才提供；取回成功才刷新；容量和邮件前门由取回入口决定。',[link(87),link(102)], [ev(ITEM,825,854)])
u(PARTY,1432,1485,'Move子命令','捕获来源对象和旧物身份；Box Link可改变来源状态而不刷新捕获值。蛋拒绝、目标邮件只提示拒绝不自动取邮件，空手转移/普通持物交换按捕获值提交。',[link(88),link(105),link(111,123)], [ev(STORAGE,1902,1934)],note='A16明确目标邮件仅拒绝，正文“须先取邮件”应按该门解释。')
u(PARTY,1486,1503,'全局主入口','从当前玩家队伍打开完整主菜单；返回值由淡入淡出包装消费，领域执行另由暂停菜单负责。',[link(20)], [ev(S+'016_UI/001_UI_PauseMenu.rb',166,185)])
u(PARTY,1504,1524,'事件选人','有处理器走资格模式，无处理器普通选择；正常返回才写索引和名称，取消写-1和空名称。',[link(23),link(131)])
u(PARTY,1525,1533,'非蛋与可用选择','两谓词不同：非蛋允许濒死；可用要求非蛋且正HP。',[link(131)])
u(PARTY,1534,1554,'交易助手默认分叉','未传处理器走普通选择，无附加拒绝；传处理器才走交易资格模式；正常返回写变量。',[link(24),link(131)])
u(PARTY,1555,1560,'按物种交易选择','目标物种正规化为基身份，提供资格处理器，因此叠加交易拒绝门。',[link(24),link(131)])
# Summary.
u(SUMMARY,1,56,'招式光标','普通四槽与学招第五槽布局区分；预选与选中图形不同。',[link(174),link(192)])
u(SUMMARY,57,99,'缎带光标','四列光标，窗口只显示12个范围内的位置，预选光标可在滚动后隐藏。',[link(164),link(178)])
u(SUMMARY,100,182,'摘要开场','初始页1，引用当前容器与索引；战斗标志仅后续选项门消费；先请求个体图再显示各页；文字窗两行逐字。',[link(136,140),link(225),link(242)], [ev(POKE,147,179),ev(SPRITE,4,75),ev(S+'010_Data/002_PBS data/009_Species_files.rb',92,108)])
u(SUMMARY,183,208,'遗忘首次显示','遗忘/查看在输入循环前绘制首招详情；零招式先访问缺失招式属性失败，无法BACK；新招可选第五槽。',[link(192)], [ev(SUMMARY,814,845)])
u(SUMMARY,209,216,'摘要正常结束','正常退出释放视图和图集；主体中途异常不会到达此清理。',[link(263)],verdict='STRUCTURE_ONLY')
u(SUMMARY,217,236,'摘要普通显示','忙时USE恢复；全显后USE/BACK关闭，逐字暂停与普通关闭分开。',[link(242)], [ev(WINDOW,300,387),ev(WINDOW,526,580)])
u(SUMMARY,237,266,'摘要确认','默认Yes，BACK false；只有不忙时才恢复或返回，忙暂停没有恢复分支。',[link(242)], [ev(WINDOW,300,387),ev(WINDOW,526,580)])
u(SUMMARY,267,291,'摘要命令菜单','初始索引参数默认0；先更新命令窗口，随后BACK优先USE；退出编码-1。',[link(186)])
u(SUMMARY,292,302,'标记显示','缺失槽按零显示，显示值上限取图集变体数减一；显示不填齐个体原标记数组。',[link(144),link(182)], [ev(POKE,1159,1227)],verdict='STATIC_SUPPORTED')
u(SUMMARY,303,378,'摘要公共头部','蛋独立页；非蛋显示球、状态优先级、治愈病毒、闪光、性别、等级、持物和标记；每次绘页重新请求个体图/图标。',[link(144),link(225)], [ev(POKE,147,179),ev(SPRITE,4,75)])
u(SUMMARY,379,480,'INFO页','National优先，否则首已解锁区域，若首区域无种即停；Shadow换心量表文字但经验条请求只受最大等级门，不受Shadow门。',[link(145)], [ev(POKE,231,238),ev(S+'014_Pokemon/003_Pokemon_ShadowPokemon.rb',93,140)],verdict='CONFLICT',note='R6-UI-PARTY-003；实际背景像素与最终可见性UNKNOWN，静态已证的是绘制请求。')
u(SUMMARY,481,541,'蛋页','蛋页获得日期/地点、自定义来源优先、无地图时蛋文案；孵化文案阈值严格小于10200/2550/1275；同宽268格式化。',[link(140),link(148)], [ev(DRAW,1035,1040),ev(DRAW,580,659)])
u(SUMMARY,542,639,'备忘录与个性','心阶段>3隐藏性格和个性；来源文本优先；孵化记录条件显示；最高IV按指定次序从个人ID余数开始取首个最大，描述余5档。',[link(146,161)], [ev(DRAW,1035,1040),ev(DRAW,580,659)])
u(SUMMARY,640,691,'能力页','按计算用性格决定能力名颜色、Shadow阶段门；特性描述最多两行；正HP才画比例HP条。',[link(162)], [ev(POKE,244,250)])
u(SUMMARY,692,739,'招式概览','有效招显示成员相关类型、名称和PP四档，非正总PP无PP字；空槽占位；不会在本页请求空招详情。',[link(163),link(174)])
u(SUMMARY,740,813,'招式选择布局','学习模式额外第五槽，当前列表与新招各自类型/名称/PP；还绘成员类型。',[link(174),link(192)])
u(SUMMARY,814,845,'选中招式详情','调用选中招式的显示威力/命中/类别与描述；零/变量威力及零命中占位；缺失首招早失败。',[link(174),link(192)])
u(SUMMARY,846,898,'缎带显示','每窗口12枚与总数；详情显示选中缎带名和描述，空位详情为空；概览本身隐藏箭头。',[link(164),link(178)])
u(SUMMARY,899,928,'切换成员','前后不回绕，跳空槽且页1之外跳蛋；换成员停音请求新叫声。',[link(168)], [ev(POKE,99,105)])
u(SUMMARY,929,993,'招式换位','首次详情后循环，BACK取消当前换位或退出；USE两段整体交换记录；Shadow不进入换位；方向在已知招间循环。',[link(174),link(223)], [ev(POKE,605,615)])
u(SUMMARY,994,1077,'缎带换位','四列网格，至少三行，上下循环；已存在来源才预选；提交两槽交换后压缩空位、修正目标及滚动，立即写入。',[link(178),link(223)])
u(SUMMARY,1078,1192,'标记编辑','使用副本；USE缺失槽按零循环，ACTION缺失槽直接比较导致异常。BACK/Cancel弃副本，OK选出编辑值，差异才整体写回。',[link(182)], [ev(POKE,1159,1227),ev(S+'002_Save data/005_Game_SaveConversions.rb',301,312),ev(STORAGE,1328,1407)],verdict='CONFLICT',note='R6-UI-PARTY-001；空数组是默认合法状态，不能把显示零值当作已补齐数组。')
u(SUMMARY,1193,1231,'摘要选项','非蛋Give、持物时Take、持图鉴时View；Mark含蛋；图鉴先登记最近见到，再打开完整单种；给物传当前容器索引。',[link(186,188)], [ev(ITEM,781,854),ev(MAIL,100,125),ev(S+'015_Trainers and player/005_Player_Pokedex.rb',222,228)])
u(SUMMARY,1232,1269,'遗忘选择输入','BACK和第五槽返回-1；USE当前旧槽返回索引；上/下按现有招式数与新槽选择。',[link(192)])
u(SUMMARY,1270,1341,'摘要主循环','ACTION停音请求叫声；BACK退出；USE分别进入招式/缎带或非战斗选项；成员切换和页变化才刷新；页面夹住。',[link(140),link(168),link(186)])
u(SUMMARY,1342,1354,'摘要屏幕包装','开场、主循环、正常收尾，返回最终成员位置；异常不保证收尾。',[link(136),link(168)])
u(SUMMARY,1355,1367,'HM门','只有学习新招且旧槽有效时拒非调试HM；查看选择没有HM拒绝；取消正常返回。',[link(192)], [ev(ITEM,630,638)])
u(SUMMARY,1368,1384,'必选入口','查看首绘后提示；BACK结果-1被外层重新提示，直到有效槽；固定脚本搜索仅定义，无静态调用者。',[link(192),link(258)],note='负证据仅固定Data/Scripts，未证明Demo、插件或动态调用不可达。')
u(SUMMARY,1385,1400,'全局事件选招','空个体直接早退不写变量；非空用可取消查看选择，正常返回后写索引/名称并请求地图刷新，零招首绘失败不会写结果。',[link(192),link(258)],note='空个体早退是额外入口边界，正文未明写；不等同零招失败。')
# Reminder.
u(RELEARN,1,18,'重学消息','普通显示/确认委托共享帮助；两行忙暂停门与Party局部实现有共同结果但独立路径。',[link(218),link(242)], [ev(HELPER,198,274),ev(WINDOW,300,387)])
u(RELEARN,19,51,'重学开场','把候选名称交命令窗，首次画列表与详情在任何选择输入前；空候选不会被拦截。',[link(216,217)], [ev(S+'010_Data/001_GameData.rb',78,108),ev(S+'001_Technical/001_Debugging/004_Validation.rb',1,31)])
u(RELEARN,52,109,'重学详情','四项可见，滚动对应当前候选；总PP用满/满或占位；严格查当前招式后显示威力/命中/类别/描述及可向上/下提示。',[link(216,217)], [ev(S+'010_Data/001_GameData.rb',78,108),ev(S+'001_Technical/001_Debugging/004_Validation.rb',1,31)])
u(RELEARN,110,140,'重学选择与结束','命令变化才重画，BACK nil、USE候选身份；正常关闭释放资源。',[link(218)])
u(RELEARN,141,166,'候选去重与顺序','非空非蛋非Shadow；先保等级表未会首现序，再把不与等级候选重叠的未会最初记录放前，最后去重。重叠记录不移前。',[link(216)], [ev(POKE,610,621),ev(POKE,681,704),ev(R+'PBS/pokemon.txt',3,29)],verdict='CONFLICT',note='R6-UI-PARTY-002；WP30 §6.3正文已有正确非重叠门。')
u(RELEARN,167,190,'教学与取消层次','选招确认才通用教学；成功才计重学统计并true；内层false回列表；BACK后退出确认，否继续，是false。',[link(218),link(253)], [ev(ITEM,582,638),ev(S+'014_Pokemon/004_Pokemon_Move.rb',4,52)])
u(RELEARN,191,199,'重学全局包装','淡入淡出包装转交结果；没有空候选预检，也无领域提交事务恢复。',[link(27),link(216),link(258)])
# Naming.
u(TEXT,1,65,'旧自由字符菜单','字库网格定义空格/换字库/OK三特殊命令；固定USEKEYBOARD=true时总入口不会走此分支。',[],verdict='INVENTORY_ONLY',note='已全文语义读取；非默认分支不自动变成未来必需API。')
u(TEXT,66,76,'键盘场景内部选择','自由命名场景固定开启键盘输入，旧字符网格受内部常量门；用户模式路由与此门不同。',[link(171,path=TEXTSPEC)],verdict='STATIC_SUPPORTED')
u(TEXT,77,179,'键盘开场与预览','初值不截短，上限只存；文字输入开启；玩家/个体/NPC/箱预览按主题分叉；min0才显示Esc取消帮助。',[link(171,178,path=TEXTSPEC),link(220,path=TEXTSPEC)], [ev(EDIT,4,47),ev(EDIT,125,137),ev(S+'015_Trainers and player/003_Trainer_Sprites.rb',1,68)])
u(TEXT,180,199,'键盘确认先于编辑','每轮Input刷新后先ESCAPE(min0)，再RETURN(min达标)，再更新编辑窗；同轮文字串与合法RETURN不保证文字串被插入。',[link(176,path=TEXTSPEC),link(267,path=TEXTSPEC)], [ev(EDIT,226,259)],note='明确先检查退出后更新编辑，未执行真实输入组合。')
u(TEXT,200,244,'旧字库输入分支','USE可空格/切组/插字/确认，确认查上下限；固定常量门使普通总入口不进入。',[],verdict='INVENTORY_ONLY')
u(TEXT,245,255,'键盘正常关闭','选定内部输入方式；正常结束才关闭文字输入开关与释放；不恢复进入前开关值，无统一异常确保。',[link(267,path=TEXTSPEC)], [ev(EDIT,226,259)])
u(TEXT,256,275,'光标字符数据','四组精确13列5行数据与六控制；同类空白格可达与整列全空分开。',[link(180,206,path=TEXTSPEC)])
u(TEXT,276,370,'命名光标图形','字符光标按13列定位；模式/删除/OK用独立位置皮肤；其属性/资源更新只是视觉结构。',[link(185,196,path=TEXTSPEC)],verdict='STATIC_SUPPORTED')
u(TEXT,371,490,'光标场景开场','初始文本助手保持全文；建立max个下划线和字组；首次淡入回调会调用更新，非正max在光标夹限处先失败。',[link(172,path=TEXTSPEC),link(213,215,path=TEXTSPEC)], [ev(EDIT,4,30)])
u(TEXT,491,519,'命名文字显示','刷新标记控制重画，文本按字符显示；不因上限设置而截断。',[link(172,path=TEXTSPEC),link(224,path=TEXTSPEC)], [ev(EDIT,4,30)])
u(TEXT,520,553,'字组动画','切组期间隐藏光标、两个字组动画交换，最后更新模式与光标；期间不裁决业务按键，音效仅请求。',[link(180,path=TEXTSPEC)])
u(TEXT,554,568,'下划线与上限失败','文本光标夹到0..max-1；max0/负在第一次回调夹逆序区间失败，主输入和结束未到；正常max更新下划线。',[link(213,215,path=TEXTSPEC)],note='按参考使用的宿主夹限合同推导ArgumentError；未运行游戏或参考脚本。')
u(TEXT,569,583,'整空列','第12列永不跳过；其它列仅当当前组五行全为空格才视为可跳；回绕是正模。',[link(185,196,path=TEXTSPEC)])
u(TEXT,584,665,'光标方向与控制','LEFT/RIGHT/UP/DOWN优先顺序；字符区行内回绕、左右跳整空列；边缘到控制、控制到代表列；实际位置变化才消费此轮。',[link(185,208,path=TEXTSPEC)])
u(TEXT,666,723,'光标编辑与提交','移动实际改变先消费；其余SPECIAL/ACTION/BACK/USE优先；ACTION只定位OK，BACK删字。满长先删末字再插，达max跳OK；首组插后位置1就切小写；OK先音再最小长度门。',[link(177,180,path=TEXTSPEC),link(208,path=TEXTSPEC)], [ev(EDIT,4,65)])
u(TEXT,724,733,'光标正常释放','正常结束淡出、释放字组与各精灵；中途异常不会到达，外层状态恢复未穷尽。',[link(267,path=TEXTSPEC)],verdict='STRUCTURE_ONLY')
u(TEXT,734,749,'命名包装','开场→输入→正常收尾→返回文本，领域名称写入在各调用者，不在本入口。',[link(171,181,path=TEXTSPEC)])
u(TEXT,750,770,'用户模式路由','选项1键盘、其余光标，选项读取异常回光标；包装淡入淡出转交文本。',[link(171,path=TEXTSPEC),link(273,path=TEXTSPEC)])
u(TEXT,771,786,'主题入口','玩家/个体/NPC/盒名只传主题与相应预览对象；盒子调用者非空返回才覆盖盒名，空返回意义由调用者决定。',[link(171,path=TEXTSPEC)], [ev(STORAGE,1228,1235)])
# Structural denominator is separated from interpretation, including every method declaration.
for row in units:
    if row['unit_id'] in ['R6-UI-party-P018','R6-UI-party-P029','R6-UI-party-P034']: row['formal_links'].append(link(222))
    p=row['source']['path']; lines=frozen(p).decode().splitlines()
    row['inventory_units']=[{'declaration_line':i,'trace_name':m.group(1)} for i,line in enumerate(lines,1) if row['source']['start_line']<=i<=row['source']['end_line'] and (m:=re.match(r'\s*def\s+([^\s(;]+)',line))]
    row['semantic_read_completed']=True
# Add hand-reviewed dependency facts, without implying full files were reviewed.
depfacts=[
('D001',ITEM,582,638,'通用教学拒绝、满槽取消与整体替换；替换早于三条消息，机械友好变化在消息后。',[link(200,205)]),
('D002',ITEM,644,752,'背包/队伍使用机器包装不同；数量与库存取小，普通使用清注解硬刷新后才消耗。',[link(95),link(103,104),link(209,212),link(231)]),
('D003',ITEM,781,854,'给物/取回的蛋、邮件与容量门；邮件取消可保留旧物入袋及原邮件入箱，取回门先查袋容量。',[link(101,102),link(224),link(234,235)]),
('D004',MAIL,1,125,'邮箱容量10；阅读消费旧快照；写作空文本可确认放弃，三快照依次取队伍k+2、k+1、实际目标。',[link(127),link(188),link(101)]),
('D005',TUTOR,428,497,'机器背包资格注解包装、成功统计/TR最初记录追加；按引用个体在选择后检查。',[link(209,212)]),
('D006',EFFECTS,1216,1375,'PRISONBOTTLE形态回调的刷新读取；融合保原主体引用，在第二选择后写融合/删除/刷新/换工具。',[link(109)]),
('D007',FORMS,422,432,'FURFROU五日严格超时门，动态提交后清时间；形态设定清特性缓存并重算登记。',[link(225)]),
('D008',WINDOW,300,580,'自动行满插暂停、busy/resume与更新合同；局部确认不在忙状态恢复，普通显示具有恢复。',[link(242),link(94,95,path=TEXTSPEC)]),
('D009',DRAW,580,665,'格式化文本按词边界和额外2单位换行，行首长串不硬拆；摘要宽268消费此路径。',[link(148)]),
('D010',RULES,1,215,'最少人数门、逐成员有效与团队校验；有效队伍前门与提交门不同。',[link(132),link(236)]),
('D011',EDIT,4,259,'字符助手按字符计数，初值不截短，插入重建文本而非原地改初值；键盘箭头/退格/Enter/Esc优先于文字串。',[link(172,178,path=TEXTSPEC),link(224,225,path=TEXTSPEC)]),
('D012',S+'007_Objects and windows/011_Messages.rb',821,859,'自由文本ESC返原文，正常关闭输入开关，无内部地图微更新，外部回调异常跳过清理。',[link(178,path=TEXTSPEC),link(267,path=TEXTSPEC)]),
('D013',S+'015_Trainers and player/003_Trainer_Sprites.rb',1,68,'命名行走第一方向四帧.5秒，箱横四帧.4秒由调用者设置，全局时钟相位。',[link(220,path=TEXTSPEC)]),
('D014',S+'010_Data/001_GameData.rb',78,108,'招式严格ID校验拒绝空候选；参数验证抛ArgumentError，早于选择循环。',[link(216),link(237)]),
('D015',POKE,1159,1227,'正常创建标记为空数组；摘要读图只用零显示替代缺失槽，没有补齐写入。',[link(182)]),
('D016',S+'001_Settings.rb',11,20,'固定代际8；重学更多开、机器保留旧PP关、队伍6、桥禁用开关35、图鉴偏移空表，条件分别由已读配置段支持。',[link(252)])]
for fid,p,a,b,fact,refs in depfacts:
    units.append({'unit_id':'R6-UI-party-'+fid,'source':ev(p,a,b),'classification':'UI dependency','review_level':'semantic','fact':fact,'formal_links':refs,'assessment':'STATIC_SUPPORTED_DEPENDENCY_RANGE','semantic_read_completed':True,'necessary_consumer_evidence':([ev(S+'001_Settings.rb',129,155),ev(S+'001_Settings.rb',207,258),ev(S+'001_Settings.rb',378,396),ev(S+'001_Settings.rb',311,321)] if fid=='D016' else []),'reference_execution':'NOT_EXECUTED','host_demo':'UNKNOWN'})
jsonl('forward-matrix.jsonl',units)
# Reading ledger: delivered ranges are only used to locate the already interpreted content.
notes={
PARTY:'已审面板状态/HP与注解门、局部消息/确认、方向与选择优先序、硬刷新、给予/邮件、资格快照、多选、主菜单与奶招/FLY、默认注册、持物旧值与事件写回。',
SUMMARY:'已审开场与首招首次绘制、公共/蛋/INFO/备忘录/能力/招式/缎带显示、成员切换、两段换位、标记副本与缺失槽ACTION、选项登记、可取消/HM/必选/全局事件结果。',
RELEARN:'已审共享消息消费者、开场前候选名称和首选严格ID查询、列表/详情、空候选失败、等级候选与非重叠最初记录去重序、教学与三层取消。',
TEXT:'已审键盘开关/长度/退出先于编辑、内部旧字库门、四组字符数据、主题预览、非正max首次回调失败、整空列、方向/操作同轮优先序、替换末字与OK门、正常释放及路由。',
SPEC:'正文所有174个非空条款块已语义审读；四处候选冲突与边界/跨包前提分别列入反向矩阵，阅读不等于PASS。',
TEXTSPEC:'全篇作为文本域与共享消息上下文读取；仅§6.2/6.3、局部确认及正常清理交界在本子域反向核源，其它WP17行为不重复承诺独立全审通过。',
CAT:'已解释本次送达的案例与共同前提；正式核源范围限PT41及命名、B16、MV、WR、M10的本域贡献，其它表行只作上下文不宣称通过。',
ITEM:'已审通用教学/HM包装、背包和队伍机器包装差异、HP恢复、物品资格、数量/刷新/消费、邮件交换与取回的真实顺序和局部失败。',
MAIL:'已全文解释邮件对象、容量与取回、旧字段快照阅读、自由文本写作的空文放弃和k+2/k+1/实际目标次序。',
POKE:'已审本次范围中的动态/简单形态与提交副作用、经验比例、HP夹限、持物/邮件自清、招式数/学习/最初记录、初始化空标记；其余个体模块未因本次读取声称全审。',
EDIT:'已解释字符计数/光标/插入容量/原文重建、文本框上限与渲染、键盘服务输入优先序；多行组件只有开头作上下文。',
HELPER:'已解释共享普通显示/确认的busy门、可见性暂存与正常恢复、数量BACK优先，后段未读部分未纳入全量通过。',
FORMS:'已核FURFROU严格五天与HOOPA三天读取/提交回调，其它邻近形态只作上下文。',
TUTOR:'已核资格注解、后选成员资格门、教学成功统计/TR追加和正常退出，前置前段428–450额外核了蛋/已会/兼容注解的具体顺序。',
RULES:'已解释人数最小/最大、资格守卫、有效队伍与确认团队校验差别；后续规则模块不属本次全文件范围。',
WINDOW:'已解释格式化自动插暂停、busy/pausing/resume与更新时序，确认与普通显示消费者分别核到，非此范围窗口功能未重复全审。',
MENU:'已解释菜单注册可用条件、排序默认与动态名称，事件集合邻近部分为结构上下文。',
SPRITE:'已解释个体图请求动态形态、图标按HP相位/选中偏移/空输入；本次物种图标开头为上下文，实际图集UNKNOWN。',
EFFECTS:'已核机器UseFromBag、进化石注解显式刷新、PRISONBOTTLE与KYUREM融合引用/部分提交，邻近其它效果保持限定。',
STORAGE:'已解释本次读到的Box Link整理开/关储存标志、队伍Item取回、盒名非空覆盖、直接盒标记与Summary不同的ACTION门；未把存储整文件全审转移为本子域结论。',
DRAW:'已核无控制/有控制格式化选择、两条宽度换行门、显式换行和摘要消费者；未证字体、裁切或实际像素。',
S+'001_Settings.rb':'已核本次配置范围中的代际8、队伍6、旧PP仅世代5、重学更多>=6、开关35与图鉴偏移空表，其它配置仅上下文。',
S+'001_Technical/001_Debugging/004_Validation.rb':'已全文解释类型/能力验证的ArgumentError边界；用于空重学首候选失败类别。',
S+'010_Data/001_GameData.rb':'已核严格符号数据查询与参数类型验证，空参数失败早于未知合法ID分支。',
S+'010_Data/002_PBS data/009_Species_files.rb':'已核从个体请求图像时读取当前形态，先读取后匹配；实际解析结果UNKNOWN。',
S+'015_Trainers and player/001_Trainer.rb':'已核删除位置守卫：最后可用不能删，融合调用者忽略其false而继续后续；其余训练家能力不在本读段。',
S+'014_Pokemon/004_Pokemon_Move.rb':'已核新招记录初始化PP提升0与当前PP满、PP夹限和总PP；其它显示数据不重复全审。',
S+'014_Pokemon/003_Pokemon_ShadowPokemon.rb':'已核Shadow判定/阶段、制作Shadow不改当前exp、心门与Hyper；只用于摘要经验条对照，不推战斗经验业务。',
S+'007_Objects and windows/011_Messages.rb':'已核自由文本开关、Esc原文、Return编辑文、正常清理与消息包装，无内建地图微更新。',
S+'015_Trainers and player/003_Trainer_Sprites.rb':'已全文解释行走/箱图切片和全局时钟帧相位、正常释放及缺失预览空图。',
S+'013_Items/007_Item_Sprites.rb':'已核物品横条方帧/全局时钟、blankzero独立空值隐藏和默认返回图、持物提示每次更新读当前物品；真实图集未查。',
S+'010_Data/002_PBS data/006_Item.rb':'已核can_hold/consumed的领域门与机器分类交界，未重复整个物品数据模块全审。',
S+'002_Save data/005_Game_SaveConversions.rb':'已核旧整数标记迁移仅作用Integer，默认空数组不被此转换填齐。',
S+'016_UI/001_UI_PauseMenu.rb':'已核队伍数前门、隐藏招结果在菜单外执行，普通退出刷新暂停菜单。',
S+'012_Overworld/004_Overworld_FieldMoves.rb':'已核已登记处理器门、默认确认真与可用/执行三个独立阶段；未声称具体场地规则全审。',
S+'018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb':'已核报名UI正常返回后才setParty；局部多选异常尚未返回，报名赋值未到；nil取消和空数组边界独立。',
FORMAL+'combat-requirements/wp55-facility-session-and-restoration.md':'已核报名返回/写入交界§2.3，非空/空数组/nil三态保持；局部UI异常不授予正常返回。',
S+'018_Alternate battle modes/002_Battle Frontier rules/003_Challenge_EntryRestrictions.rb':'已核SpeciesClause按基物种身份拒重复，错误文案正常非空；其它条款未重复全审。',
S+'015_Trainers and player/005_Player_Pokedex.rb':'已核Summary最近见到登记含性别/图鉴形态/异色，调用前写入与条目显示分开。',
R+'PBS/items.txt':'已核默认TM57实际FieldUse TR与CHARGEBEAM身份，名称不等于分类；只读该条。',
R+'PBS/pokemon.txt':'已核默认MAGNEMITE兼容CHARGEBEAM而升级表无此招；BULBASAUR低等级TACKLE/GROWL顺序与合法最初记录反例所需数据。',
FORMAL+'creature-rpg/wp30-growth-learning-and-friendship.md':'已语义对照§6.3非重叠前置规则与UI概括的冲突；正文其余未全量逆向核源。',
FORMAL+'creature-rpg/wp18-creature-identity-species-ownership.md':'已核§4创建输出明确空标记，与默认源初始化一致；其它内容不因局部读取通过。'
}
delivered=[json.loads(s) for s in (OUT/'delivery-ledger.jsonl').read_text().splitlines()]
range_notes={(TUTOR,1,27):'已解释组合后继索引推进与结束门，三选二[0,1]→[0,2]→[1,2]后结束，无修改原队伍；与28–47枚举消费者合读。',(TUTOR,28,66):'已解释固定组合助手的边界与按索引枚举；三成员取2会产生[A1,A2]、[A1,B]、[A2,B]，供多选有效队伍前门核查；随机组合邻近范围仅上下文。',
(PARTY,1,400):'已解释按钮/蓝色命令变更、空槽及成员面板创建/缓存/选择状态优先、HP背景注解门、图标定位、名字等级性别；第400行HP函数由下段接续。',
(PARTY,401,800):'已解释HP/状态/闪光/注解绘制、缓存更新、开场许可/按钮、显示/确认/命令/数量、换位演出、摘要/背包借用和完整选择输入出口。',
(PARTY,801,1200):'已解释方向确定转移、硬/软刷新、给予/邮件失败、转发与未调用限制、换位和简单PP选招、注解刷新、多选错误后旧命令可沿用、资格/交易快照；交易返回接下段。',
(PARTY,1201,1560):'已解释主菜单三门/排序/场地招插入、奶招源保留和FLY重建丢许可、默认菜单子命令、Move捕获旧物、全局事件/默认交易四前提及变量写回。',
(SUMMARY,1,400):'已解释招式/缎带光标、摘要与遗忘开场、首招详情初绘、局部消息/确认/命令、标记显示缺失槽按零、公共头部、INFO心量表开头；INFO后段接下一范围。',
(SUMMARY,401,800):'已解释INFO首地区图鉴门/主人/心量文字及独立经验条请求、蛋页严格阈值、宽268备忘录、IV轮转、能力性格着色/HP、招式PP四档和学习额外槽布局。',
(SUMMARY,801,1200):'已解释选中招式详情空值失败、缎带显示与详情、成员边界、招式/缎带即时换位、标记副本/USE/缺失槽ACTION异常/OK提交、选项开头。',
(SUMMARY,1201,1400):'已解释摘要给物/取物/最近见到登记/Mark、遗忘选择和HM门、主输入夹页与战斗选项门、屏幕正常结束、必选未调用、事件选招nil早退及正常变量写回；多选空摘要调用在持物读取前失败。',
(RELEARN,1,199):'已全文解释共享消息、开场首选严格ID、四项列表详情、候选非重叠最初项前置、选择/教学/三层取消/成功统计、全局包装；空候选首绘失败前提分开。',
(TEXT,1,400):'已解释旧字符窗非默认门、键盘开场/预览/输入开关/长度、退出先于编辑、旧字库输入、正常释放、四组字库和光标类型/定位、光标场景建立开头。',
(TEXT,401,786):'已解释主题预览、下划线建立与非正max淡入失败、叠层/字组动画、整空列、13x5和控制导航/同轮优先、光标编辑/确认/自动切组、正常释放及用户模式/主题包装。'}
ledger=[]
for i,d in enumerate(delivered,1):
    assert d['path'] in notes, d['path']
    semranges=[d['range']]
    if d['path']==SPEC and d['range']==[1,265]:semranges=[[1,119],[176,265]]
    ledger.append({'reading_id':f'party-read-{i:03d}','path':d['path'],'commit':d['commit'],'sha256':d['sha256'],'delivered_range':d['range'],'semantic_ranges':semranges,'semantic_read_completed':True,'semantic_note':range_notes.get((d['path'],*d['range']),notes[d['path']]),'review_completed_at':now,'delivery_status':'DELIVERY_ONLY_NOT_PASS','semantic_verdict':'INTERPRETED_NOT_AUTOMATIC_PASS','truncation_note':'首次长输出中段截断；120–175另一次完整读取补齐，联合覆盖1–265。' if d['path']==SPEC and d['range']==[1,265] else None})
jsonl('reading-ledger.jsonl',ledger)
# Candidate findings: review prose only, no source expressions reproduced.
den=json.loads((ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/inventory/formal-block-denominator.json').read_text())
common={'status':'PENDING_NON_PROPOSER_COUNTERREVIEW_AND_ROOT_ADJUDICATION','proposer':'party','non_proposer_counterreview_required':True,'reference_observation':'STATIC_READING_ONLY_NOT_EXECUTED','independent_model':'DERIVED_VECTOR_NOT_REFERENCE_RUNTIME','host_demo':'UNKNOWN','real_resources':'UNKNOWN','real_input':'UNKNOWN','sound':'UNKNOWN','source_commit':REF,'formal_commit':MAIN,'compatibility_decision':'实现阶段兼容选择保留；此轮仅修正参考行为描述。'}
findings=[]
def finding(fid,title,severity,source,spec,pre,ordinary,ce,cancel,neg,consumer,impact,revision,accept,regression,sync):
    findings.append(dict(common,formal_clause_ids=[d['id'] for d in den if any(e['path']==d['path'] and not(d['end_line']<e['start_line'] or d['start_line']>e['end_line']) for e in spec)],id=fid,title=title,severity=severity,classification='User Interface',source_locations=source,formal_locations=spec,preconditions=pre,ordinary_control=ordinary,minimal_counterexample=ce,cancellation_exception_partial_commit=cancel,negative_evidence_scope=neg,necessary_consumers=consumer,impact=impact,minimal_revision=revision,acceptance=accept,regression_dependencies=regression,scope_synchronization_files=sync))
syncbase=[SPEC,CAT,FORMAL+'audit/source-traceability.md','planning/feature-matrix.md (root-owned coverage update if accepted)']
finding('R6-UI-PARTY-001','默认空标记槽的ACTION在提交前失败，正文仅描述安全清零','MEDIUM',
[ev(SUMMARY,1078,1192),ev(POKE,1159,1227),ev(S+'002_Save data/005_Game_SaveConversions.rb',301,312)],
[link(182),link(186),link(227),ev(CAT,231,231),ev(CAT,236,236)],
'默认新建合法个体，markings为空列表，依赖及六槽标记资源已正常构建且变体数至少2；非战斗摘要INFO页打开Mark，初始焦点槽0；ACTION独立触发，BACK/USE/方向均不触发，无插件或外部补齐。',
'相同初态直接BACK：正常返回未变更，原空列表保持。相同初态槽0先USE得到本地1，再ACTION清为本地0，后BACK原空列表不写。已明确六个数值零的标记列表，ACTION空槽只无操作。',
'未做任何槽编辑直接ACTION槽0：画面以零显示该缺失槽，但清除门把缺失值当数值比较，抛NoMethodError，早于后续取消、OK写回及隐藏编辑层。并非“空槽ACTION无效果”。',
'原个体标记未写；此前其它摘要/领域写入不由此撤回。若先改槽0再移槽1触发，同一编辑副本的临时改动尚未提交；本地正常清理和摘要正常结束未到达，外层恢复/错误窗/进程退出未知。BACK与ACTION同轮时BACK先处理，可正常退出；不能把独立ACTION异常推广所有组合。',
'全文Summary1–1400，初始化1159–1227，固定Data/Scripts所有markings出现处搜索；旧迁移仅Integer，不补默认空数组。显示读取和Mark开场只克隆/显示，没有填齐。Storage1328–1407没有ACTION清零分支，是不同入口；插件与动态调用未知。',
[ev(PARTY,705,713),ev(SUMMARY,1193,1231),ev(SUMMARY,1270,1335),ev(SUMMARY,1348,1352),ev(STORAGE,1328,1407)],
'常见默认状态的一次合法编辑手势不能完成局部流程；另一实现若按正文统一空值为零，会把历史异常消除但仍被当作参考等价。风险是局部UI异常，无宿主崩溃证据。',
'§6.3增加缺失槽与显式0的区别：显示把缺失槽当零不写回；ACTION缺失槽在当前参考中发生提交前异常。保留副本、USE、OK差异写入和正常取消合同；不更改域创建默认空列表、不要求未来复用源API。',
'补具名静态正例和邻近反向：默认[] ACTION；[0,0,0,0,0,0] ACTION；[] USE→ACTION→BACK；编辑另一槽后缺失槽ACTION；ACTION+BACK。分别登记原值/本地副本/返回/清理到达，并保持NOT_EXECUTED。非提出者须从初始化到消费者复核是否有补齐写入。',
['PT A30/A35','WP18创建空标记','Storage直接Mark取消/提交','摘要正常Mark后页刷新','两行确认暂停条款'],syncbase+[FORMAL+'creature-rpg/wp18-creature-identity-species-ownership.md (retain default, no domain change)'])
finding('R6-UI-PARTY-002','重学中与等级候选重叠的最初招式不移到列表前端','MEDIUM',
[ev(RELEARN,150,165),ev(POKE,610,621),ev(POKE,681,704),ev(R+'PBS/pokemon.txt',3,29)],
[link(216),ev(CAT,232,232),ev(CAT,600,600),ev(FORMAL+'creature-rpg/wp30-growth-learning-and-friendship.md',170,172)],
'默认更多候选开启，合法非蛋非Shadow BULBASAUR等级2，当前只掌握兼容的AMNESIA，最初记录为[GROWL]；当前未会TACKLE/GROWL，正常资料/资源及首绘，无其它候选、插件或改写。最初记录可由既有记录编辑入口保留，不声称Demo可达。',
'记录为空时候选[TACKLE,GROWL]；记录[CURSE]且未会时（CURSE在默认蛋/教学数据中）候选[CURSE,TACKLE,GROWL]，独有最初记录确实前置。',
'记录[GROWL]与等级候选重叠，源结果仍[TACKLE,GROWL]；正文“最初招式中未会者置于表前”可导出[GROWL,TACKLE]，与WP30 §6.3明写的非重叠条件不一致。旧A31选择与等级表首项重叠，无法区分两种排序。',
'候选计算无学习/统计写入；非空首绘后BACK照常询问退出，拒绝回列表，确认false；教学与HM/满槽取消层次保持，不能改变为新取消策略。',
'全文MoveRelearner1–199及候选产生150–165；升级表、当前已会与最初记录消费已核。没有把重叠等级项移位的后续候选变换；命令窗只按当前候选顺序使用。插件/运行时数据修改未知。',
[ev(RELEARN,19,51),ev(RELEARN,52,109),ev(RELEARN,111,131),ev(RELEARN,167,185)],
'首项默认焦点和玩家可见顺序不同，会让另一实现得到不同的选招/默认确认行为。现有域正文已精确，UI摘要仍可能覆盖掉该前提。',
'§7.3把前置范围改成未会且不在等级候选中的最初记录项；等级重叠项保留等级表首现位置。旧A31与B16-C003原例保留，新增非首位重叠对照；WP30精确条款保持，必要时把其概括行42/228同步限定。',
'补上述具名低等级向量：记录空、[GROWL]、[CURSE]、重复记录及已会记录；核列表首选身份、BACK和教学后统计，不执行参考。非提出者须检验是否后续列表排序推翻源候选顺序。',
['PT A31/A32','B16-A048/C003','WP30 §6.3','背包TR与队伍机器双入口B16-A044','HM/满槽取消'],syncbase+[FORMAL+'creature-rpg/wp30-growth-learning-and-friendship.md (precise clauses retain; summaries align if needed)'])
finding('R6-UI-PARTY-003','Shadow INFO页仍请求经验条，不能把整个经验区当成完全替换','LOW',
[ev(SUMMARY,379,480),ev(POKE,231,238),ev(S+'014_Pokemon/003_Pokemon_ShadowPokemon.rb',93,140)],
[link(145)],
'合法非蛋Shadow个体，当前等级低于最大等级且当前经验在本级内产生非零比例；正常开场、图/类型/数据/文本/绘制全部到达，相关资源有效，无插件覆盖。只比较绘制请求，实际背景遮挡与像素未知。',
'同经验非Shadow显示经验文字并请求同一128像素比例条；Shadow最大等级不请求该条；Shadow本级最小经验时请求宽0，不能据看不见条推出未请求。',
'Shadow进入INFO：显示心量表/阶段而不写Exp文字，但随后最大等级门仍请求经验条。比例1/2的独立夹具请求宽64；源没有Shadow排除门。正文将Shadow替代Exp区并只在非Shadow分支描述Exp条，容易推导Shadow无条。',
'这是显示请求与读取，无新的学习或经验写入；BACK仍正常关闭。显示前的动态形态/缓存提交按§8单独保持；后段资源失败不回滚前序领域变化，外层恢复未知。',
'全文Summary1–1400、独立经验比例231–238、Shadow制作114–140；固定脚本exp_fraction搜索没有个体Shadow覆写。制作Shadow保存额外经验而不重写当前经验；不从默认捕获常取整数等级推出非零比例输入非法。',
[ev(SUMMARY,117,182),ev(SUMMARY,303,378),ev(SUMMARY,1270,1335)],
'静态渲染合同少一条请求，影响兼容测试和资源消费顺序。没有证据可承诺当前背景下条一定可见，也没有真实UI或声音观察。',
'§5.2限定Shadow替换的是经验文字/说明区；说明经验条请求仍按等级<最大等级门，含宽0与正常偶数舍入。不得把静态请求写成已观察到真实像素。',
'新增Shadow/普通×非零比例/零比例/最大等级独立向量，分别记录文字与经验条请求；持续标静态未执行。非提出者须检查背景资源/后序覆盖是否只影响可见性而未消除请求。',
['摘要INFO正常经验条','Shadow心阶段与心量表','最大等级不请求','WP18/WP21显示读取副作用','现有PT A28导航'],syncbase)
finding('R6-UI-PARTY-004','多选校验失败后旧Entry命令可触发空成员摘要，未正常回选择循环','MEDIUM',
[ev(PARTY,1051,1139),ev(PARTY,705,713),ev(SUMMARY,117,182),ev(RULES,176,220),ev(S+'018_Alternate battle modes/002_Battle Frontier rules/003_Challenge_EntryRestrictions.rb',254,268)],
[link(132),link(236),ev(CAT,227,228)],
'有效规则最少/最多2人、仅同物种禁止条款，三名健康合法非蛋成员[A1,A2,B]，A1/A2同一基物种，B不同；每名个体本身合格且存在[A1,B]有效二人队，前门通过。正常资源/文字及场景，无插件。依次选择A1并Entry、A2并Entry，各菜单Entry为第0项；新增满2人后游标自动到CONFIRM，随后USE提交。',
'同初态选A1与B，确认通过直接返回二人数组；同A1/A2选入后在CONFIRM按BACK，取消返回nil，队伍/报名不写。独立同初态首次即确认空选择、此前没有命令值：人数错误消息后可回选择循环，说明并非所有校验失败都同结果。',
'确认[A1,A2]触发重复物种错误，显示首错误并返回后没有跳回选人。第6位是CONFIRM，队伍第6位为空；缺失成员使新菜单不取输入，沿用上次Entry的命令值0，恰与新Summary项0相同，因此打开不存在的第6位摘要。摘要先安全建个体/图标空图，随后读取空成员持物身份，抛NoMethodError，早于下一轮选择或正常nil/数组返回。',
'尚无真实队伍重排、学招或报名提交；选择位次只是本地状态。错误消息已经发生；局部编辑层淡出和新摘要部分分配已执行，但正常摘要/队伍清理未到达，外层异常恢复/错误窗/宿主退出UNKNOWN。错误消息期间BACK只关闭该消息，不能跳过后序旧命令路径；提交前直接BACK正常取消。',
'全文Party1–1560与Summary1–1400；失败分支到后续成员菜单之间无重新选择、continue或命令复位。前门与终门均核Rulesets，真实SpeciesClause已读。默认无插件固定脚本；若上次成员菜单值并非0或异常前资源先失败，不能套此反例。',
[ev(RULES,176,220),ev(TUTOR,1,47),ev(PARTY,1051,1139),ev(PARTY,705,713),ev(SUMMARY,117,182),ev(S+'018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb',38,49)],
'一个有合法可选队伍的正常报名UI中，选错组合后不能按正文继续改选，局部异常可使上游报名入口没有正常返回。未证真实Demo或整个应用崩溃。',
'§4.6与§9限制“校验失败留在画面”：说明首错误后会继续后段成员命令，旧Entry0可使确认槽误入空摘要并在持物读取失败。保留正常合法提交、BACK nil与人数前门，不改变领域SpeciesClause、不新增事务回滚或框架设计。',
'增加精确2人规则三员[A1,A2,B]的两条成功/取消对照及非法重复组合；记录最后命令0、确认槽6、错误消息、空摘要首失败点、域状态未提交与清理到达。再做无旧命令的首次空确认及旧命令非0对照。非提出者必须逐跳反证错误消息后是否存在重选/复位路径。',
['PT A26/A27','多选位次撤销和自动确认焦点','WP54人数与SpeciesClause','WP55报名只有正常结果才提交','摘要空成员资源前提','前序消息恢复门'],syncbase+[FORMAL+'combat-requirements/wp55-facility-session-and-restoration.md (retain registration boundary; root checks sync need)'])
dump('findings.json',{'review_scope':'party subdomain','findings':findings,'non_proposal_observations':[{'id':'O-PT-01','status':'ROOT_TRIAGE_NO_AUTO_PASS','locations':[link(38,39),link(162)],'source':[ev(PARTY,400,431),ev(SUMMARY,678,689)],'observation':'注解还隐藏状态图；HP前景仅正HP绘制，0HP并不先取1再画2。正文尚未明写这些显示门。可能属于概括允许的细节遗漏，未独立计作重大冲突；建议根审查是否并入覆盖补充。'},{'id':'O-PT-02','status':'ROOT_TRIAGE_NO_AUTO_PASS','locations':[link(41,48)],'source':[ev(PARTY,802,853)],'observation':'多选CONFIRM/CANCEL的导航非一般最近面板描述：7 UP→6，6 DOWN→7；可用确定转移表补齐。现有两条导航向量未区分该门。'},{'id':'O-PT-03','status':'ROOT_TRIAGE_NO_AUTO_PASS','locations':[link(192)],'source':[ev(SUMMARY,1385,1400)],'observation':'事件选招空个体直接早退，不写变量，不同于零已知招式的首绘失败。正文未明确空个体合同；不从借用入口推演所有无效输入安全。'}]})
# Reverse mapping: all assigned formal blocks are accounted for; structural rows are never semantic PASS.
den=json.loads((ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/inventory/formal-block-denominator.json').read_text())
source_by_line={}
for x in units:
    for e in x['formal_links']:
        for n in range(e['start_line'],e['end_line']+1):source_by_line.setdefault((e['path'],n),[]).append(x)
context_formal={11:'入口的上游消费者/调用者限定，局部选择合同见后续条款。',13:'本稿只触发界面合同和直接写入，不重复上游规则。',48:'导航是行为化概括，组合输入/多选边缘细节见前向矩阵及观察。',109:'具名道具消费者，只保留该顺序与许可前提。',123:'MV限定来源身份/索引不变且盒取回成功；素材与输入未证。',196:'教学规则边界归WP30，战斗另域。',222:'返回值类型分层，并排除保证显示无副作用。',227:'蛋交互子集为正常非调试路径；Mark异常另登记。',234:'容量拒绝前缀与邮件已完成步骤须分开。',246:'既有案例目录与枚举是覆盖索引，案例逐行核查另表。',250:'领域依赖仅接口与必要消费者核查，不把每个领域全审移交给本子域。',251:'画面借用依赖，不宣称该画面所有路径通过。',252:'默认配置已经查读；调试与世代为明确变体。',255:'保留范围起点。',257:'战斗交界未穷尽，当前源标志消费仅选项门。',258:'静态事件入口可用不证明Demo；必选仅固定脚本定义。',259:'上游交易规则的既有未决，本子域只核选择合同。',260:'邮件数据模型依赖WP64，局部触发次序已核。',261:'FLY地图内部归WP63，仅调用取消链核查。',262:'默认菜单已核，插件组合unknown。',263:'媒体/逐帧unknown，不由图标参数推出存在。',265:'B16案例来源和保留边界是审计声明，未执行。'}
rev=[]
for d in den:
    p=d['path']; a=d['start_line']; b=d['end_line']
    if p!=SPEC:continue
    line=frozen(p).decode().splitlines()[a-1]
    xs=[]
    for n in range(a,b+1):
        for x in source_by_line.get((p,n),[]):
            if x not in xs:xs.append(x)
    is_structure=line.startswith('#') or bool(re.match(r'^\|\s*:?-{2,}',line)) or line in ['| 输入 | 条件 | 结果 |','| 入口 | 打开方式 | 模式与返回合同 |','| 命令 | 条件 | 效果与写入 |','| 分支 | 门与顺序 | 写入与失败 |','| 独立设计 | 后续输入与有序结果 | 最终袋 / A / B |','| 属性 | 余0 | 余1 | 余2 | 余3 | 余4 |']
    finding_ids=[f['id'] for f in findings if any(e['path']==p and not (b<e['start_line'] or a>e['end_line']) for e in f['formal_locations'])]
    documentary=a in [1,3,5,7,11,13,196,246,250,251,255,257,258,259,260,261,262,263,265]
    verdict='STRUCTURE_ONLY' if is_structure else ('CONFLICT_PENDING_COUNTERREVIEW' if finding_ids else ('DOCUMENTARY_OR_SCOPE_BOUNDARY' if documentary else ('STATIC_SUPPORTED_WITH_STATED_PRECONDITIONS' if xs else 'BOUNDED_DEPENDENCY_NOT_PROMOTED_TO_PASS')))
    if a in [38,39,41,43,45,46,48,162,192] and not finding_ids:verdict='STATIC_SUPPORTED_WITH_COVERAGE_OBSERVATION'
    rev.append({'formal_clause_id':d['id'],'formal_path':p,'formal_range':[a,b],'clause_type':'structure' if is_structure else 'semantic','claim_summary':context_formal.get(a, '对应前向事实的限定行为。' if xs else '结构/依赖/审计范围声明，不从读取自动判通过。'),'assessment':verdict,'source_fact_ids':[x['unit_id'] for x in xs],'source_evidence':[x['source'] for x in xs],'necessary_consumer_evidence':[e for x in xs for e in x['necessary_consumer_evidence']],'preconditions':'固定默认无插件；合法领域输入与资源/媒体/文字/场景前序已正常到达，除本条专门记录的边界失败；source内门与规格自身限定分别保留。','finding_ids':finding_ids,'runtime_status':'NOT_EXECUTED','host_demo':'UNKNOWN'})
# Text clauses belong to the assigned text source, not all WP17.
textlines=set([94,95,169,171,172,174,175,176,177,178,180,181,183,185,187,188,189,190,191,192,193,194,196,198,200,201,202,203,204,205,206,208,211,213,215,218,220,224,225,267,273,285,286,288])
for d in den:
    if d['path']!=TEXTSPEC or d['start_line'] not in textlines:continue
    a=d['start_line'];b=d['end_line'];xs=source_by_line.get((TEXTSPEC,a),[])
    rev.append({'formal_clause_id':d['id'],'formal_path':TEXTSPEC,'formal_range':[a,b],'assessment':'STATIC_SUPPORTED_TEXT_SUBDOMAIN' if xs else 'STRUCTURE_OR_SCOPE_ONLY','source_fact_ids':[x['unit_id'] for x in xs],'source_evidence':[x['source'] for x in xs],'necessary_consumer_evidence':[e for x in xs for e in x['necessary_consumer_evidence']],'preconditions':'命名模式与键盘/光标/自由文本三个入口分别适用；资源正常，输入查询是假定同采样轮服务结果，不证明实体按键。','runtime_status':'NOT_EXECUTED','host_demo':'UNKNOWN'})
# Per-test correspondence: catalog rows reviewed semantically, no shared denominator claiming all 914 lines passed.
catlines=frozen(CAT).decode().splitlines()
case_map={
202:['P032'],203:['P032','P020'],204:['P019'],205:['P019'],206:['P018','P026'],207:['P018','P026'],208:['P037','P026'],209:['P038'],210:['D003'],211:['D003','D004'],212:['D003'],213:['D003'],214:['D003'],215:['D003'],216:['P043'],217:['P043'],218:['P017'],219:['D002'],220:['D001'],221:['D001'],222:['S027'],223:['D001','S027'],224:['P033'],225:['P033'],226:['P034'],227:['P029','D010'],228:['P029','D010'],229:['S025'],230:['S020'],231:['S022'],232:['R005'],233:['R002','R003'],234:['P030','P045','P046'],235:['P031','P047'],236:['S023'],237:['D003','D004'],238:['D003'],239:['P018','P037'],240:['P034'],241:['P020'],242:['P026','P020'],
543:['T015'],544:['T014'],545:['T013','T014'],546:['T014'],547:['T014','T015'],548:['T015'],549:['T014'],550:['T003','T004'],551:['T009','T012'],552:['T004'],553:['T012','D011'],557:['D013'],567:['P008'],568:['P008'],569:['S003'],570:['P008'],590:['P018','P037'],592:['S002'],594:['D002','D005'],595:['R002','R006'],598:['D013'],600:['P033','R005','P030'],605:['P008','S003'],610:['S013'],611:['P026','P020','P037'],612:['S004','S017','S029','D001'],667:['P043'],668:['P043'],669:['P043'],760:['S013','D009'],783:['S023'],805:['P013','S007','R001','D008'],807:['P013','S007','R001'],808:['P012','S006','D008']}
# Resolve by ordinal IDs rather than trusting labels by inspection: retain trace plus exact source links.
unit_lookup={x['unit_id'].split('-')[-1]:x for x in units}
for line,keys in case_map.items():
    selected=[unit_lookup[k] for k in keys if k in unit_lookup]
    match=next((d for d in den if d['path']==CAT and d['start_line']==line),None)
    case_id=catlines[line-1].split('|')[1].strip() if catlines[line-1].startswith('|') else 'CONTEXT'
    rev.append({'formal_clause_id':match['id'] if match else 'CAT-L'+str(line),'formal_path':CAT,'formal_range':[line,line],'test_id':case_id,'assessment':'STATIC_LOCAL_CONTRIBUTION_ONLY_OTHER_CONSUMERS_NOT_PROMOTED_TO_PASS' if line in [567,569,590,592,598,600,605,760,783,805,807,808] else 'STATIC_VECTOR_REVIEWED_NOT_EXECUTED','source_fact_ids':[x['unit_id'] for x in selected],'source_evidence':[x['source'] for x in selected],'preconditions':'沿本行及共同夹具全部限定；未执行，插件/素材/真实输入/Demo未知。','finding_ids':[f['id'] for f in findings if any(e['path']==CAT and e['start_line']<=line<=e['end_line'] for e in f['formal_locations'])],'runtime_status':'NOT_EXECUTED','host_demo':'UNKNOWN'})
jsonl('reverse-matrix.jsonl',rev)
# Structural integrity and semantic coverage are independent checks.
assigned={PARTY:1560,SUMMARY:1400,RELEARN:199,TEXT:786}
coverage=[]
for p,n in assigned.items():
    rs=[x['source'] for x in units if x['source']['path']==p and not x['unit_id'].endswith(tuple(['D'+f'{i:03d}' for i in range(1,16)]))]
    represented=set(j for r in rs for j in range(r['start_line'],r['end_line']+1))
    read=set(j for r in ledger if r['path']==p for a,b in r['semantic_ranges'] for j in range(a,b+1))
    assert represented==set(range(1,n+1)),(p,'unit gap')
    assert read==set(range(1,n+1)),(p,'read gap')
    coverage.append({'path':p,'lines':n,'semantic_read_lines':len(read),'partitioned_lines':len(represented),'source_units':len(rs),'sha256':hashlib.sha256(frozen(p)).hexdigest(),'status':'COMPLETE_SEMANTIC_READ_NOT_AUTO_PASS'})
formalread=set(j for r in ledger if r['path']==SPEC for a,b in r['semantic_ranges'] for j in range(a,b+1))
assert formalread==set(range(1,266))
assert len([r for r in rev if r['formal_path']==SPEC])==174
# Independent conceptual vector calculations, not a translation or execution of reference.
vectors=[{'id':'IR-MARK-01','input':'empty marking sequence, focused missing slot','expected':'display-empty does not normalize sequence; ACTION reaches missing-value comparison before commit','evidence_kind':'STATIC_DERIVATION','reference_executed':False},
{'id':'IR-MULTI-01','input':'rule exactly2 plus species restriction; A1/A2 same species, B distinct; Entry A1 then A2 then CONFIRM','last_menu_result':0,'confirm_slot':6,'expected':'first error then stale result0 matches Summary0 for absent member; item identity read fails before new selection','evidence_kind':'STATIC_CONTROL_FLOW_DERIVATION_NOT_EXECUTED_REFERENCE'},
{'id':'IR-ORDER-01','level_candidates':['TACKLE','GROWL'],'first_record':['GROWL'],'expected':['TACKLE','GROWL'],'evidence_kind':'INDEPENDENT_MANUAL_VECTOR_NOT_EXECUTED_REFERENCE'},
{'id':'IR-EXP-01','fraction':0.5,'width_basis':128,'expected_even_width':64,'checked':round((0.5*128)/2)*2==64,'evidence_kind':'INDEPENDENT_ARITHMETIC_ONLY'},
{'id':'IR-MILK-01','source_hp':50,'source_total':120,'target_hp':30,'target_total':120,'dose':max(120//5,1),'expected_source':26,'expected_target':54,'checked':50-max(120//5,1)==26 and min(120,30+max(120//5,1))==54,'evidence_kind':'INDEPENDENT_ARITHMETIC_ONLY'},
{'id':'IR-MILK-02','target_total':50,'target_hp':30,'dose':24,'expected_gain':20,'checked':min(50,30+24)-30==20,'evidence_kind':'INDEPENDENT_ARITHMETIC_ONLY'}]
dump('independent-vectors.json',{'reference_execution':'NOT_EXECUTED','model_execution':'ONLY_ARITHMETIC_FIELDS_CHECKED_BY_PYTHON; OTHER VECTORS MANUALLY_DERIVED','host_demo':'UNKNOWN','vectors':vectors})
status={'task':'R6-UI/party','status':'COMPLETE_LOCAL_REVIEW_PENDING_COUNTERREVIEW','proposal_status':common['status'],'model':'UNVERIFIED','effort':'UNVERIFIED','tier':'UNVERIFIED','speed':'UNVERIFIED','uuid':'UNVERIFIED','input_binding':{'main_commit':MAIN,'main_tree':'6ab3429170d2762607fbc2237014c3a160449fa1','formal_tree':'1046fbb657882e84b3dfc6d017943a9edf7782e5','reference_commit':REF,'reference_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0'},'primary_source_semantic_coverage':coverage,'primary_formal_semantic_read_lines':265,'primary_formal_block_denominator':174,'primary_formal_reverse_rows':174,'source_unit_count':sum(c['source_units'] for c in coverage),'dependency_fact_count':16,'reading_ranges':len(ledger),'forward_rows':len(units),'reverse_rows':len(rev),'findings':len(findings),'blocked_unread_primary_ranges':[],'structure_checks':'JSON parsed, exact primary partitions and required semantic ranges checked; this is record integrity only','semantic_check':'Independent manual semantic reading with separately recorded conflicts, bounded dependencies and observations; no blanket PASS','actual_reference_tool_validation':'NOT_EXECUTED; fixed git blobs read only','independent_model_validation':'Six bounded vectors, only three arithmetic checks executed in Python; no reference algorithm/runtime','host_demo_validation':'UNKNOWN / NOT_EXECUTED','real_resources':'UNKNOWN','real_input':'UNKNOWN','sound':'UNKNOWN','write_scope_incident':'First report generator invocation omitted cwd and transiently created root build_review.py/forward-matrix.jsonl; both moved to owned party directory, root paths absent on read-only check; no formal/reference/old report edits.', 'formal_changes':False,'reference_changes':False,'old_report_changes':False,'update_started':False,'git_switch_commit_push':False,'external_service_or_install':False,'review_completed_at':now}
dump('task-status.json',status)
report=f'''# R6-UI / party 独立全量审读

状态：**已完成本子域指定输入的语义审读；不是通过判定**。四条提案均为 `PENDING_NON_PROPOSER_COUNTERREVIEW_AND_ROOT_ADJUDICATION`，需非提出者反证与根审裁决。未修改正式规格、参考材料或旧报告。

固定 main `{MAIN}`，主树 `6ab3429170d2762607fbc2237014c3a160449fa1`，formal树 `1046fbb657882e84b3dfc6d017943a9edf7782e5`；参考 `{REF}` / 树 `7589c800b61ba13a13040ed0d686979b80a84fd0`。树身份已只读核验。模型、effort、tier、speed、UUID无可验证回显，均 `UNVERIFIED`。

## 输入与覆盖

| 指定源 | 行数 | 语义读取 | 前向审读单元 |
| --- | ---: | ---: | ---: |
| Party | 1560 | 1560 | {coverage[0]['source_units']} |
| Summary | 1400 | 1400 | {coverage[1]['source_units']} |
| Move Relearner | 199 | 199 | {coverage[2]['source_units']} |
| Text Entry | 786 | 786 | {coverage[3]['source_units']} |

四文件共3945行全文读取，大文件连续约400行段落交付；没有未读指定源范围。WP66-A全文265行、公共分母174个非空块，反向矩阵174条逐块记账；首次长输出截断的120–175段另一次完整读取补齐。WP17全文作为上下文读取，仅命名/共享确认消费者域反向核源，其余WP17不重复取得全审结论。

测试目录逐行复核PT A01–A41，以及本域命名B04、B16、持物MV、格式化备忘录、摘要图鉴登记和局部确认暂停贡献。未把整份914行测试目录、其它owner案例或仅交付日志自动标成PASS。`reading-ledger.jsonl`为另写的语义记录，`delivery-ledger.jsonl`和read-logs仅证明交付。

`forward-matrix.jsonl`的审读单元连续分区覆盖每个指定源行，另16条必要依赖事实；嵌入方法声明清单只作结构库存。`reverse-matrix.jsonl`区分结构、范围声明、静态支持、覆盖观察、限定依赖及待反证冲突。JSON/分区检查只核记录完整性，不是游戏行为测试。

## 候选问题

| ID | 等级 | 正式定位 | 结论 |
| --- | --- | --- | --- |
| R6-UI-PARTY-001 | MEDIUM | WP66-A 182；PT A30/A35 | 默认空标记列表只在显示时按零处理。Mark初始槽0单独ACTION会在比较缺失值时抛NoMethodError，尚未提交或正常清理；正文仅描述非空清零，没有该默认边界。 |
| R6-UI-PARTY-002 | MEDIUM | WP66-A 216；PT A31 / B16-C003 | 与等级候选重叠的最初记录不移到前端。BULBASAUR L2、当前AMNESIA、最初GROWL得到TACKLE/GROWL；概括前置会给GROWL/TACKLE。WP30 §6.3已有正确非重叠门，需同步UI概括。 |
| R6-UI-PARTY-003 | LOW | WP66-A 145 | Shadow替换经验文字，但经验条请求仍只受最大等级门。非零经验比例仍产生条请求；只证请求，媒体遮挡与最终像素未知。 |
| R6-UI-PARTY-004 | MEDIUM | WP66-A 132/236 | 多选非法组合确认后沿用旧Entry命令0，误入不存在的确认槽成员摘要，在持物读取失败；并非正常回选择循环。 |

每条在`findings.json`包含精确源/规格位置、前提、普通对照、最小反例、取消/异常/部分提交、负证据范围、必要消费者、影响、最小修订、同步文件、验收与回归依赖。没有复制或转换参考代码为规格。

附加覆盖观察O-PT-01–03：注解同时隐藏状态图及零HP不绘前景；多选确认/取消按钮转移比正文概括细；空个体事件选招早退不写变量。这些仅交根审查是否补充，未扩成重大冲突或自动PASS。

## 核查过的前提与保留

默认菜单顺序及注册条件、场地招插入位置、Item/Mail互斥、快捷/菜单Switch不同ACTION/SPECIAL门、Box Link会话许可、FLY取消丢许可、从盒返回索引夹限和按槽注解恢复已逐路径核查。资格在开场缓存、进化石显式刷新、多选最少人数前门与提交校验分开。旧来源位置、对象及物品身份保留、邮件给予取消的前序入袋/入箱、盒取回后持物重复、缩队Switch部分队伍写入均保持，不用“取消全回滚”替代。

摘要的招式/缎带两次选择写入、Shadow禁招式换位、零招式详情首次失败、可取消事件选招与无静态调用者的必选入口、HM门、五页夹限、蛋单页、IV轮转并列规则、动态图像读取及缓存副作用已核。重学空候选严格ID失败在输入前、非空三层取消、成功统计、背包与队伍机器包装差异已核到消费者。

文本输入区分用户键盘/光标模式与内部旧字符网格分支。初值不截短、键盘退出先于编辑、光标BACK删除、满长替换末字、ACTION只定位OK、先音效再最小长度、整空列与同輪方向/操作优先序、非正max首次淡入失败、输入开关仅正常关闭已核。未引入跨模式统一取消或上限保证。

必要依赖按送达范围核查：物品教学与持物/邮件、个体当前形态/邮件自清/招式和创建默认、注册菜单、设施规则、共享消息窗、格式化宽度换行、图集请求、Box Link盒侧Item取回、图鉴最近见到、默认PBS与设置。跨包完整领域/实际Demo可达性没有因本子域局部读取取得通过。必选静态负证据仅固定Data/Scripts，插件/动态调用仍未知。

## 验证层次与后续

- 实际工具：只读固定git对象、源范围交付及审读记录完整性检查；**未执行参考脚本/游戏**。
- 独立模型：最小向量在`independent-vectors.json`。Python仅核128基准半比例为64与两条奶招算术；标记异常、候选顺序是静态推导，没有伪称参考运行。
- 宿主/Demo：`UNKNOWN / NOT_EXECUTED`；真实资源、输入、声音、裁切、异常外层恢复均未知。首次汇总脚本遗漏cwd，临时在仓库根产生build_review.py和forward-matrix.jsonl；已移至本目录，根目录无残留。本次程序性偏差如实登记，不冒充全程仅目录内写入。没有安装、下载、外服操作、真实存档、更新、git切换/提交/push。

非提出者须分别检查标记是否被其它消费者补齐、重学列表是否在后序重排、Shadow条请求是否只被媒体遮挡而非消除，以及多选失败后旧命令是否被重置；根审再决定修订。若接受，保持领域默认与已有取消/部分提交scope，同步WP66-A、测试目录、追溯与全局Feature Matrix；不设计未来框架API或改参考。所有新增验收保持静态未执行，真实宿主证据另域处理。
'''
(OUT/'report.md').write_text(report)
print(json.dumps({'files':['forward-matrix.jsonl','reverse-matrix.jsonl','reading-ledger.jsonl','findings.json','report.md','task-status.json','independent-vectors.json'],'primary_source_lines':3945,'formal_blocks':174,'forward_rows':len(units),'reverse_rows':len(rev),'reading_ranges':len(ledger),'findings':len(findings)},ensure_ascii=False))
