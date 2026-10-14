# R6-H / history-r4-r5 独立资格复核

本子任务完成 R4/R5 指定历史资格、当前有限后补及排除口径的审查，未提出新 finding。结论须由 root 裁决。本报告不授予旧游戏域新的全域 PASS，不代替 root 的 92 状态选择全表审计、六载荷发布审计或资源实审。

仅写入本目录。未切换、提交、push、启动 update、执行未知脚本、访问外部服务、使用真实存档或修改参考/正式/规划/旧报告。先全文阅读工作区 AGENTS.md；遵守只读参考、架构中立和规格分析限制。请求 gpt-6.1-sol / ultra / default / 普速 / 禁 Fast；实际 model、effort、tier、speed、UUID 均 UNVERIFIED，未查询额度认证。

## 固定证据与阅读方式

- main：`8ea169fbd0f33f378b5d732fd6bea59e854e04a6`。
- 第五历史入口：`f49d870c6fd616ab6736754a218a4553b5acac7f`；不要求其报告在 main 工作树出现。
- R：`8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，从参考子仓库 `git show` 读取。
- 由固定 main 的 report-index/接受登记绑定的 U08 actual 独立报告：`debf59f3c5370df253706969fd4dd1c103300bf2`。已全文新读其 `historical-review.md`、`regression-results.json` 和 `boundary-results.json`。

实际读取区间在 [reading-ledger.jsonl](reading-ledger.jsonl)。初次超长输出出现截断，未计为全文；R4 投影的截断区间及政策尾段已补读，activation/report-index 仅登记本子任务实际使用的区间，完整激活全表属于 root 分工。第一次 R 对象在错误仓库查询失败，随后改为只读参考子仓库查询，不将失败视为缺材料。

R5 的 14 条隔离记录通过两个互补、无损投影阅读全部字段，重新组合与固定对象逐记录完全相等。R4 的 17 条原 scope、排除、未知、owner 和全部 76 条有限标准进行了新语义资格阅读；重复生成的 `evidence` / `fresh_global_review_join` 地址树全结构解析，其旧游戏行为结果叶子没有获得本轮语义 PASS。该结构身份处置不扩大游戏语义分母，也不是用自动解析冒称重读了旧源。

三份正式共同入口已整篇读取：README 1–167、scope-statement 1–153、test-catalog/README 1–125。它们内嵌的 OPEN/WAIT 与执行 0 层有生成时点身份，不能重开当前已激活状态。

## R4：原 17/76、B5 16/75与有限 Summary 后补

固定 main `registration/R4-U06/findings-and-criteria.json` 仍有 17 原控制/76 条标准；全部 ID 顺序与第五历史 `regression-fourth-17.json` 相同。后者独立核算得到 16 supported 控制、75 supported 标准，唯一 partial 是 `GR4-M04-001/C01`。这不是 17 变 16 的新总分母，也不是更改原 R4 CLOSED。

所有 17 条的完整原 record 哈希、owner tuple、`historical_identity_scope_reuse` scope 哈希在当前 U08 历史输入中精确匹配。限定范围、异常输入、静态/运行前提及排除均保留，见 [forward-matrix.json](forward-matrix.json) 的 `R4_qualification_units`。

Summary 后补资格只接收原 C01 的消费者残留。固定 main U07 接受登记 692–1049 行明确：C01 获当前 Summary 有限静态支持；C02–C05 保留相应原有限范围；`whole_legacy_ID_PASS=false`、`old_verdict_transfer=false`、旧 CLOSED 不变。U08 actual `regression-results.json` 266–325 行再次限定 `PASS_EXACT_SUMMARY_RESIDUE_ONLY`，没有为整旧 ID 重新签名。

本轮新读必要源链：Summary 117–134 → 个体精灵请求 49–55 → 资源入口 92–108 → 普通形态读取/提交 147–166 → FURFROU 422–432；补读重算 1099–1127 与图鉴登记 195–218。有效非蛋 FURFROU 存储 1、无强制值、非战斗/储存、首次相关读取在整数 t+432001 时，提交 0 与清时间等已完成前缀先于资源匹配；恰 t+432000 不回退，强制 0 仅返回 0。现正式 WP18 154–156、WP21 179–196、WP66-A 225、R4-IF01–06 及 R5U03-M04-002-01/02/07 明确承接这些条件。资源失败不撤销已经完成的形态提交；未签像素、全数值改变、永久空缓存、真实场景或存档成功。

## R5：独立的 7/7/6/13

| 口径 | 精确身份 | 当前处置 |
| --- | --- | --- |
| optional 7 | BIN-001、M01-007、M09-002、M12-006、M12-104、M12-202、M12-203（均 GR5 前缀） | 原范围扩充/辅助材料/非默认入口/历史工具资格保留，不能自动升 mandatory |
| no-required 7 | M01-019、M01-020、M04-003、M05-005、M06-001、M12-005、M12-007（均 GR5 前缀） | 原重复归并或已正确具体合同保留，不新增七项关闭 |
| policy 6 | BAG-04、UTIL-03、UTIL-05、UTIL-11、UTIL-12、UTIL-13 | 兼容输入域选择，事实/政策分开，不算 unresolved fact finding |
| limits 13 | L01–L13 | 材料/宿主/库/资源/外部状态边界；不算游戏功能，不凭旧 PASS 闭合 |

fixed main 的 `quarantined-scope.json` 全 14 记录与第五发布完整记录相同；其中 policy 完整对象亦相同。limits 与第五发布字节相同，13 个 ID 唯一；actual boundary 文件的 7/7/6/13 ID 集合逐项一致。M11-005 的四个可选方面没有被增加为四个 canonical ID。

no-required 中 M01-019→M05-006、M01-020→JXN-001、M04-003→M08-001、M05-005→扩充后的 M12-101 是精确主发现归并；M05-005 的已有训练家败词消费者保留在主发现内，不能按前两项重复把第三项丢掉。M06-001 依据同条明确单 Ditto 例外与相邻限定测试无需必修；M12-005/007 依具体训练家门和公共事件管线无需必修。历史较早的 pending 摘要不覆盖最后裁决。

## SC-U07-001：四种文本位置分开

新读固定 R 转换器 975–1133 及必要 caller 1499–1503。六族门在 1000、1016、1034、1053、1075、1100 行均为普通点字符捕获、行首/行尾边界，无跨 LF 选项；每个成功分支直接替换整脚本字段。

| 输入条件 | 有限静态结果 |
| --- | --- |
| 括号体内含 LF，且无其它合法独立调用行 | 该门不命中 |
| 调用外围只有可接受空白，包括 LF | 空白门可接受，须与括号体内 LF 分开 |
| 前/后独立普通行包围合法整调用行 | 可命中该行；整字段替换，外围普通行丢失 |
| 同一行无关前缀/后缀、空括号、错误大小写 | 本行不满足门；字段另有合法行时仍按六族优先次序处理 |

普通对照为一行合法、非空、大小写准确的调用。最小反向体内 LF 与独立完整行不是同一输入。未运行转换器、独立模型或宿主；源事实按 SOURCE_STATIC，例子按 DERIVED_VECTOR。

erratum 全 225 行新读，八个错误字段定位和作者 `/findings/1/failure_cancel_partial_submit` 明确排除。32 普通标准+1 准确前提纠正标准、U07 原 33 与 R5 原 92 分母不变，原错误子主张没有 PASS。固定 main U07 接受登记 626–684、WP75 §8.2 的 221 行及 U07-C02 的 306 行一致。erratum 发出时的 WAIT 依赖是历史生成状态，当前精确接受与 activation 不继承该 WAIT。

## 当前阶段与证据边界

main activation 173–181 选择已审 `13fddb0…` 的 `records/proposed_only_after_valid_activation`；833–871 的当前计数为 required 92、51 P2/41 P3、CLOSED 92、OPEN 0，并保留 optional/noRequired/policy/limits、Summary 后补、SC 错误排除及历史 FAIL/MISMATCH。report-index 1–20 明示旧 OPEN/WAIT 是生成快照。92 逐状态/逐 scope 的完整激活反证由 root 主任务负责，本子审没有将计数字段核算冒称已重新语义审查 92 游戏条款。

U08 actual 历史审查已逐项保存 candidate01 G03/G09 FAIL、旧 U03 FAIL/operation49 定向修订、两份整 advisory SHA MISMATCH；这些在边界文件及 activation 859–864 均未反写。R4 历史隔离执行 4、R5 原 review 隔离执行 4 与 update 新行为执行 0 分期保持。此子任务新隔离参考/独立模型/host/Demo 均 0；14 项工具检查全部通过，只属 TOOL_VALIDATION。

当前 17/76、16/75、7/7/6/13 资格语义未读项为 0。旧生成地址树作为历史结构材料已全解析；原游戏源的全域复审由各领域主审完成，不在这里自签。未发现需恢复的不可得材料或待定资格阻塞；未将任何真正可读而未读的游戏源范围改写成宿主 limit 以闭合全局任务。

交付 [findings.json](findings.json)（无新提案）、[task-status.json](task-status.json)、[semantic-review.json](semantic-review.json)、[forward-matrix.json](forward-matrix.json)、[reverse-matrix.json](reverse-matrix.json) 与 [qualification-tool-validation.json](qualification-tool-validation.json)。所有结论保持有限范围，最终分类由 root 裁决。
