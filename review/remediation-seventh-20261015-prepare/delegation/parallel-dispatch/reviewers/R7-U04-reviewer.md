# R7-U04 独立云端reviewer派发

只执行本次具名角色，不创建子任务或其它作者/reviewer。父会话唯一负责 cloud_threads.create；无用户设置的并发数量上限，但不要把可并行当成已创建或服务slots证明。父会话已报告U01=01a13f52-add1-7706-b7ec-54e07e0d7013、U04=01a13f52-cc74-7568-9e75-85ac773c6015、U05=01a13f52-ecf8-73f9-8c9b-f5c164f0c017为inProgress，不重复创建它们。其它批次以父会话真实task登记去重；本静态派发文本不是创建回执。

本角色请求 gpt-6.1-sol / ultra / service_tier=default 普通速度，禁Fast。模型/档位/速度的实际有效回参缺失时逐项UNVERIFIED，不以请求argv、自报或成功退出认证配置，不查额度/认证。实际task/context/PID、请求、UTC、完整可发布工具I/O和退出分开留存；私有模型流不作为公共证据推送。

仓库 https://github.com/y805939188/pokemon-essentials-clean-room.git 。输入远端分支 `codex/remediation-seventh-20261015-cloud`；固定准备提交 `4bd152023b4bcb3dd5a3654deffe75aeebc40f10`。行为基线B `e646432c644dec04d306842cc5a559a29c718fbc`，正式tree ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c。参考固定R为 Maruno17/pokemon-essentials 的8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0。只在云端工作，不操作用户Mac，不用浮动HEAD替代固定输入。先读实际项目AGENTS.md。

原完整七组合同：提交 `f622356f3beb9e84ea8cff9db07c7fb382565d3f` 的 `review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U04.json`。
原角色入口：同提交 `review/remediation-seventh-20261015-prepare/delegation/prompts/R7-U04-reviewer.md`。
固定恢复工具：提交 `658488c81f1f3181a488298ab27850c8af951d73` 的 `review/remediation-seventh-20261015-prepare/tools/restore_container_context.py`。
逐批证据恢复清单：同提交 `review/remediation-seventh-20261015-prepare/recovery/batches/R7-U04.json`。
跨容器说明：同提交 `review/remediation-seventh-20261015-prepare/recovery/independent-containers.md`。
上述固定文件可由 `https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/<完整固定commit>/<精确路径>` 读取，不必下载80MB Manifest或扫描完整core包。先完整阅读工具和本批清单再执行；不盲跑下载程序、不执行恢复出的参考/native程序。

独立容器不共享整合者本地目录。将工具和本批清单分别保存为 `/workspace/r7-bootstrap/R7-U04-reviewer/tools/restore_container_context.py` 与 `/workspace/r7-bootstrap/R7-U04-reviewer/recovery/batches/R7-U04.json`，运行：

```bash
python3 /workspace/r7-bootstrap/R7-U04-reviewer/tools/restore_container_context.py --plan-directory /workspace/r7-bootstrap/R7-U04-reviewer/recovery/batches --batch R7-U04 --destination /workspace/r7-context/R7-U04-reviewer
```

工具定向恢复本批原载荷、身份/原绑定及L01-L14、固定源/正式读输入和冻结合同/Prompt。原 `/workspace/r7-evidence` 映射到 `/workspace/r7-context/R7-U04-reviewer/evidence`；原 `/workspace/r7-reference` 映射到 `.../inputs/reference`；固定正文在 `.../inputs/project/`，原入口在 `.../dispatch/delegation/`。这些只是有界文件快照，不是完整Git checkout或运行认证。已有匹配恢复可复用；连接中断保留目录、同环境同目录加--resume，不覆盖冲突字节、不另起替代任务。有新的具体可读依赖应具名定向补取，不能伪标limit。

规格只描述可供从零重写的独立功能、逻辑、行为，不实现引擎/TypeScript包/适配器，不移植Ruby结构或复制源表达式。完整前提、普通对照、取消/异常/部分提交、最小规则、正确保留scope、消费者和历史回归按原七组及已接非作者反证审读，不复活已被反证排除的宽提案。7 optional、2额外导航facet、1 no-required、2 policy均未采用；同一必修的条件同步须给具体矛盾和依据，不自动扩大。

L01-L14和旧56/92关闭边界保持。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、游戏宿主/Demo/native媒体/真实存档回放分开。未执行向量保持NOT_EXECUTED，身份/退出0不替代语义验收。有效配置UNVERIFIED，宿主等0不得提升。进度分母固定27项/13批；只有R7-I写正式正文、公共台账和整合分支，不改main/tag/旧证据、不force、不提前关闭依赖问题。

本批必修：GR7-M03-001、GR7-M03-002。这是完整的候选冻结后reviewer入口，**现在不是可启动回执**。父会话仅在R7-I已经完成真实候选接收/冻结后才创建本独立任务。

启动必须由R7-I另外提供：实际冻结commit/tree，以及该commit下精确路径 `review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U04/candidate-input.json`。不得用当前HEAD、浮动作者分支或作者口头PASS猜输入。缺冻结绑定、完整候选/作者证据、作者真实task身份或可确认不同的实际reviewer context，则WAIT_INPUT_OR_INDEPENDENCE，不开始语义PASS，不启动另一个reviewer。

candidate-input.json须绑定本批及必修ID、固定B、原合同commit/path、作者实际task/context资格、唯一作者分支、候选实际commit/tree、候选对B完整差异、每个候选文件和作者证据的bytes/SHA256/blob、条件同步依据、接收完整性、真实命令及未满足依赖；冻结字节不得后来被浮动branch替换。完整门见 `review/remediation-seventh-20261015-prepare/delegation/parallel-dispatch/candidate-freeze-requirements.json`（以父会话提供的本派发固定commit为准）。

你必须与本批作者为不同实际context，不派生子任务、不担任自己的作者或自己的R7-IR。task ID/PID和有效模型回参分开；无配置回显保留UNVERIFIED。收到真实冻结后先按精确文件身份读回作者候选和完整证据，保存为新的只读 `/workspace/r7-review-input/R7-U04/`；不要checkout作者分支、改作者文件或执行作者/参考未知程序。固定证据恢复工具不包含候选，也不能替代候选接收。

逐必修完整审查原七组、已接非作者反证、固定R的源/消费者、B与候选正文/目录/向量、全部正确保留scope、必要历史回归和反向消费者。检查正常/取消/异常/部分提交、源缺陷事实与未来政策分层；分别核所有强断言的前提。核作者对B的完整差异仅在本批candidates/，并只修改原批准实际目标的镜像/证据。条件同步不得借机采纳optional/policy。

特别核共享冲突组 无 的本批贡献能否与其它贡献按条款接收；这里只给候选结论，不声称其它批次依赖或实际合入已经完成。逐ID给 PASS_SCOPED_CANDIDATE / FAIL_SCOPED_CANDIDATE / WAIT_INPUT_OR_INDEPENDENCE，并引用实际候选字节和完整反例/回归范围；传输哈希、作者自审、退出0、旧全局PASS均不能代替本次独立内容审查。未执行向量不写成运行成功。

只写 `candidates/R7-U04/evidence/reviewer/r1/` 下 report.md、per-id.json、review-input-receipt.json、artifact-manifest.json 及本次真实工具证据，不修候选，不写正式/公共文件。独立成果运输按本轮普通提交/推送授权限于唯一分支 `codex/r7-u04-reviewer-20261015-r1`：在自己的干净隔离checkout从固定B `e646432c644dec04d306842cc5a559a29c718fbc` 建分支，普通提交/推送上述reviewer证据；不携带或改写作者镜像，不推作者/整合/main分支，不force。若同名分支非本task所有，保护原成果并回报，不另换分支。若父会话用平台导出传回同样须包含全部新文件和完整身份，不能仅给本地绝对路径。

返回真实审者task/context、审查输入冻结commit和候选commit/tree、逐ID结论、未满足依赖、结果commit/tree/分支及普通push/远端完整读回证据。候选PASS仅供R7-I整合；你无权登记实际整合PASS、ACCEPTED或CLOSED。实际合入后必须新建独立R7-IR审真实整合字节，依赖和回归满足后才关闭。
