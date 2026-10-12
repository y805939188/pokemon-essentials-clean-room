# U07 固定实际整合最终独立验收 attempt-01

**整体 PASS；23 必修项、76 条验收标准、7 个消费者 join 和 11 个当前共享文件的必要有限影响均通过，required blockers 0。** 这是固定 P 的独立静态整合验收，满足当前有限实际整合接受条件。唯一登记员可以据此登记 U07 接受并进入最终关闭登记阶段；关闭登记生成的新共享字节仍须冻结，由本 reviewer 延续进行有限影响复核，通过后才可最终完成 CLOSED／主分支合并与安全清理。本报告没有登记接受、写 CLOSED、合并或删除，也没有预签尚未出现的关闭字节。

受审 actual P 为 `8a0b36520b5c9c57dd893d9116cfae8620aea229`，tree `8fca4c1e4dbf051d7749276060623e2480f23992`；派发包 Q 为 `879ea2175b997984e768f687497910ffd0e8cd23`，tree `45ae8e08906244418c3374c72a7bbe54d1e5e92d`。P 父提交是已正式接受 U05 的 AC `c2eb74c7cbcf8a190d5e902d871fbce44904efd6`／tree `7f830a0b27111a76b35a294c0e9a4a1d524a008d`；Q 父提交是 P。发布回执 `d4651be2712fa11376e19bc37d96f30c724bc478` 仅作定位证据，没有用浮动管理 HEAD 代替 P。

本次是父任务派发的新独立 reviewer `/root`；与原作者／唯一登记员分离，只写本目录六个新证据文件。三个可见只读证据助手协助检查标准及有限交界，没有独立签署、作者修订或登记权限，最终判断由本 reviewer 作出。requested `gpt-6.1-sol / ultra / default`（普通速度，非 fast）按可见委派接纳；工具没有实际 model／reasoning／tier 回显，均记 UNVERIFIED。不执行隐藏 CLI 模型任务，不审计额度、凭据或后端。根 AGENTS 及 Q 任务全文已读；执行环境的 `.agents`／`.codex` 无适用本地 skills。

固定 H 为 `d5b6af3ebbabc57ed7fbdc2e1fb2c4736dbf9a65`／tree `c8a523150d75c8d1bede346857263ddd00ef0035`；原交付 D 为 `86b4d7e1d8645e75af91a215240f8786a5bb4ca8`／tree `42c29efb5422772a1d90f657f25983600f500f28`；原正式 S 为 `167296dbe9e2384627b0ed696e87aeb01f211252`／tree `33598d8a2a3acdd093cc4fe23f48eea8666100f3`。参考 R 固定 `Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`／tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，只读。当前新环境没有派发包描述的参考本地目录；此环境差异不改变既有精确来源与有效批次签署，必要消息关闭反例另读取固定 R 的两个文件并核对 blob。本次没有补资源或执行参考。

## 实际输入与复用条件

Q 的任务、输入与权威 patch，P 的全部整合输入和 11 共享文件均完整静态读入；23 canonical 与局部 actual verdict 全文、全部具名前提／场景／未知及 76 标准逐项消费，六份精确 `report.md` 完整审读。36 批次报告产物按固定 commit/tree 与完整 bytes／SHA256／Git blob 独立核对；其余局部 evidence 仅从矩阵准确对象指针复用，没有递归重读候选尝试、raw 或 ACT 历史，也没有重做全局 FINAL-1／FINAL-2。

AC→P 精确差异为 22 路径，正式 131 文件未改。44 个最新修订文件全字节匹配最新已独立 PASS 的 actual，87 个全字节匹配 S；原第三轮 206 文件的完整树／blob保持。唯一权威 patch 在临时 index 从 AC 静态 check／apply 后重建 tree 为 P。身份、JSON、链接和补丁检查用于限定证据，以下判断还依据当前正式条款、案例、消费者及共享状态内容，未以相等 hash 或 counts 代替质量裁决。

复用的是各批明确 source／premises／条款／案例／qualified scope。WP09 采用 U02 已批准后继，WP28 采用 U04 已批准后继；原 U01／U03 whole-file 签名只绑定各自 prior。本报告另外判断 P 的必要承接。旧 PENDING／接受0／18/5 等文字均为不可改写的生成时点；五个公共 prose 的当前追加段和三份 current ledgers准确给出 23/23 接受、6/6 主题接受、最终 CLOSED0、U07 待审。P 的未关闭／待审是正确输入阶段。

## 23 项与 76 标准当前判断

逐条完整具名前提、标准原文、当前路径／条款／案例、准确局部复用 pointer、未知和新裁决见 [per-id-verdicts.json](per-id-verdicts.json) 的 `verdicts23`。

| ID | 标准 | 当前判决与实质证据 |
| --- | ---: | --- |
| GR3-M01-001 | 3 | PASS；WP08/LZ18–22：过滤先于形态/行数、空译奇数拒绝及完整入口先截断；井号/空格/转义反例保持。 |
| GR3-M01-002 | 3 | PASS；WP08/LZ23–25：空0、缺1、有效5合并省域、逐图与前置非空对照，先删和实际数据未知保持。 |
| GR3-M01-003 | 3 | PASS；WP03/04/KL33–35：预处理→schema/q，Alpha结果、引号不保护井号、反写再读不保真。 |
| GR3-M01-004 | 4 | PASS；WP03/04/KR14–16/KL36：后Default覆盖与当前语言显示分层，完整三元联系人/普通道具重复拒绝。 |
| GR3-M02-001 | 3 | PASS；WP05/EP22–27：A正常/B失败/C跳过，步计数已写与外层诊断/失败前缀区别。 |
| GR3-M02-002 | 3 | PASS；当前WP09/SV12–17：两登记取10/20、最后键20、双加载/独立标记/全撤销；U02新投影不改此范围。 |
| GR3-M03-001 | 4 | PASS；WP16/203/CAM01–18：速度/双轴/钳边/包装等待与即时、整数/浮点居中及商店消费者分层。 |
| GR3-M03-002 | 4 | PASS；WP11/14/DQ01–09：驻留前提、临时查询可生成/重播/暂存、非地牢和分阶段失败前缀。 |
| GR3-M03-003 | 4 | PASS；WP13/12/CS01–13：严格Cut Scene与108/408、A→结束→请求启动、[]门及更早系统/末端门分开。 |
| GR3-M03-004 | 5 | PASS；WP11/13/当前WP09/MR01–13：先清记录，实例保留分层；同ID重建、异图through及异常前缀。 |
| GR3-M04-001 | 4 | PASS；WP21/SP01–10：编号30px对照、形状/RGB/2×2/重叠自足；PNG分帧与原生内部未知保持。 |
| GR3-M05-001 | 2 | PASS；WP18/24/SZ：203/209/210mm、完整15段/两整数阶段、原始IV/PID输入、未证caller保持。 |
| GR3-M05-002 | 2 | PASS；最新WP28/IF01–11：当前图轴7/5、A/名称、Manhattan/枚举平局、三路先统计与不拾取。 |
| GR3-M06-001 | 3 | PASS；WP30/最新WP28:216/EX01–05：钳制差量、先提示后写、同级增减与糖果入口友好分层。 |
| GR3-M07-001 | 4 | PASS；WP28/40/42/RF01–06：留消费身份、同轮终局2/下轮1/正式失能1，容量失败与未知外层。 |
| GR3-M08-001 | 3 | PASS；WP47-A/46/50/NG/MH/HI：首击至71与持久前缀；续击空身份失败早于get，101/单击对照。 |
| GR3-M10-001 | 3 | PASS；WP66-A/B/MV01–03：同来源同索引BoxLink取回后旧快照仍交B；BACK与未嵌套总量对照。 |
| GR3-M10-002 | 3 | PASS；WP66-C/QN01–04：共享与商店同轮优先级0/1及1/11，单键/边界仍消费轮；非物理输入证明。 |
| GR3-M10-003 | 3 | PASS；WP67-A/WP17/TX01–04：busy仅恢复、暂停仅解除、全显才返回；普通全显关闭无额外恢复调用。 |
| GR3-M10-004 | 3 | PASS；WP67-A/K40/AR01–02/PA-P28：首次3、正常补位4/5连判且不重播开场，旧B028限定保持。 |
| GR3-M11-001 | 4 | PASS；WP62/66-B/HAB：1/5格、缺尾不补、同格可见并集，与WP63首条/游标及PD16旧缺陷分开。 |
| GR3-M12-001 | 3 | PASS；WP75/CV-M30：两246B/8×8固定BMP可得，Graphics底图/浏览器/宿主/工具/Demo仍未证。 |
| GR3-M12-002 | 3 | PASS；WP76/GN-M14/M20：C70+12=82、238+12=250的前支资格、空历史0及非事务失败限定。 |

## 跨批承接与有限交界

| Join | 当前结论及消费者边界 |
| --- | --- |
| DEP-01 | PASS；P WP09 §3.1.1 retains U01 same-ID save last-value/two-load/all-unregister contract (10/20→20), while §4 load projection separately clears event records then invokes conditional restoration. Latest U02 successor independently covers inherited U01 scope; both precise approvals remain immutable. |
| DEP-02 | PASS；Latest U04 WP28 keeps U03 EXP prompt-before-write and bag/source identity contracts. §3.5.1 adds failure refund with retained consumption identity, normal terminal second refund, next-command and faint contrasts; the added branch does not rewrite other item consumption or EXP callers. |
| DEP-03 | PASS；WP66-A §4.4.1 keeps original source object and cached held-item identity through Box Link, then consumes the current empty target after nested take. P retains U03 capacity/source/partial-write premises and qualified C125 stale-index cancellation contrast; no stable-identity fix or global conservation inference. |
| DEP-04 | PASS；WP67-A §5.3.1 consumes exact WP28/WP40/WP42 refund result; §9.1 keeps busy/nonpaused resume, explicit pause and full-text states distinct. §9.2 keeps NaturalGift committed first-hit prefix separate from AI prediction; §10 retains Arena first presentation and continuing 3/4/5 judgment. PA-P28 is unchanged. |
| DEP-05 | PASS；U02 camera/script waits and nonresident map side effects remain their exact consumer contracts. U05 WP62 §5.3.1 consumes encounter/map metadata as character-filtered masks intersected with visible Point union; WP63 still uses only length for cursor and first same-cell record for queries. These joins do not establish real maps, host clocks or rendered visibility. |
| DEP-06 | PASS；WP76 §7.4a preserves settled C+n and empty-history increment 0; WP67-A Arena history is count/mind/skill/HP presentation with continued 3/4/5 judgment. These are separate histories and thresholds. The U06 result is not reused as an Arena reset rule or Demo execution. |
| DEP-07 | PASS；U01 synchronous callback/committed-prefix contract remains exact to notification consumers; quantity selector/shop same-frame USE+BACK and RIGHT+USE use separate priorities, while WP67-A list busy input only resumes and returns after full display. No claim covers all UI handlers or actual host sampling. |

WP09 U02 后继只改导航与普通恢复投影；U01重复登记、默认17项类型/缺键/加载门和旧目录全文保持。普通加载先清记录与直接能力输入下的条件异图through不混用。WP28 U04 后继仅改执行退款／残留终局／容量，U03探测仪与EXP顺序保留；U05列表与反应文本只承接实际提交前缀，不保证UI恢复或改战斗/AI结果。K40明确是当前Arena行，busy/pause/full另由TX三态证明；两个判点分别检查。普通全显关闭路径没有额外恢复调用。C109保留为旧过宽叙述限定，当前WP63/P34无位置→0事实未改，不另开修复。PA-P28/WP56/WP17/WP63及既有AI职责与邻接前提保持。

54既有交界、8既有链及18新增链均有独立当前有限结果：分别见 `existing_junctions54`／`existing_chains8`／`new_chains18`。每行保留原对象、具名前提/正常/失败/unknown或准确对象身份指针，并区分原资格复用与当前必要影响检查。未涉及字节和前提的行只qualified reuse；涉及修订的行另核当前消费者。原历史“缺/仍写”等缺陷语句保持为冻结输入，其当前解决情况在新字段判断；本报告没有把历史状态改名为整个能力PASS。

## 11 个当前共享身份

每项的P完整bytes／SHA256／Git blob和必要影响见 `shared11_current_verdicts`；旧整文件签名未覆盖这些新字节。

| P路径 | 当前有限影响 |
| --- | --- |
| `README.md` | PASS；新增权威当前入口准确区分旧S交付与第三轮P候选；23接受/6主题/最终0、Q外部身份、optional/NO_REQUIRED和0运行限定一致。旧全文仅按固定历史范围保留。 |
| `review/remediation-third-20261012-prepare/README.md` | PASS；初始接受0等旧生成快照通过当前追加段明确限定；当前分母23、U07为整合非新增修复批、U08未启动、同一组精确入口可解析。 |
| `review/remediation-third-20261012-prepare/registration/README.md` | PASS；旧U01待审/交接未释放语句限定为生成时点；当前段指向六已接受实际与当前approval/traceability/junction，未提前登记U07或CLOSED。 |
| `planning/feature-matrix.md` | PASS；完整AC前缀保持，六批最新来源/Feature投影未改；新增当前状态解释U05旧18/5等历史段，不削弱通知失败/保存/PNG/native/尺寸无caller/退款/输入/生成累计或资源宿主未知。 |
| `audit/source-traceability.md` | PASS；完整AC追溯前缀保持；新当前状态与6批实际报告/23canonical来源定位一致，旧来源PENDING限定为当时，不改固定R或原unknown/资源边界。 |
| `review/remediation-third-20261012-prepare/registration/finding-ledger.json` | PASS；23条既有接受记录全对象在AC→P不变，精确actual/report/receipt与catalog全相等；仅增加P外部binding与U07冻结阶段，final0，不重写canonical25或原229/341。 |
| `review/remediation-third-20261012-prepare/registration/batch-ledger.json` | PASS；补U01/U03固定actual PASS和U06准确actual/report/receipt，六批与catalog相等；23/6正式接受、U07待有限影响、最终0及WP09/U02、WP28/U04、U03/U04→U05门保持。旧局部签名未移转新公共字节。 |
| `review/remediation-third-20261012-prepare/registration/current-status.json` | PASS；六actual与U02/U04/U05 report/receipt定位准确；23/6接受、U07_complete=false、独立PENDING/CLOSED0不互相混淆；新增三后继入口全可解析。 |
| `review/remediation-third-20261012-prepare/registration/approval-ledger.json` | PASS；新6条已接受精确actual/tree/独立report/receipt与完整catalog一致；候选自检/独立局部PASS/正式接受/最终CLOSED分层，U07仍待审未接受，optional及NO_REQUIRED口径不扩大。 |
| `review/remediation-third-20261012-prepare/registration/traceability-successor.json` | PASS；新23条canonical/准确source-successor对象hash/本批actual/report/标准矩阵与当前正式身份入口逐项一致；局部旧line hints按原actual保留，当前条款/案例另于本报告绑定P。WP28经验糖果旧204在P为216，标题/正文唯一可定位，不造成缺证。 |
| `review/remediation-third-20261012-prepare/registration/junction-successor.json` | PASS；54既有/8链/18新链完整冻结前提/失败/unknown保留；当前载体按P复核，逐行有界join见本报告，历史缺陷状态不改名为完整能力PASS，未扩大M09或NO_REQUIRED为必修。 |

五prose保留AC完整精确前缀，全部40新增必要链接可在P解析或显式指向Q的外部actual identity binding。新approval六actual/report/receipt与catalog无错配，traceability23与canonical／source-successor／matrix准确相等；三旧ledger只有限阶段/定位更新，23旧finding接受对象保持。WP28经验糖果旧U03行204已移至当前P216，正式条款名称唯一可定位；矩阵某些空case导航由本报告明确SP/SZ/IF/EX/CV/GN案例补齐。此为当前定位归一化，不重开已成立的事实或要求重复行政证明。

## 原范围与结束门

229原CLOSED完整qualification对象与341 exact batch/ID/candidate/actual/report tuples按固定H原对象保留；仅消费六批已签的78投影／73唯一相关控制。每个投影保持原qualification／贡献身份及当前有限影响，见 `qualified_regression`。A022/A059的过宽历史support文字继续按IHC003/004排除；G2-5/G6-5按IHC001/002排除，其他历史纠正保持。未重签同ID其它owner、全能力、全部历史或运行。25保留=23 REQUIRED_REVISION＋GR3-M09-001 OPTIONAL暂缓＋GR3-M02-003 NO_REQUIRED_REVISION；无P1、不启动U08，新增链中的optional/无必修成员只消费既有事实。

这是供未来独立实现的逻辑行为规格验收。未实现TypeScript引擎、API、战斗或适配器，未翻译Ruby或复制源码。有限静态范围不能宣称完整引擎验证：未重新全读全PBS/备份语料、插件组合、全部注册项/地图事件或完整资源包。原缺Audio／Graphics／Plugins／Game.ini／Game.rxproj／地图、区域底图、工程/宿主及真实默认启用/caller／可达性限定保持；可得BMP、形状规则和输入hash不证明渲染、像素、动画、音频或Demo。逐IDunknown全文保持，包括真实采样/帧时序、异常诊断/后继恢复、回滚/检查点、动态消费者和未来兼容政策。

所有行为案例、参考Ruby/游戏、行为模型/模拟、编译/转换、游戏格式反序列化、真实Demo、宿主输入/渲染/音频、浏览器/像素/动画执行全部 **0 / NOT_EXECUTED**。仅Git／JSON／完整字节／链接／静态文本审读。不存在新增必修blocker；[findings.json](findings.json) 为0集合，完整身份与读取/复用范围见 [input-snapshot.json](input-snapshot.json)。

当前PASS允许唯一登记员验证本报告身份后登记U07实际整合接受并准备关闭候选。本report的 `formal_acceptance:false`、`CLOSED_written:false` 是reviewer角色边界；P输入最终CLOSED0不是缺陷。后续关闭字节需精确冻结并由本reviewer有限影响复核，本次不提前签未知hash。报告仅新增本目录六文件；普通提交、推送与六件完整远端读回的最终commit/tree由外部交付绑定，[output-identities.json](output-identities.json) 只列其余五文件，避免自hash循环。
