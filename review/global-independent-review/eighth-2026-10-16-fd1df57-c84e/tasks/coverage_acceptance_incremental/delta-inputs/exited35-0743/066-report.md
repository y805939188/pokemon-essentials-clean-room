# 第八轮库存与分母协调结果

本任务完成机械身份库存、四份 planning 正文全文阅读、适用旧 review manifest 的完整类型/身份处置、87 WP 与 113 Feature 路由和声明依赖清单。它不代表参考源、正式条款、真实接口或整个第八轮审查已完成。`UPDATE_NOT_STARTED`。

冻结 B8 为 `fd1df570cad987dc3852a3b958f03916e317f7fe`，workspace tree 为 `751dfde81048c81390f89a65ca1d1a565ba8e1ca`，formal tree 为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`。只读 R 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / `7589c800b61ba13a13040ed0d686979b80a84fd0`。逐文件身份见 [reference-inventory.json](reference-inventory.json) 和 [b8-scoped-inventory.json](b8-scoped-inventory.json)。均包括 path、Git mode、实际 mode、bytes、SHA256、blob、commit/tree、类型与用途。

| 分母 | 实测 |
| --- | ---: |
| R tracked / 现存 | 432 / 432 |
| R 额外现存 / tracked 缺失 / blob 差异 | 0 / 0 / 0 |
| R 字节总量 | 44,906,485 |
| 正式文件 / 字节 | 131 / 4,364,108 |
| planning / audit 文件 | 5 / 1 |
| 当前 delivery 导航文件 | 14 |
| R7 / R6 整改根候选载荷 | 512 / 314 |
| 根当前导航 | 3 |
| B8 上述 scoped 唯一路径 | 980 |
| 三份导航中机械链接候选 / distinct 可解析 B8 路径 | 612 / 314 |
| 独立复核的历史恢复版本载荷 | 24 |

云端 R 仅现存 432，合同所述本机准备 434 不可沿用。当前无 tracked 缺失；未获得当时两个额外文件的准确身份，不能推造它们的名字或内容。980 文件是保守候选库存；512/314 全根包含旧候选和行政材料，不能直接称作当前有效语义分母。导航可达 314 均包含于这 980 路径。history_current 对精确当前性与不可变历史输入负责，库存保留其 24 个恢复版本的全部身份并逐字节重新核验，24/24 匹配。

四份 planning 文档均完整实读：module-map 111 行、feature-matrix 596 行、coverage 287 行、extraction-plan 241 行。18 领域、113 原 Feature、87 可执行计划行均有导航映射；84 内容行包含 WP01，WP78/79/80 是三个后续审查阶段。WP47、WP52、WP66、WP67、WP73 的族简称不额外计数。十个多包 Feature 保留其完整承接关系，113 Feature 没有缺少计划 WP 的行。见 [wp-map.json](wp-map.json)、[feature-wp-formal-map.json](feature-wp-formal-map.json)。

主任务 `delegation/scope-freeze.v1.json` 及 14 组 readsets 是唯一路由。独立交叉核确认 R432、formal131 均恰有一个 primary，漏项、额外路径、重复分配均为 0。见 [routing-authoritative-check.json](routing-authoritative-check.json)。本任务旧目录分片建议已显式标为 superseded；当前 formal-shard 文件引用该权威入口。

特别需要跨域接收：WP60 树果/钓鱼、WP68 Triple Triad/Duel、WP69 Voltorb/Slot、WP70 Lottery/Mining 分处多个领域；world_activities 的五份 formal 对应源在 world_full 与 ui_full。其共享 pokemon 测试目录 primary 在 combat_review，WP62 对应条款还需 creature_review 接收。目录主读不能替代其他领域对其实际子断言和消费者的接收。kernel 的 schema/compile 阅读也不替代三组 PBS 的逐记录阅读。

旧 review manifest 为 1,420,152 bytes / 4,127 行，是截至 WP80 第171轮并带 B21 后继勘误的历史登记。原文末尾明确旧 hash/status 保留制作时点、不代表当前新字节。全部行已连续分层处置：230 行实际全文阅读，3,897 行仅完整类型/身份库存处置。现行用途/资格段 1–4、1913–1918、2801–2827、4115–4127 均已实读，包含旧版无全文/操作日志的证据限制与18处身份勘误；整个文件没有被标为 FULL_READ。旧行为摘要、案例和 PASS 用作历史导航，B8 正式行为及当前 R7/R6 状态须由准确后继来源审读接收。见 [manifest-purpose-disposition.json](manifest-purpose-disposition.json) 的逐行 offset/bytes/SHA256/path/hash 键及理由、[reading-ledger.json](reading-ledger.json) 的真实区间。

声明的完成知识依赖为 395 条，另有 9 横切义务和 3 局部检查点，见 [declared-interface-denominator.json](declared-interface-denominator.json)。它们不是运行接口全集。正向 432 个文件底账与反向 131 个文件底账已保留每文件未接收状态；实际语义 unit、fact、复合条款拆分、premise 和真实接口分母仍为 `UNFROZEN`，等待具名领域审读与消费者接收，不能用 87/113/395 或历史 PASS 替代。

协助历史审者完整读取 R6 limits、optional-facets、historical-qualification、classification-counts 四个小载荷；B8 与 9aa 均同字节，链接一次全文阅读而非虚增独立审者。L01–L14 的历史已审、未知、恢复条件与逐字段当前处置完整保留于 [r6-small-payload-reading.json](r6-small-payload-reading.json)。这些是历史资格恢复，不授 R8 源或运行批准。九项 R6 retained 载荷的前七项字节相同，planning/feature-matrix 与 audit/source-traceability 有 B8 后继差异，身份分别保留。

本任务没有提出新的正式规格 finding，也没有据此作全局 `NO_REQUIRED_UPDATE` 裁决。当前审查依赖仍包括有效补充当前性接收、所有领域逐事实/条款展开及实际接口与独立反证接收。所有可审材料的真实未读仍应由各实际审者台账反映。

请求配置为 `gpt-6.1-sol / ultra / default / Fast off`；实际 model、effort、tier、speed 均 `UNVERIFIED`。平台只回显逻辑名称 `/root/inventory_denominator` 和 running 状态，未提供 opaque agent/session ID。Library 合同 1–241 行已完整读取并保存两份原始结构回执；仅 metadata 报告 36,653 bytes，没有原始本地字节，SHA256 没有伪称验证。命令工具只作库存/文档验证，本任务新行为执行 0。读集、开始/更新/结束 UTC 与限制见 [progress.json](progress.json)。
