**B16 affected candidate／B15：PASS_SCOPED**

本独立结论锁定 candidate `ae223d7bfb9ff6ed8a1ac153debb986115345957`，tree `7b3a16f86aea8438eceb007436687b72aced8e74`；FIX_BASE 为 B13-C `27185563f307e16d2612fa86e83b2c9bd772c79e`。publication `5c70c6945ede498f1d7d59592da1d37a96c07a98` 仅用于读取派发，评审对象不是发布后继。

接受 WP62 第126/128/140–144行与新WP66-B §5.2/§6/§7接合。C121保留三个显示消费者的差异，C123正文转移表保留特殊端点的不对称守卫，不由目录末尾简称推广为任意状态的对称钳制。旧 B25/B26/B35、B31/B37/B38 以及 Pokegear 条款/行全字节保持。墙纸C120是另一个owner的真实接口，不据同文件修改将B15一起阻断。

| Caller / 真实接口 | Data / condition | 独立范围判断 |
| --- | --- | --- |
| 图鉴UI → WP62计数/观看/搜索记录 | 四状态；已有结果态BACK与失败Start后Cancel分开 | 区域只绘两个计数；Start先写模式，失败不替换接受参数/列表，非结果态Cancel不恢复模式，结果态BACK才复位。 |
| Forms选择器 → 已见档/末次形态 | 结构门先于已见；同图折雄档、命名优先、显示全部仅绕已见 | 先认结构多形态；保留首轮与移动写回、BACK不回滚；nil解析相同不证明素材。 |
| 搜索/Info → 原始体型/离散档 | locale位置3–4为US；37档与-1/37哨兵各自 | Info重/.45359与搜索重/.254分开；原始过滤不改，大小表/不对称导航及ACTION后USE职责保持。 |

固定接受输入及候选定位：

- [图鉴接受接口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md)：第126/128/140–144行。
- [UI消费者](https://github.com/y805939188/pokemon-essentials-clean-room/blob/ae223d7bfb9ff6ed8a1ac153debb986115345957/deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md)：§5.2/§6.2–6.3/§7.1–7.2。
- [Pokegear接受接口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/ae223d7bfb9ff6ed8a1ac153debb986115345957/deliverables/final-specification-set/user-interface/wp63-pokegear-map-music-and-phone.md)：既有地域/音乐/电话条件。

非阻断措辞判断见 [共享说明](../B01/nonblocking-notes.json)：C123-N1；完整定义和真实前提控制结论。

共享核验只做一次，见 [identity-and-preservation.json](../B01/identity-and-preservation.json)、[qualified-control-coverage.json](../B01/qualified-control-coverage.json) 和 [source-reading-log.json](../B01/source-reading-log.json)。完整未过滤 FIX_BASE→candidate 流为2,248,505字节，SHA-256 `f8012172e5751ba620d9ddd37793382f9128973ba2331fef187575adbbf7fd7b`；全部78路径列于独立核验，11既有payload修改、其余为本批新增证据。基线无删除；11许可payload之外36,339路径的模式/类型/blob保持，240个接受贡献及其固定统计文件字节保持。目录460旧行顺序/重复次数保持，451行逐字不变、9个分配行修订、24新行；五原稿scope3 before/after精确相同仅证明许可，六净稿及五原稿另作质量判断。24贡献/20主责的完整original/approved/current控制和12 effective值全部核验，没有把短焦点或author result当裁决。

这是静态设计/来源/差异复核。reference、游戏、Ruby、行为向量及旧作者/reviewer程序执行均为0；新Git/JSON/字节/行元数据检查不称运行测试。U01–U10、G01–G12、AX01–AX20、条件树果67、素材/翻译/宿主/输入/插件/真实Demo及未完成非局部义务保留。

请求配置为 gpt-6.1-sol／ultra／Standard（service_tier=default）；有效后端没有可信回显，按派发记录为 UNVERIFIED，未做探针、模型/CLI回退或静默降级。

本报告只签此 owner 的 candidate affected 范围；不代签 FULL、作者、scope、G/ACT 或 C，不关闭 canonical 项。全体14个owner各自结论见 [共享索引](../B01/review-index.json)。
