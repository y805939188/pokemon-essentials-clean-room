# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-19 WP04–WP07 批次复审修订后）

| 文件 | SHA-256（前 8 位速记） | 完整 SHA-256 | 字节数 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `1ca34f44` | `1ca34f4442f4e997359addfb797ac209407a69ea6f3065740d65c75093b86e0e` | 29,838 |
| `planning/module-map.md` | `32eab70d` | `32eab70d503be63ceba06287afb648ec0b1b5fe8ca6225aaab28975c67360352` | 17,523 |
| `planning/feature-matrix.md` | `563cff0e` | `563cff0efb8c8a8a478f35ad25274deb94e30990b127b2b6bc045370bcea056e` | 31,051 |
| `planning/extraction-plan.md` | `c1735877` | `c173587708c9fcaaaaa1a4079bdedaa14d02405871b3fe3cd2ed6d16caeffd78` | 46,915 |
| `specs/demo/wp01-baseline-and-evidence-scope.md`（WP01 修订稿 v4） | `2a52e94e` | `2a52e94e615d0f1f45d55b0d14317b79e58bc6f988b76095e044f770ca41b407` | 16,543 |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md`（WP02 修订稿 v4） | `82b47151` | `82b471510ff563e6964697cb28e77ae816e190062dfafc9e328f44a81c2131fa` | 37,817 |
| `specs/kernel/wp02-settings-inventory-appendix.md`（WP02 附表 v2） | `f165b1cb` | `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e` | 16,555 |
| `specs/kernel/wp03-content-identity-and-schema.md`（WP03 修订稿 v5） | `de331460` | `de331460e013bfc07533d0f368967fe729bcf0720d98e7d990a16a0614e9c27d` | 30,708 |
| `specs/kernel/wp04-pbs-lifecycle.md`（WP04 修订稿 v2） | `ffe83e59` | `ffe83e59158e5bc25ef318854939df236fc68770beb8540aa6858521c8a2227c` | 20,261 |
| `specs/kernel/wp05-events-extensions-plugins.md`（WP05 修订稿 v2） | `d969f23e` | `d969f23e5d97e75e56717849ec79731ec0985e8a9b594c424b2f337515d29071` | 17,026 |
| `specs/kernel/wp06-time-random-steps-stats.md`（WP06 修订稿 v2） | `04cd172f` | `04cd172fc730e56df003409e1e96826e6623d439e7e746c68156e52f373c611f` | 20,867 |
| `specs/kernel/wp07-diagnostics-files-http.md`（WP07 修订稿 v2） | `e8300872` | `e8300872d0963e134114457342b4bfc70eb1382c4a9e5a36854ded988c10a3a8` | 16,562 |
| `analysis/inventory/wp02_settings_common.py` | `ba01d4d2` | `ba01d4d23f6f2eef42b123befc6809d09bfac282a7dd9f928aa6ac31427a868d` | 8,231 |
| `analysis/inventory/wp02_settings_inventory.py` | `dfa38c40` | `dfa38c407258607da467e6c609e0b75c78485dc974e85f387aa9cd12969c0ca3` | 1,491 |
| `analysis/inventory/wp02_build_appendix.py` | `7c965c9d` | `7c965c9d36a7eccb039a703312aa10a6c418fc120db769b888666c03d73c03d6` | 12,192 |
| `analysis/inventory/wp02-regen-check-2026-09-19.md` | `8ce853cc` | `8ce853cc28577ca3567407fe4b92d97e2f319835508834e5ae7cbd4151bdd05e` | 3,323 |
| `analysis/inventory/out/wp02-settings-inventory-appendix.md`（临时输出） | `f165b1cb` | `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e` | 16,555 |
| `review/joint-review-2026-09-19.md` | `f0e0029d` | `f0e0029db9a1e17a9c650a5a936a4ed1dd700e580e78efd305b02d020adf9494` | 12,253 |
| `review/wp01-review-2026-09-19.md` | `e044597c` | `e044597c5d3933d9376c42207da68351063806a285041785b383b877b5afe74b` | 11,708 |
| `review/wp02-review-2026-09-19.md` | `b3923043` | `b39230435fe4a6f1aaa83f68979c9c8a529cc6f176729801c2f1d3eb41e61151` | 18,146 |
| `review/wp02-recheck-2026-09-19.md` | `858adc69` | `858adc69f6d525ac7e4107d9466d02d9e8143e1342dea1ec65652662eed3981a` | 14,343 |
| `review/wp02-closure-review-2026-09-19.md` | `5f963011` | `5f9630118e9fbdda6578106b3ebb96b9db6777519650485d7569d5fb28c49d7d` | 10,820 |
| `review/wp03-review-2026-09-19/report.md` | `6f5bd583` | `6f5bd583ee53b017828f3f3060682b31cf99eb82b5f6a82c6bc74a7eadd88846` | 18,612 |
| `review/wp03-recheck-2026-09-19/report.md` | `799f7c0d` | `799f7c0dfb8fe49add0c3a43659901b55821694d91338cfb6ce70a5ec906296d` | 14,947 |
| `review/wp03-recheck-v3-2026-09-19/report.md` | `3f2d9661` | `3f2d9661cda4d3b96deef7b1bb88b0b30d3274131f8c0837352d5ae8623d3a3a` | 7,776 |
| `review/wp03-closure-review-2026-09-19/report.md` | `1544a179` | `1544a1794074681b2f0df0e0995479ba76d42998e6e0c189d7600d43d11e9167` | 7,778 |
| `review/wp03-closure-review-2026-09-19/next-batch-prompt.md` | `a8fa4858` | `a8fa4858089357ffe3a6003a1b82793879c84f654877fbdf85a00b09c97e617e` | 10,093 |
| `review/wp04-wp07-review-2026-09-19/report.md`（WP04–WP07 批次复审原件存档，含配套快照目录） | 见原件 | 见 `review/wp04-wp07-review-2026-09-19/` 目录 | 25,625 |

关联基线：参考仓库 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`）。Git 状态证据的精确记录见 WP01 修订稿第 3 节（2026-09-19 15:32，R 内检查）。

## 2. 送审对应关系记录

### 2.1 当前哈希对应（已确认，可核实）

- 2026-09-19 各轮 review 实测哈希均与当时本地文件一致（联合 review、WP01/WP02/WP03 各轮复审、WP02/WP03 闭合复审），对应关系见第 3 节历史。
- 2026-09-19 WP04–WP07 批次复审实测四包首版（`e2bc7e6b` / `a8412720` / `c18eae6a` / `0225f652`）、WP03 状态登记版（`de331460`）、矩阵（`ab2b8f21`）与当时 manifest 的 27 项哈希全部匹配、25 项字节数匹配；本地独立重算结果一致。本轮修订后四包的当前哈希已变为 `ffe83e59` / `d969f23e` / `04cd172f` / `e8300872`；批次复审实际审查的是修订前版本，新哈希不伪称为复审对象。
- 批次复审并指出本清单两处字节记录错误（WP03 闭合复审报告 10,757→7,778、批次提示词 7,769→10,093，BATCH-C01，已按实测修正；对应哈希始终正确，属清单字段错误，非原件漂移）。
- 结论：各轮 review 的审查对象均能与本地文件对应；本轮修订前的被审版本即第 3 节所列历史版本。

### 2.2 历史版本关系（据本地记录重建，证据受限）

- 2026-09-19 14:18:53 四份总控文档定稿；约 14:38 首次计算哈希并写入清单（历史条目见第 3 节）。
- 2026-09-19 14:39:03，overview 与 module-map 在本地被进一步修订（内容增大、行数不变），送审附件为 14:39 版，清单未同步，造成联合 review 实测值与清单记录不一致（联合 review R01）。
- **证据限制**：14:39 的修改时刻来自本地文件 mtime；变更范围（补核 E04 训练家引用、E11 HTTP 工具、E21 参战/布局，细化总览 §3 与 module-map D01/D11 行）是本地模型比对当前版本与此前阅读记录后重建的说明。**没有该次修改的操作日志或旧版全文**；14:39 之前的两版内容（`0421575b` / `0e22b7f2`）在本地已被覆盖、无留存副本，无法提供逐行 diff。不补造旧版本或历史日志。

## 3. 历史条目（已被替代，仅供追溯）

| 文件 | 旧 SHA-256（前 8 位） | 记录时点 | 替代关系 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `0421575b` | 2026-09-19 约 14:38 | 被 14:39 修订版 `1ca34f44` 替代 |
| `planning/module-map.md` | `0e22b7f2` | 2026-09-19 约 14:38 | 被 14:39 修订版 `32eab70d` 替代 |
| `planning/feature-matrix.md` | `2f4e3e31` → … → `55770385` → `ab2b8f21` | 2026-09-19 | 依次经 R02/R03/WP01、C02/WP02、状态回填+WP03 追踪、WP03 复审关联、WP03 回填+WP04–WP07 追踪修订；本轮经批次复审关联修订被 `563cff0e` 替代 |
| `planning/extraction-plan.md` | `aef0d7ab` → `d441c68b` | 2026-09-19 | 依次经 R02/R03、C02 修订为 `c1735877`（当前有效） |
| `specs/demo/wp01-baseline-and-evidence-scope.md` | `403e814c` → … → `c952847d` | 2026-09-19 | 依次经 WP01-R01/R02/R03、C02、状态回填、尾部状态同步（C03）修订为 `2a52e94e`（当前有效） |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md` | `d322cf95` → … → `272b0291` | 2026-09-19 | 依次经 WP02-R01～R06、F1/F2/C1、状态回填、尾部状态同步（C03）修订为 `82b47151`（当前有效） |
| `specs/kernel/wp02-settings-inventory-appendix.md` | `6fba2cdd` | 2026-09-19 附表首版 | 经 F1/F2 修订被 `f165b1cb` 替代（当前有效） |
| `specs/kernel/wp03-content-identity-and-schema.md` | `d61233f0` → … → `7a9c85da` | 2026-09-19 | 首版经 WP03-R01～R05、复检、枚举存在条件收紧修订为 `7a9c85da`（闭合通过版）；经状态回填被 `de331460` 替代（当前有效） |
| `specs/kernel/wp04-pbs-lifecycle.md` | `e2bc7e6b` | 2026-09-19 WP04 首版 | 经 WP04-R01～R03 修订被 `ffe83e59` 替代 |
| `specs/kernel/wp05-events-extensions-plugins.md` | `a8412720` | 2026-09-19 WP05 首版 | 经 WP05-R01～R03 修订被 `d969f23e` 替代 |
| `specs/kernel/wp06-time-random-steps-stats.md` | `c18eae6a` | 2026-09-19 WP06 首版 | 经 WP06-R01～R03 修订被 `04cd172f` 替代 |
| `specs/kernel/wp07-diagnostics-files-http.md` | `0225f652` | 2026-09-19 WP07 首版 | 经 WP07-R01～R03 修订被 `e8300872` 替代 |
| `analysis/inventory/wp02_settings_inventory.py` | `46f1ba84` | 2026-09-19 | 重构为共享模块后被 `dfa38c40` 替代（当前有效） |
| `analysis/inventory/wp02_build_appendix.py` | `898134d0` | 2026-09-19 | 重构为共享模块后被 `7c965c9d` 替代（当前有效） |

## 4. 2026-09-19 修订与交付摘要（按轮次）

**第一轮至第八轮**：联合 review 处理与 WP01；WP01 复审处理与 WP02 首版；WP02 复审处理（R01～R06）；WP02 复检处理（F1/F2/C1）；WP02 闭合状态回填与 WP03 首版；WP03 复审处理（R01–R05）；WP03 复检处理（四组剩余项）；WP03 v3 复检处理（枚举存在条件收紧）。

**第九轮（WP03 闭合状态回填 + WP04–WP07 批次首版）**：WP03 限定范围回填 Reviewed；交付 WP04/WP05/WP06/WP07 首版；跨包核对无冲突。

**第十轮（WP04–WP07 批次复审修订，本轮）**：

- **WP04-R01**：编译触发与异常清理分开——Reset/SystemExit 原样重抛（跳过诊断/清理/转换）；其他异常打印后"尝试"逐文件删除（不保证全部删除）；Hangup 转 Reset、其余转通用错误；早期失败（PBS 缺失分支）清理分支面对未建立清单；启动提示拒绝不否决自动条件。
- **WP04-R02**：补活跃解析路径与内容依赖目录——split_csv_line（引号重组）、get_csv_record（`*` 重复、`^` 可重复、大写可选、q 非格式化）、cast_csv_value/checkEnumField（WP03 引用）；标注 Unused 的旧 csv 函数非现行证据；内容知识依赖链（Type→Move→Item→Species→Forms 等）；被发现≠可成功编译（moves_extra 与固定 moves.txt 边界）。
- **WP04-R03**：反写调用者分开（启动触发 vs 调试菜单主动导出）；通用写出（按条目后缀生成路径，无条目无路径）与专用写出（connections 行式/encounters 专用格式）分开；write_all 为 22 项内容写出调用；不承诺全部旧输入重建或逐字节往返。
- **WP05-R01**：插件分三阶段——源码发现（调试/发布前提）、编译（needCompiling?）、预编译产物消费（runPlugins 无调试/归档早退，发布模式仍读取/注册/执行）；空产物与读取失败分别对待；撤回"发布模式下插件整体不加载"。
- **WP05-R02**：元数据按发现/解析/注册入口分校验（缺 Name/Scripts 报错、缺键不校验、显式空值报错、缺 Essentials 仅警告）；版本比较为逐字符位置比较（1.10 < 1.9，非 SemVer）；optional_exact 可经 Requires 第三分量表达（注释与实际入口不一致，以入口为准）。
- **WP05-R03**：回调参数展开条件（arity > 2 且匹配才传完整参数，两参数回调收发送者+数组）；HandlerHashSymbol 注册无仅符号校验（查找按 `.id` 归一化）；NamedEvent/HandlerHash/菜单同键替换；处理器校验先于 nil ID 忽略。
- **WP06-R01**：时钟消费者表——电话再战（现实秒、同秒去重、每合格刷新只减 1）、电话来电（Graphics.delta 帧扣减）、多重守卫（菜单/战斗/消息/强制路线/解释器）；游戏时间锚点设置（新游戏/载入）/清空（回标题）/缺席（标题不计入）。
- **WP06-R02**：地牢待播种子无条件清空——参数种子 A 与待播种子 B 同时存在时用 A 且 B 仍被清空；只有 B 时用 B 并清空；均无则新种子；提前返回不撤回清空/播种。
- **WP06-R03**：随机入口/消费者族目录（rand 242 次文本命中的口径、sample/shuffle 53 处及寄养/地牢用例、取值范围可静态确定、跨实现重放不可证）；GameStats 74 字段分组清单（初始化非全 0：数组/空数组；NPC/道馆/名人堂事件写入字段标 U01 待证）；计步机制（pbOnStepTaken 守卫、31 位掩码、事件顺序）。
- **WP07-R01**：HTTP 按 GET/POST × 基础/便利分层——仅 POST 有 http 前缀检查（GET 传 https 给宿主，协议能力未验证）；基础入口 rescue 仅包 HTTPLite 调用、写入异常可传播，便利入口捕获；非 Hash 响应原样返回；ToFile 成功返回 `""`。
- **WP07-R02**：文件读取逐入口捕获集合——pbGetFileChar 捕获 EISDIR、pbGetFileString 不捕获（异常可传播）；非归档 1 字节 vs 归档宿主原始结果；pbRgssOpen 非归档直接打开原输入、仅归档 canonicalize；RTP.eachPath 始终本地根。
- **WP07-R03**：诊断调用前提分层——调试主流程 pbCriticalCode 包装；非调试直接调用且仅 Hangup 专门处理（打印+紧急保存）；EventScriptError 格式例外（专用事件消息、省略类/回溯）；日志写入失败则后续输出不保证；Reset/SystemExit 原样传播（与编译器一致）。
- **BATCH-C01**：本清单两处字节记录按实测修正（WP03 闭合复审报告 7,778、批次提示词 10,093；哈希始终正确）。
- **BATCH-C02**：write_all 为 22 项内容写出调用（非 21）；EventHandlers.add 53 文本命中含 1 处整行注释示例（非注释命中 52）；rand 242 为 `\brand\(` 出现次数（2 处注释、230 匹配行；宽松 `rand\(` 为 232 行/244 次含 srand 子串），均在相应文档中标注口径，不以文本命中宣称全部实际调用或覆盖完成。
- **跨包核对**：WP04 异常/清理与 WP07 诊断调用前提一致（编译器为显式业务调用者）；WP05 三阶段错误与 WP07 分层一致（pluginErrorMsg 共用诊断面）；WP06 自身计量/更新目录已补，领域扩展仍归 WP09/WP14/WP58/WP63；声明范围、矩阵状态、证据记录、清单、场景和摘要一致。
- **矩阵增量**：F02-02、F01-03、F01-04、F01-05、F03-05、F01-06、F01-07 均保持 ReviewPending（关联批次复审修订记录），未升级。
- 四包修订稿 v2 状态均为 **ReviewPending**，统一送外部 review；未自行升级 Reviewed；未执行 WP08–WP10。
