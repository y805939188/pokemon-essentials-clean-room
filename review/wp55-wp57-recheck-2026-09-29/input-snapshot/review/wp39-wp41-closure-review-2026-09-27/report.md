# WP39／WP40／WP41 v3 闭合复审

日期：2026-09-27（Asia/Shanghai）。独立 reviewer；Reference/Audit 侧材料，不是提取侧自检，也不是 WP80 sanitized 产物。

**结论：三包均 PASS_SCOPED（限定静态范围）。本轮关闭 WP39-R01、WP40-R03、WP41-R02 的剩余内容及 C03；继承上轮九项关闭，原 12 项全部闭合，无剩余必修。可以先管理性回填，再按 WP43→WP44→WP45 推进下一批。** 配套 [回填与下一批执行提示](next-batch-prompt.md)。本会话只交付审查材料，未代回填或提取下一批。

## 1. 固定版本与机械检查

| 对象 | 被审 v3 完整 SHA-256 | 字节数 |
| --- | --- | ---: |
| `specs/combat/wp39-battle-context-and-participants.md` | `864dec262b0d7e3f9bdc4944bab07f2c2bcefd459fee2f6a46af9323bf0122f5` | 42165 |
| `specs/combat/wp40-commands-obedience-and-action-order.md` | `716a244244248bc25d626ed487fc4b47b65cd942942a3d9647821cbfde84ef7d` | 40100 |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `463cab3c062a366a7b142f66248ea9e5bb5bacb9a12ff8748f930aefd498a2ec` | 31502 |
| `planning/feature-matrix.md` | `2402cf4281b1aefb0770545d0ff147e56252f5b1ff9f36ceeb97777ac0691c8f` | 46283 |
| `planning/review-manifest-2026-09-19.md` | `029ace88ec69272796cd6be016d605be5d4e0ebb18b31948a9c52008265ca30d` | 228722 |
| `review/wp39-wp41-delivery-2026-09-27/delivery-summary.md` | `8360aec47b2bff8d03287fb07e23a96a7dc229cdf305ba071f7a79794d19e841` | 11292 |

manifest **425 条**、主 TSV **329 条**逐件完整哈希／字节／短标签匹配，无缺失或重复，TSV 路径全部属于 manifest 当前表。本轮固定 **427 项输入**。主 TSV 实测 `4bf6bcf4947aebeae1e46f10ba9ced94c4ed227c2d69435253c5802f56929a97`，44821 字节。

七份提取側 revision-diff 可从 v2 快照在内存精确重建当前文件；上轮 408 项快照与 final-checks 固定的十份 reviewer 原件未变，final-checks 本身亦与登记匹配。新三稿、矩阵、交付摘要与本次提取回应共 **82 条相对链接有效**；manifest 登记的 **85 个当前 JSON 可解析**。WP40→WP39、WP41→WP40／WP39 的完整哈希引用对应当前 v3。

机械证据见 [input-manifest.json](input-manifest.json)、[diff-checks.json](diff-checks.json)、[text-checks.json](text-checks.json)。快照为 `input-snapshot/`，当前固定值为 `current-hashes.tsv`，相对 v2 的差异为 `changes-from-v2.diff`。这些检查用于固定身份；下述行为结论另由实际文本与源码核对支持。

## 2. 三项剩余内容的验收

以下行号对应 §1 的 v3。源路径相对 `reference/pokemon-essentials/Data/Scripts/`（S）；所有引用固定在 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。

### WP39-R01 — CLOSED

核对 WP39 :48、64–67、73、80–86、208–210、250、294–301。

- 单参数物种／等级数组仍创建新个体；已有个体对象才复用。数组把等级传入创建入口，与分隔式的整数／范围前置检查分开。
- 成功合并时第一位已装载的 A 对象被保存，第二事件核心装载 B 的数据参数并复用 A；没有第二次 A 装载钩子。已经探测装载、但未满足保存条件后转入自身核心的另一条路径可再次装载，现已分开。
- §7.2 不再保留旧的跨入口混排箭头。正常野生包装先生成／生成钩子，再到允许时的覆写，未截断才进入核心 skip／on_start；直接核心收到物种／等级的次序相反。直接核心与覆写截断也不冒领包装末尾回调。
- 返回值摘要与场景统一：原始结果 3／5，野生真／假、训练家假／假。覆写修改／截断场景已明确 `can_override=true`。

本轮回读 `S/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb:356–386,395–440,458–504,538–557`，同目录 `003_Overworld_WildEncounters.rb:383–386,445–448`，及 `S/014_Pokemon/001_Pokemon.rb:199–205,1159–1166`。正文、场景、self-checks、boundary 组 1 对应同一组输入／身份／时序／输出规则。上轮已接受的单次构造与 skip 差异保留。

### WP40-R03 — CLOSED

核对 WP40 :124–145、155、159–170、246、252、318–320。

- 不变量与失败节已同步：普通非特殊招前置通过，PP=5 且无额外压力扣减，后段才无目标→PP 已为 4，不因失败回补；前置已失败则保持 5。
- 挣扎虽是特殊使用，不能仅凭该性质获得状态／服从豁免；后段由先确定的 skipAccuracyCheck 控制。服从检查自身的多回合、非招式、非游戏内、非玩家拥有等早退继续保留。
- 每击命中段的简写也改为引用实际 skip 标志，没有把所有特殊使用重新写成同一豁免。

本轮回读 `S/011_Battle/002_Battler/007_Battler_UseMove.rb:49–51,154–208,249–260,369–375`；同目录 `009_Battler_UseMoveSuccessChecks.rb:107–120,207–237,568–576`。self-checks 与 boundary 组 2 同步，独立算术 5−1=4 正确。已接受的四类调用、Me First／Encore 和其他检查序未因本轮改动被重新定义。

### WP41-R02 — CLOSED

核对 WP41 :46、54–62、219–221；直接传播 WP40 :34 及 boundary 组 3。

- 直接组合查询、严格 UI、登记入口都可以执行组合检查，查询本身不写选择。“组合检查只在登记”已删除。
- checkLaxOnly 决定仅换入／组合检查；shouldRegister 决定通过后是否登记。严格＋不登记与宽松＋不登记，在具名拘束前提下分别拒绝／返回候选，两者均不写 SwitchOut。
- canSwitch／canCancel 的按钮许可与选中后的检查分开；负下标的仅换入查询、组合查询、UI 登记区别得到保留。
- 已登记后的实际替换不重新调用组合检查。WP40 的总览改为分族引用，没有继续给换人添加统一执行复检。

本轮回读 `S/011_Battle/001_Battle/005_Battle_ActionSwitching.rb:9–14,77–134,206–225,274–284`，`S/011_Battle/004_Scene/003_Scene_ChooseCommands.rb:163–183`，`S/011_Battle/001_Battle/010_Battle_AttackPhase.rb:48–66`。正文、两条严格／宽松场景和交界摘要均一致。

## 3. C03 与继承范围

C03 全部接受：

| 维护 | 当前对应 | 本轮证据 |
| --- | --- | --- |
| 野生计数量词与时点 | WP39 :146、231、309 及 self 向量；初始输入数量与参与者校验可战斗计数分开 | StartAndEnd :29–40；Starting :395–396 |
| 返回上一席位撤销 | WP40 :55，仅此分支撤销上一席位 | CommandPhase :252–260 |
| Mega 资格顺序 | WP40 :214，环检查在业主槽检查之前 | ActionOther :92–102 |
| 伤害族末段门 | WP41 :185，吸盘／扎根仅指非野生拖出末段，不覆盖野生终局 | SwitchingActing :157–174,228–254 |
| 逃跑／调试取消摘要 | WP41 :187–188，普通／替补分层；调试取消决定不变，但命令期停止其余选择 | ActionRunning :28–51,60–95,134–159；CommandPhase :238–245 |
| 交付目录与版本链 | 摘要分别标首审／复审材料目录，首发无前版仅保留为历史，当前 v1→v2→v3 明确 | 实際路径／全文差异／身份核对 |

以上短名完整路径列于 [source-checks.json](source-checks.json)。本轮没有新增阻塞或另立 C04 维护清单。

上轮已经关闭的 WP39-R02/R03、WP40-R01/R02/R04/R05、WP41-R01/R03/R04，以及 C01/C02 继续继承。差异检查没有发现本轮修改对这些已接受规则的直接回归；未重做首审或重读所有战斗效果。静态对照及检查结论见 [static-vectors.json](static-vectors.json)、[static-checks.json](static-checks.json)。

## 4. 限定通过范围与管理性回填

本轮批准的是 §1 的三个 v3 字节版本。范围如下，不能写成整个战斗系统或整行 Feature 已完成：

| 包 | 可登记 Reviewed 的限定静态范围 | 继续保留 |
| --- | --- | --- |
| WP39 | 已述野生／训练家包装与核心入口、输入校验、跳过及返回；九布局／邻近／业主和队伍段；参与者初始化与指定写回／回读；创建规则、环境输入、具名钩子与善后接口 | 完整终局／成长 WP42、捕获 WP38、设施完整规则、完整天气／效果族、真实演出和多布局运行 |
| WP40 | 已述命令与控制、选择／登记／取消、分族执行检查与 PP／物品消费；服从与主要行动排序／重排；Mega/Primal 战斗侧资格时机、Call/Shift 选择合同 | 计算细节 WP43、效果／特性／道具族 WP44–50、AI、WP22/23 完整领域、设施变体与真实输入演出 |
| WP41 | 已述换入／换出／组合／UI／登记／执行分层；替补与入场通知合同；Shift 与有界重映射；三类逃跑入口／速度计数；已述强制换出族和形态清理交界 | 完整回合末／终局 WP42、入场效果全集、AI、个体变身完整域、界面演出与运行组合 |

授权提取方同轮先作管理性回填：三稿头部／§15 写 **Reviewed（限定静态范围，2026-09-27 闭合复审 PASS_SCOPED；管理性回填）**，采用上表范围。将 F11-01/02、F11-03/04、F11-05 对应子范围改为 Reviewed，保留前向 Inventoried。

按 WP39→WP40→WP41 回填并级联上游完整哈希：新哈希是“回填后版本”，此表 v3 仍是“被审版本”。保留 v1／v2／v3 历史，保存相对本轮快照的回填 diff。允许同步三包互相的状态引用和其他规格中的必要状态引用；只关闭本次已审子范围，不能借此关闭 WP22/23、WP38、WP42 或完整效果域。旧自检／报告保留历史语境，不倒写审查结论。

**限定通过集合现为 WP01–WP21、WP24–WP31、WP33–WP36、WP39–WP41、WP59–WP60。** 不得写成 WP01–WP41 连续通过。本 reviewer 没有代改状态；提取方完成纯管理回填后无需为状态字节另等一轮批准，即可执行配套下一批。

## 5. 下一批：WP43→WP44→WP45

已核对 `planning/extraction-plan.md` §1、§2/2.1 及 WP42–45 行。WP43 的依赖 WP40／19／20 已限定通过；WP44 可接批内固定 WP43 与已审 WP20；WP45 再接已审 WP40／11／59 及批内固定 WP44。

因此按 **WP43 类型／命中／伤害 → WP44 状态／能力阶级／免疫 → WP45 天气／场地／阵营／位置** 三包推进，逐包自检、完整哈希固定，批末检查交界并统一送审。新包只登记 ReviewPending（自身具名范围），不自批 Reviewed。

WP42 的完整期限与终局规则依赖 WP44／WP45，此次不因编号连续而提前宣告 WP42 完成；也不提前提取 WP46–50 的全部修正族或 AI。配套提示已写明前向引用、阶段归属、独立数值向量和停止点。

## 6. 证据边界与执行记录

本轮新证据为实际 v2→v3 差异、修订正文和传播材料、13 个源文件的定点回读及与固定 commit blob 的一致性、手工状态对照、独立算术与机械完整性检查。上轮 24 个源文件哈希未变；旧关闭结果作为旧证据继承，不冒称本轮重新证明整个引擎。提取侧的“全部通过”仅是输入声明；本报告给出独立有限验收结论。

参考 HEAD 为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`，普通 Git 状态为空。仅在本新 review 目录创建报告、提示、检查和输入快照；未改任何规格、矩阵、manifest、计划、旧审查或 reference。未运行游戏、参考 Ruby／表达式、解释器／事件脚本、生成器、编译器、转换器、插件或真实网络；未操作真实地图／存档／输入；未创建任务／并行 Agent，未提交／推送。

**PASS_SCOPED 不等于运行确认。** Demo、宿主、媒体、插件、U01–U10 与 WP78→WP79→WP80 阶段出口继续保留。最终输入稳定性及本轮产物哈希见 [final-checks.json](final-checks.json)。
