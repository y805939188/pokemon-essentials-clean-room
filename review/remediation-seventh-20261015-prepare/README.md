# 第七轮云端整改开工核验与委派入口

当前派发登记：父会话已创建U01/U04/U05；U01/U05实际候选已接收并冻结、可创建独立ultra审者，U04按最近父回传仍inProgress。其余10批完整作者入口及13批ultra审者要求见[并行派发包](delegation/parallel-dispatch/README.md)。无用户并发数量上限；作者镜像可并行，共享实际文件仍由R7-I串行接收。有效配置UNVERIFIED，四阶段结果仍全部0/27项、0/13批。下文旧启动回执保留各自生成时点。

开工核验 READY_WITH_LIMITS；27必修（10 P2、17 P3、P1=0），13批。此提交仅冻结准备和委派输入，候选通过、整合后通过、正式接受、最终关闭均为0/27项、0/13批。

固定B `e646432c644dec04d306842cc5a559a29c718fbc`；固定发布C2 `4580645dfbfec4a3c7ccbad56ae293cc619b0d25`，workspace tree `1f4375e2a51801ed62bc143c1d51f70296fa52f3`，报告tree `a011f74704047f11ee47c9a631914337558cb81b`。Core和C1链、Prompt/Manifest完整大小/SHA/blob均匹配，见[startup/handoff-identities.json](startup/handoff-identities.json)。

实际云端项目 `/workspace/pokemon-essentials-clean-room`；只读参考 `/workspace/r7-reference`，HEAD `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。未操作用户Mac。`AGENTS.md`已完整读取，checkout及workspace无附加 `.agents/skills`。参考432、正式131、补充9、历史恢复43全字节匹配，见[最终启动核验](startup/identity-v2.json)；首次缺对象检查和普通fetch完整记录保留。身份核验不是新增语义审查或运行等价。

Manifest80MB已缓存并按顶层offset定向解析，原始C13七组与反证已从固定Core的gzip对象定向恢复549个逻辑成员到 `/workspace/r7-evidence`，逐编码/解码身份记录在[恢复记录](startup/evidence-recovery.json)。后续任务读取本批合同，不重复全包扫描。

13批作者阻塞入边为0，独立候选镜像无写写冲突；这不声明13个服务slot。共享接收图50目标含可选贡献，本次已分配候选目标42个。7个共享写入冲突组产生39次文件内配对、19对去重批次；原图48条还含读者/非必修范围。见[冲突组](delegation/conflict-groups.json)。

作者请求 `gpt-6.1-sol / xhigh / service_tier=default / 普通速度`；独立reviewer请求 `gpt-6.1-sol / ultra / default / 普通速度`；禁Fast。实际有效配置仍UNVERIFIED，真实task/context/PID与请求分开保存。所有reviewer须等待作者完成并由R7-I固定候选输入，不同时盲发26入口。

| 批次 | 必修ID | 作者前置 | 精简作者 / 独立审者 | 冲突组 |
| --- | --- | --- | --- | --- |
| R7-U01 | GR7-M01-001, GR7-J01-001 | 无 | [A](delegation/prompts/R7-U01-author.md) / [R](delegation/prompts/R7-U01-reviewer.md) | CG01, CG02, CG03, CG04, CG07 |
| R7-U02 | GR7-M04-301, GR7-M06-002, GR7-D06-001 | 无 | [A](delegation/prompts/R7-U02-author.md) / [R](delegation/prompts/R7-U02-reviewer.md) | CG01, CG06, CG07 |
| R7-U03 | GR7-M05-001, GR7-M06-001 | 无 | [A](delegation/prompts/R7-U03-author.md) / [R](delegation/prompts/R7-U03-reviewer.md) | CG04, CG05 |
| R7-U04 | GR7-M03-001, GR7-M03-002 | 无 | [A](delegation/prompts/R7-U04-author.md) / [R](delegation/prompts/R7-U04-reviewer.md) | 无 |
| R7-U05 | GR7-M07-002 | 无 | [A](delegation/prompts/R7-U05-author.md) / [R](delegation/prompts/R7-U05-reviewer.md) | 无 |
| R7-U06 | GR7-M09-001, GR7-M10-001 | 无 | [A](delegation/prompts/R7-U06-author.md) / [R](delegation/prompts/R7-U06-reviewer.md) | 无 |
| R7-U07 | GR7-M12-001 | 无 | [A](delegation/prompts/R7-U07-author.md) / [R](delegation/prompts/R7-U07-reviewer.md) | 无 |
| R7-U08 | GR7-M13-001, GR7-J16-001, GR7-J16-002, GR7-J16-003 | 无 | [A](delegation/prompts/R7-U08-author.md) / [R](delegation/prompts/R7-U08-reviewer.md) | CG06 |
| R7-U09 | GR7-M14-001, GR7-M14-002 | 无 | [A](delegation/prompts/R7-U09-author.md) / [R](delegation/prompts/R7-U09-reviewer.md) | CG05 |
| R7-U10 | GR7-M15-001, GR7-M15-002, GR7-M17-001 | 无 | [A](delegation/prompts/R7-U10-author.md) / [R](delegation/prompts/R7-U10-reviewer.md) | CG01, CG02, CG03, CG07 |
| R7-U11 | GR7-M16-001, GR7-M17-002 | 无 | [A](delegation/prompts/R7-U11-author.md) / [R](delegation/prompts/R7-U11-reviewer.md) | CG01, CG03, CG07 |
| R7-U12 | GR7-M19-001, GR7-H08-001 | 无 | [A](delegation/prompts/R7-U12-author.md) / [R](delegation/prompts/R7-U12-reviewer.md) | CG01, CG07 |
| R7-U13 | GR7-D07-001 | 无 | [A](delegation/prompts/R7-U13-author.md) / [R](delegation/prompts/R7-U13-reviewer.md) | CG01, CG04, CG07 |

逐批精确写入路径、条件路径、完整七组、前置及接收条件见[可机读清单](delegation/batches.json)和 `delegation/contracts/<批次>.json`。所有作者只写 `candidates/<批次>/<完整目标路径>` 和本批证据。条件同步须指出同一必修的具体矛盾；7 optional、2导航facet、1 no-required、2 policy均未采用。

R7-I是唯一整合/公共登记写者：先固定候选bytes及作者context → 不同实际context reviewer逐项候选PASS → 按实际条款串行整合并保留已整合贡献 → 新的非作者R7-IR对实际整合commit/tree及差异复审PASS → R7-I正式ACCEPTED → 具体共享接收、直接/传递依赖与历史回归满足后才CLOSED。可按U01–U13稳定顺序接收已PASS候选，但该顺序不虚构作者依赖；仍等待的批次不能提前关闭。

正式接收必须绑定实际输入、完整最低规则、必要正文/向量/反向消费者和正确保留scope；静态可判定项无宿主也可有限验收。L01–L14、实际配置UNVERIFIED、宿主/Demo/native媒体/真实存档回放0均保留；未运行向量保持NOT_EXECUTED。R6原56/R5原92关闭证据和所有旧状态不改。

所有新成果仅在整改分支普通提交/推送；不合并main、不force、不移动tag、不删历史。当前进度见[ledger.json](ledger.json)。

指定配置CLI启动尝试 R7-U13-A-01（真实PID1417）在创建thread前因只读文件系统退出1，无thread ID、无候选。此为执行环境障碍，未触发自动批准拒绝。原stdout/stderr、请求与退出留在[启动尝试](launch-attempts/R7-U13-A-01/reception.json)。未改用其它模型/速度；当前可直接由父会话创建13作者，独立reviewer等待冻结候选。真实任务启动数0，候选/整合PASS、ACCEPTED、CLOSED仍全部0。

精简prompt与合同的固定提交为 `f622356f`；完整提交和路径见[固定委派绑定](delegation/fixed-dispatch-binding.json)。

同一云端环境恢复已确认，原准备成果及本地证据保留，未重复派发作者。独立容器不能假定共享本环境绝对路径；请使用[逐批跨容器恢复说明](recovery/independent-containers.md)、`recovery/batches/<批次>.json` 和 `tools/restore_container_context.py`。恢复工具只取具名固定证据及读输入，不扫描80MB Manifest、不创建任务。U01远端/续传和U08共享编码对象回执已保存；这些是同环境隔离目录试验，不宣称真实独立容器验证。原prompt和合同固定提交f622356f不变。
