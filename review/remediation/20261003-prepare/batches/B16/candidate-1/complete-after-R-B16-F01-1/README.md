# B16 完整候选后继：R-B16-F01 定点修复

正式输入仍为 B13-C `27185563f307e16d2612fa86e83b2c9bd772c79e`；旧候选 `ae223d7bfb9ff6ed8a1ac153debb986115345957`。仅净目录 B16-C003 第590行“上限50对照实际20来源30目标50”改为“上限50对照实际20来源26目标50”。来源完整扣24到26，目标夹限恢复20到50。原净正文、其他十个实物输出、其余目录字节及完整原始/批准/当前限定控制保持；scope3不扩展。

本目录 manifest.json 为当前十一输出的完整身份入口；traceability-completion.json 准确继承24/20与全部非局部限制，并定点覆盖旧C003目录拷贝。作者修复证据在 `review/remediation/20261003-prepare/batches/B16/author-draft-1/remediation-R-B16-F01-1/`，旧版本全部冻结，新证据准确后继化，不重写旧review/preparation/scope报告。

OLD的独立FULL报告为 `458f4f207266154021340c09d949f7863c358df2`：23/24贡献PASS_SCOPED、20/20primary通过，C003存在唯一R-B16-F01。本作者只修订，不签新FULL或affected PASS，不创建任务；原reviewer需对固定NEW完整OLD→NEW及C→NEW流增量复核。affected仍在审OLD，若有新增发现按父任务补充。ACT、C接受、canonical关闭均未执行；各独立门保持。

完整未过滤差异与精确NEW SHA/tree将在普通提交、推送和远端读回后的新增发布入口绑定，避免文件绑定自身提交的循环。未执行参考、游戏、行为向量或历史程序；全部具名未读、U/G/AX及条件树果67等限制原样保留。
