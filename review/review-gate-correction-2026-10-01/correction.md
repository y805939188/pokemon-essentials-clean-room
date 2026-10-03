# 推进结论更正：发现问题先修复，再进入下一步

2026-10-01，依据用户澄清。此前将“完成全部WP后整体double review”理解为“已发现问题也可以留到以后修”，属于误解。

**当前推进结论更正为 REQUEST_CHANGES — DO_NOT_START_NEXT_BATCH。WP65／WP67-A／WP67-B不得开始。** 应先修复已确认问题并作定点复审；全部内容包完成后再做整体double review，寻找此前未发现的遗漏。

## 当前已确认问题

| 范围 | P2 | P3 | 合计 |
| --- | ---: | ---: | ---: |
| WP66-A | 9 | 3 | 12 |
| WP63 | 7 | 3 | 10 |
| WP64 | 5 | 2 | 7 |
| 第一组合计 | 21 | 8 | 29 |

此外，较早的GR-001～016仍为已知待修问题。它们不属于以后double review再发现的问题；须另行有界修订／复审，不能把已确认项延期视为放行依据。当前先交接第一组三包29项，避免把所有旧包混入同一次修订。

详细事实、来源和最小场景仍以两份原审查的findings.json为准：

- [WP66-A问题](../wp66a-progress-review-2026-10-01/findings.json)
- [WP63／WP64问题](../wp63-wp64-progress-review-2026-10-01/findings.json)
- [当前已知问题台账](issue-ledger.json)

## 覆盖哪些旧建议

两次进度审查中的CONTINUE_WITH_DEFERRED_FINDINGS、可以直接进入下一组、问题留待统一修订等推进建议均撤回。旧报告的静态发现与证据保持有效，旧原件不回写。

以下旧执行提示不再作为开工授权：coverage-first-handoff-2026-10-01/prompt.md、wp66a-progress-review-2026-10-01/next-task-prompt.md、wp63-wp64-progress-review-2026-10-01/next-task-prompt.md。当前改用[第一组修订提示](repair-prompt.md)，并遵守extraction-plan §2.2。

本更正不代表问题已修复或关闭，也不重开N01已通过范围；管理性回填、B批整合仍须如实登记。当前修改仅为推进计划、补充决定、交接材料及必要行政登记；未改规格正文，未执行新包提取。
