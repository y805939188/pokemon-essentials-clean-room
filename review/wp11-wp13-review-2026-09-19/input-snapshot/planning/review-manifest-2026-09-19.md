# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-19 WP08/WP10 回填与 WP11–WP13 批次交付后）

| 文件 | SHA-256（前 8 位速记） | 完整 SHA-256 | 字节数 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `1ca34f44` | `1ca34f4442f4e997359addfb797ac209407a69ea6f3065740d65c75093b86e0e` | 29,838 |
| `planning/module-map.md` | `32eab70d` | `32eab70d503be63ceba06287afb648ec0b1b5fe8ca6225aaab28975c67360352` | 17,523 |
| `planning/feature-matrix.md` | `c0aaaf1e` | `c0aaaf1e4f00ceb2cc8cf84f01affbbbbb4196412d1633e1f80b9db670a09419` | 33,169 |
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
| `specs/overworld/wp11-map-topology-transfer.md`（WP11 主文档） | `7f1274c2` | `7f1274c238289a487a2de27373fb0b6814b927694045247aa61f0709b0806566` | 13,173 |
| `specs/overworld/wp12-terrain-movement-vehicles.md`（WP12 主文档） | `9bc37359` | `9bc37359cc712269bb4399ccf82c4ec5326a31c95102499c790e87726b1813d8` | 16,406 |
| `specs/overworld/wp13-map-events-npc-followers.md`（WP13 主文档） | `86d96672` | `86d96672ff9eb5d0dca7c8bf5c2a7a9232682cf3b84b71da2a896822302e008c` | 15,081 |
| `specs/overworld/wp13-interpreter-command-matrix.md`（WP13 命令兼容矩阵附表） | `1ff42842` | `1ff428423ff1f82028db4583071c4f4e4d8cd7cd7fde8e83a66cbdb8a6221a98` | 14,359 |
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

关联基线：参考仓库 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`）。Git 状态证据的精确记录见 WP01 修订稿第 3 节（2026-09-19 15:32，R 内检查）。

## 2. 送审对应关系记录

### 2.1 当前哈希对应（已确认，可核实）

- 2026-09-19 各轮 review 实测哈希均与当时本地文件一致，对应关系见第 3 节历史。
- 2026-09-19 WP08–WP10 闭合复审实测三包 v3（WP08 `65a79ab5`、WP09 `76450356`、WP10 `d50edf92`）与当时 manifest 的 39 项哈希及字节数全部匹配；本地独立重算结果一致。本轮回填与批次交付后，WP08/WP10 的当前哈希已变为 `4aa7c989` / `b01a9fc7`，矩阵已变为 `c0aaaf1e`；闭合复审实际审查的是回填前版本，新哈希为管理性状态变更，不伪称为复审对象。
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
| `planning/feature-matrix.md` | `2f4e3e31` → … → `4712134b` | 2026-09-19 | 依次经 R02/R03/WP01、C02/WP02、状态回填+WP03 追踪、WP03 复审关联、WP03 回填+WP04–WP07 追踪、批次复审关联、三包回填、WP06 回填+WP08–WP10 追踪、批次复审关联、WP09 回填修订；本轮经 WP08/WP10 回填与 WP11–WP13 追踪修订被 `c0aaaf1e` 替代 |
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
