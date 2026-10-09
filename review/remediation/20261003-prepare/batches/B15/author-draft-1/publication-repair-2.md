# 两项修复完整候选与增量复审发布

正式 FIX_BASE `0cfe99094b76f8d75fded0d638694677855a5f0c`；派发管理提交 `4cb51a33402ec6559a396226239afe308a4b8849` 不作基线。旧 FULL/affected 审查候选 `cc08a9150131b7e9fae8424fb0ede890169dd64f`。当前完整候选 `6cd88996e5d48bffb1e85fd4bdaa87bed2d0a1d4`，tree `84f365fda7c4aea421a21297f7f6a6fb2f77d331`，分支 `codex/cloud-dot-B15-author-1-20261009`。九正式输出、16贡献/10主责以及完整变更身份在 publication-receipt-repair-2.json。父批准只限定原稿修改范围，不表示质量通过。

相对旧审查版本，仅四正式路径、六静态行（PD32/PD33、W32/W33、两版P33）和原稿分配给 C109 的 §8 区域失败一句改变。C122 明确原始/本地化 nil 与存在空串的邻近反向；C109 明确最终实际查询区域，补齐两失败／两成功反向及原稿同一条件句。两个精确原稿补丁已核验批准 blob、SHA-256、before/after 并应用，冻结提案保持历史字节。

三份正确净化正文整体字节不变；正确 WP62 §6.1 两版不变、净化 WP63 §3.1/§8 不变。其余14贡献控制、正文、静态设计流不变，仅对应IO身份刷新。2995旧行与2907其他owner行保留ID/顺序/重复；本轮不增加行ID，43新增设计数仍为43。精确七行与18目录保护证明见 ../candidate-1/combined-repair-delta-and-protection.json。以上属于作者静态及元数据证据。

old-FULL-to-candidate-repair-2.diff 是旧 `cc08a9150131b7e9fae8424fb0ede890169dd64f` 到新 `6cd88996e5d48bffb1e85fd4bdaa87bed2d0a1d4` 的完整未过滤原始Git diff；complete-candidate-repair-2.diff 是正式基线到新候选的完整未过滤diff。formal-repair-2-delta.diff 仅用于四路径导航，不能替代完整diff。三份diff均含准确命令、SHA-256、bytes并与独立远端对象生成结果一致；原始diff中的空白上下文保持Git输出，不规范化档案内容。

普通push后，全新bare独立网络fetch验证ref/FETCH_HEAD/tree、直接父提交、全部49个基线变更输出字节与33个旧FULL增量路径。无共享对象或alternates。报告后继仅增加这三份diff及当前receipt/md；其完整SHA另行返回，不改候选包或正式输出。

由父统筹让两个原reviewer并行有界增量复核：FULL审C122静态前提／反向及新diff回归；affected审B03 C109含原稿§8及nil增量接口。旧FULL 15条本地PASS与九affected状态只属于旧版本，须由独立reviewer核对delta后绑定新SHA，作者不转签。无需新全量历史审计。未来A-REG唯一整合与actual独立门仍分开待办，作者未派任务或替代review。

运行、向量执行、demo链证明、参考执行均0；U01–U10/G01–G12/AX01–AX20及具名未证限制保留。请求review Ultra，可信后端参数按批准Plan A仍UNVERIFIED，不探测或降级。无公共登记/B16/参考写入、main合并或force push；作者写入阻塞为空。
