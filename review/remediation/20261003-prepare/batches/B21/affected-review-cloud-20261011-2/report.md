# B21 NEW2 独立 affected 再审

结论：**PASS_SCOPED_NEW2_AFFECTED**。本次覆盖全部 B01–B20 owner 的固定 C→NEW2 影响；原 B21-AFF-NAV-001、B21-AFF-NAV-002 及 C029 归属勘误已真实消除。B20 两份 WP75 新字节、B03/WP13 与新旧案例，以及 B14/B19 转换/治疗/提取/编译接口回归在静态限定内通过。327 旧接受贡献与历史证据保全通过。没有剩余 affected 候选阻塞。

此结论仅属于以下精确 NEW2 字节。不是 FULL 候选、actual、B21 C、canonical 关闭或 FINAL 签名；局部 scope 许可和作者数量/断言均未被当作质量通过依据。旧报告仍固定在其原提交，不改写或撤销旧候选的 NEEDS_REVISION 结论。

| 固定角色 | commit | tree |
| --- | --- | --- |
| NEW2 被审候选 | `e58486178e746273fb6fab55df00722807f1dc44` | `1dbe28a733bfde428129ed662d7e0d66243978c4` |
| 作者发布 P2 | `9b6d16e34daf59e205f8a3df20e24930175064ed` | `11c07f505fc57d62ffd0bf643a1ea0b575a3fd8d` |
| B20 C 正式基线 | `e9c140dc33de1cb0662521318b051174909e4509` | `5baa01c8a604400b73f560bb06fa5d770089502a` |
| 原派发 D | `eb1885265fcde2a52767077de3193862036c3a71` | `c85948f536d7444bfe83d3c323ea6a48ba15d143` |
| 三路径局部 scope G | `aa57e293bf3a0a77fa42f1f42777df88cbd2fbe8` | `d1333b17eb6987d51dac40988d7d0e744b2ed677` |
| 旧 affected 报告 R1 | `7db07543137cc11ef76b725e0a3c8975796bc7b0` | `16cdcc4016407cbe1d58ede64f745090b2282b21` |

NEW2 唯一父提交为 `a740b86cb6b721c61e23fbcea5e365180fc4523e`，tree `56217c655291fd68641dd74acf9980e223fea928`；正式完整比较仍是 C，不把 a740→NEW2 的三路径变化当作全部差异。

## 精确入口、差异及局部许可

先读 P2 的 `review/remediation/20261003-prepare/batches/B21/author-draft-1/freeze-2/frozen-NEW2.json`，再读同目录 FULL/affected 入口和 review-dispatch；随后读 G 的 `batches/B21/original-scope-grant-R-B21-006-1/scope-grant.json`（以下所有相对 `batches/`、`wp78/79` 路径均以 `review/remediation/20261003-prepare/` 为根）。原 D 的完整合同、20 依赖、229 义务与原 PLAN `41fffb540c6483f5296ea0d33b789b75180d27ed` 的完整控制继续有效；本次精确比较固定输入身份后复用原有效阅读，不重新泛读整库。

独立在内存重建未过滤 `git diff --no-ext-diff --binary --full-index C NEW2`，逐字节等于唯一已发布完整差异：

`P2:review/remediation/20261003-prepare/batches/B21/author-draft-1/freeze-2/complete-C-to-NEW2.diff`；blob `f2fff7305f79d34b6d081e4b40131c0a903ada2b`；SHA256 `0213e85fbe687500343f9e3848b49650bafdb7a726cac8beb54f083ee7e41b15`；**4,541,616 bytes**。本目录只引用固定身份，不复制完整差异、旧 freeze 包或递归历史成果。

完整差异为57路径：原22正式输出＋精确获准3路径＝25输出，另32作者证据。全部25 after 在 NEW2/P2 与冻结身份一致；全部 C before 核对。获准3路径独立重算逐行差异，分别是 WP75 原稿第257行、最终稿第235行的一段替换，以及目录第243–248行的五案例与空行插入。三者均等于 G 指定的完整 after，所有 hunk 外行字节不变。scope 文档 SHA256 `a768aff855c04e0be4754270a68500fd7b2d5b715cf90c86657ebbfa9a60b3bd`，18,923 bytes；scope 的批准只负责写入范围，以下语义判断另行完成。

详见 [独立静态身份/保全审计](static-audit.json)、[新建只读审计源码](static-audit.py)。359 检查无错误；检查数量只陈述方法，不代替语义判断。

## B20 新字节与 B03/B14/B19 回归

参考来源固定 `Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。SRC-040 的 `Data/Scripts/004_Game classes/006_Game_Character.rb`，blob `9de49c288ec6c5d8c962b14f1b959ad90ae3d662`、SHA256 `48496384805d3d5b67c6ba990486de4d53f60cfb7a09e4fc81a3a8350a18d871`、30,978 bytes，静态读 `move_type_custom` 427–551：45 分支先在540求值，541–543才检查三准确行首前缀，命中544推进并545返回；未命中到548推进，在现有循环继续。没有把 `eval` 执行为本次验证；读取代码只是静态控制流证据，外层呈现/真实事件未知继承。

两份新 WP75 §8.6 现在都规定原串**任一行行首**、三准确大小写字面、整个求值正常返回前置、命中推进并结束帧、无命中推进后同帧继续、异常先于判定与推进。空白、接收者或大小写变体只使该行不匹配，其它行仍可命中；长后缀可匹配，不把字面前缀当方法签名，也不保证任意字符串求值成功。异常不到分派器的后续推进点，不承诺回滚脚本此前副作用；有效角色/列表/文本及后续循环机会是静态前提。与 C→NEW2 完全未变的 WP13 原/最终 §1/§2 一致。旧 B20 PASS 只负责固定 before，本次另外判断此新段落。

| 实际新输出 | NEW2 blob | SHA256 |
| --- | --- | --- |
| `specs/demo/wp75-project-conversion-and-authoring-tools.md` | `3d8b2744c200484fc4a5dcdac2b6fb38542a6a19` | `0db98a17ecd51cc69e7ccc307a97e103d5211585016902f669e226a5f6e7ec75` |
| `deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md` | `b2221b3a1793a579cdfbfc74f4bc1e8ea54e23d0` | `2968e3946a4ab751fcdb3d2dda241b3e94f6c4e49c04fe07b0494a5d6c9631a5` |
| `deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md` | `90d0b2513cbcde582ad62189efae93153ccbeab1` | `328093fecfc874cab446a8b969ca8e78889842643fb5859edb2ddea7dcfd17fc` |

目录全部旧字节可由删除唯一插入段还原 C；MR01–MR17 各完整行字节、次数、顺序相同，MR08 仍明确“某行行首”。MR18–22 分别补后续行命中、ASCII 空格、接收者、UD/LR 长后缀、整体异常。这些是未执行静态前提设计；正常返回或必失败各自为显式前提，不能把匹配文本本身当成功执行。WP13 最终稿仍为 SHA256 `8eca09260fa1ab57791542cfc250ae51ea0e13dab7456d85c3e0a1d5704ef5aa`。

B20 的35转换身份/ASCII和 SRC-314 `004_Compiler_MapsAndEvents.rb` 静态转换流程另读，治疗首字符预检→续行拼接→删除空白→精确匹配及原少删1缺陷、driver 先替换后 fix-use 等旧顺序不变。B14 时间/色调消费者及 B19 编辑/效果白名单、治疗/提取/编译边界不因新路线摘要得到自动执行保证。新 G7-4/G8-2/G8-3、CHAIN-6、SRC-040/SRC-314 的真实消费桥指向已更新 WP75/目录 after，而非沿用旧 hash。WP75 §3.1/8.1/8.4/10/12.1/12.2 原条款字节复用，只有 §8.6 改动。

详细顺序、反向前提、固定 source/body/case/owner 证据见 [B15–B20与路线接口独立子审](b15-b20-and-route-review.md)及[机器索引](b15-b20-and-route-review.json)。

## 原问题真实消除与九修复单元

| 单元 | affected 再核结果与资格 |
| --- | --- |
| R-B21-001 / G1-2 | Shadow 四文本131/18/4/1已读样本、字段与具名 BUTTERFREE 4000/招式顺序可查；与未读 Gen5–8身份分开。样本不降格为只存在性，也不推出编译/启用/真实 Demo，U06保留。 |
| R-B21-002 / G2-4 | 周期达到128后按成员独立1/2，命中才消费成长/Shadow门，循环后归0。0/1与1/0、126/127、空/全不合资格反向前提可表达，未使用共同概率门。 |
| R-B21-003 / G2-8 | 旧图存在/异图/类型变化局部门明确；Rain/duration7再次Rain的显式重建保留7，有效连接另后写20。同图不重掷，渐变守卫和单强度不刷新保持；20不解释为20秒。 |
| R-B21-004 / G4-2 | 原快照仅开始写；玩家队伍四入口含进行中报名/租借提交，nil与[]、开始/暂停/继续与取消/结束保存门、等级前经验/等级后物品分别保留。 |
| R-B21-005 / 原 NAV-001、OBS | FD003 root WP72及实际编辑域补足；ext4为WP67-A/WP76及B17真实row265，ext9为WP60/61/63/65及B14/15/16真实owner，ext10为WP66-A/WP67-B/README及B16/17。C029现有WP77 §6.4/demo及B20贡献精确关联，B05机制复用、B19编辑consumer复用分别命名，不冒称C029贡献。 |
| R-B21-006 | 本次三路径新字节及B20/B03/B14/B19静态接口另核，结果如上；scope许可不参与质量判定。 |
| R-B21-007 / C003 | A23/A31/A33与生命周期L09分列；WP35孵化机制、WP67-B生命周期4.1/4.2、LC-L09实际案例及真实接受owner对应。收获/机制/UI不能由同号彩票/挖矿路径替代。 |
| R-B21-008 / 原 NAV-001 | CFG25/26及SRC392/393已连接真实当前PBS机制/样本消费者和scope，不再是空路径；机制/样本/内容/启用分层，未扩大为全PBS逐条阅读或启用证明。 |
| G9-3 / 原 NAV-002 | 五当前固定管理文件区间和实际B01/B18回执/trace关联完成；九原输入限定批准、当前修改字节接受、作者待审和未来actual分层，未给B21虚构旧签名。 |

根复审直接重读 G1-2/G2-4/G2-8/G4-2 新中央条款、静态反例及对应当前 WP23/WP61/WP59/WP11/WP55 条件；其当前正文与 C 不变只是保全事实。导航逐scope又核 FD003 完整 root/extension、C003/L09/收获及 CFG/G9-3。不是仅把 domain 标签改对：当前条款/案例区间、真实 scoped 回执与 trace 都吻合。原 NAV-001 在两单元中有界修复，未注册新的 canonical 问题。

47 原批准scope对象哈希、14整项 original/approved/qualified fields保持；旧same-ID整项导航不能自动担保不同域，本次正确消费者另外阅读。G9-3 B01 GIR001 receipt0/trace1、B18 GIR001 receipt276/trace277、B18 R02 receipt283/trace284精确归属；原九输入2同字节/7各+41声明路径重映射和18原/最终文件旧限定有效，不能转授WP75新字节。

固定旧指针与当前整文件身份分别判断：G9-3的audit合同仍引用旧NEW快照第1–18行，NEW2仅末尾追加路线后继，该条款范围与NEW2完全相同（范围SHA256 `318f62c9379fb666dbc3bdfd5c1081065cc83d5942d490805013b6276bc4b1fd`）。当前audit整文件另核为NEW2 blob `31aa257d553e84cadae5b668bd80256938697644`、SHA256 `f19850de40c266e4135a829419e624ff2cdbb61258fc34edae1938dabd95fe25`、290,437 bytes，1561–1563明确当前25输出/许可/待审与真实变化。此处是同字节限定条款复用，不能冒称整文件未变。同样WT07在C/旧NEW行326、NEW2行332，完整案例行（含换行）SHA256 `da1ddd7561b88f9d1b85bb498e06d8c6736ea0bd9a199a6e388479e521b2c29c`不变；旧固定行号不被当作NEW2行号。

54交界中8行变化，8链中5项变化，source后继中8项变化按具体当前接口核；其余固定证据保留原来源/调用者/异常/样本/激活限定复用。432来源身份、35配置/17UI不是432/52个全文件语义新阅读。其它有界 opaque/身份/实现边界的空consumer仍按原范围处理，不据空值扩张支持承诺。见[导航/交界/资格独立子审](navigation-and-junction-review.md)及[机器证据](navigation-and-junction-review.json)。

## 全部 B01–B20 owner、327贡献及未受影响依据

每行都是本次固定NEW2 affected disposition，不重签旧candidate/actual或贡献接受。完整20依赖指向D固定accepted-dependency-map；全部327逐对象规范化hash与C一致，整数组 SHA256 `ca73d8b68c03e80e40066acb4349683836f8165a4f2daa5935cfef8b852cd9fa`。不得把旧 B20 接受自动扩大到新段落。

| owner | 旧贡献/primary | 具体刷新与有效复用 |
| --- | ---: | --- |
| B01 | 14/7 | PASS_SCOPED；配置/PBS身份/生命周期条件保留；Shadow与备份资格分列、CFG当前关联和G9-3实际owner复核。 |
| B02 | 12/9 | PASS_SCOPED；日期/uptime/游戏秒/保存/迁移/语言锚点、单位和部分失败复用固定旧资格。 |
| B03 | 27/19 | PASS_SCOPED；WP13与旧案例保全；新WP75/MR18–22另核，天气局部/连接门刷新。 |
| B04 | 35/23 | PASS_SCOPED；34世界显示、资源/音频/预览原合同保留；天气意图与显示门不混，目录新案例另核。 |
| B05 | 16/10 | PASS_SCOPED；Shadow样本/启用、形式读写/学习/PP与友好阶段门保持；C029当前归属纠正。 |
| B06 | 10/7 | PASS_SCOPED；对象/接收/库存/盒长、precheck/execute及部分提交未改，既有链证据限定复用。 |
| B07 | 19/12 | PASS_SCOPED；G2-4抽样/成长门刷新，消耗、学习、进化、战后次序和部分失败保留。 |
| B08 | 17/9 | PASS_SCOPED；繁殖/孵化与遭遇/OldRod/漫游雷达不改；CFG/L09关联实质复核。 |
| B09 | 20/13 | PASS_SCOPED；伙伴移位单次终局、注册/执行/音频不改；FD003呈现真实scope与A059精确row155保留。 |
| B10 | 7/2 | PASS_SCOPED；OHKO最终资格/HP/伤害入口不改，既有数据和反向条件复用。 |
| B11 | 6/3 | PASS_SCOPED；几何、near-neighbor、特性/持物阶段不改，具名调用者资格不扩大。 |
| B12 | 9/6 | PASS_SCOPED；AI上下文/评分/特殊战不改，收获机制/UI关联另核，未声明最佳策略保证。 |
| B13 | 8/5 | PASS_SCOPED；G4-2四入口/单快照、nil/[]、保存/恢复和经验/物品顺序刷新。 |
| B14 | 24/19 | PASS_SCOPED；四时间通道及输入保持，天气与B20工具接口重审，FD003 ext9真实域修正。 |
| B15 | 16/10 | PASS_SCOPED；电话18/地图/邮件/礼物共享状态不改，ext9真实owner导航刷新。 |
| B16 | 24/20 | PASS_SCOPED；容量/BoxLink/队伍/命名/部分写入不改，ext9/10分层和实际row241关联刷新。 |
| B17 | 12/7 | PASS_SCOPED；WP67呈现/交互/生命周期与WP76失败/槽序不改，ext4/10真实owner归属刷新。 |
| B18 | 8/5 | PASS_SCOPED；九原输入限定批准及小游戏前提保持，G9-3真实回执与待审层另核。 |
| B19 | 24/19 | PASS_SCOPED；120参数/白名单与编辑/转换/编译边界保持，B20新路线消费桥和FD003 root刷新。 |
| B20 | 19/15 | PASS_SCOPED；WP75新段另独立判断，35转换/三准确字面/ASCII、WP77 C029及Demo限定保全。 |

B01–B14对应106个current consumer身份逐项核：除共用目录的精确新增段，全部同C；目录所有旧字节亦保持。记录[固定证据复用与owner刷新](b01-b14-fixed-evidence-reuse.json)指向R1每owner的原语义检查、实际candidate/actual/report限定，不复制旧整包。B15–B20与新路线另见子审。未受影响判定依据为完整差异范围、具体接口读写/调用者条件、旧有效scope与当前字节对应；同blob单独不作语义通过理由。

## 历史保全、统计与执行边界

36,837受保护路径的mode/type/blob同C，包括参考、AGENTS、旧接受批历史、除获准三路径之外的原稿/正文/案例。旧两个TSV327行完整字节前缀保持，新增14行仍为OPEN作者待审且无候选独立签名；229 finding的ID/顺序与OPEN状态不变，未分配215行字节不变，分配14行只加closure_gate限定。旧中央Markdown字节层连续保留，旧JSON字段不改；日期manifest只加后继。旧报告及完整差异在固定提交可读，不要求在NEW2树递归物化。

独立统计仍为20接受批、327贡献、228触及ID、220主责最低、215整项严格、14待B21贡献/9待B21主责，229 OPEN/0 CLOSED；21/341与229整项完成均为未来投影。旧138完整数组实际计数、原158标签与九输入/历史载体证据按R1固定审计及未变历史对象复用，不改旧签名。范围和案例补齐不新增接受/关闭。

参考游戏、Ruby、编译器、转换器、参考数据反序列化器、行为向量及旧执行脚本的执行均为0；静态案例执行0、运行观察0、已证真实Demo事件链0。新审计只操作Git和UTF-8文档元数据；静态source代码是只读文本，未执行其中求值/转换。U01–U10/G01–G12/AX01–AX20及未读备份/样本/素材/地图事件、宿主/插件/配置/动态调用/容量限制全部继承，67树果完整目录仍条件性。模型参数按用户协议接纳，不做额度或模型审计、不使用CLI代替独立模型判断。

报告分支只新增本目录；没有作者正文、参考、main或旧证据写入。本轮没有旧报告改写，前轮披露的临时工作副本异常保持原记录，不冒称此轮新事件。

## 验收与后继条件

本次affected候选门已满足：原两NAV与OBS实质消除，固定NEW2的B20/B03/B14/B19新接口和全20owner回归通过，旧327/WP13/所有旧案例与历史scope保全。仍须原独立FULL候选结论另行协调。

唯一登记员后续整合时须冻结精确ACT/tree、应用前基线与实际25输出；原独立R-B21再核actual及实际影响，不能由本NEW2报告或scope许可转授。B21 C、原FINAL-1、有证据的登记员逐项关闭/最终SHA、FINAL-2仍各需完成。本报告不触发main合入、仓库整理、本地同步或第三轮review。任何新字节需其对应新独立判断。

本目录的[主结论机器记录](findings.json)、输出身份清单和独立远端读回回执记录报告发布；发布回执不能自嵌其所在提交身份，最终报告commit/tree与全部输出（包括回执自身）的末次远端读回由交接给出。
