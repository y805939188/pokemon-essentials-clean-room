# R-B06：实际 B06 integration 独立复审 1

结论：**PASS_SCOPED**，只绑定实际 `c67f400c000df4fd73ab1440e1487a3d534336aa`／tree `def2e2afbf344c3f73d2d330e282bad341af0f70` 的 B06 十项贡献、八份正式文件、公共后继增量及具名依赖交接。七项及 N001/N002、新增 A034/A059/C103 均重新复核，未自动沿用候选字节结论。本轮新增实际整合缺陷 0。父任务串行接受尚未发生；不宣布全批 READY、全域完成或关闭任何 ID，不派发 B04/B07。

请求配置为 gpt-6.1-sol／Ultra／Standard(default)，实际模型、推理档和速度 **UNVERIFIED**；方案 A 保留。未降档、加速或派生复审。参考程序、行为向量、运行观察、已证 demo 链均 0。U01–U10、G01–G12、AX01–AX20、全部具名未知及部分失败前提继续保持。

## 对象与独立证据

| 角色 | 固定 SHA |
| --- | --- |
| 已接受 B03 后继基线 | `1fd612d47dcda164de61ab2d25a1cb5e0fbde085` |
| B03 已审 actual | `e24f2ac6f43642ea0e68bd9aa21fb2c313d6ebdf` |
| B03 actual 报告 | `dea9d118d7ed3b7ddb57b1c4e7bd40db8dd06497` |
| B06 完整候选 | `4076a3fbbf6fe355b73f3fe2229d1f981fe735d2` |
| B06 作者证据后继 | `ee7461e90ad5e0943e39c56c22a080f761f4e1c0` |
| B06 候选独立报告 | `70babef632539c952aa988e7762d0c2aa19cfeb3` |
| B06 公共登记 payload | `cdba36a3bc0fcb4629945180fcc3879188f7517b` |
| 本次被审 actual | `c67f400c000df4fd73ab1440e1487a3d534336aa` |
| 本次报告 | 新分支普通提交／push 后外部交付准确 SHA；不是上面的被审对象 |

环境恢复后实际读取 AGENTS.md；主仓库干净后在被审 actual 创建独立复审分支。独立参考位于主 Git 外 `/tmp/R-B06-reference`，HEAD `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`、tree `7589c800b61ba13a13040ed0d686979b80a84fd0`、clean 均核实。参考只读，没有把参考内容加入主 Git 或推向上游。

先复读实际十项条款、60 行和固定参考关键分支，将反例／前提锁在 [independent-first-evidence.md](independent-first-evidence.md)；SHA256 `b295f2ed42577fd10bfdf46b12b746ab0cd5acd6d8c2bdab96ab51c550d45c87`。交接结构与公共增量此前仅作为定位输入，未采用其自检作独立证明。随后用本新目录的 [verify-independent.py](verify-independent.py) 重新复算 Git／文档身份，2998 断言通过、最终失败 0，见 [independent-validation.json](independent-validation.json)。历史 6594 与登记作者 1031 不是本轮断言，未运行其 verifier。

固定参考新文本阅读为 25 文件／46 个具名导航范围，见 [independent-source-reading.json](independent-source-reading.json)；导航范围不代表运行分支覆盖。旧阅读范围及作者 40 个范围另做元数据核验，且直接核实际 author-stage2 的声明与旧已审范围一致。本轮没有运行作者 helper；N002 用新复审者文档边界校验处理两条有效、七条无效输入，七条均在哈希前拒绝，见 [independent-range-validation.json](independent-range-validation.json)。此校验只处理文档索引，未求解或模拟参考行为。

## 全量差异、来源及旧批保护

完整上游→actual 无路径过滤差异为 126 路径，12,414,934 字节，SHA256 `5a6ca5416279cdecfc70115f7e32452cdef7a290dea83291765ddb98dacf7a42`。完整候选→actual 为 66 路径，10,452,233 字节，SHA256 `de0572e9c77622242723ae8a147d534db63992a4f87b3578002edda26b7147d0`。差异采用关闭外部 diff/textconv、关闭 rename、binary/full-index、unified=3 的固定选项；完整路径状态和复现工具在 [git-and-source-identities.json](git-and-source-identities.json)。冻结交接里的两个上游／候选→payload 完整 patch 逐字节重建相等；由 payload 到 actual 恰好只增加两份 patch 与 diff-and-freeze.json 三份证据。无正式、公共、来源或既有 management 字节变化。

三次普通 merge 的双父身份及第一父差异分别核对。首 merge 仅引入完整已审候选与其报告的预期来源；后两次分别增加旧 R1 的 11 文件、R2 的 14 文件，所有选入字节都等于相应第二父及 actual，没有额外正式解决改写。103 个独立来源身份逐项核固定源 SHA/path/blob/SHA256/bytes 与 actual 相等：八份正式、53 作者证据（15＋17＋21）和42复审证据（11＋14＋17）。全部历史来源不可变，不因错误范围曾存在于旧作者证据而重写历史。

八份正式是最终 WP24/25/27、两份 creature-rpg 目录、原 specs WP24/25/27；均与候选等字节。正式范围之外的既有路径只允许十个公共后继路径变化，完整树比较符合此集合；新增路径恰为95来源证据＋13整合管理证据。AGENTS、已接受 B03 十三份正式、原／最终 WP26、原／最终 WP66-B、其余既有批次／冻结／审批历史全部保持。此轮没有正式修改、公共写入、main/force/参考上游操作。

两目录从164／167到220／169，总331→389，新增56＋2＝58行；既有行只有 PS11、AQ04改动，没有删除。60分配行＝此前七项25＋新增三项35，其中含两条既有行修订，不能当作整文件总数或执行次数。CI28、HP45、IU48、SH26、GR44、DC20及全部未分配既有行保持。PS12 的治疗先于全满失败边界也保持，见 [all60-actual-static-rows.json](all60-actual-static-rows.json)。

## 十项贡献与回归

| ID（均 GIR-FD82-） | 本次静态核验及逆向对照 | 结果／仍待责任 |
| --- | --- | --- |
| A032 | 原／最终 WP24严格小于上限；等长去数字、较短保留数字、完整用户名回退；PT29–31及刷新对象前提一致 | PASS_SCOPED |
| A033 | 非调试检查早返回、调试拒绝新增 false、直接装载未知类型错误分开；装载／伙伴部分失败没有推广到检查；PT32–34 | PASS_SCOPED |
| A034 | 启动无伙伴拒绝门；先使用数／电量／摇草、后候选钩子清链且不回滚；骑车拒绝、成功新上车取消、重复上车早返回及无伙伴正常草对照；PT35–40 | PASS_SCOPED；B08未完 |
| A035 | 显式队伍索引0/5都追加同一源引用；盒目标覆盖与满队早失败作对照；PS29/30/37/38 | PASS_SCOPED |
| A036 | 当前盒优先后从0号扫描；盒2期望补齐0/1满，盒0可用对照优先0；PS11/31；PS12旧失败边界保留 | PASS_SCOPED |
| A037 | 满队静默送盒与五名追加第六名；图鉴／形态／初始招式先于放置，普通合法物种、无动态回调和操作正常前提齐备；AQ04/36；WP26只读 | PASS_SCOPED |
| A038 | 至少非蛋成员才有Give，濒死非蛋计入；蛋唯一队伍无菜单项，后守卫不倒置前门；BG30/31 | PASS_SCOPED |
| A059 | 六入口分表、数组最后非nil、储存空文本覆盖后回退与FromType保空区别、独立预置；引子记忆优先与位置查询有限兜底；PT41–63止于播放入口交付前 | PASS_SCOPED；B04/B09/B17/B21未完 |
| C103 | 层2→1→0首煤灰层；玩家持袋／无袋／NPC／上限实际增量／无煤灰对照；资源和统计先擦除、部分失败不承诺回滚；PT64–69 | PASS_SCOPED；B14未完 |
| C120 | 首次显示可写内存、空值/空文本默认显示不写、未解锁整数写回及退出无回滚；LF／先行其它文本／首匹配／非匹配文本有限观察；PS32–36/39–42 | PASS_SCOPED；B16/WP66-B未完 |

原问题的完整原对象和批准验收对象，以93e10...与41fffb...逐对象哈希／字段相等核对，包括 current_qualifications、裁决优先、有效约束、最低修订、确定复核、验收门和全部贡献者；实际登记保留旧完整独立处置、完整作者响应及精确条款／60行身份。按范围检查原／净化对应，不把共享根因、原稿已正确条款或多文件定位重复计新 ID。逐项实际处置见 [finding-contribution-dispositions.json](finding-contribution-dispositions.json)、[canonical-and-contribution-checks.json](canonical-and-contribution-checks.json)。

历史 **B06-S1-R1-N001／P3**：原／最终 WP25已准确按文本首个完整匹配行取背景数字，LF或其它行不阻止识别；PS33/39/40/41/42复读支持该范围，`box2x`没有声称后续显示或正常退出。行锚和首匹配的语言语义由官方 [Ruby Regexp](https://docs.ruby-lang.org/en/3.1/Regexp.html#class-Regexp-label-Anchors)、[Ruby String](https://docs.ruby-lang.org/en/3.1/String.html#method-i-5B-5D)复核；结合固定源文本作静态推论，没有运行Ruby。原首轮 REQUEST_CHANGES／缺陷对象均不变。

历史 **B06-S1-R1-N002／P3**：Trainer_LoadAndNew实为124行；实际后继范围为1–124，全部40作者范围合法、范围字节哈希相符。旧1–135保留为历史错误证据；新复审文档校验明确拒绝超界后才允许哈希。两缺陷均为本次 **REPAIR_VERIFIED_SCOPED_REGRESSION**，不是原229中新根或已关闭ID。

## 公共层与下游

十公共路径的blob/SHA256/bytes与冻结、current-hashes113行逐项对应。旧69审批／追溯行保持原字节前缀，新增10条＝79贡献记录，非79规范ID；候选PASS、actual待审、下游阻塞各列一致。追溯条款范围与60行哈希准确，剩余责任JSON未丢失。除目录README两行索引范围更新之外，八Markdown公共层只插入后继说明，旧正文原字节存在。B01/B02/B05旧26主责严格23／3和具体25／1／0口径保持；B03已接受19主责、B06本轮7主责不混入旧分母。canonical必修仍229 OPEN／0 CLOSED。WP79旧BattleAudio NA没有被当作新整域验收；其具名后继登记仍待串行接受，见 [public-layer-checks.json](public-layer-checks.json)。

B04批准计划逐路径匹配 **74读／8正式写**，35贡献控制（23主责），计划依赖B03；本次附加B06实际接受／WP24-A059冻结门合理且仍阻塞。B07逐路径匹配64读／8写和19贡献控制，依赖B05/B06。两批各两条原报告findings／root index读取精确绑定93e10...，其余计划读绑定本实际字节；不会把外部不可见文件冒充current-tree文件。B04八写输入及额外十二只读输入也核实。原specs仍只读；若后续需要同步，须按准确ID／条款／路径获得父任务窄授权，不能静默扩大。

B04/B06四正向接口（WP15音频、WP16战前、engine目录、UI目录）和一反向WP24接口按批准集合重算一致，A059交界必须保留逻辑请求／媒体播放／战前恢复／胜利捕获等各自范围。已接受 B03 actual/report/acceptance链及十三正式输入核实；未消费未接受B03候选。共享整文件目录的B03隐藏/取消、F9/路线/自动移动及零时长边界仍受保护，不能据B06的局部行批准整目录。

B04/B07虽无写写交集，仍有下列4＋2读写接口及共同 **C003**，没有并行安全证明：

- B04写→B07读：engine-overworld-wp11-15-59-60目录、engine-overworld-wp16目录、user-interface综合目录、WP17 messages-windows-input。
- B07写→B04读：WP28 item-use-and-training、WP30 growth-learning-and-friendship。

继续采用完整合同串行 B04→B07：B04已接受输出后重冻结B07四处读；B07 WP28/WP30后续改变B04输入时，补做B04受影响复审。C003控制指向完整原对象／批准对象，保留C-03输入差异及全部八项已裁决扩展，各WP局部贡献不能关闭共享根。C071/C072/C073预调查仅有父任务完成通知，没有固定artifact SHA/path/hash，未验证其内容身份，不借用其源阅读或批准。详情在 [downstream-contract-checks.json](downstream-contract-checks.json)。

本报告普通提交并回读远端后，停等父任务按actual与本报告的准确SHA串行接受。任何新增公共接受层或下游变化都需要新的基线身份／冻结／受影响核验；本报告不会自动迁移到变化后的字节。公共登记由父任务／A-REG执行，本复审只新增本目录证据。
