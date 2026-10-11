# main 合并准备：保留历史，不执行

核验时远端 main 为 `e1e01bb18d824931e54f182dd61af5a9f908ba85`，tree `55f14565695a857c842cb55c711ce38cbb530811`。它是最终实际、FINAL-2 以及本交付分支的祖先；main 没有相对于已审最终链的独立提交。当前发布不会移动 main。

交付分支 `codex/cloud-dot-delivery-ready-20261011` 从 FINAL-2 报告 `ed9ff08085837960f1d940ae5d47faca385982c7` 出发。新增报告／导航提交保留 FINAL-1 `c2bc1a341ba6acdf7c8c111dc88d39a162a093d6` 和原全局报告 `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 为额外父：完整历史仍可达，不 squash、不重基、不 cherry-pick 代替原提交。

该提交的树采用明确保全范围：保留 FINAL-2 基树的全部 mode/type/blob，仅引入 8 个 FINAL-1 完整原输出、原全局 findings／final-report 两份原字节和新增交付导航；根 README 从空文件写为入口。原全局报告其他附件留在其固定历史树内，并非从原树删除。正式规格、取证原稿、公共关闭登记、旧证据、AGENTS 保持最终实际字节，参考无写入。

FINAL-2 与 FINAL-1 的 `git merge-tree --write-tree` 试合并无冲突，合并树为 `374d37db8bbdf664b5a404fd89689540fca95afb`。原全局两文件在 FINAL-2 树中不存在，以原 blob 新增，没有覆盖现有文件。交付元数据的核验记录见 [merge-plan.json](merge-plan.json) 和 [validation-results.json](validation-results.json)；完整 main→交付路径与计数由 JSON 记录，不把数量当质量结论。

## 后续实施步骤

1. 父任务实施合并前重新读取远端 main 和交付分支的**精确 SHA/tree**。确认 main 仍为上述固定值；若发生漂移，先检查新增提交、祖先和范围，定点解决实际冲突并更新计划，不 force 覆盖。
2. 比较交付树与已审最终实际：正式规格／specs／公共冻结文件字节一致，两次 FINAL 报告和原全局入口身份一致，当前摘要 21/341/229 CLOSED/0 OPEN 与原限定一致。导航的新字节属于交付元数据，不冒充 FINAL-2 已审规格。
3. 在独立 main 工作树使用 `git merge --ff-only <固定交付SHA>`，随后普通推送；因为 main 是祖先，保留全部既有提交和报告合并父链。若仓库要求 PR，则从此分支创建 PR，采用保留提交历史的 merge 方式；不得 squash/rebase 或 force push。
4. 推送后读回 main SHA/tree、交付入口、正式规格身份和报告身份，再同步本地项目。同步应采用普通 fetch/merge，先保存任何新的本地修订；不擅自 reset 或覆盖本地状态。本轮已知本地停写回执保持，不重新索要离线证明。
5. 第三轮使用独立新会话和固定基线开展**只评审**，用户看报告后决定下一轮更新。分支与重复内容清理按下述清单另做可追溯处理，不绑成合并质量前置无限审计。

main 已固定的情形下未发现实质内容冲突。本次只发布可审阅分支及计划；合并由父任务依用户后续要求协调。Git CLI 凭据失效时继续使用既有授权 GitHub App，不创建或配置新凭据。
