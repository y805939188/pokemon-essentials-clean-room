import datetime, hashlib, json, pathlib, subprocess
V=pathlib.Path(__file__).parent
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B='fd1df570cad987dc3852a3b958f03916e317f7fe'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
F=json.loads((V/'forward-mapping.json').read_text()); REV=json.loads((V/'reverse-mapping.json').read_text())
assert len(F['atoms'])==1532
rows=[]
def a(unit,meaning,receiver,source='R01'):
    rows.append((source,unit,meaning,receiver))
for unit,meaning,receiver in [
 ('FakeBattler.initialize10–14','Both fake battlers reference battle.party2[0], retain battle and supplied slot index; they do not represent actual player-party members.','F06§4.2L59–60:fake-identity'),
 ('FakeBattler.pokemonIndex16','Every fake battler reports party index0.','F06§4.2L59:fake-party-index'),
 ('FakeBattler.owned8/initialize10–14','The plain owned reader has no constructor assignment; owned? is a distinct live-query method.','F06§4.2L59/§13:audited-owned-reader'),
 ('FakeBattler.isSpecies28–30','Species predicate delegates with safe navigation to the underlying Pokemon; absent Pokemon yields nil here rather than a fabricated species.','F06§4.2L59:fake-species-predicate'),
 ('FakeBattler.fainted32','Fake fainted? always returnsfalse, irrespective of the underlying Pokemon HP.','F06§4.2L59:fake-fainted'),
 ('FakeBattler.shadow33','Fake shadowPokemon? always returnsfalse.','F06§4.2L59:fake-shadow'),
 ('FakeBattler.hasMega34','Fake hasMega? always returnsfalse.','F06§4.2L59:fake-mega-qualification'),
 ('FakeBattler.mega35','Fake mega? always returnsfalse.','F06§4.2L59:fake-mega-state'),
 ('FakeBattler.hasPrimal36','Fake hasPrimal? always returnsfalse.','F06§4.2L59:fake-primal-qualification'),
 ('FakeBattler.primal37','Fake primal? always returnsfalse.','F06§4.2L59:fake-primal-state'),
 ('FakeBattler.captured38–39','Fake captured getter always returnsfalse and setter changes no state.','F06§4.2L59:fake-capture-flag'),
 ('FakeBattler.owned41–43','Fake owned? asks live global $player.owned?(underlying species), without using its unset owned field.','F06§4.2L59:live-owned-query'),
 ('FakeBattler.pbThis45–47','Wild display-name phrase uses lower/upper initial wording according to lowerCase truthiness.','F06§4.2L59/§13:fake-display-phrase'),
 ('FakeBattler.opposes49–52','Fake opposes accepts another FakeBattler or numeric index and compares index parity.','F06§4.2L59:fake-side-parity'),
 ('FakeBattler.pbReset54','Fake reset has no effect.','F06§4.2L59:fake-reset'),
 ('SafariDataBox.initialize63–76','Safari data box starts selected0, retains battle, loads the safari databox bitmap and builds a matching contents bitmap.','F06§8.3/§13:databox-creation'),
 ('SafariDataBox.initialize68–74','Databox starts at screen width−232,height−184, invisible,z50; it sets system font then refreshes.','F06§8.3/§13:databox-layout'),
 ('SafariDataBox.refresh78–87','Databox refresh clears/redraws its bitmap and displays Safari Balls plus live battle.ballCount, rather than a separate stock count.','F06§4.4L79/§8.3:databox-current-budget'),
 ('SafariDataBox.refresh81–85','Databox text uses dark72 and shadow184 RGB triples, with label at30,14 and remaining balls at30,44.','F06§8.3/§13:audited-rendering-parameters'),
 ('ThrowBait.initialize96–100','Bait animation retains fake battler and resolves trainer through its battle owner helper before parent animation construction.','F06§4.4L80/§13: bait-animation-owner'),
 ('ThrowBait.create102–132','Bait starts at player sprite x and vertical half-height; its endpoint is battler position−40,−4, with midpoint y122, twelve-frame trajectory and Battle throw sound.','F06§4.4L80/§13:bait-trajectory-intent'),
 ('ThrowBait.create120–123','Wide trainer bitmap (width≥2×height) uses throwing frames and their returned ball origin before trajectory timing.','F06§4.4L80/§13:bait-trainer-frames'),
 ('ThrowBait.create130–150','Bait fades8 frames after arrival over2, hides after10, then the battler jumps twice and tilts/eats twice; these are animation-process instructions, not proof of rendered timing.','F06§4.4L80/§13:bait-animation-sequence'),
 ('ThrowRock.initialize160–164','Rock animation retains fake battler and resolves its trainer through the same owner helper before parent construction.','F06§4.4L81/§13:rock-animation-owner'),
 ('ThrowRock.create166–195','Rock uses the player half-height origin, midpoint y122, endpoint at target sprite midpoint and twelve-frame trajectory, then weak-damage sound, opacity fade and hide.','F06§4.4L81/§13:rock-trajectory-intent'),
 ('ThrowRock.create183–186','Rock also conditionally uses wide trainer throwing frames before setting delay from ball duration.','F06§4.4L81/§13:rock-trainer-frames'),
 ('ThrowRock.create197–211','Rock creates anger sprite at endpoint−42,−36; two visibility/zoom130→100 cycles each end with hide and a96,−16 offset.','F06§4.4L81/§13:anger-animation-sequence'),
 ('Scene.pbSafariStart219–230','Safari scene clears brief-message state, creates player-slot databox, updates its appear animation and scene until done, then disposes that animation and refreshes.','F06§4.2/§8.3:safari-scene-start'),
 ('Scene.pbSafariCommandMenu232–239','Safari command menu uses the real player name and Ball/Bait/Rock/Run labels with command menu mode3.','F06§4.4L75:four-command-menu'),
 ('Scene.pbThrowBait241–250','Scene bait clears brief state, creates animation using battler1, interleaves animation/scene updates until done, then disposes normally.','F06§4.4L80/§13:bait-animation-driver'),
 ('Scene.pbThrowRock252–261','Scene rock clears brief state and drives/disposes battler1 rock animation using the same update ordering.','F06§4.4L81/§13:rock-animation-driver'),
 ('Scene.animation drivers219–261','These animation drivers have no ensure disposing after arbitrary update error; native media/resource success remains unverified.','F06§10L271–272/§13L285:animation-error-prefix'),
 ('Scene.pbThrowSuccess263–268','Success wrapper first calls the captured prior success implementation; only a SafariBattle then gets an additional wild-success scene request.','F06§4.5L90/§13:safari-success-scene'),
 ('SafariBattle274/293','Safari is its own class including CatchAndStoreMixin, rather than a subclass running ordinary Battle command/attack/end flow.','F06§4.2L60:safari-independent-flow'),
 ('SafariBattle.pbRandom295','Safari random directly calls globalrand(x), without recording wrapper or playback index.','F06§4.4L80–85/ F05§5.1L103:safari-random-domain'),
]:a(unit,meaning,receiver)

for method,line,target in [('species',17,'species'),('gender',18,'gender'),('status',19,'status'),('hp',20,'hp'),('level',21,'level'),('name',22,'name'),('totalhp',23,'totalhp'),('displayGender',24,'gender'),('shiny?',25,'shiny?'),('super_shiny?',26,'super_shiny?')]:
    a(f'FakeBattler.{method}{line}',f'Fake {method} forwards to the underlying Pokemon {target} getter; it doesnot cache a separate battle value.',f'F06§4.2L59:fake-{method}-forward')

for line,meaning,label in [
 (301,'Safari constructor retains supplied scene.','scene'),(302,'Safari constructor creates an ordinary Battle::Peer.','peer'),
 (303,'Safari backdrop constructor default is empty string.','backdrop'),(304,'Safari backdropBase constructor default is nil.','backdropBase'),
 (305,'Safari time constructor default is0.','time'),(306,'Safari environment constructor default is None.','environment'),
 (307,'Safari weather constructor default is None.','weather'),(308,'Safari decision starts0.','decision'),(309,'Safari caught queue starts empty.','caught-queue'),
 (310,'Safari player collection contains exactly the supplied player object.','player-reference'),(311,'Safari party2 retains the supplied party array reference.','party-reference'),
 (312,'Safari side sizes start[1,1].','side-sizes'),(313,'Safari creates fake battlers at slots0 and1.','battlers'),
 (315,'Safari rules starts as an empty dictionary.','rules'),(316,'Safari battle ballCount starts0 before wrapper copies the session budget.','budget'),
]:a(f'initialize{line}',meaning,f'F06§4.1L55/§4.2:constructor-{label}')
for unit,meaning,receiver in [
 ('constructor300–317/accessors275–291','Constructor doesnot set internalBattle, sendToBoxes, canRun/canLose, switchStyle/showAnims, expGain or moneyGain; prepared option fields remain a distinct later step.','F06§4.1L55/§4.2L60–61:unset-fields'),
 ('disablePokeBalls319','Safari disablePokeBalls= is an empty setter.','F06§4.1L55/§13:audited-ball-disable-setter'),
 ('sendToBoxes320','Safari sendToBoxes= is an empty setter and leaves the instance field unset; ordinary full-party ask/must-add branches therefore do not become active through normal preparation.','F06§4.5L90:safari-no-send-menu'),
 ('defaultWeather321','Safari defaultWeather= writes its weather value used by start and subsequent round weather animation lookup.','F06§4.1L55/§4.4L85:weather-preparation'),
 ('defaultTerrain322','Safari defaultTerrain= changes no state.','F06§4.1L55/§13:audited-terrain-setter'),
 ('wildBattle327/trainerBattle328','Safari reports wildtrue and trainerfalse.','F06§4.2L60:battle-kind'),
 ('setBattleMode330','Safari setBattleMode ignores the requested mode.','F06§4.2L60/§13:audited-layout-setter'),
 ('pbSideSize332–334','Safari side size indexes the mutable sideSizes array using index modulo2.','F06§4.2L59:side-size-reader'),
 ('pbPlayer339/opponent340','Safari player is the first supplied player; opponent returnsnil.','F06§4.2L60:player-opponent'),
 ('pbGetOwner342','Safari owner lookup returns its player for every battler index.','F06§4.2L59:owner-lookup'),
 ('pbSetSeen344–352','Safari seen registration first rejects absent receiver or falsey internalBattle; normal constructor leaves that flag nil, so it returns before Dex writes.','F06§4.2L61:seen-internal-gate'),
 ('pbSetCaught354–361','Safari caught registration has the same absent/internal gate and returns without caught registration for the default nil flag.','F06§4.2L61:caught-internal-gate'),
 ('pbParty366–368','Safari party query returns party2 for the opposing parity and nil for the player side.','F06§4.2L60:no-player-battle-party'),
 ('pbAllFainted370','Safari all-fainted query always returnsfalse, so ordinary catch helper doesnot set decision from that query; Safari sets4 after storing.','F06§4.4L79:own-capture-decision'),
 ('opposes375–379','Safari opposition accepts any receiver responding to index, then compares numeric parities against default side0.','F06§4.2L59:side-comparison'),
 ('pbRemoveFromParty381','Safari removing captured Pokemon from party is an empty operation.','F06§4.2L59–60:capture-remove-noop'),
 ('pbGainExp382','Safari experience entry is empty, including if shared catch helper calls it under the capture setting.','F06§4.2L60:no-exp'),
 ('display387–401','Safari regular, paused, brief and confirmation messages delegate to their distinct corresponding scene methods.','F06§4.4/§8.3:message-forwarding'),
 ('pbAbort403–407','Safari raises its own BattleAbortedException class; it is distinct from ordinary Battle abort class.','F06§4.4L86:safari-abort-type'),
 ('pbEscapeRate413','Catch rate≤45 yields escape baseline125.','F06§4.3L68:escape-first-interval'),
 ('pbEscapeRate414','Catch rate>45 and≤60 yields baseline100.','F06§4.3L68:escape-second-interval'),
 ('pbEscapeRate415','Catch rate>60 and≤120 yields baseline75.','F06§4.3L68:escape-third-interval'),
 ('pbEscapeRate416','Catch rate>120 and≤250 yields baseline50.','F06§4.3L68:escape-fourth-interval'),
 ('pbEscapeRate417','Catch rate>250 yields baseline25.','F06§4.3L68:escape-last-interval'),
 ('pbStartBattle422–426','Safari start reads first opponent, requests seen registration, starts scene, displays wild appearance, then starts Safari databox.','F06§4.2L59–61:start-order'),
 ('pbStartBattle427–429','Safari looks up current weather and conditionally requests its animation, then resolves SAFARIBALL through Item registry.','F06§4.1L55/§4.4L79:start-weather-and-ball'),
 ('pbStartBattle430–432','Initial catch factor is integer catch_rate×100÷1275, then clamped3..20.','F06§4.3L67:catch-factor'),
 ('pbStartBattle433–434','Initial escape factor is integer baseline×100÷1275, then clamped2..20.','F06§4.3L69:escape-factor'),
 ('pbStartBattle436–442','Ball command first checks global player/storage joint fullness; a true result displays full message and nexts before ball decrement/factor clamp/round random.','F06§4.4L79:capacity-no-consumption'),
 ('pbStartBattle443–444','An allowed Ball decrements ballCount unconditionally before scene refresh and throw, with no positive-budget gate here.','F06§4.4L79/§10L268:ball-decrement-prefix'),
 ('pbStartBattle445','Throw uses integer rare=catchFactor×1275÷100, giving38 at factor3 and255 at factor20.','F06§4.3L71:rate-reconstruction'),
 ('pbStartBattle446–451','With resolved Safari ball, throw targets index1, uses rare and showPlayertrue; nonempty caught queue then runs record/store before assigning decision4.','F06§4.4L79/§4.5L90:throw-store-before-decision'),
 ('pbStartBattle448–450','An exception during caught record/store can occur before Safari writes decision4; prior capture/consumption/registration is not rolled back.','F06§4.4L86/§10L271:caught-store-failure-prefix'),
 ('pbStartBattle453–457','Bait displays brief text and animation before drawing rand100; catchFactor halves only for r<90, while escapeFactor always halves using integer division.','F06§4.4L80:bait-effects-order'),
 ('pbStartBattle458–462','Rock displays brief text and animation, always doubles catchFactor, then doubles escapeFactor only for rand100<90.','F06§4.4L81:rock-effects-order'),
 ('pbStartBattle463–466','Run plays flee sound, displays paused safe escape, then assigns decision3; it never performs an escape-probability gate.','F06§4.4L82:run-order'),
 ('pbStartBattle467–469','Invalid or cancelled command immediately selects again before clamps, budget check or random escape.','F06§4.4L83:invalid-no-round'),
 ('pbStartBattle470–471','Every completed recognized action clamps catchFactor3..20 and escapeFactor2..20 before unresolved-round handling.','F06§4.3L70:post-action-clamps'),
 ('pbStartBattle473–478','Only decision0 performs round-end budget/escape/messages/weather; budget≤0 takes priority and writes decision2 after sound/message.','F06§4.4L85:budget-before-escape'),
 ('pbStartBattle478–481','With positive budget and unresolved result, escape occurs only if rand100<5×escapeFactor; equality doesnot escape.','F06§4.4L85:strict-escape-comparison'),
 ('pbStartBattle482–488','If neither budget-end nor escape, the message is eating for Bait, angry for Rock, otherwise watching.','F06§4.4L85:action-feedback'),
 ('pbStartBattle490–491','Weather is looked up/animated inside the initially unresolved-round branch even after that branch has just assigned decision2 or3.','F06§4.4L85:weather-after-round-result'),
 ('pbStartBattle493–495','Loop exits when decision>0 and normally ends scene with that result.','F06§4.4L85:normal-scene-end'),
 ('pbStartBattle420–501','The own abort rescue encloses scene setup, action loop and normal scene-end call; caught abort writes0 and calls scene-end again, without undoing balls or earlier effects.','F06§4.4L86:safari-abort-rescue-scope'),
 ('pbStartBattle496–500','Arbitrary errors are not caught by the dedicated abort rescue; even its rescue scene-end can fail, so normal result/writeback is not guaranteed.','F06§10L271–272:nonabort-failure-boundary'),
]:a(unit,meaning,receiver)

for unit,meaning,receiver in [
 ('Scene.pbInitSprites5–14','BugContest scene alias calls prior sprite initialization, then adds an initially invisible help window at z90.','F06§6.3L169:comparison-window-init'),
 ('Scene.pbShowHelp16–22','Comparison help resizes to text across screen width, places x/y0, assigns text and makes visible.','F06§6.3L169:comparison-window-show'),
 ('Scene.pbHideHelp24–26','Comparison hide only clears window visibility.','F06§6.3L169:comparison-window-hide'),
 ('BugContestBattle32','Contest battle inherits the ordinary Battle pipeline and its catch handling, with the named local overrides.','F06§6.1L155:ordinary-battle-inheritance'),
 ('initialize35–39','Contest constructor starts ballCount0 and resolves SPORTBALL id before ordinary constructor super.','F06§6.1L155/§6.2L161:contest-budget-and-ball'),
 ('pbItemMenu41–43','Contest item menu directly registers its Sport Ball for target1, with no inventory/ball-budget menu gate in this override.','F06§6.2L161,163:sport-direct-registration'),
 ('pbCommandMenu45–52','Contest command menu displays remaining Sport balls then Fight/Ball/Pokemon/Run with menu mode4.','F06§6.2L160:contest-command-menu'),
 ('pbConsumeItemInBag54–56','Contest consume method ignores item and battler arguments; it decrements budget only while budget>0 and never accesses globalBag.','F06§6.2L161,163:contest-consume-override'),
 ('pbStorePokemon59–65','If stock exists, Contest displays its name and comparison containing both names, levels and totalHP, not currentHP.','F06§6.3L169:stock-comparison-fields'),
 ('pbStorePokemon66–68','Confirming replacement assigns the new Pokemon reference as stock before hiding the help window.','F06§6.3L169:confirm-replace-prefix'),
 ('pbStorePokemon69–72','Declining hides help and immediately returns without assigning stock or final caught message; earlier capture/Dex/stat writes remain.','F06§6.3L169:decline-new-stock'),
 ('pbStorePokemon73–76','Without previous stock, Contest directly retains the new Pokemon reference, then displays caught message.','F06§6.3L168,170:first-stock'),
 ('pbStorePokemon58–77','Contest stock override never calls ordinary nickname/Peer/party/storage acceptance; that occurs only at normal session-end receiving.','F06§6.3L167–171:stock-not-final-receiving'),
 ('pbStorePokemon58–77','No ensure hides the help window after arbitrary confirm/assignment/message failure; already assigned stock is not restored.','F06§5.2L126/§10L271:stock-ui-failure-prefix'),
 ('pbEndOfRound79–82','Contest calls ordinary end-of-round first; only normally returning base EOR with budget≤0 and decision0 is overwritten to3.','F06§6.4L175:contest-EOR-gate'),
 ('pbEndOfRound79–82','An existing win/capture/loss/draw result remains unchanged by this override, even at zero or negative budget.','F06§6.4L175/F08SF19:existing-result-preserved'),
]:a(unit,meaning,receiver,'R02')

for unit,meaning,receiver,source in [
 ('pbBoxesFull4–6','Prethrow capacity is live global $player.party_full? AND global Storage.full?; short-circuit skips Storage when party has room.','F06§4.4L79/F08SF07:joint-capacity','SF-CAPACITY'),
 ('PokeBallEffects.modify15–18','Ball rate dispatcher returns handler result unless nil, and otherwise preserves the supplied catch rate.','F06§4.4L79/§6.2L162:ball-handler-dispatch','SF-BALLS'),
 ('SAFARIBALL51–53','Safari Ball ordinary-target rate handler returns input×1.5.','F06§4.4L79/F14§4L57:safari-ball-rate','SF-BALLS'),
 ('SPORTBALL171–173','Sport Ball ordinary-target rate handler returns input×1.5.','F06§6.2L162/F14§4L58:sport-ball-rate','SF-BALLS'),
 ('CaptureCalc207','Debug+CTRL returns4 before all other capture math.','F06§4.4L79/§6.2L162/F14§3L37:debug-capture-shortcut','SF-CATCH'),
 ('CaptureCalc209','Only falsey supplied catch_rate falls back to Pokemon species_data.catch_rate; explicit0 is truthy and retained.','F06§4.4L79/F14§3L38:provided-rate-truthiness','SF-CATCH'),
 ('CaptureCalc211–215','UltraBeast target with actual thrown ball other than BEASTBALL divides rate by10 and skips rate handler; bag possession of Beast Ball is not this condition.','F06§4.4L79/§6.2L162/F08SF12:actual-ball-ultra-gate','SF-CATCH'),
 ('CaptureCalc217–219','HP numerator uses fake/real battler totalHP A and currentHP B, with catch_rate.to_f before dividing by3A.','F14§3L40/F06§4.4L79:HP-float-stage','SF-CATCH'),
 ('CaptureCalc221–222','Actual battler status SLEEP or FROZEN multiplies floating x by2.5.','F14§3L40/F06§4.4L79:sleep-freeze-rate','SF-CATCH'),
 ('CaptureCalc223–224','Any other actual status except NONE multiplies floating x by1.5.','F14§3L40/F06§4.4L79:other-status-rate','SF-CATCH'),
 ('CaptureCalc226–227','Only after status multiplication does x floor, then clamp to minimum1.','F14§3L40/F06§4.4L79:floor-position-and-lower-bound','SF-CATCH'),
 ('CaptureCalc229','x≥255 returns4 without a random draw; otherwise a true unconditional-ball handler also returns4.','F14§3L41/F06§4.4L79:deterministic-return','SF-CATCH'),
 ('CaptureCalc231','The shake threshold y floors65536 divided by(255.0/x)^0.1875.','F14§3L42/F06§4.4L79:shake-threshold','SF-CATCH'),
 ('CaptureCalc233–246','Critical-capture setting gates live global Player Dex owned_count lookup and initializes modifier0.','F14§3L43/F06§4.4L79:critical-setting-and-live-dex','SF-CATCH'),
 ('CaptureCalc236–237','Owned count>600 gives critical modifier5.','F14§3L43:critical-owned600','SF-CATCH'),
 ('CaptureCalc238–239','Owned count451..600 gives modifier4.','F14§3L43:critical-owned450','SF-CATCH'),
 ('CaptureCalc240–241','Owned count301..450 gives modifier3.','F14§3L43:critical-owned300','SF-CATCH'),
 ('CaptureCalc242–243','Owned count151..300 gives modifier2.','F14§3L43:critical-owned150','SF-CATCH'),
 ('CaptureCalc244–246','Owned count31..150 gives modifier1; count≤30 remains0.','F14§3L43:critical-owned30','SF-CATCH'),
 ('CaptureCalc247','Live globalBag holding CATCHINGCHARM doubles the critical modifier.','F14§3L43:critical-charm','SF-CATCH'),
 ('CaptureCalc248–250','Critical entry threshold c uses integer x×modifier÷12; c≤0 skips even the rand256 draw; otherwise strict r<c decides entry.','F14§3L43/F06§4.4L79:critical-entry-draw','SF-CATCH'),
 ('CaptureCalc251–253','Entered critical capture sets criticalCapturetrue and draws one rand65536; r<y returns4, otherwise0 with no ordinary shake loop.','F14§3L43/F06§4.4L79:critical-one-shake','SF-CATCH'),
 ('CaptureCalc257–262','Ordinary shake loop starts0, draws at most4 rand65536 with strict r<y, and stops before the next iteration after the first failure.','F14§3L44/F06§4.4L79:ordinary-short-circuit-shakes','SF-CATCH'),
 ('RecordAndStore88–107','Record/store iterates caught queue in order: caught registration, seen registration, own/Dex path, Shadow-own path, then mode-specific store; clear occurs only after the complete loop returns.','F06§4.5L90/§6.3L169/F14§6L108:record-store-order','SF-CATCH'),
 ('RecordAndStore93–100','Unowned species gets owned write without internalBattle gate; only live global hasPokedex+unlocked-species conditions add the display/lastSeen/page path.','F06§4.5L90/F14§6L108:owned-write-vs-presentation','SF-CATCH'),
 ('RecordAndStore102','Shadow-owned direct write precedes mode store when actual Pokemon shadow predicate is true.','F06§4.5L90/F14§6L108:shadow-owned-before-store','SF-CATCH'),
 ('Store5–15','Ordinary store skips nickname for actual Shadow Pokemon; otherwise nickname requires option0 and a true confirmation, then writes returned name before storage.','F06§4.5L90/F14§6L110:nickname-gates','SF-CATCH'),
 ('PeerStore5–9','When the supplied trainer has party room, Peer appends the same Pokemon object and returns−1 before checking Storage.','F06§4.5L90/F14§6L114:party-append-receiver','SF-PEER'),
 ('PeerStore10–16','Full-party Peer optionally heals while restoring ready-to-evolve, then records currentBox and requests global Storage.pbStoreCaught.','F14§6L114–115:full-party-storage-prefix','SF-PEER'),
 ('PeerStore17–21+census','Negative StoreCaught reaches Peer.pbDisplayPaused before the intended old-box return. Fixed scripts supply no such Peer/global fallback method, so default binding fails there; no normal old-box return is promised.','F14§6L114:full-storage-missing-method-prefix','SF-PEER'),
]:a(unit,meaning,receiver,source)

premise=('FixedR/B8 default aliases/load order without later overrides. Normal Safari wrapper uses actual globalPlayer and one valid Pokemon with positive totalHP; configured catch-rate/HP/status numerics and registry/Storage/scene/callback dependencies are valid to each stated observation unless a named error or boundary is given. '
         'Contest ordinary command, capture and EOR gates remain their finite inherited contracts, not universal success of every injected item or malformed state. '
         'Scene animation process descriptions are only source instructions; media, native rendering, frame/clock/random outputs and real capture/save/game execution remain unverified. '
         'Named getter/stub/geometry details are source audit scope, without imposing new internal API or pixel-compatible product requirements.')
new=[]
for n,(source,unit,meaning,receiver) in enumerate(rows,1533):
    atom={'id':f'FAC-A{n:04}','source':source,'unit_locator':unit,'assertion':meaning,'formal_receivers':[receiver],'premise':premise,'pending_dependencies':[],
          'status':'BOUNDED_SOURCE_FACT_AND_EXPLICIT_FORMAL_CHILD_OR_AUDIT_SCOPE_ROUTING','formal_relation':'Explicit Safari/Contest local field/flow or necessary shared capture finite child; allSF case prerequisites and cross-domain semantic denominator remain separate.',
          'evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','reader':'/root/facility_atomic_completion_cloud'}
    new.append(atom);REV['mappings'].append({'formal_clause':receiver,'atomic_assertion':atom['id'],'meaning':meaning,'source':source,'source_unit':unit,'premise':premise,'status':atom['status'],'pending_dependencies':[],'relation':'EXPLICIT_NAMED_FORMAL_CHILD_OR_DECLARED_SOURCE_AUDIT_SCOPE'})

paths={'SF-CAPACITY':'Data/Scripts/019_Utilities/002_Utilities_Pokemon.rb','SF-BALLS':'Data/Scripts/011_Battle/007_Other battle code/010_Battle_PokeBallEffects.rb','SF-CATCH':'Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb','SF-PEER':'Data/Scripts/011_Battle/007_Other battle code/004_Battle_Peers.rb'}
ids={};buffers={}
for key,path in paths.items():
    b=subprocess.check_output(['git','-C','/workspace/pokemon-essentials','show',R+':'+path]);buffers[key]=b.decode().splitlines();ids[key]={'repo':'/workspace/pokemon-essentials','commit':R,'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':subprocess.check_output(['git','-C','/workspace/pokemon-essentials','rev-parse',R+':'+path]).decode().strip()};F['source_identities'][key]=ids[key]
formalpath='deliverables/final-specification-set/pokemon-rules/wp38-capture-and-receiving.md';bb=subprocess.check_output(['git','-C','/workspace/pokemon-essentials-clean-room','show',B+':'+formalpath]);fid={'repo':'/workspace/pokemon-essentials-clean-room','commit':B,'path':formalpath,'bytes':len(bb),'sha256':hashlib.sha256(bb).hexdigest(),'blob':subprocess.check_output(['git','-C','/workspace/pokemon-essentials-clean-room','rev-parse',B+':'+formalpath]).decode().strip()};F['source_identities']['F14']=fid
units=[]
for key,lo,hi,name in [('SF-CAPACITY',4,6,'Complete global capacity helper'),('SF-BALLS',4,28,'Complete ball handler dispatcher module'),('SF-BALLS',51,53,'Complete Safari Ball handler'),('SF-BALLS',171,173,'Complete Sport Ball handler'),('SF-CATCH',88,107,'Complete caught queue record/store'),('SF-CATCH',206,263,'Complete capture calculation'),('SF-PEER',5,24,'Complete Peer storage')]:
    units.append({'source':key,'identity':ids[key],'range':[lo,hi],'name':name,'content':'\n'.join(buffers[key][lo-1:hi]),'actual_reader':'/root/facility_atomic_completion_cloud','qualification':'Complete named unit only; Catch271/Peer77 ownwhole text reception separately retained.'})
F['atoms'].extend(new);F['bounded_denominator']=len(F['atoms']);F.setdefault('v2_increments',[]).append({'path':'safari-contest-battle-atomic-increment.v2.json','count':len(new),'ids':[new[0]['id'],new[-1]['id']],'utc':NOW})
REV['true_bounded_assertions']=len(F['atoms']);REV['v2_new_exact_child_bindings']=len(REV['mappings'])-992
packet={'schema':'facility-safari-contest-battle-manual-meaning-increment/v2','utc':NOW,'reader':'/root/facility_atomic_completion_cloud','explicit_source_assertions':new,'source_identities':{**{k:F['source_identities'][k] for k in ['R01','R02','R12','R18','F06','F08','F14']},**ids},'complete_supplemental_units':units,
        'source_receipts':['17ddac fullR02 andR01L1–200','2907f9 R01L201–400','3e550b R01L401–502','5fc327 complete capacity/ball units and Catch finite reread','58dc26 caught record/store','9b5ae1 completePeer77 reread','dfce07 missingPeer/global message fallback fixedscriptcensus'],
        'formal_receipts':['9dd9a6 WP53L1–112','568aa8 WP53L114–215','6cdc9f WP53L216–288','a64a8e+c65c18 wholeWP38 146L','2274b9 SF01–40 fullrows'],
        'qualification':'Finite manual source assertions only, not a full normalized Safari/Contest/SF denominator or qualification of every UI/World/Item/Dex/PBS prerequisite. Source role/callback order/real thrown ball and live receiver distinctions preserved. WP38 full current text now read; only necessary Safari/Sport capture receiving meanings adopted, not all26balls/completeShadow/partner semantics approval.',
        'source_fallback_precision':'Peer negative Storage result doesnot guarantee oldBox return: undefined default Peer message call comes first. This is already correctly bounded in currentWP38L114; no newfinding/required change.',
        'new_required':0,'new_optional':0,'new_contexts':0,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
def dump(name,obj):(V/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
dump('safari-contest-battle-atomic-increment.v2.json',packet);dump('forward-mapping.json',F);dump('reverse-mapping.json',REV)
P=json.loads((V/'progress.json').read_text());P.update(updated_utc=NOW,manually_authored_finite_source_assertions=len(F['atoms']),source_to_formal_bindings=len(REV['mappings']),finite_new_child_bindings=len(REV['mappings'])-992,state='RUNNING_SF_CATALOG_CHILDREN_GENERATOR_AND_PBS_PROOF_TAILS');dump('progress.json',P)
D=json.loads((V/'atomic-denominator.json').read_text());D['updated_utc']=NOW;D['manual_bounded_source_assertions'].update(count=len(F['atoms']),id_end=new[-1]['id']);D['finite_reverse_bindings'].update(count=len(REV['mappings']),qualification=f"992historicalregionbindings+{len(REV['mappings'])-992}newexplicitmanualchild/audit routes; not globalformaldenominator.");D['finite_safari_contest_battle']={'children':len(new),'membership':'safari-contest-battle-atomic-increment.v2.json','qualification':packet['qualification']};dump('atomic-denominator.json',D)
L=json.loads((V/'reading-ledger.json').read_text());L['updated_utc']=NOW;L.setdefault('v2_additional_source_reads',[]).append({'utc':NOW,'packet':'safari-contest-battle-atomic-increment.v2.json','complete_new_named_units':['capacity4–6','ball dispatch4–28','Safari51–53','Sport171–173'],'prior_own_full_reread':['R01all502','R02all83','Peer77','Catch271necessarymethods'],'qualification':packet['qualification']});L.setdefault('additional_formal',[]).append({'id':'F14','identity':fid,'read_ranges':[[1,146]],'actual_full_read':['a64a8e','c65c18'],'qualification':'Wholecurrent146Ltext; finite Safari/Sport capture receiver adoption only, no allball/Shadow/partner/source proof credit.'});dump('reading-ledger.json',L)
print('new',len(new),'ids',new[0]['id'],new[-1]['id'],'total',len(F['atoms']),'bindings',len(REV['mappings']))
q=(V/'safari-contest-battle-atomic-increment.v2.json').read_bytes();print('packet',len(q),hashlib.sha256(q).hexdigest())
