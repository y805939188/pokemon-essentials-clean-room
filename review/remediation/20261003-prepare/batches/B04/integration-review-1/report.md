# R-B04 实际 integration 独立复核

结论 **PASS_SCOPED**，仅绑定 actual `9e2dadfa650e2111b77f9eae1f834cc00b8805d5`（tree `f642c902b9b256c4cc7e54dcbe7500a29aed0119`）：WP15–17 的35项本批贡献／23项主责、13份正式文件（8最终正文/目录＋5授权原稿必要同步）、10份公共后继与13份管理/冻结证据。未发现新增必修缺陷。C061/C062 两个原P2返修在真实合并后仍成立。

请求 gpt-6.1-sol／Ultra／Standard(default)；工具没有实际配置选择控制或可信回显，模型、推理、服务均 **UNVERIFIED**。按用户已接受方案A完成本轮，不新增确认或配置认证门，不把旧Max收据或历史“可信门”文字当成当前配置证明。作者A-B04/A-REG与本独立R-B04不同；没有派生子任务。

固定接受基线 `6452c0e03025605222f3de9a272221e2b82eeda4`；第二轮已审候选 `50f9ca2506bf0de21c33c644569c9987f84b80a3`，作者完整交接 `5da06e2baf0879978a871c6952fab1105909b511`，独立候选报告 `c500ed089fd1192409c1c77a7a91e093c59a8a45`。第一轮 `f0d89a0989cf16d7ea2592fdf75a968b553caefa` 的 REQUEST_CHANGES 与两个P2对象保持原字节。报告承载分支 `remediation/20261003-prepare/review-B04-integration-1`，父提交是actual；**精确报告commit由普通push及origin SHA回读在最终交付中给出**，不在提交内伪造自引用。

读取 root AGENTS.md、有效净化范围声明与批准合同；未找到可适用的本地SKILL.md或更下层AGENTS。仅新增本目录，不修改正式产物、公共登记、批准计划、既有报告、ignore或参考；不整合接受、不关闭229项、不推main。

## 实际版本、全差分与来源

独立读取真实Git parents/trees：基线先普通merge第二轮报告完整候选，再普通merge第一轮不可变报告，公共登记payload为 `caf7b59c2b80a3d4bf6ad54b1ffb1d4c69bc6262`；actual是payload的单父子，仅A三份完整patch/冻结文件。13正式在候选、作者交接、两次merge、payload和actual均原字节相等。

完整未过滤差分：基线→payload116路径、候选→payload54路径；两patch均按冻结参数重建并逐字节/长度/blob/SHA256比对。基线→actual **119** 路径＝96来源＋10公共修改＋13管理/冻结；候选→actual **57**＝4 freeze-stage-2＋30独立报告＋10公共＋13管理/冻结。payload→actual只A3，正式/公共无末提交暗改。实际原始差分哈希与全部path-status见 [complete-diff-identities.json](complete-diff-identities.json)。

96来源从精确来源commit的目录独立推导：13正式＋53作者/冻结＋30独立报告（R1 14、R2 16）。登记的来源以c500提取82及f0提取14；另向每份最初作者/冻结/独立报告真实commit比对，不把提取commit当最早创作commit。106条 current-hashes 是96来源（其中13 formal）＋10公共的去重分母，与119完整路径分母不同。[input-identity-manifest.json](input-identity-manifest.json)逐份给出actual和源身份。

## 完整35项与两P2

从固定93e原报告、41ff计划验收对象核完整current_qualifications、root裁决、有效case constraints、每条扩展及其他批次责任，未据作者成功摘要裁决。actual完整五份最终正文重新读过；三目录新增114静态行/八旧行及五原稿必要同步按实际正文、差分和候选字节证明复核。同一R-B04前两轮固定源阅读只作为明确的历史上下文；本轮参考复读单独记录，未冒充全参考新读。

35项逐项理由、actual条款范围哈希、静态行身份及其他贡献责任见 [finding-dispositions.json](finding-dispositions.json)，完整固定对象见 [fixed-control-bindings.json](fixed-control-bindings.json)。资源/缓存失败、音频参数与记忆、视觉过渡、消息/富文本实体与文尾消费、数字/命名/精确Unicode字符及状态退出均未因合并改变。本报告只给本批必要行为与登记满足，未批准其它WP/批次或根项闭合。

- **C061／R-B04-1-002（原P2）**：直接空名32×32，与非空未缓存缺图且宿主抛普通加载错的传播分开；普通非前缀动画包装捕获后空白，前缀/输入nil另有失败。SnakeSquares正时长、背景满足且到达共享black_square加载的缺图反例，失败早于nil判定并不在后续宿主重试内；有效共享图只对照加载阶段。actual WP15§5.1、原稿及R13/R14/R27/R28保留这些条件。损坏媒体/所有异常/整段演出成功未证。
- **C062／R-B04-1-001（原P2）**：合法192×128源2帧、默认.25秒、首次加入且无额外force。容量2048不折叠为64×1536/计数2；1024折叠为128×768，因计数先存/折叠标志后写保留播放计数4；共享起点后.5秒分别帧0/x0与帧2/x128。actual世界§3.2.1、原稿、W01/W24保留源帧/播放分母和宽边界未知；不推真实硬件、越界像素或安全二位置循环。

两者分别关联既有C061/C062，不另建canonical。第一轮REQUEST_CHANGES和原缺陷P2不改写，第二轮返修为候选历史。本轮actual返修证据与验收见 [repair-verification.json](repair-verification.json)；未登记观察或canonical关闭。[new-findings.json](new-findings.json)新增必修缺陷0。

C071–73复读静态入口：无符号负初值归0/有符号保留、全负范围两端归0与取消不夹限；4组5×13字符/空格及方向、实际移动消耗、SPECIAL→ACTION→BACK→USE优先；max0键盘可空返回而光标首次淡入夹[0,−1]失败，负上限光标夹[0,−2]/键盘关闭容量守卫。部分UI写入与正常清理/外层未证边界保持，没有改成统一安全空输入。

## 公共登记、历史、范围与计数

公共10路径各按actual哈希核验：approval-ledger与traceability-successor的原79行原字节前缀保留，追加35候选局部记录、其中23主责；全部actual待审/父接受未做，B07 BLOCKED，不混入接受分母。旧五批接受历史、原计划和历史源范围字节不变。全部新增公共相对链接50条解析成功，目录索引仅相关三字段和B04尾段更新；旧批准头有当前层时点解释，不转授新字节。

既有五批主责52：具体修订51满足/1缺具体消费/0证据不足；严格全贡献47/5；79已接受贡献记录/76触及ID。A017、A034、C053、WP80-B02-R02口径差异及A024等B07保留。当前两种114分母分开：114公共记录=79接受＋35候选；114新增静态设计=111保留（108原字节、R13/R14/W01修订）＋R27/R28/W24。目录311→339、33→92、401→428；大写ID口径UI398→425另有旧T06b/T25b/T34b，重复T01–T21各两次且顺序/字节保留。仅RS09/RS10/RS17、WR06/WR12、MG23/DT03/DT07八旧行变动；B03 A–G251及其余旧条目保护，B06八正式输出不变。

ROOT002当前后继仅地点条10/灯光5/黑暗6/图片8/计时器5=34具名静态场景；四原NA具名对象与旧WP79 source-judgments全文件原字节保留，不批准全文件覆盖或真实事件链。C003只本批C-04扩展，完整根/八扩展及他批责任保留；A059仅接口已接受与本批播放边界，完整BattleAudio不获整体接受。详见 [public-registration-and-history.json](public-registration-and-history.json)。

## 读取冻结及后续边界

B06四最终读者＋原WP15音频、B07四最终读者＋原WP17消息，各五份身份在actual、候选、基线/前轮都核验。B04全部74、B07全部64计划读取按current或具名固定93e对象核哈希；两个全局finding/index不在当前checkout，明确读取93e固定对象，不误称actual中的文件。

B06 WP24§5.4/PT41–63六逻辑选择/引子交付前记忆原字节不变：普通[A,B]/[A,nil]/[A,空文本]与直接FromType不同；选择不清预置，引子首次Q/0且取消待播计时、既有R/r保留。播放参数/音量/暂停/恢复由WP15，正常返回清四预置由WP16；伙伴/雷达和其它责任不增授批准。

**B04→B07保持串行**。本报告不是父任务C接受或B07解锁；父任务接受精确actual/报告SHA后，再按精确后继重冻结全部计划/五份相关原稿读取。未来B07 WP28、WP30任何改动都触发受影响B04反向核验，当前两路径基线字节及锚哈希保留。[interfaces-and-limits.json](interfaces-and-limits.json)提供各五身份与两反向锚。

## 独立检查与证据限制

先独立保存 PASS_SCOPED 初判及 **2374** Git/文档检查，再详细比对A-REG检查名称与结果；补核后 **2596** 文档检查通过。758输入检查、1315登记检查以及前轮1168/作者900计数是已保存记录，本轮没有运行这些作者/历史审者程序。只有本目录新写独立Git/哈希/JSON/TSV检查器被运行。[independent-first-judgment.json](independent-first-judgment.json)、[independent-validation-before-author.json](independent-validation-before-author.json)、[independent-validation.json](independent-validation.json)、[author-comparison.json](author-comparison.json)保存顺序和证据。

参考独立目录真实commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`、正确origin且clean；仅只读文本，不运行游戏/Ruby/编译/转换/反序列化/媒体程序/参考模拟器/求解/行为向量。**参考执行0、静态设计执行0、运行观察0、已证真实demo链0**。U01–10/G01–12/AX01–20、具名素材/宿主/配置/备份未读限制继续保留；本轮新读与未读补集、其余未读文件单列 [source-reading-log.json](source-reading-log.json)，历史范围不并入本轮新读。

本范围没有剩余实质阻塞。有效配置仍UNVERIFIED、媒体/宿主/真实交互未证是明确范围限制；Plan A不新增配置认证门。规范229继续OPEN、关闭0；父任务后续接受/重冻结与其他贡献/最终全局门仍需其授权阶段处理。
