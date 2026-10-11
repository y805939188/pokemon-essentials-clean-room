# B20 独立有界 AFFECTED_ACTUAL：B07–B12

本范围结论：**PASS_SCOPED_AFFECTED_ACTUAL_B07_B12，剩余阻塞 0**。该判断绑定 ACT `6babcf657aef559dbf101aeb093a1beb730ab507` / tree `7f511347be10a55ed1341f4132e198ac6bdedede`，覆盖下列六个 owner 的真实受影响接口。它是本次独立 actual 判断，不转签 candidate PASS，不签 FULL、C 或 canonical 关闭。

固定管理包为 `66ba31f7895067c9d925aba20ce3de046fbf60e7` / tree `2f30f3ae648c593a32c52e2598a968bf677317ea`，入口 `review/remediation/20261003-prepare/batches/B20/actual-freeze-1/affected-actual-dispatch.json`，逐 owner 入口同目录 `affected-owner-entrypoints.json#/owners/6` 至 `/owners/11`。固定 NEW2 为 `3f521e6dea0b442e4bb174a9715c458416386b37` / tree `49f406a6de8ca2786e5dda27abada19780fdfa05`；旧正式 C 为 `de1a1c28a4255ff1cfd59fb6fb96f9be2d6ece1f`。

本子审只生成 `/tmp/b20-act-owners07-12.md` 及同名 JSON，交付父审纳入独立报告分支；未修改 repo、正文、原稿、main、参考或旧报告。完整 C→ACT、NEW2→ACT 差异由父审统一独立重建核对，本子审不重复发布流。

## 证据使用与实际整合判断

独立 Git/哈希核验七个 ACT payload 全部等于已审 NEW2；NEW2→ACT 没有 `deliverables/` 或 `specs/` 文件差异。本组原 PLAN 的 50 个输出路径出现、44 个唯一文件，在 C→NEW2→ACT 逐字相同。各 owner 的旧证据子树也保持相同路径、blob 和 mode；旧78条贡献及45主责ID的完整 qualified 对象分别固定绑定，未只引用标题或局部案例。

据用户要求，未重复无变化正文/参考的语义阅读；复用固定已审报告与源文本证据，独立重绑定到 ACT 的实际交付 blob、条款范围及整合状态。复用的是明确的行为条件/证据，不是旧 verdict。本次逐 owner 还判断了这些真实 caller、状态提交、数据来源和间接 route，在唯一 G 的 pending19 管理记录及外部 ACT 绑定下是否仍成立。

NEW2→ACT 的作者目录删除属于不同整合树中的证据导航变化；本审使用证据的固定历史 commit，未将某个候选树不包含独立报告分支误判为旧报告丢失。ACT 的公共三个文件均保留 C 原始前缀字节；新增 B20 记录仍 pending。该整合事实没有把旧局部接受扩大为整包通过，也没有改变实际消费者的执行门。

固定复用报告：

- `680e3988c4144db269e063971991134b8e0bd678:review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-1/b20-owners-b07-b12.md`，blob `578c2b7e2753bd0ccb8e6510cd3faaba62396700`，SHA256 `78852360415090216f799d55bd79305ee687b823551e6fa19e5d5e8b685168e1`。
- `7c5309763a6cf2e31564a1fe42786ebcbfecbef5:review/remediation/20261003-prepare/batches/B20/affected-review-cloud-20261011-2/b20-r2-other-owners.json`，本组逐 owner `/owners/0` 至 `/owners/5`；同目录 `b20-r2-phone-coins.md/.json` 的电话只读资料修复证据亦复用。
- 原 PLAN：`41fffb540c6483f5296ea0d33b789b75180d27ed:review/remediation-20261003-prepare/batches.json#/6` 至 `/11`；完整 qualified 对象为同 commit 的 `finding-acceptance.json` 各 ID 根对象，SHA256 `54e4c86be3db493a5463ce4bcdef81c7184f1a1d89e6b3bbea358f14cc347225`。
- 完整接受接口：`924c7c3a7a5029b07ad18085cf2dadb594512186:review/remediation/20261003-prepare/batches/B20/refreeze-after-B19-C-1/accepted-interface-map.json#/interfaces/6` 至 `/interfaces/11`，blob `265041e0830bd47130492e314c67520bb738f562`，SHA256 `80dde444746b204e6d2a1985da7d41e5bb51e8ae3e2557b9847e8c91055ee28c`。

所有路径、完整文件及条款哈希、完整 qualified 对象指针和对象摘要、旧子树身份、旧公共前缀与七 payload 身份的实际重新核验结果在 [本组 JSON](b20-act-owners07-12.json)。没有复制旧证据正文或源代码。

## 逐 owner 的实际判断

| Owner | 旧固定资格和范围 | ACT 的真实接口与有界结论 |
| --- | --- | --- |
| B07 | 19贡献/12主责，旧 report `d218aed120ed8ea1c88e1ec4752e5f7dcaaac226`；WP28–32道具、成长、进化及目录 | WP30 每级 LevelUp 公共演出实际消费 WP74 的 Common 名称/播放；EXP、EV、库存、学习、进化与演出各自提交门保留。8个原PLAN输出及旧证据子树同字节。**PASS_SCOPED_AFFECTED_ACTUAL**。 |
| B08 | 17贡献/9主责，旧 report `6a060abf891021e942cb08a86495c840393d3f9f`；WP33/35/36/37、繁殖孵化遭遇漫游及目录 | WP77 平衡级缩放实际消费 WP36 唯一数学；电话 TE 只读取联系人地图遭遇资料，均匀首4槽不代替实时遇敌权重/快照。8个输出及旧证据子树同字节。**PASS_SCOPED_AFFECTED_ACTUAL**。 |
| B09 | 20贡献/13主责，旧 report `aa7ed0226f36220c1ac6ad598bdcad132aee5e4b`；WP38–42捕获、参战、命令与回合结束 | 继续覆盖 WP74 演出及实际 WP75 六族输出→WP39 创建规则。7个输出及旧证据子树同字节；O01勘误和四个旧必需affected收据保留，不把转换/演出当成参战或结果。**PASS_SCOPED_AFFECTED_ACTUAL**。 |
| B10 | 7贡献/2主责，旧 report `e0259f89915f6448b77f08658c7032a0384db2d4`；WP43–46数值/每击/恢复及目录 | WP46 每击/恢复演出消费 WP74 映射、槽、偏移；实际HP、伤害计划、提交、反应及吸取反伤先后仍用领域门。8个输出及旧证据子树同字节。**PASS_SCOPED_AFFECTED_ACTUAL**。 |
| B11 | 6贡献/3主责，旧 report `8c39c8e07a1d812b7892da1c9727a749b7c11c45`；WP47/48/50类别目标、能力持物及目录 | 虽原声明无直接route，仍覆盖真实 WP47-A 动态卡带类型/环境借用/Ghost分支→动画名和偏移→WP74。8个输出及旧证据子树同字节。B11不是电话owner，不关闭CONFUSIO未决。**PASS_SCOPED_AFFECTED_ACTUAL**。 |
| B12 | 9贡献/6主责，旧 report `75900f825c94732107232fa5f69dffba1cfbd648`；WP51/52/53评分、效果绑定与大会及目录 | WP74 演出数据和 AI 查询/评分边界保留；11个输出及旧证据子树同字节，两个必需旧actual收据保留。动画存在不证明有效效果绑定、纯查询、统一回滚或完整AI。**PASS_SCOPED_AFFECTED_ACTUAL**。 |

全部原 qualified 根、裁决扩展、前提、最小修订、确定性复查和非本地责任继续约束。局部 examples 或新子例没有替代原对象；B08 的局部接受仍带 B07 影响/R04 两组 caller 限定，B09 的旧 O01 勘误及 required affected receipts 保留，B12 两个 required actual reports 保留。

## 消费条件与回归边界

**B07。** ACT WP74:394–421 与 NEW2 同字节，WP30:91–114 的原成长合同亦相同。基础份额逐步截断和零份额早退、经验写入和逐级学习保持；当前在场成员且显示门允许才请求 LevelUp。公共名把 `Common:` 与输入立即拼接，带空格名称保持不同身份。固定源证据为 `011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb:186–213`、`001_Battle.rb:838–844` 和 `004_Scene/004_Scene_PlayAnimations.rb:509–519`。缺演出不回滚已写成长；WP28 稀有糖果演出内取消消耗也不被编辑器 Cancel 重定义。验收条件：实际交付的名/缓存合同不得把槽命中或编辑保存变成EXP、库存、进化成功。

**B08。** ACT WP77:147、159–164 仍引用 WP36 的完整数学：全部队伍含蛋和濒死、人口标准差、分段权重夹限0.001–0.999、归一/取整、先下限后加2后最大级；空队/人工零和为1。地图标记门后才减4加0..4偏移并夹限、赋级、重算和重置招式。固定源为 `019_Utilities/002_Utilities_Pokemon.rb:194–237` 及 `012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb:47–59`。既审静态对照仍为 M100 的 `[5,5]→7→3..7`、`[10,50]→52→48..52`、空队/零和→1、`[100,100]→100→96..100`，均 **NOT_EXECUTED**。

ACT WP77:113–121 和目录:277 的电话 TE 对请求版本缺失回退0；双版缺或 Land/Cave/Water 全空才返回空文字；取首非空表首最多4槽均匀且保留重复、忽略槽权重。其固定源为 `013_Items/004_Item_Phone.rb:506–531` 与 `010_Data/002_PBS data/013_Encounter.rb:30–35`。这不等于 WP36 的当前装配快照、实时加权选择、触发机会、允许门或实际生成；未保护空队伍/非法参数/非法物种失败继续存在。验收条件：不得把电话回退与均匀资料选择传给实时遇敌或把平衡级缩放近似为普通平均；原繁殖、孵化、漫游/雷达的阶段和未知继续保留。

**B09。** ACT WP75:192–210 六族输出与 NEW2 同字节，WP39:219–226 创建规则合同同字节。尾参仍按存在性/字面位置，结果默认1；无显式禁逃/可败不插对应规则，显式非默认才插，训练家版本0存在且非nil仍传。固定源 `021_Compiler/004_Compiler_MapsAndEvents.rb:997–1133` 与 `012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb:30–86` 支持规则名归一、outcome/outcomevar配值、cannotrun/canlose状态和悬挂参数失败。四个事件简写前缀的修订不推广成六族脚本名/元数/尾参改变。验收条件：转换插入和实际战斗仍分开；参与者、伙伴、覆写、PP、目标、服从和结果解码继续过各自门。本判断不代替六族整节FULL C034质量签名。

**B10。** ACT WP74:394–421 与 WP46:17–35 的实际阶段合同保持。固定源 `011_Battle/002_Battler/007_Battler_UseMove.rb:620–668` 的每击目标/计算/计划损失、招式演出、HP提交、反应/主效顺序仍有支持；`004_Scene_PlayAnimations.rb:412–485、492–519` 的映射/翻转/类型类别后备和局部早退不能改实际数值。验收条件：帧、槽、不透明度不能代替HP，动画可见不能代表命中；HP均分、139/域外1、OHKO及吸取反伤原资格不由整合扩大。

**B11。** ACT WP47-A:39–69 与 WP74:394–421 均保持固定身份。卡带本次类型早读与演出再读允许不同，当前有效且注册才形成基底和偏移；环境借用实际名、精神场地CONFUSIO未决、CURSE的Ghost/non-Ghost演出偏移仍独立于目标门。固定源为 `003_Move/008_MoveEffects_MoveAttributes.rb:1459–1487` 与 `003_Move/012_MoveEffects_ChangeMoveEffect.rb:210–217、313–333`。验收条件：无直接route不能免审此实际间接消费；事件前缀大小写不敏感不传成Move/OppMove/Common登记身份规则，也不凭槽命中变更目标或关闭未决。

**B12。** ACT WP52-A:11–17 与 WP74:394–421 保持。评分不是实际伤害/成功；预测准备可能触发真实查询副作用，无统一回滚。整体/目标失败、基数、技能门、copy/最终绑定、条件物品和大会伙伴优先继续各自合同。固定源 `005_AI/011_AIMove.rb:95–128` 和旧有限文本检索提供局部佐证，不成为动态不存在证明。验收条件：演出存在不能认证AI效果绑定/纯查询/全AI；771出现、786全量及783/782、57/839原计数资格不由本次签名重定义。

## 固定身份与限制

参考源固定 `8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b` / tree `7589c800b61ba13a13040ed0d686979b80a84fd0`；本次只重新核验旧证据指向的 Git/hash 身份，不新执行或重复语义阅读源。

ACT 七 payload 的固定 blob：正式WP74 `42b214af3267436755339815ced7d67f67a3add1`；正式WP75 `d29ea4f31cf0b076991bf2cfda391c7703cd3040`；正式WP77 `e792348b0a7f35145736f7d595e86ec290b420b8`；目录 `d77a72b65a44f8d91b62dd06f0b324e7bfac774a`；原稿WP74 `76400f81ab7735c7a633049b4b3cec2b9915f49b`；原稿WP75 `3796ec9ff81a2b3d41fc42a952167c2925e0ca46`；原稿WP77 `64fc5fcf9ace768deaa640cc7f9a4190473785ea`。每项 SHA256/bytes 及 NEW2/ACT 独立比较在 JSON。

所有静态案例仍 **NOT_EXECUTED**；runtime observations=0、proven Demo chains=0。未执行参考游戏、Ruby、编译器、转换器、反序列化器、生成器、行为向量或旧脚本。仅执行新写 Git/JSON/hash/文本元数据核验。scope许可未作为质量通过依据，candidate PASS未机械转签。其余 owner、完整流、七payload整体、scope链、308总贡献及目录整体保护由父审另汇总核验；本子审不扩大局部实际结论。

本组剩余问题清单为空；无需本组作者修复。后续 actual 或 C 接受仍须父审/另一独立门和正式流程，不由本子审完成。
