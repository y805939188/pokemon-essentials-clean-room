# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-19 WP03 存在条件收紧后）

| 文件 | SHA-256（前 8 位速记） | 完整 SHA-256 | 字节数 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `1ca34f44` | `1ca34f4442f4e997359addfb797ac209407a69ea6f3065740d65c75093b86e0e` | 29,838 |
| `planning/module-map.md` | `32eab70d` | `32eab70d503be63ceba06287afb648ec0b1b5fe8ca6225aaab28975c67360352` | 17,523 |
| `planning/feature-matrix.md` | `55770385` | `55770385ebf478ee5c4e2bf729fb9086f3d48e0e54845f2460127542221c80e4` | 29,196 |
| `planning/extraction-plan.md` | `c1735877` | `c173587708c9fcaaaaa1a4079bdedaa14d02405871b3fe3cd2ed6d16caeffd78` | 46,915 |
| `specs/demo/wp01-baseline-and-evidence-scope.md`（WP01 修订稿 v4） | `2a52e94e` | `2a52e94e615d0f1f45d55b0d14317b79e58bc6f988b76095e044f770ca41b407` | 16,543 |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md`（WP02 修订稿 v4） | `82b47151` | `82b471510ff563e6964697cb28e77ae816e190062dfafc9e328f44a81c2131fa` | 37,817 |
| `specs/kernel/wp02-settings-inventory-appendix.md`（WP02 附表 v2） | `f165b1cb` | `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e` | 16,555 |
| `specs/kernel/wp03-content-identity-and-schema.md`（WP03 修订稿 v4） | `7a9c85da` | `7a9c85dae2031c167f172395dc4b769d6bd16575ce48310127249445df079575` | 30,257 |
| `analysis/inventory/wp02_settings_common.py` | `ba01d4d2` | `ba01d4d23f6f2eef42b123befc6809d09bfac282a7dd9f928aa6ac31427a868d` | 8,231 |
| `analysis/inventory/wp02_settings_inventory.py` | `dfa38c40` | `dfa38c407258607da467e6c609e0b75c78485dc974e85f387aa9cd12969c0ca3` | 1,491 |
| `analysis/inventory/wp02_build_appendix.py` | `7c965c9d` | `7c965c9d36a7eccb039a703312aa10a6c418fc120db769b888666c03d73c03d6` | 12,192 |
| `analysis/inventory/wp02-regen-check-2026-09-19.md` | `8ce853cc` | `8ce853cc28577ca3567407fe4b92d97e2f319835508834e5ae7cbd4151bdd05e` | 3,323 |
| `analysis/inventory/out/wp02-settings-inventory-appendix.md`（临时输出） | `f165b1cb` | `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e` | 16,555 |
| `review/joint-review-2026-09-19.md`（联合 review 原件存档） | `f0e0029d` | `f0e0029db9a1e17a9c650a5a936a4ed1dd700e580e78efd305b02d020adf9494` | 12,253 |
| `review/wp01-review-2026-09-19.md`（WP01 复审原件存档） | `e044597c` | `e044597c5d3933d9376c42207da68351063806a285041785b383b877b5afe74b` | 11,708 |
| `review/wp02-review-2026-09-19.md`（WP02 复审原件存档） | `b3923043` | `b39230435fe4a6f1aaa83f68979c9c8a529cc6f176729801c2f1d3eb41e61151` | 18,146 |
| `review/wp02-recheck-2026-09-19.md`（WP02 复检原件存档） | `858adc69` | `858adc69f6d525ac7e4107d9466d02d9e8143e1342dea1ec65652662eed3981a` | 14,343 |
| `review/wp02-closure-review-2026-09-19.md`（WP02 闭合复审原件存档） | `5f963011` | `5f9630118e9fbdda6578106b3ebb96b9db6777519650485d7569d5fb28c49d7d` | 10,820 |
| `review/wp03-review-2026-09-19/report.md`（WP03 复审原件存档） | `6f5bd583` | `6f5bd583ee53b017828f3f3060682b31cf99eb82b5f6a82c6bc74a7eadd88846` | 18,612 |
| `review/wp03-recheck-2026-09-19/report.md`（WP03 复检原件存档） | `799f7c0d` | `799f7c0dfb8fe49add0c3a43659901b55821694d91338cfb6ce70a5ec906296d` | 14,947 |
| `review/wp03-recheck-v3-2026-09-19/report.md`（WP03 v3 复检原件存档） | `3f2d9661` | `3f2d9661cda4d3b96deef7b1bb88b0b30d3274131f8c0837352d5ae8623d3a3a` | 7,776 |

关联基线：参考仓库 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`）。Git 状态证据的精确记录见 WP01 修订稿第 3 节（2026-09-19 15:32，R 内检查）。

## 2. 送审对应关系记录

### 2.1 当前哈希对应（已确认，可核实）

- 2026-09-19 五轮 review（联合 review、WP01 复审、WP02 复审、WP02 复检、WP02 闭合复审）实测哈希均与当时本地文件一致，对应关系见第 3 节历史。
- 2026-09-19 WP03 复审实测 WP03 首版（`d61233f0`）、矩阵（`816b0536`）、WP01 v3（`c952847d`）、WP02 v3（`272b0291`）与当时 manifest 的 18 项哈希及字节数全部相符。
- 2026-09-19 WP03 复检实测 WP03 v2（`f7213e83`）等 19 项哈希全部匹配、18 项字节数匹配；并指出 WP03 复审原件字节记录错误（15,034→18,612，WP03-C04，已修正）。
- 2026-09-19 WP03 v3 复检实测 WP03 v3（`f1d8a763`）等 20 项哈希与字节数全部一致；本地独立重算结果一致。本轮修订后 WP03 的当前哈希已变为 `7a9c85da`；复检实际审查的是修订前版本，新哈希不伪称为复审对象。
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
| `planning/feature-matrix.md` | `2f4e3e31` → `5b6c7b29` → `55f6d01c` → `816b0536` | 2026-09-19 | 依次经 R02/R03/WP01、C02/WP02、状态回填+WP03 追踪、WP03 复审关联修订为 `55770385`（当前有效） |
| `planning/extraction-plan.md` | `aef0d7ab` → `d441c68b` | 2026-09-19 | 依次经 R02/R03、C02 修订为 `c1735877`（当前有效） |
| `specs/demo/wp01-baseline-and-evidence-scope.md` | `403e814c` → `515500c2` → `2c1a553e` → `c952847d` | 2026-09-19 | 依次经 WP01-R01/R02/R03、C02、状态回填、尾部状态同步（C03）修订为 `2a52e94e`（当前有效） |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md` | `d322cf95` → `4352c450` → `d6ef14ae` → `272b0291` | 2026-09-19 | 依次经 WP02-R01～R06、F1/F2/C1、状态回填、尾部状态同步（C03）修订为 `82b47151`（当前有效） |
| `specs/kernel/wp02-settings-inventory-appendix.md` | `6fba2cdd` | 2026-09-19 附表首版 | 经 F1/F2 修订被 `f165b1cb` 替代（当前有效） |
| `specs/kernel/wp03-content-identity-and-schema.md` | `d61233f0` → `f7213e83` → `f1d8a763` | 2026-09-19 | 首版经 WP03-R01～R05 修订为 `f7213e83`；经复检四组剩余项修订为 `f1d8a763`；本轮经枚举存在条件收紧被 `7a9c85da` 替代 |
| `analysis/inventory/wp02_settings_inventory.py` | `46f1ba84` | 2026-09-19 | 重构为共享模块后被 `dfa38c40` 替代（当前有效） |
| `analysis/inventory/wp02_build_appendix.py` | `898134d0` | 2026-09-19 | 重构为共享模块后被 `7c965c9d` 替代（当前有效） |

## 4. 2026-09-19 修订与交付摘要（按轮次）

**第一轮（联合 review 处理 + WP01）**：R01 版本对应确认并保留历史；R02 extraction-plan 新增第 2.1 节状态约定、feature-matrix 同步；R03 WP46 完成条件限定本包范围；交付 WP01 首版。

**第二轮（WP01 复审处理 + WP02 首版）**：WP01 修订稿 v1（Git 证据分离、来源逐项标注、候选变体表述）；C01 清单分层表述、C02 总控文档阶段说明；交付 WP02 首版。

**第三轮（WP02 复审处理）**：WP02-R01～R06 全部修订（逐定义清单附表、数值语义、命中分层、PBS 边界、语言层次、静态场景）；C01/C02/C03 同步。

**第四轮（WP02 复检处理）**：F1 附表值与表格结构（共享解析模块重构）、F2 设施引用集合（实际解析为 10）、C1 维护项；临时目录重跑并与交付附表 diff 一致。

**第五轮（闭合复审状态回填 + WP03 首版）**：闭合复审归档；WP01/WP02 限定范围回填 Reviewed；矩阵 F01-01/F02-03/F18-07 同步；交付 WP03 首版。

**第六轮（WP03 复审处理）**：WP03-R01 按类例外与查询副作用、WP03-R02 重复处理按入口分开、WP03-R03 schema 事实与错误入口、WP03-R04 加载边界与资源来源、WP03-R05 字段组责任目录；WP03-C01 计数口径、WP03-C03 尾部状态同步。

**第七轮（WP03 复检处理）**：R01 电话默认键三入口与遭遇枚举实现描述、R02 遭遇槽权重累加合并与节身份拒绝、R04 move2anim 回退前提、R05 责任表补 Type/Ability 与七处错配、C04 复审原件字节修正。

**第八轮（WP03 v3 复检处理，本轮）**：

- WP03-R01 剩余项：遭遇按版本枚举收紧为存在条件——在正常编译的符号键表中，目标版本 v > 0 时枚举所有已存在的版本 v 条目，同时枚举所有已存在的版本 0 条目（不论同地图是否已有版本 v）；不会生成缺失版本的记录；v = 0 时仅枚举已存在的版本 0 条目。静态场景补入四格存在条件（已有 0、2 → 产出 0、2；仅 0 → 仅 0；仅 2 → 仅 2；均无 → 无；均不改变表内容）。保留 `get` 的版本回退与 `exists?` 的精确组合检查，不与枚举混为入口。
- R02/R04/R05/C04 及此前全部关闭项保持关闭，未重开。
- 矩阵 F01-02/F02-01 保持 ReviewPending，未升级；WP03 修订稿 v4（`7a9c85da`）状态为 **ReviewPending**，送外部 review；未执行 WP04。
