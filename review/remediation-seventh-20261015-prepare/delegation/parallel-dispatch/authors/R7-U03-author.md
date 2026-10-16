# R7-U03 独立云端author派发

只执行本次具名角色，不创建子任务或其它作者/reviewer。父会话唯一负责 cloud_threads.create；无用户设置的并发数量上限，但不要把可并行当成已创建或服务slots证明。父会话已报告U01=01a13f52-add1-7706-b7ec-54e07e0d7013、U04=01a13f52-cc74-7568-9e75-85ac773c6015、U05=01a13f52-ecf8-73f9-8c9b-f5c164f0c017为inProgress，不重复创建它们。其它批次以父会话真实task登记去重；本静态派发文本不是创建回执。

本角色请求 gpt-6.1-sol / xhigh / service_tier=default 普通速度，禁Fast。模型/档位/速度的实际有效回参缺失时逐项UNVERIFIED，不以请求argv、自报或成功退出认证配置，不查额度/认证。实际task/context/PID、请求、UTC、完整可发布工具I/O和退出分开留存；私有模型流不作为公共证据推送。

仓库 https://github.com/y805939188/pokemon-essentials-clean-room.git 。输入远端分支 `codex/remediation-seventh-20261015-cloud`；固定准备提交 `4bd152023b4bcb3dd5a3654deffe75aeebc40f10`。行为基线B `e646432c644dec04d306842cc5a559a29c718fbc`，正式tree ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c。参考固定R为 Maruno17/pokemon-essentials 的8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b/tree7589c800b61ba13a13040ed0d686979b80a84fd0。只在云端工作，不操作用户Mac，不用浮动HEAD替代固定输入。先读实际项目AGENTS.md。

原完整七组合同：提交 `f622356f3beb9e84ea8cff9db07c7fb382565d3f` 的 `review/remediation-seventh-20261015-prepare/delegation/contracts/R7-U03.json`。
原角色入口：同提交 `review/remediation-seventh-20261015-prepare/delegation/prompts/R7-U03-author.md`。
固定恢复工具：提交 `658488c81f1f3181a488298ab27850c8af951d73` 的 `review/remediation-seventh-20261015-prepare/tools/restore_container_context.py`。
逐批证据恢复清单：同提交 `review/remediation-seventh-20261015-prepare/recovery/batches/R7-U03.json`。
跨容器说明：同提交 `review/remediation-seventh-20261015-prepare/recovery/independent-containers.md`。
上述固定文件可由 `https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/<完整固定commit>/<精确路径>` 读取，不必下载80MB Manifest或扫描完整core包。先完整阅读工具和本批清单再执行；不盲跑下载程序、不执行恢复出的参考/native程序。

独立容器不共享整合者本地目录。将工具和本批清单分别保存为 `/workspace/r7-bootstrap/R7-U03-author/tools/restore_container_context.py` 与 `/workspace/r7-bootstrap/R7-U03-author/recovery/batches/R7-U03.json`，运行：

```bash
python3 /workspace/r7-bootstrap/R7-U03-author/tools/restore_container_context.py --plan-directory /workspace/r7-bootstrap/R7-U03-author/recovery/batches --batch R7-U03 --destination /workspace/r7-context/R7-U03-author
```

工具定向恢复本批原载荷、身份/原绑定及L01-L14、固定源/正式读输入和冻结合同/Prompt。原 `/workspace/r7-evidence` 映射到 `/workspace/r7-context/R7-U03-author/evidence`；原 `/workspace/r7-reference` 映射到 `.../inputs/reference`；固定正文在 `.../inputs/project/`，原入口在 `.../dispatch/delegation/`。这些只是有界文件快照，不是完整Git checkout或运行认证。已有匹配恢复可复用；连接中断保留目录、同环境同目录加--resume，不覆盖冲突字节、不另起替代任务。有新的具体可读依赖应具名定向补取，不能伪标limit。

规格只描述可供从零重写的独立功能、逻辑、行为，不实现引擎/TypeScript包/适配器，不移植Ruby结构或复制源表达式。完整前提、普通对照、取消/异常/部分提交、最小规则、正确保留scope、消费者和历史回归按原七组及已接非作者反证审读，不复活已被反证排除的宽提案。7 optional、2额外导航facet、1 no-required、2 policy均未采用；同一必修的条件同步须给具体矛盾和依据，不自动扩大。

L01-L14和旧56/92关闭边界保持。SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、REFERENCE_OBSERVATION、独立完整模型、游戏宿主/Demo/native媒体/真实存档回放分开。未执行向量保持NOT_EXECUTED，身份/退出0不替代语义验收。有效配置UNVERIFIED，宿主等0不得提升。进度分母固定27项/13批；只有R7-I写正式正文、公共台账和整合分支，不改main/tag/旧证据、不force、不提前关闭依赖问题。

本批必修：GR7-M05-001、GR7-M06-001。作者前置批次：无；所有作者仅写各自镜像，可同时准备，不能因此同时覆盖共享正式文件。

## GR7-M05-001

{
  "最小行为合同": "WP12分开碰撞创建与正常完成：创建不改位置/距离/离格通知；完成仍发一般步通知并可能进入玩家后处理。WP61登记该可达来源，保留强制路线、解释器、自动运动及消费者中断门。",
  "正确保留范围": [
    "不是所有失败移动/碰撞创建立即全局+1；非玩家受阻不新增此计时。",
    "保持普通移动开始写位置/距离、完成再玩家计步；WP13/MR02与WP06守卫正确。",
    "默认毒伤关闭；不主张默认中毒损伤，也不称只有所列三字段变化。空寄养仍可推进自身周期。"
  ],
  "禁止扩大": "本中文视图不得复活已被反证排除的普通游戏故障、统一事务、宿主成功或未来架构强制。"
}

{
  "验收条件": [
    "正文、目录及必要同步只陈述本记录最小行为合同，所有保留范围均不变。",
    "按下列具名前提/普通对照/取消/失败/部分提交分别核验；执行阶段按第七组真实证据标记。",
    "后续实际变更须由非作者核验，根接受中文视图不等于已经修订或关闭。"
  ],
  "回归向量与可判观察点": [
    "碰撞返回/完成两点分别观察B、坐标/距离、全局/友好/Repel。",
    "仅前方通行对照；触碰成功及失败对角无新碰撞链。",
    "强制路线碰撞并用合法WAIT保持forcing到完成：一般通知后早退，无玩家周期/Repel推进。",
    "未完成或一般消费者失败：只断言实际前缀。"
  ]
}

## GR7-M06-001

{
  "最小行为合同": "WR01应直接给显示坐标x实际增加128子像素（无放大、前后独立量化），或补居中跟随/无旧卷动/无钳边条件，并增加玩家右移而镜头不移的对照。",
  "正确保留范围": [
    "WP16量化/邻图/镜头时长/钳边/中心规则与GR3-CAM06–08保持。",
    "不提出新镜头算法、整文重写、像素可见或对象复用保证。"
  ],
  "禁止扩大": "本中文视图不得复活已被反证排除的普通游戏故障、统一事务、宿主成功或未来架构强制。"
}

{
  "验收条件": [
    "正文、目录及必要同步只陈述本记录最小行为合同，所有保留范围均不变。",
    "按下列具名前提/普通对照/取消/失败/部分提交分别核验；执行阶段按第七组真实证据标记。",
    "后续实际变更须由非作者核验，根接受中文视图不等于已经修订或关闭。"
  ],
  "回归向量与可判观察点": [
    "小图右移显示0；居中大图320→448。",
    "30×20、SnapEdges真、显示x1792向右仍1792。",
    "已有手动卷动只按在途任务，不按人物位移推镜头增量。"
  ]
}

精确允许写集仅为下列完整候选镜像及本批 `evidence/author/`：

- required: `candidates/R7-U03/deliverables/final-specification-set/engine-overworld/wp12-terrain-movement-vehicles.md`
- conditional_same_record_not_automatic: `candidates/R7-U03/deliverables/final-specification-set/generic-kernel/wp06-time-random-steps-stats.md`
- required: `candidates/R7-U03/deliverables/final-specification-set/pokemon-rules/wp61-field-passive-effects-and-blackout.md`
- required: `candidates/R7-U03/deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md`
- required: `candidates/R7-U03/deliverables/final-specification-set/test-catalog/engine-overworld-wp16.md`
- required: `candidates/R7-U03/deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md`

冲突组：CG04, CG05。父会话/R7-I使用固定 `f622356f3beb9e84ea8cff9db07c7fb382565d3f` 的 `review/remediation-seventh-20261015-prepare/delegation/conflict-groups.json` 中各实际路径和当前完整合同判定共享接收，候选隔离不等于正式合入无冲突。

在自己的独立容器/checkout从固定B `e646432c644dec04d306842cc5a559a29c718fbc` 创建唯一成果分支 `codex/r7-u03-author-20261015-wave1`。如存在同名分支、未发布成果或父会话已登记本批实际task，先核HEAD/status/远端并保护原成果，不覆盖、不reset、不force、不自换替代分支；若共享整合者工作树，不切换其分支，回报父会话取得隔离工作树。

本派发按本轮普通提交/推送授权和父会话要求，**仅覆盖旧精简入口“不提交/不推送”的成果传输限制**：可普通提交本批candidates镜像及证据，只普通push至 `codex/r7-u03-author-20261015-wave1`。与B的差异必须全部位于 `candidates/R7-U03/`；不夹带bootstrap、恢复输入、其它批次、正式文件或公共台账。不得推送整合分支或main，不合并main、不移动tag。原行为合同和验收范围未改变。

以固定B原字节建立完整镜像，定点修订最低规则。交 `candidates/R7-U03/evidence/author/report.md`、`per-id.json`、`artifact-manifest.json`：逐文件原B/新bytes/SHA/blob、精确scope/读写集、全部必要向量的阶段/结果、失败/取消/部分提交、未满足依赖、真实task/context、请求与实际配置资格、命令I/O和退出。新文件必须进入候选提交，不只回报容器绝对路径。

返回真实候选commit/tree、唯一分支、普通push和逐新文件完整远端读回证据；完成后冻结停止写入。只报告 CANDIDATE_READY_NOT_REVIEWED，不自称独立PASS、ACCEPTED或CLOSED。R7-I核完整差异/身份后生成candidate-input.json，再由不同实际context的ultra reviewer审候选；之后R7-I逐条整合，再由新的R7-IR审实际整合字节。候选PASS、整合PASS、ACCEPTED、CLOSED分开，共享接收和直接/传递依赖/历史回归未满足保持OPEN。
