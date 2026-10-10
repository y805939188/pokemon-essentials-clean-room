# B19 affected 独立有界再审

**结论：BLOCKED_SCOPED；1 项精确阻塞 AFFECTED-R07-01。** 本报告覆盖固定修复候选的 B01–B18 影响接口、修复增量和旧证据沿用边界，不替代 FULL 作者独立复审，不代签整合后 actual 或正式接受。

审查对象 NEW `afb97d4dc161594d36b7dcebe35155a206ceb511`，tree `c5075947e57fb1795c12fc35093c45bfe139314f`。正式基线 C `52f24036d09503144c6ec89960029db4ed370734`，tree `3b20f8f2c0dab0ef3e2867aa2bac0fa98497c44b`；修复前 OLD_NEW `dfe8e726669a83c751d02e923cf290bdafc82bd7`，tree `b830a49ad76369d19ebaae227aaf190ca5542069`。

固定发布 `69f05c26facc42c3a47c4f0d86b16eb8e0711229`，tree `9aabcec9292ebaa574fdc27d0be3bf710a904994`；派发入口 `review/remediation/20261003-prepare/batches/B19/author-draft-2/repair-1/complete-candidate-1/publication-1/README.md`，实际 affected 范围 `review/remediation/20261003-prepare/batches/B19/author-draft-2/repair-1/complete-candidate-1/publication-1/affected-recheck-dispatch.md`（blob `6ee38d665745a24ce633656c60bf3e82ec0a7d68`，SHA-256 `95a45061e5d95ff201d56f9b406de9719fbf8b170defb06094793145d761436a`，4753 bytes）。

报告独立分支 `review/b19-affected-recheck-20261010-1` 以已发布读回证据 `71090724c21f379dede97b3b8f5ca834f916962a`（tree `16b72dd28c5547371e3f8092c9db1b6048d2b571`）为父；只新增此报告目录，原 affected 报告不覆盖。父提交及 author metadata 不构成质量结论。

**阻塞：WE-M17 同值确认的已改标记与退出保存门。**

固定 NEW 的 `deliverables/final-specification-set/test-catalog/demo-dx-wp72-73-74-75-76-77.md` 第91行（WE-M17；blob `2ec999cc9f234dcdee8d9b9e4e5eccd3f5ed2894`，文件 SHA-256 `c3a5e4ee277ff5be9e0fef6738cb32eee083dacd3b6ef12ed9cf20ce5dbcd3bc`，87691 bytes；完整行去行尾 SHA-256 `676b34aa22031033fdd4d8bfc9a94cbe379c25d77fcf7a0110ef235523785d67`）末句无条件要求确认后标已改。

该行自己包含合法旧尺寸0、无自有阴影、通用1不可解析而只有0可选的条件。新会话尚无其它已确认改动时，不改变尺寸而按USE确认：参考保留尺寸0及已改标记假，随后正常退出不进入指标保存询问，只重载档案。当前目录末句会推出标记真并进入保存询问，产生不同的可观察流程。ACTION也只在尺寸不同于本次旧值时设置标记；它的前进是独立结果。

新鲜静态证据：参考 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `Data/Scripts/020_Debug/001_Editor screens/004_EditorScreens_SpritePositioning.rb`，blob `7bca3f9267744af568fb57c091ba6ce43172198f`，SHA-256 `7ef2c7a1d0a1de69608054dc3752306485913d20b4419cecd3e4b3986922b881`，13377 bytes，86–97/176–188/199–217行。固定正式 WP73-B 第127行规定退出保存门依赖已确认指标改动；源初始化、USE/ACTION条件置标记及关闭分支共同支持反例。未执行资源夹具或宿主。

最小修正仅需当前目录行：实际尺寸与本次旧值不同才标已改，同值USE/ACTION保持标记；单列旧0/仅0且无其它已改项时退出不询问保存，并保留改成1后置标记、ACTION前进、BACK恢复的邻例。PBS实际路径仍按既有§7.5集合/后缀规则，不能从进入保存门推成一定写某个文件。此问题影响 B01 指标保存入口、B04 预览/保存交界、B17共享目录；作为 R07 的有界补充，不绑定 C016。完整阻塞和再检方法见 `repair-recheck.json#/blockers/0`。

**独立重建与保护证据。**

- OLD_NEW→修复NEW 完整无路径过滤仓库差异：`git diff --no-ext-diff --no-color --binary --full-index OLD_NEW NEW`，836807 bytes，SHA-256 `840829cfe203bb818f8f553b7c485c849a74884ac5a369bbc5ecbe3ee9934105`，与固定发布唯一完整差异逐字节相同（发布 blob `cbf17ec5ef104a943911f164ecbd99e73e2380b5`）。只引用既有 `publication-1/full-unfiltered-OLD-NEW-to-repair-NEW-repository.diff`，不复制差异正文。37路径=7修改+30新增，无删除。

- C→修复NEW 完整无路径过滤仓库差异独立重建：2566830 bytes，SHA-256 `b3838c64e0aa7014b663059e1b970a071e1ce48f89e293ab93d437da0d554005`，与发布 metadata相同；64路径=7修改+57新增。C的36778既有路径只修改七个既定载荷；其余既有正文、原稿、旧证据保持。

- 72固定声明输入的before/review共144身份、七载荷三版本身份及所有固定 evidence references分别从Git读回核对，无不符；24原合同/批准控制完整对象从原始固定SHA和JSON pointer重新核对对象哈希，无字段裁剪。身份核对不冒充72全文语义复审。

- grant3 `d90043962356c3d960daf1a2bc21a7f84086c66b` / `original-scope-grant-3/scope-receipt.json`（blob `0238d37c27ae887f6de9c5892728cc3fb5ab8073`，SHA-256 `e7e4bb8bc747dd99e57376adc77ee9c0556143bdce12aafda69ba2b449f8e09b`）三份授权complete-after与真实原稿整文件相同，恰7/1/1条完整行改动、含LF的九条before/after哈希均匹配；无额外删除/清理。scope grant只证明写入边界。

- 284 accepted contribution receipts整文件与C相同，B01–B18计数14/12/27/35/16/10/19/17/20/7/6/9/8/24/16/24/12/8合计284。旧178目录ID顺序及重数保持；修复前后均195行，只改九整行、186行相同。累计C→修复NEW有30旧行修订、148旧行相同，17新增补充行保持；不能把身份保护当R05内容保全，五个当前整行另已逐项审查。

- B17三条PA040全文与C相同：设施255/255=510，普通培养252门，重复HP/ATK/ATK分母3后170/170=340；不被debug EV分配替代。B18三真实目录及Tile原稿完整字节与C相同，T01/T18/三反向前提沿用固定已读证据，修复实际接口不进入Tile动作域。

- WP72 E001–E120完整120参数行与OLD_NEW逐字节相同；83成员/22阵营/13全场/2席位逐项参数核对只沿用固定原独立参数证据；E088颜色比较和−2/−1邻例本次重新读取。白名单排除集合、成员空位/濒死显示与RIGHT人工空尾非终止边界没有提升为运行保证。

**修复主题有界结论。**

| 主题 | affected 再审结论 | 核心证据 |
| --- | --- | --- |
| R01 | PASS within affected | 表达式完整资格与前处理局部失败已恢复；同原槽读、常量、刷新标记及全角反例明确。开关与ACTION为写值→页重绘→刷新请求；普通数值/文本USE及左右步进为先写/请求、再调用方重绘。 |
| R02 | PASS within affected | 直接登记查询、新/同版本装配、现有遭遇快照、后续指标预览刷新、下一次布局与已有战斗精灵逐帧显示已分层。保存/No/调试Compile不自动装配；档案/PBS/内存及部分失败边界保留。 |
| R03 | PASS within affected | 源模块签名、类实例分派、结果元组/列号、内部写方法改为可观察类别；三池去重/入口原地规范化/交换方向/蛋招排序/取消门和身份预选仍与源文本一致。LocationFlag的实际数值门、必要外部ID、PC两入口、动画截断等保留。正确原稿只按grant3九条改动，不清理成另一个取证稿。 |
| R04 | PASS within affected | E088登记−2、显示基准−1、编辑范围−1..99与ACTION复位−1分开；当前−2绿色、−1普通颜色。120完整参数行与OLD_NEW逐字节相同，沿用已核46条固定参考文本身份及原逐项120参数证据，不把E088当成员引用。 |
| R05 | PASS within affected | 五条当前完整行恢复了数字夹限/250字、添加与填盒/填包容量、HP/PP/三种特性、天气/期限/Mega/NPC/改时段/空背景文本、六编辑器Yes/No及嵌套写盘。保留新ACTION、Teach、100字、IV/EV显式0与分层保存条件；未恢复旧不准确的全流程无写入/即时三层一致总断言。 |
| R06 | PASS within affected | 战斗/非战斗均先取目标、清六项，再选随机项、满项重选、抽1..floor(S/4)、依次夹剩余目标及单项余量、零增量重试、扣目标至0、重算。默认S252/T510、普通目标0..509/最大510；默认/取消、IV诊断、PID0x加8位大写与低/高16位次序恢复。未执行随机向量。 |
| R07 | BLOCKED：AFFECTED-R07-01 | 编号1起逐增并在首个解析缺口停止的主体修复成立，三组条件资源列表/自有阴影拒绝/BACK恢复成立；新WE-M17末句却遗漏实际尺寸变化的标记门，详见独立阻塞。此补充不绑定或重命名C016。 |
| R08 | PASS within affected | 五个可选主槽、四个空槽的显示与第二空槽添加、取消不写、同值确认清槽及独立额外槽恢复；只写战斗层。固定参考类型查询及同值删除的消费边界沿用，不提升为所有稀疏人工类型状态或运行宿主保证；正确原稿220未改。 |

WP72第72行旧错词已修为取消服务选择返回调试流程，B19-C008第245行相同；普通PC服务与直接整理盒子、受限父级合同保持。

**B01–B18 独立影响判定。**

| owner | receipts | 本次判定 | 独立依据 |
| --- | ---: | --- | --- |
| B01 | 14 | AFFECTED_INTERFACE_BLOCKED | 登记/档案/PBS/编译和指标布局分层修复成立；旧Land0→21、OldRod0→0、Land70、指标后缀/五组等值及正/反进化阶段字节和固定证据保持。WE-M17同值标已改会改变指标保存入口，AFFECTED-R07-01阻塞本接口。 |
| B02 | 12 | BOUNDARY_PRESERVED_PASS | 变量普通数值/文本、ACTION顺序及EV/PID使用边界已重核；不改变系统随机接口、时间、语言、统计或存档契约。已接受条文全部未改，普通/可空输入与宿主边界沿用固定等字节证据。 |
| B03 | 27 | AFFECTED_INTERFACE_PASS | 刷新请求与实际地图刷新分开；开关与ACTION重绘早于请求，不覆盖事件变量写入请求及解释器路由前缀。元数据标量取消、共享嵌套副作用保留；拓扑、tag、事件转换/注释、三个ASCII route前缀均在未改区间，沿用固定读取。 |
| B04 | 35 | AFFECTED_INTERFACE_BLOCKED | 资源编号连续前缀与指标刷新/布局分层已重核；消息解析、ASCII/全角、普通图像与训练家局部救援、缺目录/空目录和音乐释放条件原字节保持。WE-M17同值确认的保存提示推导不成立，AFFECTED-R07-01阻塞共享预览/保存边界。 |
| B05 | 16 | AFFECTED_INTERFACE_PASS | 空作者route不免审：在场HP下限1/最大HP1拒绝、HP写穿、非在场PP只写原、三种特性分层和Teach的Shadow局部门均已重核或固定等字节沿用。EV/IV/PID修改未被推为普通净化、形态或自然触发。 |
| B06 | 10 | AFFECTED_INTERFACE_PASS | 空route仍按实际消费者审查：队伍满/全满/填盒先图鉴后容量、填包0口袋、训练家六保存门和子IV/EV0值已重核。demo固定六物种/初始招式、单角色延后proc局部失败及PC服务/盒子差别均固定未改，不提升为全局默认。 |
| B07 | 19 | AFFECTED_INTERFACE_PASS | EV随机为重置分配而非追加，目标和分配算法/取消/重算已重核；普通培养252/510与设施创建255/255及重复分母3是不同门。战斗调试Teach与普通Shadow拒绝合同原字节保持，不重定义自然升级/进化或培养。 |
| B08 | 17 | AFFECTED_INTERFACE_PASS | 当前遭遇快照vs登记、同版本早退与异版本有上下文setup已重核；原宽限4→0/累积210保持、DayCare选择取消仍写变量而不提交寄存、育种及漫游条款位于等字节区间。 |
| B09 | 20 | AFFECTED_INTERFACE_PASS | HP/特性双层、战斗EV重算同步、五主槽和独立额外槽、E088显示已重核。既有训练家数量2席反例及中途构造非事务边界、Wonder局部显示vs有效查询保持；不保证已布局精灵因指标保存立即移动。 |
| B10 | 7 | AFFECTED_INTERFACE_PASS | E088−2/−1颜色、120参数不变、五槽类型编辑与战斗类型查询已核；天气/期限/Mega邻例明确。Wonder有效查询与原始赋值及自然伤害/回合/天气生产者合同未改，静态诊断不能当触发这些生产者。 |
| B11 | 6 | AFFECTED_INTERFACE_PASS | 空route不免审：120效果白名单各参数与原独立逐项证据一致，E088仍普通整数；战斗主/额外类型与特性直接修改不等于普通技能/特性/道具事件。正常模仿仅战斗、写生持久及消费触发门均未改。 |
| B12 | 9 | BOUNDARY_PRESERVED_PASS | E088修复仅显示基准，五槽修复恢复界面可选数和战斗层写入；类型查询有可能消费新战斗类型，但无新增AI重评或空间评分调用。AI既有基础防/特防及技能评分门保持原字节/固定证据，不替普通AI算法接受签字。 |
| B13 | 8 | BOUNDARY_PRESERVED_PASS | 设施内若用battle-debug会消费同一战斗字段合同，未增加设施报名、Palace半HP生产者或录像执行。120集合及Pinch直接写边界保持；设施255/255和重复170/170三条PA040固定全文与C相同。 |
| B14 | 24 | AFFECTED_INTERFACE_PASS | 地图刷新请求的早晚顺序已重核，与实际地图更新/世界时刻分开；旧24小时RGBA四通道全集、35有序转换、条件berry67没有被120效果数替代。对应已接受字节和固定静态读取保持；条件欠项不转为完成。 |
| B15 | 16 | BOUNDARY_PRESERVED_PASS | 六编辑器保存与列表身份中性化不改变Pokegear音乐/电话的正常对象合同；旧18电话接口逐项条件/缺项/返回和BGM缺目录vs空目录、正常释放vs异常未保证等位于固定等字节区间，继续保留。 |
| B16 | 24 | AFFECTED_INTERFACE_PASS | 普通PC服务与直接盒子源码入口分开，旧正常服务/退出合同原字节保持；WP72第72行错词已改为返回调试流程且B19-C008一致。选择器取消/身份/键位、Teach Shadow边界和普通输入门已重核；不以子项存在推受限父级可达。 |
| B17 | 12 | AFFECTED_INTERFACE_BLOCKED | 旧178 ID顺序/重数和完整195行身份保持；修复九整行、186行等字节；累计C→NEW为30旧行修订/148旧行等字节，17补充行不变。R05五旧行已自足恢复，PA040三行未改；WE-M17却对同值确认给错保存门，AFFECTED-R07-01阻塞共享目录。 |
| B18 | 8 | UNAFFECTED_WITH_EVIDENCE_PASS | 三真实目录及Tile原稿全文与固定C一致，T01空手/格0空、T18合法完成态/新确认和三反向记录的固定证据保持。实际修复是debug页、内容选择器/保存和目录阴影例，没有修改或调用Tile动作域；共同C003身份不足以推翻这些未改前提。 |

B05/B06/B11作者route为空不构成免审；实际共享消费者已纳入上述判定。除共享demo目录外，所有owner既有接受写入路径均与C相同；共享路径的九个新改行、受影响内容与未改旧行分别独立检查。各owner的固定旧读取ID、真实fresh读取和保护metadata pointer见 `owner-judgments.json`，不以作者路由指派代替判断。

**固定证据沿用边界。**

原独立报告 `aee3655d109c2bdb1a5fe221efd4b0a3eda3c758` / `review/remediation/20261003-prepare/batches/B19/affected-independent-review-20261010/report.md`（blob `c49da65d8b7fa777baaa8c41a8473b9cecfc13f5`，SHA-256 `59855b6d9fedb34d665b23a48836b684e69a3e0b929e4ae010f5d46b66b01859`）的 PASS只适用于OLD_NEW。本次不复制或继承该结论。

原 `source-reading-log.json`（blob `d3d4061bcf681ec15b0cda0f497576054b39e0d1`，SHA-256 `3d45055c9dbd85d7609aa389586fa9b28dced68581e456278b2078b6b8355d07`）88条读取身份全部重新核对：46条固定参考文本；30条接受文本全文不变；6条旧候选的有界读取范围不变；另6条旧候选读取范围有修复行，仅沿用明确列出的等字节连续区间， changed lines及其依赖在本次重新审查。每个等字节段的old/new行号、SHA-256与字节数见 `independent-verification.json#/bounded_evidence_reuse`。

B01 PBS/指标/进化、C003相邻前提/取消/别名、副作用；C007旧24时刻/35转换/18电话和条件berry67；C020缺目录/空目录、普通预览与局部救援、正常释放和异常边界；ASCII U+003A/U+005C与全角负例均继续受固定控制和未改段支持。R01/R02/R03/R04/R05/R06/R07/R08的新论断各有本次读取，不把旧固定身份当修复质量证明。

原FULL阻塞记录只用作问题定位：`0fb4acd6ce8532436c016ab939532e30a13a3f07` / `independent-full-review-20261010-1/contribution-review.json`（blob `b17cde491a46f7a361ae03f2aea7a676d3d3198b`，SHA-256 `523fbd801a4a5f34788de32740948e2c1f981734dd52898bac3ad90e0a392aed`），R01–R08 pointers及作者修复说明不预分配本次通过。原稿220的五主槽正确且未改，R07无canonical finding alias。

**方法、输出及剩余门。**

只使用普通Git读取/差异/哈希、JSON/text metadata及新编写的独立辅助脚本；仅本报告目录写入仓库。没有执行参考游戏、Ruby、编译器、转换器、生成器、反序列化器、随机/行为向量或旧执行脚本；runtime observations与proven Demo chains均0。U01–U10/G01–G12/AX01–AX20及原具名未读/条件限度保留；真实媒体、宿主异常收口及运行像素未验证。

请求模型配置被接纳即按Plan A有效使用；effective backend维持UNVERIFIED，无额度、回参、echo或模型后端探测，无CLI/native fallback，无嵌套任务。canonical OPEN229/CLOSED0，284接受记录不变。

交付六文件：本入口 `report.md`、18项 `owner-judgments.json`、精确阻塞/八主题 `repair-recheck.json`、独立身份/全差异/授权/保护/沿用核验 `independent-verification.json`、本次真实有界读取 `source-reading-log.json`、五文件内容身份 `outputs-manifest.json`。manifest自身身份由普通推送后的独立远端全字节读回单独返回，避免自哈希环。

剩余阻塞只有 AFFECTED-R07-01；修正须新固定候选与完整当前行再核。本次没有生成FULL最终质量判定；整合后的实际ACT/tree还需独立FULL与all-owner supported actual门，之后由唯一登记者决定正式接受。
