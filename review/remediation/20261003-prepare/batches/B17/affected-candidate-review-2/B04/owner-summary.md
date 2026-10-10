# B17 NEW affected candidate 独立增量复核

**PASS_SCOPED**。reviewedSHA `19095065e39481e408b40a2ca01e5a4660a320c9`；tree `d9ca0072aaaa6773983bcd09bbb7d1886ab1fb0f`；OLD `86bcafffbb2127c66b8636d10943cf702c18a557`。旧affected报告 `8610526b5079f06f7ea9701f0f5bbd24dfec317f` 不变，旧FAIL不自动改签。

B06原阻塞B17-AFF-01解除：第165行PLAYER1/PLAYER2恢复，固定静态caller及其它输入条件一致。B17-AFF-02第185行双方R1500/D350、σ＝0.9明确输入恢复；只签返修事实与affected范围，FULL门不代签。

| Owner | NEW独立分结论 |
|---|---|
| [B01](../B01/README.md) | NOT_AFFECTED_SUPPORTED |
| [B02](../B02/README.md) | NOT_AFFECTED_SUPPORTED |
| [B03](../B03/README.md) | NOT_AFFECTED_SUPPORTED |
| [B04](../B04/README.md) | PASS_SCOPED |
| [B05](../B05/README.md) | PASS_SCOPED |
| [B06](../B06/README.md) | PASS_SCOPED |
| [B07](../B07/README.md) | PASS_SCOPED |
| [B08](../B08/README.md) | NOT_AFFECTED_SUPPORTED |
| [B09](../B09/README.md) | PASS_SCOPED |
| [B10](../B10/README.md) | NOT_AFFECTED_SUPPORTED |
| [B12](../B12/README.md) | NOT_AFFECTED_SUPPORTED |
| [B13](../B13/README.md) | NOT_AFFECTED_SUPPORTED |
| [B14](../B14/README.md) | NOT_AFFECTED_SUPPORTED |
| [B15](../B15/README.md) | NOT_AFFECTED_SUPPORTED |
| [B16](../B16/README.md) | PASS_SCOPED |

完整OLD→NEW三文件流独立重建一致：39479字节，blob `483c0925b44a2a8523db056794474a9209429bce`，SHA256 `b696d08a3ab5c7d7f6233a9eea5568f40f10c4505627a6b1dd0ade4ff8d07d1a`。精确不可变位置：`c52d727da6ab7ae3f519f0040a26eb2f305527cf:review/remediation/20261003-prepare/batches/B17/candidate-2/OLD-to-NEW.full.diff`。不递归复制流。

只两行恢复、+9字节；36613其它旧路径mode/blob保持。两目录/两原稿/40设计完整字节不变；B16 24行与264贡献统计再次核验。15owner原接受输入逐owner保护并据caller条件独立判断，没有自动转签。

剩余affected阻塞：无。最小返修：无。后续FULL、sole registrar和separate actual/G/ACT/C职责仍保留，未签署或自开任务。

报告普通独立分支：`codex/cloud-dot-B17-affected-review-2-20261010`。只新增affected-candidate-review-2/<owner>/；发布后远端ref/tree及全部报告字节独立读回结果由最终回执提供。

请求ultra/Standard，gpt-6.1-sol，Plan A继续；可信有效回显UNVERIFIED，无认证新增门。未执行reference/game/Ruby/向量/旧程序。完整限制见[shared-verification.json](shared-verification.json)。
