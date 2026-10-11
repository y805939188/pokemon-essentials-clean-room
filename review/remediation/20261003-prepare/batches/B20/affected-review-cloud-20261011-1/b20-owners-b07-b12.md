# B20 独立 affected 静态复审：B07–B12

审查目标为 NEW `1abaefb1db5818ff9404392143c476979d34c21a` / tree `2e40f9ad0e8fa40377d39e5a19eaa74cc2e05e85`；基线 C `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f` / tree `88a400af08253bea8d97ee2ef2fa6636f0900f92`。入口 `9a46a131ba2f7ea82b6eed823aa892cb57b0fba7:review/remediation/20261003-prepare/batches/B20/author-draft-1/candidate-review-1/affected.md`，最终读回包 `272885cca76c36cd04dde27b6be2c654759ec4c2`。本子审只写 `/tmp` 交付给父审，不改仓库，不签 actual/C。

本范围结论：**B07–B12 的下列实际有界接口 PASS_SCOPED / 保留；阻塞缺陷 0**。B11 的“无直接声明路线”不能作为完全未受影响结论，实际存在 WP47-A→动画映射/槽号的间接播放接口。B09 实际也消费 WP75 六旧战斗族转换输出，应在父报告补入其规则交界，原路由只列 WP74 并不穷尽实际影响。上述两项为影响范围补正，未发现必须改候选正文的缺陷；不替代 FULL 19/15 门，不扩大旧 owner 接受资格。

## 依据与静态限制

已读根 AGENTS.md、固定派发 `669997ac28258f26d0bafc81b1d081abb407a3a1` 下 B20/refreeze-after-B19-C-1 的 dispatch/author-contract/source-limits/accepted-interface-map。接口 map blob `265041e0830bd47130492e314c67520bb738f562`，SHA256 `80dde444746b204e6d2a1985da7d41e5bb51e8ae3e2557b9847e8c91055ee28c`，197120 bytes；本组 pointers `/interfaces/6` 至 `/interfaces/11`。原 owner PLAN 固定 `41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/batches.json#/6..11`，具体职责与读写范围均按该对象，未从标题或作者许可推出质量。

静态源为 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`，位于父审统一提供的 `/tmp/b20-reference`，只读。只运行新写的 Git/JSON/hash/文本记账，未执行任何参考游戏、Ruby、编译/转换/反序列化、行为向量或历史程序。所有数字和正反案例都是 **NOT_EXECUTED** 静态推导；运行观察与已证 Demo 链均 0。完整差异由父审统一重建并引用既定唯一流，本组未复制流或旧完整证据。

`b20-owners-b07-b12.json` 是本组自有元数据结果：逐 owner 全部 PLAN 写入文件的 C/NEW blob、SHA256、bytes 和逐字节比较；固定接口及参考文本范围身份；目录旧行顺序、重数及变化定位。字节相同只是回归证据，以下消费者/状态/条件判断才是保留依据。

## 逐 owner 判定

| Owner | 旧接受依据（仅其 scoped receipt） | B20 实际影响 / 结论 |
| --- | --- | --- |
| B07 | `d218aed120ed8ea1c88e1ec4752e5f7dcaaac226`，`review/remediation/20261003-prepare/batches/B07/integration-review-1/report.md`；19 贡献，WP28–32/目录范围 | 有界影响：WP30 升级公共动画名经 NEW WP74 §15，及共享 C003 的充分前提。8 个 PLAN 输出全部 C→NEW 同字节；道具实际 HP/库存、TR记录、EXP 逐步截断/零份额早退、糖果动画内取消消耗、进化/满队接收等旧责任保留。**PASS_SCOPED_INTERFACES_PRESERVED**。 |
| B08 | `6a060abf891021e942cb08a86495c840393d3f9f`，`B08/integration-review-1/report.md`；17 贡献，WP33/35/36/37/目录范围 | 有界影响：WP77 实际等级缩放数学消费、电话地图遭遇数据来源，WP75 请求生成后的遭遇/战斗入口，及 C003/C007 静态前提。8 个 PLAN 输出全部同字节；WP36 唯一数学、快照/版本、触发/选择/允许/主动包装，WP37 漫游/雷达资格及通知区分保持。**PASS_SCOPED_INTERFACES_PRESERVED**。 |
| B09 | `aa7ed0226f36220c1ac6ad598bdcad132aee5e4b`，`B09/integration-review-1/report.md`；20 贡献，WP38–42/目录范围 | 有界影响：WP74 的演出查找；另有实际 WP75 §8.2→WP39 §7.1 创建规则入口。7 个 PLAN 输出同字节；不能把动画名字命中当作参战、服从、PP、目标、命中或结果成功。伙伴接收/终局持物还原的 O01 勘误及已接受局部结论原样保留。**PASS_SCOPED_INTERFACES_PRESERVED**。 |
| B10 | `e0259f89915f6448b77f08658c7032a0384db2d4`，`B10/actual-review-round-1/report.md`；7 贡献，WP43–46/目录范围 | 有界影响：WP46 每击和恢复演出的动画数据查找及多帧/槽号。8 个 PLAN 输出同字节；每击 calcDamage/hpLost、实际 HP、吸取反伤先后、HP平均、65请求与139身份及域外1保持。**PASS_SCOPED_INTERFACES_PRESERVED**。 |
| B11 | `8c39c8e07a1d812b7892da1c9727a749b7c11c45`，`B11/integration-review-1/report.md`；6 贡献，WP47/48/50/目录范围 | 原派发确无直接声明路径，但实际 WP47-A 的卡带类型动画、环境借用动画、Ghost/non-Ghost 动画分支消费 WP74 关联与偏移，故本审追加有界间接影响。8 个 PLAN 输出同字节；动态目标、skillswapclause、有效能力/物品、重量、消费阶段保持。**PASS_SCOPED_INDIRECT_ANIMATION_INTERFACE_PRESERVED**，不得标“完全未受影响”。 |
| B12 | `75900f825c94732107232fa5f69dffba1cfbd648`，`B12/integration-review-1/report.md`；9 贡献，WP51/52/53/目录范围 | 有界影响：WP74 的数据命名/播放接口和真实效果查询的责任边界；11 个 PLAN 输出同字节。AI 的整体/目标失败、基数、整体/目标分数、技能开关、有效绑定/copy失败、道具资格与伙伴优先保持，未把演出结果反写为预测或真实数值。**PASS_SCOPED_INTERFACES_PRESERVED**。 |

上述 50 个 owner PLAN 输出逐文件身份都在 JSON 中，两份共享目录只算其真实文件身份；这个数量不代表 50 个独立质量结论。78 条旧 scoped receipts 仅定位旧资格，不转签本批或其它 owner。

## 具体消费链、正反证据与验收边界

### B07：成长/道具与公共动画

C 与 NEW `deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md` 第 91–114 行仍将基础份额截断、≤0 早退、修饰逐步取整、经验写入、每级学习与演出分层。NEW WP74 第 394–421 行只修必要 ASCII 名称/公共名拼接与保存/缓存交界，没有重写该算术、EV 已写副作用或 WP28 库存门。

源 `Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb` 第 186–213 行表明经验逐级写入/经验条在先，当前在场成员才请求名为 LevelUp 的公共动画，再继续升级数值/亲密度处理。经 `001_Battle.rb` 第 838–844 行的显示开关，至 `004_Scene/004_Scene_PlayAnimations.rb` 第 509–519 行按公共前缀与输入直接拼接查找。静态正反：输入 LevelUp 对应无新增空格的公共名；带空格的另一个名称不是自动等价。名称无命中不构成“没有获得经验”，也不回滚已经提交的成长。WP28 稀有糖果演出内取消后的消耗规则仍读其原入口，不能套用动画编辑器 Cancel。

保留验收边界：任何后续修订不得从动画保存/重编译或演出命中推出 EXP、库存、进化成功，且 C003 各旧根/扩展前提仍以原 owner 为准。

### B08：WP36 数学为唯一入口

C/NEW `deliverables/final-specification-set/creature-rpg/wp36-wild-encounters-and-modifiers.md` 第 188–203 行，尤其 §6.2 第 199–203 行，完整输入为全部队伍（含蛋、濒死），人口标准差、占比分段权重/0.001–0.999夹限、归一、正数半值向上、先下限再加2再 M 上限；空队/人工零和直接1。NEW `demo-dx/wp77-demo-evidence-and-capability-coverage.md` 第 152–156 行精确引用此入口，不引入近似均值。源 `019_Utilities/002_Utilities_Pokemon.rb` 第 194–237 行逐分支相符；`012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb` 第 47–59 行才在地图标记门后取该值、偏移 0..4、夹到 [1,M]、赋级、重算、重置招式。

静态正反：M100 的 [5,5] 为7→3..7，[10,50] 为52→48..52；空/人工零和为1，偏移后最终1；[100,100] 为100→96..100。成员改为蛋/濒死仍参与，不能先取 able 队伍。NEW 目录第 285 行 B20-C083 明示 NOT_EXECUTED；C 的当前地图选择第 164–174 行、生成第 178–186 行、入口生命周期第 207–225 行不被该生成后钩子改成统一筛选或统一清理。电话 TE 只消费联系人的地图资料（NEW WP77 第 113–115 行），不冒充当前已装配遭遇快照/实际遇敌；地图缺口与全部 Demo 链0仍保留。

保留验收边界：继续保留默认/可改示例区的限定、WP37 临时生成/已存在两门、雷达查询与步进机会差别；本组不批准插件改写或证明地图051真的进入并产生遭遇。

### B09：动画与实际转换输出的创建规则

C/NEW WP40 第 140–161 行仍把前 PP 资格、实际 PP、目标和逐击阶段分开；WP39 第 219–226 行仍是创建规则/战斗内 clause 区分的唯一主规则。NEW WP74 第 396–421 行的名→映射→保存/重编译/缓存仅决定查到的演出槽。源 `011_Battle/003_Move/002_Move_Usage.rb` 第 67–73 行存在 showAnimation、亲子爱公共演出和普通招式演出的分支；`001_Battle.rb` 第 838–844 行还有总显示门。不能从编辑器预览可见或查到槽推出真实动作合法/PP返还。

NEW WP75 第 192–209 行六族实际输出中，尾部缺省先按存在性/字面判断，再按位置插不能逃、可败和结果；不是固定参数数量，也不是求布尔语义。源 `021_Compiler/004_Compiler_MapsAndEvents.rb` 第 997–1133 行的六族分支已逐条静态阅读；野生核心两参、结果默认1、无禁逃/可败时不插对应规则，显式非默认才插；单训练家版本0存在且非nil仍传。`012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb` 第 30–86 行把规则名大小写归一，outcome/outcomevar 配值、cannotrun→canRun假、canlose→canLose真，悬挂配值失败，与 WP39 第 223–225 行一致。

保留验收边界：转换识别不保证所生战斗启动/执行，参与者/级数/伙伴/覆写/结果解码仍依 WP39/40 原门；六族正文总体质量由 FULL C034 门，门/训练家页面的全部条件继承由相关 affected owner 门另核，本组只核实际创建规则接口。

### B10：播放与每击数值次序分层

C/NEW `pokemon-rules/wp46-damage-multihit-and-healing.md` 第 17–35 行仍保留前 PP/目标阶段、每击重算与吸收、HP提交、反应/主要效果、终局与早退，动画随实际门/击数出现。源 `011_Battle/002_Battler/007_Battler_UseMove.rb` 第 620–668 行先给本击目标/计算/计划损失，调用本击招式动画，再实际提交 HP 与后续反应；不是把演出帧位或渐变不透明度作为 HP。

NEW WP74 第 396–399 行保留用户/对方映射优先与回退、命中槽加偏移、零有效编译保留旧映射及换序须重编译。源 `004_Scene_PlayAnimations.rb` 第 412–485、492–519 行对应：对方映射有无命中决定回退/翻转，类型/类别缺省与 TACKLE 后备仍受注册身份检查；查不到动画有局部返回门。源调用顺序与 C 的真实多击规则没有混成“成功动画即成功命中”。

保留验收边界：原 HP均分的不守恒/上限、持物触发、吸取/反伤、OHKO加载资格和139/新增1归属不由本批迁移；媒体/宿主运行失败仍未知，未保证所有异常出口正常继续。

### B11：无声明直接路线仍有实际间接播放依赖

C/NEW `combat-requirements/wp47-a-move-attributes-targeting-and-calling.md` 第 39–46 行将本次类型查询与卡带演出时再读基底类型分开，第 65–69 行环境效果有具体借用动画名/精神场地的 CONFUSIO 未决。源 `003_Move/008_MoveEffects_MoveAttributes.rb` 第 1459–1487 行，在演出时重新查询当前卡带基底类型并选偏移0..4；`003_Move/012_MoveEffects_ChangeMoveEffect.rb` 第 313–333 行选环境借用的具体招式名；第 215–217 行 Ghost/non-Ghost CURSE 演出另选偏移。随后仍经普通演出包装→WP74 编译映射/播放查找。NEW §15 的 ASCII 修订与 Common 立即拼接因此实际影响播放选择，即使 PLAN 没有直接路径交集。

静态正反：类型有效/已注册且卡带当前有效才形成对应基底/演出偏移；禁用持物不能凭“有卡带”取得该演出选择。本次早取类型不必等于稍后演出再查询。把秘密之力精神场地借用名自动修成 CONFUSION 会越过已接受未决；NEW 没有这么做。CURSE 的类别/目标门和 Ghost/non-Ghost 演出偏移是不同事实，不能因一动画槽命中重定向目标。

保留验收边界：追加的 affected 范围只限播放选择、名字、槽号与偏移，原 B11 六项接受、skillswapclause、动态类别与目标集合门、重量、特性/持物身份与阶段均保留；不得把 B11 路由遗漏升级为整包旧接受重审或将其未知统一关闭。

### B12：评分绑定与演出数据不互换

C/NEW `combat-requirements/wp52-a-generic-numerical-and-status-evaluation.md` 第 11–17 行明确分数不是伤害/成功，预测准备可能有真实查询副作用，但未保证统一回滚。其覆盖附表第 7–15 行和 B 主稿第 9–19 行、C 主稿第 9–17 行仍列整体/目标失败、基数和整体/目标分族、技能门、缺源 copy/最终绑定和条件物品分组。NEW WP74 只更正演出名、槽号、缓存和可观察编辑行为，没有增加 AI 效果登记或从一动画存在反推效果处理器。

静态源 `011_Battle/005_AI/011_AIMove.rb` 第 95–128 行的粗伤继续查询本招攻防/类别/修饰；对固定参考 `005_AI` 与 `006_AI MoveEffects` 的文本检索未找到 pbAnimation/pbCommonAnimation/move2anim/PBAnimation/PkmnAnimation/pbLoadBattleAnimations 消费。该有限定位佐证预测消费者与映射不同，不是完整动态调用不存在证明。B12 已接受有效绑定、Geomancy整体/目标差别、宝石世代门、药品资格与捕虫大会伙伴优先仍依其旧正文，不将候选静态演出案例当运行测试。

保留验收边界：A334/B270/C167 共771出现、全786与783/782直接有效及条件57/839的口径仍按原资格；动画存在不成为“全AI效果正确/纯查询/无副作用”的证明，动态插件与真实战斗成功不在本门。

## 共享目录保护与问题清单

独立按整文件文本提取：C 195 ID 行，NEW 214；旧195 ID完整前缀顺序/重复次数相同，193行逐字相同，仅 AN-M23（C/NEW第126行）和 CV-M18（C/NEW第161行）改变，追加19行。源文件整体 C blob `17ea088afe9e3fb67e4cbeaf5a7e6faa2eff940d` / SHA256 `ffd8992eef39f39892709d5dd591780669c97a0bd59dda9cc0f55818fee2e9f1` / 90084 bytes；NEW blob `a4a5279c9826d87e9663780c6e35a92cc733ffef` / SHA256 `6e9e463d4f6b7d7591d0d30e457787b759c56c4a3638080a15e92e63eb84cc45` / 100779 bytes。B19旧行及 PA040 与其他旧行一起同字节保留。各数字是目录记账，不是运行覆盖。

本组无阻塞 finding、无必需作者修复。父报告应记录两个实际 scope 补正：**B11→WP47-A演出→WP74映射/偏移**；**B09→WP75六族输出→WP39创建规则**。完成后仍只能声称这些 actual supported interfaces 保留；FULL/其余 owners、唯一登记者 G/ACT、独立 actual 两门和正式接受均保留。
