# R3 combat：两行当前来源校准 FAIL；R2 依赖修正 PASS

固定候选 `c0f62d973180679134f2eb1a488c1dc359c8658f` 的 combat 粗标、责任、范围与依赖 facet 均通过；**当前来源校准仍有一个 P3 根因、两行失败：FR29/32，`R3-EV-BOUNDARY-001`**。该根因由 root 与 world 的 FR456 合并，不能把两个分工算成额外接受票。实际 final5f 正文正确，错误在候选对其变化的摘要；不否定来源接受、去向类别或已修的 PP 依赖。

完整逐行结果：[combat-results.json](combat-results.json)。逐边证据：[combat-dependency-crosscheck.json](combat-dependency-crosscheck.json)。精确 finding：[combat-findings.json](combat-findings.json)。独立静态复核脚本与证据：[combat-audit.py](combat-audit.py)、[combat-static-evidence.json](combat-static-evidence.json)、[combat-audit-run-history.json](combat-audit-run-history.json)。没有作者候选修补、正式规格改写、提交或业务执行。

| 本域口径 | PASS | FAIL |
| --- | ---: | ---: |
| 136 原 ID，含 11 完整退役 | 134 | 2 |
| 134 当前 active overall | 132 | 2 |
| 分类 / 责任 / 范围 / 依赖，各 facet | 各 134 | 0 |
| 当前来源校准 facet | 132 | 2 |
| 11 retired metadata 合并记录 | 11 | 0 |
| 96 当前出站 feature-ref 边 | 96 | 0 |
| 三项 R1 残留、COMBAT-R2-DEP-001 | 4 | 0 |

**唯一新根因与必要修正。** `routing-manifest.json#/features/28/differences/1`（29）和 `/features/31/differences/1`（32），以及 `revisions/r3/feature-source-deltas.json#/records/8/source_fact_delta`、`/records/9/source_fact_delta`、`source-file-reassessment.json#/records/3/source_fact_reassessment`，称“超总量EV受领者先在单项负上界夹取失败”。final5f WP42 L73 指向 WP19 §5.3 的正常模板 HP255/ATK255：总量 `255+255=510`，等于总上限；越的是单项 252。HP 先被处理，`252−255=−3`，因此单项区间先失败，尚未执行总量夹限。

可区分的独立静态对照是普通非 Shadow 存量 HP/ATK/DEF/SPA/SPD 各100、速度20，总量520、每项均不超过252。在首先处理 HP 时，单项余量152非负，而总量余量−10非法。因此“总量越额”不能推出“先在单项门失败”。这里没有执行 EV 分配器，只按已读的先后门和常数运算说明概括错误。最小修正是把上述当前摘要限定成“HP EV255 等单项越额模板在 HP 首项反向区间失败”；若还要概述总量越额，须按实际第一个非法余量门分开。不要改正确源正文、分类/责任/scope、现有依赖或未验证状态。32 的本身正文是世界善后 L203–250；它附带的同一文件级 EV 摘要同样不准确，但世界善后职责仍成立。

**R2 依赖修正。** 已完整新读 final5f 的 FR61 L116–159、66 L85–99、69 L191–216、目标739 L162–171、740 L192–205，以及68 L124–190、71 L225–261 正向对照。61 的 C/I/R/P、Belch/钱标记，66 的离场/真正濒死、HP/状态/形态与能力链，69 的天气、治疗、阶级和取物都不消费招式 PP 同步。三条错误 739 边精确移除，4/31/740 等真实初始化、终局、持物写穿与可更新还原记录边保留。

68 的 CURSEDBODY 读取当前招式槽的 PP/有限总 PP，且有已扣 PP 的失败前缀；71 的 DANCER 不额外扣原槽 PP、IMPOSTER 临时招式 PP/总 PP 固定5。这两条739边保留合理，740的持物用途也未盲删。739本身不因被误引用判失败。完整图由 R2 的98边减三条、增92→76，得到 **96边、25源、53目标**。

全部边保留每条实际用途、源/目标有效范围与身份、R2信用及本轮非影响理由。R2与final5f有效单元相同的边仅保留其精确限定语义，不以整行相等自动授 PASS。改变的目标 13/29/32/135/446/451/677/683，和新增源92，均连同相应本域调用者完整新读。446的删档导航不改变设施安全保存 IO假/其它异常分层；451新增有序删除是恢复层对照，不为设施补造自动恢复。677的野生输入/debug细化不改回放命令覆写及中止；683新增倒下音频/动画回退不改捕获ME3.5秒、消息等待和BACK中止。目标消费者的新增内容不使原真实用途失效。

**FR92 与共享 AI 准备。** final5f WP52-A §6 L211–246 及 FR76 L132–151 已完整读。原始类型候选发现不查PP；当代只首槽、旧代全部槽，排伪类型和已有类型。随后计算后类型的伤害匹配只过滤有限总PP下的PP0，不重做 Disable/Taunt 完整命令资格；首次匹配只加14一次。普通 User/0 目标路径不消费这项逐目标贡献，也不能推定完整候选总分固定100。框架拥有偏好、候选及贡献评分，战斗侧候选提供当前类型/PP/伤害分类与计算类型，新增92→76连到真实候选/目标数调度；direct_ref 使用B8真实WP51 §5标题，没有把新current锚点伪装成旧source。

六个共享准备单元76/88/89/98/99/111的完整有效源与候选责任均新读，`revisions/r2/shared-ai-preparation.json`与固定R2字节相等。逐目标恢复原评估对象、calcType/moldBreaker、Prankster正常清除、GemConsumed具名清理、真实类别/SecretPower prepare、damageState读取和 NaturalGift/BeatUp 异常前缀分开。框架协调策略/顺序；Showdown候选拥有具名共享准备写入及正常清理。没有把它们写成纯查询、通用finally回滚、真实HP/PP提交或已验证引擎支持。CAI-R1-01继续PASS。

**67/769 与四类协作边界。** FR67的scope/current locator仍精确100–105、107–123；FR769独占L106，原完整source不缩写。野生敌方当前同侧存活人数门、随后可逃查询、决定3，训练家拒绝门、回合末只召回、非回合末等待业主选择、负下标假与已提示前缀均完整保留。20/22/31/32/734和PROTO-ESCAPE是实际消费者，返回真不当作世界提交完成。

战斗物品11/731及28的186/187、正常终局31完整新读：登记扣物、分族执行复检、退款残留、同轮终局再次退款、下轮/失能直接清选择与容量错误分别处理。捕获525的菜单/登记/专用球执行及无目标异常，和31的接收/持物还原也按真实消费者看待，捕获失败不自动退球。成长29的EV/经验/逐级HP与PP回读、学招等待/取消，及外层32的世界善后保持分责；新EV错误仅在当前摘要。捕获、战斗道具、逃跑、战中成长四个协作原型均未运行，尚不能授目标兼容或实现验收，也不因此否决这些合理粗标。

**累计来源与新标题。** 本域完整读8个累计文件diff，重新读12个直接改变的active有效单元，逐18条改变的有效clause列结果。文件为WP39/40/41/42、WP52-A主稿、WP58及两个catalog。WP39的新零计数/原序边界与WP40配置范围priority、WP67-A实际UI/命令遍历相合；缺失计数不规范化为0，AI登记Q不保证Q被调度，也不推出自动获胜或最终UI。火药自损雨门、换人重算先于完整入场、王者盾牌配置身份、世界行走动画复位、debug helper随机域均有准确现有承载方。WP58与WP76 §7.2的主AI控制和直接helper访问失败已分开。

三条新增heading均从final5f取全体正文并重算file/unit、标题only hash和原Markdown行hash，现有消费者全部核用：

| 新标题 / 当前范围 | 当前消费者与结论 |
| --- | --- |
| WP39 §4.3.1 L167–182 | 2/7初始化与失败、9命令、13priority、677/686UI请求边界；PASS |
| 创建/EV catalog L299–317 | 2/7/9/13、456模板/额度、204分配、29成长；Z/M/EV独立静态组，PASS映射 |
| AI catalog L351–363 | 92现存直调贡献、76普通目标数消费；CV01–05与旧T02同步，PASS |

FR29摘要的错误不使目录映射到真实成长消费者失效。新增标题没有新增承载边界，无须伪造新实现ID；SOURCE_STATIC/DERIVED_VECTOR、NOT_EXECUTED 保留。历史本域456章节字节保留，当前459章节；四catalog原37节另有结果。来源9接受事件/39事项/230绑定与全局工具门由root/source分工核验，本域没有凭作者ACCEPTED标签代替目标行为证明。

**历史与限定继承。** 全27主文件各有一次primary reading ledger（23正文、4catalog），列B8、R2 current908、final5f及candidate工作区B8的精确身份和本轮fresh范围。8变源文件的完整diff为新读；完整有效问题单元、同根消费者与extra consumers另列。其余只在有效正文精确身份相同、职责/scope未变、累计源/目标不影响其真实用途后复用固定R2及更早全文阅读信用，不声称本轮重读27篇全文。解析JSON、枚举标题及字节核验未冒称语义全文。

136旧ID逐个保留原source，134 current locator全部从final5f重算。11退役对象剥去retirement后完整等于初d62行；11metadata对象与固定R2相等。retirement replacement和metadata消费者集合相同，允许原有排序差异。受13/92/135源变化或61依赖修正影响的索引范围已新读，仍是历史责任/真实消费者导航，不计独立实现；META33完整A历史表不冒充B/C当前行为。父→excluded_child_refs→子间接导航合理，不要求每个向量新ID。CAI-R1-02及COMBAT-R1-01继续PASS。

完整R2本域report/results、98边结果与相关静态/变换证据，及root REPORT、findings、feature/finding/issue/reading/section结果已读或完整结构化解析并对齐；本域每个旧/active结果的全部字段与root汇总一致，9组/3残留及11metadata对应一致。原9组的全部原case修正保持PASS；当前扩大scope中COMBAT-05因29校准新根因FAIL，其R2 PP修正已PASS，其余8组当前scopePASS。没有回写旧报告。

静态审查脚本最终exit0只证明记录、范围/身份、完整历史和结果对齐，不能消去上述语义FAIL。首次运行错误地把navigation引用集合要求成列表顺序相等，在META5/META7的既有顺序差异处断言失败；按真实语义改为集合比较，同时仍分别核完整原对象不变，未改候选，失败运行不授通过信用。运行历史单列保留。

实际model、effort、service tier、speed、Fast及真实cloud UUID缺权威echo，逐字段UNVERIFIED。当前结论仅为此固定候选的限定独立审查；不宣布来源全轮CLOSED、Showdown兼容、实现完成、用户排除或阶段批准。未执行Ruby/参考游戏/宿主/Showdown/未来框架，未触发外部消息。后续修复只需精确更正29/32及root合并456的来源概括，再冻结候选复核对应校准facet。
