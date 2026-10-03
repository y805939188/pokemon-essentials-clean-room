# 版本清单与送审记录（2026-09-19）

用途：固定总控文档与各工作包产物的版本，供外部 review 按「文件 + 哈希前缀 + 行号」引用。
本清单本身不纳入自哈希；每次内容修订后重算并在此追加记录，旧条目保留为历史、标注替代关系，不回写抹除。

## 1. 当前有效版本（2026-09-19 WP03 回填与 WP04–WP07 批次交付后）

| 文件 | SHA-256（前 8 位速记） | 完整 SHA-256 | 字节数 |
| --- | --- | --- | --- |
| `analysis/repository-overview.md` | `1ca34f44` | `1ca34f4442f4e997359addfb797ac209407a69ea6f3065740d65c75093b86e0e` | 29,838 |
| `planning/module-map.md` | `32eab70d` | `32eab70d503be63ceba06287afb648ec0b1b5fe8ca6225aaab28975c67360352` | 17,523 |
| `planning/feature-matrix.md` | `ab2b8f21` | `ab2b8f21bcfbd1ce1dfb81c56b8aa3884c708e6edd5e203b42f81f25855fadfe` | 30,617 |
| `planning/extraction-plan.md` | `c1735877` | `c173587708c9fcaaaaa1a4079bdedaa14d02405871b3fe3cd2ed6d16caeffd78` | 46,915 |
| `specs/demo/wp01-baseline-and-evidence-scope.md`（WP01 修订稿 v4） | `2a52e94e` | `2a52e94e615d0f1f45d55b0d14317b79e58bc6f988b76095e044f770ca41b407` | 16,543 |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md`（WP02 修订稿 v4） | `82b47151` | `82b471510ff563e6964697cb28e77ae816e190062dfafc9e328f44a81c2131fa` | 37,817 |
| `specs/kernel/wp02-settings-inventory-appendix.md`（WP02 附表 v2） | `f165b1cb` | `f165b1cbb32a122100a9d9f844b1184a036ad908b845bae65ae8b0a758601e8e` | 16,555 |
| `specs/kernel/wp03-content-identity-and-schema.md`（WP03 修订稿 v5，状态回填） | `de331460` | `de331460e013bfc07533d0f368967fe729bcf0720d98e7d990a16a0614e9c27d` | 30,708 |
| `specs/kernel/wp04-pbs-lifecycle.md`（WP04 主文档） | `e2bc7e6b` | `e2bc7e6b8d7e71f1a05a62bbb2b66202a618558cf0cf1c57402dbba28819a534` | 14,456 |
| `specs/kernel/wp05-events-extensions-plugins.md`（WP05 主文档） | `a8412720` | `a841272064aad91af5c055a3dcfbd0b47861ae92ff7b83dabe50bdad9b8d24aa` | 13,734 |
| `specs/kernel/wp06-time-random-steps-stats.md`（WP06 主文档） | `c18eae6a` | `c18eae6ab2add4cf4cbbb8233baa6f941439999a675996e84363573c7a2f06dd` | 14,255 |
| `specs/kernel/wp07-diagnostics-files-http.md`（WP07 主文档） | `0225f652` | `0225f652aa929eeda879102707e70cef6afdae6cd0fa38e59e254b836fcced9b` | 12,397 |
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
| `review/wp03-closure-review-2026-09-19/report.md` | `1544a179` | `1544a1794074681b2f0df0e0995479ba76d42998e6e0c189d7600d43d11e9167` | 10,757 |
| `review/wp03-closure-review-2026-09-19/next-batch-prompt.md` | `a8fa4858` | `a8fa4858089357ffe3a6003a1b82793879c84f654877fbdf85a00b09c97e617e` | 7,769 |

关联基线：参考仓库 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（`v21.1-23-g8c5911e4`）。Git 状态证据的精确记录见 WP01 修订稿第 3 节（2026-09-19 15:32，R 内检查）。

## 2. 送审对应关系记录

### 2.1 当前哈希对应（已确认，可核实）

- 2026-09-19 各轮 review 实测哈希均与当时本地文件一致（联合 review、WP01/WP02/WP03 各轮复审、WP02/WP03 闭合复审），对应关系见第 3 节历史。
- 2026-09-19 WP03 闭合复审实测 WP03 v4（`7a9c85da`）与当时 manifest 的 21 项哈希及字节数全部一致；本地独立重算结果一致。本轮状态回填后 WP03 的当前哈希已变为 `de331460`；闭合复审实际审查的是回填前版本，新哈希为管理性状态变更，不伪称为复审对象。
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
| `planning/feature-matrix.md` | `2f4e3e31` → `5b6c7b29` → `55f6d01c` → `816b0536` → `55770385` | 2026-09-19 | 依次经 R02/R03/WP01、C02/WP02、状态回填+WP03 追踪、WP03 复审关联修订；本轮经 WP03 回填与 WP04–WP07 追踪修订被 `ab2b8f21` 替代 |
| `planning/extraction-plan.md` | `aef0d7ab` → `d441c68b` | 2026-09-19 | 依次经 R02/R03、C02 修订为 `c1735877`（当前有效） |
| `specs/demo/wp01-baseline-and-evidence-scope.md` | `403e814c` → `515500c2` → `2c1a553e` → `c952847d` | 2026-09-19 | 依次经 WP01-R01/R02/R03、C02、状态回填、尾部状态同步（C03）修订为 `2a52e94e`（当前有效） |
| `specs/kernel/wp02-rule-configuration-and-data-variants.md` | `d322cf95` → `4352c450` → `d6ef14ae` → `272b0291` | 2026-09-19 | 依次经 WP02-R01～R06、F1/F2/C1、状态回填、尾部状态同步（C03）修订为 `82b47151`（当前有效） |
| `specs/kernel/wp02-settings-inventory-appendix.md` | `6fba2cdd` | 2026-09-19 附表首版 | 经 F1/F2 修订被 `f165b1cb` 替代（当前有效） |
| `specs/kernel/wp03-content-identity-and-schema.md` | `d61233f0` → `f7213e83` → `f1d8a763` → `7a9c85da` | 2026-09-19 | 首版经 WP03-R01～R05、复检四组剩余项、枚举存在条件收紧修订为 `7a9c85da`（闭合复审通过版本）；本轮经状态回填被 `de331460` 替代 |
| `analysis/inventory/wp02_settings_inventory.py` | `46f1ba84` | 2026-09-19 | 重构为共享模块后被 `dfa38c40` 替代（当前有效） |
| `analysis/inventory/wp02_build_appendix.py` | `898134d0` | 2026-09-19 | 重构为共享模块后被 `7c965c9d` 替代（当前有效） |

## 4. 2026-09-19 修订与交付摘要（按轮次）

**第一轮至第七轮**：联合 review 处理与 WP01 交付；WP01 复审处理与 WP02 首版；WP02 复审处理（R01～R06）；WP02 复检处理（F1/F2/C1）；WP02 闭合状态回填与 WP03 首版；WP03 复审处理（R01–R05）；WP03 复检处理（四组剩余项）。

**第八轮（WP03 v3 复检处理）**：遭遇枚举存在条件收紧；WP03 修订稿 v4（`7a9c85da`）。

**第九轮（WP03 闭合状态回填 + WP04–WP07 批次，本轮）**：

- **WP03 状态回填**：WP03 → Reviewed（内容身份、注册/查找/枚举、已述缺失值和状态变化、schema 结构及校验边界、固定规则与作者数据区分、字段责任目录及适用静态场景范围）；矩阵 F01-02/F02-01 同步为 Reviewed（WP03 子范围）＋Inventoried（字段语义）；被审哈希 `7a9c85da` 保留于历史，回填后新哈希 `de331460`。
- **WP04（PBS 生命周期）**：编译触发（调试前提、六种触发条件、新鲜度检查）、输入发现与 22 项编译调度、五类写回（.dat 删除与重建、PBS 改名改写、MapInfos 导入、地图/公共事件转换、动画映射）、失败与部分状态（编译前删除、异常再删除、非原子性、错误定位）、交界（WP08/WP73/WP75/WP15）。`e2bc7e6b`
- **WP05（通知/扩展与插件）**：通知原语（Event/NamedEvent/HandlerHash 族）、命名事件注册表（18 事件名 53 注册点/19 事件名 35 触发点）、菜单扩展（202 注册点，选项结构 name/order/condition/effect）、插件元数据与依赖（meta.txt、注册校验、依赖/冲突/循环、版本比较）、插件载入（调试/发布前提、编译、执行、版本警告、错误即退出）、与 WP07 共用诊断面。`a8412720`
- **WP06（时间/随机/计步/统计）**：四类时间来源（现实时间/运行时长/游戏时间惰性累加/帧更新）、现实时间规则族（时段 5/10/14/17/20 边界、日历、月相、日夜调色）、计步与约 60 项统计字段（$stats 九组、距离累加、保存值注册）、随机入口（rand 242 处无统一服务、显式种子仅地牢/彩票 2 类、录像随机序列回放）、保存/恢复交界与 U05 保持开放。`c18eae6a`
- **WP07（诊断/文件/HTTP）**：文件访问层（遍历/存在性/读写/资源解析/保存目录，读取失败归一 nil 不区分原因）、HTTP 包装（下载/提交，失败归一空结果、无重试、仅 http）、诊断面（异常格式化、errorlog.txt、debuglog.txt 仅 debug+INTERNAL、控制台着色输出、三层用户反馈）、失败层次对照（文件 nil / HTTP 空结果 / 编译位置报告 / 插件终止 / 未捕获异常 errorlog）。`0225f652`
- **跨包核对**：WP04 编译写回与 WP07 文件失败（异常路径共用 pbPrintException 诊断面，无重复机制）；WP05 插件错误与 WP07 诊断（同一 errorlog 面）；WP06 统计持久化与 WP09 交界（只登记保存值事实，不定义生命周期）；WP04 与 WP03 身份/重复/缺失规则（引用不重复）；WP05 与 WP04 启动顺序（插件早于编译检查，一致）；WP06 与 WP05 事件订阅（引用一致）；WP07 与 WP03 的 nil 返回≠缺失同例（一致）。未发现规则重复定义或冲突。
- **矩阵增量**：F02-02 → ReviewPending（WP04 范围）＋Inventoried（编辑器/转换全集）；F01-03、F01-04 → ReviewPending（WP05 机制范围）＋Inventoried/Provisional（语义/真实组合）；F01-05、F03-05 → ReviewPending（WP06 机制范围）＋Provisional/Inventoried（一致性/全集迁移）；F01-06、F01-07 → ReviewPending（WP07 范围）＋Inventoried/Provisional（业务失败/HTTPS 归档）。
- 四包状态均为 **ReviewPending**，统一送外部 review；未自行升级 Reviewed；未执行 WP08。
