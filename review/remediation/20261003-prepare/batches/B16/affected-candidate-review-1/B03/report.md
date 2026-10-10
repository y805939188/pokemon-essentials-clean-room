**B16 affected candidate／B03：NOT_AFFECTED**

本独立结论锁定 candidate `ae223d7bfb9ff6ed8a1ac153debb986115345957`，tree `7b3a16f86aea8438eceb007436687b72aced8e74`；FIX_BASE 为 B13-C `27185563f307e16d2612fa86e83b2c9bd772c79e`。publication `5c70c6945ede498f1d7d59592da1d37a96c07a98` 仅用于读取派发，评审对象不是发布后继。

反向导航仅指向共享 UI 目录。完整差异中的9条旧行修订全部在 NV/PT/BG，24条增补归本批；没有改 B03 的 MP 或其它地图条件，也没有把 C003 的地图/属性子类型改成 UI 示例。地图正文和地图目录全字节保持。没有发现新 caller/data/condition 进入本 owner 的转移合同，因此有据 NOT_AFFECTED。

| Caller / 真实接口 | Data / condition | 独立范围判断 |
| --- | --- | --- |
| 地图拓扑/转移 → UI 字段与地域读者 | 地图身份、区域与既有 MP/WT 条件 | 新局部 PT-A23/A31/A33、单位和图鉴显示条件不改地图连接、转移、区域身份或属性选择器提交。 |

固定接受输入及候选定位：

- [地图合同](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md)：§1 / §9；MP01–MP27。
- [地图目录](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md)：MP/WT 原行。

共享核验只做一次，见 [identity-and-preservation.json](../B01/identity-and-preservation.json)、[qualified-control-coverage.json](../B01/qualified-control-coverage.json) 和 [source-reading-log.json](../B01/source-reading-log.json)。完整未过滤 FIX_BASE→candidate 流为2,248,505字节，SHA-256 `f8012172e5751ba620d9ddd37793382f9128973ba2331fef187575adbbf7fd7b`；全部78路径列于独立核验，11既有payload修改、其余为本批新增证据。基线无删除；11许可payload之外36,339路径的模式/类型/blob保持，240个接受贡献及其固定统计文件字节保持。目录460旧行顺序/重复次数保持，451行逐字不变、9个分配行修订、24新行；五原稿scope3 before/after精确相同仅证明许可，六净稿及五原稿另作质量判断。24贡献/20主责的完整original/approved/current控制和12 effective值全部核验，没有把短焦点或author result当裁决。

这是静态设计/来源/差异复核。reference、游戏、Ruby、行为向量及旧作者/reviewer程序执行均为0；新Git/JSON/字节/行元数据检查不称运行测试。U01–U10、G01–G12、AX01–AX20、条件树果67、素材/翻译/宿主/输入/插件/真实Demo及未完成非局部义务保留。

请求配置为 gpt-6.1-sol／ultra／Standard（service_tier=default）；有效后端没有可信回显，按派发记录为 UNVERIFIED，未做探针、模型/CLI回退或静默降级。

本报告只签此 owner 的 candidate affected 范围；不代签 FULL、作者、scope、G/ACT 或 C，不关闭 canonical 项。全体14个owner各自结论见 [共享索引](../B01/review-index.json)。
