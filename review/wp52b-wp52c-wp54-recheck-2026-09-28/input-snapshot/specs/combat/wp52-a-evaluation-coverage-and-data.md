# WP52-A 评估覆盖与默认数据 v2（WP51状态传播）

状态：**Reviewed（限定静态范围，2026-09-28有限复审PASS_SCOPED；管理性回填）**；范围随[主稿](wp52-a-generic-numerical-and-status-evaluation.md)A～F的有界目录与具名数据。源名仅审计，不是未来对象结构。注册索引不代替主稿参数、条件和分支。

## 1. 有界集合与责任

全Scripts登记搜索得到784条add／copy语句、12文件；按复制目标展开786条登记出现、783个不同“族＋身份”组合；3个组合各重复登记一次，均属B/C前向（下列计数按出现）。WP52-A 334，WP51已有15，WP52-B前向247，WP52-C前向190；未归属0。A含164个不同效果身份，以及22通用修正和AbilityRanking登记。这里的有界全集是当前这些注册，不等于所有未注册的真实效果都已有专用AI策略。**其中B247／C190为A阶段历史定位**：23条纯数值／恢复／誓约责任后由C移入B，当前B 270出现、268有效键（有限修订v2，R01待有限复审）、C 167出现、165有效直接键（2026-09-28独立首审PASS_SCOPED，限定Reviewed回填），以B／C有界附表为准。

共同默认：无失败处理器为假、无效果评分保留输入、无基数处理器保留默认基数、未命中能力评级0。通用数值消费者在主稿§2/3；独立真实合同WP40/43/44/48及相关效果包。本表只把B/C定位到明确包；“均未提取、未自检通过、未启动新包”为A阶段历史记法，当前B／C已完成首稿并分别处于R01待有限复审、2026-09-28限定通过，状态以各自正文与附表为准。

## 2. 本包具体效果登记

F＝整体失败，T＝目标失败，S＝整体效果分，G＝目标效果分，P＝基数预测。行号位于`011_Battle/006_AI MoveEffects/`下文件；每个注册若为copy，沿该族复制已有行为、仍读取实际本招参数。

| 效果身份 | 族／行号 | 文件 | 主合同与参数责任 |
| --- | --- | --- | --- |
| `DoesNothingCongratulations` | S:9 | 001_AI_MoveEffects_Misc.rb | 主稿§7 |
| `DoesNothingFailsIfNoAlly` | S:18←DoesNothingCongratulations | 001_AI_MoveEffects_Misc.rb | 主稿§7 |
| `DoesNothingUnusableInGravity` | S:24←DoesNothingCongratulations | 001_AI_MoveEffects_Misc.rb | 主稿§7 |
| `DoubleMoneyGainedFromBattle` | S:35←DoesNothingCongratulations | 001_AI_MoveEffects_Misc.rb | 主稿§7 |
| `FailsIfNotUserFirstTurn` | F:41、S:46 | 001_AI_MoveEffects_Misc.rb | 主稿§7 |
| `FailsIfUserHasUnusedMove` | F:55 | 001_AI_MoveEffects_Misc.rb | 主稿§7 |
| `FailsIfUserNotConsumedBerry` | F:73 | 001_AI_MoveEffects_Misc.rb | 主稿§7 |
| `FailsUnlessTargetSharesTypeWithUser` | T:91 | 001_AI_MoveEffects_Misc.rb | 主稿§7 |
| `RaiseUserAttack1` | F:4、S:10 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击＋1 |
| `RaiseUserAttack2` | F:19←RaiseUserAttack1、S:21←RaiseUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击＋2 |
| `RaiseUserAttack2IfTargetFaints` | G:27 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseUserAttack3` | F:39←RaiseUserAttack1、S:41←RaiseUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击＋3 |
| `RaiseUserAttack3IfTargetFaints` | G:47←RaiseUserAttack2IfTargetFaints | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `MaxUserAttackLoseHalfOfTotalHP` | F:53、S:59 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseUserDefense1` | F:73←RaiseUserAttack1、S:75←RaiseUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：防御＋1 |
| `RaiseUserDefense1CurlUpUser` | F:81←RaiseUserDefense1、S:83 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseUserDefense2` | F:97←RaiseUserDefense1、S:99←RaiseUserDefense1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：防御＋2 |
| `RaiseUserDefense3` | F:105←RaiseUserDefense1、S:107←RaiseUserDefense1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：防御＋3 |
| `RaiseUserSpAtk1` | F:113←RaiseUserAttack1、S:115←RaiseUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特攻＋1 |
| `RaiseUserSpAtk2` | F:121←RaiseUserSpAtk1、S:123←RaiseUserSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特攻＋2 |
| `RaiseUserSpAtk3` | F:129←RaiseUserSpAtk1、S:131←RaiseUserSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特攻＋3 |
| `RaiseUserSpDef1` | F:137←RaiseUserDefense1、S:139←RaiseUserDefense1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特防＋1 |
| `RaiseUserSpDef1PowerUpElectricMove` | F:145←RaiseUserSpDef1、S:147 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseUserSpDef2` | F:160←RaiseUserSpDef1、S:162←RaiseUserSpDef1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特防＋2 |
| `RaiseUserSpDef3` | F:168←RaiseUserSpDef1、S:170←RaiseUserSpDef1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特防＋3 |
| `RaiseUserSpeed1` | F:176←RaiseUserSpDef1、S:178←RaiseUserSpDef1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：速度＋1 |
| `RaiseUserSpeed2` | F:184←RaiseUserSpeed1、S:186←RaiseUserSpeed1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：速度＋2 |
| `RaiseUserSpeed2LowerUserWeight` | F:192←RaiseUserSpeed2、S:194 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseUserSpeed3` | F:219←RaiseUserSpeed1、S:221←RaiseUserSpeed1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：速度＋3 |
| `RaiseUserAccuracy1` | F:227←RaiseUserSpeed1、S:229←RaiseUserSpeed1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：命中＋1 |
| `RaiseUserAccuracy2` | F:235←RaiseUserAccuracy1、S:237←RaiseUserAccuracy1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：命中＋2 |
| `RaiseUserAccuracy3` | F:243←RaiseUserAccuracy1、S:245←RaiseUserAccuracy1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：命中＋3 |
| `RaiseUserEvasion1` | F:251←RaiseUserAccuracy1、S:253←RaiseUserAccuracy1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：闪避＋1 |
| `RaiseUserEvasion2` | F:259←RaiseUserEvasion1、S:261←RaiseUserEvasion1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：闪避＋2 |
| `RaiseUserEvasion2MinimizeUser` | F:267←RaiseUserEvasion2、S:269 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseUserEvasion3` | F:287←RaiseUserEvasion1、S:289←RaiseUserEvasion1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：闪避＋3 |
| `RaiseUserCriticalHitRate2` | F:295、S:300 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseUserAtkDef1` | F:324、S:336←RaiseUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击＋1，防御＋1 |
| `RaiseUserAtkDefAcc1` | F:342←RaiseUserAtkDef1、S:344←RaiseUserAtkDef1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击＋1，防御＋1，命中＋1 |
| `RaiseUserAtkSpAtk1` | F:350←RaiseUserAtkDef1、S:352←RaiseUserAtkDef1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击＋1，特攻＋1 |
| `RaiseUserAtkSpAtk1Or2InSun` | F:358←RaiseUserAtkSpAtk1、S:360 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `LowerUserDefSpDef1RaiseUserAtkSpAtkSpd2` | F:374、S:390 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseUserAtkSpd1` | F:401←RaiseUserAtkSpAtk1、S:403←RaiseUserAtkSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击＋1，速度＋1 |
| `RaiseUserAtk1Spd2` | F:409←RaiseUserAtkSpAtk1、S:411←RaiseUserAtkSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：速度＋2，攻击＋1 |
| `RaiseUserAtkAcc1` | F:417←RaiseUserAtkSpAtk1、S:419←RaiseUserAtkSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击＋1，命中＋1 |
| `RaiseUserDefSpDef1` | F:425←RaiseUserAtkSpAtk1、S:427←RaiseUserAtkSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：防御＋1，特防＋1 |
| `RaiseUserSpAtkSpDef1` | F:433←RaiseUserAtkSpAtk1、S:435←RaiseUserAtkSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特攻＋1，特防＋1 |
| `RaiseUserSpAtkSpDefSpd1` | F:441←RaiseUserAtkSpAtk1、S:443←RaiseUserAtkSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特攻＋1，特防＋1，速度＋1 |
| `RaiseUserMainStats1` | F:449←RaiseUserAtkSpAtk1、S:451←RaiseUserAtkSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击＋1，防御＋1，特攻＋1，特防＋1，速度＋1 |
| `RaiseUserMainStats1LoseThirdOfTotalHP` | F:457、S:463 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseUserMainStats1TrapUserInBattle` | F:479、S:485 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `StartRaiseUserAtk1WhenDamaged` | S:510 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `LowerUserAttack1` | S:527 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击−1 |
| `LowerUserAttack2` | S:536←LowerUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击−2 |
| `LowerUserDefense1` | S:542←LowerUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：防御−1 |
| `LowerUserDefense2` | S:548←LowerUserDefense1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：防御−2 |
| `LowerUserSpAtk1` | S:554←LowerUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特攻−1 |
| `LowerUserSpAtk2` | S:560←LowerUserSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特攻−2 |
| `LowerUserSpDef1` | S:566←LowerUserDefense1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特防−1 |
| `LowerUserSpDef2` | S:572←LowerUserSpDef1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：特防−2 |
| `LowerUserSpeed1` | S:578←LowerUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：速度−1 |
| `LowerUserSpeed2` | S:584←LowerUserSpeed1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：速度−2 |
| `LowerUserAtkDef1` | S:590←LowerUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：攻击−1，防御−1 |
| `LowerUserDefSpDef1` | S:596←LowerUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：防御−1，特防−1 |
| `LowerUserDefSpDefSpd1` | S:602←LowerUserAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；使用者：速度−1，防御−1，特防−1 |
| `RaiseTargetAttack1` | T:608、G:614 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseTargetAttack2ConfuseTarget` | T:623、G:629 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseTargetSpAtk1ConfuseTarget` | T:645、G:651 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseTargetSpDef1` | T:667、G:672 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseTargetRandomStat2` | T:681、G:691 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseTargetAtkSpAtk2` | T:721、G:727 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `LowerTargetAttack1` | T:737、G:743 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：攻击−1 |
| `LowerTargetAttack1BypassSubstitute` | T:752←LowerTargetAttack1、G:754←LowerTargetAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `LowerTargetAttack2` | T:760←LowerTargetAttack1、G:762←LowerTargetAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：攻击−2 |
| `LowerTargetAttack3` | T:768←LowerTargetAttack1、G:770←LowerTargetAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：攻击−3 |
| `LowerTargetDefense1` | T:776←LowerTargetAttack1、G:778←LowerTargetAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：防御−1 |
| `LowerTargetDefense1PowersUpInGravity` | T:784←LowerTargetDefense1、G:786←LowerTargetDefense1、P:788 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `LowerTargetDefense2` | T:797←LowerTargetDefense1、G:799←LowerTargetDefense1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：防御−2 |
| `LowerTargetDefense3` | T:805←LowerTargetDefense1、G:807←LowerTargetDefense1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：防御−3 |
| `LowerTargetSpAtk1` | T:813←LowerTargetAttack1、G:815←LowerTargetAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：特攻−1 |
| `LowerTargetSpAtk2` | T:821←LowerTargetSpAtk1、G:823←LowerTargetSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：特攻−2 |
| `LowerTargetSpAtk2IfCanAttract` | T:829、G:838←LowerTargetSpAtk2 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `LowerTargetSpAtk3` | T:844←LowerTargetSpAtk1、G:846←LowerTargetSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：特攻−3 |
| `LowerTargetSpDef1` | T:852←LowerTargetDefense1、G:854←LowerTargetDefense1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：特防−1 |
| `LowerTargetSpDef2` | T:860←LowerTargetSpDef1、G:862←LowerTargetSpDef1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：特防−2 |
| `LowerTargetSpDef3` | T:868←LowerTargetSpDef1、G:870←LowerTargetSpDef1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：特防−3 |
| `LowerTargetSpeed1` | T:876←LowerTargetSpDef1、G:878←LowerTargetSpDef1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：速度−1 |
| `LowerTargetSpeed1WeakerInGrassyTerrain` | T:884←LowerTargetSpeed1、G:886←LowerTargetSpeed1、P:888 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `LowerTargetSpeed1MakeTargetWeakerToFire` | T:897、G:904 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `LowerTargetSpeed2` | T:922←LowerTargetSpeed1、G:924←LowerTargetSpeed1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：速度−2 |
| `LowerTargetSpeed3` | T:930←LowerTargetSpeed1、G:932←LowerTargetSpeed1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：速度−3 |
| `LowerTargetAccuracy1` | T:938←LowerTargetSpeed1、G:940←LowerTargetSpeed1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：命中−1 |
| `LowerTargetAccuracy2` | T:946←LowerTargetAccuracy1、G:948←LowerTargetAccuracy1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：命中−2 |
| `LowerTargetAccuracy3` | T:954←LowerTargetAccuracy1、G:956←LowerTargetAccuracy1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：命中−3 |
| `LowerTargetEvasion1` | T:962←LowerTargetAccuracy1、G:964←LowerTargetAccuracy1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：闪避−1 |
| `LowerTargetEvasion2` | T:1026←LowerTargetEvasion1、G:1028←LowerTargetEvasion1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：闪避−2 |
| `LowerTargetEvasion3` | T:1034←LowerTargetEvasion1、G:1036←LowerTargetEvasion1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：闪避−3 |
| `LowerTargetAtkDef1` | T:1042、G:1054←LowerTargetAttack1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：攻击−1，防御−1 |
| `LowerTargetAtkSpAtk1` | T:1060←LowerTargetAtkDef1、G:1062←LowerTargetAtkDef1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md)；目标：攻击−1，特攻−1 |
| `LowerPoisonedTargetAtkSpAtkSpd1` | T:1068、G:1075←LowerTargetAtkSpAtk1 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseAlliesAtkDef1` | T:1081、G:1087 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaisePlusMinusUserAndAlliesAtkSpAtk1` | F:1096、T:1109、S:1116、G:1125 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaisePlusMinusUserAndAlliesDefSpDef1` | F:1134、T:1147、S:1154、G:1163 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseGroundedGrassBattlersAtkSpAtk1` | T:1172、G:1179 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `RaiseGrassBattlersDef1` | T:1188、G:1194 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `UserTargetSwapAtkSpAtkStages` | G:1203 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `UserTargetSwapDefSpDefStages` | G:1229 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `UserTargetSwapStatStages` | G:1255 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `UserCopyTargetStatStages` | G:1281 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `UserStealTargetPositiveStatStages` | G:1320 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `InvertTargetStatStages` | T:1339、G:1344 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `ResetTargetStatStages` | G:1367 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `ResetAllBattlersStatStages` | F:1389、S:1394 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `StartUserSideImmunityToStatStageLowering` | F:1418、S:1423 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `UserSwapBaseAtkDef` | S:1444 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `UserTargetSwapBaseSpeed` | G:1471 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `UserTargetAverageBaseAtkSpAtk` | G:1492 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `UserTargetAverageBaseDefSpDef` | G:1540 | 002_AI_MoveEffects_BattlerStats.rb | 主稿§4.1–4.3；真实参数／前门[WP44对应行](../pokemon-rules/wp44-effect-coverage.md) |
| `SleepTarget` | T:4、G:9 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `SleepTargetIfUserDarkrai` | F:58、T:63、G:68←SleepTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `SleepTargetChangeUserMeloettaForm` | G:74←SleepTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `SleepTargetNextTurn` | T:80、G:87←SleepTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `PoisonTarget` | T:93、G:98 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `PoisonTargetLowerTargetSpeed1` | T:153、G:159 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `BadPoisonTarget` | T:172←PoisonTarget、G:174←PoisonTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `ParalyzeTarget` | T:180、G:185 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `ParalyzeTargetIfNotTypeImmune` | T:241、G:249←ParalyzeTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `ParalyzeTargetAlwaysHitsInRainHitsTargetInSky` | G:255←ParalyzeTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `ParalyzeFlinchTarget` | G:261 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `BurnTarget` | T:280、G:285 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `BurnFlinchTarget` | G:343 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `FreezeTarget` | T:362、G:367 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `FreezeTargetSuperEffectiveAgainstWater` | G:410←FreezeTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `FreezeTargetAlwaysHitsInHail` | G:416←FreezeTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `FreezeFlinchTarget` | G:422 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `ParalyzeBurnOrFreezeTarget` | G:441 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `GiveUserStatusToTarget` | F:461、T:466、G:471 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `CureUserBurnPoisonParalysis` | F:495、S:500 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `CureUserPartyStatus` | F:510、S:515 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `CureTargetBurn` | G:530 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `StartUserSideImmunityToInflictedStatus` | F:549、S:554 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `FlinchTarget` | G:576 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `FlinchTargetFailsIfUserNotAsleep` | G:597←FlinchTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `FlinchTargetFailsIfNotUserFirstTurn` | F:603、G:608←FlinchTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `FlinchTargetDoublePowerIfTargetInSky` | G:619←FlinchTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `ConfuseTarget` | T:625、G:630 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `ConfuseTargetAlwaysHitsInRainHitsTargetInSky` | G:656←ConfuseTarget | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `AttractTarget` | T:662、G:667 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§5 |
| `SetUserTypesBasedOnEnvironment` | F:690、S:706 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `SetUserTypesToResistLastAttack` | T:738、G:753 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `SetUserTypesToTargetTypes` | T:772 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `SetUserTypesToUserMoveType` | F:785、G:799 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `SetTargetTypesToPsychic` | T:827、G:832 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `SetTargetTypesToWater` | T:855←SetTargetTypesToPsychic、G:857 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `AddGhostTypeToTarget` | T:880←SetTargetTypesToWater、G:882 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `AddGrassTypeToTarget` | T:906←AddGhostTypeToTarget、G:908 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `UserLosesFireType` | F:932 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `SetTargetAbilityToSimple` | T:941、G:947 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `SetTargetAbilityToInsomnia` | T:965、G:971 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `SetUserAbilityToTargetAbility` | T:989、G:995 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `SetTargetAbilityToUserAbility` | T:1012、G:1020 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `UserTargetSwapAbilities` | T:1038、G:1045 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `NegateTargetAbility` | T:1069、G:1074 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |
| `NegateTargetAbilityIfTargetActed` | G:1091 | 003_AI_MoveEffects_BattlerOther.rb | 主稿§6 |

## 3. 通用修正与能力评级注册

| 族 | 身份 | 方式／复制源 | 文件及起行 | 合同 |
| --- | --- | --- | --- | --- |
| GeneralMoveAgainstTargetScore | `shiny_target` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:4 | 主稿§2.2 |
| GeneralMoveScore | `shadow_moves` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:18 | 主稿§2.2 |
| GeneralMoveScore | `thawing_move_when_frozen` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:32 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `priority_move_against_faster_target` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:53 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `target_can_Magic_Coat_or_Bounce_move` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:87 | 主稿§2.2 |
| GeneralMoveScore | `any_foe_can_Magic_Coat_or_Bounce_move` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:105 | 主稿§2.2 |
| GeneralMoveScore | `any_battler_can_Snatch_move` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:130 | 主稿§2.2 |
| GeneralMoveScore | `good_move_for_choice_item` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:150 | 主稿§2.2 |
| GeneralMoveScore | `damaging_move_and_either_side_no_reserves` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:183 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `target_can_powder_fire_moves` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:208 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `target_can_make_moves_Electric_and_be_immune` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:225 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `target_semi_invulnerable` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:245 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `predicted_accuracy` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:280 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `predicted_damage` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:297 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `external_flinching_effects` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:330 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `thawing_move_against_frozen_target` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:351 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `trigger_target_ability_or_item_upon_hit` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:373 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `trigger_user_ability_upon_hit` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:409 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `knocking_out_a_destiny_bonder_or_grudger` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:431 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `damaging_a_raging_target` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:459 | 主稿§2.2 |
| GeneralMoveAgainstTargetScore | `damaging_a_biding_target` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:480 | 主稿§2.2 |
| GeneralMoveScore | `dance_move_against_dancer` | add | 005_AI/007_AI_ChooseMove_OtherScores.rb:506 | 主稿§2.2 |
| AbilityRanking | `BLAZE` | add | 005_AI/008_AI_Utilities.rb:235 | 主稿§6 |
| AbilityRanking | `CUTECHARM` | add | 005_AI/008_AI_Utilities.rb:242 | 主稿§6 |
| AbilityRanking | `RIVALRY` | copy←CUTECHARM | 005_AI/008_AI_Utilities.rb:249 | 主稿§6 |
| AbilityRanking | `FRIENDGUARD` | add | 005_AI/008_AI_Utilities.rb:251 | 主稿§6 |
| AbilityRanking | `HEALER` | copy←FRIENDGUARD | 005_AI/008_AI_Utilities.rb:260 | 主稿§6 |
| AbilityRanking | `SYMBOISIS` | copy←FRIENDGUARD | 005_AI/008_AI_Utilities.rb:260 | 主稿§6 |
| AbilityRanking | `TELEPATHY` | copy←FRIENDGUARD | 005_AI/008_AI_Utilities.rb:260 | 主稿§6 |
| AbilityRanking | `GALEWINGS` | add | 005_AI/008_AI_Utilities.rb:262 | 主稿§6 |
| AbilityRanking | `HUGEPOWER` | add | 005_AI/008_AI_Utilities.rb:269 | 主稿§6 |
| AbilityRanking | `PUREPOWER` | copy←HUGEPOWER | 005_AI/008_AI_Utilities.rb:276 | 主稿§6 |
| AbilityRanking | `IRONFIST` | add | 005_AI/008_AI_Utilities.rb:278 | 主稿§6 |
| AbilityRanking | `LIQUIDVOICE` | add | 005_AI/008_AI_Utilities.rb:285 | 主稿§6 |
| AbilityRanking | `MEGALAUNCHER` | add | 005_AI/008_AI_Utilities.rb:292 | 主稿§6 |
| AbilityRanking | `OVERGROW` | add | 005_AI/008_AI_Utilities.rb:299 | 主稿§6 |
| AbilityRanking | `PRANKSTER` | add | 005_AI/008_AI_Utilities.rb:306 | 主稿§6 |
| AbilityRanking | `PUNKROCK` | add | 005_AI/008_AI_Utilities.rb:313 | 主稿§6 |
| AbilityRanking | `RECKLESS` | add | 005_AI/008_AI_Utilities.rb:320 | 主稿§6 |
| AbilityRanking | `ROCKHEAD` | add | 005_AI/008_AI_Utilities.rb:327 | 主稿§6 |
| AbilityRanking | `RUNAWAY` | add | 005_AI/008_AI_Utilities.rb:334 | 主稿§6 |
| AbilityRanking | `SANDFORCE` | add | 005_AI/008_AI_Utilities.rb:341 | 主稿§6 |
| AbilityRanking | `SKILLLINK` | add | 005_AI/008_AI_Utilities.rb:348 | 主稿§6 |
| AbilityRanking | `STEELWORKER` | add | 005_AI/008_AI_Utilities.rb:355 | 主稿§6 |
| AbilityRanking | `SWARM` | add | 005_AI/008_AI_Utilities.rb:362 | 主稿§6 |
| AbilityRanking | `TORRENT` | add | 005_AI/008_AI_Utilities.rb:369 | 主稿§6 |
| AbilityRanking | `TRIAGE` | add | 005_AI/008_AI_Utilities.rb:376 | 主稿§6 |

## 4. 基础能力评级完整表

源Utilities:101–159；数据名称按字面保留，包括拼写不同的身份；未列0。这里是完整默认数据，不是源程序。中等能力依赖见主稿§6。

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
| -1 | DEFEATIST, HEAVYMETAL, KLUTZ, NORMALIZE, PERISHBODY, STALL, ZENMODE |
| -2 | SLOWSTART, TRUANT |

共267条身份、13档，无重复。GULPMISSLE／PROPELLORTAIL按字面；能力修正copy为SYMBOISIS，不能悄悄改成SYMBIOSIS。

## 5. 已有与前向登记逐项归属

以下按文件＋包＋族分组，列全展开身份；行内包名后的状态词为A阶段历史定位（当时未启动），当前B／C状态以各自有界附表为准。B/C只登记边界，不从目录推断行为已完成。相同效果跨族可分责，尤其畏缩的天空双倍基数B、其状态分A。

| 归属 | 文件／族 | 展开身份 |
| --- | --- | --- |
| WP51（已限定通过的回填后版本） | 005_AI/002_AI_Switch.rb／ShouldSwitch | perish_song, significant_eor_damage, cure_status_problem_by_switching_out, wish_healing, yawning, asleep, battler_is_useless, foe_absorbs_all_moves_with_its_ability, absorb_foe_move, sudden_death, high_damage_from_foe |
| WP51（已限定通过的回填后版本） | 005_AI/002_AI_Switch.rb／ShouldNotSwitch | lethal_entry_hazards, battler_has_super_effective_move, battler_has_very_raised_stats, battler_is_immune_via_wonder_guard |
| WP52-C（A阶段定位） | 005_AI/008_AI_Utilities.rb／ItemRanking | ADAMANTORB, AGUAVBERRY, ASSAULTVEST, BERRYJUICE, BIGROOT, BINDINGBAND, GRIPCLAW, BLACKSLUDGE, CHESTOBERRY, CHOICEBAND, MUSCLEBAND, CHOICESPECS, WISEGLASSES, DEEPSEASCALE, DAMPROCK, DEEPSEATOOTH, ELECTRICSEED, EVIOLITE, FIGYBERRY, FLAMEORB, FULLINCENSE, LAGGINGTAIL, GRASSYSEED, GRISEOUSORB, HEATROCK, IAPAPABERRY, ICYROCK, IRONBALL, KINGSROCK, RAZORFANG, LEEK, STICK, LIGHTBALL, LIGHTCLAY, LUCKYPUNCH, LUSTROUSORB, MAGOBERRY, METALPOWDER, QUICKPOWDER, MISTYSEED, ORANBERRY, POWERHERB, PSYCHICSEED, RINGTARGET, SMOOTHROCK, SOULDEW, TERRAINEXTENDER, THICKCLUB, THROATSPRAY, TOXICORB, WHITEHERB, WIKIBERRY, ZOOMLENS |
| WP52-C（A阶段定位） | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb／MoveFailureAgainstTargetCheck | FailsIfTargetHasNoItem |
| WP52-C（A阶段定位） | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb／MoveEffectAgainstTargetScore | FailsIfUserDamagedThisTurn, FailsIfTargetActed |
| WP52-B（A阶段定位） | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb／MoveEffectAgainstTargetScore | CrashDamageIfFailsUnusableInGravity |
| WP52-B（A阶段定位） | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb／MoveFailureCheck | StartSunWeather, StartRainWeather, StartSandstormWeather, StartHailWeather, StartElectricTerrain, StartGrassyTerrain, StartMistyTerrain, StartPsychicTerrain, RemoveTerrain, AddSpikesToFoeSide, AddToxicSpikesToFoeSide, AddStealthRocksToFoeSide, AddStickyWebToFoeSide, UserMakeSubstitute, StartShadowSkyWeather, RemoveAllScreensAndSafeguard |
| WP52-B（A阶段定位） | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb／MoveEffectScore | StartSunWeather, StartRainWeather, StartSandstormWeather, StartHailWeather, StartElectricTerrain, StartGrassyTerrain, StartMistyTerrain, StartPsychicTerrain, RemoveTerrain, AddSpikesToFoeSide, AddToxicSpikesToFoeSide, AddStealthRocksToFoeSide, AddStickyWebToFoeSide, UserMakeSubstitute, AttackTwoTurnsLater, AllBattlersLoseHalfHPUserSkipsNextTurn, UserLosesHalfHP, StartShadowSkyWeather, RemoveAllScreensAndSafeguard |
| WP52-C（A阶段定位） | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb／MoveFailureCheck | SwapSideEffects, UserSwapsPositionsWithAlly |
| WP52-C（A阶段定位） | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb／MoveEffectScore | SwapSideEffects, RemoveUserBindingAndEntryHazards, UserSwapsPositionsWithAlly, BurnAttackerBeforeUserActs |
| WP52-B（A阶段定位） | 006_AI MoveEffects/001_AI_MoveEffects_Misc.rb／MoveFailureAgainstTargetCheck | AttackTwoTurnsLater |
| WP52-B（A阶段定位） | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb／MoveFailureAgainstTargetCheck | LowerTargetEvasion1RemoveSideEffects |
| WP52-B（A阶段定位） | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb／MoveEffectAgainstTargetScore | LowerTargetEvasion1RemoveSideEffects, UserTargetAverageHP |
| WP52-B（A阶段定位） | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb／MoveFailureCheck | StartUserSideDoubleSpeed |
| WP52-B（A阶段定位） | 006_AI MoveEffects/002_AI_MoveEffects_BattlerStats.rb／MoveEffectScore | StartUserSideDoubleSpeed, StartSwapAllBattlersBaseDefensiveStats |
| WP52-B（A阶段定位） | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb／MoveBasePower | FlinchTargetDoublePowerIfTargetInSky |
| WP52-C（A阶段定位） | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb／MoveFailureCheck | StartUserAirborne, StartGravity |
| WP52-C（A阶段定位） | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb／MoveEffectScore | StartUserAirborne, StartGravity |
| WP52-C（A阶段定位） | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb／MoveFailureAgainstTargetCheck | StartTargetAirborneAndAlwaysHitByMoves, TransformUserIntoTarget |
| WP52-C（A阶段定位） | 006_AI MoveEffects/003_AI_MoveEffects_BattlerOther.rb／MoveEffectAgainstTargetScore | StartTargetAirborneAndAlwaysHitByMoves, HitsTargetInSkyGroundsTarget, TransformUserIntoTarget |
| WP52-B（A阶段定位） | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb／MoveBasePower | FixedDamage20, FixedDamage40, FixedDamageHalfTargetHP, FixedDamageUserLevel, FixedDamageUserLevelRandom, LowerTargetHPToUserHP, OHKO, OHKOIce, OHKOHitsUndergroundTarget, PowerHigherWithUserHP, PowerLowerWithUserHP, PowerHigherWithTargetHP, PowerHigherWithUserHappiness, PowerLowerWithUserHappiness, PowerHigherWithUserPositiveStatStages, PowerHigherWithTargetPositiveStatStages, PowerHigherWithUserFasterThanTarget, PowerHigherWithTargetFasterThanUser, PowerHigherWithLessPP, PowerHigherWithTargetWeight, PowerHigherWithUserHeavierThanTarget, PowerHigherWithConsecutiveUse, PowerHigherWithConsecutiveUseOnUserSide, RandomPowerDoublePowerIfTargetUnderground, DoublePowerIfTargetHPLessThanHalf, DoublePowerIfUserPoisonedBurnedParalyzed, DoublePowerIfTargetAsleepCureTarget, DoublePowerIfTargetPoisoned, DoublePowerIfTargetParalyzedCureTarget, DoublePowerIfTargetStatusProblem, DoublePowerIfUserHasNoItem, DoublePowerIfTargetUnderwater, DoublePowerIfTargetUnderground, DoublePowerIfTargetInSky, DoublePowerInElectricTerrain, DoublePowerIfUserLastMoveFailed, DoublePowerIfAllyFaintedLastTurn, EffectivenessIncludesFlyingType, TypeDependsOnUserIVs, TypeAndPowerDependOnUserBerry, TypeAndPowerDependOnWeather, TypeAndPowerDependOnTerrain |
| WP52-B（A阶段定位） | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb／MoveFailureAgainstTargetCheck | LowerTargetHPToUserHP, OHKO, OHKOIce, OHKOHitsUndergroundTarget, CannotMakeTargetFaint, TargetMovesBecomeElectric |
| WP52-B（A阶段定位） | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb／MoveEffectAgainstTargetScore | OHKO, OHKOIce, OHKOHitsUndergroundTarget, DamageTargetAlly, DoublePowerIfTargetAsleepCureTarget, DoublePowerIfTargetParalyzedCureTarget, DoublePowerIfTargetLostHPThisTurn, DoublePowerIfTargetActed, DoublePowerIfTargetNotActed, RemoveProtections, RemoveProtections, HoopaRemoveProtectionsBypassSubstituteLowerUserDef1, RecoilQuarterOfDamageDealt, RecoilThirdOfDamageDealtParalyzeTarget, RecoilThirdOfDamageDealtBurnTarget, RecoilHalfOfDamageDealt, CategoryDependsOnHigherDamagePoisonTarget, EnsureNextMoveAlwaysHits, StartNegateTargetEvasionStatStageAndGhostImmunity, StartNegateTargetEvasionStatStageAndDarkImmunity, TargetMovesBecomeElectric |
| WP52-B（A阶段定位） | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb／MoveEffectScore | PowerHigherWithConsecutiveUse, PowerHigherWithConsecutiveUse, DoublePowerIfUserLostHPThisTurn, EnsureNextCriticalHit, StartPreventCriticalHitsAgainstUserSide, UserEnduresFaintingThisTurn, StartWeakenElectricMoves, StartWeakenFireMoves, StartWeakenPhysicalDamageAgainstUserSide, StartWeakenSpecialDamageAgainstUserSide, StartWeakenDamageAgainstUserSideIfHail, RemoveScreens, ProtectUser, ProtectUserBanefulBunker, ProtectUserFromDamagingMovesKingsShield, ProtectUserFromDamagingMovesObstruct, ProtectUserFromTargetingMovesSpikyShield, ProtectUserSideFromDamagingMovesIfUserFirstTurn, ProtectUserSideFromStatusMoves, ProtectUserSideFromPriorityMoves, ProtectUserSideFromMultiTargetDamagingMoves, TypeDependsOnUserMorpekoFormRaiseUserSpeed1, NormalMovesBecomeElectric |
| WP52-B（A阶段定位） | 006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb／MoveFailureCheck | StartPreventCriticalHitsAgainstUserSide, StartWeakenElectricMoves, StartWeakenFireMoves, StartWeakenPhysicalDamageAgainstUserSide, StartWeakenSpecialDamageAgainstUserSide, StartWeakenDamageAgainstUserSideIfHail, ProtectUserSideFromDamagingMovesIfUserFirstTurn, ProtectUserSideFromStatusMoves, ProtectUserSideFromPriorityMoves, ProtectUserSideFromMultiTargetDamagingMoves, HoopaRemoveProtectionsBypassSubstituteLowerUserDef1, EnsureNextMoveAlwaysHits, TypeAndPowerDependOnUserBerry, TypeDependsOnUserMorpekoFormRaiseUserSpeed1 |
| WP52-B（A阶段定位） | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb／MoveBasePower | HitTwoTimes, HitTwoTimesPoisonTarget, HitTwoTimesFlinchTarget, HitTwoTimesTargetThenTargetAlly, HitThreeTimesPowersUpWithEachHit, HitThreeTimesAlwaysCriticalHit, HitTwoToFiveTimes, HitTwoToFiveTimesOrThreeForAshGreninja, HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1, HitOncePerUserTeamMember, TwoTurnAttackOneTurnInSun, MultiTurnAttackPowersUpEachTurn, MultiTurnAttackBideThenReturnDoubleDamage |
| WP52-B（A阶段定位） | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb／MoveEffectAgainstTargetScore | HitTwoTimes, HitTwoTimesPoisonTarget, HitTwoTimesFlinchTarget, HitThreeTimesPowersUpWithEachHit, HitThreeTimesAlwaysCriticalHit, HitTwoToFiveTimes, HitTwoToFiveTimesOrThreeForAshGreninja, HitTwoToFiveTimesRaiseUserSpd1LowerUserDef1, HitOncePerUserTeamMember, TwoTurnAttack, TwoTurnAttackOneTurnInSun, TwoTurnAttackParalyzeTarget, TwoTurnAttackBurnTarget, TwoTurnAttackFlinchTarget, TwoTurnAttackRaiseUserSpAtkSpDefSpd2, TwoTurnAttackChargeRaiseUserDefense1, TwoTurnAttackChargeRaiseUserSpAtk1, TwoTurnAttackInvulnerableUnderground, TwoTurnAttackInvulnerableUnderwater, TwoTurnAttackInvulnerableInSky, TwoTurnAttackInvulnerableInSkyParalyzeTarget, TwoTurnAttackInvulnerableInSkyTargetCannotAct, TwoTurnAttackInvulnerableRemoveProtections |
| WP52-B（A阶段定位） | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb／MoveFailureCheck | HitOncePerUserTeamMember, TwoTurnAttackRaiseUserSpAtkSpDefSpd2 |
| WP52-B（A阶段定位） | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb／MoveEffectScore | AttackAndSkipNextTurn, MultiTurnAttackBideThenReturnDoubleDamage |
| WP52-B（A阶段定位） | 006_AI MoveEffects/005_AI_MoveEffects_MultiHit.rb／MoveFailureAgainstTargetCheck | TwoTurnAttackInvulnerableInSkyTargetCannotAct |
| WP52-B（A阶段定位） | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb／MoveFailureCheck | HealUserFullyAndFallAsleep, HealUserHalfOfTotalHP, HealUserDependingOnWeather, HealUserDependingOnSandstorm, HealUserHalfOfTotalHPLoseFlyingTypeThisTurn, HealUserPositionNextTurn, StartHealUserEachTurn, StartHealUserEachTurnTrapUserInBattle, UserLosesHalfOfTotalHPExplosive, UserFaintsExplosive, UserFaintsPowersUpInMistyTerrainExplosive, UserFaintsHealAndCureReplacement, UserFaintsHealAndCureReplacementRestorePP, AttackerFaintsIfUserFaints |
| WP52-B（A阶段定位） | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb／MoveEffectScore | HealUserFullyAndFallAsleep, HealUserHalfOfTotalHP, HealUserDependingOnWeather, HealUserDependingOnSandstorm, HealUserHalfOfTotalHPLoseFlyingTypeThisTurn, HealUserPositionNextTurn, StartHealUserEachTurn, StartHealUserEachTurnTrapUserInBattle, UserLosesHalfOfTotalHP, UserLosesHalfOfTotalHPExplosive, UserFaintsExplosive, UserFaintsPowersUpInMistyTerrainExplosive, UserFaintsFixedDamageUserHP, UserFaintsHealAndCureReplacement, UserFaintsHealAndCureReplacementRestorePP, StartPerishCountsForAllBattlers, AttackerFaintsIfUserFaints, SetAttackerMovePPTo0IfUserFaints |
| WP52-B（A阶段定位） | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb／MoveFailureAgainstTargetCheck | CureTargetStatusHealUserHalfOfTotalHP, HealUserByTargetAttackLowerTargetAttack1, HealUserByHalfOfDamageDoneIfTargetAsleep, HealUserAndAlliesQuarterOfTotalHP, HealUserAndAlliesQuarterOfTotalHPCureStatus, HealTargetHalfOfTotalHP, HealTargetDependingOnGrassyTerrain, StartDamageTargetEachTurnIfTargetAsleep, StartLeechSeedTarget, StartPerishCountsForAllBattlers |
| WP52-B（A阶段定位） | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb／MoveEffectAgainstTargetScore | CureTargetStatusHealUserHalfOfTotalHP, HealUserByTargetAttackLowerTargetAttack1, HealUserByHalfOfDamageDone, HealUserByHalfOfDamageDoneIfTargetAsleep, HealUserByThreeQuartersOfDamageDone, HealUserAndAlliesQuarterOfTotalHP, HealUserAndAlliesQuarterOfTotalHPCureStatus, HealTargetHalfOfTotalHP, HealTargetDependingOnGrassyTerrain, StartDamageTargetEachTurnIfTargetAsleep, StartLeechSeedTarget, UserFaintsLowerTargetAtkSpAtk2 |
| WP52-B（A阶段定位） | 006_AI MoveEffects/006_AI_MoveEffects_Healing.rb／MoveBasePower | UserFaintsPowersUpInMistyTerrainExplosive, UserFaintsFixedDamageUserHP |
| WP52-C（A阶段定位） | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb／MoveEffectAgainstTargetScore | UserTakesTargetItem, TargetTakesUserItem, UserTargetSwapItems, RemoveTargetItem, DestroyTargetBerryOrGem, CorrodeTargetItem, StartTargetCannotUseItem, AllBattlersConsumeBerry, UserConsumeTargetBerry, ThrowUserItemAtTarget |
| WP52-C（A阶段定位） | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb／MoveFailureAgainstTargetCheck | TargetTakesUserItem, UserTargetSwapItems, CorrodeTargetItem, StartTargetCannotUseItem, AllBattlersConsumeBerry |
| WP52-C（A阶段定位） | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb／MoveFailureCheck | RestoreUserConsumedItem, UserConsumeBerryRaiseDefense2, ThrowUserItemAtTarget |
| WP52-C（A阶段定位） | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb／MoveEffectScore | RestoreUserConsumedItem, StartNegateHeldItems, UserConsumeBerryRaiseDefense2 |
| WP52-C（A阶段定位） | 006_AI MoveEffects/007_AI_MoveEffects_Items.rb／MoveBasePower | RemoveTargetItem, ThrowUserItemAtTarget |
| WP52-C（A阶段定位） | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb／MoveEffectScore | RedirectAllMovesToUser, RandomlyDamageOrHealTarget, CurseTargetOrLowerUserSpd1RaiseUserAtkDef1, DoublePowerAfterFusionFlare, DoublePowerAfterFusionBolt, CounterPhysicalDamage, CounterSpecialDamage, CounterDamagePlusHalf, UserAddStockpileRaiseDefSpDef1, PowerDependsOnUserStockpile, HealUserDependingOnUserStockpile, GrassPledge, FirePledge, WaterPledge, BounceBackProblemCausingStatusMoves, StealAndUseBeneficialStatusMove, ReplaceMoveWithTargetLastMoveUsed |
| WP52-C（A阶段定位） | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb／MoveEffectAgainstTargetScore | RedirectAllMovesToTarget, HealAllyOrDamageFoe, CurseTargetOrLowerUserSpd1RaiseUserAtkDef1, EffectDependsOnEnvironment, TargetNextFireMoveDamagesTarget, PowerUpAllyMove, UseMoveTargetIsAboutToUse, ReplaceMoveThisBattleWithTargetLastMoveUsed |
| WP52-C（A阶段定位） | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb／MoveBasePower | RandomlyDamageOrHealTarget, HitsAllFoesAndPowersUpInPsychicTerrain, CounterPhysicalDamage, CounterSpecialDamage, CounterDamagePlusHalf, PowerDependsOnUserStockpile |
| WP52-C（A阶段定位） | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb／MoveFailureAgainstTargetCheck | HealAllyOrDamageFoe, CurseTargetOrLowerUserSpd1RaiseUserAtkDef1, TargetNextFireMoveDamagesTarget, PowerUpAllyMove, UseLastMoveUsedByTarget, UseMoveTargetIsAboutToUse, ReplaceMoveThisBattleWithTargetLastMoveUsed, ReplaceMoveWithTargetLastMoveUsed |
| WP52-C（A阶段定位） | 006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb／MoveFailureCheck | CurseTargetOrLowerUserSpd1RaiseUserAtkDef1, UserAddStockpileRaiseDefSpDef1, PowerDependsOnUserStockpile, HealUserDependingOnUserStockpile, UseLastMoveUsed, UseRandomMoveFromUserParty, UseRandomUserMoveIfAsleep, ReplaceMoveThisBattleWithTargetLastMoveUsed |
| WP52-C（A阶段定位） | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb／MoveFailureCheck | FleeFromBattle, SwitchOutUserStatusMove, SwitchOutUserPassOnEffects, TrapAllBattlersInBattleForOneTurn, UsedAfterUserTakesPhysicalDamage, DisableTargetMovesKnownByUser |
| WP52-C（A阶段定位） | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb／MoveEffectScore | FleeFromBattle, SwitchOutUserStatusMove, SwitchOutUserDamagingMove, SwitchOutUserPassOnEffects, TrapAllBattlersInBattleForOneTurn, UsedAfterUserTakesPhysicalDamage, UsedAfterAllyRoundWithDoublePower, StartSlowerBattlersActFirst |
| WP52-C（A阶段定位） | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb／MoveFailureAgainstTargetCheck | LowerTargetAtkSpAtk1SwitchOutUser, SwitchOutTargetStatusMove, TrapTargetInBattle, TrapTargetInBattleMainEffect, TrapTargetInBattleLowerTargetDefSpDef1EachTurn, TargetUsesItsLastUsedMoveAgain, LowerPPOfTargetLastMoveBy4, DisableTargetLastMoveUsed, DisableTargetUsingSameMoveConsecutively, DisableTargetUsingDifferentMove, DisableTargetStatusMoves, DisableTargetHealingMoves |
| WP52-C（A阶段定位） | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb／MoveEffectAgainstTargetScore | LowerTargetAtkSpAtk1SwitchOutUser, LowerTargetAtkSpAtk1SwitchOutUser, SwitchOutTargetStatusMove, SwitchOutTargetDamagingMove, BindTarget, BindTargetDoublePowerIfTargetUnderwater, TrapTargetInBattle, TrapTargetInBattleMainEffect, TrapTargetInBattleLowerTargetDefSpDef1EachTurn, TrapUserAndTargetInBattle, TargetActsNext, TargetActsLast, TargetUsesItsLastUsedMoveAgain, LowerPPOfTargetLastMoveBy3, LowerPPOfTargetLastMoveBy4, DisableTargetLastMoveUsed, DisableTargetUsingSameMoveConsecutively, DisableTargetUsingDifferentMove, DisableTargetStatusMoves, DisableTargetHealingMoves, DisableTargetSoundMoves, DisableTargetMovesKnownByUser |
| WP52-C（A阶段定位） | 006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb／MoveBasePower | BindTargetDoublePowerIfTargetUnderwater |

重复登记定点：MoveAttributes:220/238的MoveEffectScore PowerHigherWithConsecutiveUse、:1175/1190的MoveEffectAgainstTargetScore RemoveProtections，及SwitchingActing:104/109的MoveEffectAgainstTargetScore LowerTargetAtkSpAtk1SwitchOutUser。前两组交B、后一组交C，后续须按真实覆盖顺序核行为，不把两次加法并用；本包不宣称已完成这些规则。

附表没有无名未归属注册；真实效果没有专用AI登记时只能适用通用默认，不能因此称其不存在。WP52-B/C完成后须回查跨族共用数据与通用消费；全局覆盖出口WP79保留。

本轮记录：2026-09-28 [独立首审报告](../../review/wp50-wp51-wp52a-review-2026-09-28/report.md)／[有限修订提示](../../review/wp50-wp51-wp52a-review-2026-09-28/revision-prompt.md)；仅维护WP51通过状态；登记身份、默认评级、B/C归属与三个前向重复键不变，本包A～F在本次有限复审限定通过。被审首稿v1完整身份 `b620a868091aff4e1bb519f18e89698688eef279dbb020f828e2a0dfa25739c6`（58,177字节）保留历史，当前新字节不冒充被审对象；其它已支持范围、运行未决与阶段出口保留。

本次闭合回填：2026-09-28 [独立有限复审报告](../../review/wp50-wp51-wp52a-recheck-2026-09-28/report.md)§3–4，164效果身份／334登记出现与267能力评级数据；B/C原定位分工非外审通过限定通过；本次只维护状态、排版与完整身份，行为及场景输入/期望不变。被审附表v2 `a5a13acaf8572fa621b91911430b2286b23340618c72d4b5d2e1522aaf4ec5f9`（58,772字节）保留历史；当前新字节不冒充被审对象。运行及阶段出口继续保留。

本次状态维护：2026-09-28 BATCH-C01（非阻塞）。§1的B247／C190与§5行状态词改为A阶段历史定位（行内“未启动”→“A阶段定位”），当前B270／C167及B／C各自状态以有界附表为准；登记身份、默认评级、B／C归属与三个前向重复键不变，未重审A行为。本次维护后当前字节不冒充此前被审对象；被审/此前身份 `fa760facb18685586550f4a831c30616e4503942e2e170eaf605afa517ed868b`（59,366字节）保留历史。运行及阶段出口继续保留。
