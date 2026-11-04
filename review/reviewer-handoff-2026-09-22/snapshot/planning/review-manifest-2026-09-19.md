# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-22 WP11–WP13 v2 复审修订后）

| 文件 | SHA-256（前 8 位速记） | 完整 SHA-256 | 字节数 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `1ca34f44` | `1ca34f4442f4e997359addfb797ac209407a69ea6f3065740d65c75093b86e0e` | 29,838 |
| `planning/module-map.md` | `32eab70d` | `32eab70d503be63ceba06287afb648ec0b1b5fe8ca6225aaab28975c67360352` | 17,523 |
| `planning/feature-matrix.md` | `55352c01` | `55352c019b90f84411f8dc54a6ab890321394b86cfb06add89ef660fdd1f2bce` | 33,653 |
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
| `specs/kernel/wp08-localization.md`（WP08 修订稿 v4，状态回填） | `4aa7c989` | `4aa7c989d3874e63cfc9772f0e04c1c71b4f511c022a3d632a7df6e62dc4b331` | 18,258 |
| `specs/kernel/wp09-save-startup-continue.md`（WP09 修订稿 v3） | `76450356` | `76450356b03f11abc59808e84c7c07e0f69c3f6543aaafc9b1856b3cdf2de4e6` | 18,087 |
| `specs/kernel/wp10-migration-failure-recovery.md`（WP10 修订稿 v4，状态回填+C04） | `b01a9fc7` | `b01a9fc7315bcef7fd5e9a246c147d0dcf5597f134abcc42ce33d9dc8c2df17b` | 22,733 |
| `specs/overworld/wp11-map-topology-transfer.md`（WP11 修订稿 v3） | `df39a9e5` | `df39a9e5210b4fdd3ff63f27a76b82fbb0ed37d13c6e6bd53e4160e5b36c1f36` | 19,521 |
| `specs/overworld/wp12-terrain-movement-vehicles.md`（WP12 修订稿 v3） | `7f1979bd` | `7f1979bd4734cc2f878117b934589f1e5ccf26754984d703d3e14701f9cee974` | 31,489 |
| `specs/overworld/wp13-map-events-npc-followers.md`（WP13 修订稿 v3） | `1ec410b6` | `1ec410b6d084d841ba0701e6089d6c7b1e11a4eda2f2e6294a21ce1dce3d5f97` | 27,706 |
| `specs/overworld/wp13-interpreter-command-matrix.md`（WP13 命令兼容矩阵附表 v3） | `ab69bc87` | `ab69bc87c97b805f1a2f0848a35e9b86aa8b582f8128553038f2487b85245de5` | 17,561 |
| `specs/overworld/wp13-move-route-matrix.md`（WP13 移动路线附表 v2） | `f637f1c3` | `f637f1c32db9fd59e93b0b3c81f33637f22e715dfeaaabb74f5fad6a71db12c7` | 8,315 |
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
| `review/wp08-wp10-review-2026-09-19/report.md` | `4e455ffc` | `4e455ffc6295c470477653dc2aa6b3a24968e527904c3f9af154d0c3a254635b` | 21,222 |
| `review/wp08-wp10-review-2026-09-19/revision-prompt.md` | `ebfc287b` | `ebfc287b9a61659b9a77da301c96bae21b65c8904fe1125f3435b9afb60fcd09` | 7,637 |
| `review/wp08-wp10-recheck-2026-09-19/report.md` | `03ac20b4` | `03ac20b4a64bdd868affe6ada45822f6580b2c23eaef108492701e4299251e62` | 10,903 |
| `review/wp08-wp10-recheck-2026-09-19/revision-prompt.md` | `facc4d4c` | `facc4d4c9b17864b11ce2331e818eb9f75c5dea7202fcdcc1c1d1a0429f02b4c` | 4,040 |
| `review/wp08-wp10-closure-review-2026-09-19/report.md` | `f414b7ff` | `f414b7ff4232d6df892b8c90cc9c7ea0e43e2955546a01349b4bd24fda9c6150` | 7,335 |
| `review/wp08-wp10-closure-review-2026-09-19/next-batch-prompt.md` | `22fe65a9` | `22fe65a9602b7a9d15cdfe0d52cc7d25c8f21d5a7060690371f1805bb22bec99` | 10,818 |
| `review/wp11-wp13-review-2026-09-19/report.md` | `490e02ac` | `490e02ac1030e11c869699bad9c8f402dcd9322a4d65d9df5ae71e39df40692d` | 21,538 |
| `review/wp11-wp13-review-2026-09-19/revision-prompt.md` | `bc6c9624` | `bc6c9624c2fc941756080f0c2698d5b313688d66de4cae1ec227996c57c038f7` | 9,769 |
| `review/wp11-wp13-review-2026-09-19/revision-response.md` | `048cf40b` | `048cf40b059647e3feed3a184ddeee4b46aa4334ec50f6a1dad4b910098f545d` | 12,906 |
| `review/wp11-wp13-review-2026-09-19/revision-diffs/wp11-map-topology-transfer.diff` | `031308f7` | `031308f7ef3059cd02afd2b673cbea0e73ccc2c8d39e23a1bd4cbacc23f902a8` | 23,168 |
| `review/wp11-wp13-review-2026-09-19/revision-diffs/wp12-terrain-movement-vehicles.diff` | `5dd8b477` | `5dd8b477ab85d0b013b757c40ac60ce84799f70c96cf0e3d73cce55e75419195` | 31,633 |
| `review/wp11-wp13-review-2026-09-19/revision-diffs/wp13-map-events-npc-followers.diff` | `a5dc6d8f` | `a5dc6d8f53a14ce0872e4a1c6cdabfbd7e893bb021efaf90521cb5cec3178681` | 28,599 |
| `review/wp11-wp13-review-2026-09-19/revision-diffs/wp13-interpreter-command-matrix.diff` | `367d0e0c` | `367d0e0c4f6e159d993e1147a6139bd05e44795bc53fcb8912b68e5411a4559c` | 23,105 |
| `review/wp11-wp13-recheck-2026-09-20/report.md` | `80d829f3` | `80d829f306e2aba9d19b25dfd89acb4ebe602b422bb2ce9e8ef8ea0f38ca5854` | 20,746 |
| `review/wp11-wp13-recheck-2026-09-20/revision-prompt.md` | `5cf2dd7e` | `5cf2dd7eda388586a035a8cc5f0c6e901597f3af723b356f3c3ba763fd686354` | 8,784 |
| `review/wp11-wp13-recheck-2026-09-20/revision-response.md` | `afeca04a` | `afeca04a52f7b0a447fb68c51e876144e29a4e3abdb8a8c42a8828aa7bc2833a` | 9,382 |
| `review/wp11-wp13-recheck-2026-09-20/revision-diffs/wp11-map-topology-transfer.diff` | `d82215d7` | `d82215d749cc1ab8b6215f174eb539c5730d6d688c174c94ba28b0b5a44f3af1` | 8,713 |
| `review/wp11-wp13-recheck-2026-09-20/revision-diffs/wp12-terrain-movement-vehicles.diff` | `407f47a7` | `407f47a7679e58a99fa76a9c30880825de41aea0a14d7cde1f03fe22c659bf8a` | 18,060 |
| `review/wp11-wp13-recheck-2026-09-20/revision-diffs/wp13-map-events-npc-followers.diff` | `995070d2` | `995070d2cbe6ad4ad6e3bbb767b59e269eed77f2c29c6bde919d4e9d5ed981c2` | 17,398 |
| `review/wp11-wp13-recheck-2026-09-20/revision-diffs/wp13-interpreter-command-matrix.diff` | `393b8c0c` | `393b8c0cd21db2bf97b4e96d3e3fbab6dc92c85f48d444ed3f63613b46bff6d3` | 1,621 |
| `review/wp11-wp13-recheck-2026-09-20/revision-diffs/wp13-move-route-matrix.diff` | `355c9260` | `355c9260e88b31af17e815cdce8074df32a67032e1bb292556c7b4fb15efcd47` | 5,313 |

关联基线：参考仓库 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`）。Git 状态证据的精确记录见 WP01 修订稿第 3 节（2026-09-19 15:32，R 内检查）。

## 2. 送审对应关系记录

### 2.1 当前哈希对应（已确认，可核实）

- 2026-09-19 各轮 review 实测哈希均与当时本地文件一致，对应关系见第 3 节历史。
- 2026-09-19 WP08–WP10 闭合复审实测三包 v3（WP08 `65a79ab5`、WP09 `76450356`、WP10 `d50edf92`）与当时 manifest 的 39 项哈希及字节数全部匹配；本地独立重算结果一致。本轮回填与批次交付后，WP08/WP10 的当前哈希已变为 `4aa7c989` / `b01a9fc7`，矩阵已变为 `c0aaaf1e`；闭合复审实际审查的是回填前版本，新哈希为管理性状态变更，不伪称为复审对象。
- 结论：各轮 review 的审查对象均能与本地文件对应；本轮修订前的被审版本即第 3 节所列历史版本。
- 2026-09-19 WP11–WP13 批次复审修订前，实测四份被审文件与 manifest（`c14b62d1`，17,435 字节）的 SHA-256 及字节数与复审 report.md 第 1 节固定版本全部一致，修订意见适用；修订后三包与命令矩阵新哈希为 `ac090bc1` / `92dba89d` / `a1288287` / `6da4a23e`，新增移动路线附表 `77cbdb3d`；被审哈希保留于第 3 节历史，复审实际审查的是修订前版本，新哈希不伪称为复审对象。
- 2026-09-22 WP11–WP13 v2 复审修订前，实测五份规格/附表、manifest（`fd03ca37`，22,721 字节）与 feature-matrix（`033e48b7`）的 SHA-256 及字节数与 v2 复审 report.md 第 1 节固定版本全部一致，修订意见适用；修订后三包、两附表新哈希为 `df39a9e5` / `7f1979bd` / `1ec410b6` / `ab69bc87` / `f637f1c3`；v2 被审哈希保留于第 3 节历史，v2 复审实际审查的是 v2 版本，v3 新哈希不伪称为复审对象。

### 2.2 历史版本关系（据本地记录重建，证据受限）

- 2026-09-19 14:18:53 四份总控文档定稿；约 14:38 首次计算哈希并写入清单（历史条目见第 3 节）。
- 2026-09-19 14:39:03，overview 与 module-map 在本地被进一步修订（内容增大、行数不变），送审附件为 14:39 版，清单未同步，造成联合 review 实测值与清单记录不一致（联合 review R01）。
- **证据限制**：14:39 的修改时刻来自本地文件 mtime；变更范围（补核 E04 训练家引用、E11 HTTP 工具、E21 参战/布局，细化总览 §3 与 module-map D01/D11 行）是本地模型比对当前版本与此前阅读记录后重建的说明。**没有该次修改的操作日志或旧版全文**；14:39 之前的两版内容（`0421575b` / `0e22b7f2`）在本地已被覆盖、无留存副本，无法提供逐行 diff。不补造旧版本或历史日志。

## 3. 历史条目（已被替代，仅供追溯）

| 文件 | 旧 SHA-256（前 8 位） | 记录时点 | 替代关系 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `0421575b` | 2026-09-19 约 14:38 | 被 14:39 修订版 `1ca34f44` 替代 |
| `planning/module-map.md` | `0e22b7f2` | 2026-09-19 约 14:38 | 被 14:39 修订版 `32eab70d` 替代 |
| `planning/feature-matrix.md` | `2f4e3e31` → … → `033e48b7` | 2026-09-19 | 依次经 R02/R03/WP01、C02/WP02、状态回填+WP03 追踪、WP03 复审关联、WP03 回填+WP04–WP07 追踪、批次复审关联、三包回填、WP06 回填+WP08–WP10 追踪、批次复审关联、WP09 回填修订、WP08/WP10 回填与 WP11–WP13 追踪修订、WP11–WP13 复审修订（v2 状态与移动路线附表登记）；2026-09-22 经 v2 复审修订（v3 状态与关闭项登记）被 `55352c01` 替代 |
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
| `specs/kernel/wp08-localization.md` | `1f2fd3a6` → … → `65a79ab5` | 2026-09-19 | 首版经 WP08-R01～R03、R01 旧总结清理修订为 `65a79ab5`（闭合通过版）；本轮经状态回填被 `4aa7c989` 替代 |
| `specs/kernel/wp09-save-startup-continue.md` | `359eb1c1` → … → `76450356` | 2026-09-19 | 首版经 WP09-R01～R03、状态回填与 BATCH-C02 限定修订为 `76450356`（v2 通过版，当前有效） |
| `specs/kernel/wp10-migration-failure-recovery.md` | `12018885` → … → `d50edf92` | 2026-09-19 | 首版经 WP10-R01～R05、三处条件收紧与 BATCH-C03 修订为 `d50edf92`（闭合通过版）；本轮经状态回填与 BATCH-C04 维护被 `b01a9fc7` 替代 |
| `analysis/inventory/wp02_settings_inventory.py` | `46f1ba84` | 2026-09-19 | 重构为共享模块后被 `dfa38c40` 替代（当前有效） |
| `analysis/inventory/wp02_build_appendix.py` | `898134d0` | 2026-09-19 | 重构为共享模块后被 `7c965c9d` 替代（当前有效） |
| `specs/overworld/wp11-map-topology-transfer.md` | `7f1274c2` → `ac090bc1` | 2026-09-19 首版送审 | 首版经 WP11-R01/R02/C01 修订为 `ac090bc1`（v2）；2026-09-22 经 v2 复审 WP11-R02 剩余范围修订被 `df39a9e5` 替代（当前有效） |
| `specs/overworld/wp12-terrain-movement-vehicles.md` | `9bc37359` → `92dba89d` | 2026-09-19 首版送审 | 首版经 WP12-R01/R02/R03 修订为 `92dba89d`（v2）；2026-09-22 经 v2 复审剩余范围修订被 `7f1979bd` 替代（当前有效） |
| `specs/overworld/wp13-map-events-npc-followers.md` | `86d96672` → `a1288287` | 2026-09-19 首版送审 | 首版经 WP13-R01–R05 修订为 `a1288287`（v2）；2026-09-22 经 v2 复审剩余范围修订被 `1ec410b6` 替代（当前有效） |
| `specs/overworld/wp13-interpreter-command-matrix.md` | `1ff42842` → `6da4a23e` | 2026-09-19 首版送审 | 首版经 WP13-R01/R02 修订为 `6da4a23e`（v2）；2026-09-22 经 v2 复审 WP13-R02 剩余范围修订被 `ab69bc87` 替代（当前有效） |
| `specs/overworld/wp13-move-route-matrix.md` | `77cbdb3d` | 2026-09-19 附表首版 | 2026-09-22 经 v2 复审 WP13-R01 剩余范围修订被 `f637f1c3` 替代（当前有效） |

## 4. 2026-09-19 修订与交付摘要（按轮次）

**第一轮至第十四轮**：联合 review 处理与 WP01；WP01 复审处理与 WP02 首版；WP02 复审处理（R01～R06）；WP02 复检处理（F1/F2/C1）；WP02 闭合状态回填与 WP03 首版；WP03 复审处理（R01–R05）；WP03 复检处理（四组剩余项）；WP03 v3 复检处理（枚举存在条件收紧）；WP03 闭合状态回填与 WP04–WP07 批次首版；WP04–WP07 批次复审修订；WP04–WP07 复检六项修订；三包状态回填与 WP06 定点修订；WP06 闭合登记与 WP08–WP10 批次首版；WP08–WP10 批次复审修订；WP09 回填与 WP08/WP10 剩余项修订。

**第十五轮（WP08/WP10 闭合登记 + WP11–WP13 批次，本轮）**：

- **WP08/WP10 状态回填**：WP08 → Reviewed（文本域与已述身份形态、默认/当前语言消息分层、主动/延迟载入、查找/空译/异常边界、占位格式化、提取/编译/直写工作流及适用静态场景范围）；WP10 → Reviewed（固定默认转换登记、版本筛选/顺序、旧格式入口边界、备份与写回路径、已述恢复/紧急保存/地图失败分支、转换目录及已记录参考快照反例范围）；矩阵 F02-05、F03-02、F03-04 同步；被审哈希保留于历史。
- **BATCH-C04 维护**：WP10 树果转换行改为"构造新对象→条件填充→正常到达末尾时替换条目"（非符号输入跳过条件填充仍可到达末尾替换；填充抛错时尚未执行末尾替换）。
- **WP11（地图拓扑与转移）**：地图身份与加载（setup/valid?/validLax?）；连接配置与坐标/偏移规则（边字母换算 N/W→0、E→宽、S→高、显式坐标、双向索引、两端尺寸为 0 忽略）；边缘跨图（连接换算、on_leave_map/on_enter_map、天气重置）；显式传送（取消载具、setup 重建、moveto/转身、跟随者转移、精灵集重建）；生命周期（邻图加载/显示偏移/连接与范围修剪、地图索引错误处理）；地图恢复分支（WP09/WP10 引用）。`7f1274c2`
- **WP12（地形/运动/载具）**：18 个地形标签能力表；通行判定链（通行位/事件阻挡/玩家阻挡/水约束/冰/岩架/桥/冲浪/骑行/严格通行/调试穿透/跨图）；移动入口与结果（move_generic 移动/岩架跳下/下瀑/碰撞）；运动状态机（步行 3/跑步 4/骑行 5/冲浪 4/潜水 3/冰滑 4/瀑布 2 及停止态）；载具函数（上下车、目的地清理、BGM）；瀑布下/上瀑；许可与领域边界（跑鞋/强制路线/徽章交界）。`9bc37359`
- **WP13（地图事件/NPC/跟随）**：事件页选择（从后向前、条件满足、nil 页不可见可穿透）；触发方式（动作键/玩家接触/事件接触/自动运行/并行处理/感知 sight-trainer/counter）；解释器更新循环（冻结防护/失联终止/子解释器/消息/移动/上岸/计时/菜单等待/深度 100 限制）；命令兼容矩阵（48 有实现/18 空操作 command_dummy/2 标记/else 回退）；NPC 移动与感知；跟随者生命周期（FollowerData、实例化、移动/转向/更新、转移限制 followers=0 守卫、持久化与弃用格式）。`86d96672`、`1ff42842`
- **跨包核对**：WP11 转移与 WP12 移动结果一致（跨图通行引用）；WP12 移动与 WP13 触发/等待/跟随一致（步后触发与 over_trigger 联动）；WP13 解释器与 WP05 通知一致（事件通知引用）；WP11 地图恢复与 WP09/WP10 分支一致（引用不重复）；WP13 命令与 WP04 编译转换一致（简写转换与运行时解释器）。未发现规则重复定义或冲突。
- **矩阵增量**：F04-01 → ReviewPending（WP11）＋Inventoried（元数据语义与可达）；F04-02、F04-03 → ReviewPending（WP12）＋Inventoried（真实地图流程/场地招式媒体）；F04-04、F04-05 → ReviewPending（WP13）＋Inventoried（Demo 事件/完整跟随系统）。
- 三包状态均为 **ReviewPending**，统一送外部 review；未自行升级 Reviewed；未执行 WP14。

**第十六轮（WP11–WP13 批次复审修订，本轮）**：

- **复审处理**：外部复审 REQUEST_CHANGES（WP11-R01/R02/C01、WP12-R01/R02/R03、WP13-R01–R05）。修订前实测四份被审文件与 manifest 哈希/字节数与复审固定版本一致；逐项核实→修订→新哈希→清单更新，修复回应见 `review/wp11-wp13-review-2026-09-19/revision-response.md`（`048cf40b`），逐项差异见同目录 `revision-diffs/`。
- **WP11 v2（`ac090bc1`）**：连接端点改为二维锚点定义（N/S 配置值为锚点 x、边值为 y；E/W 反之；显式坐标直用）；修正两个坐标场景（(xA−6, 0)、人工 wB=20 得 (19,2) 及反向例）；显示偏移按子像素单位（REAL_RES=128/格）；四入口转移对照（边缘/同图/跨图 setup/读档恢复）补 moving 守卫、普通移动出界检查、moveto 取模、索引回退、通知时机与玩家位置、缺图入口差异；生命周期补实例复用/重建与临时/持久自开关分层；5.1 表头补证据列。
- **WP12 v2（`92dba89d`）**：通行判定重构为五层（地图层/玩家专用层/角色层/玩家覆写/跟随者严格入口），水/冰限制归非玩家分支；can_run? 补 diving 例外与 must_walk/must_walk_or_run 区分；速度表加非强制路线与 bumping 前提及等级/时间换算；岩架失败不转碰撞；increase_steps 实际行为与计步层次（全局计步引用 WP06）；pbEndSurf 仅结束冲浪、上水另一入口；瀑布清理两分支与调用链；pbCancelVehicles 参数语义与重复上车不计数。
- **WP13 v2（`a1288287`、`6da4a23e`、新增 `77cbdb3d`）**：命令矩阵 10 项误报改空操作（126/133/301/311–313/315–318），统计改 28 dummy + 2 标记 + 66 其他入口（96 分派）并加口径；补 401/655 续行消费；控制结果列逐行区分启动效果/等待/推进（209 vs 210、203、205–207/223–225/232–236/242/246、233、105 双推进、111/122/314/204/353/355 实际语义）；失联改"event_id 归 0、列表继续"并与命令结束/显式退出分列；触发按调用者分入口（over_trigger? 非 through 别名、感知两种检查、更新机会与菜单差别）；跟随补全（去重/移除/领队链/相连与不相连/即时定位/转移后隐藏恢复/互动/守卫适用入口）；新增移动路线命令矩阵附表。
- **交叉检查**：WP11×WP12 载具清理调用点一致；WP12×WP06 计步引用不重复定义；WP13×WP11/12 跟随与路线通行引用一致；WP13×WP07 脚本异常分层一致；WP11×WP09/10 缺图入口差异一致。
- 三包状态保持 **ReviewPending**，v2 再送外部复审；未自行升级 Reviewed；未执行 WP14；未修改 reference/；未提交/推送。

**第十七轮（WP11–WP13 v2 复审修订，本轮，2026-09-22）**：

- **复审处理**：v2 独立复审结论为 WP11/WP12/WP13 分别 REQUEST_CHANGES（剩余 1/3/4 项），WP11-R01、WP11-C01、WP13-R03 关闭。修订前实测五份规格/附表、manifest 与 feature-matrix 哈希/字节数与复审固定版本全部一致；逐项核实→修订→新哈希→清单更新，修复回应见 `review/wp11-wp13-recheck-2026-09-20/revision-response.md`（`afeca04a`），逐项差异见同目录 `revision-diffs/`。
- **WP11 v3（`df39a9e5`）**：显式传送缺图失败按音频前提分两阶段（有 BGM/BGS 时 autofade 先于清桥/setup 读取目标图即失败；无音频时到达 setup 后失败），不再统一"失败时集合已清空"。
- **WP12 v3（`7f1979bd`）**：优先级 0 图块事件的提前许可明确为"结束本次地图层判定"（角色层碰撞仍执行）；层 5 区分跟随者实际入口（location_passable?/move_through）与全向 strict 能力（未检索到默认调用链）；计步层次改为运动开始/完成两观察点（统计与条件性离格通知在开始侧，全局计步仍引用 WP06）；上水状态提交（前跳前提交、失败无回滚）；surf_jump 清理分层守卫；新增 on_enter_map 的 force_cycling 消费者（强制骑行图上车/禁骑图下车/边缘切图亦触发/同图传送无通知）。
- **WP13 v3（`1ec410b6`、`ab69bc87`、`f637f1c3`）**：路线附表推进规则按运动状态（玩家 bump 置计时也算运动状态）并重写、补空强制路线边界；主文档移动等待补"已置等待标记（210）"前提并删除相反场景括注；矩阵 101 行消费范围纠正（相邻 101 不消费、401/102/103 区分）；触发表按实际调用者重写（玩家失败→玩家侧 [1,2]、NPC 失败→事件侧 trigger 2、步完成同位 here 要求 over_trigger 真、counter 仅移动完成后）；跟随位移改条件分支（同轴一格/两格四种许可组合/非同轴直接定位）。
- **交叉检查**：WP12 层 5 × WP13-R05 共用一处通行定义；force_cycling × WP11 通知时机一致；移动等待 × 强制路线术语一致；全局计步仍归 WP06。
- 三包状态保持 **ReviewPending**，v3 再送外部复审；未自行升级 Reviewed；未执行 WP14；未修改 reference/；未提交/推送。
