# R7-U01 云端独立作者派发（首波）

你是 R7-U01-A，仅做本批作者。父会话已查询最新50个账户任务未发现R7作者；这是父会话提供的去重结果，不是你可自行推断的全局无任务证明。派发仅由父会话执行；不要创建子任务、reviewer或重复作者。如父会话登记已存在同批实际task ID，先续接该任务。

请求模型 gpt-6.1-sol、推理xhigh、service_tier=default普通速度，禁Fast。真实模型/档位/速度缺明确有效回参一律UNVERIFIED，不以请求或自报认证。独立reviewer将由父会话另建 gpt-6.1-sol ultra，非作者本人。

仓库 https://github.com/y805939188/pokemon-essentials-clean-room.git 。输入远端分支 `codex/remediation-seventh-20261015-cloud`；已核固定准备提交 `df3553d65ef8380360cbdded2a2ec925d88ef5fd`，不得以浮动分支HEAD替代合同输入。固定行为基线B `e646432c644dec04d306842cc5a559a29c718fbc`，正式tree ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c。固定参考 Maruno17/pokemon-essentials 的8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0。仅云端，不连接Mac。

完整合同：提交 `f622356f3beb9e84ea8cff9db07c7fb382565d3f` 的 `review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U01.json`。
原精简作者入口：同提交 `review/remediation-seventh-20261015-prepare/delegation/prompts/R7-U01-author.md`。
固定恢复工具：提交 `658488c81f1f3181a488298ab27850c8af951d73` 的 `review/remediation-seventh-20261015-prepare/tools/restore_container_context.py`。
本批恢复清单：同提交 `review/remediation-seventh-20261015-prepare/recovery/batches/R7-U01.json`。
恢复说明：同提交 `review/remediation-seventh-20261015-prepare/recovery/independent-containers.md`。
这些均可通过 `https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/<上述完整固定commit>/<精确路径>` 定向读取，无须获取80MB Manifest或恢复完整报告树。先读项目AGENTS.md，完整阅读工具和本批恢复清单后再执行工具；不要盲跑下载程序。

独立容器不要假定共享整合者目录。将工具和本批清单分别存入 `/workspace/r7-bootstrap/R7-U01/tools/restore_container_context.py` 与 `/workspace/r7-bootstrap/R7-U01/recovery/batches/R7-U01.json`，然后运行：

```bash
python3 /workspace/r7-bootstrap/R7-U01/tools/restore_container_context.py --plan-directory /workspace/r7-bootstrap/R7-U01/recovery/batches --batch R7-U01 --destination /workspace/r7-context/R7-U01
```

工具默认恢复本批具名证据、固定源/正式输入以及原完整合同/Prompt，逐编码/解码身份核验；不创建任务。目的地若已有完整恢复，先读回执核身份，不重复下载；若中断，保留该目录，在同一容器加 `--resume`，不覆盖冲突字节。原 `/workspace/r7-evidence` 映射到 `/workspace/r7-context/R7-U01/evidence`，原 `/workspace/r7-reference` 映射到 `/workspace/r7-context/R7-U01/inputs/reference`；固定正文快照在 `inputs/project/`，原完整合同和Prompt在 `dispatch/delegation/`。快照不是完整Git checkout；不得宣称整树/宿主已验证。需要其它具名可读依赖时定向补取并记录，不假标limit。

本批必修：GR7-M01-001、GR7-J01-001。作者前置批次：无。最低任务：仅修 GR7-M01-001 和 GR7-J01-001：整数键查找与记录对整数相等分开，保留双身份/同类/符号等正确范围；三类复合节头的省略/空位、正整数、显式0拒绝、转换后身份别名与重复拒绝，保留三个消费者与Tileset合法对照。按完整J01-V01–V13及已接非作者反证核前提，不复活被排除的默认游戏故障或架构要求。

只允许下列候选镜像（所有原实际目标均加 candidates/R7-U01/ 前缀）及 `candidates/R7-U01/evidence/author/` 中本批证据：
- required: candidates/R7-U01/audit/source-traceability.md
- conditional_same_record_not_automatic: candidates/R7-U01/deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md
- conditional_same_record_not_automatic: candidates/R7-U01/deliverables/final-specification-set/engine-overworld/wp14-random-dungeons.md
- required: candidates/R7-U01/deliverables/final-specification-set/generic-kernel/wp03-content-identity-and-schema.md
- required: candidates/R7-U01/deliverables/final-specification-set/generic-kernel/wp04-pbs-lifecycle.md
- conditional_same_record_not_automatic: candidates/R7-U01/deliverables/final-specification-set/pokemon-rules/wp23-shadow-data-and-vectors.md
- conditional_same_record_not_automatic: candidates/R7-U01/deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md
- required: candidates/R7-U01/deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md
- required: candidates/R7-U01/deliverables/final-specification-set/test-catalog/generic-kernel-wp02-03-04.md
- required: candidates/R7-U01/planning/feature-matrix.md

conditional_same_record_not_automatic 仅在同一必修有具体矛盾须同步时可提出并解释依据；不自动采用optional/policy。先完整读本批七组、已接非作者反证、固定源/消费者及必要历史向量，再以固定B字节建立完整镜像，按最低规则修改。不得复写更宽旧提案、复制参考表达式、实现TypeScript框架或改参考源码。

成果唯一远端分支：`codex/r7-u01-author-20261015-pilot1`。在你自己的独立容器/checkout中，以固定B `e646432c644dec04d306842cc5a559a29c718fbc` 为父输入创建该分支；如果当前已有未发布成果或同名分支，先读HEAD/status/远端和父会话task登记并保护原成果，不reset、不force、不覆盖别人的分支。若与整合者共享同一工作树，不切其分支，回报父会话取得隔离工作树。不要修改main、tag、旧报告、共享正式路径、公共台账或整合分支。

本派发依据父会话本次明确要求，**仅覆盖旧精简Prompt中“作者不提交、不推送”的成果传输限制**：允许对上述本批 candidates/ 范围做普通提交，并且只普通push到 `codex/r7-u01-author-20261015-pilot1`。不得推送任何其它分支，不合并main；仍由R7-I唯一写正式正文/台账。若分支已存在且非本task，保留本地成果并报告，不另选替代分支。返回实际commit/tree、普通push结果和远端完整字节核验。不要只回报容器本地绝对路径；新建文件及证据必须全部进入该候选提交。

交付 evidence/author/report.md、per-id.json、artifact-manifest.json。逐文件记录固定B的原blob/SHA/大小及新bytes/SHA/blob，精确scope/读写集/每项向量的阶段、正常/取消/异常/部分提交、未满足依赖、真实task/context及配置UNVERIFIED；保留真实命令/退出和可发布tool I/O，原私有模型流不作为公共证据推送。

候选提交对B的差异必须仅在 `candidates/R7-U01/`；不能夹带bootstrap/输入快照、其它批次或正式修改。R7-I先验证完整差异和身份并冻结candidate-input.json，再由不同实际context的独立reviewer核候选；候选PASS后R7-I逐条串行整合，共享贡献不得整文件覆盖，再交新的R7-IR核实际整合commit/tree。候选PASS、实际整合PASS、ACCEPTED、CLOSED严格分开。你只交 CANDIDATE_READY_NOT_REVIEWED，不自称独立PASS、ACCEPTED或CLOSED。

本首波U01/U04/U05没有相互共享目标；并不取消U01与后续批次的共享冲突。进度分母固定27项/13批，7 optional、2额外导航facet、1 no-required、2 policy不采用。L01–L14、静态/推导/工具/真实观察分层、有效配置UNVERIFIED、宿主/Demo/native媒体/真实存档回放0及旧56/92关闭边界保持。依赖未满足不提前关闭。
