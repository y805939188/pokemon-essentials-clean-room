# R8-U01 独立复审入口

此入口供父协调任务创建实际不同于作者的 `gpt-6.1-sol ultra/default` 审查任务。本任务只作候选修订与静态文档核验，没有正式 review。请求 speed normal / Fast off；实际配置无权威 echo 时逐项 UNVERIFIED，不探测CLI或改模型。

候选载荷提交将在发布绑定记录提供；分支 `revision/r8-u01-20261017`。固定作者输入 `4575e80d041ab0c74a42e2e36399d05791dbaa5b`，B8 `fd1df570cad987dc3852a3b958f03916e317f7fe`，参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。候选4文件精确身份见 [candidate-manifest.json](candidate-manifest.json)，逐项原证据/修改位置/区分场景/引用/依赖/去向见 [remediation-record.json](remediation-record.json)。

最新授权覆盖旧prompt中的全部optional未选限制。本批已按标准选择 GR8-UI-001，仅作普通保存拒绝括注限定，不新增UI目录写集或命名规则。原29 required / 10 optional分类和历史裁决不改；另9项可选不属本批。

按仓库路径读取以下完整材料：

1. `AGENTS.md`；`review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md`。
2. 同报告 `handoff/batches/R8-U01/prompt.md`、`readset.json`、`reviewer-prompt.md`，`handoff/batch-assignment.json` 的 R8-U01，以及 `handoff/contracts.zh.json` records 0/1/9 完整合同。旧启动/optional状态以本次用户授权与实际发布绑定为准。
3. 同报告 `handoff/accepted-facts-and-mandatory-companions.json`、`history-qualifications.json`、`policy-and-preservation.json`、manifest及原恢复读集。保原5caff来源与C35恢复身份，原根记录及其反方完整按合同接收，不以截图/搜索片段代替。
4. [reading-ledger.json](reading-ledger.json) 中21个固定源/规格整文件，继承报告载荷的身份/typed-purpose和本批完整根语义。作者的身份核验或原审者FULL不代替本次必要语义实读；可得未读不改标limit。
5. `mirror/` 中4个最终候选整文件（从候选根相对路径）；同本目录4个diff及 manifest 比较。不能只读diff或验证输出代替最终全文与累计保留接收。

最小独立检查：

- KER001 五类控制分别核文件状态与UI请求；P先删、单个P.bak后删，首删失败不检查备份，第二步失败无主档/有备份，下次P存在门不读孤立备份；标题返回、无效档拒绝退出/同意重置、提示/非捕获异常各分开。保UI已有不回滚、递归备份读取与紧急保存原资格。
- KER002 无主档/可读旧序列空表/有效当前非空三种装配结果；默认17/全新已加载门/两语言显式前提；空表不转换备份写回；后续校验、递归有效备份、无备份拒删退出/同意成功后菜单、语言BACK默认0与解码失败各分开。保WP08、SV02、LZ13/14、UI65后续链和无文件充分示例。
- UI001 有界首次可变地图名读取→No仍保内存前缀，对照Town/已展开；实际改文仅“不调用持久层保存”，同节不回滚、false/选择音和正常收尾不变；不产生新mandatory或第二地图命名规则。
- 新13行全部静态未执行；原目录整段字节、正文其余部分、历史关闭事实及材料/宿主边界保留。检查允许写集、链接锚点、证据声明与实际差异相合。

可复核工具命令（仅文档/身份检查）：

```sh
python review/remediation-eighth-20261016-prepare/candidates/R8-U01/evidence/validate.py
```

工具57项通过不授予候选正式PASS。审者应按完整事实给独立结论；即便候选PASS，仍需R8-INTEGRATOR整合后另接收实际受影响全文和累计保留，分别登记actual integrated PASS、ACCEPTED、CLOSED。审者不要替本批直接写正式规格或main。

打标任务入口为 [tagging-handoff.json](tagging-handoff.json)，含章节、候选行号、锚点、行为变更和13行ID；没有重复全面打标。
