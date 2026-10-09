# B15 完整候选发布与独立远端读回

新完整九路径候选 `cc08a9150131b7e9fae8424fb0ede890169dd64f`，tree `9344b2a973519cdbe8fe9ad5c2e5549334669a9a`；正式FIX_BASE `0cfe99094b76f8d75fded0d638694677855a5f0c`；分支 `codex/cloud-dot-B15-author-1-20261009`。父批准输入 `70a28cfc56ee17b8dc4d815515e96640d80c6321` 仅为原稿范围批准/旧草案管理版本，不替代正式基线。三份原稿按批准完整patch精确应用，before/after全字段匹配；六净化正式文件保持先前作者修订字节。范围批准不代表质量PASS。

全部31变更路径、九正式输出身份、原稿批准/应用、独立角色/建议写目录与有限结束条件见 publication-receipt-after-sync.json。完整未过滤基线→候选diff保存 complete-candidate-after-sync.diff，SHA-256 `a8dc56586bc3397aa0570bec8360985caac64c6b588c165865b1364a585125d3`，834537字节；旧管理发布→新候选的未过滤增量另存 approved-publication-to-candidate-after-sync.diff，仅作准确版本增量导航。旧publication-receipt.json/complete-candidate.diff绑定旧六路径草案，保持历史，不作新候选依据。

普通push后全新bare对象库独立fetch分支及准确正式基线，核验ref/FETCH_HEAD/tree、全部31变更文件字节和两份未过滤diff，前后remote ref一致；新候选remote对象的父提交也精确为旧发布70a28cfc56ee17b8dc4d815515e96640d80c6321。后继只发布本读回/diff，SHA在任务返回中外部绑定。

作者范围与metadata检查通过；运行/向量执行/demo已证全0，U01–U10/G01–G12/AX01–AX20及具名限制保留。没有作者独立review、正式接受、canonical关闭、公共台账修改、main合并或force push。作者有限结束条件已满足；下一步父另派R-B15完整candidate Ultra及必要bounded affected gate，sole A-REG整合后新actual再FULL/affected Ultra，不能转移旧草案或candidate结论到actual。
