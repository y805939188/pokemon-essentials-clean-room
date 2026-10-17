# Pokémon 域 R1 独立复核

固定候选 `5666b7b912e2fb79b5119283ee6a37401a7071db` 的本域结论为 **FAIL，仅剩目录消费关系的两项 P3**。POK-S01–S08 八组原问题均已实际修复；165 个旧行逐一新判 PASS（含 8 个完整退役行），181 个活跃行逐一 PASS（含 24 个新增行），8 份元数据分类和消费者导航 PASS。上述 PASS 是静态粗标结论，不是目标兼容、实现、运行或 R8 最终验收。

全部逐行理由、原 case、父子范围、阅读信用和新问题见 [pokemon-results.json](pokemon-results.json)。独立 Git/范围/定位/视图检查见 [pokemon-mechanical-evidence.json](pokemon-mechanical-evidence.json)，可复现脚本为 [pokemon-audit.py](pokemon-audit.py)。

四份目录共 47 个元数据章节另有逐节判定：30 PASS、17 FAIL（16 节同号误连，1 节缺 724）。功能行 PASS 与这些目录层 FAIL 分开计数。

## 固定身份、范围与配置

- 旧候选：`d62b41f4d620e50bb04c80a7505374bd284d8210`；旧 FAIL：`a0352c7fba38391afc535525988245701d5ce202`。已核旧全局逐行裁定与本域 128 PASS / 37 FAIL 一致，无被全局覆盖后漏收的本域 verdict。
- B8 与候选正式树：`f292698cdd4a8e725525a9be6dc34b75faaf151e`。当前接受 payload：`908273093e1f6b27fc58249417675dd62d146224`，正式树：`6ae817df5b11eafdec671214b0d04e542ad364bc`。从固定 Git 对象读取当前树果正文，未用工作区 B8 字节冒充 current。
- 负责 27 份正文、4 份相关静态目录。旧全文信用为 4,919 正文行及 1,144 目录行；本轮采用字段差分后的合理继承与受影响源节/混合表/消费者定向重读，没有声称重新全文读完全部 31 份文件。
- `/root/r1_pokemon` 是分工角色；真实云任务 UUID、实际 model、effort、service tier、speed、Fast 均 **UNVERIFIED**。父任务请求 gpt-6.1-sol / ultra / default 不作为有效执行 echo。
- 只分析 Markdown/JSON/Git。Ruby、参考游戏、Showdown、宿主、框架、业务向量和四类原型执行均为 0。

## 剩余必修

### POK-R1-CATALOG-001 · P3 · 新补漏单元 724 未接入其具名静态目录

位置：`section-coverage.json#/sections/2275/feature_refs`。来源为 `test-catalog/pokemon-rules-wp43-44-46-48-50.md` L270–283 的 R5-U04 / FB01–FB06，明确唯一主合同是 WP43 §2.1。

新增 `FR-000724` 正确承担源 L29–36 的未知效果变化失败、伤害回退、PP 前缀及 SHADOWSHED 绑定边界。但本目录仍仅引用旧 WP43–50 功能集合；沿所有明确 `functional_scope.excluded_child_refs` 和 `dependencies.feature_refs` 的机器导航闭包均无法到达 724。724 是原先漏标后追加的独立行为，没有旧父可以间接承接该关联。

必要修正：在该具名目录章节关联 724，或提供清楚等价的显式消费导航。无需逐 case 新造功能 ID，也不改变静态未执行状态。

### POK-R1-CATALOG-002 · P3 · 同号不同体系的反向误连仍存在

位置：`section-coverage.json#/sections/2277` 至 `/sections/2292` 的 `feature_refs`。`test-catalog/pokemon-rules-wp53-60-61-62-69-70.md` L3 明确对应 Safari/捕虫、Berry、Field、Pokédex、Voltorb、Lottery 六份正文；本次新读区间与身份相同的旧完整阅读共同确认该范围。

这些 16 个章节仍统一关联 Fishing 的 `FR-000380–387`、Slot 的活跃 `FR-000699–706` 子集、Mining 的 `FR-000708–712` 及新增 `FR-000728/730`。例如树果 BP 与彩票 LT 章节均带这些不同体系的 ID。共享 WP60/69/70 编号不能证明目录消费了它们。这是 WORLD-CATALOG-F01 同根因在本域方向的遗漏传播，交 root 与世界目录主审合并。

必要修正：按目录明确正文或具名后继单元移除错误子体系关联，保留真正的跨域地图、消息、持久状态等消费关系。可保持章节级粗导航。

## 八组原问题与同根因复核

| 原组 | 结论 | 全部 case 的修复要点 |
| --- | --- | --- |
| POK-S01 | PASS | 724、725 分别补完整未知效果回退及彩票整数转换/低16位/连续五位匹配行为；724 的后继目录消费遗漏另列。 |
| POK-S02 | PASS | 484/485/487/488 明确派入/Call/战前快照、持久招式与场上副本差异、战斗收益暂存、香的登记/复检/退款；748 承接净化恢复。成长/道具/捕获原型及 WP20/28/40/42 消费边界已保留。 |
| POK-S03 | PASS | 519 改为协作并绑定逃跑原型，持续个体与正常终局后的 HP/PP/异常/持物、双方离场能力、仅玩家还原、结果编号/布尔/终结及异常通知分开。 |
| POK-S04 | PASS | 543/571/574/576/577/579 全部重读；持久计数、C/I/R/P/Belch、LEPPA 先持久槽后异身份战斗槽、被动不扣背包、负选择已消费明确。754/755 承接成长和世界持物输入。 |
| POK-S05 | PASS | 原 16 个 FAIL 全部核对。标记/缎带、净化室、交换双收尾、雷达、Safari/捕虫、树果、步进/毒伤/回程/调试、图鉴及 Voltorb 的输入/资源/生命周期已拆分或给出具体混合职责。 |
| POK-S06 | PASS | 492 只保准备/动画/取消，743 拥有统计、持物消耗、额外克隆入队扣球、物种/HP、图鉴和学招的有序领域提交。 |
| POK-S07 | PASS | 478/480/482/500/539/553/573/618 完整退役，8 个 metadata 不计实现功能。META23/24 可经 487→748、489→749 的明确排除子引用到达新消费者；没有强求重复穷尽直接 ID。 |
| POK-S08 | PASS | 537 保战斗开关/样本，753 将 Type/Move 作者缺省、类别×威力校验和本地化归框架，并引用 WP03/04/08。 |

128 个原 PASS 的原 source、有效范围、去向/伙伴、依据、问题、原型和决策均逐项比较；新增职责与直接引用没有否定旧结论。受同根因影响的 Shadow、持物、形态/编辑失败、进化、捕获接收等边界另读相应完整源节及必要消费者。纯战斗计算没有因持久交界修复而一概改归框架；未把同公式/数值或来源静态 PASS 当作目标已兼容。

除了 724，本域新增拆分子行均能通过原目录引用的父行 `excluded_child_refs` 到达。`pokemon-results.json#catalog_consumer_navigation_results` 保存 14 组完整例证及机器链。父可读视图未展示子 ID 的问题由 root 审核，不在这里把可接受的间接链另记失败。

## U03 当前适用回填

完整读取 `git show 9082730…:pokemon-rules/wp60-berry-plants.md` L1–199，以及 B8→908 的真实差分、`861f7a44…` 回执与 `548d6bb9…` actual 报告。仅 L45 把“多数”替换为 CHERI/CHESTO/PECHA/RAWST/ASPEAR 五果具名样本；构造缺省、字段域、未知 ID、产量、时间/覆盖物、取消与采摘微更新均保持。

本域真实接受集合是 **10 行**：588–595 八个旧活跃行加 760/761 两个新子行；口述“本域9行”与真实 17 行集合不一致，本审按路径全部核对。10 行 current locator 的范围、unit/file SHA 和 blob 均在 908 重算一致，旧 source 保持 B8。只有 588 的有效文本改变，另外 9 行属于同一接受文档的已核对关系。

本域 29 个有批次绑定的活跃行中，10 行登记 U03 ACCEPTED，其余 19 行仍 pending；没有把接受扩为 CLOSED、去向已验证、其它批次完成或上游全部结束。

## 机械证据与阅读边界

独立脚本结果无结构差异：165 个旧 ID 恰在 active/retired 中一次；157 个保留活跃 source 完全不变；8 个 retired 去掉 retirement 后逐字段等于旧完整行；所有父范围均为原 source 精确扣子范围；181 个有效范围无重叠；181 个 current locator 身份与 908 一致；181 个本域 view ID 与主要字段/职责投影一致；181 行仍待验证、阶段待定未批准、未实现未验收。

最终实际静态命令 exit 0、stderr 空，完整命令与 stdout/UTC 见 [pokemon-command-evidence.json](pokemon-command-evidence.json)。结构成功没有代替上述人工语义判断。

补充参考身份核验曾误向规格仓库查独立参考仓库的 commit，exit 1 原始记录保存在 `pokemon-command-evidence-ref-lookup-failed.json`；改为只读 `/workspace/pokemon-essentials` 后确认 R 与 HEAD 均为固定 `8c5911e4…`。没有为该工具路径修正更改受审输入。

阅读台账逐文档保存固定 commit、完整 blob/bytes/SHA、真实新读区间及继承理由。主要新读包括 Shadow 全文、持物主文/附表全文、908 树果全文、Voltorb 与 Lottery 全文，以及形态展示/进化提交/交换/漫游/状态/活动/失败回程/图鉴相关完整混合源节；必要消费者包括 WP20 状态/PP/持物、WP28 执行退款、WP40 Call、WP41 逃跑和 WP42 成长/终局。目录已新读 FM/SH、BE/CX/RM、HI/未知效果，以及 SF/BP/FP/PD/VF/LT 的相关区间；其余未受影响全文信用明确来自旧固定报告，不冒称本轮新读或已执行测试。

本报告只写本新 review 的 `agents/pokemon-*`，未改输入、正式规格、参考或旧报告，未切分支、提交或启动新子任务。目标 Showdown 版本/格式与四原型、用户特殊/首版范围、其余上游接受和最终累计独立验收仍待办。
