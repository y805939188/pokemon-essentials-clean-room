"""Emit private preparation from literal static reasoning and immutable Git text.

No game/source execution, behavioral simulation, original amendment or verdict.
"""
import difflib
import hashlib
import importlib.util
import json
from pathlib import Path

_spec = importlib.util.spec_from_file_location("inspect_inputs", Path(__file__).with_name("inspect-inputs.py"))
_inputs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_inputs)
BASE, PACKAGE, REFERENCE, OUT = _inputs.BASE, _inputs.PACKAGE, _inputs.REFERENCE, _inputs.OUT
blob, dump, identity, package = _inputs.blob, _inputs.dump, _inputs.identity, _inputs.package


UI = "deliverables/final-specification-set/user-interface/"
CAT = "deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md"
FILES = {
    "H": UI + "wp65-controls-help-appendix.md",
    "T": UI + "wp65-title-load-options-pause-and-pc.md",
    "A": UI + "wp66-a-party-and-summary-ui.md",
    "B": UI + "wp66-b-storage-and-pokedex-ui.md",
    "C": UI + "wp66-c-bag-item-storage-and-shop-ui.md",
}
# Ranges below are actually inspected text in this preparation turn. Hashes bind
# the ranges, not a claim that every referenced file or planned input was read.
READS = {
 "Data/Scripts/016_UI/005_UI_Party.rb": "133-160;235-248;653-695;746-800;855-874;1013-1020;1141-1168;1264-1287;1340-1349;1394-1405;1504-1533",
 "Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb": "206-209;254-259",
 "Data/Scripts/016_UI/022_UI_MoveRelearner.rb": "19-49;52-108;150-199",
 "Data/Scripts/010_Data/001_GameData.rb": "97-105",
 "Data/Scripts/001_Technical/001_Debugging/004_Validation.rb": "12-29",
 "Data/Scripts/016_UI/006_UI_Summary.rb": "184-207;589-637;740-843;929-936;1283-1287;1385-1400",
 "Data/Scripts/016_UI/017_UI_PokemonStorage.rb": "24-42;378-396;424-434;1020-1062;1498-1535;1724-1767;1770-1782;1814-1843",
 "Data/Scripts/016_UI/007_UI_Bag.rb": "190-207;235-246;350-386;442-447;464-469;578-600",
 "Data/Scripts/016_UI/003_UI_Pokedex_Main.rb": "517-538;631-664;771-774;804-823;851-865;913-1082;1092-1101;1110-1120;1168-1178;1176-1252;1266-1277",
 "Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb": "59-135;154-220;247-292",
 "Data/Scripts/016_UI/002_UI_Pokedex_Menu.rb": "17-32;99-115",
 "Data/Scripts/014_Pokemon/001_Pokemon-related/003_Pokemon_Sprites.rb": "83-203;208-316",
 "Data/Scripts/013_Items/007_Item_Sprites.rb": "7-11;31-45;72-109;116-157",
 "Data/Scripts/007_Objects and windows/007_BitmapSprite.rb": "32-35;65-85;119-135",
 "Data/Scripts/015_Trainers and player/003_Trainer_Sprites.rb": "7-16;24-65",
 "Data/Scripts/016_UI/025_UI_TextEntry.rb": "118-174;191-224;400-457;554-567",
 "Data/Scripts/016_UI/013_UI_Load.rb": "133-135;165-184;216-224;281-288",
 "Data/Scripts/007_Objects and windows/005_SpriteWindow_text.rb": "421-440;981-992",
 "Data/Scripts/016_UI/001_Non-interactive UI/001_UI_SplashesAndTitleScreen.rb": "12-14;30-55;73-115",
 "Data/Scripts/016_UI/001_Non-interactive UI/002_UI_Controls.rb": "37-81",
 "Data/Scripts/001_Technical/001_MKXP_Compatibility.rb": "30-41",
 "Data/Scripts/016_UI/015_UI_Options.rb": "27-28;348-354;401-418;532-544",
 "Data/Scripts/003_Game processing/001_StartGame.rb": "21-34",
 "Data/Scripts/004_Game classes/002_Game_System.rb": "113-122;170-177;187-203;223-232",
 "Data/Scripts/008_Audio/002_Audio_Play.rb": "74-88",
 "Data/Scripts/013_Items/008_PokemonBag.rb": "58-114;160-166;263-299",
 "Data/Scripts/016_UI/020_UI_PokeMart.rb": "598-673",
 "Data/Scripts/016_UI/021_UI_BattlePointShop.rb": "169-219;334-373;446-502",
 "Data/Scripts/013_Items/001_Item_Utilities.rb": "333-338;582-627;710-752",
 "Data/Scripts/013_Items/002_Item_Effects.rb": "75-91",
 "Data/Scripts/019_Utilities/001_Utilities.rb": "452-486",
 "Data/Scripts/009_Scenes/002_EventScene.rb": "134-171",
 "Data/Scripts/005_Sprites/010_PictureEx.rb": "362-406;432-456",
}
LOCALS = {
 "H": "1-56", "T": "1-150", "A": "19-80;113-209", "B": "1-230", "C": "1-153",
 "catalog": "96-125;128-160;160-199;200-204;205-250;251-266;267-307;308-331",
}

# Each record has a local defect/preservation decision, determinate static design,
# adjacent reverse, anticipated neutral clauses and unfulfilled acceptance work.
ROWS = [
 ("003", "源组织泄漏的局部行为化", "T:88-95;A:57-62,141-145;catalog:A38",
  "当前选项仍以控件构造关系解释；队伍换位和招式/奖章使用来源容器语义。删组织说明，但保留选项顺序、资格、数值兼容选择器、可观察状态和失败。原始审计规格中的来源组织不是一概可删的原文缺陷。",
  "合法队伍选择的兼容选择器0：ACTION无效果、SPECIAL桥可用；1：ACTION请求快捷换位并返回具名成员（取消位除外）；2：ACTION取消、SPECIAL禁用。USE的成员选择与BACK取消分别保留。T列可见选项及边界，不要求复现窗口/回调结构。",
  "菜单Switch目标选择为0、桥允许；ACTION快捷目标选择为2、桥禁用。两入口同目标仍可USE，不能把0写成禁止所有选择或把1写成菜单Switch模式。",
  "T 选项行为表；A 主菜单/选择/招式/奖章；catalog A38", "全局主责 B21；这里仅 B16 局部贡献。不得重定义共有 003 或认领其他 WP 完成。",
  ["005_UI_Party.rb", "015_UI_Options.rb", "006_UI_Summary.rb"]),
 ("004", "交换成功后仍持原目标", "B:71,101;catalog:B07",
  "B:71 与 B:101 自相矛盾。持 X 交换目标 Y 成功后目标为 X、游标继续持 Y；不得清空持有态。",
  "整理模式持盒中 X，目标 Y 合法且可交换：USE 后格为 X、held 为 Y，BACK 仍命中持有守卫。",
  "目标空格放下成功时 held 清空；被最后可用成员等守卫否决时 X/Y 未交换。",
  "B 整理模式拿起/交换/放下三分支；catalog 具名 X/Y 结果", "核对失败分支、后续取消、既有 B25/B26/B35 的 last-able 守卫；原 B:71 需同步建议。",
  ["017_UI_PokemonStorage.rb"]),
 ("006", "箭头帧数与绝对相位", "C:29;H 导航;catalog BG",
  "只写箭头可见性不能推出帧宽、三帧循环与初始相位。向下等通用箭头三帧一周 0.15 秒；横向专用箭头三帧一周 0.1 秒，按绝对运行时间取相位。",
  "合法三帧箭头、绝对运行时间0.12秒：横向专用0.1秒周期取首帧，通用0.15秒周期取第三帧；新建箭头不保证帧0。",
  "无滚动空间箭头隐藏；暂停箭头/文本导航另有八帧，不合并成三帧。",
  "C 背包滚动箭头；H/相关文本提示补充边界；静态相位设计", "共有主责 B21；B04 已接受范围保留。需补各实际消费者及方向差别，不能把来源类名作为兼容条件。",
  ["007_BitmapSprite.rb", "005_SpriteWindow_text.rb", "007_UI_Bag.rb"]),
 ("A015", "跳过载入菜单的空数据前提", "T:36;catalog:T03;generic SV02",
  "T 与 T03 已保留空则新游戏、非空则继续。全球 SV02 的缺前提不在本次允许原文范围；这里保护正确 UI 并确保未来本地主责最小验收追踪。",
  "调试、非打包、跳继续为真、已读存档非空且有效：不经菜单继续；不能推出一律新游戏。",
  "三个门相同，仅已读数据为空：直接新游戏；跳继续为假回正常调试入口。",
  "T 调试启动与 T03 双分支；与 SV02 所属范围协调", "保留 B02 局部接受；B16 主责仍需自身完整贡献核验，不能以 T03 已正确宣称根因关闭。",
  ["013_UI_Load.rb"]),
 ("A044", "一次性招式机入口差别", "A:174-177;catalog:A27 等",
  "当前 UI 与原文已正确：背包入口首次成功学习 TR 追加首招式，队伍持物使用入口不追加。保留 B07 域规则接受与两条独立入口，补明确静态对照。",
  "合法兼容、非蛋、尚未记入首招式、学习成功：从背包用 TR 新添记录；同对象状态从队伍持物入口成功学习不新增首招式记录。",
  "蛋/不兼容/已会/学习拒绝不成功、不写新记录；TM 不套用 TR 首招式登记。",
  "A 教招式入口表；catalog TR 首招式和消费结果", "需 PBS/具体物品/兼容资格实例绑定与前后集合；不能移除源入口差异或再次改坏正确原文。",
  ["002_Item_Effects.rb", "001_Utilities.rb", "001_Item_Utilities.rb"]),
 ("A048", "空重学候选在首绘失败", "A:181-202;catalog:A32",
  "无候选仍可打开并取消的保证错误。初始化绘制在选择循环前以空首候选查严格招式数据，类型验证失败；无 BACK 窗口。",
  "非蛋合法对象、等级/蛋/升级候选均空、合法资源前提：打开重学在首绘严格 ID 校验抛 ArgumentError，无学习、无取消返回。",
  "至少一个合法候选时首绘成立，BACK 返回取消而不改招式；顶层没有对象的另一早返回不等于空候选画面。",
  "A 重学入口与失败阶段；catalog A32 前提/异常", "原正文与 A32 需建议同步；保留 B07 域空集合接受，不把 UI 故障修成容错。",
  ["022_UI_MoveRelearner.rb", "001_GameData.rb", "004_Validation.rb"]),
 ("A055", "失败搜索持久模式不回滚", "B:152-162;catalog:B28",
  "当前 UI 与原文四态正确：Start 先写持久排序，再过滤；无结果回搜索，后 Cancel 不恢复该写入。B15 已接受域结果可复用，不替代 UI 局部贡献。",
  "持久模式 0、编辑模式 1、筛选结果空：Start→持久 1→返回搜索；Cancel 仍持久 1，活动全列表恢复原上下文。",
  "只编辑模式后 Cancel、从未 Start：持久仍 0；成功 Start 正常提交本次参数/结果上下文。",
  "B 四状态和写时点；catalog 失败 Start 后 Cancel", "非主责；只保护并补 UI 精确观测点，不重复原文同步。B15 scoped 接受非 B16 PASS。",
  ["003_UI_Pokedex_Main.rb"]),
 ("A056", "区域选择两个可见计数", "B:134;catalog:B21",
  "内部三元数据含区域长度，但区域菜单只画已见/已捕两个字段；区域长度仅用于完成标志。B15 域已经接受，B16 UI 仍有三可见计数错误。",
  "区域长度 3、seen 1、owned 1：菜单呈现已见1/已捕1，不显示长度3；没有完成标志。",
  "seen/owned 均 3 时完成标志可出现；保留内部长度作完成阈值，不把它删出规则数据。",
  "B 区域选择呈现与完成阈值；catalog 两字段/完成对照", "B16 主责最低验收仍需当前 UI 文本与设计；原文同错需建议，B15 receipt 不能转签。",
  ["002_UI_Pokedex_Menu.rb"]),
 ("A058", "行走预览和命名预览周期", "T:45;A/B 命名入口",
  "继续预览省略第一行四帧/0.5秒；命名预览采用四帧水平切片/0.4秒；两者绝对运行时间相位，不能写均为静态首格或均同周期。",
  "合法4×4行走图：继续预览只取首行四格、0.5秒一周；命名四水平格0.4秒一周。在绝对时间0.45秒，继续预览第四格、命名预览第一格。",
  "缺合法图资源可在装载失败；未证真实素材尺寸。新建图标不保证初始帧0，不把盒内静态首方格当命名动画。",
  "T 继续预览；A/B 命名预览及图标附表", "原 T 继续预览缺项需建议；具体资源与 t、宽高需未来实例，宿主相位仅静态公式。",
  ["003_Trainer_Sprites.rb", "013_UI_Load.rb", "025_UI_TextEntry.rb", "017_UI_PokemonStorage.rb"]),
 ("B035", "有限槽回退保总数不保分布", "C:120;catalog:C24",
  "失败后普通删除回退已添加量，不指定新槽；总量可恢复而旧槽分布改变。不要把无净物品增量写成整个背包无写入。",
  "有限2槽、禁止自动排序、POTION 每槽上限999，旧[999,997]、合法金钱1000单价200，买3：添2后失败，回退2由首槽删，最终[997,999]，总量1996、金钱/统计不变。BP足够时同普通袋逻辑。",
  "单有限槽旧[997]买3：添2失败回退后[997]；无限口袋不能套此容量失败。",
  "C money/BP 回退共享袋条件及状态分量；catalog C24 扩展", "原文过宽需同步建议；未来具名口袋配置/物品/排序/统计观测，保留B07/D023边界。",
  ["008_PokemonBag.rb", "020_UI_PokeMart.rb", "021_UI_BattlePointShop.rb"]),
 ("C003", "PT 的三处决定性前提", "catalog:A23,A31,A33;A 测试原表",
  "A23 缺目标HP上限；A31 缺升级/初始候选交集；A33 非蛋资格却假设唯一合格者蛋，自相矛盾。其他 CE/AN/CV/DG/MG/WR/EN/WT/FS/FP/TP/LC 归属保护，不能只按同 ID 改全表。",
  "A23目标30/50、来源50/120→可转20，源30/120、目标50/50；A31两升级U1/U2、初始U1→去重候选2；A33唯一成员蛋→没有合格者但仍开资格选择画面、标NOT ABLE，选蛋拒绝留循环，BACK写-1/空串；不能称该蛋合格。",
  "A23目标30/120可转24→来源26、目标54；A31初始I1与U1/U2不重合→3候选；A33同样对象非蛋且其他资格成立可进入选择。",
  "catalog 保旧ID顺序/行重数，改 PT 三行；A原表建议", "非主责；每个 PT 子例均需来源输入/结果/正反对照，不宣称全部扩展整改。A32 单独归A048。",
  ["005_UI_Party.rb", "001_Item_Utilities.rb", "022_UI_MoveRelearner.rb"]),
 ("C058", "SE 选项和共享BGS记忆", "T:102;catalog:T20",
  "正在播放 BGS 时变更SE会把当前记录音量改为新百分数；已记忆同一记录也变，恢复时再次缩放。实际播放请求与主机听感严格区别。",
  "SE100、BGS记录80、先记忆同一记录，再改SE50：记录/记忆音量均50；暂停恢复/后续恢复请求按50×50%=25，不是旧80×50%=40。",
  "没有播放BGS时不改该记录；音量值没变不触发该分支；拿播放信息副本不能假设与共享记忆相同。",
  "T SE预览状态与请求；catalog 记忆前后/无BGS", "原文只写暂停恢复需建议扩展。音频素材、听感及宿主播放未证；不克隆状态修复reference。",
  ["015_UI_Options.rb", "002_Game_System.rb"]),
 ("C114", "开场/标题/操作帮助分阶段时序", "T:29-30;H:34,40;catalog:T01,CH",
  "开场每张0.4淡入+2停留+0.4淡出，输入只在停留响应；标题叫声请求、等待1秒、0.4淡出，BGM淡出请求1秒。帮助旧内容先0.5淡出再新内容0.5淡入，阶段内仍更新输入，但旧确认回调先清除、完成后重挂。",
  "无输入、合法资源：每张总2.8秒，两张5.6秒；淡入期间USE不等于立即跳过。帮助确认产生退出/跳页应区分清除、两段绘制和输入检查时点。",
  "停留期间输入可提前终止该等待；debug入口可跳开场。帮助退出0.4秒与翻页两段1秒不可混写。",
  "T 开场/标题时序表；H 翻页/退出/输入窗口；catalog T01/CH", "原T/H时序与原T01需建议；PictureEx20Hz为事件时间单位非固定渲染帧率。实际素材/精确主机时间不证。",
  ["001_UI_SplashesAndTitleScreen.rb", "002_UI_Controls.rb", "002_EventScene.rb", "010_PictureEx.rb", "002_Audio_Play.rb", "002_Game_System.rb"]),
 ("C115", "屏幕索引倍率和负值", "T:112;catalog:T34",
  "上界只取min4，非下界钳0。索引0/1/2/3请求0.5/1/1.5/2倍；4或负数先请求内部尺寸再全屏；启动读7请求4但不当场回写，退出选项才写4。",
  "保存值7启动：按4全屏请求、保存值仍7；进选项读为4，退出写4。保存值-1请求全屏，不能推负倍率。",
  "合法索引2→内部尺寸、关闭全屏、1.5倍并居中；不保证宿主支持/实际画面大小。",
  "T 屏幕映射/启动与UI写时点；catalog 输入-1/0/3/4/7", "原缺实际映射需建议补齐；mkxp.json/主机输出未读未证。",
  ["001_MKXP_Compatibility.rb", "001_StartGame.rb", "015_UI_Options.rb"]),
 ("C117", "取消排序后保存索引仍变", "C:36;catalog:C05",
  "取消恢复当前选择和顺序，但拖动已即写口袋保存索引，不能推关闭重开恢复原游标。",
  "同口袋原索引0、三件合法物品，ACTION抓起第一件→下移到2→BACK：顺序/当前索引回0，保存索引2；随后普通BACK关闭，重开读2。",
  "未拖动直接BACK保存索引仍0；确认排序则当前、顺序和保存索引都保留移动结果。",
  "C 三种状态分量/关闭再开；catalog C05 对照", "原正文净效果过宽需建议；保留 PC 存入/出售中排序已接受写入和筛选袋独立边界。",
  ["007_UI_Bag.rb"]),
 ("C118", "图标切片/周期/HP/空值消费者", "C:30;T:45;A/B图标",
  "个体精灵首行方形帧，常态0.25秒、半血0.5秒、四分之一血1秒，濒死首帧；种类图标0.25秒；物品H=48时48方格W/48向下取整至少1帧且1秒，否则整图单帧；绝对相位与选择偏移须明列。",
  "合法个体128×64→2方形帧；HP10/40周期1秒，时间0.6秒取第二帧。选中前半周期偏移(+4,+6)、后半(+4,-2)。合法物品96×48→2帧1秒。",
  "HP0首帧；种类图标不按HP减速；非48高物品一帧；空个体隐藏、物品0按consumer空隐藏/图像选择不能全局统一；持物nil清空bitmap。",
  "跨T/A/B/C的中立图标行为附表及消费者引用；catalog 切片/相位/空值", "需完整消费位置/blankzero差异、宽高和时间具名设计；原文遗漏建议加表，继承B04/B05域结果不签UI。",
  ["003_Pokemon_Sprites.rb", "007_Item_Sprites.rb", "005_UI_Party.rb", "013_UI_Load.rb"]),
 ("C120", "看盒子时墙纸可写回", "B:49,109,189;catalog:B19",
  "viewBoxes 不全是只读。刷新到墙纸首次装载/变化时，旧box数字串转数字，非法或不可用值写回盒号模16；空串/nil仅显示fallback不一定改底层值。",
  "盒号5（零基）墙纸为锁定16且实际刷新：显示/存储改5；旧box2→整数2。随后仅退出也已持久改字段。",
  "盒号5（零基）墙纸空串：显示5但底层仍空；合法可用3保留3；未触发刷新不能套该写入。",
  "B 浏览盒/背景刷新副作用；catalog 旧格式/锁定/空值", "原浏览只读保证需建议收窄。保留B06盒数据及现有last-able/sentinel处理；资源可见效果条件化。",
  ["017_UI_PokemonStorage.rb"]),
 ("C121", "US 显示分支和重量差异", "B:170,搜索大小;catalog:B39扩展",
  "按语言字符串位置3-4是否US切分；信息页重量为round(原始百克值/0.45359)/10，搜索重量标签为round(原始百克值/0.254)/10；搜索过滤仍用原始分米/百克数，不倒转显示值。",
  "假定language位置3-4为US，合法重量数据100百克：信息页22.0lb，搜索同一具体档39.4，不能承诺一致；过滤上下界仍比较100。",
  "非US采用公制；同原始数据/界限换locale只改标签，不改入选资格。",
  "B info/search 单位/格式/原始过滤表；catalog 具名locale和原始值", "原文缺表需建议；具体四舍五入、英尺英寸格式应依已读247-292/517-538逐项定表；不能修正看似错误常数。",
  ["004_UI_Pokedex_Entry.rb", "003_UI_Pokedex_Main.rb"]),
 ("C122", "形态页先合格性别折叠与结构标签", "B:174-176;catalog:B31,B38",
  "B15完整域规则可复用：两性基形同正面图时先已见male后female只输出先合格者；女性种查female、无性查male；结构多形态在已见过滤之前认定，影响标签。",
  "合法双性基形、male/female正面解析路径相同且两者seen：只一male条；合法结构form1存在但未seen仍可使可见form0保留One Form标签。",
  "基形双性正面不同且已见可显示两性；缺素材双方nil相等只证明比较结果，不证明资源存在。原已有空标签应保留空。",
  "B 形态构建/标签行为表+UI显示；catalog保持B31/B38并增折叠对照", "B16 主责需UI反映全规则，不能把B15局部接受当主责完成；原文同缺陷需建议。首次循环写回未seen现行为保护。",
  ["004_UI_Pokedex_Entry.rb"]),
 ("C123", "两套37档和不对称端点导航", "B:搜索参数;catalog:B39",
  "连续十元组不足：height/weight各37个明确档。上界先选，未选与越界哨兵转换不对称；参数ACTION仅聚焦OK，主画面ACTION仅聚焦Start，各需USE。",
  "height当前2.5m→下一具体档3.0m，2.6不可选。上界未选(-1)LEFT到末具体档仅在下界未到末档；上界0 LEFT若下界未选到高侧哨兵37，RIGHT从37回0。",
  "主画面ACTION而未USE不执行搜索、不写模式；参数ACTION+USE只提交参数不跑搜索。相等上下界合法但移动不能越过对端。",
  "B 完整尺表/端点/焦点转移；catalog 不连续档/哨兵/相等边界", "原文应建议增中立标尺与转移表，未来正文完整列所有分支，不以37计数代替表。",
  ["003_UI_Pokedex_Main.rb"]),
 ("C124", "个性最高IV平手顺序和30含义", "A:128;catalog:A15扩展",
  "需兼容数据：最高IV平手按HP/攻击/防御/速度/特攻/特防，从PID模6起依次循环，首个最高获选；IV模5决定该属性5句，共30含义。",
  "HP与攻击IV均31其余低、PID模6=1：选攻击余1（喜欢胡闹）；PID模6=0：选HP余1（常睡午觉）。",
  "最高IV唯一时PID不改属性；PID模6=3时速度优先于特攻不是最终规格常见六维展示排序。",
  "A 备忘平手次序/30意义表；catalog tie/unique", "原文缺30表和顺序需建议；技能/IV域B05接受保留；本次静态含义不保证翻译素材字面。",
  ["006_UI_Summary.rb"]),
 ("C125", "BoxLink 收缩后旧换位源部分写入", "A:29,57-62;catalog:A40,A41",
  "普通Switch保留源旧索引。BoxLink存入删成员并压缩、只钳当前游标，源索引未重绑。返回提交换位可先改队伍再因空面板setter失败，无回滚。",
  "队伍[A,B]两者可用，先选B为源索引1，普通Switch中SPECIAL→存B入合法空盒→返回[A]游标0→USE：队伍先成为[空,A]、B仍在盒，随后结束动画操作空面板失败，不能保证完成UI返回。",
  "没有删源的普通换位可成功；ACTION快捷换位使用选择器2时SPECIAL禁用，不能在该入口套反例。仅打开盒后BACK保留已成功盒写入。",
  "A Switch入口/返回后的旧源/失败阶段；catalog A40具名最小反例+A41保护", "原文缺失败顺序需建议；不补索引重新绑定、数组压缩或回滚。动态完整游戏链未执行。",
  ["005_UI_Party.rb", "004_PokemonStorage.rb"]),
 ("C126", "零招式普通概要与详情/忘招不同", "A:130,141,157;catalog:A20等",
  "普通招式页可显示四空格；选入详情首绘查nil的伤害/属性失败，事件/直接忘招先同样首绘，来不及BACK。普通学习不足4招可直接添加，不能写零招式均失败。",
  "合法非蛋对象零招式、资源合法：普通第4页显示4空；USE详情或直接事件忘招首绘在BACK循环前失败，无招式更改。",
  "已有一个合法招式可打开详情/BACK；零招式普通学新招走直接添加成功，不进忘招页。",
  "A 页展示/详情/普通学/事件忘招分阶段；catalog 四入口对照", "原文取消保证过宽需建议；不添空保护或把nil失败写成取消；明确异常在首绘字段访问，不等同A048的严格ID类型失败。",
  ["006_UI_Summary.rb", "001_Item_Utilities.rb"]),
 ("D023", "BP 数量窗是半价乘数量", "C:98;catalog:C29",
  "正文缺数量因子。显示为quantity×floor(unitPrice/2)，确认/扣款/统计仍quantity×fullPrice。原C29的2×20→20BP本身正确，须保护。",
  "BP足够、单价20、数量3：显示30BP，确认与扣款60BP；单价奇数21、数量3显示30而非31。",
  "数量1单价20显示10、扣20；无足够BP首查拒绝，取消数量0无购买；商店钱显示不套半价。",
  "C 数量显示/确认/扣款公式；catalog C29保留并新增3件/奇数", "原正文需建议而原C29不改；保留B07价格覆盖及消费结果；UI误显示是真兼容结果。",
  ["021_UI_BattlePointShop.rb"]),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def log_ranges(commit, path, ranges, reference=False):
    data = blob(commit, path, reference)
    lines = data.splitlines(keepends=True)
    return {**identity(commit, path, reference), "read_kind": "BOUNDED_STATIC_TEXT_INSPECTED",
            "ranges": [{"lines": span, "sha256": sha(b"".join(lines[int(span.split('-')[0])-1:int(span.split('-')[1])]))}
                       for span in ranges.split(';')]}


def main():
    controls = package("original-and-acceptance-controls.json")["controls"]
    byid = {c["id"].removeprefix("GIR-FD82-"): c for c in controls}
    source_paths = list(READS)
    records = []
    for short, title, local, defect, case, reverse, targets, gap, sources in ROWS:
        c = byid[short]
        records.append({
            "id": c["id"], "primary": c["primary"], "status": "PREPARATION_ONLY_NO_VERDICT",
            "canonical_state": c["canonical_state"], "title": title,
            "whole_original_object_binding": c["whole_original_object_binding"],
            "whole_approved_acceptance_binding": c["whole_approved_acceptance_binding"],
            "qualified_current_control": c["complete_current_control_fields"],
            "current_UI_locators_at_B15_C": local,
            "local_defect_or_preservation": defect,
            "static_minimum_counterexample_design": case,
            "adjacent_reverse_design": reverse,
            "anticipated_neutral_WP_and_catalog_clauses": targets,
            "minimum_acceptance_work_remaining": gap,
            "source_and_caller_reading": [{"path": p, "commit": REFERENCE, "ranges": READS[p]}
                for name in sources for p in source_paths if p.endswith(name)],
            "designs_executed": False, "formal_remediation_claim": False,
            "common_remaining_gate": "Refreeze after exact B12 C; write only future authorized scope; neutral body/appendix/catalog consistency, full qualified original/current control and per-primary minimum; independent Ultra FULL all24/20, necessary affected candidate/actual, sole G/C. No closure or review by author.",
        })
    assert len(records) == 24 and sum(r["primary"] for r in records) == 20
    assert set(byid) == {r[0] for r in ROWS}
    dump("contribution-analysis.json", {
        "formal_input": BASE, "package": PACKAGE, "24_contributions": 24, "20_primary": 20,
        "formal_writes": 0, "independent_reviews": 0, "formal_C": False,
        "record_order_matches_dispatch": [c["id"] for c in controls] == [r["id"] for r in records],
        "precedence": "Qualified current/root/extension/effective constraints control; whole immutable original/approval identity remains binding. Literal preparation designs do not replace control or satisfy minimum.",
        "contributions": records,
    })
    logs = [log_ranges(REFERENCE, p, spans, True) for p, spans in READS.items()]
    logs += [log_ranges(BASE, CAT if key == "catalog" else FILES[key], spans) for key, spans in LOCALS.items()]
    dump("source-reading-log.json", {
        "reference_execution": 0, "behavior_vectors_executed": 0,
        "range_hashes_are_not_runtime_proof": True, "reading": logs,
        "separate_identity_only_inputs": "input-verification.json planned_reads:74; no claim that all74 underwent whole-file semantic reading.",
        "controls_reading": "All24 whole source-bound controls compared exactly (48 object equality checks); current qualifications/root/extensions/effective cases/minimum/recheck analyzed; immutable raw-report/history duplicates not recursively re-read.",
        "original_reading": "All five potential originals inspected at assigned clauses and exact before text, see original-sync-proposals.json, not whole-file approval.",
    })
    dump("source-limits.json", {
        "inherited_binding_and_limits": package("source-limits.json"),
        "own_semantic_scope": "Finite assigned UI/static source/caller inspection at ranges in source-reading-log.json; only new Git/JSON/hash/text tooling executed.",
        "execution_counts": {k: 0 for k in ["reference", "Ruby", "compiler", "converter", "generator", "deserializer", "historical_author_reviewer_program", "behavior_vectors", "runtime_observations", "proven_Demo_chains"]},
        "newly_recovered_read_cache": "/tmp/b16-reference.git exact reference commit/tree; specified workspace bare cache absent; no reference checkout, execution or modification.",
        "unproven": "All U01–U10/G01–G12/AX01–AX20 retained. Actual assets/sizes/sound/host output and capacity, binary/serialized files, maps/events, plugins/dynamic dispatch/aliases/shadow reachability and real Demo chains remain unproven. Literal legal-resource or finite-pocket premises are designs, not observed defaults.",
    })


if __name__ == "__main__":
    main()
