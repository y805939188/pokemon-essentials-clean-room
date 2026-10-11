# B20 ACT：B01–B19 接受贡献与目录保留的独立有界核验

结论：**PASS_SCOPED_ACTUAL_IDENTITY_AND_CATALOG_PRESERVATION**；保留范围内问题 0。本子审不是 FULL、C 接受或 canonical 关闭。

精确 ACT `6babcf657aef559dbf101aeb093a1beb730ab507`，tree `7f511347be10a55ed1341f4132e198ac6bdedede`；管理包 `66ba31f7895067c9d925aba20ce3de046fbf60e7`，tree `2f30f3ae648c593a32c52e2598a968bf677317ea`。
已审 NEW2 `3f521e6dea0b442e4bb174a9715c458416386b37`，tree `49f406a6de8ca2786e5dda27abada19780fdfa05`；B19 C `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f`，tree `88a400af08253bea8d97ee2ef2fa6636f0900f92`。

固定 NEW2 保留证据：`7c5309763a6cf2e31564a1fe42786ebcbfecbef5:review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-2/b20-r2-preservation.json`，blob `5524083b0bf8e6b0a7aeb485ebbc28c99f520549`，SHA-256 `85ff5a7e8cbacbcadec2c88d2dc1f406d72800f97271b1d7471df93c5eead174`。
完整旧 qualified 哈希证明：`680e3988c4144db269e063971991134b8e0bd678:review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-preservation.json` 的 `/qualified_obligation_identity_by_all216_touched_IDs` 与 `/owners`，blob `3f53b569f69097421a1302df3c66d0388cd0eba2`，SHA-256 `5612de987509aebf71f432f69fc27a9c30c354adfeec5860a33442265d81da42`。这里只引用固定元数据身份，不复制旧正文或完整流。

## 独立保留结果

- ACT 七个 payload 与 NEW2 全部 mode/type/blob、SHA-256、字节数相同。固定 NEW2 的有界语义审查可作为未变内容证据归因，但 candidate 签名没有转签 ACT。
- 308 个唯一 `(owner,ID)` receipt、205 primary、216 touched ID 与原 PLAN 完整键集合相同；旧 receipt 全文件在 C、NEW2、ACT 字节一致。
- 全部 19 owner 的旧证据，共 2757 个 C 中路径，mode/type/blob 在 NEW2、ACT 相同；每个完整 qualified 接受容器保持。B10–B19 的 138 个已审 local-qualified 条件，及全 216 个 original/approved 条件沿用固定独立证明，绑定容器身份已重核。
- 当前完整 control overlay、accepted-interface-map、author-contract 在 ACT 与固定 scope `924c7c3a7a5029b07ad18085cf2dadb594512186` blob相同；scope 仅证明绑定，不构成质量通过。
- 整个共享目录 ACT 与 NEW2 字节相同：214 条 ID occurrence；195 个旧 ID 的原顺序和重复次数完整保留，193 行与 C 字节相同，AN-M23/CV-M18 两 assigned 行保持 NEW2 的固定值。旧 261 行除两行外与 C 完全相同。
- B19 的 17 行、PA040 的 3 行逐个行 SHA-256 与固定旧审证据相同；原 traceability 目标存在且 blob 未变。
- 旧 approval-ledger、traceability-successor、final-integration-review 的 C 全部原始字节在 ACT 中作精确前缀保留；canonical ledger 全 blob 未变。旧 C 无路径删除，既存路径变化精确为七 payload 与三项公共追加记录。

ACT 没携带 NEW2 author-draft 下 75 个候选证据文件；这些均未存在于旧 C。这是 author/independent 报告保留在固定外部提交的整合方式，不构成旧 308 已接受贡献丢失。元数据证明始终以 C 的 2757 owner 证据路径与完整 receipt 容器为基线。

## 每 owner 的保留身份

| owner | contribution / primary | 旧证据文件 | ACT 保留 |
| --- | --- | --- |
| B01 | 14 / 7 | 46 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B02 | 12 / 9 | 66 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B03 | 27 / 19 | 106 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B04 | 35 / 23 | 121 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B05 | 16 / 10 | 76 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B06 | 10 / 7 | 130 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B07 | 19 / 12 | 98 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B08 | 17 / 9 | 187 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B09 | 20 / 13 | 298 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B10 | 7 / 2 | 95 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B11 | 6 / 3 | 142 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B12 | 9 / 6 | 155 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B13 | 8 / 5 | 249 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B14 | 24 / 19 | 247 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B15 | 16 / 10 | 222 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B16 | 24 / 20 | 252 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B17 | 12 / 7 | 83 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B18 | 8 / 5 | 94 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |
| B19 | 24 / 19 | 90 | PASS_SCOPED_ACTUAL_IDENTITY_PRESERVATION |

旧 NEW2 汇总字段将 B10–B19 local-qualified hash 记录数写为158。本次按固定第一 proof 的 owner 数组独立重计138；相应完整接受容器与全部记录仍保持，历史报告原件不改。这是旧元数据计数说明纠正，不构成 ACT 接受贡献损失。

## 支持身份与边界

完整元数据、所有七 payload 的固定 commit/path/blob/SHA-256/bytes、各 owner 接受容器、原公共记录前缀和目录行哈希见 [b20-act-preservation.json](b20-act-preservation.json)。

没有重读未变全库正文，没有复制 full diff，没有执行 reference 游戏、Ruby、编译器、转换器、反序列化器、行为向量或旧执行脚本。只运行新写 Git/JSON/hash/text 元数据核验；runtime observations=0，Demo proof chains=0，静态案例 NOT_EXECUTED。主审另行核全流、scope链、整合接口及所有 owner 真实消费者后出 scoped AFFECTED_ACTUAL 结论。本子审没有修改 repo、正文、main 或参考，没有重签旧 actual，没有签 C 或 canonical 关闭。
