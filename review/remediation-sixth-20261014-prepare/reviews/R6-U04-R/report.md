# R6-U04-R 独立非作者候选复审

结论：**CANDIDATE_PASS**。`GR6-CA-EB-001`、`GR6-CA-EB-002`、`R6-CA-EA-P001` 均 **PASS**，本固定候选无必要实质修订。结论仅覆盖下面绑定的三个镜像及原合同限定的静态验收；**不是 INTEGRATED_PASS、正式接受或 CLOSED**。原正式文件仍为基线。没有开展新全局 review，没有修改作者候选、正式稿、参考源或公共 ledger。

## 固定被审身份与审者独立性

- 仓库：`y805939188/pokemon-essentials-clean-room`；实际 cwd：`/workspace/pokemon-essentials-clean-room`。
- 准备：`469a268b92daed7b4d28d7fd0da75520cbb7228f`，tree `78cd0f429bbcfe3724cbcaf0f09d3fcf80d48d06`。
- 完整审者入口：`review/remediation-sixth-20261014-prepare/prompts/R6-U04-R.md`，221397 bytes，SHA256 `4de6aa24117b630b22f0de7546d5674e7ef498d1f9578f53957085f3df687a00`，blob `2bef897e43ce86c1124d61b00da966ac88816ecf`。3526行的通用合同、三项完整七组/原提案及共同证据恢复索引全部读取；展开 JSON 与独立 `contracts/R6-U04.json` 相同。共同恢复索引按全字段等价表读取；未据此重审其它领域。
- 正式输入：`8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，workspace tree `6ab3429170d2762607fbc2237014c3a160449fa1`，formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`。
- 参考：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。仅从本审查目录 `.scratch/reference.git` 的固定 blob 读取，无参考工作树或参考定义执行。
- 作者：用户明确指定 `thread01a13ab2-510d-75e5-b7f6-a55691aa503e`；作者分支 `codex/remediation-sixth-r6-u04-author-20261014`。其语义候选 `1fa0f30525ae87ff4f3fb22f4d8448b4447b694b`，发布 **`22cc12e141ac2c2dd23c1dea218bf0873c5f86ca`**，tree **`2e2d4f590983f4e327b2de37cf69014229af7f12`**。本审查始终绑定发布对象；语义/发布的 mirror tree 同为 `52b11a8359743a7b25efab6e9fcb7e4f9aa1f3b9`，没有跟随浮动分支换版。
- 审者逻辑身份 `R6-U04-R`，本独立执行环境 `ccarenv_b64_Y2NhcmVudl9hOGEwMDZmNjVjYzA4MTkxYTAwMjc5ZmNiODgwYTllYQ`，工具任务路径 `/root`。此路径不是 opaque UUID，也不是作者身份。本审者未撰写或修订该候选/正式规格，独立回源、复算和出具本报告；作者自检、原提出者支持和旧 PASS 未替代新裁定。
- 请求配置 `gpt-6.1-sol / ultra / default tier / default speed`、普速；实际 model/effort/tier/speed/opaque UUID **UNVERIFIED**，本会话没有有效配置回显。依本轮明确指令直接审查，未启动 CLI 或额外代理追查配置，未降档自签、改认证/安全配置或安装服务。不能把请求冒充有效回显；此元数据限制保留，不用它拖延已授权静态审查。
- 审查分支：`codex/remediation-sixth-r6-u04-review-20261014`，从固定作者发布建立。全部新增内容仅在 `review/remediation-sixth-20261014-prepare/reviews/R6-U04-R/`。报告的实际 commit/tree 由有限发布回执和最终响应外部绑定，不预写自身未来身份。

以下路径均以 `review/remediation-sixth-20261014-prepare/candidates/R6-U04/mirror/` 为前缀，type=blob、mode=100644；完整 baseline/candidate 对照见 [candidate-binding.json](candidate-binding.json)。

| 镜像内正式相对路径 | bytes | SHA256 | Git blob |
| --- | ---: | --- | --- |
| `deliverables/final-specification-set/combat-requirements/wp52-b-effect-coverage.md` | 16260 | `c80e5780a1d775a88a11e6c41ab490e36f36356dd06abf8ec6044361331cf754` | `be1237e215d6f724da5b638fc82156bd75c01d52` |
| `deliverables/final-specification-set/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md` | 41357 | `954252ebda7475a1fe4efcb65b3a822c0c20fbd5c8c6235f78c666f90a3af3d7` | `36a4ada2f7ca1a6019045f85f62d61892c329a5f` |
| `deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md` | 48020 | `8e629a8aa34be11a73ac51b94caccb837c6950be10f8af23b11ee90c6f3a1c41` | `64f78d069fe3bccaabaec810aaa919e6c8a1c5ef` |

作者报告 `candidates/R6-U04/evidence/author-report.md`：19000 bytes，SHA256 `07748639f671dc18bf7070cd3627f1b1834443221dbf0747746f11aeac24bfcc`，blob `6146380222ca93db26247cfdbd7ae7a2a120238e`。`formal-only.patch`：21871 bytes，SHA256 `724db13a0560ffec3240e7efdc0c5372c1ec86dc4b734c13709b148aae090467`，blob `280835e762cf147ae71a4464c9f117f74969f13f`。三份镜像全文与完整差异均实审；基线全文240/111/294行和镜像全文248/111/311行分别新读，非只读摘要或搜索命中。

## 新读范围与反证基础

根 `AGENTS.md` 全文已读并遵守 clean-room 分离。本审不输出参考代码片段或未来框架实现。源/正式文件的读取区间、固定身份、argv、cwd、UTC、exit、stderr、显示摘要哈希见 [reading-ledger.jsonl](reading-ledger.jsonl)；早期直接工具读取与显示截断处理见 [execution-and-limitations.json](execution-and-limitations.json)。JSON字段投影只证明所列字段的语义读取，不冒称整个历史大 JSON 复审。

源路径以下相对固定 R 根；除特别注明外为有连续上下文的具名范围，没有宣称全 R432 或全 PBS8712行再审。

| 源/消费者 | 本审新读区间及用途 |
| --- | --- |
| `011_Battle/005_AI/005_AI_ChooseMove.rb` | 全文1–393；资格→准备→预测→目标枚举→包外100/包内未完成赋值→通用评分→权重/登记 |
| `001_Technical/001_Debugging/001_PBDebug.rb` | 全文1–77；普通异常捕获、正常诊断返回的限定、条件式日志请求 |
| `011_Battle/005_AI/009_AITrainer.rb` | 全文1–100；32/48门、Flags追加、Anti独立删除 |
| `011_Battle/005_AI/011_AIMove.rb` | 1–400、495–545；基数入口、普通粗伤整链、至少1夹限、会心历史接口及共享字段 |
| `011_Battle/005_AI/007_AI_ChooseMove_OtherScores.rb` | 260–390；通用命中/伤害消费者，普通伤害独立求粗伤 |
| `011_Battle/005_AI/001_Battle_AI.rb` | 全文1–163；入口阶段和各族默认、通用修正按登记遍历，没有统一60早退 |
| `011_Battle/006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb` | 1–210；三份围攻登记及双击/2–5击对照 |
| `011_Battle/006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb` | 1409–1450；自然之恩失败/基数分族；170–205、430–475；压榨/磨砺历史对照 |
| `011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb` | 1320–1395；自然之恩完整定义、类型空守卫、基数先缺物身份失败、正常结束消费 |
| `011_Battle/003_Move/009_MoveEffects_MultiHit.rb` | 145–195；真实围攻名单在起用失败阶段建立，没有本族命令资格覆写 |
| `011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb` | 1–145；PP/安可/真实资格与NearOther目标门 |
| `011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb`；`003_Move/002_Move_Usage.rb` | 1–110；1–100；真实命令资格没有空名单/无物统一拒绝、普通招式默认可选 |
| `011_Battle/001_Battle/001_Battle.rb` | 355–430；业主队伍段包含合格U、过滤空成员，非整侧伙伴名单 |
| `011_Battle/005_AI/010_AIBattler.rb`；`002_Battler/001_Battle_Battler.rb`；`010_Data/001_GameData.rb` | 1–100/270–305；60–95；85–125；当前持物查询代理及空输入返回空，没有虚拟NONE物品兜底 |
| `011_Battle/003_Move/001_Battle_Move.rb`；`003_Move/003_Move_UsageCalculations.rb` | 120–170；1–35；替身绕过、基底类型与后置类型覆盖的既有责任 |
| `011_Battle/006_AI MoveEffects/001_AI_MoveEffects_Misc.rb` | 157–465；天气/地形对照、四危害失败和整体效果分 |
| `011_Battle/006_AI MoveEffects/006_AI_MoveEffects_Healing.rb` | 225–255；第五生命水滴独立评分守卫 |
| `PBS/moves.txt`；`PBS/items.txt` | 625–650、5575–5600；5252–5260；默认BEATUP/NATURALGIFT正PP/目标/属性及ORAN完整80标志 |

五份合同指定反证全部新读，逐份 bytes/SHA256/blob 与恢复索引一致：`EV-8dd3ec6afe1b1ada`、`EV-e0bd1ab619cc4c90`、`EV-1c4621c48f63b0f5`、`EV-8c075af60e244dcc`、`EV-9164b2d28833a017`。其中其它根因 GR6-C-001 的24个隔离向量和内部空槽事实未转记为本批已执行。两行为项的原反证承认通用异常总述有效，但不能据此推断具名合法入口；本审重新沿真实资格、准备、消费者及包装检查，支持原裁定，未把旧支持当本候选 PASS。

## GR6-CA-EB-001：PASS（required/P2）

1. **身份与裁决**：canonical/root均为本ID，无新增别名。原主合同B§3第89行；本候选第93、105–107行，测试B16/B72–B76，§7/§8同步。保持固定required/P2，未重新裁级或扩成所有围攻故障。
2. **双向证据**：AI MultiHit151–185分别给空名单失败、合计基数、破替身目标评分；ChooseMove25–42确认真实资格之后才由预测标记控制整招失败。65–68包外初值100，232–285完整评分返回才赋值，294–310评分标记独立。AIMove81–106/367–374的普通粗伤不因合计基数0早返，返回后再以实际合格人数除。候选正文/目录准确回指这条链，coverage54/56/58三族定位保留。真实围攻155–180及WP46§3.1没有前置命令名单拒绝，不能拿真实使用失败门消除AI评分可达性。
3. **合法前提、反例和提交前缀**：普通内部训练家单打已到选招、无先行换人/用物/已有选择；技能32、AntiPredictMoveFailure、评分开；U存活非蛋/真中毒，默认BEATUP/正PP/其余真实选择门放行，业主仅U或全可战成员真状态，n0；T存活合法敌、正替身，本招不绕替身；普通正攻防HP、双方无物、没有先行粗伤异常、普通诊断正常返回。首个本处失败在人数除法，未到严格破替身比较/通用目标修正；包内评分未返回，100只是保留初值，不是成功计算。无菜单取消、无本处HP/阶级/PP/物品消费或动作登记；准备字段已写，不宣称统一回滚或诊断失败后继续。后续整次候选扫描可清模式破坏者，不能把瞬时前缀宣称永远保留。
4. **最小修订**：只将空名单预计失败明确受预测门，并补合法n0/替身异常和包装出口；P27、名单包含合格U、正常n、严格小于、真正逐人执行均保留。不是修参考、添加安全守卫、架构设计或永久缺陷兼容政策。B16加预测开启前提，其输出未改。
5. **验收/回归**：B72–B76逐条静态核准，详见下表。健康成员种族攻100给n1/P15；因n−1为0，正替身不获本项+10，仍继续通用修正。预测开启→20、目标体未入；清替身只跳本处分母，不取消后续通用粗伤；关闭评分→目标体未入。R1压榨入口、R2会心、R5生命水滴、通用选择和真实围攻责任均按具名范围新核对，未借旧PASS验新异常。
6. **独立裁定**：本非作者直接新审以上固定三份mirror，支持原反例及全部验收，**PASS**，无必要修复。337项工具检查没有替代这一语义裁定；没有执行围攻处理器、完整评分器或宿主。
7. **依赖/接收**：主批唯一R6-U04；WP51技能/资格/包装、WP52-A通用评分/权重、WP46真实围攻为具名非阻塞作者依赖。正文与测试候选交R6-I唯一正式写者；共享测试须与R6-U02贡献合成。原audit追溯同步仍属整合者，审者不写。接收后须绑定实际合成全文、直接/传递接口及历史回归独立复验；本PASS不提前签后续门。

## GR6-CA-EB-002：PASS（required/P2）

1. **身份与裁决**：canonical/root均为本ID，无别名；原B§2.1第54行，本候选第54、61–63行，B77–B82及§7/§8。保持required/P2，空当前物与有物无完整数值分开。
2. **双向证据**：AI MoveAttributes1423–1436失败/基数独立。真实MoveAttributes1338–1380中，该族基底类型先检有物、无物安全给一般；基数先访问当前物身份，空物在数据获取及默认1之前失败。Battler81–83→GameData109–115支持真实空物，无NONE兜底。ChooseMove准备/目标阶段→OtherScores297–323通用伤害→AIMove81–92中等基数，使本招没有专属目标分也可触发。异常出口仍是包外100/未完成赋值/诊断正常返回。正文与B77–B82正确对应此链。
3. **前提、反例与边界**：普通内部训练家单打已到选招，默认NATURALGIFT、正PP、U无物且其它真实门过、T普通存活合法敌、正攻防HP，32/预测关/评分开、无先行评分异常、诊断正常返回。类型查询不会因空物先失败，通用粗伤在专属基数缺物身份首次异常，无正常0或1基数；保100不等于威力100/最终动作。类型文字处于WP47-A§3.1的该族基底类型上下文，后置输电/等离子浴覆盖仍依既有共享合同，不由本PASS扩大为任意场域的最终类型保证。无取消、HP/状态/PP/物品提交或本处动作登记；准备上下文不统一回滚。
4. **最小修订**：补独立门下的合法无物查询异常及候选包装，明确有当前物的无完整匹配才正常1→0；有完整数值至少10、默认67项表、真实无果起用失败/真实续击消费前缀均未改。不新增getter、异常守卫或统一安全回退。
5. **验收/回归**：B77异常/保100；B78仅开预测→20且通用基数未入；B79有效ORAN完整NaturalGift_POISON_80→P80，不由评分耗果；B80存在有效、仅前缀无完整数字的合法作者数据→正常1→0，与空物异常不同，非默认PBS样本；B81只关评分→通用伤害未入；B82技能31→数据P1先替60、跳专属基数，不声称最终分60。GR3-M08-001真实首击提交/HP71/第二击缺物边界及高HP/单击对照保留，未被AI保100替代。
6. **独立裁定**：固定候选在原有效前提和全部静态验收下 **PASS**，无必要修复。独立质疑了隐藏无物命令拒绝、类型阶段先异常、未匹配正常回退、通用伤害不消费等可能性；上述源链不支持这些反证。本轮未执行自然之恩定义/评分器/宿主。
7. **依赖/接收**：唯一主批R6-U04；WP51、WP52-A通用伤害、WP47-A真实数据/类型/起用/续击为非阻塞作者依赖。R6-I接收正文/测试并完成原audit同步，测试与U02串行合成；WP47-A又有U05本轮贡献，真实接合的复验须对整合后的实际版本，不能由本基线消费者核对预签。

## R6-CA-EA-P001：PASS（required/P3，导航项）

1. **身份与裁决**：原ID/根因保持，无别名；仅覆盖附表第21行导航修订，P3。不是AI运行缺陷，也未新增行为要求。
2. **双向证据**：Misc358–362/386–390/414–418/440–444四个整体失败登记为撒菱≥3、毒菱≥2、隐岩/黏网真；ChooseMove38–43/177–191在合法候选且预测开启时消费为20。真正正文在§5.2，原第178行、本候选第186行；coverage第23行的整体分本来已正确在§5.2。
3. **反例/正常对照**：读者仅循原AddSpikesToFoeSide失败定位§5.1，找不到满3层失败；循修订§5.2可以找到。天气/四地形/RemoveTerrain仍应§5.1，整体效果分§5.2为正常对照。没有运行、菜单取消、资源/动作或持久化影响。
4. **最小修订**：第21行只拆定位组，四危害失败改§5.2，天气/地形/移除地形保留§5.1，其它身份/copy/注册序和正文原值不动。使用稳定章节导航，未机械保留已位移的178行号。
5. **验收/回归**：四身份全部正确定位；天气/地形正常对照保持；第23行、主稿危害整段和B39原字节不变；英文身份/copy序列逐字相同，仅这一行替换。是SOURCE_STATIC定位比较及TOOL_VALIDATION，不需要也没有行为向量执行。
6. **独立裁定**：本非作者新读源、正式全文、附表/差异确认 **PASS**，无必要修复。原父审意见只支持窄导航范围，本报告保持该范围。
7. **依赖/接收**：唯一R6-U04，候选coverage交R6-I唯一写者；无作者阻塞依赖。接收后的全文导航/共享正文仍需实际版本复验，不借导航项扩大运行/兼容或关闭范围。

## 全部11项静态验收与证据等级

共同夹具为候选目录第230行，继承普通内部单打、合法敌目标、正PP/真实资格、32/预测关/评分开、无前置异常或重定向干扰、普通诊断正常返回；各行只作其独立变化。下表结果是本审者的SOURCE_STATIC/DERIVED_VECTOR核定，**不是执行输出**。

| 向量 | 新回源核定的预期 | 结果 |
| --- | --- | --- |
| B72 | 围攻全状态n0/正替身/不绕：粗伤返回后人数除零，未到比较/通用分；正常诊断后候选保初100 | PASS |
| B73 | 仅开预测：空名单整体失败20，目标评分不进入 | PASS |
| B74 | 仅添健康无状态种族攻100成员：n1/P15、严格比较界0、无此+10，通用修正继续 | PASS |
| B75 | 仅清替身：跳本处除法，通用伤害近似仍独立执行 | PASS |
| B76 | 仅关评分、预测仍关：专属目标体未入，无本处异常 | PASS |
| B77 | 无物自然之恩：类型基底空守卫安全，通用粗伤/中等专属基数先缺物身份异常，无正常0/1；候选保初100 | PASS |
| B78 | 仅开预测：无果整体失败20、目标基数不进入 | PASS |
| B79 | 仅持有效ORAN完整80标志：基数80、无本处缺物异常，评分不消费果 | PASS |
| B80 | 持物存在、有效树果仅前缀无完整数字：正常返回1再改0，不等于最终粗伤0 | PASS |
| B81 | 仅关评分、预测仍关：通用伤害消费者未入 | PASS |
| B82 | 仅改31且保评分/反预测：P1先替60，专属基数未入，不保证最终分60 | PASS |

已全文检查作者 `validate.py`，重新计算其相同337项检查：只适配固定R对象缓存位置，以及把作者当时的工作区差集/未跟踪观察替换为固定发布的提交差集/空未跟踪集合，未改任何行为预期或静态断言。适配脚本 [reproduce_author_checks.py](reproduce_author_checks.py) 与真实过程 [processes/reproduced-author-337.json](processes/reproduced-author-337.json)、完整stdout/stderr均保存。两份作者归档结果各337项、各exit0；本复算337项的检查名/结果与两次原结果全部一致。它们不是674个不同行为测试。

337项中263项是旧表行保留断言（含结构/表头），15项输入身份＋15项mode/type，其余为基线、差集、定位、目录、文字及常数算术。这些检查不能证明处理器运行、最终动作或宿主恢复；作者文件已经明确保留这个等级。本审另做55项独立身份/包清单/不可变对象/补丁重建/证据分期检查，[static-verification.json](static-verification.json) 全部通过；在自有scratch从固定main应用补丁，三份结果逐字等于被冻结镜像。此处没有编辑实际正式稿。

| 等级 | 本轮实际范围 |
| --- | --- |
| SOURCE_STATIC | 本人新读合同/三项原提案/五份反证、固定源上下文、正式/镜像全文和具名消费者/历史span |
| DERIVED_VECTOR | B72–B82全部11条人工路径推导、原正常/边界对照；未执行 |
| TOOL_VALIDATION | 337项静态复算＋55项独立载荷/文本/补丁检查、Git读取/发布/完整对象读回；Python成功不转成行为执行 |
| ISOLATED_REFERENCE_EXECUTION | 0，NOT_EXECUTED；没有加载R或调用实际Ruby定义 |
| INDEPENDENT_BEHAVIOR_MODEL | 0，NOT_EXECUTED；没有评分器/独立完整玩法模型 |
| COMPLETE_HOST/DEMO、真实save/生产服务 | 0，NOT_EXECUTED；不签原生图形/音频/输入、宿主恢复、任意插件组合或持久化成功 |

## 必要消费者与精确历史回归

新读WP51全文1–156；WP52-A§1–§3.3（1–111）；WP47-A§3.1/§3.1.1（56–94）；WP46§2/§3.1（1–64）。四文件在固定候选中仍等于固定main字节；它们不是本审整域新PASS。R5任务合同、R3/R4资格和唯一激活只读取相关完整对象/字段；大文件其它记录未作为本批复审成果。

| 资格或接口 | 本次新核对及保留结果 |
| --- | --- |
| R1原WP范围、WP52-B-R01 | 新读 `review/wp52b-wp52c-wp54-recheck-2026-09-28/report.md` 的R01完整内容，源AI MoveAttributes188–195、资格与基数包装重新核准；压榨普通有限PP0提前排除，确达处理器PP0缺别名异常、PP1/2=200/80及负PP短路50，正文及B04/B04b/B04c保持。原资格不覆盖新增异常 |
| R2 229控制/21批/341精确贡献资格，GR-015相关span | 新读原GR013–016 report§3及recheck-v2，当前A/B会心条款、AIMove495–545、AI MoveAttributes430–475与B12b/AE N02b–d。旧表16/8/4/3/2截索引4为2→局部115；新24/8/2/1截索引3为1→60；负下标旧2/新1均满足粗伤≤2，真实禁会心责任保留。只核本批接点，没有重新授341贡献整域资格 |
| R3 23/76、GR3-M08-001 | 从 `9366d9d…` 读取required23-acceptance中完整checks/15对象，与现WP47-A/WP46具名正文比较。ORAN首击80/反伤20/自耗至71、C/I/R/P/Belch前缀、续击首次缺物身份异常、高HP101/单击对照仍正确；AI保100不替真实执行恢复。M09 optional/U08历史未启动、M02 no-required不重开 |
| R4当前17/76与B5原16/75 | 从固定 `9366d9d…` 新读R4-U04实际acceptance，核其GR4-M05-001是主动PP道具资格，非本批无物/状态选招前门。源真实命令资格及WP51主动道具/选招责任分开；本候选未改该路径/任何公共资格。Summary残余、历史旧FAIL/WAIT保留，不由本签扩大 |
| R5唯一92CLOSED、GR5-M09-001 | 读取 `13fddb…` closure-candidate完整records/66，R5-U05完整task-packet与其精确 `22fba…` 对象同字节；核 `12df95…` activation唯一键/当前计数/保留历史/执行字段，绑定候选13fddb＋审查044c348，92/OPEN0、51P2/41P3只限原精确scope。新读AI Healing225–255；生命水滴独立恢复守卫和B64–B71全保留：100/107/95、合法被封锁盟友、开预测/关评分/关HP意识/自身封锁早拒。不是把旧CLOSED转签到本批新异常 |
| 所有受影响原表/覆盖/正文 | 除声明的7个旧行替换（coverage1、body4、catalog2）外旧字句保持；AB/AI/AE及CE整体不变，旧测试表行除B16补门均保留。BE75→86、B72–B82唯一，正文与目录数一致。危险正文/整体评分导航正确，所有英文身份/copy序不变；正常多击、真实资源消费、权重/动作未误改 |

R1不臆造总数；R2五元组资格不提升为新全量行为审查；R3 23/76、R4/B5区分及R5唯一选择都原样保留。两advisory MISMATCH、旧candidate01 G03/G09 FAIL、U03旧FAIL/定向修复、SC-U07-001体内LF错误/纠正不抹除；第五7optional、7no-required、6policy、13limits与第六新增policy/L14继续隔离。没有增添新mandatory、未来兼容决策或行政补修门。

## 接收与剩余门

该候选可以提交R6-I接收。输入冲突图实际只将U02/U04的 `test-catalog/combat-requirements-wp49-51-52.md` 列为本批共享冲突；正文和coverage仍交唯一正式写者。作者发布载荷把当前接收者记为 `thread01a13a93-d1da-71e4-a488-63b8524f503d`（R6-I），本审仅保留其输入绑定，不冒称看到了该线程运行状态。

R6-I须串行合成U02/U04测试贡献，处理WP51/WP52-A和WP47-A后继实际接合，完成原 `audit/source-traceability.md` 同步；然后由非作者对**真实整合后全文/接口/受影响历史span**重新给结论，依次登记实际整合、INTEGRATED_PASS、正式接受、CLOSED。本审者不替写这些对象或给未来版本预签。没有候选内容阻塞；有效配置回显及宿主/运行未知如实保留在限制记录中。
