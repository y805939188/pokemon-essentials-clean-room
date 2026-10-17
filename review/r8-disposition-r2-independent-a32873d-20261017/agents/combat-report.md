# R2 combat 独立复核：依赖传播 FAIL；分类修正保留 PASS

固定候选 `a32873d2860b15d9f5e27727db8f131f4ec433b6` 的三个原 combat 残留问题已修，分类 facet 通过；补核全部出站边发现新问题 **COMBAT-R2-DEP-001/P3**，本域 overall 为 FAIL。FR61/66/69 误挂仅负责招式与PP同步的739，须移除或给出真实用途后冻结新候选复核。目标739本身不因入站误用判失败。当前仍是 `908273093e1f6b27fc58249417675dd62d146224` 阶段，不授予 Showdown 兼容、实现完成、用户阶段批准或累计来源最终校准资格。

机器结果为 [combat-results.json](combat-results.json)，全98边证据为 [combat-dependency-crosscheck.json](combat-dependency-crosscheck.json)，作者变换限定核对为 [combat-author-transform-consistency.json](combat-author-transform-consistency.json)。可复现静态核对为 [combat-audit.py](combat-audit.py) 与 [combat-dependency-crosscheck.py](combat-dependency-crosscheck.py)，实际运行证据为 [combat-static-evidence.json](combat-static-evidence.json)。没有运行 Ruby、参考游戏、业务向量、宿主、Showdown 原型或未来框架；作者脚本只完整读文本与AST，从未导入或执行。只写本新 review 的 `agents/combat-*`。

## 分母与逐项结果

从固定 Git 清单与本域来源重算，覆盖 23 正式正文、4 对应 catalog、全部 136 原 ID、8 个 R1 新增及新 769。136 旧 ID 的 R1 结论为 128 PASS / 8 FAIL，本轮 overall 为 **133 PASS / 3 FAIL**；当前 134 active 为 **131 PASS / 3 FAIL**，分类 facet 134 PASS。11 份 retired 与 11 份 metadata 全PASS，37 个 catalog 章节另列。三个原残留 issue 全PASS；九原组的全部原case缺口已修，但COMBAT-05扩大的当前依赖scope因新传播问题为FAIL，其余八组当前scope PASS。原case与扩大scope分别记录，不改写R1报告。

126 个 R1 active PASS 的**完整行**与固定 R1 逐字段相等，包括 8 个 R1 新增 731–738；128 个旧 ID PASS（其中 10 个已退役）的完整记录同样未变。这只证明保全，不证明旧边语义正确。全出站边补核后，未改的61/66/69由R1 PASS转本轮overall FAIL，分类/持久责任facet仍PASS。逐行结果保留固定记录哈希、原修正信用、新用途判断与finding归属；其余依赖继承范围受完整98边检查约束。

## 三项残留问题

### COMBAT-R1-01：PASS

当前 WP49 L100–123 已完整重读。原 FR67 的不可变 source 整个对象保留；`functional_scope` 与 current locator 都为 **L100–105、L107–123**，只扣走 L106。新 FR769 的 source、scope、current locator 精确为 **L106–106**，不是覆盖整个 §5.1，也未把父 source 缩写掉。

L106 的野生敌方存活人数额外门、后续 WP41 可逃查询、决定 3 和返回真，训练家对侧全灭/换出/后备拒绝、回合末只召回后段补位、非回合末等待业主选择、负选择返假及已提示前缀、正常替换/清选择/模式破坏者与完整入场都在该子范围中。新行以候选粗责任分别安排 Showdown 触发、可逃/替补资格与决定，框架等待恢复、WP42 终局及世界消费，MZ 业主选择、等待与返回；依赖 20/22/31/32/734 及 `PROTO-ESCAPE`，保留负选择失败和回合末差异。

本轮另完整读 WP41 L46–137、L152–195 与 WP42 L166–236：可逃查询不同于普通/替补执行，写决定 3 不等于已做世界善后，正常终局 0/3 仍进入共同收尾，野生与训练家包装返回不同。新769没有用成功真假替代世界提交，也没有将等待当已完成替补。FR20/22/23/31/32/58/734 完整行未改，其原责任继续有效。父视图能直达 769，AB H02/H03 可沿 catalog→67→769；无需为每条向量另造 ID。

### CAI-R1-01：PASS

六行 76/88/89/98/99/111 的整段问题源章与混合表重读范围见下表，且完整读 `revisions/r2/shared-ai-preparation.json`。共享合同为 `CANDIDATE_UNVERIFIED`：框架拥有策略、逐目标评估对象重建和准备→查询→具名正常清理→评分/登记的协调；Showdown **候选**拥有供评估共享的战斗查询/准备状态、具名写入及正常显式清理。六行自身职责和问题字段都指向此合同，有具名正式源 direct refs。

| 行 | 已核具体准备/清理与异常边界 |
| --- | --- |
| 76 | calcType/global moldBreaker 准备；评分正常结束清 moldBreaker；最终登记仍用原槽。 |
| 88 | 逐目标恢复原评估招，Copycat/NaturePower/MirrorMove 替换后准备，防前目标替代招泄漏。 |
| 89 | 粗优先查询可写 Prankster 后显式清；宝石倍率调用可写 GemConsumed 后显式清；类别查询可真实 prepare，并可读 damageState。 |
| 98 | NaturalGift 无当前物品异常可发生在类型/忽略特性准备后；包装初值 100 不是正常威力或真实 HP 提交。 |
| 99 | BeatUp 空名单零分母可发生在共享准备后；无宝石夹具不凭空重置 GemConsumed，也不许诺所有字段回滚。 |
| 111 | 调用替换沿共同准备；SecretPower 真实 prepare 写附效代码，随后由 AI 自身坏映射评分，不补造真实降阶收益。 |

正常路径的显式清理与异常前缀分开；没有将评估写成纯查询、通用 finally 清理或失败后无残留。字段映射与目标兼容仍待固定目标版本验证；这不阻止本次合理候选职责分配通过。其余 AI 策略/偏好/登记数据、真实执行区分及 CAI-03 的现有依赖未改，六行只是新增具名共享准备导航，没有移走已有消费者。

### CAI-R1-02：PASS

WP52-A 数据附表 L237–260 完整重读：L239 明确按文件/包/族分组，A 阶段历史定位不授予 B/C 当前行为。FR86 已从 active 移除，**剥去新增 retirement 后与 d62 原完整行完全相等**，包括旧 source、去向计划、依赖和状态，没有保留 R1 的错误功能模板作为历史替代。旧 ID 未复用。

新 META33 是历史责任索引，不计实现。L241–242 普通换人实际消费者为 74/80；物品评级由 103–105 与 C 实际登记承接；其余 B/C 身份按现行有界登记及评分连 94/95/98–102/109–113。允许这些章节/字段组聚合导航，不要求每个效果新 ID。retirement replacement、META33 `feature_refs`、章节 `metadata_refs`/`retired_feature_refs` 同步。现行功能依赖和 catalog 活跃引用都不再指向86；其历史仍可查。

## 九个原组与继承范围

| 原组 | R1→R2 | 全部原 case 与本轮处理 |
| --- | --- | --- |
| CAI-01 | FAIL→PASS | 41 case；六共享准备与86重新语义判断，其余完整行/源身份相等后继承策略、数据与执行分界。 |
| CAI-02 | FAIL→PASS | 81/97/108 三原 case 精确保留；传播86→META33新审。 |
| CAI-03 | PASS→PASS | 16 依赖 case 全保留；六行新增具名准备源引用逐条核用，无现有依赖删除。 |
| COMBAT-01 | PASS→PASS | 10/11 两 case 与731/732父子范围、退款物品原型全保留。 |
| COMBAT-02 | PASS→PASS | 4/52/61/66/68/69/71 七 case 与735写生双提交完整保全；L106拆分不改持久/物权边界。 |
| COMBAT-03 | PASS→PASS | 5/10/18/114/129/136 六 case 及733/732/734/736/737/738未改；29→206的共享MZ遗忘界面合同继续有效。 |
| COMBAT-04 | PASS→PASS | 46/47/56/57/63/122/131 七来源/历史 case 完整保全；另同根因86新审。 |
| COMBAT-05 | 原case PASS；当前scope FAIL | 11/22/29/61/124/136原缺口修正保留，61→740→577→574/576及29→206共享导航仍明确；新传播61/66/69→739无真实PP用途，见新增finding。 |
| COMBAT-06 | FAIL→PASS | 20/58两原 case 精确保留；传播67精确扣L106、新769补逃跑原型与交接。 |

11 个 retired 均独立与 d62 原完整行比较，不是只检查 source；旧十个 metadata 整行相等，新 META33另审。四 catalog 共37章节的固定正文不变，静态/NOT_EXECUTED性质保留；映射只在 WP49/51/52 的八节移去86活跃引用，其余本域 catalog 章节映射完整相等。拆分后的退款、UI、写生、报名、裁判、回放和新769均有显式父子间接路径。

## 固定身份和实际新读

R1 本域 report/results、root REPORT/findings/finding-results/feature-results/reading-coverage/root-findings 均从报告提交 `8c8b46e919e0a15aaaf204f16df5b4ad3c9888b8` 读取，并与 `/workspace/r8-disposition-r1-review/` 物理副本逐字节一致。逐136旧行、134 R1 active、退役/metadata、37 catalog和九组完整 case 进行结构化核对；root 聚合的额外 attribution 字段不影响与本域原语义字段的逐字段一致。R1 源阅读信用按其完整 ledger 与原 a035 全文记录逐篇核身份，不将解析字节或旧结论当成本轮全文重读。

27 本域文件各用 `git show` 读取 B8、R1、当前候选与 current908，SHA256/blob/字节相同，且与 R1 ledger 与 root reading-coverage 的相同正文身份对应。134 个 current locator 的 unit/file SHA256、blob及精确scope重新计算通过，active范围交叠0；全部136原source对象保留。第一次分类问题定向新读如下；随后追加完整98边的全部源/目标有效scope阅读，见 `supplemental_reading_ledger` 与独立crosscheck文件，不把后来的真实重读错误记为最初继承。

| current908 文件 | 本轮新读范围 |
| --- | --- |
| wp41-switching-positioning-and-escape.md | L46–137、L152–195 |
| wp42-growth-end-of-round-and-battle-outcomes.md | L166–236 |
| wp49-ability-phase-triggers.md | L100–123 |
| wp51-ai-action-selection-and-skill.md | L132–160 |
| wp52-a-evaluation-coverage-and-data.md | L237–260 |
| wp52-a-generic-numerical-and-status-evaluation.md | L1–111 |
| wp52-b-field-damage-healing-and-target-evaluation.md | L23–114 |
| wp52-c-items-calling-and-control-evaluation.md | L106–133 |
| combat-requirements-wp49-51-52.md | L1–42 |

读取契约、根AGENTS、root/R2 README、最新review-prompt、要求的clean-document-revision技能及R8 DELIVERY、当前源范围入口；技能正文修订要求不授权改正式正文或审计历史。本报告没有这样做。全局工具、完整新接受输入、全局视图与保护由root承担；本域额外核对所有显式父行可读子ID，不能以此代替全局工具验收。

## 全出站边补核与新 finding

完整重读本域24个非空feature_refs源和52个不同目标的全部有效scope，逐98边说明用途，结果95 PASS / 3 FAIL。每边保留当前source/target范围和用途；补充reading ledger保留各完整有效单元的当前文件与单元哈希。没有只按标题、同WP或旧行相等判依赖PASS。

**COMBAT-R2-DEP-001/P3**：61有效L116–159为物品C/I/R/P/Belch及金钱标记，66有效L85–99为普通离场/真正濒死的HP、状态、友好和形态，69有效L191–216为回合末天气、治疗、阶级和取物。三者均挂739，然而739仅WP20 L162–171，定义招式包装、PP三层写回、升级学招与首招记录，没有上述三源的实际消费或明确排除用途。740才是它们正确的持物写穿与可更新还原记录合同。必要修正是移除这三条错边，保留真实物权/终局/初始化边；不要求变更正确分类、正式正文或目标739。

同一目标的正确对照不能批量删：68有CURSEDBODY当前槽PP门以及已扣PP故障前缀；71明确DANCER不扣原槽PP和IMPOSTER临时PP/总PP5，739作为临时/持久招式身份边界有真实用途。735→207按源L209明确“全局学习/遗忘不是复制效果替代”的排除性对照保留，不给写生升级摘要菜单；129→20按Arena顺序补位不同于普通业主选人保留对照。124→449/451限于候选direct_ref具名的旧格式/恢复失败层对照，不宣称设施保存调用迁移或自动恢复；保存假/传播异常的实际生产者是446。其余每条共享/消费关系见机器边账。

因此COMBAT-02的原持久职责修正仍PASS，COMBAT-05原六case的原缺口亦PASS；扩大后的COMBAT-05当前依赖scope FAIL。机器结果用 `original_case_verdict` 与 `current_scope_verdict` 双字段区分，当前feature overall另列，不反向改R1历史裁定。

## 作者显式变换限定核对

完整只读 `revise-data.py` L1–358、`write-evidence.py` L1–204，并解析全部11条explicit-decisions。没有导入或运行作者脚本。AST的11个decision调用的根因、description与operations均逐项等于决策记录；实际manifest的17个changed active、新增769/移除86、retired/metadata和全部coverage差分与作者data-diff逐项相等；10个受改metadata的显式源组消费者并集、retirement replacement与章节导航同步。

revise-data从固定5666原字节加载并拒绝覆盖不同输入，按明确ID/字段组修改；碰撞清理按五个固定文档身份，不以同WP编号重分类。67扣L106、769追加、86取完整d62归档都有显式代码。写出前保持source/current snapshot/旧归档body/决策/原型约束。write-evidence有固定f7e6语义快照哈希guard与pre-calibration绑定，将保全和作者处置写成待独立审查，而不是作者PASS。该脚本/数据一致性限定PASS，不能证明每个依赖语义正确；本次739新问题正说明完整行保全的语义局限。外域逐源语义由相应owner/root负责，本记录不转授未新读外域全文PASS。

## 独立待办

当前应用仍是908/U02、U03；后继49/0eee以及736 prepared locator不计作已应用/current。U04尚无正式回执，六文件/十新增标题及共享UI65的来源接受门保留，本分类修正结果不授予完整来源切换或2704当前覆盖。其余上游校准、目标版本/格式与四原型、用户范围/阶段决定继续待办。

实际 model、effort、service tier、speed、Fast 和真实云 UUID 无权威 echo，逐字段 UNVERIFIED。独立子上下文只是一次审查分工，不是多个接受票。可复现脚本首次适配误认为d62含retired_features，异常退出后已按真实v1结构修正；最终全部独立静态断言通过，未给失败运行任何通过信用。
