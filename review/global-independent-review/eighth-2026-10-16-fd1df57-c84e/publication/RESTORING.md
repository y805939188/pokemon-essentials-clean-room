# 恢复大证据

`compressed-artifacts.json`逐项绑定逻辑原path/mode/bytes/SHA256/Git blob与gzip容器的相同身份字段。原始本地文件保留；报告分支发布无损容器，避免重复大JSON和原始工具stdout。失败/中断的原输出同样保留，不删失败记录。

先全文读同目录`restore-packed-evidence.py`。在固定报告commit的checkout运行`python3 <报告根>/publication/restore-packed-evidence.py /workspace/scratch/<全新且不存在的目录>`。helper只校验并恢复惰性证据字节，不执行恢复内容，不覆盖已有目标。恢复后的相对path对应manifest原path；未压缩报告仍从固定checkout读取。复原不是语义阅读或业务运行。

旧历史精确缓存和隔离bare不重复发布。其选择与恢复回执、原commit/blob/transport绑定仍在任务报告；`tasks/history_current/recovery-guide.md`与`tasks/preflight_resources/resource-recovery-selection.json`、`resource-recovery-receipt.json`给准确原来源。按固定对象或已绑定transport恢复，不能假设Mac历史目录在云端存在。

远端读回须同时核发布容器完整字节及恢复后原bytes/SHA256/blob。公开报告投影与平台私有流分列，未发布的私有流不声称已远端读回。`UPDATE_NOT_STARTED`。
