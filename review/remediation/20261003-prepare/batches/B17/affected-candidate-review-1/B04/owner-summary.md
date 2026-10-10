# B17 全部 potential owner affected candidate 分结论

本轮 reviewedSHA `86bcafffbb2127c66b8636d10943cf702c18a557`（tree `8626342ceeba125603aca6cac5b86b4e454a8ba0`）；唯一正式 FIX_BASE `f66366b2bbe5c3e1cdd39459f80be672173e7f94`；发布封套 `d0effbf6e7cddb88482658f8c1b7616a9d5b4091`；独立报告分支 `codex/cloud-dot-B17-affected-review-1-20261010`。

**Affected candidate 结果：FAIL_SCOPED（B06 训练家 caller 数据回归）。** 两个最小返修见下；这不是 FULL/actual/C 签名。其它接口的独立有界结论不覆盖该阻塞。

| Owner | 分结论 | 必要 candidate gate |
|---|---|---|
| [B01](../B01/README.md) | NOT_AFFECTED_SUPPORTED | 有据 NOT_AFFECTED |
| [B02](../B02/README.md) | NOT_AFFECTED_SUPPORTED | 有据 NOT_AFFECTED |
| [B03](../B03/README.md) | NOT_AFFECTED_SUPPORTED | 有据 NOT_AFFECTED |
| [B04](../B04/README.md) | PASS_SCOPED | 是 |
| [B05](../B05/README.md) | PASS_SCOPED | 是 |
| [B06](../B06/README.md) | FAIL_SCOPED | 是 |
| [B07](../B07/README.md) | PASS_SCOPED | 是 |
| [B08](../B08/README.md) | NOT_AFFECTED_SUPPORTED | 有据 NOT_AFFECTED |
| [B09](../B09/README.md) | PASS_SCOPED | 是 |
| [B10](../B10/README.md) | NOT_AFFECTED_SUPPORTED | 有据 NOT_AFFECTED |
| [B12](../B12/README.md) | NOT_AFFECTED_SUPPORTED | 有据 NOT_AFFECTED |
| [B13](../B13/README.md) | NOT_AFFECTED_SUPPORTED | 有据 NOT_AFFECTED |
| [B14](../B14/README.md) | NOT_AFFECTED_SUPPORTED | 有据 NOT_AFFECTED |
| [B15](../B15/README.md) | NOT_AFFECTED_SUPPORTED | 有据 NOT_AFFECTED |
| [B16](../B16/README.md) | PASS_SCOPED | 是 |

精确影响导航列15个potential owner；B11没有列入该导航，不伪造其门。作者建议六个必要owner仅作为导航：已独立核查B04/B05/B06/B07/B09/B16，并检验其余九个的真实消费者和条件保持。

1. **B17-AFF-01（B06阻塞）**：WP76 §7.2 名字 `PLAYER1/PLAYER2` 被删为 `PLAYE/PLAYE`。固定静态调用分别创建两原名字；003净化保留必要数据身份。只恢复两个名字，不改参考或其它owner正式文档。
2. **B17-AFF-02（作者/FULL返修交接）**：WP76 §7.4 固定核对行 `R1500/D350` 被删为 `/D350`。恢复 `R1500`、其余公式输出/限定不变；本角色不代签FULL数学门。

共享核验一次通过：完整20文件未过滤流369630字节与独立重建逐字节相同；5 formal+2 originals+13作者证据清单完整。demo旧175/不变174，UI旧484/不变480；B16新24行及264旧贡献统计均逐字节保持；两exact原稿after与获批完整proposal一致。Scope许可不等于质量。

完整流只引用 `d0effbf6e7cddb88482658f8c1b7616a9d5b4091:review/remediation/20261003-prepare/batches/B17/candidate-1/C-to-candidate.full.diff`；blob `fa1d7c2d4255e005b285977e33421903085ee782`；SHA256 `a84c956e06b387ff163cefb8e52459883828336fe0c7f7e6ae98703b30d80343`。此新目录不递归复制流或完整历史控制。

只写15个owner的新报告目录。普通独立分支commit/push和远端ref/tree/所有报告字节读回由发布后结果报告；report SHA不自嵌套。没有formal/public/main/reference/旧报告写入，没有自开任务或其它角色签名。

请求配置：gpt-6.1-sol / ultra / Standard(default)，父线程cloud create已准入；有效回显UNVERIFIED，Plan A不设新配置阻塞。40静态设计未运行；reference/game/Ruby/行为向量/旧脚本执行0，真实Demo链证明0。完整具名限制见 [shared-verification.json](shared-verification.json)。
