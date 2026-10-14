# 第六轮全量双向独立全局审查 prompt（收尾主分支身份待填实）

状态：范围完整的交接草稿，**未启动第六轮，不是最终已填实发布基线**。父任务完成主分支发布/清理对齐后，填入以下全部字段，校验commit/tree/tag/index一致，再交用户手动在本地启动。任何占位符未填或身份不吻合，停止依赖该基线的审读，先做只读核验；不把旧B5、临时整改head或分支名自行当最终第六轮基线。

| 固定输入 | 必填值 |
| --- | --- |
| 本地项目仓库 | `<LOCAL_PROJECT_REPOSITORY>`，GitHub `y805939188/pokemon-essentials-clean-room` |
| 清理/同步完成后的正式主分支commit | `<FINAL_MAIN_COMMIT>` |
| 对应workspace tree | `<FINAL_MAIN_TREE>` |
| 对应正式131目录tree | `<FINAL_FORMAL_TREE>`（当前第五轮已接受为1046fbb657882e84b3dfc6d017943a9edf7782e5；若后续实质变化须明确重新绑定） |
| 对应交付tag及其准确目标 | `<FINAL_DELIVERY_TAG_AND_TARGET>` |
| 最终主分支/远端读回和报告索引 | `<FINAL_PUBLICATION_RECEIPT_COMMIT_TREE_PATH>` |
| 本地只读参考仓库 | `<LOCAL_REFERENCE_REPOSITORY>`，参考 `Maruno17/pokemon-essentials` |
| 固定参考R | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，原tracked432；启动时独立核inventory |

第五轮重要追溯点：B5 `9366d9d17aaeac3b4414236468affa650fb3dd27`；语义全局报告 `c0ff33024aea424c68d29f9778fe7c8e807d21e8`；其发布 `f49d870c6fd616ab6736754a218a4553b5acac7f`；U08 actual `e9f7590e68347849450fd5cbdba538e605cda0a7`、actual报告 `debf59f3c5370df253706969fd4dd1c103300bf2`；已审关闭候选 `13fddb0a217b36974c75657aa68da0caf104ee48`、关闭报告 `044c3483229e7e76bedf1fc244fc84d274bf059c`；唯一激活 `12df95a8e81061a606d50d3f0a0528793b2e6b2c`、发布 `0378dc85cab61642ca1467e5a901b3c829df976a`。这些是历史/精确资格索引，**不得继承为本次新全局语义PASS**。

---

你是第六轮独立全局 reviewer。请使用 **GPT-6.1 sol / ultra / default普速，禁Fast**，用户将手动在本地启动本任务。实际model/effort/tier/speed或task UUID未回显只标UNVERIFIED，不检查额度、认证或反复追查模型配置。你应与第五轮规格修订作者/唯一整合者保持任务角色独立；Git账号、父线程引用和请求参数不能伪造真实task或实际模型回显。

目标是对已经清理、同步并冻结的正式规格做**完整、全量、双向、独立的新全局审查**，为后续从零实现提供准确行为规格。不是抽样检查，不是仅验第五轮92整改项，不是diff-only或关键词覆盖，也不沿用相同blob/旧PASS跳过本轮语义阅读。不能实现新引擎、移植Ruby代码、设计原类结构对应的新框架，不能把参考当架构/源码模板。战斗/AI全部保留；未来可能采用Showdown不缩本轮事实或规格审查范围。

## 启动与冻结

先完整读取本地根及适用目录的AGENTS.md，检查 `.agents/skills` 与相关已提供skills；明确实际适用说明和读写边界。用户既有授权优先于技能建议。只读核项目/R的commit/tree、远端主分支及交付tag、dirty/untracked状态、正式目录131身份及所有有效补充材料来源。不要reset/删除/覆盖已有或未发布成果，不碰R，不用移动分支头来掩盖输入不一致。

全部基线字段须已填实并可核对。创建本轮唯一审查根 `review/global-independent-review/sixth-<YYYY-MM-DD>-<main-short>-<nonce>/` 与独立报告分支 `codex/review-sixth-<date>-<main-short>-<nonce>`。写集只限本轮独立报告/证据；不修正式、planning/audit、R、旧报告、第五轮关闭回执、main或原历史字节。报告普通push可按用户授权进行；不force、不merge main、不删分支、不归档释放环境。

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

## 独立反证与并行分工

可按具备独立读写条件的完整领域并行工作，无用户数量上限。所有任务请求sol/ultra/default普速禁Fast；每个子任务独立目录，只读正式/R。角色分离：领域事实提案、非提案者反证、跨域接收者/历史/覆盖核验各具名；根reviewer整合但不能靠角色数量或hash通过代替必要实读。

每条疑似发现给固定source/spec路径与精确行/offset/字段、原前置、普通对照、最小反例、失败/取消/部分提交、负证据搜索、必要消费者、预期/当前差别、影响、最小修正规则、必需同步/向量范围、原来正确scope须保留项、未知与excluded claims、证据等级。独立反证后裁为required、optional、no-required revision、独立policy或limit；不能把待决兼容政策强塞mandatory，也不能以“无默认caller/无运行环境”免除可判定静态事实。

## 材料、资源、二进制及执行边界

13历史限制不是本轮偷懒跳过材料的许可。重新核现有可得资料与可安全解析范围：Main49、messages数据、两根BMP、字体映射/度量/已编码字形、soundfont完整RIFF/hydra与参数链接、可读shader/兼容脚本/controller表、作者工具可读IL/导入/控制流等都按实际单位完整覆盖；若现有材料发生变化重新核分母与内容。机器码全部CFG、实际native版本/后端选择、GPU精度/采样/像素、音频合成听感、字体宿主、Windows窗口/.NET/RGSS、完整map/media/Demo可达、真实存档/网络及无界plugin/config组合等不由格式/字符串推通过。

初始新reference/model/host/Demo行为执行记0。若为必要边界新增安全隔离执行，先确定固定输入、命令、工具/替身、作用范围与输出，保存原始stdout/stderr/exitcode/时间/失败；不启动生产游戏/真实账号、不安装改安全配置或触未授权外部服务。TOOL_VALIDATION、SOURCE_STATIC、DERIVED_VECTOR、REFERENCE_OBSERVATION、独立模型、完整宿主/Demo严格分开。历史R4隔离4和R5review隔离4不重算本轮新增；捕获错误的exit0不等业务成功，向量无运行记录不得包装为执行PASS。

## 交付与完成条件

本轮输出至少包含：固定输入/逐载荷身份与安全范围；source/formal/有效补充全量inventory和逐结构reading ledger；正向source-fact→spec及反向clause→source矩阵；共享接口/全部有效接合与有限历史当前对照；规范findings、独立反证/裁决、主因去重、必要同步和消费者；实际执行/工具/推导分期；材料/宿主/机器码/外部与policy边界；模块级/主合同primary映射、覆盖闭合与未审精确分母；final-report、summary、可执行后续有限整改分批与作者/审者独立入口。

所有路径/事实有来源和读取等级，不能只给统一模板或“完整已看”口号。每个可得可审文件/单位与每个当前formal clause都有正反关联或具名处置；大文件结构覆盖完整、反证搜索真实完成、consumer/交界接收明确。任何真正缺读/缺依赖只隔离该范围并继续独立工作，最后如实列阻塞，不伪造未审0。全局结论区分可审静态完成与运行未知。

冻结报告core commit/tree及files bytes/SHA/blob，普通push独立报告分支，再核本轮新增报告完整远端读回与固定输入身份；可精确复用输入传输缓存，不能用传输校验代替本轮全量新语义阅读，也不要为行政回执循环读回整1GB仓库。报告自己commit/tree用外部后继绑定，不构造递归selfhash。最终给报告固定入口、正反分母/已读/未审、规范裁决计数、执行/材料边界和最小剩余步骤。

整个任务只审查并写本轮独立证据；不重修规格、不实现引擎、不merge main、不改R或历史接受/关闭、不删分支、不丢未发布成果、不归档释放环境。用户会在基线填实后手动本地启动，不代其自动开第六轮。
