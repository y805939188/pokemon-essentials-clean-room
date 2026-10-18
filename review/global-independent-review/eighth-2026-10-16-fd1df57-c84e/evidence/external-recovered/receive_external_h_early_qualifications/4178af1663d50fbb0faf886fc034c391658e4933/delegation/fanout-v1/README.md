# H-EARLY 剩余有限接收：四份完整派发合同

状态 `FROZEN_NOT_STARTED`。只冻结材料，没有自行spawn。父主线程从本次最终回显取得准确包含提交SHA，再以该固定提交派发四个真实非目标作者context；不得读取分支未来HEAD。当前协调线程仍在原专用分支，main/tag/原作者/公共台账只读。

| 合同 | 完整实质主责 | 原R5合同/检查 | 独占输出目录（均在本任务目录内） |
| --- | --- | --- | --- |
| [early_r1_r4](shards/early_r1_r4/prompt.md) | R1全部资格/勘误/阶段；R2全部229资格与21/341分列；R3/R4完整原控制、排除、有限Summary后继；H05执行限定 | 不拥有R5 primary | `receivers/fanout-v1/early_r1_r4/` |
| [r5_u01_u02](shards/r5_u01_u02/prompt.md) | U01全部34及U02全部14合同、每项完整原值/当前值/理由与必要消费者 | 48 / 294 | `receivers/fanout-v1/r5_u01_u02/` |
| [r5_u03_u06_core](shards/r5_u03_u06_core/prompt.md) | U03全部11、U04全部7、U05的1及U06前13；U03旧FAIL/有限后继与对应完整接口 | 32 / 196 | `receivers/fanout-v1/r5_u03_u06_core/` |
| [r5_tail_shared_policy](shards/r5_tail_shared_policy/prompt.md) | U06末5项和U07全部7；14非必修、13limit、6policy、共享/依赖/写者/贡献及唯一激活的准确资格 | 12 / 78 | `receivers/fanout-v1/r5_tail_shared_policy/` |

每目录均有完整 `prompt.md`、精确 `readset.json`、无损 `complete-records.json.gz` 和 `manifest.json`。每份prompt内嵌完整原接收prompt、完整全局prompt、AGENTS、review-SKILL，没有只留下摘要。readset绑定自身完整对象、原始载荷与当前R/B8文件候选的固定身份。新增合同的包含commit由父派发消息给出，载荷bytes/SHA/blob已在readset冻结，避免自身未来commit递归。

`aggregation.json`给主责集合和汇总接收规则。92 primary与568原schema恰各一次，交集0；不同轮控制/criterion/贡献/共享合同不相加。V/N值、hash、JSON叶和结构绑定行只作恢复/关联；它们不产生额外验收。4,993个R5字典条目均有所属完整对象的上下文绑定，raw和expanded双视图保留。生成/校验信用0，不能宣称这些对象已经被新context阅读。

`shared/r5-originals/`还保存18份完整原始R5合同、独立复审和接受输入的惰性gzip，共10,050,868解码字节；原commit/tree/mode/blob/bytes/SHA见 `evidence/original-r5-input-identities.json`。原H10载荷及357目标载荷可从固定前一检查点ab44ee8的readset完整恢复。读集含普通对照、取消/失败/部分提交、所有原提案/反证/完整标准；不依赖V字符串片段才能取得完整合同。

恢复前全文读懂 `restore_fanout_inputs.py`。在自己的隔离bare普通fetch固定目标11c057d9、固定前一检查点ab44ee8与父给出的合同包含提交，核目标checkout/task tree和原357行完整身份集合，随后使用该helper和prompt里的readset SHA，仅写本独占输出目录。helper逐载荷核Git成员、编码身份及有界解码身份，不执行恢复文件。`shared/available-R-B8-files.json.gz`只是文件可用性/完整身份索引，不要求各接收者重审全部432或131文件；必要完整定义/caller/receiver/条款由实际事实决定并精确扩展登记。

四份都可独立起步。共享/跨域最终接合按相关producer逐事实收据进行；tail接收全局资格不能替代其它producer实读，producer也不能替代tail的共享/阶段接收。只阻塞相关范围，不等无关上下文。共享工作树时四者不得并发写Git索引，唯一发布者负责普通commit/push；独立checkout的专用输出分支由父实际派发采用readset中的建议或明确覆盖，不自行改main/tag或强推。

必须处理的后继输入：

- `shared/mandatory-policy-clarifier.v1.json`：RECEPTION-H-EARLY-POLICY-002，UTIL-03末尾LF反例；是待非提出者裁决的旧policy事实限定，不决定未来兼容，也不自动新增B8必修。
- 固定ab44ee8 `findings.json`中的RECEPTION-H-EARLY-EVIDENCE-001：业务原actual正文不能按键名行政化；28长值本体已经补读，但完整上下文/消费者接收仍由tail完成。
- 固定ab44ee8 `evidence/historical-five-identities.json`：五旧报告新认证身份；原UNVERIFIED副本继续保留。
- 当前 `evidence/followup-policy-review.json`：六policy完整记录及有限完整定义已继续读到，完整消费者链与独立裁决仍OPEN；不继承整域/整接口签名。

所有必要未接收归零且全部相关接口实际接合后，根主审才能签全H task-final。四份合同冻结、工具验证、未来四个任务退出或普通push均不等于该条件已满足。当前整体继续 `INCOMPLETE / UPDATE_NOT_STARTED`。
