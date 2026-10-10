# B19 独立 affected 精确 actual 复审

结论：**PASS_SCOPED**，0阻塞。18份有依据的actual判定覆盖全部已接受B01–B18，绑定 `a022325260df386cb8d8033314c8464be6edc2e7` / tree `8d82cd04b4925b874a16167e3779666b18adda87`；旧284项接受贡献保全。`AFFECTED-R07-01` 在此ACT保持消除。这是有界affected actual门；不签FULL24/19 actual、B19 C接受或canonical关闭。

## 固定对象与入口

- 仓库：`y805939188/pokemon-essentials-clean-room`。
- 唯一G/受审ACT：`a022325260df386cb8d8033314c8464be6edc2e7`，tree `8d82cd04b4925b874a16167e3779666b18adda87`。
- 派发包：`5aa266f06baaaa081ce3b76d5cb4b68cf9765339`，tree `bcdcd1cdb3d0b6706824306d99db48bd8f0b4d8a`。
- 固定入口：`5aa266f06baaaa081ce3b76d5cb4b68cf9765339:review/remediation/20261003-prepare/batches/B19/actual-freeze-1/affected-actual-dispatch.md`；精确合同和18个owner字段要求见同目录 `affected-actual-dispatch.json`。
- 正式before B18 C：`52f24036d09503144c6ec89960029db4ed370734`，tree `3b20f8f2c0dab0ef3e2867aa2bac0fa98497c44b`。
- 已审NEW：`7be976f821a49aa22dadec52cf6165c4e1d0887b`，tree `ae9e3e9930fe1cf704b74ddf4b616fce480adc62`。
- 候选affected证据提交：`41ac86d11a11fb33b3ca95ac3e3683a5f3221e0c`；其结论只适用于NEW，本轮不迁移签名。
- 原合同：`a022325260df386cb8d8033314c8464be6edc2e7:review/remediation/20261003-prepare/batches/B19/refreeze-after-B18-C-1/author-contract.json`，blob `c4213c00068fa04e8bfadebf437762163547a494`，SHA256 `cd36fa966985261b0001f878c6a0f531794089fd4c4a8be22fa93d819edc0618`。
- 新报告分支：`review/b19-affected-actual-20261010-1`；父提交为派发包P，仅新增本报告六文件。

[independent-verification.json](independent-verification.json) 保存本轮实际执行检查和固定SHA/路径/blob/SHA256/字节数；[owner-judgments.json](owner-judgments.json) 保存全部18个必需字段和每个owner的公共共享记录；[repair-recheck.json](repair-recheck.json) 保存ACT修复接口判定；[source-and-nonexecution-limits.json](source-and-nonexecution-limits.json) 明确证据沿用、未读及未执行限制。旧证据正文、控制正文及完整差异均未复制进本报告。

## 两份完整差异

独立重建 `git diff --no-ext-diff --no-color --binary --full-index <C或NEW> ACT`；没有路径过滤，完整name-status也独立核对。两份流各与派发包唯一已发布文件逐字节一致，仅临时重建，不另保存。

| 端点 | 字节 | SHA256 | 发布blob |
| --- | ---: | --- | --- |
| 52f24036d09503144c6ec89960029db4ed370734 → ACT | 2,054,730 | `8078a7edf68f6725ff958974522ffd8227dd2656c7d05103acd2a424f7fcf494` | `475be5d9c176c27779c4d39a313c0989b91771ac` |
| 7be976f821a49aa22dadec52cf6165c4e1d0887b → ACT | 5,065,998 | `09ee427d3a733995f068cf6f89081c0e4e3d0d24ebdbe69a197fab9abbc0eaf4` | `41ade954dd9ab6bf0d30b0f8c7eb9bc3a6433051` |

固定路径分别为 `5aa266f06baaaa081ce3b76d5cb4b68cf9765339:review/remediation/20261003-prepare/batches/B19/actual-freeze-1/complete-C-to-ACT.diff` 和同目录 `complete-NEW-to-ACT.diff`，全部参数和完整路径清单另见固定 `diff-manifest.json`。

C→ACT有61条name-status（10M/51A）：仅七份获准规格载荷、三个公共文件修改，其余为管理材料新增。C既有36,778路径无删除、其它路径全部同字节。NEW→ACT有135条name-status（3M/81D/49A/R065/R059各1）；物理树比较是3修改/83删除/51新增。两条R是Git相似度配对，不是规格迁移。83个删除全在作者证据目录，原发布NEW/作者包仍保有不可变证据；ACT引用这些固定发布。没有规格删除/变化，也没有未验收B20/B21正文加入。

72个输入的候选/实际144身份逐一核对（70个当前ACT、2个不可变控制）；七载荷均全文等NEW。原稿三份最终状态与四轮许可逐次衔接，正式正文和目录身份也等已审NEW。13个已实际静态读取记录的整文件与所有区间SHA256在ACT/固定参考再核相同；88/22旧等范围证据沿用固定候选验证记录。身份检查不冒充新语义读取，未重复整库阅读。

## 四轮原稿许可及保全

四轮固定receipt提交依次为 `d91452fa69d5d18885b254c4a76454deee0d41ef`、`4ceec8e78604d13bcf884b013300e1beb3e200d0`、`d90043962356c3d960daf1a2bc21a7f84086c66b`、`84cd4bc4c054aa9799532f79f94a237956bacee7`，对应 `review/remediation/20261003-prepare/batches/B19/original-scope-grant-1/` 至 `original-scope-grant-4/scope-receipt.json`。本轮重新核对每个固定before、许可完整patch、完整after和已应用作者版本；用新建纯文本检查器核对每个hunk的上下文/位置/计数并重建全文，不运行历史脚本。

四轮7次应用的hunk数分别6；10/9；4/1/1；3，所有整文件重建吻合完整after，下一轮before等上一轮状态，最终三原稿与ACT/NEW逐字节一致。只应用许可固定patch，没有另授correct-original 003架构清洗或R07原稿改动；R07仍独立补充，未成为C016或新canonical。所有identity、hunk元数据、固定哈希详见JSON `/original_scope_chain` 与 `/final_original_checks`。

## 实际G/public登记与贡献边界

本轮直接解析ACT三个公共文件及G的24记录，对原字节和新增记录另作判断：`approval-ledger.tsv`、`traceability-successor.tsv` 均完整保留C的284行原字节/内容并只追加24行至308行；`final-integration-review.md`也完整保留C原字节前缀，仅追加G说明。新增记录的19主责/5共享、ID顺序和各自完整原始/已批准对象的独立规范JSON哈希全部核对。完整qualified field指针、当前限定控制和有效case aggregate所在固定overlay身份相同。

每条公共remaining obligations的all/accepted/remaining贡献者集合均与G及完整限定控制一致，集合互斥并完整；旧accepted contributors未被清掉，也未把B19加入accepted。公共ACT自SHA占位符由派发包 `5aa266f06baaaa081ce3b76d5cb4b68cf9765339:review/remediation/20261003-prepare/batches/B19/actual-freeze-1/public-registration-actual-binding.json` 外部精确绑定到A：24个G JSON指针均解出实际记录，actual规格、条文区间和目录行哈希逐一核对；未借占位符绑定导航提交。

所有24记录仍 `PENDING` actual/C；candidate PASS只是具名候选签名，ACT记录没有预置actual receipts、B19接受数为0、canonical均OPEN、final closure假。19主责的actual minima仍待FULL复审；有限非局部贡献与下游B20/B21门继续保留。本角色核登记保护与受影响接口，不替FULL逐项质量门或registrar正式接受。

旧接受统计整体字节等C：`52f24036d09503144c6ec89960029db4ed370734:review/remediation/20261003-prepare/batches/B18/acceptance-stage-1/completion-statistics-successor.json`，blob `e7579392696cf24b86f8a35169a2afdb2d739107`，SHA256 `336a267b23b941ab9b14dceab0ceead26d351eb0ae68906cf4b8215d7504cbac`。B01–B18的接受数仍14/12/27/35/16/10/19/17/20/7/6/9/8/24/16/24/12/8，总284；正式仍18/21，canonical 229OPEN/0CLOSED。

## 18份有依据actual判定

每条的固定候选证据、当前ACT路径保护、实际G/public影响和共享记录指针完整列入owner JSON。受影响消费者的必要条件在下表明示；B02/B15边界和B18未受影响结论也以消费者/作用域为据。空作者route不免除B05/B06/B11审查。

| owner | 旧接受数 | ACT判定范围 | 消费者和限定条件 |
| --- | ---: | --- | --- |
| B01 | 14 | AFFECTED_INTERFACE / PASS_SCOPED | 登记/档案/PBS/编译和后续布局分层；原遭遇零字段、指标后缀及进化重编译条件。ACT中同尺寸确认不新增dirty，既有真保留，真实改值确认才新增真；正常关闭保存门继承固定条件。NPC序列仍仅当前战斗资源。 |
| B02 | 12 | BOUNDARY_PRESERVED / PASS_SCOPED | 系统输入返回、随机、时间、语言、统计及存档接口。ACT表达式救援类别的精确描述不调用这些普通生产者；NPC池/指标dirty没有新增普通输入副作用。 |
| B03 | 27 | AFFECTED_INTERFACE / PASS_SCOPED | 开关原槽写入→即时重绘→地图刷新请求的先后及失败位置；事件变量自然写请求、解释器路由ASCII前缀、拓扑/tag与共享元数据。ACT保留前处理/范围外错误传播，不补异常恢复。 |
| B04 | 35 | AFFECTED_INTERFACE / PASS_SCOPED | 局部绘制救援与宿主收口、NPC空合法序列与无NPC之别、阴影编号首缺停止、自有阴影拒绝、同值dirty和正常关闭保存。消息ASCII/全角、普通图像失效与目录/音乐释放条件仍限定。 |
| B05 | 16 | AFFECTED_INTERFACE / PASS_SCOPED | 物种/个体自然规则和调试HP/PP/特性/形态/Shadow边界。ACT的NPC重复资源项不等于个体持物、普通获取或自然触发，空route没有免除这一消费者判断。 |
| B06 | 10 | AFFECTED_INTERFACE / PASS_SCOPED | 队伍/盒子/包、图鉴先登记、初始招式和普通PC服务。NPC池No返回当前进入序列并由战斗调用方赋回，不推动队伍/包落盘；空道具序列仍可编辑。 |
| B07 | 19 | AFFECTED_INTERFACE / PASS_SCOPED | 普通培养252/510、设施255/255与重复分母3；EV随机重置/取消/重算、自然进化与调试隔离。NPC池允许重复与三禁重复池明确分开，不改变培养门。 |
| B08 | 17 | AFFECTED_INTERFACE / PASS_SCOPED | NPC资源战斗层、EggMoves入口共享去重/ID排序而NPC没有入口规范化；当前遭遇快照与登记、同版本早退和异版本有上下文装配、育种/寄存取消及漫游。 |
| B09 | 20 | AFFECTED_INTERFACE / PASS_SCOPED | ACT中NPC资源保留多重项/顺序和No赋回；所属训练家数组由战斗消费者取得，正常消耗条件满足才删一个匹配项。HP/特性双层、五主槽/独立额外槽、E088/120参数与既有布局不广播边界保持。 |
| B10 | 7 | AFFECTED_INTERFACE / PASS_SCOPED | 自然道具消费/回合/天气/伤害生产者与直接调试赋值隔离。ACT允许多重NPC资源被消费者读取，但编辑本身不触发自然事件；类型与效果参数固定。 |
| B11 | 6 | AFFECTED_INTERFACE / PASS_SCOPED | NPC多重资源到普通道具消耗路径、技能/特性/道具自然事件门，以及模仿/写生持久差异。ACT仅在正常消耗资格满足时移除一个资源项；120参数与类型/特性分层保持。 |
| B12 | 9 | AFFECTED_INTERFACE / PASS_SCOPED | 内部战斗AI逐项读取所属训练家资源序列；重复资源会进入候选收集，ACT未新增评分公式或重评入口。静态读取不推断随机/并列选择运行结果，既有评分门限定仍在。 |
| B13 | 8 | AFFECTED_INTERFACE / PASS_SCOPED | 设施若调用NPC战斗资源则继承重复和单项消耗合同；ACT未新增报名、Palace半HP生产者或录像执行。PA040三条全文等C，255/255、252/510与重复分母3区分保全。 |
| B14 | 24 | AFFECTED_INTERFACE / PASS_SCOPED | 即时重绘成功后才请求地图刷新，与世界更新/时刻生产者分开。ACT保留24时刻RGBA四通道、35有序转换与berry67条件的固定范围，不从局部效果集合推完整世界覆盖。 |
| B15 | 16 | BOUNDARY_PRESERVED / PASS_SCOPED | 音乐/电话正常对象合同及旧18电话条件、缺目录/空目录、正常/异常释放差异。ACT的物种列表、NPC池和影子dirty没有新增这些消费者的调用。 |
| B16 | 24 | AFFECTED_INTERFACE / PASS_SCOPED | 物种列表无新建项、选择器身份/排序/取消/键位、NPC两类池重复和No返回/赋回；普通PC服务与直接存储分开，修复错词保持，不由子项存在推出受限父级可达。 |
| B17 | 12 | AFFECTED_INTERFACE / PASS_SCOPED | 共享目录195条、旧178ID顺序/重数、31旧行修订/147旧行同字节、17补充行不变与PA040全文保全。ACT的四修复行与已核静态消费者同字节，R07同值dirty旧阻塞保持消除。 |
| B18 | 8 | UNAFFECTED_WITH_EVIDENCE / PASS_SCOPED | 三实际目录和Tile原稿全文等C；T01空手/格0空、T18合法完成/新确认及三反向记录仍限定。ACT没有写入或调用Tile动作域；共享C003公共登记保留B18已接受贡献且不把它重新判为待验收。 |

ACT共享目录全文等NEW：195条，旧178ID顺序/重数不丢，31旧行修订/147旧行同字节，17补充行不变；PA040三行全文等C，设施255+255=510、普通252/510、重复技能分母3导致170+170=340的旧区别保持。正式WP72全部120效果行仍8,674字节，SHA256 `0cb237496cb3708aa709327d4bb830a5516a605c4a710ed19d2975726f2064dd`，83/22/13/2逐参数固定证据保留范围。三B18实际目录与 `specs/ui/wp71-tile-puzzles.md` 整文件等C，未因公共共享C003新增待验收记录重开B18已接受切片。

R01表达式类别/前处理/重绘顺序、R03无新物种项与允许重复NPC池、R07同尺寸dirty均在ACT精确等范围并保持固定源码推导条件。R07的USE/ACTION同值保留假或已有真，真实改值确认才新增真；ACTION前进独立、BACK恢复不清先前真。新会话旧0仅0正常退出不询问保存，改0→1确认后才走保存门；实际保存集合决定PBS路径。`AFFECTED-R07-01` 仅在受审ACT绑定下解除。其它R02/R04/R05/R06/R08及PC错词的有效固定证据沿用原条件，未把候选PASS直接转签。

## 未执行与仍独立的门

仅运行新建Git/JSON/hash/text检查器，0次参考游戏/Ruby/编译器/转换器/生成器/反序列化器/历史执行脚本/表达式/随机或行为向量执行。0次运行观测与已证明Demo链。U01–U10、G01–G12、AX01–AX20及具名媒体/宿主/插件/非局部/berry67/metrics样本/备份/杯赛/录像等条件与未读仍保留，绑定固定限度文件；静态/已实施元数据检查与运行证明明确分开。

按已接纳Ultra/default配置工作，effective backend UNVERIFIED；不探额度/回参、不改用CLI模型、不建新/嵌套任务。只有本独立报告目录新增，未编辑正文、原稿、参考、旧证据、公共登记或main。

本报告签affected exact actual全18、0阻塞；FULL24/19 actual仍另属独立复审，正式C接受/合main/canonical关闭均未执行。报告普通推送后从新bare仓库完整读回六输出，固定commit/tree和独立读回凭据在最终回复提供；[outputs-manifest.json](outputs-manifest.json)记录五文件哈希，manifest自身由固定提交及外部读回绑定。
