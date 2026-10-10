# B19 repair-2 独立有界 affected 再检

结论：**PASS_SCOPED**。本次仅覆盖全部已接受 B01–B18 的受影响接口及有依据的边界保全；0 个阻塞。旧 `AFFECTED-R07-01` 在本固定 NEW 消除。FULL 作者复审、整合后 actual 复审及正式接受仍各自独立，本报告不代签。

- 仓库：`y805939188/pokemon-essentials-clean-room`。
- 审查 NEW：`7be976f821a49aa22dadec52cf6165c4e1d0887b`；tree `ae9e3e9930fe1cf704b74ddf4b616fce480adc62`。
- 发布及读回包：`537de126c2671368caa26988cd1aebce89ea4de4`；tree `face0a662d2a5b26fc005b3123c260e31ea79d69`。
- 原固定入口：`393ec2680af6e118c1fc959fd0c6290d0cb7c82f:review/remediation/20261003-prepare/batches/B19/author-draft-2/full-candidate-1/publication-1/affected-independent-dispatch.md`。
- 本次入口：`537de126c2671368caa26988cd1aebce89ea4de4:review/remediation/20261003-prepare/batches/B19/author-draft-2/repair-2/complete-candidate-1/publication-1/README.md` 与同目录 `affected-recheck-dispatch.md`、`affected-recheck-navigation.json`。
- 基线 B18 C：`52f24036d09503144c6ec89960029db4ed370734`；tree `3b20f8f2c0dab0ef3e2867aa2bac0fa98497c44b`。
- 上次审查 NEW：`afb97d4dc161594d36b7dcebe35155a206ceb511`；tree `c5075947e57fb1795c12fc35093c45bfe139314f`。
- 参考仅限固定静态文本：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`；tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。
- 写入仅限新分支 `review/b19-affected-repair2-recheck-20261010-1` 的本报告目录；父提交为发布包 P。本目录外不作写入。

完整证据路径、Git blob、SHA256、字节数见 [independent-verification.json](independent-verification.json)；逐 owner 判定见 [owner-judgments.json](owner-judgments.json)，四修复组见 [repair-recheck.json](repair-recheck.json)，实际静态读取及区间哈希见 [source-reading-log.json](source-reading-log.json)。所有证据绑定固定提交。JSON 中的旧报告指针只导航、复用身份和范围，不把旧结论迁移为新签名。

## 独立重建与许可

分别独立重建未过滤的 OLD_NEW→NEW 和 C→NEW 全仓库差异，参数为 `git diff --no-ext-diff --no-color --binary --full-index`，没有路径过滤。前者 30 路径（4M/26A），1,436,191 字节，SHA256 `94e2886ec016df3cdacb09ba883a13f825f740e793cfef1008dbd902cac4eb30`；与 P 中唯一完整差异逐字节一致，该差异路径为 `review/remediation/20261003-prepare/batches/B19/author-draft-2/repair-2/complete-candidate-1/publication-1/full-unfiltered-OLD-NEW-to-repair2-NEW-repository.diff`，blob `893715dd951ce1a3c43b42ebcb8bae052632a053`。C→NEW 90 路径（7M/83A），3,945,512 字节，SHA256 `c1c491920f9d55730619cb50df1548cf718bc1604dfe7184c6341427f91bb257`。完整流仅临时重建核对；本报告不保存或递归复制完整差异、旧报告/控制正文。

repair-2 的载荷实际仅四文件改动：正式 WP72 三行、正式 WP73-A 五行、共享目录四行、WP72 原稿三行。四文件的每个变动区间均重新读；正式/原稿 WP73-B 及原稿 WP73-A 未改。72 输入的前后144个身份、七载荷及固定引用逐一核对。旧24个完整原始/已批准控制对象的先前独立哈希核对仅在其固定文件身份再核对相等后沿用。

原稿许可为 `84cd4bc4c054aa9799532f79f94a237956bacee7:review/remediation/20261003-prepare/batches/B19/original-scope-grant-4/scope-receipt.json`，blob `8577b331e2ece5242607554a7636a9dba5cba46a`，SHA256 `3894a6fe72d808e7406620565a1bdbc6514f5b9781a317fff4265b59e4fc8493`。实际 WP72 原稿整文件与许可 after 逐字节一致，blob `a5b71ae5addc7a098aa17b3144dd0366fe6b2148`，SHA256 `6b50e82e43035f0eeba573a6004bee5a3fb021aaa5c4ee43131f21483a1733a9`，99,280 字节；仅第82/306/338行变化，行数不变，各条 LF-inclusive before/after 哈希吻合，区间外字节保全。许可没有授予 WP73-A/B 原稿新修改；两者均保全。R07 不冒充 C016、没有增加 canonical ID。

## 修复与交叉消费者

R01：参考读取 T001 与官方语言分类共同支持默认救援仅捕获 StandardError/子类。SyntaxError 属 ScriptError，在该范围外；资格前处理也在求值救援之前。非字母首片段获准仍求值完整表达式，不能把资格通过等同完整语法有效。整数除零与无效赋值相邻例只是静态推导，未执行。即时重绘失败发生在原槽已翻转、后续刷新请求未到达之间；未补宿主画面、恢复或进程结局。正式 WP72 第64/288行、目录 DG-M06 第16行与原稿三个许可行一致。[官方救援规则](https://docs.ruby-lang.org/en/3.0/syntax/exceptions_rdoc.html)、[ScriptError 分类](https://docs.ruby-lang.org/en/3.0/ScriptError.html)、[整数除零分类](https://docs.ruby-lang.org/en/3.0/ZeroDivisionError.html)。

R03-includeNew：T005/T006 证明物种列表不加入新建项；正式 WP73-A 第105行保留此必要行为并移除不必要的构造参数。其它选择器身份、取消、排序、保存行为在等字节区间；正确原稿取证未被清洗。

R03-NPC池：T002/T003 证明 NPC 用允许重复且不自动排序的池，训练家资源先取副本。添加已有项追加、改到已有项保留多重项、No返回进入序列，调用方仍赋返回值并可创建对应资源集合；空合法序列仍能打开，仅无NPC才提示。三禁重复池的入口去重、蛋招ID入口排序及名称刷新排序没有被抹掉，No不撤销入口规范化。T007/T008 证明普通消费者取所属训练家资源序列并在消耗条件成立时删一个匹配项；T009 证明内部战斗AI逐项读取该资源。这也覆盖作者导航未列出的 B12/B13；未推断随机选择结果、评分公式改变、自然道具事件或档案/PBS写入。正式 WP72 第225行、WP73-A第66/67/71/138行与 DG-M21/CE-M15 同步。

R07：T004 与目录 WE-M17 第91行逐条件吻合。同值确认保留已有dirty：假保持假、真保持真；只有当前尺寸不同于本次旧尺寸才新增真。ACTION前进独立，BACK恢复旧值并保留先前标记。新会话旧0且只有0时确认后不显示保存询问、正常关闭重载档案；改0→1后确认才新增dirty，退出进入保存门，Yes先档案后按实际集合反写。首缺停止、自有阴影拒绝和媒体/宿主条件保留。旧阻塞定位为 `bcdfba40b8ed1eefadf3a964eec4bc3b7dbc7b3c:review/remediation/20261003-prepare/batches/B19/affected-independent-recheck-20261010-1/repair-recheck.json`，blob `af4b28a8d58bbadbe852ccd49ef390cc30b9a5c0`，SHA256 `3915519fa4e49422a08ce33484ccf281f15bd81ab60c99e194fd08639aee8c73`；解除仅绑定本 NEW。

R02/R04/R05/R06/R08及旧错词修复的有效部分继续按固定源码身份和候选等字节范围复用：当前遭遇快照/登记/版本装配分层；档案/PBS/编译非事务阶段；E088归一显示与完整120参数；容量、HP/PP/特性、天气/Mega/保存和子项取消邻例；EV随机重置、IV/PID门；五主类型槽与独立额外槽；普通PC服务与直接存储分开。旧 source log 的88个记录和 repair-1 的22个记录均重新核对身份，候选改动文件仅复用精确相同的行段并保存旧/新行号、字节数、SHA256。改过的条款以本次读取为准，未把源执行或未读正文视为证据。

## 全部已接受 owner

表中的 PASS 均为本次有界接口判定；每个 owner 的固定旧证据 read ID、当前等字节区间、新静态读取及接受路径保护指针完整列入 JSON。B05/B06/B11 的空作者route没有免审；B18的未受影响结论也给出作用域和消费者理由。

| owner | 既有接受贡献数 | 本次判定 | 依据与条件 |
| --- | ---: | --- | --- |
| B01 | 14 | AFFECTED_INTERFACE_PASS | 登记/档案/PBS/编译与后续布局分层仍成立；NPC序列改动仅战斗资源。R07同值假不置真、既有真保留、改值确认才新增真，保存门已与固定源码相符，解除本接口旧阻塞。旧遭遇零字段及指标后缀条件保持。 |
| B02 | 12 | BOUNDARY_PRESERVED_PASS | 系统输入、随机、时间、语言、统计和存档条文及固定范围未变。R01改变对错误类别的准确表述，未调用或修改这些消费者；NPC池与尺寸dirty也没有改变普通输入返回合同。 |
| B03 | 27 | AFFECTED_INTERFACE_PASS | R01范围外错误发生在原槽翻转与刷新请求之间，事件/地图消费者只能按已到达的请求处理。资格前处理和三ASCII route前缀保持，未补异常恢复；事件变量自然写入、拓扑、tag及共享元数据条件未变。 |
| B04 | 35 | AFFECTED_INTERFACE_PASS | 局部绘制救援与宿主收口明确分开；NPC列表为空/无NPC两门不同；首缺阴影资源、同尺寸dirty及正常关闭保存门已核。通用图像局部失败、消息解析、ASCII/全角、目录缺/空和音乐释放证据保持。解除R07旧阻塞。 |
| B05 | 16 | AFFECTED_INTERFACE_PASS | 改动未改物种/个体自然规则。NPCItem池的资源项允许重复不等于个体持物或普通获取；HP/PP/特性/形态/Shadow调试与自然事件隔离、原字节及等范围证据保持。空作者route不免审。 |
| B06 | 10 | AFFECTED_INTERFACE_PASS | NPC序列副本和空序列入口已核，No仍由战斗调用方赋回，不推动队伍/盒子/包保存。队伍满/全满、图鉴先登记、初始招式和PC服务边界的原字节与已读范围保持。空route不免审。 |
| B07 | 19 | AFFECTED_INTERFACE_PASS | NPC池允许重复与三禁重复池分开，不改培养/自然进化。EV随机重置和252/510与设施255/255/重复分母3的固定条件、取消与重算范围保持。 |
| B08 | 17 | AFFECTED_INTERFACE_PASS | NPC序列写回仅当前战斗训练家资源；EggMoves入口去重/排序仍有共享原地副作用，NPC不执行。当前遭遇快照/登记、同版本早退、异版本有上下文setup、育种/寄存取消及漫游边界保持。 |
| B09 | 20 | AFFECTED_INTERFACE_PASS | 新增NPC条款恢复当前战斗资源重复/顺序和No赋回；消费者取所属训练家数组，消耗一个匹配项。HP/特性双层、五槽独立额外槽、120效果/E088及既有显示布局边界保持；不推广为普通训练家构造事务。 |
| B10 | 7 | AFFECTED_INTERFACE_PASS | NPC多重资源项可被普通战斗消耗路径读取，但调试编辑不直接触发自然道具/回合/天气生产者。新条款没有重定义消耗资格；E088、120参数、五槽/额外槽及自然伤害条件保持。 |
| B11 | 6 | AFFECTED_INTERFACE_PASS | 作者空route仍审NPC资源到道具消费接口：只有普通消耗条件满足才删一个数组项，多重项继续存在；编辑不直接产生技能/特性/道具事件。120参数、模仿/写生持久区别及类型/特性分层证据保持。 |
| B12 | 9 | AFFECTED_INTERFACE_PASS | 独立扩展到NPC池AI消费者：内部战斗门之后逐项读取所属训练家序列，因此允许重复资源会进入候选收集；没有改AI评分公式或加入新重评入口，也不推断概率/并列选择运行结果。既有评分合同原字节和固定范围保持。 |
| B13 | 8 | AFFECTED_INTERFACE_PASS | 设施若消费NPC战斗资源则继承重复项与单项消耗合同；没有新增报名、Palace半HP生产者或录像执行。设施生成255/255、普通252/510、重复技能分母3对应PA040三条全文固定C相同，静态算术保全。 |
| B14 | 24 | AFFECTED_INTERFACE_PASS | R01仅在即时重绘成功后请求地图刷新，失败分支不替世界更新。24时刻RGBA四通道全集、35有序转换及berry67条件均在未改范围；NPC池/dirty不修改世界生产者或补欠项。 |
| B15 | 16 | BOUNDARY_PRESERVED_PASS | 音乐/电话的普通对象合同未改，NPC池/物种列表行为中性化及影子dirty没有新增这些调用。旧18电话逐项条件、缺目录/空目录和正常/异常释放差异按固定未改范围保留。 |
| B16 | 24 | AFFECTED_INTERFACE_PASS | 物种列表无新建项行为保留，构造参数删去不改变选择器身份、取消/排序/键位；NPC池两类重复与No返回/赋回门明确。普通PC服务与直接盒子仍分开，已修错词字节不动；不以子项存在推受限父级可达。 |
| B17 | 12 | AFFECTED_INTERFACE_PASS | 195条记录仅DG-M06/DG-M21/CE-M15/WE-M17四整行增量，191条同字节；旧178ID顺序/重数保留，累计31旧行修订147旧行同字节，17补充行不变。四行均与独立静态消费者核对，WE-M17条件修正消除旧阻塞；PA040三行全文不变。 |
| B18 | 8 | UNAFFECTED_WITH_EVIDENCE_PASS | 三真实目录及Tile原稿与固定C全文同字节；T01空手/格0空、T18合法完成/新确认及三反向记录范围仍精确相同。repair-2入口消费开关/物种选择/战斗道具/阴影指标，未写或调用Tile动作域；共同C003身份不足以改变Tile前提。 |

284 个已接受 scoped contribution receipts 的固定记录整体保全：`52f24036d09503144c6ec89960029db4ed370734:review/remediation/20261003-prepare/batches/B18/acceptance-stage-1/completion-statistics-successor.json`（实际完整路径以 JSON 为准），blob `e7579392696cf24b86f8a35169a2afdb2d739107`，SHA256 `336a267b23b941ab9b14dceab0ceead26d351eb0ae68906cf4b8215d7504cbac`；逐批数为14/12/27/35/16/10/19/17/20/7/6/9/8/24/16/24/12/8。canonical仍229 OPEN/0 CLOSED。

C的36,778个既有路径无删除，只有七个获准载荷修改。共享目录保持旧178个ID顺序/重复结构，现195条；本增量4行修改/191行同字节，累计C→NEW31旧行修订/147旧行同字节，17补充行不变。PA040三行全文等C，保持设施255+255=510、普通252/510及重复技能分母3导致170+170=340的既有区分。正式WP72的120效果行全部等上次NEW，8,674字节，SHA256 `0cb237496cb3708aa709327d4bb830a5516a605c4a710ed19d2975726f2064dd`；83/22/13/2旧逐参数静态证据继续限定其范围。

B18三实际目录 `test-catalog/creature-rpg-wp35-36-57-64-68.md`、`test-catalog/pokemon-rules-wp53-60-61-62-69-70.md`、`test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md`（均在 `deliverables/final-specification-set/` 下）及 `specs/ui/wp71-tile-puzzles.md` 的整文件身份均等固定C；证据详情见JSON，不递归复制旧目录。

## 限制与发布读回

模型请求按已接纳配置有效；不审计额度、后端回参，不改用CLI模型。effective backend仍UNVERIFIED。无新增/嵌套任务，遵守固定author contract的配置；审查人与作者分离。本次仅运行新建Git/JSON/hash/text辅助器，没有运行参考游戏、Ruby、编译器、转换器、生成器、反序列化器、随机/行为向量或历史执行脚本。

素材/宿主/真实执行链未验证，完整owner质量和FULL24/19质量不在本角色；PASS_SCOPED不代签整合后actual或正式C接受。输出清单见 [outputs-manifest.json](outputs-manifest.json)。本目录只含新审查报告和固定身份/哈希元数据，没有旧报告、控制对象正文或完整差异副本。发布使用普通推送，最终回复给出完整提交、tree及独立远端读回结果；提交自身不能内嵌自身hash，远端读回凭据作为该固定提交之后的独立外部验收记录提供。
