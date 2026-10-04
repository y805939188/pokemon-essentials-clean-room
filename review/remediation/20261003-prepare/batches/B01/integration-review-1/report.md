# R-B01 实际整合第 1 轮独立核验：PASS_SCOPED

审查者 R-B01，2026-10-04。本轮只新增独立审查材料，未修改正式规格、测试、作者材料、历史批准或公共登记，未派生子任务。

**结论：PASS_SCOPED，唯一被审实际整合对象为 `93d0714ddfdb4900e946c0acd1cc80cf6431f0a0`。** 完整 PRE0→整合的八份正式文件保持已独立审查候选的字节；新增／修改的十五份公共登记的当前范围、导航、计数、逐 ID 追溯及历史／当前身份分层成立。本批七项主责修正／后继勘误、六项部分跨批贡献和 GIR-FD82-001 的局部入口修复通过本次有界整合核验。没有发现本批直接引入的正式新问题或阻断返修项。**这不是十四项 finding 关闭、其他批次通过或全集整改验收通过；229 项必整改 finding 仍全部 OPEN。**

本结论满足批准方案的 B01-I 独立上游门禁，可由父统筹按既定流程登记并向 B02/B05 交接该准确冻结输入；本审查未启动下游或修改中央门禁字段。候选复审 `c919657…` 仍保持原字节，其一项链接检查支持证据由本轮明确更正，见 [reviewer-evidence-errata.md](reviewer-evidence-errata.md)。

## 1. 对象与执行身份

| 角色 | 固定身份 |
| --- | --- |
| 原实际被审基线 | `e1e01bb18d824931e54f182dd61af5a9f908ba85` |
| 原最终全局报告 | `93e10babe0b9c9ef8b3f5277754541b447beeeb4`，`review/global-independent-review/2026-10-03-fd82a639/` |
| 批准方案 | `41fffb540c6483f5296ea0d33b789b75180d27ed`，`review/remediation-20261003-prepare/` |
| 完整差异起点 PRE0 | `8f3a811855fc43b5fe5eb7809931b4e1749200de` |
| 完整被审候选 | `c7e30a1197083e86315d735fcfde5e31574d935a` |
| 先前独立候选报告提交 | `c919657840bb09394ce03a8a8688b02666f030dc` |
| 保留双父的合并 | `56a2391b49156abbf81b8e8f0add5ac7a9e5bff0`，父 PRE0 与 c919657，树与 c919657 相同 |
| **本次实际被审整合提交** | **`93d0714ddfdb4900e946c0acd1cc80cf6431f0a0`**，远端 `remediation/20261003-prepare/integration` |
| 独立固定参考 | `Maruno17/pokemon-essentials@8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree `7589c800b61ba13a13040ed0d686979b80a84fd0` |
| 本轮报告分支 | `remediation/20261003-prepare/review-B01-integration-1` |

**被审整合 SHA 与本轮报告提交 SHA 不同。** 报告提交在提交及普通 push 后由外部交接给出，本文不写自己的提交哈希。输入 tree、blob、完整 SHA-256、字节数和远端输入回读见 [scope-manifest.json](scope-manifest.json)。

在新执行环境中重新核对主仓库、AGENTS.md、固定方案 B01-G/B01-I/B01-C、B02/B05 读写／依赖合同、semantic-dependencies 和 physical-conflicts；项目没有相关 `.agents/skills/SKILL.md`，没有借用未读技能要求。独立 fetch 并 `ls-remote` 核实整合 SHA，而不是依据作者临时 receipt。独立重新 clone 参考到主 Git 外 `/workspace/reference-r-b01-integration-independent`，核定 detached HEAD、tree、origin、clean，其后只读。作者执行目录的临时 publication receipt 和 patch 不作为已读取证据；本轮直接从固定 Git 对象重建两份完整 patch。

本轮明确请求 **gpt-6.1-sol / Ultra / Standard(default)**，以已受理委派及用户允许的参数请求／平台受理为执行依据；未自行降档、加速、回退或更改配置。**实际生效 model／reasoning／speed 仍全部 UNVERIFIED**：本环境没有可独立验证的三项实际配置回显，也没有取得可独立审计的原始参数回执。作者 Max／Standard 与审查 Ultra／Standard 分别保留，不能互相代替。

## 2. 完整变化与保护范围

独立重建 **PRE0→93d0714**，共 59 个路径：8 份正式文件、30 份作者／扩围记录、6 份先前独立候选审查材料、15 份公共登记。相对候选报告 c919657 只有这 15 份公共路径改变；八份正式文件在 c7e30a、c919657、93d0714 三个对象中均逐字节一致。不能只审前一未审候选 e6f14de 的两份原规格增量。

正式范围是最终 WP02、WP03、WP04、WP05；两份 generic-kernel 测试目录；原 `specs/kernel/wp04-pbs-lifecycle.md` 与 `wp05-events-extensions-plugins.md`。两份原规格的授权扩围只涉及 WP04 A001/A002、WP05 A004/A009，范围记录与原候选复审仍完整冻结。完整正式 diff 与已独立审查的候选全差异相同，53,229 字节，SHA-256 `e3524c14241fa44699d9628abf339ed526a11f79f8c27b15c03f95e37d131517`。

八份正文／测试的全文、原对象 current_qualifications／有效二审／扩展及反例判断继承先前独立复审，前提是本轮已重新核定完整对象和字节相同。本轮重新阅读公共新增／修改部分及其相关身份、条款、测试和固定参考重点，判断新公共层是否改变原有验收意义；没有把作者成功摘要或哈希一致当作新公共语义批准。原报告中十四个完整 finding 对象与作者 original-findings 仍完全一致；规划有效字段、七项主责、严重度和原扩展均未改。

30 份作者材料、6 份候选审查材料、PRE0-handoff／global-premises／model-request-receipts、批准方案、历史审查与批准、dated manifest、旧 current-hashes 均未倒写。双父合并树与 c919657 相同，证明没有选择另一版丢弃内容；作者声明的临时合并过程无冲突未被本审查现场观察，树与父对象关系才是本轮独立可复核证据。

## 3. 十五份公共输入的语义核验

| 公共路径／分组 | 独立判断及适用边界 |
| --- | --- |
| `deliverables/final-specification-set/scope-statement.md`、`README.md` | 同时说明批次1–15／113份来源静态输入的全集作者交付、全局 review 完成、229项必修 OPEN，以及局部候选通过与新公共输入待审的冻结时点区别。README 使用真实 `user-interface/` 导航。scope §2 未验证表、§3 证据等级、§4 净化纪律均原字节保持；§5 完成度声明合理更新，不升级运行证据。 |
| `deliverables/final-specification-set/test-catalog/README.md` | KC01–06、KR01–13、KL01–32、EP01–21 对应实际目录；51＋87＝138 行。相对 PRE0 新增20 ID，已有只改 KL10／EP07／EP08，无删除；非 EP 共享行保持。其他15份目录索引没有新增批准，全部静态条目未运行。 |
| `audit/source-traceability.md` | 仅追加当前有界层；既有 T-表与批准／当前历史身份原文保持。新层准确区分 WP02语言贡献与旧原稿欠项、WP03映射依赖与 WP19完整表、WP04授权原稿同步与其他专用写出交界、WP05路径／顺序／假值／Link。不会把旧 GR-001 批准转给新字节。 |
| `planning/coverage.md`、`planning/feature-matrix.md` | 既有状态归到历史被审时点，增加本批当前限定层，没有提升旧 Feature 行。113 Feature／84包是归属统计，不是完整行为正确性。WP08／WP19／WP36／WP73等欠项及具名未知保留。 |
| `review/remediation/20261003-prepare/finding-ledger.tsv` | 229行等于原229必修规范 ID，全部 OPEN；priority、required、source_status、owner、contributor、closure_gate均不变。只有14行工作流更新，其余215行逐字段原样保持。 |
| 同目录 `approval-ledger.tsv`、`traceability-successor.tsv` | 14项绑定正确 c7候选、R-B01／c919报告、原93e报告及本批实际处置。原状态与当前整合分栏：历史 proposal-only 不能改称候选入口已修；scope/README的实际局部后继应用另列。测试 ID均存在，跨批剩余明确，未伪造本轮独立结论或关闭。 |
| 同目录 `candidate-manifest.json`、`integration-manifest.json` | 八份正式输入、八份不变原依赖、七份公共修改、七份后继记录及六份独立候选报告的 blob／SHA-256／bytes 全部独立重算一致。候选历史处置14对象逐字等于 c919记录；当前 integration state 单列。manifest 不自哈希／不构造自引用 commit，本报告直接绑定实际93d对象。 |
| 同目录 `final-integration-review.md` | 明确 A-REG 交接而不是独立整合报告；其 PENDING／BLOCKED 是被审提交冻结时点，未伪装已有新公共结论。实际依据是本报告，不能用这个作者文件名作为通过证据。 |
| 同目录 `historical-errata.md` | R01旧“全面移出”、R02两条目的地及 C022父No／真正写出分层的后继关系准确；四项原规格授权同步说明新身份，不倒改旧处置、旧批准、AX或其他真实共享副作用。 |
| 同目录 `reference-reading-limits.md`、`scope-counts.json` | U/G/AX、未读与未验证范围、配置 UNVERIFIED 和四项执行0保留。Git清单为131份最终 Markdown，其中111行为文、17目录；历史113来源输入与现有文件数量口径不同，未混同。 |

公共修改／新增 Markdown 中 **188 个实际本地文件／目录引用全部解析到 Git 对象存在的目标**。这不包括 GIR-FD82-001 七份原有正文内的错误路径；该七处确实仍在且与原基线字节相同，Voltorb 三层回退是正确对照。锚点存在／全仓库导航／跨批所有正文并非本轮重新全文验证范围。

旧 `current-hashes.tsv` 中本批六份最终／目录行仍匹配 PRE0 字节，已不匹配新整合；dated manifest 中原 WP04／WP05 的旧完整哈希同样匹配 PRE0而非新字节。新 audit／README／coverage 当前层明确将读者引向当前 integration manifest 的八份新身份，因此旧行作为带日期历史保留成立。没有宣称旧 TSV 对当前所有文件仍是实时哈希表，更没有复用旧 Reviewed 通过新增字节。

## 4. 逐 ID 实际整合处置

严重度沿用原最终有效裁决；旧 WP80 P2 沿革不被删除，当前残留为 P3。以下“已核验”只指本批有界贡献在准确整合对象中的实际应用；每项规范状态均 **OPEN**。机器可读处置见 [finding-dispositions.json](finding-dispositions.json)。

| 原规范 ID | severity／责任 | 本轮实际整合处置与反向对照 | 仍需路径／验收 |
| --- | --- | --- | --- |
| GIR-FD82-001 | P3／贡献 | scope/README当前范围、作者交付与独立批准分层及 user-interface导航的**局部正式修复已核验**；候选原proposal-only身份不冒改。实际七个两层回退仍不可达，三层回退及Voltorb对照可达 | B18/B21修七份具名正文源路径；逐文解析、保留来源／净化边界。全finding未解决 |
| GIR-FD82-A001 | P2／主责 | 原／最终WP04、KL10与公共身份一致：端点各一个 U+005C/U+0022，`\"Alpha,Beta\"`合并耗尽保留端点，独立尾`,Other`时去端点；KL07–09及旧正确普通／末／非末对照保持 | A-REG登记本轮有界整合报告与新字节；旧GR-001只绑定旧对象，不能宣称全局关闭 |
| GIR-FD82-A002 | P2／主责 | 整秒全集合最大值：调试、PBS存在、合法发现且可读输入、必选数据可读、非负时间、其他触发关闭的隔离前提保持。1000.1/1000.9同截1000仍触发；999.9对900.1和1000.1数据集合不由新鲜度触发。相等／反向向量、原最终同步成立 | 保留非调试早退、必选产物缺失／读取失败、其他触发分层，按实际整合登记 |
| GIR-FD82-A003 | P2／主责 | 正常省略Scripts且无自动候选→合法空列表；解析后缺失／nil／false防御错误与EP18的静态故障前提保持，EP17整个产物无条目另列；未把false边界说成正常解析自然出现 | U09真实插件组合未知；登记新有界贡献，空列表不能等价报错 |
| GIR-FD82-A004 | P2／主责 | 自动候选按完整路径小写`.rb`子串：old.rb.bak、Marked.rb/readme.txt入选，普通readme.txt／仅.RB排除；显式b,a先于自动a,b,c，首次文本去重b,a,c。每层排序、本层文件先行、产物保序与EP19–21、原最终同步保持 | 不把自动筛选套到显式项，不保证路径别名去重或候选执行成功；真实组合仍未知 |
| GIR-FD82-A006 | P2／部分跨批 | WP02/KC06贡献实在：提取选B后取消类别选择，玩家及当前消息仍A；启动／载入的真实选择入口与载入存档直接写入保留 | B02／公共同步：原WP02:288、设置附表:200、原WP08:58、最终WP08:37；不得沿用错误切换分类或外推其他入口不存在 |
| GIR-FD82-A009 | P3／主责 | 合法已登记B1.0，A需B2.0：有／无已登记有效Link均版本错误并终止，仅有Link附更新后缀。EP08／原最终一致；省略Link允许与显式空Link注册拒绝EP13/14保持 | 不补造无Link链接，不撤销其他注册／依赖错误；登记实际整合 |
| GIR-FD82-A020 | P2／部分跨批 | WP03/KR13只完成固定Nature顺序及映射依赖：LONELY攻+10防−10、BRAVE攻+10速−10及既有静态算术反例不变，公共层没有称完整表已交付 | B05/B07交付完整25身份／20修正＋5中性、WP19正文／测试、WP28消费者；保留覆盖优先、取整、缓存 |
| GIR-FD82-C004 | P2／部分跨批 | WP04/KL22四层交界：合法非空Land槽登记0→档案0→PBS省略→成功重编译21；OldRod默认0保0、Land70保70。当前地图缓存另属C005，不借此关闭 | B08/B19的WP36、WP73-B、对应原稿和编辑器测试同步，不能默认无损往返或回滚 |
| GIR-FD82-C016 | P2／部分跨批 | 保存时非零形态后缀决定路径：基本形态高度0→4只存档，旧PBS0、档案重载4、旧PBS重编译0；同后缀五组相等只省略节、不取消路径，异后缀额外路径及惰性查询新增记录保留。KL23–26一致 | B19及领域／公共：指标编辑保存／预览、原稿与WP15/16领域；不声称全0集合正常UI必然持续可达 |
| GIR-FD82-C022 | P2／部分跨批 | 父No复数Evolutions不把16转文本；Yes清A并先存档，B旧反向关系暂留；真正单数Evolution写出才有共享前向参数转换，其前档案仍数值、全量成功重编译重建。KL27–29及后继勘误正确 | B19/B21：原WP73-A:35、最终:19及编辑器测试／保存追溯仍须修；不倒写旧AX／批准，不把旧No反例合理化为参考异常 |
| GIR-FD82-C080 | P2／部分跨批 | WP04/KL30–32专用编译：重复Land70后省略／空概率清旧PIDGEY槽而保70，显式21才覆盖；junk→0、负概率保留、权重／等级0拒绝、负权重不进数字开头槽分支。地图／版本前缀及重复节错误独立 | B08原／最终WP36及测试同步；不沿用“重复Land恢复21”或统一非负数规则 |
| WP80-B02-R01 | P3／主责 | 最终WP02§7来源41文件命中数确已移出；直接世代依赖、118/88/30/47及41布尔配置数量保持。新公共索引接旧“全面移出”勘误，不改原审计统计 | 按本轮报告登记后继；原历史结论不变成当前完整验收，全finding不关闭 |
| WP80-B02-R02 | P3／主责 | 旧第14行指原WP02§4.3和附表§7/§7.4精确审计锚点，非复制全部；第81行41/139/0指原附表§7.2经T-WP02-02，非净化§3。当前后继索引／身份正确实际应用 | 保留旧表与旧批准对象；A-REG登记本轮后继，不倒改历史 |

六项跨批 P2 欠项与七处 P3 断链均继续按原编号／原 severity 保留，没有静默降级或转为“不适用”。本轮不关闭任何规范 finding；没有新增正式 finding，`new_findings=[]`。候选 scope-approved 的七主责完成不等于七规范 ID 已满足最终关闭门禁。

## 5. 静态检查与 reviewer 证据更正

[independent-validation.json](independent-validation.json)记录 **41 项独立 Git／JSON／文本／路径检查 PASS，0 FAIL**；不是行为向量运行结果。覆盖完整59路径、候选/公共分层、所有输入身份、14对象与有效验收、229 OPEN／215不变、138行／20新增／3修订、188引用、正确七个断链、旧哈希时点及B02/B05门禁。完整patch见 [PRE0-to-integration.patch](PRE0-to-integration.patch)，公共新增patch见 [candidate-review-to-integration-public.patch](candidate-review-to-integration-public.patch)。

完整输入 `git diff --check` 对三份原作者保存的 unified-diff payload 报空白行诊断：上下文空行是单个空格，属于保持真实patch字节的结果；八份正式与十五份公共文字自身检查通过。未删改这些冻结patch以制造无诊断摘要。

**R-B01-I-ERR01：** 上次候选脚本的“七断链”支持检查使用手列清单，漏了 mining-data、误列正确Voltorb，且两层路径子串可误匹配三层路径；该项旧PASS记录不能作为七处断链的有效证据。本轮从固定原 GIR-FD82-001 / RUN-C-132 枚举真正七份，解析完整定界路径并验证实际Git目标。七处仍断、Voltorb仍正确，对局部候选结论和本轮范围结论无改变。旧报告六份原字节保持，由这个公开后继更正替代相关证据，不假装旧39项记录全部仍是有效检查。

本轮检查器开发还曾错误地将§5“完成度声明”认作§4，拟提出一个不准确的证据问题；真实标题分节证明§2/3/4均未改，该拟议问题被证据否定，未列为正式finding。早期解析器假设七个路径是点击链接，而实际为代码跨度；旧TSV只含六份最终／目录，新原WP04/05在dated manifest；亦已按实际对象更正。以上是 reviewer 检查假设更正，没有要求作者返修或降级任何有效 finding。

作者manifest中34项自检是作者材料，本轮逐类对照真实Git及文本后形成独立结论；包括“sections2/3/4 exact”的断言确实成立。没有依据作者全成功摘要直接准入。详细只读范围及未验证边界见 [source-reading-log.json](source-reading-log.json)。

## 6. 下游冻结与剩余门禁

批准方案明确 B02-A、B05-A 都依赖 **B01-I＋PRE0**；B01-C由A-REG在B01-I后登记本次核验。**本次实际 B01-I 有界独立核验已完成，通过对象严格是93d0714。** 被审提交内PENDING/BLOCKED为作者冻结时点，未倒写；父统筹可使用本报告进行后继登记及准确冻结交接。机器可读边界见 [downstream-freeze.json](downstream-freeze.json)。

- B02冻结读取本次WP02/04/05、测试与公共身份，但A006的原WP02／附表／WP08旧错误属于待修目标，不得作为已正确的规范前提。共享 `generic-kernel-wp05-06-07-08-09-10.md` 必须保留本次EP条款／EP01–21；按 physical-conflicts 串行写入、先冻结／rebase，改变字节后独立复审。新的原稿扩围须由父统筹按既有授权落实精确范围，本审查不擅自扩写。
- B05冻结读取WP03/KR13固定映射依赖、公共逐ID剩余；没有提前批准缺失的WP19完整25表或WP28消费者。必须对固定参考完成B05/B07对应贡献与正文／测试同步，继续保留其余条款的实际范围。
- 本审查没有启动B02/B05，没有写中央ledger、approval或其他B01-C正式产物。后继登记、下游新候选／实际整合、B21及最终Ultra仍需分别满足方案门禁；任何后继的新正式或公共语义字节不得冒用本报告对93d0714的结论。

仍保留 **U01–U10／G01–G12／AX01–AX20、未读备份／样本／素材、宿主与真实插件组合**。未全文重审整个参考仓库、全局所有原规格／最终正文、历史大型manifest/覆盖表的全部语义；本轮对这些只核不变身份及必要锚点。未运行游戏、Ruby、编译、转换、生成、反序列化、模拟器、求解器或测试向量；**参考执行0、运行观察0、真实demo链0、静态向量执行0**。独立clone/reference没有加入主Git或推参考上游。

没有本轮阻断返修路径；跨批返修路径及原验收如逐ID表保留。报告commit与普通push、核远端完成后停止，等待父任务安排；不合main、不force、不改历史、不做全局关闭。
