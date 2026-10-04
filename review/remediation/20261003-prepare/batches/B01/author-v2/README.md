# B01 v2 作者候选交接

状态：**AUTHOR_CANDIDATE_PENDING_FRESH_INDEPENDENT_ULTRA**。收到父任务两份原规格的最小扩围授权后，同步 GIR-FD82-A001／A002／A004／A009；其余贡献沿用旧作者候选，当前全部待针对新冻结 SHA 的独立 Ultra／Standard 复审。

- RUN_ID：20261003-prepare；分支：remediation/20261003-prepare/batch-B01。
- 本次追加提交的唯一父提交／旧未审候选：e6f14de7d0d9600ce0e058c1bd05b9348f7a06d3。
- 完整复审差异基线 PRE0：8f3a811855fc43b5fe5eb7809931b4e1749200de；增量差异基线为旧未审候选。
- REVIEW_BASE：e1e01bb18d824931e54f182dd61af5a9f908ba85；REVIEW_REPORT：93e10babe0b9c9ef8b3f5277754541b447beeeb4。
- FIX_BASE／固定方案：41fffb540c6483f5296ea0d33b789b75180d27ed；参考固定提交：8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b。

完整正式差异为八份文件；本次仅增改两份原规格与新的版本交接。既有六份最终规格／目录、全部旧 author 文件、PRE0 四份材料、冻结方案与历史审查／批准逐字保留。原规格头部 Reviewed 和历史状态段只描述旧被审版本，不批准此次新增字节；当前 v2 仍待独立复审。

- [scope.json](scope.json)、[范围修订01](../scope-amendment-01.md)：两条新增路径、限定条款、授权与依赖。
- [author-response.md](author-response.md)、[finding-responses.json](finding-responses.json)、[candidate-ledger.tsv](candidate-ledger.tsv)：14贡献／7主责，四项本轮同步；其他10响应对象沿用旧候选，全为 OPEN。
- [static-vectors.json](static-vectors.json)、[source-reading-log.tsv](source-reading-log.tsv)：31条最终目录静态向量保留，原规格11条关联场景（含三个保留的引号对照）、本增量新增六条原规格场景，最终 ID 新增0。
- [registry-proposals.json](registry-proposals.json)、[scope-conflicts.md](scope-conflicts.md)：当前内容身份/追溯的后继建议，其他跨批范围继续保持；没有正式公共登记更新。
- [candidate-manifest.json](candidate-manifest.json)、[formal-diff.patch](formal-diff.patch)、[incremental-formal-diff.patch](incremental-formal-diff.patch)、[validation-results.json](validation-results.json)：完整八文件与增量两文件实际差异、内容哈希及作者结构检查。

原报告完整对象和阅读证据复用冻结旧材料：[原14对象](../author/original-findings.json)、[全部2538叶引用](../author/reading-leaf-references.json)、[573叶值](../author/reading-leaf-values.jsonl)。[旧后继勘误](../author/historical-errata.md) 保留其时点；[旧作者回应](../author/author-response.md) 仅作历史记录，本轮四项原规格完成情况以 v2 为准。

明确请求仍为 gpt-6.1-sol／Max／Standard(default)，没有 Max 不支持证据，未使用 xhigh 或改配置。实际生效模型、推理与速度 **UNVERIFIED**，继承用户已批准的方案A披露；不以自述替代平台证据，不读认证、令牌或 /root/.codex/sessions。独立复审应由父任务另行指派 Ultra／Standard，本作者没有派生任务、自审通过、整合或关闭 finding。

只运行自有文本／JSON／Git结构核验。参考、游戏、编译、生成、转换、反序列化、模拟器与求解器执行次数均0；运行观察与真实Demo链均0；U01–U10、G01–G12、AX01–AX20及其他未知保持。integration 停在 PRE0、main 停在 REVIEW_BASE。

复审命令：`git diff 8f3a811855fc43b5fe5eb7809931b4e1749200de <new-full-candidate-SHA>` 核对完整候选；`git diff e6f14de7d0d9600ce0e058c1bd05b9348f7a06d3 <new-full-candidate-SHA>` 核对本次授权增量。新候选完整 SHA 必须取提交推送后独立 publication receipt。
