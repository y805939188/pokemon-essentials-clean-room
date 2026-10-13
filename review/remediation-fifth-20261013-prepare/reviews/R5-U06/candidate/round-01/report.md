# R5-U06 非作者独立候选复审 round-01

固定候选整体 **FAIL**：18 项中 16 项限定候选 PASS、2 项 FAIL；145 条必修验收中 142 PASS、3 FAIL。该裁决只绑定下列候选字节，不签 actual、正式接受或 CLOSED。U02、U03、U04、U05 的上游贡献门保持 **WAIT**，公共登记不变。

审者真实任务 `01a1352f-333a-77a9-bf84-d250e499e00c`（环境 CODEX_THREAD_ID），父来源线程 `01a10d94-84b9-759e-aa1d-edb0d9b6d0e2`。本任务在作者固定候选产生后被另行委派；未创作或改动作者字节。四个分组独立源语义任务加一个精确回归审计，主审直接复核两处反例并独立重建/应用补丁。Git 发布账号不作为任务独立性证据。

合同 `22fba7786b0090a1955ce6211315b0036cddfbcd` / tree `21f3484d167d8cab7a288e0204c72f275414d52e`；B5 `9366d9d17aaeac3b4414236468affa650fb3dd27` / tree `594e65edcb192a19110540245fc1663bae2de007`；只读 R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。候选 `f393d261c8ab1660323d8b32fe4a7d81c33e3e2c` / tree `b147ba1322a5cb9ecd9074d2a15b1a2d24cc5cf0`；证据 `bc2b9f77fffe81e618bf7ef0ca2573fc7816e8a7` / tree `7f20a072a4f52116b2596efa0f90e9785d7ed95a`。作者分支 `codex/r5-u06-author-20261013`。请求参数 gpt-6.1-sol / ultra / default / 普速 / 禁 Fast；实际模型、推理、服务和速度回显均 **UNVERIFIED**，不猜测或审计认证/额度。

| ID | 固定候选裁决 | 通过/验收 | 失败验收 | actual/接受/关闭门 |
| --- | --- | --- | --- | --- |
| GR5-M10-001 | PASS | 9/9 | — | WAIT |
| GR5-M10-002 | PASS | 7/7 | — | WAIT |
| GR5-M10-003 | FAIL | 6/7 | GR5-M10-003/C03 | WAIT |
| GR5-M10-004 | PASS | 6/6 | — | WAIT |
| GR5-M10-005 | PASS | 9/9 | — | WAIT |
| GR5-M10-006 | PASS | 6/6 | — | WAIT |
| GR5-M10-007 | PASS | 8/8 | — | WAIT |
| GR5-M10-008 | PASS | 7/7 | — | WAIT |
| GR5-M10-009 | PASS | 7/7 | — | WAIT |
| GR5-M10-010 | PASS | 7/7 | — | WAIT |
| GR5-M10-011 | FAIL | 7/9 | GR5-M10-011/C01, GR5-M10-011/C04 | WAIT |
| GR5-M10-012 | PASS | 8/8 | — | WAIT |
| GR5-M10-013 | PASS | 10/10 | — | WAIT |
| GR5-M11-001 | PASS | 6/6 | — | WAIT |
| GR5-M11-002 | PASS | 8/8 | — | WAIT |
| GR5-M11-003 | PASS | 9/9 | — | WAIT |
| GR5-M11-004 | PASS | 9/9 | — | WAIT |
| GR5-M11-005 | PASS | 13/13 | — | WAIT |

最小必修返修：

1. **GR5-M10-003/C03**：`U06-M10-003-D/E` 的完整前提要求“B、T为有效字符串”，刺激却为 `T=null`。无 T 是合同要求的独立分支；矛盾前提不能签该对照。WP67-A §3.2.1 的可选 T 和资源选择链本身通过。改为“B为有效字符串；T存在时为有效字符串，不存在时为null”，同步 static-vectors、共享 engine-overworld 测试提案、edits/fragment/patch 及相关派生 manifest/引用身份。正式共享目标仍由 R5-I 写入。只需定向复审缺 T 的 D/E、关联前提与同步字节。
2. **GR5-M10-011/C01、C04**：`[4,2]`、t0=.375、t=.475 被正文和向量 C 无条件写为帧1。固定 R 的普通浮点时差/帧时长再截取整数，在二进制64输入条件下比值为 `3602879701896396/3602879701896397 < 1`，应为帧0；这是静态算术反例，未调用参考函数或行为模型。主审直接核了 R 的创建时钟/时长/更新及候选正文。最小改 t=.48 作帧1的内部采样点，.725 的帧3可保留；同步 WP15 镜像、共享测试提案、static-vectors、edits、fragment-manifest、formal-diff.patch 与派生身份/criterion 引用。若保留精确边界，则必须补足数值前提及边界舍入说明，不能以通用“宿主未测”替代。其余切帧、创建原点、全局相位反向、迟到更新、复制和静止化子范围通过。

非阻塞措辞澄清：M11-005 的 WP63 §3.3 可写为“写逻辑坐标并建立本次插值起点，随后刷新地点/详情，再收按钮”，使它与固定 R 的顺序更易核对。本段不扩大必修分母，不改变 M11-005 的限定候选 PASS。

独立校验从固定 B5 和完整唯一锚点重建 24 个目标/43 个编辑，14 份直接镜像一致；15 个共享片段覆盖10个共享目标，保留 WAIT，零上下文 `git apply --unidiff-zero` 复现同一批完整拟字节。全部39份候选/后继证据载荷按 bytes/SHA256/Git blob核对；覆盖恰为18项/145验收/106静态向量及合同的逐项消费者目标。机械覆盖和 hash 成功不替代上述语义裁决。

完整字节取证复用本地 B5/冻结 Git 对象；合同42份固定 R 源、18份原证据、必要额外源及6份共享/精确旧回归输入只定向读取并缓存。原提出者、root-M10/M11/C10/C11、GCV及共享条款被逐项反查。阅读日志区分完整载荷验证与具体语义范围/JSON selector。源和消费者正常、失败、取消、部分提交前缀分别验证；012完整单元后写坐标和013重复抑制后空单元失败分开，M11-002焦点与003同轮仲裁分开，M11-005只接收六个 required 时序子范围。

旧回归：35个唯一精确历史记录（44处限定引用）、11个共享合同记录和18个canonical范围关系核对；旧 owner/scope 和正确合同保留。作者列的303个不同path/line旧行均原字节保留。独立扫描24目标得到1418个含旧ID的表格物理行也均保留；该数含跨消费者重复ID，不是全局旧向量总数，字节不变不自动转签语义或历史 PASS/CLOSED。

执行账分列：历史 R4 隔离参考记录 **4**；历史 R5review 隔离参考记录 **4**；本 update 新参考/行为模型/宿主/Demo执行均 **0**。R5-REF-004 是旧记录1份、原进程2次（先设施失败，再加惰性 Rect 替身重试）、5个原观察，只静态核身份与原观察，不复跑、不借给005。106个向量均为 **DERIVED_VECTOR / NOT_EXECUTED**；Git、格式、hash、补丁和数学算术为 **TOOL_VALIDATION**。媒体可听/可见结果、宿主属性量化、真实采样/物理输入、插件、异常外层恢复和Demo仍未测。

optional7、no-required7、政策6、M11-005内optional范围及冻结13项限制继续隔离；本复审未增批次或重开全局review。只新增本 round-01 六份 review 文件，未改正式规格、作者候选、公共登记、reference、冻结历史或main，未访问Mac。修复后只针对上述两处及受影响同步字节复审；无新增实质证据不重复扩大审查。候选通过贡献若随上游改变，实际整合后仍须定向检验新字节，且不能转签 actual。

完整逐条证据见 [criterion-results.json](criterion-results.json)、[source-reading-log.json](source-reading-log.json)、[regression-results.json](regression-results.json)、[independent-validation.json](independent-validation.json) 和 [review-manifest.json](review-manifest.json)。普通推送及完整新增载荷读回记录由 independent-validation 的后继回执绑定；最终 commit/tree 由交接回复给出，避免自哈希递归。
