import pathlib, json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_08a.json').read_text());d=base['source_dictionary'];rows=[]
d['ai_finite']={'contribution':'ai-selected-complete-interface-input.json','receipt':'ai-interface-reception.v1.json','original_reader':'/root/com_ai','actual_receiver':'/root/core_atomic_reception','reception':'12 complete named AIU objects, shared premises/failures and 8 complete source identities actually received; 7 bounded joins, no whole963129B reception or allAI policy closure'}
d['entry_exit_handlers']={'actual_reader':'/root/core_atomic_reception','reading':'Personally FULL effect files already read; complete named bodies freshly read for this semantic unit, not allhandler closure','complete_units':[{'path':'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb','range':[367,408]},{'path':'Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb','range':[447,471]},{'path':'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb','range':[3064,3121]}]}
def row(n,c,u,chain,**kw): rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(428,[
 'RecallAndReplace tests the old Battler.fainted? only around scene.pbRecall. Fainted actors skip this animation; the following switchout/lineup/message/binding chain is not globally skipped by that guard.',
 'AttackSwitch initially requires a living registered actor, but after Pursuit only positive battle.decision returns. A newly fainted oldactor with decision0 still reaches RecallAndReplace and can bind the stored candidate; mandatory C0427 clarification governs the earlier shorthand.'
],['switching','attack','battlerfull'],'oldactor liveness→optional recallanimation; later cleanup/replacement remains reached unless earlier error/decision return.',failure='No ensure or rollback around animation/cleanup. If recall raises, later cleanup doesnot run; Pursuit may already have HP/status/choice side effects.')
row(429,[
 'After optional recall, oldactor.pbAbilitiesOnSwitchOut runs before lineup, replacement message or newbinding. Active ability dispatch receives endOfBattle=false.',
 'Default NaturalCure unconditionally assigns NONE once its active caller dispatch is reached; Immunity/Insomnia+VitalSpirit/Limber/MagmaArmor/WaterVeil+WaterBubble assign NONE only for their matching current status. Regenerator, with endOfBattle=false, calls RecoverHP(totalhp/3,false,false). These use the actual Battler setters/recovery and can change persistent Pokemon before replacement.',
 'Then Peer.LeavingBattle receives old Pokemon and usedInBattle[side][fieldindex/2], default endBattle=false; it runs species leave-form hook, conditionally writes a changed truthy form, caps persistent HP only if above new totalhp, then changePokemonOnLeavingBattle.',
 'Active NeutralizingGas writes only old Battler @hp0/@faintedtrue before NGEnding; active Unnerve/AsOne does so before UnnerveEnding. The same local writes also occur unconditionally at the end, followed by primordial weather ending check.',
 'The local HP/fainted writes do not call Pokemon.hp=. Old persistent HP can remain positive and eligible in later same-owner Illusion query; status/recovery/form hooks remain separate genuine persistent writers.'
],['switching','ability_item','entry_exit_handlers','peer','battlerfull','b_change'],'animation→active switchout ability→Peer leaveform→local disable/NG-or-Unnerve ending→primordial end→later replacement.',open=['Species-specific getFormOnLeavingBattle/changePokemonOnLeavingBattle beyond finite received CTF/CAA units remain individually OPEN; the generic dispatch order is actually read.'])
row(430,[
 'Lineup display occurs only when pbSideSize(idxBattler)==1, using the old slot side-size query after its switchout cleanup and before replacement message.',
 'This is a scene call, not partyorder repair or command registration; multi-seat sides skip it regardless of how many current actors remain alive.'
],['switching','battlefull'],'declared current-side size→optional ShowPartyLineup→replacement message.',open=['Concrete ShowPartyLineup visual rendering implementation beyond the finite received UI facts remains OPEN; invocation/gate complete.'])
row(431,[
 'MessagesOnReplace is omitted only by randomReplacement=true in RecallAndReplace. Otherwise it first reads the actual participating party candidate name.',
 'For candidate raw original ability ILLUSION and no active global NeutralizingGas, it queries same-owner pbLastInTeam and substitutes that eligible last member name when index is nonnegative and differs from candidate. This candidate test is not activeability query on the old Battler.',
 'Player-owned outgoing slot chooses greeting from its direct opposing Battler: fainted or HP==totalhp first tier, else HP>=totalhp/2 second, else HP>=totalhp/4 third, else fourth, using integer division. Owner identity is current battle ownership, not original Pokemon Owner.',
 'Nonplayer-owned slot displays current battle owner.full_name plus selected display name; player-side partner ownership can therefore use the nonplayer wording.',
 'LastInTeam enumerates persistent nonnil able members only within current owner segment, retaining maximal partyOrders rank through strict greater-than. It doesnot repair nil ranks or inspect locally disabled old Battler HP.'
],['switching','teams','battlefull','battlerfull','ability_item'],'candidate identity/rawability→optional same-owner rankquery→current battle owner→directfoe integerHP tier→message; all before newbinding.')
row(432,[
 'Replace saves old pokemonIndex, then initializes the existing Battler with candidate persistent Pokemon, candidate party-array index and batonPass argument. InitPokemon rejects egg before copying fields; otherwise it maps current Pokemon.moves to new Battle::Move wrappers and clears participants.',
 'Initialization is InitPokemon→InitEffects(batonPass)→DamageState.reset. The already authored C0110–C0114 complete reset/baton children remain the actual subset contract; no blanket clearing of all persistent Pokemon data or all effects is inferred here.',
 'Only after initialization returns does it swap partyOrder[candidate index] with partyOrder[old Pokemon index]. A nil old display rank can be moved by ordinary array swap; swap doesnot synthesize a missing numeric rank.',
 'Then SendOut runs for the newly bound slot and optional incremental priority calculation follows. An initialization failure may preserve copied fields/reset prefixes while leaving partyorder/sendout untouched; no transaction wraps this sequence.'
],['switching','b_init','movebase','usagefull','battlefull'],'candidate persistentobject→existingruntime binding/move wrappers→effect subset→order exchange→sendout→optional priority.',open=['Concrete Move subclasses and foreign effect consumers referenced by C0111/C0114 remain individually OPEN; those existing pending items are not cleared by this binding-level repeat.'])
row(433,[
 'SendOut first invokes Peer.OnEnteringBattle for every supplied [slot,Pokemon] pair, passing wild flag from newly bound Battler.opposes? && wildBattle?. Only after all these hooks return does scene.SendOutBattlers run.',
 'Peer entry calls getFormOnEnteringBattle, assigns truthy returned form, synchronizes Battler.form if different from Pokemon.form, then changePokemonOnEnteringBattle. Form setter ordering and selected species data use finite CTF reception, not all species proof.',
 'After scene returns, each pair resets that slot command-menu index, then SetSeen(new Battler), then writes usedInBattle[slot&1][slot/2]=true.',
 'SetSeen returns for nil object or !internalBattle; for Battler it passes display species/gender/form/shiny to player.pokedex.register, while Pokemon object takes the other register overload. UsedInBattle write is independent of this internalBattle skip.',
 'UsedInBattle producer index is side plus active field-position/2. Different party Pokemon successively entering the same slot overwrite the same boolean record; this is not reliable per-party-member participation.',
 'Normal ending iterates participating party entries and reads usedInBattle[side][partyindex] for leave hooks. The differing consumer index is already correctly delimited by GR-013/WP41 and is not a new defect or repaired by this review.'
],['switching','peer','battlefull','end','crec_form_join','capture'],'all Peerentry hooks→scene→per-slot menu reset→conditionalPokedex→slot-index used flag; end consumer reads party index, explicit non-equivalence.',open=['All species-specific entry-form handlers beyond selected finite CTF/CAA records and exact Pokedex registration internal storage/display/reload beyond received CAA facts remain OPEN.'])
row(434,[
 'Replacement calls CalculatePriority(false,[idxBattler]) only when Settings.RECALCULATE_TURN_ORDER_AFTER_SPEED_CHANGES is true, after sendout normal completion.',
 'The false full-recalc argument and singleton entry list request incremental actor update; this differs from startup full CalculatePriority(true) and doesnot promise rerunning already executed actions.',
 'Priority may invoke active ability/item priority callbacks; the actual saved bracket/flag and tie/order logic is bound by existing priority FULL source/finite media producer, not an assumption that every speed change re-sorts everything.'
],['switching','priority','b_settings'],'successful replacement/sendout→configtrue→incremental priority callback/sort; earlier failure means no call.')
row(435,[
 'The existing legal player3/opponent ownerA2+ownerB2 triple setup has combined opposing party A0,A1,B0,B1 and initial opposing slots A0/A1/B0 at field1/3/5. OwnerB start2 plus two already sent on the whole side writes display-rank destination4, leaving B0 index2 ranknil and B1 index3 rank3.',
 'A live B0→healthy same-owner B1 can pass CanSwitchIn/duplicate/CanSwitchOut and RegisterSwitch under no trap/duplicate/other mutation. New candidate original ILLUSION, no global active NG and nonrandom replacement guarantee the later message rankquery is reached after oldactor cleanup, provided Pursuit doesnot make positive decision.',
 'The correct WP39/WP41 existing vector includes healthy non-egg B0/B1, actual same owner, ordinary layouts and reached-message premises; missing rank is not itself a universal invalid input or all-actions-fail conclusion.'
],['teams','startendfull','switching','attack','b_init','ai_finite'],'legal multi-owner triple layout→rank write gap→qualified live switchregistration→nonrandom Illusion message; preserve existing correct bounded paragraph.')
row(436,[
 'Before the Illusion replacement message, optional recall and oldactor switchout cleanup have already run; local @hp0/@faintedtrue doesnot zero persistent B0 HP. Both persistent B0 then B1 therefore remain eligible in ownerB LastInTeam enumeration.',
 'First eligible B0 sets ret without comparison; next B1 attempts numeric rank3 > partyOrder[B0]=nil. This local comparison failure precedes new B1 initialization, ordinary partyorder swap, sendout and entry notification.',
 'Earlier recall/ability/Peer/form/local-disable/primordial prefix is not rolled back. No claim is made that every callback was a no-op or that newbinding partially occurred before this particular failure.',
 'AttackPhase diagnostic wrapping may return normally after general error and let its outer phase continue; it doesnot resume the failed replacement method remainder. Host termination and successful switch are not inferred from that outer handling.'
],['teams','switching','ability_item','peer','attack','errors'],'persistenteligibility→nilrank comparison failure after oldcleanup→no newbinding/sendout; outerdiagnostic is separate continuation boundary.')
row(437,[
 'Independent double 2+2 control yields [0,1,3,2], so this B0/B1 comparison has numeric ranks; triple ownerA2+ownerB3 yields [0,1,4,3,2], so B0 rank exists.',
 'Keeping broken ranks but making persistent B0 genuinely fainted removes B0 from LastInTeam eligibility; sole eligible B1 sets ret without this comparison. The rank structure itself remains unrepaired.',
 'No reached Illusion last-member query means the nil rank alone proves neither universal startup failure nor all action failure. Scene party-order unmapped-rank handling has a different actual receiver and cannot stand in for this message path.',
 'UI chosen rank maps back to party index before its actual qualification; AI chooser filters CanSwitchIn and returns party index, with actual registration separate. Neither query repairs partyOrder; no future representation/compatibility policy is prescribed.'
],['teams','switching','scene_party','ai_finite','b_init'],'ordinarycontrols/eligibility/noquery→bounded comparison outcome; distinct UI/AI receivers preserve indexdomain and existing correct scope.')
row(438,[
 'Entry accepts scalar or Array, wraps scalar and flatten!s the supplied array. Unless skip_event_reset, it first clears droppedBelowHalfHP and statsDropped on current living allBattlers.',
 'It takes pbPriority(true) cached speed-only variant and visits only actors whose actual field index is in the entry list and which are not fainted at that visit.',
 'The same entry dispatch doesnot promise a fresh speed recalculation before each callback; startup separately calculates full priority and ordinary replacement has its own optional incremental update.'
],['switching','priority','attack'],'entryindices/flatten→optionalflagreset→cachedspeed snapshot→included living actors; callback mutation/recursive dispatch remains possible.')
row(439,[
 'RecordBattlerAsParticipated sets field.AmuletCoin=true for nonopposing actor with raw item_id AMULETCOIN or LUCKINCENSE. This raw identity check has no itemActive? gate and the routine doesnot clear an already true money flag.',
 'Then all current living allBattlers call UpdateParticipants. That callee only records for a living opposing recipient, appending unique pokemonIndex of living opposing-to-recipient actors.',
 'Participation arrays hold player-side participating party indices for later opposing faint/capture Exp consumer; this differs from usedInBattle slot-index boolean. Exp internalBattle/expGain/ownership/able gates and existing CRE001 clamp limitation remain intact.'
],['switching','b_init','growth','battlefull','money'],'entry actor rawitem→sticky money flag; all-live recipients→unique party participants→later gated Exp/EV, separate from slot used flag.')
row(440,[
 'Shadow entry branch runs after participation and only when newly bound Battler.shadowPokemon?; it invokes Shadow common animation.',
 'Additional Oh! A shadow Pokemon! text is only for opposing shadow actor; own-side shadow actor still gets the animation. This branch doesnot itself modify heart gauge/hyper flag or ownership.'
],['switching','battlerfull','shadowother'],'newactor shadow predicate→animation→opposes textgate; no shadow-state mutation inferred.')
row(441,[
 'HealingWish is position-index state. If present and newactor canHeal? OR status!=NONE, it animates/messages, RecoverHP(totalhp), CureStatus(false), then clears the flag.',
 'If HealingWish is present but actor needs neither HP nor status recovery, generation<8 clears the flag without benefit; default8 retains it for a later entrant.',
 'LunarDance uses the same position ownership and HP/status gates plus any move pp<total_pp. On benefit it recovers HP/status and calls SetPP(total_pp) for each current Battle move before clearing flag.',
 'A full-HP/status-clear/full-PP entrant under LunarDance consumes empty flag only generation<8; default8 retains it. The move SetPP synchronizes realMove PP only matching id and !Transform, so no blanket all temporary move PP persistence.',
 'Animation/message/heal/status/PP occur before final flag clear; later callback/setter failure can leave benefit prefixes and the flag still true. Neither position effect follows the old Pokemon out of its slot.'
],['switching','b_change','b_settings','config'],'positionflag→need gate→ordered healing/status/PP→flagclear; generation-empty branch distinct, realMove PP synchronization conditional.')
row(442,[
 'StealthRock requires side flag, takesIndirectDamage?, registered ROCK type, and no active HeavyDutyBoots. It computes Rock effectiveness from current pbTypes(true), skips immunity, then reduces totalhp*effectiveness/8, displays and checks HP-heal item.',
 'Spikes requires positive layers, indirect-damage eligibility, grounded actor and no active Boots; damage totalhp/[8,6,4][layers-1], then message and HP-heal item. Each hazard uses current state after prior callbacks.',
 'ToxicSpikes requires positive layers, living grounded actor; Poison-type actor absorbs/clears layers before any Boots refusal. Otherwise CanPoison?(nil,false) and !activeBoots cause ordinary poison for one layer or toxic=true for two.',
 'StickyWeb requires side flag, living grounded actor and no active Boots; after caught message, CanLowerSpeed? controls LowerSpeed1(nil source) followed by stat-restore item check.',
 'Damage goes through actual ReduceHP clamping and persistent HP setter, setting half-HP/damage flags only for positive registered damage. Indirect immunity or Boots checks do not imply absorption or all later callbacks skipped.',
 'Hazard writers are sequential, not a single precomputed damage total; heal/status/stat callbacks may affect subsequent state, and an error preserves already committed HP/flags/items/messages.'
],['switching','b_change','battlerfull','ability_item','abilityeffects','item','calculations','typefull'],'side hazards in rock→spikes→toxic→web order→actual HP/status/stage/item consumers with independent live/airborne/active gates.',open=['Complete concrete grounded/indirect immunity and all reached HP-heal/stat-restore/status-protection handler joins beyond already received bounded AbilityItem units remain individually OPEN; no allhazard callback PASS is asserted.'])
row(443,[
 'After the entire EntryHazards routine returns, entry tests b.fainted?. On true it invokes Faint, then GainExp, then Judge, then next for that actor, skipping form/Primal/entry ability/item stages.',
 'Faint itself requires current zero-HP predicate and not already @fainted; otherwise returns. Reached normal faint runs message/scene/defeated, InitEffects(false), status reset, internal happiness, Peer leave, explicit makeUnmega/makeUnprimal, clearChoice/last-fainted/direct-damage fields, faint abilities and primordial ending.',
 'GainExp may play wild-victory BGM before internalBattle/expGain early return. It then considers opposing actors with nonempty participants and fainted/captured state, filters participant persistent able/current owner, and can clear each processed participants array only at normal reached end.',
 'Judge can set a terminal decision, but the entry code here uses next rather than an immediate global return; outer speed-table scan semantics remain the actual source. Any exception in Faint/GainExp/Judge skips its remaining later calls with prior writes retained.',
 'Existing CRE001 negative EV clamp limitation applies to reached rewards; this paragraph is correct ordered invocation, not a guarantee every faint produces a fully completed award.'
],['switching','b_change','growth','startendfull','peer','pokemon_mega_full','clauses'],'hazard return→faint check→Faint→Exp→Judge→nextactor; actual callback failures/terminal decision remain separate.')
row(444,[
 'For actor surviving hazards, entry first CheckForm then pbPrimalReversion(index). Primal here executes entry transformation when Pokemon has an available Primal form and current conditions pass; it is not automatic makeUnprimal.',
 'ContinualAbilityChecks(true) next ends unsupported primordial weather and may Trace a random eligible opposing ability through battle RNG, with show/set/message/hide. Its onSwitchIn=true suppresses its own immediate copied-ability switchin call because outer entry performs that layer.',
 'Outer entry ability dispatch is reached when (!fainted? && unstoppableAbility?) OR abilityActive?, with true switch-in argument; primordial weather ending is checked again after that callback.',
 'Only active item gets OnSwitchIn dispatch, then HeldItemTriggerCheck and AbilityStatusCureCheck are called in that order under their own internal gates. Item/ability callback invocation doesnot by itself prove a message, consumption or cure occurred.',
 'Generic entry and finite CTF form/Mega/Primal records establish ordering/cache/persistent setter prefixes; individual form callbacks, Trace targets, ability/item families still retain their own exact conditions and failures.'
],['switching','b_change','other','ability_item','abilityeffects','item','crec_form_join','pokemon_mega_full','primal_producers'],'survivor→form→Primalenter→continual/Trace→entry ability→weather recheck→active entryitem→heldtrigger→statuscure.',open=['All nonselected species CheckForm/MultipleForms handlers and all concrete OnSwitchIn/HeldItem/StatusCure producer→consumer joins remain individually OPEN where not yet explicitly bound by the received 80-family/463-registration evidence.'])
row(445,[
 'After the entered-actor loop, it traverses the same cached speed order: first each actor.pbItemOnStatDropped, and only if false its pbAbilitiesOnDamageTaken. First truthy result breaks this particular scan; it is not one exit for an entire recursive replacement cascade.',
 'Item stat-loss dispatcher requires statsDropped and active item. Ability dispatcher requires droppedBelowHalfHP and active ability. ReduceHP sets the flag only when positive registered damage crosses from >=integer totalhp/2 to <that threshold; recovery and new event-reset can change the later facts.',
 'Default EjectPack rejects SkyDrop relations, opposing side all fainted, wild bearer, inability to switch out or no eligible nonactive. Reached use animates/messages and ConsumeItem(true,false) BEFORE EOR branch or replacement selection.',
 'At EOR EjectPack only recalls if living, runs switchout cleanup and returns true. Otherwise it asks replacement index; negative returns false after the already consumed item/message, while nonnegative recalls/replaces, clears choice, conditionally clears MoldBreaker for matching move_user, recursively runs entry, then returns true.',
 'EmergencyExit/WimpOut reject SkyDrop relations. In wild battle opposing multi-seat bearer refuses, then CanRun controls message/sound and decision3/true. Trainer branch refuses all opposing fainted, CanSwitchOut false or no candidate before splash/message.',
 'Trainer EmergencyExit at EOR only recalls/cleans out and returns true; otherwise negative chosen replacement returns false after messages, nonnegative replacement/clearChoice/MoldBreaker/recursiveentry then true. This is distinct from EjectPack consumption and from all item/ability callbacks returning true.',
 'After this scan normal completion clears droppedBelowHalfHP and statsDropped on all current living actors; errors before that leave flag prefixes. Recursive entry owns another reset/scan and can select additional exits.'
],['switching','ability_item','entry_exit_handlers','b_change','running','ai_finite'],'entry damage/stage flags→speed item-first/ability-second→firsttruthy localbreak→normalflagclear; actual exit recursion and consume-before-cancel retained.')
row(446,[
 'Command-selected SwitchOut attack stage performs recall message and Pursuit, returns only if positive decision, then clears halfHP/statsDropped on all current living actors BEFORE RecallAndReplace.',
 'It then invokes entry(index,true), skipping entry-start event reset. A newly set EjectPack flag from old NeutralizingGas ending during RecallAndReplace therefore survives into this entry final exit scan.',
 'Ordinary entry calls with skip_event_reset=false clear these flags on current living actors at entry start; the two reset times intentionally differ. The later common end reset remains a separate write.',
 'The parameter changes reset timing only; it doesnot bypass hazard/eligibility hooks, guarantee a replacement completes, or introduce a second post-Pursuit faint guard.'
],['attack','switching','ability_item','entry_exit_handlers'],'Pursuit/decision→pre-recall liveflagclear→NG-ending possible newflag→entry skipreset→local exit scan→normal finalclear.')
row(447,[
 'Persistent Pokemon HP, realMove PP, status/count, level and held item remain on their referenced individual; changing active slot doesnot itself replace or clear the party object.',
 'Actual switchout NaturalCure/status handlers, Regenerator, form recalc/HP cap and item callbacks can genuinely modify those persistent fields, so preservation is object identity rather than no field ever changes.',
 'Runtime stages/effects use complete reset/baton subset already authored in C0110–C0114. Move wrappers are rebuilt from new Pokemon moves; writes through PP depend on realMove matching id and !Transform.',
 'Serialization/reload remains only the finite KERNEL registered-object/save facts actually received. Native Marshal recursion or whole post-reload battle continuation is NOT_EXECUTED and not inferred from object references.'
],['battlerfull','b_init','b_change','ability_item','entry_exit_handlers','peer','capture'],'old/new persistent identities→specific real writers versus runtime reset→conditional realMove synchronization; no blanket clear or immutability.')
row(448,[
 'Ordinary switchout runs active switchout ability, Peer leave-form family and primordial ending, but has no generic makeUnmega/makeUnprimal call. Surviving Kyogre/Groudon primal forms have only finite received getPrimalForm registrations and no generic getUnprimalForm/leave reversal in their supplied registration facts.',
 'Explicit makeUnmega/makeUnprimal occurs on reached normal Faint and normal battle cleanup, separately from ordinary withdrawal; source not idealized into uniform every-leave transformation reversal.',
 'PrimalReversion invoked at entry means entering primal form through Pokemon.makePrimal and runtime/UI update, not undo. Selected raw orb/species records/form setter/cache order are received in CTF package.',
 'Switchout local @hp0/@faintedtrue supports NG/Unnerve cleanup and runtime inactivity. Persistent Pokemon HP can remain positive; only actual recovery/form-cap/other callback writers change it, not those bare local assignments.'
],['ability_item','peer','b_change','end','other','pokemon_mega_full','crec_form_join','primal_producers'],'ordinaryleave hookfamily/localdisable versus explicit faint/end transformation undo; preserve correct WP41 scoped paragraph.')
row(449,[
 'Replace alone exchanges candidate and old Pokemon index entries in partyOrder after initialization, before SendOut.',
 'Shift swaps active Battler objects, their field indices, choices and sprites and remaps specified active effect references. It has no partyOrder exchange and doesnot create a new party Pokemon binding.',
 'Both routines may fail after partial writes; neither provides an atomic party/order/effect transaction. This comparison doesnot prescribe a future rank representation repair.'
],['switching','swap','other','use'],'replacement partyidentity change→partyorder exchange; Shift activeposition change→explicit targetremap, persistentparty order unchanged.')
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_08b.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children'])for x in rows),'open_rows':sum(bool(x.get('open'))for x in rows)})
