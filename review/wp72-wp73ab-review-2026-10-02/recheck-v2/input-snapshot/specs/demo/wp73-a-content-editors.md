# WP73-A 规格：内容编辑器（物种/道具/训练家/元数据/图鉴列表）

| 字段 | 内容 |
| --- | --- |
| 工作包 | WP73-A（内容编辑器） |
| 关联功能 | F18-02（数据和世界编辑器，D18——与 WP73-B 分治：本包为内容编辑部分） |
| 分类 | Demo/Developer Experience（主）；Generic Kernel（GameData 持久/编译反写交界）、User Interface（属性框架/列表器/选择器）分别注明；类名/方法名是参考侧取证记录，不是未来框架 API |
| 参考基线 | `reference/pokemon-essentials/` @ commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（WP01 固定） |
| 输入 | 四份编辑器主域文件分段全文（`020_Debug/001_Editor screens/001_EditorScreens.rb` 1,324 行、`020_Debug/002_Editor_DataTypes.rb` 1,706 行、`020_Debug/003_Editor_Listers.rb` 647 行、`020_Debug/001_Editor_Utilities.rb` 410 行，共 4,087 行）；GameData 持久层（load/save/load_all）、地区图鉴装载、训练家新建/转换辅助定点 |
| 前置依赖 | WP04（PBS 生命周期/编译反写，必需）、WP18（个体/图鉴，必需）、WP24（玩家/训练家，必需）、WP27（背包/物品，必需）四份必需；边界引用 WP02/WP03/WP05/WP06/WP07/WP09/WP11/WP15/WP17/WP19/WP20/WP21/WP28/WP30/WP31/WP34/WP36/WP39/WP65/WP72（各自具名通过范围，以独立报告为准） |
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
- 不重提取已通过规则：PBS 编译与反写生命周期（WP04）、个体/图鉴（WP18）、玩家/训练家（WP24）、背包（WP27）、物种/招式/特性数据语义（WP19/WP31/WP34）、遭遇数据语义（WP36）、调试入口（WP72）。
- 不运行编辑器/编译器/反序列化、不写 PBS/.dat/地图文件、不操作真实存档、不设计未来编辑器布局或 API。

## 2. 概念与术语

- **三层持久模型**：**内存 `DATA` 层**（`GameData::X::DATA` 常量哈希——所有编辑先落在这里）；**`.dat` 层**（`GameData::X.save` 把 `DATA` 序列化写 `Data/X.dat`；`GameData::X.load` 从 `.dat` 整体重载并**丢弃内存改动**——`010_Data/001_GameData.rb:63–69, 138–144, 203–209`）；**PBS 文本层**（`Compiler.write_*` 按 `DATA` 重写对应 PBS 文件——WP04 引用）。**三类保存时机**（§4 逐项）：**逐条即时**（训练家类型/道具/物种/元数据——每次确认保存即 `register`＋`save`＋`write_*`）；**退出时确认**（训练家战斗/地区图鉴——编辑只动内存，退出时 "Save changes?" 确认才 `save`（＋反写），否则 `load` 丢弃）；**子编辑返回决定**（嵌套属性编辑的 "Save/Apply changes?" 只决定该子结构是否回写进父编辑的数据数组）。
- **属性列表编辑器（`pbPropertyList`）**：以 `名称=格式化值` 逐行显示属性表；**USE** 调用该属性类型的 `set` 并把**返回值直接赋给该槽**（`set` 的取消语义由各属性类型自定——多数返回旧值即不变，部分返回 nil 即清空）；**ACTION** 对该槽**确认后重置为 `defaultValue`（无 defaultValue 则 nil）**（ReadOnly 除外）；**BACK** 结束编辑——带 `saveprompt` 时给 **"Save changes?" Yes/No/Cancel**：Yes 返回真（调用方执行保存）、No 返回假（不保存）、Cancel 回到编辑；不带 `saveprompt` 时**恒返回 nil**（保存与否由调用方自行决定）。`002:1624–1706`。
- **属性副本与嵌套数据（A-R04 新增）**：编辑的数据数组按内容分三类——**局部标量**（多数数值/文本/布尔/选择槽：改动只在本编辑的本地副本，父层不保存即丢弃）；**共享数组/哈希**（部分属性取值返回**原嵌套对象**——如蛋招池、地图尺寸数组、物种进化路径数组：池编辑的去重/排序**原地**作用于原数组，物种进化取值把原嵌套参数**转成文本**后才进入编辑）；**原地规范化**（打开即发生——**无需父层保存，运行内存也可变化；`.dat` 不因此自动保存**）。三类反例：非空无序蛋招池仅打开后选 No——原数组可已排序；有数字等级进化参数的物种打开属性后 No——原嵌套参数可已转文本；已有地图尺寸改宽后父层 No——运行内存仍可保留宽度。**不把内存变化写成已落盘，也不把所有属性都当成共享**（局部与共享按各属性取值实现分列）。
- **列表器（Lister）与块循环（`pbListScreenBlock`）**：列表器提供命令表/起始下标/取值/预览刷新；块循环中 **USE/ACTION 把选中值交给调用方处理**（编辑/删除），处理后重取命令表；**BACK 退出**。空表时直接返回 `value` 以 −1 为实参的结果。`003:4–112`。
- **ID 派生规则（新建类编辑器）**：名称 → é 转 e → 去掉非字母数字下划线 → 全大写；空 → 类型前缀＋序号（`T_%03d`/`ITEM_%03d`）；首字符非字母 → 加前缀；已存在 → 追加 `_1`…`_100` 去重；仍冲突 → 失败消息。`001:392–420, 869–897`。
- **校验拒绝（不写入；A-R02 修订——可达性分开）**：训练家战斗编辑的校验分两级——**清空类型后属性返回空结果、外层立即结束该次编辑**（**不到错误消息**）；**名字为空与队伍为空**才分别给 "Can't save…" 消息并回到编辑（`001:519–525`）；**改键冲突无唯一性拒绝**（先覆盖目标再删旧键——§4.2）；其它编辑器以属性类型自身范围与选择器约束为主（§3 表）。
- **引用失效的显示（A-R06 修订——分两型）**：**有保护**——Species/Item/Type/Move/Ability/TrainerType/SpeciesForm/GameDataProperty 等 `format` 以存在性判定显示 **"-"**；**严格读取**——**BallProperty、`GameDataPoolProperty` 的池内容格式化、`TrainerPokemonProperty` 格式化、`WeatherEffectProperty` 格式化等直接取记录——**失效 ID 可抛异常**（人工/失效数据前提，不声称正常基线必然出错）；列表器预览图加载失败 rescue 为空白。**只影响显示或如实报错，不做级联清除**（§3.4）。
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
- **StringListProperty**：字符串集合编辑——**[ADD VALUE]**（非空才去重追加；已存在仅移动光标）、**Edit**（改为已存在值时删除本项）、**Delete**；退出时 **"Keep changes?"** 确认才回写（否则原集合不变）。
- **TypesProperty**：双类型槽——逐槽选类型（`pbChooseTypeList`）后 **uniq＋compact**；**有变化且 "Apply changes?" 确认**才生效；默认 [:NORMAL]。

### 3.4 游戏数据引用型（选择器取消＝保留旧值；失效显示 "-"）

- **单引用**：TrainerTypeProperty、SpeciesProperty（`pbChooseSpeciesList`——仅 0 形态）、SpeciesFormProperty（含形态，显示 `名字_形态`）、TypeProperty（排除伪类型）、MoveProperty、MovePropertyForSpecies（**合法招式优先**——物种升级/教授/蛋招并集排序在前，全招式表随后；`001_Utilities:4–14, 181–218`）、AbilityProperty、ItemProperty、BallProperty（球类子集）、GenderProperty（男/女，取消 → nil）、GameDataProperty（任意 GameData 模块列表）。
- **文件引用**：BGMProperty／MEProperty（音频列表器——**浏览时试听**、dispose 恢复原 BGM）、WindowskinProperty／CharacterProperty（图形列表器——**预览缩放显示**）；均取**去扩展名文件名**，取消/空保留旧值。
- **地图坐标**：MapProperty（地图列表）；MapCoordsProperty（选图＋**点选坐标**——取消保留旧值）；MapCoordsFacingProperty（再加**朝向四选**——2/4/6/8）；RegionMapCoordsProperty（区域图列表——0 个提示、1 个直选、多个选择——再点选）；MapSizeProperty（宽 1–30＋0/1 有效格串）。
- **WeatherEffectProperty**：天气列表（当前预选）＋概率 0–100；**取消或选 None → nil**。

### 3.5 复合结构型（A-R05 修订——按子页是否询问分型）

- **无本页询问（BACK 直接返回给父页）**：**IVsProperty、EVsProperty、MapSizeProperty、TrainerPokemonProperty**——属性页关闭时**直接返回**（**没有本页 "Save/No" 选项**）；**IV/EV 初始化还会在传入哈希补数字顺序键**；**EV 超总额要求继续削减**（不能带着超限离开——这不是保存门，返回照样发生）。**父层是否落盘另算**（由父编辑的确认链决定）。
- **有明确保存询问（"Save/Apply/Keep changes?"）**：**BaseStatsProperty、EffortValuesProperty、StringListProperty、TypesProperty、GameDataPoolProperty、LevelUpMovesProperty、EvolutionsProperty**——选 No 时父槽保持旧值。
- **不与嵌套别名（§2 A-R04）混为一个事务**：无询问子页的返回值直接赋父槽；有询问子页选 No 才保证父槽不变——两者都**不直接等同落盘**。
- **BaseStatsProperty**：各项 1–255（缺省 10）；保存确认才回写数组。
- **EffortValuesProperty**：各项 0–255；**只保留 >0 的项**回写 `[stat, value]` 对。
- **IVsProperty(limit)**／**EVsProperty(limit)**：按 PBS 顺序逐项（LimitProperty2）；**EV 总额超限（>EV_LIMIT）时消息要求削减并回到编辑**（`002:665–671`）。
- **GameDataPoolProperty(模块, 允许多个, 自动排序)**：池编辑——**[ADD VALUE]**（`pbChooseFromGameDataList`；不许多个时去重并跳光标）、**Change value**（同上约束）、**Delete**、ACTION+Up/Down 换序；退出 **"Apply changes?"** 确认才回写。子类：**EggMovesProperty**（Move、不许多、自动排序）、**EggGroupsProperty**、**AbilitiesProperty**。
- **LevelUpMovesProperty**：等级＋招式对——**按等级排序**（同级才可换序）；添加（等级 0–最大、取消 −1；同等级同招式去重）；改等级/改招式（目标已存在时**删除本项**）；删除；退出 **"Save changes?"** 确认才回写。
- **EvolutionsProperty**：进化路径（物种＋方法＋参数）——添加（物种选择→方法列表→**参数编辑器**：按方法的参数类型分派——Item/Move/Species/Type/Ability 选择器；**String 类注册**（如 LocationFlag——编辑器的字符串实例匹配不命中类对象，**实际走 0–65,535 数值输入**：默认值数值转换为 0、取消 −1 → nil——**当前基线不能输入任意地区标志文字**；不把意图当已实现、不修参考，A-R07）；**枚举符号**（param_type 为符号常量的方法——对应选择器）；Integer 0–65,535（取消 −1 → nil）；无参数方法跳过）；编辑（改物种/改方法——**改方法后参数重置为 0**/改参数/删除）；**所有改动去重**（已存在相同路径时删除本项并跳光标）；退出 **"Save changes?"** 确认才回写；参数显示（无参数方法省略；未知符号常量显示常量名；空显示 "???"）。
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

### 4.3 道具（`pbItemEditor`＋`pbItemEditorNew`；`001:822–921`）

- **列表**：ItemLister（含 [NEW ITEM]；图标预览）。
- **USE（已有项）**：editor_properties → `pbPropertyList`（saveprompt）→ **确认保存**：schema 组哈希＋保留 suffix → **register＋save＋`Compiler.write_items`**（即时生效，无退出确认）。
- **ACTION（已有项）**：严肃确认 → 删除＋**立即 save＋write_items**＋消息。
- **新建（A-R03 修订）**：名称 → ID 派生（`ITEM_` 前缀系）→ **口袋选择**（PocketProperty，返回 0＝放弃）→ **价格**（0–999,999——**BACK 返回 0 而非 −1**（默认值经钳制、无独立取消值）——**按 BACK 仍继续后续创建（价格 0）**；正常输入 0 同为价格 0——**口袋取消与价格 BACK 是两个不同的分支**）→ 描述（StringProperty）→ register＋save＋write_items＋创建与图形提示消息；复数名自动为 `名称+s`。

### 4.4 物种（`pbPokemonEditor`；`001:926–987`）

- **列表**：SpeciesLister（**不含新建项**——`includeNew` 为假）。
- **USE（已有项）**：editor_properties 取值——**身高/体重以 ×10 整数显示**；`pbPropertyList`（saveprompt）→ **确认保存**：身高/体重除 10 回写、schema 组哈希、保留 suffix → **`Compiler.validate_compiled_pokemon` 净化**（WP04 引用）＋**进化参数按方法类型重铸**（无参数 → nil；Integer → 无符号整型 cast；非 String → 枚举 cast）→ register＋save＋`Compiler.write_pokemon`＋"Data saved."消息。
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
| 有询问子结构（升级招式/进化/池/字符串列表/类型对/基础能力/努力产出） | 子编辑返回数组 | 随父编辑的保存确认回写进父数据 | 子编辑 "Save/Apply/Keep changes?" 选 No → 父槽位保持旧值 |
| 无询问子结构（IV/EV/地图尺寸/训练家个体，A-R05） | **BACK 直接返回赋父槽** | 父层确认链决定 | **无本页 No 选项**（EV 超总额要求继续削减——不是保存门）；父层不保存则该次改动不保留（共享嵌套对象例外见 §2 A-R04） |

- **取消仍写入的情形（如实登记，A-R04）**：`pbPropertyList` 的 **ACTION 重置**与 **USE 赋值**在进入 "Save changes?" 之前就已写入**本地属性数组**——多数槽位只影响内存副本；**但共享嵌套对象（蛋招池/地图尺寸/进化路径）的原地操作不等待父层确认即可改变运行内存**（§2——**不写 `.dat` 但内存可变**）；真正落盘都经上表确认链或 §4 逐项即时链。**没有"取消却仍落盘"的路径**（新建流程中嵌套类型创建的 PBS 反写是确认流程外的落盘——§4.2 已具名）。
- **生效（运行时可见）**：`.dat` 保存后运行时读取方立即用新数据（运行期 `DATA` 已同步）；PBS 反写保持文本与 `.dat` 一致（WP04 生命周期）；地区图鉴另清 `$game_temp` 缓存强制下次重载。

## 7. 同文件边界归属（只登记，不展开）

- **WP73-B（同 `001_EditorScreens.rb`）**：`pbEncountersEditor`（遭遇集/类型/槽三层编辑＋退出 "Save changes?" 确认——save＋write_encounters，否则 load 丢弃）、`pbMapMetadataScreen`/`pbEditMapMetadata`（地图元数据——save＋write_map_metadata 即时）。
- **WP74（同 `001_EditorScreens.rb`）**：`pbAnimationsOrganiser`（动画表 Z 序换序/插删＋"Save changes?"——写 `Data/PkmnAnimations.rxdata`＋清缓存）。
- **WP04/WP75**：`Compiler.write_*` 反写与 `validate_compiled_pokemon`/`cast_csv_value` 净化/重铸为引用点；编译全集与转换归 WP75。

## 8. 默认行为与配置变体

- **配置值（WP02 引用）**：`MAX_PARTY_SIZE`（训练家队伍槽数）、`Settings.bag_pocket_names`（口袋选择表）、`GrowthRate.max_level`（等级上限）、`Pokemon::IV_STAT_LIMIT/EV_STAT_LIMIT/EV_LIMIT`（个体值/努力值上限）、`MAX_MONEY` 等按各属性范围生效。
- **新建 ID 派生**：§2 规则；**新建物种不支持**；新建训练家给**示例队伍**（`pbNewTrainer` 合同引用——WP24/WP39）。
- **未验证组合**：编辑器实际运行表现、预览/试听素材存在性（WP15/U01）、编译反写的完整诊断（WP04）、PBS 与 `.dat` 不一致时的实际消费方行为。

## 9. 边界、失败与未知

- **校验拒绝**：训练家战斗三项 "Can't save…"（未选类型/名字空/队伍空）；新建 ID 冲突失败；新建训练家版本满（0–255 用尽）"没有空间"；训练家类型/道具新建的名称为空放弃（有缺省名时回落缺省）；新建道具口袋返回 0/价格取消 −1 放弃；EvolutionsProperty 参数类型缺失时按 nil 处理；EV 总额超限循环。**拒绝时不写文件**。
- **删除**：训练家类型/道具/物种的 ACTION 删除**立即落盘**（严肃确认后）；训练家战斗删除**待退出确认**；地区图鉴删除**无确认**（主界面即时）。
- **引用失效**：format 显示 "-"；列表器预览 rescue 空白；**不做级联清除或自动修复**（失效引用保留在数据里，运行时语义归各数据主责包）。
- **异常路径**：图形/音频缺失仅显示层回落；`pbPropertyList` 对未知属性对象按自身 set 行为（UndefinedProperty/ReadOnlyProperty 消息）；**不虚构事务回滚或部分写入保证**——逐条即时类编辑器在一次 register＋save＋write 内不拆原子性承诺。
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
| M02 取消语义分型（人工夹具） | a) LimitProperty2 数值取消；b) SpeciesProperty 选择取消；c) BooleanProperty2 取消；d) WeatherEffectProperty 选 None | a) 返回 nil（槽清空）；b) 返回旧值（不变）；c) 返回 nil；d) 返回 nil |
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
| M15 GameDataPoolProperty（A-R04/R05；人工夹具） | a) 不许多个时添加重复值；b) 改值为已存在值；c) 退出选 No；d) 非空无序蛋招池仅打开后选 No | a) 不追加、光标跳到既有项；b) **删除本项**并跳光标；c) 父槽位保持旧值（有询问子页不回写）；d) **原数组可已排序**（池编辑打开即对原嵌套数组原地去重/排序——不写 `.dat` 但运行内存可变；无本页 No 能阻止） |
| M16 LevelUpMovesProperty（人工夹具） | a) 添加同级同招；b) 改等级撞到已有同级同招；c) 同级换序；d) 退出 Yes | a) 不新增、光标跳已有；b) **删除本项**、光标跳已有；c) 仅同级可换；d) 去辅助列后回写（等级排序） |
| M17 EvolutionsProperty（A-R07；人工夹具） | a) 改方法；b) 无参数方法改参数；c) LocationFlag（String 类注册）改参数；d) 所有改动去重 | a) 方法换且**参数重置为 0**；b) "不使用参数"消息；c) **实际出现数值框（0–65,535、默认 0）——不能输入任意地区标志文字**（数值/枚举参数对照：枚举符号走选择器、Integer 走数值框、取消 −1 → nil）；d) 相同（物种,方法,参数）已存在时删除本项跳光标 |
| M18 列表器行为（人工夹具） | a) 空目录 GraphicsLister；b) MusicFileLister 浏览后退出；c) MapLister 选 [GLOBAL]；d) 块循环删除最后一项 | a) "There are no files."消息；b) **dispose 恢复原 BGM**（浏览试听不残留）；c) 返回 0；d) **下标保持为新命令数（不是钳到最后有效项）**——可见选中可能失效（静态边界，不推断像素表现） |
| M19 选择器（人工夹具） | a) pbChooseSpeciesList；b) pbChooseTypeList；c) pbChooseMoveListForSpecies；d) pbChooseBallList 取消 | a) **只列 0 形态**；b) **排除伪类型**；c) 合法招式（升级+教授+蛋招）排序在前、全表随后；d) 返回旧值 |
| M20 生效时机总核（A-R01/R05/R08；静态核对） | 六编辑器各执行一次确认保存与一次取消；另核新建嵌套与无询问子页 | 与 §6 表逐行一致：逐条即时类（类型/道具/物种/元数据）确认即三层同步；退出确认类（训练家战斗/图鉴）取消即 load/弃克隆——**嵌套例外：新建流程创建类型的 PBS 反写已落盘保留**；**无询问子页 BACK 直接赋父槽**（EV 超限要求削减不是保存门）；**空表保存分支非终止**；**无"取消仍落盘"路径**（嵌套反写已具名） |

## 11. 证据与来源（traceability）

- **本轮复核（2026-10-02，首版）**：四份编辑器主域文件**分段全文阅读**（`001_EditorScreens.rb` 1–1,324；`002_Editor_DataTypes.rb` 1–1,706；`003_Editor_Listers.rb` 1–647；`001_Editor_Utilities.rb` 1–410，共 4,087 行）。
- **定点阅读**：`010_Data/001_GameData.rb:55–75, 130–150, 195–215, 240–250`；`010_Data/002_PBS data/001_MiscPBSData.rb:28–40`；`015_Trainers and player/002_Trainer_LoadAndNew.rb:12–110`；`010_Data/002_PBS data/015_Trainer.rb:1–15`。
- **继承同基线既有记录**：WP04（PBS 编译/反写/校验——`Compiler.write_*`、`validate_compiled_pokemon`、`cast_csv_value` 引用）；WP03（GameData schema/注册）；WP18/WP19/WP21（个体/属性/形态）；WP24（玩家/训练家——`pbNewTrainer`/训练家数据语义）；WP27（背包/口袋）；WP31/WP34（招式/育种数据）；WP36（遭遇数据语义——WP73-B 主责其编辑器）；WP72（调试入口与工具归属，当前字节 `49731474`）；WP61（`d84dff78`）、WP53（`75fc4db7`）、WP37（`d032f5b7`）、WP65、WP67-A/B、GR-001～016、WP23-N01（各自具名通过范围）。
- 全部静态证据；**无运行确认**（未运行编辑器/游戏/UI、未执行编译器或反序列化、未写 PBS/.dat/地图文件、未播放音频、未操作真实存档、未访问网络）。

## 12. 未决问题

1. 编辑器实际运行表现与宿主窗口/素材行为（预览图、试听、小地图——WP15/U01）。
2. PBS 反写与外部手工编辑并发时的一致性（WP04/WP75 边界）；`Compiler.write_*` 的诊断输出细节（WP04）。
3. demo 中各编辑器入口的默认可达性与真实使用编排（WP77/U01）。
4. `pbNewTrainer` 示例队伍生成规则的完整合同（WP24/WP39 主责——本包只引用调用点）。

## 13. 状态与后续

- 2026-10-02 **统一首审修订 v2**（统一 review 34 项中 WP73-A 的 11 项＋共通 3 项）：**R01** 新建流程嵌套保存分层——创建类型立即落盘并反写两份 PBS（可带出先前内存编辑）；外层 No 只重载 `.dat` 不回滚 PBS；交互建队首只必选、后续逐个确认。**R02** 校验可达性——清空类型立即结束该次编辑（不到消息）；名字空/队伍空才回校验循环；改键冲突先覆盖目标再删旧键（无唯一性拒绝）。**R03** 新道具价格 BACK 返回 0 而非 −1（继续创建价格 0；口袋取消才是放弃）。**R04** 属性副本三类——局部标量/共享嵌套对象（蛋招池/地图尺寸/进化路径原地操作）/原地规范化（不写 `.dat` 但内存可变）。**R05** 子页分型——无本页询问（IV/EV/地图尺寸/训练家个体 BACK 直接赋父槽）与有询问子页分开；EV 超限要求削减不是保存门。**R06** 失效引用分两型——有保护显示 "-" 与严格读取可抛异常（球/池内容/训练家个体/天气格式化）。**R07** String 类注册的进化参数（LocationFlag）实际走数值框（0–65,535、默认 0）——不能输入任意文字。**R08** 图鉴子编辑进入先去空、退出全量去空（子 No 也压空洞）；空表保存分支非终止（静态推导未运行）。**R09** 删除尾项后下标保持为新命令数（不是钳到最后有效项——可见选中可能失效）。**R10** 动画分配无空槽时调整为目标长度 10 并返回调整前长度（超长截断不恢复）。**R11** ID 向量更正为 CAFEOWNER。**BATCH-R01** 正文哈希构造式改独立散文。**BATCH-R02** 数量按最终文件重算。**BATCH-R03** 同批 WP72/WP73-B 引用改为同批待审记法。场景 M01–M20 保留（v2 修订 8 行：M05、M06、M08、M14、M15、M17、M18、M20）；v1 被审身份 `4c3e591c` 留史；v1 材料不改写。
- WP73-A 自身范围（第 1 节四项）已提取并自检，2026-10-02 首版登记 **ReviewPending（具名静态范围，待统一 review）**；不自行标 Reviewed、不宣称通过。依据用户批次授权（WP72＋WP73-A＋WP73-B）与 `planning/extraction-plan.md` 的 WP73-A 任务定义执行；四份编辑器主域文件分段全文阅读、持久层与训练家辅助定点核对并建立覆盖映射（见交付目录附表）。
- **已通过边界原样继承**：WP04、WP61（`d84dff78`）、WP53（`75fc4db7`）、WP37（`d032f5b7`）、WP65、WP67-A/B、GR-001～016、WP23-N01——本包只引用其合同，不重开、不修改 reference；**同批待审依赖（不作通过结论）**：WP72（`49731474`）、WP73-B。
- **WP73-A 完成 ≠ F18-02 完成**：世界编辑器归 WP73-B；编辑器运行验证、素材、demo 编排保留；Feature Matrix 按聚合规则分别显示，不将整个 D18 标完成。
- 后续包引用本文的编辑器合同（三层持久、保存时机表、属性类型目录、校验拒绝）时，不得把参考侧类/方法组织当作未来框架的 API；发现与本文冲突的新证据时，先修订本文并通知受影响包。批次内后续（WP73-B）与整体 double review（WP78/79）、WP80 净化交付按 extraction-plan 执行，本包完成不自动推进。
