import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11f.json').read_text());d=base['source_dictionary'];rows=[dict(number=872,layout_reason='G table column heading; individual growth vectors below require their full numeric/individual/scene consumers.')]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(873,[
 'G01 has an opposing faintedA with nonempty participants including a living able player-ownedP, another opponentB still able, and internal expGain enabled.',
 'GainExp processes each opposing captured/fainted battler with a nonempty participants record; it does not require the whole opposing party to be defeated.',
 'It counts actual able player-owned participants and iterates only the player owner team for ordinary awards.',
 'For eligible P it calls GainEVsOne before GainExpOne, so permanent/saved EV prefix precedes experience/level presentation and learning.',
 'After normal processing it clearsA participants; an earlier EV/exp/message callback failure can leave some awards with that record not yet cleared.',
 'B remains in battle under the fixture, so delaying these awards until final victory would not reproduce the reached ordinary pipeline.'
],['growth_all','teams','owners','pokemon_growth_qual','item','stat_full'],'opposingA captured/fainted +nonempty record -> able ownedP -> EV then EXP/levels -> clearA; B still able no terminal prerequisite.')
row(874,[
 'G02 fixes Medium n^3 curve, initial level4/exp64, actual bounded increment152/final216 and an on-field non-Transform receiver.',
 'The curve boundaries are level5 at125 and level6 at216.',
 'GainExpOne increases total_exp_gained once by the actual152 before the per-level animation loop.',
 'It first writes the threshold125, animates the bar, calculates stats/updates the bound battler and displays/learns for level5.',
 'It next reaches216 and performs the corresponding level6 stat/readback/display/learning, rather than jumping directly to6 without intermediate consumers.',
 'After the per-level loop reaches the final experience it recalculates the Pokemon again and refreshes the bound battler/scene at the final tail.',
 'Statistics do not add152 again for each level; callback failure can leave prior experience/level/stat prefixes and the already counted actual award.',
 'Curve registry reading credit remains the actual CRE source reader; this reception adopts the complete finite curve/exp facts, not own GrowthRate whole-source credit.'
],['growth_all','crec_growth','pokemon_learn_stats','pokemon_growth_qual','b_change','scene_growth'],'actual152 stats once -> exp125/level5 updates+learning -> exp216/level6 -> final recalc/readback.')
row(875,[
 'G03 follows G02 through a full-moveset level5 learning prompt, then cancellation and confirmed give-up, with another level6 learning entry.',
 'The level5 EV, experience threshold, stat/HP recalculation and battler refresh happen before that learning choice.',
 'A negative forget selection followed by confirmed give-up displays did-not-learn and ends only this learn-move loop without replacing the chosen persistent/battler move slot.',
 'It returns to the enclosing per-level GainExpOne loop, which can continue to level6 and its separate matching learning entries.',
 'It does not roll back prior growth or cancel every later learning opportunity.',
 'Cancellation preserves the learning-slot domain only; complete WP21 dynamic form/icon readers can still have their specified earlier side effects, as received NO_REQUIRED WP30 scope adjudication preserves.'
],['growth_all','scene_forget','summary_forget','persistent_move','pokemon_learn_stats'],'growth committed before learn -> negative slot/giveup -> no replacement -> return to later level learning; no growth/all-object rollback.')
row(876,[
 'G04 has already received EV, is already at maximum experience, and calc_stats changes persistentAttack100 to101 while the current battle-copyAttack is100.',
 'GainExpOne checks max experience first and explicitly calls pkmn.calc_stats before returning.',
 'This early branch does not obtain or pbUpdate the corresponding battler and does not run later level/final-refresh logic.',
 'Thus the individual can have101 while the battle copy remains100 until a genuinely reached later refresh reads it.',
 'This is the stated current-copy divergence, not a claim no later caller can refresh it or a reason to roll back already gained EV.'
],['growth_all','pokemon_learn_stats','b_change','pokemon_growth_qual'],'EV -> maxexp guard -> persistent recalc101 -> early return before battle readback; later refresh separate.')
row(877,[
 'G05 assumes EV has been written before GainExpOne and then the calculated award hits a nonpositive early-return gate.',
 'The a/share result exp<=0 returns before experience modifiers, exp/statistics writes and the normal final recalculation/readback.',
 'A later expGained<=0 cap/modified-result gate also returns before the normal ordinary loop; neither branch rolls back EV.',
 'In the positive ordinary non-level-up control, it still writes final experience in the loop then takes the curLevel>newLevel tail with persistent calc_stats and battler update/scene refresh.',
 'Therefore zero award does not guarantee EV-derived stats become current in the battle copy, while a normally completed positive no-level award does refresh.',
 'The max-experience branch is separately G04 with its explicit persistent-only recalc, not silently equated to all zero-award branches.'
],['growth_all','pokemon_learn_stats','b_change','pokemon_growth_qual'],'EV prefix -> one exact zero gate returns without normal refresh OR positive no-level loop -> final persistent/battle refresh.')
row(878,[
 'G06 has merged player/partner participation, no able player-owned member, and a live participating partner member.',
 'Whole-side ability/judgment counts can still find the partner able; player-personal count0 does not equal side-all-fainted.',
 'GainExp ordinary recipients are selected by eachInTeam(0,0) and ownership checks, restricting them to the player first-owner segment.',
 'Partner participation or being the only live field occupant does not transfer the ordinary player award to the partner.',
 'With no able eligible player member this path gives no ordinary partner growth, while battle continuation and replacement depend on actual whole-side/team state.'
],['growth_all','teams','owners','partner','battlefull','start_end_full'],'merged side able via partner -> judgment remains possible -> owner0 ordinary award enumeration excludes partner.')
row(879,[
 'G07 compares ExpAll true with an empty defeated-opponent participants array versus a nonempty record whose original participant is now fainted.',
 'An empty record is skipped before participant counting or ExpAll recipient loops.',
 'A nonempty record can pass that front gate even when numPartic becomes0 after current able/owner filtering.',
 'ExpAll true then admits the processing branch and other able player-owned nonparticipant members can receive their ExpAll EV/exp path.',
 'Thus numPartic0 and record.empty are not equivalent eligibility predicates; the record is cleared after normal processed completion.',
 'The actual half-award/arithmetic and recipient abilities still determine whether a positive final exp is written.'
],['growth_all','teams','pokemon_growth_qual','battlerfull'],'record-empty frontgate vs nonempty/current0 -> ExpAll admission -> other owned able awards -> normal recordclear.')
row(880,[
 'G08 uses internal wild battle with expGain=false, opposing party all fainted and own side still able.',
 'GainExp checks and calls scene.pbWildBattleSuccess before its !internalBattle/!expGain early return.',
 'It then returns without EV/experience awards or clearing any unprocessed participants array in this invocation.',
 'The victory request follows the accepted actual BGM caller correction; this does not claim ME output, host playback or total battle cleanup.',
 'A later independent call/callback can change records, so only this entry nonprocessing is established.'
],['growth_all','audio','audio_path','battlefull'],'wild victory-condition scene request first -> expGainfalse return -> noaward/no recordclear this call.')
row(881,[
 'G09 supplies a real Shadow individual heartStage2 with a calculated actual increment121 and exp headroom.',
 'GainExpOne enters the Shadow branch and calls pkmn.exp +=121 because heartStage<=3, then total_exp_gained +=121 and returns.',
 'The Shadow exp= override computes the requested delta against current ordinary exp and accumulates it into saved_exp instead of raising current exp at this heart stage.',
 'Thus current experience/level remain while saved experience and actual-award statistic increase121.',
 'No ordinary per-level loop, bar/level learning or final normal stat/battler refresh runs in this branch.',
 'Actual purification/withdrawal of saved experience and the whole Shadow lifecycle remain separate finite dependencies, not inferred from this award.'
],['growth_all','shadow_main','shadow_exp_heart','crec_growth','pokemon_growth_qual'],'calculated actual121 -> Shadow stage<=3 exp setter storesdelta -> stat+121 -> return before ordinary growth.')
row(882,[
 'G10 uses a full moveset and successful valid second-slot selection with a legal newly learned move whose totalPP20.',
 'Battle LearnMove constructs a fresh Pokemon::Move and assigns it into persistent second slot, discarding the former move object and remainingPP.',
 'If a bound battler exists it constructs its corresponding Battle::Move from that new real move and replaces the matching battle slot.',
 'The new object initializes currentPP from totalPP, so the stated new20/20 replaces the old depleted PP rather than preserving the old amount.',
 'Only after both assignments does the normal forget/learn feedback and moveset-form check run; later failure can leave the replacement committed.',
 'Negative selection with confirmed give-up assigns neither slot; earlier experience/EV/form-reader prefixes remain independent.'
],['growth_all','persistent_move','move_pp_hm_data','movebase','scene_forget','summary_forget','b_change'],'successful slot1 -> fresh persistent MovePP20 -> matching battle MovePP20 -> feedback/form check; cancel neither assignment.')
row(883,[
 'G11 retains every declared arithmetic fixture exclusion: ordinary internal wild, defaultCATERPIE2/BaseExp39 defeated, single able player nonEgg/nonShadowCATERPIE3/exp27/EV room, scaled on/split off, noExpAll/Share/outsider/charm/current-or-initial exp item/affection/extra interference.',
 'EV processing runs before exp arithmetic, with the controlled real/default record identity and callback success premises.',
 'Base a=2*39=78 and no-split sole participant share remains78.',
 'Scaled branch performs integer exp/=5 first, producing15 rather than retaining15.6.',
 'The level factor is sqrt((14/15)^5)=(14/15)^2.5, applied to15 and floored before participant+1.',
 'That yields floor(15*(14/15)^2.5)+1=13, actual experience27to40, below Medium level4 threshold64 so still level3.',
 'Delaying the integer division/truncation would instead floor(15.6*(14/15)^2.5)+1=14 and wrong final41.',
 'Only actual expGained13 is added to statistics on normal ordinary processing; no game/native compiled-data execution is claimed.'
],['growth_all','caterpie_raw','pokemon_growth_qual','crec_growth','pokemon_learn_stats','item','b_settings'],'controlled record/EV -> base78 -> integer /5=15 -> scaledfloor+1=13 -> exp40/level3 -> actualstat13.')
row(884,[
 'G12 is the complete legal-author data fixture BaseExp1/defeatedlevel1 with positive EV yield, two eligible participant recipients, split/scaled on and all listed boost/share/affection exclusions.',
 'For each recipient the participant share is integer1/2=0.',
 'The exp<=0 check returns immediately before scaled integer/5 or participant+1, leaving experience and total_exp_gained unchanged while earlier EV remains.',
 'Changing only split=false gives each participant share1, which passes that early positive check.',
 'Scaled integer1/5 then becomes0, but the later participant+1 makes1, producing a positive actual award when headroom remains.',
 'This proves the pre-scaling zero gate differs from testing only the final computed value; it does not assume every zero intermediate eventually gains1.',
 'The fixture is lawful authored data and source-derived arithmetic, not a claim this exact enemy default PBS entry or actual runtime test exists.'
],['growth_all','b_settings','pokemon_growth_qual','crec_growth','item'],'split1/2=0 -> earlyreturn before+1/keepEV; control no-split1 -> passesfront -> /5=0 -> participant+1=1.')
row(885,[
 'G13 supplies one ordinary displayable nonEgg/nonShadow Pokemon with four legal known moves, one legal new unknown move, nondebug mode and normal assets, then confirms forgetting.',
 'Battle Scene.pbForgetMove passes the single same Pokemon into SummaryScreen.pbStartForgetScreen; it does not insert a party-member selection layer.',
 'Forget initialization and drawing expose four existing moves plus the new fifth candidate under the same individual reference.',
 'BACK or selecting the new fifth entry yields-1, while a selected permissible old slot returns0..3.',
 'A hidden/HM old move is rejected by the normal nondebug screen and selection repeats; debug Scene always-forget-first override is excluded by the fixture.',
 'A returned old slot triggers the persistent and bound-battler fresh move/PP assignments specified by G10.',
 'Cancel followed by confirmed give-up means no move replacement; previous growth remains and the complete dynamic form/icon contract can still produce its allowed earlier reader prefix.',
 'This existing local learning scope has actual different-context WP30 cancellation NO_REQUIRED receipt; no universal all-object-purity or native UI execution claim is introduced.'
],['growth_all','scene_forget','summary_forget','persistent_move','move_pp_hm_data','ui_command','pokemon_learn_stats'],'Battle samePokemon -> direct Summary Forget4+1 -> Back/new=-1 or old0..3/HMrepeat -> actual fresh moves or giveup no move replacement.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11g.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
