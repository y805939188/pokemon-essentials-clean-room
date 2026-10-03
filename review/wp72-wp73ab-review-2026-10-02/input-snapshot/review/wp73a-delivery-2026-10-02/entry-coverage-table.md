# WP73-A 数据／状态／覆盖附表（编辑器／属性类型 → 输入与取消 → 校验 → 写入层与时机 → 反馈 → 失败／未达点 → 来源 → 主责包）

2026-10-02；WP73-A 首版附件。每行一个已核对编辑器/属性类型组；「主责包」指该行为规则的主责规格（本包=WP73-A 主稿章节，其余为引用）。来源定位见主稿 §10.1/§11（`001:`＝`001_EditorScreens.rb`、`002:`＝`002_Editor_DataTypes.rb`、`003:`＝`003_Editor_Listers.rb`、`U:`＝`001_Editor_Utilities.rb`）。本表是取证覆盖记录，不是功能数量或完成证明；分组数据行数按机械实测登记（见 checks.json）。

## 1. 属性框架与数值/文本/布尔/枚举类型

| 能力 | 输入与取消 | 校验 | 写入层与时机 | 反馈 | 失败／未达点 | 主责包 |
| --- | --- | --- | --- | --- | --- | --- |
| pbPropertyList 框架 | USE 调属性 set 赋回该槽；ACTION 确认重置 defaultValue/nil；BACK 结束 | — | saveprompt：Yes 真／No 假／Cancel 回编辑；无 saveprompt 恒 nil | 行显示 名称=format；描述窗随选中 | ReadOnly 豁免 ACTION 重置 | WP73-A §3.1；002:1624–1706 |
| Undefined/ReadOnly | 无（消息） | — | 返回旧值（不写） | "此处不能编辑"/"不可编辑" | — | WP73-A §3.2；002:4–27 |
| UInt/Limit/Limit2/NonzeroLimit | 数值框（限位/0–max/0–max 取消 −1→nil/1–max） | 范围框 | 赋入槽位（随父保存链） | 默认 0/0/nil/1 | Limit2 取消即清空 | WP73-A §3.2；002:32–128 |
| Boolean/Boolean2 | 确认／True-False 选择（取消 nil） | — | 同上 | True/False/"-" | — | WP73-A §3.3；002:133–160 |
| String/LimitString/ItemName | 自由文本（250/limit/30） | 长度框 | 同上 | 原文显示 | — | WP73-A §3.3；002:165–192,906–919 |
| Enum（EnumProperty） | 枚举列表（取消留旧） | — | 同上 | 值名显示；EnumProperty2 基线 Unused | — | WP73-A §3.3；002:197–246 |
| StringListProperty | ADD（去重）/Edit（撞名删本项）/Delete；退出 Keep changes? | 非空 | 确认才回写父槽 | 列表显示 | 取消→父槽不变 | WP73-A §3.3；002:251–337 |
| TypesProperty | 双槽选类型＋uniq/compact；Apply changes? | — | 确认才生效 | 类型名逗号串 | 取消→旧值 | WP73-A §3.3；002:496–523 |

## 2. 引用/文件/坐标/复合结构类型

| 能力 | 输入与取消 | 校验 | 写入层与时机 | 反馈 | 失败／未达点 | 主责包 |
| --- | --- | --- | --- | --- | --- | --- |
| 单引用型（TrainerType/Species/SpeciesForm/Type/Move/MoveForSpecies/Ability/Item/Ball/Gender/GameData） | 各选择器（取消留旧） | 失效显示 "-" | 赋入槽位 | real_name 显示 | Species 只 0 形态；Type 排除伪类型；MoveForSpecies 合法招式在前 | WP73-A §3.4；002:342–584,695–711,1022–1035；U:116–242 |
| 文件引用型（BGM/ME/Windowskin/Character） | 文件列表器（取消/空留旧） | — | 赋入槽位（去扩展名） | 试听/预览；dispose 恢复 | "无文件"消息 | WP73-A §3.4；002:374–411,716–725；003:117–244 |
| 地图坐标型（Map/MapCoords/MapCoordsFacing/RegionMapCoords/MapSize/WeatherEffect） | 地图列表＋点选（＋朝向）＋概率；取消留旧 | Region 0 个提示 | 赋入槽位 | 小地图/坐标显示 | WeatherEffect 选 None/取消 → nil | WP73-A §3.4；002:730–901；U:64–111 |
| BaseStats/EffortValues | 各项 1–255（缺省 10）／0–255（只留 >0） | — | 保存确认才回写 | 逗号串 | — | WP73-A §3.5；002:944–1017 |
| IVs/EVs | 逐项 LimitProperty2 | **EV 总额超 EV_LIMIT → 消息＋回编辑** | 随父保存链 | 按 PBS 序逗号串 | 超限不能离开 | WP73-A §3.5；002:607–690 |
| GameDataPoolProperty（含 EggMoves/EggGroups/Abilities 子类） | ADD（不许多去重）/Change（撞名删本项）/Delete/换序；退出 Apply changes? | 模块存在性（构造时 raise） | 确认才回写 | 名字池列表 | 取消→父槽不变 | WP73-A §3.5；002:1040–1182 |
| LevelUpMovesProperty | 添加（等级 0–max＋招式；同级同招去重）/改等级/改招式（撞则删本项）/删除；同级换序；退出 Save changes? | — | 确认才回写 | "等级: 招式"列表 | 取消→父槽不变 | WP73-A §3.5；002:1187–1335 |
| EvolutionsProperty | 添加（物种→方法→参数按型分派）/改物种/改方法（参数重置 0）/改参数/删除；全程去重；退出 Save changes? | 无参数方法跳过参数 | 确认才回写 | 参数显示（空 "???"） | String 参数空白→nil | WP73-A §3.5；002:1340–1570 |
| EncounterSlotProperty（WP73-B 复用） | 概率 1–999＋物种形态＋等级区间；新建缺省 [20,首种,5,5] | 最低>最高交换 | 随父保存链 | "概率, 名字_形态 (Lv.a-b)" | — | WP73-A §3.5；002:1575–1619；WP73-B |

## 3. 六个内容编辑器

| 编辑器 | 输入与取消 | 校验 | 写入层与时机 | 反馈 | 失败／未达点 | 主责包 |
| --- | --- | --- | --- | --- | --- | --- |
| 训练家类型（编辑） | editor_properties→pbPropertyList | — | **确认即** register＋save＋pbConvertTrainerData | "Data saved"层（消息表刷新＋两 PBS 反写） | No→不写 | WP73-A §4.1；001:345–390 |
| 训练家类型（删除/新建） | ACTION 严肃确认／名称→ID 派生→性别→基础金钱(0–255,默认30) | ID 冲突去重/失败 | 删除：**立即** save＋convert；新建：register＋save＋convert | 删除/创建消息＋图形提示 | 名称为空放弃；ID 失败消息 | WP73-A §4.1；001:351–356,392–443 |
| 训练家战斗（编辑） | TrainerBattleProperty（类型/名字/版本 0–9999/台词/队伍槽×MAX/道具槽×8） | **未选类型/名字空/队伍空三拒绝回编辑** | 内存 DATA＋modified；**退出确认才** save＋convert | — | 键改变删旧键 | WP73-A §4.2；001:448–544 |
| 训练家战斗（新建/删除/退出） | 类型（现有/新建/取消）→名字→空版本(0–255) | 版本满→"没有空间" | 新建：pbNewTrainer 示例队伍 register＋modified；删除：严肃确认＋modified；**退出 No → load 丢弃全部** | "已添加"/删除消息 | 取消链各处放弃 | WP73-A §4.2；001:545–599；015/002:12–110 |
| TrainerPokemonProperty（单槽） | 物种/等级(1–max)/昵称/形态(0–999)/性别/闪光×2/Shadow/招式×4/特性(位)/道具/性格/IV/EV/友好/球 | **物种 nil → 整槽 nil**；EV 总额超限循环 | 招式去重去空后返回 | — | 四招式全空＝野生招式表 | WP73-A §4.2；001:604–687 |
| 道具（编辑/删除/新建） | editor_properties→pbPropertyList／ACTION 严肃确认／名称→ID→口袋→价格(0–999999,−1 放弃)→描述 | — | **确认即** register＋save＋write_items（删除同） | 创建/删除消息＋图形提示 | 口袋 0/价格 −1 放弃 | WP73-A §4.3；001:822–921 |
| 物种（编辑/删除） | editor_properties（身高体重 ×10 显示）→pbPropertyList | **validate_compiled_pokemon 净化＋进化参数按方法类型重铸** | **确认即** register＋save＋write_pokemon＋"Data saved." | 保存消息 | **新建不支持**（消息） | WP73-A §4.4；001:926–987；WP04 |
| 全局/玩家元数据 | MetadataLister（GLOBAL/Player N/ADD NEW）→pbPropertyList | 角色不存在→消息返回 | **确认即** register＋save＋write_metadata | — | 新建取最小未用 ID | WP73-A §4.5；001:692–774 |
| 地区图鉴（主界面） | ADD（空白/全国/按族填充）；已有：Edit/Copy/Delete（无确认）；Z 序换序 | — | 克隆数组；**退出确认才** save_data(dat)＋清缓存＋write_regional_dexes＋"Data saved." | 列表（尺寸显示） | 退出 No→克隆弃 | WP73-A §4.6；001:1099–1202 |
| 地区图鉴（子编辑） | Z+Up/Down/Right/Left/D；点选：Change species（**同物种他位自动清**）/Clear/Insert/Delete；退出 Save changes? | 唯一性（自动去重） | 确认才回写主界面该图鉴（压尾 nil） | "----------"空位显示 | 取消→不回写 | WP73-A §4.6；001:992–1097 |

## 4. 共享基础设施与边界

| 能力 | 输入与取消 | 校验 | 写入层与时机 | 反馈 | 失败／未达点 | 主责包 |
| --- | --- | --- | --- | --- | --- | --- |
| 通用窗口（pbListWindow/pbListScreen/pbListScreenBlock/pbCommands2/pbCommands3/pbChooseList） | USE/BACK/ACTION 组（换序/插删/SPECIAL） | — | 无 | 小字体命令窗；空表直接返回 value(−1) | 删除后下标钳表尾 | WP73-A §5；003:4–112；U:247–410 |
| 列表器组（Graphics/Music/Metadata/Map/Species/Item/TrainerType/TrainerBattle） | 浏览＋选择 | — | 无 | 预览图/试听/小地图/队伍摘要 | 空目录消息；图像 rescue 空白 | WP73-A §5；003:117–647 |
| 选择器组（GameData/物种(0形态)/形态/类型(排伪)/道具/特性/招式/物种招式/球） | 列表选择（取消留旧/nil） | 模块存在 raise | 无 | 字母/ID 双序（ACTION 换序） | — | WP73-A §5；U:116–242 |
| 工具函数（pbGetLegalMoves/pbSafeCopyFile/pbAllocateAnimation/pbMapTree） | — | — | pbSafeCopyFile 相同跳过/不同确认覆盖 | — | — | WP73-A §5；U:4–111；WP74 |
| GameData 持久层 | — | — | save→`Data/X.dat`；load→整体重载丢弃内存 | — | — | WP73-A §2；001_GameData:63–69,138–144,203–209 |
| WP73-B 边界（遭遇编辑器/地图元数据编辑器） | — | — | 遭遇：退出确认 save＋write_encounters 否则 load；地图元数据：确认即 save＋write_map_metadata | — | 归属 WP73-B | WP73-A §7；001:6–340,779–817；WP73-B |
| WP74 边界（动画组织器） | Z 序换序/插删；Save changes? | — | 写 PkmnAnimations.rxdata＋清缓存 | "Data saved." | 归属 WP74 | WP73-A §7；001:1252–1324；WP74 |
| WP04/WP75 边界（Compiler.write_*/validate/cast） | — | — | PBS 反写与净化/重铸为引用点 | 诊断 WP04 | 编译全集 WP75 | WP73-A §7；WP04/WP75 |
