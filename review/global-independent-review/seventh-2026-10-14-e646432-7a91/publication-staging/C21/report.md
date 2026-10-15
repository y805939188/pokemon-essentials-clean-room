# R7-C21 实际交接包有限接收

本次33文件的完整字节、结构和固定C0绑定已核，未发现剩余具体包内容错误。结论仅为 STRUCTURE_AND_IDENTITY_VERIFIED_SCOPED；不签全局PASS，UPDATE_NOT_STARTED。

C0：28e0d9df6ca4f75de9773a502ebdaa177cc0752c；workspace tree a2e8143f5f514ac8db5fcc36e8cbdaaaaf428133；report tree 3583466aef215439358c9578f956871afa1f98af；formal tree保持ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c。

- root、canonical、C13中文合同及32个交接消费输入与C0实际gzip对象解码值一致。37项分类为27必修、7可选、1无需必修、2policy；必修10P2/17P3；canonical与C13的259组逐对象相等。
- 主prompt逐字节内嵌完整C0 C13正文和两facet正文，37节/259组标题和全部组顶层字段标签完整；历史非必修及L01–L14完整嵌入。R6的8optional/1FLOAT/7policy/14limits/1no-required保持独立。
- 27必修恰有唯一primary，13批第一波与实际批ID完全相同；26入口为13author/13reviewer，源字段完整保留，状态均未启动。dry分支在Popen前明确返回，本任务没有调用它。
- H08两optional facet的六条运行关系在当前依赖图保留六条、冲突图两种视图共十二处而唯一关系仍六条。batch_id为空、mandatory_scope排除、完整scope/角色/root_evidence保持，未进入必修分母。
- 索引34251逻辑路径与21449对象全部绑定实际C0树。用一次cat-file batch完整读取985,248,330 encoded bytes，逐对象bytes/SHA256/Git-blob全匹配。没有把其余13.7GB原日志档案再解压计为新读源。
- package-members的32个非自身成员与33个实际文件逐字节核bytes/SHA/blob；自身索引另作外部身份，不递归selfhash。

根最后追加的独立恢复说明已单独接收：prompt严格追加2153字节，manifest只增standalone_evidence_recovery，原全部对象值不变；成员索引仅两个成员行更新，其余30文件不变。新增说明明确tasks/R7-C13/原链接base、固定C0/report tree、实际gzip树成员及三身份校验、隔离restore和私有流边界。

最终身份：

| 文件 | bytes | SHA256 |
| --- | ---: | --- |
| prompt | 3134972 | 3eed43dbc8e8efcc16e0929cb31c1e1660f6a1ba09fbfb61a84eec29911f599a |
| manifest | 80065362 | fe1bdf280165a73ee527937c2978850b08d7455eb1e4d8c6a75fc06af83d5862 |
| package-members | 8034 | 3a4f8233e4584c996b49793a90b2a0af6c61560863e04b845c4c56daf67b3b9e |

保留两类检查方法假警报：整记录JSON fence假设不适用于人类Markdown；原overlay逐行比较需识别path外提及仅在完整overlay保留的evidence_scope_pointer。原失败检查未抹去，后继按实际结构验证，不视为合同缺组或scope丢失。

C19未产owner task.json/report.md。C0索引确无这两文件，progress.final真实指向final-adjudication-integrity.json并明示该事实；本任务未补造。根另述的旧refs/7 worktree保护结果作为外部收到的保护证据保留，C21不冒充重新执行。

本任务未联网、启动CLI/agent/--launch/update，未执行reference/native/游戏/行为模型或Git变更；只在publication-staging/C21写接收证据。实际模型配置UNVERIFIED，无额度或认证探测。远端全部逻辑载荷解压读回仍由根后继执行；该边界不由本地结构接收替代。
