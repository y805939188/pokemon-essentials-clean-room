# R6-U13-R repair-01 recording-save 补充复审

冻结修订 `9971fe84896786645cdcda3ab45e5caf7785cabc`、tree `93ebe95d038954fd0dfb14fd07ac2f95a2485baf`：**GR6-F-S001 七组限定源静态 PASS；GR6-F-V005 同源、同合同、同镜像身份接合后保持限定源静态 PASS。** 新 SF30 d/e 补回旧正确控制，原唯一语义缺口已经修复。本意见不签配置合格 CANDIDATE_PASS、INTEGRATED_PASS、正式接受或 CLOSED。

旧候选 `00b45de642f07cee9953e42f04cce9c35d77346f` 及非作者 FAIL 发布 `3ef4854ef43eac92fd1dc57350e4cf6aa160082b` 保留。旧 S001 FAIL 只绑定旧载荷；新结论只绑定本次冻结修订，不改写旧裁决。本审者 `/root/recording_save` 为原非作者辅助审读者，未参与候选撰写；本轮只写本目录，未切分支、提交、运行作者脚本或启动配置 CLI。

请求为 gpt-6.1-sol / ultra / default tier / default speed；actual model、effort、tier、speed、平台 UUID 均 **UNVERIFIED**。协作公开 metadata 不提供有效配置回显，不能把请求、逻辑任务名或静态辅助意见写成配置符合。WP66-A 实际接收、唯一整合者共享全文复核及正式接受仍是后续门。

## 阅读和绑定范围

原报告已完成 AGENTS、prompt 通用要求、两个责任 ID 全七组、完整原提案、原证据/反证、必要生产消费链及相交历史资格的语义审读。该旧报告和账本作为同一审者、同一不可变源的资格，不将其全文阅读冒称本轮新增阅读。固定 R 仍为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；固定 formal 仍为 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`。合同 R6-U13.json 与旧候选完整字节相等。

本轮新增实读为新 pokemon 测试目录 1–51（完整 SF 表）、WP53 234–249（完整保存/持久单元）、固定 formal 测试目录 37–43（含原 SF30）、新 repair-01/report.md 1–26、conversion-controls.json 1–49、checks.json 1–170、r5-path-recovery.json 1–97、delta-manifest.json 1–215，以及 remote-readback.json 全部结构字段和值。报告/账本严格分开新增语义阅读、元数据差异阅读、有限文档检查和旧同源资格绑定；没有重新全审不变目录或全部历史。

`reading-ledger.jsonl` 记录实际新呈现范围及 commit/path、bytes、SHA256、blob、argv/cwd/UTC/exit。`metadata-reading-attestation.json` 记录已完整审读的相关 metadata 改动 hunks，以及 tool-validation 的完整紧凑结构阅读；未单独捕获的早期呈现 UTC 不重建。作者脚本只读相关差异，不声称本审者完整审读或执行全部作者程序。`metadata-diff.patch` 和 `mirror-diff.patch` 保留冻结差集。

自有 `check_delta.py` 是有限文档/身份检查，exit0 收据为 `execution-receipt.json` 与 stdout/stderr；它不证明语义正确。独立核得八份镜像只有 pokemon 测试物理第40行不同，其他273行及 BP 起全部非 SF 后缀字节相等，七份其它镜像完全相等；原 SF30 a/b/c 输入、预期前缀相等。先保留原始行序列再计数，SF 原始40/唯一40、SF01–SF40 无重复。QC49/WS36/PA32/RC29 的新作者原始计数字段与边界层次已核，未借建字典后的数量证明原始唯一性。

## GR6-F-S001：PASS_LIMITED_SOURCE_STATIC

| 七组 | 绑定新候选的判断与证据 |
| --- | --- |
| identity_and_verdict | PASS。canonical S001、聚合 F-009、required/P2、原提案身份与合同均未变化；SF30 d/e 是同根因的正确控制恢复，未新增 ID。旧候选 FAIL 留存，新裁决没有转写原历史裁决。 |
| bidirectional_evidence | PASS。旧实读固定链 MenuHandlers101–116、PauseMenu254–272/304–321、UI_Save100–128、Game.save111–125、SaveData57–61、SaveValue48–52/279–283、SaveValues3–8/76–81，仍反向对应不变 WP53 239–248 及新 SF30/SF36–40。新读取 WP53 234–249 与 SF 表确认普通 Quit Game 无专门 Save 的模式门，两会话对象仍整体持久，正常结束/转换控制已重新具名承接。 |
| premises_and_counterexample | PASS。新 SF30 d 明定两会话正常结束、常规持久值及保存/普通载入依赖有效、无其它状态改写；期望会话未开始/已结束态及模式统计持久，计时起点等运行时刻值重载语义仍未知。不是对真实保存/载入的执行断言。e 限定固定参考当前默认转换集合与注册者，排除插件/动态追加；最强反证“所有存档均无迁移”被明确排除。活动 Safari/未到期捕虫及正常交互依赖等旧反例前提继续由 SF36/37、WP53 241 保留。 |
| minimum_revision_contract | PASS。新测试第40行保留旧候选菜单集合完整前缀，另追加 d/e，恢复 fixed formal 第40行旧 b 正常结束保存→载入和旧 c 无专用模式转换。未恢复“活动中都不能保存”，未把 serializer 可达提升成磁盘/时钟实测，也未扩大为任意版本/插件无迁移。新镜像仅这一物理行变化，是原 FAIL 的最小修订；不再需要候选修订。 |
| acceptance_and_regression | PASS。完整新 SF1–40 已读，SF36–40 第46–50行保留活动对象可达、拒退出、拒保存/覆盖、捕获 IO 与未捕获异常的具体前缀/尾部边界；SF30 d/e 第40行恢复独立正常/转换对照。原 SF35 及全部非 SF 后缀完全不变，未因保存时单员队伍推导捕虫战斗接管。SF总数仍40；有限 presence 检查仅证明文本/数量，语义保全由本次独立对照判断。 |
| independent_adjudication | PASS。本审者反向尝试新 d 把时间值说成可恢复、e 把全版本或整个存档说成无转换、修复把专门 Save 门扩成普通 Quit Game 门、或只是关键词出现而未保旧正常语义：完整前提/预期/未知边界及不变正文均否定这些反例。作者工具/报告和旧 PASS 不代替这一新裁决。配置合格验收仍 UNVERIFIED。 |
| dependencies_and_receivers | PASS（接口限定；实际整合另验）。唯一主批 U13、WP53 与 pokemon 目录接收者不变。旧 WP09 保存前缀、WP65 正常返回退出/四组合、WP17 消息期间更新/到期前提的已读同源接点继续适用；WP66-A 的人数/读取值焦点接口是 R6-I 唯一整合者后置接收责任，本辅助不越权修改或签其实际整合通过。 |

新 SF30 d 合法正常控制并不与活动保存可达性相斥：它只在两个会话已正常结束、常规对象图及依赖有效时检查原正常行为；活动对象可保存仍在原 a/b/c、SF36/37 和 WP53 246–247 中。新 SF30 e 的源资格由本审者旧冻结账本完整 Conversion1–223、SaveConversions1–420 绑定：Conversion 的版本选择/登记/执行（51–65/158–209）不专门转换模式字段；默认十四个注册处理树果、跟随者、寄养、背包、玩家编号、图鉴、选项、天气、统计、标记、电话、笛子、碰撞统计。旧固定全域 register_conversion 查询及保存五单元模式名有界负查询与完整两单位语义阅读合用，仅支持当前默认集合无专用模式格式迁移，不能推出插件/动态追加、任意历史版本或旧对象图加载都成功。

`delta-checks.json/source_qualification_binding` 已重新核两源完整旧范围与当前固定字节相同：Conversion bytes7964、SHA `52cd055e408386f1764051eb6e86b1245ed6bd7a294f5acbae00973453606bfb`、blob `bd5f42d50e12536c4c5267dd30e4d77751f612f5`；SaveConversions bytes13988、SHA `ff162d13c4f40a9f3332569fc2c4956ea4c7bcd549691f6f0a743f0c4dc1be60`、blob `63e10203bd2553f01925a13f4ad4c45f8e29b36c`。这是明确获授权的同源资格复用，不是本轮新完整源阅读。

拒绝/失败/异常界限仍依旧固定链：拒绝退出只刷新重开，不调用保存；接受退出后拒 Save，或满足异存档警告门时拒覆盖，保存正常返回 false，Quit Game 忽略该值仍走场景置空。正常持久前缀先有 safesave/计数/magic/最近保存时刻，再取值/校验/写档；捕获 IO/SystemCallError 只回滚保存计数，其它前缀不回滚。未捕获取值类型等异常不保证画面清理或退出尾部，参数校验在前缀前，不能与取值校验合并。新 SF38–40 与 WP53 241–242 不变；消息正常返回、无无关更新/到期回调仍是有效前提，未承诺冻结时钟。

## GR6-F-V005：保持 PASS_LIMITED_SOURCE_STATIC

新旧 WP56 与 combat 目录字节完全相等，责任合同与固定 Palace/ActionSwitching 源不变。本轮由身份与差集核接合原全七组审读，不声称新全文重读或运行换人程序。

| 七组 | 不变资格与本轮接合 |
| --- | --- |
| identity_and_verdict | PASS。V005/F-008 身份及 required/P2 不变，同合同完整字节已核。 |
| bidirectional_evidence | PASS。旧固定 Palace184–243、ActionSwitching9–33/77–105 的完整上下文继续绑定 WP56 78–80、combat PA-P32第141行，不变身份已核。 |
| premises_and_counterexample | PASS。合法存活1/205整数百分比0不严格增大初值0而建 best；h24、无提前分支/状态修正/旧标记等合法前提和 r0 后段写标记再登记的反例不变。3/205整数1的相邻对照通过最佳早返保留标记，实际HP>0与整数0%未混淆。 |
| minimum_revision_contract | PASS。严格增大0才建候选、正同值留先者和早返/后段差异均未改动；无需修订。 |
| acceptance_and_regression | PASS。PA-P32 a–d、P12/P24/P25 的已读边界与概率门全文不变。因子30是静态规则推导预期，文档工具只检查整数除法及给定常量比较，不能声称工具独立证明概率语义。 |
| independent_adjudication | PASS。原非作者对0%等于倒下、0数学最大也必建best、相同概率必有相同标记的反证仍由同一不变条件/严格门/早返位置否定。本轮未借工具修正引入新的源行为结论。 |
| dependencies_and_receivers | PASS（限定接口）。U13唯一责任、WP56/combat接收者不变，root共享实际整合及历史限定另验；当前意见不覆盖未来修改。 |

精确身份：WP56 bytes19053、SHA `fee7a028ad9b1db8fae48145b092b18efc89757db943eb6e3f234ace7c111368`、blob `0ff4bc7581fa77266d28ed2477c9dd68ed1edde5`；combat 目录 bytes33561、SHA `e6336cc59798b5f02dfe92c0e799344a3aa652627b2adfacbe6861562537f1c8`、blob `cc28e3400d3bab787ce66c18156c45bcba6e5829`。

## 元数据更正和剩余边界

新修订明确撤回作者原“先建字典即可核原始唯一性”和“略过 SF30整行即证明正确控制保全”的过强证明。本审者有限核亦先保原始 ID 序列并精确对照所有非40行；语义控制恢复由上述七组判断支持。纠正本人旧报告的工具表述：旧工具未独立计算概率因子30，只核1/205→0、3/205→1及传入预期30的比较；因子依据来自旧源全文静态推导。新作者 tool-validation 分列 `expected_constants_not_computed`、`probability_factor_semantics_proved=false`，限定正确；这一证据层次更正不改变 V005 源结论。

R5 修复是路径恢复与记录更正：三个原 `qualified_scope` 投影完整相等；当前固定 f49d commit/path 与原 blob、bytes/SHA 全等。作者初期失败原因未记录，保持 UNKNOWN_NOT_RECONSTRUCTED；错误的路径不存在推断已撤回，不重建原失败 UTC、不改原资格。不要把这次 R5 metadata 纠正和本审者旧 core 对象缺失失败混为同一事件；旧 core 失败/撤回/精确恢复收据仍在旧审查中。

修订 delta-manifest 的16项前后载荷身份均核相等于实际冻结字节；它明示不包含自身。另有发布证据 remote-readback.json：本审者完整读其字段，不替作者签远端成功；本地核77dc→9971只新增该收据。它绑定77dc时语义候选及后继证据提交的层次，不是 S001 独立语义验收或运行证明。整个旧候选→新候选差集因此是17个 evidence 载荷（含 delta-manifest/发布收据）及一个镜像行修复，未把16项清单冒称覆盖所有文件。

新受影响目录身份：pokemon 测试 bytes61919、SHA `ca5801868b2861784e9cbf56c07a542d4a2b1d10f9b92c58f77f90028c310181`、blob `4f652cc1ae09ae4bc655c22325d2ef8c20013004`；WP53 bytes51237、SHA `1a9c9581d7b91bf5e4dd5474b9e2f4fef4115e795d7122663eb743e55bfaa999`、blob `5acc4f03fcecd49001325ff218034f00aff8a20a`。

本轮记录/播放接口没有载荷变更：WP58、RC目录以及固定 RecordedBattle/Challenge_Battles 同源资格继续适用。旧源121–125/198–222四席命令记录及玩家侧一次消费、Challenge40–105临时/全局记录清除和异常前缀界限不被 SF30 修复改变；不会因为身份检查自动外推未执行完整播放。其相交历史 R2 B13/B029、B018及B12/B026的旧限定资格接点保持；本轮未新增全部历史语义通过声明。

剩余条件为实际配置障碍的准确处理、R6-I 唯一整合接收（含 WP66-A）、实际组成全文及接口/精确历史复验、正式接受与 CLOSED 分层记录。参考程序、作者脚本、serializer/行为模型、fake/isolated writer、真实保存/载入、宿主窗口/进程、地图可达性、媒体/Demo执行均为0；重载时钟及未绑定插件组合继续未知。当前无需再修 S001；这些后续条件不应被写成已经完成。
