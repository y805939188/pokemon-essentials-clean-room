# R8-U04 独立候选复审入口

本入口交给协调任务 `01a14a04-b178-7567-a4eb-0f0bfac9a0d9` 创建的**实际非作者**使用。请求配置为 `gpt-6.1-sol / ultra / default / normal / Fast off`；无权威回显时 actual 各字段为 `UNVERIFIED`。作者没有启动复审、没有自签候选PASS、实际整合PASS、ACCEPTED或CLOSED。

冻结身份：仓库 `y805939188/pokemon-essentials-clean-room`，输入 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`，作者分支 `revise/r8-u04-20261017`。候选为**本文件所在的实际提交**；完整SHA由外部最终交付绑定，不能以移动分支名代替。参考仓库只读，固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。C35 `2460370f1e410bd49cc29e377b89662838aed2b3` 是语义core，C36 `802cef65d44772504304016b8ecbe9be558009a0` 是原handoff发布；不把历史来源全部重标为C35。

候选根为 `review/remediation-eighth-20261016-prepare/candidates/R8-U04/`。`candidate-manifest.json`精确绑定六个镜像文件的路径、bytes、SHA256、blob及固定输入身份；镜像相对路径与正式目标一一对应。只允许协调任务把候选贡献整合到正式层；本作者没有修改正式规格、公共索引或main。

审者先完整读固定输入中的AGENTS、`review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md`，同根 `handoff/batches/R8-U04/reviewer-prompt.md`、`prompt.md`、`readset.json`、`handoff/batch-assignment.json`与manifest，以及所属六条完整 `handoff/contracts.zh.json` records 8、10、11、18、19、20；同时使用accepted-facts/history/policy伴件与当前根接收。完整恢复原提案、反证及根裁决，不以标题、摘要或作者的FULL代替本人实读。

完整阅读读集全部40个相关源/规格单位（精确身份见`input-identities.json`及原readset），并逐一完整阅读下列最终受影响文件；审者应亲自核全部未改内容与累计保留，而非只看diff：

1. `mirror/deliverables/final-specification-set/engine-overworld/wp11-map-topology-transfer.md`
2. `mirror/deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md`
3. `mirror/deliverables/final-specification-set/engine-overworld/wp13-interpreter-command-matrix.md`
4. `mirror/deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md`
5. `mirror/deliverables/final-specification-set/engine-overworld/wp14-random-dungeons.md`
6. `mirror/deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md`

逐项以`issue-dispositions.json`接合原证据、修改位置、区分场景、引用与去向，但结论必须由审者自己的完整阅读支持：

- GR8-PBSW-002：三处一致区分已知[051] Dungeon=true与实际Map051/绑定/编译装载/进入查询/Demo未知。
- GR8-WORLD-001：正常摆放与进入后异常、明确捕获继续、同实例重建/缓存清理及新容器、进入前/收尾后边界、成功与失败加载前缀。
- GR8-WORLD-002：显式speed0、100格单轮12800/10240≥3328、26格3328/768、小偏移/moving/snap/无连接分支、全局与容器引用、失败取图前分叉的条件保存、读档/继续预览先取图、第二轮及非零速度限定。
- GR8-WORLD-003：独立普通移动与跳跃计时、合法零跳的ACTION/SPECIAL、已有debug与登记门分层、消息/微更新、请求前缀及无UI/跳跃清理保证。
- GR8-WORLD-INT-001：117携父当时编号、子绑定当前图、父保原图；连接/同图/失联、缺记录、深度101及异常写入前缀，保R5-ID与event0独立入口。
- GR8-WORLD-INT-002：直接119首同名、缺目标正常外层到下一项、末尾入口先结束、101仅前向预读独立、有限回跳/损坏结构边界及后继部分提交。

最新用户授权已覆盖旧prompt全部optional未选限制，但U04的可选分配为空。`optional-dispositions.json`列出十项对应责任批次与本批不越权理由；不把它当作全局拒选。只检查本批六必修，不重复全面打标；`tagging-handoff.json`提供变更章节、稳定锚点与行为清单。

文档工具校验可重现：在仓库根执行 `python review/remediation-eighth-20261016-prepare/candidates/R8-U04/evidence/validate.py`。它会更新本批证据中的manifest/validation；如需保持复审输入完全冻结，应在审者自己的独占工作树副本执行并把输出写到审者证据目录。`validation.json`的PASS仅为结构/身份/保留校验，不是业务执行或独立接受。首轮退出码误判及修正后的真实I/O保留在`commands.jsonl`和`io/`。

本次所有行为为 `SOURCE_STATIC / DERIVED_VECTOR / NOT_EXECUTED`；未运行Ruby、游戏、独立行为模型、编译、真实存档往返、媒体或宿主UI，未开发框架。真实材料/宿主缺口不得阻止可读静态事实，也不得被静态推导抹去。

审者只在自己的独占复审证据目录写结论，不改作者候选或正式层。分别报告候选是否PASS及未决；实际整合后仍须重新冻结输入、全文接收共享消费者与累计保留，再分别登记actual integrated PASS、ACCEPTED、CLOSED。作者的本次交付只表示修订候选已准备好。
