"""Exact, reviewable document edits for the six authorized R6-U14 findings."""
from pathlib import Path
import datetime
import hashlib
import json

OUT=Path(__file__).resolve().parent
MIRROR=OUT.parent/'mirror/deliverables/final-specification-set'
changes=[]
def replace(path, old, new, finding):
    p=MIRROR/path
    before=p.read_text()
    assert before.count(old)==1, (path,old[:90],before.count(old))
    after=before.replace(old,new,1)
    p.write_text(after)
    changes.append(dict(finding=finding,path=str(p.relative_to(OUT.parents[4])),
                        old=old,new=new,before_sha256=hashlib.sha256(before.encode()).hexdigest(),
                        after_sha256=hashlib.sha256(after.encode()).hexdigest()))

replace('generic-kernel/wp08-localization.md',
'④ 作者翻译工作流（文本收集、提取、编译、写回与失败副作用）。',
'④ 作者翻译工作流（文本收集、提取、编译、写回与失败副作用）；⑤ 当前语言对指定 UI 图像身份的选择。','R6-D-LZ-002')
replace('generic-kernel/wp08-localization.md',
'### 5.2 空译与异常边界',
'''#### 5.1.1 指定 UI 图像身份的语言选择

当前语言材料也可把指定 UI 图像的原始身份 A 映射为另一身份 B；这些字符串仍属于 SCRIPT_TEXTS，不新增文本域。查找先于图像创建／加载：语言 game 优先于语言 core；两层均缺译时交付原身份 A；命中非空译文 B 时交付 B，即使 A 本身可用也不改回 A。说明标签的文本查找与图像身份查找分别进行。

| 指定消费者 | 语言材料选择的范围 | 独立固定资源 |
| --- | --- | --- |
| 控制帮助 | 七个键图身份 | 控制帮助背景 |
| 图形模式下的战斗命令／招式菜单 | 命令与招式光标图、类型图、Mega 与换位按钮图 | 对应菜单背景 |
| 训练家卡 | 卡片及女性卡片图身份；女性分支另有资源存在性门 | 背景与徽章图 |
| 翻牌小游戏 | 背景和备忘图的基名；查找后仍在该消费者的图像目录下加载 | 其它图块、光标等资源 |

此规则只覆盖指定的查找调用者，不把所有 UI 图像都设为可翻译。空译仍是命中，随后怎样处理空身份、不可解析身份或加载异常由 [WP15](../engine-overworld/wp15-resource-matching-and-audio.md) 的实际资源入口决定；没有“译后资源失败就重试原图”的通用保证。查找本身不新增语言选择提示或存档写入，场景可能已建立视口／部分图像，不据后续失败保证整体清理或回滚。资源存在、合适尺寸、加载成功及实际像素仍须分别验证。

### 5.2 空译与异常边界''','R6-D-LZ-002')
replace('generic-kernel/wp08-localization.md',
'#### 6.1.1 默认哈希材料的替换与追加',
'''**收集键与运行输入的换行边界**：普通脚本的源拼写解码不保证得到与运行查找输入相同的字符序列。一个片段在 A/B 间的源拼写为两个 U+005C 后接 U+006E 时，按上述收集次序可得到 A＋U+005C/U+000A＋B；对应的普通运行输入却为 A＋U+005C/U+006E＋B。键规范化不会把字母 n 转成 LF。在有效当前语言两层只给收集键译文 Q、运行键均缺译且无覆写时，运行查找返回原输入，不选 Q；随后消息显示层才把反斜线 n 处理为换行，不能凭相同换行外观认定查找已命中。无此转义差异且实际运行键命中 Q 的普通消息仍选 Q。此区别只限定上述输入，不推成全部转义文本或整个语料的翻译失效；是否在未来实现中保留该异常另作兼容决定。

物品成功接收／拾取／奖品和树果成功采摘的口袋提示到达此查找前，库存写入已发生；缺译是正常回退，不自行抛错或撤销该写入。作者导出取消、确认覆盖后先删后写及完整导入先截断输出仍按 §6.2–§6.4 的独立边界。

#### 6.1.1 默认哈希材料的替换与追加''','R6-D-LZ-001')
replace('generic-kernel/wp08-localization.md','的 LZ01–LZ35（','的 LZ01–LZ41（','R6-D-LZ-001/R6-D-LZ-002')
replace('engine-overworld/wp15-resource-matching-and-audio.md',
'### 3.3 默认窗口皮肤的选择与显式设置',
'''指定 UI 图像在进入资源访问前，可先按 [WP08 §5.1.1](../generic-kernel/wp08-localization.md#511-指定-ui-图像身份的语言选择) 由当前语言选择资源身份：缺译交原身份 A，非空命中 A→B 则交 B。控制帮助键图、图形战斗菜单按钮、训练家卡及翻牌小游戏的指定资源有此接点；固定背景等独立资源不因此一并翻译。资源解析／缓存／动画包装仍按本文件各自入口处理 B；译后资源未命中或加载失败不带通用原身份重试，空译的后续消费也不等于语言缺译回退。身份选择不认证媒体存在、加载成功或像素结果。

### 3.3 默认窗口皮肤的选择与显式设置''','R6-D-LZ-002')
replace('user-interface/wp65-controls-help-appendix.md','| 页 | 键图（文件名） | 说明标签内容（本地化文本） |','| 页 | 键图（原始资源身份） | 说明标签内容（本地化文本） |','R6-D-LZ-002')
replace('user-interface/wp65-controls-help-appendix.md',
'- **页面组建**：冻结图形',
'''七个键图各自在创建图像前按当前语言查找资源身份，规则见 [WP08 §5.1.1](../generic-kernel/wp08-localization.md#511-指定-ui-图像身份的语言选择)：缺译请求原图 A，非空译文 A→B 请求 B；说明标签独立本地化，背景 bg 保持固定身份。A/B 都是可用合适图像时可比较加载请求身份，不能据此认证像素。译后资源失败不保证重试 A；空译及加载失败按 WP15 的实际入口处理，已完成的场景构造不据此保证回滚。

- **页面组建**：冻结图形''','R6-D-LZ-002')
replace('user-interface/wp65-controls-help-appendix.md','（说明标签的本地化文本）','（说明标签与七个键图身份的语言选择；背景独立）','R6-D-LZ-002')

replace('generic-kernel/wp03-content-identity-and-schema.md',
'| Ability：Name、Description、Flags |',
'| Type：Name、IconPosition、IsSpecialType、IsPseudoType | Unnamed、0、false、false | 名称再经 TYPE_NAMES 查找；图标位置与旧配置的物理／特殊分类分别消费原始值，伪类型标记不自动等同攻击无效 |\n| Ability：Name、Description、Flags |','R6-D-PBS-C05')
replace('generic-kernel/wp03-content-identity-and-schema.md',
'| Move：Category、Power、Target、FunctionCode | Status、0、None、文本 None | 类别与威力须先通过《PBS 生命周期》§4.5 的交叉校验；既有 Type NONE、命中 100、PP 5 默认保持 |',
'| Move：Name、Description、Priority、EffectChance、Flags；Category、Power、Target、FunctionCode | Unnamed、???、0、0、空标记列表；Status、0、None、文本 None | 名称／描述各经对应文本域；类别与威力须先通过《PBS 生命周期》§4.5 的交叉校验；既有 Type NONE、命中 100、PP 5 默认保持 |\n| Item：NamePlural（单数 Name 已显式给 Review） | Unnamed | 复数原名独立默认，不从 Review 自动生成；普通复数名再经 ITEM_NAME_PLURALS 查找。份名缺席按下文回对应普通名称 |','R6-D-PBS-C05')
replace('generic-kernel/wp03-content-identity-and-schema.md',
'StorageCreator 先查本字段的译文/原文，',
'''上表只规定属性省略，不统一解释显式空属性。特性 Flags 出现但没有 CSV 值时的登记与后续查询结果见《PBS 生命周期》§4.2 的具名相邻例；其省略为空列表的默认不变。

StorageCreator 先查本字段的译文/原文，''','R6-D-DATA-C01')
replace('generic-kernel/wp03-content-identity-and-schema.md',
'### 4.4 查询副作用',
'''#### 4.3.2 显式指标记录的缺字段默认

合法物种的指标作者节已经存在且成功转换／登记时，省略 BackSprite、FrontSprite、FrontSpriteAltitude、ShadowX、ShadowSize 分别得到 (0,0)、(0,0)、0、0、2。基础节与非零形态节都按这组自身默认，不按物种形态字段继承，也不逐字段复制基础指标。查询命中已有形态指标时保留该记录；仅整条指标身份缺席时才执行 §3.2 的基础默认／形态克隆登记。来源后缀仍由 PBS 来源或查询创建入口决定。

例如基础背面坐标为 (5,6)，其它前提正常、无后续编辑或覆写：形态1的作者指标节仅给 ShadowSize=2，随后查询背面为 (0,0)；完全没有该形态指标记录后首次查询才复制 (5,6)；显式给形态背面 (7,8) 则保留 (7,8)。登记／查询结果不等于档案、PBS 保存或已有布局刷新；相应编辑与输出边界见 [WP73-B §7.5](../demo-dx/wp73-b-world-editors.md#75-保存时记录集合pbs-路径与消费者) 和《PBS 生命周期》§5.5。

### 4.4 查询副作用''','R6-D-PBS-C06')
replace('generic-kernel/wp03-content-identity-and-schema.md','的 KR01–KR16（','的 KR01–KR16 及 R6-U14-C05/C06 静态对照（','R6-D-PBS-C05/R6-D-PBS-C06')
replace('creature-rpg/wp27-bag-and-item-storage.md',
'### 2.2 数量判定与逐槽显示',
'''**名称的独立省略默认**：合法新物品显式给单数原名 Review、但省略 NamePlural 时，复数原名为 Unnamed，不自动使用 Review 或推导 Reviews；显式给 NamePlural=Reviews 才保存 Reviews。普通单／复数名称分别查各自语言域，原始默认不保证最终显示字面 Unnamed。份名单／复数原字段缺席时，分别回对应普通名称；非空份名命中空译仍返回空串（WP03 §4.3.1／WP08），不改成普通名。

### 2.2 数量判定与逐槽显示''','R6-D-PBS-C05')
replace('pokemon-rules/wp43-types-accuracy-and-damage.md',
'已核数据样本：',
'''作者省略字段只决定原始记录，不保证最终本地化文字或战斗效果。合法新 Type 仅给身份时，原名／图标位置／特殊标记／伪标记为 Unnamed／0／false／false；显式图标3及两标记 true 保留。合法新 Move 显式引用已登记 NORMAL，其余数据校验正常，省略 Name／Description／Priority／EffectChance／Flags 得 Unnamed／???／0／0／空列表；同时省略 Category／Power 则得到 Status／0，仍遵守 WP04 的类别×威力校验。显式正常名、描述、优先级和概率保留；名称／描述再按各自语言域查找（WP03 §4.3.1／WP08）。现有类型 NONE、命中100、PP5、目标 None 及效果 None 默认不由这组补充改变。

已核数据样本：''','R6-D-PBS-C05')
replace('demo-dx/wp73-b-world-editors.md',
'### 7.1 编辑器框架',
'''指标作者节的缺字段默认与编辑器查询缺整条记录分开：已编译登记的基础或非零形态指标节省略五组时，分别采用背面 (0,0)、正面 (0,0)、高度0、阴影横移0、阴影大小2；已有部分记录不会因查询而逐字段补基础值。整条形态指标缺席才惰性克隆基础，见 [WP03 §4.3.2](../generic-kernel/wp03-content-identity-and-schema.md#432-显式指标记录的缺字段默认)。基础背面 (5,6) 下，形态节仅给 ShadowSize=2／整条形态缺席后查询／显式背面 (7,8)，结果分别 (0,0)／(5,6)／(7,8)。这三组在后续编辑之前观察，不声称已保存文件或已有战斗重定位；§7.5 的来源后缀、等值省略、查询副作用与保存门继续适用。

### 7.1 编辑器框架''','R6-D-PBS-C06')

replace('generic-kernel/wp04-pbs-lifecycle.md',
'**枚举求值**分两类来源：',
'''**特性 Flags 的显式空相邻例**：合法且未登记的新特性、schema／查询无覆写，其余转换、终检依赖正常时，省略 Flags 得空列表，普通标志查询为否；Flags 给普通文本 Other 得一个正常文本元素，查询 FasterEggHatching 为否。出现 Flags 属性但等号后没有 CSV 值时，重复字符串位置仍求首组，产出含一个缺值元素的列表；该列表不是零元素列表，登记保留它。随后普通标志查询在首个缺值元素的字符串比较处失败，不是跳过该元素或正常返回否。此例不推广到所有字段、所有 Flags 或所有显式空列表。

登记已完成不证明整表保存；终检和保存各自成功才谈档案加载，后续查询失败不自动撤回登记。普通文件读取没有本例的 UI 取消动作，外层编译清理仍按 §3.2／§6。条件孵化投影另要求一个正常蛋原剩2步、首个被检查的非蛋队员带该特性且此前正常：先减至1，随后标志查询失败，尚未额外减步、夹0或孵化；省略 Flags 对照仍为1且正常经过检查。外层事件恢复、最终错误画面和资源释放未知。上述均为静态推导、NOT_EXECUTED；未来保留、拒绝或清理此异常输入属于独立兼容政策。

**枚举求值**分两类来源：''','R6-D-DATA-C01')
replace('generic-kernel/wp04-pbs-lifecycle.md','的 KL01–KL36（','的 KL01–KL36 及 R6-U14-FLAGS 静态对照（','R6-D-DATA-C01')

replace('creature-rpg/wp18-creature-identity-species-ownership.md',
'  - 友好度：= 物种记录值。',
'  - 友好度：直接采用物种记录值，创建入口不另夹到 0–255。合法基础物种 PBS 的 Happiness 为非负整数，省略为70；独立作者值256可登记并在成功创建后保留256。编辑器的0–255限制及后续受控变化是不同入口（WP30 §7.1）。','R6-D-PBS-C07')
replace('creature-rpg/wp30-growth-learning-and-friendship.md',
'| 友好度 | 0–255 的持久值；变化按「方法 × 当前值档位」取值，再按场景修正（地图/球/道具/软上限）。 |',
'| 友好度 | 持久整数；通常受控变化域为0–255，作者初值直接保留的边界见§7.1。变化按「方法 × 当前值档位」取值，再按场景修正（地图/球/道具/软上限）。 |','R6-D-PBS-C07')
replace('creature-rpg/wp30-growth-learning-and-friendship.md',
'- 持久整数 0–255；创建初值 = 物种记录值（WP18）；调试/事件可直接写入（E 类登记）。\n- 变化后一律钳到 [0, 255]。',
'''- 持久整数；0–255是通常受控变化及作者编辑器的常规域，不是所有创建／直接写入的硬不变量。创建初值直接采用物种记录值（WP18），不另夹限；基础物种 PBS 的 Happiness 接受非负整数，省略为70，已读物种校验不另设255上限。合法独立作者夹具只把基础 Happiness 改为256，其余数据和创建依赖正常，关闭默认招式初始化与创建形态复检且无覆写，在创建成功返回、任何后续友好变化前观察：物种记录和个体都保留256。255、省略、显式0的独立对照分别保留255、70、0，不声称随附默认数据超界。
- 调试／事件的直接写入仍是另一入口。下述变化方法正常完成时才把结果钳到 [0,255]；创建和直写不由这个后继步骤提前修正。裸创建无确认／取消流程；前门或依赖失败不产生上述成功返回结果，也不保证全局回滚。未来是否对作者初值拒绝或夹限须另作兼容政策。''','R6-D-PBS-C07')
replace('creature-rpg/wp30-growth-learning-and-friendship.md',
'### 7.2 变化方法表（值 × 当前友好度档位 ⌊h / 100⌋）',
'''### 7.2 变化方法表（值 × 当前友好度档位 ⌊h / 100⌋）

下表档位适用于当前值0–255；末档为200–255，不无限外推“200+”到任意作者初值。超界初值能被创建保留，不保证任何后续方法都正常完成；正常完成后的夹限与创建观察点分开。''','R6-D-PBS-C07')
replace('creature-rpg/wp30-growth-learning-and-friendship.md','| 方法 | 档位 0–99 / 100–199 / 200+ |','| 方法 | 档位 0–99 / 100–199 / 200–255 |','R6-D-PBS-C07')
replace('creature-rpg/wp18-creature-identity-species-ownership.md',
'另见同目录 U03-SZ01',
'另见同目录 R6-U14-CI01–CI04 的作者 Happiness 初值对照，均为 NOT_EXECUTED；创建复制与后续受控变化分开。\n\n另见同目录 U03-SZ01','R6-D-PBS-C07')
replace('creature-rpg/wp30-growth-learning-and-friendship.md',
'另见同目录 U03-EX01',
'另见同目录 R6-U14-GR01–GR05 的作者初值及正常变化夹限对照，均为 NOT_EXECUTED，不改变GR-35–GR-42的正常值向量。\n\n另见同目录 U03-EX01','R6-D-PBS-C07')

def append(path,text,finding):
    p=MIRROR/path
    before=p.read_text(); assert text not in before
    p.write_text(before.rstrip()+'\n\n'+text+'\n')
    changes.append(dict(finding=finding,path=str(p.relative_to(OUT.parents[4])),operation='append',new=text,
                        before_sha256=hashlib.sha256(before.encode()).hexdigest(),after_sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
append('test-catalog/generic-kernel-wp05-06-07-08-09-10.md', '''## LZ36–LZ41：收集键与指定图像身份（静态设计）

全部为 DERIVED_VECTOR／NOT_EXECUTED_THIS_UPDATE；有效当前语言game/core、未覆写查找／消费者、前序正常。字符身份在查找后、窗口处理前观察；图片例只观察交付创建／加载的资源身份，不执行媒体或宿主。正文WP08 §6.1／§5.1.1、WP15 §3.2、WP65控制帮助§3。

| ID | 输入／前提 | 静态预期 |
| --- | --- | --- |
| LZ36 | 普通物品成功消息无转义换行差异，实际规范运行键命中Q；正常色彩控制与参数 | 先选Q再替换参数，色彩控制后处理，不因控制码普遍缺译 |
| LZ37 | A/B间普通脚本源拼写为U+005C/U+005C/U+006E；收集键间隔U+005C/U+000A，运行间隔U+005C/U+006E；两层仅收集键→Q、运行键均缺译 | 两键不同；普通查找返回原运行输入，不选Q，后续窗口才处理反斜线n为换行；显示换行不证明译文命中 |
| LZ38 | 合法物品和口袋，库存添加成功后到达LZ37条件的口袋提示；独立作者取消导出／非法导入对照 | 缺译正常回退，已写库存不撤销。取消未进入导出不写；完整导入旧输出已覆盖打开后解析失败，截断不恢复，与运行缺译分列 |
| LZ39 | 控制帮助已到达键图创建，原身份A可用，两语言层均缺该键；标签独立查找 | 请求A；背景固定身份，标签按自身语言结果；无新增语言选择或存档写入 |
| LZ40 | 同LZ39，A/B均为可用合适图片，game或仅core命中A→非空B；A本身仍可用，标签与背景不改 | 键图请求B；game同键优先于core；不因A存在而保留A，仅指定键图变化，不认证像素 |
| LZ41 | 同指定键图消费，A→非空B，但B资源未解析到或宿主加载失败；独立A→空字符串 | 非空B交现有资源入口，失败按WP15入口分层，没有通用重试A；空译仍命中、把空身份交消费者，不当作缺译；已有场景前缀不保证整体回滚，最终宿主呈现未知 |''','R6-D-LZ-001/R6-D-LZ-002')
append('test-catalog/generic-kernel-wp02-03-04.md', '''## R6-U14：有限默认、部分指标与显式空特性标志

全部为 DERIVED_VECTOR／NOT_EXECUTED_THIS_UPDATE；固定参考、合法唯一新身份、无schema／查询覆写、其它字段／引用／终检依赖正常。各行独立复位，观察登记原始记录／直接查询；名称例无语言命中或只读原始字段，不声称完成整表落盘、UI绘制或宿主执行。正文WP03 §4.3.1–§4.3.2、WP04 §4.2；域内消费者另见WP27／WP43／WP73-B。

| ID | 输入／前提 | 静态预期 |
| --- | --- | --- |
| R6-U14-C05-01 | 新Item显式Name=Review，省略NamePlural及两份名 | 原始单数Review、复数Unnamed；份名读取分别回普通单／复数名，不自动派生Reviews |
| R6-U14-C05-02 | 同Item显式NamePlural=Reviews；独立普通名称查找命中非空／空译 | 原始Review／Reviews保留；显示查找可交对应译文／空串，原始默认与最终本地化分层 |
| R6-U14-C05-03 | 新Move显式Type=NORMAL已登记，省Name／Description／Priority／EffectChance／Flags／Category／Power／Target／FunctionCode | Unnamed／???／0／0／空列表；Status／0／None／文本None；Type仍NORMAL，既有命中100／PP5保持；类别×威力校验正常 |
| R6-U14-C05-04 | 合法Move显式Name=Review、Description=Text、Priority=1、EffectChance=25、Flags=Other、Category=Physical、Power=40，Type正常 | 所列原始值保留；不因有限省略默认拒绝合法显式输入，战斗效果仍按其消费者 |
| R6-U14-C05-05 | 新Type仅给合法身份；独立显式Name=Review、IconPosition=3、IsSpecialType=true、IsPseudoType=true | 省略例Unnamed／0／false／false；显式例Review／3／true／true。类型名另查语言，不推定像素或攻击无效 |
| R6-U14-C06-01 | 有效VENUSAUR及形态1；基础背面(5,6)，形态指标作者节存在且仅给ShadowSize=2，无额外查询／覆盖 | 形态背面(0,0)、正面(0,0)、高度0、阴影横移0、大小2；后续查询命中它，不逐字段复制基础(5,6) |
| R6-U14-C06-02 | 同基础(5,6)，整条形态1指标缺席；首次正常查询 | 惰性克隆背面(5,6)和其余基础指标，登记形态，后缀为空；不继承基础来源后缀 |
| R6-U14-C06-03 | 同有效作者形态节，显式BackSprite=7,8，其余五组字段按省略规则 | 背面(7,8)；其它缺字段取自身默认，与C06-01/02分开；登记不自动证明保存／布局刷新 |
| R6-U14-FLAGS-01 | 新Ability省略Flags，查询普通FasterEggHatching | 登记零元素空列表，查询否；现有C01F-016-01保持 |
| R6-U14-FLAGS-02 | 同合法新Ability出现Flags但等号后没有CSV值；宿主／插件未赋予缺值元素字符串比较能力 | 首组求值形成一个缺值元素，登记保留；随后普通标志查询在首元素比较处失败，不正常返回否／清理为空；不证明已保存档案或随附数据含此空属性 |
| R6-U14-FLAGS-03 | 同合法新Ability，Flags=Other，查询FasterEggHatching | 正常文本元素保留，查询否；不把全部显式列表推广为失败 |
| R6-U14-FLAGS-04 | FLAGS-02已登记；正常蛋原剩2步，首个检查的非蛋队员带此特性，之前正常；独立省略Flags对照 | 空属性例先2→1再查询失败；未到额外减步／夹0／孵化；省略例保持1并通过检查。外层恢复、最终画面、资源释放仍未知；无真实存档或宿主执行 |''','R6-D-PBS-C05/R6-D-PBS-C06/R6-D-DATA-C01')
append('test-catalog/creature-rpg-wp18-20-24-25-26.md', '''## R6-U14-CI：作者友好度初值（静态设计）

DERIVED_VECTOR／NOT_EXECUTED_THIS_UPDATE。独立有效基础BULBASAUR作者夹具，其余字段、注册表、等级5创建与能力计算依赖正常；无插件，关闭默认招式初始化与创建形态复检，无后续友好写入。先观察编译物种原值，再观察创建成功返回值；不执行随机／创建／档案或宿主。裸创建无确认／取消，前门异常不产生成功返回。正文WP18 §4.1与WP30 §7.1。

| ID | 作者Happiness输入 | 物种／个体静态结果 |
| --- | --- | --- |
| R6-U14-CI01 | 256 | 非负格式接受、所读物种验证不设255上限；物种256、创建直接保留256 |
| R6-U14-CI02 | 255 | 物种255、个体255 |
| R6-U14-CI03 | 属性省略 | 物种默认70、个体70 |
| R6-U14-CI04 | 显式0 | 物种0、个体0，0不被当作省略 |

该夹具不声明默认随附数据超界；普通NPC的成员字段上限与后续覆盖、孵化固定值、正常变化夹限保持各自入口。''','R6-D-PBS-C07')
append('test-catalog/creature-rpg-wp27-28-29-30-33.md', '''## R6-U14-GR：初值与正常变化夹限（静态设计）

全部DERIVED_VECTOR／NOT_EXECUTED_THIS_UPDATE。GR01–04各自采用R6-U14-CI的完整合法基础BULBASAUR／等级5／关闭招式初始化与形态复检／无插件前提，在成功创建后、任何变化前观察；不运行参考或独立模型。GR05是独立普通变化对照，不能用它提前夹限创建初值。正文WP30 §7.1–§7.2。

| ID | 输入／观察点 | 静态预期 |
| --- | --- | --- |
| R6-U14-GR01 | 作者Happiness256，成功创建 | 物种256、个体256；无无条件0–255存储保证 |
| R6-U14-GR02 | 作者Happiness255，成功创建 | 物种255、个体255 |
| R6-U14-GR03 | 省略Happiness，成功创建 | 物种70、个体70 |
| R6-U14-GR04 | 显式Happiness0，成功创建 | 物种0、个体0 |
| R6-U14-GR05 | 合法普通个体h254，walking正常完成；非获得地图、非豪华球、无安抚铃、软上限关，无其它改写 | 基础+1，正常变化后h255；GR-35–GR-42方法、修正、软上限及亲密档旧控制保持；异常未到末端不保证夹限 |''','R6-D-PBS-C07')

(OUT/'edit-receipt.json').write_text(json.dumps(dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),changes=changes),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(document_edit_operations=len(changes),changed_paths=len({x['path'] for x in changes}),status='CANDIDATE_REVISED_PENDING_AUTHOR_CHECK_AND_NONAUTHOR_REVIEW'),ensure_ascii=False))
