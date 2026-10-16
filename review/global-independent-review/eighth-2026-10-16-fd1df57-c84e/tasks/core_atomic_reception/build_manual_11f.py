import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11e.json').read_text());d=base['source_dictionary'];rows=[]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(856,[
 'SW21 uses the damaging force-out family with a sole wild target higher-level than the user and ordinary hit/damage eligibility satisfied.',
 'Unlike status Roar, this family does not fail the move in an earlier target-failure method for that level comparison.',
 'The ordinary damage can therefore be applied; its later wild-escape effect simply omits decision3 when target.level<=user.level is false.',
 'The post-use trainer drag loop skips wild targets, so this family does not instead select a wild reserve.',
 'It is damage without this flee result, not a guaranteed miss, refund, or rollback of damage.'
],['switch_effects_full','use','usagefull','checksfull'],'damaging hit -> ordinary damage -> later level<= conditional false -> no wild flee; nonwild drag separate.')
row(857,[
 'SW22 supplies one living wild target, level<=user, canRun=true, no active substitute and successful ordinary damaging hit with target surviving.',
 'The damaging family effect checks wild, no living ally, canRun, level<= and (current Substitute0 OR ignoresSubstitute).',
 'Those conditions write decision3 in the target effect.',
 'This wild effect does not contain the nonwild post-use Ingrain/SuctionCups gates; those gates must not be imported from the different branch.',
 'Earlier ordinary target/accuracy/type/damage requirements remain and any earlier callback failure may prevent reaching the decision assignment.'
],['switch_effects_full','use','usagefull','checksfull','battlerfull'],'successful damaging effect -> solewild/canRun/level/current substitute gates -> decision3; trainer drag guards not transplanted.')
row(858,[
 'SW23 changes the force-out target to a trainer-owned member rather than wild.',
 'The later damaging drag consumer requires no earlier switched index, living user and numHits>0.',
 'It excludes fainted, unaffected or damageState.substitute targets, then excludes wild, Ingrain and active SuctionCups unless battle.moldBreaker.',
 'Only after those guards does it obtain a random legal incoming reserve and perform replacement/choice-clear/entry.',
 'No reserve or an immunity guard preserves the damage already inflicted but prevents this drag; this is not the wild decision3 branch.'
],['switch_effects_full','switching','use','usagefull','battlerfull'],'damaging nonwild post-use -> hit/damage/root/ability guards -> random legal reserve -> replace/choiceclear/entry.')
row(859,[
 'SW24 fixes successful ordinary single-target PartingShot reflection, reflected stat-drop eligibility, original path unaffected and outer real hit count0.',
 'Reflection can lower the original user via the reflected effect while the outer hit loop exits on magicCoater/magicBouncer before incrementing realNumHits.',
 'PartingShot post-use selects a possible reflected switcher from target MagicCoat/MagicBounce flags but then returns when numHits==0.',
 'Thus the reflected stat mutation can occur without any later switch from this outer use.',
 'The normal successful unreflected path still uses the positive-hit/live-switcher/reserve/Pursuit gates; reflection does not erase those guards.',
 'Previously reached stage/messages are not reverted merely because the later switching condition fails.'
],['switch_effects_full','parting_parent','use','checksfull','stages'],'reflected effect stage writes -> outer hit loop zero -> post-use switcher selection -> zero-hit return no switch.')
row(860,[
 'SW25 fixes a sole living wild target with substituteHP5, a successful damaging hit that breaks it, permitted level/canRun and target still alive.',
 'Damage reduction marks damageState.substitute and subtracts from current substitute durability; the target-effect call observes current Substitute0 after the break.',
 'The wild damaging force-out condition therefore admits decision3 even though damageState.substitute records absorption for this hit.',
 'If that same hit leaves current durability positive and the move does not ignore substitute, the wild condition does not write3.',
 'For a trainer target, post-use drag instead checks damageState.substitute and rejects the same absorbed hit even after durability reached0.',
 'Current durability and per-hit absorption flag are distinct consumers, not interchangeable definitions of bypassing substitute.'
],['switch_effects_full','use','usagefull','damage_state'],'substitute damage/flag -> current durability0 -> wild effect decision3; nonwild later absorption-flag rejection.')
row(861,[
 'SW26 has a living primal Kyogre ordinarily recalled/replaced, with fixed default form callbacks and no plugin override.',
 'Switch-out runs active ability OnSwitchOut and Peer.pbOnLeavingBattle with the actual usedInBattle flag, then treats the outgoing battle copy as fainted for gas/weather checks.',
 'This ordinary withdrawal path does not explicitly call Pokemon.makeUnprimal; its primary permanent primal form is retained in the stated default callback scope.',
 'The leave form hooks still run and can make their own reached writes; lack of an explicit unprimal call is not a promise all arbitrary plugin callbacks preserve every form.',
 'The temporary battle HP0 used for ability cleanup is separate from writing permanent Pokemon HP through the ordinary setter.'
],['switching','ability_item','peer','pokemon_mega_full','primal_producers','crec_form_join'],'normal recall -> switchout effect/Peer leave -> raw battle-copy faint treatment/weather -> no explicit makeUnprimal.')
row(862,[
 'SW27 compares actual formal fainting and normal post-battle cleanup with ordinary live withdrawal.',
 'Formal pbFaint first performs reached scene/defeat/effect/status/happiness/Peer operations, then explicitly makeUnmega if Mega and makeUnprimal if Primal.',
 'World after_battle explicitly unMega/unPrimal on player party and separately registered partner party as applicable, rather than relying solely on the leave hook.',
 'Those explicit calls operate on bound individual forms; the callback/individual/species setters retain their own qualification and recalculation effects.',
 'An earlier exception prevents the later explicit reset; this is no universal guarantee every aborted/native-failed battle receives normal cleanup.',
 'Existing COM005 animation-only tail and audio channel corrections remain mandatory companions for any adopted full after-battle description.'
],['b_change','after','peer','pokemon_mega_full','crec_form_join'],'formalFaint prefix -> explicit form reset; independent normal world cleanup party resets; not ordinary live withdrawal.')
row(863,[
 'SW28 supplies a legal same-owner0/2 Shift with user FuryCutter2, Counter20 and CounterTarget1 where enemy1 is not swapped, and no extra clearing.',
 'SwapBattlers remaps CounterTarget only when its value equals0 or2, so the external enemy1 pointer stays1.',
 'It does not clear the Counter damage quantity20.',
 'ProcessTurn Shift then calls pbBeginTurn and pbCancelMoves, whose explicit FuryCutter reset changes2 to0.',
 'The Shift path writes lastRoundMoved to current turn, making the user acted.',
 'Only a reached normal EOR tail later sets Counter and CounterTarget to-1; early positive-decision exits before that tail preserve their current values.',
 'A CounterTarget equal to one of swapped indices is remapped to the other index, while damage quantity remains unchanged.'
],['use','swap','eor','b_init'],'Shift swap -> conditional pointer remap -> CancelMoves FuryCutter0 -> acted -> only reached EOR tail Counter/target-1.')
row(864,[
 'SW29 fixes ordinary physical U-turn, target Eiscue form0/ICEFACE, no Substitute/MoldBreaker and all eligibility/hit requirements passing; both alive, legal user reserve and opposing side still able, with no other reaction switches.',
 'The absorption helper sees that exact species/form/raw ability/physical conjunction and sets damageState.iceFace.',
 'Damage calculation sets its intermediate calcDamage1; ReduceDamage/LoseHP absorption paths leave actual target HP loss0.',
 'Normal hit processing still reports success and the outer realNumHits increments to1; the later IceFace presentation changes target form1.',
 'U-turn end-use checks actual numHits, user alive/opposing side able, not-all-targets-already-switched and legal reserve; zero actual HP loss is not one of its rejection guards.',
 'With the remaining ordinary Pursuit/selection/scene callbacks normal, it can replace the user, clear its choice and invoke entry notification.',
 'Changing only to a miss with no successful hit leaves realNumHits0, so the end-use switch guard returns; no inference every zero-damage path succeeds.'
],['switch_effects_full','usagefull','calculations','use','hit_triggers','switching','b_change','damage_state'],'IceFace absorption -> calcDamage1/HP0loss -> hit success count1 -> form1 -> U-turn positive-hit/reserve path; miss0 returns.')
S='Complete fixture S from catalogSW30: ordinary internal wild2v1, one player owner/no partner/debug/variant/plugin; >=3 initially able with fixedlayout; EORSwitch entrydecision0, slots0/2 formally fainted boundparty0/1, livefoe1; only legal nonEgg nonactive reservePparty2 HP60/120, order[0,1,2]; canRuntrue, faintedslot0 rawspeed100/foe50; position2HealingWishtrue/position0none, ownSpikes1 only; Pgrounded/indirect-damage/noBoots/noheal/exit/form/ability extra effects; all resources/scenes/callbacks normal. Slot0 choosesNo, later2Yes+P except the explicitly stated independent change.'
row(865,[
 'SW30 uses the complete named fixture S, including two formally fainted slots, one legal reserve and all normal callbacks; it is not a lethal-hazard or arbitrary multi-replacement example.',
 'At entry decision0 passes the initial guards and Judge leaves battle continuing because the player party still contains usable reserveP.',
 'For slot0, CanChooseNonActive succeeds; No invokes pbRun(0,true), and raw100>50 sets rate256 without random draw/count increment.',
 'Flee feedback normally returns before writing decision3; then pbRun returns1 and switch=false, so slot0 is not replaced.',
 'The same @battlers scan contains no decision check/break after that new3 and proceeds to fainted slot2, still finding P as a legal reserve.',
 'After slot2 Yes and validP selection, Replace initializes the existing slot2 battler with the same P object/index2, resets runtime state, swaps partyOrder[2] with oldpartyindex1 to[0,2,1], and sends it out.',
 'The post-scan entry wave reaches slot2; HealingWish sees healable P, recovers60 to120, cures status and clears the position2 flag after normal helpers.',
 'Spikes then computes totalhp120/8=15 and writes HP105 on both battle copy and bound P under ordinary setter conditions.',
 'P survives and is active; no other legal nonactive reserve remains, so the next replacement scan contributes no switched index and exits.',
 'No supplied callback overwrites decision3, so normal return still has3.',
 'The enclosing EOR immediately returns after pbEORSwitch when decision>0, before distant-shift, continual-ability checks or the silent tail clears.',
 'This static nonlethal prefix does not assert an entry-hazard knockout, later terminal/save/native cleanup, or executed fixture.'
],['switching','running','b_init','b_change','battlefull','priority','eor','statuses_full','battlerfull'],'entry0 -> slot0 No numeric escape writes3 -> same scan slot2Yes -> bind/order/send -> position heal60to120/flagclear -> Spikes15to105 -> noreserve -> EORpositive return.',premise=S)
row(866,[
 'SW31 independently changes only slot2 to still living, leaving slot0 as the sole required replacement in fixtureS.',
 'Slot0 No succeeds and writes decision3 as before, but the scan skips living slot2.',
 'Because no slot was replaced, switched remains empty and the replacement loop exits without entry notification.',
 'P is not rebound, position2 HealingWish is not consumed, and no entry hazard is applied to P by this call.',
 'Normal return preserves3; this is not a general prohibition of all effects on a currently active slot by unrelated callbacks.'
],['switching','running','eor','b_change'],'S with live2 -> slot0escape3 -> skip2 -> switchedempty -> no entry/P writes.',premise=S+' Independent only change: slot2 living.')
row(867,[
 'SW32 independently changes only the first slot0 response to Yes and validP selection.',
 'This takes replacement without calling the slot0 escape path and therefore does not write3 there.',
 'P binds slot0; its active presence removes the only legal nonactive reserve for later fainted slot2, so slot2 is skipped before a prompt/selection.',
 'Position0 has no HealingWish; the specified nonlethal one-layer Spikes can apply its ordinary entry prefix without the position2 heal.',
 'With all other result writers excluded by S, decision remains0 after normal replacement processing.',
 'It does not claim decline/escape side effects from SW30 somehow occur before the changed Yes response.'
],['switching','running','b_init','b_change','eor'],'S slot0Yes -> bindP0/no Run -> noreserve for2 -> nonlethal entry -> decision0.',premise=S+' Independent only change: slot0Yes+P.')
row(868,[
 'SW33 independently gives ordinary pbEORSwitch a pre-existing positive decision3 with favorDraws=false.',
 'Its very first guard returns before Judge, replacement scanning, prompts, binding, send-out or entry.',
 'This differs from SW30 where entrydecision0 allows the scan and only an inner Run later writes3.',
 'No position/HP/order mutation is produced by this early-returning invocation; earlier effects outside this call are not undone.'
],['switching','eor'],'preexisting decision3 +!favorDraws -> first guard immediate return, no scan prefix.',premise=S+' Independent only change: entrydecision3, ordinary favorDrawsfalse.')
row(869,[
 'SW34 retains slot0 No successful escape and its already committed feedback/decision3 before the later required slot2 selection.',
 'GetReplacementPokemonIndex without random calls SwitchInBetween with lax checking and default canCancel=false for the player-controlled party scene.',
 'The Scene negative-selection/back input repeats the selection loop when canCancel is false, rather than returning a cancellation result.',
 'When the user eventually picks legalP, it proceeds with the same slot2 binding/order/heal/hazard normal prefix as SW30.',
 'The attempted Back does not retract the earlier escape or reverse decision3.',
 'This is the required replacement UI only; ordinary optional cancellable party screens retain their separate permitted cancellation behavior.'
],['switching','scene_party','command','running'],'S firstNoescape3 -> later required party UI !canCancel -> Back loops -> legalP -> same normal prefix; no prior rollback.',premise=S+' Independent later input: Back attempted before eventual legalP.')
row(870,[
 'SW35 splits independent exceptions by exact reached writes in the same S continuation, rather than assuming every error produces the successful SW30 final state.',
 'An exception during the later prompt or required selection before Replace leaves earlier escape feedback/decision prefix but does not guarantee P binding, party-order mutation or send-out.',
 'Recall/leave/message failures before pbInitialize do not justify inventing the later replacement state.',
 'After pbInitialize boundP or the partyOrder swap has happened, later send-out/scene failure preserves only those reached earlier mutations; there is no transaction restoring old occupants/order.',
 'During position healing, animation/message precede HP recovery, status cure precedes HealingWish flag=false; an exception must retain precisely which of those writes was reached.',
 'After recovery or Spikes HP writes, a later error does not roll them back or guarantee all later flags/callbacks/decision branches completed.',
 'The S normal-return final3/HP105 is not imposed on every exceptional branch, nor are unexecuted operations counted as done.',
 'Diagnostic suppression/propagation follows the exact PBDebug/outer call boundaries already reviewed; helper exit0 is not target/business success.'
],['switching','scene_party','running','b_init','b_change','eor','pbdebug','errors'],'same S prefix -> independent exception points -> preserve reached binding/order/HP/flag/message writes only; no global success/rollback.',premise=S+' Independent error injection points are derived static vectors, not executed tests.')
row(871,[
 'The catalog explicitly labels BC26–31 and SW30–35 SOURCE_STATIC/DERIVED_VECTOR and executionNOT_EXECUTED.',
 'It claims no reference game, behavior-model, actual UI or host runtime observation for those vectors.',
 'SW fixture scope is the nonlethal continued scan, not an asserted lethal entry-hazard terminal path.',
 'The capture controls check target-resolution prefixes; random capture outcome, ordinary menu reachability and real save playback remain separate dependencies.',
 'The vectors do not instruct future implementation to preserve every reference anomaly permanently; current static review facts and future compatibility policy are distinct.'
],['switching','catch_full','use','scene_party'],'explicit evidence/fixture boundary -> no business execution/sourceFULL/whole-domain or future-policy overclaim.',support='SUPPORTED_BOUNDED_SCOPE_QUALIFICATION')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11f.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows))
