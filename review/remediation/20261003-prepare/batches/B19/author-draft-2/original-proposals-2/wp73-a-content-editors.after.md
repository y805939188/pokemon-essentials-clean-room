# WP73-A 规格：内容编辑器（物种/道具/训练家/元数据/图鉴列表）

| 字段 | 内容 |
| --- | --- |
| 工作包 | WP73-A（内容编辑器） |
| 关联功能 | F18-02（数据和世界编辑器，D18——与 WP73-B 分治：本包为内容编辑部分） |
| 分类 | Demo/Developer Experience（主）；Generic Kernel（GameData 持久/编译反写交界）、User Interface（属性框架/列表器/选择器）分别注明；类名/方法名是参考侧取证记录，不是未来框架 API |
| 参考基线 | `reference/pokemon-essentials/` @ commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（WP01 固定） |
| 输入 | 四份编辑器主域文件分段全文（`020_Debug/001_Editor screens/001_EditorScreens.rb` 1,324 行、`020_Debug/002_Editor_DataTypes.rb` 1,706 行、`020_Debug/003_Editor_Listers.rb` 647 行、`020_Debug/001_Editor_Utilities.rb` 410 行，共 4,087 行）；GameData 持久层（load/save/load_all）、地区图鉴装载、训练家新建/转换辅助定点 |
| 前置依赖 | WP04（PBS 生命周期/编译反写，必需）、WP18（个体/图鉴，必需）、WP24（玩家/训练家，必需）、WP27（背包/物品，必需）四份必需；边界引用 WP02/WP03/WP05/WP06/WP07/WP09/WP11/WP15/WP17/WP19/WP20/WP21/WP28/WP30/WP31/WP34/WP36/WP39/WP65（各自具名通过范围，以独立报告为准）；**同批待审依赖** WP72、WP73-B（引用其合同，不作通过结论——当前身份见登记清单） |
| 规格状态 | **ReviewPending（WP73-A 具名静态范围，待统一 review）**：属性编辑器框架（pbPropertyList 与全部属性类型）、训练家类型/训练家战斗/道具/物种/全局与玩家元数据/地区图鉴列表六个内容编辑器的输入、校验、取消、保存与反写合同；共享列表器与选择器。世界编辑器（WP73-B：地图连接/地图元数据/地形/遭遇/指标）、动画工具（WP74）、编译与转换（WP75）不在本状态内 |
| 证据等级 | 全部为静态证据：已定位 / 静态确认 / 数据样本确认；**无运行确认**（未运行游戏/编辑器/UI、未执行编译器或反序列化、未写 PBS/.dat/地图文件、未播放音频、未操作真实存档） |

## 1. 目的、范围与非目标

**目的**：固定内容编辑器的规则合同——**每个内容编辑器读什么输入、按什么校验拒绝、取消时是否仍写入、编辑何时生效（内存/`.dat`/PBS 三层）、引用失效如何提示**。后续包据此判断"某次编辑实际落到了哪一层"，而不是各自重新追踪四份编辑器文件。编辑器实现是作者行为要求的参考，不作为未来编辑器的布局或交互设计模板。

**范围**（WP73-A 自身声明范围）：

1. 属性框架：`pbPropertyList` 的交互与保存提示合同；全部属性类型（数值/文本/布尔/枚举/列表/游戏数据引用/文件引用/地图坐标/复合结构）的输入、默认值、取消与格式化语义。
2. 六个内容编辑器：训练家类型（`pbTrainerTypeEditor`＋新建）、训练家战斗（`pbTrainerBattleEditor`＋`TrainerBattleProperty`＋`TrainerPokemonProperty`）、道具（`pbItemEditor`＋新建）、物种（`pbPokemonEditor`）、全局与玩家元数据（`pbMetadataScreen`/`pbEditMetadata`/`pbEditPlayerMetadata`）、地区图鉴列表（`pbRegionalDexEditorMain`＋`pbRegionalDexEditor`）。
3. 共享基础设施：列表器（Graphics/Music/Metadata/Map/Species/Item/TrainerType/TrainerBattle）、选择器函数（物种/形态/类型/道具/特性/招式/球/GameData 列表）、通用命令窗口（pbCommands2/3、pbChooseList）与工具函数（合法招式、文件安全复制、地图树）。
4. 持久与反写：内存 `DATA` 层 / `.dat` 保存与重载 / `Compiler.write_*` PBS 反写三层的触发时机与取消丢弃语义。

**非目标**：

- 不提取世界编辑器（WP73-B 主责：地图连接、地图元数据、地形标签、遭遇、指标与自动定位——同文件内的 `pbEncountersEditor`/`pbMapMetadataScreen`/`pbEditMapMetadata` 只登记归属）；不提取动画编辑器/组织器/导入导出（WP74——同文件内的 `pbAnimationsOrganiser` 只登记归属）；不提取编译器全集与文件更名/文本抽取/工程转换（WP75）；不展开 GameData schema/编译校验全集（WP03/WP04 主责，本包只引用编辑器调用点）。
- 不重提取已通过规则：PBS 编译与反写生命周期（WP04）、个体/图鉴（WP18）、玩家/训练家（WP24）、背包（WP27）、物种/招式/特性数据语义（WP19/WP31/WP34）、遭遇数据语义（WP36）。同批待审合同不展开：调试入口（WP72，同批待审）。
- 不运行编辑器/编译器/反序列化、不写 PBS/.dat/地图文件、不操作真实存档、不设计未来编辑器布局或 API。

## 2. 概念与术语

- **三层持久模型**：**内存 `DATA` 层**（`GameData::X::DATA` 常量哈希——所有编辑先落在这里）；**`.dat` 层**（`GameData::X.save` 把 `DATA` 序列化写 `Data/X.dat`；`GameData::X.load` 从 `.dat` 整体重载并**丢弃内存改动**——`010_Data/001_GameData.rb:63–69, 138–144, 203–209`）；**PBS 文本层**（`Compiler.write_*` 按 `DATA` 重写对应 PBS 文件——WP04 引用）。**三类保存时机**（§4 逐项）：**逐条即时**（训练家类型/道具/物种/元数据——每次确认保存即 `register`＋`save`＋`write_*`）；**退出时确认**（训练家战斗/地区图鉴——编辑只动内存，退出时 "Save changes?" 确认才 `save`（＋反写），否则 `load` 丢弃——**嵌套例外：训练家战斗新建流程中创建类型立即落盘并反写两份 PBS、可带出先前内存编辑；外层 No 只重载 `.dat`、不回滚已写 PBS**（§4.2，A-R01））；**子编辑返回决定**（嵌套属性编辑的 "Save/Apply changes?" 只决定该子结构是否回写进父编辑的数据数组）。
- **属性列表编辑器（`pbPropertyList`）**：以 `名称=格式化值` 逐行显示属性表；**USE** 调用该属性类型的 `set` 并把**返回值直接赋给该槽**（`set` 的取消语义由各属性类型自定——多数返回旧值即不变，部分返回 nil 即清空）；**ACTION** 对该槽**确认后重置为 `defaultValue`（无 defaultValue 则 nil）**（ReadOnly 除外）；**BACK** 结束编辑——带 `saveprompt` 时给 **"Save changes?" Yes/No/Cancel**：Yes 返回真（调用方执行保存）、No 返回假（不保存）、Cancel 回到编辑；不带 `saveprompt` 时**恒返回 nil**（保存与否由调用方自行决定）。`002:1624–1706`。
- **属性副本与嵌套数据**：局部标量仅改本地槽，父No丢弃；共享蛋招池打开时原地去重/排序，已有地图尺寸可共享改宽，父No不撤销这些运行内存改动、不因此写档案。物种编辑取的是旧复数进化属性，该取值返回空，回落为空进化工作表；打开后父 No 不会发生旧稿声称的数字参数转文本。合法 A→B、B原有反向前身关系且终末的夹具：不编辑进化字段而保存 A，会用空表替换 A 的整进化列表（包括该记录的前身条目），注册与档案/PBS写出成功后 B 的旧反向关系仍留在当前注册/档案；没有即时全体反向关系重建。成功整批重新编译新 PBS 后才从新正向记录重建，B 的旧 A 前身消失。独立保留 C→D 数字参数的记录，PBS 写出使用实际单数 Evolution 属性，该导出分支才将相关嵌套参数转文本；不能归因于打开复数编辑字段。必要外部字段 Evolution 与旧编辑字段的兼容差异保留，源对象组织不作实现要求。
- **列表器（Lister）与块循环（`pbListScreenBlock`）**：列表器提供命令表/起始下标/取值/预览刷新；块循环中 **USE/ACTION 把选中值交给调用方处理**（编辑/删除），处理后重取命令表；**BACK 退出**。空表时直接返回 `value` 以 −1 为实参的结果。`003:4–112`。
- **ID 派生规则（新建类编辑器）**：名称 → é 转 e → 去掉非字母数字下划线 → 全大写；空 → 类型前缀＋序号（`T_%03d`/`ITEM_%03d`）；首字符非字母 → 加前缀；已存在 → 追加 `_1`…`_100` 去重；仍冲突 → 失败消息。`001:392–420, 869–897`。
- **校验拒绝（不写入；A-R02 修订——可达性分开）**：训练家战斗编辑的校验分两级——**清空类型后属性返回空结果、外层立即结束该次编辑**（**不到错误消息**）；**名字为空与队伍为空**才分别给 "Can't save…" 消息并回到编辑（`001:519–525`）；**改键冲突无唯一性拒绝**（先覆盖目标再删旧键——§4.2）；其它编辑器以属性类型自身范围与选择器约束为主（§3 表）。
- **引用失效的显示（A-R06 修订——分两型）**：**有保护**——Species/Item/Type/Move/Ability/TrainerType/SpeciesForm/GameDataProperty 等 `format` 以存在性判定显示 **"-"**；**严格读取**——**BallProperty、`GameDataPoolProperty` 的池内容格式化、`TrainerPokemonProperty` 格式化、`WeatherEffectProperty` 格式化等直接取记录——**失效 ID 可抛异常**（人工/失效数据前提，不声称正常基线必然出错）；训练家图列表器预览加载失败有局部保护回落空白，普通图形预览不继承该保证。**只影响显示或如实报错，不做级联清除**（§3.4）。
- **入口与可达性**：全部编辑器从调试菜单进入（WP72 §8.3 入口表——`$DEBUG` 门在调用侧；受限载入菜单同样可见）；脚本直接调用各公开函数走自身前提，不附加调试门。
- **已通过边界（必须继承，不重开）**：WP04（PBS 编译/反写/校验，含 `validate_compiled_pokemon` 与 `cast_csv_value` 引用点）、WP03（GameData schema/注册语义）、WP18/WP19/WP21/WP24/WP27/WP31/WP34/WP36（数据语义）、WP61/WP53/WP37、WP65、WP67-A/B、GR-001～016、WP23-N01。**同批待审依赖（引用其合同，不作通过结论——BATCH-R03）**：WP72（调试入口与工具归属——含归属更正：本包为其 WP73-A 归属的主体）、WP73-B（世界编辑器——本包为其复用 EncounterSlotProperty 的属主）。

## 3. 属性类型目录（`002_Editor_DataTypes.rb` 全文；按输入行为分组）

### 3.1 框架交互（`pbPropertyList`；`002:1624–1706`）

- 逐行显示 `名称=format(当前值)`；描述窗跟随选中显示该属性说明。
- **USE**：把该槽当前值交给属性类型的 `set`，**返回值无条件赋回该槽**（各类型自行保证取消时返回旧值；返回 nil 的类型即清空语义）。
- **ACTION**：非 ReadOnly 时**确认后重置**——有 `defaultValue` 写默认值、否则写 nil。
- **BACK**：`saveprompt` 为真 → **"Save changes?"**：Yes＝返回真／No＝返回假／Cancel＝继续编辑；为假 → 直接结束且**返回 nil**。

### 3.2 不可编辑与数值型

| 类型 | 输入 | 默认值 | 取消/边界 | 格式化 |
| --- | --- | --- | --- | --- |
| UndefinedProperty | 无（消息"此处不能编辑"） | — | 返回旧值 | inspect |
| ReadOnlyProperty | 无（消息"不可编辑"；ACTION 重置也豁免） | — | 返回旧值 | inspect |
| UIntProperty(maxdigits) | 数值（限位数、默认旧值或 0） | 0 | 数值框自身语义 | inspect |
| LimitProperty(max) | 0–max（旧值缺省 1） | 0 | 同上 | inspect |
| LimitProperty2(max) | 0–max、**取消 −1 → nil** | nil | 取消即清空 | 值或 "-" |
| NonzeroLimitProperty(max) | **1**–max（旧值缺省 1） | 1 | 范围排除 0 | inspect |

### 3.3 布尔/文本/枚举/列表型

- **BooleanProperty**：确认询问（是＝true／否＝false）。**BooleanProperty2**：True/False 选择，取消 → nil；显示 True/False/"-"。
- **StringProperty**：自由文本（**最长 250**）；**LimitStringProperty(limit)**：限长文本。**ItemNameProperty**：限长 30，默认 "???"。
- **EnumProperty(values)**：枚举列表（取消保留旧值；默认 0）；EnumProperty2（常量模块版——**基线标注 Unused**）。
- **StringListProperty**：添加非空值，已有仅移光标；编辑/删除与Keep确认。字符串工作表去重包含当前项本身：单项非空 A 编辑后确认仍 A，或文本 ESC 返回旧 A，都命中自身并删除。Keep changes? Yes 将空表返回父槽，No 保留原集合；父保存门另算。修改为不与任何项相同的新值则保留修改项；空输入不进入这次非空去重。
- **TypesProperty**：双类型槽——逐槽选类型（`pbChooseTypeList`）后 **uniq＋compact**；**有变化且 "Apply changes?" 确认**才生效；默认 [:NORMAL]。

### 3.4 游戏数据引用型（选择器取消＝保留旧值；失效显示分两型，A-R06）

- **单引用**：TrainerTypeProperty、SpeciesProperty（`pbChooseSpeciesList`——仅 0 形态）、SpeciesFormProperty（含形态，显示 `名字_形态`）、TypeProperty（排除伪类型）、MoveProperty、MovePropertyForSpecies（**合法招式优先**——物种升级/教授/蛋招并集排序在前，全招式表随后；`001_Utilities:4–14, 181–218`）、AbilityProperty、ItemProperty、BallProperty（球类子集）、GenderProperty（男/女，取消 → nil）、GameDataProperty（任意 GameData 模块列表）。
- **物种招式预选**：物种招式选择把按名称排序的合法招式段放在按名称排序的全招式段前，重叠招式在两段各保留一次。默认在合法段非首位时保留该位置；在合法段首位时仍可能被全段的局部位置覆盖；仅在全段时也把全段局部位置直接当合并列表位置，不加合法段长度。夹具合法段 [A]、全段 [A,B,C]、默认 C，合并为 [A,A,B,C]，初始零基 2 实为 B，不移动确认返回 B；BACK 选择器返回空，父属性保留 C。必须先有合法物种，不能由默认值推定实际预选招式。
- **文件引用**：BGMProperty／MEProperty（音频列表器——**浏览时试听**、dispose 恢复原 BGM）、WindowskinProperty／CharacterProperty（图形列表器——**预览缩放显示**）；均取**去扩展名文件名**，取消/空保留旧值。
- **地图坐标**：MapProperty（地图列表）；MapCoordsProperty（选图＋**点选坐标**——取消保留旧值）；MapCoordsFacingProperty（再加**朝向四选**——2/4/6/8）；RegionMapCoordsProperty（区域图列表——0 个提示、1 个直选、多个选择——再点选）；MapSizeProperty（宽 1–30＋0/1 有效格串）。
- **WeatherEffectProperty**：天气类型列表 BACK 或选 None 返回空，父槽清空；选新类型 W2 后概率框 BACK 返回旧概率，没有独立取消哨兵，所以旧 W1/30 得 W2/30，而非空或 W1/30。正常确认 60 得 W2/60。返回先写父编辑槽，父 No 丢弃局部值、Yes 才按元数据保存链落盘；不由此断言当前地图已即时切换天气。

### 3.5 复合结构型（A-R05 修订——按子页是否询问分型）

- **无本页询问（BACK 直接返回给父页）**：**IVsProperty、EVsProperty、MapSizeProperty、TrainerPokemonProperty**——属性页关闭时**直接返回**（**没有本页 "Save/No" 选项**）；**IV/EV 初始化还会在传入哈希补数字顺序键**；**EV 超总额要求继续削减**（不能带着超限离开——这不是保存门，返回照样发生）。**父层是否落盘另算**（由父编辑的确认链决定）。
- **有明确保存询问（"Save/Apply/Keep changes?"）**：**BaseStatsProperty、EffortValuesProperty、StringListProperty、TypesProperty、GameDataPoolProperty、LevelUpMovesProperty、EvolutionsProperty**——选 No 时**不把新编辑集合赋入父槽**（"确认才回写"只指新编辑集合）；**但池类进入时的原地去重/排序不被撤销**（§2 A-R04——有没有确认与有没有共享引用是两条独立条件）。
- **不与嵌套别名（§2 A-R04）混为一个事务**：无询问子页的返回值直接赋父槽；有询问子页选 No 时**不把新编辑集合赋入父槽**——**但入口对共享原数组的去重/排序仍保留**（A-R04 v4——新集合不赋回不等于父槽内容没有变化）；两者都**不直接等同落盘**。
- **BaseStatsProperty**：各项 1–255（缺省 10）；保存确认才回写数组。
- **EffortValuesProperty**：各项 0–255；**只保留 >0 的项**回写 `[stat, value]` 对。
- **IVsProperty(limit)**／**EVsProperty(limit)**：按PBS顺序逐项、可空有界数值取消−1→空、超EV总额需削减。IV/EV 整字段未指定时，合法 L20 训练家按正常加载默认每项 IV10/EV30（无插件/钩子改写）。只打开相应子页立即 BACK，会把未指定变为显式六项 0；部分缺项或单项数值取消也在返回时补 0。子页没有本页 No，返回即赋父槽；父 No 仍不提交，父 Yes 注册后外层保存 Yes 才保存档案与反写，外层 No 重载。未打开且保持未指定是默认 10/30 对照。地图尺寸未指定打开即 [宽0,有效格空串]，直接 BACK 也返回它；宽数值框仅实际打开时限定1–30，不把未进入宽框的初始0改成1。
- **GameDataPoolProperty(模块, 允许多个, 自动排序)**：池编辑——**[ADD VALUE]**（`pbChooseFromGameDataList`；不许多个时去重并跳光标）、**Change value**（同上约束）、**Delete**、ACTION+Up/Down 换序；退出 **"Apply changes?"** 确认才回写。子类：**EggMovesProperty**（Move、不许多、自动排序）、**EggGroupsProperty**、**AbilitiesProperty**。
- **LevelUpMovesProperty**：等级＋招式对——**按等级排序**（同级才可换序）；添加（等级 0–最大、取消 −1；同等级同招式去重）；改等级/改招式（目标已存在时**删除本项**）；删除；退出 **"Save changes?"** 确认才回写。
- **EvolutionsProperty**：进化路径（物种＋方法＋参数）——添加（物种选择→方法列表→**参数编辑器**：按方法的参数类型分派——Item/Move/Species/Type/Ability 选择器；**String 类注册**（如 LocationFlag——编辑器的字符串实例匹配不命中类对象，**实际走 0–65,535 数值输入**：默认值数值转换为 0、取消 −1 → nil——**当前基线不能输入任意地区标志文字**；不把意图当已实现、不修参考，A-R07）；**枚举符号**（param_type 为符号常量的方法——对应选择器）；Integer 0–65,535（取消 −1 → nil）；无参数方法跳过）；编辑（改物种/改方法——**改方法后参数重置为 0**/改参数/删除）；**所有改动去重**（已存在相同路径时删除本项并跳光标）；退出 **"Save changes?"** 确认才回写；参数显示（无参数方法省略；未知符号常量显示常量名；空显示 "???"）。
- **进化工作表同值**：进化工作表的物种、方法、参数去重也包含正在编辑项；在本次会话新加一条合法记录，再确认相同物种/方法/参数会删除该项。同方法在参数重置为 0 前先按旧参数检测，所以不能假设同方法总会保留；实际换成未重复的新方法才把参数重置为 0。数值参数 BACK 返回 −1→空，跳过去重并保留项；不推所有取消删除。工作表 Save Yes 才接收新表、No 返回旧表，父物种保存与文件写出另外决定。
- **EncounterSlotProperty**（WP73-B 遭遇编辑复用）：`[概率(1–999), 物种/形态, 最低级, 最高级]`——新建缺省 `[20, 首个物种, 5, 5]`；**最低>最高时交换**；格式化 `概率, 名字[_形态] (Lv.a[-b])`。

## 4. 六个内容编辑器逐项合同

### 4.1 训练家类型（`pbTrainerTypeEditor`＋`pbTrainerTypeEditorNew`；`001:345–443`）

- **列表**：TrainerTypeLister（含 [NEW TRAINER TYPE] 项；预览图 rescue 空白）。
- **USE（已有项）**：按 `editor_properties` 取各属性当前 PBS 值（nil 且属性有 defaultValue 则先填默认）→ `pbPropertyList`（saveprompt）→ **确认保存**：按 schema 组哈希（ID 走 SectionName 键）＋保留 `pbs_file_suffix` → **register＋save＋`pbConvertTrainerData`**（写训练家类型/训练家 PBS 并刷新类型名消息表——`015/002:62–68`）。**不保存**：内存与文件均不变（本次属性数组丢弃）。
- **ACTION（已有项）**：**严肃确认** → `DATA` 删除＋**立即 save＋`pbConvertTrainerData`**＋消息（**删除不走退出确认**）。
- **USE（新建项）**：名称（空且无缺省 → 放弃）→ **ID 派生**（§2）→ 性别三选 → 基础金钱 0–255（默认 30）→ register＋save＋convert＋创建消息＋**图形缺失提示**（`Graphics/Trainers/<ID>.png` 缺失则空白）。

### 4.2 训练家战斗（`pbTrainerBattleEditor`＋`TrainerBattleProperty`＋`TrainerPokemonProperty`；`001:448–599, 604–687`）

- **列表**：TrainerBattleLister（类型/名字/版本排序；预览训练家图＋队伍摘要文本）。
- **内存先行**：全部编辑/删除只改 `GameData::Trainer::DATA` 并置 `modified`；**退出时 `modified 且 "Save changes?" 确认 → save＋`pbConvertTrainerData`；否则 `load` 整体重载丢弃**（`001:593–598`）。
- **USE（已有项，A-R02 修订）**：`TrainerBattleProperty.set`——属性表：类型（TrainerTypeProperty）、名字（StringProperty）、**版本（0–9,999）**、败北台词、**最大队伍数个宝可梦槽**（TrainerPokemonProperty）、**8 个道具槽**（ItemProperty）；**校验可达性**：**清空类型后属性返回空结果、外层立即结束该次编辑**（**不到"未选类型"消息**）；**名字空与队伍空才回校验循环**（分别 "Can't save. No name was entered."／"…Pokémon list is empty."）；通过 → 组哈希（队伍只收有物种的槽、道具只收非空槽、保留 `pbs_file_suffix`）→ register；**改键冲突**：**改成已存在的（类型,名字,版本）键时先 register 覆盖目标、再删旧键——无唯一性拒绝**（对照：A 改为已有 B 的键——内存只剩新 B、旧 A 删除；外层退出 No 仍可由 `.dat` 重载恢复）；**不得借新建 ID 去重逻辑推断编辑改键也去重**；置 modified。
- **USE（新建项，A-R01 修订）**：先定义类型——**用现有**（列表）／**新建类型**（走 §4.1 新建流程——**该嵌套保存立即落盘**：register＋save＋`pbConvertTrainerData` 反写两份训练家 PBS——**且会把先前仅在内存的训练家编辑一并带进 PBS**）／取消；名字（空 → 放弃）；**版本分配**（`pbGetFreeTrainerParty`——0–255 首个空闲，无 → "没有空间"消息）；`pbNewTrainer`（save_changes 为假——`015/002:12–60`）**交互建队**：**首只必选**（循环直到选定——物种列表＋等级（1–最大、缺省 10））、**其后逐个"再加一只？"确认**（拒绝即结束——每只同样物种＋等级逐个选定）；随后编辑器自行组哈希 register＋"已添加"消息＋modified（**此步只动内存**）。**分层对照（A-R01）**：嵌套创建类型后中途放弃（名字取消/外层退出 No）——**类型文件与 PBS 反写已落盘保留**；外层退出 No 只重载训练家 `.dat`（内存编辑丢弃），**不回滚已写 PBS**；只用现有类型则全程无文件写入直到退出确认。
- **ACTION（已有项）**：严肃确认 → `DATA` 删除＋modified＋消息（**文件层仍待退出确认**）。
- **TrainerPokemonProperty（单个宝可梦槽）**：物种（缺省 nil）／等级（1–最大，**NonzeroLimit**）／昵称／形态（0–999）／性别／闪光／超级闪光／Shadow（BooleanProperty2 三态）／**4 招式槽**（MovePropertyForSpecies——**全空即野生招式表**，Z 键删除语义在说明中）／特性／特性位（0–99）／持有物／性格／IVs（EVsProperty 同类 LimitProperty2 子编辑）／EVs（**总额超 EV_LIMIT 循环要求削减**）／友好（0–255）／球（BallProperty）；返回时**招式去重去空**；**物种为 nil → 整个槽返回 nil**（`001:604–681`）。
- **空物种招式分支**：新建空训练家个体槽，物种未选时四个招式字段已可选；选择任一招式先严格查该物种以生成合法招式，空物种导致本地失败，早于整槽结束时的无物种返回空守卫。不补自动禁用/提示修复，也不确定宿主异常画面。直接 BACK 结束空槽正常返回空；先选合法物种再开招式选择正常进入。失败前没有本次文件保存。

### 4.3 道具（`pbItemEditor`＋`pbItemEditorNew`；`001:822–921`）

- **列表**：ItemLister（含 [NEW ITEM]；图标预览）。
- **USE（已有项）**：editor_properties → `pbPropertyList`（saveprompt）→ **确认保存**：schema 组哈希＋保留 suffix → **register＋save＋`Compiler.write_items`**（即时生效，无退出确认）。
- **ACTION（已有项）**：严肃确认 → 删除＋**立即 save＋write_items**＋消息。
- **新建（A-R03 修订）**：名称 → ID 派生（`ITEM_` 前缀系）→ **口袋选择**（PocketProperty，返回 0＝放弃）→ **价格**（0–999,999——**BACK 返回 0 而非 −1**（默认值经钳制、无独立取消值）——**按 BACK 仍继续后续创建（价格 0）**；正常输入 0 同为价格 0——**口袋取消与价格 BACK 是两个不同的分支**）→ 描述（StringProperty）→ register＋save＋write_items＋创建与图形提示消息；复数名自动为 `名称+s`。

### 4.4 物种（`pbPokemonEditor`；`001:926–987`）

- **列表**：SpeciesLister（**不含新建项**——`includeNew` 为假）。
- **USE（已有项）**：身高/体重×10显示，保存÷10回写，按schema组数据、保留后缀、净化与合法参数类型重铸，注册→档案保存→物种PBS写出→完成消息。物种编辑取的是旧复数进化属性，该取值返回空，回落为空进化工作表；打开后父 No 不会发生旧稿声称的数字参数转文本。合法 A→B、B原有反向前身关系且终末的夹具：不编辑进化字段而保存 A，会用空表替换 A 的整进化列表（包括该记录的前身条目），注册与档案/PBS写出成功后 B 的旧反向关系仍留在当前注册/档案；没有即时全体反向关系重建。成功整批重新编译新 PBS 后才从新正向记录重建，B 的旧 A 前身消失。独立保留 C→D 数字参数的记录，PBS 写出使用实际单数 Evolution 属性，该导出分支才将相关嵌套参数转文本；不能归因于打开复数编辑字段。必要外部字段 Evolution 与旧编辑字段的兼容差异保留，源对象组织不作实现要求。
- **ACTION（已有项）**：严肃确认 → 删除＋**立即 save＋write_pokemon**＋消息。
- **新建**：**不支持**——"Can't add a new species."消息（`001:982`）。

### 4.5 全局与玩家元数据（`pbMetadataScreen`/`pbEditMetadata`/`pbEditPlayerMetadata`；`001:692–774`）

- **顶层**：MetadataLister——**[GLOBAL METADATA]**＝编辑全局、**Player N**＝编辑该角色、**[ADD NEW PLAYER]**＝新建角色（取最小未用 ID）；BACK 退出。
- **编辑**：editor_properties → `pbPropertyList`（saveprompt）→ **确认保存**：schema 组哈希（全局元数据补 ID 为 0 的键；保留 suffix）→ **register＋save＋`Compiler.write_metadata`**（即时生效）。**角色不存在** → "未找到"消息返回；新建角色先以含新 ID 的数据实例化再进同一流程。

### 4.6 地区图鉴列表（`pbRegionalDexEditorMain`＋`pbRegionalDexEditor`；`001:992–1202`）

- **主界面**：现有图鉴列表（从 `Data/regional_dexes.dat` 惰性装载的**克隆**——`001_MiscPBSData:28–34`）＋**[ADD DEX]**；**Z+Up/Down 换序**；点选：**ADD**（空白填充／全国图鉴填充——`each_species` 全物种／**按进化族分组填充**——`get_family_species` 去重连接）；**已有项**：Edit（进子编辑）/Copy（克隆追加）/Delete（无确认直接删）。
- **子编辑（单个图鉴，A-R08 修订）**：**进入先移除全部空项**再取编辑副本；条目列表（nil 显示 "----------"）；**Z+Up/Down 换序、Z+Right 插入、Z+Left 删除、D 清空**；点选条目：**Change species**（物种选择——**自动去除其它位置的同物种**保证唯一）、Clear、Insert、Delete；**退出返回全量去空、父层总是接收**——**子 No 也压空洞**（[A，空，B] 不作编辑选 No，主界面得到 [A,B]）；子 Yes 同理回写；**空表保存分支非终止**（删除末项直到末项非空——**空表没有终止条件：静态推导未运行**——空白新图鉴或清空全表后选 Yes 无法退出该循环，**不保证空表可正常保存**）；外层主界面仍有克隆与最终保存门（**外层 No 不写 `.dat`**）。
- **总保存**：主界面 BACK → **"Save changes?" Yes**：**写 `Data/regional_dexes.dat`（`save_data`）＋清运行缓存（`$game_temp` 的地区图鉴缓存置空）＋`Compiler.write_regional_dexes`**＋"Data saved."；No：退出不写（**克隆被弃——原数据不变**）；Cancel：回到编辑。

## 5. 共享基础设施（`003_Editor_Listers.rb`、`001_Editor_Utilities.rb` 全文）

- **通用窗口**：`pbListWindow`（小字体命令窗）；`pbListScreen`（一次性选择——USE 选定/BACK 取消，空表直接返回 `value` 以 −1 为实参的结果）；`pbListScreenBlock`（USE/ACTION 交块处理；BACK 退出——**删除尾项后下标保持为新命令数（不是钳到最后有效项）**：窗口赋下标不校验范围，**可见选中可能失效——静态边界如实登记，不推断像素表现**，A-R09）；`pbCommands2`（USE/BACK，取消值可正可负）；`pbCommands3`（**SPECIAL＝[5]、ACTION+Up/Down＝[1]/[2] 换序、ACTION+Left/Right＝[3]/[4] 插删**）；`pbChooseList`（ID/字母双序切换——ACTION 换序；符号 ID 按第三列匹配）。
- **列表器**：GraphicsLister（png/gif 扫描＋**预览缩放**、"无文件"消息）；MusicFileLister（wav/ogg/mp3/midi/mid/wma、**浏览试听、dispose 恢复原播放**）；MetadataLister（全局/角色/新建三分）；MapLister（**地图树缩进显示**＋小地图预览；可选 [GLOBAL] 项返回 0）；SpeciesLister（字母序、可选 [NEW SPECIES]）；ItemLister（字母序＋图标）；TrainerTypeLister（字母序＋图像 rescue 空白）；TrainerBattleLister（类型/名字/版本三级排序＋训练家图与队伍摘要）。
- **选择器**：`pbChooseFromGameDataList`（模块＋可选块过滤）；`pbChooseSpeciesList`（**只列 0 形态**）；`pbChooseSpeciesFormList`（含形态 `名字_形态`）；`pbChooseTypeList`（**排除伪类型**）；`pbChooseItemList`／`pbChooseAbilityList`／`pbChooseMoveList`（全表）；`pbChooseMoveListForSpecies`（合法招式在前）；`pbChooseBallList`（球类子集、**取消返回旧值**）。
- **工具**：`pbGetLegalMoves`（升级＋教授＋蛋招去重——WP34 引用）；`pbSafeCopyFile`（**存在且内容相同则跳过、不同则确认覆盖**——WP74 引用）；`pbAllocateAnimation`（首个空槽/空动画位；**无空槽时集合调整为目标长度 10（不是增加 10 个槽位）并返回调整前长度**——**原长度超 10 时尾部被截断**；随后导入写到返回下标可重新扩展，但**被截断内容不恢复**（12 项均非空的集合：分配先截成 10、返回 12，写 12 号位时旧 10/11 号内容已丢失）——WP74 引用，A-R10）；`pbMapTree`（按 parent_id 层级与 order 排序的地图树——WP11 数据引用）。

## 6. 生效时机与取消语义汇总（本包核心问题）

| 编辑器 | 编辑落点 | 文件生效时机 | 取消路径 |
| --- | --- | --- | --- |
| 训练家类型（编辑/删除/新建） | 内存 register | **每次确认即** save＋write_trainer_types/trainers | pbPropertyList 选 No → 不写（标量槽位是本地副本——共享嵌套对象例外见 §2 A-R04） |
| 训练家战斗（编辑/删除/新建） | 内存 DATA＋modified | **退出时确认才** save＋write_trainer_types/trainers——**嵌套例外（A-R01）：新建流程中创建类型立即落盘并反写两份 PBS（可带出先前内存编辑）** | 退出选 No → **load 重载丢弃全部内存改动**（含删除）——**不回滚已写 PBS**；只用现有类型则全程无文件写入直到退出确认 |
| 道具（编辑/删除/新建） | 内存 register | **每次确认即** save＋write_items | pbPropertyList 选 No → 不写 |
| 物种（编辑/删除） | 内存 register | **每次确认即** save＋write_pokemon | 同上；新建不支持 |
| 全局/玩家元数据 | 内存 register | **每次确认即** save＋write_metadata | 同上 |
| 地区图鉴 | 克隆数组（子编辑进入先去空、退出全量去空——**子 No 也压空洞**，A-R08） | **退出时确认才** save_data(dat)＋清缓存＋write_regional_dexes | 选 No → 克隆被弃；**空表保存分支非终止（静态推导未运行）——不保证空表可正常保存** |
| 有询问子结构（升级招式/进化/池/字符串列表/类型对/基础能力/努力产出） | 子编辑返回数组 | 随父编辑的保存确认回写进父数据 | 子编辑 "Save/Apply/Keep changes?" 选 No → **不把新集合赋父槽**（**池类进入时原地规范化不被撤销**，§2 A-R04） |
| 无询问子结构（IV/EV/地图尺寸/训练家个体，A-R05） | **BACK 直接返回赋父槽** | 父层确认链决定 | **无本页 No 选项**（EV 超总额要求继续削减——不是保存门）；父层不保存则该次改动不保留（共享嵌套对象例外见 §2 A-R04） |

- **取消仍写入的情形（如实登记，A-R04）**：`pbPropertyList` 的 **ACTION 重置**与 **USE 赋值**在进入 "Save changes?" 之前就已写入**本地属性数组**——多数槽位只影响内存副本；**但共享嵌套对象（蛋招池/已有地图尺寸；旧复数进化取值例外见§2）的原地操作不等待父层确认即可改变运行内存**（§2——**不写 `.dat` 但内存可变**）；真正落盘都经上表确认链或 §4 逐项即时链。**外层取消不撤回嵌套创建类型已写入的类型文件与 PBS**（§4.2 已具名）；**不保证整个被取消流程没有文件变化**——区分"取消动作是否新增写盘"与"取消整个流程后是否已有文件变化"（A-R01 v4）。
- **生效（运行时可见）**：`.dat` 保存后运行时读取方立即用新数据（运行期 `DATA` 已同步）；PBS 反写**按当时内存 `DATA` 重写**（WP04 生命周期——**反写后可与 `.dat` 不同**：嵌套反写保留而 `.dat` 被重载回旧值的对照见 §4.2/§6，A-R01）；地区图鉴另清 `$game_temp` 缓存强制下次重载。

## 7. 同文件边界归属（只登记，不展开）

- **WP73-B（同 `001_EditorScreens.rb`）**：`pbEncountersEditor`（遭遇集/类型/槽三层编辑＋退出 "Save changes?" 确认——save＋write_encounters，否则 load 丢弃）、`pbMapMetadataScreen`/`pbEditMapMetadata`（地图元数据——save＋write_map_metadata 即时）。
- **WP74（同 `001_EditorScreens.rb`）**：`pbAnimationsOrganiser`（动画表 Z 序换序/插删＋"Save changes?"——写 `Data/PkmnAnimations.rxdata`＋清缓存）。
- **WP04/WP75**：`Compiler.write_*` 反写与 `validate_compiled_pokemon`/`cast_csv_value` 净化/重铸为引用点；编译全集与转换归 WP75。

## 8. 默认行为与配置变体

- **配置值（WP02 引用）**：`MAX_PARTY_SIZE`（训练家队伍槽数）、`Settings.bag_pocket_names`（口袋选择表）、`GrowthRate.max_level`（等级上限）、`Pokemon::IV_STAT_LIMIT/EV_STAT_LIMIT/EV_LIMIT`（个体值/努力值上限）、`MAX_MONEY` 等按各属性范围生效。
- **新建 ID 派生**：§2 规则；**新建物种不支持**；新建训练家为**交互建队**（首只必选、其后逐个"再加一只？"确认——`pbNewTrainer` 流程引用，A-R01；WP24/WP39）。
- **未验证组合**：编辑器实际运行表现、预览/试听素材存在性（WP15/U01）、编译反写的完整诊断（WP04）、PBS 与 `.dat` 不一致时的实际消费方行为。

## 9. 边界、失败与未知

- **校验拒绝（A-R02/A-R03 分型）**：训练家战斗编辑——**清空类型后属性返回空、外层立即结束该次编辑（不到错误消息）**；**名字空与队伍空**才分别 "Can't save…" 回校验循环；新建 ID 冲突失败；新建训练家版本满（0–255 用尽）"没有空间"；训练家类型/道具新建的名称为空放弃（有缺省名时回落缺省）；新建道具**口袋返回 0 放弃**（**价格 BACK 返回 0 并继续创建——不是取消 −1 放弃**，A-R03）；EvolutionsProperty 参数类型缺失时按 nil 处理；EV 总额超限循环。**拒绝时不写文件**。
- **删除**：训练家类型/道具/物种的 ACTION 删除**立即落盘**（严肃确认后）；训练家战斗删除**待退出确认**；地区图鉴删除**无确认**（主界面即时）。
- **引用失效（A-R06 两型）**：**有保护的 format 显示 "-"**（Species/Item/Type/Move/Ability/TrainerType 等）；**严格读取的 format 可抛异常**（Ball/池内容/训练家个体/天气——人工/失效数据前提，§3.4）；训练家图预览有局部保护回落空白，普通图形预览不继承该保证；**不做级联清除或自动修复**（失效引用保留在数据里，运行时语义归各数据主责包）。
- **异常路径**：目录缺失与已存在但为空分开：Windowskin 的 Graphics/Windowskins 或音乐 Audio/BGM 缺失时，在列文件的进入目录处失败，早于「没有文件」消息与正常释放；已建空目录才正常提示无文件并返回。原播放为空的合法夹具可直接定位此链；正常退出才恢复原 BGM，不推异常退出必恢复。训练家图预览有局部保护，失败回落空白；普通图形列表的位图预览没有等价保护，命名文件加载失败可传播。宿主最终呈现/清理未验证。 未知/只读属性返回旧值并提示；逐项保存仍不承诺事务回滚。
- **未知/未证**：编辑器实际运行表现与宿主窗口行为；素材存在与试听/预览（WP15/U01）；demo 中调试入口的默认可达性（WP77/U01）；PBS 反写与手工编辑并发时的外部一致性（WP04/WP75 边界）。

## 10. 可复核性与静态场景

### 10.1 复核方式

| 事实 | 复核方式 |
| --- | --- |
| 六个内容编辑器（训练家类型/训练家战斗/道具/物种/元数据/地区图鉴） | 阅读 `S/020_Debug/001_Editor screens/001_EditorScreens.rb`（1,324 行全文） |
| 属性框架与全部属性类型 | 阅读 `S/020_Debug/002_Editor_DataTypes.rb`（1,706 行全文） |
| 列表器与通用窗口 | 阅读 `S/020_Debug/003_Editor_Listers.rb`（647 行全文） |
| 选择器与工具函数 | 阅读 `S/020_Debug/001_Editor_Utilities.rb`（410 行全文） |
| GameData 持久层（load/save/load_all） | `S/010_Data/001_GameData.rb:55–75, 130–150, 195–215, 240–250` |
| 地区图鉴装载 | `S/010_Data/002_PBS data/001_MiscPBSData.rb:28–40` |
| 训练家新建/转换/版本分配 | `S/015_Trainers and player/002_Trainer_LoadAndNew.rb:12–110` |
| 数据文件常量（trainers.dat 等） | `S/010_Data/002_PBS data/015_Trainer.rb:1–15`（同类各文件同构——`001_GameData.rb` 基类方法） |
| 调试入口归属 | WP72 主稿 §8.3（已登记入口表；本包为其 WP73-A 归属的主体） |

### 10.2 静态推导场景（未运行，待运行验证）

| 场景 | 输入 | 推导预期 |
| --- | --- | --- |
| M01 pbPropertyList 交互（人工夹具） | a) USE 编辑某槽后 BACK 选 Yes；b) BACK 选 No；c) BACK 选 Cancel；d) ACTION 某槽 | a) 返回真（调用方保存）；b) 返回假（不保存）；c) 回到编辑；d) 确认后该槽写 defaultValue（无则 nil；ReadOnly 不响应） |
| M02 取消语义分型（人工夹具） | 普通0–255旧7、UInt旧5 BACK；可空有界数值旧7 BACK；普通确认否；可空三态布尔BACK；物种BACK；天气None | 依次返回7、5；空；false；空；旧物种；空。普通数值无独立取消哨兵，可空数值显式−1，普通确认与三态选择分开。 |
| M03 训练家类型编辑保存链（人工夹具） | 已有类型：改名字段后选 Yes／选 No | Yes：register＋save＋pbConvertTrainerData（类型名消息表刷新＋两 PBS 反写）；No：内存与文件均不变 |
| M04 训练家类型删除（人工夹具） | ACTION 已有类型并严肃确认 | **立即** DATA 删除＋save＋convert＋消息（无退出确认）；拒确认则不动 |
| M05 新建训练家类型 ID 派生（A-R11；人工夹具） | a) 名称 "Café Owner"；b) 名称 "123"；c) 与既有 ID 冲突 | a) ID **"CAFEOWNER"**（é→e、去非字母数字、大写）；b) "T_123"（首字符非字母加前缀）；c) 追加 _1…_100 去重，仍冲突→失败消息 |
| M06 训练家战斗校验与改键（A-R02；人工夹具） | a) 清掉类型后保存；b) 名字清空保存；c) 队伍全空槽保存；d) 全部合法保存且改了名字；e) 把键改成已存在的（类型,名字,版本） | a) **属性返回空结果、外层立即结束该次编辑——不到错误消息**；b) "…No name was entered."回到校验循环；c) "…Pokémon list is empty."回到校验循环；d) register 新键＋**删除旧键**＋modified；e) **先覆盖目标、再删旧键——无唯一性拒绝**（内存只剩新键；外层退出 No 仍可由 `.dat` 重载恢复） |
| M07 训练家战斗退出确认（人工夹具） | a) 编辑后退出选 Yes；b) 删除后退出选 No | a) save＋convert（改动落盘）；b) **load 重载——删除被撤销** |
| M08 新建训练家战斗（A-R01；人工夹具） | a) 新建类型链完整后中途放弃（名字取消）；b) 版本 0–255 全占用；c) 只用现有类型并退出 No | a) **类型文件与 PBS 反写已落盘保留**（嵌套保存），交互建队未开始；此前内存中的其它训练家编辑**可已被反写带进 PBS**——外层 No 只重载 `.dat`、不回滚 PBS；b) "没有空间"消息、不建；c) **全程无文件写入**（内存改动随 load 丢弃） |
| M09 TrainerPokemonProperty（人工夹具） | a) 物种留空；b) 四招式槽全空；c) EV 总额超限 | a) 整槽返回 nil（父编辑视为空槽）；b) 招式表空＝**野生招式表**（说明文本）；c) 消息要求削减并**回到子编辑**（不能带着超限离开） |
| M10 道具编辑/新建（人工夹具） | a) 已有道具改价后 Yes；b) ACTION 删除；c) 新建（口袋选 0） | a) register＋save＋write_items；b) 严肃确认后**立即**删除落盘；c) 放弃（不写） |
| M11 物种编辑（人工夹具） | a) 身高显示值；改后 Yes；b) ACTION 删除；c) 新建项 | a) 显示为实际 ×10；保存时 /10 回写＋validate 净化＋进化参数按方法重铸＋save＋write_pokemon＋"Data saved."；b) 严肃确认后立即删除落盘；c) "Can't add a new species."消息 |
| M12 元数据编辑（人工夹具） | a) 顶层选 GLOBAL；b) 选 Player 2（不存在）；c) ADD NEW PLAYER；d) 保存 Yes | a) 编辑全局（保存补 ID 为 0 的键）；b) "未找到"消息；c) 取最小未用 ID 实例化后进入同一属性编辑；d) register＋save＋write_metadata |
| M13 地区图鉴主界面（人工夹具） | a) ADD→全国图鉴填充；b) ADD→按族填充；c) Copy 一个图鉴；d) 退出选 No | a) 全物种顺序入列；b) 进化族去重连接；c) 克隆追加到末尾；d) **克隆被弃、.dat 不变** |
| M14 地区图鉴子编辑（A-R08；人工夹具） | a) 进入含 [A,空,B] 的图鉴不作编辑选 No；b) Z+Left 删条目；c) Change species 选已在其它位的物种；d) 主界面退出选 Yes；e) 空白新图鉴或清空全表后选 Yes（静态推导） | a) **主界面得到 [A,B]**（进入先去空、退出全量去空——子 No 也压空洞）；b) 删除并刷新；c) **其它位自动清 nil**（唯一性）；d) **写 .dat＋清缓存＋write_regional_dexes＋"Data saved."**；e) **非终止**（删除末项直到末项非空——空表无终止条件，**静态推导未运行，不保证空表可正常保存**；外层 No 仍不写 .dat） |
| M15 GameDataPoolProperty（A-R04/R05；人工夹具） | a) 不许多个时添加重复值；b) 改值为已存在值；c) 退出选 No；d) 非空无序蛋招池仅打开后选 No | a) 不追加、光标跳到既有项；b) **删除本项**并跳光标；c) **不把新编辑集合赋父槽**（有询问子页选 No 不接收新集合——**进入时的原地去重/排序不被撤销**，见 d 对照）；d) **原数组可已排序**（池编辑打开即对原嵌套数组原地去重/排序——不写 `.dat` 但运行内存可变；无本页 No 能阻止） |
| M16 LevelUpMovesProperty（人工夹具） | a) 添加同级同招；b) 改等级撞到已有同级同招；c) 同级换序；d) 退出 Yes | a) 不新增、光标跳已有；b) **删除本项**、光标跳已有；c) 仅同级可换；d) 去辅助列后回写（等级排序） |
| M17 EvolutionsProperty（A-R07；人工夹具） | 同会话新增合法进化项；相同物种/方法/数值参数确认；数值参数BACK；合法不同方法；无参数；字符串类注册地点旗标 | 进化工作表的物种、方法、参数去重也包含正在编辑项；在本次会话新加一条合法记录，再确认相同物种/方法/参数会删除该项。同方法在参数重置为 0 前先按旧参数检测，所以不能假设同方法总会保留；实际换成未重复的新方法才把参数重置为 0。数值参数 BACK 返回 −1→空，跳过去重并保留项；不推所有取消删除。工作表 Save Yes 才接收新表、No 返回旧表，父物种保存与文件写出另外决定。 地点旗标实际数值0–65,535，不任意文字；无参数只提示。 |
| M18 列表器行为（人工夹具） | Graphics/Windowskins与Audio/BGM分别不存在或存在空目录；音乐正常退出；地图GLOBAL；删除尾项 | 目录缺失与已存在但为空分开：Windowskin 的 Graphics/Windowskins 或音乐 Audio/BGM 缺失时，在列文件的进入目录处失败，早于「没有文件」消息与正常释放；已建空目录才正常提示无文件并返回。原播放为空的合法夹具可直接定位此链；正常退出才恢复原 BGM，不推异常退出必恢复。训练家图预览有局部保护，失败回落空白；普通图形列表的位图预览没有等价保护，命名文件加载失败可传播。宿主最终呈现/清理未验证。 GLOBAL返回0，删除尾项下标仍为新命令数不钳。 |
| M19 选择器（人工夹具） | 合法物种0形态；类型排除伪类型；合法[A]/全[A,B,C]/默认C，不移动确认或BACK；球BACK | 物种招式选择把按名称排序的合法招式段放在按名称排序的全招式段前，重叠招式在两段各保留一次。默认在合法段非首位时保留该位置；在合法段首位时仍可能被全段的局部位置覆盖；仅在全段时也把全段局部位置直接当合并列表位置，不加合法段长度。夹具合法段 [A]、全段 [A,B,C]、默认 C，合并为 [A,A,B,C]，初始零基 2 实为 B，不移动确认返回 B；BACK 选择器返回空，父属性保留 C。必须先有合法物种，不能由默认值推定实际预选招式。 物种仅0形态、类型排除伪类型、球BACK保留旧值。 |
| M20 生效时机总核（A-R01/R05/R08；静态核对） | 六编辑器各执行一次确认保存与一次取消；另核新建嵌套与无询问子页 | 与 §6 表逐行一致：逐条即时类（类型/道具/物种/元数据）确认即三层同步；退出确认类（训练家战斗/图鉴）取消即 load/弃克隆——**嵌套例外：新建流程创建类型的 PBS 反写已落盘保留**；**无询问子页 BACK 直接赋父槽**（EV 超限要求削减不是保存门）；**空表保存分支非终止**；**除已具名的嵌套反写外，无其它"取消仍落盘"路径**（嵌套例外与总则同表成立） |

## 11. 证据与来源（traceability）

- **本轮复核（2026-10-02，首版）**：四份编辑器主域文件**分段全文阅读**（`001_EditorScreens.rb` 1–1,324；`002_Editor_DataTypes.rb` 1–1,706；`003_Editor_Listers.rb` 1–647；`001_Editor_Utilities.rb` 1–410，共 4,087 行）。
- **定点阅读**：`010_Data/001_GameData.rb:55–75, 130–150, 195–215, 240–250`；`010_Data/002_PBS data/001_MiscPBSData.rb:28–40`；`015_Trainers and player/002_Trainer_LoadAndNew.rb:12–110`；`010_Data/002_PBS data/015_Trainer.rb:1–15`。
- **继承同基线既有记录**：WP04（PBS 编译/反写/校验——`Compiler.write_*`、`validate_compiled_pokemon`、`cast_csv_value` 引用）；WP03（GameData schema/注册）；WP18/WP19/WP21（个体/属性/形态）；WP24（玩家/训练家——`pbNewTrainer`/训练家数据语义）；WP27（背包/口袋）；WP31/WP34（招式/育种数据）；WP36（遭遇数据语义——WP73-B 主责其编辑器）；WP61（`d84dff78`）、WP53（`75fc4db7`）、WP37（`d032f5b7`）、WP65、WP67-A/B、GR-001～016、WP23-N01（各自具名通过范围）；**同批待审依赖**：WP72（调试入口与工具归属——当前身份见登记清单，不沿用 v1 短哈希）。
- 全部静态证据；**无运行确认**（未运行编辑器/游戏/UI、未执行编译器或反序列化、未写 PBS/.dat/地图文件、未播放音频、未操作真实存档、未访问网络）。

## 12. 未决问题

1. 编辑器实际运行表现与宿主窗口/素材行为（预览图、试听、小地图——WP15/U01）。
2. PBS 反写与外部手工编辑并发时的一致性（WP04/WP75 边界）；`Compiler.write_*` 的诊断输出细节（WP04）。
3. demo 中各编辑器入口的默认可达性与真实使用编排（WP77/U01）。
4. `pbNewTrainer` 交互建队流程的完整合同（首只必选与逐个确认的详细行为——WP24/WP39 主责；本包只引用调用点）。

## 13. 状态与后续

- 2026-10-02 **统一首审修订 v2**（统一 review 34 项中 WP73-A 的 11 项＋共通 3 项）：**R01** 新建流程嵌套保存分层——创建类型立即落盘并反写两份 PBS（可带出先前内存编辑）；外层 No 只重载 `.dat` 不回滚 PBS；交互建队首只必选、后续逐个确认。**R02** 校验可达性——清空类型立即结束该次编辑（不到消息）；名字空/队伍空才回校验循环；改键冲突先覆盖目标再删旧键（无唯一性拒绝）。**R03** 新道具价格 BACK 返回 0 而非 −1（继续创建价格 0；口袋取消才是放弃）。**R04** 属性副本三类——局部标量/共享嵌套对象（蛋招池/地图尺寸/进化路径原地操作）/原地规范化（不写 `.dat` 但内存可变）。**R05** 子页分型——无本页询问（IV/EV/地图尺寸/训练家个体 BACK 直接赋父槽）与有询问子页分开；EV 超限要求削减不是保存门。**R06** 失效引用分两型——有保护显示 "-" 与严格读取可抛异常（球/池内容/训练家个体/天气格式化）。**R07** String 类注册的进化参数（LocationFlag）实际走数值框（0–65,535、默认 0）——不能输入任意文字。**R08** 图鉴子编辑进入先去空、退出全量去空（子 No 也压空洞）；空表保存分支非终止（静态推导未运行）。**R09** 删除尾项后下标保持为新命令数（不是钳到最后有效项——可见选中可能失效）。**R10** 动画分配无空槽时调整为目标长度 10 并返回调整前长度（超长截断不恢复）。**R11** ID 向量更正为 CAFEOWNER。**BATCH-R01** 正文哈希构造式改独立散文。**BATCH-R02** 数量按最终文件重算。**BATCH-R03** 同批 WP72/WP73-B 引用改为同批待审记法。场景 M01–M20 保留（v2 修订 8 行：M05、M06、M08、M14、M15、M17、M18、M20）；v1 被审身份 `4c3e591c` 留史；v1 材料不改写。
- WP73-A 自身范围（第 1 节四项）已提取并自检，2026-10-02 首版登记 **ReviewPending（具名静态范围，待统一 review）**；不自行标 Reviewed、不宣称通过。依据用户批次授权（WP72＋WP73-A＋WP73-B）与 `planning/extraction-plan.md` 的 WP73-A 任务定义执行；四份编辑器主域文件分段全文阅读、持久层与训练家辅助定点核对并建立覆盖映射（见交付目录附表）。
- 2026-10-02 **统一首审修订 v3**（v2 有限复审剩余 5 项＋共通项）：**R01** 总述原位限定——§2 退出确认条补嵌套例外、§6 生效条改为"PBS 按当时内存 DATA 重写（反写后可与 `.dat` 不同）"、§8/§13 示例队伍改交互建队；M20 改为"除已具名嵌套反写外无其它取消后留盘路径"（不再一边保例外一边断言无留盘路径）。**R02** §9 失败汇总改为可达性分型（清空类型立即结束该次编辑、不到消息；名字空/队伍空才回校验循环）。**R03** §9 删除价格取消 −1 放弃断言（口袋返回 0 才是放弃；价格 BACK 返回 0 继续创建）。**R04** 有询问子页选 No 的保证限定为不把新编辑集合赋父槽（池类进入时原地去重/排序不被撤销——确认与共享引用是两条独立条件）；§3.5/§6 表/M15-c 同步。**R06** §3.4 标题与 §9 失败汇总同步为失效显示两型（有保护 "-"／严格读取可抛异常）。**BATCH-R01** 附表取值调用式改散文；全量 13 文本广谱复核。**BATCH-R02** 修改行清单按实测更正（v2 实际修订 9 行：M05、M06、M08、M12、M14、M15、M17、M18、M20——v2 声明遗漏 M12 已补）；阅读范围与身份清单同口径。**BATCH-R03** 前置依赖/非目标/证据/状态四处把 WP72/WP73-B 从已通过规则分出为同批待审；依赖身份指向登记清单、不沿用 v1 短哈希。v2 被复审身份 `dd4f9b2a`／47,378 与 v2 附表 `9adf6118`／12,144 留史；v1/v2 材料与审查原件不改写。
- 2026-10-02 **统一首审修订 v4**（v3 有限复审剩余 2 项＋BATCH-R02 记录更正）：**R01** §6 取消总结改为"外层取消不撤回嵌套创建类型已写入的类型文件与 PBS——不保证整个被取消流程没有文件变化"（区分取消动作是否新增写盘与取消整个流程后是否已有文件变化）。**R04** §3.5 事务条与池专行统一为"选 No 不把新编辑集合赋入父槽，但入口对共享原数组的去重/排序仍保留"（确认才回写只指新编辑集合——新集合不赋回不等于父槽内容没有变化）。**BATCH-R02** 当轮改动与累计改动、案例新增与重改、语义与纯格式变化分别计数（本轮主稿实际修订 M15／M20 两行的重新限定，累计修订仍为 9 行）；前态字节按实测更正。v3 被复审身份 `81a96fe0`／50,432 与 v3 附表 `6bd60c9a`／12,322 留史；v1/v2/v3 材料与审查原件不改写。
- **已通过边界原样继承**：WP04、WP61（`d84dff78`）、WP53（`75fc4db7`）、WP37（`d032f5b7`）、WP65、WP67-A/B、GR-001～016、WP23-N01——本包只引用其合同，不重开、不修改 reference；**同批待审依赖（不作通过结论）**：WP72、WP73-B（当前身份见登记清单，不沿用 v1 短哈希）。
- **WP73-A 完成 ≠ F18-02 完成**：世界编辑器归 WP73-B；编辑器运行验证、素材、demo 编排保留；Feature Matrix 按聚合规则分别显示，不将整个 D18 标完成。
- 后续包引用本文的编辑器合同（三层持久、保存时机表、属性类型目录、校验拒绝）时，不得把参考侧类/方法组织当作未来框架的 API；发现与本文冲突的新证据时，先修订本文并通知受影响包。批次内后续（WP73-B）与整体 double review（WP78/79）、WP80 净化交付按 extraction-plan 执行，本包完成不自动推进。
