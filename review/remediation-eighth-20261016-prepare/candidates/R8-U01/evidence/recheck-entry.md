# R8-U01-REVIEW-LOC-01 原审者复核入口

原独立报告固定于 `1a5c6dab85b6638403ef6e42bc97f23e842580b1`：`review/remediation-eighth-20261016-prepare/independent-reviews/R8-U01/cloud-independent-20261017/report.md`，12239 bytes / SHA256 `002448cc6afa3f0cb20ecfc1694aa56b92450f2ef7298bfb18b6137c84f1d1d7`。已完整读取。三项语义PASS、完整交接证据FAIL的原判定保留；本修订作者不承担正式复核或关闭。

对比基准为被审完整候选 `bce1659e01ca33ecafb91464ce1ada32c0499faf`，继续使用分支 `revision/r8-u01-20261017`，最终后继SHA由父任务发布入口绑定。全部改动限本批独占 evidence，四个 mirror 和原13个静态场景均保持相同 mode/blob/bytes/SHA。原作者输入、B8、参考身份及已选可选范围不变。

本次精确定位差异仅两对象共六字段，见 [recheck-location-fix.diff](recheck-location-fix.diff) 和 [recheck-binding.json](recheck-binding.json)：

- `remediation-record.json /records/1/change_locations/0`：line 33 → 102；locator 扩为 `| 启动读取 | 先检查默认主档：`。
- `tagging-handoff.json /changes/4`：相同行号/locator；section 改 `4.1 启动阶段表`，anchor 改 `#41-启动阶段表`。

原生成器对短前缀取首个匹配而误中登记说明。新的 [refresh-locations.py](refresh-locations.py) 对每个locator要求唯一匹配，统一重算两记录的8个位置与tagging章节/锚点；另核每处确属作者实际diff、四mirror与原被审字节相同。原短前缀在L33/L102有两个命中，负向控制明确拒绝，不再静默选择第一处。全部8处已核，原其它7处未变，结果为 [location-validation.json](location-validation.json)。这只是文档工具核验，业务执行仍NOT_EXECUTED。

原审者请核两份完整JSON中的变更对象及其余保留，对照WP09全文的L97标题/L102规则、原完整合同和真实diff；核其余7处及四mirror身份未变。可执行文档核验入口：

```sh
python review/remediation-eighth-20261016-prepare/candidates/R8-U01/evidence/refresh-locations.py
```

该命令无 `--write` 时只读核对已有两份定位，不写任何文件；`--write` 才更新两记录及独占定位核验报告。审者仍须独立检查事实，不能以工具输出代替实际复核。

旧 `candidate-manifest.json` 只绑定四mirror，旧 `remote-readback.json` 明确绑定原提交，不改写成新候选传输证据。新SHA的普通push和独立远端回读由发布时另行绑定。完整交接证据PASS由原独立ultra审者复核后决定；actual integrated PASS、ACCEPTED、CLOSED仍未授予。
