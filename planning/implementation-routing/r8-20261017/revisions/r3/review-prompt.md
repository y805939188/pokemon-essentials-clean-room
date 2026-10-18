# R8 去向打标 R3 固定候选累计独立复审

当前后继为七行来源摘要作者修复候选；请先使用[有界复核提示词](../r3-calibration-repair/review-prompt.md)。下文保留原完整R3检查与固定输入，作为既有PASS信用和必要传播的核对背景；本轮不要求重开所有已通过范围。

受审候选为**父任务调用消息给定的完整40位SHA**；缺失时不得以浮动分支/工作区HEAD代替。请求真正非作者 `gpt-6.1-sol / ultra / service_tier=default / normal / Fast off`，由父线程云任务创建。请记录创建参数与有效执行echo的区别；缺权威echo的model/effort/tier/speed/Fast/云UUID逐字段UNVERIFIED，工具广告priority或逻辑任务名不证明default/云UUID。审查分工构成一份独立审查，不增算接受票。

本任务是独立语义与结构复审，不是作者续修。仅在新的独占review路径写输出，不修改作者候选、正式规格、参考仓库、R1/R2历史或main，不修清单来取得PASS。不运行Ruby、参考游戏、业务场景、宿主、Showdown/框架原型或新实现。读取根AGENTS及用户 `review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/inputs/review-SKILL.md`；尊重既有clean-room与文档格式，不凭技能推定需要额外用户批准才可进行只读复审。

## 固定输入

必须在独立环境取得并逐SHA绑定以下对象；它们不都位于打标分支祖先线上：

| 角色 | 固定SHA |
| --- | --- |
| 新R3候选 | 父调用消息提供40位SHA |
| R2候选 | a32873d2860b15d9f5e27727db8f131f4ec433b6 |
| R2独立FAIL | 0ef0b7ad5f9465cfe31da0d7a35f56b5ccba5add |
| R1候选 / R1 FAIL | 5666b7b912e2fb79b5119283ee6a37401a7071db / 8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8 |
| 初候选 / 初FAIL | d62b41f4d620e50bb04c80a7505374bd284d8210 / a0352c7fba38391afc535525988245701d5ce202 |
| B8来源 / R8交付 | fd1df570cad987dc3852a3b958f03916e317f7fe / 4575e80d041ab0c74a42e2e36399d05791dbaa5b |
| 当前累计接受源码 | 5f87743293290de2e219ecdd6c19e88280f60c9a |
| 完整累计输入包 | 8336249c78b4698cd77445653d3b05ff6a76ce94 |
| U04最终回执 / actual报告 | a974eb133bdb280ac46f2684df4b309a18fc6cc1 / 40f428ef33d9b09ba9cc584ef4794779cc9869cb |
| U02/U03回执 / actual报告 | 861f7a44a6f763c265a11761ab17a8ec3b55f304 / 548d6bb9a21d0967680445c013e66d9d5661d2d6 |
| 五批回执 / actual报告 | e042c2f061eb2951a8d662a5987804e3314cb6b4 / 834888e29f939d0a5ed9478d763deb86eb021211 |
| U06回执 / actual报告 | 3157ef455fdac41f0bf5485b281ef2e1699c8599 / 8f71c18480a847348b8450c9df1e7e8194c03985 |

R2报告目录为 `review/r8-disposition-r2-independent-a32873d-20261017/`，有94输出；完整读REPORT、findings、六域报告、相关逐行/逐组/读取范围结果，机器派生数组和脚本可完整解析但不得冒称语义全文。R3作者对94输入的台账在 `revisions/r3/tools/r2-review-input-ledger.json` 和 `revisions/r3/review-input-consumption.json`，须独立核身份，不以作者声明代替结论。

累计包入口为 `review/remediation-eighth-20261016-prepare/accepted-cumulative/calibration-input.json`，11文件含9回执、39项证据链、131身份、38完整差异、21新标题和UI65最后两行修订。包内引用的固定对象也须取得。参考固定commit为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，只读。作者工作区正式子树仍B8 `f292698cdd4a8e725525a9be6dc34b75faaf151e`；当前正式树为5f的 `93dc967b4cdb653359afc123d3b8b318d6475fdd`。必须从fixed current Git对象读当前正文，不能把B8工作区当current。

## 审核目标及判定尺度

实际正式索引应重新计算，历史131文档/87WP只是核对；当前观察131文档，736活跃、33完整退役/33metadata，历史2683标题/当前2704（新增21）。五类承载为框架、Showdown、协作、MZ、用户明确不纳入。每行固定source/当前适用/未来计划/去向验证/实现/目标验收/阶段批准分别判断；来源静态PASS、引用或数值一致都不能证明目标行为覆盖。

按章节粒度，跨承载/验收边界才细分，不要求逐句/逐向量新ID。不把责任表/来源清单/静态用例伪装为实现功能。目录可章节聚合，允许明确父→excluded_child_refs→子或具名共享合同的间接导航；不要求重复所有最细ID。依赖可表示前置、共享、消费者或具名排除性对照，必须有实际用途，不能按同WP/标题相邻或只看字节相等授PASS。

捕获、背包战斗道具、逃跑、战中成长保持协作原型候选。未执行原型、目标版本未固定及仍未批准首版细项独立登记，不因尚未运行就否决合理粗标，也不将其说成兼容已验证。Shadow、设施、特殊玩法、作者工具、XP/旧格式不自动排除；必须用户明确范围决定才允许“不纳入目标”。

## 必须逐项复核的 R3 返修

1. **7项R2问题及28行依赖**。作者 `revisions/r3/finding-resolution.json`、`dependency-repairs.json`、`source-refinement-patch.json` 是被审陈述。逐四组源和目标有效scope判断，保留不受影响分类/职责/scope。
   - COMBAT-R2-DEP-001：61/66/69→739错PP边；740真实持物边保留，68/71→739真PP对照不能一并删除。
   - R2-CRE-DEP-001：186/190退款须落WP42正常终局§6/6.0/31，而非外层世界治疗32；192 Mist建立/期限须WP45§6.2/39，非交换清除40。
   - R2-CRE-DEP-002：244 GiftMaster/会话/Export/线上四层与263/265六类PBS工具区别；741奖金统计420与421货币组区别；742真实共享训练家编辑器保留。
   - POK-WORLD-R2-DEP-001：348/372/373/487/608/664/681/682/749/751/754/755/756/757/759/764/760/761/762/766共20行；按实际领域源/目标修正异体系及错章节边。作者在相同scope还清751/760→355与664→159/160/161，须核真实理由及替代365/366/364/存储/过滤使用等是否准确，没有盲删、同号替换或设计扩展。744训练家数据卡、735学习排除对照、741→579→755和753诊断等正确导航不因间接性自动判错。
2. **3项来源工具缺陷**由父作者修复，见 `revisions/r3/tool-finding-resolution.json`：SOURCE-R2-001旧回执不能授权同路径后继未接受字节，全部文档current snapshot须等于全局snapshot（包括无活跃功能的纯元数据文档）；SOURCE-R2-002完整prospective coverage在核心/归档写入前符合schema（不是dict.get保留null）；SOURCE-R2-003治理豁免仅固定三文档/46标题，普通行为章不能用ALL_FORMAL_FEATURES清空消费者。必须复核代码和隔离真实Git/JSON负例，不预授工具PASS。
3. **6行当前源职责/依赖精化**：645/647 final UI65 L152/L210与WP12独立跳跃/普通移动门；92原始类型候选/PP限定计算类型匹配/一次+14、普通User/0不消费贡献；397十五蛋群固定作者身份与WP18/33/34分工；699/703七图像语言选择、实际高度、空译分入口失败和对象/随机/音效/财务前缀。类别不变不能代替判断职责是否充分。新current锚点不能伪装为B8已存在的direct_ref。
4. **全源累计应用**：核9真实ACCEPTED事件及39项（29required+10optional），40目标贡献、38变更文件、131current身份及736locator；原计划义务保留，6份实际扩展文档纳入。230已绑定行全部backfilled、0pending/0partial，39新增绑定/47新增或扩展的口径分别核。UI65旧U01历史贡献不等于当前全文已接受，final U04须实际绑定最后两行修复；较早U04实际FAIL只由真实后继报告/回执覆盖，不改写历史报告。
5. **21新增标题/2704当前覆盖**：全部现有feature/meta消费者按final5f正文判断，原10pending必须实际重估，不能只改状态；历史2683覆盖字节保留，新增current范围/标题/层级/末行/归属与身份从Git独立重算。metadata消费者精度与退役replacement、覆盖导航同步，不新造伪功能。
6. **保全及合理PASS传播**：从35175接受后归档＋统一逐字段before/after重建整个manifest，与最终字节/对象核对。补丁78行/162字段，保持全部source、ID、current/upstream、类别/伙伴、阶段/实现/验收，future职责仅6行精化、依赖28行修复与51源差异注记交集明确。33退役完整旧体仍等于初d62对应行，33metadata、历史source/覆盖及58份R1/R2历史工件原字节保全。R2的708 PASS/28 FAIL以及736分类facet PASS是旧判断；新源/目标引用/6职责受影响facet需要实际重审，其余可有固定身份及不受影响依据后有限继承。全44原组/12R1残留/721旧ID历史保留，不能把R3作者映射当独立通过，也不能字节相等证明引用真。见736行 `feature-resolution.json`、`facet-inheritance.json` 与44组 `retained-pass-propagation.json`。

## 工具事实及必须保留的失败证据

作者最终 `cumulative-source` 10命令全部exit0，17登记输入hash稳定；27结构负例、9自检、2导航负例、11生成物一致、19保全、5接受绑定负例、2704覆盖/4负例、4来源门隔离夹具（覆盖3项工具问题）通过，36父/39子/39边导航，另最终校准15检查通过。请在独立fixture重放并核真实argv/stdout/stderr/exit/UTC/前后hash；不要把这些作者检查等同语义审查。

首次累计apply沿当时旧代码实际写入后，完整current schema暴露1776 null；旧代码gzip、初始I/O、失败full result和后续归一化保留。现行prospective guard的隔离新检查在写核心及归档前拒绝注入null。请核真实时序，不能倒填“初次apply已有该门”。R2阶段的7命令/5扩展和2704 NOT_EXECUTED_AWAITING_U04是该固定历史当时事实，R3现在实际执行后继检查，不回写旧证据。根 `backfill-contract`、handoff、unresolved、README/prompt应一致为当前R3最终态。

推荐入口：`routing.py validate`、`routing.py check-generated`、`revisions/r3/tools/run-author-checks.py --phase cumulative-source`。重放应在不把review untracked文件混入作者工件集的独立fixture进行；保留真实失败与修后结果，不修改候选绕过工具。静态脚本可执行，业务/原型不执行。

21条heading证据的旧source_identity.heading_sha256按SHA256_UTF8_TITLE_ONLY保留，新加raw_markdown_heading_sha256按原Markdown整行；current locator使用整行hash。须按声明各自验证，不能把两口径误报为漂移，也不能借口径之名跳过unit/file/consumer核对。初映射字节与sourceapply I/O匹配并gzip归档，initial probe与后续15项proof分开保留。

## 输出与资格

输出完整独立REPORT、7问题及新增同根finding、逐736活跃/33metadata/721旧ID与44组的限定facet结果、131篇阅读台账及2704章节映射核验、工具真实I/O与负例/保护结果、精确输出字节清单。每个FAIL给具体固定源/目标有效区间、JSON指针、可区分反例和最小必要修正。合理既有PASS保留，不为未知而强造新功能/框架设计，不以抽样代替受影响项完整判断。

阅读信用区分本轮fresh、按精确身份复用、定向摘录、标题/字节/JSON/AST机械解析；截断输出不得冒称全文。报告仅给新固定候选的有限独立结论，不宣布目标兼容、实现完成、用户范围/阶段批准或全轮CLOSED。全部736去向仍待验证、待定/未批准、未实现/未验收，四协作原型未运行，排除0。若缺固定对象/权威配置等，按实际限制登记；作者不能代签本人工作。
