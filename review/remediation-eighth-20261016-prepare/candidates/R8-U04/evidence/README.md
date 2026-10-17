# R8-U04 作者交付

六项必修已形成最终态候选，仅写本批六个合同镜像及独占证据。该交付等待真实非作者复审与协调任务正式整合；不是正式接受。

- `issue-dispositions.json`：逐项原证据、修改位置、区分正误的场景、固定源引用、保留义务、未决依赖与共享去向。
- `optional-dispositions.json`：按最新用户授权处理；本批可选分配为空，十项均交各责任批次，未跨批修改。
- `input-identities.json`、`contract-input-identities.json`、`reading-spans.jsonl`、`reading-ledger.json`：40完整源/规格单位、完整六合同与相关审计语义的身份和阅读范围。混合全局载荷只计本批及共同资格，不冒认其余body FULL。
- `final-composition.json`：已完整阅读原文与完整最终改文逐段接合，覆盖六份最终整文件全部行；不是独立审查。
- `candidate-manifest.json`、`validation.json`：六文件内容身份与文档结构/写集/旧内容保留检查；不验证游戏行为。
- `commands.jsonl`、`io/`：实际记录的文档校验与发布命令、真实UTC/exit/stdout/stderr。前段交互式fetch及阅读以平台会话工具输出和reading-spans为准，没有倒造其完整进程I/O。
- `tagging-handoff.json`：本次章节/锚点/行为变化，供另一个打标任务使用，不重新全面打标。
- `independent-review-entry.md`：完整独立复审入口、冻结及四门接收规则。
- `status.json`：配置请求与actual UNVERIFIED、职责及未决门。

旧catalog全部行除必改MP13外逐行保留；新增30条R8-PBS/NP/RP/JT/CE/LB有限对照。矩阵96个编号与28/2/66分类不变，仅117/119两行原位更正。WP11的GR3-MR/DQ、WP12的碰撞/路线WAIT/零跳与R7边界、WP13的R5-ID/冻结防护/101预读及原DG失败限定全部保留。

静态校验首轮把`git diff --no-index --check`的无诊断exit1误当失败；修正为允许差异退出码且必须无诊断后通过。原失败与后继通过均保留。这是工具判定修正，不是参考业务失败或通过。

作者未运行Ruby/游戏/行为模型/宿主、未开发框架、未改main/正式规格/公共索引，未强推。所有行为向量仍为NOT_EXECUTED。提交与远端回读的实际完整SHA由最终外部交付绑定，文件不编造自身未来SHA。
