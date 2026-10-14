# group-D / U10 最终快照增量非作者复审

四项 U10 及具名 **GR6-F-002 联合接口均为 ACTUAL_PASS_SCOPED_STATIC**；必要正文修订 **0**。只签最终快照 `86bbc99b28d93db4ed9d6897daf5f3725ccd1808` 的静态范围。旧 9d 报告和 F002 的 PENDING_EXCLUDED 保留原样；本补充是在修订生产者加入后的新实际全文与联合复审，不能迁签旧报告。

审者 `/root/storage_review`，独立非作者，未撰写被审候选正文。请求 gpt-6.1-sol / ultra / default tier / default speed / Fast=false；有效 model、effort、tier、speed、Fast、平台 UUID 无回显，全部 **UNVERIFIED**。未运行 CLI/config/auth 探测或另开代理。

## 固定对象、增量和生产者

- final commit `86bbc99b28d93db4ed9d6897daf5f3725ccd1808`，workspace tree `67e8c55d520fa8cad2928cb4b95e24c3ed602d5a`，formal tree `ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c`。
- prior actual `9d5b4e99b617828690e6529b77a1e555d7c9eb1b`，tree `faae3b9a22c37a2e2e994553f59e7099c6394db0` / formal tree `74dccc64506d008d50cf1cdfd906f701931020cc`；固定 main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`。
- R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；全部以 git show 固定对象只读，没有源 checkout、修改或执行。
- final input `integration/U01-U14-final-composite-20261014/actual-review-input.json`：152860 bytes，3243 行，SHA256 `4671c1c31f18858a7719e88533029d746c62dfb77d4239cbb0cae633e79863da`，blob `ccf79b03165573f27070a417a2e3d986907f6623`。完整读取本组/U13批、具名文件节点、完整 delta_from_prior_actual、receiver/根编辑、状态/要求/排除/行政节点；不宣称全部其它批或全3243行语义阅读。
- U13 repaired candidate `9971fe84896786645cdcda3ab45e5caf7785cabc`，candidate tree `93ebe95d038954fd0dfb14fd07ac2f95a2485baf`，mirror tree `13d502e4131ace3e8fe2e59ce07a338b98ff7967`；独立 PASS 审 `411b563309a4e642e628dcf8289e36c6fe3fd37f` 的 repair-01/review-report.md **1–74全文新读**，11273 bytes，SHA256 `1445036698ffb92561fd87c121310ee65dac157f038b7ab098e5ccb21710970a`，blob `04df5bf6c83056ed44697f379a306ed5f3476d32`。精确 PASS 仅绑定修订候选；旧 3ef 原始全局 FAIL/局部 F002 接收依赖仍保留，本人新读该报告1–30及49–61。

WP54、WP55、设施目录、WP53实际完整字节与上述 PASS 候选镜像一致。生产者 PASS 是入口资格，实际裁决来自本次新全文、固定源和控制接合。五个 U10贡献文件与9d完全同字节，原replace/insert保留事实按旧精确receipt复用；WP66-A虽同blob仍按根要求重新全文读267行。机器核验不等于语义 PASS。

## 直接新读与准确复用

| final 正式文件（deliverables/final-specification-set/ 下） | 本人本轮直接语义读 | bytes | SHA256 | blob |
| --- | --- | ---: | --- | --- |
| combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md | 全文1–156 | 27791 | ce75fa71462b015963efb374f35325a8572698d86ab8d7595362a10675ca9148 | 5e424c11be607c4da3ecf6bcc2b5684706655cd3 |
| combat-requirements/wp55-facility-session-and-restoration.md | 全文1–150 | 23528 | 7d44312c84538220f024fdb32b9f840e0fd1b5d5c5ae961067fe61e9fe2e078c | 41050e9487f2b342d588ed0ba60860268d3436d5 |
| test-catalog/combat-requirements-wp54-55-56-58.md | 全文1–177 | 33561 | e6336cc59798b5f02dfe92c0e799344a3aa652627b2adfacbe6861562537f1c8 | cc28e3400d3bab787ce66c18156c45bcba6e5829 |
| pokemon-rules/wp53-safari-and-bug-catching-contest.md | 全文1–288 | 51237 | 1a9c9581d7b91bf5e4dd5474b9e2f4fef4115e795d7122663eb743e55bfaa999 | 5acc4f03fcecd49001325ff218034f00aff8a20a |
| user-interface/wp66-a-party-and-summary-ui.md | 全文1–267 | 45706 | 2a5ed9d7b30ae7f309381d96ef01d33b21324793e1761d8ef7cea8a90a4dac49 | 00acb05350a3cbd4fce1cc0ecf74cb3c845ae07f |
| user-interface/wp67-a-battle-interaction-and-presentation.md | 224–232 / 302–305 | 78217 | 66153fc4a013bf78743f37b58e9eeab1e7f8f01c139326e4e52f0176cd82553b | 44b915c2149ddc62f008445c309424626816fb55 |
| test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md | 224–242 / 947–1011 | 170395 | b4edb87c39ad8f9ec9f0572b55464d3f46f3d1da755ee578d33e2cef4ae546e5 | 4bc6fcda1473e6d31870dff079ba111bee97567b |

WP18全1–386与WP30全1–286沿本人旧9d语义全文、同一R/同blob准确复用：分别37612 bytes / SHA256 `a6410f5d3bcdedef2d682bddaeff4d49facef22e297f19b9a908d855893d346c` / blob `63048ab21f8fa5db77df11316f285db13e162594`；32271 bytes / SHA256 `f622dee4cd0fb1bbf89e47ef2c47bcf3c98f16dd12b5dfa48c006d39aec39fc3` / blob `1d6957846328bc5ad228932334c4fa32b02a47e5`。WP67-A旧全348保留，当前关键段另新读。共享UI本人旧208–358/566–938/947–1011复用，当前224–242/947–1011另新读；其余属于root/evidence团队receipt，未虚报本人全1026。

原 U10 合同四个完整七组/原提案/原反证、完整捕获/Safari原反证、party results0/1及精确R1–R5资格是本人上一轮直接语义读集，原合同120055 bytes / SHA256 `eb86301b11ef040f4a98365b93d8a6649409f32fe095a13974e697fe160d64f0` / blob `c33b84a0308bdd6776bee11dea7ee4243ba301f4`。本轮仅复用这些同身份固定事实，新增消费者与接口重新核。旧 report.md 16221 bytes / SHA256 `126f395a779c3a0792331c47bd3c935843c94767d737ebf47d4a6c015c00f3a5`；旧完整ledger/coverage身份在本轮reading-coverage.json，七份旧载荷完整字节未变核验在identity-validation.json。

新读 U13 合同完整 `/scope_contracts/1`（全部七组和原提案），文件370944 bytes / SHA256 `f202a22b1faf72a80edd2d663b9326bf4a9b9be4409fe88780835de909b08473` / blob `8c05e33d56064ff5a79ea25545f696b6156f4543`；不称整个6947行合同均语义已读。完整F002原countercheck项及完整两个stale-command负证据也直接新读。工作树合同/证据与final固定对象完整同字节另绑定。新producer字节diff全文153行已读。

R 本轮新读：Rulesets **1–323全文**；Party **1051–1139完整多选unit**；Challenge_Data **1–100**；BattleChallenge **1–45、79–95、118–143、181–304、345–362**。源payload完整bytes/hash/blob/模式、逐段UTC/cwd/argv/exit、JSON指针和语义区间均在新ledger/coverage，范围外源全文不虚报。

根AGENTS.md上轮1–297全文（6328 bytes / SHA256 `41cea9c6aa439dc70eaca2c26ce1f7967a887538c1aef25b9297c07b0437ff40` / blob `07b3655388c7405ec32aeb12e143db10a5e28c81`）本轮相同hash核验；未发现适用nested AGENTS，`.agents`缺失。仅写final-increment，不改旧peer、formal、candidate、public或git。

## 四项 U10 逐 ID 七组裁决

### R6-UI-001 — ACTUAL_PASS_SCOPED_STATIC

1. **identity_and_verdict**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。唯一 U10 主责、P2 required，根因是满队替换送盒暂停的删除/记忆次序；不扩为全部接收、伙伴还原或任意存储异常。
2. **bidirectional_evidence**：final WP67-A224–232 与 CP01–09 新读；R 及 WP38具名消费者沿精确同身份旧独读复用。消息前删除/消息后记忆与回填仍一致。
3. **premises_and_counterexample**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。满队 [A..F]、合法实际下标0、N待接收、至少一盒空位、sendToBoxes0（成功目标2同）、图鉴/命名/离场/盒名正常、无插件/竞争时，旧成员送盒提示内为盒持同一A、队伍[B..F]、N未入队、记忆未移。提示内受控失败仅保此前前缀，不保证队列清空、N收编、终局或外层恢复。
4. **minimum_revision_contract**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。实际226与228同时修好旧成员提示前删除和新成员提示后回填；不是只改附表。其余去向/强制档/显示初始0/BACK99保持。最小必要再修订0。
5. **acceptance_and_regression**：final UI947–1011完整新读中 CP01–09，正常0/成功目标2、仅N送盒、BACK/禁取消和两个消息局部异常前缀保持；原R1–R5资格按原精确载荷复用，不把未变散列作为实测。
6. **independent_adjudication**：同一非作者身份，四ID全部原提案/反证/消费者及R1–R5在旧9d独审已直接完整按资格读；本轮以精确同R/同blob绑定复用其读事实，新增消费者/接口另直接读。未重跑源/作者模型；未把原SUPPORT、候选PASS、字节相同或团队读集当成当前本人新全文。
7. **dependencies_and_receivers**：final WP67-A 与原 WP38 控制链保持；新 WP54/WP55 不改变捕获提示或旧成员/记忆观察点。WP38伙伴集合错配仍属另具前提，终局还原不被本项承诺。

### R6-UI-002 — ACTUAL_PASS_SCOPED_STATIC

1. **identity_and_verdict**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。唯一U10/P2 required，仅Safari Ball容量拒绝门及扣球前后观察；不扩普通球概率或会话全域。
2. **bidirectional_evidence**：final WP67-A302–305新读，WP53全1–288新读，双满门79、球消费85、接收90均核；其 final 新存档取消层15/239–247/276不替换球门。
3. **premises_and_counterexample**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。合法Safari、单存活目标、球10、默认容量6、正常前门/资源/输入、无竞争。party1且盒全满允许10→9/刷新/投球请求；party6且盒全满拒绝、不扣/投、不进入回末；party6但一盒有位允许。放行不是捕获保证；扣球后异常没有退球/正常收编保证。
4. **minimum_revision_contract**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。实际304完整写双满、拒绝重选与扣球→刷新→投球；WP53本来正确的门保留。再修订0。
5. **acceptance_and_regression**：final UI947–1011中 SF01–05新读，party1/allboxesfull、party6/allfull、party6/freebox正反控制与扣球后异常前缀保持。WP53 savingdelta有新全文/153行producerdiff检查，未声称重验全GR6-S-001真实存档。
6. **independent_adjudication**：同一非作者身份，四ID全部原提案/反证/消费者及R1–R5在旧9d独审已直接完整按资格读；本轮以精确同R/同blob绑定复用其读事实，新增消费者/接口另直接读。未重跑源/作者模型；未把原SUPPORT、候选PASS、字节相同或团队读集当成当前本人新全文。
7. **dependencies_and_receivers**：新 WP53消费者全文加入本轮接合，capacity/receive规则没有丢失或被取消的可保存行为推广改变。局部Ball签名不代签其 Bug Contest、saving所有运行资格或 U13其它ID。

### R6-UI-PARTY-001 — ACTUAL_PASS_SCOPED_STATIC

1. **identity_and_verdict**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。U10唯一/P2 required，摘要Mark合法缺槽ACTION的局部失败边界；原“非空槽清零”不足以定义缺槽，不把覆盖缺口夸成已有强断言。
2. **bidirectional_evidence**：final WP66-A全1–267新读并核182/184；WP18全386沿精确相同 blob旧本人全文复用，UI947–1011中MK01–09新读。新设施 receiver132接合同一UI而不扩Mark入口。
3. **premises_and_counterexample**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。非战斗INFO正常进入Mark、初槽0、六槽图集且至少2变体、无补齐/插件，独立ACTION对缺失值先数值比较失败，原[]保持，隐藏/返回/摘要收尾未到。显式六零为正常无动作，不和缺失槽混同。先编辑其它槽后失败也未提交标记副本。
4. **minimum_revision_contract**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。WP18默认与WP66-A正常/缺槽条款及32向量中的MK01–09共同保留，行为语言没有要求未来复制源结构或永久保持缺陷。再修订0。
5. **acceptance_and_regression**：MK01–09新读保持缺槽独立ACTION失败、六零正常、组合键优先、编辑副本BACK弃稿及OK写回；U01 Owner/U14Happiness旧组合事实复用，未补齐marks[]。R5动态读取/三行确认资格保持。
6. **independent_adjudication**：同一非作者身份，四ID全部原提案/反证/消费者及R1–R5在旧9d独审已直接完整按资格读；本轮以精确同R/同blob绑定复用其读事实，新增消费者/接口另直接读。未重跑源/作者模型；未把原SUPPORT、候选PASS、字节相同或团队读集当成当前本人新全文。
7. **dependencies_and_receivers**：新设施 receiver 132已按WP54/WP55/设施177及完整Partyunit联合新审，本轮有界通过，旧9d PENDING_EXCLUDED仍是旧快照事实。该通过不把设施取消传播为Mark取消，也不签其它U13 IDs。

### R6-UI-PARTY-002 — ACTUAL_PASS_SCOPED_STATIC

1. **identity_and_verdict**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。U10唯一/P2 required，仅最初记录与等级候选重叠的重学排列；不新建全蛋招表/来源法定可达/Demo要求。
2. **bidirectional_evidence**：final WP66-A全新读218/220，WP30旧全文286沿相同 blob复用，UI947–1011中RL01–09新读；设施ordinals与重学Move窗口的顺序消费者分开。
3. **premises_and_counterexample**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。合法非蛋非Shadow基形BULBASAUR L2、当前仅AMNESIA、更多候选开、合法记录编辑、注册/首绘正常。记录[GROWL]仍[TACKLE,GROWL]，不能搬成[GROWL,TACKLE]；记录[CURSE]才前置。重复记录仅诊断夹具，不声称正常记录链生成重复。
4. **minimum_revision_contract**：原同身份七组独审事实复用；最终载荷与9d字节相同，受影响消费者另新审。领域概括与UI概括均收窄为未会且不在等级候选；WP30原精确§6.3保持，新UI RL02补旧A31首项重叠无法区分的顺序。再修订0。
5. **acceptance_and_regression**：RL01–09新读保留overlap[GROWL]不搬移、only[CURSE]前置、重复/已会/配置关闭、取消短确认与教学后统计；A048空候选早失败及C0033/2/来源26、A044双入口原资格精确复用。
6. **independent_adjudication**：同一非作者身份，四ID全部原提案/反证/消费者及R1–R5在旧9d独审已直接完整按资格读；本轮以精确同R/同blob绑定复用其读事实，新增消费者/接口另直接读。未重跑源/作者模型；未把原SUPPORT、候选PASS、字节相同或团队读集当成当前本人新全文。
7. **dependencies_and_receivers**：WP30/U14友好度相邻组合没有变字；新的设施资格/报名写入不能改重学排序或其true/false。F002的nil[]仅属于具名EntryScreen wrapper，不推广到MoveRelearner取消。

## GR6-F-002 的新联合接口七组

1. **identity_and_verdict**：GR6-F-002唯一U13/P2 required，本审只签其WP66-A接收器与WP54资格、设施Q/WS条目、WP55取消/登记接合；本轮具名静态范围ACTUAL_PASS_SCOPED_STATIC。原9d pending不重写。
2. **bidirectional_evidence**：完整scope_contracts/1原七组/原提案/反证直接新读，R Rulesets1–323、Party1051–1139完整unit、Challenge_Data1–100、BattleChallenge具名范围。新实际WP54全156/WP66-A全267/设施全177/WP55全150，新行及首错误与源逆向互查。
3. **premises_and_counterexample**：见joint-static-cases.json 13个明确控制：raw0、explicit1/3、raw−1、Standard−1、setter−1、final首错误、ordinal/newEntry focus、nil/[]包装、range和会话层及旧stale反证。默认UI最大6，七人为工具列表反向；所有资源/规则/无插件前提明确。
4. **minimum_revision_contract**：WP54:19/35–47、WP66-A:132/238、facility:Q31/Q48/Q49/WSW28–30/35–36与WP55:40/48/52–57已共同对齐。必要正文修订0；接收器既有单句在新producer加入后重新全文/联合实审，不以stable免接合。
5. **acceptance_and_regression**：0/1/3不混成通用正数上限；raw负数getter=6而Standard getter=-1、两者finalmax6；focus仅人数等于且刚新增；minimum→maximum→member→team→subset firsterror；nil不setParty并nil返回，[]工具边界写报名且false/活动队伍可清空。UIA26/A27和旧R1 fixed3/仅2可用预检资格保持。
6. **independent_adjudication**：新读9971精确candidate对应411b独审全文74，WP54/QC/WP55/WP53实际与其mirror完整字节相同。生产者PASS是候选入口绑定，实际结论仍来自本文新context审；保留旧3ef全局FAIL/局部F002资格及两份反对stale-command证据，Ruby历史未重跑也不作为宿主证明。
7. **dependencies_and_receivers**：新WP54定义提供最终约束/firsterror，WP66-A提供UI cap/focus/order与包装，WP55提供提交/活动party/取消层，facility为所有控制的可审目录；彼此相容。未签U13其它7IDs、WP56/58、完整保存执行或公共行政registry。

### 正常、反例与组合控制

| 静态控制 | 前提与可观察结果 |
| --- | --- |
| raw 默认0 | min1/max0、A/B合法、无队伍规则：预检可true；Entry不封顶，不自动focus；确认2人先max失败，空确认先min失败。不是最终无上限。 |
| explicit1/3 | setter同时固定min/max；新第一/第三人才focus；再选超限成员被Entry门挡；确认返回原对象按Entry順序。fixed3选2最终min失败。 |
| raw−1 / Standard−1 | raw读取归一化6，sixth新Entry可focus且cap生效；Standard读取原−1，无正cap/该focus。最终max都6；七人仅工具反向，不能声称默认6槽UI可选七人。setter−1另截断1。 |
| first error | 最终min→max→member→team→subset；先命中短路只追加首错。预检eligible并未替代最终资格。 |
| ordinals/focus | No Entry中间项后紧缩FIRST/SECOND；加入第三才focus；Summary或仅count相等不自动确认。 |
| nil取消 / []工具返回 | nil不setParty并nil返回，旧报名不改；[]为truthy，覆盖报名且包装false，活动live party立即[]。正常min≥1空确认失败，不宣称菜单能提交正常空列表。 |
| 1..3范围/不可用 | A26三合法一BANNED选2可成功；A27全不合法、R1 fixed3仅2可用预检nil。范围与固定人数分开。 |
| 会话层 | 普通菜单nil取消不调用session cancel/end。WP55 inner cancel可还原oldParty后reset；inner end先赋oldParty再检查inProgress；outer end才另保存累计/currentChallenge=-1。不能混同。 |

所有正常成员身份、显示、注册、资源、资格规则、默认MAX_PARTY_SIZE=6和无插件/竞争前提，以及各工具边界/受控失败范围，写入joint-static-cases.json。它是人工静态控制记录，13项均 DERIVED_STATIC_NOT_EXECUTED，未执行模型或Ruby。

### 原反证中的矛盾与历史资格

原 generator counterchecks-root-findings.json 的F002完整项（文件42012 bytes / SHA256 `0f8df84ee410cfefeed9b64b4a57e7521d709a8aacf39ff2522c9feff704878e` / blob `3a9934a081e66a1d85d0bcb9c523ae4f58778ac3`）正确指出UI cap只在number>0，但第五静态反例把loop块内command误推为跨迭代残留。完整负证据 countercheck-ui-entry-stale-command.json（2442 bytes / SHA256 `320b742ad5bd6f804610535ee08e8de2747a524799ba2bcf98647feaf2b990c0` / blob `6a2ecc27f138a1471e768d128363d6c6f097d7b5`）与isolated-entry-rejection-counter.json（2919 bytes / SHA256 `3f066179f97e0c2ab3974219c395c982944931035f7dfdaae8bea4b748701e71` / blob `fd828c7d156245c4ec5a50da727e7c1e6b810f19`）保留Ruby2.6.10隔离方法/内存scene的正常成功、重复Species拒绝→BACK、空确认失败控制，Summarycalls=[]，支持撤回该stale推断。

本轮只读其历史载荷并按固定方法块局部生命周期核对，没有重跑历史Ruby或宿主；隔离负证据不证明全部真实UI/宿主版本，也不要求未来保留源结构。首错误失败后保留选择、ret=nil与正常BACK退出相容。

R1–R5准确历史五元组/静态范围/正常反向及局部失败前缀沿旧独读coverage复用：R1初始CONTINUE_WITH_DEFERRED_FINDINGS和v3具名A–G；R2 B16 candidate356b46b/actual29b21fe/review191e669c（A044/A048 B16主责、C003 B21主责/B16局部）；R3 accepted341 records244/245/250及失败前驱；R4 U03actual-v1的17/76不混成B5的16/75；R5精确13fddb closing、12df activation的92 CLOSED/51 P2/41 P3，不重签全部92行为。

本轮final WP66-A全文再次核动态形态227、三行确认244、Mark182/184与Relearn218/220；共享UI836–840沿相同blob旧直接读。设施默认min预检/final首错与多选A26/A27不改变原R1资格；U10新RL02重叠顺序仍保旧C0033/2数量、来源26、A048空候选首绘早失败及A044背包/Party双入口；nil/[]的设施返回不会推广到普通Mark/教学返回。媒体/字体/真实时钟/宿主/save/Demo原未知保留。

## 修订、失败记录与复验边界

必要正文修订0。输入的根receiver依赖文字仍描述生成时的pending；本审不改该输入，而以此最终receipt限定解决当前86bbc的具名联合静态接口。public planning/audit行政同步和其精确字节审由R6-I后续办理；本文不办理正式接受、CLOSED或所有56项的整体签名。全文阅读设施其它向量/新WP55取消条款不等于代签其它U13七个ID。

最初final对象/路径不可解析和工作树input缺失保留为对象未恢复时的失败，不能提前定性规范或路径缺陷；根恢复后读取准确tuple。第一次combined scope/input、locator、diff和最后源段输出截断已分段补足；未捕获首失败UTC不倒补，详见peer-review.json。

本轮有限Git/UTF-8/JSON/diff/receipt工具为本人已知静态读写；源、Ruby、作者脚本、独立完整行为模型、宿主、Demo、真实save执行均0。当前新送达 32 次/19 个载荷，UTC 2026-10-14T16:46:52.548713+00:00 至 2026-10-14T16:57:45.416067+00:00；每载荷模式/完整身份/区间/指针/cwd/argv/exit和读集身份全列新coverage。机器同字节与直接语义、原同身份复用、团队阅读明确分列。

未来WP66-A/WP54/设施目录任一blob改变需准确新tuple和新全文联合核；WP55报名、活动party、cancel/end变更需重验nil/[]与层级；WP53/WP67-A门/接收/结算变更需重验SF；WP18/WP30/Mark/Relearn变更需重验对应正常反例/向量和精确历史资格。未变同blob可复用已读事实，新增组合不能凭文件stable、相同名字或候选PASS继承。

交付：report.md、peer-review.json、joint-static-cases.json、reading-ledger.jsonl、reading-coverage.json、identity-validation.json、producer-delta.diff，以及本人有限reader/formatter；delivery-validation.json记录包身份。旧9d七份已知载荷完整字节未改。
