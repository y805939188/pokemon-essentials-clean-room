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

## 索引维护

- 后续批次按同字段追加（每批一个 `T-<包>-<序>` 区块）；字段可按批次实际需要调整，但不新增具体框架 API。
- **身份定位规则**：被审身份（复审批准对象）以各闭合/通过报告的固定版本表与独立复审冻结输入为准；当前登记身份以 manifest §1 当前行为准；历史身份链见 manifest §3。**不得以 manifest §1 的当前行替代历史被审身份**；索引正文应直接给出被审身份的完整哈希或可直接定位它的批准基线/冻结输入。
- 批准输入身份变化（修订/回填）时更新「批准输入」并保留被审身份；本索引自身随批次登记入中央清单。
- 净化正文与索引不一致时以批次检查记录为准先登记问题，不静默改写。
