import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_10e.json').read_text());d=base['source_dictionary'];rows=[]
d['statup_parent_complete']={'path':'Data/Scripts/011_Battle/003_Move/004_Move_BaseEffects.rb','range':[85,105],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete StatUpMove actual read, including additional-effect stat eligibility/raise; no whole BaseEffects'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
def layout(n,why):rows.append(dict(number=n,layout_reason=why))
row(748,[
 'Ordinary entry callback first records participation/messages, then calls position recovery before pbEntryHazards.',
 'The complete hazards method orders StealthRock, Spikes, ToxicSpikes, then StickyWeb.',
 'Rock/Spikes may invoke item HP healing immediately after their own damage/message, changing current HP before subsequent hazards.',
 'Each later hazard rechecks its own living/grounding/item/status/stage conditions; one hazard immunity does not imply all are skipped.',
 'After the whole hazards method returns, ordinary entry checks fainted, formally faints, grants experience and judges before continuing next battler.',
 'A surviving receiver then continues form/Primal/continuous ability/OnSwitchIn/item/status checks, with later common emergency-switch checks.',
 'Hazard existence, a particular receiver being ineligible, and poison-type absorption deleting ToxicSpikes are distinct state outcomes.'
],['switching','battlerfull','b_change','ability_item','statuses_full','stages'],'ordinary entry -> position healing -> Rock/Spikes/Toxic/Web with per-stage checks/item HP -> formal Faint/judge or further entry; no single hazard boolean for all.')
layout(749,'Hazard table column heading only; four complete payload records C750–753 carry individual eligibility, writes and lifetimes.')
row(750,[
 'StealthRock requires its side flag and takesIndirectDamage, which rejects fainted and active MagicGuard.',
 'It separately requires a registered ROCK type and absence of active HEAVYDUTYBOOTS.',
 'It obtains the current complete pbTypes(true) list and calls base Effectiveness.calculate(ROCK,*types).',
 'This table calculation multiplies each current type effectiveness with float normalization; it does not invoke ordinary Move immunity/conversion/StrongWinds/etc adjustments.',
 'An ineffective type result skips HP damage/message/item heal.',
 'Otherwise nominal damage totalhp*eff/8 passes to ReduceHP, which rounds, clips current HP and enforces living minimum1.',
 'HP write precedes pointed-stone feedback and item HP-heal check; airborne alone is not a predicate in the complete Rock branch.',
 'Rock hazard flag is not removed just because this receiver is immune or wears Boots.'
],['switching','battlerfull','typefull','b_change','ability_item'],'Rock flag + indirect/record/item gates -> current type table product -> nonzero amount -> HP rounded write -> message -> item healing; no flight exemption.')
row(751,[
 'Spikes requires a positive own-side layer count and takesIndirectDamage.',
 'It additionally requires !airborne and absence of active Boots; it does not call affectedByTerrain.',
 'One ordinary layer selects divisor8.', 'Two layers select divisor6.', 'Three layers select divisor4.',
 'Integer totalhp/divisor is passed to ReduceHP minimum/clip boundary, then message and item HP-heal check.',
 'Layer record is not consumed by ordinary application and is not owned by the original setter.',
 'Malformed layer counts outside the ordinary producer range are not silently clamped by this lookup; normal valid default state is the premise.'
],['switching','battlerfull','b_change','ability_item','misc_full'],'positive1/2/3 layer -> grounding/item/indirect gates -> integer fraction -> HP/message/item check; no side-record removal.')
row(752,[
 'ToxicSpikes requires positive layers, a nonfainted entering battler and !airborne.',
 'A current POISON-type receiver first absorbs: ToxicSpikes0 before absorption message.',
 'That poison-type branch precedes Boots checks, so active Boots does not prevent grounded poison absorption.',
 'Nonpoison receiver calls pbCanPoison?(nil,false) before the Boots rejection check.',
 'That query delegates ordinary pbCanInflictStatus(POISON,nil,false,nil): faint/current status/Substitute/terrain/type/ability and other actual gates apply.',
 'The ordinary Safeguard check needs a nonnil Move argument, absent here; side-name immunity alone cannot be imported into ToxicSpikes.',
 'If eligible and no active Boots, exactly2 layers calls pbPoison with toxic=true, otherwise the ordinary valid1 layer uses false.',
 'InflictStatus writes POISON and its count through actual setters; callback/message/ability/status-item checks can follow those writes.',
 'Nonpoison rejection or Boots prevention does not clear the hazard; airborne poison never enters the absorption branch.'
],['switching','battlerfull','statuses_full','abilityeffects','ability_item'],'grounded live -> poison absorption before Boots OR nil-source ordinary poison query -> Boots -> status setter/toxic count; distinct persistence outcomes.')
row(753,[
 'StickyWeb requires its side flag, live receiver, !airborne and no active Boots.',
 'It sends its caught-in-web message before querying stage loss.',
 'It calls pbCanLowerStatStage(SPEED) with nil user/Move; if permitted it calls LowerStatStage(SPEED,1,nil), then item stat restoration.',
 'Contrary is checked early and can redirect the eligibility and actual change into a raise, under current MoldBreaker gates.',
 'MirrorArmor redirection needs a nonnil distinct user in both eligibility/actual mutation paths; nil-source Web does not supply one.',
 'Mist, Substitute and actual ability/stat-min checks remain their ordered nil-source stat-query gates; not every ability name has an unconditional effect.',
 'The side Web flag remains after application or ineligible stage loss; current member stages/items may change, not the hazard record itself.',
 'A message failure can precede any stage write; a later stat animation/ability/item failure may preserve already changed stages.'
],['switching','battlerfull','stages','ability_item','abilityeffects'],'Web live/grounded/no Boots -> feedback -> nil-source ordered stage query/change -> item stat restoration, preserving side flag.')
row(754,[
 'Boots are queried as an active item for each applicable hazard, not a delete-hazards command.',
 'Grounded poison with Boots still clears ToxicSpikes because absorption is tested before Boots.',
 'Airborne poison does not absorb; the outer grounded/live gate is earlier than type absorption.',
 'Hazards use airborne where listed; terrain affected additionally rejects six semi-invulnerable functions, so the two queries are not interchangeable.',
 'Boots suppressed by MagicRoom/Embargo/CorrosiveGas/activeKlutz or fainted default gate do not supply the active-item immunity.'
],['switching','battlerfull'],'actual per-hazard item/airborne order -> apply/skip/absorb; preserved hazard unless explicit poison absorption/removal writes it.')
row(755,[
 'Wish setup writes Counter2 and creation-time round(totalhp/2), not the current missing-HP difference.',
 'Each reached Wish EOR visit with nonzero counter decrements it; positive remainder waits.',
 'At0, current slot must contain a battler passing canHeal: live, missingHP and no positive HealBlock.',
 'A valid successor in the same slot can receive the saved amount after creator replacement.',
 'Naming uses pbThisEx(slot, saved Maker party index) and the current party context; source name is not a frozen string.',
 'Empty/fainted/full/HealBlocked receiver loses this due recovery after counter already becomes0; it is not held at1 for a later attempt.',
 'This expiration helper does not clear Amount or Maker; counter0 disables automatic further triggering.',
 'A subsequent new Wish may overwrite counter0 and its old auxiliary metadata.',
 'Successful HP recovery is before the came-true message; failure in name lookup can occur after counter0 but before HP write.'
],['position_heal_producers','eor_all','battlerfull','battlefull','b_change'],'Wish2/snapshot amount -> actual tick to0 -> current canHeal occupant/name -> HP write/message OR no retry, auxiliary metadata retained.')
row(756,[
 'Entering-position notification processes HealingWish before LunarDance.',
 'HealingWish flag triggers if canHeal OR raw status !=NONE; it does not require both.',
 'Passed OR gate calls animation/message, RecoverHP(totalhp), CureStatus(false), then clears HealingWish false.',
 'LunarDance checks all actual moves for pp<total_pp; its trigger is canHeal OR raw status!=NONE OR any PP deficit.',
 'Passed LunarDance OR calls animation/message, RecoverHP(totalhp), CureStatus(false), then SetPP(total_pp) for each move, then clears flag.',
 'Those are not three independently gated repairs after the OR. An HP eligibility rejection alone does not forbid the branch when status or PP supplies another benefit.',
 'RecoverHP clips/rounds/minimum at its own write; CureStatus uses Battler status= and the actual permanent Pokemon write-through.',
 'SetPP always changes the battle Move; it writes realMove.pp only for matching ID, a real Move and no Transform, preserving that sync boundary.',
 'Thus model HP/status/eligible PP can persist on original Pokemon before later flag clear/message; no unconditional complete transaction.'
],['switching','battlerfull','b_change','statuses_full','persistent_move'],'position flags -> benefit OR gate -> ordered HP/status/(PP) writers -> flagfalse; persistent write-through exact, not all-field guarantee.',failure='Presentation can fail before repairs; later HP/status/PP failure can leave a prefix and still-true flag, permitting later notification. No ensure rollback/clear.')
row(757,[
 'If HealingWish has no HP/status benefit, gen<8 clears its flag; gen>=8 leaves it true.',
 'If LunarDance has no HP/status/PP benefit, gen<8 clears its flag; gen>=8 leaves it true.',
 'PP deficit alone can consume LunarDance, but does not satisfy HealingWish benefit test.',
 'Formal fainting of the source does not clear already established position flags, because only member effects are initialized there.',
 'A later actual position notification may consume retained current-gen flags; mere time/round advancement does not invoke that notification by itself.'
],['switching','b_change','b_init','position_heal_producers','b_settings'],'benefit absent -> old-gen clear/current-gen retain -> later explicit entry/AllySwitch notification; position record independent of source faint.')
row(758,[
 'FutureSight creation counter is3; each actual nonzero visit decrements before target/source checks.',
 'At0, empty or fainted current target returns before source reconstruction.',
 'It searches current allBattlers for the saved source side and saved pokemonIndex, not necessarily the original slot.',
 'If found source is itself at the target position, it returns without attacking itself.',
 'Only when no current source exists does it look up saved-side party[saved index].',
 'That party object must exist and be able; otherwise no reconstructed source and an early return.',
 'For an able off-field source it constructs Battler at the saved source slot then calls InitDummyPokemon with the current Pokemon.',
 'Dummy copies current name/species/form/level/HP/types/stats/status/party reference, while intentionally not copying ability, item or ordinary move list.',
 'These are later current inputs, not an earlier saved final damage value or a full ordinary active battler clone.'
],['misc_full','eor_all','b_init','battlefull','battlerfull'],'Counter3 -> reached tick0 -> current target/source search -> optional current able party dummy -> special call or early exit, exact ownership retained.')
row(759,[
 'Only the able off-field source reconstruction creates a new Battler and executes InitBlank then InitEffects(false) before copying source Pokemon.',
 'During that initialization, each current living battler pointing Attract at the saved slot is cleared to-1.',
 'JawLock pointing at the saved slot is cleared to-1.',
 'MeanLook pointing there is cleared to-1.',
 'Octolock pointing there is cleared to-1.',
 'SkyDrop pointing there is cleared to-1.',
 'A positive LockOn with matching LockOnPos is cleared: count0 and position-1.',
 'A matching TrappingUser clears Trapping0 and User-1, without clearing that other battler TrappingMove identity in this cross-clean loop.',
 'Pointers to other slots are unaffected by those equality checks; relationships newly made by a replacement in the saved slot can still be cleared.',
 'On-field source path skips reconstruction, so it has no such additional constructor cross-clean.',
 'Target unavailable/no able off-field source earlier returns do not run these constructor side effects.',
 'These cross-clean writes precede later source copy/attack result, so later miss/immunity/exception does not roll them back.'
],['eor_all','b_init','battlefull','battlerfull'],'off-field able source -> Battler constructor InitEffects(slot) -> actual living-pointer equality clears -> InitDummy copy -> later attack; source context not silently pure.')
row(760,[
 'Executable FutureSight uses saved Move ID and current target slot through pbUseMoveSimple with default specialUsage true.',
 'Simple use creates a fresh Move with pp-1 when no move-list index was supplied; its ordinary current data binding still applies.',
 'Caller first saves moveUser.lastMoveFailed then sets battle.futureSight true.',
 'After a normally returned special call it sets futureSight false and restores that prior failure record.',
 'It then formally faints the target if current HP says fainted.',
 'Only after those steps does it clear Counter0, Movenil, UserIndex-1 and UserPartyIndex-1.',
 'Earlier target/source returns leave already-decremented0 and auxiliary metadata; counter0 prevents automatic retry and permits a later new setup.',
 'If the call or later target faint throws before final cleanup, actually reached flags/HP/relationships may remain; no ensure protects futureSight/failure restoration.',
 'Damage inputs and special-call ordering follow current data/WP43 and WP40, rather than an immutable setup-time damage snapshot.'
],['eor_all','use','misc_full','b_init','battlerfull','movebase','persistent_move'],'savedID/current target -> save failure + futureSighttrue -> special current Move -> normal restore -> target Faint -> final metadata clear; early/fault prefixes explicit.')
row(761,[
 'Common SwapBattlers rejects absent residents, opposing sides and different owner indices before swapping.',
 'Successful common swap exchanges resident objects, their index values and choice rows, requests sprite swap, then retargets the ten named member-pointer effects.',
 'It does not exchange @positions or invoke position healing, hazards or full entry by itself.',
 'Therefore Wish/FutureSight/HealingWish/LunarDance remain assigned to the old slots after common swap.',
 'Shift branch invokes common swap, its own movement feedback, BeginTurn/CancelMoves and round-moved marker, without extra position/entry call.',
 'AllySwitch Move checks exactly one nearby same-owner ally, common-swaps, then explicitly notifies entering-position for both resulting slot occupants.',
 'That AllySwitch extra callback can consume position healing; it still does not call pbEntryHazards or full entry.',
 'A sprite/message failure can interrupt before pointer retarget or extra position notification after some resident/index/choice writes; no atomic swap-and-all-callback guarantee.'
],['battlefull','swap','other','use','misc_full','switching'],'caller-specific Shift vs AllySwitch -> common resident/choice/10pointer swap, position container fixed -> only AllySwitch extra recovery notifications.')
layout(762,'Catalog navigation/count: W7+T4+F3+S7+H4+P7+C1=33 static rows; listed topics are not executed tests or proof all semantic children accepted. Exact catalog row inputs/outputs follow at their own locators.')
layout(763,'Upstream dependency and historical bounded-pass wording is a responsibility pointer, not this context approving all of WP11/59/43/44 or inheriting their runtime evidence. Actual relevant consumers separately named.')
layout(764,'Downstream whole family/mode/UX/Demo responsibility declaration; no family-wide acceptance from merely enumerating these links.')
layout(765,'Explicit unresolved scope for unexpanded families/full terminal/facility combinations/runtime; readable necessary code continues independently, no material-limit claim.')
layout(766,'Debug/Recorded direct weather or terrain assignment has a separate caller scope; this paragraph explicitly does not equate it with normal Move entry contracts. Detailed receiver acceptance remains in actual bounded FAC/DEV interfaces.')
layout(767,'Static NOT_EXECUTED qualification: no reference process/game/native test was run; tool success means evidence I/O only.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_10f.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
