# R1 combat 全域独立复核：FAIL

固定候选 `5666b7b912e2fb79b5119283ee6a37401a7071db`；旧候选 `d62b41f4d620e50bb04c80a7505374bd284d8210`；旧独立FAIL `a0352c7fba38391afc535525988245701d5ce202`。本域覆盖23正文、4相关catalog、全部136旧行（65 PASS / 45 FAIL / 26待查）、134新活跃行（其中8追加）、10退役旧行与10新metadata，9组原finding全部case。结论仅针对此固定去向清单，不是最终R8整改或目标兼容验收。

逐旧行新结论：{'PASS': 128, 'FAIL': 8}；活跃行：{'PASS': 126, 'FAIL': 8}。旧PASS中FR67因同根因传播重新判FAIL，其余64项仅在来源/去向/范围不变、职责补充无冲突及同根因检查后保留。旧FAIL/待查不自动继承；8篇AI正文1523行已在本上下文重新全文读过，其他变更按完整源节/混合表格及必要消费者复核。逐项结果、具体理由和实际新读区间见 `combat-results.json`。

## 阻塞问题

### COMBAT-R1-01 / P2 — 跨半退出能力的真实逃跑与业主替补仍留Showdown单方父行

功能：FR-000067。

FR67 §5.1包含野生拥有者经WP41可逃后写决定3，以及训练家非回合末等待业主选择、负选择返假/保留提示前缀。现去向Showdown承担，职责仅通用框架输入/接收与Showdown阶段执行，prototype_refs和feature_refs均空，没有框架消费世界结果及MZ等待/选择的候选边界。direct_refs对WP41/WP42的整篇共同前置未给该入口的不同归属，不能替代已在FR20/58修正的逃跑/替补协议。

证据：wp49-ability-phase-triggers.md L100–123。候选JSON pointer：FR-000067 `/features/61`。

必要修正：保留纯能力反应粗行；为该具名退出边界补协作或待原型决策，明确框架结果消费、Showdown资格/写决定、MZ业主选择，并接FR22/PROTO-ESCAPE与替补/终局合同。无需现在运行原型。

### CAI-R1-01 / P3 — AI策略与查询已分开，共享准备写入/清理仍未分配候选责任

功能：FR-000076, FR-000088, FR-000089, FR-000098, FR-000099, FR-000111。

这六行现在说明框架拥有策略/评分、Showdown提供实时查询，改进有效；但所有行仅把“共享准备字段与异常前缀”留为同式问题，没有给实际写calcType/全局moldBreaker、清恶作剧之心/GemConsumed、调用真实准备改类别/秘密之力字段及中途异常已写状态的候选拥有者/交接责任。源章明确这些不是纯输出查询，也无统一回滚证明。把所有写入默认为Showdown或框架均超出实际字段陈述，故旧CAI-01所要求的这一独立边界仍证据不足。

证据：wp51-ai-action-selection-and-skill.md L132–148；wp52-a-generic-numerical-and-status-evaluation.md L9–108；wp52-b-field-damage-healing-and-target-evaluation.md L23–114；wp52-c-items-calling-and-control-evaluation.md L106–133。候选JSON pointer：FR-000076 `/features/70`, FR-000088 `/features/81`, FR-000089 `/features/82`, FR-000098 `/features/90`, FR-000099 `/features/91`, FR-000111 `/features/102`。

必要修正：在上述共用评估/准备合同按行为组明确哪方拥有并修改/清理共享战斗准备状态、另一方怎样消费，保留正常清理与异常前缀差异；可用一个共享粗合同引用，无需按每字段造功能ID或现在运行目标。

### CAI-R1-02 / P3 — 已有/前向归属索引仍是活跃待实现AI功能

功能：FR-000086。

完整§5只按文件/包/族列A阶段已有/前向身份归属，明确B/C只登记边界、当前状态以各自附表为准。已有行为登记/默认查询已由FR80、FR94/95、FR103/104等承接。FR86仍以“拥有评估登记的已有/前向责任的策略、默认参数、候选/评分输出”作为框架功能；本源节并没有这样的独立策略或输出，替换模板名未创造功能。

证据：wp52-a-evaluation-coverage-and-data.md L237–255。候选JSON pointer：FR-000086 `/features/79`。

必要修正：保持FR86/source历史完整，转退役/metadata并连接现行具体评分/登记消费者；勿将A阶段定位当新的实现单元，勿删除或复用旧ID。

## 九组原finding复核

| 原finding | 结论 | 完整原case / 同根因传播 |
| --- | --- | --- |
| CAI-01 | FAIL | 41原case全部核对；无新增传播FAIL |
| CAI-02 | FAIL | 3原case全部核对；FR-000086 FAIL |
| CAI-03 | PASS | 16原case全部核对；无新增传播FAIL |
| COMBAT-01 | PASS | 2原case全部核对；无新增传播FAIL |
| COMBAT-02 | PASS | 7原case全部核对；无新增传播FAIL |
| COMBAT-03 | PASS | 6原case全部核对；另核FR29共享MZ承接充分 |
| COMBAT-04 | PASS | 7原case全部核对；无新增传播FAIL |
| COMBAT-05 | PASS | 6原case全部核对；无新增传播FAIL |
| COMBAT-06 | FAIL | 2原case全部核对；FR-000067 FAIL |

COMBAT-01退款残留已独立为731；COMBAT-02各持久写回/物权病例已有具体双方责任，写生735扣除父范围；COMBAT-03原六case均保留修正信用（733/732/734/736/737/738）。COMBAT-04七个来源/责任/历史行完整归档且不计实现；CAI-02原三个责任行也正确退役，但FR86同根因仍活跃。COMBAT-05必要共享合同允许明确间接导航，例如FR61→740→577→574/576能到WP50持物调用/触发，不因未单独列一个direct_ref否定修正。COMBAT-06原20/58两case已经接逃跑原型，FR67传播未接。CAI-03全部16个依赖原case已补具体A/B/C、WP44/47/50等合同。

## 父子范围、metadata与catalog

136旧ID在active/retired恰一次；全部旧source对象逐字段不改；10退役行剥去retirement后与d62完整原行相同。8个追加ID为731–738，无复用；134活跃有效范围在本域无交叠。各新MZ单元允许带框架规则/数据伙伴，未要求逐句造ID。

全部37个catalog章节保留静态验收来源和NOT_EXECUTED性质，没有制造活跃功能。没有把“缺直接孩子ID”当缺陷：如退款/目标选择可由FR10的excluded_child_refs到731/732，写生由52到735，报名由114到736，裁判由129到737，回放由136到738。父行明确扣除与孩子直接依赖共同提供可理解导航；原静态向量未改变。10个metadata单元同样保留旧ID导航、主合同及必要间接消费者。逐节结果与导航列表在JSON，不把同WP编号本身当语义证明。

## 固定身份、版本和实读

对27文档逐篇用 `git show 908273...:<path>` 取当前字节，与B8、候选及工作区相等；当前正式树 `6ae817df5b11eafdec671214b0d04e542ad364bc`，工作区正式树仍B8 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。不能据本地文件冒称908当前。完整bytes/SHA256/blob与真实静态命令exit见 `combat-static-evidence.json`。

本轮源新读范围如下；其余源事实只在固定身份/旧完整阅读记录及未受影响裁定范围内继承，不声称本上下文重新全文读完27篇。所有AI8篇完整重读；WP55/WP56完整重读。

| 文件 | 本轮实际新读 | 旧完整信用 |
| --- | --- | --- |
| wp39-battle-context-and-participants.md | L196–278, L322–335 | `agents/combat-results.json#/reading_ledger/0` |
| wp40-commands-obedience-and-action-order.md | L78–123, L347–360 | `agents/combat-results.json#/reading_ledger/1` |
| wp41-switching-positioning-and-escape.md | L46–137, L152–195, L238–250 | `agents/combat-results.json#/reading_ledger/2` |
| wp42-growth-end-of-round-and-battle-outcomes.md | L25–96, L166–202, L275–285 | `agents/combat-results.json#/reading_ledger/3` |
| wp45-weather-terrain-side-and-position-effects.md | 无新正文输出；实际字段差分/身份核对 | `agents/combat-results.json#/reading_ledger/4` |
| wp47-a-attributes-targeting-calling-data.md | L202–214 | `agents/combat-results.json#/reading_ledger/5` |
| wp47-a-move-attributes-targeting-and-calling.md | L177–221 | `agents/combat-results.json#/reading_ledger/6` |
| wp47-b-control-items-coverage-data.md | L95–105 | `agents/combat-results.json#/reading_ledger/7` |
| wp47-b-switching-control-and-item-changes.md | L19–47, L96–159, L182–200 | `agents/combat-results.json#/reading_ledger/8` |
| wp49-ability-phase-triggers.md | L85–272 | `agents/combat-results.json#/reading_ledger/9` |
| wp51-ai-action-selection-and-skill.md | L1–160 | `agents/combat-ai-report.json#/source_ledger/0` |
| wp51-ai-decision-defaults.md | L1–92 | `agents/combat-ai-report.json#/source_ledger/1` |
| wp52-a-evaluation-coverage-and-data.md | L1–260 | `agents/combat-ai-report.json#/source_ledger/2` |
| wp52-a-generic-numerical-and-status-evaluation.md | L1–253 | `agents/combat-ai-report.json#/source_ledger/3` |
| wp52-b-effect-coverage.md | L1–111 | `agents/combat-ai-report.json#/source_ledger/4` |
| wp52-b-field-damage-healing-and-target-evaluation.md | L1–248 | `agents/combat-ai-report.json#/source_ledger/5` |
| wp52-c-item-control-coverage-and-data.md | L1–191 | `agents/combat-ai-report.json#/source_ledger/6` |
| wp52-c-items-calling-and-control-evaluation.md | L1–208 | `agents/combat-ai-report.json#/source_ledger/7` |
| wp54-entry-eligibility-level-adjustment-and-clauses.md | L15–50 | `agents/combat-results.json#/reading_ledger/10` |
| wp54-entry-rules-and-cup-data.md | L49–87 | `agents/combat-results.json#/reading_ledger/11` |
| wp55-facility-session-and-restoration.md | L1–152 | `agents/combat-results.json#/reading_ledger/12` |
| wp56-palace-and-arena-variants.md | L1–141 | `agents/combat-results.json#/reading_ledger/13` |
| wp58-battle-recording-and-playback.md | L138–181 | `agents/combat-results.json#/reading_ledger/14` |
| combat-requirements-wp39-40-41-42-45.md | L75–76, L79–120, L137–137, L163–163, L170–170, L246–260 | `agents/cc-catalog-full-results.json#/documents/3` |
| combat-requirements-wp47-ab.md | L19–19, L34–37 | `agents/cc-catalog-full-results.json#/documents/4` |
| combat-requirements-wp49-51-52.md | L1–42, L53–54, L62–62, L312–312 | `agents/combat-ai-report.json#/source_ledger/8` |
| combat-requirements-wp54-55-56-58.md | L1–60, L117–190 | `agents/cc-catalog-full-results.json#/documents/5` |

已读本次合同、根AGENTS、候选README/R1 README/review-prompt、R8 DELIVERY/review-SKILL/handoff范围、旧root REPORT/完整本域逐行结果/原finding/阅读台账；作者处置表仅作被审陈述。报告不是clean-document-revision最终态写作，不改正式来源事实。

## 保留边界

四类原型均未运行，未知目标版本/格式与用户范围决定保留；这些未知不免除分类语义审查，也不单独阻塞合理粗标。U02/U03 ACCEPTED回执已读，CLOSED均false；只接受FR403/588所在域的部分回填。combat正文/相关catalog的current908同字节，U06绑定继续待整改后核对，不扩为已接受或全上游完成。

请求继承gpt-6.1-sol / ultra / default / Fast off；工具未给权威执行echo或云UUID，actual model/effort/tier/speed/Fast/UUID逐项UNVERIFIED。只执行静态Markdown/JSON/Git，未运行参考、业务向量、宿主或新框架。本代理只写本新review的agents/combat-*，未切支、提交或修改作者工件。

## 共享合同补充核对

成长持久依赖WP19/20/30等已补；经实际共享路径复核，FR29 direct_ref固定WP30合同，FR206有效范围含§6.3 L168，明确战斗/通用wrapper共用4旧+1新遗忘、取消/HM重选且已有MZ职责；FR207另管持久/临时槽同步。现有共享MZ承接充分，不要求重复FR659/MZ标签。

另按root请求核WP72测试战斗消费者：FR257关联004/011/022/025/031/529合理。FR261的120项编辑只写当前战斗四层，L217明确不改原个体；其框架“原个体及持久层白名单读写”职责已向Demo owner报告，域外最终裁定由其整合，不在本域重复计finding。外域实际新读区间/固定身份见additional_reading_ledger。

FR67与FR29的裁定区别：FR29引用的WP30 §6.3实际明说战斗/通用两wrapper共用遗忘选择，而FR206已给该共享界面MZ职责，故共享导航足以PASS。FR67引用WP41/42仅为整篇通用前置，未说明跨半能力入口真实返回3与业主等待的框架/MZ消费及原型门；该入口仍被描述为Showdown单方阶段执行，故保留P2传播缺口。此判断基于实际责任内容，未一律要求直接ID。
