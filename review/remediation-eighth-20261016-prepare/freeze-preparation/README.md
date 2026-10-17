> 本目录为c0f待复审阶段的历史准备与机械证据；当前整体验收状态从[候选交付](../DELIVERY.md)及真实后继冻结manifest读取。下文保留原时点。

# 待冻结整体验收输入准备

状态为 `NOT_FROZEN_DO_NOT_START_REVIEW`。29必改、10选入可选、9批已接受；CLOSED仍0。本文不是最终交付或独立复审结果。

[组装计划](assembly-plan.json)列出尚需完成的门、最终载荷范围和真实artifact/后继input-binding两阶段绑定步骤。[输入模板](../coordination/final-review-input.template.json)已解析九批真实候选入口；[54项来源引用核对](source-reference-checks.json)确认入口、候选/实际独立报告及批次回执可在固定提交读取，并与准备基线5b35018e的完整字节一致。此核对不增加语义阅读或独立票数。

父任务已将[R3累计打标候选](https://github.com/y805939188/pokemon-essentials-clean-room/blob/c0f62d973180679134f2eb1a488c1dc359c8658f/planning/implementation-routing/r8-20261017/revisions/r3/README.md)交原ultra/default独立审者复核，结果未收到。[候选接收记录](../coordination/tagging-R3-candidate-reception.json)分开记录作者声明、机械核验和待定独立门；[159文件身份索引](prospective-R3-file-identities.json)覆盖完整38,327,011字节，并核对作者158项载荷清单与清单自身Git身份。这里仅保存身份，没有把候选正文或标签导入正式打标路径。

收到明确绑定该候选及最终5f来源的独立PASS后，才可按固定路径整合打标及实际报告、完成交接和最终报告，再产生真实冻结输入。打标候选的工作树仍为B8，导入必须限定经复审的打标前缀，保留当前已接受5f正式树。去向、原型、阶段批准、实现和未来验收的待验证状态继续保留。

收尾基准见[只读预检](../cleanup-preflight/snapshot-20261017-162220Z/README.md)，新增R3与整改分支的推进见[漂移补充](../cleanup-preflight/R3-pending-ref-drift.json)。原快照不改写；实际合并与清理前仍须按最终头重新盘点。未合并main、创建归档标签、删除分支或操作用户本地。
