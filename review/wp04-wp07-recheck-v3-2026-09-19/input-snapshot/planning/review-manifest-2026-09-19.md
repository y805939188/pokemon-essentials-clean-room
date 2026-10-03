# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-19 WP04–WP07 复检六项修订后）

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
| `specs/kernel/wp04-pbs-lifecycle.md`（WP04 修订稿 v3） | `0df88787` | `0df88787a53863e2ee6d521c45e0b5c9e297d18670b4e263bdb084aaf1d37028` | 22,748 |
| `specs/kernel/wp05-events-extensions-plugins.md`（WP05 修订稿 v3） | `aae49934` | `aae49934ce2f557af8d49cf6d8822fd5670e9162f592359d78331abe818ab46c` | 18,157 |
| `specs/kernel/wp06-time-random-steps-stats.md`（WP06 修订稿 v3） | `09e01e07` | `09e01e07f48bda95f7f0b1644aa0d13482d004c7f0dd9d392b43dbee99a5ff1f` | 19,824 |
| `specs/kernel/wp06-stats-directory.md`（WP06 统计目录附表） | `0ea55ff1` | `0ea55ff18aedfef58dbe47df3da226b4fb89fb66fead78760200effb518b0882` | 13,543 |
| `specs/kernel/wp07-diagnostics-files-http.md`（WP07 修订稿 v3） | `101577ef` | `101577efd4304b59cbbd3cf20bad24766db318579799337ba206024805837727` | 17,049 |
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
| `review/wp04-wp07-review-2026-09-19/report.md`（批次复审原件存档） | 见原件 | 见 `review/wp04-wp07-review-2026-09-19/` 目录 | 25,625 |
| `review/wp04-wp07-recheck-2026-09-19/report.md`（批次复检原件存档） | 见原件 | 见 `review/wp04-wp07-recheck-2026-09-19/` 目录 | 16,743 |

关联基线：参考仓库 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`）。Git 状态证据的精确记录见 WP01 修订稿第 3 节（2026-09-19 15:32，R 内检查）。

## 2. 送审对应关系记录

### 2.1 当前哈希对应（已确认，可核实）

- 2026-09-19 各轮 review 实测哈希均与当时本地文件一致，对应关系见第 3 节历史。
- 2026-09-19 WP04–WP07 批次复审实测四包首版（`e2bc7e6b` / `a8412720` / `c18eae6a` / `0225f652`）与当时 manifest 的 27 项哈希及字节数全部匹配；批次复检实测四包 v2（`ffe83e59` / `d969f23e` / `04cd172f` / `e8300872`）、矩阵（`563cff0e`）与当时 manifest 的 27 项哈希及字节数全部匹配；本地独立重算结果一致。本轮修订后四包的当前哈希已变为 `0df88787` / `aae49934` / `09e01e07` / `101577ef`；两次复审实际审查的是修订前版本，新哈希不伪称为复审对象。
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
| `planning/feature-matrix.md` | `2f4e3e31` → … → `ab2b8f21` | 2026-09-19 | 依次经 R02/R03/WP01、C02/WP02、状态回填+WP03 追踪、WP03 复审关联、WP03 回填+WP04–WP07 追踪、批次复审关联修订为 `563cff0e`（当前有效） |
| `planning/extraction-plan.md` | `aef0d7ab` → `d441c68b` | 2026-09-19 | 依次经 R02/R03、C02 修订为 `c1735877`（当前有效） |
| `specs/demo/wp01-baseline-and-evidence-scope.md` | `403e814c` → … → `c952847d` | 2026-09-19 | 依次经 WP01-R01/R02/R03、C02、状态回填、尾部状态同步（C03）修订为 `2a52e94e`（当前有效） |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md` | `d322cf95` → … → `272b0291` | 2026-09-19 | 依次经 WP02-R01～R06、F1/F2/C1、状态回填、尾部状态同步（C03）修订为 `82b47151`（当前有效） |
| `specs/kernel/wp02-settings-inventory-appendix.md` | `6fba2cdd` | 2026-09-19 附表首版 | 经 F1/F2 修订被 `f165b1cb` 替代（当前有效） |
| `specs/kernel/wp03-content-identity-and-schema.md` | `d61233f0` → … → `7a9c85da` | 2026-09-19 | 首版经 WP03-R01～R05、复检、枚举存在条件收紧修订为 `7a9c85da`（闭合通过版）；经状态回填被 `de331460` 替代（当前有效） |
| `specs/kernel/wp04-pbs-lifecycle.md` | `e2bc7e6b` → `ffe83e59` | 2026-09-19 | 首版经 WP04-R01～R03 修订为 `ffe83e59`；本轮经复检 R02 修订被 `0df88787` 替代 |
| `specs/kernel/wp05-events-extensions-plugins.md` | `a8412720` → `d969f23e` | 2026-09-19 | 首版经 WP05-R01～R03 修订为 `d969f23e`；本轮经复检 R02/R03 修订被 `aae49934` 替代 |
| `specs/kernel/wp06-time-random-steps-stats.md` | `c18eae6a` → `04cd172f` | 2026-09-19 | 首版经 WP06-R01～R03 修订为 `04cd172f`；本轮经复检 R03 修订被 `09e01e07` 替代 |
| `specs/kernel/wp07-diagnostics-files-http.md` | `0225f652` → `e8300872` | 2026-09-19 | 首版经 WP07-R01～R03 修订为 `e8300872`；本轮经复检 R01/R03 修订被 `101577ef` 替代 |
| `analysis/inventory/wp02_settings_inventory.py` | `46f1ba84` | 2026-09-19 | 重构为共享模块后被 `dfa38c40` 替代（当前有效） |
| `analysis/inventory/wp02_build_appendix.py` | `898134d0` | 2026-09-19 | 重构为共享模块后被 `7c965c9d` 替代（当前有效） |

## 4. 2026-09-19 修订与交付摘要（按轮次）

**第一轮至第九轮**：联合 review 处理与 WP01；WP01 复审处理与 WP02 首版；WP02 复审处理（R01～R06）；WP02 复检处理（F1/F2/C1）；WP02 闭合状态回填与 WP03 首版；WP03 复审处理（R01–R05）；WP03 复检处理（四组剩余项）；WP03 v3 复检处理（枚举存在条件收紧）；WP03 闭合状态回填与 WP04–WP07 批次首版。

**第十轮（WP04–WP07 批次复审修订）**：WP04-R01 异常类别与阶段、WP04-R02 活跃解析路径与内容依赖、WP04-R03 反写调用者与写出格式；WP05-R01 三阶段、WP05-R02 按入口校验与版本比较、WP05-R03 回调参数与注册规则；WP06-R01 时钟消费者表、WP06-R02 地牢种子清空、WP06-R03 随机入口/统计字段清单初版与计步机制；WP07-R01 HTTP 分层、WP07-R02 文件捕获集合、WP07-R03 诊断调用前提；BATCH-C01/C02 维护。

**第十一轮（WP04–WP07 复检六项修订，本轮）**：

- **WP04-R02**：补属性级规则（普通重复属性后值覆盖、`^` 属性累加、通用未知属性不被消费不报错、新身份定义/重复身份/未知引用三分）；更正"未定义节名即报错"泛化；依赖表改按编译解析/校验依赖、调度先后、运行期关联分类——BerryPlant 无 Item 枚举（其校验为空，仅运行期关联/调度先后，非编译枚举依赖）；TrainerType→Trainer、TrainerType→PlayerMetadata（`017_PlayerMetadata.rb:14`）、Item→Metadata.StartItemStorage（`016_Metadata.rb:24`）分别登记，撤回 Trainer→Metadata 误边；保留 Type→Move→Item 等正确关系。
- **WP05-R02**：Scripts 归一化——readMeta 默认空数组兜底 + 递归收集去重；作者省略 Scripts 行不触发 541 行错误（省略行 ≠ 解析后值为假）；补"省略 Scripts 且有脚本→自动收集""省略 Scripts 且无脚本→空列表不报错"两例；空脚本插件条目与整个预编译产物为空分别说明。
- **WP05-R03**：trigger 首参改为"按已有 id 规则归一化后的键，类型不保证为 Symbol"（字符串键登记并触发时首参仍为该字符串）。
- **WP06-R03**：交付 74 字段统计目录附表 `wp06-stats-directory.md`——全部声明字段的字段名/组/单位形态/初始化/更新规则类别与定位/持久化/证据等级/后续责任；Safari 两个统计与 BugContest 两个统计改为"脚本写入静态确认、Demo 可达未证"（`001_SafariZone.rb:150–153`、`002_BugContest.rb:192–216`），不标 U01；waterfalls_descended 补归属（`004_Overworld_FieldMoves.rb:910`、`008_Game_Player.rb:157`）；U01 仅限确实依赖缺失事件的 10 个字段，不连带同组其他字段；派生 getter 与 Game_Temp 锚点分开不计入。
- **WP07-R01**：汇总表失败可区分性修正——请求异常、非 200、成功空正文可同为 `""`（不可区分）；基础写入异常可以传播，便利包装按其捕获范围处理；非 Hash 响应原样返回；撤回"HTTPLite 调用失败可区分"。
- **WP07-R03**：Reset/SystemExit 原样传播限定于 pbCriticalCode、Compiler.main 等具体分支；插件脚本执行入口的 `rescue Exception` 捕获含 Reset/SystemExit 的全部异常并进入插件诊断/退出路径（`005_PluginManager.rb:634–640`），与 WP05 交叉核对一致；撤回"任意阶段"全局承诺；日志写入自身失败的既有限制保留。
- 跨包核对：WP04 异常/清理与 WP07 诊断前提一致；WP05 插件执行异常入口与 WP07 Reset 限定一致；WP06 统计目录交付，U01 范围与矩阵/摘要一致；声明范围、矩阵状态、证据记录、清单、场景和摘要一致。
- 矩阵保持 ReviewPending（F02-02、F01-03、F01-04、F01-05、F03-05、F01-06、F01-07 均未升级；本轮矩阵未修改，沿用第十轮记录）。
- 四包修订稿 v3 与 WP06 统计目录附表状态均为 **ReviewPending**，统一送外部 review；未自行升级 Reviewed；未执行 WP08–WP10。
