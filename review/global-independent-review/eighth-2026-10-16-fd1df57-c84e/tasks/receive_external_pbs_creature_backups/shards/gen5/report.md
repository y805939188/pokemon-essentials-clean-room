# 第八轮有限剩余接收 pbs_gen5

本组独立可完成的主读与有限语义接收已完成；任务状态为 **INCOMPLETE**，仅三个完整接口 IF01、ELR-I03、CD-I06 尚待真实跨代 producer 及外域累计接收。没有据缺席的贡献签完整接口，没有新增已成立的 required、optional 或 policy 提案。此报告交原接收者和主审累计整合，不增加审查层，不签 root canonical/task-final。

## 1. 合同、实际身份与保护范围

固定合同为 `30afe79aabc084e3baf9842cb87b90acbc5c6d0a`，合同 checkout tree 为 `2daa299ea92fe891294c96b4ea15e2c5717f9a4d`。B8 为 `fd1df570cad987dc3852a3b958f03916e317f7fe`，其正式规格 tree 为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`；R 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，tree 为 `7589c800b61ba13a13040ed0d686979b80a84fd0`。

唯一目标作者提交为 `b6f12ecfbe006ef0f2ea463d6689d78094915e75`，原 checkout tree 为 `fd4d9ee5b2abcd583cd9e180c3f0502e7172e58e`，原任务 tree 为 `b840da3155ee4ade9414e313061f38a188f5ba3b`。复用父发布 `bf36d6c3e5b8323d530155fc68ac6a4249336f66` 中已恢复的精确原件；父语义 core 为 `7ebc431b1cc47d2c41cba2506512ce20c1f4ca84`，父合同为 `40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232`。32 个原件均重新核对 bytes/SHA/blob；身份核对不授阅读信用。

实际平台环境的 CODEX_THREAD_ID 与 CODEX_SESSION_ID 均回显 `01a144a2-cdca-74e0-a8b6-5f8e90d95021`，不同于目标作者 `01a143b3-2169-7510-89e4-e6e3c9712029` 及父接收上下文 `01a14465-b40a-7432-ba2a-27fb50ffa001`。独立性依据是实际回显，不是角色名称或 git user。没有自行 spawn。请求配置为 gpt-6.1-sol / ultra / default / normal / Fast off；实际 model、effort、tier、speed、Fast 均 **UNVERIFIED**。

实际开始 UTC 为 `2026-10-16T12:19:46.676416+00:00`；完成阅读和报告的实际时刻、进程状态在 `progress.json`。平台入口为本派发的 `/root` 与选定执行环境。唯一写集是本目录；唯一发布分支按用户最新明确指令为 `codex/r8-final-pbs-gen5-20261016`，替代旧 prompt 的 `codex/r8-receive-pbs-gen5-20261016`。没有修改正式规格、R、公共账本、其它片、main、tag，也没有整改或 TS 开发。**UPDATE_NOT_STARTED**。

项目根及本目录全部祖先的适用 AGENTS 已读取；派发入口、共同前提、全局 prompt、review-SKILL、父 readset、保留接收及本片完整 readset 已按实际业务对象接收。review-SKILL 对审计报告保留其既定审计记录规则；没有把最终正文修订规则用于抹除失败或历史资格。

## 2. 覆盖、完整阅读及可恢复材料

| 人口 | 本次主责完成 | 必要未接 |
| --- | ---: | --- |
| P02 基础原文 | 649 / 649 | 0 |
| P03 形态原文及同代基础接合 | 86 / 86；涉及 24 个基础 | 0 |
| 显式字段绑定 | 15811 / 15811 | 0 个本代字段绑定 |
| 省略/默认/继承处置 | 12137 / 12137 | 0 个本代处置 |
| 独占原子断言 | 17 / 17 | 0 个本组原子 |
| 头声明 | 1 / 1，HC-BASE | 0 |
| 完整接口 | 0 / 3 | IF01、ELR-I03、CD-I06 |

这些人口分别计数，不能相加成一个 PASS 分母。四个字段合同中的断言别名不另加票；必要共享定义的重复读取也不增加主责人口。

P02 的 16902 行与 P03 的 381 行全部实际显示并读取，包括每一个 Moves、TutorMoves、EggMoves、Evolution 的完整有序值、重复项与每篇完整 Pokedex。P02 先按连续区间读，再与 P03 全部形态接合；没有抽样或只看名称。首次 5 MB readset 大输出和若干组合输出曾截断，未据其认定完整；所有本次采用的缺段均补读，凭证、修复区间及未采用的外域部分保留在 `reading-ledger.json`。Info 页旧 locator 未含最后结束行，已补至实际完整定义第 300 行。

全部原 forward 业务结构以可逆字典呈现：`forward-field-dictionary.txt` 保存原字段顺序，`forward-omission-dictionary.txt` 保存全部政策/基础锚规则，五个 `forward-000-150.txt` 至 `forward-600-735.txt` 保存每条身份、节、行界、字段/省略模式、参数数及具体基础锚，均已实际读完。原字段 hash、重复 locator、输入 tree/blob 是完整性或定位字段，未充当业务文字。完整原对象仍固定在合同 readset 的各 `/owned_records/N/complete_target_forward_object`；本次逐条决定不继承原作者 local_status。

`record-reception-ledger.json` 对 735 条分别记录坐标、字节 SHA、完整原对象入口、四个主责字段的完整原值、判定理由与有限消费者范围；86 条形态另逐属性列出实际基础值或自身默认。全部原始字面数据保存在两个小型无损视图：`views/P02-literal.txt.gz`、`views/P03-literal.txt.gz`。恢复方法为标准 gzip 解压；解压后依每条 `byte_offsets_half_open` 取单元，再核 `source_unit_sha256`。它们恢复原 PBS 字节，含 BOM、换行、完整列表和正文；不是运行结果或规格正文。`identities.json` 保存原文件及所用源/正式条款的固定 commit、mode/blob/bytes/SHA。

## 3. 本代记录的具体语义接合

基础记录的 Name、Category、Pokedex、Generation 均有显式原值。Generation 是出场代描述：例如前代记录仍保留其 1–4，末段是 5；不因备份名把所有值改成 5。图鉴中的历史、物理、战斗叙述仍是可本地化描述，不自行转成新机制。源中 NORMAL 的 Clefairy、Mawile 的 STEEL、Mandibuzz 的 SPECIAL_ATTACK EV、图鉴拼写等均按冻结值接收，没有用官方资料纠正候选数据。

全部学习表按出现次序接收。例如 Mew 的完整教学表、Smeargle 的重复 SKETCH、同等级的拳/气候招式、Reshiram/Zekrom/Kyurem 的重复 IMPRISON、Feebas 的两条 Evolution、Eevee 的七分支及 Tyrogue 的三分支均未去重为摘要。字段语法允许什么、编译如何规范化、真实学习/进化消费者怎样选择是不同观察点；本次没有把原列表存在当成已经学会或进化成功。

形态逐一使用 Gen 5 的实际基础记录，而非当前主 PBS 或其它代同名记录。详细全部值在 ledger；以下为必要差异和普通对照：

- Unown 各字母与标点保留独立 FormName；26/27 显式 Generation=3，普通字母继承基础 2。Pichu,2 为 Generation=4，保留 PIKACHU/None 声明；没有把 None 解释成可触发进化。
- Deoxys、Wormadam、Shaymin、Therian 三者、Kyurem 与 Meloetta 的六能力、EV、类型、能力和完整学习表按各自覆盖/继承逐项接合。身高体重的编译单位为十分之一，显式值先乘十取整且至少一；继承取已规范化基础值。
- Rotom 五形态只覆类型和名称；能力值仍来自本代基础 `50,50,77,91,95,77`，未补官方形态数值或专属招式。Genesect 四 Drive 只有名称覆盖，仍继承 BUG/STEEL 等数据；季节名称也不自行执行变形逻辑。
- Arceus,9 保留 QMARKS；Arceus,16 自身完整 116 项教学表，其余相应形态继承基础的 115 项。Kyurem,3/4 明确 PokedexForm=1/2，却缺 FormName：结果是自身 nil，不能从基础或 White/Black 形态补名称。
- 三档持物全缺才共同继承；Basculin,1 自身 uncommon=DEEPSEASCALE，使另两档为自身空池。重复相同三档原值也分别保留，没有折成独立概率三次抽取。
- FormName、PokedexForm、MegaStone、MegaMove、UnmegaForm、MegaMessage 采用形态自身默认；十六个标量、十类集合、嵌套学习/进化列表及三档持物分别按完整定义处置。Evolution/Evolutions 是一个逻辑字段，缺少另一拼写不等于清空已显式的逻辑列表。

`property_resolution` 记录作者输入和继承来源。编译终检还会按完整登记表转换进化参数并合成前驱；它不是编译后整图快照。所有枚举、其它必要输入和较早阶段先成功、无插件覆写是条件前提；没有宣称整个备份实际可完整编译或跨代兼容。

## 4. 四合同、十七原子与头声明

| 原子 | 独立接收的当前意义及证据 |
| --- | --- |
| FC01.grammar/default/form/consumer | 基础 Name 的活动语法是 s，缺值为 Unnamed；形态不开放 Name 并按 nil 继承基础原名。Species.name 经 SPECIES_NAMES 查译；Pokemon.speciesName 取实际 species_data.name，显示名不替代内容身份。 |
| FC30.grammar/default/form/consumer | Category 在基础/形态均是 s；缺值 ???，形态继承具体基础。基础终检 set、形态终检 add SPECIES_CATEGORIES；getter 与 Info 的拥有门分别核对。 |
| FC31.grammar/default/form/consumer | Pokedex=q，但先经行预处理删首 # 后缀及端部空白，引号不保护井号。缺值 ???，形态继承实际基础全文；基础 set、形态 add POKEDEX_ENTRIES。查译不保证返回字面原文；Info 只有 owned? 为真才请求正文显示。 |
| FC32.grammar/default/form/consumer | Generation=i 是严格有符号整数，构造缺值 0；本组显式值不收窄通用语法。形态显式值优先，否则继承本代基础。出场代、机制世代常量、作者选择数据是三种输入。 |
| G32 | 全部保存取值/类型校验先于目标文件打开；更早回调或调用者内存副作用不会因此自动回滚。覆盖打开及 Marshal 写入、逐值装载、转换回调与写回均不构成全图事务承诺。 |
| HC-BASE（单列） | 新节身份语法 m；普通编译在完整本节校验后拒绝已存在身份，先前登记前缀不自动撤销。所有记录仍是条件备份作者实例。 |

活动解析器是 `get_csv_record` 的 split/cast/checkEnum 链，未以文件中旧 unused 解析器代替。通用编译、基础/形态编译与各自终检、GameData 登记/存取、物种反写、顶层发现/完整编译/启动清理的必要真实定义均读至结束；来源范围在 ledger。对应当前 WP02/WP03/WP04/WP18 明确身份、schema、备份选择、继承和非原子前缀。WP08 的必要 hash set/add/get 定义与调用、WP62 Info 文字/拥有门也已接合。

原四条 default 断言使用了通用模板措辞“base/explicit metric record”。本次按各 FC 的所属 Species、对应 schema 与构造定义接收默认值；这个短语不提供 SpeciesMetrics 的额外字段或默认事实。其最强有限解释由原字段合同的 BASE_ONLY/BASE_AND_FORM 及 D01 定位支持，不能扩成 metrics 接口已收。原文保留在逐原子账本并附此限定；没有据模板用词新增正式规格整改。

本地化接合还保留默认 core 规范键过滤、set 替换和 add 保留旧 game 的差别、缺值候选与空候选，以及运行时当前语言 game→core→原文的查找链。空译是有效命中，不能借缺译正常回退推出导入、盘写或整个 UI 已执行。Player.owned? 的包装及 Pokedex.owned? 归到基础 species 身份、仅布尔 true 才算拥有的必要定义均读完。

G32 不沿用原对象“foreign formal pending”作为本次自动结论：本次直接读取 D40–D43、完整 Game.save/读取/转换必要定义及当前 WP09/WP10 必要条款，形成独立有限接收。正常路径的 17 项取值/校验在 open 之前；Game.save 更早已写 safesave、计数、magic、时刻。类型错误不在其 IO/系统调用捕获集合中；相应错误分支只回退计数而非全部状态。转换先写内存快照到默认 .bak，再顺序执行和版本更新，成功转换后写回读取路径；无转换时不写该转换备份/写回。回调、装载、备份、覆盖盘写的失败前缀分别保留。没有扩展接收 WP10 §4 的逐项旧转换目录或完整外域保存接口。

## 5. 正反证据、相邻例与裁决

正向从四字段及 G32 的固定源定义对到当前 WP18 §3.1–3.2、WP03 §3–5、WP04 parser/编译/反写、WP08 hash 文本、WP09 §5、WP10 §3；反向按这些必要条款回查真实调用者和前提。逐原子映射在 `atomic-reception.json`；逐记录映射在 ledger。未把未使用的整份外域文档算作已验证，也未把所有共享源定义当成新的全系统 review。

静态例与预期的最强反证是：顶层普通输入与备份目录分别观察；AlphaBeta 对 Alpha#Beta 及引号包围井号；形态三档全缺与只给一档；Kyurem 有标签与仅图鉴别名；正常保存与回调/校验前失败、open 后失败、逐转换中失败分别观察。当前规格已有相应边界和合理范围，不成立新增 required。对应 KC、KL33–35/KL46–50、LZ、SV10/11/17、MG03–05、CI25 的必要向量文本已读；**没有运行向量**。

新 required=0、optional=0、policy=0、material-limit=0。尚未接完 producer 是接口真实缺口，不归为正文缺陷或宿主材料限制。没有产生需要另一个上下文反证的新提案，未由提案作者兼任唯一独立反证者。

既有 2772 字面记录、20 个有限命题、IF04/IF06 及 XPCB001 的有限 NO_REQUIRED 保持父合同中的原 reader、范围与前提；本次没有把它们算新阅读或新投票，也没有降级。XPCB001 仅保留其精确正常 Symbol 注册路径/map-version/条件 Area 的既有反证资格；未重审 Encounter/Area，未越过 compiler 658–765 或 UI 302–352 的强制后继更正签新断言。第七轮 27 项及历史 optional/FLOAT/policy/limit/no-required 的分别资格保持不变。

## 6. 接口真实缺口与直接交接

| 接口 | 本次已收 | 必要待收 |
| --- | --- | --- |
| IF01 | 本组 735 原始实例；发现、显式激活、schema/登记/编译/反写/载入及 G32 的必要共同定义与当前条款 | Gen6/7/8 逐字段 producer；KERNEL/DEVELOPER 的原接口累计实质接收与适用更正 |
| ELR-I03 | 本组两份 PBS 的完整 Name/Category/Pokedex/Generation、默认/继承及 set/add/get/拥有门接合 | 其它代际逐字段事实；原 35 份 PBS 所属 PBS_CURRENT/BATTLE/WORLD 等 producer 的真实累计接收，原读者个人未读资格保留 |
| CD-I06 | 本组完整作者值与必要 parser/compile/export/default/backup 激活定义 | 其它代际逐字段事实及 KERNEL/DEVELOPER/PBS_CURRENT/BATTLE 等必要消费者/producer 接收；未接的 Encounter/metrics 不作自动通过 |

本次针对 `codex/r8-final-pbs-gen6-20261016`、gen7、gen8 的精确只读远端探测均无匹配 ref（exit 0；最近凭证 dddd57）。这只证明本次未取得贡献，不证明其它 context 未启动或未来分支不存在。没有用未来 HEAD、同名状态或路由名单编造 producer 事实。provider_entrypoints 只作固定导航/可得性，不继承其 PASS/FULL；直接读完的共享定义只承担本组必要前提，不替代外域未读业务。

供原接收者/主审直接继续：按本合同 `incoming_peer_contract` 接收其余三片的精确提交、逐字段完整值、省略/同代继承、读片凭证与限定，再依本报告 `interfaces.json` 的三条分层接合。外域原接口完整对象均保留在该 JSON，不需再构造一轮审查。可得但未接的外域 producer 明确是 OPEN_NOT_RECEIVED，不能改写为材料或宿主 limit。本组主原文、字段绑定、原子及头声明没有剩余未读对象。

## 7. 执行与限制

参考编译、反写、游戏、保存、转换、宿主/媒体、行为向量均 **NOT_EXECUTED**。自写 Python 仅做静态身份核对、视图与报告整理；gzip 回读、计数、Git tree、远端传输验证均不授语义信用。没有执行恢复的旧脚本。原作者的执行/I/O/失败与旧更正保留于固定原件，不倒填未知 exit 或输出。

私有平台 chunk ID 是实际显示/读取定位，不是公开的完整终端流。公开投影是本目录的完整 PBS 视图、可逆 forward 视图、逐对象 ledger 和固定身份；未声称原私有流已远端回读。真实的无界插件/宿主运行、完整备份组合兼容仍无执行证据；这不豁免本组可读原文或必要定义。

## 8. 交付与发布边界

主要入口：本报告、`progress.json`、`identities.json`、`reading-ledger.json`、`record-reception-ledger.json`、`atomic-reception.json`、`interfaces.json`、`proposal-counters.json`、`execution.json` 和 `views/`。语义 core 先冻结；后继 `publication/` 绑定实际 core/checkout tree/本目录 tree 与逐文件完整回读。自身未来 commit/tree 不写入自身文件，最终发布身份由最终回复收口。

用户已授权普通报告证据 commit/push，只发布专用分支。发布核对仅针对本组新增报告和完整载荷，逐文件核 path/mode/blob/bytes/SHA/集合与目录 tree；两个 gzip 还核解压后的原文件身份。不合并 main，不强推、不动 tag。最终状态维持 **INCOMPLETE / UPDATE_NOT_STARTED**，接口完整性由真实后继贡献及主审累计接收决定。
