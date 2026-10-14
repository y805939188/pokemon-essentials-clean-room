# Non-registration units and common-query boundaries

These named comment units were read in the full primary-source ranges. Negative registration search covers **all 005_AI and all nine 006_AI MoveEffects files**, logged in `logs/non-handler-negative-search.txt`; the result is a scoped registration/default finding, not proof that the real move effect is absent. Shared defaults: `005_AI/001_Battle_AI.rb:97-118`. Formal counterparts: WP52-B main L13, L61 and coverage L111.

| Primary source unit | Name / fact | Necessary consumer / qualification |
|---|---|---|
| 004:411 | DoublePowerIfUserStatsLoweredThisTurn has no dedicated local base/score registration. | No name-implied double in AI; AIMove base default L81-87. Real base query is different execution scope, real MoveAttributes L596-600. |
| 004:436 | AlwaysCriticalHit has no dedicated local scoring registration. | AIMove rough critical override L530-539 consumes real override; “no handler” is not “no crit”. |
| 004:1312 | CategoryDependsOnHigherDamageIgnoreTargetAbility has no dedicated local effect registration. | AIMove setup L11-16 and rough damage L108-111 use ability-bypass and real category preparation. |
| 004:1317 | UseUserDefenseInsteadOfUserAttack has no dedicated local effect handler. | Real attack-stat query still consumed at AIMove L112; do not add a parallel score just because named here. |
| 004:1322 | UseTargetAttackInsteadOfUserAttack has no dedicated local effect handler. | Same query stage L112, actual receiver chooses source attack. |
| 004:1327 | UseTargetDefenseInsteadOfTargetSpDef has no dedicated local effect handler. | Real defense-stat query at AIMove L118; category/defense are not necessarily identical. |
| 004:1404 | IgnoreTargetDefSpDefEvaStatStages has no dedicated local effect handler. | AIMove accuracy L481-483 zeroes target evasion for this identity; real attack/defense queries remain separate. |
| 004:1409 | TypeIsUserFirstType has no dedicated local base/score handler. | Medium rough_type calls real type query AIMove L32-35; lower skill reads original data type. |
| 004:1441 | TypeDependsOnUserPlate no dedicated local score/base handler. | Same medium real type query; no artificial held-item valuation granted here. |
| 004:1446 | TypeDependsOnUserMemory no dedicated local score/base handler. | Same query route; do not infer copied Plate implementation in future architecture. |
| 004:1451 | TypeDependsOnUserDrive no dedicated local score/base handler. | Same query route, distinct data identity. |
| 005:484 | MultiTurnAttackPreventSleeping no dedicated local base/effect registration. | Common base/score defaults retain input; real multi-turn execution not denied. |
| 005:489 | MultiTurnAttackConfuseUserAtEnd no dedicated local base/effect registration. | No implicit confusion-cost score from this comment; real fatigue execution separately specified. |
| Real MoveAttributes L1046-1050; all-AI negative search | Plain RecoilThirdOfDamageDealt has real one-third recoil but no dedicated AI target-recoil score. | Do not borrow one-third status variants or quarter/half penalty by family resemblance. WP52-B §6.2 only names existing registered recoil families; common default retains input before generic damage scoring. |

The Aegislash/StanceChange identity comparison was checked against real ability accessor `002_Battler/001_Battle_Battler.rb:72-74` and data identity equality `010_Data/001_GameData.rb:220-232`. It is supported symbol identity comparison; no object-versus-symbol mismatch finding was proposed.
