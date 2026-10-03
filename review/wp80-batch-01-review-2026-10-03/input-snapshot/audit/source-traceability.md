# 来源追溯索引（WP80；2026-10-03 起）

用途：为 `deliverables/final-specification-set/` 的净化正文提供**独立追溯**——从最终条目反查批准的输入规格及身份、独立审查依据、参考文件及已读范围、证据层级与对应场景/向量。**本索引是审计材料**：净化正文可独立阅读，不依赖本索引；审计定位（源方法名、源文件路径、行号）集中保存在此处，正是净化正文不含它们的原因。

## 字段口径

| 字段 | 含义 |
| --- | --- |
| 最终条目 | 净化交付位置（文件 § 章节） |
| 分类/归属 | 项目分类与内容包 ID（84 个既有包 ID；附表归入父包） |
| 批准输入 | 批准的输入规格（路径）及其内容身份（SHA-256 前 8 位/字节；完整身份见 manifest §1） |
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
| 批准输入 | `specs/overworld/wp16-world-rendering-and-visual-transitions.md`（`d7aad4aa`／21,399；Reviewed 限定静态范围） |
| 审查依据 | 2026-09-23 外部闭合复审 PASS_SCOPED（WP16-R01/R02 关闭；`review/wp14-wp16-recheck-2026-09-23/`）；WP79 覆盖审查继承（`review/wp79-stage-review-2026-10-03/recheck-v6/report.md`） |
| 参考与已读 | 全文：`006_Map renderer/001_TilemapRenderer.rb`（620）、`005_Sprites/003_Sprite_Character.rb`（187）、`004_Sprite_Reflection.rb`（89）、`006_Spriteset_Global.rb`（56）、`007_Spriteset_Map.rb`（131）；定点：`012_Overworld/001_Overworld visuals/001_Overworld_Weather.rb`（结构/常量/fade_in 段及 :16–17, :66–95, :425–428, :460–477）、`010_Data/001_Hardcoded data/012_Weather.rb`（注册目录）、`004_Game classes/001_Game_Screen.rb:13–69` 及更新段（含 :65–70）、`012_Overworld/003_Overworld_Time.rb:100–126`、`005_Sprites/009_Sprite_DynamicShadows.rb:1–40`；引用不重读：WP11/WP12/WP13/WP15/WP06 |
| 证据层级 | 已定位/静态确认；无运行确认 |
| 场景/向量 | 测试目录 WR01–WR15（`test-catalog/engine-overworld-wp16.md`） |
| 具名未验证 | 一切实际视觉结果/动画时序/宿主输出；动态阴影全部创建者；地图元数据天气字段消费者链；战斗内画面 |

### T-WP16-02 《战前过渡》

| 字段 | 内容 |
| --- | --- |
| 最终条目 | `deliverables/final-specification-set/engine-overworld/wp16-pre-battle-transitions.md` §1–§10 |
| 分类/归属 | Engine/Overworld Integration（主）、Combat Requirements（交界）；WP16 附（F05-04-supp-BT） |
| 批准输入 | `specs/overworld/wp16-pre-battle-transitions-appendix.md` v2（`2d499cf4`／23,334——被审对象；当前回填身份 `aabb2509`／23,630，行为正文相同） |
| 审查依据 | 2026-10-03 WP79 v6 独立复审 PASS_SCOPED（R02 关闭；`review/wp79-stage-review-2026-10-03/recheck-v6/report.md`） |
| 参考与已读 | 全文：`012_Overworld/002_Battle triggering/002_Overworld_BattleIntroAnim.rb`（432——注册表 :17–42、让位助手 :51–57、包装 :59–152、核心演出 :154–188、五组注册 :198–432，资源规则 :277–298 定点复核）；定点：`009_Scenes/001_Transitions.rb:1–175`（入口/单位/特殊判定/基类）与十四个固定时长声明行（:459, :527, :596, :675, :754, :845, :943, :1010, :1092, :1168, :1244–1245, :1437–1438, :1677–1678, :1768–1769）、:1244–1345（VSTrainer 资源/时间线）、:1437–1460、:1677–1690、:1768–1786（三效果资源段）、:440–454（淡黑/淡白无固定时长）、`_interrupt_transition` 全库检索（仅 :31/:45 两处读取）；`012_Overworld/001_Overworld.rb:527–536`（等待秒单位）；`001_Technical/002_Files/001_FileTests.rb:119–133`（路径解析）；调用侧 `012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb:401–402, 521–522`、`018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb:65–66, 125–126`、`002_BugContest.rb:382`、`001_SafariZone.rb:132–133`；引用不重读：WP15/WP36 §4.5/WP42 §7/WP60/WP63/WP67-A §3.2 |
| 证据层级 | 已定位/静态确认；无运行确认 |
| 场景/向量 | 测试目录 BT01–BT16（`test-catalog/engine-overworld-wp16.md`） |
| 具名未验证 | 素材存在性（Graphics/ 缺失）与实际帧呈现/墙钟耗时；注册表运行期改动与扩展注册；具名效果逐帧呈现细节（像素级具名排除） |

## 索引维护

- 后续批次按同字段追加（每批一个 `T-<包>-<序>` 区块）；字段可按批次实际需要调整，但不新增具体框架 API。
- 批准输入身份变化（修订/回填）时更新「批准输入」并保留被审身份；本索引自身随批次登记入中央清单。
- 净化正文与索引不一致时以批次检查记录为准先登记问题，不静默改写。
