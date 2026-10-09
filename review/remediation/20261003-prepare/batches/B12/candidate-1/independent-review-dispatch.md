# B12 独立 Ultra 派发入口

这是作者交给父任务的可派发资料，不是已启动复审或作者签出的 PASS。父任务以最终交付的外部完整 candidate SHA/tree 冻结输入；branch tip 只作导航，不代替 SHA。正式 FIX_BASE 仍为 B15-C `1d06c45cc0a744fca181ac80ee573cc9ebb9b862`，tree `5c99f51ec4cc084bc1c2b081306f1b55370744df`；管理包 `9ad5539f38544fef6037356018015fe418021514` 不能替代它。

## FULL 候选任务

请求独立 gpt-6.1-sol / ultra / Standard。reviewer 与作者隔离，按已批准 Plan A 分记 requested/admission/effective；无可信回显如实 UNVERIFIED，不做参数/额度审计，不静默降级或 CLI/native 替代。阅读 AGENTS.md；作者不得启动或代签本任务。

输入入口：

- [independent-review-request.json](independent-review-request.json)：派发需求及原合同的 independent-review-requirements。
- [qualified-control-bindings.json](../author-draft-1/qualified-control-bindings.json)：全部 9 个精确原控制／批准验收对象身份和完整当前 qualified 字段。读取必要原对象与当前 root/extension/effective 限定，不能以局部摘要替代。
- [contribution-matrix.json](contribution-matrix.json)：9 贡献为 003、A046、B017、B020、B021、B022、B023、B024、B026；6 主责为 B020、B021、B022、B023、B024、B026。全部最低验收、合法输入、最小反例、反向与消费者门均须核查。
- [formal-output-identities.json](formal-output-identities.json)、[original-output-identities.json](original-output-identities.json)：11 正式＋5 原稿输出；[scope-amendment-1.json](../author-draft-1/scope-amendment-1.json) 绑定父精确批准的 proposal/patch/before/after。原稿应用只获范围批准；reviewer 仍须检查质量。
- [reading-log.json](../author-draft-1/reading-log.json)、[source-reading-log.json](../author-draft-1/source-reading-log.json)、[registration-collection-comparison.json](../author-draft-1/registration-collection-comparison.json)、[catalog-preservation.json](../author-draft-1/catalog-preservation.json)、[metadata-checks.json](metadata-checks.json)：作者证据，不是独立判定。
- [source-limits.json](source-limits.json)：全部继承限制，含具名未读、条件树果 67、非局部贡献。参考固定为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，只能静态只读；不执行参考、游戏、Ruby、编译、转换、生成、反序列化、行为向量或历史作者/reviewer 程序。可自写 Git/JSON/hash/text 元数据核验。

完整候选 diff 必须用 `git diff --binary --no-ext-diff --no-textconv 1d06c45cc0a744fca181ac80ee573cc9ebb9b862 <CANDIDATE_SHA>` 取得未过滤全流，包括正式、原稿、scope、提案和证据文件。外部完整 diff 身份与独立远端 readback 在最终交付给出，不能用精选目录 diff 代替。

逐项重点：完整 Items 扫描→资格→整阶段异常→无消费/后续阶段；各残余分量资格/最低量/运算顺序及 H11 消费门；全部 A/B/C 族＋身份＋copy 绑定，区分 B 重复出现元数据与最终单个有效行为；默认 Geomancy User0 与局部目标处理器；基础6/机制世代5或8/对应招的宝石门；Bug 开始→步进第二候选→公开基数/允许覆盖门→普通伙伴准备／大会预算、保留、通知。原／净／附表／静态目录相互一致，保留 WP28、WP36、WP46、WP50 和 B15 已接受边界。所有运行观察与执行设计为 0，不能将静态算术签成运行测试。

## 必要 affected 候选任务

完整 potential 列表和精确已接受 reader 输入见 [affected-interface-proposals.json](affected-interface-proposals.json)。这是导航，不自动等于 affected，也没有作者签出的 PASS/NOT_AFFECTED。父任务与独立 reviewer 依据本次完整改动（含新批准的五原稿）作精确判定，仅复核实际改变的接口，不重审整个旧 owner。

| 作者建议重点 | 有界接口与独立待检条件 |
| --- | --- |
| B07 | WP28 主动回复量和人工所选 PP 索引 vs WP51 AI 估量/缺索引资格；合法混列退出不能改变真实手动执行合同 |
| B08 | WP36 force-single/Safari/partner/一员优先及 WP37 覆盖门 vs WP53 单敌/允许覆盖、普通双打／大会预算与通知 |
| B10 | 已接受 WP46 痛楚平分执行 vs AI 比例；真实 loaded OHKOIce 条款门 vs AI 独立冰失败；MH39–44 和原 139＋1 身份保持 |
| B11 | WP50 持有 LEPPA/SITRUS vs 主动资格/AI 估量；共享 combat 目录 AB 全旧行与已接受持有触发保持 |

B02/B03/B04/B09/B14/B15 等其余 potential 导航也须由独立角色给准确版本依据，不能因为作者观察“旧行保持”而自动代签未受影响。B15 WP62/63/64、C122 nil/空串和 C109 最终选定查询不回退。新原稿批准不沿用旧 B11/B15 许可，也不能将本 B12 通过当成 B13、B16、B21 或所有共享根因通过。

## actual 与接受门

候选 FULL 和真正必要 affected 门齐全后，sole A-REG 才可 G。精确 actual G 输入另取当前已接受前驱→actual 和 candidate→actual 两份完整未过滤 diff，分别完成独立 Ultra FULL／必要 affected actual 检查，不能沿用 candidate PASS。全部 actual 门齐全后 root 才 C。

B16 私有准备已完成且不并发写正式文件；B12 C 后父任务须按 [cross-input-report.json](../author-draft-1/cross-input-report.json) 重新冻结五正式 reader 和实际新影响的原稿/caller 输入。canonical 关闭还需所有非局部贡献和最终全局 Ultra，本入口不签任何关闭。
