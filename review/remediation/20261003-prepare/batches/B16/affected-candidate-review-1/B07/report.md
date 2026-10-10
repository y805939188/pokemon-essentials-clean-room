**B16 affected candidate／B07：PASS_SCOPED**

本独立结论锁定 candidate `ae223d7bfb9ff6ed8a1ac153debb986115345957`，tree `7b3a16f86aea8438eceb007436687b72aced8e74`；FIX_BASE 为 B13-C `27185563f307e16d2612fa86e83b2c9bd772c79e`。publication `5c70c6945ede498f1d7d59592da1d37a96c07a98` 仅用于读取派发，评审对象不是发布后继。

接受 WP28 第89–92/192–199行、WP29 有限槽及第174行、WP30 §6.3 与新 UI 消费者接合。B035 不是默认库存失败结论；A048/C126 没有把首次详情失败搬到正常少招教学。PT-A23 的24/20实际转移、A31不同/重叠3/2、A33健康蛋无合格仍可取消等只覆盖本地 C003，其他子类型完整保持。A044简称建议与B05相同，不改变真实选物来源判断。

| Caller / 真实接口 | Data / condition | 独立范围判断 |
| --- | --- | --- |
| 背包/Party → WP28/WP30 教学与重学 | TR具名兼容、更多候选开启、正常遗忘；重学空候选与非空分开 | 背包包装初始记录影响遗忘后候选，队伍通用学习不追加；空候选首次严格ID校验失败早于选择循环，普通教学不套空重学失败。 |
| 商店 → WP29 容量/库存/金钱与BP | 有限两槽不排序；POTION999/997、购买3；默认无限容量另列 | 仅前2件添加后第3件失败，移除从首槽扣2得997/999；金钱/购买统计无成功增加。移除失败可部分写入；不改默认无限容量规则。 |
| 背包排序 → 保存选中位置 | 手动可排序口袋；过滤/自动排序不套用 | 方向移动即写保存索引；BACK恢复次序/本次位置，保存索引保留。 |
| BP数量窗 → 实际确认扣款 | 足额BP、正常资源/容量；价格20及奇数21 | 数量×floor(单价/2)仅显示，实际数量×单价；旧C29逐字保持。 |

固定接受输入及候选定位：

- [物品接受接口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md)：第89–92/192–199行。
- [商店接受接口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/creature-rpg/wp29-shops-and-exchanges.md)：有限容量/第174行。
- [成长/重学接受接口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md)：§6.3。
- [新UI消费者](https://github.com/y805939188/pokemon-essentials-clean-room/blob/ae223d7bfb9ff6ed8a1ac153debb986115345957/deliverables/final-specification-set/user-interface/wp66-c-bag-item-storage-and-shop-ui.md)：§3.2/§6.2。
- [教学UI消费者](https://github.com/y805939188/pokemon-essentials-clean-room/blob/ae223d7bfb9ff6ed8a1ac153debb986115345957/deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md)：§7。

非阻断措辞判断见 [共享说明](../B01/nonblocking-notes.json)：A044-N1；完整定义和真实前提控制结论。

共享核验只做一次，见 [identity-and-preservation.json](../B01/identity-and-preservation.json)、[qualified-control-coverage.json](../B01/qualified-control-coverage.json) 和 [source-reading-log.json](../B01/source-reading-log.json)。完整未过滤 FIX_BASE→candidate 流为2,248,505字节，SHA-256 `f8012172e5751ba620d9ddd37793382f9128973ba2331fef187575adbbf7fd7b`；全部78路径列于独立核验，11既有payload修改、其余为本批新增证据。基线无删除；11许可payload之外36,339路径的模式/类型/blob保持，240个接受贡献及其固定统计文件字节保持。目录460旧行顺序/重复次数保持，451行逐字不变、9个分配行修订、24新行；五原稿scope3 before/after精确相同仅证明许可，六净稿及五原稿另作质量判断。24贡献/20主责的完整original/approved/current控制和12 effective值全部核验，没有把短焦点或author result当裁决。

这是静态设计/来源/差异复核。reference、游戏、Ruby、行为向量及旧作者/reviewer程序执行均为0；新Git/JSON/字节/行元数据检查不称运行测试。U01–U10、G01–G12、AX01–AX20、条件树果67、素材/翻译/宿主/输入/插件/真实Demo及未完成非局部义务保留。

请求配置为 gpt-6.1-sol／ultra／Standard（service_tier=default）；有效后端没有可信回显，按派发记录为 UNVERIFIED，未做探针、模型/CLI回退或静默降级。

本报告只签此 owner 的 candidate affected 范围；不代签 FULL、作者、scope、G/ACT 或 C，不关闭 canonical 项。全体14个owner各自结论见 [共享索引](../B01/review-index.json)。
