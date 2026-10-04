# B06 stage2 完整十项作者候选

本包完成 A034/A059/C103 的获准 B06 文字贡献，继承 A032/A033/A035/A036/A037/A038/C120 七项既有内容；完整十项等待新一轮独立 Ultra。作者检查不构成候选通过、实际整合通过、接受或 canonical 关闭。`whole_B06_ready=false`，公共登记仍交 A-REG 单写。

## 恢复身份与合并

父任务交付的串行接受为 `1fd612d47dcda164de61ab2d25a1cb5e0fbde085`；其中 [B03 恢复合同](https://github.com/y805939188/pokemon-essentials-clean-room/blob/1fd612d47dcda164de61ab2d25a1cb5e0fbde085/review/remediation/20261003-prepare/batches/B03/acceptance-stage-1/downstream-handshake.json) 的项目路径实际为 `review/remediation/20261003-prepare/batches/B03/acceptance-stage-1/downstream-handshake.json`。完整控制项、原三项/验收对象和全部身份已核，200 条声明整文件身份检查通过；根 AGENTS 已读，相关本地技能目录未见可读 SKILL.md。

实际 B03 `e24f2ac6f43642ea0e68bd9aa21fb2c313d6ebdf` / tree `d773aa6c96be4ca878350bd0a3ce6098ca71971b` 已获 [固定独立实际报告](https://github.com/y805939188/pokemon-essentials-clean-room/blob/dea9d118d7ed3b7ddb57b1c4e7bd40db8dd06497/review/remediation/20261003-prepare/batches/B03/integration-review-1/report.md) PASS_SCOPED，随后由父任务串行接受。B06 原七项候选 `b1b09be809822ffa8ab79684589d104ec783095a` / tree `a05352598a27430f5ee75bfcb59235333a5b4b5b` 已获 [第二轮固定报告](https://github.com/y805939188/pokemon-essentials-clean-room/blob/296a26070cf14b49a42c1c2767274fd7b4e5f7dc/review/remediation/20261003-prepare/batches/B06/review-stage-1-round-2/report.md) PASS_SCOPED，包括 N001/N002 返修。这些旧字节结论未迁移为本次完整十项通过。

在既有 batch-B06 分支从 `5059760ea678e3c21ce01a87a13317b5b6cc2e1d` 普通非 rebase 合并精确接受 SHA，得到恢复基线 `df65e346d85213742a2538588818a10f50b819e5` / tree `974dc9062cd991700c933ef27f1ad27775f3fcb8`，父提交依次为 5059760…、1fd612d…。无冲突，没有自动 ours/theirs 处理；合并边界八份 B06 正式文件与原候选逐字相等，十三份 B03 输入与已接受 actual 逐字相等。

完整合并差分含 129 条路径、44,157,390 字节，全部是指定已接受上游字节；每条 before/after 身份及完整重建命令/哈希见 [merge-and-dependency-impact.json](merge-and-dependency-impact.json)。未将接受方的公共登记变化当作本作者登记。原 25 条计划读输入中仅共享 engine 目录上游 blob 从 `f4ca72c…` 变为 `21950e9…`；其它计划上游输入不变。原总审 JSON/索引仍仅在固定 93e10ba… Git 对象读取，没有伪称它们存在于恢复树。

新冻结区分已接受上游、八份继承 B06 本地内容与两份外部固定总审输入，完整覆盖 25 读、5 写、3 原稿、13 个 B03 正式输入及 17 项新增只读上下文，见 [input-freeze.json](input-freeze.json)。原作者两包 32 件树内文件原字节保持；R1/R2 共 25 件独立证据保留各自固定提交。未重写历史 Max 收据、报告结论、读取勘误或哈希。

## 精确三项增量

相对恢复基线，作者正式增量精确为以下三路径，全部具名条款受合同约束：

| 相对路径 | A034 | A059 | C103 |
| --- | --- | --- | --- |
| `deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md` | §6.4 原雷达错误句及紧邻说明 | 独立新增 §5.4 逻辑选曲/引子表 | §4.1 火山灰 writer 行及紧邻三层说明 |
| `specs/creature-rpg/wp24-player-trainers-partners.md` | 仅同步上述 §6.4 | 仅新增同一 §5.4 | 仅同步上述 §4.1 |
| `deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md` | PT-35～40 | PT-41～63 | PT-64～69 |

净化 WP24 原 34 条导航原字节保留，仅追加本次 35 条导航；PT 标题扩展到 69。WP24 §5.1/5.2/5.3/6.1、伙伴注册/返回/部分失败及漫游/野生其它正确条款保持。其余五份本地整文件、WP26、WP66-B、WP37、WP61、WP06、WP15 和 B03 十三文件均未增写。精确条款差分记录见 [formal-edit-ledger.json](formal-edit-ledger.json)。

| ID（GIR-FD82-） | 源/原反例对应的作者静态结果 | 成对边界及未补证范围 |
| --- | --- | --- |
| A034 | 正常 11×11 全可摇夹具中有/无伙伴都先成功启动、使用数 +1、电量 50；伙伴在后续候选钩子清临时链，前段提交不撤销 | PT35/36 启动对照；PT35/37 后段对照；PT38 已骑车拒绝；PT39/40 成功新上车取消与已骑车早返回。无真实摇草/遭遇/声音观察，不保证其它候选保持链；B08 贡献待 |
| A059 | 逐入口独立下一战预置→候选→地图元数据→全局→固定默认；训练家数组最后非 nil 值覆盖，确实储存空文本覆盖后再回退；直接 FromType 保留空请求。引子已有备忘保留，无备忘时待播 Q/位置0 优先并取消计时，否则记当前曲/位置，仅位置查询失败取0 | 顺序、nil/空文本、元数据缺失、地图/全局默认、三预置独立、直接辅助与普通入口、备忘/待播/当前位置及查询失败均有明确静态对照。空文本仅有效作者夹具；只观察请求/交付播放前状态。实际播放/恢复/等待/默认 BGM 覆盖未补审；B04/B09/B17/B21 待 |
| C103 | 一次已到达的通用通知按层2→1→0处理首煤灰层；仅玩家持袋先请求灰量+1、钳位后按实际增量统计，再擦首层。NPC/无袋/9999仍擦而增量0；9998达到9999、统计+1 | PT64～69 给 NPC、无袋、上限、低于上限、多层/层优先及无煤灰对照。按通知计，不把普通移动许可或每个物理步概括为一次必然采集；有效实格/地形/访问前提与部分失败保持；B14/WP61待 |

完整原十项对象、current_qualifications、有效二审、扩展和批准验收逐项与固定 93e10ba…/41fffb5… 原对象相等，见 [finding-inputs.json](finding-inputs.json)。十项回应及来源/行哈希/反向对照见 [finding-responses.json](finding-responses.json)，新增 35 行原文见 [new-static-vectors.json](new-static-vectors.json)。合同、完整报告与条款人读限制见 [reading-and-limit-receipt.json](reading-and-limit-receipt.json)。它们都是人工静态预期，没有行为执行结果。

## 七项回归与文档核验

十五个旧已审条款片段及全部 25 行七项向量按原字节、次序和哈希保持；原目录所有旧行（含 PT22/23、PS11、AQ04、CI/HP）及其它非自有正文保持。完整旧目录可由新目录删除 PT35～69、还原 PT 标题后精确重建；不是只核被分配的25行。五份本地整文件、17个上游保护版本、8个仍保护的完整章节通过字节核验；只有合同明确释放的 WP24 §4.1/6.4 被改。

N001 的墙纸行边界、LF 和首匹配定义/对照由 WP25 整文件与25行守卫保留；N002 的 Trainer_LoadAndNew 读取范围继续为实际 1–124。新参考收据包含 15 个本轮人读文件/23跨度，另继承10份已纠正历史人读收据并重核17跨度，共40跨度先验界再哈希，未把阅读范围当分支覆盖。FromType 固定 Scripts 纯文本检索仍仅命中定义，未定位普通调用者；动态/插件调用不因此被排除。见 [source-reading-log.json](source-reading-log.json)。

两个展示请求曾超过文件 EOF：雷达 155–280（实际267）及 Game_Player 596–638（实际616）；写收据前的范围校验拒绝，随后按155–267、596–616重新读取和登记。无不存在行的哈希证明。文档工具再核两条合法范围、五条既有非法范围及这两条非法展示请求；七条反例都在哈希前拒绝、哈希观察函数调用0，共9条文档范围检查。参考/游戏向量执行数仍0。

作者核验脚本只读 Git/JSON/文字与范围元数据，仅写本后继验证结果；没有运行旧作者/独立复审脚本或参考程序。结果见 [static-validation.json](static-validation.json)，源码见 [verify-documents.py](verify-documents.py)。本次新35行 + 旧25行＝60行分配静态证据；PT全目录69行。作者文档检查通过不替代独立语义审查。

## 差分、未接受依赖与下一门

三份逐字差分均含文件身份/长度/哈希，见 [patch-identities.json](patch-identities.json)：[恢复基线→三路径增量](recovered-base-to-candidate.patch)、[旧已接受 ae230e7…→B06八路径完整十项](old-accepted-to-full-ten-formal.patch)、[新接受1fd612d…→B06八路径完整十项](accepted-B03-to-full-ten-formal.patch)。采用零上下文保存，周围上下文由固定 Git 重建；新增差分空白检查通过，不借用上游 literal 全上下文 patch 的空白结果。新候选 SHA/tree/八份正式文件、全包身份及后继交接关系由随后仅新增的 [candidate-manifest.json](candidate-manifest.json) 固定。

合同指定 B06 先、B04 等待；未发现本限定逻辑文字需要另一项未接受上游才能完成。B04→B06四个输入、反向WP24和共同A059仍具依赖，不能因写写交集为空宣布并行安全。任何后续播放/位置/恢复/等待/呈现新声明仍需其精确上游；B04 必须等 B06 实际接受后重冻结，B07仍需B06-I。A034/B08、C103/B14、C120/B16、A059/B04/B09/B17/B21贡献门全部保留。本作者未写 WP79 旧 NA 公共判断，给 A-REG 的建议仅指向本次具体合同与未完成贡献，见 [registrar-proposals.json](registrar-proposals.json)。

下一步由父任务独立 Ultra 重审完整十项，包括七项回归、N001/N002与变化的B03接口；候选 scoped PASS 后再实际整合、按实际新SHA复审及接受。恢复点见 [resume-checkpoint.json](resume-checkpoint.json)。本轮不整合 B06、不关闭 ID、不应用公共登记；原229项 OPEN/0 CLOSED 口径保持。

当前作者请求 **gpt-6.1-sol / xhigh / Standard(default)**，xhigh 为用户最新直接请求，不是 Max 不支持 fallback；实际配置 **UNVERIFIED**，未见可信平台回显。历史 Max 收据保持，新收据见 [execution-request-receipt.json](execution-request-receipt.json)，未改配置或派生代理。

参考独立 Git 固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，主项目外且 clean；参考未进项目 Git、未改 ignore、未推上游。未运行参考/Ruby/游戏/编译/转换/生成/反序列化/模拟器/求解器；行为向量执行0、运行观察0、已证demo链0。U01–U10/G01–G12/AX01–AX20、具名未知及真实素材/宿主/插件/事件可达性限制全部保持。
