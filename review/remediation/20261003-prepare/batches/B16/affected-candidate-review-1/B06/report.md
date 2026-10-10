**B16 affected candidate／B06：REQUEST_CHANGES**

本独立结论锁定 candidate `ae223d7bfb9ff6ed8a1ac153debb986115345957`，tree `7b3a16f86aea8438eceb007436687b72aced8e74`；FIX_BASE 为 B13-C `27185563f307e16d2612fa86e83b2c9bd772c79e`。publication `5c70c6945ede498f1d7d59592da1d37a96c07a98` 仅用于读取派发，评审对象不是发布后继。

004 的交换身份、C125 的有序位置与失败前缀、预览/图标消费者均通过此范围复核。C120 的新条款同时存在于原稿和净稿，丢失接受 WP25 §3.4 与完整 root adjudication 明示的“不保证任意字符串归一”条件。此处需要收紧局部写回保证，不需要重审或修改旧 WP25、旧贡献/目录。

| Caller / 真实接口 | Data / condition | 独立范围判断 |
| --- | --- | --- |
| 盒显示读取 → WP25 背景记录 | 首次或值已变化；nil/空串、匹配旧格式、整数、非匹配非空字符串各自不同 | 候选 §8.5 的“非法或未解锁墙纸写回”没有保留非法字符串与不可用整数的区别；详见 B16-AFFECTED-C120-1。 |
| 拿起/交换/放下 → WP25 暂持身份 | 持有X、目标Y；目标空/非空与退出守卫 | 成功交换后目标为X、暂持为Y，BACK仍阻挡；成功放下才清暂持。新规则与接受WP25一致。 |
| Party SPECIAL/盒返回 → 队伍有序位置 | 普通Switch旧来源1、存B后队伍压缩；快捷禁SPECIAL | 旧位置仍提交，部分队伍写入及首个面板失败不回滚；BACK无新交换但盒写入保留，未把索引重绑为B身份。 |

固定接受输入及候选定位：

- [接受墙纸兼容边界](https://github.com/y805939188/pokemon-essentials-clean-room/blob/27185563f307e16d2612fa86e83b2c9bd772c79e/deliverables/final-specification-set/creature-rpg/wp25-party-and-storage.md)：§3.4 第79–96行。
- [候选错误新增条款](https://github.com/y805939188/pokemon-essentials-clean-room/blob/ae223d7bfb9ff6ed8a1ac153debb986115345957/deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md)：§8.5 第217行。
- [原稿同一新增条款](https://github.com/y805939188/pokemon-essentials-clean-room/blob/ae223d7bfb9ff6ed8a1ac153debb986115345957/specs/ui/wp66-b-storage-and-pokedex-ui.md)：§8.5 第217行。
- [暂持与位置接口](https://github.com/y805939188/pokemon-essentials-clean-room/blob/ae223d7bfb9ff6ed8a1ac153debb986115345957/deliverables/final-specification-set/user-interface/wp66-a-party-and-summary-ui.md)：§3.3。

阻断项 [B16-AFFECTED-C120-1](findings.json)：新增规则将“非法或未解锁墙纸”笼统保证为写回盒号模16，同时仅排除空串/nil。

以零基盒5的既有或人工背景记录 `box3x`、未读缓存或背景已变化、基础存储依赖正常且无插件为静态边界；不声称正常游戏生成该值或Demo可达。该文本不为空、不符合旧box数字完整行，读取把它留作当前背景并交可用性数值比较；比较先失败，尚未到fallback写回或位图加载。不能由“非法”推出记录改成5、成功显示5。未执行参考、Ruby或向量；不凭静态阅读声称具体宿主异常观察。

独立负整数边界也不支持笼统保证：默认16基础墙纸时，背景编号 `-1` 在可用性谓词的“小于16”分支直接通过，未进入默认编号写回；随后会尝试对应素材，素材存在及实际加载结果仍未证。这里区分实际不可用谓词与笼统非法值，均未执行参考或向量。

最小修复范围：两个新增 §8.5 条款及本批对应追溯，明确不可用整数与成功旧格式转换的回写条件、保留非匹配文本边界。旧 WP25 和旧正确目录无需修改。原稿的精确 after 改动需新的有限 scope 确认；scope3 的许可不代替质量通过。

固定源静态补读：[盒背景读取](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/016_UI/017_UI_PokemonStorage.rb#L378-L397)与[可用性比较](https://github.com/Maruno17/pokemon-essentials/blob/8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/Data/Scripts/014_Pokemon/001_Pokemon-related/004_PokemonStorage.rb#L101-L106)。

共享核验只做一次，见 [identity-and-preservation.json](../B01/identity-and-preservation.json)、[qualified-control-coverage.json](../B01/qualified-control-coverage.json) 和 [source-reading-log.json](../B01/source-reading-log.json)。完整未过滤 FIX_BASE→candidate 流为2,248,505字节，SHA-256 `f8012172e5751ba620d9ddd37793382f9128973ba2331fef187575adbbf7fd7b`；全部78路径列于独立核验，11既有payload修改、其余为本批新增证据。基线无删除；11许可payload之外36,339路径的模式/类型/blob保持，240个接受贡献及其固定统计文件字节保持。目录460旧行顺序/重复次数保持，451行逐字不变、9个分配行修订、24新行；五原稿scope3 before/after精确相同仅证明许可，六净稿及五原稿另作质量判断。24贡献/20主责的完整original/approved/current控制和12 effective值全部核验，没有把短焦点或author result当裁决。

这是静态设计/来源/差异复核。reference、游戏、Ruby、行为向量及旧作者/reviewer程序执行均为0；新Git/JSON/字节/行元数据检查不称运行测试。U01–U10、G01–G12、AX01–AX20、条件树果67、素材/翻译/宿主/输入/插件/真实Demo及未完成非局部义务保留。

请求配置为 gpt-6.1-sol／ultra／Standard（service_tier=default）；有效后端没有可信回显，按派发记录为 UNVERIFIED，未做探针、模型/CLI回退或静默降级。

本报告只签此 owner 的 candidate affected 范围；不代签 FULL、作者、scope、G/ACT 或 C，不关闭 canonical 项。全体14个owner各自结论见 [共享索引](../B01/review-index.json)。
