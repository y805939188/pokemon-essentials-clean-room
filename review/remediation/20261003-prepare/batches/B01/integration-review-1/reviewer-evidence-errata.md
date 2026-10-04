# R-B01 证据后继更正

本文件只更正 reviewer 的证据，不改候选审查原件，不改原 finding 或作者正式输入。

## R-B01-I-ERR01：上轮“七断链”支持检查的清单与匹配错误

固定旧报告提交 `c919657840bb09394ce03a8a8688b02666f030dc`，文件 `review-round-1/verify-input-identities.py` 第209–217行和 `independent-validation.json` 同名检查。手列七项包括正确的 `pokemon-rules/wp69-voltorb-layouts.md`，漏掉 `user-interface/wp70-mining-data.md`。旧脚本用两层回退子串检索，再人工构造两层目标，没有核所写完整路径；该子串可以出现在正确三层回退路径中。因此该旧PASS支持检查无效，旧report中“39项均通过”的有效性声明对这一项应由本更正限定。

从固定原全局报告 `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 的 GIR-FD82-001 / RUN-C-132 原证据独立抽取正确七项：

1. `deliverables/final-specification-set/creature-rpg/wp68-triple-triad.md`
2. `deliverables/final-specification-set/user-interface/wp68-duel.md`
3. `deliverables/final-specification-set/user-interface/wp69-slot-machine.md`
4. `deliverables/final-specification-set/user-interface/wp69-slot-reels.md`
5. `deliverables/final-specification-set/user-interface/wp70-mining-data.md`
6. `deliverables/final-specification-set/user-interface/wp70-mining.md`
7. `deliverables/final-specification-set/user-interface/wp71-tile-puzzles.md`

它们在 e1e01bb／PRE0／c7候选／实际93d整合中均为原字节；正文定界路径为 `../../audit/source-traceability.md`，均解析到不存在的 `deliverables/audit/source-traceability.md`。正确三级回退解析到已有 `audit/source-traceability.md`。Voltorb附表实写 `../../../audit/source-traceability.md`，是可达正确对照，不能列为断链。

本轮两个检查从完整代码跨度／Markdown目标定界符解析实际路径，读取Git树验证存在性，结果见 [independent-validation.json](independent-validation.json) 与 [scope-manifest.json](scope-manifest.json)。不得用子串匹配替代实际目标解析。

更正处置：**旧支持检查已被本轮独立证据替代**；旧报告六文件字节原样保留。原finding七断链结论及P3仍成立，候选proposal-only和当前局部入口修复结论保持；B18/B21实际七处欠项未消除，不关闭任何规范ID。该事项属于reviewer支持证据纠错，不是本次作者整合新finding。

## 本轮检查器开发记录

最初将scope §5完成度变更误认成§4，评论中拟提出P3；真实标题分节及逐字比较证明§2/3/4均未变，作者断言成立，立即公开纠正。该拟议问题由证据否定，未作为正式finding发布；没有静默降级有效finding。

本轮开发还修正了路径为代码跨度而非点击链接、旧current-hashes仅含本批六份最终／目录而两份原规格在dated manifest、完整diff的patch空白诊断应与正式／公共文本分别核验这些假设。最终独立41项检查均通过，全部是文本／Git／JSON检查，行为向量没有运行。
