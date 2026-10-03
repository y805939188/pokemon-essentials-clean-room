# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-19 WP02 复检处理后）

| 文件 | SHA-256（前 8 位速记） | 完整 SHA-256 | 字节数 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `1ca34f44` | `1ca34f4442f4e997359addfb797ac209407a69ea6f3065740d65c75093b86e0e` | 29,838 |
| `planning/module-map.md` | `32eab70d` | `32eab70d503be63ceba06287afb648ec0b1b5fe8ca6225aaab28975c67360352` | 17,523 |
| `planning/feature-matrix.md` | `55f6d01c` | `55f6d01c191b4b229fcaf1074a181a50629ba279e3bf8dab8cf2bc10d87aceea` | 28,585 |
| `planning/extraction-plan.md` | `c1735877` | `c173587708c9fcaaaaa1a4079bdedaa14d02405871b3fe3cd2ed6d16caeffd78` | 46,915 |
| `specs/demo/wp01-baseline-and-evidence-scope.md`（WP01 修订稿 v2） | `2c1a553e` | `2c1a553e47da58c73696efcfed8039dec0a3f3ed6e81ebedf2e6ab37323d52a2` | 16,363 |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md`（WP02 修订稿 v2） | `d6ef14ae` | `d6ef14ae297beb6bc5a7141e64b3b9b6d0c8074e68aaa6b194a293e891ab7b51` | 37,417 |
| `specs/kernel/wp02-settings-inventory-appendix.md`（WP02 附表 v2） | `f165b1cb` | `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e` | 16,555 |
| `analysis/inventory/wp02_settings_common.py`（共享解析模块） | `ba01d4d2` | `ba01d4d23f6f2eef42b123befc6809d09bfac282a7dd9f928aa6ac31427a868d` | 8,231 |
| `analysis/inventory/wp02_settings_inventory.py`（控制台清单程序） | `dfa38c40` | `dfa38c407258607da467e6c609e0b75c78485dc974e85f387aa9cd12969c0ca3` | 1,491 |
| `analysis/inventory/wp02_build_appendix.py`（附表生成器） | `7c965c9d` | `7c965c9d36a7eccb039a703312aa10a6c418fc120db769b888666c03d73c03d6` | 12,192 |
| `analysis/inventory/wp02-regen-check-2026-09-19.md`（重跑与一致性检查记录） | `8ce853cc` | `8ce853cc28577ca3567407fe4b92d97e2f319835508834e5ae7cbd4151bdd05e` | 3,323 |
| `analysis/inventory/out/wp02-settings-inventory-appendix.md`（临时输出，与交付附表一致） | `f165b1cb` | `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e` | 16,555 |
| `review/joint-review-2026-09-19.md`（联合 review 原件存档） | `f0e0029d` | `f0e0029db9a1e17a9c650a5a936a4ed1dd700e580e78efd305b02d020adf9494` | 12,253 |
| `review/wp01-review-2026-09-19.md`（WP01 复审原件存档） | `e044597c` | `e044597c5d3933d9376c42207da68351063806a285041785b383b877b5afe74b` | 11,708 |
| `review/wp02-review-2026-09-19.md`（WP02 复审原件存档） | `b3923043` | `b39230435fe4a6f1aaa83f68979c9c8a529cc6f176729801c2f1d3eb41e61151` | 18,146 |
| `review/wp02-recheck-2026-09-19.md`（WP02 复检原件存档） | `858adc69` | `858adc69f6d525ac7e4107d9466d02d9e8143e1342dea1ec65652662eed3981a` | 14,343 |

关联基线：参考仓库 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`）。Git 状态证据的精确记录见 WP01 修订稿第 3 节（2026-09-19 15:32，R 内检查）。

## 2. 送审对应关系记录

### 2.1 当前哈希对应（已确认，可核实）

- 2026-09-19 联合 review 实测四份附件哈希 `1ca34f44` / `32eab70d` / `2f4e3e31` / `aef0d7ab`；本地独立重算，overview 与 module-map 结果与之完全一致。
- 2026-09-19 WP01 复审实测 WP01 主文档、extraction-plan、feature-matrix 与联合 review 存档哈希，与当时清单记录一致（`403e814c` / `d441c68b` / `5b6c7b29` / `f0e0029d`）。
- 2026-09-19 WP02 复审实测 WP02 首版、WP01 修订稿 v1、feature-matrix、extraction-plan 哈希，与当时清单记录一致（`d322cf95` / `515500c2` / `55f6d01c` / `c1735877`）；并指出清单中 WP02 字节字段 30,363 与实测 30,364 相差 1 字节——属清单大小字段记录错误，非版本漂移。
- 2026-09-19 WP02 复检实测 WP02 修订稿、附表与两份脚本的哈希（`4352c450` / `6fba2cdd` / `46f1ba84` / `898134d0`），本地独立重算结果与之完全一致；并指出清单中 `wp02_build_appendix.py` 大小字段 11,572 与实测 11,840 不符——该值是脚本两次编辑前的旧记录，哈希当时已正确，属大小字段滞后，非版本漂移。
- 结论：四轮 review 的审查对象均能与本地文件对应；本轮修订前的被审版本即第 3 节所列历史版本。

### 2.2 历史版本关系（据本地记录重建，证据受限）

- 2026-09-19 14:18:53 四份总控文档定稿；约 14:38 首次计算哈希并写入清单（历史条目见第 3 节）。
- 2026-09-19 14:39:03，overview 与 module-map 在本地被进一步修订（内容增大、行数不变），送审附件为 14:39 版，清单未同步，造成联合 review 实测值与清单记录不一致（联合 review R01）。
- **证据限制**：14:39 的修改时刻来自本地文件 mtime；变更范围（补核 E04 训练家引用、E11 HTTP 工具、E21 参战/布局，细化总览 §3 与 module-map D01/D11 行）是本地模型比对当前版本与此前阅读记录后重建的说明。**没有该次修改的操作日志或旧版全文**；14:39 之前的两版内容（`0421575b` / `0e22b7f2`）在本地已被覆盖、无留存副本，无法提供逐行 diff。不补造旧版本或历史日志。

## 3. 历史条目（已被替代，仅供追溯）

| 文件 | 旧 SHA-256（前 8 位） | 记录时点 | 替代关系 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `0421575b` | 2026-09-19 约 14:38 | 被 14:39 修订版 `1ca34f44` 替代 |
| `planning/module-map.md` | `0e22b7f2` | 2026-09-19 约 14:38 | 被 14:39 修订版 `32eab70d` 替代 |
| `planning/feature-matrix.md` | `2f4e3e31` | 2026-09-19 约 14:38 | 经 R02/R03/WP01 追踪修订被 `5b6c7b29` 替代；再经 C02/WP02 追踪修订被 `55f6d01c` 替代 |
| `planning/extraction-plan.md` | `aef0d7ab` | 2026-09-19 约 14:38 | 经 R02/R03 修订被 `d441c68b` 替代；再经 C02 修订被 `c1735877` 替代 |
| `specs/demo/wp01-baseline-and-evidence-scope.md` | `403e814c` → `515500c2` | 2026-09-19 | 首版经 WP01-R01/R02/R03 修订被 `515500c2` 替代；再经 C02 修订被 `2c1a553e` 替代 |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md` | `d322cf95` → `4352c450` | 2026-09-19 | 首版经 WP02-R01～R06 修订被 `4352c450` 替代；再经 F1/F2/C1 修订被 `d6ef14ae` 替代 |
| `specs/kernel/wp02-settings-inventory-appendix.md` | `6fba2cdd` | 2026-09-19 附表首版 | 经 F1/F2 修订被 `f165b1cb` 替代 |
| `analysis/inventory/wp02_settings_inventory.py` | `46f1ba84` | 2026-09-19 | 重构为共享模块后被 `dfa38c40` 替代 |
| `analysis/inventory/wp02_build_appendix.py` | `898134d0` | 2026-09-19 | 重构为共享模块后被 `7c965c9d` 替代 |

## 4. 2026-09-19 修订与交付摘要（按轮次）

**第一轮（联合 review 处理 + WP01）**：R01 版本对应确认并保留历史；R02 extraction-plan 新增第 2.1 节状态约定、feature-matrix 同步；R03 WP46 完成条件限定本包范围；交付 WP01 首版。

**第二轮（WP01 复审处理 + WP02 首版）**：WP01 修订稿 v1（Git 证据分离、来源逐项标注、候选变体表述）；C01 清单分层表述、C02 总控文档阶段说明；交付 WP02 首版。

**第三轮（WP02 复审处理）**：WP02-R01 逐定义清单与统计单位（附表首版）；WP02-R02 数值语义；WP02-R03 命中与消费者分层；WP02-R04 普通发现边界与显式输入例外；WP02-R05 语言层次与任务引用；WP02-R06 静态预期场景；C01 字节说明、C02 WP01 引用注明复审中、C03 目录归类说明。

**第四轮（WP02 复检处理，本轮）**：

- F1（附表值与表格结构）：重构取证脚本为共享模块 `wp02_settings_common.py`（有限形式显式求值器，不执行任意源码表达式；未求值显式报告），控制台清单程序与附表生成器共用，消除解析漂移。修正：元信息取列错误（VERSION/ERROR_TEXT/MKXPZ_VERSION 现显示真实值）；SCALED_EXP_FORMULA 的 `||` 复合条件求值（世代 8 下 true）；APPLY_HAPPINESS_SOFT_CAP 设置间引用解析（默认 false，引用关系留在派生列）；表格单元格竖线转义（逐定义表全部 5 列）；附表第 4 行生成路径说明改为"生成器写出 Markdown、清单程序为独立控制台程序"。临时目录重跑一次：118 常量/3 方法型/3 元信息集合保持，无未求值项，与交付附表 diff 完全一致（记录见 `analysis/inventory/wp02-regen-check-2026-09-19.md`）。
- F2（设施引用集合）：从固定提交的 `battle_facility_lists.txt` 实际解析——1 个 DefaultTrainerList + 4 个 TrainerList，各节 Trainers/Pokemon 字段去重后**被引用输入路径 10 个**；区分"目录存在的候选文件（12）""被当前名单引用的文件（10）""存在但未被引用的候选文件（2：cup_fancy_pkmn.txt、cup_fancy_trainers.txt，用途未调查）"；主文档、附表、生成器同步为该限定表述；完整专用读取路径仍归 WP04。
- C1：`wp02_build_appendix.py` 大小字段滞后说明（11,572 为编辑前旧值，实测 11,840；本轮重写后新值 12,192）；主文档 4.1 展示行改为 75（含 3 个方法型配置）；编译调用改为 22 项内容编译调用（不含发现/改写两个准备调用，修正此前"21 步"）；主文档两处"当前行为由设置文件最终文本决定"收窄为"声明的默认配置由设置文本确定，具体行为仍需消费者、数据、状态和其他选项"；SHINY/POKERUS 行的错误附表章节引用改指第 4.3 节路径。
- WP01 修订稿 v2、WP02 修订稿 v2 与附表 v2 状态均为 **ReviewPending**，一并送外部 review；未自行标为 Reviewed。
