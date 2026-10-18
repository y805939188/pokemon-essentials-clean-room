# R8 七行来源摘要恢复候选独立复核

**分类修正 PASS；最终累计来源校准 PASS；总体 PASS。固定候选可交协调方进行最终整合冻结与验收。**

受审候选为 `7ed3e0554ac24339a7e61cab152f628037111644`，精确单亲为 `c0f62d973180679134f2eb1a488c1dc359c8658f`。本次对固定旧报告的两项P3、七个case完成有界独立复核，七项均PASS，无新增同scope问题、无本复核范围内剩余阻塞。此结论不表示全轮已发布、已merge、CLOSED或目标实现验收完成；这些动作仍由协调方负责。

本报告仅在新的独占review目录产出。未修改作者清单、正式规格、参考仓库、旧FAIL报告或main来取得PASS。三路分工构成这一份独立审查，未重复计接受票。判定同时依据固定源正文、完整变源差异、职责/依赖用途与边界反例；结构检查通过和数据相等各自只承担对应证据作用。

## 固定输入和完整身份

| 输入 | 固定身份 |
| --- | --- |
| 本次候选 / 作者恢复分支 | `7ed3e0554ac24339a7e61cab152f628037111644` / `codex/r8-r3-seven-line-recovery-20261017` |
| 精确父候选 | `c0f62d973180679134f2eb1a488c1dc359c8658f` |
| 完整先前独立复核 | `34202eb7accfee48bb8761db88b340bd77f54a42`，`review/r8-disposition-r3-independent-c0f62d9-20261017/` |
| 实际累计接受源 | `5f87743293290de2e219ecdd6c19e88280f60c9a` |
| 累计包 | `8336249c78b4698cd77445653d3b05ff6a76ce94` |
| 历史B8 / R8交付 | `fd1df570cad987dc3852a3b958f03916e317f7fe` / `4575e80d041ab0c74a42e2e36399d05791dbaa5b` |
| 本次manifest SHA256 | `c6b2d3ea0346c82f4aa224b67a176c21901b50efc337df25af7aa26e0242e3ea` |
| 累计补丁 SHA256 | `6351505a314c88b1bed3aab98c6808639b319461e25f796ded87221225e0418b` |

候选完整打标目录独立枚举为175文件、**38,564,194字节**；174个非自身条目与候选身份表的bytes/SHA256/Git blob/适用行数逐项一致，身份表自身由固定提交绑定。相对c0实际41个变化路径，等于38个声明payload加3个明确自身/交叉身份排除项，无删除；实际16新增、25修改，排除身份后15新增、23修改，全部位于打标目录。见[evidence/candidate-identities.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/evidence/candidate-identities.json)及[evidence/candidate-delta-identities.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/evidence/candidate-delta-identities.json)。

本审查另从全新bare对象库、不使用本地alternates获取精确7ed提交，175文件全部逐字节、模式、blob、bytes和SHA256回读一致，见[evidence/candidate-fresh-remote-readback.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/evidence/candidate-fresh-remote-readback.json)。作者声称的回读未直接转授为本审查PASS。

先前报告全部111文件、52,119,792字节也按342提交逐项绑定，含110条输出身份表及其自身；原findings、七条FAIL证据、领域报告、逐736/721/33/44结果和131/2704阅读/覆盖账均保持固定历史。R1/R2及接受回执的所有原固定SHA继续经该完整历史证据链绑定，未重写为当时PASS。见[evidence/prior111-input-identities.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/evidence/prior111-input-identities.json)。

候选正式树仍为B8 `f292698cdd4a8e725525a9be6dc34b75faaf151e`；实际current5f正式树为 `93dc967b4cdb653359afc123d3b8b318d6475fdd`。本轮current有效正文从5f Git对象读取，未将工作区B8当成current。根AGENTS、指定clean-document-revision文本及复核提示词已读；该技能明确排除评审/审计报告，本审查未据其要求修改正式文档或增加批准门。

父委派请求及admission的ultra/default可追溯；实际runtime/model/effort/tier/speed/Fast/云UUID无权威echo，逐字段保持UNVERIFIED。作者README中的配置字样和工具广告不替代父委派，也不证明实际配置；此项不构成FAIL理由。

## 两项根因、七项逐案裁定

以下指针均相对本候选`routing-manifest.json`，全部current正文固定于5f。

| 根因 / 行 | 精确指针 | 完整有效源及判定 |
| --- | --- | --- |
| R3-SOURCE-ATTRIBUTION-001 / 173 | `/features/161/differences/1` | **PASS**。WP26 §5 L122–142、直接变更L138为记录战斗收服存储空操作；回放另按WP58 §6.2–6.4分层。新摘要已消除Gift命名错配，未扩成回放隔离。 |
| 同根 / 227 | `/features/215/differences/1` | **PASS**。WP36 §4 L115–161、变更L132为接受负概率前缀、负累加器及除200向下取整、不钳零。WP36原Repel规则保持，未拿它代替本次差分。 |
| 同根 / 596 | `/features/566/differences/1` | **PASS**。WP61 §3有效范围L22–26、37–40、42–44、46–49、51–54、56–57；L56补默认首非蛋（含濒死）/替代首可战。计步、遭遇允许及MZ选择消费者分责保持。 |
| R3-EV-BOUNDARY-001 / 29 | `/features/28/differences/1` | **PASS**。WP42 §4 L59–96、尤其L65/69/73：普通非Shadow达到该路径时，HP255单项余量−3先失败，早于总量夹限、本接收者EV/经验及后续刷新。更早设施门、此前受领者/回调前缀分开。 |
| 同根 / 32 | `/features/31/differences/1` | **PASS**。WP42 §7 L203–250、直接变化L207为正常核心返回、外层善后和结束通知后，复位行走动画状态及转向预锁记录。新摘要正确归属本单元，不写成EV摘要或面向方向写入。 |
| 同根 / 204 | `/features/192/differences/1` | **PASS**。WP30 §4 L79–126、L122把HP255/ATK255总510与单项252分开；首HP夹限失败未达总量夹限、本接收者写入和后续重算。普通非Shadow、设施早退、此前前缀各自保留。 |
| 同根 / 456 | `/features/433/differences/1` | **PASS**。WP19 §5 L126–181及223–234，L174/L178明确正常模板255/255/其余0、总510满足总量上限但超单项252；重算保留存储值，普通非Shadow增量路径先在HP失败。 |

独立区分依据没有执行业务向量：255＋255＝510不超总量；单项252−255＝−3先非法。相反HP/ATK/DEF/SPA/SPD各100、SPE20总520，各单项均合法，首先HP单项余量152合法，随后总量余量−10才失败。因此总量越额不能推出首单项门失败。默认非内部设施在更早成长门返回；接收者未写也不保证此前接收者或回调统一回滚，Shadow、道具、净化另有合同。

记录战斗存储空操作不证明回放隔离：固定WP58保留队伍/训练家副本、实时背包等依赖，以及正常结束与中止不同路径。floor(−1/200)＝−1区别于截断或钳零。活动Repel下首非蛋濒死L50、下一健康L10、野生L20，默认与替代配置选择不同成员，比较结果不同；概率取整不能替代该规则。FR244真实Gift命名、WP36原Repel条款及FR762排除子范围均保持。

各case的完整固定源身份、反例、侧证据精确指针及依赖非影响理由见[agents/attribution-results.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/agents/attribution-results.json)和[agents/ev-results.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/agents/ev-results.json)；语义报告分别为[attribution-report](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/agents/attribution-report.md)、[ev-report](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/agents/ev-report.md)。

## 必要传播与完整重建

主清单递归差分精确为上述七个`differences/1`字符串叶；其余所有值不变。全部736行source/current/upstream、stableID、有效范围、职责、类别/伙伴、依赖、阶段、实现及验收对象完整保持。729行完整对象逐字段等于c0，七行剥除该说明后也完全相等。未新增功能/排除项、未扩大设计、未把未知原型当作来源事实。

七条单元`feature-source-deltas`和六条文件`source-file-reassessment`仅修相应事实/未来边界；WP42文件摘要同时包含成长与战后变化，而FR29/FR32的生成输入使用独立unit override，避免再次把文件级摘要误当具体单元差分。生成器相应六组manual事实/边界与实际侧证据一致，历史固定35175输入保护原字节保留，未强行重跑历史writer。

统一补丁仅七个after说明变化，所有before和原归档保持。真实接受后归档解压SHA256为`35175c7094b008e77af35cf6a7811c5fcd6f1a0dd20020b64d32b40d5670256e`；独立按全部78行、162字段的before/after重放，**完整对象及最终序列化字节**均等于当前manifest。原应用回执、原来源摘要纠正回执及58份R1/R2作者历史文件完全保留。见[agents/propagation-reconstruction.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/agents/propagation-reconstruction.json)。

facet-inheritance和feature-resolution只给七行增加作者修复待独立复核信息，保留收到的旧校准FAIL及其余四facet PASS。本报告的新PASS写在独立结果中，未改作者记录或原FAIL历史。三个受影响视图精确为旧行替换七处说明；全部736行/33metadata、36父/39子/39边的导航、职责及状态投影另外完整核验。11个可生成物从干净候选重放后字节一致。

原c0生成器中三个与最终侧证据不同的WP13/WP14历史manual值在本候选未变，来自既有后继摘要纠正；它们不是本轮六组同步项。传播分工保留过宽探索断言及收窄到本合同的记录，没有改候选或伪装为新缺陷。完整路径/JSON指针差异、保全和传播结果见[agents/propagation-report.md](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/agents/propagation-report.md)。

## 全覆盖继承和最终累计口径

本轮新读七个完整有效单元、六文件完整B8→5f差异及必要消费者；同时完整核对全部变更路径与派生传播。没有声称再次全文阅读131篇。旧完整阅读及语义信用仅对固定源/范围/职责/依赖用途不变且不受本次修正影响的部分保留，逐条身份与非影响依据可追溯；数据相同本身不证明行为覆盖或依赖合理。

七条新摘要描述的是已经接受、已经审查的5f规则，没有新源正文、输入生产者、状态写入、消费边、职责或范围。语义分工重新阅读回放、Shadow、背包/持物、PP、成长UI、计步/遭遇和排除子范围，确认消费者真实用途不因说明纠正改变。其余729行在同一源与同一依赖图上完整不变；因此原五facet信用可限界保留。七行的原四facet信用保留，校准facet由本次源语义复核新判PASS。

| 覆核对象 | PASS | FAIL |
| --- | ---: | ---: |
| 两根修复 / 七case | 2 / 7 | 0 |
| 当前736 active，五facet各自 | 736 | 0 |
| 原721 ID（含33完整退役） | 721 | 0 |
| 33 metadata及退役/替换处置 | 33 | 0 |
| R2七问题 / R1十二残留 | 7 / 12 | 0 |
| 44原组具体case、分类依赖及扩大当前scope | 各44 | 0 |
| R2失败28行 / R2通过708行传播 | 28 / 708 | 0 |

COMBAT-05与POK-S05原case及分类/依赖原先已PASS；扩大当前scope中的29和596说明现已通过，故这两个扩大scope组本次均PASS。没有回写R2/R3当时FAIL，也没有以一个组通过隐含接受无关目标行为。逐行结果见[feature-results.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/feature-results.json)，逐组见[finding-results.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/finding-results.json)，两根七case见[issue-results.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/issue-results.json)。

正式集合重算仍为131文档、87WP、历史2683/当前2704标题（＋21）、736活跃/33退役/33metadata。当前131身份、全部2704标题及21新增映射从固定Git重算；历史覆盖字节、元数据与退役体/替换引用不变。逐131阅读继承和逐2704章节结果分别见[reading-coverage.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/reading-coverage.json)、[section-results.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/section-results.json)。标题的title-only hash与原Markdown标题行hash按各自声明核对。

九接受事件、40目标贡献、39事项（29 required＋10 optional）及230行绑定均逐项保全；230全部回填，pending0、partial0，原绑定义务不丢失，CLOSED0。接受registry、源身份、current覆盖和回执对象均未变。原R2七项工具/依赖修复、六职责精化、58历史文件及此前真实失败I/O保持原样；本轮没有借七说明替换来源接受或修复历史。

原始183行绑定亦另从d62逐项追踪：175行原绑定身份字段完全相同，UI65八行在保留原批次/required IDs的基础上增加U04义务；180个原active行当前已绑定，另398/407/704三个完整退役体的旧“待整改后核对”标签原样保留，其对应当前文档均已ACCEPTED绑定。故230个当前active零pending没有偷偷改写完整退役历史。见[evidence/original183-bindings.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/evidence/original183-bindings.json)。

## 实际静态执行及发布保护

独立干净shared clone逐字节使用本候选输入，实际重放原`run-author-checks.py --phase cumulative-source`十命令，全部exit0、17登记输入hash稳定且等于候选。27结构负例、9自检、2导航负例、11生成一致、19保全、5接受绑定负例、2704覆盖及4负例、4来源门夹具均通过；另实际调用原`check-repair.py`的12项及`final-calibration-proof.py`的15项，全部通过。真实argv/stdout/stderr/exit/UTC和前后hash保存在[evidence/tool-replay-io.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/evidence/tool-replay-io.json)、[evidence/replay-actual-command-io.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/evidence/replay-actual-command-io.json)，摘要见[evidence/tool-replay-summary.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/evidence/tool-replay-summary.json)。

未运行作者`run-repair-checks.py`封装来冒领其中硬编码的历史缺jsonschema环境观察；该观察保留为作者历史声明。本环境真实调用另行留证，未发生该准备失败。干净fixture使独立review输出不污染作者untracked保全器，未弱化候选检查。根身份/保护审计838检查通过；语义判断不由作者FACTS常量、验证器或这些通过数量自动产生。

所有执行限静态Markdown/JSON/Python/Git，Ruby、参考游戏、业务向量、宿主、Showdown/框架及四原型执行均0。格式检查原样保留Git diff空白上下文和编号空源行的冒号空格前缀；编号源行逐条与固定Git验证，不为消除提示修改证据。报告、JSON和代码检查另行通过，见[evidence/output-validation.json](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1baee5d7346592478b72d8983b0109e1b2a5e2d9/review/r8-r3-seven-line-independent-7ed3e05-20261017/evidence/output-validation.json)。

main仍为fd1，原任务分支仍为c0，作者恢复分支仍为7ed；候选与正式/参考保护路径diff为空，参考HEAD `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`且clean。独立分支仅提交本review目录，不force、不merge。精确输出bytes/SHA256由`output-file-manifest.json`绑定；首个报告提交的全新远端逐文件回读保存为`publication-proof.json`，最终带证明提交再全新回读并在交接给出完整SHA，避免自证未来自身hash。

所有736去向仍待验证、阶段待定/未批准、未实现/未验收；框架307、Showdown74、双方协作130、MZ225、排除0。捕获、背包战斗道具、逃跑和战中成长继续按已核协作边界保留。合理粗标已通过本次来源校准；固定目标版本、四原型、用户范围/阶段决定、目标兼容及整轮发布/CLOSED仍独立待办。协调方可据本固定候选及独立结果进行最终整合冻结。
