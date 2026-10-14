# R6-U13 repair-01：历史／载荷独立复审

**内容与证据包：PASS（有限静态范围）。配置资格：UNVERIFIED。** 被审对象为 `9971fe84896786645cdcda3ab45e5caf7785cabc`，tree `93ebe95d038954fd0dfb14fd07ac2f95a2485baf`。此结论只绑定该对象，修复旧候选 `00b45de642f07cee9953e42f04cce9c35d77346f` 的本文历史／工具缺口及SF30正确子例保留条件；旧FAIL及其冻结报告 `3ef4854ef43eac92fd1dc57350e4cf6aa160082b` 保持原样。不授实际整合验收、正式接受或CLOSED。

本次全文读取四脚本 `bind_history.py` 1–103、`verify_candidate.py` 1–190、`edit_candidate.py` 1–76/77–129、`repair-01/check_repair.py` 1–81；全文读取 repair-01 全部七份证据、author-report及tool-validation。对candidate-manifest、changed-spans、per-id-verification、historical-regression作完整结构差量核对，对作者reading-ledger完整新追加三记录逐字段审读／固定原件校验。原74导航／原资格投影无差量，因此复绑旧审读，不冒称这次重审全部历史报告。完整新范围、真实UTC、cwd、argv、运行时、stdout、stderr与独立Git读取退出在 `reading-ledger.jsonl` 和 `read-*.stdout.txt`/`read-*.stderr.txt`。

| 审核项 | 新固定载荷的结果与证据界限 |
| --- | --- |
| SF30正常控制恢复 | **PASS。** pokemon测试目录第40行新增独立d：两会话正常结束、有效持久值／保存／普通载入且无其它改写→保存→载入后非活动会话／模式统计持久；重载时钟仍未知且明确未执行。e恢复固定当前默认转换集合／注册者检索，排除插件／动态追加；只说无两会话专用格式迁移，不说全部存档或任意版本无迁移。d/e承接旧main SF30 b/c的正确有限含义，a/b/c菜单对照两列文字前缀保留。只增同一ID的子例，仍SF40。 |
| 原始ID唯一性 | **PASS。** verify:123–130先生成raw/ids，Counter识别重复并assert，最后才dict；145–165在建索引前计raw总行和唯一数，并保持原ID。本人独立原始行重数QC49/WS36/PA32/RC29/SF40均raw数＝唯一数、无重复。check_repair:21–40只选两个已读纯文档helper，旧FAIL缺d/e和注入第二个SF30都作为反向控制；这类helper执行是文档工具验证，不是原R源或玩法模型执行。本人未执行／导入任何作者脚本或helper。 |
| SF30证明强度 | **PASS（有界主张）。** verify:132–142/166–176明确查d/e输入、预期、时钟未知、未执行和不外推限定，并查菜单前缀；tool-validation:78–86与check_repair:77明示其只能证明文字存在／字节／输入身份，不能证明任意变更行语义或真实保存。repair report:7–11/20另作具名静态语义对照。关键词工具不单独完成语义验收；完整实际SF30和旧控制逐项比较支持本次有限保留结论。 |
| 因子常量分期 | **PASS。** verify:186–188及tool-validation:540–549将两次整数除法、与给定30的比较放在arithmetic，把两h24 factor30放在expected_constants_not_computed，并明确probability_factor_semantics_proved_by_this_tool=false。repair report:22撤回旧独立概率计算证明。它没有补造因子计算或新的模型执行。 |
| R5错误获取说明 | **PASS。** bind_history:60–76从固定f49d准确root-M07/root-JXN路径取完整原字节，核预期bytes/SHA/blob和100644 blob入口，才生成三个note。旧“fixed object无路径”字面已从生成逻辑删除；check_repair:62保留该字串仅作反向防回归断言。新三note撤回推断、保持初次失败原因UNKNOWN_NOT_RECONSTRUCTED，保留原blob恢复和旧FAIL引用。r5-path-recovery:81–97保留原exit128/观察stderr、UTC未捕获和原因未知，后继本地成功有新的UTC/exit，不倒补初期失败。 |
| 固定R5资格不变 | **PASS（复绑）。** 三个R5 qualified_scope及旧current_check完全相等；本人对两个准确f49d路径新核完整bytes/SHA/blob/mode及三个指针的投影。原14R3/R4、9R2、B12/B13、74导航与分母等无差量keys完全相等。仅新增有界SF30保留检查及降为BOUNDED...AWAITING_NON_AUTHOR_REVIEW的作者状态，无旧PASS转移、无新增required根因。 |
| 镜像及载荷 | **PASS。** 本人从Git对象逐项绑定全部30候选载荷，只有pokemon测试第40行变化、其它七镜像完整身份相等；该文件其余行与全部BP/FP/PD/VF/LT后缀相等。manifest8项身份匹配，37 changed spans精确重建；per-id仅S001修复注释／pending复审状态变化，未改七组原范围。作者原79条账本字节前缀不变，追加三条fixedR Conversion1–223、SaveConversions1–210/211–420的mode/blob、全文／分段bytes/SHA均吻合。 |

作者check_repair:64–68的八份review_inputs身份可核，但full_text_presented_and_read=true为直接写入的作者阅读声明，不能由脚本读bytes自动证明界面完整呈现或实际语义理解；本文没有把它计为本人新阅读或独立工具证明。本人的新脚本／修复证据全文与分段回执另列。

转换e的证据按层分开：本人完整审读新 conversion-controls49行及固定注册查询记录，核三条新源读取账本身份；同固定R两转换单元的既有完整语义审读由原非作者 recording_save 在3ef冻结报告具名保存，该审者本次确认不访问两模式会话，14默认注册范围未变。此为明确旧同源读集复绑及新SF30范围审查，不把搜索无匹配、hash或peer receipt称作本人新源全文／源执行。

出版载荷分期没有自哈希缺口：delta-manifest列semantic core `77dc1102feb99e1a5cfdcf1933b143e9228bbfbb` 的16项变化，排除自身并由外部Git绑定；remote-readback完整清单为该core的29载荷，全部与当前9971同路径字节一致。9971相对77dc仅增加remote-readback本身，故最终30载荷须由父审外部新回读；root已另保存 `repair-01/candidate-remote-readback.json` 的9971全部30载荷／1,002,864字节远端完整核验。本报告本地30身份核验与父审远端核验分列，不以旧core回执冒充9971自身出版回执。

独立验证为本人编写的 `audit_repair.py`，只作Git静态读取、AST检查、JSON／文本／hash比较。23项检查全部通过，见 `independent-validation.json`。首轮本人误将作者账本的git_entry当作独立git_blob字段，KeyError导致独立工具exit1；原程序、stderr及UTC回执保留为 `audit_repair-attempt-01.py`、`audit.stderr.txt`、`audit-command-receipt.json`。第二轮按真实bytes/SHA与git_entry分别核查，独立exit0见 `audit-attempt-02-command-receipt.json`。这个文档工具错误不是参考缺陷，成功重跑没有抹除失败。

只写本repair-01/history-payload目录；无新agent／辅助、无checkout／分支切换／提交、无作者脚本或原定义执行、无CLI模型／认证检查、无宿主／serializer／真实保存。请求gpt-6.1-sol/ultra/default/普速仍不等实际回显，model/effort/tier/speed/UUID全UNVERIFIED。内容PASS与配置要求满足是两件不同状态。

本范围没有剩余候选修订要求。后继仍须唯一整合者接收WP66-A正读取人数限定／焦点／最终判断接点，绑定实际整合版本的共享全文与跨批独立复验，之后才能正式接受或关闭。新候选内容PASS不改变这些pending，也不改第五92 CLOSED或其资格分母。
