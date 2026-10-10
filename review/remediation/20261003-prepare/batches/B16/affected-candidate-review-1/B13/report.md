**B16 affected candidate／B13：PASS_SCOPED**

本独立结论锁定 candidate `ae223d7bfb9ff6ed8a1ac153debb986115345957`，tree `7b3a16f86aea8438eceb007436687b72aced8e74`；FIX_BASE 为 B13-C `27185563f307e16d2612fa86e83b2c9bd772c79e`。publication `5c70c6945ede498f1d7d59592da1d37a96c07a98` 仅用于读取派发，评审对象不是发布后继。

B13-C是本次FIX_BASE。独立对接 WP54 第47/93/99–103行、WP56 Arena 与WP58录制条款，候选新增接口段明确继承三个已接受限定，既不把nil与[]合并，也不把位置保存变成按身份事务还原。此PASS_SCOPED不是B13整批重审，更不为后续ACT背书。

| Caller / 真实接口 | Data / condition | 独立范围判断 |
| --- | --- | --- |
| 多选UI → WP54报名 | UI nil取消；工具/替换UI可提交[]；人数下限仍是正常UI守卫 | nil不提交；[]覆盖报名并校验false、进行中可置活动队伍空。候选不声称正常CONFIRM可提交空列表。 |
| 选择/战斗 → WP54位置恢复/WP56 Arena/WP58记录 | 正常返回的当前位置恢复；中途失败、连续计数及属主询问时点分开 | 新§4.6引用保持位置而非身份恢复、失败前缀、Arena持续3/4/5及问询非一律回合末。 |

固定接受输入及候选定位：

- [报名/恢复接受接口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md)：第47/93/99–103行。
- [Arena接受接口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/combat-requirements/wp56-palace-and-arena-variants.md)：Arena连续计数/替补。
- [录制接受接口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md)：初始/攻击/回合末属主询问。
- [UI桥](https://github.com/y805939188/pokemon-essentials-clean-room/blob/ae223d7bfb9ff6ed8a1ac153debb986115345957/deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md)：§4.6 第116行。

共享核验只做一次，见 [identity-and-preservation.json](../B01/identity-and-preservation.json)、[qualified-control-coverage.json](../B01/qualified-control-coverage.json) 和 [source-reading-log.json](../B01/source-reading-log.json)。完整未过滤 FIX_BASE→candidate 流为2,248,505字节，SHA-256 `f8012172e5751ba620d9ddd37793382f9128973ba2331fef187575adbbf7fd7b`；全部78路径列于独立核验，11既有payload修改、其余为本批新增证据。基线无删除；11许可payload之外36,339路径的模式/类型/blob保持，240个接受贡献及其固定统计文件字节保持。目录460旧行顺序/重复次数保持，451行逐字不变、9个分配行修订、24新行；五原稿scope3 before/after精确相同仅证明许可，六净稿及五原稿另作质量判断。24贡献/20主责的完整original/approved/current控制和12 effective值全部核验，没有把短焦点或author result当裁决。

这是静态设计/来源/差异复核。reference、游戏、Ruby、行为向量及旧作者/reviewer程序执行均为0；新Git/JSON/字节/行元数据检查不称运行测试。U01–U10、G01–G12、AX01–AX20、条件树果67、素材/翻译/宿主/输入/插件/真实Demo及未完成非局部义务保留。

请求配置为 gpt-6.1-sol／ultra／Standard（service_tier=default）；有效后端没有可信回显，按派发记录为 UNVERIFIED，未做探针、模型/CLI回退或静默降级。

本报告只签此 owner 的 candidate affected 范围；不代签 FULL、作者、scope、G/ACT 或 C，不关闭 canonical 项。全体14个owner各自结论见 [共享索引](../B01/review-index.json)。
