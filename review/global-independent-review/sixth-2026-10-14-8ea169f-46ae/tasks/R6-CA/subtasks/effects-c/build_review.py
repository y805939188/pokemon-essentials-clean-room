"""Serialize this reviewer's hand-written semantic observations; no source execution.

Each data row binds an actual, already-read registration interval to a distinct
behavior fact and a formal clause. A regex below inventories registration starts
only, to detect an accidentally omitted row. It never assigns semantic outcomes.
"""
import collections
import datetime
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-CA/subtasks/effects-c'
SRC = ROOT / 'reference/pokemon-essentials/Data/Scripts/011_Battle/006_AI MoveEffects'
F = 'deliverables/final-specification-set/combat-requirements/wp52-c-items-calling-and-control-evaluation.md'
B = 'deliverables/final-specification-set/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md'
C = 'deliverables/final-specification-set/combat-requirements/wp52-c-item-control-coverage-and-data.md'
BC = 'deliverables/final-specification-set/combat-requirements/wp52-b-effect-coverage.md'
CAT = 'deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md'
REG = {'F':'MoveFailureCheck', 'FT':'MoveFailureAgainstTargetCheck', 'S':'MoveEffectScore', 'ST':'MoveEffectAgainstTargetScore', 'P':'MoveBasePower'}
FILES = {'007':'007_AI_MoveEffects_Items.rb', '008':'008_AI_MoveEffects_ChangeMoveEffect.rb', '009':'009_AI_MoveEffects_SwitchingActing.rb'}

# Hand-written after the actual contiguous reads. Columns: file, range,
# receiver, identity (copy rows use destination identity), clause line, fact,
# independent normal/boundary contrast. "B" prefixes a WP52-B clause.
DATA = r'''
007|4-24|ST|UserTakesTargetItem|87|Steal preference guards wild user, occupied user, target absent/unlosable item, receiving incompatibility, substitute, and Sticky Hold unless bypassed; independently zero inactive sides' valuation differences; add four user gain minus four target gain.|V gains U+9/T−9 give +72; U inactive gives +36; wild U preserves s.
007|29-35|FT|TargetTakesUserItem|88|Delivery target failure requires user lacking/retaining its item or occupied/incompatible recipient; no added Sticky Hold test here.|Empty U fails; transferable held item and empty compatible T do not fail this check.
007|36-50|ST|TargetTakesUserItem|88|Delivery effect adds four times user's no-item benefit minus four times recipient benefit; side effectiveness queried independently.|U gains +7 by removal and T gains +9 yields −8; suppress T alone yields +28.
007|55-64|FT|UserTargetSwapItems|89|Swap failure covers wild U, both empty, both persons against both item identities, and Sticky Hold without bypass.|Both empty fails; one empty compatible recipient can pass; bypass removes Sticky Hold rejection only.
007|65-83|ST|UserTargetSwapItems|89|Swap scores each independent hypothetical item change at +4ΔU−4ΔT, with inactive sides zeroed; same-function previous valid move penalized 15.|ΔU=2/ΔT=−3 gives +20; same-function recent move gives +5; invalid recent identity adds no repetition penalty.
007|88-92|F|RestoreUserConsumedItem|90|Recycle fails for missing saved consumed identity or any currently held item.|R present and current empty passes; same R with current occupied fails.
007|93-101|S|RestoreUserConsumedItem|90|Recycle returns local 60 if current item activation false, otherwise four times saved-item versus empty value.|ΔV5 gives s+20; Magic Room gives 60; no persistent item is written.
007|106-110|P|RemoveTargetItem|91|Knock Off delegates a base-damage estimate: mechanics >=6 and transferable target item produce rounded 1.5 multiplier, even through current substitute/Sticky Hold.|P65 yields98 with eligible item; no item yields65; this estimates base power, not item loss.
007|111-124|ST|RemoveTargetItem|91|Removal preference rejects wild user, absent/unlosable target item, substitute, non-bypassed Sticky Hold, and inactive target item; subtracts four times target no-item gain.|Vitem9/Vnone0 gives +36; identical item disabled preserves s.
007|129-143|ST|DestroyTargetBerryOrGem|92|Destroy preference restricts berries or >=6 gems; incompatibility check uses U against target item; substitute, non-bypassed Sticky Hold, inactivity preserve s; then −4ΔT.|Gem at generation5 preserves s; generation6 transferable active V6 item gives +24.
007|148-156|FT|CorrodeTargetItem|93|Corrosion rejects absent/unlosable item, substitute, effective Sticky Hold without a bypass exception, and side/party slot already corroded.|Mold Breaker with Sticky Hold still fails; clear ordinary eligible target passes.
007|157-166|ST|CorrodeTargetItem|93|Corrosion adds four times target's no-item gain, opposite removal; inactive target difference is zero.|Active V9 to0 gives −36; inactive target gives0 local delta.
007|171-175|FT|StartTargetCannotUseItem|94|Embargo prediction only checks existing positive Embargo duration.|Duration1 fails; duration0 does not fail this dedicated check.
007|176-186|ST|StartTargetCannotUseItem|94|Embargo preference gives60 for missing/inactive/nonpositive-value item, otherwise twice current item value.|Active V9 yields+18; V0 or negative gives60, without estimating bag use.
007|191-227|S|StartNegateHeldItems|95|Magic Room duration1 returns nil and wrapper preserves input; held-item sum excludes inactive items only at medium, with room itself ignored while active; no items or wrong sum sign gives60; beneficial magnitude capped20.|W7 opening gives+20; W0 gives60; W−3 closing gives+12; remaining1 preserves s.
007|232-237|F|UserConsumeBerryRaiseDefense2|96|Stuff Cheeks fails unless U holds an active berry.|Berry inactive fails; ordinary berry active passes this check even if ordinary consumption barred.
007|238-263|S|UserConsumeBerryRaiseDefense2|96|Stuff Cheeks adds non-useless Defense2 score from0, preserves negative forced-consumption utility, then medium Cheek Pouch heal8, Harvest/Recycle8, ordinary-consume inability5, future Belch5, Unburden5.|With other terms0 and ordinary consumption barred, medium adds5; no HP/item/stage is submitted.
007|268-272|FT|AllBattlersConsumeBerry|97|Teatime rejects target without berry or semi-invulnerable; no item-active requirement in dedicated failure.|Disabled berry without semi-invulnerability passes; same target semi-invulnerable fails.
007|273-295|ST|AllBattlersConsumeBerry|97|Teatime uses preserving utility only for allies; same medium berry aftermath benefits, then negates for enemy target.|Enemy E−6 clamps0 so adds0; enemy E6 adds−6; ally E−6 remains−6 before general target synthesis.
007|300-324|ST|UserConsumeTargetBerry|98|Bug Bite/Pluck guards absent/nonberry, U incompatibility, substitute, non-bypassed Sticky Hold; adds clamped U consumption, medium U pouch8/Belch5 and T Unburden−5, then −3 target removal difference without active-item gate.|T V9→0 adds27 plus U utility; disabled T item still supplies valuation term if other guards clear.
007|329-337|F|ThrowUserItemAtTarget|99|Fling failure requires held active losable item, consume permission for berries, and any Fling_ prefix, not necessarily a complete numeric tag.|Fling_bad prefix can pass dedicated failure yet default base10; no held item fails when prediction enabled.
007|338-342|P|ThrowUserItemAtTarget|99|Fling delegates first complete numeric power flag with minimum10/default10 for held item; underlying no-item branch is0 if directly reached outside predicted eligibility.|Fling_5→10; Fling_130→130; malformed prefix held item→10; absent item underlying0.
007|343-376|ST|ThrowUserItemAtTarget|99|Fling delegates ordinary poison/burn/paralysis/flinch for six harmful items; otherwise subtracts clamped target consumption utility; medium berry Belch benefit−5 and U Unburden+5; twice user's no-item gain last.|Toxic Orb routes ordinary poison, not toxic expected loss; non-effect item with U Δ7 adds14; no actual item discarded.
008|4-16|S|RedirectAllMovesToUser|121|Follow Me/Rage Powder useless without ally; HPAware and U above integer two-thirds gives10 for each ally at/below integer one-third.|U H100/h67, ally h33/H100 gives+10; U h66 gives0; no ally60.
008|21-32|ST|RedirectAllMovesToTarget|122|Spotlight enemy needs allies both beside target and user; otherwise local−20, including ally targets not subject to two enemy conditions.|Enemy in singles60; ally target with no further ally still s−20 before eventual inversion.
008|42-46|P|RandomlyDamageOrHealTarget|B58|Present predicts base50 as an approximate representative, without random expectation simulation.|Nominal random damage/heal outcomes all feed fixed50 at this medium base hook.
008|47-52|S|RandomlyDamageOrHealTarget|B58|Present overall preference always subtracts10.|s100→90 independent of target current HP or sampled gift.
008|57-61|FT|HealAllyOrDamageFoe|B128|Pollen Puff target failure only for ally currently unable to heal; enemy is not checked for healing eligibility.|Full-HP ally fails; full-HP foe passes this dedicated check.
008|62-75|ST|HealAllyOrDamageFoe|B128|Pollen Puff enemy preserves s; ally HPAware at least half subtracts10, below half adds integer missing-HP preference20 fraction.|H100/h49 ally +10; h50 ally−10; foe0 before generic damage/ally inversion.
008|80-97|F|CurseTargetOrLowerUserSpd1RaiseUserAtkDef1|128|Curse Ghost route includes current Ghost or rough Ghost with effective Protean/Libero; non-Ghost failure only if all requested raises and drops impossible centrally.|Non-Ghost all stage requests blocked fails; any one permitted passes; Ghost bypasses this stage gate.
008|98-105|FT|CurseTargetOrLowerUserSpd1RaiseUserAtkDef1|128|Ghost-route Curse rejects cursed target or indirect-damage immunity; non-Ghost path gives false.|Already cursed Ghost target fails; same effects on non-Ghost path do not fail this check.
008|106-114|S|CurseTargetOrLowerUserSpd1RaiseUserAtkDef1|128|Non-Ghost Curse first applies user raise helper with whole-effect default; local60 stops before speed drop; else drop helper uses whole=false.|Raise helper60 prevents speed-drop gain; Ghost preserves overall s.
008|115-139|ST|CurseTargetOrLowerUserSpd1RaiseUserAtkDef1|128|Ghost Curse HPAware at/below integer half returns60; turnCount<2 +10; medium no damage move+15/no target reserve+10; high ProtectMove knowledge+5.|H100/h50 with HPAware→60; h51 early/no damage/no reserve/protect yields+40; no actual HP cost.
008|144-182|ST|EffectDependsOnEnvironment|130|Secret Power prepares environment effect; codes2/10/0,1/9/7,11,13 delegate sleep/burn/paralysis/freeze/flinch. Intended stat cases leave stat variable empty and query ability-symbol key, preserving s with no registered key.|Cave code7 reaches flinch; water code5 keeps score rather than attack-drop benefit; chance is delegated helper bias, not expected-damage multiplication.
008|187-191|P|HitsAllFoesAndPowersUpInPsychicTerrain|B57|Expanding Force base estimate delegates terrain multiplier and grounding gate; targets still determined by real target query.|P81 grounded Psychic→121; ungrounded→81, separate from target average/multitarget10.
008|196-200|FT|TargetNextFireMoveDamagesTarget|124|Powder failure check tests existing Powder boolean only.|Existing true fails; false passes this dedicated check.
008|201-209|ST|TargetNextFireMoveDamagesTarget|124|Powder needs usable current calculated Fire move, gets10 and another10 if no usable non-Fire move; includes status moves.|One Fire status-only move yields+20; none Fire60; PP-exhausted Fire excluded.
008|214-222|S|DoublePowerAfterFusionFlare|B69|Fusion Bolt overall preference adds10 per living ally with available Fusion Flare function.|Two eligible allies +20; same-function ally0; no check of actual choices or order.
008|227-235|S|DoublePowerAfterFusionBolt|B69|Fusion Flare overall preference symmetrically adds10 per living ally knowing opposite fusion function.|One opposite-function ally+10; exhausted finite PP removes that evidence.
008|240-244|FT|PowerUpAllyMove|123|Helping Hand target failure checks existing HelpingHand boolean only.|True rejects; target already acted with false does not fail this dedicated check.
008|245-250|ST|PowerUpAllyMove|123|Helping Hand target preference60 without usable damaging move, otherwise+5; no additional overall score registration.|Target has damage move and already acted still local+5; overall default remains s.
008|255-259|P|CounterPhysicalDamage|B71|Counter fixed-damage base representative is60, not real recent damage.|Medium base60 irrespective of real recent physical damage; fixed-damage consumer returns it without ordinary damage multipliers.
008|260-282|S|CounterPhysicalDamage|B71|Counter needs movable foe with available physical move respecting U substitute unless ignored; each eligible enemy attack>special+5, medium previous physical+8, Taunt+5; none60.|One eligible stronger physical/last physical/taunted enemy adds18; frozen enemy cannot supply qualifying move.
008|287-291|P|CounterSpecialDamage|B71|Mirror Coat fixed-damage base representative60.|Same60 for last special loss0 or high loss; not true retaliatory damage computation.
008|292-314|S|CounterSpecialDamage|B71|Mirror Coat substitutes special qualification, special>attack comparison, prior special8 and Taunt5; same movement/substitute rules and empty60.|Eligible stronger special/prior special/taunted foe+18; only physical foe60.
008|319-323|P|CounterDamagePlusHalf|B71|Metal Burst fixed-damage base representative60.|60 represents output without multiplying actual incoming damage by1.5.
008|324-344|S|CounterDamagePlusHalf|B71|Metal Burst additionally excludes foes slower than U in wrapper comparison; any usable damage ignoring substitute as required; medium last damage+8/Taunt+5 but no stat-comparison bonus.|One slower foe cannot qualify; one faster last-damaging taunted foe adds13.
008|349-353|F|UserAddStockpileRaiseDefSpDef1|B127|Stockpile failure at count>=3 only.|Count2 passes; count3 fails even if stages could rise.
008|354-364|S|UserAddStockpileRaiseDefSpDef1|B127|Stockpile applies Defense/SpDef1 whole=false, then raw battler move-function knowledge of Spit Up/Swallow adds10/10/8/5 by count0/1/2/3.|Count2 with exhausted Spit Up still can add8 because direct raw function query, not available-move helper.
008|370-374|F|PowerDependsOnUserStockpile|B59|Spit Up whole failure only zero stockpile.|0 fails;1 passes this check.
008|375-379|P|PowerDependsOnUserStockpile|B59|Spit Up base delegates100 per stockpile.|Count1→100;2→200;3→300; not actual consumed-stage loss.
008|380-386|S|PowerDependsOnUserStockpile|B59|Spit Up overall preference subtracts5 below count2; ignores loss of stored stage buffs.|Count1−5;count2 unchanged; prediction-off count0 still local−5 if reached.
008|392-400|F|HealUserDependingOnUserStockpile|B127|Swallow fails at stockpile0 or cannot heal with both tracked stockpile defensive gains0.|Cannot-heal plus one tracked gain still passes this check, but next score may60.
008|401-413|S|HealUserDependingOnUserStockpile|B127|Swallow cannot heal→60; HPAware >=half returns s−10 immediately; otherwise missing-HP20 fraction, then low-stockpile−5 if not early returned.|H100/h50 stockpile1→s−10;h49→s+10−5; not s−15 at half.
008|418-426|S|GrassPledge|B228|Grass Pledge adds10 per ally with either Fire/Water Pledge available, at most once per ally.|Ally knows both alternatives→+10, not20; same pledge-only0.
008|431-439|S|FirePledge|B228|Fire Pledge adds10 per ally with Grass/Water alternative.|Two different qualifying allies→20; no actual combined side effect forecast.
008|444-452|S|WaterPledge|B228|Water Pledge adds10 per ally with Grass/Fire alternative.|One exhausted alternative finite PP0 alone→0; usable alternative→10.
008|460-465|F|UseLastMoveUsed|112|Copycat only checks original function if preparation could not replace it; empty/unknown last global move or function blacklist predicts failure.|Valid allowed previous move is substituted before this dedicated failure; missing stays original and fails.
008|473-479|FT|UseLastMoveUsedByTarget|113|Mirror Move original failure checks target regular last identity/data and CanMirrorMove flag; successful target preparation replaces original evaluation.|Flagged valid move uses replacement handlers; unflagged current record fails original target check.
008|484-488|FT|UseMoveTargetIsAboutToUse|114|Me First predicts failure if no usable damaging, nonblacklisted target move.|One legal damage move passes despite target's actual planned status move; all banned fails.
008|489-498|ST|UseMoveTargetIsAboutToUse|114|Me First gives60 if target wrapper-faster; else−8 if target has any usable status or banned move; no1.5 damage preview.|Faster T60; slower T with legal damage plus status gives−8; all ordinary damage preserves.
008|514-530|F|UseRandomMoveFromUserParty|115|Assist scans entire same-side party except missing and U party index; eggs excluded only>=6; any nonblacklisted/non-Shadow move suffices, without fainted or PP filter.|Fainted member PP0 eligible move passes;>=6 sole egg candidate fails; no probability average computed.
008|535-546|F|UseRandomUserMoveIfAsleep|116|Sleep Talk scans own actual indexed moves and real sleep-talk selection mode, after blacklist; any legal slot passes.|Allowed nonblacklisted slot passes; all mode-ineligible fail; normal asleep pre-gate separate.
008|551-568|S|BounceBackProblemCausingStatusMoves|119|Magic Coat60 if U effective Magic Bounce; otherwise+5 each movable enemy with usable reflectable status, no such enemy60; HPAware below integer half truncates missing-HP penalty20 fraction.|H100/h40 and one qualifying foe:5−12=−7 delta; magic-bounce U returns60 before foe scan.
008|573-589|S|StealAndUseBeneficialStatusMove|120|Snatch+5 each movable enemy with usable snatchable status, none60; same HPAware low HP penalty, no Magic Bounce guard.|H100/h40 two qualified foes:10−12=−2 delta; only allied snatchable move does not count.
008|594-598|F|ReplaceMoveThisBattleWithTargetLastMoveUsed|117|Mimic whole failure if transformed U or current moves do not contain this original move identity.|Transformed U fails; ordinary U with Mimic passes whole check before target prediction.
008|599-609|FT|ReplaceMoveThisBattleWithTargetLastMoveUsed|117|Mimic target failure only when U wrapper-faster, then rejects unknown target regular move, already known, blacklist or Shadow type.|Slower U with unknown record returns false; faster U with same record true.
008|610-620|ST|ReplaceMoveThisBattleWithTargetLastMoveUsed|117|Mimic target score−10 and+5 if U wrapper-faster.|Fast U−5;slow U−10, independent of future copied utility.
008|625-626|FT|ReplaceMoveWithTargetLastMoveUsed|118|Sketch successfully copies Mimic target failure behavior within same registry; does not copy whole transformed/own-slot check.|Slower Sketch with invalid old record dedicated target prediction false; faster true.
008|627-628|S|ReplaceMoveWithTargetLastMoveUsed|118|Sketch overall copy looks for absent Mimic overall source, creates no destination; target-score penalty is not imported.|Normal Sketch lacks −5/−10 copy preference; overall wrapper default preserves s.
009|4-8|F|FleeFromBattle|138|Escape predicts failure from real cannot-run or wild U with living ally.|Wild U with one living ally fails; same ally fainted no longer counted.
009|9-14|S|FleeFromBattle|138|Escape overall local preference−20.|s100→80 without ending battle during evaluation.
009|19-26|F|SwitchOutUserStatusMove|138|Status pivot wild path uses escape gates; trainer path requires real selectable reserve.|Wild ally blocks; trainer with no legal reserve fails independently of can-run.
009|27-57|S|SwitchOutUserStatusMove|138|Status pivot wild−20; trainer ReserveLastPokemon with exactly1 reserve60; else Perish20/confusion>1 10/Attract10, positive stage>=2−15 else negative+10, residual positive15/negative−15, no damage+10, three hazards−10 each.|Trainer reserve-last early60 hides all later gains; without flag Perish+20 plus one hazard−10 gives+10.
009|62-88|S|SwitchOutUserDamagingMove|140|Damaging pivot no reserve preserves s; reserve-last1 subtract20 then same statuses/stages/residual/hazards, no no-damage bonus.|No reserve0 delta; sole reserved ace+Perish cancels−20+20=0, not local60.
009|93-103|FT|LowerTargetAtkSpAtk1SwitchOutUser|142|Parting Shot predicts failure only if every requested central stat drop unavailable.|One of Attack/SpAtk droppable passes even without user reserve.
009|104-108|ST|LowerTargetAtkSpAtk1SwitchOutUser|142|Parting Shot target preference invokes stat-drop helper whole=false for actual requested drops.|No reserve still receives stat-drop evaluation; no automatic pivot gain.
009|109-110|ST|LowerTargetAtkSpAtk1SwitchOutUser|142|Parting Shot later copy has absent source in target-score registry; prior stat-drop binding survives unchanged.|Same stat-only result with/without hypothetical successful pivot; not two handler sums.
009|115-119|F|SwitchOutUserPassOnEffects|144|Baton Pass whole failure if no legal reserve.|Zero legal reserve true; any legal reserve false independent of current boosts.
009|120-159|S|SwitchOutUserPassOnEffects|144|Baton Pass reserve-last−20, bad effects with exact durations, positive transferable effects, prioritized stage bins25/15/−15, residual±15, no damage+15, hazards−10 each.|Perish positive−20 plus one stage+4 +25 gives+5; negative stage does not override a+4.
009|164-168|FT|SwitchOutTargetStatusMove|146|Status phazing delegates current real target-failure query.|Dedicated AI check has same immediate eligibility as that move's real current target query; no successful replacement simulated.
009|169-195|ST|SwitchOutTargetStatusMove|146|Status phazing wild−10 early; trainer Perish positive60; HPAware <=integer third−10; target positive stage15 else negative−15; residual damage−15/heal15; three hazards+10 each.|Wild with hazards still early−10; trainer Perish ignores otherwise positive stage/hazard gains.
009|200-233|ST|SwitchOutTargetDamagingMove|146|Damaging phazing wild preserves; effective Suction Cups without bypass/Ingrain/no switch-in/current substitute preserve; then Perish−20 and stage/residual/hazard terms, without lowHP penalty.|Current substitute preserves even if damage will break it; trainer with Perish and hazard one gives−10.
009|238-272|ST|BindTarget|150|Binding preserves for existing trapping/substitute; active band/claw5, indirect harm10; newly trappable8/residual±10/Perish15; if trap or damage useful, medium clearing-move penalty10.|Eligible active-band, indirect, trappable, residual+,Perish gives48; clearing move medium reduces38; prior bind0 delta.
009|277-281|P|BindTargetDoublePowerIfTargetUnderwater|150|Whirlpool folds real diving terminal multiplier into power estimate.|P35 diving→70; not diving→35; separate from fixed binding score.
009|282-283|ST|BindTargetDoublePowerIfTargetUnderwater|150|Whirlpool successfully copies BindTarget target score at registration time.|Same48 binding example; no added score solely from copy occurrence.
009|288-295|FT|TrapTargetInBattle|152|General trap target failure applies only status moves and existing MeanLook>=0 or MORE_TYPE_EFFECTS Ghost.|Damaging variant false despite Ghost; status Ghost rejected only when type-effects flag on.
009|296-324|ST|TrapTargetInBattle|152|Cannot newly trap/no reserve/residual lethal/medium clearing makes status60 but damage preserve; additional-effect−999 preserves; else helper bias plus one15 if Perish/Attract/confusion>0/residualpositive.|No reserve status60 vs damage s; confusion1 still+15; simultaneous four bad states still one15.
009|329-330|FT|TrapTargetInBattleMainEffect|152|Main-effect variant successfully copies general trap failure.|Status variant existing MeanLook fails; damage variant not rejected by this dedicated gate.
009|331-332|ST|TrapTargetInBattleMainEffect|152|Main-effect variant copies exact trap target preference, including additional-effect helper handling.|No reserve status60; helper−999 preserves s after earlier value guards.
009|337-344|FT|TrapTargetInBattleLowerTargetDefSpDef1EachTurn|154|Octolock status failure uses Octolock>=0 or MORE_TYPE_EFFECTS Ghost; damaging case bypasses.|Octolock existing index0 counts; default−1 does not.
009|345-370|ST|TrapTargetInBattleLowerTargetDefSpDef1EachTurn|154|Octolock first computes two defensive drops whole=false; only if target can newly trap and has reserve, residual lethal or clearing move at any skill yields status60/damage current score; else bad-status15 once.|Cannot trap still preserves stat-drop score; clearing move low skill still no trap bonus unlike general trap.
009|375-401|ST|TrapUserAndTargetInBattle|154|Mutual trap ignores user's trapping cost; if T newly trappable with reserve, residual lethal/medium clearing gives status60 or damage preserve; bad-state15 once; no base8.|Ordinary trappable target without bad states0 delta; Perish gives15, not23.
009|406-410|F|TrapAllBattlersInBattleForOneTurn|154|Fairy Lock whole failure existing positive field duration.|1 fails;0 passes.
009|411-416|S|TrapAllBattlersInBattleForOneTurn|154|Fairy Lock overall score−10.|s100→90; no real trapping state committed.
009|426-436|F|UsedAfterUserTakesPhysicalDamage|156|Shell Trap predicts failure if no foe has available physical move; ignores foe can_attack here.|Frozen foe knowing physical can make dedicated failure false; all special foes true.
009|437-451|S|UsedAfterUserTakesPhysicalDamage|156|Shell Trap U substitute60; otherwise no foe with special+10 and unconditional−10; no true trigger forecast.|Only physical foes net0; mixed or special knowledge net−10; substitute60.
009|456-470|S|UsedAfterAllyRoundWithDoublePower|158|Round scans living same side including U; any available same-function move yields10 once.|U alone with available Round +10; finite PP0 excluded so no guarantee of ally.
009|475-500|ST|TargetActsNext|162|After You rejects foe, rough-speed position before U or distance<=1; sorted low-to-high during current Trick Room else high-to-low; success+10 before general inversion.|Order U,foe,T gives+10;U,T,foe gives60; actual priority ignored.
009|505-535|ST|TargetActsLast|162|Quash needs enemy T and movable ally; sorted current rough speed, reject T before U/alreadylast/slowest ownside before T; success−10.|Order U,T,ally permits−10;U,ally,T gives60; slowest ownside includes U but movable-other prerequisite independent.
009|540-544|FT|TargetUsesItsLastUsedMoveAgain|164|Instruct dedicated failure only existing multiturm-attack state.|Ongoing multi-turn true; all other execution failure gates not reproduced here.
009|545-569|ST|TargetUsesItsLastUsedMoveAgain|164|Instruct rejects enemy/faster T/missing regular last move; first matching current slot selected, finite PP0 or blacklist60; otherwise+10.|Duplicate firstPP0,lastPP2→60; firstPP2,lastPP0→+10; real execution lookup differs.
009|574-608|S|StartSlowerBattlersActFirst|166|Trick Room gathers living rough speeds and independently doubles Tailwind>1/halves Swamp>1, even if rough-speed already included; empty side60; current room>1 transforms speeds for comparison; allies all faster60, enemies all faster20, lower ally integer mean10, else−10.|Ordinary allies100 enemies200 gives+20; room>1 reverses relation→60; room1 retains+20; high skill Tailwind can count twice.
009|618-633|ST|LowerPPOfTargetLastMoveBy3|170|PP3 additional-effect−999 preserves; U faster with found last regular slot and totalPPpositive adds helper then pp<=3 +20/<=5 +10/>9−10; otherwise keeps.|Fast pp3 helper5→+25;pp6 helper5→+5;slow keeps even helper5.
009|638-642|FT|LowerPPOfTargetLastMoveBy4|171|Spite target failure if no usable move matches regular-last identity.|Last finitePP0 unavailable→true; totalPP0 matching identity can pass.
009|643-653|ST|LowerPPOfTargetLastMoveBy4|171|Spite fast uses last slot: pp<=4 +20/<=6 +10/>10−10; all other paths−10 including slow and pp7..10. Missing slot dereference can fail with prediction disabled.|Fast6→+10;7→−10;11→−10;slow3→−10; fast missing slot throws before normal output.
009|658-664|FT|DisableTargetLastMoveUsed|172|Disable rejects current positive duration, absent regular-last, Aroma Veil failure, no available matching slot.|Duration1 true; exhausted finite last slot true; legal matching move false.
009|665-680|ST|DisableTargetLastMoveUsed|172|Disable active Mental Herb60; else+5, any lock field/effective choice item/Gorilla Tactics+10 once, last data damaging+8.|Ordinary recent damage+13; lock+damage+23; Mental Herb60 regardless of other gains.
009|685-691|FT|DisableTargetUsingSameMoveConsecutively|173|Torment rejects existing boolean or Aroma Veil guard.|Existing true fails; no last-move requirement.
009|692-705|ST|DisableTargetUsingSameMoveConsecutively|173|Torment active Mental Herb60; else+10 plus same choice-lock group10 once.|Both choice item and Gorilla still only+20 total; no recent-damage8 unlike Disable.
009|710-721|FT|DisableTargetUsingDifferentMove|174|Encore rejects existing duration, absent/unknown/blacklisted regular-last, ShellTrap, Aroma Veil, or missing usable matching move.|Unknown last data fails; legal but PP0 finite matching slot fails; valid clear case passes.
009|722-757|ST|DisableTargetUsingDifferentMove|174|Encore Mental Herb60; fast U uses actual last data: status User/BothSides10/other8, damage NearOther/Other original-type effectiveness immunity20/resist15/super−8/normal8; slow10.|Fast original-type neutral eligible damage+8;immune20;super−8;slow+10 independent of old move usefulness.
009|762-770|FT|DisableTargetStatusMoves|175|Taunt rejects active duration/Aroma Veil or >=6 Oblivious effective without bypass.|Generation5 Oblivious not this rejection; generation6 bypass cancels only ability gate.
009|771-810|ST|DisableTargetStatusMoves|175|Taunt needs usable status; long actual sleep with no sleep-status60; empty choice lock plus effective choice/Gorilla60; raw usable status slots+5 each; ten protection functions give10 once.|Two usable status slots one protect→+20; same item with populated lock can continue, empty lock60.
009|815-821|FT|DisableTargetHealingMoves|176|Heal Block rejects existing positive duration/Aroma Veil.|Duration1 fails; unlike utility Mental Herb thresholds here no >1 boundary.
009|822-835|ST|DisableTargetHealingMoves|176|Heal Block needs usable healing move or active Leftovers/active Black Sludge on Poison T; otherwise60; eligible+10.|Only non-Poison Black Sludge60; Poison Sludge+10 even absent healing move.
009|840-852|ST|DisableTargetSoundMoves|177|Throat Chop existing duration>1 or no usable sound preserves; helper−999 preserves; otherwise helper adjustment+8.|Duration1 sound with helper5→+13;duration2 keeps s;Sheer Force suppression keeps.
009|857-861|F|DisableTargetMovesKnownByUser|178|Imprison whole failure only existing U Imprison boolean.|False passes whole check regardless of enemy overlap;true fails.
009|862-877|ST|DisableTargetMovesKnownByUser|178|Imprison target-score registration scans foes for one usable overlap with any raw own slot, stops first, then60 for0/+8 for1. Ordinary User target-count0 never calls it.|Two overlapping foes direct handler+8 not16; normal Imprison target-count0 leaves overall default100 absent other modifiers.
'''

consumer = {
 'F': {'path':'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/005_AI_ChooseMove.rb','start':177,'end':191,'gate':'PredictMoveFailure; whole prediction before target enumeration; rejection gives20'},
 'FT': {'path':'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/005_AI_ChooseMove.rb','start':196,'end':225,'gate':'PredictMoveFailure and actual target path; rejection gives−1 and may leave no-target failure20'},
 'S': {'path':'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/005_AI_ChooseMove.rb','start':232,'end':285,'gate':'ScoreMoves; after target combination; then generic whole modifiers, truncate, clamp'},
 'ST': {'path':'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/005_AI_ChooseMove.rb','start':294,'end':323,'gate':'ScoreMoves and enumerated actual target; targetless User does not enter; generic target modifiers and optional ally inversion follow'},
 'P': {'path':'reference/pokemon-essentials/Data/Scripts/011_Battle/005_AI/011_AIMove.rb','start':79,'end':106,'gate':'medium>=32 and rough-damage consumer reached; low skill does not call this registry; fixed-damage returns power estimate directly'},
}
rows=[]
for raw in DATA.strip().splitlines():
    file, interval, receiver, name, clause, fact, vector = raw.split('|')
    start,end=map(int,interval.split('-'))
    formal_path=B if clause.startswith('B') else F
    formal_line=int(clause.lstrip('B'))
    path=str((SRC/FILES[file]).relative_to(ROOT))
    source_line=(ROOT/path).read_text().splitlines()[start-1]
    operation='copy' if '.copy(' in source_line else 'add'
    status='SOURCE_STATIC_MATCH_WITH_PRECONDITIONS'
    if (file,start) in [('008',627),('009',109)]: status='COPY_SOURCE_ABSENT_NOT_A_SECOND_EXECUTING_SCORE'
    if (file,start)==('009',862): status='HANDLER_MATCH_ORDINARY_TARGETLESS_CONSUMER_NOT_ENTERED'
    coverage_lines={'007':{'F':58,'FT':54,'S':60,'ST':56,'P':62},
      '008':{'F':70,'FT':72,'S':66,'ST':68},
      '009':{'F':78,'FT':82,'S':80,'ST':84,'P':86}}
    coverage_path=C
    if formal_path==B:
        coverage_path=BC
        coverage_line={'P':78,'S':80,'F':86,'FT':82,'ST':84}[receiver]
    else:
        coverage_line=coverage_lines[file][receiver]
    if file=='008' and start==627: coverage_line=74
    rows.append({'unit_id':f'EC-{file}-{start:03d}', 'source':{'path':path,'start':start,'end':end},
        'registration':{'receiver':REG[receiver],'operation':operation,'destination_identity':name},
        'fact':fact, 'necessary_consumer':consumer[receiver],
        'formal':{'path':formal_path,'line':formal_line,'clause':('WP52-B' if formal_path==B else 'WP52-C')+' behavioral row/paragraph'},
        'formal_coverage':{'path':coverage_path,'line':coverage_line,'clause':REG[receiver]+'/'+name},
        'independent_vector':vector,'disposition':status,'semantic_review':'HAND_READ_AND_REASONED',
        'evidence':'SOURCE_STATIC + DERIVED_VECTOR',
        'probability':'No random outcome sampled. Additional-effect helper only supplies −999/0/5 bias where named; final WP51 weight selection separate.',
        'exceptions_and_partial_commit':'If this scoring invocation raises, candidate-local outer diagnostic block may retain initialized100; no general rollback of prepared fields. Failure prediction exceptions occur outside the local scoring block. No real move effect/resource commit by these handlers.',
        'aggregate_pass':False})
    if file=='008' and start in [255,287,319]:
        rows[-1]['ordinary_consumption']={
          'status':'NOT_ENTERED_FOR_DEFAULT_NONE_TARGET_ORDINARY_MOVE_SCORING',
          'reason':'Default Counter/Mirror Coat/Metal Burst use None, whose number of selectable targets is0. Whole-score handlers execute; generic target damage and these base estimates do not execute in ordinary scoring absent another explicit rough-damage caller.',
          'sources':['PBS/moves.txt:2255-2265,7278-7288,8205-8214','010_Data/001_Hardcoded data/017_Target.rb:26-33,53-57','011_Battle/005_AI/005_AI_ChooseMove.rb:45-56,232-285'],
          'formal_status':'WP52-B line13 and catalog line144 qualify local hook/base values; line71 is not evidence of normal base60 consumption.'}
    if (file,start) in [('009',475),('009',545),('008',62)]:
        rows[-1]['ordinary_consumption']={
          'status':'DEFAULT_SINGLE_TARGET_FOE_FILTER_EXCLUDES_ALLY_BRANCH',
          'reason':'Default After You/Instruct/Pollen Puff use NearOther with targets_foe true. Ordinary single-target candidate loop removes allies. After You/Instruct foe branch gives60; Pollen Puff foe branch preserves local input then generic damaging modifiers can act. Positive ally-only local formulas do not establish ordinary ally candidates.',
          'sources':['PBS/moves.txt:53-62,5687-5694,7460-7468','010_Data/001_Hardcoded data/017_Target.rb:136-141','011_Battle/005_AI/005_AI_ChooseMove.rb:57-69'],
          'formal_status':'WP51 line132 explicitly documents extra foe filtering;C162/164 and B128/catalog cases are local branches subject to this shared consumer.'}

inventory=[]
for key,filename in FILES.items():
    lines=(SRC/filename).read_text().splitlines()
    for num,line in enumerate(lines,1):
        m=re.search(r'Handlers::(\w+)\.(add|copy)\(',line)
        if m: inventory.append((key,num,m.group(1),m.group(2)))
mapped=[(r['unit_id'].split('-')[1],r['source']['start'],r['registration']['receiver'],r['registration']['operation']) for r in rows]
assert set(mapped)==set(inventory), {'unmapped':list(set(inventory)-set(mapped)), 'extraneous':list(set(mapped)-set(inventory))}
assert len(rows)==len(inventory)==119
def jsonl(name,values):
    (OUT/name).write_text(''.join(json.dumps(v,ensure_ascii=False)+'\n' for v in values))
jsonl('forward-matrix.jsonl',rows)
reverse=[]
for r in rows:
    reverse.append({'clause':r['formal'], 'source_unit':r['unit_id'], 'source':r['source'],
        'supporting_fact':r['fact'], 'consumer_preconditions':r['necessary_consumer'],
        'boundary_vector':r['independent_vector'],'status':r['disposition'],'aggregate_pass':False})
    reverse.append({'clause':r['formal_coverage'],'source_unit':r['unit_id'],'source':r['source'],
        'supporting_fact':'Exact family/identity/operation located; callable result separately reasoned in forward matrix.',
        'consumer_preconditions':r['necessary_consumer'],'status':'COVERAGE_IDENTITY_CHECKED_NOT_SEMANTIC_PASS_BY_INDEX','aggregate_pass':False})
jsonl('reverse-matrix.jsonl',reverse)
jsonl('unit-inventory.jsonl',[{'source_file':key,'start':line,'receiver':registry,'operation':op,'classification':'STRUCTURAL_INVENTORY_ONLY'} for key,line,registry,op in inventory])
semantic=[]
for key,filename in FILES.items():
    data=(SRC/filename).read_bytes()
    semantic.append({'kind':'semantic_review_completed_for_assigned_file','path':str((SRC/filename).relative_to(ROOT)),
      'start':1,'end':len(data.decode().splitlines()),'sha256':hashlib.sha256(data).hexdigest(),
      'reviewed_units':sum(1 for r in rows if r['unit_id'].startswith('EC-'+key)),
      'record':'forward-matrix.jsonl/reverse-matrix.jsonl', 'not_runtime_pass':True,
      'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
with (OUT/'reading-ledger.jsonl').open('a') as f:
    for r in semantic:f.write(json.dumps(r,ensure_ascii=False)+'\n')
print(json.dumps({'actual_structural_registration_count':len(inventory),'manually_reasoned_rows':len(rows),
 'by_file':dict(collections.Counter(r['unit_id'].split('-')[1] for r in rows)), 'missing_rows':0},ensure_ascii=False))
