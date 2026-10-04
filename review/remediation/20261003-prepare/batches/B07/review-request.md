# B07 与受影响 B04 独立复审请求

本文件仅定义待父任务调度的复审范围，不启动审查、不作 verdict。完整 B07 候选 SHA／tree 由作者交付与外部 publication receipt 指定；必须核对该 SHA 的所有输出及 batch-local 证据。作者基线 `219cc3c182750155e9dbf2cb619f420b3922de27`，固定原 findings `93e10babe0b9c9ef8b3f5277754541b447beeeb4`，批准计划 `41fffb540c6483f5296ea0d33b789b75180d27ed`。

R-B07 请求独立 Ultra／Standard(default)，承担19贡献／12主责完整合同：冻结下游 handshake 的全部 contribution_controls，原 findings 完整对象、current_qualifications、effective_case_constraints、最终 root_adjudications、各 extensions.root_review（C003全部8扩展），以及计划 finding-acceptance。作者 acceptance-map 是定位索引，不替代上述原验收对象，不凭历史/raw措辞扩张现行资格。实际有效配置没有可信回显则继续 UNVERIFIED，Plan A 已接受，不新设认证门。

请读完整未过滤差异 `git diff 219cc3c182750155e9dbf2cb619f420b3922de27 <完整候选SHA>` 和全部新证据，核对8正式输出、6必要原稿、28新增静态行、8必要旧行修正，以及正确原条款、旧ID顺序／重复和BG/DC、RM/CP完整保护章节。每原ID要核验具体输入、顺序状态变化／部分失败、唯一静态预期及邻近反向分支；保留共责、其他批待项、源未读范围与0执行，不增加根因计数或关闭。

单独 R-B04 受影响候选复审同样请求独立 Ultra／Standard(default)，不能由 R-B07报告或作者自检代替。触发文件与精确前后身份如下，基线均为上述219完整SHA；after对应完整候选。

| 变化的消费者 | before blob / SHA256 / bytes | after blob / SHA256 / bytes |
| --- | --- | --- |
| deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md | `048b8ecc193fccaacf0f6f6e8bf1d887f3856076` / `6aba982f3fff5a053030d0bfff71b3866b9c4f5ac55aa6f21a2df4ed176e2feb` / 32079 | `bb7c344cfbb24b8f8eb3e8ed8bfea0be6e426580` / `63d6b9d244b1700f88e311edae37306aad9831358256c1c8ed60f63a11a5737a` / 39277 |
| deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md | `72578036b0cc9d1268d3be5250a3737195082df9` / `24ad1e4513a5e2ac0458895851d32a6969c1cc2ffe8ee38728260ea98257d610` / 25396 | `ea4ebda45c4827d31a4d0af9bcf4332313b64104` / `97145b9f2bb6c5109f011c61514455558ac4bf62254a701258facd786f042e38` / 28837 |

WP28 的新增 HP／状态／混乱资格及消费、糖果取消／成功提交、TR 和形态交互、直接缺处理器分支应反查 B04 资源／消息／音效调用边界：不得把效果失败、取消或复检的状态规则推成通用回滚；正常返回清理与异常路径分开。WP30 的摘要遗忘、重学最初记录与空候选首次详情失败、事件选择及经验消息需反查 B04 文本严格身份验证、消息窗口、资源匹配与视觉转场：明确前置成功和空详情最早失败，不把未读字体／媒体加载或外层预检当作已证。WP31预演也只给有效资源／计时前提下静态属性，不能替B04宣告真实像素。

B04 具体核验依赖为 WP15 资源匹配／BGM／BGS暂停恢复／ME与演化音效，WP16前战转场的正常返回、预置清理、fade及失败前置，WP16世界视觉与资源分支，WP17 draw-text标签／消息严格身份验证。所有既有批准与 C003 共享资格保留历史身份，变化交界在本次精确版本重新核验。以下8份追加输入均不变，具体SHA256/bytes在 dependency-manifest中：

| B04 固定输入 | blob | SHA256 | bytes |
| --- | --- | --- |
| deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md | `23c487115d8b01638ed2db062546ef2a58abdc9f` | `541d0c8592068c3c6714ddc90824ee735955b85cc154257b9351aca6b7fc13a1` | 20852 |
| deliverables/final-specification-set/engine-overworld/wp16-pre-battle-transitions.md | `e81a8d1230dd341568dbff2d7506cfacb5c38c64` | `bae1ca4a6430d26d01070e2163b9c4b87acf708c66ab97606c623e268e4221f1` | 16503 |
| deliverables/final-specification-set/engine-overworld/wp16-world-rendering-and-visual-transitions.md | `af9e568596a6e317c912184af37549a44977c9ed` | `7923f168dd0c907c03721d7265ce060f914005ec5404066d795db01d34577b3a` | 32860 |
| deliverables/final-specification-set/user-interface/wp17-draw-text-tags.md | `0e643fe2440bc78ac6095d9e6fb4d15fca3994b0` | `fb9261280143bb35c63e98c40df4a4dbb87bbde5d2c97dbda66f5855d41e48dc` | 8275 |
| specs/overworld/wp15-resource-matching-and-audio.md | `dd57e87cd65884a260ce6774a1bc15123ac7e1cd` | `2f0104d988b0e0860ceb63e8b321d433d5a36cf0098bcdee15cacfc4965c0a57` | 32257 |
| specs/overworld/wp16-pre-battle-transitions-appendix.md | `12e8aadffdd03262079185e5be447ed6f2748dff` | `87373d476223c5dbfa419daeb9e1c2d3a7bcdddafbdedcb16c3791707083559f` | 24626 |
| specs/overworld/wp16-world-rendering-and-visual-transitions.md | `304d2a97d2543cc91472b63d8ac5b5fcbe59b5f8` | `9da65d3ac6ec004e2f88b43d9d575fd41064dc59d167e22dece1b568cc8605af` | 39209 |
| specs/ui/wp17-draw-text-tags.md | `1a4c1afed08602c44280f01c2951a72d777871a5` | `3b875044c4102756575f20bc3012cbb61e284fb23089582ab3d6fe555d0861bb` | 9268 |

完整依赖除上述8份还有64计划输入及35冻结证据、2管理、7计划身份，均见 dependency-manifest／input-identities。B06 WP24 只承接六逻辑音轨请求和引子前记忆；其PT41–63既有字节与Q/0、R/r及末空文本差异保持，不自动批准伙伴、雷达或完整BattleAudio。

两类候选独立报告分别返回：完整 before／after commit与未过滤差异；受影响正文／原稿／目录／caller-callee定位；固定原controls、acceptance与共享资格；正向／负向静态对照及运行0；独立审者、verdict、报告完整SHA、实际配置可信程度、残余范围和依赖身份。发现问题先回传原ID与精确条款，不自行批准关闭；报告需覆盖真正候选所有字节。

AREG 若做实际整合，须重新绑定完整 actual SHA、实际依赖和 `predecessor→actual`、`candidate→actual` 未过滤差异，再分别完成 R-B07 actual受影响Ultra 与单独受影响 R-B04 actualUltra。候选 PASS 不能自动带入 actual，也不能替其他责任批／严格门。父任务C只在收到精确实际与两类报告收据后决定接受；当前229 OPEN、0 CLOSED，B07尚未接受。

保留U01–10／G01–12／AX01–20和全部具名未读范围；仅允许固定参考只读文本、Git/hash/JSON文档记账，不运行参考、游戏、Ruby、编译／转换／生成／反序列化器、模拟器或行为向量。运行观察、执行向量、参考执行、已证demo链均0。作者自检不替独立报告；公共登记唯一写者AREG，本候选只附建议。
