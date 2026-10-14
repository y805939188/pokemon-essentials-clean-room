# repair-01 history-payload 分段阅读账本

所有下列范围均从9971固定Git载荷完整呈现，未运行作者脚本。Hash/读取成功不代语义或配置PASS。

| 序号 | 载荷 | 完整读取范围 | 输出 |
| --- | --- | --- | --- |
| 1 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/verify_candidate.py | 1–190 / 190 | read-001.stdout.txt |
| 2 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/bind_history.py | 1–103 / 103 | read-002.stdout.txt |
| 3 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/edit_candidate.py | 1–76 / 129 | read-003.stdout.txt |
| 4 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/edit_candidate.py | 77–129 / 129 | read-004.stdout.txt |
| 5 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/repair-01/check_repair.py | 1–81 / 81 | read-005.stdout.txt |
| 6 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/repair-01/report.md | 1–26 / 26 | read-006.stdout.txt |
| 7 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/repair-01/r5-path-recovery.json | 1–97 / 97 | read-007.stdout.txt |
| 8 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/repair-01/conversion-controls.json | 1–49 / 49 | read-008.stdout.txt |
| 9 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/repair-01/checks.json | 1–170 / 170 | read-009.stdout.txt |
| 10 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/repair-01/delta-manifest.json | 1–215 / 215 | read-010.stdout.txt |
| 11 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/author-report.md | 1–32 / 32 | read-011.stdout.txt |
| 12 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/tool-validation.json | 1–555 / 555 | read-012.stdout.txt |
| 13 | review/remediation-sixth-20261014-prepare/candidates/R6-U13/evidence/repair-01/remote-readback.json | 1–362 / 362 | read-013.stdout.txt |

补充差量读取：metadata-delta.json记录candidate-manifest、changed-spans、per-id-verification、historical-regression全部变更字段及作者ledger新增三行；原相同范围只身份复绑，旧完整阅读不冒称本次重复。该差量工具的内容输出保留于平台回显，未倒补额外实际UTC。

peer receipt：/root/recording_save确认fixedR原Conversion223及SaveConversions420语义范围，未扩成当前宿主运行；父审独立远端回读9971全部30载荷单列。

独立工具首轮exit1与修正后exit0都有保存的实际UTC/stdout/stderr/exit，失败未删除。
