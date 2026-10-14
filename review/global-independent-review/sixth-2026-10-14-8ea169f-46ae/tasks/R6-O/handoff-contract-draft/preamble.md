# 第六轮后续修订任务的通用执行合同

本合同用于启动第六轮已裁定的正式规格修订与独立验收。交接准备本身不启动 update，不启动作者或审者，不改正式稿。本合同之后必须接上每个 ID 的完整七组实录、每批实际读写范围、共享接收人与验收条件；不得用摘要、模板、链接集合、旧 PASS 或任务名代替这些记录。收到后继用户明确修订任务后，按其授权执行本合同及完整逐项记录，不因已经获准的常规操作反复要求确认。

工作只产生行为规格、测试目录、审查证据和交接记录。先全文读项目 `AGENTS.md`，遵守 clean-room 分离：参考实现回答可观察行为、规则、输入输出、状态和失败前提，不提供未来框架的源码模板或类层级。本轮发现的源缺陷必须准确记录；是否在未来独立实现中保留该缺陷，是另一个兼容范围决定。不得修参考源、把源表达式抄进规格、逐行翻译 Ruby、实现框架、引擎适配器或战斗系统。

**固定身份与读取入口。** 项目目录为 `/Users/dingshinn/Desktop/pokemon-framework-reference`，项目 origin 为 `y805939188/pokemon-essentials-clean-room`。本轮正式输入是固定 main 提交 `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，工作区 tree 为 `6ab3429170d2762607fbc2237014c3a160449fa1`，`deliverables/final-specification-set/` tree 为 `1046fbb657882e84b3dfc6d017943a9edf7782e5`。131份正式文件的逐载荷身份以本轮实录为准，不能把新的报告提交当成新的正式输入。

固定 lightweight tag `refs/tags/delivery/fifth-round-closed-final-20261014` 指向上述 main 提交。R 的独立仓库目录是 `/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`，origin 为 `Maruno17/pokemon-essentials`，commit 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree 为 `7589c800b61ba13a13040ed0d686979b80a84fd0`。R 全程只读；其432 tracked材料、额外两份 DS_Store 库存、地图／媒体缺失和原生限制分别保留，不把额外文件混入432分母。

第六轮报告目录是 `review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/`，报告分支是 `codex/review-sixth-2026-10-14-8ea169f-46ae`。已实际冻结的本地语义 core 提交为 `5210b009db5191f307301115845e31475cd798ef`，workspace tree 为 `04b494cc46b645c27b2ab19b1cbf6a8086b0f6a9`，该报告目录 tree 为 `e1f08b1a8bada95edb1dcfbaf6b34417f787c771`。这些是已解析的对象身份，不是远端发布成功的替代凭据。实际发布对象 P、远端分支、逐载荷回读和后继 handoff 的身份必须由 root 的真实发布回执外部绑定；没有这些证据时不得预填“已发布”、假 SHA、假 UUID 或假远端链接。初始固定输入文件里的 `NOT_YET_FROZEN` 等状态保留其记录时点，不能覆盖后继真实 core 绑定。

在修改前，逐载荷验证 source 与 formal 的仓库、commit、tree、path、mode、type、bytes、SHA256 和 git blob；行号是该载荷内的定位，不是脱离版本的永久坐标。必要审读入口包含本轮 `findings/normative-records.json`、原完整 proposal、独立反证、`findings/aliases-and-tombstones.json`、`findings/policy-records.json`、`findings/limit-records.json`、`coverage/`的当前载荷与双向索引、领域阅读台账、三份 `handoff/` 分批／依赖／冲突文件、`execution-evidence.json` 和实际发布回执。它们必须实际取回、校验并阅读相关完整内容，不能把“入口存在”视为已完成审读。当前 report/core 供固定依据使用；后续作者仍须新读本批正式全文、源上下文及必要消费者，不能继承审查者阅读作为自己的阅读。

**历史资格不能扩大。** 固定历史身份如下，缺本地工作区文件时按指定 Git 对象取回，不以当前同名文件替代：

| 用途 | 固定提交／目录 |
| --- | --- |
| R4/B5正式基线 | `9366d9d17aaeac3b4414236468affa650fb3dd27` |
| R5语义 core／发布 | `c0ff33024aea424c68d29f9778fe7c8e807d21e8`／`f49d870c6fd616ab6736754a218a4553b5acac7f` |
| U08实际候选／报告 | `e9f7590e68347849450fd5cbdba538e605cda0a7`／`debf59f3c5370df253706969fd4dd1c103300bf2` |
| 第五关闭所选候选／报告 | `13fddb0a217b36974c75657aa68da0caf104ee48`／`044c3483229e7e76bedf1fc244fc84d274bf059c` |
| 唯一 activation core／发布 | `12df95a8e81061a606d50d3f0a0528793b2e6b2c`／`0378dc85cab61642ca1467e5a901b3c829df976a`；目录 `review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-activation/` |
| main发布行政 core | `b67f542b47ad33ac23053a21f62748077c167a23`，tree `e5fa5de69c1e3164597815a42776aa859c6ea4b7`；目录 `review/remediation-fifth-20261013-prepare/integration/final-main-publication-20261014/` |

最后一行的六份载荷分别为 `final-main-report.md`、`local-sync-and-recovery.md`、`main-publication-readback.json`、`package-manifest.json`、`publication-receipt.json`、`remote-cleanup-receipt.json`。恢复入口及已经具名的 archive 根保留；读取恢复说明不授权移动、删除或释放这些对象。

R1只按原 WP 范围取得历史资格，不臆造总数。R2保留229控制／21批／341精确贡献五元组；R3保留23／76，并保留 M09 optional、U08历史未启动和 M02 NO_REQUIRED 的具体范围。R4当前17／76与B5的16／75区分，Summary后继仅覆盖具名残余。第五唯一 activation 只选择已审 `13fddb…` 候选的92 proposed条目及其原精确内容，当前92 CLOSED／OPEN0，51 P2／41 P3；它不是全部旧提案、整文件、整领域或原生宿主通过。第五7 optional、7 no-required、原6 policy、原13 limits各自保留；410 native、568 schema、158 extra及21 shared／18 deps／85 solewriter均分列。262原贡献＝259显式＋3镜像，6行政 transfer与3纠正不混作新的语义贡献。

本轮受影响 path、clause span 和生产—消费接口必须重新回归对应R1–R5资格。旧 candidate01 G03／G09 FAIL、U03旧FAIL与定向修复、两 advisory MISMATCH、SC-U07-001体内LF原错误及纠正、旧时点 OPEN／WAIT均保留。不能因旧字段字样重开第五已闭项，也不能用92 CLOSED取消第六轮的独立必修。读取指针／hash只验证资格可恢复，不等于新行为 PASS。

**本轮分母与当前边界。** 65条规范裁决为56 required（39 P2／17 P3）、8 optional、1 no-required revision。AN007一般浮点递推的 Float recurrence另1 facet，不加入65；7独立政策＝原6＋GR6-POL-001，也不加入规范 optional／required数。14限制＝原L01–L13本轮刷新＋L14执行与工具元数据缺口。别名、聚合父ID、consumer facet和已经撤销的 UI-PARTY-004不得另造 mandatory或重复根因。optional与policy没有自动修改授权，未选择的未来兼容profile不阻塞56项事实修订。

本轮全量有限静态范围为 R432、formal131／28,851行／20,379有限Markdown块、supplements116（111旧稿secondary结构／身份／primary处置＋5独立保留全文），以及main的38,093 blobs用途处置。20,379块包括标题、结构、历史与scope，不是20,379条行为要求；69份结构化文本没有声称逐物理行手工全文。可得可审的有限范围已闭合，不代表全部机器码、任意未选字符串、原生选择、媒体、地图或完整Demo验收。

L01地图／完整工程、L02图形音频、L03原生执行、L04 Game与运行库、L05可读内嵌程序、L06 animmaker、L07 extendtext、L08字体、L09 soundfont、L10序列化、L11动态扩展配置、L12外部状态服务、L13纯元资料及L14元数据的精确材料、范围、剩余未知与恢复条件都按完整实录保留。限制不是源码未读的替代标签；不能把可得可读单元藏进 native opaque 或 inventory_only。反过来，缺宿主不妨碍完成有限静态事实、修订和静态验收，不得因缺宿主提前放弃这些工作。

**唯一正式写者与首波。** 后继整合 root 对所有实际 `deliverables/final-specification-set/`共享文件和公共行政台账拥有唯一写权限。R6-I是本轮接收角色名，后继必须登记实际root任务身份，不能用角色名伪装已存在UUID。作者只写自己批次的隔离candidate镜像与证据目录，审者只写自己的独立审查目录；任何作者、审者或新子代理都不得直接修改正式共享文件、另一个候选、公共finding／状态／acceptance台账或旧报告。root不得并行安排第二个实际正式写者。

14个首波候选批为 R6-U01内核／所有权／产蛋、U02战斗对象／精神香草、U03钓鱼／解释器、U04 AI失败门／评分／定位、U05行动清理／状态／后期目标、U06作者内容／转换工具、U07动画编辑／播放、U08 Debug入口／反馈／日志、U09编译／缓存／注释、U10捕获／Summary／重学、U11储存导航／图鉴、U12背包／BP店、U13设施／Arena／Palace／活动保存、U14本地化／数据默认／指标／空Flags。每个required恰有一个主批；全部14批可基于固定事实独立准备候选。54正式候选路径、24文件冲突对和100节点／110边的依赖图决定共享接收与整合验收；它们没有作者候选准备的跨批阻塞边，不等于整合或关闭不受阻塞。

28个作者／审者入口是每批 `R6-Uxx-A` 与 `R6-Uxx-R`，交接时均为 `NOT_STARTED`。这是计划身份，不是28个实际运行任务、PID或UUID。首波先准备14份候选，逐批完成候选身份绑定后才能做该批独立审查。当前协作工具容量实核为4、root占1；未来CLI实际并行容量未知，要按已验证可用资源调度并保存排队／启动状态，不把“14首波”写成无上限同时运行承诺，也不悄悄删除未启动批次。

作者请求 `gpt-6.1-sol`、reasoning effort `xhigh`；非作者审者请求同模型、effort `ultra`。二者service tier与speed均为 `default`，禁Fast／priority。审者必须与候选作者独立；曾撰写具体规格者不能成为该变更的唯一终裁者。root的写入接收和正式接受也不能替代非作者的实际整合后审查。无法取得要求的模型／effort时明确登记真实障碍，不能静默换模型、降档或开Fast；配置请求未获有效回显时实际model／effort／tier／speed／UUID标为UNVERIFIED，不能把请求、bundled模型目录或CLI exit0当作有效配置证明。

**真实可用本地CLI及查询。** 本机已实读 `codex-cli 0.162.0-alpha.17.2` 的 `codex --help`、`codex exec --help`、`codex debug --help`、`codex debug models --help` 和 `codex agents --help`。`codex debug models --bundled`不刷新目录，本地所带 `gpt-6.1-sol`列明支持xhigh／ultra，priority标为Fast；它只证明本机目录信息，不证明当前账号可用性或某次任务实际模型。启动前在实际执行宿主重验help，保留返回版本，不用记忆推断不存在的参数。

以下是本机已核参数的调用形式，仅供收到启动授权后的root使用。`repo_root`必须设为上述实际项目路径，`task_output`必须设为root已登记、已创建、属于该入口的绝对目录；两个不同入口不可共享该输出目录。root先把完整中文合同与本批完整七组记录写入实际 `prompt.md`，再启动；命令没有在本次交接准备中运行。

```sh
codex exec -C "$repo_root" -s workspace-write -m gpt-6.1-sol \
  -c 'model_reasoning_effort="xhigh"' -c 'service_tier="default"' \
  --json --color never -o "$task_output/last-message.md" - \
  < "$task_output/prompt.md" > "$task_output/stdout.jsonl" 2> "$task_output/stderr.log"
```

审者的同一调用将 `model_reasoning_effort`改为`"ultra"`，并使用自己独立的prompt／输出路径。`-C`指定工作根不是新增正式写授权；prompt里的逐路径写入allowlist仍须严格执行。launcher同时指定真实cwd，并捕获精确argv、PID、实际UTC起止、stdout／stderr、独立退出码、逻辑ID、请求配置与有效回显。不得遗漏cwd后在仓库根创建文件；本轮INC-R6-001曾真实发生这种创建后移入，现路径不存在或tracked clean不能改写为从未越界。不要复用旧launcher原始日志来伪装新任务已启动。

`codex exec`在本机没有`--cloud`；顶层实验性`codex cloud`也不等于该选项。本地 `exec`不冒称云端任务。若后继明确要求云端，只有在实际工具／API、参数、可用环境和真实回执核定后才使用该入口；未取得云端能力时如实登记，而不是发明flag或UUID。本合同提供的已核可执行入口是本地CLI。

查询优先读取该入口的launcher状态、`task-status.json`、实际stdout JSONL、stderr与阅读／差集台账。真实平台UUID从`thread.started`回显取得，PID从launcher取得；未捕获就保留缺失。`codex agents`是本机真实会话浏览入口，没有在help中出现的`agents list`／`exec status`等子命令不得臆造。`codex resume UUID`会继续会话，不能当只读状态查询。Desktop可用的read_thread／wait_threads必须用真实ID；缓存notLoaded／interrupted不能推翻仍推进的CLI日志。`ps -p`只有结合登记的启动时间、命令和PID复用情况才有意义。任务通信成功排队不代表消息已消费，进程exit0不代表合同全读或候选PASS。

不用查认证、token、额度或私密配置来补证据；不得为该任务安装／下载、开启服务、修改安全配置或重置额度。确需已授权范围之外的新能力或材料时，只阻塞依赖它的部分，继续独立可完成的静态任务，并向root登记准确缺口。

**安全执行与证据分期。** 先懂依赖，再决定是否执行。允许的额外验证仅限已全文审读、依赖已知的有限静态解析、常量算术或安全隔离原协调器／定义；在owned目录内使用显式替身和内存临时输入。不得运行未知项目脚本、原EXE／DLL／IL／loader、完整游戏、真实旧存档、外部服务或生产网络；不得以Marshal／eval等方式把未知序列化载荷当安全数据工具。需要宿主／完整地图／媒体的观察另登记材料与恢复条件，未经授权不扩执行范围。

每次验证分别记录SOURCE_STATIC、DERIVED_VECTOR、TOOL_VALIDATION、ISOLATED_REFERENCE_EXECUTION／REFERENCE_OBSERVATION_WITH_SURROGATES、独立完整行为模型与完整host／Demo。人工向量、Fraction断言、Array语言探针、RIFF／SF2／PCM／PE／CIL／COFF解析、字形／字段结构或安全数据解码不自动成为原参考程序、宿主、声音、像素或完整模型执行。资源加载／音频播放／flash／时间等待／Game.save请求分别只证明源侧请求或替身记录；不能补实际媒体存在、调用成功、固定帧完成、可见／可听结果或持久化结果。

如实际执行原定义或回调，不管旧输出把它叫什么，都如实记源执行。每一尝试保存argv、cwd、实际UTC、runtime、输入身份、替身范围、stdout、stderr、独立进程退出和每向量结果。已发生错误不删除：路径错且未加载R、部分原协调器因替身缺属性停止、无效Purify替身、被覆盖的重复运行都与修正后尝试分列。已预期并捕获的向量异常不算进程失败；tee管道exit0不能当Ruby独立exit0；历史未捕获UTC／退出／stderr不能以mtime、更新时点或重跑倒补。

本轮既有指定探针是18次Ruby尝试：12个已知exit0、4个exit1、2个独立Rubyexit未知；其中1次未加载R、17次进入原定义，exit0仍含无效Purifyv2及F重复运行。向量按O22、CA24含9捕获异常、F当前10、UI有效当前7、K早期7分别保留，不合称全局唯一向量；O3成功／2失败、F三脚本实际五次与K元数据缺失另列。R4隔离4／R5审查隔离4与update0是历史执行分母，不转入后继已执行数。本轮完整宿主、Demo、完整独立玩法模型、真实save与生产服务均0；后继新增执行须独立计量，不继承为新运行PASS。

**逐ID的七组有效验收。** 作者、独立审者和整合后审者必须实际核对以下七组；任一关键项仍缺证据就保留对应未闭合状态，不能仅填一个PASS字段。所需完整逐ID正文必须在交接中展开，以下通用标准不替代该正文。

1. `identity_and_verdict`：canonical ID、别名、根因、领域、当前required／optional／no-required分类、级别与主合同载荷一致。保留原提案／反证／撤销过程，不把子facet或父聚合新增为独立根因。作者不擅自重新裁级或把optional加入本轮必修。
2. `bidirectional_evidence`：源具名unit／事实到实际或有条件消费者再到当前主规格，正式clause反向回到固定源身份、实际范围与输入前提。需要的生产、消费、显示、缓存、保存和后继分支具名；新全文与局部join、本人阅读与当前peer receipt区分。hash／索引／读取成功不能自动给语义PASS，未定位显式caller不宣称native／动态不存在。
3. `premises_and_counterexample`：普通对照、最小反例、合法输入域、真实状态前提、时间／随机短路顺序、取消／故障／部分提交以及负证据范围齐全。失败只说明已经到达的前缀，不补全局回滚、后继完成或永久异常。静态反例与实际运行观察分列；源缺陷与未来兼容选择分开。
4. `minimum_revision_contract`：用独立行为语言作最小规则修订，准确修主合同和必要同步路径，保留已经正确的scope、数值、前提、显示门及正常案例。不能理想化源缺陷、抄源表达式、只改traceability或只在附表列名字而漏正文。测试目录、覆盖附表和跨域引用与新正文一致。
5. `acceptance_and_regression`：逐ID有效正常、边界、失败／取消向量按完整输入前提核对，不能用错误替身结果证明源缺陷。实际受影响R1–R5 span、第五92CLOSED的精确资格、共享消费者及独立控制回归均具名；旧PASS不代新验收。缺宿主时完成可定静态验收，同时把未执行层保持未知；不得冒称已运行宿主或完整模型。
6. `independent_adjudication`：非作者针对确定candidate／integrated载荷作新审，记录实际审者身份、请求／有效模型元数据、读取区间、反证尝试、结果、缺口和被审内容hash。审者报告要明确支持、反对或未能裁定的范围；root保存不采纳意见及理由。作者自检、提出者原支持、CLI完成或root接收文件均不能替代独立审查。
7. `dependencies_and_receivers`：每required唯一主批、实际candidate路径、所有共享文件接收者、冲突段、非阻塞领域依赖和整合／关闭阻塞边准确。14批可并行准备不消除24文件冲突对；root必须合并全部必要写入而非最后覆盖胜出。验收依赖须绑定实际已整合版本，不能靠“已委托”“预计完成”消除pending。

**状态与整合顺序。** 当前所有后续入口保留 `UPDATE_NOT_STARTED`。正式授权后，root先登记新的实际update工作根／分支、已有工作保护、唯一写者、逐任务真实输出allowlist和输入快照；作者创建镜像候选，逐次记录精确变更及预期影响。遇共享文件仍只交候选，由root串行接收。不得自行切换／重置他人工作区、移动main或delivery tag、force push、删除分支／tag、归档或释放环境／工作树；原62额外文件与当前8工作树等保护按真实清单保留，不把旧10工作树快照当当前状态。

候选完成后由独立审者核被审候选SHA与完整七组内容，形成`CANDIDATE_PASS`或具名FAIL／未闭。root接收已通过候选进入实际整合文件，记录来源、冲突解决、接收后SHA和精确受影响clause。随后由独立审者对真实整合后全文、共享接合、56项修订及受影响历史回归复验，取得`INTEGRATED_PASS`。任何后续变更都会使其受影响验收失效，必须对新内容重验，不能保留旧PASS覆盖新编辑。

root在全部必要整合验收、回归、载荷身份、同步路径和阻塞依赖齐备后才能写正式acceptance。`CANDIDATE_PASS`、`INTEGRATED_PASS`、正式接受与`CLOSED`是不同事件：候选可PASS而仍未接收，已接收可待共享复验，已接受可待最终发布／关闭回执。只有对应实际版本的全部关闭条件满足才CLOSED；未启动、部分完成、异常、待材料或未审差集如实保留，不能为交付摘要清零。task进程完成不自动关闭finding。

**最终交付与发布核验。** root是唯一公共记录写者，最终报告逐ID给出原裁决、候选／独立审查／整合／接受／关闭的实际身份及结果，分别列56必修、8optional、1no-required、Float1、policy7、limits14、执行分母、未执行层及INC-R6-001。全部实际新正式文件、测试目录、跨域接合、回归回执、候选／反证／状态及未启动入口必须在完整交接与manifest中具名。无源码、框架实现、R修改或未获授权的optional／policy更改；保护检查只能报告检查所覆盖时点和路径。

在获准的实际报告／修订分支按正常push发布，发布成功须以真实远端对象及每一新增载荷完整回读确认：比较原字节／bytes／SHA256／git blob／mode／type／path、关联commit和目录tree，核完整清单与未声明差集。push超时、进程exit0、远端只存在branch或本地remote-tracking ref都不单独等于每载荷回读成功。保留失败及普通retry，禁止force／删除或把本地对象身份预写成远端成功。

manifest不递归自哈希。先冻结有限语义载荷core C，再由独立的有限发布／交接载荷绑定已实际存在的C和其tree；manifest可明确排除自身，整个Git tree由外部实际对象绑定。最终发布P与P内载荷的核验由外部回执或最终响应记录，不要求P内文件预先含自身commit／目录tree，也不为追求自引用闭合无限重写、重commit、重push。只读回读实际内容，最后报告真实C／P／路径／载荷身份和未闭合发布条件，不制造下一轮虚假identity来消除未知。

持续执行至已获授权的全部修订、独立验收与交付目标完成；跨上下文保留原目标、实读范围、保护约束、原始失败与当前未闭合工作。状态提问或新信息按当前任务的steering处理，回答后继续必要工作；只有明确取消／暂停或不兼容的新目标才替换任务。可完成的静态工作不因缺宿主、长上下文或任务规模提前收尾。完成报告必须自足，读者能从逐ID完整合同和实际证据恢复结论，而不是依赖聊天摘要或“全量PASS”口号。
