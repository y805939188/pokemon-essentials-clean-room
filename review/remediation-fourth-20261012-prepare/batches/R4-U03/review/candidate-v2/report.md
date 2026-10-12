# R4-U03 candidate-v2 有限独立复验

裁决：**PASS_SCOPED_CANDIDATE_V2**。GR4-M11-001标准6的唯一候选退回点已满足；逐项候选结论7 PASS、0 REQUIRES_CHANGES。30条标准的证据来源是本次新作1条静态复验、固定v1报告限定复用29条，并非重做全局审查或重新运行历史。

候选 `d7875398e130b5bfa621c55d6c016ee0f8965cf7` / tree `8c763de4279e5140e64cd0a9fe58a820ea2cb92b`；发布证据 `165b01ce06ff88e5c5f50df7a11d017417ed1213` / tree `8938c8ff5578fcbb3bd1d5f7a456ab569810fbae`。固定任务包仍为 `08a57fb55118914a74ac1ffaf617647c01df8938`，R仍为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。原独立报告绑定 `0bdfd26ef95ced597db5d924a69d0e35de9a188b` / tree `fe5a7240c5fee213583a85857977cd8b37642708`；原候选58cd8b1上的REQUIRES_CHANGES报告保持不可变。

| finding | 本候选裁决 | 证据模式 |
| --- | --- | --- |
| GR4-M04-001 | PASS | 原5标准限定证据复用，正式/源规则未变 |
| GR4-M06-001 | PASS | 原4标准限定证据复用，正式/源规则未变 |
| GR4-M10-001 | PASS | 原5标准限定证据复用，输入裁决及其向量未变 |
| GR4-M10-002 | PASS | 原3标准限定证据复用，皮肤合同及其向量未变 |
| GR4-M10-003 | PASS | 原4标准限定证据复用，排版合同及其向量未变 |
| GR4-M10-004 | PASS | 原3标准限定证据复用，108格和回退合同及其向量未变 |
| GR4-M11-001 | PASS | 原标准1–5限定证据复用；标准6本次独立源行为/前提复验 |

原29条具体依据继续绑定原commit/path/pointer；详见 [criteria-results.json](criteria-results.json) 与 [findings.json](findings.json)。本次没有扩大既有6项、旧23/229/341或依赖的签名范围。

## 标准6修复与必要边界

正式仅改两目录的两个输入单元格：图鉴目录R4-PD05第220行、UI目录R4-DX05第785行。现在两行都规定默认合法RATTATA、显示全部形态关闭、基础雄性0与具名且展示自身的Alolan雄性1均已见（可仅异色），初始[性别0,形态1]确在可列列表且可列项>1。原预期、普通刷新/单项对照与NOT_EXECUTED列保持原字节。这正是R4-U03-REVIEW-001所需的最小前提修复。

正向夹具在物种、metrics、地区、玩家、条目资格、前序界面和条件资源依赖正常、无插件、此前无形态浏览写入、首轮仅BACK且其余查询假的完整范围内，具名Alolan先检查已见雄档并列入male1；初始记录[0,1,true]匹配该项。首轮在BACK之前三参写末次，异色默认false；退出不回滚，得到 **[0,1,false]**。雌档也已见不改变雄先及具名形态只列首个合格性别的结果，不要求列表恰有两项。

原独立反向仍成立：另设基础male0已见、Alolan1仅female已见、maleAlolan1未见，合法独立最近见到写入末次[0,1,true]而不登记seen表。列表仍多项，但末次male1不匹配，首轮选排序首项male0并写 **[0,0,false]**，BACK不恢复。此状态现在不满足新向量的male1已见/匹配前提，不能再否定该正向预期；原WP62性别筛选/首项、WP66-B首轮、PD31/PD34/B38正确反向合同保留。

选择器外普通预览/Info/Forms刷新仍只消费末次性别/形态、固定普通外观，保存true/false各保持。独立单项BULBASAUR只有1可列项，Forms入口不调用选择器，无该首轮写入，保持[0,0,true]。这些均为SOURCE_STATIC/SPEC_STATIC/DERIVED_VECTOR，未观察真实窗口或像素，也没有写任何真实记录。

本次实际回读固定R Entry139–199、446–478、506–511，Pokedex61–69、129–139、195–227及Settings/PBS必要前提。新独立辅助审者和根审者均读源/新两行/旧反向，不以作者自评代签。详细四组前提、推导、精确行和read-ledger见 [criterion6.json](subreviews/criterion6.json) 及 [read-ledger.json](read-ledger.json)。

## 身份、复用与执行限制

候选仅2正式文件+2/-2、只输入前提变更；2文件其他行、其余129正式文件及10批准文件完整字节保持。全131正式文件的候选/证据/工作树完整bytes相等。v2全部46镜像中只有PD05/DX05两个full_row字段变化，另44完整对象原样；发布后继只增加回执。独立完整增量核验见 [identity-delta.json](subreviews/identity-delta.json)，不是全131语义复审。

旧SPINDA、动态孵化、IV、同轮数量/命名/文本、图鉴资格/栖息地和A053/B08精确qualified历史，按原独立报告的原scope复用。此次必要回归只检查性别/匹配/首项、普通刷新、单项门与受影响旧行完整字节，没有重算或补签全部旧23/229/341。

**本次新增参考函数、行为模型、宿主或Demo执行均0，NOT_EXECUTED_THIS_UPDATE。** 第四review历史4次(M01一次、M02两次、M12一次)归属和异常限制仍独立保留，未重跑，原author/execution.json完整bytes不变。Git/JSON/增量/镜像/报告发布读回是TOOL_VALIDATION，不能计成新行为执行或UI通过。真实字体/物理输入、媒体/像素/动画、地图/完整Demo和外部插件未证，未来兼容政策未代选。

## 审者与发布

根审者真实task `/root`、thread `01a130de-2480-707d-a4fe-c7056c71c02e`；辅助criterion6与身份审者为各具名子审记录的原真实thread，独立于作者。请求sol/ultra/default/Fast=false、普通速度；实际配置回显UNVERIFIED。

只在 `review/r4-u03-independent-v2-20261012` 分支新增自身 `review/candidate-v2/` 材料，普通推送并从独立对象库fresh fetch核完整commit/tree/blob/报告工作字节及12批准正式字节。发布后继 [publication.json](publication.json) 绑定已冻结报告的完整读回；最终回执头自身身份再读回后由交接给出，避免自嵌hash。

**候选范围无剩余必修阻塞。** 这是有限候选PASS；实际整合commit/tree尚未审，ACTUAL_PASS/ACCEPTED_SCOPED/CLOSED未登记，没有提前关闭任何依赖或公共台账。
