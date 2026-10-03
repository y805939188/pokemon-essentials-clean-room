# 来源追溯索引（WP80；2026-10-03 起）

用途：为 `deliverables/final-specification-set/` 的净化正文提供**独立追溯**——从最终条目反查批准的输入规格及身份、独立审查依据、参考文件及已读范围、证据层级与对应场景/向量。**本索引是审计材料**：净化正文可独立阅读，不依赖本索引；审计定位（源方法名、源文件路径、行号）集中保存在此处，正是净化正文不含它们的原因。

## 字段口径

| 字段 | 含义 |
| --- | --- |
| 最终条目 | 净化交付位置（文件 § 章节） |
| 分类/归属 | 项目分类与内容包 ID（84 个既有包 ID；附表归入父包） |
| 批准输入 | 批准的输入规格（路径）及其**被审身份**（复审批准对象的完整 SHA-256/字节——以闭合/通过报告固定版本表为准）与**当前管理性回填身份**（以 manifest §1 当前行为准；两者分列，历史链见 manifest §3） |
| 审查依据 | 独立复审结论（报告路径；含关闭项编号） |
| 参考与已读 | 参考快照内被实际阅读的文件与范围（全文/定点；固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`） |
| 证据层级 | 静态证据档位（已定位/静态确认/数据样本确认）；全部无运行确认 |
| 场景/向量 | 对应静态场景 ID（测试目录条目） |
| 具名未验证 | 该条目保留的具名未验证子范围 |

## 批次 1：engine-overworld / WP16

### T-WP16-01 《世界绘制与视觉过渡》

| 字段 | 内容 |
| --- | --- |
| 最终条目 | `deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md` §1–§11 |
| 分类/归属 | Engine/Overworld Integration；WP16（F05-03、F05-04） |
| 批准输入 | `specs/overworld/wp16-world-rendering-and-visual-transitions.md`——**被审身份（v3）`ccb7bb9ac4039d186cedcea4c5f0e35c03afdd562bc8e221a22f6f05cdd33563`／21,104**（闭合复审固定版本表）；**当前管理性回填身份 `d7aad4aa649cf7e07cebdda593b7f8b454a712f9fb05ae673cc8cc0a4dca347a`／21,399**（Reviewed 状态回填，行为正文与被审对象一致；当前身份见 manifest §1 当前行，被审身份见闭合复审报告与 manifest §3 历史） |
| 审查依据 | **2026-09-23 WP14–WP16 v3 闭合复审 PASS_SCOPED——WP16-R01 本次关闭、WP16-R02 继承关闭（`review/wp14-wp16-closure-review-2026-09-23/report.md`）**；此前 `review/wp14-wp16-recheck-2026-09-23/` 结论为 REQUEST_CHANGES（WP16-R01 有剩余），仅作历史过程、不作通过依据；WP79 覆盖审查继承（`review/wp79-stage-review-2026-10-03/recheck-v6/report.md`） |
| 参考与已读 | 全文：`006_Map renderer/001_TilemapRenderer.rb`（620）、`005_Sprites/003_Sprite_Character.rb`（187）、`004_Sprite_Reflection.rb`（89）、`006_Spriteset_Global.rb`（56）、`007_Spriteset_Map.rb`（131）；定点：`012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb`（结构/常量/fade_in 段及 :16–17, :66–95, :425–428, :460–477）、`010_Data/001_Hardcoded data/012_Weather.rb`（注册目录）、`004_Game classes/001_Game_Screen.rb:13–69` 及更新段（含 :65–70）、`012_Overworld/003_Overworld_Time.rb:100–126`、`005_Sprites/009_Sprite_DynamicShadows.rb:1–40`；**v3 有界澄清定点（WP80-B01-R01/R02）**：`006_Map renderer/001_TilemapRenderer.rb:459–462, 511–512, 571–576`（显示偏移换算后先取整到整数像素、格内余数取自整数像素坐标——620 行全文已读范围内的定点复核）、`004_Game classes/004_Game_Map.rb:32–37`（每格 32 像素、每像素 4 子像素单位）、`003_Game processing/002_Scene_Map.rb:18–26, 37–53, 72–101`（逐图显示处置与全局持有者保持：已存在则不重建）、`005_Sprites/006_Spriteset_Global.rb:7–29, 32–54`（图片显示关联独立图片记录、计时器按独立计时状态）、`005_Sprites/001_Sprite_Picture.rb:1–36`、`002_Sprite_Timer.rb:1–42`（显示内容跟随记录，处置显示不等于删除记录）；引用不重读：WP11/WP12/WP13/WP15/WP06 |
| 证据层级 | 已定位/静态确认；无运行确认 |
| 场景/向量 | 测试目录 WR01–WR17（`test-catalog/engine-overworld-wp16.md`） |
| 具名未验证 | 一切实际视觉结果/动画时序/宿主输出；动态阴影全部创建者；地图元数据天气字段消费者链；战斗内画面 |

### T-WP16-02 《战前过渡》

| 字段 | 内容 |
| --- | --- |
| 最终条目 | `deliverables/final-specification-set/engine-overworld/wp16-pre-battle-transitions.md` §1–§10 |
| 分类/归属 | Engine/Overworld Integration（主）、Combat Requirements（交界）；WP16 附（F05-04-supp-BT） |
| 批准输入 | `specs/overworld/wp16-pre-battle-transitions-appendix.md`——**被审身份（v2）`2d499cf4fdfc30a1d4832c1b411e925b563836a6a76cb66f42443807e7a790be`／23,334**（WP79 v6 复审批准对象，见通过报告 §1）；**当前管理性回填身份 `aabb25096a5f36bbe73a1148d61f929bea98838fe553ebf593db0243c15b8dee`／23,630**（状态回填，行为正文与被审对象一致；当前身份见 manifest §1 当前行，被审身份见通过报告与 manifest §3 历史） |
| 审查依据 | 2026-10-03 WP79 v6 独立复审 PASS_SCOPED（R02 关闭；`review/wp79-stage-review-2026-10-03/recheck-v6/report.md`） |
| 参考与已读 | 全文：`012_Overworld/002_Battle triggering/002_Overworld_BattleIntroAnim.rb`（432——注册表 :17–42、让位助手 :51–57、包装 :59–152、核心演出 :154–188、五组注册 :198–432，资源规则 :277–298 定点复核）；定点：`009_Scenes/001_Transitions.rb:1–175`（入口/单位/特殊判定/基类）与十四个固定时长声明行（:459, :527, :596, :675, :754, :845, :943, :1010, :1092, :1168, :1244–1245, :1437–1438, :1677–1678, :1768–1769）、:1244–1345（VSTrainer 资源/时间线）、:1437–1460、:1677–1690、:1768–1786（三效果资源段）、:440–454（淡黑/淡白无固定时长）、`_interrupt_transition` 全库检索（仅 :31/:45 两处读取）；`012_Overworld/001_Overworld.rb:527–536`（等待秒单位）；`001_Technical/002_Files/001_FileTests.rb:119–133`（路径解析）；调用侧 `012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb:401–402, 521–522`、`018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb:65–66, 125–126`、`002_BugContest.rb:382`、`001_SafariZone.rb:132–133`；引用不重读：WP15/WP36 §4.5/WP42 §7/WP60/WP63/WP67-A §3.2 |
| 证据层级 | 已定位/静态确认；无运行确认 |
| 场景/向量 | 测试目录 BT01–BT16（`test-catalog/engine-overworld-wp16.md`） |
| 具名未验证 | 素材存在性（Graphics/ 缺失）与实际帧呈现/墙钟耗时；注册表运行期改动与扩展注册；具名效果逐帧呈现细节（像素级具名排除） |

## 批次 2：generic-kernel / WP02＋WP03＋WP04

### T-WP02-01 《规则配置档案与数据变体》

| 字段 | 内容 |
| --- | --- |
| 最终条目 | `deliverables/final-specification-set/generic-kernel/wp02-rule-configuration-and-data-variants.md` §1–§11 |
| 分类/归属 | Generic Kernel（主；部分跨 Pokémon Rules/宿主/UI/作者配置）；WP02（F01-01、F02-03） |
| 批准输入 | `specs/kernel/wp02-rule-configuration-and-data-variants.md`（修订稿 v4；当前身份 `82b471510ff563e6964697cb28e77ae816e190062dfafc9e328f44a81c2131fa`／37,817——闭合复审后当前有效版本，被审与当前同版；早期身份链见 manifest §3） |
| 审查依据 | 2026-09-19 WP02 闭合复审通过（`review/wp02-closure-review-2026-09-19.md`；固定基线配置档案、声明默认/派生、候选材料与输入边界、静态场景范围）；WP79 覆盖审查继承（recheck-v6） |
| 参考与已读 | 全文：两个设置文件（`001_Settings.rb` 524 行、`002_BattleSettings.rb` 140 行）；定点：`021_Compiler/001_Compiler.rb:967–1018`（普通发现函数与 22 项调用）、`002_Compiler_CompilePBS.rb`（compile_trainer_lists）、`PBS/battle_facility_lists.txt`（全文）；LANGUAGES 与 game_credits 使用点行级核实；逐定义清单独立复算（附表全部统计）；全仓库 Settings 定义点搜索 |
| 证据层级 | 已定位/静态确认/数据样本确认；无运行确认 |
| 场景/向量 | 测试目录 KC01–KC05（`test-catalog/generic-kernel-wp02-03-04.md`） |
| 具名未验证 | U02/U03/U06/U09；非法取值后果；专用读取路径全集；各开关领域语义全集 |

### T-WP02-02 WP02 设置附表（逐定义清单与检索索引）

| 字段 | 内容 |
| --- | --- |
| 最终条目 | 净化 §3/§4 词典与 §6 的数值与键名（词典内容承接）；逐定义行号、复算口径、检索索引与使用点路径保留于本索引 |
| 分类/归属 | Generic Kernel（配置取证附表）；WP02 附 |
| 批准输入 | `specs/kernel/wp02-settings-inventory-appendix.md`（当前身份 `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e`／16,555） |
| 审查依据 | 随 WP02 闭合复审（WP02-R01 验收：词典与逐定义清单双向对应）；WP79 覆盖审查继承 |
| 参考与已读 | 附表全文（§1–§8：统计单位、独立复算、88＋30 逐定义行、3 方法型、3 元信息、检索规则、世代引用 41/139/0、LANGUAGES 分类、16 开关行级分类、名单 10 路径与 2 未引用） |
| 证据层级 | 已定位/静态确认（复算证据） |
| 场景/向量 | 随 T-WP02-01（KC01–KC05） |
| 具名未验证 | 同 T-WP02-01；生成程序（analysis/inventory/ 下只读解析脚本）为工具侧产物，不属行为范围 |

### T-WP03-01 《内容身份、注册与 schema》

| 字段 | 内容 |
| --- | --- |
| 最终条目 | `deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md` §1–§12 |
| 分类/归属 | Generic Kernel（身份/注册/schema 机制）；WP03（F01-02、F02-01） |
| 批准输入 | `specs/kernel/wp03-content-identity-and-schema.md`（修订稿 v5；当前身份 `de331460e013bfc07533d0f368967fe729bcf0720d98e7d990a16a0614e9c27d`／30,708——闭合复审后当前有效版本；早期身份链见 manifest §3） |
| 审查依据 | 2026-09-19 WP03 闭合复审通过（`review/wp03-closure-review-2026-09-19/report.md`；内容身份、注册/查找/枚举、已述缺失值和状态变化、schema 结构及校验边界、固定规则与作者数据区分、字段责任目录及适用静态场景范围）；WP79 覆盖审查继承 |
| 参考与已读 | 逐行阅读 `010_Data/001_GameData.rb`；全文 `008_Species.rb`、`006_Item.rb`、`005_Move.rb`、`018_MapMetadata.rb`；例外定点：`015_Trainer.rb:56–84`、`021_PhoneMessage.rb:36–69`、`013_Encounter.rb:20–59`、`016_Metadata.rb:55–57`、`017_PlayerMetadata.rb:45–49`、`011_TerrainTag.rb:31–36`、`019_DungeonTileset.rb:38–42`、`020_DungeonParameters.rb:58–65`、`010_SpeciesMetrics.rb:32–56`；编译侧 `002_Compiler_CompilePBS.rb:4–60, 283–327, 610–625, 658–767, 791–886`、`001_Compiler.rb:95–148, 384–459, 742–842, 1039–1075`；启动 `999_Main/999_Main.rb:25–41`；资源 `001_MiscPBSData.rb:27–63`；验证 `004_Validation.rb:12–29`；战斗呈现链 `006_Battle_Scene_Objects.rb:585–590`；`019_Utilities/001_Utilities.rb:137–153` |
| 证据层级 | 已定位/静态确认；无运行确认 |
| 场景/向量 | 测试目录 KR01–KR12（`test-catalog/generic-kernel-wp02-03-04.md`） |
| 具名未验证 | U06；字符串查找大小写/符号一致性；未知身份异常呈现；schema 全集与非法输入拒绝；非类产物结构；双身份键冲突 |

### T-WP04-01 《PBS 生命周期》

| 字段 | 内容 |
| --- | --- |
| 最终条目 | `deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md` §1–§11 |
| 分类/归属 | Demo/Developer Experience（作者工作流）；Generic Kernel（编译机制）；WP04（F02-02、F02-03） |
| 批准输入 | `specs/kernel/wp04-pbs-lifecycle.md`（当前身份 `6cbb57db365be998ec3d117a61fb388008d2f7c63e6674d23e9f6bcf86880a9b`／25,113——含 GR-001 分词位置条件已闭合修订的当前有效版本；早期身份链见 manifest §3） |
| 审查依据 | 2026-09-19 WP04–WP07 v3 复审通过（`review/wp04-wp07-recheck-v3-2026-09-19/report.md`）；2026-10-01 GR-001～003 定点复审 PASS_SCOPED（`review/gr001-gr003-review-2026-10-01/recheck-v2/report.md`）；WP79 覆盖审查继承 |
| 参考与已读 | 定点逐行：`001_Compiler.rb:12–40, 184–293, 384–463, 690–737, 742–842, 924–947, 1020–1116`；`002_Compiler_CompilePBS.rb:4–67, 1274–1319`；`003_Compiler_WritePBS.rb:1–65, 105–131, 794–820`；`004_Compiler_MapsAndEvents.rb:45–83, 473–512, 771–800, 1683–1750`；`999_Main/999_Main.rb:16–41`；`020_Debug/003_Debug menus/002_Debug_MenuCommands.rb:1378–1385` |
| 证据层级 | 已定位/静态确认/数据样本确认；无运行确认 |
| 场景/向量 | 测试目录 KL01–KL18（`test-catalog/generic-kernel-wp02-03-04.md`） |
| 具名未验证 | 失败后部分状态组合与恢复；转换规则全集（WP75）；插件影响（U09）；文本收集细节（WP08）；宿主工程写回条件；schema 逐字段语义 |

## 索引维护

- 后续批次按同字段追加（每批一个 `T-<包>-<序>` 区块）；字段可按批次实际需要调整，但不新增具体框架 API。
- **身份定位规则**：被审身份（复审批准对象）以各闭合/通过报告的固定版本表与独立复审冻结输入为准；当前登记身份以 manifest §1 当前行为准；历史身份链见 manifest §3。**不得以 manifest §1 的当前行替代历史被审身份**；索引正文应直接给出被审身份的完整哈希或可直接定位它的批准基线/冻结输入。
- 批准输入身份变化（修订/回填）时更新「批准输入」并保留被审身份；本索引自身随批次登记入中央清单。
- 净化正文与索引不一致时以批次检查记录为准先登记问题，不静默改写。
