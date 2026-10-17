# R1 世界与界面独立复核

固定候选：`5666b7b912e2fb79b5119283ee6a37401a7071db`。本分工结论为 **FAIL：WP编号碰撞的反向目录传播仍未修正**。世界/UI功能去向本身的返修成立：168个旧ID均获新的PASS判定，其中164个活跃、4个完整退役；8个追加ID成立，新活跃合计172。此结论只适用于本固定规划候选，不是R8最终整改、目标兼容或四类原型通过。

逐旧ID、新活跃ID、退役/元数据、九组原问题及真实阅读账本见 [world-ui-results.json](world-ui-results.json)。独立机械证据见 [world-ui-static-evidence.json](world-ui-static-evidence.json)；两个本分工静态脚本分别为 [world-ui-audit.py](world-ui-audit.py) 与 [world-ui-build-results.py](world-ui-build-results.py)。它们只处理Markdown/JSON/Git，语义理由为本次逐项人工裁定，不运行作者工具或业务代码。

## 身份与覆盖

审者为 `/root/r1_world_ui`，不是作者。父任务请求 `gpt-6.1-sol / ultra / default / Fast off`；actual model、thinking、service tier、speed、Fast和云任务UUID均为逐字段 **UNVERIFIED**。可见canonical task名不是云任务UUID，工具广告priority不是default执行资格。

已取得并核验新旧候选、旧独立报告 `a0352c7fba38391afc535525988245701d5ce202`、接受payload `908273093e1f6b27fc58249417675dd62d146224`、回执 `861f7a44a6f763c265a11761ab17a8ec3b55f304`、actual报告 `548d6bb9a21d0967680445c013e66d9d5661d2d6` 和固定B8/R8交付对象为commit。候选正式树仍为 `f292698cdd4a8e725525a9be6dc34b75faaf151e`；908当前正式树为 `6ae817df5b11eafdec671214b0d04e542ad364bc`。两者没有被混为同一工作区版本。本域28正文与3相关catalog在SOURCE、d62、5666、908的完整字节身份均相同；候选工作区字节也一致。

覆盖分母为engine-overworld 11正文、user-interface 17正文、3相关catalog和94个catalog章节。旧168行的原结果为117 PASS、31 FAIL、20待查；本轮逐旧ID恰一次active/retired，旧source对象全部不变，4个退役行去掉retirement后与旧完整行逐字段一致。8个新ID均为追加，全部功能有效区间无重叠。172个活跃行在本域可读视图各有且仅有一行，去向、当前908版本、待验证/未实现/未验收字段相符。

本次继承旧独立审查对28正文5,408行和3catalog 2,067行的有证据完整阅读信用；**没有声称这些正文全部重新阅读**。本次实际新增阅读为正文2,173行、三catalog219行，以及具名跨域主消费者的完整source单元。75个旧功能的完整源单元重新阅读；其余93行使用固定全文信用加本轮字段差分。新增职责/同根因混合单元已完整重读，尤其地牢§3/5/6、天气§4/5、钓鱼§4–7、电话§4、队伍/盒子/图鉴/PC/商店混合表、WP67-A/B、六份特殊玩法/数据附表。2173和219只计本分工31文档的新读区间，不把外域消费者读集混入该分母。

根AGENTS、根/R1 README、完整review-prompt、R8 DELIVERY/review-SKILL/中文handoff相关合同入口及旧本域逐行结果、原finding、完整catalog逐节结果已读。clean-document-revision明确不用于审计报告，未据此改写作者正文。全部输入只读；本分工只写新review下world-ui前缀文件，没有切分支、提交或运行业务。

## 九组裁定

| 原问题 | 新裁定 | 具体结论 |
| --- | --- | --- |
| WU-01 | PASS | 726/727/728/729分别补战前包装、Duel生命/准入、Slot入口和Mining公开入口；730完整承接61有序候选主表L9–75，706仅13铁形状；707成为来源元数据。全部五个原case逐范围核过。 |
| WU-02 | PASS | Duel矩阵/权重、Slot场景账/支付/转轮表、Mining摆放/削层/结算、Tile局面/合法动作/洗牌/不变量改归框架。MZ输入、动画、时间读回有具体职责；767/768分离时间门，父scope精确扣除，不逐字段过拆。全部14个原失败ID与同根因旧待查/PASS已复核。 |
| WU-03 | PASS | 677–682及684明确框架/Showdown/MZ生产消费；逃跑、战斗物品、成长和捕获分别连接四原型。完整退款残留/二退、持久/战斗招式两次提交、敌队移除/接收队列/满队记忆回填及特殊模式表均保留。 |
| WU-04 | PASS | 744拥有克隆历史、递增编号、正/负/零上限和PC门；691扣除139–147并保留呈现/浏览。记录内存更新与保存落盘分开。 |
| WU-05 | PASS | 684特殊模式/回放及690净化室均传递DEC-SPECIAL-AND-HOST-SCOPE，仍待用户范围决定；未把阶段待定冒充批准。 |
| WU-06 | PASS | 326明确WP09恢复门，384明确WP38/39/42实际消费者，659明确WP30学习/重学与统计；原wp_refs规划来源和实际direct_refs语义分开。三个原case均完整重读。 |
| WU-07 | PASS | 345/704/707/713完整退役为META-000018/030/031/032；保留旧身份和实际行为导航，不再计空壳实现功能。 |
| WORLD-CATALOG-F01 | **FAIL** | 本域29世界节和52 UI节的原active错误子体系均已移除，81个原case分别PASS。相同根因没有传播到反向Pokemon目录16节，仍列Fishing/Slot/Mining，含新增728/730。 |
| WORLD-CATALOG-F02 | PASS | 原四case分别补596、187/011/031/049/554/555/577、581、206；退款/自然之恩/Safari/重学主源与消费者均重读，原型可导航。 |

对新增744/767/768的目录消费又做了传播检查。LC、M11-003和M11-005虽未在catalog feature_refs直接重复子ID，但已列691/710/718，后者的excluded_child_refs准确指向新子行；目录→父→子的机器路径明确。它们的scope扣除和责任成立，因此没有因dependencies.feature_refs未重复列同一子而判FAIL。新子行完整出现在源域可读视图；父行额外展示子ID的可读性由root统一裁定。

52个UI目录节仍带retired_feature_refs `FR-000618`（Lottery旧依赖/批准/开放问题，替代615/616/617/725）。这缺少“旧错误关系已撤销”的说明，建议删除错误当前导航或明确只记录历史错误。但本分工没有仅凭历史ID存在，就认定活跃Lottery误关联仍未修。

## 剩余P3：WU-R1-N01

位置为 `planning/implementation-routing/r8-20261017/section-coverage.json` 的 `/sections/2277/feature_refs` 至 `/sections/2292/feature_refs`。源 `test-catalog/pokemon-rules-wp53-60-61-62-69-70.md` L3明确对应Safari、树果、被动效果、图鉴、Voltorb、Lottery正文；本分工独立重读L1–6和L199–242，核对全部16节映射，Pokemon分工负责该源其余全文。

这16节仍全部关联Fishing `FR-000380–387`、Slot `FR-000699/700/701/702/703/705`、Mining `FR-000706/708/709/710/711/712` 和新增 `FR-000728/730`。例如VF和LT具名向量是Voltorb/Lottery，无法给三转轮或Mining候选表提供验收设计。问题依据是明确不同子体系的来源关系，并非宽导航本身。

必要修正是按实际对应正文和具名后继限定反向目录消费者，保留真实跨域交界；与Pokemon分工报告合并为WORLD-CATALOG-F01同根传播，不另计重复根。不需要逐case新建功能ID。

## 状态与执行边界

172行全部为去向待验证、阶段待定/未批准、未实现、未验收，56行继续待整改后核对，116行为固定基线待后继差分核对；本域接受事件空。908对U02/U03的接受没有扩张为本域其它批次已校准、CLOSED或目标兼容通过。四类原型都未运行。

静态审查脚本实际exit 0，输出168旧行/172活跃/8新增/4退役/4元数据、31文档、94catalog节，身份/完整退役/源单元hash/视图关键字段/状态错误0、有效区间重叠0。没有运行Ruby、参考游戏、保存/回放、宿主、Showdown、业务向量或未来框架。全局schema、生成器、完整回执和保护验收由root整合；本文不替代这些检查。
