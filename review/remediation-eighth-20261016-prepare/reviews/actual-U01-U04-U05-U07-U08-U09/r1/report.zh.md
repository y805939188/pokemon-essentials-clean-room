# R8 六批实际整合独立验收 r1

固定输入 `56cc0f683249bd54658b94134d1a61be6e8748e0`；实际快照 `49a558f7d5498680ba88d532f3815e07d7844459`；登记核对 `3cc8e017c6629a0fc8cb0827bc16dda0e9adca91`。结论仅适用于这些固定字节。本报告没有替 owner 登记 ACCEPTED/CLOSED，也未给 U06、打标或整轮签收。

| 批次 | 必改／已选可选 | actual integrated 结论 | 依据与剩余门 |
| --- | --- | --- | --- |
| R8-U01 | 2／1 | **PASS** | 必须接收返修 c877e66d 与 c56790b 独立 PASS；旧 FAIL 保留。保存有序失败、空旧格式、普通 No 与共享地图名副作用均落实。 |
| R8-U04 | 6／0 | **FAIL** | 六项主责正文均落实，但 GR8-WORLD-003 的 UI65 必要入口未同步计时定义，见 ACTUAL-U04-001。其余五项 PASS。 |
| R8-U05 | 2／0 | **PASS** | 濒死首非蛋 Repel 分支、负遭遇步数及累计前提准确，消费者时序与原控制保持。 |
| R8-U07 | 3／1 | **PASS** | 后继 metadata overlay；历史不改写，r2/续审/输入时点分别绑定；**NO_FORMAL_DELTA**。 |
| R8-U08 | 1／0 | **PASS** | 七语言角色及两必要消费者同步；原四族与固定资源保持，N01 非阻断限定保留。 |
| R8-U09 | 2／5 | **PASS** | EggGroup15值、MG命名及五 optional准确；共享Creature全文原127 ID保持，仅MG-32行精化。 |

23 项全部逐项审读：15/16 required PASS、1/16 required FAIL，7/7 selected optional PASS。逐项反例、最强反方、正式去向及保持范围见 [per-id.json](per-id.json)。候选报告的 PASS 只是输入资格，未代替本次实际结论。

## 唯一阻断：ACTUAL-U04-001（P3，原 GR8-WORLD-003）

实际 UI65 §6.1（第152行）及 §8.1（第210行）继续独立使用“玩家未移动／静止”描述菜单、快捷与已有调用的同一末端门；§8.1只回指自身§6.1，没有绑定 WP12 的新计时定义。WP12 第175行明确限定“本段”的静止仅为无普通移动／碰撞计时，第183行又给出仍在跳跃时可请求菜单／快捷的有限例。

固定 R 的完整 Scene_Map、Character、Player、Overworld_Metadata 与 Game_Temp已审读。直接 (0,0) 跳跃只建立 jump_timer；在合格的下一普通轮0.01秒、跳跃尚未完成、消息假且登记门放行时，ACTION/SPECIAL分别可登记并消费。只有普通移动计时的对照则不登记／不消费。UI65 自足入口仍留下原 required 根因所针对的合并运动状态歧义。

最强反方是主责 WP12 已正确且合同最小写集未列 UI65，候选独立报告也给六项 PASS。本次实际协议及 manifest另要求具名 UI暂停／快捷／debug 必要消费者按实际文本接收；因此不能仅凭主责局部定义或镜像相等签该接收。这里不据“强制移动”一词断言它必然指强制路线，也不新增第九轮问题。

最小回修：仅在 UI65 §6.1明确本门“未移动／静止”=无普通移动／碰撞计时，跳跃独立不额外阻止，并链接 WP12 `#r8-terminal-motion`；§8.1沿同一定义。复用 R8-JT01–06检查消息早退、新登记／已有消费、菜单禁用与优先级，保留原 UI取消和失败前缀。详见 [findings.json](findings.json)。本审者未修改正式文本。

## 身份、完整性与保护

- 25实际目标（24正式文件＋1 metadata overlay）均全文阅读，非抽样。实际正式 diff 的新增／上下文由全文覆盖，全部删除行及文件／hunk头另读；机械证据确认 patch 精确等于固定4575→49a558的24文件 `git diff -U0`。25目标与正确候选镜像相等，49a558→3cc8也不变。
- U01只接收 `c877e66d7011e5e1a0bb9b43ba39cbb15255064d`，独立回检 `c56790b0654d48616f2479dd86cd1bd310287cce`。返修镜像与旧版同字节不消除旧FAIL；三次命中短前缀勘误独立接收，没有把它写成第三次删除。
- Creature公共目录全文保持127唯一原ID：EG20／EN32／FC17／TT26／MG32；141次全部ID出现及顺序保持，MG-32原行只有一处。MG族32不是整文件分母；Factory、Triad、E相关保持范围和旧别名分别核对。
- 正式全集131份，累计26变更／105未变；本组六批24正式目标之外的先前 U02/U03两目标及其已接受报告／回执完整保持。机械40项中39相等；唯一更强比较不相等项是旧U02/U03输入后的活跃 integration-plan.json更新，非已接受正式／证据损坏。
- 86168条现存历史review路径保持。U07仅后继overlay；旧WAIT、程序违例、r1/r2、作者与辅助资格、L01–L14及历史运行0不改写。当前metadata接收涵盖R7资格、历史资格、U06续审资格及供唯一整合者审核四facet，同一context不虚增票。
- 公共audit/planning当前头明确限定旧批准不转授，相关旧行是保留历史导航；无需自动改写历史行。正式owner引用与本次目录单独核对；空public_contributions没有掩盖UI65缺口。跨批 X01–X10与必要接收见 [cross-batch-and-receptions.json](cross-batch-and-receptions.json)。

## 实读与验证资格

完整AGENTS、原review-SKILL、六批提示／23合同及三个公共伴件均已读取；重复完整合同以严格类型和值去重，全部1113不同语义值及1282行提示义务实际审读，原JSON指针可追溯。readset中95条明确父身份记录不冒充本审者全文；foreign U06范围保持可见且不授其PASS。25正式／metadata目标、六候选报告、作者handoff、必要当前消费者和有界源单元分别在 [reading-ledger.json](reading-ledger.json)记载。76个具名参考源范围已全部覆盖；33个B8正式范围中26个通过已读实际全文／删除行精确去重，另7个79行直接补读，见 [读集覆盖](reading-coverage-check.json) 与 [后继补读](reading-coverage-supplement.json)。只做必要source静态推导，没有扩大成131文件全局或第九轮审查。

父任务提供2026-10-17 14:27 UTC明确cloud创建请求与started admission：gpt-6.1-sol／ultra／service_tier default。该请求／创建证据与运行时回显分开；运行时仍 **UNVERIFIED**，缺失本身不阻断语义结论。仅此实际context作语义裁决，机械辅助不投独立票；详见 [input-and-configuration.json](input-and-configuration.json)。参考、Ruby、游戏、业务模型、编译／转换／反序列化、素材和原生宿主执行均 **NOT_EXECUTED**。Python/git检查只验证文件、JSON、身份、链接和计数，未执行业务向量。

[mechanical-checks.json](mechanical-checks.json)记录输入／目标／保护身份；[link-and-diff-checks.json](link-and-diff-checks.json)记录23新增本地链接、15 fragment、29标题／anchor以及远端main和参考clean检查。它们是辅助证据，非语义PASS证书。独立分支普通push与独立对象库远端回读将由同目录publication-receipt记录；最终输出SHA在任务答复给出，避免报告自引用未来commit。

剩余：U04最小回修与后继独立actual复核；其它批的owner ACCEPTED／最终CLOSED及U06／打标／整轮门继续由各自授权流程处理。本组六批五份PASS不自动满足这些外部门。
