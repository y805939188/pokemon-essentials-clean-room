# B21 独立 affected 候选复审

结论：**NEEDS_REVISION — 中央精确导航/归属仍有阻塞；B01–B20 既有接口及327旧接受贡献保全通过。** 本报告负责全部20个既有owner的C→NEW affected范围，不能命名为FULL、actual通过、B21接受或FINAL签名。复审独立于作者；分析附件是本次复审辅助材料，结论由本报告统一给出。

被审 NEW `5c3e19831e1e29450247fa6061f3c2feac2f893e`，tree `98062bf1205669936426ae870913e578528b740c`；唯一父 C `e9c140dc33de1cb0662521318b051174909e4509`，tree `5baa01c8a604400b73f560bb06fa5d770089502a`。作者最终发布 P `fa5e1d876c9082797d6eb71f1590f3d8d9a19b0a`，tree `de3dae76d08f1d08e54f78fe95a185211a63d14a`。精确派发 D `eb1885265fcde2a52767077de3193862036c3a71`，tree `c85948f536d7444bfe83d3c323ea6a48ba15d143`。报告只在独立报告分支添加本目录材料；发布不包含作者候选、正文、参考、main或旧证据改动。工作副本的一次误写/恢复另在下文如实披露。

## 阅读及判断依据

先读取 P 的 `review/remediation/20261003-prepare/batches/B21/author-draft-1/freeze-1/frozen-NEW.json`，再读取同目录 `review-FULL.md`、`review-affected.md`和`review-dispatch.json`；随后读取 D 的 `refreeze-after-B20-C-1/author-contract.json`、完整控制overlay、accepted-dependency-map、全部229义务及global-closing-requirements。原合同为 `41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/batches/B21.md`（blob `81582535b2eeef776d408b8c3a830594c99f52b7`，SHA256 `c297a9131ad4352b392b807bf2044cc9adea9eec903950fbc9897d2f6ef3f0f6`），原完整控制分别按`93e10babe0b9c9ef8b3f5277754541b447beeeb4`和`41fffb540c6483f5296ea0d33b789b75180d27ed`解引用。导航overlay未被当成原控制替代品。

独立重建未过滤 `git diff --binary --full-index C NEW`，在内存逐字节比较 P 已发布的唯一完整差异：

`P:review/remediation/20261003-prepare/batches/B21/author-draft-1/freeze-1/complete-C-to-NEW.diff`，blob `4c62a62920b5d41f95c2f3b7ad74e5ff8f7d518d`，SHA256 `7cb43d6e3b3ab252029396234dd5de631ff37b85171270be40f0a239d39dcb8a`，3,430,268 bytes。

重建一致；本目录仅引用该位置，不复制完整差异或递归整包。35变化路径精确分成22正式输出与13新增作者证据；22输出均与冻结身份和P实际字节一致。96派发输入及216个项目固定证据身份逐项独立核验，无身份错误。作者自检、数量和未变化blob只用于导航/保全核对，没有被当成语义通过依据。

语义检查按全部20 owner及54交界/8链展开，读取当前具名消费者条件、顺序、失败/取消、邻近反例，以及原限定控制、旧精确candidate/actual报告和真实回执。无变化有效证据固定复用；身份核验不是对每个来源全文的新语义阅读。完整逐owner刷新范围及未受影响理由见[B01–B07](owners-b01-b07.md)、[B08–B14](owners-b08-b14.md)、[B15–B20](owners-b15-b20.md)；另见[54交界/8链](junction-chains-review.md)、[导航/14资格/47映射](navigation-review.md)、[九输入及历史保全](approval-history-review.md)和[机器可读主结论](findings.json)。附件局部编号B21-NAV-01与R-B21-JUNCTION-NAV-001分别对应本报告的两个阻塞，不新增canonical根。

## 阻塞与有界返修

**B21-AFF-NAV-001：当前扩展/资格→owner→条款映射错配/遗漏。** `NEW:author-draft-1/obligation-map.json`保留了完整原批准对象，但其精确当前domain/consumer摘要并非全部正确；整项same-ID旧追溯能救回旧证据，不能使明确写错的扩展映射成立。

- `/records/9`（GIR-FD82-003，`extension_decisions/4`）把WP67-A+WP76错成WP39+WP76。原批准明确保留WP67-A呈现/接受/执行的分层，仅移除非必要参数位置/基类/继承组织；WP39战斗领域上下文不能替代WP67-A交互/呈现条款。正确旧B17证据保留在C traceability数据行265及B17精确actual FULL记录。
- `/records/14`（同ID，`extension_decisions/9`）原位置包含WP61/WP63/WP65/WP60，当前domain却列WP63/WP65/WP66/WP67，漏掉WP60/61。
- `/records/15`（同ID，`extension_decisions/10`）原位置是WP66-A/WP67-B/README，当前domain却投到WP72/73/74/75。
- `/records/39`（GIR-FD82-C029）及`traceability.json#/records/9/current_consumer_nodes`缺少实际B20修订承接的WP77及对应demo静态目录。WP21当前条目仍只称“特定宝珠”，提供主读取机制但未给GRISEOUSORB完整身份；WP77 §6.4第145–146行和demo目录第278行才承接GIRATINA/GRISEOUSORB/DistortionWorld、强制形态含0、battle/storage短路、普通form与form_simple差异和12个静态对照。

另补查`NEW:wp79-config-successor.tsv`数据行25/26（文件行26/27）及`wp79-source-successor.json#/rows/391`、`/rows/392`：CFG-25/26和SRC-392/393的`current_consumer_paths`均为空，source的`assigned_control_ids`也为空；只回链C旧v4限定。它们不是NA/deferred，机制文字已明确WP31/WP33/WP35/WP55/WP47-B及WP22/WP31/WP32等实际当前消费域。必须把这些限定分别绑定当前精确条款、样本承接及真实已接受owner，保持样本/机制/启用分列，不能扩大为全PBS逐条语义读取。其它34个空source项分别为15个身份、9个不透明材料和10个继承的实现边界，按其限定不据空值新增缺失结论。该缺口并入本导航返修，未新增canonical finding或第三阻塞；详见[资格消费关联补查](qualification-consumer-supplement.md)。

本项阻塞的是B21约定的精确导航/归属交付，不是这些owner既有行为遭到删除。原完整控制hash、same-ID接受回执、消费者实际字节均保持。原批准GIR003的逐条语义映射和body/data/test/successor-trace一致验收不能由47对象数量、泛化域名或所有same-ID旧行代替。精确对象hash、正确位置和逐映射结果见`navigation-review.md`。修订只需本批新中央/作者导航材料（含配置与来源资格后继），不需要改动正文或历史证据。

**B21-AFF-NAV-002：G9-3管理交界没有当前合同和owner绑定。** `NEW:review/remediation/20261003-prepare/wp78-junction-successor.tsv`的G9-3两列`current_contracts`和`accepted_owner_dependency_pointers`都为`[]`。对应`junction-evidence.json`仅给大量C旧trace行和泛化完整控制声明，未精确定位本轮matrix/manifest/规格头部逐位置管理状态、更正后的九输入批准链和真实owner归属。当前接口/反向描述本身方向正确，旧证据保存；但“54个合格交界具有实际当前条款/案例/evidence links”的有限交付义务仍未满足。需补当前NEW中央条款身份、相关旧B01/B18等精确限定回执及本轮B21待审层，不能给尚未接受的B21虚构旧签名。详见`junction-chains-review.md`。

**B21-AFF-OBS-001（非阻塞文字归属勘误）：** C029的`static_case_navigation_not_executed`写“accepted B05/B19/B20 C029 cases”。真实C029接受贡献仅B20，回执为C统计`/accepted_contribution_receipts/317`、C traceability数据行318。B05 WP21为已接受主机制复用，B19为编辑器consumer，不是C029接受贡献。机器接受字段未扩大，故不单独判行为/接受链失败；下一版应明确分列，避免reader误认旧owner签名范围。

## 全部20 owner的限定结果

各行表示本次affected对旧接口条件和归属的判断，不是重新签发旧candidate/actual门。`OLD_INTERFACE_PRESERVED`只覆盖本轮中央变化对已接受接口的影响，全部原来源/调用者/异常/静态限制继承。公共导航阻塞归B21作者返修，不抹去旧owner接受。

| owner | 旧贡献/primary | 本次affected结果与关键接口 |
| --- | ---: | --- |
| B01 | 14/7 | OLD_INTERFACE_PRESERVED；WP02配置/原统计与WP04身份、兼容字面、索引与迁移声明分别保持。 |
| B02 | 12/9 | OLD_INTERFACE_PRESERVED；时间/统计单位、迁移失败、原值与部分写入不被中央数量替换。 |
| B03 | 27/19 | OLD_INTERFACE_PRESERVED；地图/天气20、移动/地牢、ASCII路由前缀与三个求值门保持。 |
| B04 | 35/23 | OLD_INTERFACE_PRESERVED；34世界显示场景、箭头首显/相位、命名预览、按入口音频/资源保持。 |
| B05 | 16/10 | OLD_INTERFACE_PRESERVED；形态求值/提交、强制门、Shadow及学习接口保持；C029归属文字需勘误。 |
| B06 | 10/7 | OLD_INTERFACE_PRESERVED；伙伴身份/接收、有限库存与存储接受前提保持。 |
| B07 | 19/12 | OLD_INTERFACE_PRESERVED；持物/训练/成长/学习与战后上下文、失败差异保持。 |
| B08 | 17/9 | OLD_INTERFACE_PRESERVED；繁殖/孵化、遭遇机会与主动OldRod、漫游先于雷达和专属邻接保持。 |
| B09 | 20/13 | OLD_INTERFACE_PRESERVED；伙伴移位单次终局恢复、注册/执行/音频消费与owner精确row155承接保持。 |
| B10 | 7/2 | OLD_INTERFACE_PRESERVED；最终生效资格与加载后OHKO差异、HP/参数/伤害规则保持。 |
| B11 | 6/3 | OLD_INTERFACE_PRESERVED；目标几何及near-neighbor判定、特性/持物分阶段条件保持。 |
| B12 | 9/6 | OLD_INTERFACE_PRESERVED；AI实际评分/上下文、失败与特殊捕获战保持，非泛化最佳策略保证。 |
| B13 | 8/5 | OLD_INTERFACE_PRESERVED；设施nil/[]、等级前经验/等级后物品、Arena和回放部分副作用保持。 |
| B14 | 24/19 | OLD_INTERFACE_PRESERVED；24小时四通道、世界/场地/钓鱼/毒感染输入限定保持；GIR003新导航漏域须修。 |
| B15 | 16/10 | OLD_INTERFACE_PRESERVED；地图/电话18旧入口、邮件及礼物共享状态保持；GIR003新导航须精确归属。 |
| B16 | 24/20 | OLD_INTERFACE_PRESERVED；有限库存/BoxLink、队伍/摘要/命名预览、部分写入及价格显示保持；新扩展导航须修。 |
| B17 | 12/7 | OLD_INTERFACE_PRESERVED；WP67分层/音频/生命周期与WP76失败/槽序语义保持；GIR003新domain错配须修。 |
| B18 | 8/5 | OLD_INTERFACE_PRESERVED；九原输入限定批准、小游戏取消/结算/拼图前提与静态夹具保持。 |
| B19 | 24/19 | OLD_INTERFACE_PRESERVED；120效果全部参数/白名单、编辑取消/共享内容与保存/编译/缓存分界保持。 |
| B20 | 19/15 | OLD_INTERFACE_PRESERVED；35旧转换、三精确路线前缀、动画身份、WP77 C029与Demo证据分层保持；当前C029导航须补。 |

直接consumer列表不全不自动判失败。例如A059的直接节点未列WP39，但同ID继承的C traceability数据行155已准确定位WP39 §7.5、BC23/24/25和B09回执154，独立读当前正文可以闭合。本报告因此没有把该列表遗漏升级为行为退化。相反B21-AFF-NAV-001涉及作者明确写错的扩展domain和关键承接位置，且原合同要求精确映射，故不能仅以整体same-ID链接冲销。

## 保全、统计与资格

新静态元数据审计`static-audit.json`的441检查和216固定身份均无错误。327回执逐对象规范化SHA256及完整数组一致；数组SHA256为`ca73d8b68c03e80e40066acb4349683836f8165a4f2daa5935cfef8b852cd9fa`。D全部20依赖逐回执对象与C统计完全一致，60个旧candidate/actual/report提交均可解析到固定tree，旧签名只按其原范围复用。旧approval/traceability两个TSV的完整327行字节前缀原样保留，新增14行均为作者待审、OPEN且无独立签名。229 finding原ID/顺序/状态保持；未分配215行逐字节未变，分配14行只追加closure_gate限定。

全树核对36,840个受保护路径的mode/type/object identity，无丢失或更改：最终111正文及17测试族、原稿/参考/AGENTS和旧历史材料保留。旧中央Markdown原字节作为连续层完整保留，dated manifest只追加后继；旧中央JSON既有每个字段完整保持。固定提交证据不要求当前树物化，例如B14部分旧独立报告只存在其原固定commit，C→NEW没有删除它们；附件区分树内保全与固定提交可读复用。

过程异常：临时审计输出整理时误复用了路径变量，短暂将JSON写到本工作副本的`review/remediation/20261003-prepare/batches/B01/author/historical-errata.md`。随即从固定C恢复，所有实质读取仍来自固定Git对象；根复审再核工作副本=C=P，3,003 bytes、SHA256 `bafff7cd954b8150456518ad407b9768559cceeb407bfe619cc1e62088cbf624`，该路径git status为空。误写未提交/未发布，本报告分支最终差异只新增报告目录。此异常不应被省略，也不构成旧证据最终字节丢失。

独立推算当前统计为20已接受批/327贡献/228触及ID/220主责最低修订/215严格整项/14待B21贡献/9待B21主责，229 OPEN、0 CLOSED。21批/341贡献/229整项为未来投影。当前最终Markdown实计131：七域111、17测试族+1索引、根2。旧B10–B19十个完整local-qualified数组独立重数为138（7+6+9+8+24+16+24+12+8+24），原158标签及所有数组保持，使用已接受B20后继勘误；本报告不复制旧整数组。

432固定来源身份、35配置mechanism/sample/activation、17UI entry/scenario/keybranches和111当前consumer身份/heading另有独立审计。14完整original/approved对象、逐qualified字段以及47根/扩展对象集合/hash匹配；这些保全事实不等于47当前语义映射正确。四旧NA世界消费者、箭头、训练家预览、入口选曲和清游戏时间路径已按具名consumer限定重关联。67树果完整目录仍为条件性建议；材料身份/机制/样本/启用分列，NA和数量不升级成全行为覆盖。

8链保持伙伴移位单次恢复、有限库存/邮件/BoxLink、设施经验及物品恢复时点、Shadow/形态/学习、编译转换缓存、Arena/回放和世界显示/目标几何的顺序、部分失败及邻近反例。53个具名交界可依当前/旧固定定位闭合；G9-3管理交界方向正确但精确当前绑定未完成，见阻塞。没有发现本次中央增量删除必要ASCII、外部身份、共享可见副作用或真实异常结果。

全部U01–U10/G01–G12/AX01–AX20、未读备份/样本/素材/真实地图事件、宿主/插件/动态调用/配置与容量限制继承。参考游戏、Ruby、编译器、转换器、参考数据反序列化器、行为向量和旧脚本执行均为0；运行观察0、已证真实Demo事件链0。新审计只解析Git和UTF-8文档元数据，静态场景及人工数学/前提判断未报运行测试。模型请求参数依用户协议接纳，不做额度/模型元数据审计，不用CLI代替独立模型审查。

## 验收条件及后续门

1. 在有界作者修订中纠正B21-AFF-NAV-001全部错配、关键WP77承接及CFG-25/26/SRC-392/393限定消费关联，给逐扩展/资格精确当前owner/条款/数据/案例/旧回执指针；同时纠正C029接受归属文字。
2. 给G9-3实际当前中央条款身份、批准链与历史位置、更正的owner限定和作者待审层，保持旧ReviewPending/dated manifest/所有旧签名不变。
3. 冻结新候选NEW′/tree及对固定C的完整差异身份，按约定仅单次发布差异并引用；22输出边界、327旧贡献、229 OPEN、所有限制继续保全。独立复审对新精确字节重核这两个阻塞及关联owner接口，旧本报告结论不自动转授新字节。
4. 候选完整门另行协调；通过后唯一登记员整合并冻结精确actual，原独立R-B21另核actual及受影响范围。随后B21 C、原FINAL-1、有证据的登记员关闭/最终SHA、FINAL-2均仍必需。本报告未签actual、B21接受、关闭或FINAL，不触发main合入/整理/同步或后期第三轮review。

报告提交/tree和独立远端读回身份由`publication-readback.json`及最终交接给出；报告提交只新增本目录，差异不包含候选输出或旧证据改动。
