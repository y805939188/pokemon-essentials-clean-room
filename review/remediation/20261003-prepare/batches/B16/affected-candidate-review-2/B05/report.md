**B16 affected 增量复核／B05：PASS_SCOPED**

独立结论锁定 NEW `356b46b320884e57e71a1cab8413e13594524a7d`／tree `344b606d8368eb09dc9313e09fdda1fa227e6f39`；OLD `ae223d7bfb9ff6ed8a1ac153debb986115345957`。FIX_BASE仍为B13-C `27185563f307e16d2612fa86e83b2c9bd772c79e`，publication `7585b16a65338392af8ff78e7d8a8cb23cd19901`只提供冻结派发，不作为质量目标。

新增检查GIR-FD82-C003的实际HP接口：合法来源50/120用量24先扣至26；目标30/50只回复20至50，目标封顶不回补来源。NEW目录与未变WP66-A原净§4.2一致，符合WP20持久HP和WP28封顶恢复。旧TR/初始记录、原始IV、零招式详情等字节及前提保持；本次补齐实际奶招状态，不从旧通过或作者声明自动推导。

真实接口：Party奶招 → 成员HP记录；实际来源扣量与目标实际回复量独立。

准确旧范围证据来自 [原B05结论](https://github.com/y805939188/pokemon-essentials-clean-room/blob/6abb85d39993db446069e35880eb5de3b9295e4d/review/remediation/20261003-prepare/batches/B16/affected-candidate-review-1/B05/verdict.json)（旧结论只属于OLD）。当前输入的BASE/OLD/NEW完整身份及不变/变化状态见 [共同核验](../B01/identity-and-protection.json) 中本owner条目；不从导航或旧PASS自动推出NEW结论。

[奶招实际接口检查](../B01/milk-interface-check.json)只签本角色的来源/目标HP兼容：完整扣24与实际回复20分开，来源26正确；R-B16-F01的独立FULL门仍由原FULL reviewer签。

共享保护独立核验一次：完整未过滤OLD→NEW 4,453,488字节／49路径，FIX_BASE→NEW 6,692,823字节／124路径；与publication完整拷贝相同。OLD既有36,417路径仅3个单行变化，其余36,414模式/类型/blob保持；11输出中8份不变。BASE许可11输出外36,339路径保持，240接受贡献字节保持。目录OLD484行仅B16-C003改变，其他483行逐字保持；BASE460旧行顺序/重复保持，451原字节保护、9既有分配修订、24本批新增。

完整24贡献／20主责的原始/批准/当前root/extensions/minimum控制以及12 effective值与旧精确证据一致，见 [完整控制与复用记录](../B01/qualified-controls-and-reuse.json)。旧报告、旧错误trace/partial状态冻结；NEW明确后继覆盖当前正确行及两条款，不改写历史或代签其他角色。

全程静态来源/设计/差异及新Git/JSON/字节元数据核验。reference/game/Ruby/compiler/converter/generator/deserializer/行为向量及历史程序执行均为0，不称运行测试。保留全部U/G/AX、具名未读、条件树果67、媒体/宿主/插件/真实Demo及非局部未证。

请求gpt-6.1-sol／ultra／Standard（default）；有效后端无可信回显为UNVERIFIED，按准确派发Plan A继续，未probe/回退/静默降级。

本owner对NEW无剩余affected阻塞；不构成FULL、ACT、G、C或canonical关闭。全体14个独立owner结论见 [报告索引](../B01/review-index.json)。
