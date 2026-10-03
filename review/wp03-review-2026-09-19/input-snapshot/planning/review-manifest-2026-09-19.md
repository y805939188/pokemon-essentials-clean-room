# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-19 状态回填与 WP03 交付后）

| 文件 | SHA-256（前 8 位速记） | 完整 SHA-256 | 字节数 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `1ca34f44` | `1ca34f4442f4e997359addfb797ac209407a69ea6f3065740d65c75093b86e0e` | 29,838 |
| `planning/module-map.md` | `32eab70d` | `32eab70d503be63ceba06287afb648ec0b1b5fe8ca6225aaab28975c67360352` | 17,523 |
| `planning/feature-matrix.md` | `816b0536` | `816b05367bfc15f0b52aa87888658cc8347d29ffe3c0fbd05afd28a0d30e6efe` | 29,072 |
| `planning/extraction-plan.md` | `c1735877` | `c173587708c9fcaaaaa1a4079bdedaa14d02405871b3fe3cd2ed6d16caeffd78` | 46,915 |
| `specs/demo/wp01-baseline-and-evidence-scope.md`（WP01 修订稿 v3，状态回填） | `c952847d` | `c952847df72610300bbec20235124ba64d95aa015f0abdbaffe8ca83bb51605b` | 16,419 |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md`（WP02 修订稿 v3，状态回填） | `272b0291` | `272b0291dda4ff81276ad9a519c8f3fa594e0f2d5f305570509b9b3d362677c4` | 37,576 |
| `specs/kernel/wp02-settings-inventory-appendix.md`（WP02 附表 v2） | `f165b1cb` | `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e` | 16,555 |
| `specs/kernel/wp03-content-identity-and-schema.md`（WP03 主文档） | `d61233f0` | `d61233f0ee48a8848cdbf92ee9c42686a01d5028d308dc15772e7d7153d83f54` | 18,721 |
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

关联基线：参考仓库 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`）。Git 状态证据的精确记录见 WP01 修订稿第 3 节（2026-09-19 15:32，R 内检查）。

## 2. 送审对应关系记录

### 2.1 当前哈希对应（已确认，可核实）

- 2026-09-19 四轮 review（联合 review、WP01 复审、WP02 复审、WP02 复检）实测哈希均与当时本地文件一致，对应关系见第 3 节历史。
- 2026-09-19 WP02 闭合复审实测其 manifest 的 16 项完整哈希与字节数均与实际文件一致；本地独立重算，WP02 修订稿 v2（`d6ef14ae`）、附表 v2（`f165b1cb`）、WP01 修订稿 v2（`2c1a553e`）与三份脚本、检查记录的哈希与之完全一致。本轮状态回填**之后**，上述三个文档的当前哈希已变为 `c952847d` / `272b0291` /（矩阵）`816b0536`；闭合复审实际审查的是回填前版本（见第 3 节历史），新哈希为管理性状态变更，不伪称为复审对象。
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
| `planning/feature-matrix.md` | `2f4e3e31` → `5b6c7b29` → `55f6d01c` | 2026-09-19 | 依次经 R02/R03/WP01、C02/WP02 追踪修订；本轮经状态回填与 WP03 追踪修订被 `816b0536` 替代 |
| `planning/extraction-plan.md` | `aef0d7ab` → `d441c68b` | 2026-09-19 | 依次经 R02/R03、C02 修订为 `c1735877`（当前有效） |
| `specs/demo/wp01-baseline-and-evidence-scope.md` | `403e814c` → `515500c2` → `2c1a553e` | 2026-09-19 | 首版经 WP01-R01/R02/R03 修订；v2 经 C02 修订；本轮经状态回填被 `c952847d` 替代 |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md` | `d322cf95` → `4352c450` → `d6ef14ae` | 2026-09-19 | 首版经 WP02-R01～R06 修订；v2 经 F1/F2/C1 修订；本轮经状态回填被 `272b0291` 替代 |
| `specs/kernel/wp02-settings-inventory-appendix.md` | `6fba2cdd` | 2026-09-19 附表首版 | 经 F1/F2 修订被 `f165b1cb` 替代（当前有效） |
| `analysis/inventory/wp02_settings_inventory.py` | `46f1ba84` | 2026-09-19 | 重构为共享模块后被 `dfa38c40` 替代（当前有效） |
| `analysis/inventory/wp02_build_appendix.py` | `898134d0` | 2026-09-19 | 重构为共享模块后被 `7c965c9d` 替代（当前有效） |

## 4. 2026-09-19 修订与交付摘要（按轮次）

**第一轮（联合 review 处理 + WP01）**：R01 版本对应确认并保留历史；R02 extraction-plan 新增第 2.1 节状态约定、feature-matrix 同步；R03 WP46 完成条件限定本包范围；交付 WP01 首版。

**第二轮（WP01 复审处理 + WP02 首版）**：WP01 修订稿 v1（Git 证据分离、来源逐项标注、候选变体表述）；C01 清单分层表述、C02 总控文档阶段说明；交付 WP02 首版。

**第三轮（WP02 复审处理）**：WP02-R01～R06 全部修订（逐定义清单附表、数值语义、命中分层、PBS 边界、语言层次、静态场景）；C01/C02/C03 同步。

**第四轮（WP02 复检处理）**：F1 附表值与表格结构（共享解析模块重构）、F2 设施引用集合（实际解析为 10）、C1 维护项（大小字段、展示行 75、编译调用 22、措辞收窄、引用修正）；临时目录重跑并与交付附表 diff 一致。

**第五轮（闭合复审状态回填 + WP03，本轮）**：

- 闭合复审（PASS_SCOPED）归档于 `review/wp02-closure-review-2026-09-19.md`，历史 review 原件均未改写。
- 状态回填（管理性变更，不改变任何规格内容）：WP01 → Reviewed（基线、材料缺口、待证登记范围；Demo/运行未验证）；WP02 → Reviewed（固定基线配置档案、声明默认/派生、候选材料与输入边界、静态场景范围）；矩阵 F01-01 → Reviewed（WP02 词典范围）＋Inventoried（领域语义）；F02-03 → Reviewed（候选材料登记及发现边界）＋Provisional（切换/编译/兼容）；F18-07 → Reviewed（WP01 基线范围）＋Provisional（WP77 Demo）。未验证的领域语义、数据组合与 Demo 范围保持原状态。
- WP03 交付：`specs/kernel/wp03-content-identity-and-schema.md`——内容身份模型（三类身份与查找语义、21 个作者数据类 + 17 个固定规则类全清单）、注册/查找/缺失值处理（含 OPTIONAL 唯一例 ShadowPokemon）、schema 与编译期校验（重复节名/未定义引用/必需参数）、固定规则与作者数据区分、字段责任目录（全部内容类 → 领域包指派）；矩阵 F01-02、F02-01 → ReviewPending（WP03 范围）＋Inventoried（字段语义全集）。
- WP03 状态为 **ReviewPending**，送外部 review；未执行 WP04。
