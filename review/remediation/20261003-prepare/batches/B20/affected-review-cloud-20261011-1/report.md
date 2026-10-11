# B20 独立 affected 候选复审

结论：**REQUEST_CHANGES_SCOPED_AFFECTED_CANDIDATE，3 个 P2 阻塞**。旧接受记录及目录保留通过；本 NEW 的三个消费者条款/新增案例未满足原 qualified 合同。AF-01–03 是本报告局部证据编号，没有创建 canonical finding，也不撤销任何 B01–B19 已接受贡献。

## 固定对象与入口

| 对象 | commit | tree |
| --- | --- | --- |
| 审查 NEW | `1abaefb1db5818ff9404392143c476979d34c21a` | `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85` |
| B19 基线 C | `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f` | `88a400af08253bea8d97ee2ef2fa6636f0900f92` |
| 候选入口包 E | `9a46a131ba2f7ea82b6eed823aa892cb57b0fba7` | `3397ef849f652c47506b492dabc32c51f5a12c76` |
| 最终读回包 P（报告分支基点） | `272885cca76c36cd04dde27b6be2c654759ec4c2` | `46969272b7387645bc97b91d227734e89a5f8a80` |
| 原完整派发 D | `669997ac28258f26d0bafc81b1d081abb407a3a1` | 固定 commit 下的 B20/refreeze-after-B19-C-1 |
| 固定参考 S | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` | `7589c800b61ba13a13040ed0d686979b80a84fd0` |

入口为 E 的 [`review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/affected.md`](https://github.com/y805939188/pokemon-essentials-clean-room/blob/9a46a131ba2f7ea82b6eed823aa892cb57b0fba7/review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/affected.md)。本报告独立分支 `review/b20-affected-cloud-20261011-1`，只新增本目录。正文、main、参考及旧证据未修改；报告 commit/tree 和远端读回身份由后继 publication 对象外部绑定，不能以自引用或移动 tip 代替固定 NEW。

已读 AGENTS、D 的完整作者合同、19 owner 接口、原合同/控制、目录锁及源限制。原 PLAN 和批准 qualified acceptance 固定于 `41fffb540c6483f5296ea0d33b789b75180d27ed`；完整原 finding 固定于 `93e10babe0b9c9ef8b3f5277754541b447beeeb4`。root/extension 资格、有效 case、前提、最低修订、确定再检及其它 owner/最终全局义务继续绑定。作者的 completion、scope grant、数量和路线声明均仅作导航，未作为质量通过依据。

完整无过滤 C→NEW 流在内存中按无 pathspec、无外部 diff、无 textconv、binary、full-index、no-renames、无 whitespace-ignore 独立重建，与发布件逐字节一致：**42 个路径，1,189,663 bytes，SHA256 `0889ed6d2a4d300325c0fa5d319d9fd89b72bdaeec8e8a0401c7185a25f9eccb`**。唯一引用为 commit `f325f625f879105f7811713d9a38cc58da875de2`，path `review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/stream/C-to-NEW.full.diff`，blob `54c4dcf3be88f175fcceaca5c3642c29c532adfe`。没有再发布差异流或递归复制旧证据正文。七个实际正文/目录的 commit/path/blob/SHA256/bytes 均独立重算匹配，见 [evidence-identities.json](evidence-identities.json) 和 [metadata-verification.json](metadata-verification.json)。

## 三个有界阻塞及最低验收

完整证据身份、数值行范围、静态前提/结果和验收条件见 [findings.json](findings.json)。以下路径均指固定 NEW；旧对照指 C，参考指 S。所有案例 **NOT_EXECUTED**。

**AF-01 / P2 / B05 / C029：形态 getter 漏掉战斗和仓库短路门。** 正式 WP77 第 139 行以及目录 B20-C029 第 278 行，只以 getter 被读取且无 forced 覆盖为前提，给 GIRATINA 的宝珠/DistortionWorld 0/1结果。S 的 `Data/Scripts/014_Pokemon/001_Pokemon.rb:147–152` 先取 forced 值，再在战斗或仓库返回存储形态，随后才调用动态处理器；`001_FormHandlers.rb:267–272` 仅是处理器内的宝珠/地图标记规则。C/NEW 的 `pokemon-rules/wp21-dynamic-forms-and-display.md:246` 明确保留此门，C029 最低修订也要求链接形态主规格求值门。

静态反例：stored=0、forced=nil、宝珠或地图标记成立、in_storage=true，实际 getter 返回存储0；stored=1、无宝珠/标记、in_battle=true，返回存储1。两者都不会进入动态处理器。应将正式 WP77 及新的 C029 静态说明明确绑定 WP21 外层门，并列动态求值、forced、战斗和仓库的邻近对照。原稿 WP77:163 仅审计局部处理器，保持正确，不要求清洗它或重审整个 B05。其它物种/宝珠限定和 Demo 未证保持。

**AF-02 / P2 / B15 / C028：缺资料的空文字与版本0回退被写成底层失败。** 正式 WP77:115、原稿 WP77:139、目录 B20-C028:277 及作者静态说明，将缺训练家/遭遇资料作为底层失败。C/NEW `user-interface/wp63-pokegear-map-music-and-phone.md:145`、S `013_Items/004_Item_Phone.rb:506–531` 与 `010_Data/002_PBS data/013_Encounter.rb:30–35` 分别规定：无训练家记录返回空文字；遭遇请求版本缺失先回退0；两版都缺或 Land/Cave/Water 三表均空也为空文字。数据存在但队伍空、非法参数或非法物种是不同前提，仍不承诺同等保护。C028 最低修订明确缺失回退由 WP63 承接。

应在两份 WP77、本案例及其新后继静态说明中保留这四种缺资料对照，区别未保护异常。每通只取一次 TP/TE、max(current,start)、联系人队伍和地图、成员次数不去重、首最多4槽均匀及 Land→Cave→Water 保持；不能改成普通野生遭遇权重。保持旧 WP63/PL16/PL17、参考和其它旧目录行，不要求所有输入成功或提供非空替代文本。

**AF-03 / P2 / B04、B19（关联 B06 coins 数据）/ C003：新增 CN 预期错误。** 目录 B20-C003:270 和 `author-draft-1/per-ID-remediation-and-static-cases.json:32` 写“CN金银铜钱”。S `007_Objects and windows/011_Messages.rb:330–343/584–592` 的 cn 分支显示玩家 coins 的代币窗，g 分支独立显示金钱；没有金/银/铜分档。C/NEW WP17:47 和旧 CV-M14:157 均正确描述 CN 代币窗。新增案例与同目录已接受条款相冲突。

应仅修新增 B20-C003 及同一预期的新后继说明为 CN 代币窗/玩家 coins，准确区分 G 金钱窗。保持旧 CV-M14、17 个 B19 行、3 个 PA040 行、旧195 ID顺序和重数，以及 .midi/.mid、CommonEvent 和 ASCII 的正确边界。B06 的代币字段旧规则没有因此重新开放；阻塞属于这个新增格式码消费者预期。

三个问题分别由实际 getter、缺资料回退和格式码读者支持，不是增加新范围、重开旧接受或把静态例当运行测试。每项修复须在新的固定候选身份上核对正文/目录/静态说明一致，普通发布并独立读回；旧冻结证据仍按固定身份引用。本报告未要求递归证明阅读历史链。

## B01–B19 实际影响范围

每行“保留”只针对所述支持接口；旧资格继续原范围，均不签整包质量。贡献/主责数字来自原 PLAN 和固定 C receipts 的独立重建。详细路径、源调用条件、状态及正常/反向证据见四份 owner 子报告与对应 JSON。

| owner | 旧贡献/主责 | 实际支持的影响范围和本门判定 |
| --- | --- | --- |
| B01 | 14/7 | WP75编译流程、WP74映射写回和共享目录 reverse reader；编译顺序/部分写回不改PBS新鲜度、配置/插件与持久失败资格，范围保留。 |
| B02 | 12/9 | WP74目录进入先于窗口、空表/具名文件占位及正常清理，WP75兼容文本与原PLAN读取交界；目录传播与文件捕获分开，旧接口保留。 |
| B03 | 27/19 | WP75 门外层识别、开关22先行副作用/结构门、WP11转移、WP13位置快照/累计路线/through/210等待/持久可见性；脚本先求值再看准确行首前缀、页末优先且全条件合取。相关正文与真实消费者支持保留。 |
| B04 | 35/23 | WP15/17 局部保护、目录枚举与文件加载、正常释放/屏幕/BGM恢复、消息格式码；异常无统一兜底保证。旧资格保留；新增 CN 消费者 AF-03 阻塞。 |
| B05 | 16/10 | 派发无直接声明路线，实际 WP77→GIRATINA getter→WP21 求值门必须纳入；只限本消费者，AF-01 阻塞，旧形态主规格与接受保持。 |
| B06 | 10/7 | 派发无直接声明路线，实际 CN→WP24 coins 数据字段及WP77→完整party数学输入须纳入；35旧文本转换只是词法产物，不重定义库存/金钱/代币运行门或WP25容量。旧资格保持；新增 CN 预期归 AF-03。 |
| B07 | 19/12 | 成长公共动画、经验先提交/逐级取整和道具消耗交界；演出名命中不推出经验、库存或进化成功，接口保留。 |
| B08 | 17/9 | WP77→WP36唯一平衡等级数学→地图缩放；蛋/濒死参与、人口标准差、权重截限/归一/舍入/加2/上下限保持。电话遭遇资料不冒充当前快照/实际遇敌，数学及旧遭遇责任保留。 |
| B09 | 20/13 | WP74真实战斗演出；另补 WP75六族输出→WP39创建规则的实际接口。outcome/cannotRun/canLose等位置及副作用与战斗内条款分开，旧责任保留。 |
| B10 | 7/2 | 每击动画、槽号/偏移与真实伤害、HP提交/吸取反伤先后交界；动画帧或不透明度不作为HP，接口保留。 |
| B11 | 6/3 | 派发无直接声明路线，实际 WP47-A 动态类型/环境借用/Ghost分支→动画映射/偏移，须追加有界间接影响；目标/PP/能力持物与未决不被演出改写，接口保留。 |
| B12 | 9/6 | 实际AI效果查询/评分绑定与动画数据命名的责任边界；演出存在不证明AI完整、纯查询或数值成功，旧资格保留。 |
| B13 | 8/5 | 动画独立复制/Insert联动、呈现与录制/回放；不把编辑器快照当作记录字段格式，不重定义参赛/还原/替补，接口保留。 |
| B14 | 24/19 | 治疗精确词法→Recover All→WP61成员集合/存储设置；少删1/单命令持续插入保留，不声称与旧仅队伍循环等价。中心识别≠构造，世界状态/回程失败边界保留。 |
| B15 | 16/10 | 电话五标记/联系人版本/地图资料与CommonEvent登记的实际交界；图鉴/邮件/礼物旧范围保持，电话缺资料回退 AF-02 阻塞。 |
| B16 | 24/20 | 编辑器屏幕倍率、有效缓存/临时集合/首槽空、正常生命周期与未证宿主恢复；不重定义摘要/BoxLink索引/物品消费，接口保留。 |
| B17 | 12/7 | 补入实际 WP67-A播放reader，核ASCII Move/OppMove及Common直接拼接、首匹配/回退/缓存/槽号重编译；生命周期取消/提交、WP76入口限制及PA040保留。 |
| B18 | 8/5 | WP74局部素材条件与WP77玩法证据reader；卡牌/老虎机/挖矿/拼图仍用自身状态/资源/完成门，Game Corner不证明可玩，三只读目录及旧玩法义务保留。 |
| B19 | 24/19 | 实际六输入、120效果完整数据、编辑取消/PBS反写/缓存、世界快照、资源先复制、CommonEvent可达块、ASCII映射/战斗lookup；旧资格保持，新增 CN 案例 AF-03 阻塞。 |

影响范围依据实际消费者补全了派发导航：B05 getter、B06 coins、B11间接播放、B09创建规则，以及 B17 的 WP67-A reader。“无直接声明路线”和文件无交集没有被当作未受影响证据。涉及未变化领域的结论同时由旧条款字节保留、实际消费条件和不越接口的边界支持。

B19 相对 B18 真正变化的六输入已逐项消费：正式 WP72、73-A、73-B、共享目录及原稿 WP72、73-A。C→NEW 中前述五份正文逐字相同；120效果及各范围/默认/哨兵仍完整。`.midi` 在音乐列表 glob 可列，而动画批量导入以末3字符筛选不命中；`.mid`、合格图/音资源可在坏 `.anm` 校验前复制。入口短句“.midi先复制资源”不精确，本复审按真实源/正确正文澄清，不用它改写旧资格。CommonEvent只有满足真实收集/每块首解析支/Battle等门的块可达；保存、换序、重编译与已存在缓存失效分别判断，没有即刻全消费者同步保证。

## 308 贡献与整个目录保留

从原 PLAN前19 owner及 C receipts 重建 **308 个(owner,ID)、205主责、216触及ID**；每条 receipt 对固定派发的对应owner全字段相同。历史统计和派发仅分组次序不同，C记录没有被重排。完整 qualified 原对象/批准对象引用及哈希保持，**2,757 个旧owner证据文件 blob 不变**。这些是静态保留证据，不重跑/重签过去 actual 门。

共享目录完整 C/NEW 核验：原 **195 ID次序及重复次数全保留；193旧行逐字相同；仅同位置126 AN-M23和161 CV-M18修订；末尾追加19项，总214**。原261行除这两行全部相同，17个B19行和3个PA040行原样。AN-M23保留20fps/恢复/对方侧/静音/可见标志，渐变定位到WP74§10.2a；CV-M18保留旧a–e结果并改指WP75§8.1。旧链接与新增章节定位有效。见 [b20-preservation.md](b20-preservation.md) 和 [b20-preservation.json](b20-preservation.json)。新增行的正确性仍由本报告三个阻塞及 FULL 门分别判断。

源只在独立静态副本 S 阅读相关文本；未修改 tracked reference。仅运行自己新写的 Git/JSON/hash/text 元数据核验，未执行参考游戏、Ruby、编译器、转换器、反序列化器、行为向量或旧执行脚本。静态案例不是运行测试。U01–U10/G01–G12/AX01–AX20及既有 unread/conditional/插件/宿主/媒体/数据/非局部限制保留；运行观察和已证明Demo事件链均0。

本输出只作上述 NEW/tree 的 affected candidate 判定，不签 FULL19/15、actual、正式接受、canonical关闭或合main。三个有限缺口修复并由本门独立核验后，仍须另一路 FULL candidate，以及 sole registrar 唯一G固定ACT后原独立两路 actual 门和准确发布读回，才具备正式接受条件。本次没有输入、工具或发布权限方面的已知剩余阻塞；剩余的是 AF-01–03 的质量缺口。

## 支持文件

- [B01–B06实际消费者](b20-owners-b01-b06.md) / [身份与逐owner判断](b20-owners-b01-b06.json)
- [B07–B12实际消费者](b20-owners-b07-b12.md) / [身份与逐owner判断](b20-owners-b07-b12.json)
- [B13–B18实际消费者](b20-owners-b13-b18.md) / [身份与逐owner判断](b20-owners-b13-b18.json)
- [B19六输入与真实逆向reader](b20-owner-b19.md) / [身份与24项保留判断](b20-owner-b19.json)
- [证据身份](evidence-identities.json)、[完整差异重建与写入边界](metadata-verification.json)、[三个问题与验收](findings.json)、[输出清单](output-manifest.json)

报告文件内不预填自身 commit/tree；发布后由 `publication/report-readback.json` 绑定报告提交，最终包由第二次独立远端读回及最终回复给出准确 commit/tree。
