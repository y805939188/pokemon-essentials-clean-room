# 有界效果归属与数据对应（净化附表；批次 7）

本附表是 [wp44-statuses-stat-stages-and-immunities](wp44-statuses-stat-stages-and-immunities.md) 的附件：有界身份归属与对应已述规则；114／31／23 审计身份及 K01–K22 合同连接。主行为见主稿。审计身份仅为不透明数据标识，不是未来架构建议。源行号定位见 `../../../audit/source-traceability.md` 本包条目。

## 1. 范围和核对方法

固定源为阶级效果文件：全文结构清点 114 个效果标识，67 个纯参数段读取常量数据，47 个其它行为段逐段阅读。下表 114 行各有归属；「前向」不是该效果已完成，也不把它当未发现。行为族共享边界向量不是为每个名称重新运行一个程序。

其中 106 项含本包阶级或附带标记合同（含除雾的阶级部分，其清理范围归场域规格）；3 项建立侧/全场效果归场域规格；4 项原能力值变更归招式变更规格；1 项 HP 平均归《多次攻击、特殊伤害与恢复》。主归属计数 106＋3＋4＋1＝114，共享责任不再计为新增效果。

## 2. 阶级效果 114 项归属表

### 2.1 基本/多项族（WP44 §5、§7；验收 G01/G02/G03/G06）

普通参数共 **65 项**，下表把审计身份、对象和请求序列分别列出。箭头表示实际请求先后，不能按身份的拼写顺序推断；请求量不是保证变化量。每项均接主稿 §5 的查询、提交、夹限、反馈及部分成功规则。两项普通多目标下降参数在 §2.4，未并入本表。

| 审计身份 | 对象 | 按顺序请求的阶级变化 |
| --- | --- | --- |
| `RaiseUserAttack1` | 使用者 | 攻击＋1 |
| `RaiseUserAttack2` | 使用者 | 攻击＋2 |
| `RaiseUserAttack3` | 使用者 | 攻击＋3 |
| `RaiseUserDefense1` | 使用者 | 防御＋1 |
| `RaiseUserDefense2` | 使用者 | 防御＋2 |
| `RaiseUserDefense3` | 使用者 | 防御＋3 |
| `RaiseUserSpAtk1` | 使用者 | 特攻＋1 |
| `RaiseUserSpAtk2` | 使用者 | 特攻＋2 |
| `RaiseUserSpAtk3` | 使用者 | 特攻＋3 |
| `RaiseUserSpDef1` | 使用者 | 特防＋1 |
| `RaiseUserSpDef2` | 使用者 | 特防＋2 |
| `RaiseUserSpDef3` | 使用者 | 特防＋3 |
| `RaiseUserSpeed1` | 使用者 | 速度＋1 |
| `RaiseUserSpeed2` | 使用者 | 速度＋2 |
| `RaiseUserSpeed3` | 使用者 | 速度＋3 |
| `RaiseUserAccuracy1` | 使用者 | 命中＋1 |
| `RaiseUserAccuracy2` | 使用者 | 命中＋2 |
| `RaiseUserAccuracy3` | 使用者 | 命中＋3 |
| `RaiseUserEvasion1` | 使用者 | 闪避＋1 |
| `RaiseUserEvasion2` | 使用者 | 闪避＋2 |
| `RaiseUserEvasion3` | 使用者 | 闪避＋3 |
| `RaiseUserAtkDef1` | 使用者 | 攻击＋1 → 防御＋1 |
| `RaiseUserAtkDefAcc1` | 使用者 | 攻击＋1 → 防御＋1 → 命中＋1 |
| `RaiseUserAtkSpAtk1` | 使用者 | 攻击＋1 → 特攻＋1 |
| `RaiseUserAtkSpd1` | 使用者 | 攻击＋1 → 速度＋1 |
| `RaiseUserAtk1Spd2` | 使用者 | 速度＋2 → 攻击＋1 |
| `RaiseUserAtkAcc1` | 使用者 | 攻击＋1 → 命中＋1 |
| `RaiseUserDefSpDef1` | 使用者 | 防御＋1 → 特防＋1 |
| `RaiseUserSpAtkSpDef1` | 使用者 | 特攻＋1 → 特防＋1 |
| `RaiseUserSpAtkSpDefSpd1` | 使用者 | 特攻＋1 → 特防＋1 → 速度＋1 |
| `RaiseUserMainStats1` | 使用者 | 攻击＋1 → 防御＋1 → 特攻＋1 → 特防＋1 → 速度＋1 |
| `LowerUserAttack1` | 使用者 | 攻击−1 |
| `LowerUserAttack2` | 使用者 | 攻击−2 |
| `LowerUserDefense1` | 使用者 | 防御−1 |
| `LowerUserDefense2` | 使用者 | 防御−2 |
| `LowerUserSpAtk1` | 使用者 | 特攻−1 |
| `LowerUserSpAtk2` | 使用者 | 特攻−2 |
| `LowerUserSpDef1` | 使用者 | 特防−1 |
| `LowerUserSpDef2` | 使用者 | 特防−2 |
| `LowerUserSpeed1` | 使用者 | 速度−1 |
| `LowerUserSpeed2` | 使用者 | 速度−2 |
| `LowerUserAtkDef1` | 使用者 | 攻击−1 → 防御−1 |
| `LowerUserDefSpDef1` | 使用者 | 防御−1 → 特防−1 |
| `LowerUserDefSpDefSpd1` | 使用者 | 速度−1 → 防御−1 → 特防−1 |
| `LowerTargetAttack1` | 目标 | 攻击−1 |
| `LowerTargetAttack2` | 目标 | 攻击−2 |
| `LowerTargetAttack3` | 目标 | 攻击−3 |
| `LowerTargetDefense1` | 目标 | 防御−1 |
| `LowerTargetDefense2` | 目标 | 防御−2 |
| `LowerTargetDefense3` | 目标 | 防御−3 |
| `LowerTargetSpAtk1` | 目标 | 特攻−1 |
| `LowerTargetSpAtk2` | 目标 | 特攻−2 |
| `LowerTargetSpAtk3` | 目标 | 特攻−3 |
| `LowerTargetSpDef1` | 目标 | 特防−1 |
| `LowerTargetSpDef2` | 目标 | 特防−2 |
| `LowerTargetSpDef3` | 目标 | 特防−3 |
| `LowerTargetSpeed1` | 目标 | 速度−1 |
| `LowerTargetSpeed2` | 目标 | 速度−2 |
| `LowerTargetSpeed3` | 目标 | 速度−3 |
| `LowerTargetAccuracy1` | 目标 | 命中−1 |
| `LowerTargetAccuracy2` | 目标 | 命中−2 |
| `LowerTargetAccuracy3` | 目标 | 命中−3 |
| `LowerTargetEvasion1` | 目标 | 闪避−1 |
| `LowerTargetEvasion2` | 目标 | 闪避−2 |
| `LowerTargetEvasion3` | 目标 | 闪避−3 |

自身多项上升先判断至少一项可升，再依序查询和提交各项；单项受限不回滚已成功项目。自身下降在实际伤害后的附效阶段进入，若对侧已无存活成员则整组略过。目标单项下降分别沿变化招目标检查或伤害附效的资格与替身门。实际升降提示按中央规则给出，不能把数据描述顺序当作提示顺序。

### 2.2 具名复合/直接重写族（WP44 §7）

| 源效果标识（审计） | 行为提要 | 验收关联 |
| --- | --- | --- |
| `RaiseUserAttack2IfTargetFaints` | 击倒记录成立后升攻击＋2 | 击倒/未击倒，G01 上限 |
| `RaiseUserAttack3IfTargetFaints` | 击倒记录成立后升攻击＋3 | 击倒/未击倒，G01 上限 |
| `MaxUserAttackLoseHalfOfTotalHP` | HP 代价后直接设攻击极值 | G10 |
| `RaiseUserMainStats1LoseThirdOfTotalHP` | 五项上升并付 1/3 总 HP 代价 | G06/G10 |
| `RaiseTargetAttack2ConfuseTarget` | 目标增强与混乱分别查询并部分成功 | G11/V06 |
| `RaiseTargetSpAtk1ConfuseTarget` | 目标增强与混乱分别查询并部分成功 | G11/V06 |
| `RaiseTargetRandomStat2` | 从资格通过的七阶级集合随机升 2 | G12 |
| `UserTargetSwapAtkSpAtkStages` | 直接交换攻与特攻阶级；方向标记各自更新 | G07/G08 |
| `UserTargetSwapDefSpDefStages` | 直接交换双防阶级；方向标记各自更新 | G07/G08 |
| `UserTargetSwapStatStages` | 直接交换全七项阶级；方向标记各自更新 | G07/G08 |
| `UserCopyTargetStatStages` | 直接复制七阶级；方向标记各自更新 | G07/G08 |
| `UserStealTargetPositiveStatStages` | 计算伤害前夺正阶级；目标归零不以用户接收成功为条件 | G08 |
| `InvertTargetStatStages` | 直接反转阶级（逐项取相反数）；方向标记各自更新 | G07/G08 |
| `ResetTargetStatStages` | 直接归零目标阶级；方向标记各自更新 | G07/G08 |
| `ResetAllBattlersStatStages` | 直接归零全场阶级；方向标记各自更新 | G07/G08 |

### 2.3 K01–K22 复杂项（WP44 §7.1 主规则，对象/条件/入口分支在主稿完整给出）

| 源效果标识（审计） | 行为提要 | 主规则/验收 |
| --- | --- | --- |
| `RaiseUserDefense1CurlUpUser` | 蜷缩并升防：防御＋1；通用效果先设蜷缩标记，再执行该阶段的自身上升 | K01；G01/G06 |
| `RaiseUserSpDef1PowerUpElectricMove` | 充电并升特防：先把充电计数设 2，再请求特防＋1；电招威力消费引用《战斗类型、命中与伤害计算》 | K02；G01/G14 |
| `RaiseUserSpeed2LowerUserWeight` | 身体轻量化：速度＋2；先比较「当前重量查询结果＋已存重量变化」是否大于 1，是则已存重量变化再减 1000 参考重量单位并反馈，然后进入自身升速 | K03；G01/G06 |
| `RaiseUserEvasion2MinimizeUser` | 变小并升闪避：先设置变小标记，再请求闪避＋2；踩踏计算引用《战斗类型、命中与伤害计算》 | K04；G01/G03 |
| `RaiseUserCriticalHitRate2` | 聚气：聚气记录直接设 2，属于会心输入，不是七阶级中某项＋2 | K05；G14 |
| `RaiseUserAtkSpAtk1Or2InSun` | 成长：攻击→特攻依序请求各＋1；使用开始阶段若用户有效天气为晴/大日照，本次两项请求都改＋2 | K06；G06 |
| `RaiseUserMainStats1TrapUserInBattle` | 背水一战：攻击→防御→特攻→特防→速度，各请求＋1；随后仅当当时拘束聚合查询为假才设置背水一战标记 | K07；G06 |
| `StartRaiseUserAtk1WhenDamaged` | 愤怒记录：建立时只置愤怒真，不立即升阶；后续命中反馈中，愤怒者存活且可升攻击时请求攻击＋1 | K08；G01 |
| `RaiseTargetAttack1` | 目标升攻击：目标攻击＋1 | K09；G01/G06 |
| `RaiseTargetSpDef1` | 目标升特防：特防＋1；招式明确忽略替身 | K10；G01 |
| `RaiseTargetAtkSpAtk2` | 装饰式双攻增强：每个目标先攻击＋2，再特攻＋2 | K11；G06 |
| `LowerTargetAttack1BypassSubstitute` | 忽略替身降攻击：攻击−1；相比普通攻击−1 族，明确允许招式忽略替身 | K12；J03 |
| `LowerTargetDefense1PowersUpInGravity` | 重力增强降防：防御−1；重力计数 >0 时，在招式基底威力输入阶段把整数威力乘 3/2 并取整数下界，81→121；重力不生效则保留原值 | K13；J01 |
| `LowerTargetSpAtk2IfCanAttract` | 诱惑式降特攻：特攻−2 | K14；G05 |
| `LowerTargetSpeed1WeakerInGrassyTerrain` | 青草削弱降速：速度−1；当前存储场地为青草时，在本招基底威力阶段减半并四舍五入（正值恰半向上），61→31；否则保留原值 | K15；J02 |
| `LowerTargetSpeed1MakeTargetWeakerToFire` | 沥青射击：先进入速度−1 的普通单项提交；之后目标尚无沥青标记时置真，使后续火相性乘 2，不叠加标记 | K16；G05/G01 |
| `LowerUserDefSpDef1RaiseUserAtkSpAtkSpd2` | 破壳：精确提交顺序：防御−1 → 特防−1 → 攻击＋2 → 特攻＋2 → 速度＋2 | K17；J04/G06 |
| `RaiseAlliesAtkDef1` | 同侧盟友攻防增强：每个有效目标攻击＋1 → 防御＋1 | K18；J05/G06 |
| `RaisePlusMinusUserAndAlliesAtkSpAtk1` | 正负电双攻增强：每个有效目标攻击＋1 → 特攻＋1 | K19；J05/J06/G06 |
| `RaisePlusMinusUserAndAlliesDefSpDef1` | 正负电双防增强：每个有效目标防御＋1 → 特防＋1 | K20；J05/J06/G06 |
| `RaiseGroundedGrassBattlersAtkSpAtk1` | 耕地式草成员增强：每个有效目标攻击＋1 → 特攻＋1 | K21；J07/G06 |
| `RaiseGrassBattlersDef1` | 鲜花防守式草成员增强：防御＋1 | K22；J07/G01 |

### 2.4 多项镜甲预检族（WP44 §5.3；模式破坏者不关闭本层，中央反射另判）

| 源效果标识（审计） | 行为提要 | 验收 |
| --- | --- | --- |
| `LowerTargetAtkDef1` | 目标：攻击−1，防御−1 | M01–M03；原参数及有界目标资格保留 |
| `LowerTargetAtkSpAtk1` | 目标：攻击−1，特攻−1 | M01–M03；同上 |
| `LowerPoisonedTargetAtkSpAtkSpd1` | 毒目标集合与多项下降；镜甲来源资格另核 | M01–M03；同上 |

### 2.5 域外归属项（已定位，归属清楚，不冒称本包已覆盖完整招式）

| 源效果标识（审计） | 行为提要 | 负责范围 |
| --- | --- | --- |
| `LowerTargetEvasion1RemoveSideEffects` | 降闪避与清理独立，清理可使招式在不能降时仍可行 | 阶级部分归本包；清理范围与期限归场域规格（除雾对照 G05/G06） |
| `StartUserSideImmunityToStatStageLowering` | 侧保护建立 | 场域规格主规则；本包查询或数值交界 |
| `UserSwapBaseAtkDef` | 战斗原能力值交换，非阶级 | 招式变更规格；本包读取输入引用《战斗类型、命中与伤害计算》（本轮仅定位，不声称验收整招） |
| `UserTargetSwapBaseSpeed` | 战斗原能力值交换，非阶级 | 同上 |
| `UserTargetAverageBaseAtkSpAtk` | 战斗原能力值平均，非阶级 | 同上 |
| `UserTargetAverageBaseDefSpDef` | 战斗原能力值平均，非阶级 | 同上 |
| `UserTargetAverageHP` | 双方 HP 均分与各自上限，非阶级 | [《多次攻击、特殊伤害与恢复》§6.4](wp46-damage-multihit-and-healing.md#64-hp-均分)；接收合同与覆盖表 §1.7 |
| `StartUserSideDoubleSpeed` | 顺风建立 | 场域规格主规则；本包查询或数值交界 |
| `StartSwapAllBattlersBaseDefensiveStats` | 奇妙空间建立 | 场域规格主规则；本包查询或数值交界 |

## 3. 状态文件的有界目录（31 项）

状态效果文件的状态段含 31 项，逐段读取；计算替代（天气命中、特殊相性）引用《战斗类型、命中与伤害计算》，完整变身/动作引用其负责包。

| 源标识 | 主归属 |
| --- | --- |
| `SleepTarget`、`SleepTargetIfUserDarkrai`、`SleepTargetChangeUserMeloettaForm`、`SleepTargetNextTurn`、`PoisonTarget`、`PoisonTargetLowerTargetSpeed1`、`BadPoisonTarget`、`ParalyzeTarget`、`ParalyzeTargetIfNotTypeImmune`、`ParalyzeTargetAlwaysHitsInRainHitsTargetInSky`、`ParalyzeFlinchTarget`、`BurnTarget`、`BurnTargetIfTargetStatsRaisedThisTurn`、`BurnFlinchTarget`、`FreezeTarget`、`FreezeTargetSuperEffectiveAgainstWater`、`FreezeTargetAlwaysHitsInHail`、`FreezeFlinchTarget`、`ParalyzeBurnOrFreezeTarget`、`GiveUserStatusToTarget`、`CureUserBurnPoisonParalysis`、`CureUserPartyStatus`、`CureTargetBurn`、`FlinchTarget`、`FlinchTargetFailsIfUserNotAsleep`、`FlinchTargetFailsIfNotUserFirstTurn`、`FlinchTargetDoublePowerIfTargetInSky`、`ConfuseTarget`、`ConfuseTargetAlwaysHitsInRainHitsTargetInSky`、`AttractTarget` | WP44 §3–6（状态/附带入口） |
| `StartUserSideImmunityToInflictedStatus` | 场域规格侧保护建立/期限；WP44 免疫查询 |

余下标识已定位，**不因与状态同文件而算作本包完成**：`SetUserTypesBasedOnEnvironment`、`SetUserTypesToResistLastAttack`、`SetUserTypesToTargetTypes`、`SetUserTypesToUserMoveType`、`SetTargetTypesToPsychic`、`SetTargetTypesToWater`、`AddGhostTypeToTarget`、`AddGrassTypeToTarget`、`UserLosesFireType`、`SetTargetAbilityToSimple`、`SetTargetAbilityToInsomnia`、`SetUserAbilityToTargetAbility`、`SetTargetAbilityToUserAbility`、`UserTargetSwapAbilities`、`NegateTargetAbility`、`NegateTargetAbilityIfTargetActed`、`IgnoreTargetAbility`、`StartUserAirborne`、`StartTargetAirborneAndAlwaysHitByMoves`、`HitsTargetInSky`、`HitsTargetInSkyGroundsTarget`、`TransformUserIntoTarget`（以上 21 项：类型/特性/浮空/变身完整族，归招式变更规格；WP43/44 只引用实际输入/守卫）；`StartGravity`（重力，归场域规格；WP43/44 有效查询消费）。

## 4. 当前数据样本（文本数据确认）

每条只记录用于与效果身份核对的字段，未执行编译器或生成器；显示描述不是行为证据。

| 数据 ID | 类型/类别 | 效果标识 |
| --- | --- | --- |
| SWORDSDANCE | NORMAL／Status | `RaiseUserAttack2` |
| GROWL | NORMAL／Status | `LowerTargetAttack1` |
| BELLYDRUM | NORMAL／Status | `MaxUserAttackLoseHalfOfTotalHP` |
| SHELLSMASH | NORMAL／Status | `LowerUserDefSpDef1RaiseUserAtkSpAtkSpd2` |
| SWAGGER | NORMAL／Status | `RaiseTargetAttack2ConfuseTarget` |
| TOPSYTURVY | DARK／Status | `InvertTargetStatStages` |
| HAZE | ICE／Status | `ResetAllBattlersStatStages` |
| PSYCHUP | NORMAL／Status | `UserCopyTargetStatStages` |
| TOXIC | POISON／Status | `BadPoisonTarget` |
| YAWN | NORMAL／Status | `SleepTargetNextTurn` |
| REST | PSYCHIC／Status | `HealUserFullyAndFallAsleep` |
| ATTRACT | NORMAL／Status | `AttractTarget` |

状态与阶级全局名录来自已读 Status/能力项数据定义；阶段型特性/道具的完整效果目录由《特性参与计算、免疫与有效性》、阶段触发规格、《持有物计算、触发与消耗》继续提取。此表只给本包实际范围与负责包，不能据此宣称所有域外功能已经实现或验证。
