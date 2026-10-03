# GR-013～016 收尾批次有界复审（2026-10-01）

**结论：REQUEST_CHANGES。GR-014、GR-015 CLOSED；GR-013、GR-016 OPEN_PARTIAL。** 四项原始问题的核心修正均与来源一致；剩余是一处场景编号冲突与一处新增总量保证错误，沿用原GR编号，不新增全局问题编号。

**现在也不能进入整体 double review。** 总路线仍有13个内容包未完成；本轮剩余问题闭合后，下一内容批应为 WP65 → WP67-A → WP67-B。WP78／WP79 的整体审查在全部内容包及已知问题完成之后。

## 1. 被审身份

| 文件 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `c456e49407c54a9f5dbae206698dd67af9e60894f2a05705abdfa11f9f2780bb` | 35,065 |
| `specs/combat/wp42-growth-end-of-round-and-battle-outcomes.md` | `f6e5d683fc18a5d3d7d28b255cc3bd5acafd98dba7fae35fc09b755ce0ab72fe` | 44,526 |
| `specs/combat/wp58-battle-recording-and-playback.md` | `74a2077b517a10051a3edaf5b178986f0e4510d5f891726b3ed32601f212b995` | 32,625 |
| `specs/combat/wp47-b-switching-control-and-item-changes.md` | `00409b29ded9dbd29d29e1a9384b9bc365c4da1e55f6b70326e05cc01d10866e` | 43,261 |
| `specs/combat/wp52-a-generic-numerical-and-status-evaluation.md` | `42138911ff6ec27780170f10c630c0e9e4eacae1f59e4f36d6658b6e5022cc67` | 52,988 |
| `specs/combat/wp52-b-field-damage-healing-and-target-evaluation.md` | `15e28d3975d69eb5735004c38297f2dcee34d6617bbc1bbc20f8258d304c66c5` | 47,142 |
| `specs/pokemon-rules/wp19-attributes-ability-and-stats.md` | `f5611332759af16658dce669552a04764672449e5e6aae73c2af5c61657c6f41` | 40,355 |

本轮被审规格、交付材料与管理文件固定于 input-snapshot；逐项结论见 [findings.json](findings.json)。

## 2. GR-013：行为修正接受，场景编号需补修（P3）

WP41 普通派出按侧内场上位置写标记、WP42 正常终局按当前队伍下标读取，以及WP58对BURMY回放正例收紧前提，均正确。单打下标1换入席位0得到记录 [true,false]、终局传假而保持形态0；下标0首发的真标记正例和实时图鉴写入也成立。WP21处理器合同与WP62登记门保持正确。

但 **WP42 第287～289行新增的 E07／E08／E09，与第290～292行原有三例重名**。原E07是病毒传播，E08是调试上限中止，E09是显式中止未退物品；都不能被新增BURMY场景覆盖。新E08的“同E07”现有歧义，也不适合后续按ID生成测试。冻结基线31条编号案例均唯一；当前34行仍只有31个唯一标识，详见 [scenario-id-checks.json](scenario-id-checks.json)。

请保留原三例编号和内容，只调整新增三例的编号及其当前交叉引用／状态注记。WP41、WP58的本次行为修订无需继续改动。该项是同一GR的交付一致性补修，不重开已接受的参战标记行为。

## 3. GR-014、GR-015：CLOSED

**GR-014**：投掷每击反应中的INNARDSOUT反伤、U半血ORAN恢复及消费、T正式倒下、目标强制物品处理早退，最终在U当前空持物查询处首次失败的顺序与来源一致。伤害／恢复／消费已提交，后段尚未发生；不回滚、不回绑原持物，外层一般异常诊断边界与两个不自耗对照正确。保留WP47-B当前字节。

**GR-015**：旧会心分母表五档16／8／4／3／2、新表24／8／2／1及各自截尾正确；具名累计5的磨砺局部分旧115／新60成立；负下标取旧2／新1后仍满足粗伤近似条件。真实WP43规则、B评分算法及既有近似差异均未被误改。保留WP52-A、WP52-B当前字节。

## 4. GR-016：255 EV例外正确，但总量不恒等510（P2）

WP19已正确撤回所有正常入口都保证单项≤252的全称：默认SUNKERN双项255／255、DROWZEE三项各170，以及禁用计算不改存储的场景均成立，原能力公式保持。

问题在 **WP19 第152行新增“合计恒为510（项数≤510的整数商）”**。创建时各努力项分别取整数商，没有余数再分配。合法人工模板选四个不同有效努力项HP／ATK／DEF／SA，其他字段、等级、IV、训练家与正常返回条件有效：每项为127，四项合计 **508**，其余两项0，余下2未分配。这里不声称默认PBS中存在该行，也不需要修改PBS或运行生成器。

依据：`Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb:113–138`接受这些有效努力项，`:201–217`逐项作整数分配并重算；`Data/Scripts/014_Pokemon/001_Pokemon.rb:1191–1197`新建各项从0开始，能力重算不回写EV。不同有效努力项数量为 n＞0 时，总量是 **n × ⌊EV_LIMIT/n⌋**，不一定等于EV_LIMIT；该公式须保留“项互不重复”的前提。

请去掉恒等保证并补四项508的对照，保留已有双项／三项／禁用计算三个正确场景；不要给分配器补余数、不要把设施改为单项252，也不扩展重复项配置目录。

## 5. 独立登记核验与矩阵裁定

七份diff从上轮冻结的当前基线逐段严格应用，**7/7精确重建当前字节**。manifest §1 **1,112条完整身份**、主TSV v63 **1,017条**全量与磁盘一致、无重复；两条旧无哈希行未变，阶段最终身份匹配。只有七份规格、矩阵、manifest与TSV这十份既有文件变化；六份只读支持稿、WP62、GR-001～012及旧审查材料保持不变。

**接受本轮六行矩阵归属**：GR-013按WP41／42／58的实际功能分记F11-05／F11-07／F13-06；GR-015的A/B评估同属F12-08可合记；GR-014的F12-05与GR-016的F06-04也合适。同一GR不重复计数，无需为补修重新挪行。

当前manifest身份 `98129e4e7b2b1a2884f6d8b3dc45cef18ceb38bb51c65a1f9a45983c1bdf1ade`／709,229字节；TSV `afbc1f1759cd3914b1c9e852e15fb952bb2de5680d4edab4d5c936c54c12ddb9`／142,249字节。详见 [registration-checks.json](registration-checks.json)、[feature-matrix.diff](feature-matrix.diff)、[source-checks.json](source-checks.json)与[final-checks.json](final-checks.json)。登记通过不能代替内容正确性。

## 6. 正确的下一步

先按[有限补修提示](next-task-prompt.md)仅修GR-013编号和GR-016总量说明／向量，完成后定点复审。GR-001～012、GR-014／015共14项已关闭；不要把“16项均做过首轮修订”当成“16项全部关闭”。

随后才按 `planning/extraction-plan.md` §2.2 继续以下13个内容包：

| 批次 | 内容包 |
| --- | --- |
| 2 | WP65 → WP67-A → WP67-B |
| 3 | WP37 → WP53 → WP61 |
| 4 | WP72 → WP73-A → WP73-B |
| 5 | WP74 → WP75 → WP76 |
| 6 | WP77 |

全部内容与已知问题闭合，再进入WP78一致性、WP79覆盖／遗漏的整体double review；发现额外问题后继续修订复审，最后WP80净化交付。此处是路线裁定，**不构成本轮启动这些内容包的许可**。[路线核对](route-checks.json)保留依据；早期计划中尚未集中回填的第一组／N01状态按后来批准结论继承，不重开、不重提取。管理回填与B批整合另行处理。

审查方仅新增本目录，未修改被审规格或外部总审原件。reference固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，30份定点读取来源与该提交一致且Git清洁；仅静态阅读与固定常数核算，未执行参考代码、编译／生成、战斗／回放／AI或行为模型；未创建任务／Agent、未发送跨会话消息、未提交／推送。
