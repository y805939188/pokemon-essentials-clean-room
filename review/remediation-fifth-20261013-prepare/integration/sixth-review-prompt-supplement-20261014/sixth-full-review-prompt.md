# 第六轮全量双向独立全局审查完整中文prompt（本地路径、调度与云端整改交接合同补充版）

状态：第五轮远端main发布、准确交付tag、25候选分支保全及退役已完成；第六轮尚未启动。以下内容身份已填实，用户在父任务同步并核验本地项目后手动启动本prompt。不得自动启动或以旧B5/临时分支名代替固定输入。

审查的正式项目输入是固定main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`，不是后继整改分支上的行政report/prompt commit。父任务已给定本地项目 `/Users/dingshinn/Desktop/pokemon-framework-reference`，参考为项目内 `reference/pokemon-essentials`（绝对路径 `/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`）。启动时用这些准确入口逐项只读核Git身份、dirty/untracked和内容分母；路径缺失或身份不符时登记实际差异，不能reset/移动分支、换另一个clone或假已读。

| 固定输入 | 已填实值或本地定位入口 |
| --- | --- |
| 本地项目仓库 | `/Users/dingshinn/Desktop/pokemon-framework-reference`；核实际git根与origin `y805939188/pokemon-essentials-clean-room`，先检查所有适用AGENTS/skills |
| 正式主分支commit | `8ea169fbd0f33f378b5d732fd6bea59e854e04a6` |
| 对应workspace tree | `6ab3429170d2762607fbc2237014c3a160449fa1` |
| 对应正式131目录tree | `1046fbb657882e84b3dfc6d017943a9edf7782e5` |
| 准确交付tag | `refs/tags/delivery/fifth-round-closed-final-20261014` → `8ea169fbd0f33f378b5d732fd6bea59e854e04a6`（轻量tag，禁止retarget） |
| 最终主分支发布/清理报告core | `b67f542b47ad33ac23053a21f62748077c167a23` / tree `e5fa5de69c1e3164597815a42776aa859c6ea4b7`；[完整发布回执](https://github.com/y805939188/pokemon-essentials-clean-room/blob/b67f542b47ad33ac23053a21f62748077c167a23/review/remediation-fifth-20261013-prepare/integration/final-main-publication-20261014/publication-receipt.json)；同目录 `final-main-report.md`、`remote-cleanup-receipt.json`、`main-publication-readback.json`、`local-sync-and-recovery.md`、`package-manifest.json`（共6载荷，全量远端读回已验证） |
| 当前唯一92关闭回执与原证据索引 | 项目main内 `review/remediation-fifth-20261013-prepare/registration/successors/20261014-final-activation/activation-receipt.json` 与同目录 `report-index.json`；精确沿用旧选择对象，独立审其当前解析，不自动继承语义PASS |
| 本地只读参考仓库 | `/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials`（相对项目为 `reference/pokemon-essentials`），来源 `Maruno17/pokemon-essentials`；只读并核下一行固定R身份 |
| 固定参考R | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；原tracked432，启动时独立核inventory |

启动门：项目HEAD必须准确为固定main、正式目录tree准确、origin/main和交付tag按父任务同步时点与固定身份核对，R的commit/tree准确。若远端或本地后来变化，列差异并明确冻结范围，不自动追新head或覆盖既有工作。最终发布报告6文件属于行政与证据输入，须完整读取并准确处置，不当游戏语义来源。当前源/正式/有效补充清单由本次独立建立，不能用历史432/131和旧未审0直接宣告本轮阅读完成。

本地同步输入在固定报告core的 `local-sync-and-recovery.md`。62候选原字节、所有原环境和未发布成果保持；不因25远端别名删除而删除本地工作树或释放环境。远端保留四重要分支、149历史tags＋25本轮archive tags＋1准确delivery tag共175；已退役作者/审者历史均从具名archive根恢复，旧SHA文本不等保存根。

第五轮重要追溯点：B5 `9366d9d17aaeac3b4414236468affa650fb3dd27`；语义全局报告 `c0ff33024aea424c68d29f9778fe7c8e807d21e8`；其发布 `f49d870c6fd616ab6736754a218a4553b5acac7f`；U08 actual `e9f7590e68347849450fd5cbdba538e605cda0a7`、actual报告 `debf59f3c5370df253706969fd4dd1c103300bf2`；已审关闭候选 `13fddb0a217b36974c75657aa68da0caf104ee48`、关闭报告 `044c3483229e7e76bedf1fc244fc84d274bf059c`；唯一激活 `12df95a8e81061a606d50d3f0a0528793b2e6b2c`、发布 `0378dc85cab61642ca1467e5a901b3c829df976a`。这些是历史/精确资格索引，**不得继承为本次新全局语义PASS**。

---

你是第六轮独立全局 reviewer。请使用 **GPT-6.1 sol / ultra / default普速，禁Fast**，用户将手动在本地启动本任务。实际model/effort/tier/speed或task UUID未回显只标UNVERIFIED，不检查额度、认证或反复追查模型配置。这是新的独立审查任务。主会话可亲自review、提出发现或做独立反证；必须登记各实际角色，不能由发现提出者自证为唯一独立反证。对自己曾写过的具体规格范围，要由独立非作者核验其最终裁决。Git账号、父线程引用和请求参数不能伪造真实task或实际模型回显。

目标是对已经清理、同步并冻结的正式规格做**完整、全量、双向、独立的新全局审查**，为后续从零实现提供准确行为规格。不是抽样检查，不是仅验第五轮92整改项，不是diff-only或关键词覆盖，也不沿用相同blob/旧PASS跳过本轮语义阅读。不能实现新引擎、移植Ruby代码、设计原类结构对应的新框架，不能把参考当架构/源码模板。战斗/AI全部保留；未来可能采用Showdown不缩本轮事实或规格审查范围。

## 项目目标、历轮背景与本轮问题类型

项目目标是形成完整、准确、可从零实现的功能与逻辑规格，覆盖Pokémon Essentials的可观察行为、数学、状态、数据、配置、用户流程、失败与接合。本轮交付是规格审查事实和后续最小修订合同，不是新代码。未来以TypeScript从零建设现代框架；参考Ruby实现只提供行为证据，不能照搬源码、类层级、宿主或旧架构。完整战斗/AI仍在范围，潜在Showdown选型不自动缩减要求。

历轮闭合为定位与回归资料，不是本轮新PASS：

| 阶段 | 既有工作及当前资格 |
| --- | --- |
| 第一轮 | 逐WP进行审查与修订；各原WP合同、主合同primary映射与其当时范围须保留。此处不臆造第一轮问题总数。 |
| 第二轮 | 229个控制项，21个整改批次；精确owner贡献341的口径单列，不能把229/341/21当同一种分母。 |
| 第三轮 | 23个控制项，76标准；optional/no-required及其历史U08未启动时点保留。 |
| 第四轮 | 当前资格17控制/76标准；B5时原16/75与Summary残余后来补充的时点、来源和范围分别保留。 |
| 第五轮 | 92必修（51P2/41P3）有效CLOSED、OPEN0；7optional、7no-required、6独立兼容政策、13限制独立分母。410原native静态、568原schema与158额外单位分列；21共享限定回执、18依赖、85solewriter及262原贡献＋6行政transfer＋3纠正保持准确口径。 |

当前重点包括源事实漏覆盖、反向clause无根据或过强全称语句、调用/receiver/注册/覆写/配置接线差异、producer→write→consumer→display→persist断链、正常与异常/取消/部分提交不同、内存/PBS/导出/重载身份混用、资源请求冒充宿主输出、跨正式共享文件矛盾、primary/ID重复、旧回归范围丢失、向量冒充执行以及旧生成台账冒充当前关闭。既有SC捕获体LF错误、U03旧FAIL、U08旧G03/G09 FAIL和两MISMATCH必须保留其准确历史；不能把这些关注点变成抽样范围或只查旧92项。

本轮仍须全部R、正式131与有效补充的新双向实读；可审有限材料未审0仅代表该明确分母闭合，不能推宿主、资源、机器码或无界配置运行通过。

## 已授权的本地review、执行与远端报告发布

用户已授权在本轮review范围内读取上述本地项目、只读参考及必要相关材料，执行必要的本地解析、静态工具验证、对照和安全隔离参考/独立模型/可用宿主或Demo观察，并在独立review分支普通发布报告。例行授权范围内读/执行/报告发布继续完成，不逐项重问。执行必须绑定固定输入、隔离临时工作目录和安全可控作用范围；先读执行对象及依赖，不盲目运行未知下载脚本，不改真实存档、生产账户或项目/R原文件。

所有授权仍受系统/平台权限与安全规则约束，不能以本prompt绕过具体拒绝或安全边界。缺兼容宿主、工程、资源或安全运行条件时如实登记限制，继续可独立完成的静态审查；不得安装/改系统安全配置、访问未授权外部服务或将空白环境伪装运行验证。原始成功/失败/替身/命令/时间/exitcode/stdout/stderr均保留，exit0不等业务成功。

写集只有本轮独立review根、分任务证据和必要临时检查文件。禁止自动整改、改正式规格/planning/audit、实现TS/Ruby引擎、改R、改main/tag、force、删分支、释放原环境或丢未发布成果。完整云端整改交接必须准备好，但云端update启动不在本review自动执行范围；最终明确 `UPDATE_NOT_STARTED`。主会话无需为生成完整交接资料等待额外许可。

## 启动与冻结

先完整读取本地根及适用目录的AGENTS.md，检查 `.agents/skills` 与相关已提供skills；明确实际适用说明和读写边界。用户既有授权优先于技能建议。只读核项目/R的commit/tree、远端主分支及交付tag、dirty/untracked状态、正式目录131身份及所有有效补充材料来源。不要reset/删除/覆盖已有或未发布成果，不碰R，不用移动分支头来掩盖输入不一致。

以下Git内容身份和本地路径已填实；从 `/Users/dingshinn/Desktop/pokemon-framework-reference` 与 `/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials` 只读核对，不以当前CLI的偶然cwd替换输入。创建本轮唯一审查根 `review/global-independent-review/sixth-<YYYY-MM-DD>-<main-short>-<nonce>/` 与独立报告分支 `codex/review-sixth-<date>-<main-short>-<nonce>`。写集只限本轮独立报告/证据；不修正式、planning/audit、R、旧报告、第五轮关闭回执、main或原历史字节。报告普通push可按用户授权进行；不force、不merge main、不删分支、不归档释放环境。

## 全量清单与真实阅读

1. 独立建立R全部tracked文件清单，以及项目正式131和当前有效补充材料清单，记录commit/tree、path、bytes/SHA256/Git blob、类型、用途和实际阅读/解析范围。核分母，不用历史432/131覆盖新增或缺失材料；相同定义的生成副本可精确关联，但原载荷及其有效语义仍须纳入本轮完整审读范围。
2. 所有可得且可审文本、脚本、PBS/default/backup配置、作者工具、可安全恢复的序列化内容、资源/二进制可读嵌入程序及其实际消费者都须全文/全结构覆盖。大文件按结构/行区间/字段表/入口拆分完整读，不反复向上下文倾倒全文，不用“读开头/只看修改行/检索出现关键词”冒充全量。
3. 许可/纯行政/历史快照/生成导航按真实用途完整读或做完整类型/身份处置，不作为游戏语义或法律结论。有效补充中的案例、向量、依赖、数据契约、覆盖声称、当前状态字段要独立核事实；旧生成时点和现在的激活状态分层，不能把旧OPEN/WAIT误当当前未闭或以新CLOSED回写旧时点。
4. 维护file→unit→fact→consumer→spec与spec-clause→source-fact→premise两向台账。每个可得语义单元有具名处置；无法安全恢复/不属于当前可读语义/宿主未建等明确列边界，不能填假已读或假行为PASS。最终可审文本/有限可读单位的未审应为0；这不等于全部机器码控制流、原生GPU/音频/字体/序列化宿主或所有动态配置已验证。

## 正向：参考→规格

按实际完整定义和上下文提取可观察行为、能力、规则、状态转移、数学、输入/输出、前置、数据/config要求、用户流程及失败边界。逐入口核定义、默认和备选配置、注册/覆盖/分派、caller、真实receiver、生产→写入→消费→展示→持久、缓存/别名、取消、异常/部分提交和后续结果。没有默认caller的定义不能免读或推“无功能”；有定义/名字/字符串不等于游戏实际接线或宿主选择。

每个参考事实要映射到当前正式独立行为合同，或被明确处置为合法超范围、历史/纯管理、optional、独立兼容政策、材料/宿主限制。对未覆盖或反向断言形成具名gap与最小反例。不把源缺陷修成理想行为，不默认新实现必须永久保留缺陷；事实与是否要求兼容分开。

## 反向：规格→参考

完整读当前每份正式规格的所有章节、段落、表格行、脚注、附录、规则、算法、状态、配置、失败语句和测试向量，逐clause标识根证据、前提、观察点及边界。核存在性、顺序、条件、数值/舍入/时钟、身份/单位/命名、容量、别名/复制/可变值、存档/档案/PBS/内存差异、缓存、回滚/部分提交、取消、异常层级、资源请求与最终画面/听感等实际差别。

特别检验“必然、任何、全部、无写入、只读、无副作用、原样往返、统一失败、原子提交、失败全回滚”等全称语句。不能由静态请求、catch后exit0、方法/导入名、相同blob、许可或旧PASS推出业务成功或运行等价。发现过强/错误/过窄/前提遗漏/同一事实多套相矛盾规则，应具体定位当前clause和参考反例。

## 接合与跨模块

完整建立领域接口/primary identity、producer/write/consumer/display/persistence/failure关系；逐有效接口和组合链检查输入输出、身份/单位/状态/时间/能力门、注册/编译→使用→显示→保存/重载、成功/失败/取消/部分提交的接收。所有共享当前正式文件要完整读，不用逐片段PASS推出整篇一致性。

覆盖Generic Kernel、Creature-RPG、Pokémon Rules、Combat/AI Requirements、Engine/Overworld、UI、Demo/DX、资源/可读binary与作者工作流各领域。把主因/必要同步正文、附表、向量和反向consumer连成精确修订范围，别只修一个入口。跨域重复事实只留具名主合同与引用，不重复发明同一mandatory ID。

## 旧资格与第五轮关闭

第五轮有效92 CLOSED由唯一激活回执选择同一已审候选proposed状态，旧台账的current_effective OPEN、候选WAIT及旧生成导航保持原时间。独立核当前有效接受/关闭解析正确、ID分母与scope/exclusions一致；不随意重开或删旧记录。

对第四轮17控制/76标准、第三轮23/76、第二轮229控制/341精确owner贡献和本次影响旧交界/链，按原qualified范围做新当前对照：历史PASS只供定位，本次当前结论须由新全局读源/读clause支持。保留R4在B5时16/75及Summary残余后来有限补充的时点；GR3-M09-001历史optional/U08未启动、GR3-M02-003 NO_REQUIRED不冒充第六轮mandatory。保留第五轮candidate01 G03/G09 FAIL、U03旧FAIL与定向修订、两advisory MISMATCH；SC-U07-001原错误capture-bodyLF字段不能复活为当前事实，准确不跨体内LF/外围空白/独立合法整调用行及整字段丢文分别核。

## 主会话调度、并行与CLI可见追踪

主会话负责唯一调度入口、公共台账、分母、依赖、跨域接收、主因去重/裁决、整合和交付；可以亲自review一个或多个具备实读条件的范围。公共状态不得被各任务同时覆盖。不能把“主会话”局限为转发，也不能用根会话参与替代领域证据或非提出者反证。

允许多个subagent或多个Codex Desktop独立会话；全部请求 **GPT-6.1 sol / ultra / default普速，禁Fast**。所有具备独立读写条件的任务可并发，无用户数量上限；遵守实际工具容量。使用当前环境真实可见的工具/CLI/会话入口，先核一次支持的参数和状态接口，不臆造CLI flags，不通过反复查额度/认证或换模型凑证据。实际model/effort/speed未回显仅UNVERIFIED，不停住其它审查。

每个任务必须具名：逻辑入口ID、任务/范围、负责人角色、实际agent/session/task入口ID（有回显才写）、所请求模型设置、实际回显状态、读集、独立写目录、冻结输入、依赖、状态、日志/结果路径、开始/更新/结束事件。逻辑ID与真实平台UUID/会话ID严格分列。task-registry可有 `PLANNED/RUNNING/WAIT_DEPENDENCY/COMPLETED/FAILED/INTERRUPTED` 等真实状态，不能将计划任务标运行或完成。

CLI必须有可查看的入口ID、任务、状态和日志。优先使用平台实际提供的状态/日志命令，并保存其真实输出；同时在review根提供 `task-registry.json`、`task-events.jsonl`、`logs/<logical-id>/` 与可实际运行的 `task-status.py`（或等价CLI入口），让用户能够列任务、按ID查看详情和打开/尾读实际日志。实现后演示该真实命令及输出。若平台缺实时活动/UUID接口，在对应字段明确UNVERIFIED/接口不可用，保留具名本地逻辑入口、真实启动/退出/可见日志和最后更新时间；不能用本地JSON伪造平台实时状态或实际模型回显。

并行必须覆盖完整领域与全部有效接口，不按几个关键词抽样。每个任务只写独立目录；原源/正式只读。提出者与反证者分离；需要共享数据的任务可以读同一固定资料，但不能多写公共台账或一个报告文件。主会话跨域去重后仍保留原各发现和反证链；若同一正式范围由旧作者本人参与，非作者终审的责任与证据须具名。缺依赖只隔离依赖范围，继续独立可得工作，真实缺读不得填未审0。

## 独立反证与并行分工

可按具备独立读写条件的完整领域并行工作，无用户数量上限。所有任务请求sol/ultra/default普速禁Fast；每个子任务独立目录，只读正式/R。角色分离：领域事实提案、非提案者反证、跨域接收者/历史/覆盖核验各具名；根reviewer整合但不能靠角色数量或hash通过代替必要实读。

每条疑似发现给固定source/spec路径与精确行/offset/字段、原前置、普通对照、最小反例、失败/取消/部分提交、负证据搜索、必要消费者、预期/当前差别、影响、最小修正规则、必需同步/向量范围、原来正确scope须保留项、未知与excluded claims、证据等级。独立反证后裁为required、optional、no-required revision、独立policy或limit；不能把待决兼容政策强塞mandatory，也不能以“无默认caller/无运行环境”免除可判定静态事实。

## 材料、资源、二进制及执行边界

13历史限制不是本轮偷懒跳过材料的许可。重新核现有可得资料与可安全解析范围：Main49、messages数据、两根BMP、字体映射/度量/已编码字形、soundfont完整RIFF/hydra与参数链接、可读shader/兼容脚本/controller表、作者工具可读IL/导入/控制流等都按实际单位完整覆盖；若现有材料发生变化重新核分母与内容。机器码全部CFG、实际native版本/后端选择、GPU精度/采样/像素、音频合成听感、字体宿主、Windows窗口/.NET/RGSS、完整map/media/Demo可达、真实存档/网络及无界plugin/config组合等不由格式/字符串推通过。

### 13项已知限制逐项核对

下表完整沿用第五轮具名L01–L13作为历史恢复条件索引，来源为固定发布 `f49d870c6fd616ab6736754a218a4553b5acac7f` 的 `review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/limits-and-missing-materials.md`。本轮须按当前实际材料重新核可得范围与边界，不能继承旧“已审”跳过新阅读，也不能把已存在BMP/SF2/Main49/messages或可读IL/shader称缺失。新增材料或限制另给稳定ID并解释与旧项关系；policy与limit不塞进mandatory。

| 编号 | 已有证据 | 仍不能确定的事项及最小恢复条件 |
| --- | --- | --- |
| L01 地图与完整示例工程 | 可读地图/事件/解释器/编译/设施/开发工具脚本、PBS与具名静态调用均已按实际范围登记 | R没有完整地图、CommonEvents、System、Tilesets、Game.ini/Game.rxproj及完整项目资源。实际NPC/道馆/发奖/完整Demo可达流程需绑定来源与身份的相应工程材料；不能由源码能力存在推实际事件已接好。 |
| L02 图形与音频 | R根目录`knownpoint.bmp`和`selpoint.bmp`均存在，已解析全部64像素；已有字体、音色库、资源选择代码和尺寸/坐标请求事实 | 缺完整Graphics/Audio等资源。未验证实际图像加载、动画帧、坐标量化、音轨、叫声、混音或听感。两BMP存在不证明完整资源可用，也不能再称根BMP缺失。 |
| L03 原生执行 | 已检查本机现有Ruby/Python/Node与静态检查工具；没有为任务安装软件或变更安全配置 | 本轮未建立兼容Windows/RGSS/mkxp原生游戏宿主及.NET工具宿主。Mac上的隔离Ruby函数执行不能证明随附Ruby 3.1游戏宿主行为。恢复需可用的授权宿主、完整所需资源及明确的隔离执行方案。 |
| L04 Game与运行库 | `Game.exe`、`x64-msvcrt-ruby310.dll`、`zlib1.dll`存在。已检查PE结构、接口/依赖、可读内容的来源与范围；BIN对可恢复的兼容脚本、着色器、字符串分类和控制器表另有逐项证据 | 未对这些二进制的全部机器码建立完整控制流语义，也没有执行它们。可读定义不证明当前原生分派实际选中了哪个版本、后端、平台表或保护分支；不能由导入/导出名认定运行功能已通过。 |
| L05 可读内嵌程序 | BIN登记55份着色程序、可读兼容脚本及完整字段/函数投影，相关定义和宿主选择分别记录；其中数学顺序的新范围为可选GR5-BIN-001 | 未证明GPU编译、采样、精度、程序接线、真实像素或颜色输出。源码请求值与最终画面不是同一证据；不要求未来引擎复用原GPU架构或兼容类层级。 |
| L06 animmaker | RES/CRES读取15个方法的可读IL、控制流和异常分支；画布/矩形/缺图槽位/保存与失败前缀已形成条件事实。可选GR5-M12-202保留其证据范围 | 外部图像/XML库对空矩形、编码选择、错误格式化、文件失败的实际结果及真实工具输出未运行。不能把文档中的≤96当成实际验证门，也不能保证按扩展名一定输出PNG或所有失败均回滚。 |
| L07 extendtext | RES/CRES已解读实际工作循环、17个接口导入、四窗口/子控件请求、互斥量分支与150ms等待请求；可选GR5-M12-203 | 未运行Windows窗口系统；API返回未检查不等于请求成功。不能承诺实际窗口尺寸、精确150ms循环、目标进程所有权或工具自动启动。运行库启动余部没有被冒称全部语义已审。 |
| L08 字体 | 八份字体全部字符映射、表范围、度量/字形边界及全部已编码Unicode字形联系表已检查；默认字体名/尺寸/偏移和消费者另有源证据 | Pillow/FreeType联系表是资源检查，不是游戏字体匹配或实际UI效果。原生Font.exist/字宽/hinting、未编码字形及内部字节码执行语义未建立；需要目标字体渲染宿主验证。 |
| L09 soundfont | 完整RIFF/hydra字段、236预设、240乐器、505样本、采样点与1524链接已解析并逐类解释；配置明确选择此文件 | 原生加载接受、标称参数/末尾guard异常的处理、合成及声音不可由格式解析决定。SF2可得，绝非缺失文件；现有音频请求合同也不承诺完整采样器等价。 |
| L10 序列化内容 | `Data/Scripts.rxdata`的唯一Main已安全解码，全部49行按行为审查；两根脚本所带同字节版本有精确复用证明。`Data/messages_core.dat`以受限惰性解析器全量比对全部对应文本数据 | 解码没有执行序列化对象、启动游戏或证明原生载入。正文、键、字段结构核对不等于翻译语言质量审校。 |
| L11 动态扩展与配置组合 | 固定脚本中的入口、注册、覆写、配置声明/消费者、默认与备选PBS均按有限材料审查；不存在默认caller的定义仍有具名处置 | 动态插件、作者任意事件表达式、外部对象覆写、无界输入、所有配置笛卡尔组合和实际调度未穷尽。缺具体插件/事件材料时不能宣称无功能或已验证所有组合。 |
| L12 外部状态与服务 | 文件/网络/存档/归档的可读分支、返回/异常/部分提交可以静态解释；有限隔离执行单独登记 | 没有真实网络、真实用户存档往返、打包归档、生产账户或外部服务验证。捕获异常后进程exit 0不等于业务成功，空字符串也不证明请求已发出。 |
| L13 纯元资料 | 许可、追溯、旧审批、历史管理回执及生成副本均按用途和固定身份分类；当前有效语义字段另行审查 | 许可正文不作为游戏行为规格、不做法律结论；历史哈希与旧PASS不授予当前语义批准。只读开头的许可文件保持inventory_only，不伪称全文语义阅读。 |

初始新reference/model/host/Demo行为执行记0。若为必要边界新增安全隔离执行，先确定固定输入、命令、工具/替身、作用范围与输出，保存原始stdout/stderr/exitcode/时间/失败；允许在固定材料和可用兼容宿主中进行必要安全隔离观察；不改真实工程/存档或用生产账号，不安装改安全配置或触未授权外部服务。TOOL_VALIDATION、SOURCE_STATIC、DERIVED_VECTOR、REFERENCE_OBSERVATION、独立模型、完整宿主/Demo严格分开。历史R4隔离4和R5review隔离4不重算本轮新增；捕获错误的exit0不等业务成功，向量无运行记录不得包装为执行PASS。

## 最终必交：完整中文第六轮云端整改接手prompt与manifest

本节是本轮review完成时的强制交付合同。现在尚无第六轮发现或第六轮报告commit，不能把第五轮报告改名为R6、预填空发现为“0问题”或捏造后续report身份。review完成后必须实际生成可完整复制、可供用户另行手动委派云端整改的 `cloud-sixth-update-handoff-prompt.md` 和 `cloud-sixth-update-handoff-manifest.json`。不能只交final-report、链接集、短提纲、七批固定模板或“稍后补manifest”；准备交接的工作在本轮review授权内，但不启动update。

### 固定身份与交接来源

报告先冻结语义core commit/tree，涵盖真实inventory、reading ledger、正反矩阵、findings、反证/裁决、历史/接口对照、task状态/日志、执行与limits/policy证据。完整交接prompt/manifest在后继发布中绑定这个已存在core；填入准确repo、固定main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6` / tree `6ab3429170d2762607fbc2237014c3a160449fa1`、formal tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`、交付tag、固定R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，以及**实际本次第六轮报告core与发布commit/tree**。第五轮历史身份/准入资格作输入索引，不替代R6事实裁决。

core自己SHA不写回core正文；后继可绑定core自身，后继自己的commit/tree由外部固定Git入口/最终回复绑定，不制造递归selfhash或无限行政后继。报告新增载荷与完整交接载荷全部普通推送后逐文件完整远端读回，核实际bytes/SHA256/Git blob与目录tree；旧精确不变载荷可复用身份/传输缓存，不为行政登记反复下载1GB。传输/哈希PASS不是本轮语义阅读PASS。

### 每个稳定ID必须完整可执行

发现建立稳定ID，例如 `GR6-M01-001`；ID分配后不因排序/分批改号，去重合并保留alias/tombstone及裁决理由。required、optional、no-required revision、独立兼容policy、材料/执行limit各分类分母独立；severity依据实际影响及前提解释，不因运行未知自动升级，也不把oldGR5-ID当newGR6-ID。一个根因跨消费者以一个primary项＋同步接收范围登记，不合并不相关事实。

交接prompt对每一规范项给完整具名记录，manifest提供同一数据与准确证据绑定，至少包括：

1. 稳定ID、严重度及理由、分类、模块/主合同、根因key、canonical/alias、原历史ID联系和当前状态。
2. 源与规格精确证据：固定repo/commit、path、原file bytes/SHA256/blob，行区间/offset/字段/方法/表格clause及必要上下文、source→producer/write/consumer/display/persist链和反向clause依据。证据原文/原输出或可精确恢复的具名evidence载荷、检索范围、缺证位置完整保留，不能只说“参见代码”。
3. 前提/输入域、普通对照、最小反例的具体输入与步骤、参考期望或实际观察、当前规格断言及差异、失败/取消/异常/部分提交、必要消费者、影响、证据等级和未执行标识。
4. 最小行为规则修正（非源码搬运）、必须保留的正确范围、必要同步正文/附表/测试向量/消费者及其原因、精确建议读写范围；不实现TS/Ruby引擎，不额外扩scope。
5. 每条具名验收项与可判定条件、精确回归项/旧资格/正常与边界向量、怎样区分SOURCE_STATIC/DERIVED_VECTOR/TOOL_VALIDATION/实际执行；运行条件不足仍允许静态可判定项验收，但不假称运行PASS。
6. 独立反证者、原提出者、证据/裁决路径及理由；去重aliases/撤销项保留历史。author/reviewer不是同一个入口自证。
7. 依赖IDs、blocking/nonblocking理由、文件冲突、所属批次、独立author/reviewer入口、共享整合接收者、closure门、待决policy、limitations与excluded claims。

不适用字段给具名理由，不能用空数组/同一句套话冒充完成。required项必须有非空必要证据、反例、最小修正规则、验收、保留scope与必要读写/回归范围。通过独立反证裁成no-required的项仍说明为什么、哪些原文保持；optional/policy/limit不自动纳入必修。完整交接prompt必须包含全部规范项与可执行合同，不用“其余按模板/见未展开附件”省略记录；共同原载荷可以evidence ID去重，但准确证据内容/定位/身份和恢复方式必须完整且可得。

### 有限批次、并发与唯一整合

按**本次实际裁决项和真实文件/依赖**生成有限批次，不能预先照搬第五轮七批或人为限制独立并发数量。每个必修ID恰有一个主负责batch；共享同步/消费者接收任务具名但不得重复成为不同mandatory。提供 `batch-assignment.json`、`dependency-graph.json`、`file-conflict-graph.json`，以及每批独立author入口与非作者reviewer入口（逻辑ID、冻结输入、真实可用CLI/Desktop启动方法、所请求GPT-6.1 sol/ultra/default普速、日志/状态路径）。

每批合同列逐ID、精确读集/写集、必要原证据、原反例、验收、回归、依赖、条件门与候选目录。直接或传递依赖未满足不关闭；第一波给全部真的可独立开工的批次及数量，不按“无用户上限”假装资源无限。共享正式文件、公共台账或公共索引不得并行多写，即使不同段落也先证明独立条件；可由各批分别写候选mirror/patch，由唯一整合者接收、机械搬运/整合后再做独立实际review。主会话/R6-I独占公共台账、去重与最终注册；作者与审者分离。

冻结前以conflict图核每个实际/候选写路径、重叠、接口/共享接收边，不只是口头说并行。待决policy隔离，继续不依赖它的必修。候选PASS、实际整合后PASS、正式接受、最终CLOSED分开；验收/共享接收/历史回归/依赖有缺口时不能用行政状态关闭。第六轮review只提出后续修正规格和必要静态验收材料，严禁自动执行这些update动作。

### manifest最低结构与完整性

`cloud-sixth-update-handoff-manifest.json`至少含schema、repo/基线/R/实际R6core与发布身份、local/source材料位置和保护范围、所有文件完整身份、阅读/正反分母、规范records及其唯一主batch、severity/classification计数、optional/no-required/policy/limits分母与记录、aliases与去重裁决、accepted facts/负证据、批次合同、author/reviewer入口、依赖及冲突图、第一波可并行任务数量、历史资格、执行分期、状态语义与 `update_started:false`。

每个源/规格/报告/有效补充/证据载荷记录path、commit、tree归属、bytes、SHA256、Git blob、类型、用途、完整阅读/结构范围或inventory-only理由；大文件结构块台账覆盖全部真实范围并说明identity去重，不能让“完整hash”替代必要新实读。manifest及正文ID集合、计数、分批、依赖、引用都相互核对。manifest自身及整包commit/tree外部绑定，禁止递归hash。最终给prompt与manifest完整文件、准确固定commit/tree/path、bytes/SHA256/blob、有限整包完整远端读回结论和可直接复制正文；不要只给一段摘要。

如果required为0，仍完整交接事实、分类/limits/policy和NO_REQUIRED_UPDATE裁决，给空必修计划的具体理由；不捏造整改或自动实现optional。若有真实缺读/身份/材料依赖，隔离精确阻塞、继续其它工作，交接不能把未知变PASS。review与update新增执行、旧R4隔离4/旧R5review隔离4各分期；本轮新增实际执行如实计数，未执行向量DERIVED_VECTOR。最终状态必须同时说明：本轮review哪些静态范围完成、哪些运行未知、云端update未启动。

## 交付与完成条件

本轮输出至少包含：固定输入/逐载荷身份与安全范围；source/formal/有效补充全量inventory和逐结构reading ledger；正向source-fact→spec及反向clause→source矩阵；共享接口/全部有效接合与有限历史当前对照；规范findings、独立反证/裁决、主因去重、必要同步和消费者；实际执行/工具/推导分期；材料/宿主/机器码/外部与policy边界；模块级/主合同primary映射、覆盖闭合与未审精确分母；final-report、summary、完整中文cloud-sixth-update-handoff-prompt.md和cloud-sixth-update-handoff-manifest.json、可执行后续有限整改分批与作者/审者独立入口、CLI可见任务/状态/日志。

所有路径/事实有来源和读取等级，不能只给统一模板或“完整已看”口号。每个可得可审文件/单位与每个当前formal clause都有正反关联或具名处置；大文件结构覆盖完整、反证搜索真实完成、consumer/交界接收明确。任何真正缺读/缺依赖只隔离该范围并继续独立工作，最后如实列阻塞，不伪造未审0。全局结论区分可审静态完成与运行未知。

冻结报告core commit/tree及files bytes/SHA/blob，普通push独立报告分支，再核本轮新增报告完整远端读回与固定输入身份；可精确复用输入传输缓存，不能用传输校验代替本轮全量新语义阅读，也不要为行政回执循环读回整1GB仓库。报告自己commit/tree用外部后继绑定，不构造递归selfhash。最终给报告与完整云端整改交接prompt/manifest的固定入口及完整可复制正文、bytes/SHA/blob、正反分母/已读/未审、规范裁决计数、依赖并发批次、执行/材料边界和UPDATE_NOT_STARTED。

整个任务只审查并写本轮独立证据；不重修规格、不实现引擎、不merge main、不改R或历史接受/关闭、不删分支、不丢未发布成果、不归档释放环境。上述内容身份已填实；父任务先按固定main完成并核验本地同步，用户再手动本地启动，不代其自动开第六轮。
