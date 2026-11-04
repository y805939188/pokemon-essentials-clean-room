# 历史会话材料

这些文件用于 2026 年 9–10 月不同 AI 会话之间恢复上下文，已由后续规格、实际审查和 R8 关闭记录取代。它们不再作为开工入口。

本次整理删除了三套 reviewer 运输包中 **96 份完全重复的快照**（1,662,540 字节）；每份都在当前仓库保留了 Git blob 相同的另一份副本。**21 份含独有文字或元数据的交接文件仅迁到此处，字节未改**。逐文件原路径、blob、SHA-256、现路径或相同副本位置见 [清单](inventory.json)。实际独立审查报告、原问题、接收/关闭记录和来源证据没有删除。

这些迁入件是历史原件，不是重新生效的任务、授权、当前状态或质量结论。其正文链接、绝对本机路径和 JSON/TSV 中的路径均保留原语境；**完整浏览历史包请使用下面的固定提交入口**，不要把它们在本目录下的相对路径当作新的审查输入。

| 历史包 | 完整原树 |
| --- | --- |
| 2026-09-19 reviewer | [固定原包](https://github.com/y805939188/pokemon-essentials-clean-room/tree/5c9805de2331f75565891851d4d7b2bc97acad94/review/reviewer-handoff-2026-09-19) |
| 2026-09-22 reviewer | [固定原包](https://github.com/y805939188/pokemon-essentials-clean-room/tree/5c9805de2331f75565891851d4d7b2bc97acad94/review/reviewer-handoff-2026-09-22) |
| 2026-09-23 reviewer | [固定原包](https://github.com/y805939188/pokemon-essentials-clean-room/tree/5c9805de2331f75565891851d4d7b2bc97acad94/review/reviewer-handoff-2026-09-23) |
| 根目录及提取员旧交接 | [整理前完整目录](https://github.com/y805939188/pokemon-essentials-clean-room/tree/5c9805de2331f75565891851d4d7b2bc97acad94)；具体原路径见清单 |

有包含原提交对象的本地仓库时，可读单文件：

```sh
git show 5c9805de2331f75565891851d4d7b2bc97acad94:<原路径>
```

需要完整恢复旧运输包时，在另一个独立工作树中执行：

```sh
git restore --source=5c9805de2331f75565891851d4d7b2bc97acad94 -- review/reviewer-handoff-2026-09-19
```

没有改写历史、清理 Git 对象或删除标签。历史索引中的原路径与哈希仍指其原时点；当前开发从[正式规格](../../deliverables/final-specification-set/README.md)和[当前交付](../../CURRENT-DELIVERY.md)开始。

仍保留的非正式材料有明确用途：`specs/` 原稿和 `audit/source-traceability.md` 承担追溯；`planning/` 承担覆盖、依赖、去向和路线；`review/` 与 `delivery/` 保留实际审查及限定结论。`handoff/cloud-dot-20261009/` 含独有保全/出处/未发布准备记录，`review/local-handoff-2026-09-19/` 有四份在其他当前路径找不到完全相同字节的快照，本次均保留。R8 的 `development-handoff.md` 和 `known-limits.md` 仍是当前接收链与限制说明，也保留。

这是一轮文档整理，不增加游戏、Ruby、宿主、媒体、存档/回放或目标兼容的验证结论。现有 6.3 GB 审查历史中仍有唯一证据和版本身份，未按文件名批量删除；本次也不会缩小 Git 历史或完整克隆的下载量。

整理验证：96 份删除件均有保留位置、相同 Git blob 和 SHA-256；21 份迁入件的 blob/SHA-256 均未改变；131 份正式文档仍齐全，其中 130 份原字节不变，正式 README 的原内容完整保留在新增导航之后。扫描 16,044 份继续使用的 Markdown，未发现本次操作新增的相对文件/目录链接失效；历史原件的路径语境按上文固定原树恢复。其他原有受追踪文件均未改变，用户原 checkout 的 `main` 和未跟踪 `investigations/` 保持原状；`git diff --cached --check` 通过。
