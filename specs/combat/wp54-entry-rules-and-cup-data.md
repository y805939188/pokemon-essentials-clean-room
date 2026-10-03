# WP54 默认杯赛、条款与资格目录 v1

状态：**Reviewed（限定静态范围，2026-09-28独立首审PASS_SCOPED；管理性回填）**。随[主稿](wp54-entry-eligibility-level-adjustment-and-clauses.md)A～F的56定义身份、10活动工厂、5直接样本、3模式与14条款键数据；默认组合来自固定文本，源身份仅审计；不按参考类层级设计未来规则体系。块注释示例不是当前可调用工厂。设施完整会话、租借、回放与运行不随之通过。

## 1. 十个活动规则工厂

单双只决定场上布局，不自动改变下表最终人数；成员未额外装Able者不能自加“HP必须正”。表中条款短名均加clause后缀，具体阶段/失败返回在主稿§6。

| 工厂身份 | 最终人数/布局 | 成员限制 | 组合限制 | 等级调整 | 战斗条款 |
| --- | --- | --- | --- | --- | --- |
| pbPikaCupRules | 恰3，单双均如此 | Standard；等级15..20 | 物种不重/物品不重；总等级≤50实际入整队 | 仅对手总等级15/20/50 | sleep, freeze, selfko |
| pbPokeCupRules | 恰3，单双均如此 | Standard；等级50..55 | 物种不重/物品不重；总等级≤155实际入整队 | 仅对手总等级50/55/155 | sleep, freeze, selfdestruct |
| pbPrimeCupRules | 单3/双4 | 无Standard/最低最高成员限制 | 物种不重/物品不重 | 仅对手开放下限最大等级（当前100） | sleep, freeze, selfdestruct |
| pbFancyCupRules | 恰3，单双均如此 | Standard；等级25..30；身高≤2m/重≤20kg；Baby | 物种不重/物品不重；总等级≤80实际入整队 | 仅对手总等级25/30/80 | sleep, freeze, perishsong, selfdestruct |
| pbLittleCupRules | 单3/双4 | Standard；UnevolvedForm；最高5 | 物种不重/物品不重 | 仅对手固定5 | sleep, freeze, selfdestruct, perishsong, sonicboom |
| pbStrictLittleCupRules | 恰3，单双均如此 | Standard；UnevolvedForm；最高5；LittleCup附加禁表 | 仅物种不重，无ItemClause | 仅对手固定5 | sleep, evasion, ohko, selfko |
| pbBattleTowerRules | 单3/双4 | Standard | 物种不重/物品不重 | open真仅对手开放下限60；假双方上限50 | souldew |
| pbBattlePalaceRules | 单3/双4 | 同Tower | 同Tower | 同Tower，另战斗种类为Palace | souldew；Palace完整行为WP56 |
| pbBattleArenaRules | 恰3且单打 | 同Tower | 同Tower | 同Tower，另战斗种类为Arena | souldew；Arena完整行为WP56 |
| pbBattleFactoryRules | 单3/双4 | 无Standard；禁UNOWN；最高100(open)/50(非open) | 物种不重/物品不重 | 双方固定100/50 | souldew；租借会话WP57 |

总等级经addLevelRule加入，但真实“子集添加”写整队列表；完整输入报名按整队总级判断，最终所选也同样判断。建议等级未按该总额均摊，不能替代最后资格检查。已有规则字段setRuleset/setLevelAdjustment后写覆盖；附加规则顺序执行，重复布局后者生效。

## 2. 直接规则集样本与模式转换

以下直接样本只初始化最大数，最少仍1；没有等级调整/战斗条款。与上表同名工厂不同。

| 审计样本 | 参赛最少..最大 | 成员/组合 |
| --- | --- | --- |
| StandardRules(n,L可选) | 1..n（负n最大域特殊见主稿） | Standard、物种不重、物品不重；L存在加最高级 |
| StandardCup | 1..3 | 上项最高50 |
| DoubleCup | 1..4 | 上项最高50；这里只是名字，不自动建双战条款 |
| FancyCup | 1..3 | Standard、最高30、身高≤2m、重≤20kg、Baby；总级≤80实际整队；物种/物品不重；无最低25 |
| LittleCup | 1..3 | Standard、最高5、Baby；物种/物品不重；无必须还能进化条件 |
| LightCup | 1..3 | Standard、最高50、重≤99kg、Baby；物种/物品不重 |

真实会话modeToRules独立组合：

| mode | 成员/队伍 | 调整 | 其它 |
| --- | --- | --- | --- |
| 1开放 | StandardRules(所给人数,最大等级) | 仅对手开放下限30 | 指定种类/布局，未自动装心之水滴 |
| 2帐篷 | 同上 | 仅对手开放下限60 | 同上 |
| 其它 | StandardRules(所给人数,50) | 仅对手开放下限50 | 同上；Arena强制单布局 |

register已有rules时不重新生成；Factory注册另设租借数据、人数3及Tower战斗种类，完整租借会话前向WP57。set给定规则的名称解析/写杯工具不等于真实接待事件已存在。ChallengeRules:267–382的历年赛事/Colosseum等块注释只作为未启用作者示例，不加入上述默认集合，不复制其长示例程序。

## 3. 固定限制集合与参数

| 合同 | 字面集合/默认值 |
| --- | --- |
| Standard提前普通能力允许 | TRUANT, SLOWSTART（读species_data.abilities，不是当前个体能力） |
| Standard提前物种允许 | DRAGONITE, SALAMENCE, TYRANITAR |
| Standard物种拒绝 | WYNAUT, WOBBUFFET |
| Standard种族总和拒绝界 | ≥600，位于前两允许之后 |
| LittleCupRestriction禁物 | BERRYJUICE, DEEPSEATOOTH |
| 同附加禁招 | SONICBOOM, DRAGONRAGE |
| 同附加禁物种 | SCYTHER, SNEASEL, MEDITITE, YANMA, TANGELA, MURKROW |
| NegativeExtended的显式拒绝 | ARCEUS；MICLEBERRY, CUSTAPBERRY, JABOCABERRY, ROWAPBERRY；其余缺true仍不通过 |
| 限制物种数量模板 | 整队模板4，子集模板2；自定义通用上限与名单由作者给 |
| 全局默认 | MAX_PARTY_SIZE=6，GrowthRate最大等级由Settings.MAXIMUM_LEVEL=100 |

名称/顺序是此快照数据，不泛化为官方赛事或所有世代；物种/物品别名、形态、缺数据处理依WP03/18及主稿资格。

## 4. 有界来源身份及行为归属

下表完整列本包五个规则文件实际定义身份；只是源定位，合同按主稿成员/队伍/调整/条款组织。空基类及未用例外同样具名，不按存在推导默认可达。

| 文件:行 | 审计身份 | 主合同 |
| --- | --- | --- |
| 001_Challenge_ChallengeRules.rb:4 | `PokemonChallengeRules` | 主稿§2/5 |
| 002_Challenge_Rulesets.rb:4 | `PokemonRuleSet` | 主稿§2/5 |
| 002_Challenge_Rulesets.rb:229 | `StandardRules` | 主稿§2/5 |
| 002_Challenge_Rulesets.rb:244 | `StandardCup` | 主稿§2/5 |
| 002_Challenge_Rulesets.rb:257 | `DoubleCup` | 主稿§2/5 |
| 002_Challenge_Rulesets.rb:270 | `FancyCup` | 主稿§2/5 |
| 002_Challenge_Rulesets.rb:291 | `LittleCup` | 主稿§2/5 |
| 002_Challenge_Rulesets.rb:309 | `LightCup` | 主稿§2/5 |
| 003_Challenge_EntryRestrictions.rb:4 | `StandardRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:27 | `HeightRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:41 | `WeightRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:55 | `NegativeExtendedGameClause` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:70 | `BabyRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:84 | `UnevolvedFormRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:100 | `NicknameChecker` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:126 | `NicknameClause` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:145 | `NonEggRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:154 | `AblePokemonRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:163 | `SpeciesRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:180 | `BannedSpeciesRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:197 | `RestrictedSpeciesRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:219 | `RestrictedSpeciesTeamRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:228 | `RestrictedSpeciesSubsetRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:237 | `SameSpeciesClause` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:254 | `SpeciesClause` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:273 | `MinimumLevelRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:288 | `MaximumLevelRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:303 | `TotalLevelRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:324 | `BannedItemRestriction` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:341 | `ItemsDisallowedClause` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:350 | `SoulDewClause` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:359 | `ItemClause` | 主稿§3 |
| 003_Challenge_EntryRestrictions.rb:378 | `LittleCupRestriction` | 主稿§3 |
| 004_Challenge_LevelAdjustment.rb:4 | `LevelAdjustment` | 主稿§4 |
| 004_Challenge_LevelAdjustment.rb:84 | `FixedLevelAdjustment` | 主稿§4 |
| 004_Challenge_LevelAdjustment.rb:100 | `TotalLevelAdjustment` | 主稿§4 |
| 004_Challenge_LevelAdjustment.rb:132 | `CombinedLevelAdjustment` | 主稿§4 |
| 004_Challenge_LevelAdjustment.rb:153 | `SinglePlayerCappedLevelAdjustment` | 主稿§4 |
| 004_Challenge_LevelAdjustment.rb:162 | `CappedLevelAdjustment` | 主稿§4 |
| 004_Challenge_LevelAdjustment.rb:178 | `LevelBalanceAdjustment` | 主稿§4 |
| 004_Challenge_LevelAdjustment.rb:196 | `EnemyLevelAdjustment` | 主稿§4 |
| 004_Challenge_LevelAdjustment.rb:212 | `OpenLevelAdjustment` | 主稿§4 |
| 005_Challenge_BattleRules.rb:10 | `BattleRule` | 主稿§6 |
| 005_Challenge_BattleRules.rb:17 | `DoubleBattle` | 主稿§6 |
| 005_Challenge_BattleRules.rb:24 | `SingleBattle` | 主稿§6 |
| 005_Challenge_BattleRules.rb:31 | `SoulDewBattleClause` | 主稿§6 |
| 005_Challenge_BattleRules.rb:38 | `SleepClause` | 主稿§6 |
| 005_Challenge_BattleRules.rb:45 | `FreezeClause` | 主稿§6 |
| 005_Challenge_BattleRules.rb:52 | `EvasionClause` | 主稿§6 |
| 005_Challenge_BattleRules.rb:59 | `OHKOClause` | 主稿§6 |
| 005_Challenge_BattleRules.rb:66 | `PerishSongClause` | 主稿§6 |
| 005_Challenge_BattleRules.rb:73 | `SelfKOClause` | 主稿§6 |
| 005_Challenge_BattleRules.rb:80 | `SelfdestructClause` | 主稿§6 |
| 005_Challenge_BattleRules.rb:87 | `SonicBoomClause` | 主稿§6 |
| 005_Challenge_BattleRules.rb:94 | `ModifiedSleepClause` | 主稿§6 |
| 005_Challenge_BattleRules.rb:101 | `SkillSwapClause` | 主稿§6 |

## 5. 条款设置与消费清单

| 字面规则键 | 设置方式 | 真实消费定位 |
| --- | --- | --- |
| souldewclause | 本文件有对应布尔真设置 | ItemEffects:1024–1031/1210–1217；WP50 |
| sleepclause | 本文件有对应布尔真设置 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| freezeclause | 本文件有对应布尔真设置 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| evasionclause | 本文件有对应布尔真设置 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| ohkoclause | 本文件有对应布尔真设置 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| perishsongclause | 本文件有对应布尔真设置 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| selfkoclause | 本文件有对应布尔真设置 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| selfdestructclause | 本文件有对应布尔真设置 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| sonicboomclause | 本文件有对应布尔真设置 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| modifiedsleepclause | 本文件有对应布尔真设置 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| skillswapclause | 本文件有对应布尔真设置 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| drawclause | 本五文件无对应设置包装；作者其它入口可设 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| modifiedselfdestructclause | 本五文件无对应设置包装；作者其它入口可设 | Battle_Clauses:1–306，主稿§6逐条阶段 |
| suddendeath | 本五文件无对应设置包装；作者其它入口可设 | Battle_Clauses:1–306，主稿§6逐条阶段 |

本表不称14条款都默认开启；默认杯只开§1所列集合。WP54-N01的OHKOIce继承别名影响已独立确认，WP46已按授权同步（差异见本轮回应）；真实约束/调整/反馈及数值对照见主稿。设施会话/回放/生成器未完成。

本轮记录：2026-09-28 独立首审PASS_SCOPED后限定Reviewed管理回填（[报告](../../review/wp52b-wp52c-wp54-review-2026-09-28/report.md)§5）；56定义身份、10活动工厂、5直接样本、3模式、14条款键与已述例外不变。被审首稿v1 `b45c976e01251aedc4b445a93efee7bb645c35cdd374bef6e741ab40375a4815`（11,746字节）保留历史，当前新字节不冒充被审对象。
