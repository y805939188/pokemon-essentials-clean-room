# WP52-A 评估覆盖与默认数据附表（净化正文；批次 12）

分类：combat-requirements／pokemon-rules 数据附表；性质：实现独立行为数据。

本附表为净化正文的一部分：按统一交接将批准输入 WP52-A《评估覆盖与默认数据》转写为独立行为数据，不含源文件路径与行号（源定位集中登记于 `../../audit/source-traceability.md` 批次 12 条目）。源名仅审计，不是未来对象结构。注册索引不代替主稿参数、条件和分支。全部内容为静态证据；**无运行确认**（见 `../scope-statement.md`）。

## 1. 有界集合与责任

全 Scripts 登记搜索得到 784 条 add/copy 语句、12 文件；按复制目标展开 786 条登记出现、783 个不同「族＋身份」组合；3 个组合各重复登记一次，均属 B/C 前向（下列计数按出现）。WP52-A 334，WP51 已有 15，WP52-B 前向 247，WP52-C 前向 190；未归属 0。A 含 164 个不同效果身份，以及 22 通用修正和 AbilityRanking 登记。这里的有界全集是当前这些注册，不等于所有未注册的真实效果都已有专用 AI 策略。**其中 B247／C190 为 A 阶段历史定位**：23 条纯数值/恢复/誓约责任后由 C 移入 B，当前 B 270 出现、268 有效键（有限复审 PASS_SCOPED 后限定 Reviewed 回填）、C 167 出现、165 有效直接键（独立首审 PASS_SCOPED，限定 Reviewed 回填），以 B/C 有界附表为准。

共同默认：无失败处理器为假、无效果评分保留输入、无基数处理器保留默认基数、未命中能力评级 0。通用数值消费者在主稿 §2/3；独立真实合同 WP40/43/44/48 及相关效果包。本表只把 B/C 定位到明确包；「均未提取、未自检通过、未启动新包」为 A 阶段历史记法，当前 B/C 已完成首稿并分别处于 2026-09-28 有限复审 PASS_SCOPED 后限定 Reviewed 回填、2026-09-28 独立首审限定通过，状态以各自正文与附表为准。

## 2. 本包具体效果登记

F＝整体失败，T＝目标失败，S＝整体效果分，G＝目标效果分，P＝基数预测；「←X」表示该注册为 copy，沿该族复制 X 的已有行为、仍读取实际本招参数。真实参数/前门按 WP44 附表对应行；源文件与行号见追溯条目。

### 2.1 Misc（主稿 §7）

| 效果身份 | 族 | 主合同 |
| --- | --- | --- |
| DoesNothingCongratulations | S | §7 |
| DoesNothingFailsIfNoAlly | S←DoesNothingCongratulations | §7 |
| DoesNothingUnusableInGravity | S←DoesNothingCongratulations | §7 |
| DoubleMoneyGainedFromBattle | S←DoesNothingCongratulations | §7 |
| FailsIfNotUserFirstTurn | F、S | §7 |
| FailsIfUserHasUnusedMove | F | §7 |
| FailsIfUserNotConsumedBerry | F | §7 |
| FailsUnlessTargetSharesTypeWithUser | T | §7 |

### 2.2 阶级（主稿 §4.1–4.3；参数为使用者/目标变化）

| 效果身份 | 族 | 参数 |
| --- | --- | --- |
| RaiseUserAttack1 | F、S | 攻击 +1 |
| RaiseUserAttack2 | F←RaiseUserAttack1、S←RaiseUserAttack1 | 攻击 +2 |
| RaiseUserAttack2IfTargetFaints | G | — |
| RaiseUserAttack3 | F←RaiseUserAttack1、S←RaiseUserAttack1 | 攻击 +3 |
| RaiseUserAttack3IfTargetFaints | G←RaiseUserAttack2IfTargetFaints | — |
| MaxUserAttackLoseHalfOfTotalHP | F、S | 腹鼓（§4.3） |
| RaiseUserDefense1 | F←RaiseUserAttack1、S←RaiseUserAttack1 | 防御 +1 |
| RaiseUserDefense1CurlUpUser | F←RaiseUserDefense1、S | 变圆（§4.3） |
| RaiseUserDefense2 | F←RaiseUserDefense1、S←RaiseUserDefense1 | 防御 +2 |
| RaiseUserDefense3 | F←RaiseUserDefense1、S←RaiseUserDefense1 | 防御 +3 |
| RaiseUserSpAtk1 | F←RaiseUserAttack1、S←RaiseUserAttack1 | 特攻 +1 |
| RaiseUserSpAtk2 | F←RaiseUserSpAtk1、S←RaiseUserSpAtk1 | 特攻 +2 |
| RaiseUserSpAtk3 | F←RaiseUserSpAtk1、S←RaiseUserSpAtk1 | 特攻 +3 |
| RaiseUserSpDef1 | F←RaiseUserDefense1、S←RaiseUserDefense1 | 特防 +1 |
| RaiseUserSpDef1PowerUpElectricMove | F←RaiseUserSpDef1、S | 充电（§4.3） |
| RaiseUserSpDef2 | F←RaiseUserSpDef1、S←RaiseUserSpDef1 | 特防 +2 |
| RaiseUserSpDef3 | F←RaiseUserSpDef1、S←RaiseUserSpDef1 | 特防 +3 |
| RaiseUserSpeed1 | F←RaiseUserSpDef1、S←RaiseUserSpDef1 | 速度 +1 |
| RaiseUserSpeed2 | F←RaiseUserSpeed1、S←RaiseUserSpeed1 | 速度 +2 |
| RaiseUserSpeed2LowerUserWeight | F←RaiseUserSpeed2、S | 轻量化（§4.3） |
| RaiseUserSpeed3 | F←RaiseUserSpeed1、S←RaiseUserSpeed1 | 速度 +3 |
| RaiseUserAccuracy1 | F←RaiseUserSpeed1、S←RaiseUserSpeed1 | 命中 +1 |
| RaiseUserAccuracy2 | F←RaiseUserAccuracy1、S←RaiseUserAccuracy1 | 命中 +2 |
| RaiseUserAccuracy3 | F←RaiseUserAccuracy1、S←RaiseUserAccuracy1 | 命中 +3 |
| RaiseUserEvasion1 | F←RaiseUserAccuracy1、S←RaiseUserAccuracy1 | 闪避 +1 |
| RaiseUserEvasion2 | F←RaiseUserEvasion1、S←RaiseUserEvasion1 | 闪避 +2 |
| RaiseUserEvasion2MinimizeUser | F←RaiseUserEvasion2、S | 变小（§4.3） |
| RaiseUserEvasion3 | F←RaiseUserEvasion1、S←RaiseUserEvasion1 | 闪避 +3 |
| RaiseUserCriticalHitRate2 | F、S | 聚气（§4.3） |
| RaiseUserAtkDef1 | F、S←RaiseUserAttack1 | 攻击 +1，防御 +1 |
| RaiseUserAtkDefAcc1 | F←RaiseUserAtkDef1、S←RaiseUserAtkDef1 | 攻击 +1，防御 +1，命中 +1 |
| RaiseUserAtkSpAtk1 | F←RaiseUserAtkDef1、S←RaiseUserAtkDef1 | 攻击 +1，特攻 +1 |
| RaiseUserAtkSpAtk1Or2InSun | F←RaiseUserAtkSpAtk1、S | 晴成长（§4.3） |
| LowerUserDefSpDef1RaiseUserAtkSpAtkSpd2 | F、S | 破壳（§4.3） |
| RaiseUserAtkSpd1 | F←RaiseUserAtkSpAtk1、S←RaiseUserAtkSpAtk1 | 攻击 +1，速度 +1 |
| RaiseUserAtk1Spd2 | F←RaiseUserAtkSpAtk1、S←RaiseUserAtkSpAtk1 | 速度 +2，攻击 +1 |
| RaiseUserAtkAcc1 | F←RaiseUserAtkSpAtk1、S←RaiseUserAtkSpAtk1 | 攻击 +1，命中 +1 |
| RaiseUserDefSpDef1 | F←RaiseUserAtkSpAtk1、S←RaiseUserAtkSpAtk1 | 防御 +1，特防 +1 |
| RaiseUserSpAtkSpDef1 | F←RaiseUserAtkSpAtk1、S←RaiseUserAtkSpAtk1 | 特攻 +1，特防 +1 |
| RaiseUserSpAtkSpDefSpd1 | F←RaiseUserAtkSpAtk1、S←RaiseUserAtkSpAtk1 | 特攻 +1，特防 +1，速度 +1 |
| RaiseUserMainStats1 | F←RaiseUserAtkSpAtk1、S←RaiseUserAtkSpAtk1 | 攻击 +1，防御 +1，特攻 +1，特防 +1，速度 +1 |
| RaiseUserMainStats1LoseThirdOfTotalHP | F、S | 五项升且扣 1/3 HP（§4.3） |
| RaiseUserMainStats1TrapUserInBattle | F、S | 背水一战（§4.3） |
| StartRaiseUserAtk1WhenDamaged | S | 愤怒（§4.3） |
| LowerUserAttack1 | S | 攻击 −1 |
| LowerUserAttack2 | S←LowerUserAttack1 | 攻击 −2 |
| LowerUserDefense1 | S←LowerUserAttack1 | 防御 −1 |
| LowerUserDefense2 | S←LowerUserDefense1 | 防御 −2 |
| LowerUserSpAtk1 | S←LowerUserAttack1 | 特攻 −1 |
| LowerUserSpAtk2 | S←LowerUserSpAtk1 | 特攻 −2 |
| LowerUserSpDef1 | S←LowerUserDefense1 | 特防 −1 |
| LowerUserSpDef2 | S←LowerUserSpDef1 | 特防 −2 |
| LowerUserSpeed1 | S←LowerUserAttack1 | 速度 −1 |
| LowerUserSpeed2 | S←LowerUserSpeed1 | 速度 −2 |
| LowerUserAtkDef1 | S←LowerUserAttack1 | 攻击 −1，防御 −1 |
| LowerUserDefSpDef1 | S←LowerUserAttack1 | 防御 −1，特防 −1 |
| LowerUserDefSpDefSpd1 | S←LowerUserAttack1 | 速度 −1，防御 −1，特防 −1 |
| RaiseTargetAttack1 | T、G | — |
| RaiseTargetAttack2ConfuseTarget | T、G | 虚张声势（§4.3） |
| RaiseTargetSpAtk1ConfuseTarget | T、G | 吹捧（§4.3） |
| RaiseTargetSpDef1 | T、G | — |
| RaiseTargetRandomStat2 | T、G | 点穴（§4.3） |
| RaiseTargetAtkSpAtk2 | T、G | 装饰（§4.3） |
| LowerTargetAttack1 | T、G | 攻击 −1 |
| LowerTargetAttack1BypassSubstitute | T←LowerTargetAttack1、G←LowerTargetAttack1 | 攻击 −1 |
| LowerTargetAttack2 | T←LowerTargetAttack1、G←LowerTargetAttack1 | 攻击 −2 |
| LowerTargetAttack3 | T←LowerTargetAttack1、G←LowerTargetAttack1 | 攻击 −3 |
| LowerTargetDefense1 | T←LowerTargetAttack1、G←LowerTargetAttack1 | 防御 −1 |
| LowerTargetDefense1PowersUpInGravity | T←LowerTargetDefense1、G←LowerTargetDefense1、P | 重力降防（§4.3） |
| LowerTargetDefense2 | T←LowerTargetDefense1、G←LowerTargetDefense1 | 防御 −2 |
| LowerTargetDefense3 | T←LowerTargetDefense1、G←LowerTargetDefense1 | 防御 −3 |
| LowerTargetSpAtk1 | T←LowerTargetAttack1、G←LowerTargetAttack1 | 特攻 −1 |
| LowerTargetSpAtk2 | T←LowerTargetSpAtk1、G←LowerTargetSpAtk1 | 特攻 −2 |
| LowerTargetSpAtk2IfCanAttract | T、G←LowerTargetSpAtk2 | 诱惑（§4.3） |
| LowerTargetSpAtk3 | T←LowerTargetSpAtk1、G←LowerTargetSpAtk1 | 特攻 −3 |
| LowerTargetSpDef1 | T←LowerTargetDefense1、G←LowerTargetDefense1 | 特防 −1 |
| LowerTargetSpDef2 | T←LowerTargetSpDef1、G←LowerTargetSpDef1 | 特防 −2 |
| LowerTargetSpDef3 | T←LowerTargetSpDef1、G←LowerTargetSpDef1 | 特防 −3 |
| LowerTargetSpeed1 | T←LowerTargetSpDef1、G←LowerTargetSpDef1 | 速度 −1 |
| LowerTargetSpeed1WeakerInGrassyTerrain | T←LowerTargetSpeed1、G←LowerTargetSpeed1、P | 青草降速（§4.3） |
| LowerTargetSpeed1MakeTargetWeakerToFire | T、G | 沥青（§4.3） |
| LowerTargetSpeed2 | T←LowerTargetSpeed1、G←LowerTargetSpeed1 | 速度 −2 |
| LowerTargetSpeed3 | T←LowerTargetSpeed1、G←LowerTargetSpeed1 | 速度 −3 |
| LowerTargetAccuracy1 | T←LowerTargetSpeed1、G←LowerTargetSpeed1 | 命中 −1 |
| LowerTargetAccuracy2 | T←LowerTargetAccuracy1、G←LowerTargetAccuracy1 | 命中 −2 |
| LowerTargetAccuracy3 | T←LowerTargetAccuracy1、G←LowerTargetAccuracy1 | 命中 −3 |
| LowerTargetEvasion1 | T←LowerTargetAccuracy1、G←LowerTargetAccuracy1 | 闪避 −1 |
| LowerTargetEvasion2 | T←LowerTargetEvasion1、G←LowerTargetEvasion1 | 闪避 −2 |
| LowerTargetEvasion3 | T←LowerTargetEvasion1、G←LowerTargetEvasion1 | 闪避 −3 |
| LowerTargetAtkDef1 | T、G←LowerTargetAttack1 | 攻击 −1，防御 −1 |
| LowerTargetAtkSpAtk1 | T←LowerTargetAtkDef1、G←LowerTargetAtkDef1 | 攻击 −1，特攻 −1 |
| LowerPoisonedTargetAtkSpAtkSpd1 | T、G←LowerTargetAtkSpAtk1 | 毒液陷阱（§4.3） |
| RaiseAlliesAtkDef1 | T、G | 指导（§4.3） |
| RaisePlusMinusUserAndAlliesAtkSpAtk1 | F、T、S、G | 正电（§4.3） |
| RaisePlusMinusUserAndAlliesDefSpDef1 | F、T、S、G | 负电（§4.3） |
| RaiseGroundedGrassBattlersAtkSpAtk1 | T、G | 耕地（§4.3） |
| RaiseGrassBattlersDef1 | T、G | 花盾（§4.3） |
| UserTargetSwapAtkSpAtkStages | G | 阶级交换（§4.3） |
| UserTargetSwapDefSpDefStages | G | 阶级交换（§4.3） |
| UserTargetSwapStatStages | G | 阶级交换（§4.3） |
| UserCopyTargetStatStages | G | 自我暗示（§4.3） |
| UserStealTargetPositiveStatStages | G | 偷正阶（§4.3） |
| InvertTargetStatStages | T、G | 颠倒（§4.3） |
| ResetTargetStatStages | G | 清除（§4.3） |
| ResetAllBattlersStatStages | F、S | 黑雾（§4.3） |
| StartUserSideImmunityToStatStageLowering | F、S | 白雾（§4.3） |
| UserSwapBaseAtkDef | S | 力量戏法（§4.3） |
| UserTargetSwapBaseSpeed | G | 速度互换（§4.3） |
| UserTargetAverageBaseAtkSpAtk | G | 力量平分（§4.3） |
| UserTargetAverageBaseDefSpDef | G | 防守平分（§4.3） |

### 2.3 状态（主稿 §5）

| 效果身份 | 族 | 主合同 |
| --- | --- | --- |
| SleepTarget | T、G | §5 睡 |
| SleepTargetIfUserDarkrai | F、T、G←SleepTarget | §5 暗黑洞 |
| SleepTargetChangeUserMeloettaForm | G←SleepTarget | §5 古老之歌 |
| SleepTargetNextTurn | T、G←SleepTarget | §5 瞌睡 |
| PoisonTarget | T、G | §5 毒 |
| PoisonTargetLowerTargetSpeed1 | T、G | §5 毒降速 |
| BadPoisonTarget | T←PoisonTarget、G←PoisonTarget | §5 剧毒 |
| ParalyzeTarget | T、G | §5 麻 |
| ParalyzeTargetIfNotTypeImmune | T、G←ParalyzeTarget | §5 类型免疫变体 |
| ParalyzeTargetAlwaysHitsInRainHitsTargetInSky | G←ParalyzeTarget | §5 天空变体 |
| ParalyzeFlinchTarget | G | §5 麻+畏缩 |
| BurnTarget | T、G | §5 烧 |
| BurnFlinchTarget | G | §5 烧+畏缩 |
| FreezeTarget | T、G | §5 冻 |
| FreezeTargetSuperEffectiveAgainstWater | G←FreezeTarget | §5 冷冻干燥 |
| FreezeTargetAlwaysHitsInHail | G←FreezeTarget | §5 冰雹变体 |
| FreezeFlinchTarget | G | §5 冻+畏缩 |
| ParalyzeBurnOrFreezeTarget | G | §5 三随机状态 |
| GiveUserStatusToTarget | F、T、G | §5 精神转移 |
| CureUserBurnPoisonParalysis | F、S | §5 自治 |
| CureUserPartyStatus | F、S | §5 全队治 |
| CureTargetBurn | G | §5 治 T 灼伤 |
| StartUserSideImmunityToInflictedStatus | F、S | §5 神秘守护 |
| FlinchTarget | G | §5 畏缩 |
| FlinchTargetFailsIfUserNotAsleep | G←FlinchTarget | §5 畏缩 |
| FlinchTargetFailsIfNotUserFirstTurn | F、G←FlinchTarget | §5 击掌奇袭 |
| FlinchTargetDoublePowerIfTargetInSky | G←FlinchTarget | §5 畏缩（基数交 B） |
| ConfuseTarget | T、G | §5 混乱 |
| ConfuseTargetAlwaysHitsInRainHitsTargetInSky | G←ConfuseTarget | §5 天空变体 |
| AttractTarget | T、G | §5 迷恋 |

### 2.4 类型与能力（主稿 §6）

| 效果身份 | 族 | 主合同 |
| --- | --- | --- |
| SetUserTypesBasedOnEnvironment | F、S | §6 环境变型 |
| SetUserTypesToResistLastAttack | T、G | §6 纹理 2 |
| SetUserTypesToTargetTypes | T | §6 镜面属性 |
| SetUserTypesToUserMoveType | F、G | §6 纹理 |
| SetTargetTypesToPsychic | T、G | §6 改纯超能 |
| SetTargetTypesToWater | T←SetTargetTypesToPsychic、G | §6 改纯水 |
| AddGhostTypeToTarget | T←SetTargetTypesToWater、G | §6 添加幽灵 |
| AddGrassTypeToTarget | T←AddGhostTypeToTarget、G | §6 添加草 |
| UserLosesFireType | F | §6 燃尽 |
| SetTargetAbilityToSimple | T、G | §6 能力操作 |
| SetTargetAbilityToInsomnia | T、G | §6 能力操作 |
| SetUserAbilityToTargetAbility | T、G | §6 扮演 |
| SetTargetAbilityToUserAbility | T、G | §6 传递 |
| UserTargetSwapAbilities | T、G | §6 特性交换 |
| NegateTargetAbility | T、G | §6 胃液 |
| NegateTargetAbilityIfTargetActed | G | §6 核心惩罚 |

## 3. 通用修正与能力评级注册

### 3.1 通用修正 22 项（主稿 §2.2；均为 add）

GeneralMoveAgainstTargetScore：shiny_target、priority_move_against_faster_target、target_can_Magic_Coat_or_Bounce_move、target_can_powder_fire_moves、target_can_make_moves_Electric_and_be_immune、target_semi_invulnerable、predicted_accuracy、predicted_damage、external_flinching_effects、thawing_move_against_frozen_target、trigger_target_ability_or_item_upon_hit、trigger_user_ability_upon_hit、knocking_out_a_destiny_bonder_or_grudger、damaging_a_raging_target、damaging_a_biding_target。

GeneralMoveScore：shadow_moves、thawing_move_when_frozen、any_foe_can_Magic_Coat_or_Bounce_move、any_battler_can_Snatch_move、good_move_for_choice_item、damaging_move_and_either_side_no_reserves、dance_move_against_dancer。

### 3.2 AbilityRanking 23 项（主稿 §6）

add：BLAZE、CUTECHARM、FRIENDGUARD、GALEWINGS、HUGEPOWER、IRONFIST、LIQUIDVOICE、MEGALAUNCHER、OVERGROW、PRANKSTER、PUNKROCK、RECKLESS、ROCKHEAD、RUNAWAY、SANDFORCE、SKILLLINK、STEELWORKER、SWARM、TORRENT、TRIAGE。

copy：RIVALRY←CUTECHARM；HEALER、SYMBOISIS、TELEPATHY←FRIENDGUARD；PUREPOWER←HUGEPOWER。

## 4. 基础能力评级完整表

数据名称按字面保留，包括拼写不同的身份；未列 0。这里是完整默认数据，不是源程序。中等能力依赖见主稿 §6。

| 评级 | 默认身份（源顺序） |
| ---: | --- |
| 10 | DELTASTREAM, DESOLATELAND, HUGEPOWER, MOODY, PARENTALBOND, POWERCONSTRUCT, PRIMORDIALSEA, PUREPOWER, SHADOWTAG, STANCECHANGE, WONDERGUARD |
| 9 | ARENATRAP, DRIZZLE, DROUGHT, IMPOSTER, MAGICBOUNCE, MAGICGUARD, MAGNETPULL, SANDSTREAM, SPEEDBOOST |
| 8 | ADAPTABILITY, AERILATE, CONTRARY, DISGUISE, DRAGONSMAW, ELECTRICSURGE, GALVANIZE, GRASSYSURGE, ILLUSION, LIBERO, MISTYSURGE, MULTISCALE, MULTITYPE, NOGUARD, POISONHEAL, PIXILATE, PRANKSTER, PROTEAN, PSYCHICSURGE, REFRIGERATE, REGENERATOR, RKSSYSTEM, SERENEGRACE, SHADOWSHIELD, SHEERFORCE, SIMPLE, SNOWWARNING, TECHNICIAN, TRANSISTOR, WATERBUBBLE |
| 7 | BEASTBOOST, BULLETPROOF, COMPOUNDEYES, DOWNLOAD, FURCOAT, HUSTLE, ICESCALES, INTIMIDATE, LEVITATE, LIGHTNINGROD, MEGALAUNCHER, MOLDBREAKER, MOXIE, NATURALCURE, SAPSIPPER, SHEDSKIN, SKILLLINK, SOULHEART, STORMDRAIN, TERAVOLT, THICKFAT, TINTEDLENS, TOUGHCLAWS, TRIAGE, TURBOBLAZE, UNBURDEN, VOLTABSORB, WATERABSORB |
| 6 | BATTLEBOND, CHLOROPHYLL, COMATOSE, DARKAURA, DRYSKIN, FAIRYAURA, FILTER, FLASHFIRE, FORECAST, GALEWINGS, GUTS, INFILTRATOR, IRONBARBS, IRONFIST, MIRRORARMOR, MOTORDRIVE, NEUROFORCE, PRISMARMOR, QUEENLYMAJESTY, RECKLESS, ROUGHSKIN, SANDRUSH, SCHOOLING, SCRAPPY, SHIELDSDOWN, SOLIDROCK, STAKEOUT, STAMINA, STEELWORKER, STRONGJAW, STURDY, SWIFTSWIM, TOXICBOOST, TRACE, UNAWARE, VICTORYSTAR |
| 5 | AFTERMATH, AIRLOCK, ANALYTIC, BERSERK, BLAZE, CLOUDNINE, COMPETITIVE, CORROSION, DANCER, DAZZLING, DEFIANT, FLAREBOOST, FLUFFY, GOOEY, HARVEST, HEATPROOF, INNARDSOUT, LIQUIDVOICE, MARVELSCALE, MUMMY, NEUTRALIZINGGAS, OVERCOAT, OVERGROW, PRESSURE, QUICKFEET, ROCKHEAD, SANDSPIT, SHIELDDUST, SLUSHRUSH, SWARM, TANGLINGHAIR, TORRENT |
| 4 | ANGERPOINT, BADDREAMS, CHEEKPOUCH, CLEARBODY, CURSEDBODY, EARLYBIRD, EFFECTSPORE, FLAMEBODY, FLOWERGIFT, FULLMETALBODY, GORILLATACTICS, HYDRATION, ICEFACE, IMMUNITY, INSOMNIA, JUSTIFIED, MERCILESS, PASTELVEIL, POISONPOINT, POISONTOUCH, RIPEN, SANDFORCE, SOUNDPROOF, STATIC, SURGESURFER, SWEETVEIL, SYNCHRONIZE, VITALSPIRIT, WATERCOMPACTION, WATERVEIL, WHITESMOKE, WONDERSKIN |
| 3 | AROMAVEIL, AURABREAK, COTTONDOWN, DAUNTLESSSHIELD, EMERGENCYEXIT, GLUTTONY, GULPMISSLE, HYPERCUTTER, ICEBODY, INTREPIDSWORD, LIMBER, LIQUIDOOZE, LONGREACH, MAGICIAN, OWNTEMPO, PICKPOCKET, RAINDISH, RATTLED, SANDVEIL, SCREENCLEANER, SNIPER, SNOWCLOAK, SOLARPOWER, STEAMENGINE, STICKYHOLD, SUPERLUCK, UNNERVE, WIMPOUT |
| 2 | BATTLEARMOR, COLORCHANGE, CUTECHARM, DAMP, GRASSPELT, HUNGERSWITCH, INNERFOCUS, LEAFGUARD, LIGHTMETAL, MIMICRY, OBLIVIOUS, POWERSPOT, PROPELLORTAIL, PUNKROCK, SHELLARMOR, STALWART, STEADFAST, STEELYSPIRIT, SUCTIONCUPS, TANGLEDFEET, WANDERINGSPIRIT, WEAKARMOR |
| 1 | BIGPECKS, KEENEYE, MAGMAARMOR, PICKUP, RIVALRY, STENCH |
| 0 | ANTICIPATION, ASONECHILLINGNEIGH, ASONEGRIMNEIGH, BALLFETCH, BATTERY, CHILLINGNEIGH, CURIOUSMEDICINE, FLOWERVEIL, FOREWARN, FRIENDGUARD, FRISK, GRIMNEIGH, HEALER, HONEYGATHER, ILLUMINATE, MINUS, PLUS, POWEROFALCHEMY, QUICKDRAW, RECEIVER, RUNAWAY, SYMBIOSIS, TELEPATHY, UNSEENFIST |
| −1 | DEFEATIST, HEAVYMETAL, KLUTZ, NORMALIZE, PERISHBODY, STALL, ZENMODE |
| −2 | SLOWSTART, TRUANT |

共 267 条身份、13 档，无重复。GULPMISSLE／PROPELLORTAIL 按字面；能力修正 copy 为 SYMBOISIS，不能悄悄改成 SYMBIOSIS。

## 5. 已有与前向登记逐项归属

以下按文件＋包＋族分组，列全展开身份；行内包名后的状态词为 A 阶段历史定位（当时未启动），当前 B/C 状态以各自有界附表为准。B/C 只登记边界，不从目录推断行为已完成。相同效果跨族可分责，尤其畏缩的天空双倍基数 B、其状态分 A。

- WP51（已限定通过的回填后版本）／ShouldSwitch：perish_song, significant_eor_damage, cure_status_problem_by_switching_out, wish_healing, yawning, asleep, battler_is_useless, foe_absorbs_all_moves_with_its_ability, absorb_foe_move, sudden_death, high_damage_from_foe
- WP51（已限定通过的回填后版本）／ShouldNotSwitch：lethal_entry_hazards, battler_has_super_effective_move, battler_has_very_raised_stats, battler_is_immune_via_wonder_guard
- WP52-C（A 阶段定位）／ItemRanking：ADAMANTORB, AGUAVBERRY, ASSAULTVEST, BERRYJUICE, BIGROOT, BINDINGBAND, GRIPCLAW, BLACKSLUDGE, CHESTOBERRY, CHOICEBAND, MUSCLEBAND, CHOICESPECS, WISEGLASSES, DEEPSEASCALE, DAMPROCK, DEEPSEATOOTH, ELECTRICSEED, EVIOLITE, FIGYBERRY, FLAMEORB, FULLINCENSE, LAGGINGTAIL, GRASSYSEED, GRISEOUSORB, HEATROCK, IAPAPABERRY, ICYROCK, IRONBALL, KINGSROCK, RAZORFANG, LEEK, STICK, LIGHTBALL, LIGHTCLAY, LUCKYPUNCH, LUSTROUSORB, MAGOBERRY, METALPOWDER, QUICKPOWDER, MISTYSEED, ORANBERRY, POWERHERB, PSYCHICSEED, RINGTARGET, SMOOTHROCK, SOULDEW, TERRAINEXTENDER, THICKCLUB, THROATSPRAY, TOXICORB, WHITEHERB, WIKIBERRY, ZOOMLENS
- WP52-C（A 阶段定位）／Misc 文件各族：MoveFailureAgainstTargetCheck — FailsIfTargetHasNoItem；MoveEffectAgainstTargetScore — FailsIfUserDamagedThisTurn, FailsIfTargetActed；MoveFailureCheck — SwapSideEffects, UserSwapsPositionsWithAlly；MoveEffectScore — SwapSideEffects, RemoveUserBindingAndEntryHazards, UserSwapsPositionsWithAlly, BurnAttackerBeforeUserActs
- WP52-B（A 阶段定位）／Misc 文件各族：MoveEffectAgainstTargetScore — CrashDamageIfFailsUnusableInGravity；MoveFailureCheck — StartSunWeather, StartRainWeather, StartSandstormWeather, StartHailWeather, StartElectricTerrain, StartGrassyTerrain, StartMistyTerrain, StartPsychicTerrain, RemoveTerrain, AddSpikesToFoeSide, AddToxicSpikesToFoeSide, AddStealthRocksToFoeSide, AddStickyWebToFoeSide, UserMakeSubstitute, StartShadowSkyWeather, RemoveAllScreensAndSafeguard；MoveEffectScore — StartSunWeather, StartRainWeather, StartSandstormWeather, StartHailWeather, StartElectricTerrain, StartGrassyTerrain, StartMistyTerrain, StartPsychicTerrain, RemoveTerrain, AddSpikesToFoeSide, AddToxicSpikesToFoeSide, AddStealthRocksToFoeSide, AddStickyWebToFoeSide, UserMakeSubstitute, AttackTwoTurnsLater, AllBattlersLoseHalfHPUserSkipsNextTurn, UserLosesHalfHP, StartShadowSkyWeather, RemoveAllScreensAndSafeguard；MoveFailureAgainstTargetCheck — AttackTwoTurnsLater
- WP52-B（A 阶段定位）／BattlerStats 文件各族：MoveFailureAgainstTargetCheck — LowerTargetEvasion1RemoveSideEffects；MoveEffectAgainstTargetScore — LowerTargetEvasion1RemoveSideEffects, UserTargetAverageHP；MoveFailureCheck — StartUserSideDoubleSpeed；MoveEffectScore — StartUserSideDoubleSpeed, StartSwapAllBattlersBaseDefensiveStats
- WP52-B（A 阶段定位）／BattlerOther 文件各族：MoveBasePower — FlinchTargetDoublePowerIfTargetInSky
- WP52-C（A 阶段定位）／BattlerOther 文件各族：MoveFailureCheck — StartUserAirborne, StartGravity；MoveEffectScore — StartUserAirborne, StartGravity；MoveFailureAgainstTargetCheck — StartTargetAirborneAndAlwaysHitByMoves, TransformUserIntoTarget；MoveEffectAgainstTargetScore — StartTargetAirborneAndAlwaysHitByMoves, HitsTargetInSkyGroundsTarget, TransformUserIntoTarget
- WP52-B（A 阶段定位）／MoveAttributes 文件各族：MoveBasePower — FixedDamage20, FixedDamage40, FixedDamageHalfTargetHP, FixedDamageUserLevel, FixedDamageUserLevelRandom, LowerTargetHPToUserHP, OHKO, OHKOIce, OHKOHitsUndergroundTarget, PowerHigherWithUserHP, PowerLowerWithUserHP, PowerHigherWithTargetHP, PowerHigherWithUserHappiness, PowerLowerWithUserHappiness, PowerHigherWithUserPositiveStatStages, PowerHigherWithTargetPositiveStatStages, PowerHigherWithUserFasterThanTarget, PowerHigherWithTargetFasterThanUser, PowerHigherWithLessPP, PowerHigherWithTargetWeight, PowerHigherWithUserHeavierThanTarget, PowerHigherWithConsecutiveUse, PowerHigherWithConsecutiveUseOnUserSide, RandomPowerDoublePowerIfTargetUnderground, DoublePowerIfTargetHPLessThanHalf, DoublePowerIfUserPoisonedBurnedParalyzed, DoublePowerIfTargetAsleepCureTarget, DoublePowerIfTargetPoisoned, DoublePowerIfTargetParalyzedCureTarget, DoublePowerIfTargetStatusProblem, DoublePowerIfUserHasNoItem, DoublePowerIfTargetUnderwater, DoublePowerIfTargetUnderground, DoublePowerIfTargetInSky, DoublePowerInElectricTerrain, DoublePowerIfUserLastMoveFailed, DoublePowerIfAllyFaintedLastTurn, EffectivenessIncludesFlyingType, TypeDependsOnUserIVs, TypeAndPowerDependOnUserBerry, TypeAndPowerDependOnWeather, TypeAndPowerDependOnTerrain；MoveFailureAgainstTargetCheck — LowerTargetHPToUserHP, OHKO, OHKOIce, OHKOHitsUndergroundTarget, CannotMakeTargetFaint, TargetMovesBecomeElectric；MoveEffectAgainstTargetScore — OHKO, OHKOIce, OHKOHitsUndergroundTarget, DamageTargetAlly, DoublePowerIfTargetAsleepCureTarget, DoublePowerIfTargetParalyzedCureTarget, DoublePowerIfTargetLostHPThisTurn, DoublePowerIfTargetActed, DoublePowerIfTargetNotActed, RemoveProtections, RemoveProtections, HoopaRemoveProtectionsBypassSubstituteLowerUserDef1, RecoilQuarterOfDamageDealt, RecoilThirdOfDamageDealtParalyzeTarget, RecoilThirdOfDamageDealtBurnTarget, RecoilHalfOfDamageDealt, CategoryDependsOnHigherDamagePoisonTarget, EnsureNextMoveAlwaysHits, StartNegateTargetEvasionStatStageAndGhostImmunity, StartNegateTargetEvasionStatStageAndDarkImmunity, TargetMovesBecomeElectric；MoveEffectScore — PowerHigherWithConsecutiveUse, PowerHigherWithConsecutiveUse, DoublePowerIfUserLostHPThisTurn, EnsureNextCriticalHit, StartPreventCriticalHitsAgainstUserSide, UserEnduresFaintingThisTurn, StartWeakenElectricMoves, StartWeakenFireMoves, StartWeakenPhysicalDamageAgainstUserSide, StartWeakenSpecialDamageAgainstUserSide, StartWeakenDamageAgainstUserSideIfHail, RemoveScreens, ProtectUser, ProtectUserBanefulBunker, ProtectUserFromDamagingMovesKingsShield, ProtectUserFromDamagingMovesObstruct, ProtectUserFromTargetingMovesSpikyShield, ProtectUserSideFromDamagingMovesIfUserFirstTurn, ProtectUserSideFromStatusMoves, ProtectUserSideFromPriorityMoves, ProtectUserSideFromMultiTargetDamagingMoves, TypeDependsOnUserMorpekoFormRaiseUserSpeed1, NormalMovesBecomeElectric；MoveFailureCheck — StartPreventCriticalHitsAgainstUserSide, StartWeakenElectricMoves, StartWeakenFireMoves, StartWeakenPhysicalDamageAgainstUserSide, StartWeakenSpecialDamageAgainstUserSide, StartWeakenDamageAgainstUserSideIfHail, ProtectUserSideFromDamagingMovesIfUserFirstTurn, ProtectUserSideFromStatusMoves, ProtectUserSideFromPriorityMoves, ProtectUserSideFromMultiTargetDamagingMoves, HoopaRemoveProtectionsBypassSubstituteLowerUserDef1, EnsureNextMoveAlwaysHits, TypeAndPowerDependOnUserBerry, TypeDependsOnUserMorpekoFormRaiseUserSpeed1
- WP52-B（A 阶段定位）／MultiHit 文件各族：MoveBasePower — HitTwoTimes, HitTwoTimesPoisonTarget, HitTwoTimesFlinchTarget, HitTwoTimesTargetThenTargetAlly, HitThreeTimesPowersUpWithEachHit, HitThreeTimesAlwaysCriticalHit, HitTwoToFiveTimes, HitTwoToFiveTimesOrThreeForAshGreninja, HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1, HitOncePerUserTeamMember, TwoTurnAttackOneTurnInSun, MultiTurnAttackPowersUpEachTurn, MultiTurnAttackBideThenReturnDoubleDamage；MoveEffectAgainstTargetScore — HitTwoTimes, HitTwoTimesPoisonTarget, HitTwoTimesFlinchTarget, HitThreeTimesPowersUpWithEachHit, HitThreeTimesAlwaysCriticalHit, HitTwoToFiveTimes, HitTwoToFiveTimesOrThreeForAshGreninja, HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1, HitOncePerUserTeamMember, TwoTurnAttack, TwoTurnAttackOneTurnInSun, TwoTurnAttackParalyzeTarget, TwoTurnAttackBurnTarget, TwoTurnAttackFlinchTarget, TwoTurnAttackRaiseUserSpAtkSpDefSpd2, TwoTurnAttackChargeRaiseUserDefense1, TwoTurnAttackChargeRaiseUserSpAtk1, TwoTurnAttackInvulnerableUnderground, TwoTurnAttackInvulnerableUnderwater, TwoTurnAttackInvulnerableInSky, TwoTurnAttackInvulnerableInSkyParalyzeTarget, TwoTurnAttackInvulnerableInSkyTargetCannotAct, TwoTurnAttackInvulnerableRemoveProtections；MoveFailureCheck — HitOncePerUserTeamMember, TwoTurnAttackRaiseUserSpAtkSpDefSpd2；MoveEffectScore — AttackAndSkipNextTurn, MultiTurnAttackBideThenReturnDoubleDamage；MoveFailureAgainstTargetCheck — TwoTurnAttackInvulnerableInSkyTargetCannotAct
- WP52-B（A 阶段定位）／Healing 文件各族：MoveFailureCheck — HealUserFullyAndFallAsleep, HealUserHalfOfTotalHP, HealUserDependingOnWeather, HealUserDependingOnSandstorm, HealUserHalfOfTotalHPLoseFlyingTypeThisTurn, HealUserPositionNextTurn, StartHealUserEachTurn, StartHealUserEachTurnTrapUserInBattle, UserLosesHalfOfTotalHPExplosive, UserFaintsExplosive, UserFaintsPowersUpInMistyTerrainExplosive, UserFaintsHealAndCureReplacement, UserFaintsHealAndCureReplacementRestorePP, AttackerFaintsIfUserFaints；MoveEffectScore — HealUserFullyAndFallAsleep, HealUserHalfOfTotalHP, HealUserDependingOnWeather, HealUserDependingOnSandstorm, HealUserHalfOfTotalHPLoseFlyingTypeThisTurn, HealUserPositionNextTurn, StartHealUserEachTurn, StartHealUserEachTurnTrapUserInBattle, UserLosesHalfOfTotalHP, UserLosesHalfOfTotalHPExplosive, UserFaintsExplosive, UserFaintsPowersUpInMistyTerrainExplosive, UserFaintsFixedDamageUserHP, UserFaintsHealAndCureReplacement, UserFaintsHealAndCureReplacementRestorePP, StartPerishCountsForAllBattlers, AttackerFaintsIfUserFaints, SetAttackerMovePPTo0IfUserFaints；MoveFailureAgainstTargetCheck — CureTargetStatusHealUserHalfOfTotalHP, HealUserByTargetAttackLowerTargetAttack1, HealUserByHalfOfDamageDoneIfTargetAsleep, HealUserAndAlliesQuarterOfTotalHP, HealUserAndAlliesQuarterOfTotalHPCureStatus, HealTargetHalfOfTotalHP, HealTargetDependingOnGrassyTerrain, StartDamageTargetEachTurnIfTargetAsleep, StartLeechSeedTarget, StartPerishCountsForAllBattlers；MoveEffectAgainstTargetScore — CureTargetStatusHealUserHalfOfTotalHP, HealUserByTargetAttackLowerTargetAttack1, HealUserByHalfOfDamageDone, HealUserByHalfOfDamageDoneIfTargetAsleep, HealUserByThreeQuartersOfDamageDone, HealUserAndAlliesQuarterOfTotalHP, HealUserAndAlliesQuarterOfTotalHPCureStatus, HealTargetHalfOfTotalHP, HealTargetDependingOnGrassyTerrain, StartDamageTargetEachTurnIfTargetAsleep, StartLeechSeedTarget, UserFaintsLowerTargetAtkSpAtk2；MoveBasePower — UserFaintsPowersUpInMistyTerrainExplosive, UserFaintsFixedDamageUserHP
- WP52-C（A 阶段定位）／Items 文件各族：MoveEffectAgainstTargetScore — UserTakesTargetItem, TargetTakesUserItem, UserTargetSwapItems, RemoveTargetItem, DestroyTargetBerryOrGem, CorrodeTargetItem, StartTargetCannotUseItem, AllBattlersConsumeBerry, UserConsumeTargetBerry, ThrowUserItemAtTarget；MoveFailureAgainstTargetCheck — TargetTakesUserItem, UserTargetSwapItems, CorrodeTargetItem, StartTargetCannotUseItem, AllBattlersConsumeBerry；MoveFailureCheck — RestoreUserConsumedItem, UserConsumeBerryRaiseDefense2, ThrowUserItemAtTarget；MoveEffectScore — RestoreUserConsumedItem, StartNegateHeldItems, UserConsumeBerryRaiseDefense2；MoveBasePower — RemoveTargetItem, ThrowUserItemAtTarget
- WP52-C（A 阶段定位）／ChangeMoveEffect 文件各族：MoveEffectScore — RedirectAllMovesToUser, RandomlyDamageOrHealTarget, CurseTargetOrLowerUserSpd1RaiseUserAtkDef1, DoublePowerAfterFusionFlare, DoublePowerAfterFusionBolt, CounterPhysicalDamage, CounterSpecialDamage, CounterDamagePlusHalf, UserAddStockpileRaiseDefSpDef1, PowerDependsOnUserStockpile, HealUserDependingOnUserStockpile, GrassPledge, FirePledge, WaterPledge, BounceBackProblemCausingStatusMoves, StealAndUseBeneficialStatusMove, ReplaceMoveWithTargetLastMoveUsed；MoveEffectAgainstTargetScore — RedirectAllMovesToTarget, HealAllyOrDamageFoe, CurseTargetOrLowerUserSpd1RaiseUserAtkDef1, EffectDependsOnEnvironment, TargetNextFireMoveDamagesTarget, PowerUpAllyMove, UseMoveTargetIsAboutToUse, ReplaceMoveThisBattleWithTargetLastMoveUsed；MoveBasePower — RandomlyDamageOrHealTarget, HitsAllFoesAndPowersUpInPsychicTerrain, CounterPhysicalDamage, CounterSpecialDamage, CounterDamagePlusHalf, PowerDependsOnUserStockpile；MoveFailureAgainstTargetCheck — HealAllyOrDamageFoe, CurseTargetOrLowerUserSpd1RaiseUserAtkDef1, TargetNextFireMoveDamagesTarget, PowerUpAllyMove, UseLastMoveUsedByTarget, UseMoveTargetIsAboutToUse, ReplaceMoveThisBattleWithTargetLastMoveUsed, ReplaceMoveWithTargetLastMoveUsed；MoveFailureCheck — CurseTargetOrLowerUserSpd1RaiseUserAtkDef1, UserAddStockpileRaiseDefSpDef1, PowerDependsOnUserStockpile, HealUserDependingOnUserStockpile, UseLastMoveUsed, UseRandomMoveFromUserParty, UseRandomUserMoveIfAsleep, ReplaceMoveThisBattleWithTargetLastMoveUsed
- WP52-C（A 阶段定位）／SwitchingActing 文件各族：MoveFailureCheck — FleeFromBattle, SwitchOutUserStatusMove, SwitchOutUserPassOnEffects, TrapAllBattlersInBattleForOneTurn, UsedAfterUserTakesPhysicalDamage, DisableTargetMovesKnownByUser；MoveEffectScore — FleeFromBattle, SwitchOutUserStatusMove, SwitchOutUserDamagingMove, SwitchOutUserPassOnEffects, TrapAllBattlersInBattleForOneTurn, UsedAfterUserTakesPhysicalDamage, UsedAfterAllyRoundWithDoublePower, StartSlowerBattlersActFirst；MoveFailureAgainstTargetCheck — LowerTargetAtkSpAtk1SwitchOutUser, SwitchOutTargetStatusMove, TrapTargetInBattle, TrapTargetInBattleMainEffect, TrapTargetInBattleLowerTargetDefSpDef1EachTurn, TargetUsesItsLastUsedMoveAgain, LowerPPOfTargetLastMoveBy4, DisableTargetLastMoveUsed, DisableTargetUsingSameMoveConsecutively, DisableTargetUsingDifferentMove, DisableTargetStatusMoves, DisableTargetHealingMoves；MoveEffectAgainstTargetScore — LowerTargetAtkSpAtk1SwitchOutUser, LowerTargetAtkSpAtk1SwitchOutUser, SwitchOutTargetStatusMove, SwitchOutTargetDamagingMove, BindTarget, BindTargetDoublePowerIfTargetUnderwater, TrapTargetInBattle, TrapTargetInBattleMainEffect, TrapTargetInBattleLowerTargetDefSpDef1EachTurn, TrapUserAndTargetInBattle, TargetActsNext, TargetActsLast, TargetUsesItsLastUsedMoveAgain, LowerPPOfTargetLastMoveBy3, LowerPPOfTargetLastMoveBy4, DisableTargetLastMoveUsed, DisableTargetUsingSameMoveConsecutively, DisableTargetUsingDifferentMove, DisableTargetStatusMoves, DisableTargetHealingMoves, DisableTargetSoundMoves, DisableTargetMovesKnownByUser；MoveBasePower — BindTargetDoublePowerIfTargetUnderwater

## 6. 重复登记定点

MoveAttributes:220/238 的 MoveEffectScore PowerHigherWithConsecutiveUse、:1175/1190 的 MoveEffectAgainstTargetScore RemoveProtections，及 SwitchingActing:104/109 的 MoveEffectAgainstTargetScore LowerTargetAtkSpAtk1SwitchOutUser。前两组交 B、后一组交 C，后续须按真实覆盖顺序核行为，不把两次加法并用；本附表不宣称已完成这些规则。

附表没有无名未归属注册；真实效果没有专用 AI 登记时只能适用通用默认，不能因此称其不存在。WP52-B/C 完成后须回查跨族共用数据与通用消费；全局覆盖出口 WP79 保留。
