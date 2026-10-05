# R-B04：B09 candidate-2 独立受影响复审

RUN_ID：`20261003-prepare`。结论：**PASS_SCOPED**。在下述精确候选及限定接口范围内，未发现新增阻断问题或新根因。该结论是静态文档复审；本轮未执行任何行为向量、参考程序或游戏，运行观察与已证明 Demo 链均为 **0**。

本轮由独立 R-B04 角色承担，作者与复审角色不同，未派生子任务。请求配置为 `gpt-6.1-sol / Ultra / inherited Standard(default)`；无可信实际配置回显，保留 **UNVERIFIED**。沿用已接受 Plan A，不增加配置审批门，不探测配置、鉴权或额度。

## 精确版本及报告身份

| 角色 | 完整 commit | tree / 用途 |
| --- | --- | --- |
| 被审完整候选 C | `18873059e56314fcd48f6081d5a65a79301a52f6` | `bf79e3a86623e05d7f3d994194b67cc4e2dd4fea` |
| C 的 payload 父提交 | `ab81adc17a0ee50f21032c58036b7b56b28da51b` | `b8c33f2aa972e8d43bcbe3bba7a47928f6afb028` |
| 历史 candidate-1 | `8ff72341b5b91736970b5bfa5dc1b88137e618a5` | 仅用于历史与增量核对 |
| 已接受前序 B | `407536adb682a04161d3e9c82f153a62b1becd97` | `aeccdd10ac56344c3faf5b7c66300c8e5ab258d3` |
| 独立准备的参考 S | `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` | `7589c800b61ba13a13040ed0d686979b80a84fd0` |
| 原始独立裁决 G | `93e10babe0b9c9ef8b3f5277754541b447beeeb4` | GIR findings 的有效限定与裁决 |
| 批计划 P | `41fffb540c6483f5296ea0d33b789b75180d27ed` | B04/B09 计划、验收及依赖控制 |

报告仅新增本目录，分支为 `remediation/20261003-prepare/review-B09-affected-B04-1`。报告提交必须是父提交精确等于 C 的普通提交。包含本报告的完整报告 SHA 由外部最终交接及远端完整 SHA 回读绑定；提交内文件不嵌入自身提交 SHA。被审 C、payload 和报告提交分别记录，不互相替代。详见 [handoff.json](handoff.json)。

冻结依据是 B 中 B08 接受后 `B09-downstream-contract.json`，其 blob 为 `b6f42254c2bf398340ed8958428d3c6709640aea`，SHA-256 为 `7ba7a21d3acd096ae410b4834963028c86a7cc915665d7759afc87f0d22116c8`。原 62 项读取加 8 项授权补充共 70 项输入均核身份。五份原稿同步授权和 WP20 两路径、四条范围修订仅授权范围；独立正确性门仍需完成。

## 复审范围及证据方法

复审 WP39/WP40 调用、数据与条件变化对已接受 WP15–17 资源、音频、视觉过渡、通用消息及输入合同的影响，并明确纳入 WP41 SW09 询问触发、WP42 成长及学招呈现与自动居中布局、WP38 捕获命名及接收菜单、WP20 精确终局接收者修订的公共接口影响。本轮未承担完整 B09 主责正确性、整包 B04 重演或实际整合验收。

B→C 完整差异为 **87 路径：14 修改、73 新增**，无删除或重命名；14 规范路径含 8 最终正文/目录及 6 原稿，73 新增均在 B09 证据目录。完整 14 规范差异已读取，WP39 当前 1–325 行与 WP40 当前 1–314 行已完整读取。其余新增历史、报告和验证器大块按身份及结构核对；未声称逐字语义复审全部证据内容，未运行作者或历史验证器。

本容器独立准备 Maruno17 参考 S，验证真实 commit、tree、detached 与清洁状态，之后仅只读。自行编号读取参考 **26 文件、57 次范围、2441 个去重行号**；项目正文/目录 **12 文件、24 次范围、1341 个去重行号**。先读取固定参考、反例与反向对照、完整规范差异、修订后正文和依赖，再冻结 [first-judgment.json](first-judgment.json)，之后对照作者详细自检。请求、范围和交接元数据此前已读，故不声称盲审。

可追溯材料：

- [instructions-and-inputs.json](instructions-and-inputs.json)：AGENTS、固定计划、接受合同和历史回执身份。
- [scope-and-impact.json](scope-and-impact.json)：WP39/WP40 的 28 条完整前后文本、5 组保持的 owner 条款及新增受影响接口。复制的冻结身份中 `commit: null` 由本报告明确绑定当前 C，实际 blob/哈希另经独立核对。
- [source-reading-log.json](source-reading-log.json)、[source-searches.json](source-searches.json)、[project-reading-log.json](project-reading-log.json)：自身读取范围和文本检索位置；未复刻参考源码。
- [all14-normative.diff](all14-normative.diff)、[diff-manifest.json](diff-manifest.json)：全部规范差异及三组无路径过滤、无外部 diff/textconv 的完整 Git 差异压缩件与原始字节哈希。压缩仅用于报告保存。
- [all87-path-identities.json](all87-path-identities.json)、[B04-preserved-current-identities.json](B04-preserved-current-identities.json)：穷尽路径分区及 13 个当前 B04 正式文件 B→C 字节保持。历史 B04 接受后经 B07/B08 接受的变更另列，未把历史 9e2dadfa 全部文件误称为与 B 相同。
- [control-bindings.json](control-bindings.json)：20 贡献、13 主责的有效资格、裁决、最低验收与复审关系。完整原始对象及计划验收对象分别核身份；扩展投影与完整原始扩展对象区分。

## 静态语义核对结果

以下 15 组为本轮独立静态设计，均**未执行**。每组的完整前提、顺序预期、相邻反向对照及精确 S/C 行号见 [independent-static-designs.json](independent-static-designs.json)。表中的“支持”限于本轮接口范围及显式前提。

| 组 | 核对结果及验收边界 |
| --- | --- |
| 01 六入口音频选择 | 支持各入口独立优先序；训练家后项非 nil 覆盖，储存空文本与 nil 分开，直接类型辅助的空请求单独保留。未证明真实发声。 |
| 02 Intro 记忆 | 支持已有备忘保持、待播 Q 取消计时并记位置 0、无待播时记当前位置的顺序；仅位置查询失败回落 0。空 Intro 不改这些状态，后段失败无统一回滚保证。 |
| 03 普通开战过渡 | 支持音乐请求交 WP16；训练家 1/3 过渡类别在确保参与者及缩减之前取得，不能从后来布局反推。skip/handled override 与正常消费者分开；正常返回清理不等于异常 ensure。 |
| 04 捕获呈现 | 支持野生捕获 ME 与 3.5 秒目标等待；训练家抢夺不走该野生消费者。等待目标、实际墙钟、音乐发声分开。 |
| 05 无可战斗 NPC | 支持非空全倒队伍先到 invalid-owner，未到场景开战、派出或 has-no-able；外层音乐/过渡可能已发生，无回滚承诺。空队伍及合法活成员为不同对照。 |
| 06 招式拒绝消息 | 支持回复封锁在扣 PP 前拒绝、历史字段清理及普通/特殊调用差异。战斗忙态快推与 WP17 通用消息 resume 分开。 |
| 07 Direct5 空效果 | 合法物品在默认资格真时可登记、扣库存并显示使用消息，但空效果不会据此成为成功效果或自动退款。类型 1/3 的效果存在门为反向对照。 |
| 08 NearAlly | 支持明示 3v3 布局保持时初选远活盟友、文字 nil、按钮未选中、USE 仍登记及执行拒远的错配；近活盟友及无活非己成员分别核对。现有 GIR-FD82-005 的 B17 贡献仍待该 owner 验收。 |
| 09 SW09 询问 | 支持完整内部/训练家/玩家单席/switchStyle/存活与后备等门，确认后还须合法替补选择；仅关闭 switchStyle 无询问，对方仍补位。 |
| 10 成长提示及音乐 | 支持野生胜利音乐检查先于经验开关/内部早退。ExpAll 总提示先于首名合格非参战接收者的收益计算，不要求其实际收益大于 0；空参与记录更早跳过。 |
| 11 学招交接 | 支持直接单个体 4 旧招+1 新招的摘要入口及取消只放弃当前招；先前成长提交保留。未批准专业摘要 UI 全流程。 |
| 12 自动居中 | 支持先收全计划再执行：指定 3v3 结果 2/3、3v2 结果 2/1；成功才发移动消息，不套手动 Shift 代价。该布局变化是以后 NearAlly 用例须重冻的条件。 |
| 13 捕获/WP20 接收者 | 支持身份及终局数据变化保持公共命名、菜单、消息参数与提交边界；实际持物映射完整正确性留给 full R-B09、B05/B07 对应门。 |
| 14 C071–73 | 当前 WP17 正文、原稿及目录字节保持；普通捕获仍 min0/固定正上限10/初空。无符号负数、有符号幅值、导航/ACTION 仅定位 OK、非正上限两模式限制继续保留。未将专业目标 UI 套用通用命名规则。 |
| 15 架构净化及兼容 | 支持去固定容器、槽数和创建组织仍保留必要身份、共享副作用、提交与呈现交接；未新增富文本、数字输入或音频参数、全局缺资源安全保证。 |

本轮新增缺陷 **0**、新增根因 **0**、范围阻断 **0**。已有 A059、005、B013 的来源关系记录于 [findings.json](findings.json)；局部接口核对通过不关闭这些根因或批准其他 owner 的完整贡献。

## 作者自检比较及报告核验

第一独立判断冻结时已有 821 项自身身份/文本断言；后续扩大证据核验后为 **945/945**。这些是 Git、JSON、文本、范围与哈希审计，不能计作行为测试执行。自身 [verify_candidate_identity.py](verify_candidate_identity.py) 是本轮审计脚本保存件；当次结果与完整绑定见 [identity-audit.json](identity-audit.json)。

作者自检记录 321 项成功，状态明确为 `PASS_AMENDED_DOCUMENT_SCOPE_AND_IDENTITY_SELF_CHECK_ONLY`。本轮在冻结后解析和比较这些记录，未运行作者验证器，结论未变化。独立核实最终正文、授权范围、目录保护、限定与历史身份；作者过去分支、lease、事前写入时间仅保留为其自述。局部 ledger 的后 CP20 锚点来自此前暂存修订，不能当作直接 B 锚点或完整补丁；完整 Git 差异控制最终文本。详见 [author-check-comparison.json](author-check-comparison.json)。

[verify_report.py](verify_report.py) 只核报告身份、引用、静态状态及文件封套，不执行参考行为或静态向量。[report-file-manifest.json](report-file-manifest.json) 绑定报告内容文件；自身清单和验证结果由普通报告提交的 Git tree 绑定，避免哈希自引用。[report-validation-results.json](report-validation-results.json) 保存本轮报告核验结果。

## 保留限制与后续门

[model-and-limits.json](model-and-limits.json) 完整保留 U01–10、G01–12、AX01–20 及具名未读/配置限制。八份 cup-list、pokemon_metrics、素材、字体、soundfont、二进制、序列化数据、mkxp/宿主配置、备份/生成、插件动态路径、地图事件与 Demo 均不由本轮静态读取变成已证明。有效数据、对象、资源与宿主是显式条件。参考游戏、编译、转换、生成、反序列化、参考行为模拟器、历史/作者验证器、行为向量执行均为 0。

仍须 full R-B09、独立受影响 B05/B07/B08 的同候选回执及后续精确 actual 复审。本报告未批准实际整合、公共登记或 ID 关闭；canonical 仍 229 OPEN / 0 CLOSED。B16 的 A048/C003/D023、B17 专业目标/捕获等待/居中 UI 等现有分配继续保留。

B04→B07 历史串行要求及以后 WP28/WP30 改动再核 B04 的门不变。B09→B14 正式串行保留：接受 B09-C 后才可冻结 B14 全 72 读取/6 写入并评估变更；后续 WP59/WP60/WP61、共享目录或调用/数据/条件变化须重新冻结受影响候选与 actual。完整清单见 [retained-obligations.json](retained-obligations.json)。

报告完成后返回父任务，等待其收齐相应回执与执行后续门。
