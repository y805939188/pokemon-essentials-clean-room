# WP39／WP40／WP41 v2 复审收尾回应（提取侧 v3）

日期：2026-09-27（Asia/Shanghai）。提取／修订方材料，非独立审查结论、非 WP80 sanitized 产物。依据本目录 [report.md](report.md) 与权威执行细节 [revision-prompt.md](revision-prompt.md)。参考库只读，固定 commit `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b`。已读根 AGENTS.md；涉及的活动子目录无新增适用 AGENTS.md，审查快照中的副本只作历史证据。

**复审给定结论：REQUEST_CHANGES，9/12 关闭。** 关闭项 WP39-R02/R03、WP40-R01/R02/R04/R05、WP41-R01/R03/R04 及三个剩余编号已接受部分保留；C01/C02 已接受。本次仅收尾 **WP39-R01、WP40-R03、WP41-R02**、C03 及直接传播，三包仍为 **ReviewPending（自身具名范围）**，新 v3 尚未外审。下列“验收”均是提取侧的只读文本核对和人工推导，不宣称 reviewer 已关闭剩余项。

## 1. 固定输入与意见适用性

修订前逐件调用 `shasum -a 256` 与 `stat -f %z`，并与本轮 `input-snapshot/` 逐字节比较。提示 §1 六件必检及 self／boundary／主 TSV 三件补检，**九件全部 MATCH，未漂移，意见适用**。未修改快照。

| 对象 | 被审 v2／修订前完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp39-battle-context-and-participants.md` | `1fdfb8bc8c12ab33bde658f4569849a097f9a0fea0bcd058b6ee02dd5479e197` | 38,555 |
| `specs/combat/wp40-commands-obedience-and-action-order.md` | `555282ba37ae92ae1fb75b2fbfebc5a989efe4a7f73e956dae714c6d097f7cde` | 38,012 |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `237ac575dc1da67e4e9776d6f28a24a7bbefb239cbccc9e9d9a40897f3d93033` | 28,916 |
| `planning/feature-matrix.md` | `0fe9fe2fce11fd3db104f752361115a164bc5442be54be613a1baebb43922683` | 46,193 |
| `planning/review-manifest-2026-09-19.md` | `5bf42d0d98ca4a2a39cfc3d06815ac9fd8747be8dbc49631993dca8101fa84b1` | 218,662 |
| `review/wp39-wp41-delivery-2026-09-27/delivery-summary.md` | `f9209703a127a2165d3c821d5e42487e5cd4e61bb2993e66ade0bb51c40b948e` | 8,855 |
| `review/wp39-wp41-delivery-2026-09-27/self-checks.json` | `9633f336394ae2577c5784d5e1f3e736e310c147a614d6901478b239a94adbd7` | 12,444 |
| `review/wp39-wp41-delivery-2026-09-27/boundary-checks.json` | `0db06e6834764314a7b1247fd808bef4f67fbddacbe6fd5c60e3a29bebc21a4a` | 5,323 |
| `review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv` | `1a5a56e8521544f38c5aa3b1a588d9dfc270219fa3b3a63504f930fab49ea7a8` | 42,331 |

本轮所有源文件为静态读取；13 个本轮定点读取文件的路径、范围、实测哈希／字节与固定 commit 文本一致性记录在 [self-checks.json](../wp39-wp41-delivery-2026-09-27/self-checks.json) 的 `v3_recheck.source_checks`。早期全文阅读为继承证据，不冒称本轮重读整个引擎。

## 2. WP39-R01：输入、待战复用、钩子与返回摘要

**回源结论**：`Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb:356–440,458–601` 分开处理包装与直接核心、数据与对象。合并探测成功保存的是第一次已装载训练家 A；第二事件把其对象交入核心，对第二位 B 的数据输入装载并触发钩子，对 A 复用且不再次触发装载钩子。若第一次虽装载却未满足待战保存条件，原数据进入自身核心且未 skip 时才可能再次装载，这是另一分支。野生包装先创建个体，再尝试覆写，之后才核心 skip／开战记录；直接核心先 skip／开战记录再创建。单参数物种／等级数组仍创建新个体，已有个体参数才复用；数组等级交给后续创建入口，不具备分隔式的整数／范围前置检查。野生生成钩子位置另核同目录 `003_Overworld_WildEncounters.rb:383–384,445–448`；等级后续写入核 `014_Pokemon/001_Pokemon.rb:199–204,1159–1165`。野生包装结果 3／5 为真／假，训练家包装为假／假。

**修改位置**：WP39 §3.1–3.3（当前 :48、64–67、73、81–86）、§7.2（:208–210）、§9（:250）、§12.2（:294–301）；头尾标注 v1／被审 v2／当前 v3。旧混合钩子总览、合并后重新装载 A 的保证、数组原样复用与两包装统一“非胜”归一均被改写。覆写修改与截断场景均补 `can_override=true`。self-checks 对应向量、boundary 组 1 与下游完整哈希同步。

**静态验收**：

| 条件 | 核对预期 |
| --- | --- |
| A 数据探测成功并保存；B 数据触发第二事件，核心不 skip | A 装载及装载钩子仅第一次；第二核心装载 B、复用 A；A 的修改保留 |
| 已探测装载，但单一训练家／队伍上限条件不成立；自身核心不 skip | 原数据可再装载，不套成功合并路径的次数结论 |
| 单野生物种／等级，允许覆写且修改不截断 | 构造／生成钩子一次，先于覆写、skip、开战记录；核心用同一个体 |
| 正常包装的单参数合法数组／已有个体对象 | 分别创建一次／直接复用；数组等级检查不与分隔式混同 |
| 相同物种／等级输入、skip 成立；包装未覆写截断 | 包装已生成；直接核心尚未生成 |
| 结果 3、5 | 野生真、假；训练家假、假 |

**保留边界**：单次野生构造、skip 时点及对象输入已接受部分保留；不运行生成器、解释器或事件，不改变真实地图／输入；待战事件可达性、覆写模式完整域与宿主时序仍保留。

## 3. WP40-R03：PP 与服从摘要一致性

**回源结论**：`Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb:50–51,154–206,249–253,369–374` 显示：普通调用先通过前置检查再扣 PP，后面才确定目标并处理无目标失败；挣扎属于特殊调用，但不打开 skipAccuracyCheck。`009_Battler_UseMoveSuccessChecks.rb:107–120,207–236` 则以 skip 标志决定是否进入状态／服从后段；服从门自身仍保留多回合、非招式、非内部战斗与非玩家拥有等直接通过条件。

**修改位置**：WP40 §5.2 第 4 步（:134）、§5.3 的命中豁免简写（:155）、§8 第 8 条（:246）、§9（:252）、§12.2（:318–320）。保留已接受 §5.2 四类调用表与 §5.4 第 5 条，清除摘要中的统括特殊动作豁免和无目标免耗断言；self-checks 与 boundary 组 2 同步。不把进入服从门等同于一定不服从。

**静态验收**：普通非特殊招、前置通过、PP=5、无额外压力扣減、后段无目标→独立算术 5−1=4，失败不回补；前置失败则 PP=5。挣扎特殊调用且此前检查通过，满足内部战斗、玩家拥有、高等级及配置等实际服从前提时继续该门；不因 specialUsage 自动豁免。普通起始的多回合续招不追溯打开 skip 标志，但服从检查自身的多回合早退照常。

**保留边界**：不重写使用招式流程，不重算伤害，不扩展效果族；Me First、Encore、Stance Change、PP 主序及已关闭的道具／抢夺等合同保留。全部为静态对照，未抽样或执行参考过程。

## 4. WP41-R02：查询强度与登记分开

**回源结论**：`Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb:77–133` 的队伍界面先选宽松换入检查或严格组合检查，再决定是否登记；直接组合查询不写选择，登记入口再次组合检查。不登记界面仍可走完整组合资格。仅换入查询对负下标直接通过，组合查询仍检查重复选择与换出，界面请求登记另拒绝负下标。`004_Scene/003_Scene_ChooseCommands.rb:168–182` 的 canSwitch／canCancel 仅控制按钮许可。`001_Battle/010_Battle_AttackPhase.rb:48–65` 到 Switching :220–225、274–284 的实际替换链不重新调用组合检查；随机／宽松候选路径另核 Switching :206–215。

**修改位置**：WP41 §3.1（:46）、§3.3–3.4（:54–62）、§12.2（:219–220）；WP40 §2 登记概念（:34）改引用 §8 分族合同；self-checks 新增严格／宽松不登记、正常登记与执行不复查对照，boundary 组 3 改写整个资格摘要，移除登记专属限制。

**静态验收**：共同前提为合法本业主存活非蛋替补，未在场、无重复候选、按钮允许；当前成员被拘束且无幽灵／必换特性道具豁免。

| 路径 | 结果 | 选择写入 |
| --- | --- | --- |
| 严格界面（checkLaxOnly=false），不登记 | 组合检查因换出拘束而拒绝 | 不写 SwitchOut |
| 宽松界面（checkLaxOnly=true），不登记 | 仅换入通过并返回候选 | 不写 SwitchOut |
| 正常登记，另有组合资格全过的前提 | 登记入口再次组合检查，通过后写入 | 写 SwitchOut 与下标 |
| 已登记有效换人，较快对手入场后新抓取 | 实际替换不重新调用组合检查；其它执行前提保持 | 使用既有选择 |

**保留边界**：保留 canSwitch 只影响普通可取消 UI、已登记执行不复查、负下标与取消分离的既有结论；不操作队伍菜单，不定义未来 API，不扩展 AI 或拘束效果族。

## 5. BATCH-C03 有界维护

| 项 | 回源与结论 | 修改位置／静态验收 | 保留边界 |
| --- | --- | --- | --- |
| 可战斗野生计数 | StartAndEnd :30–40 按队可战斗计数；Starting :396 起初按输入个数设置尺寸 | WP39 §4.3 :146、§8 :231、§12.2 :309 与 self 向量，明确两个时点 | 九布局与已接受 1v1／1v2 缩减例不变 |
| 上一席位撤销 | CommandPhase :252–260，该分支撤销上一席位后退出 | WP40 §3.2 :55；self 对照不再多算当前席位撤销 | 成功登记保留与取消分离不变 |
| Mega 顺序 | ActionOther :97–101，天空摔投后先环再业主槽 | WP40 §7.1 :214；self／boundary 同步 | DEBUG 位置、非负复位与 -2 保留不变 |
| 伤害族末段门 | SwitchingActing :228–254，先排除野生再查吸盘／扎根 | WP41 §10 :185；boundary 组 3 限为非野生拖出 | 已接受的野生终局与变化／伤害分族不变 |
| 逃跑与调试取消摘要 | ActionRunning :5–160；CommandPhase :238–245 消费返回 | WP41 §10 :187–188 引用三入口；决定不变但命令期停止其余选择 | 替补跳过整组、94／64 与当前战斗副本速度不变 |
| 摘要目录与版本 | 实测首审回应／diff 位于首审目录，已有 v1→v2 链 | delivery-summary 版本记录、§2、§5–7：首发无前版仅作历史；当前 v1→v2→v3 | 原回应／diff 原件与旧回填结论不覆盖 |

上述简称对应的完整路径与本轮读取范围见 self-checks 的 source_checks；全部 13 文件与固定 commit 文本匹配。C03 不作为重开九个关闭项的理由。

## 6. 新稿固定、交付与差异

三规格已按 WP39→WP40→WP41 顺序写入后立即实测；WP40→WP39、WP41→WP40／WP39 共三条完整哈希绑定准确。头尾保留被审 v1／v2 完整哈希，当前注明批内修订稿（v3）尚未外审；矩阵五行保留具名 ReviewPending＋前向 Inventoried。

| 当前对象 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `specs/combat/wp39-battle-context-and-participants.md` | `864dec262b0d7e3f9bdc4944bab07f2c2bcefd459fee2f6a46af9323bf0122f5` | 42,165 |
| `specs/combat/wp40-commands-obedience-and-action-order.md` | `716a244244248bc25d626ed487fc4b47b65cd942942a3d9647821cbfde84ef7d` | 40,100 |
| `specs/combat/wp41-switching-positioning-and-escape.md` | `463cab3c062a366a7b142f66248ea9e5bb5bacb9a12ff8748f930aefd498a2ec` | 31,502 |
| `planning/feature-matrix.md` | `2402cf4281b1aefb0770545d0ff147e56252f5b1ff9f36ceeb97777ac0691c8f` | 46,283 |
| `review/wp39-wp41-delivery-2026-09-27/self-checks.json` | `6d16628fb0c8b2819c6a83aa792785849ce839d8ce95a695121ffd2d18b6a8ea` | 23,048 |
| `review/wp39-wp41-delivery-2026-09-27/boundary-checks.json` | `46a58b20347ce9089cec89497d046a2270fc28eb9599f052b66ed4f03bd949d0` | 6,926 |
| `review/wp39-wp41-delivery-2026-09-27/delivery-summary.md` | `8360aec47b2bff8d03287fb07e23a96a7dc229cdf305ba071f7a79794d19e841` | 11,292 |

七份差异均相对本目录 `input-snapshot/`，含 self／boundary；已独立解析差异块并在内存从快照精确重建当前文件，7/7 匹配，未向快照应用补丁。

| 差异 | 完整 SHA-256 | 字节 |
| --- | --- | ---: |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/wp39-revision.diff` | `23a5fb57d6f7f43d2fa3fe087e479d0185e9bdf1f4f5f146cda3b1c648bcf445` | 20,031 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/wp40-revision.diff` | `56cf484f1a68b95a394b02c5614bbfbb57c1afd60fbf9644221781e29b7e1745` | 18,173 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/wp41-revision.diff` | `d92fe8e1360cff1003c8a9cfcef22472866a393b50ec389409339beee3c4e685` | 11,805 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/feature-matrix.diff` | `24113271408ca25006c18a3b4b2fd7e615847d33169b96499bd13f93c9999e83` | 7,059 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/self-checks.diff` | `b2f0c90446ddae528d2ed4c8f5e129a4e75460509d349d184ff20555d0f843fc` | 21,014 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/boundary-checks.diff` | `e8b470e999c710daae54092a8e952cb6a819a253747421ac6c7ed9213b0e20ea` | 10,364 |
| `review/wp39-wp41-recheck-2026-09-27/revision-diffs/delivery-summary.diff` | `c2e32a5fce83c85243af6b605a9bc051194493baf59a188145e904fe7e77090b` | 14,927 |

此前原 408 项快照全部重新校验匹配；登记前只有上述七个允许对象的活动版本变化，原件不变。本轮 reviewer 自有材料共 11 份（含不自哈希的 final-checks.json）；其中 final-checks 固定的另 10 件已与其记录比对。相关当前 JSON 16 件均能解析。旧矛盾句已作全文关键词清扫，历史声明仍以历史身份保留。以上证明材料与文本对应，不构成独立行为审查。

登记次序：本回应与七差异、reviewer 11 件加入主 TSV v22（保留原 310 条、追加 19 条），再更新 manifest 第四十七轮 §1／§2.1／§3／§4。manifest／主 TSV 不自哈希；包含它们的全量最终哈希、字节、短标签、缺失／重复、集合、相对链接、JSON 和 reference Git 终检在登记完成后实测，由最终交付消息报告，避免自哈希循环。

## 7. 送审集合与停止点

只送 **WP39-R01、WP40-R03、WP41-R02 三个剩余编号、C03 差异及直接传播**短复审。三包与 F11-01～05 维持 ReviewPending（各自具名范围）＋前向 Inventoried，不自批 Reviewed；已关闭九项及三个编号已接受部分保留。

既有限定通过集合仍为 **WP01–WP21、WP24–WP31、WP33–WP36、WP59–WP60**。未启动 WP22／WP23／WP32／WP37／WP38／WP42／WP61 或其它包，未向 reviewer 发消息、未创建任务／并行 Agent、未提交／推送。未运行游戏、参考 Ruby／表达式、解释器／事件脚本、生成器、编译器、转换器、插件或真实网络；未操作真实地图／存档／输入；仅自有文本、哈希、集合、JSON、diff 与独立算术。Demo、宿主、媒体、插件、U01–U10 与 WP78→WP79→WP80 阶段出口继续保留。
