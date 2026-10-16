import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_10d.json').read_text());d=base['source_dictionary'];rows=[]
d['position_heal_producers']={'path':'Data/Scripts/011_Battle/003_Move/010_MoveEffects_Healing.rb','complete_units':[[341,358],[590,608],[614,632]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete Wish/HealingWish/LunarDance classes personally read; no whole Healing file'}
d['shadow_shed_raw']={'path':'PBS/Shadow Pokémon backup/moves_shadow_pkmn.txt','complete_records':[[193,202]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete optional SHADOWSHED raw record; actual compiled registration/load is separate'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
rows.append(dict(number=734,layout_reason='Position-record table heading only. FutureSight four fields, Wish three and two position-heal flags are distinct payload records, not new behavior from a heading.'))
row(735,[
 'FutureSightCounter initializes 0, FutureSightMove nil, FutureSightUserIndex -1 and FutureSightUserPartyIndex -1 per target position.',
 'AttackTwoTurnsLater is a position-targeting Move; initial setup refuses an already positive counter at the target slot.',
 'In setup effect it writes Counter3, the actual Move ID, user.index and user.pokemonIndex in that target position.',
 'It saves no final damage amount; setup-mode damaging/accuracy/display overrides defer the later attack.',
 'Each reached EOR FutureSight helper with nonzero counter decrements it, returning if still positive.',
 'At 0 it resolves the current target slot and current source identity/party index, then executes or takes a specific early return.',
 'Auxiliary cleanup is only the final normal path; 0-counter early returns can preserve old metadata without automatic retry.',
 'Position ownership persists when occupants change; the original target Pokemon need not be the later receiver.'
],['activefield_full','misc_full','eor_all','b_init','use'],'position setup 3 + identity -> actual local countdown -> current occupant/source resolution -> special move call or early return, exact cleanup follows C758–760.')
row(736,[
 'Wish initializes Counter0, Amount0 and Maker-1 per position.',
 'Wish Move rejects an already positive own-position counter.',
 'Successful effect writes Counter2.',
 'It writes Amount=round(user.totalhp/2.0) using total HP at establishment, not current missing HP.',
 'It writes Maker=user.pokemonIndex for later naming.',
 'Reached EOR helper decrements a nonzero Wish and at 0 heals only a current nonnil canHeal receiver at that same slot.',
 'The creating Pokemon need not remain in that position; source index is used for pbThisEx naming, not receiver identity equality.'
],['activefield_full','position_heal_producers','eor_all','battlerfull','battlefull','b_change'],'own slot Wish2/creation amount/source party index -> two reached ticks -> current canHeal occupant -> actual HP recovery, not original HP deficit.')
row(737,[
 'HealingWish and LunarDance initialize false per position.',
 'Each producer first requires pbCanChooseNonActive?(user.index): at least one actual party candidate passing pbCanSwitchIn.',
 'The ordinary Move use/healing eligibility fronts remain separate; an eligible replacement is not a guarantee the entire Move succeeds.',
 'In the respective pbSelfKO method, an already fainted user returns; otherwise ReduceHP(user.hp,false) and ItemHPHealCheck precede the position flag true.',
 'The flag is written in the self-KO stage, rather than inferred from later formal faint notification.',
 'Formal user Faint resets member effects but does not reconstruct the position container, so it does not erase a flag already placed there.',
 'Ordinary entry calls position recovery; Ally Switch explicitly calls it for both swapped positions after a successful same-owner/unique-near-ally swap.',
 'Shift by itself does not supply that recovery notification; identical underlying swapping does not imply identical callers.',
 'Current gen8 can retain a no-benefit flag for later named position notification; earlier generation consumes it even with no benefit.'
],['activefield_full','position_heal_producers','switching','misc_full','battlefull','other','b_change','use','b_settings'],'replacement-eligible Move -> selfKO HP/item prefix -> flag at source slot -> later actual position notification -> benefit/old-gen clear or gen8 retain.',failure='HP can be 0 before item-check/flag or formal Faint. If an earlier selfKO dependency fails, later flag/normal replacement not guaranteed. A later failure does not undo a written position flag.')
row(738,[
 'SeaOfFire early helper processes each side with a nonzero counter by decrementing before damage.',
 'A counter reduced to 0 immediately skips this damage pass.',
 'Otherwise current priority members on that side need takesIndirectDamage and non-Fire type; nominal amount is integer totalhp/8.',
 'It uses TakeEffectDamage with actual HP minimum/clip, message, HP-item/half-ability/Faint chain, rather than only a direct field decrement.',
 'Later side-ending helper independently decrements the same SeaOfFire if still positive and sends ending message at 0.',
 'From initial4 with both phases completed: first round 4->3/damage->2, next round 2->1/damage->0/end message.',
 'From initial1: early1->0 skips damage; later helper sees 0 and does not produce its own decrement-to-0 message.',
 'An early decision/exception skipping the later helper invalidates that complete double-decrement vector; do not rewrite this as four ordinary damage ticks.'
],['eor_all','activefield_full','battlerfull','b_change','ability_item'],'earlier SeaOfFire --/maybe damage -> later generic side --/expiry; two different actual consumers, execution premise explicit.')
row(739,[
 'CraftyShield duplicate true fails before the common last-in-round query.',
 'CraftyShield also needs another nonfainted unmoved UseMove/Shift battler.',
 'MatBlock rejects user.turnCount>1 and then last-in-round; its class has no separate same-side MatBlock duplicate check.',
 'Quick/Wide Protect-parent duplicate fails and resets ProtectRate1.',
 'Gen<=5 consecutive ProtectRate>1 can draw and fail; gen>=6 side type skips only that draw.',
 'The later last-in-round gate still applies in current generation and resets ProtectRate1 on failure.',
 'Other item/switch choices, already moved members, self and fainted members are not qualifying pending actions.',
 'Only passed effect writes side flag true and multiplies ProtectRate by 3 current /2 old before message.',
 'Complete EOR tail clears the four side flags; it does not globally clear every user record.'
],['side_protect_producers','protect_parent_complete','usagefull','battlerfull','eor_all','b_settings'],'distinct gates -> protected side flag and personal rate writes -> full-tail reset; no actor-count shortcut.')
row(740,[
 'CraftyShield target check requires its side flag, different user/target indices, statusMove and a target mode that is not targets_all.',
 'WideGuard requires its side flag, different indices and target-mode num_targets>1; generation>=7 accepts status as well as damaging Moves.',
 'QuickGuard requires the common canProtectAgainst gate and a positive priority saved in choices[user.index][4].',
 'MatBlock requires its side flag and damagingMove inside the common canProtectAgainst group.',
 'Active user UNSEENFIST plus raw contactMove bypasses the enclosing Wide/Quick/Mat and ordinary protection group, but CraftyShield is checked earlier outside it.',
 'A reached protection writes target.damageState.protected and user successState.protected before returning failure, after any guarded presentation.',
 'These are target-success gates in their fixed ordering, not a new universal accuracy multiplier; other earlier/later qualifications remain as WP40.'
],['checksfull','battlerfull','priority','target_modes','use'],'fixed target-success order -> specific flag/target-mode/priority/contact gates -> presentation + protection state -> false; not all flags same effect.')
row(741,[
 'CourtChange swaps AuroraVeil.', 'It swaps LightScreen.', 'It swaps Mist.', 'It swaps Rainbow.',
 'It swaps Reflect.', 'It swaps Safeguard.', 'It swaps SeaOfFire.', 'It swaps Spikes.',
 'It swaps Swamp.', 'It swaps Tailwind.', 'It swaps ToxicSpikes.', 'It swaps StealthRock.', 'It swaps StickyWeb.',
 'Its Move rejects only when all selected numeric entries on both sides are 0 and selected booleans false.',
 'The complete effect exchanges each selected pair at its existing value without refreshing durations or layer counts.',
 'LuckyChant, four current-round guard flags, EchoedVoiceCounter/Used, Round and LastRoundFainted are not among the selected 13 and remain on their original sides.',
 'The broad source comment about all side effects is narrower in executable arrays; do not enlarge this into swapping all22.',
 'If a later message fails, all completed pair writes remain; it is not a rollback transaction across the loop and presentation.'
],['misc_full','activefield_full'],'explicit 11 numeric +2 boolean selected IDs -> per-pair exchange -> message; nonselected 9 records untouched by this class.')
row(742,[
 'RemoveScreens complete Move ignoresReflect for its damage calculation.',
 'Reached EffectGeneral clears positive opposing LightScreen to0 then its feedback.',
 'It likewise clears opposing Reflect and AuroraVeil in that fixed order.',
 'It neither selects all side effects nor removes the same three from both sides by this class.',
 'Actual Move use front/target outcome determines whether this general-effect stage is reached; definition alone does not guarantee clearing on every attempt.'
],['screens_lucky_producers','use','calculations'],'ordinary Move process -> reached general effect -> opposing three screens sequential clear; ignoring reduction is a separate function property.')
row(743,[
 'ScreenCleaner OnSwitchIn returns if both sides all three selected screen values are 0.',
 'Otherwise it shows an ability splash, then clears positive opposing AuroraVeil/LightScreen/Reflect followed by own-side same three, with each message.',
 'It does not clear Mist/Safeguard/LuckyChant/hazards or every side record in this complete handler.',
 'Actual OnSwitchIn caller abilityActive/registration gates still govern invocation; a stored ability name alone is not enough.',
 'Message/scene failure after one clear can leave a prefix of the six clear operations; no all-side atomicity or complete splash cleanup guarantee.'
],['abilityeffects','ability_item','battlerfull','switching'],'actual active OnSwitchIn dispatch -> exact six screen clears -> splash hide on normal return; complete family qualification separate.')
row(744,[
 'Defog target failure check first permits target-side positive AuroraVeil/LightScreen/Reflect/Mist/Safeguard.',
 'It also permits target-side any StealthRock/Spikes/ToxicSpikes/StickyWeb.',
 'Gen>=6 permits any of those four hazards on the target opposing side.',
 'Gen>=8 permits any non-None terrain; otherwise it falls back to the actual stat-down parent eligibility.',
 'Reached effect attempts EVASION decrease if its actual stage query permits, but cleanup does not depend on that decrease succeeding.',
 'It clears target-side three screens, Mist and Safeguard individually to0.',
 'It clears target-side four hazards; gen>=6 clears the other side same hazards.',
 'Gen>=8 directly clears current terrain None after feedback, preserving the old duration and avoiding natural expiry/default restart loops.',
 'It does not clear LuckyChant/Tailwind or unlisted side records; partial writes remain after later callback/presentation failure.'
],['defog_complete','targetstatdown_parent','stages','eor_all','weather_core_complete'],'specific existing effect permits target continuation -> optional stat decrease -> exact walls/hazards -> gen terrain clear; not an all-side reset.')
row(745,[
 'RapidSpin class uses its dedicated pbEffectAfterAllHits, conditional on user not fainted and target.damageState.unaffected false.',
 'If trapped, it resolves saved trapping Move/user for message, then clears Trapping0/TrappingMovenil/TrappingUser-1.',
 'If seeded, it clears LeechSeed-1 before its feedback.',
 'It clears own StealthRock false, Spikes0, ToxicSpikes0 and StickyWeb false, individually with messages.',
 'Its gen>=8 Speed raise is a separate pbAdditionalEffect calling the StatUp parent; the dedicated clear method does not test whether Speed rose.',
 'Inherited Move success/target state and the final all-hits call determine reachability; do not recast it as an effect on every individual hit.',
 'Other-side hazards and all unrelated own-side effects remain outside this class clear list.'
],['misc_full','use','stages','move_default_callbacks'],'complete after-all-hits phase -> live/user + affected target -> trapping/seed/own hazard cleanup; independent additional-effect stage for current Speed increase.')
row(746,[
 'When a legal registered Move binds exact RemoveAllScreensAndSafeguard and ordinary fronts pass, its whole-Move check accepts any positive AuroraVeil/LightScreen/Reflect/Safeguard on either side.',
 'All eight counters nonpositive fails with ordinary failure feedback.',
 'Reached general effect writes own-side AuroraVeil0/LightScreen0/Reflect0/Safeguard0 and other-side the same four to0.',
 'It then gives one barrier-broken feedback instead of invoking each natural expiry helper.',
 'Mist/Tailwind/LuckyChant/four hazards and other records are not assigned by this class.',
 'The bound identity is distinct from RemoveScreens and from the optional raw RemoveAllScreens string.'
],['shadowother','movebase','use','activefield_full'],'exact content function binding -> any-positive of eight guard -> two-side four-record clear -> one feedback; no inferred family-name alias.')
row(747,[
 'Optional raw SHADOWSHED record is Status, TargetBothSides, FunctionCode RemoveAllScreens; this raw record alone is not loaded/compiled registration proof.',
 'Fixed Ruby defines RemoveAllScreensAndSafeguard, not an automatic normalization from that shorter content identity.',
 'Move factory resolves exact function class name, falling back to Unimplemented when absent; a status Unimplemented fails whole-Move check.',
 'Only a legal actual binding to exact implemented RemoveAllScreensAndSafeguard receives the eight-clear contract in C746.',
 'Definition, optional content sample, actual default registration/reachability and native execution remain separate evidence scopes.',
 'For the implemented bound path, a callback/presentation failure after completed writes does not undo that prefix; no game/host execution was performed.'
],['shadowother','shadow_shed_raw','movebase','unimplemented','use'],'raw function ID -> exact class lookup (no guessed alias) -> fallback status failure OR explicit implemented bound clear; scoped source lookup, not plugin absence proof.',open=['Optional data default load/compiled identity/event use/native results remain unexecuted and not inferred from raw backup record.'])
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_10e.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
