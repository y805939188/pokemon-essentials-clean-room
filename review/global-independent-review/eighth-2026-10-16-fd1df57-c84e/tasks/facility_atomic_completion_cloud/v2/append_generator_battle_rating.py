import pathlib,json,datetime,subprocess,hashlib
V=pathlib.Path(__file__).parent;NOW=datetime.datetime.now(datetime.timezone.utc).isoformat();R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
F=json.loads((V/'forward-mapping.json').read_text());REV=json.loads((V/'reverse-mapping.json').read_text());assert len(F['atoms'])==1689
rows=[]
def a(unit,meaning,receiver,source='R22'):rows.append((source,unit,meaning,receiver))
for unit,meaning,receiver in [
 ('RuledTeam.initialize8','Team sampling count is rule.ruleset.suggestedNumber.','F12§6.3L133:sample-count'),
 ('RuledTeam.initialize9–16','Each attempted team is assigned selected party object references, with each random index removed immediately from the supplied party pool.','F12§6.3L133:destructive-sampling'),
 ('RuledTeam.initialize17–18','Only the completed sampled team is rulevalidated; failure restarts sampling without returning removed prior-attempt members to the pool.','F12§6.3L133:invalid-attempt-pool-loss'),
 ('RuledTeam.initialize11–18','Team rejection loop has no iteration bound or explicit exhausted-pool fallback.','F12§6.3L133/§10L256,259:no-team-sampling-cap'),
 ('RuledTeam.initialize19','A successfully constructed new team starts settled totalGames0.','F12§6.3L134/§7.4L190:new-settled-games'),
 ('RuledTeam.initialize20','A new team creates the active PlayerRating implementation.','F12§6.3L134:active-rating-object'),
 ('RuledTeam.initialize21','New history binds to that same new rating object.','F12§6.3L134/§7.4L182:history-binding'),
 ('RuledTeam.team5/[24–26','Team getter/setter and indexer expose the stored team member array/references, not snapshots.','F12§6.3/§7.2:team-reference-boundary'),
 ('RuledTeam.length28–30','Team length reports current team array length.','F12§6.4L145:member-count-consumer'),
 ('RuledTeam.rating32–34','Team rating used by sorting/match estimates is cached winChancePercent, not raw numericR.','F12§7.4L189:display-rating-consumer'),
 ('RuledTeam.ratingData36–38','ratingData returns the underlying rating object reference.','F12§7.4L182:rating-source-object'),
 ('RuledTeam.ratingRaw40–42','ratingRaw requests [rawR,rawD,rawsigma,displayPercent] in that order.','F12§7.4L179,189:audited-raw-rating-reader'),
 ('RuledTeam.compare44–46','Direct team.compare forwards to @rating.compare; active PlayerRating class in this file supplies no compare implementation. This helper is not part of the shown generator consumers.','F12§7/§12L277:audited-internal-compare-boundary'),
 ('RuledTeam.totalGames48–50','Visible totalGames equals falsey-settled fallback0 plus current history length.','F12§6.4L142/§7.4L190:visible-games-sum'),
 ('RuledTeam.addMatch52–54','Adding a match passes the opponent rating object and supplied score into this team own history.','F12§7.4L182:match-append-owner'),
 ('RuledTeam.games56–58','Unsettled games is exactly history length.','F12§7.4L190:pending-games'),
 ('RuledTeam.updateRating60–66','Update initializes a falsey settled counter0, records old history size, updates/clears history, records new size, then adds old−new to settled total.','F12§7.4L190:games-settlement-order'),
 ('RuledTeam.updateRating60–66','Normally cleared n-match history adds n once to settled total, preserving visible C+n; a repeated successful empty history adds0.','F12§7.4L190/§7.4aL200–204:games-conservation'),
 ('RuledTeam.updateRating60–66','A rating update exception before history clear prevents the final settled increment; no ensure rolls back earlier rating writes.','F12§7.4L191/§7.4aL205:rating-failure-prefix'),
 ('RuledTeam.toStr68–70','Direct toStr requests @rating.to_i and @games.to_i; active rating defines no to_i and the team constructor doesnot set @games. This unconsumed helper is audited, not promised as a public string API.','F12§7/§12L277:audited-toStr'),
 ('RuledTeam.load72–78','Direct load uses stored team entries as party indexes; freshly constructed teams hold Pokemon objects, so that representation is not automatically an index list. No default generator load caller was found.','F12§6.3/§12L277:audited-load-representation'),
 ('SingleMatch.initialize90–95','Single match snapshots the opponent rating numeric value at append time.','F12§7.4L182:opponent-rating-snapshot'),
 ('SingleMatch.initialize90–95','Single match snapshots opponent deviation numeric value at append time.','F12§7.4L182:opponent-deviation-snapshot'),
 ('SingleMatch.initialize93','Single match retains score−1/0/1 as supplied without mapping draw to0.5 here.','F12§7.4L182,185:raw-score'),
 ('SingleMatch.initialize90/94','Single match default K value is16 and stored as supplied. Active variant update doesnot consume that field.','F12§7.4L192:auxiliary-K-field'),
 ('MatchHistory.initialize104–107','History starts an empty matches array and retains its owning rating reference.','F12§6.3L134:history-initialization'),
 ('MatchHistory109–119','History index, length and each expose/iterate its stored matches in order.','F12§7.4L182:history-ordered-consumption'),
 ('MatchHistory.addMatch121–124','Appending constructs a SingleMatch from opponent currentR/D and result, preventing later opponent rating updates from retroactively changing that snapshot.','F12§7.4L182:append-time-snapshot'),
 ('MatchHistory.updateAndClear126–129','Owner rating update happens before matches.clear; error from update leaves the pending history present.','F12§7.4L190–191:update-before-clear'),
 ('PlayerRatingElo.initialize140–145','Unused Elo initializes R1600.0,D0,sigma0 and nil display cache.','F12§7.4L192:unused-Elo-defaults'),
 ('PlayerRatingElo.K138','Unused Elo declares K_VALUE16.','F12§7.4L192:unused-Elo-K'),
 ('PlayerRatingElo.win147–152','Unused Elo returns existing truthy cache or computes1/(1+10^((R−1600)/400)), with an x==0 fallback1.0.','F12§7.4L192:unused-Elo-display'),
 ('PlayerRatingElo.update154–163','Empty Elo history returns before mutations; nonempty loops without binding a match variable and fails upon match.score lookup in the default class binding.','F12§7.4L192:unused-Elo-nonempty-failure'),
 ('PlayerRatingElo.update158–162','The uncompleted Elo update text would map draw to0.5 and accumulate kValue×(score−e), but no usable nonempty update is inferred.','F12§7.4L192:unused-Elo-unreached-tail'),
 ('PlayerRating.initialize175','Active rating starts R1500.0.','F12§7.4L179:active-R0'),
 ('PlayerRating.initialize176','Active rating starts D350.0.','F12§7.4L179:active-D0'),
 ('PlayerRating.initialize177','Active rating starts volatility0.9 in its original scale.','F12§7.4L179,181:active-sigma0'),
 ('PlayerRating.initialize178','Active display cache begins nil.','F12§7.4L189:display-cache-initial'),
 ('PlayerRating.win181–183','A truthy cached display is reused; otherwise deviation>100 selects the Smogon branch and≤100 selects GLIXARE.','F12§7.4L189:display-cache-and-threshold'),
 ('PlayerRating.win185–189','Smogon branch compares to fixed otherR1500/otherD350, computes s=sqrt(100000+D²+350²), then percent=100/(1+10^((1500−R)×0.79/s)).','F12§7.4L189:Smogon-formula'),
 ('PlayerRating.win192–195','GLIXARE computes sqrt(15.905694331435×(D²+221781.21786254)), inner=(1500−R)×pi/sqr, then (10000/(1+10^inner)+0.5)/100.','F12§7.4L189:GLIXARE-formula'),
 ('PlayerRating.rating2248–250','Normalized rating is(R−1500)/173.7178.','F12§7.4L181:rating-scale'),
 ('PlayerRating.deviation2252–254','Normalized deviation isD/173.7178.','F12§7.4L181:deviation-scale'),
 ('PlayerRating.volatility2246','volatility2 aliases the raw volatility reader; it doesnot divide by173.7178.','F12§7.4L181:raw-volatility-alias'),
 ('PlayerRating.update200–207','Empty history changes only deviation via sqrt(phi²+sigma²), then returns before R/sigma setters.','F12§7.4L188:empty-history-inflation'),
 ('PlayerRating.getG256–260','Each g divides opponent rawD by173.7178, then uses1/sqrt(1+3×D2²/pi²).','F12§7.4L183:g-factor'),
 ('PlayerRating.getE262–267','Each e normalizes opponent rawR then uses1/(1+exp(−g×(ownR2−opponentR2))).','F12§7.4L183:e-factor'),
 ('PlayerRating.update211–216','Nonempty update computes g/e and retains every match raw score in index order.','F12§7.4L182–185:all-record-inputs'),
 ('PlayerRating.update218–222','Variance is the reciprocal of the sum g²×e×(1−e), including draw records.','F12§7.4L184:variance-all-matches'),
 ('PlayerRating.update224–228','Improvement sum adds g×(score.to_f−e) only when score!=−1; draws contribute no improvement term.','F12§7.4L185:draw-excluded-improvement'),
 ('PlayerRating.update229','Volatility update consumes old sigma, old phi, computed variance/improvement sum and system parameter, default1.2.','F12§7.4L186:volatility-inputs'),
 ('PlayerRating.update231–232','New normalized deviation uses t=oldphi²+newSigma² and1/sqrt(1/t+1/variance).','F12§7.4L187:new-sigma-before-deviation'),
 ('PlayerRating.update234','New normalized rating adds newPhi²×improvementSum.','F12§7.4L187:new-deviation-before-rating'),
 ('PlayerRating.update235–237','Nonempty update commits rating setter, deviation setter, then volatility setter in that order.','F12§7.4L187,191:rating-commit-order'),
 ('PlayerRating.setRating273–276','Rating setter invalidates display cache and rescales value×173.7178+1500.','F12§7.4L187,189:rating-setter-cache'),
 ('PlayerRating.setDeviation278–281','Deviation setter invalidates display cache and rescales value×173.7178.','F12§7.4L187,189:deviation-setter-cache'),
 ('PlayerRating.setVolatility269–271','Volatility setter stores its value without a scale conversion or display-cache invalidation.','F12§7.4L181,187:volatility-setter'),
 ('PlayerRating.volatility284','Volatility improvement i0 is improvementSum×variance.','F12§7.4L186:improvement-scale'),
 ('PlayerRating.volatility285','Volatility iteration starts a=log(oldSigma²).','F12§7.4L186:iteration-log-start'),
 ('PlayerRating.volatility286–289','Iteration precomputes system²,phi²,2×variance,and phi²+variance.','F12§7.4L186:iteration-precomputed-terms'),
 ('PlayerRating.volatility290–291','x0 starts at a for each update, and loop permits at most100 iterations.','F12§7.4L186:iteration-start-and-limit'),
 ('PlayerRating.volatility292–295','Each iteration computes e=exp(x), d=phi²+variance+e, d² and i=i0/d.','F12§7.4L186:iteration-intermediates'),
 ('PlayerRating.volatility296','h1=−(x−a)/system²−0.5×exp(x)×i².','F12§7.4L186:Newton-h1'),
 ('PlayerRating.volatility297–298','h2=−1/system²−0.5×e×(phi²+v)/d²+v×e×(phi²+v−e)/d³; source0.5×(v+v) equals v.','F12§7.4L186:Newton-h2'),
 ('PlayerRating.volatility299–301','Iteration retains oldx, updates x−=h1/h2, and stops only for absolute step<0.000001 or loop exhaustion.','F12§7.4L186:Newton-step-stop'),
 ('PlayerRating.volatility303','Volatility result is exp(finalx/2); source supplies no separate convergence-success result.','F12§7.4L186/§10L261:volatility-return-boundary'),
 ('WinnerEffectiveness310–312','Estimator returns0 immediately for a Move data power0, regardless of other effect metadata.','F12§7.3L174:zero-power-exclusion'),
 ('WinnerEffectiveness313–315','Otherwise it starts typemod1.0; exact ability idLEVITATE plus move typeGROUND skips both type queries.','F12§7.3L174:Levitate-skip'),
 ('WinnerEffectiveness316–317','Normal estimator queries first defender type; second identical type contributes1.0 instead of duplicate effectiveness query.','F12§7.3L174:two-type-components'),
 ('WinnerEffectiveness318–320','Exact ability idWONDERGUARD independently changes every nonsuper component to1.0 before multiplying the two.','F12§7.3L174:WonderGuard-component-rule'),
 ('WinnerEffectiveness322–324','The component product is multiplied by4; Levitate+Ground skipped product remains1×4=4 and scores neutral.','F12§7.3L174:normalized-matrix-scale'),
 ('WinnerEffectiveness325','Scaled effect0 selects score slot0.','F12§7.3L174:ineffective-matrix-index'),
 ('WinnerEffectiveness326','Scaled effect1 selects score slot1.','F12§7.3L174:double-resistance-index'),
 ('WinnerEffectiveness327','Scaled effect2 selects score slot2.','F12§7.3L174:resistance-index'),
 ('WinnerEffectiveness328','Scaled effect4 selects score slot3.','F12§7.3L174:normal-index'),
 ('WinnerEffectiveness329','Scaled effect8 selects score slot4.','F12§7.3L174:super-index'),
 ('WinnerEffectiveness330','Scaled effect16 selects score slot5.','F12§7.3L174:double-super-index'),
 ('WinnerEffectiveness331','Any other scaled effect returns0 rather than clamping/interpolating a score.','F12§7.3L174:other-effect-boundary'),
 ('WinnerScore339–343','Defender types and ability_id are read from persistent Pokemon, with absent second type replaced by first; active Battler ability suppression is not consulted here.','F12§7.3L174:persistent-defender-traits'),
 ('WinnerScore344–352','Each nonnil move of every attacker is scored separately against every defender and accumulated.','F12§7.3L174:move-defender-cartesian-score'),
 ('WinnerScore349','Estimator matrix ineffective/doubleResist/resist/normal/super/doubleSuper is exactly[−16,−8,0,4,12,20].','F12§7.3L174:matrix-values'),
 ('WinnerScore353–354','Each attacker adds cached base-species BST integer-divided by10 separately before summation.','F12§7.3L174/§9.1L238:BST-per-member-floor'),
 ('WinnerScore355','Each attacker with a truthy resolved item object adds10; no full held-item effect is executed by this estimate.','F12§7.3L174:item-bonus'),
 ('WinnerScore357','Each party score adds its supplied scaled rating and one independent globalrand32 value.','F12§7.3L174:per-side-jitter'),
 ('DecideWinner362–363','Each input display rating scales by15.0/100 and rounds before score computation or tie breaking.','F12§7.3L173:rating-scale-and-round'),
 ('DecideWinner364–365','First-party score and second-party score are computed in order, with their separate random calls.','F12§7.3L174:two-score-order'),
 ('DecideWinner366–368','Equal total scores return5 if rounded scaled ratings also equal, otherwise1/2 according to their rounded rating order.','F12§7.3L175:rounded-tiebreak'),
 ('DecideWinner369–370','Unequal total scores return1 for score0>score1 and2 otherwise.','F12§7.3L175:score-tiebreak'),
 ('RuledBattle378–379','Every match initializes decision0 then uses globalrand100==0 for real battle; all other values choose estimation.','F12§7.1L162:real-estimate-gate'),
 ('RuledBattle380–383','Real branch gets rule suggestedLevel, first TrainerType key and creates fresh PLAYER1/PLAYER2 NPC trainers of that type.','F12§7.2L166:real-trainer-construction'),
 ('RuledBattle386–394','Team1 traversal skips nil; unequal-level members are levelassigned then calc_stats, every nonnil item_id is captured at its source index, and same member is appended to NPCparty.','F12§7.2L166:real-team1-preparation'),
 ('RuledBattle395–403','Team2 uses the same nil/level/item/reference ordering separately.','F12§7.2L166:real-team2-preparation'),
 ('RuledBattle404–405','Real branch creates DebugSceneNoVisuals then asks rule.createBattle, retaining the rule own type/recording/clause composition.','F12§7.2L167:real-scene-and-rule'),
 ('RuledBattle406','Real branch sets battle.debugtrue.','F12§7.2L167:debug-flag'),
 ('RuledBattle407','Real branch sets controlPlayertrue, which ordinary command ownership routing uses to choose AI for player side.','F12§7.2L167:controlPlayer-flag'),
 ('RuledBattle408','Real branch sets internalBattlefalse before start.','F12§7.2L167:internal-flag'),
 ('RuledBattle409','Real branch decision comes from pbStartBattle return; debugtrue alone is not the player-AI routing condition.','F12§7.2L167:real-decision-source'),
 ('RuledBattle410–414','After a normally returned real battle, every nonnil Team1 member heals before item restored from its saved matching index.','F12§7.2L169:team1-restore-order'),
 ('RuledBattle415–419','Team2 receives its own normal-return heal then matching item restore.','F12§7.2L169:team2-restore-order'),
 ('RuledBattle377–438','This real wrapper has no ensure restoring after start/execute/restore exceptions; normalized levels have no original-level rollback.','F12§7.2L169/§10L260:real-error-boundary'),
 ('RuledBattle421–425','Estimate branch builds arrays from team indexers/lengths and calls decideWinner with each team display rating.','F12§7.3L173–175:estimate-inputs'),
 ('RuledBattle427–430','Decision1 appends team1win1 and team2loss0, in that order.','F12§7.1L162:team1-win-history'),
 ('RuledBattle431–433','Decision2 appends team1loss0 and team2win1.','F12§7.1L162:team2-win-history'),
 ('RuledBattle434–436','Every other returned decision appends draw−1 to each team; this includes results other than estimator5.','F12§7.1L162:other-decision-draw'),
]:a(unit,meaning,receiver)

for unit,meaning,receiver,source in [
 ('Type.effectiveness61–67','Type relation checks nilattack→normal, then weakness→super, resistance→notvery, immunity→ineffective, else normal, in that priority.','F12§7.3L174:type-relation-priority','GEN-TYPE'),
 ('Effectiveness.calculate130–140','Each defender component reads defender Type.effectiveness(attacker), divides by2.0 and multiplies from1.0; estimator passes one defender type per call.','F12§7.3L174:type-component-calculation','GEN-TYPE'),
 ('Move.initialize41–57/readers5,7','Move data type/power readers expose initialized fields; absent type defaultsNONE and absent power0.','F12§7.3L174:move-data-field-boundary','GEN-MOVEDATA'),
 ('Pokemon.types313–315','Persistent Pokemon types is a clone of current species_data.types, distinct from R21 getTypes(baseSpeciesID).','F12§7.3L174:current-form-types','S01'),
 ('Pokemon.level199–205','Pokemon level assignment validates1..maximum, writes minimum experience and cached level, and doesnot itself calc_stats.','F12§7.2L166/§8.3L220:level-write-boundary','S01'),
 ('Pokemon.heal274–306','For a non-egg, heal calls HP fill, status/count clear, allmove PP fill, then clears ready_to_evolve; it is not the old HP/PP snapshot.','F12§7.2L169:complete-heal-consumer','S01'),
 ('Pokemon.heal300–306','An egg returns before all heal writes, while the wrapper still proceeds to the separate item assignment if heal returned.','F12§7.2L169:egg-heal-guard','S01'),
 ('Pokemon.ability_id445–458','Persistent ability_id resolves cached species/form natural/hidden slots, including hidden fallback through PID; estimator uses this id directly, without invoking real ability handlers.','F12§7.3L174:persistent-ability-boundary','S01'),
 ('DebugScene.initialize5–10','NoVisuals scene starts nilbattle and fourzero lastCmd/lastMove arrays; logging defaultsfalse.','F12§7.2L168:noVisuals-defaults','GEN-SCENE'),
 ('DebugScene.start13–17','Scene start retains the battle and resets both fourzero arrays.','F12§7.2L168:noVisuals-start','GEN-SCENE'),
 ('DebugScene.Blitz19–21','Direct Blitz helper ignores keys and returns globalrand30.','F12§7.2L168:Blitz-helper','GEN-SCENE'),
 ('DebugScene.message46–53','Regular/paused messages only conditionally PBDebug log; regular display alias uses same implementation.','F12§7.2L168:optional-message-logging','GEN-SCENE'),
 ('DebugScene.confirm55–58','Direct confirm logs only if enabled and returns true.','F12§7.2L168:confirm-helper','GEN-SCENE'),
 ('DebugScene.commands60–63','Direct showCommands logs only if enabled and returns0.','F12§7.2L168:commands-helper','GEN-SCENE'),
 ('DebugScene.item67','Direct item menu returns−1.','F12§7.2L168:item-helper','GEN-SCENE'),
 ('DebugScene.forget75','Direct forget-move helper returns0, selecting first move.','F12§7.2L168:forget-helper','GEN-SCENE'),
 ('DebugScene.command77–81','Direct command helper tries Bag on rand15==0; only if that fails does it try Call on rand10==0, otherwise Fight.','F12§7.2L168:conditional-menu-random','GEN-SCENE'),
 ('DebugScene.fight83–88','Direct fight helper loops at most50 yields, but reads battler.move.length (singular) before yielding its random result; ordinary Battler declares plural moves.','F12§7.2L168:singular-move-helper-boundary','GEN-SCENE'),
 ('DebugScene.target90–94','Direct target helper takes other-side current battlers indexes; empty returns−1, otherwise sample from that list.','F12§7.2L168:target-helper','GEN-SCENE'),
 ('DebugScene.party96–105','Direct party helper collects same-team positions not currently found as battlers; none returnsnil, otherwise at most50 random-position yields with scene as second arg.','F12§7.2L168:party-helper','GEN-SCENE'),
]:a(unit,meaning,receiver,source)

for name,line in [('pbBeginCommandPhase',24),('pbBeginAttackPhase',25),('pbBeginEndOfRoundPhase',26),('pbShowOpponent',27),('pbDamageAnimation',28),('pbCommonAnimation',29),('pbAnimation',30),('pbHitAndHPLossAnimation',31),('pbShowPartyLineup',32),('pbShowAbilitySplash',33),('pbReplaceAbilitySplash',34),('pbHideAbilitySplash',35),('pbEndBattle',36),('pbWildBattleSuccess',37),('pbTrainerBattleSuccess',38),('pbBattleArenaJudgment',39),('pbBattleArenaBattlers',40),('pbUpdate',42),('pbRefresh',43),('pbRefreshOne',44),('pbSendOutBattlers',65),('pbRecall',66),('pbResetCommandsIndex',68),('pbHPChanged',70),('pbChangePokemon',71),('pbFaintBattler',72),('pbEXPBar',73),('pbLevelUp',74)]:
    a(f'DebugScene.{name}{line}',f'NoVisuals {name} is an explicitly empty callback; its method changes no scene/game state itself.',f'F12§7.2L167–168:noVisuals-{name}','GEN-SCENE')

premise=('FixeddefaultR/B8/no later overrides. Valid numeric rating data/history and valid parties/rules/registries/source field types, with dependencies normally returning to each observation unless a named error boundary is stated. '
         'All equations were textually and symbolically reconciled, no rating/estimation/battle/MonteCarlo/model execution. Native Math/float overflow, convergence, actual random distribution and real battle/AI quality remain unknown. '
         'NoVisuals helpers are direct-helper source facts; actual generator controlPlayer/command route uses already fully received finite CORE5facts, not these random menus. Unconsumed helper defects are audit-scope descriptions, not automatic future API requirements. '
         'BST assumes existing memoized value or cold/consistent source registry; concrete all649trait classes/move/PBS domains and everyGNcase prerequisite remain separatelyOPEN.')
new=[]
for n,(source,unit,meaning,receiver) in enumerate(rows,1690):
    atom={'id':f'FAC-A{n:04}','source':source,'unit_locator':unit,'assertion':meaning,'formal_receivers':[receiver],'premise':premise,'pending_dependencies':[],'status':'BOUNDED_SOURCE_FACT_AND_EXPLICIT_FORMAL_CHILD_OR_AUDIT_SCOPE_ROUTING','formal_relation':'Explicit generator battle/rating/NoVisuals meaning or declared internal audit scope; not allGNcatalog prerequisite/normalization/producer closure.','evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','reader':'/root/facility_atomic_completion_cloud'};new.append(atom)
    REV['mappings'].append({'formal_clause':receiver,'atomic_assertion':atom['id'],'meaning':meaning,'source':source,'source_unit':unit,'premise':premise,'status':atom['status'],'pending_dependencies':[],'relation':'EXPLICIT_NAMED_GENERATOR_SOURCE_CHILD_OR_DECLARED_INTERNAL_SCOPE'})
extra={'GEN-TYPE':'Data/Scripts/010_Data/002_PBS data/003_Type.rb','GEN-MOVEDATA':'Data/Scripts/010_Data/002_PBS data/005_Move.rb','GEN-SCENE':'Data/Scripts/011_Battle/004_Scene/009_Battle_DebugScene.rb','GEN-BATTLERDECL':'Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb'};buffers={};ids={}
for key,p in extra.items():
    b=subprocess.check_output(['git','-C','/workspace/pokemon-essentials','show',R+':'+p]);buffers[key]=b.decode().splitlines();ids[key]={'repo':'/workspace/pokemon-essentials','commit':R,'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':subprocess.check_output(['git','-C','/workspace/pokemon-essentials','rev-parse',R+':'+p]).decode().strip()};F['source_identities'][key]=ids[key]
units=[]
for key,lo,hi,name in [('GEN-TYPE',1,141,'Complete Type data/effectiveness source'),('GEN-MOVEDATA',3,16,'Move field readers'),('GEN-MOVEDATA',22,36,'Complete Move schema'),('GEN-MOVEDATA',41,57,'Complete Move constructor'),('GEN-SCENE',1,106,'Complete NoVisuals class/source'),('GEN-BATTLERDECL',1,46,'Complete basic Battler declarations')]:units.append({'source':key,'identity':ids[key],'range':[lo,hi],'name':name,'content':'\n'.join(buffers[key][lo-1:hi]),'actual_reader':'/root/facility_atomic_completion_cloud','qualification':'Complete stated named unit only; Type141 andNoVisuals106 wholefile ownread, not wholeTypePBS/AI/Move/Battlerdomain.'})
pkpath=F['source_identities']['S01']['path'];pkb=subprocess.check_output(['git','-C','/workspace/pokemon-essentials','show',R+':'+pkpath]).decode().splitlines()
for lo,hi,name in [(199,205,'Complete Pokemon level writer'),(274,277,'Complete healHP'),(280,284,'Complete healstatus'),(290,297,'Complete healPP'),(300,306,'Complete heal'),(313,315,'Complete types'),(428,437,'Complete ability index reader/writer'),(440,458,'Complete ability object/id resolution')]:units.append({'source':'S01','identity':F['source_identities']['S01'],'range':[lo,hi],'name':name,'content':'\n'.join(pkb[lo-1:hi]),'actual_reader':'/root/facility_atomic_completion_cloud','qualification':'Finite complete methods only; CRE-A7facts54units prior receipt remains finite.'})
F['atoms'].extend(new);F['bounded_denominator']=len(F['atoms']);F.setdefault('v2_increments',[]).append({'path':'generator-battle-rating-flow-atomic-increment.v2.json','count':len(new),'ids':[new[0]['id'],new[-1]['id']],'utc':NOW});REV['true_bounded_assertions']=len(F['atoms']);REV['v2_new_exact_child_bindings']=len(REV['mappings'])-992
packet={'schema':'facility-generator-battle-rating-manual-meaning-increment/v2','utc':NOW,'reader':'/root/facility_atomic_completion_cloud','explicit_source_assertions':new,'source_identities':{**{k:F['source_identities'][k] for k in ['R22','R20','S01','F12']},**ids},'complete_supplemental_units':units,'actual_source_reads':['9ab0fd R22L1–180','02d07f R22L181–320','a2737e R22L321–438','f1a640 Type73–141/Moveconstructor+fields','34cb86 Type1–72/wholeNoVisuals106/Pokemonfinite','8c371e ability_id whole445–458','80a41a completeBSTcache helpers/Battlerdeclarations','c7a0a1 exact fixedscript helpercallercensus','CORE5facts complete command/source packet actuallyreceivedearlier'],'actual_formal_reads':['6276b9 WP76§6/7L113–206 full','a2737e WP76L201–279 full','priorwholeWP76 all279'],
        'qualification':'Finite manually authored field/flow/equation assertions, not true allGEN/source/formal denominator or allGN vector acceptance. EveryNoVisuals empty callback separately listed. Source activevariant, snapshot timing, original-scale sigma/draw handling/100iterationlimit, direct-helper boundary and actual AI route retained. CurrentWP76 already accurately documents shown active/Elo/NoVisuals/estimate peculiarities. No new finding classified.','helper_scope':'RuledTeam.compare/toStr/load and inactiveElo remain audited source definitions with exact represented limitations; absence of shown default callers doesnot excuse reading them, nor automatically require preserving internal APIs. SingularNoVisuals.move versus pluralBattler.moves agrees currentWP76; declaration/census is finite and native/plugin overrides excluded.','OPEN':['Full finite signed necessary factory/AI/MOVE/ABILITY/CRE/World/Developer joins and allGN/202externalcase prerequisites not automatically accepted by sourcefileFULL.','R19/R20/R21 remaining generation/content/rejection/caches/writer/normalization/iteration meanings plus actual453species649classes2732provenances/proof inputreconciliation.','NativeMath/battle/AI/runtime/actualratings/float/convergence/real output quality NOT_EXECUTED.'],'new_required':0,'new_optional':0,'new_contexts':0,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
def dump(n,x):(V/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
dump('generator-battle-rating-flow-atomic-increment.v2.json',packet);dump('forward-mapping.json',F);dump('reverse-mapping.json',REV)
P=json.loads((V/'progress.json').read_text());P.update(updated_utc=NOW,manually_authored_finite_source_assertions=len(F['atoms']),source_to_formal_bindings=len(REV['mappings']),finite_new_child_bindings=len(REV['mappings'])-992,state='RUNNING_REMAINING_GENERATOR_AND_TRAIT_PROOF_CHILDREN');dump('progress.json',P)
D=json.loads((V/'atomic-denominator.json').read_text());D['updated_utc']=NOW;D['manual_bounded_source_assertions'].update(count=len(F['atoms']),id_end=new[-1]['id']);D['finite_reverse_bindings'].update(count=len(REV['mappings']),qualification=f"992historicalregionbindings+{len(REV['mappings'])-992}newexplicit source/audit/case-childroutes; notglobalformaldenominator.");D['finite_generator_battle_rating']={'source_assertions':len(new),'membership':'generator-battle-rating-flow-atomic-increment.v2.json','qualification':packet['qualification']};dump('atomic-denominator.json',D)
L=json.loads((V/'reading-ledger.json').read_text());L['updated_utc']=NOW;L.setdefault('v2_additional_source_reads',[]).append({'utc':NOW,'packet':'generator-battle-rating-flow-atomic-increment.v2.json','complete_units':len(units),'actual_source_reads':packet['actual_source_reads'],'qualification':'WholeNoVisuals106 andType141text personallyread; finiteMove/Battlerdeclarations/Pokemonmethods. No TypePBS/Moveallrecords/Battler/AI/abilitydomain inheritance.'});dump('reading-ledger.json',L)
b=(V/'generator-battle-rating-flow-atomic-increment.v2.json').read_bytes();print('new',len(new),'range',new[0]['id'],new[-1]['id'],'total',len(F['atoms']),'routes',len(REV['mappings']),'bytes',len(b),'sha',hashlib.sha256(b).hexdigest())
