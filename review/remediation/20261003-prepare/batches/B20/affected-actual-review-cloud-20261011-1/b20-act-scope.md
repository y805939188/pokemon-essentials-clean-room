# B20 ACT：scope 授权链、G 登记与 actual 管理绑定独立核验

结论：**PASS_STATIC_SCOPE_AND_INTEGRATION_BINDINGS，剩余阻塞0**。这是独立 affected actual 复审中的管理与范围子任务判断；不替代 owner 消费接口语义判断、不签 FULL、不签正式 C、不关闭 canonical。

精确 reviewed ACT：`6babcf657aef559dbf101aeb093a1beb730ab507`，tree `7f511347be10a55ed1341f4132e198ac6bdedede`。固定管理包 M：`66ba31f7895067c9d925aba20ce3de046fbf60e7`，tree `2f30f3ae648c593a32c52e2598a968bf677317ea`。唯一 G：`405d7884058d30d94655be0b75f8f12eb07a15d9`，tree `31ed364e0d9617c1f126019476be9f768594e947`。ACT 的直接父为 G，G 的直接父为 `924c7c3a7a5029b07ad18085cf2dadb594512186`。

固定 C 仍是 `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f`。已审 NEW2 为 `3f521e6dea0b442e4bb174a9715c458416386b37` / tree `49f406a6de8ca2786e5dda27abada19780fdfa05`；七 payload 在 ACT 与 NEW2 的完整字节、blob、SHA256 和长度逐一相同，G→ACT 完整路径集合恰为这七项。原 scope 链和管理差异实际核验如下。

- 最初六项管理 slice 没有开始、没有完成产物。`669997ac28258f26d0bafc81b1d081abb407a3a1` 的 `refreeze-after-B19-C-1/previous-scope-supersession.json:11,13` 明示以19贡献/15主责的完整 refreeze 替代旧依赖 hold 与单 WP74 写权限。当前合同最初只授权四个 formal/catalog 路径，原稿写权限为空；完整 qualified obligation 并未缩减到旧六项。
- `d54fba72a75a3324d7a3daf8e02bc1ecf6c8beeb` 的 `original-scope-grant-1/scope-receipt.json#/granted_files` 精确授权 WP74/WP75/WP77 三原稿的13/4/2个 hunk。逐个独立验证 C 全 before、固定 proposal 完整 after、原 NEW 全 after，以及十九个 literal-before/literal-after/complete-hunk 哈希；全部一致。该 receipt 的2393行明确 scope permission 不是质量证据。
- `924c7c3a7a5029b07ad18085cf2dadb594512186` 的 `candidate-fix-1-original-scope-grant-1/scope-receipt.json:29,288,293,311` 只追加授权 WP75 一个、WP77 两个 hunk。独立验证旧 NEW/BASE 完整 before、固定 repair proposal 完整 after、NEW2 完整 after，三组字面范围和 hunk 哈希全部一致；未把第一轮十九 hunk 隐式扩成新许可。WP74 在第二轮未变，ACT 三原稿仍等于相应最终 after。C→ACT 的原稿变化集合也只有这三项，架构003清理未获授权亦未因此扩展。
- G→ACT 只复制七个完整 payload；924→G 则只修改三个公开登记文件并新增十个 integration 管理文件。管理新增文件不能凭“管理”标签自动判无害：本次实核了十九 record 的 original/approved 完整对象哈希、qualified control pointer、候选 FULL 逐 ID pointer、owner accepted/remaining contributor 列表、固定候选报告与 published readback 身份以及 source limits 路由。没有仅按标题、局部例子或 scope receipt 判质量通过。

`integration-stage-1/finding-registration.json#/records` 恰19条、15 primary/4 shared，各条的 canonical_state 保持 OPEN，actual_gate 保持精确 ACT 的 FULL19/15 和 bounded all19 affected 待审，C 与 canonical_closure 为 NOT_PERFORMED。该文件第一条相应字段在84–86行，其余十八条精确行号在伴随 JSON `/field_line_anchors`。其 complete_control_records、whole original/approved object 和 FULL contribution 指针均可达且身份匹配；全部十九完整原对象/批准对象重算的规范 JSON SHA256 与 control overlay/登记一致，accepted 与 pending contributor 数组也与整个 qualified record 一致。overlay 在 refreeze、两次 scope、G 与 ACT 的完整 blob 不变，完整 root/extension/effective-case/premise/minimum-revision/determinate-recheck/nonlocal obligation 并未因为整合而被缩减。

候选 FULL 与 affected 的固定报告分别归属 `2d854ca5462876156d371554c56fd51b0003a472`、`7c5309763a6cf2e31564a1fe42786ebcbfecbef5`，绑定同一 NEW2/tree、候选0阻塞；`candidate-gate-receipts.json:65,69` 明示 candidate 不等于 actual 或 C。这里只核 attribution 和固定身份，不把旧候选签名平移为新的 actual 签名。缺失的 FULL 对象曾通过授权公共 Git remote 读到隔离 `/tmp/b20-act-scope-external.git`；主 checkout 后亦可读同固定对象，过程未改报告分支或正文。

公开 `approval-ledger.tsv` 和 `traceability-successor.tsv` 的 C 完整文件各309行（header+308 record）仍是 ACT 的逐字节原始前缀。两者只在 ACT 310–328行各追加相同十九 B20 pending ID，15 primary/4 shared；旧308 contribution 没有覆盖重签。`final-integration-review.md` 的 C 完整文件597行亦逐字节保留，只在598–601行追加 G 总述。逐个 TSV 新行中的 whole qualified control、G record pointer、accepted/remaining contributors、candidate identities、NOT_EXECUTED case 身份全部与相应 G record 一致；虽列名含 accepted，新增值实际为 G_INTEGRATED_PENDING 或 PRIMARY/SHARED_PENDING，没有生成 B20 C。canonical `finding-ledger.tsv` 的 C→ACT 完整 blob/字节不变：229 OPEN、0 CLOSED。

M 的 `actual-freeze-1/public-registration-actual-binding.json:2–3,65` 将三个 public file 的 G placeholder 外部绑定到上述精确 ACT/tree，不修改这些 public 文件、不执行接受；其完整 ACT file 身份、旧 C 前缀 SHA256/长度与实际 Git bytes 独立一致。不能把管理包 M 当成 reviewed ACT，也不能把任一候选或 G commit 误当正式 C。

旧 B10–B19 的 `acceptance-stage-1/contribution-acceptance.json#/records` 实际长度为7/6/9/8/24/16/24/12/8/24，总和 **138**；十份完整 C 文件在 ACT 全部字节与 blob 原样保留。历史摘要的 **158** 是计数差错，不能据此推断 ACT 丢失20个贡献，也不改变固定308 owner/ID接受键。精确逐文件身份与数组长度在伴随 JSON `/B10_B19_original_local_arrays`。

source-limits 从 NEW2 修复完成包指向原完整 prior/repair limits；G/M均保持 U01–U10、G01–G12、AX01–AX20及 host/media/plugin/unread/conditional 等限制，没有声明新运行、Demo 或数据覆盖。所有静态案例为 NOT_EXECUTED；runtime observations=0、proven Demo chains=0。只使用自己新写的 Git/JSON/hash/text 元数据核验，未执行参考游戏、Ruby、编译器、转换器、反序列化器、行为向量或旧脚本。未改 repo 正文、原稿、main、reference、旧报告或接受证据。

独立元数据结果：763个检查，255个唯一固定文件身份，535次固定引用核对，140个唯一 JSON pointer，可达/身份/对象哈希/登记一致检查全部通过。完整C→ACT/NEW2→ACT差异由 root 统一独立重建后引用，本文不复制任何差异流或历史正文。所有身份、具体行/JSON pointer、前缀与增量摘要、七 payload、scope hunk 范围哈希和无阻塞结果见 [b20-act-scope.json](b20-act-scope.json)。

下表为关键入口证据的固定完整身份；路径均是仓库绝对相对路径，范围子任务可复核，不以作者断言或登记许可代替质量。

| commit | 路径 | Git blob | SHA256 | 字节 |
| --- | --- | --- | --- | --- |
| `669997ac28258f26d0bafc81b1d081abb407a3a1` | `review/remediation/20261003-prepare/batches/B20/refreeze-after-B19-C-1/previous-scope-supersession.json` | `dd06296461101146d799335f4befa5785eaecf0a` | `b4d1df2fdfe3a9857fb3dc7232999cf224e4e779167c0a7a51631a131de70919` | 826 |
| `d54fba72a75a3324d7a3daf8e02bc1ecf6c8beeb` | `review/remediation/20261003-prepare/batches/B20/original-scope-grant-1/scope-receipt.json` | `79a50735dc09edbf39845bde132e65f1218e994e` | `23cc954aebac0877326b3c7fd1ce0f0e0e4188b827743a3bcd0a1b8d006c9097` | 121505 |
| `924c7c3a7a5029b07ad18085cf2dadb594512186` | `review/remediation/20261003-prepare/batches/B20/candidate-fix-1-original-scope-grant-1/scope-receipt.json` | `36ea6e26a6876858cae61b968f2400580dc95709` | `3b63ea40281dbe2390180f23c72e513585debc02f44a8b20ad031c20340cdef7` | 16978 |
| `405d7884058d30d94655be0b75f8f12eb07a15d9` | `review/remediation/20261003-prepare/batches/B20/integration-stage-1/candidate-gate-receipts.json` | `0977d989fd4924d400198afa6f278308e8815361` | `ca3f1981b395c2d85a6916c357c4b12a9a732956f07ac5d14ea11d287c24a16e` | 3407 |
| `405d7884058d30d94655be0b75f8f12eb07a15d9` | `review/remediation/20261003-prepare/batches/B20/integration-stage-1/finding-registration.json` | `2800cac1ebe844d777ee4d2777d53cb05949ba37` | `8647743f4df3eca378b79291c8d692f70890d8d4ea61b23cea2b9d3a862c7af4` | 54990 |
| `66ba31f7895067c9d925aba20ce3de046fbf60e7` | `review/remediation/20261003-prepare/batches/B20/actual-freeze-1/public-registration-actual-binding.json` | `1174a32d53986b34e9fa7673b7b97f6ceaa0f3c0` | `ecaab7ebf416641e28d56a9c5a97dd06fc279744cfb34a85976684a9ee702a96` | 2905 |
| `66ba31f7895067c9d925aba20ce3de046fbf60e7` | `review/remediation/20261003-prepare/batches/B20/actual-freeze-1/source-limits.json` | `6e0266d316f0c721abefa4496e4d0c4cfb958643` | `9557227d85e60b44b74653808675e0e20b11442c87727ecb158dda54dc47560d` | 871 |
