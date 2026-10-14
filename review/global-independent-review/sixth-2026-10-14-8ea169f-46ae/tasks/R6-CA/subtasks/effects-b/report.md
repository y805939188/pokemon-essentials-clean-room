# R6-CA / effects-b independent review

本子域全文静态与双向语义审查完成；有 2 个独立待反证提案，尚无 root 最终分类。没有修改正式规格或参考文件，没有启动 update。

## 输入与边界

- Workspace main `8ea169fbd0f33f378b5d732fd6bea59e854e04a6` / tree `6ab3429170d2762607fbc2237014c3a160449fa1`。
- Formal set tree `1046fbb657882e84b3dfc6d017943a9edf7782e5`。本子域完整阅读全文：WP52-B 正文 240 行、覆盖附表 111 行、AI 对应测试目录 294 行。
- 只读参考 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`。
- 主源为 `Data/Scripts/011_Battle/006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb`（1559 行）、`005_AI_MoveEffects_MultiHit.rb`（531 行）、`006_AI_MoveEffects_Healing.rb`（683 行），共 2773 行。逐登记分母 106 / 41 / 56，共 203 条语句。
- AGENTS.md 297 行已全文读取。参考只读、实现独立、不得实施框架等要求适用；本轮用户的“仅写指定 tasks 子目录”限制优先于 AGENTS 一般全局矩阵更新流程，因此以本目录矩阵交付，不改全局 Feature Matrix。
- 实际 model / effort / tier / speed / UUID 均 **UNVERIFIED**。未查认证、额度或反复探测配置。

## 证据与覆盖

`reading-ledger.jsonl` 把真实区间读取与语义审查记录分开；`logs/` 留存带行号原文读取。`structural-inventory.json` 只作 inventory_only 分母；没有把机器读入或登记存在当语义通过。

`forward-matrix.json` / `.md` 含 203 个逐登记单元的精确源区间、family、receiver、覆盖/复制状态、行为事实、实际消费者、flag/skill 前提、正式 clause 与边界。`reverse-matrix.json` / `.md` 含 167 条正式条款/覆盖/向量反向记录。`vector-matrix.json` 对本源直接负责的 56 个 BE 向量分别核算；其它 BE 与 AB/AI/AE/CE 向量已整篇阅读作为上下文，不冒充本子域重新审核全部非本源行为。

本三个主源的可审未读行与未处理登记单元均为 **0**。三个正式输入未读行为 **0**。WP52-B 涉及 Misc / BattlerStats / BattlerOther / ChangeMoveEffect 的其它主源行为由 R6-CA 父任务汇总；反向矩阵明确保留所有者边界，未用本子域结论泛盖它们。

新增读取的必要消费者包括：

- `005_AI/001_Battle_AI.rb:1-163`：对象建立、主体设置、决策阶段及五族分派共同默认。
- `005_AI/005_AI_ChooseMove.rb:1-393`：真实资格、目标枚举/重定向、调用招式替换、独立预测/评分门、候选异常包装、聚合/盟友反转及最终权重。
- `005_AI/009_AITrainer.rb:1-100`：野生/训练家默认、32/48 档与 Anti 标记独立消去。
- `005_AI/010_AIBattler.rb:1-595`、`011_AIMove.rb:1-563`：包装 receiver、有限 PP 查询、真实/粗速区别、状态意愿、伤害/命中/会心/附效与基数消费。
- `005_AI/008_AI_Utilities.rb:1-100`：具名迭代入口跳空/跳倒下，和公开原数组不同。
- 真实 MoveAttributes 基数/固定量/类型查询、MultiHit 计划次数与真实名单、默认 PBS 的 BEATUP / GEOMANCY / NATURALGIFT / LIFEDEW。
- `007_AI_ChooseMove_OtherScores.rb:1-329` 的通用目标消费者、`006_AI_ChooseMove_GenericEffects.rb:1-95,310-392` 的升降 helper 前门，以及相应状态/阶级处理器的具名调用/复制来源。未将这些依赖区间扩大成其全文件独立语义结论。
- `001_Battle/002_Battle_StartAndEnd.rb:279-282` 与 `009_Battle_CommandPhase.rb:198-215` 证明普通 host 入口：先设置席位再建 AI，命令循环有已有选择/真实可显示命令守卫后才调用 AI。替换选择入口由父任务完整核查。
- `003_Game processing/005_Event_Handlers.rb:97-141` 的同族及时复制/覆盖/缺源无写入，及 `001_PBDebug.rb:4-17` 的普通异常出口。

## 关键核验结论

连续切割两次整体登记不可叠加：最终分读回声侧计数，基数仍读连续切割。解除保护反向缺源 copy 不会抹掉旧 +7，也不会创建 BypassSubstitute 目标分。所有 copied 基数保留当前招式 receiver，不能把源身份的公式固定给目的身份。

默认 GEOMANCY 的 User / target-count 0 路径不消费其目标两回合/升阶 handler；四种 HP/香草对照只有共同整体修正，不能看到 handler 就声称扣两回合分。LIFEDEW 的目标评分有独立 canHeal 守卫；B64–B71 的预测、评分、HP 意识和更早用户治疗封锁门逐条区分。JUNGLEHEALING 调错整体族时只保留输入 HP 分，不补造其目标族偏好。

多击用总基数一次粗伤，2–5 击无连续攻击的代表基数 3.1P 与替身次数 3 分开；Triple Kick 没有逐击命中概率折算；智蛙基数和复制的破替身近似保留不同门。吸取、反伤和 LiquidOoze 的严格大小关系、整数/浮点差别、末端截断均保留，未写成真实逐击 HP 结果。

保护各独立 body 的资格集合不同：王盾/拦堵要求伤害招，普通/碉堡/尖刺允许可保护非伤害招；戏法防守、掀榻榻米、快防、广防、挺住各自的倍率/残余/已存在门独立核。旧代广防误查当前防守招类别，快速防守未重建实际最后行动失败门，均不能按理想规则修平。

磨砺新旧会心表不是同一分母：旧 cap index 4 为 2，115；新 cap index 3 为 1，60。幸运咒用当前潜力计分，不乘精确概率。锁定/识破/奇迹之眼/输电的直接槽枚举不补 PP 过滤；其它 check_for_move 保留有限 PP0 过滤。

对 GR6-C-001 的本子域影响检查：本三个主源通过 each_battler / each_foe_battler / each_same_side_battler 枚举者使用 `008_AI_Utilities.rb:9-35` 的空位/倒下过滤；真实 allBattlers / allSameSideBattlers 同样过滤。未把 C 提案的原数组扫描异常泛盖这些正常集合。C 的高技能瞌睡/睡眠换人原数组扫描及其所有后续 caller，由父任务作完整非提出者反证；本子域不冒称已独立裁决该全 scope。

## 待反证提案

`findings.json` 留有完整前提、普通对照、最小反例、异常/部分提交、负搜索范围、精确 source/spec、必要消费者、影响等级建议、最小修订/保留 scope、同步文件、验收与依赖：

- **GR6-CA-EB-001（建议 P2）**：围攻全状态合法队伍，PredictMoveFailure 关、ScoreMoves 开且目标正替身时，人数为 0 的目标评分除法无守卫；普通诊断成功返回可保留候选初值 100。现 B16 只有“空名单预计失败”，未具名这个独立门组合。
- **GR6-CA-EB-002（建议 P2）**：自然之恩无当前物、32 档评分开而预测关，通用伤害分会进入实际基数，先缺失物品身份查询而失败；不是“无完整 flag 正常回 1 再变 0”。现条款未具名此合法状态入口。

两条都是本子审提出，尚须非提出者反证并由 root 决定；当前文件不宣称成立最终缺陷。特别保留反证方向：更早真实资格是否拒绝、共同一般异常条款是否已足够满足本轮范围，不因发现路径就自动要求扩充规格。

## 证据等级与未执行范围

SOURCE_STATIC：本轮真实文本区间；DERIVED_VECTOR：逐条静态分支/常数数学推导；TOOL_VALIDATION：只读身份核对、结构分母与输出完整性校验。ISOLATED_REFERENCE / INDEPENDENT_MODEL / COMPLETE_HOST_DEMO 均 **NOT_EXECUTED**。未执行任何参考脚本、旧测试器、未知脚本、真实存档或外部服务。

完整战斗、设施、宿主表现、演出媒体、插件和未来 Showdown 接入仍保留完整既定范围；这里只证明当前参考 AI 在其具体入口的合同和异常边界，没有将其替换成未来实现架构，也没有缩减未来战斗范围。

所有文件仅在本子目录。没有 git 切换/提交/push、没有下载/安装/安全配置变更，没有外发回报消息。机器结构校验结果见 `validation.json`，该结果不替代以上语义审查。
