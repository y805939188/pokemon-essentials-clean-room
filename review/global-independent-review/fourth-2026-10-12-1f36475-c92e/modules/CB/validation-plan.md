# CB 执行记录计划

候选事实取证已完成，不追加行为探针。接下来唯一专项执行是本目录产物校验。

- 目的：检查6个输入ID恰有6个裁决、schema及必需字段、证据枚举、10次全131检索、所消费findings冻结身份，以及源码/规格实际阅读路径在读取日志中。不是行为测试。
- 输入：CB的verdicts.json、negative-evidence.json、read-log.json、report.md；固定CB-input-identities.json及M07–M12 findings.json。
- 命令：python3 review/global-independent-review/fourth-2026-10-12-1f36475-c92e/modules/CB/validate_review.py
- 版本：共享baseline报告Python3.14.0；执行中只回显当前Python解释器版本。
- 预期输出：PASS_TOOL_VALIDATION_ONLY及计数；若失败仅修CB产物。
- 副作用：只写CB/validation-result.json及CB/execution.json；不执行或改写R、B，不读取真实存档、不联网。
