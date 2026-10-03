# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-19 WP08–WP10 批次复审修订后）

| 文件 | SHA-256（前 8 位速记） | 完整 SHA-256 | 字节数 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `1ca34f44` | `1ca34f4442f4e997359addfb797ac209407a69ea6f3065740d65c75093b86e0e` | 29,838 |
| `planning/module-map.md` | `32eab70d` | `32eab70d503be63ceba06287afb648ec0b1b5fe8ca6225aaab28975c67360352` | 17,523 |
| `planning/feature-matrix.md` | `90bae2b9` | `90bae2b9d5c5f1cbef910d89948c543595c4182d0aebdefe2c9c0afaedfb1a8e` | 32,225 |
| `planning/extraction-plan.md` | `c1735877` | `c173587708c9fcaaaaa1a4079bdedaa14d02405871b3fe3cd2ed6d16caeffd78` | 46,915 |
| `specs/demo/wp01-baseline-and-evidence-scope.md`（WP01 修订稿 v4） | `2a52e94e` | `2a52e94e615d0f1f45d55b0d14317b79e58bc6f988b76095e044f770ca41b407` | 16,543 |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md`（WP02 修订稿 v4） | `82b47151` | `82b471510ff563e6964697cb28e77ae816e190062dfafc9e328f44a81c2131fa` | 37,817 |
| `specs/kernel/wp02-settings-inventory-appendix.md`（WP02 附表 v2） | `f165b1cb` | `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e` | 16,555 |
| `specs/kernel/wp03-content-identity-and-schema.md`（WP03 修订稿 v5） | `de331460` | `de331460e013bfc07533d0f368967fe729bcf0720d98e7d990a16a0614e9c27d` | 30,708 |
| `specs/kernel/wp04-pbs-lifecycle.md`（WP04 修订稿 v4） | `b5d33db1` | `b5d33db1ac4172c216715df713bda414f7358fa69dcf5c21b5a8a0409d48da59` | 23,172 |
| `specs/kernel/wp05-events-extensions-plugins.md`（WP05 修订稿 v4） | `d65b6d14` | `d65b6d14bf95f47d59166f7bcef74984d92b243e465f8c035daa95b9521a24f7` | 18,497 |
| `specs/kernel/wp06-time-random-steps-stats.md`（WP06 修订稿 v5） | `c01140cb` | `c01140cb60d76f8f13de454a7a52f5fae544ac0fe415eaf81d877df0e24c9d7d` | 21,359 |
| `specs/kernel/wp06-stats-directory.md`（WP06 统计目录附表 v2） | `15b75cea` | `15b75cea1698c8978f4cc33380089f3c501cfec0ab8894f3991a6a6513e2d04a` | 14,954 |
| `specs/kernel/wp07-diagnostics-files-http.md`（WP07 修订稿 v4） | `2cd5408a` | `2cd5408ae9dbb1d96281057829c6bff125fdf471b2afc0e96020d105801cdbd2` | 17,398 |
| `specs/kernel/wp08-localization.md`（WP08 修订稿 v2） | `755bb489` | `755bb4896bd508530eb46671d1d12e699bb031f005eb1f8e55acd2ab95dbd89a` | 17,467 |
| `specs/kernel/wp09-save-startup-continue.md`（WP09 修订稿 v2） | `3b760de3` | `3b760de3eb47f7e66a9b19c08f9a1e837d1264dda7f914eceda134bc9b15cccb` | 17,358 |
| `specs/kernel/wp10-migration-failure-recovery.md`（WP10 修订稿 v2） | `6911628d` | `6911628db6c7e5bf4d285ee94d4ca6b4bdc69b122563cc777603547f022e714e` | 21,178 |
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
| `review/wp04-wp07-review-2026-09-19/report.md` | 见原件 | 见 `review/wp04-wp07-review-2026-09-19/` 目录 | 25,625 |
| `review/wp04-wp07-recheck-2026-09-19/report.md` | 见原件 | 见 `review/wp04-wp07-recheck-2026-09-19/` 目录 | 16,743 |
| `review/wp04-wp07-recheck-v3-2026-09-19/report.md` | `4c208ff8` | `4c208ff8713bda3ea26a857422d420f04fd3f20b188f2c3bbeb0bc2559a33ed2` | 10,897 |
| `review/wp04-wp07-recheck-v3-2026-09-19/revision-prompt.md` | `4b247519` | `4b247519f52a70b1439a70b61fe470058f1ab8e2d3863e2f33145e8e92fa2215` | 3,983 |
| `review/wp04-wp07-closure-review-2026-09-19/report.md` | `1cc5e453` | `1cc5e453a023fea7d0b7225e35895fc946637e04528d84172e0cb5ce3df3b9ce` | 7,457 |
| `review/wp04-wp07-closure-review-2026-09-19/next-batch-prompt.md` | `a416fcc2` | `a416fcc2dae05a5e1e24e4d6280c89f0b551247222af3efa3073208264f290c4` | 10,313 |
| `review/wp08-wp10-review-2026-09-19/report.md`（批次复审原件存档） | `4e455ffc` | `4e455ffc6295c470477653dc2aa6b3a24968e527904c3f9af154d0c3a254635b` | 21,222 |
| `review/wp08-wp10-review-2026-09-19/revision-prompt.md`（批次修订提示原件存档） | `ebfc287b` | `ebfc287b9a61659b9a77da301c96bae21b65c8904fe1125f3435b9afb60fcd09` | 7,637 |

关联基线：参考仓库 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`）。Git 状态证据的精确记录见 WP01 修订稿第 3 节（2026-09-19 15:32，R 内检查）。

## 2. 送审对应关系记录

### 2.1 当前哈希对应（已确认，可核实）

- 2026-09-19 各轮 review 实测哈希均与当时本地文件一致，对应关系见第 3 节历史。
- 2026-09-19 WP08–WP10 批次复审实测三包首版（`1f2fd3a6` / `359eb1c1` / `12018885`）与当时 manifest 的 35 项哈希及字节数全部匹配；本地独立重算结果一致。本轮修订后三包的当前哈希已变为 `755bb489` / `3b760de3` / `6911628d`；批次复审实际审查的是修订前版本，新哈希不伪称为复审对象。
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
| `planning/feature-matrix.md` | `2f4e3e31` → … → `4fa78f7d` | 2026-09-19 | 依次经 R02/R03/WP01、C02/WP02、状态回填+WP03 追踪、WP03 复审关联、WP03 回填+WP04–WP07 追踪、批次复审关联、三包回填、WP06 回填+WP08–WP10 追踪修订；本轮经批次复审关联修订被 `90bae2b9` 替代 |
| `planning/extraction-plan.md` | `aef0d7ab` → `d441c68b` | 2026-09-19 | 依次经 R02/R03、C02 修订为 `c1735877`（当前有效） |
| `specs/demo/wp01-baseline-and-evidence-scope.md` | `403e814c` → … → `c952847d` | 2026-09-19 | 依次经 WP01-R01/R02/R03、C02、状态回填、尾部状态同步（C03）修订为 `2a52e94e`（当前有效） |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md` | `d322cf95` → … → `272b0291` | 2026-09-19 | 依次经 WP02-R01～R06、F1/F2/C1、状态回填、尾部状态同步（C03）修订为 `82b47151`（当前有效） |
| `specs/kernel/wp02-settings-inventory-appendix.md` | `6fba2cdd` | 2026-09-19 附表首版 | 经 F1/F2 修订被 `f165b1cb` 替代（当前有效） |
| `specs/kernel/wp03-content-identity-and-schema.md` | `d61233f0` → … → `7a9c85da` | 2026-09-19 | 首版经 WP03-R01～R05、复检、枚举存在条件收紧修订为 `7a9c85da`（闭合通过版）；经状态回填被 `de331460` 替代（当前有效） |
| `specs/kernel/wp04-pbs-lifecycle.md` | `e2bc7e6b` → … → `0df88787` | 2026-09-19 | 首版经 WP04-R01～R03、复检 R02 修订为 `0df88787`（v3 通过版）；经状态回填被 `b5d33db1` 替代（当前有效） |
| `specs/kernel/wp05-events-extensions-plugins.md` | `a8412720` → … → `aae49934` | 2026-09-19 | 首版经 WP05-R01～R03、复检 R02/R03 修订为 `aae49934`（v3 通过版）；经状态回填被 `d65b6d14` 替代（当前有效） |
| `specs/kernel/wp06-time-random-steps-stats.md` | `c18eae6a` → … → `3cdfc081` | 2026-09-19 | 首版经 WP06-R01～R03、复检 R03、附表定点修订为 `3cdfc081`（闭合通过版）；经状态回填与 BATCH-C03 维护被 `c01140cb` 替代（当前有效） |
| `specs/kernel/wp06-stats-directory.md` | `0ea55ff1` | 2026-09-19 附表首版 | 经附表事实定点修订被 `15b75cea` 替代（当前有效） |
| `specs/kernel/wp07-diagnostics-files-http.md` | `0225f652` → … → `101577ef` | 2026-09-19 | 首版经 WP07-R01～R03、复检 R01/R03 修订为 `101577ef`（v3 通过版）；经状态回填被 `2cd5408a` 替代（当前有效） |
| `specs/kernel/wp08-localization.md` | `1f2fd3a6` | 2026-09-19 WP08 首版 | 经 WP08-R01～R03 修订被 `755bb489` 替代 |
| `specs/kernel/wp09-save-startup-continue.md` | `359eb1c1` | 2026-09-19 WP09 首版 | 经 WP09-R01～R03 修订被 `3b760de3` 替代 |
| `specs/kernel/wp10-migration-failure-recovery.md` | `12018885` | 2026-09-19 WP10 首版 | 经 WP10-R01～R05 修订被 `6911628d` 替代 |
| `analysis/inventory/wp02_settings_inventory.py` | `46f1ba84` | 2026-09-19 | 重构为共享模块后被 `dfa38c40` 替代（当前有效） |
| `analysis/inventory/wp02_build_appendix.py` | `898134d0` | 2026-09-19 | 重构为共享模块后被 `7c965c9d` 替代（当前有效） |

## 4. 2026-09-19 修订与交付摘要（按轮次）

**第一轮至第十二轮**：联合 review 处理与 WP01；WP01 复审处理与 WP02 首版；WP02 复审处理（R01～R06）；WP02 复检处理（F1/F2/C1）；WP02 闭合状态回填与 WP03 首版；WP03 复审处理（R01–R05）；WP03 复检处理（四组剩余项）；WP03 v3 复检处理（枚举存在条件收紧）；WP03 闭合状态回填与 WP04–WP07 批次首版；WP04–WP07 批次复审修订；WP04–WP07 复检六项修订；三包状态回填与 WP06 定点修订。

**第十三轮（WP06 闭合登记 + WP08–WP10 批次首版）**：WP06 限定范围回填 Reviewed；BATCH-C03 摘要维护；交付 WP08/WP09/WP10 首版。

**第十四轮（WP08–WP10 批次复审修订，本轮）**：

- **WP08-R01**：默认 core/game（收集与导出）与当前语言 core/game（运行查找，先 game 后 core、不再查默认语料）分开；主动加载（启动直接 load_message_files）与 Translation 延迟加载分开；物种/招式名按 real_name 哈希键查找（非数组索引），不由域编号推断域内身份。
- **WP08-R02**：空字符串是有效命中（直接返回空串、不触发回退）；缺键/nil、空译、载入失败、查找结构异常、格式化异常按入口区分；`_INTL/_ISPRINTF` 的 rescue 只包查找、格式化向外传播；`_MAPINTL/_MAPISPRINTF` 无同样捕获保证。
- **WP08-R03**：导出格式分数组三行/Hash 两行；compile_text 先截断输出再解析（非法输入时旧 .dat 可能已被截断）；extract 确认后删除 Dir.all 全部文件（不限 .txt）；收集遇 Hangup 后部分完成；真实菜单路径（Text_*_* → 含后缀片段 → messages 文件）；载入菜单已有存档时切换语言把选项写入存档 Hash 并直接写回（不经 Game.save，与 WP09 对齐）。
- **WP09-R01**：valid? 不容忍缺键；load_values 缺键默认分支与键存在但类型错误分开；新游戏只初始化"有新游戏值且未加载或要求重置"的项；game_system 是启动已加载、非强制重置的值（可保留）；stats 重建后会话数为 1。
- **WP09-R02**：普通无存档路径仍构建菜单；仅 $DEBUG + 无 Game.rgssad + SKIP_CONTINUE_SCREEN 三者同时成立才直接新游戏/继续；地图恢复分支改为"magic_number 不一致或 safesave 为真时重新 setup（缺图时调试选图/取消退出、非调试报错），两者都不成立才 setMapChanged"；events=nil 的地图损坏与缺图分开。
- **WP09-R03**：保存前后内存与磁盘边界（safesave/save_count/magic_number/time_last_saved/锚点先变；IOError 分支仅回退 save_count；InvalidValueError 不在该捕获内且此阶段尚未打开文件）；路径选择（默认数据目录 vs 自定义）；语言菜单直写、转换读取写回各自责任，不暗示都经 Game.save。
- **WP10-R01**：版本向量修正（"19" vs "20" 第一位 1 与 2 → -1，低于阈值应触发；删除自相矛盾推演）；essentials 族先于 game 族、各族阈值从低到高、同阈值按登记顺序；旧格式边界（17 个默认登记均无 from_old_format → Array→Hash 为空 Hash 并跳过转换，登记接口存在不等于已有实际适配）。
- **WP10-R02**：转换备份是内存 Hash 序列化到固定路径的快照（非原文件逐字节复制；紧急保存备份才是逐块复制）；备份不随读取路径变化（默认/默认 .bak/自定义三例的备份与写回目标）。
- **WP10-R03**：启动值读取到 UI 校验/递归备份的完整链（早期启动值错误可能不到达备份界面；读取/转换抛错与返回无效 Hash 分开；备份递归 .bak.bak；拒绝删除退出；删除失败提示）；缺地图时调试选图/取消与非调试报错（与 events=nil 的地图损坏分开，不全部归为 WP77 待证）。
- **WP10-R04**：紧急保存（保存旧 scene 后置 nil、无 player 直接返回不恢复 scene、无旧档也可尝试新建保存、备份复制失败可阻止保存、成功提示"旧档已备份"仅在存在旧档时成立、scene 恢复只在正常走到底时执行）；两种模式的主流程 Hangup 分支均调用紧急保存（非调试先打印、调试重抛后由外层转 Reset），前提是 Hangup 到达该分支。
- **WP10-R05**：14 项转换目录补实际前提/跳过条件/关键输出/缺失值行为；寄养反例（旧 A 填入两个新槽、旧 B 找不到空槽——不是一对一保留，空旧槽以 MANAPHY 50 级占位）与电话反例（转换调用访问运行全局的方法，但调用者时机早于全局载入，不能写成无条件成功）均登记为参考快照观察，不修 reference。
- **BATCH-C01**：文本域由"30 个、编号不连续"修正为"31 个、编号 0–30 连续"。
- **跨包核对**：WP08 语言切换直写与 WP09 保存边界一致（直写不经 Game.save）；WP09 的 loaded/default/valid 与 WP10 的损坏/备份前提一致（valid? 不容忍缺键、启动值错误可能不到达备份界面）；WP10 转换比较调用与 WP05 比较器、两层主程序 Hangup 与 WP07 诊断限制一致（引用不重复定义）；转换前后内存对象、运行全局对象、原文件与备份文件未混为同一份状态。
- **矩阵增量**：F02-05、F03-01、F03-03、F03-02、F03-04 均保持 ReviewPending（关联批次复审修订记录），未升级。
- 三包修订稿 v2 状态均为 **ReviewPending**，统一送外部 review；未自行升级 Reviewed；未执行 WP11。
