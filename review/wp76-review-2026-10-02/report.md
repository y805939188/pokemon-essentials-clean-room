# WP76 首版独立审查：需要修订

2026-10-02。结论：**REQUIRES_REVISION，不能进入WP68–70成果整合或集中管理回填。** 本次确认 **20项必修：1项P1、19项P2；20 OPEN**。先完成本轮修订和有界复审，通过后再恢复已安排的整合批次。WP74的18/18、WP75的20/20及其它既有具名批准保持，不因WP76问题重开整包。

本次实际重读四主域全文，共1,346行；核对消息、规则、个体构造和治疗、无视觉场景的AI消费、评级、列表编译反写、名称生成和PBS数据。未运行参考代码、生成器、游戏、反序列化或行为模拟器。审查对象是交付规格是否准确描述参考行为；要求修正规格，不修复参考实现的异常。

## 被审身份与独立验证

| 对象 | SHA-256 | 字节 |
| --- | --- | ---: |
| WP76主稿 | 5d2432264a85dbbbc430bc1ffb30c48dd1cc14415c920d3f1f6358565940235e | 36,040 |
| WP76入口附表 | 8ad84d76bc19735cd2278cfcccc2f781b7633cedb4eb53074667462e33f65f32 | 8,317 |
| 主TSV v100 | 3f1d5e026858f82d030c3d7abbbf5ec0f9b87ff12d1331d70f608cf55ec7b3f9 | 179,585 |
| manifest第125轮 | bec34b1e44c3df5840f1d6dfe4d6cf6bc7695be14129588d8adcc5bcd0a81798 | 1,067,773 |
| Feature Matrix | 4733af0fa031940847769e62f024bc594d8477dd86f88f3d8023da61c7cbc5db | 68,195 |

- 独立复核TSV **1,288条**、manifest §1 **1,383条完整身份＋2条历史无哈希记录**：文件、完整哈希、短标签和字节匹配，无重复路径。登记正确不等于行为通过。
- WP75 v4交接中的**184个唯一保护对象**匹配；矩阵相对冻结基线仅F18-04限定通过标注及F18-05新送审行变动。TSV只改矩阵身份并新增5份WP76材料。旧批准及已通过主稿/表未因本审查修改。
- 入口表实测3/2/7/6/5/6，共29行；M01–M24均唯一；5个Markdown链接可解析。场景存在不代表期望正确，错误见R18及相关行为项。
- reference HEAD为8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b，Git状态清洁。来源原文保持在reference中，报告仅给行为解释和定位。

## 必修清单

| 编号 | 级别 | 问题 | 主稿位置 |
| --- | --- | --- | --- |
| WP76-R01 | P1 | 随机训练家普通分支没有成功退出条件 | 202–205 |
| WP76-R02 | P2 | 写回既有列表不保证默认唯一，也不只更新一个匹配项 | 215–220 |
| WP76-R03 | P2 | 生成询问混淆初始选中项与取消返回项 | 68–72 |
| WP76-R04 | P2 | EV强调条目可重复，均分分母不是去重后的能力数 | 98–128 |
| WP76-R05 | P2 | 招式加权的首次入集与剪枝自删除语义缺失 | 110–113 |
| WP76-R06 | P2 | Sketch会修改共享缓存，且组合规则有Sketch豁免 | 117–123 |
| WP76-R07 | P2 | 道具目录与招式分类不足以确定生成结果 | 103–124 |
| WP76-R08 | P2 | 20与600是补充目标，不是始终成立的容量上限 | 52–55 |
| WP76-R09 | P2 | 模拟对手只取第五次抽样，场次结算时序亦需纠正 | 160–160 |
| WP76-R10 | P2 | 生成用双成员规则与最终原挑战规则没有分开 | 152–168 |
| WP76-R11 | P2 | 真实分支战后治疗包含PP和进化准备标记 | 181–181 |
| WP76-R12 | P2 | 真实模拟的控制标志与场景辅助入口被混写 | 179–180 |
| WP76-R13 | P2 | 估算分支的飘浮结果和同分裁决对象不准确 | 185–187 |
| WP76-R14 | P2 | 评级数学尚不能独立复现，平局和空历史边界有错 | 191–194 |
| WP76-R15 | P2 | 训练家分配混淆去重编号与成员列表，并漏掉随机补位规则 | 209–213 |
| WP76-R16 | P2 | 反写空性格并非空字段，部分写入失败与编译边界未闭合 | 217–220 |
| WP76-R17 | P2 | 名称生成尾部未读到，截断和大小写输出被误述 | 228–230 |
| WP76-R18 | P2 | 静态场景包含错误期望或缺少使期望成立的前提 | 274–287 |
| WP76-R19 | P2 | 缺少已编译数据不能推导所有运行读取都为空 | 250–250 |
| WP76-R20 | P2 | 净化零命中结论漏掉正文中的源码表达式 | 64–64 |

## WP76-R01 · P1 · 随机训练家普通分支没有成功退出条件

定位：[WP76主稿第202行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L202)；受影响附表、场景和自检须同批同步。

正文、F组附表、M23和自检把空训练家表描述为能产生200名训练家；“无上限重抽”被限定为找不到合格类型的情形，遗漏普通分支即使抽到合格类型也持续循环。

**应记录的行为：** 类型抽样普通分支在选中基础奖金小于100的类型后仍返回同一循环，不能前进到名称生成。YOUNGSTER快捷分支才绕过此循环；每一位训练家都会重新选择分支。当前PBS存在YOUNGSTER，连续200次均走快捷分支是可继续到后续阶段的特殊路径；不能把一般随机生成写成保证完成，也不能说所有路径必然卡住。普通分支没有进度回调，五秒刷新不构成独立看门狗。已有非空训练家表绕过这段。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/003_ChallengeGenerator_Trainers.rb:19–48`
- `PBS/trainer_types.txt:191–194`
- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/001_ChallengeGenerator_Data.rb:324–333`

**复审验收：**

- 空表、普通分支抽到合格类型后仍不进入命名的静态路径
- YOUNGSTER不存在／快捷分支未命中／连续快捷命中的区别
- 已有训练家表继续分配的对照；同步M23、F组、摘要和自检

## WP76-R02 · P2 · 写回既有列表不保证默认唯一，也不只更新一个匹配项

定位：[WP76主稿第215行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L215)；受影响附表、场景和自检须同批同步。

§8.4、§10、M24-d及交付材料把默认标志变化称为“唯一化”，会误导重跑与回退行为。

**应记录的行为：** 先记录扫描开始时是否存在任意默认列表，再更新所有含挑战ID的条目，各条目的默认标志都取该先前事实的反值；遍历途中不重新计算。已有默认且该默认也命中ID时，该默认会被清除，可能最后没有默认；原来无默认且多个条目命中时，多个条目都会成为默认；原有不匹配的多个默认不被清理。所有匹配条目都更新并保留原文件名，只有零匹配才新增。复用路径不做同样的标志操作。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/003_ChallengeGenerator_Trainers.rb:185–207`
- `Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb:21–32`
- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/001_ChallengeGenerator_Data.rb:308–317`

**复审验收：**

- 无默认＋零／一／多个匹配
- 已有默认自身匹配及已有多个不匹配默认
- 逐项列最终标志、查询回退和重跑结果；移除全部“唯一化”保证

## WP76-R03 · P2 · 生成询问混淆初始选中项与取消返回项

定位：[WP76主稿第68行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L68)；受影响附表、场景和自检须同批同步。

无列表的YES/NO询问被写成默认NO，并把第三个实参解释为默认下标；M01-b重复此结论。

**应记录的行为：** 消息入口第三个参数指定取消返回值，初始光标另由默认选择参数决定。无列表时初始选中YES，按确认进入长任务确认；按取消映射到NO返回。有列表时初始选中NO；长任务确认的初始选中为Yes、取消为No。生成进度只有回调到达时才检查时间；有文本消息时立即显示并刷新，不能承诺每五秒有文本或长循环仍保持刷新。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/001_ChallengeGenerator_Data.rb:289–333`
- `Data/Scripts/007_Objects and windows/011_Messages.rb:687–705,721–750`

**复审验收：**

- 无列表：初始光标、立即确认、取消分别给结果
- 有列表和二次确认对照
- 修正A组、M01/M03及自检，不把取消规则称默认光标

## WP76-R04 · P2 · EV强调条目可重复，均分分母不是去重后的能力数

定位：[WP76主稿第98行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L98)；受影响附表、场景和自检须同批同步。

正文把EV强调描述成集合，并把纯物理／纯特殊调整说成补入集合；实际追加可能重复同一能力，影响最终EV数值。

**应记录的行为：** 最初独立抽样不重复，但纯物理／纯特殊接受后的80%追加没有去重；构造阶段以含重复条目的长度为分母，按条目逐个对该能力写同一整数值，重复写不会累加。例：HP、攻击、攻击三条会使HP和攻击各170，总计340，而不是两能力各255。空强调保持初始化EV；一个强调可写510，生成路径没有自动夹到单项252，需区分其自身赋值与最终规则是否另行拒绝。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/002_ChallengeGenerator_Pokemon.rb:171–172,325–333`
- `Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb:201–216`
- `Data/Scripts/014_Pokemon/001_Pokemon.rb:91–93,1085–1127`

**复审验收：**

- 空、一条、两种、带重复条目四组确定性向量
- 明确追加和删除对重复条目的作用
- 主稿、C组和构造场景采用同一分母与最终数值

## WP76-R05 · P2 · 招式加权的首次入集与剪枝自删除语义缺失

定位：[WP76主稿第110行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L110)；受影响附表、场景和自检须同批同步。

三路权重没有说明跨来源首次入集后跳过重复来源；剪枝被描述为只删除“其它”招式，遗漏必中招式可删除自身及在被遍历集合上删除的顺序影响。

**应记录的行为：** 来源按升级、机器、蛋招顺序处理；招式已有副本时，后续来源不再加权。首次加入产生零副本时，后续来源仍可能加入。必中、无附加效果且满足自身比较条件的招式没有身份排除，会删除自身全部副本；固定PBS的AERIALACE、SWIFT均具备这种数据条件。剪枝使用一份初始比较资料并在当前遍历集合上删除，不应把它改写为顺序无关的理想优势筛选。PP门属于发起比较的招式，不能只说两个招式中任一个PP为10/15就能剪枝。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/002_ChallengeGenerator_Pokemon.rb:50–123`
- `PBS/moves.txt:2990–3000,5141–5151`

**复审验收：**

- 同招式由升级和机器同时提供时不累加权重
- 机器首次零权重而蛋招后续加入
- 必中无效果招式与自身比较的删除向量；保留迭代顺序影响
- PP门方向相反的成对对照

## WP76-R06 · P2 · Sketch会修改共享缓存，且组合规则有Sketch豁免

定位：[WP76主稿第117行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L117)；受影响附表、场景和自检须同批同步。

§5.6把Sketch替换写成当前个体的全部招式位变更，未描述共享合法招式缓存被直接写入；蓄力组合又被写成无例外的硬约束。

**应记录的行为：** 首项为Sketch时改写缓存列表的前四个位置，列表不足四项会扩展，超过四项的尾部保留。相同等级同种后续采样会看到改后的缓存，通常不再带Sketch标志；等级切换才清空合法招式缓存。四种及以上招式的组合筛选中，Sketch标志豁免蓄力与喷出／吞下配对要求。梦话和鼾声各自有独立的睡觉例外门，若两者同时存在而无睡觉，满足例外前提也需两门均通过。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/002_ChallengeGenerator_Pokemon.rb:193–195,259–298`
- `PBS/pokemon.txt:6191–6204`
- `PBS/moves.txt:6395–6403`

**复审验收：**

- 同等级同种连续两次调用与等级切换后的对照
- 缓存前四项与第五项以后的保留行为
- Sketch与普通候选的蓄力组合对照；两种睡眠招式同时存在的双门

## WP76-R07 · P2 · 道具目录与招式分类不足以确定生成结果

定位：[WP76主稿第103行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L103)；受影响附表、场景和自检须同批同步。

41项候选没有完整列出，文字举例包含实际不在候选表中的节拍器；专属门计数为12但实际13。SILKSCARF门又把有普通系变化招式当成可保留的条件。

**应记录的行为：** 用独立输入数据表准确列出41个道具标识和13个物种限定门；不存在的候选道具不会在抽样阶段统一剔除，个体中间表示会把无效道具变为空。物理、特殊、普通系标志只检查威力非零招式；在至少四种招式的筛选路径中，只有普通系变化招式不足以保留SILKSCARF。唯一招式不足四种时不经过这段门。总威力180/140两门共用一次十面抽样，不是两个独立随机拒绝事件。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/002_ChallengeGenerator_Pokemon.rb:196–258,266–338`
- `Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb:154–163`

**复审验收：**

- 41/13数量与逐项数据一致，移除未在池中的例子
- 普通系变化招式＋其它系攻击招式的SILKSCARF结果
- 不足四种招式的跳过路径
- 总威力140/141/180/181和同一抽样值的边界

## WP76-R08 · P2 · 20与600是补充目标，不是始终成立的容量上限

定位：[WP76主稿第52行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L52)；受影响附表、场景和自检须同批同步。

概念区称池上限20，§6.4称队伍库上限600，忽略种子/退休回池、条件分支和删除后继续递增游标的实际结果。

**应记录的行为：** 池不足20才补充，已有大池不截断；种子和退休成员可令其超过20。同种10只限制仅在显式去重阶段生效。队伍库600是补齐目标；更替前两支可先于超额删除命中，删除后游标还会前进，移到当前位置的队伍可跳过本轮扫描。例：602支正常长度且避开前两支的队伍，在下标600删除后，本轮可能留下601支。不能承诺任何检查点库长均不超过600。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/001_ChallengeGenerator_Data.rb:113–124,178–226`

**复审验收：**

- 种子池超过20、退休回池超过20
- 602支队伍删除移位的向量
- 超额队伍先命中低分/场次替换支的向量
- M14每支写清未命中更早分支的前提

## WP76-R09 · P2 · 模拟对手只取第五次抽样，场次结算时序亦需纠正

定位：[WP76主稿第160行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L160)；受影响附表、场景和自检须同批同步。

“最多重掷5次避免自对”和“每队打一场”暗示找到有效对手即结束；§7.4还把累计场次更新写到评级结算之前。

**应记录的行为：** 每个发起位置无条件抽五次，只用最后一次；最后仍是自身就跳过，不会使用前面已抽到的有效对手。对手也记录场次，所以每队本轮得到的场数不固定；续战门取全库历史场次的整数平均，非每队达到12。每条对局记录保存记录当时对手评级与偏差，之后逐队结算不回头改这些值。累计已结算场次在评级成功更新、历史清空之后才增加；可见累计场次还包含当前历史长度。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/001_ChallengeGenerator_Data.rb:230–249`
- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/004_ChallengeGenerator_BattleSim.rb:48–65,121–128,427–437`

**复审验收：**

- 前四次非自身、第五次自身→跳过；相反顺序→对局
- 600支队伍时最后抽到自身的概率为1/600，不是五次连续自身的概率
- 全库均值达到12但个别队未达到的合法收束
- 结算失败时历史与累计场次的顺序边界

## WP76-R10 · P2 · 生成用双成员规则与最终原挑战规则没有分开

定位：[WP76主稿第152行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L152)；受影响附表、场景和自检须同批同步。

主稿只说明复制规则并设为2，随后把该规则笼统贯穿分层与训练家分配，遗漏11轮结束后恢复原挑战规则的阶段切换。

**应记录的行为：** 候选、组队和模拟使用设为两成员的规则副本；汇集后分层和训练家分配重新使用原规则。最终合法性、建议等级和可组队要求按原规则消费，不应继续把数量2当全流程不变量。训练家分配的等级更改只赋等级，不显式重算数值；建议等级与数量的关系及规则副本的最小数量语义应引用WP54并核对消费点。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/001_ChallengeGenerator_Data.rb:171–175,254–269`
- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/003_ChallengeGenerator_Trainers.rb:52–60`
- `Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/001_Challenge_ChallengeRules.rb:16–23`
- `Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/002_Challenge_Rulesets.rb:13–25,44–77`
- `Data/Scripts/014_Pokemon/001_Pokemon.rb:199–205`

**复审验收：**

- 原挑战为3成员：模拟取2、最终分配使用原3成员要求
- 给独立自定义规则下建议等级变化的条件例，而非套用普通杯赛必然变化
- 明确原规则未被数量2修改及恢复后的重检时点

## WP76-R11 · P2 · 真实分支战后治疗包含PP和进化准备标记

定位：[WP76主稿第181行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L181)；受影响附表、场景和自检须同批同步。

正文与M16明确说PP不回滚，与实际完整治疗及已通过WP20合同冲突。

**应记录的行为：** 正常返回后，对非蛋成员补满HP、清状态和状态计数、补满全部PP并清进化准备标记，再恢复保存的持物；这是治疗到目标状态，不是恢复战前受伤或低PP快照。已归一等级不由此包装恢复。其它字段是否由正式战斗清理由相应合同确定，不能因本包装没有全字段快照就断言一律不还原。恢复段不包住所有异常出口。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/004_ChallengeGenerator_BattleSim.rb:386–419`
- `Data/Scripts/014_Pokemon/001_Pokemon.rb:274–306`
- `specs/creature-rpg/wp20-hp-status-moves-helditem.md:64–79`

**复审验收：**

- 低PP／异常／待进化标记的正常返回后状态
- 战前低PP不会恢复到旧低PP
- 起战或执行抛错时不承诺已执行治疗和持物恢复
- 同步M16、E组、摘要与自检

## WP76-R12 · P2 · 真实模拟的控制标志与场景辅助入口被混写

定位：[WP76主稿第179行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L179)；受影响附表、场景和自检须同批同步。

E组“debug/controlPlayer/internalBattle关”与实际三个标志值不一致；正文把场景随机菜单并列成真实模拟的运行合同，且Call概率少了前一门条件。

**应记录的行为：** 真实分支打开调试与玩家方AI控制，关闭内部战斗标志。主命令路径因此交由AI选择，并不靠场景随机Bag/Call/Fight决定双方策略。场景辅助菜单若被直接调用，Bag概率1/15，Call仅在未选Bag时再以1/10触发，整体为7/75；这些辅助入口应与实际模拟消费路径分开。目标/替补辅助入口的候选范围与无候选返回需具名。出招辅助入口使用的单数招式访问在当前Battler定义中未找到对应接口，不能凭循环文字承诺直接调用必能随机选招；该辅助问题不应反推AI主路径必然失败。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/004_ChallengeGenerator_BattleSim.rb:404–409`
- `Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb:198–230`
- `Data/Scripts/011_Battle/004_Scene/009_Battle_DebugScene.rb:77–105`
- `Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb:12`

**复审验收：**

- 三个标志分别列真／真／假并追到AI命令消费侧
- 辅助菜单条件概率与无候选返回
- 辅助出招访问异常边界和当前模拟可达性分开，不自行修参考

## WP76-R13 · P2 · 估算分支的飘浮结果和同分裁决对象不准确

定位：[WP76主稿第185行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L185)；受影响附表、场景和自检须同批同步。

M17把飘浮对地面写成“效果正常算（非重置）”；正文同分比较“评分”没有保持缩放取整后的对象，可能造成错误胜负。

**应记录的行为：** 飘浮遇地面时跳过类型查询，最终落入普通效果得分，即+4，不按其本身属性弱点计算。神奇守护按每一个属性分量分别把非克制分量置为中性，然后相乘；不能替换成正式免疫合同。双方评分先乘0.15并取整，得分相同时再比较的也是这两个取整值。原始评分50和51都变为8；若总分相同则平局。BST加项按每个成员分别整数除10，抖动每方独立抽取。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/004_ChallengeGenerator_BattleSim.rb:310–372`
- `Data/Scripts/010_Data/002_PBS data/003_Type.rb:73–139`

**复审验收：**

- 飘浮＋对地面有弱点的属性仍得+4
- 神奇守护双属性逐分量的向量
- 原始评分不同但缩放值同、总分同→平局
- 明确每成员BST整数加项

## WP76-R14 · P2 · 评级数学尚不能独立复现，平局和空历史边界有错

定位：[WP76主稿第191行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L191)；受影响附表、场景和自检须同批同步。

主要更新仅写Glicko-2名称和过程概述，缺独立公式；GLIXARE的指数变量未定义。M18把原尺度偏差直接与波动率平方相加，漏了173.7178尺度换算。

**应记录的行为：** 补齐归一化尺度、对手记录、g/e、方差、改进和、实际波动率迭代、最终评级/偏差/展示分数等数学定义及参数1.2；不要用标准算法名称替代本来源实际变体。平局记录参与方差但不进入改进和，不等同按0.5计分。空历史只膨胀归一化偏差，换回原尺度时需要173.7178；初值350、波动率0.9的原尺度新偏差约383.332855。明确定义GLIXARE指数和偏差100的分界。未使用Elo辅助路径的非空更新还存在未建立当前对局变量的问题，应记录为未使用定义的静态缺陷，不承诺可用更新算法。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/004_ChallengeGenerator_BattleSim.rb:135–164,169–305`

**复审验收：**

- 不调用或移植参考实现的独立数学说明与固定算术向量
- 空历史、单胜、单负、全平局、偏差100/略大于100
- 展示缓存随评级/偏差变更失效
- Elo定义与活动评级明确分开，保留异常而非修成标准式

## WP76-R15 · P2 · 训练家分配混淆去重编号与成员列表，并漏掉随机补位规则

定位：[WP76主稿第209行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L209)；受影响附表、场景和自检须同批同步。

“补至满且可注册、受表长上界约束”把不同集合和规则检查合成了一个理想化过程，遗漏重复项、过滤范围和过早停止。

**应记录的行为：** 首轮双属性可两次加入同一候选，之后只对编号去重，成员列表仍可重复；同种顺序补足又可把已经选过的编号再次加入，最终仅排序不再次去重。第一次补足门使用清除个体规则的副本，该副本也有WP54已述最小数量复制边界；后续退出和随机阶段用原规则。随机补位不再依据预先缓存的单体合法性筛选，可能加入不合法候选，只要全表中存在合格子队伍也可停。编号长度限制不是抽样次数上限；重复抽到已收录编号可持续无进展，已有重复编号又可能提前达到长度停止，不能保证输出六个不同合法候选或全部候选均已尝试。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/003_ChallengeGenerator_Trainers.rb:52–60,99–172`
- `Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/002_Challenge_Rulesets.rb:13–25,176–188`

**复审验收：**

- 双属性首轮双命中后两个集合的长度对照
- 同种补足重复编号保留到最终排序
- 清个体规则副本与原规则的门分别列出
- 随机加入不合法候选、重复抽样无进展、重复计数触发提前停止

## WP76-R16 · P2 · 反写空性格并非空字段，部分写入失败与编译边界未闭合

定位：[WP76主稿第217行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L217)；受影响附表、场景和自检须同批同步。

正文声称nil道具/性格都会变成空字段，实际反写入口对性格进行必需查找；同时只给成功往返，没有本包明确要求的写入失败与重跑语义。

**应记录的行为：** 反写道具可空，性格为空或无效时不走同样的空值保护，会在查找时失败。先保存列表数据，再打开并截断总PBS，逐列表交错写总表、训练家表和宝可梦表；后续失败不自动撤销先前数据或已写文件，末尾成功消息/窗口销毁也不保证到达。编译时缺总表可新建默认引用，缺文件名是错误，文件名存在但所指文件缺失则该子表为空；宝可梦行缺必要分隔字段也不同于未知标识变空。应给各阶段失败的可见残留和重跑输入，引用WP04/WP75不代替这些具体消费边界。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/001_ChallengeGenerator_Data.rb:315–337`
- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/003_ChallengeGenerator_Trainers.rb:207–210`
- `Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb:511–619`
- `Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb:951–1021`
- `Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb:113–138`
- `Data/Scripts/010_Data/001_GameData.rb:88–114`

**复审验收：**

- 空道具与空性格的反写对照
- 列表数据已保存、后续PBS写出失败的残留表
- 缺总表／缺必需文件名／缺被引用文件／坏宝可梦行分别给结果
- 旧检查点继续保留且重跑不是事务回滚

## WP76-R17 · P2 · 名称生成尾部未读到，截断和大小写输出被误述

定位：[WP76主稿第228行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L228)；受影响附表、场景和自检须同批同步。

登记阅读只到Utilities第340行，函数实际到369行；正文声称超过50次返回当前结果、不保证非空，遗漏最后截断和本调用的大写转换。

**应记录的行为：** 有效性别选择模板，至多尝试50次寻找不超限名称，最后仍截断到长度上限；本调用要求全大写，并且不把名称写入游戏变量。空输出来自非法性别或非正长度等入口条件，不能归因为50次都过长。应读完整函数并记录真实范围，说明随机音节生成范围与截断后的输出限制。

**来源：**

- `Data/Scripts/019_Utilities/001_Utilities.rb:285–369`
- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/003_ChallengeGenerator_Trainers.rb:34–39`

**复审验收：**

- 合法性别正常输出全大写且最长12
- 达到尝试上限后仍截断
- 非法性别/非正上限与本次合法调用分开
- 来源记录、正文、F组、自检同步

## WP76-R18 · P2 · 静态场景包含错误期望或缺少使期望成立的前提

定位：[WP76主稿第274行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L274)；受影响附表、场景和自检须同批同步。

M11-a声称同招式换槽位就不重复，未排除另一条属性判据；M22的BST300/T1和非传说590层集合错误；M24-b把位次差5的权重写为1。

**应记录的行为：** 同种、槽位不同但道具/性格/全部EV相同仍重复，M11不重复例必须显式使第二判据也失败。BST300非传说只可入T0，非传说BST590可入T7和T8，传说590可入T6/T8；还需说明先通过原规则且无可入层时丢弃。位次差5的基础权重为0，差4才是1，应选类型计数非零的对照来暴露差别。M14各更替例补足更早分支不成立的条件。

**来源：**

- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/001_ChallengeGenerator_Data.rb:67–108,126–140,199–217`
- `Data/Scripts/018_Alternate battle modes/003_Battle Frontier generator/003_ChallengeGenerator_Trainers.rb:110–124`

**复审验收：**

- M11两条重复判据交叉正反例
- M22全部层集合与边界、无层丢弃
- M24差4/差5且类型计数为1的对照
- 所有被本审查改动的M场景同时更新正文、附表和自检

## WP76-R19 · P2 · 缺少已编译数据不能推导所有运行读取都为空

定位：[WP76主稿第250行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L250)；受影响附表、场景和自检须同批同步。

当前磁盘没有trainer_lists.dat是事实，但正文和摘要进一步宣称“本包全部列表读取落入空表”，把静态材料缺口扩成运行入口保证。

**应记录的行为：** 仅能断言未经准备的该快照在直接执行这些读取且仍缺文件时会回退空表；编译管线明确把列表数据列为必需产物，能从当前PBS生成它，生成/复用也能写回，后续读取不一定为空。分开记录文件存在性、带缺文件前提的直接调用、正常工程准备后的可能输入以及未验证demo可达性。不能据原始快照断言正常启动必走随机训练家空表分支。

**来源：**

- `Data/Scripts/021_Compiler/001_Compiler.rb:993–1018,1051–1075`
- `Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb:951–1021`
- `Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb:21–32`
- `PBS/battle_facility_lists.txt:1–25`

**复审验收：**

- 原始快照存在性证据保留
- 直接缺文件读取与编译后读取分开
- 全部／必然空表之类结论从正文、摘要及自检中移除
- WP77运行/demo未知保持，不伪造运行验证

## WP76-R20 · P2 · 净化零命中结论漏掉正文中的源码表达式

定位：[WP76主稿第64行](../../specs/demo/wp76-facility-content-generation-and-simulation.md#L64)；受影响附表、场景和自检须同批同步。

正文§3.1仍保留完整的参考提前返回语句，§7.4保留累加赋值式；与AGENTS的禁止复制源码表达式及自检“全部行为化、零命中”声明冲突。

**应记录的行为：** 保留必要审计标识与独立数学，移除直接复制的控制流、赋值和源码表达式；不要只靠“带参数调用”正则判断净化。评级部分按独立变量、定义域、方程及边界表重新表述，禁止逐行改写源码伪码。当前源式只在冻结证据中保留历史，不再传播到新稿和修订摘要。

**来源：**

- `AGENTS.md:Strict Source Separation Rules / Clean-Room Output Rules`
- `specs/demo/wp76-facility-content-generation-and-simulation.md:64,194`
- `review/wp76-delivery-2026-10-02/checks.json:clean_room_scans`

**复审验收：**

- 人工通读当前正文、表、摘要、自检及新增数学附录
- 不在修订说明里再次抄录被删除的源码片段
- 新扫描规则、范围与实际结果一致，旧首版原件冻结保留

## 修订边界与下一步

只修WP76主稿并新增revision-v2交付；旧首版交付表、摘要、自检、source-identities、末检以及本审查原件和冻结快照保持原字节。新附表/摘要/自检分别落新版本，按原20个编号逐项回应，提供相对本次冻结主稿的严格diff、来源阅读范围及最终身份。已有正确的槽位敏感去重、1%真实分流、显式非终止路径、默认查询顺序等不应因修订被改成理想化规则。

登记只更新F18-05为“修订v2待复审”及必要manifest/TSV身份与追加历史；F18-04已通过标注保持。不得自行将任何本审查问题标为CLOSED或将WP76标为Reviewed。所有新正文、表、场景、摘要和自检使用相同最终语义，完成后全量检查登记、保护对象、链接、表行数及净化情况。

修订完成后停止送本轮有界复审。通过之前不进入WP68–70整合、集中管理回填或WP77–80；这执行的是现行extraction-plan §2.2“当次review问题先修订并复审”的门槛，不是重新索要批次授权。后续整合授权与顺序保留。

[逐项结构化发现](findings.json) · [修订执行提示](next-task-prompt.md) · [冻结输入](input-manifest.json) · [来源实读记录](source-read-log.json) · [独立核对](independent-checks.json) · [登记检查](registration-checks.json) · [最终完整性](final-verification.json)
