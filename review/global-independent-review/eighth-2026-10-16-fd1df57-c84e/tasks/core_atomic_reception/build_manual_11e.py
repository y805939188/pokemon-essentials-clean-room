import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_11d.json').read_text());d=base['source_dictionary'];rows=[dict(number=835,layout_reason='SW table column heading only; each actual vector receives its independent full fixture and behavior decomposition below.')]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(836,[
 'SW01 assumes ordinary successful command-time switch registration with a valid replacement index and later nonfainted user/decision/Pursuit continuation.',
 'RegisterSwitch first runs the full combined switch check, then writes SwitchOut, the party index and nil move.',
 'AttackPhaseSwitch recognizes that retained choice, gives recall feedback, allows Pursuit interruption and returns early if a positive decision is reached.',
 'On its reached normal path RecallAndReplace performs recall/leave ability hooks/messages before actual replacement and send-out, followed by entry notification.',
 'Replacement initialization resets the choice/acted state such that the incoming member does not perform the former occupant scheduled action this round.',
 'Later callback failure or Pursuit changes can prevent later steps; the vector is not an unconditional promise all registrations finish a switch.'
],['switching','attack','b_init','ability_item','b_change'],'registration check/write -> attack recall/Pursuit -> reached replacement/send-out -> entry; old scheduled action cleared.')
row(837,[
 'SW02 supplies a real otherwise eligible party index owned by the partner/another owner rather than the switching battler owner.',
 'CanSwitchIn checks owner membership after egg and before fainted/active checks, returning false for this foreign segment.',
 'When an actual partyScene is supplied, it obtains that individual owner and displays the named cannot-switch-others message.',
 'Direct queries with nil partyScene still reject but do not emit this optional message; no SwitchOut registration occurs after failed combined validation.'
],['switching','owners','teams','command'],'party index -> owner segment mismatch -> optional named scene message -> false before registration.')
row(838,[
 'SW03 compares separate otherwise valid indices for Egg, fainted member and an already active party member.',
 'Egg fails first with Egg message when partyScene exists.',
 'A correctly owned non-Egg fainted member fails with its no-energy name message.',
 'An otherwise eligible owned living member already returned by pbFindBattler fails with already-in-battle feedback.',
 'These ordered predicates are separate fixtures, not a claim an Egg that is also fainted emits all three messages; nil partyScene suppresses feedback but not rejection.',
 'Out-of-range or missing positive indices fail still earlier without those three named messages.'
],['switching','battlefull','owners','teams'],'index exists -> egg -> owner -> faint -> currently bound battler -> valid; first failure controls message.')
row(839,[
 'SW04 has a legal living nonactive same-owner replacement already reserved in another same-side SwitchOut choice.',
 'CanSwitch first verifies CanSwitchIn, then scans same-side scheduled SwitchOut indices and rejects the duplicate.',
 'With partyScene it displays already-selected before the switch-out ability/trap stage.',
 'The second registration returns false without overwriting its own choice; the first reservation is not automatically cancelled or transferred.'
],['switching','battlefull','command'],'valid incoming -> same-side choice duplicate -> optional selected message -> false before own write.')
row(840,[
 'SW05 fixes canSwitch=false and an ordinary cancellable party UI in mode0.',
 'The Scene Switch In command requires able? AND (battle.canSwitch OR !canCancel), so that ordinary cancellable UI omits the button.',
 'Direct CanSwitchIn/CanSwitch predicates do not read battle.canSwitch and can accept an otherwise legal candidate.',
 'A required noncancellable replacement UI can show Switch In because !canCancel is true; the ordinary cancellable restriction is not a universal executor veto.',
 'The direct successful query does not itself write a SwitchOut choice or prove an unavailable button was selected.'
],['scene_party','switching','command'],'UI mode/able/canCancel gate reads canSwitch; direct candidate validation separate and read-only.')
row(841,[
 'SW06 fixes a same-owner living non-Egg nonactive replacement with no duplicate reservation, permitted UI button, and trapped current member without Ghost/certain-switch ability/item exemptions.',
 'Strict PartyScreen(checkLaxOnly=false,shouldRegister=false) uses the combined CanSwitch predicate.',
 'The incoming checks pass, then the outgoing trappedInBattle predicate rejects and optional partyScene shows cannot-switch feedback.',
 'No candidate is accepted from that failed callback and no SwitchOut choice is written because registration was not requested.',
 'Fainted outgoing members, actual certain-switch callbacks and enabled Ghost exemption are earlier outgoing successes and are excluded by the fixture.'
],['switching','scene_party','battlerfull','abilityeffects','item','b_settings'],'strict candidate -> CanSwitchIn+no duplicate -> outgoing exemption checks -> trapped false result; no register.')
row(842,[
 'SW07 changes only to lax checking while keeping the legal incoming candidate and shouldRegister=false.',
 'The PartyScreen callback invokes CanSwitchIn only, so it does not ask the current occupant outgoing trap predicate or combined duplicate check.',
 'It records and returns the accepted party index through the normal Scene completion.',
 'No SwitchOut choice is written; lax candidate return and successful command-time registration are different operations.',
 'An invalid incoming candidate still fails its egg/owner/faint/active checks, so lax does not mean arbitrary indices are allowed.'
],['switching','scene_party'],'lax callback -> incoming validation only -> return idx -> no registration write.')
row(843,[
 'SW08 gives a later-executed player SwitchOut choice that was legal when registered; an earlier faster opposing entry subsequently creates trapping.',
 'AttackPhaseSwitch consumes the stored SwitchOut choice with nonfainted/positive-decision/Pursuit conditions, rather than rerunning the combined CanSwitch predicate.',
 'Thus newly present trapping does not by itself reject this already registered switch in that executor.',
 'Recall, Pursuit and replacement/entry still execute in their own order and may interrupt/fail under their actual gates.',
 'This behavior is not permission to register a new trapped switch after the trap or to skip owner/incoming checks at command time.'
],['attack','switching','ability_item','entry_exit_handlers'],'registered choice -> faster enemy entry/trap -> later executor without combined recheck -> normal other gates.')
row(844,[
 'SW09 supplies internal trainer battle, switchStyle=true, player side size1, opposing fainted slot with legal reserve, live player0 not yet in switched, legal player reserve and Outrage0.',
 'EORSwitch first obtains the opposing replacement and owner, then checks exactly that switch-style conjunction.',
 'It may substitute an Illusion display name under its current ability/global-gas conditions; that affects announced identity, not replacement ownership.',
 'After confirmation true it offers a cancellable strict player choice; only returned index>=0 triggers player recall/replacement and adds0 to switched.',
 'The opposing replacement happens afterward regardless of declining or cancelling that optional player choice, assuming normal subsequent calls.',
 'Changing only switchStyle=false omits the prompt/player option while preserving the opponent replacement path.',
 'Send-out/recalculation precedes the later combined entry notification as accepted COM008; this vector does not impose the superseded overview order.',
 'Callback/message/choice failures preserve only reached prefixes and do not guarantee both replacements or the final entry wave.'
],['switching','b_init','ability_item','priority','style_system','config'],'opponent reserve -> exact style conjunction -> optional prompt/strict choice -> player replacement if>=0 -> opponent replacement -> combined entry.')
row(845,[
 'SW10 has ordinary double battle player-side size2 when an opposing trainer member is replaced.',
 'The optional switch-style conjunction requires pbSideSize(0)==1, so double battle does not show that optional player switch prompt.',
 'The valid opposing replacement can still occur, and required player fainted replacements elsewhere are unaffected.',
 'This is a static predicate boundary rather than observed UI playback.'
],['switching','mode'],'double size2 -> single-size conjunction false -> no optional style prompt; required replacement path retained.')
row(846,[
 'SW11 reaches EORSwitch for a fainted player-owned slot in a wild battle with a legal nonactive replacement.',
 'The scan asks Use next Pokemon; Yes proceeds to required replacement selection.',
 'No immediately calls pbRun(index,true) and chooses to replace only if its return<=0.',
 'A successful escape return1 suppresses replacement for that slot but does not insert a break from the surrounding battler scan; later slots can still be processed as SW30 explicitly details.',
 'Escape calculation in this path is based on the fainted battler snapshot raw speed, and duringBattle excludes the ordinary Ghost/guaranteed-escape/trapping group.',
 'A new positive decision written inside this scan differs from a positive decision already present at EORSwitch entry.'
],['switching','running','battlerfull'],'required playerwild slot -> prompt -> No Run(duringBattle) -> <=0 replacement bool; continue outer scan.')
row(847,[
 'SW12 supplies a successfully bound/send-out replacement whose entry StealthRock damage is lethal, with normal callback/scene paths.',
 'Entry handles position healing before hazards and the ordered hazard effects before its explicit faint test.',
 'On faint it calls formal pbFaint, then GainExp and Judge, recording only reached formal/individual/battle changes.',
 'The enclosing replacement loop can scan again for another legal reserve if the resulting decision/available reserves permit, rather than treating one attempted replacement as permanent occupancy success.',
 'A terminal judgment or callback error can prevent a further replacement; this is not a guarantee of an infinite mandatory loop or a lethal SW30 fixture.'
],['switching','b_change','growth_all','start_end_full','battlerfull'],'replacement -> position effects -> lethal Rock -> formalFaint/EXP/Judge -> conditional next replacement scan.')
row(848,[
 'SW13 is the legal same-owner three-slot outer0/central2 Shift fixture already fully coupled in CM25.',
 'The swap exchanges battler array residents, their indices and choices, then scene sprites; ten effect-pointer kinds are remapped on living battlers.',
 'The moved-to-center message is followed by BeginTurn, cancellation of multi-turn effects and acted-round marker.',
 'Position effects remain slot-bound; ordinary withdraw/entry/hazard callbacks are not automatically invoked by this position swap.',
 'No executed host animation is inferred from the static Scene call.'
],['use','swap','other','attack','b_change'],'Shift choice -> same-owner swap -> ten pointers -> center message -> Begin/Cancel/acted, no entry.')
row(849,[
 'SW14 assumes a living effect-bearing battler Attract pointer equals one of the two swapped indices.',
 'After the resident/choice/sprite prefix, SwapBattlers rewrites Attract idxA to idxB or idxB to idxA so it continues to identify the same resident.',
 'LeechSeed is deliberately absent from the remap list and retains its source position number.',
 'Other pointers not equal to either swapped index are unchanged; dead battlers are excluded from the allBattlers remap loop.',
 'A scene exception before the remap loop can leave the already swapped residents/choices with old pointers; there is no ensure rollback.'
],['swap','battlefull','battlerfull'],'resident swap -> sprite callback -> living pointer remap Attract; LeechSeed stays positional.')
row(850,[
 'SW15 reaches the ordinary numeric flee calculation after all earlier trainer/debug/canRun/certain/trap checks pass, with raw player speed100 and maximum live opposing raw speed50.',
 'The source uses the raw speed accessor rather than pbSpeed stage/item/field calculation.',
 'Because player raw speed>enemy raw speed, rate is set256.',
 'The rate>=256 short-circuit guarantees local success without invoking battleAI.pbAIRandom for this comparison.',
 'Normal flee audio and paused message precede decision3 and return1, so a presentation exception before the assignment does not guarantee decision3.'
],['running','battlerfull','ai_finite'],'earlier flee gates -> raw100>50 -> rate256 -> no AIRandom -> sound/message -> decision3/return1.')
row(851,[
 'SW16 reaches ordinary numeric flee calculation with raw50/100 and prior runCommand0.',
 'Because duringBattle=false, it increments runCommand first to1.',
 'The integer speed contribution is(50*128)/100=64, then adds1*30 for rate94.',
 'With rate<256 the AI random draw is compared strictly<94; draw93 succeeds and94 fails.',
 'Normal success writes decision3 after feedback and returns1; normal failure feedback returns-1 and retains the incremented runCommand.',
 'Later exception does not roll back the earlier attempt count or any reached feedback.'
],['running','battlerfull','ai_finite'],'ordinary numeric attempt -> count0to1 -> integer64+30 -> strict AIRandom<94 -> success1/failure-1.')
row(852,[
 'SW17 changes the same numeric fixture to duringBattle=true with runCommand0.',
 'It does not increment runCommand, so raw50/100 gives rate64 without the30 increment.',
 'The complete !duringBattle group is skipped: Ghost special case, guaranteed escape ability/item and both ordinary trapping groups are not evaluated there.',
 'Earlier opposing/trainer/debug/canRun branches still precede the numeric calculation and are not bypassed just by duringBattle.',
 'Under those passing earlier gates, draw<64 succeeds; the replacement prompt decides whether to replace based on actual return, not a separate CanRun query.'
],['running','switching','b_settings','ai_finite'],'duringBattle true -> no count increment/no ordinary escape-trap group ->64 -> actual result to EOR replacement bool.')
row(853,[
 'SW18 assumes an ordinary internal trainer run attempt with no DEBUG outcome override.',
 'After the debug result0 it detects trainerBattle and internalBattle, displays forbidden-run feedback and returns0.',
 'It does not enter the raw-speed random attempt or increment runCommand.',
 'RunMenu treats0 as false, so ordinary command selection continues instead of consuming the remaining action choices.',
 'External trainer forfeiting and debug outcome selection are different explicit earlier branches, not exceptions silently applied to this internal fixture.'
],['running','command'],'ordinary internal trainer -> forbidden message ->0 -> menu continues, no numeric attempt/count.')
row(854,[
 'SW19 assumes a successful Roar-like status move against a trainer member with legal same-owner reserve, and all ordinary immunity/root/target/numHits gates passing.',
 'The function failure stage checks active SuctionCups unless MoldBreaker, Ingrain, and actual availability of an incoming party member.',
 'At the post-use drag consumer it requires no earlier switched battler, living user, numHits>0, live affected nonwild target, no Ingrain and no active unbroken SuctionCups.',
 'It randomly chooses from valid CanSwitchIn candidates, recalls/replaces with randomReplacement=true, gives dragged-out feedback and clears that target choice.',
 'The incoming member therefore performs no inherited scheduled action this round; entry notification follows before adding the switched index.',
 'This drag is not an ordinary outgoing trap validation or a new voluntary command; it retains all actual incoming/ability conditions and failure prefixes.'
],['switch_effects_full','switching','b_init','use','checksfull','ability_item'],'status drag failure gates -> actual successful hit -> random valid reserve -> replace/message/clear choice -> entry.')
row(855,[
 'SW20 supplies a sole living wild target with level>user, canRun=true, and earlier ordinary SuctionCups/Ingrain/other target checks not rejecting first.',
 'The status force-out function checks that level comparison in its target-failure method.',
 'It returns true for failure with optional failed feedback before the effect that would write decision3.',
 'Thus no wild escape is produced by this status function; PP/earlier-use prefixes already reached remain rather than being refunded.',
 'The damaging force-out family performs a later conditional escape effect instead and must not inherit this status-family failure contract.'
],['switch_effects_full','checksfull','use','switching'],'solewild canRun and too-highlevel -> status function failure -> no effect decision3; earlier PP retained.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_11e.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
