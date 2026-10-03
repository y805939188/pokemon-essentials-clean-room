# GROUP1-C02 最后一个字段更正

在 `/Users/dingshinn/Desktop/pokemon-framework-reference` 工作。先读本目录report.md／findings.json／checks.json与AGENTS。

本次收尾核验其余均通过，原29项与GROUP1-C01均保持CLOSED。只修改：

`review/wp66a-wp63-wp64-delivery-2026-10-01/registration-final-checks.json`

找到 rounds 中 round=80 的记录，将 `drift_vs_recheck_v3_inputs` 的值改为 **4**（可在同一字符串中注明基线为 `review/wp66a-wp63-wp64-recheck-v3-2026-10-01/inputs.json`）。14只属于v2基线 `review/wp66a-wp63-wp64-recheck-2026-10-01/inputs.json`，原具名勘误及历史轮次记录保持不变。不要把其它正确的14改成4。

该文件按既有约定不注册到manifest／主TSV，且现有最终身份集合不包含它自身，因此无需新登记轮次，无需新建修订版本目录；不要改主稿、fixed、自检、组摘要、manifest／TSV或旧审查材料，也不要重写已经正确的新收尾最终检查C7。

改后只读复测两个基线的完整漂移路径集合（v2=14，v3=4），确认两份最终检查引用的manifest／TSV／摘要身份仍匹配，三份主稿及固定／自检文件不变。完成后报告并停在收尾核验，不自行CLOSED，不开GR整改或新WP；核验通过后再按用户安排进入GR-001～016有界整改。

reference只读，不执行参考实现／游戏／网络；不创建任务／Agent、不发跨会话消息、不提交／推送。
