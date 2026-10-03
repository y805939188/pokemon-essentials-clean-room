# WP04–WP07 批次闭合复审

日期：2026-09-19。独立 reviewer，Reference/Audit 侧。本文及配套快照不是 WP80 sanitized 产物。

**结论：PASS_SCOPED。WP06-R03 已闭合，WP04/WP05/WP07 的管理性状态回填通过。WP04–WP07 批次的限定范围均已通过，可以开始下一批 WP08–WP10。**

有一处不影响字段目录及行为结论的摘要重复计数，按 §4 在状态登记时维护即可，不阻塞后续批次。

## 1. 实际对象与固定基线

工作区 `/Users/dingshinn/Desktop/pokemon-framework-reference/`。参考 HEAD 实测仍为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，describe 为 `v21.1-23-g8c5911e4`；默认机制世代 8。

| 对象 | 被审 SHA-256 | 字节数 |
| --- | --- | ---: |
| WP06 主文档 | `3cdfc081a9256695f1ceec4853e21e1303947b8697d6b578c0957bff288ef75a` | 20824 |
| WP06 统计目录附表 | `15b75cea1698c8978f4cc33380089f3c501cfec0ab8894f3991a6a6513e2d04a` | 14954 |
| WP04 状态回填版 | `b5d33db1ac4172c216715df713bda414f7358fa69dcf5c21b5a8a0409d48da59` | 23172 |
| WP05 状态回填版 | `d65b6d14bf95f47d59166f7bcef74984d92b243e465f8c035daa95b9521a24f7` | 18497 |
| WP07 状态回填版 | `2cd5408ae9dbb1d96281057829c6bff125fdf471b2afc0e96020d105801cdbd2` | 17398 |
| Feature Matrix | `2a1b55fb7ebd1c1c8d43ac22a4d7658b527f34af8051951e372fa45c060f854c` | 30861 |
| manifest | `c482cfb033872bf5f39cdb778bcc1d348db4c6143cf6c05c84cc30fdef0d07a1` | 13666 |

当前 manifest **30 项完整哈希和字节数全部匹配**。固定 32 项输入，上轮报告/提示词原件未变。见 [input-manifest.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-closure-review-2026-09-19/input-manifest.json)。

WP04/WP05/WP07 各仅改头尾两处状态说明，没有行为变化；矩阵实际回填五个 Feature 行（F02-02、F01-03、F01-04、F01-06、F01-07），不是摘要表所称“三行”，但均在上轮许可范围内。WP06 两个 Feature 行未擅自升级。实际差异见 [changes-from-v3.diff](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-closure-review-2026-09-19/changes-from-v3.diff)。

## 2. 已执行检查及结果

- 逐项对照上轮 WP06-R03 的数值含义、单位、赋值/读取定位及来源未知项，检查主文档、附表与新场景的一致性。
- 重读树果采摘、普通/BP 商店、纪念球奖励、GameStats 赋值方法及名人堂 UI 读取片段；按名称复核两个赋值方法与 battle_points_won 的定位边界。
- 独立复算：GameStats 74 个声明字段与附表 74 个不同条目一致，无缺失、额外项或重复。见 [stats-field-check.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-closure-review-2026-09-19/stats-field-check.json)。
- 上轮完整性集合的 109 个源文件哈希均未变，Git blob 与固定提交一致；这不等于本轮全文重读 109 文件。Git 只读查询退出码均为 0，普通状态为空，ignored 仍为 `.DS_Store`、`PBS/.DS_Store`。见 [source-checks.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-closure-review-2026-09-19/source-checks.json)。
- 未运行游戏、Ruby、参考表达式、编译器、插件或网络请求；未执行 WP08–WP10。结果是静态审查与推导，不是运行观察。

## 3. 问题处置与通过边界

| 原 WP06-R03 剩余内容 | 本轮结果 |
| --- | --- |
| 最高产量字段 | 已准确改为达到/超过配置最高产量条件的采摘次数；确认及容量前提明确，独立起始的 2→2/3/3 向量正确。 |
| 商店与纪念球统计 | 已改为件数/个数累计；成功购买 3 件增加 3、实际添加 2 球增加 2 的预期正确。 |
| 名人堂/徽章时间 | 实际赋值方法定位到 GameStats；UI 读取另列；赋值机制可读与事件调用者未证分别表达。 |
| battle_points_won | 已撤回“缺失设施发奖事件已证”的断言，改为来源待查；可能依赖缺失事件仅作为推断，允许继续未决。 |

**WP06-R03 关闭。** 上轮及更早关闭的其余 WP04–WP07 问题继续关闭，WP01–WP03 的限定通过结论不变。

WP06 通过范围：固定基线的时间/随机来源与已述消费者边界、游戏计时锚点、通用计步机制、种子/录像输入的有限区分、74 字段统计目录及已述初始化/更新/保存交界、适用静态场景。各领域的完整概率/玩法规则、存档迁移/恢复、缺失事件调用和跨系统确定性仍由原主规格或未知项承接。

本次通过不会关闭 U01–U10；尤其统计赋值方法存在不等于事件可达，BP 获得统计来源仍待查，插件、宿主与外部服务仍未运行验证。也不代表 WP80 清理通过。

## 4. 非阻塞维护项 BATCH-C03：主文档摘要重复计数

**位置**：`specs/kernel/wp06-time-random-steps-stats.md@3cdfc081:92`。

摘要写“特殊中的 7”，将 max_yield_berry_plants 再列入特殊组，但该字段已包含在“道具活动 9”中。附表正确且没有重复；仅该摘要重复归组。特殊组中机制可读的字段为两个时间赋值字段及 Safari/BugContest 四项，共 **6** 个。

**最小维护**：将“特殊中的 7”改为 6，并从这段特殊组枚举删除 max_yield_berry_plants；或删除冗余的组数摘要，直接引用附表。按当前分类，可读机制 65 项、八项缺失事件相关登记及一项来源待查合计 74，但不必再维护一套重复总数。

这是统计摘要维护，不改变任何字段行为、来源定位或目录覆盖，**不要求再次全包送审，也不阻塞 WP08–WP10**。可与 WP06 状态回填同次完成，保留本轮被审字节与维护 diff。

## 5. 状态建议

可以登记 WP06 主文档与统计附表为 **Reviewed（§3 限定范围）**，并回填：

- F01-05：WP06 时间/随机/计步的已审机制子范围为 Reviewed；U05 一致性及后续领域规则保持其原状态/归属。
- F03-05：WP06 统计目录、已述更新与保存交界子范围为 Reviewed；迁移、保存生命周期、缺失事件与业务完整语义不随之升级。

WP04/WP05/WP07 已回填的范围维持，其他 Feature 不扩张。回填及 C03 维护后保留旧被审哈希、新哈希与实际差异，不改旧报告原件。

## 6. 下一批及停止点

原计划 `planning/extraction-plan.md@c1735877` 的下一批可为 **WP08–WP10，共 3 包**：

| 包 | 内容 | 声明依赖与批内顺序 |
| --- | --- | --- |
| WP08 | 本地化：文本域、语言选择、提取/编译/回退 | WP03、WP04 已通过 |
| WP09 | 保存、启动、新游戏/继续 | WP03、WP06 已通过 |
| WP10 | 迁移和恢复 | WP02 已通过；使用本批 WP09 已自检、固定版本的相关输出，并在批末联合核对 |

无需每做完一包就等外审。逐包保持独立产物与状态，批内 WP09→WP10 的知识依赖不能省略，也不把同批自检当 Reviewed。计划仍为 87 个可执行包，不重新编号。

使用 [WP08–WP10 批次执行提示词](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-closure-review-2026-09-19/next-batch-prompt.md)。本轮止于报告与提示词交付，未代提取方回填状态或开始新包。最终一致性记录见 [final-checks.json](/Users/dingshinn/Desktop/pokemon-framework-reference/review/wp04-wp07-closure-review-2026-09-19/final-checks.json)。
