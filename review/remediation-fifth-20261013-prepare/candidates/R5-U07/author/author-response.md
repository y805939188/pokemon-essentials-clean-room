# R5-U07 作者候选

7项全部提交规格候选；6项为 ADDRESSED_STATIC，GR5-M12-002 为 ADDRESSED_STATIC_WITH_INPUT_CONFLICT。这些是作者逐项对照，未自签独立复审、正式接受或CLOSED。

固定B5 `9366d9d17aaeac3b4414236468affa650fb3dd27`；R `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`（Maruno17/pokemon-essentials，只读）；任务冻结 `22fba7786b0090a1955ce6211315b0036cddfbcd` / tree `21f3484d167d8cab7a288e0204c72f275414d52e`；准备发布 `93524fe5cf396de2bd01f3c5c1e08ba4b874bc68`；原证据发布 `f49d870c6fd616ab6736754a218a4553b5acac7f` / tree `e5dc6aaf626885666e7d472865563f0c9bfbdf46`。模型请求gpt-6.1-sol/xhigh/default/禁Fast，实际回显UNVERIFIED；未审计额度。作者真实任务ID未由平台回显，标UNVERIFIED，不用预留槽或父线程ID冒充。

## 候选内容

| ID | 修订与验收载荷 | 作者状态 |
| --- | --- | --- |
| GR5-M12-001 | WP75§12.4安全可读Main发现、错误分层；U07-L01–03 | ADDRESSED_STATIC |
| GR5-M12-002 | WP75§8.2六族行门/整字段丢文、18参数回归；U07-C02、B20-C034 | ADDRESSED_STATIC_WITH_INPUT_CONFLICT |
| GR5-M12-003 | WP75§7.2两页门、§7.2b独立转移全部参数；U07-C03 | ADDRESSED_STATIC |
| GR5-M12-004 | WP75§5.2两布尔族累计启用及首页/再战；U07-C04 | ADDRESSED_STATIC |
| GR5-M12-101 | WP73-A新建类型/道具实际原文与已有训练家败词三层；U07-T01–03 | ADDRESSED_STATIC |
| GR5-M12-102 | WP73-A§4.3a REPEL四阶段、两份量/空串/SellPrice/消费门；U07-P01–02 | ADDRESSED_STATIC |
| GR5-M12-103 | WP72后置显式门、普通/在场写穿/场下简化消费；U07-F01–03 | ADDRESSED_STATIC |

`finding-responses.json`覆盖33条mandatory static criterion，逐条绑定目标、向量和理由；`static-vectors.json`列18旧输入、48六族行门对照、8布尔锁存和18形态字段对照，均DERIVED_VECTOR/NOT_EXECUTED。其余正常/失败/取消/部分提交向量在测试片段和规范表内。`regression-results.json`保留精确owner/scope，旧PASS不转签；`source-reading-log.json`区分全字节身份验证与实际语义读取范围。

唯一正文镜像为 `formal/deliverables/final-specification-set/demo-dx/wp75-project-conversion-and-authoring-tools.md`。WP72、WP73-A与测试目录由 `fragment-manifest.json`给出精确B5替换锚点、payload字节区间、所属ID、正确旧行为和依赖。`formal-diff.patch`是这四份拟整合字节相对B5的补丁，仅在scratch重建核对。作者未写工作树正式路径或公共registration；R5-I共享实写，非共享仅机械接入独立通过的精确字节。

## 精确剩余问题

SC-U07-001：冻结任务包称括号捕获体可跨行，固定源六模式使用无m选项的(.+)。候选按固定源写捕获体不跨LF，同时完整修复独立前后行命中并整字段丢失。Ruby官方文档的Options节与直接源字节支持此区分：[Regexp](https://docs.ruby-lang.org/en/3.1/Regexp.html)。只将这一前提交独立审者裁定，不改冻结合同、不以作者判断关闭问题。所需裁定详见scope-conflicts.json。

U01、U03、U06所需实际贡献尚未提供接受回执，全部整合门WAIT。WP21/WP62/WP29/WP24及门跟随正确主规则只读复用，未越界改消费者。GR4-M04-001/C01当前Summary残余仍由GR5-M04-002相关上游贡献承接；其余限定图像/动态读取控制没有因103扩成全ID通过。

R4历史隔离参考执行4与R5review隔离执行4分别保留；本update新增参考/模型/宿主/Demo行为执行均0，只有格式/哈希/重建TOOL_VALIDATION。缺完整地图/事件/Graphics/Audio和原生宿主等原限制不被静态参数补齐解除。optional/no-required/兼容政策均未纳入。

## 独立审者入口

固定合同入口：`review/remediation-fifth-20261013-prepare/contracts/R5-U07/reviewer-entry.md`（prepare发布commit读取）。先按candidate-manifest核候选全载荷，再读7项完整task-packet和固定R必要锚点；将SC-U07-001作为具名反向对照，不凭作者状态签PASS。此作者未启动本批审者。候选commit/tree由后继publication-evidence及父任务绑定；独立candidate通过后仍须等待依赖、R5-I实际整合、actual-reviewer入口及唯一登记。
