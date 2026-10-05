# R-B04：B08 actual 两组受影响接口复审

结论 **PASS_SCOPED**。独立核对 actual `49c21538e72b7a5873972cd00fcae1ee390cce64`（tree `6312cddce2e2a43841bde5ec19d0bb480c284314`），本轮两组接口未发现新增缺陷，无修复项。结论覆盖孵化动态形态／媒体／消息及大会伙伴单／双敌包装交界；完整 R-B08、受影响 R-B07 的 actual 判断及父任务 C 仍分别办理。B04 的35贡献／23主责历史接受不扩展，规范 ID 不关闭。

## 精确版本与证据

接受前驱 `759eee80ce7856570fde2de12d5dcf98ce7e6017`，候选 `0f35a393d9de467cd5f7e695b6072687bb582186`。三份候选报告分别为 R-B08 `239a29c466d6efc1a5a240f57ad53b55c91f9e42`、受影响 R-B07 `7fd9271bc77b534e0eba5b47c77034e2453dd560`、本审者有界 R-B04 `ceb6c07340c8f4f2b7c508df36b2a2ef98f12711`；它们都固定在候选，不作为本 actual 的替代判断。

actual 唯一父是 public payload `e91c974c5a05a55da8d6cb228afe5b30174fb02c`；payload 父 `7d1463f088201a3efad56dadee9a86bb0a923934`。三次普通 merge 依次 `d68eece866631713fe205345be3d93f1e48cbfa9`、`3a1852d08f854122e4ff36e0a9b810aa331004d2`、`7d1463f088201a3efad56dadee9a86bb0a923934`，精确双父在 [独立身份审计](independent-input-validation.json)。无冲突处置或正式字节改写。

报告分支 `remediation/20261003-prepare/review-B08-affected-B04-integration-1` 从 exact actual 建立，只新增本目录。报告 SHA 在普通提交／push 后由远端回读完整交付；报告 HEAD 与被审 actual 是两个版本，文件不虚构自引用 SHA。

完整前驱→actual 共131路径：12正式修改＋45作者新增＋51候选报告新增＋10公共修改＋13集成新增；候选→actual 共74路径：51报告新增＋10公共修改＋13集成新增。13集成文件为10管理 payload＋末尾3冻结证据，完整差异没有漏掉后3件。108来源＝12正式＋45作者＋51报告，逐件原字节保持。12正式＝8最终正文／测试目录＋4精确授权原稿。

| 独立完整差异（无过滤，gzip无损存档） | 原始字节／SHA-256 |
| --- | --- |
| [前驱→actual](complete-predecessor-to-actual.diff.gz) | 44855413／544c57a5207b67274b5ee6dcae6b0e8e36391df0eaa436da6a07e95f678dba60 |
| [候选→actual](complete-candidate-to-actual.diff.gz) | 42725496／9ff58534d9bbf7f16ceecf0a0343bcd9d6fde9e64539dc4683a1b675412e914a |

压缩仅存储报告自身差异字节，解压后与 independently regenerated Git diff 完全一致；不转换参考。参数／完整路径清单在 [diff-identities.json](diff-identities.json)。另附 [全部12输出差异](all12-predecessor-to-actual.diff) 和 [10公共差异](public10-predecessor-to-actual.diff)。A-REG 原存两 patch 止于 payload，已独立重生成核对；本轮实际证据覆盖最终 actual。全差异按路径／Git字节／JSON控制审核，业务正文语义复读限定两组调用，不声称审核其它 B08 域。

## 独立方法与有效控制

读取根 AGENTS.md 和有效项目／固定批次规范；报告目录祖先无附加 AGENTS.md 或本地 SKILL.md，历史快照不作为当前指令。沿本审者独立准备的 `/tmp/rb04-reference` 再核真实 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`、Maruno17 origin 与干净状态，之后只读。未将参考跟踪进主 Git、未改 ignore、未 push 参考。

固定原问题为 GIR `93e10babe0b9c9ef8b3f5277754541b447beeeb4` 的 findings.json，批准计划／finding-acceptance 为 `41fffb540c6483f5296ea0d33b789b75180d27ed`。逐项 current_qualifications、最终 root／extension 裁决优先；raw/historical 状态不扩大范围。17项 B08 完整原问题／接受对象及全部扩展与固定源精确相等，这是完整性核验；语义裁决仅 A053 孵化交界、B026 a/b/c 公开入口、C003 C05 EN16 的前提收窄与 C082 大会陆地调用。未重新批准全部17项贡献。

本轮新读21参考文本文件、36次范围、1200唯一行，已读及每文件未读补集、blob／SHA-256 见 [source-reading-log.json](source-reading-log.json)；行数不代表分支覆盖。当前 caller／原稿／receiver 范围在 [project-reading-log.json](project-reading-log.json)。先冻结 [first-judgment.json](first-judgment.json)，后比较 A-REG 的1837／1665检查记录；此前已读 manifest、公共当前层、冻结元数据和候选门，因此不声称盲审。作者／历史审者检查程序未执行，其成功摘要不替代本轮1321项独立检查或参考判断。

## 孵化：动态形态与失败阶段

范围为 WP35 §5.2／9、EG-13／20及原稿对应条款，连接 WP15 蛋／裂纹／前图／叫声、音乐恢复与 WP17 实际孵化／命名消息。参考 EggHatching 13–40、52–137、202–268，Pokemon 92–116／147–178，FormHandlers 322–328，Time 201–203，Species_files 1–115／183–244，Pokedex 195–218；全部在上述精确参考 commit。

| 静态前提／反向对照 | 有界判断 |
| --- | --- |
| 普通非Shadow DEERLING 蛋，存储form0、无forced、steps1、月2，非战斗／非储存，玩家／地图／图鉴有效，媒体与消息正常、跳过命名、无其它改写 | 计数先归0，core字段按序写入；场景首读动态形态提交form1、重算及登记已见形态，随后蛋／裂纹资源使用该形态，通常拥有／见过蛋写入在成功消息之后。 |
| 月1；或有效非nil forced；或战斗／储存短路 | 月1保持form0，无该次季节setter；forced优先于季节处理，战斗／储存返回存储形态。EG-20不推广到这些条件。 |
| core之后，Huh或背景阶段先抛错，尚未到首个动态form读取 | core已有写入，季节提交和后续拥有／见过蛋未得到保证；背景缺失是否报错仍按实际消费者及明确宿主前提。 |
| form提交后，裂纹所有候选不能解析 | 解析nil交给 AnimatedBitmap 4–19 明确拒绝；core／form不回滚，通常图鉴写入尚未到达。异常不变成演出正常返回false，也不触发文本替代分支。 |

蛋／裂纹的形态→物种→通用候选均可耗尽；前图bitmap可nil、叫声缺失可0／不播放，不能把这些后继与裂纹nil异常合并。候选请求不证明素材存在、实际呈现或发声。PBS 的 DEERLING FormName 及夏形态样本已读，图鉴已见形态不误归form0；未读其它样本不外推。

实际 core 后 Huh 使用暂停，再进入 with-music fade；演出后清名称，孵化消息含文首空SE和wt80（逻辑4秒，非墙钟观察），之后通常图鉴写入及条件图鉴／昵称流程。Messages 478–551／613–654 的普通resume与实际入口一致；昵称入口min0/max10沿WP17模式规则，没有新增数字输入、兼容字符或富文本合同。

MessageConfig 629–641 只在 inner block 正常返回后恢复位置／BGM／BGS；559–590 的外层确保处理淡出／视口，不替内层恢复音乐、领域回滚或统一资源释放。WP35 原稿、净化正文及EG-13／20在actual原字节一致，明确core没有显式改形态与场景读取可提交的区别。未发现新增 B04 接口不一致。

## 大会：伙伴与公开单／双敌包装

范围为 WP36 §3.3／4.1／4.4／7、EN-16／32和相关原稿，连接WP16 foe数／类别／位置／正常清理、WP15 BGM及WP17实际消息。参考 WildEncounters 47–98／211–217／249–263，Overworld 172–217，BattleStarting 171–201／306–345／354–408，BugContest 171–196／350–404，BattleIntroAnim 59–151，BattleAudio 1–20。

| 独立夹具／反向对照 | 公开调用后果 |
| --- | --- |
| 活动大会已选一名可战玩家，Sport20／保留K、时限足、合法BugContest草地、概率／允许通过，非Safari，无雷达／漫游／其它覆盖／插件／布局残留，合法伙伴且force-single假；正常击败并返回 | 伙伴真门先于一员假门→双候选。公开start仅单敌可派发覆盖，双敌走普通core／伙伴准备→foe数组与类别2。没有大会预算传入／回写或K大会存储改写，不发单敌wild-end；普通善后因伙伴存在治疗玩家与伙伴。 |
| 同夹具无伙伴；或伙伴保留而force-single真 | 一敌；仅can_override且大会覆盖未被先行处理器接管时进大会、类别0。20预算传入，正常包装返回后回写；预算耗尽公告／judging仅属该单敌分支。 |
| 触发／允许拒绝、正常返回false、包装异常 | 按各阶段合同区分。步进开战调用正常返回后才清type、置trigger并复位force-single；不得补造异常治疗、预算写回或清理保证。 |

移动陆地汇总含contest，雷达普通land查询仍排除contest；机会真或仅有表不保证最终开战。§4.1计步回绕在迈步事件／孵化之前，不改B04形态月份、媒体入口或消息控制。完整概率／平衡等级数学域由其它复审负责。

类别2与位置2分别是双敌野生及洞穴输入；surf／dive→fishing→cave→indoor→outdoor位置判定独立于伙伴／大会。默认过渡野生族和自定义资格接受实际类别／foe数，不能反推训练家类别。正常包装返回才恢复音乐／音效、清记忆与位置和四类下一战预置、reset计步、请求0.4秒淡回并清in_battle，步进字段清理在其后；无确保式全异常恢复。

Wild BGM仍nextBattleBGM→非空地图wild→非空全局wild→默认，忽略foe内容／数量／等级。RM35的48／52级不生新选曲键。B06 WP24仅§5.4/PT41–63六逻辑请求与引子记忆接口，WP15参数／默认覆盖／音量／素材门保持，无全BattleAudio或伙伴／雷达批准扩张。

实际一／二敌野生开场由 Battle StartAndEnd 170–209 选择文本，经 Battle 824–825 到 Scene 230–265，暂停与skipAhead属于战斗场景，不能套通用pbMessage的resume合同；大会预算公告不套普通双敌。原稿正确既有优先序保留；EN-16 force-single反例与EN-32公开双敌正常返回前提匹配。完整战斗UI、伙伴捕获B013／CP20、WP53全部预算规则不由本门接受。

## 公共层、同步与下游

1321项独立审计全通过。12正式在actual与候选精确相等；四原稿的before在接受前驱／WIP一致，after在candidate／actual一致，31346字节v2patch SHA-256 `05b75bcafcb1fd9359e9a35e935e8b7cbb7dd038a0f3349a1172d1fe3ba88f25` 原样。历史prepare→authorize→apply和跨容器锁继续AUTHOR_SELF_REPORT_ONLY，不由最终树追认。WP33／37只验授权集合与身份，不接管业务裁决。

公共10路径的当前层、批准ledger及trace后继均区分候选PASS、三actual待审及父C未执行。旧133TSV行是精确字节前缀，新17条保留OPEN／pending、候选SHA／报告SHA、完整限定控制指针和其他责任。七份非catalog公共正文历史字节保持；catalog README仅三范围更新及追加当前层。旧候选报告的待办措辞按其冻结时点保留。旧接受统计133记录／118触及／87主责、具体87/0/0、严格79/8完整对象保持，当前150行不升级B08接受数或A034严格统计。

79计划输入在actual重新绑定，其中3个公共读者相对候选发生管理层变化；全部不是浮动branch。B04十三正式及WP24／28／30／34原／最终八正文仍是前驱字节。B04→B07串行门、未来WP28／30或共享caller/data/condition变化后分别candidate／actual B04复核条件保留。

B09当前准备合同是62读／7写、20贡献／13主责，路径集合与固定计划相同。全20控制完整对象仅审核完整性；没有B09业务批准。B09／B14／B15／B19／B20／B21仍NOT_DISPATCHED；三份分别actual报告同一SHA均通过之后再父C，C接受后的精确后继须重新冻结全部planned reads/writes及有界extras，旧批准只约束未变精确版本；B08四原稿许可不传给B09。全文件目录锁与反向caller gate保留，不授权并写。

其他责任保留：B09 B013/CP20伙伴捕获与持物还原、WP39漫游消费；B12 WP53完整大会预算／伙伴；B19编辑器／缓存／编译快照；B20 WP77平衡等级；B14/B15/B21全局与整合；B16 A048、C003 A23/A31/A33、D023。完整current_qualifications／所有扩展保持，不能以本接口PASS关闭共根或批准这些后续贡献。

N01只是固定前驱→候选的353诊断＝344trailing-space＋9new-blank-line-at-EOF，本轮独立复算一致，13存档diff／patch路径原样保留。作者344子集及R-B07历史口径不追改，不称actual全库总数、不新增canonical问题。

## 限制与交接

请求gpt-6.1-sol／Ultra／Standard(default)，可信配置回显缺失，实际model／reasoning／tier保留**UNVERIFIED**，继续Plan A。配额监控按用户关闭，认证／令牌／配置探测0；未派生子任务。

U01–U10／G01–G12／AX01–AX20及具名未读全部保留：八杯赛名单、pokemon_metrics样本、备份/gen未全文，Data/Scripts.rxdata及二进制、真实地图事件、图像／音频／字体／声字体、Game／DLL／mkxp宿主配置与实际容量，插件／动态／deprecated、EventScene／动态阴影可达性、真实Demo链。容量1024／2048、缺图宿主错误仅条件夹具。每个已开参考文件的未读补集清楚列出；本轮1200行不填补其余未读。

参考／游戏／编译／转换／反序列化／媒体读取／参考行为模拟器执行0，静态行为向量执行0，运行观察0，已证Demo链0。本轮Python仅处理Git／JSON／文本／hash／报告存档，不执行或模拟参考行为。

本报告仅新增本目录、普通commit／push报告分支、远端SHA回读后交付。没有公共／正式／历史修改或ID整合关闭。无本轮范围内修复阻塞；其他两份actual复审及父C仍是整批接受门。精确交接见 [handoff.json](handoff.json)，等待父任务。
