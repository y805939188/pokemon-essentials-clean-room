**B16 affected candidate／B05：PASS_SCOPED**

本独立结论锁定 candidate `ae223d7bfb9ff6ed8a1ac153debb986115345957`，tree `7b3a16f86aea8438eceb007436687b72aced8e74`；FIX_BASE 为 B13-C `27185563f307e16d2612fa86e83b2c9bd772c79e`。publication `5c70c6945ede498f1d7d59592da1d37a96c07a98` 仅用于读取派发，评审对象不是发布后继。

WP66-A §7.2/§5.2/§6.1/§6.5 与接受 WP20/WP19 的记录和原始IV接口一致。源侧 Party Item→Use 先从背包选物，当前正文 §4.3、§7.2 已正确定义它。新增“队伍持物Use”简称宜改为“队伍 Item→Use（从背包选物）”，但完整上下文没有承诺消耗成员持物，也没有承诺袋空持物单独成功，故作为非阻断建议。C126 初绘失败与普通教学成功分开，没有强迫领域层统一失败。

| Caller / 真实接口 | Data / condition | 独立范围判断 |
| --- | --- | --- |
| 机器双入口 → WP20 招式与初始记录 | 默认TM57为TR/CHARGEBEAM；合法兼容成员、正常背包选物与教学 | 背包包装去重追加初始记录/机器统计，队伍 Item→Use 不追加二者；成功消耗取实际背包物品。 |
| 摘要 → WP19 原始IV描述 | 原始IV及个人ID；Shadow展示门另列 | HP/攻击/防御/速度/特攻/特防环序，ID模6首遇最大，IV模5；不读Hyper代替值。 |
| 零招式详情 → WP20 成员招式 | 合法零招式、详情首次绘制、资源正常 | 普通MOVES四空位可绘；详情首招字段失败先于BACK。通用少于4招教学仍可直接成功。 |

固定接受输入及候选定位：

- [持久招式接受接口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/creature-rpg/wp20-hp-status-moves-helditem.md)：招式/初始记录条款。
- [IV接受接口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/pokemon-rules/wp19-attributes-ability-and-stats.md)：第145/149–160行。
- [UI消费者](https://github.com/y805939188/pokemon-essentials-clean-room/blob/ae223d7bfb9ff6ed8a1ac153debb986115345957/deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md)：§4.3/§5.2/§6.1/§6.5/§7.2。

非阻断措辞判断见 [共享说明](../B01/nonblocking-notes.json)：A044-N1；完整定义和真实前提控制结论。

共享核验只做一次，见 [identity-and-preservation.json](../B01/identity-and-preservation.json)、[qualified-control-coverage.json](../B01/qualified-control-coverage.json) 和 [source-reading-log.json](../B01/source-reading-log.json)。完整未过滤 FIX_BASE→candidate 流为2,248,505字节，SHA-256 `f8012172e5751ba620d9ddd37793382f9128973ba2331fef187575adbbf7fd7b`；全部78路径列于独立核验，11既有payload修改、其余为本批新增证据。基线无删除；11许可payload之外36,339路径的模式/类型/blob保持，240个接受贡献及其固定统计文件字节保持。目录460旧行顺序/重复次数保持，451行逐字不变、9个分配行修订、24新行；五原稿scope3 before/after精确相同仅证明许可，六净稿及五原稿另作质量判断。24贡献/20主责的完整original/approved/current控制和12 effective值全部核验，没有把短焦点或author result当裁决。

这是静态设计/来源/差异复核。reference、游戏、Ruby、行为向量及旧作者/reviewer程序执行均为0；新Git/JSON/字节/行元数据检查不称运行测试。U01–U10、G01–G12、AX01–AX20、条件树果67、素材/翻译/宿主/输入/插件/真实Demo及未完成非局部义务保留。

请求配置为 gpt-6.1-sol／ultra／Standard（service_tier=default）；有效后端没有可信回显，按派发记录为 UNVERIFIED，未做探针、模型/CLI回退或静默降级。

本报告只签此 owner 的 candidate affected 范围；不代签 FULL、作者、scope、G/ACT 或 C，不关闭 canonical 项。全体14个owner各自结论见 [共享索引](../B01/review-index.json)。
