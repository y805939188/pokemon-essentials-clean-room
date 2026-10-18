# R3 最终来源摘要校准候选

本候选基于 `c0f62d973180679134f2eb1a488c1dc359c8658f`，接收固定独立报告 `34202eb7accfee48bb8761db88b340bd77f54a42` 的两项 P3、七行当前来源摘要修正。独立报告已判分类、职责、范围、依赖四 facet 全部736行 PASS、原R2七项问题 PASS；其当前来源校准为729 PASS/7 FAIL。本轮只完成作者修复，七行校准仍须父任务另建真正非作者 ultra/default 复核。

| 根因 | 行 | 当前摘要 |
| --- | --- | --- |
| R3-SOURCE-ATTRIBUTION-001 | 173 | WP26 记录战斗收服存储空操作；回放另按WP58副本、实时依赖及正常终局/中止合同。 |
| 同根 | 227 | WP36 接受负概率/负累加器，整数商向下取整且不钳零。 |
| 同根 | 596 | WP61 Repel 默认首非蛋（含濒死），替代首可战成员。 |
| R3-EV-BOUNDARY-001 | 29/204/456 | HP/攻击255、总量510，超过单项252；HP首项负余量失败，未到总量夹限与本接收者写入。 |
| 同根 | 32 | WP42 外层正常返回及结束通知后复位行走动画状态/转向预锁记录。 |

[逐字段原值/新值及固定源](correction-record.json)绑定七个精确 `differences/1` 指针；主清单其余值全部相等。相应七条单元证据、六份文件级摘要/未来边界、统一补丁七个after值、可复用生成输入及七行当前facet记录同步。[作者精确证明](repair-proof.json)核固定5f单元与文件身份、完整对象/序列化字节重建、历史writer保护及写入范围。生成器仍拒绝对最终清单重跑历史写入步骤。

不可变source/current/upstream、稳定ID、退役体、33metadata、职责、依赖、类别、阶段与未验证状态保留。131文档/87WP、历史2683/当前2704标题、九接受事件及230绑定清零继续核验。原35175归档、原应用回执、R1/R2历史及正式B8工作树原字节保留；当前源只从 `5f87743293290de2e219ecdd6c19e88280f60c9a` Git对象读取。未运行Ruby、参考游戏、业务场景、宿主或四类原型。

静态回归入口为原 `../r3/tools/run-author-checks.py --phase cumulative-source`、`../r3/tools/final-calibration-proof.py --output ...` 与本目录 `check-repair.py`；[后继真实I/O](command-io.json)记录实际命令、UTC、stdout/stderr、exit及输入哈希。原十命令的明细结果仍在 `../r3/tools/actual-command-io.json`。初次环境缺jsonschema的观察和隔离依赖安装与正式回归分开登记，不把准备失败改写为PASS。

[相对c0的精确文件差分](changes-from-c0.json)、[主清单统一diff](manifest-from-c0.diff)、根候选身份表在冻结后写入。自身哈希排除项由最终Git提交绑定，父交接给精确40位SHA，避免未来自身哈希循环。[有界复核入口](review-prompt.md)保留既有PASS信用并复核七行及必要传播。普通push后须全新、无alternates回读远端提交的打标目录全文；不修改原任务分支或main，不force、不merge。

全部736去向仍待验证、阶段待定/未批准、未实现/未验收；框架307/Showdown74/协作130/MZ225/排除0，CLOSED0。目标版本、原型和用户范围/阶段决定由协调任务后续处理。请求gpt-6.1-sol/xhigh/default，实际运行配置缺权威echo，保持UNVERIFIED。
