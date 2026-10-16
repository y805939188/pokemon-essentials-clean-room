import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11g.json').read_text());d=base['source_dictionary'];rows=[dict(number=886,layout_reason='R table column heading only; each end-round vector below has its own phase/decision/prefix conditions.')]
d['perish_move_complete']={'path':'Data/Scripts/011_Battle/003_Move/010_MoveEffects_Healing.rb','range':[637,665],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete PerishSong class including4methods/end actually read; loaded Clauses override separately ownFULL'}
d['lapras_raw']={'path':'PBS/pokemon.txt','range':[3453,3480],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete LAPRAS record actually read3453–3477 plus3478–3484 confirmed next header; no compiled/native/fullPBS credit'}
d['perish_growl_raw']={'path':'PBS/moves.txt','complete_records':[[5961,5970],[6225,6234]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete two raw records; default registration/load remains finite fixed-R premise, not executed'}
d['growl_complete']={'path':'Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb','range':[923,928],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete LowerTargetAttack1 class actual read; TargetStatDown parent separately actual read173–193'}
d['pokemon_iv_stat_formulas']={'path':'Data/Scripts/014_Pokemon/001_Pokemon.rb','complete_units':[[1076,1083],[1086,1090],[1093,1096],[1099,1127]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete calcIV/calcHP/calcStat/calc_stats actually read; not whole Pokemon'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(887,[
 'R01 enters ordinary EOR with speeds100/50, TrickRoom active and a previously established same-round priority tie order.',
 'EOR calls incremental CalculatePriority to refresh speeds, then pbPriority(true).',
 'The true query builds a separate array sorting only cached speed descending and saved tie value; it does not apply TrickRoom speed reversal or move/subpriority.',
 'Thus100 precedes50 for the cached EOR phase list despite TrickRoom.',
 'Same-speed comparisons reuse saved tie values from prior full ordering; this EOR step does not reshuffle or redraw randomOrder.',
 'Later replacement/other calls can calculate again under their own gates, so this is the actual EOR list construction rather than an all-phase ordering guarantee.'
],['eor','priority','battlerfull'],'incremental recalc -> speed-onlyPriority(true) ->100then50/saved ties, independent TrickRoom move sort.')
row(888,[
 'R02 starts with current weather duration1 and current Grassy duration1, with alive healable terrain-affected members and no interfering callbacks.',
 'The weather phase runs first, decrements its positive duration1to0, ends that current weather and may restore a separately configured default.',
 'At the later terrain-healing phase Grassy is still current and has not yet had its own duration decremented.',
 'Eligible members therefore recover under Grassy before the later EndTerrain phase changes1to0.',
 'This ordering prevents applying weather expiration timing to terrain healing; a restored default/weather or earlier callback still follows its own explicit conditions.'
],['eor','weather_core_complete','battlerfull','b_change'],'Weather1to0 early -> later stillGrassy healing -> later terrain1to0; distinct phase clocks.')
row(889,[
 'R03 assumes both SeaOfFire-related local phases are reached in each round.',
 'The early damage helper decrements4to3 and applies eligible SeaOfFire damage while the new count is nonzero.',
 'The later side-effects helper decrements3to2 in the same complete round.',
 'Next complete round performs2to1 with damage then1to0 with expiry feedback.',
 'If the phase14 positive-decision return occurs first, the later side decrement is not reached; the source is not a single decrement-per-round counter.',
 'Damage recipients still require the actual side/indirect/nonFire eligibility and do not determine whether the counter itself decrements.'
],['eor','battlerfull','b_change'],'early decrement+conditionaldamage -> later side decrement; phase14 return removes second decrement only.')
row(890,[
 'R04 is ordinary1v1 with each side sole living nonEgg, PerishSong count1 with stored sources on player side, player Flinchtrue, Reflect1, drawclause true and no other mode/result modifiers.',
 'EndBattlerEffects decrements song1to0, saves each PerishSongUser, reduces HP0 and runs actual formal fainting.',
 'Formal faint initialization already clears Flinch before the silent EOR tail; false Flinch therefore does not prove the whole tail ran.',
 'Both song sources being the same side makes checkpoint use that saved source-side battler, and the drawclause assigns2 for player-side source when both parties all fainted.',
 'The enclosing next positive-decision check runs GainExp then returns before side-effect countdown, leaving Reflect1.',
 'Because endOfRound=true was set at entry and false only at the reached normal tail, it remains true on this early exit.',
 'Independent no-zero/decision0 normal-tail control decrements Reflect1to0 and ends with endOfRound=false, provided both sides remain able and all later calls return.',
 'No raw HP-only, lastMoveUser or permanent-direction inference replaces these explicit source/checkpoint/formal-faint assignments.'
],['eor','clauses','b_change','b_init','growth_all','battlefull'],'song countdown/formalFaint -> Flinch reset -> same saved-source checkpoint2 -> phase14 return -> Reflect1/endOfRoundtrue.')
row(891,[
 'R05 explicitly assumes residual damage has made the last member fainted but no reached callback/checkpoint has yet assigned a decision.',
 'HP0/fainted predicates alone do not make the main EOR perform a universal immediate return after every local effect.',
 'Later configured local phases can still run until an actual decision check or replacement-entry judge is reached.',
 'EORSwitch calls ordinary Judge and can assign the outcome from whole-party able counts at its own entry.',
 'The vector does not suppress explicit earlier checkpoint/ability/item writers; those are excluded by its premise, and their presence can cause an earlier positive return.'
],['eor','switching','start_end_full','b_change','battlefull'],'residualHP0 without decisionwrite -> reached remaining phases -> replacement-entryJudge -> actual outcome assignment.')
row(892,[
 'R06 gives two fainted player slots with legal reserves, one new entrant then being hazard-fainted, and actual availability/result conditions for further replacement.',
 'The replacement scan chooses and binds eligible reserves per slot, recording only indices actually replaced in switched.',
 'After that scan, one entry-notification call handles the complete switched collection in speed order.',
 'Entry hazards can formally faint one entrant, award/judge and leave that position eligible for another pass.',
 'The outer loop clears switched and scans again until no new replacement, an entry/ordinary judgment result or missing legal reserves prevents further work.',
 'It does not fabricate a replacement for every fainted field object without checking party owner/able/nonactive eligibility or guarantee continuation after callback error.'
],['switching','b_init','b_change','growth_all','start_end_full','priority'],'per-slot legal binding -> combined entry -> possible hazardFaint/Judge -> repeat actual reserve scan.')
row(893,[
 'R07 has a fainted field opponent but at least one able nonEgg opponent reserve in the relevant whole side.',
 'Ordinary Judge uses pbAllFainted over party members and does not declare victory solely from current field HP.',
 'The replacement loop chooses who fills the vacated active slot if the owner team has a legal reserve.',
 'Partner/multiowner ownership and wild replacement restrictions remain separate actual predicates; this is not a claim every able member can enter every slot.'
],['start_end_full','battlefull','teams','owners','switching'],'whole-party able predicate -> no field-only victory -> valid owner replacement selection.')
row(894,[
 'R08 records two distinct assignments: an earlier checkpoint has set decision2 while both full parties are now all fainted, then ordinary Judge is actually invoked afterward.',
 'Judge itself has no existing-positive-decision early guard; on both all-fainted it assigns pbDecisionOnDraw.',
 'With selfkoclause false the loaded wrapper delegates to the original default5.',
 'Thus later ordinary Judge can replace intermediate2 with5; this does not imply every normal caller invokes Judge after a positive checkpoint, since other callers may return earlier.',
 'No individual/HP rollback follows the reassignment, and decision provenance/timing must remain explicit.'
],['start_end_full','clauses','battlefull'],'actual checkpoint2 -> later actualJudge bothfainted -> no selfKO -> default5 overwrites intermediate.')
row(895,[
 'R09 requires normal arrival at distant-shift stage23, no reserves, established3v3 six objects, one owner per side, only outer0/1 alive and central2/3 existing fainted.',
 'Planning scans both sides before execution; no current live opposing pair is near, so it queues0to2 and1to3.',
 'Both three-slot plans pass owner checks and execute in order, giving final living positions2/3.',
 'The independent3v2 case still plans two swaps but the two-slot side plan is skipped when total plan count>1; only the three-slot0to2 executes, final2/1.',
 'The independent legal three-player-owner3v3 case rejects own0to2 because owner differs, while opponent1to3 remains allowed, final0/3.',
 'If an initial live pair is already near, the planning outer loop breaks with no required candidate plan.',
 'A direct fixture with a missing swap endpoint makes SwapBattlers false and suppresses only that pair message; subsequent queued pairs are still tried.',
 'Planning/executing are separate and an endpoint/owner failure is not automatically a global result or a justification to replan from a partially executed array.'
],['eor','swap','battlefull','owners','mode'],'precomputed bothside plans -> owner check -> totalplans two-slot skip rule -> each swap/message iftrue; later pairs continue.')
row(896,[
 'R10 has saved FutureSight source A at party identity/slot0, A now able off-field, live replacementB at0, live nonGhost targetT1, target MeanLook0 just created byB, count1 and no other relation changes.',
 'EOR decrements count1to0 before obtaining the delayed attack source.',
 'The current living same-side source search matches the saved party identity, so B with another Pokemon index is not reused as A.',
 'Finding able partyA off-field constructs a new Battler at saved index0; its constructor invokes InitEffects before the dummy copies A current attack inputs.',
 'That constructor clears current living T MeanLook equal0, so B remaining physically at0 does not protect the freshly established relationship.',
 'The delayed attack is attempted only after that clear; a later miss/ineffectiveness does not restore the earlier relation.',
 'Independent A-still-on-field control reuses A and does not construct the dummy, avoiding this additional cross-clearing path.',
 'Only living battlers in allBattlers and matching pointer values receive this clearing; other relation sources remain.'
],['eor','b_init','battlefull','battlerfull','use'],'saved partyA off-field -> constructor savedslot0 InitEffects -> liveT MeanLook0clear -> copyA -> delayedattack; on-fieldA no constructor.')
row(897,[
 'R11 is the complete external ordinary1v1 trainer fixture: drawclause true, other named KO/song rules false, two level60 neutral/EV0 Lapras, WaterAbsorb, no held items/extra residuals, HP226, speed IV20/0 and no switches/reflection.',
 'Default LAPRAS raw data has HP130/Speed60; with enabled IVs and relevant HPIV0, calcHP gives226 and neutral calcStat gives speeds89/77 for SpeedIV20/0. Other fixture values remain controlled, not a full PBS compile assertion.',
 'Default PERISHSONG is Status/AllBattlers/functionStartPerishCountsForAllBattlers; the actual function writes count4 and source user.index to every affected target.',
 'WaterAbsorb is not Soundproof and its water-type immunity handler does not block this Normal status song; loaded perishsongclause override is disabled by the fixture.',
 'Player0 acts first with song and opponent1 Growl; later three rounds Growl produce no listed damage or residuals, while song counts at each EOR3/2/1/0.',
 'At fourth-round zero, both stored song sources remain0 even though latest move user is opponent1.',
 'The all-same-source-side checkpoint takes that saved player-side source and sets2, independent of the later Growl lastMoveUser.',
 'External GainExp early return does not overwrite2; ordinary EOR and main battle loop positive-decision exits preserve2 on this actual trace.',
 'Changing only lastMoveUser to player0 still leaves this song checkpoint2.',
 'The separate ordinary both-fainted selfKO draw function, when enabled and actually called, uses lastMoveUser: opposite returns2, own returns1, unknownnegative returns5; it does not reverse the song source rule.',
 'All named data/function/HP/speed/phase traces are static source-derived vectors, with no host battle, audio, RNG, asset or save observation.'
],['lapras_raw','perish_growl_raw','perish_move_complete','growl_complete','targetstatdown_parent','pokemon_iv_stat_formulas','stat_full','b_settings','abilityeffects','checksfull','use','eor','clauses','growth_all','battle_loop_complete'],'raw legalLAPRAS/formulas -> song source0count4 -> fourEORs -> saved-source checkpoint2 -> externalgrowth/positive exits retain2; ordinaryselfKO separate.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11h.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
