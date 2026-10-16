"""Manual finite receipt for operative clauses routed outside ItemEffects.

This is evidence assembly, never an implementation or execution of the behavior.
The original owners retain primary authority; these are necessary local joins.
"""
finite=[]
def receipt(fid,line,sources,meanings,ordinary,boundary):
    finite.append(dict(id=fid,operative=dict(path=MAIN,line=line,text=spec_lines[line-1]),
        sources=[dict(path=p,ranges=r) for p,r in sources],manual_meanings=meanings,
        ordinary_control=ordinary,minimal_control=boundary,
        received_by='current delegated /root external_item_atomic_completion',
        source_reader='Personally read finite complete definitions or the explicit central branch; original /root/com_move ownership retained',
        disposition='SUPPORTED_FINITE_JOIN; no whole foreign primary approval',
        failure_prefix='Reached mutations remain if later feedback/helper errors. No transaction or generic end restoration inferred.',
        execution='NOT_EXECUTED'))
BM='Data/Scripts/011_Battle/002_Battler/'
BT='Data/Scripts/011_Battle/001_Battle/'
MV='Data/Scripts/011_Battle/003_Move/'
receipt('F-DISABLE',90,[(BM+'009_Battler_UseMoveSuccessChecks.rb',[[1,100]]),(BM+'003_Battler_ChangeSelf.rb',[[297,325]]),(BM+'002_Battler_Initialize.rb',[[61,64],[128,186]]),(BT+'011_Battle_EndOfRoundPhase.rb',[[312,324],[334,366]])],[
 'Mental Herb clears the Disable count only; ordinary choice/execution compares the retained identity without requiring a positive count.',
 'After count0, the positive-count end-round guard skips expiry and cannot reach that expiry branch identity clear.',
 'Without Herb, the positive count decrements and reaching0 clears identity. Normal initialization and completed Transform independently clear count and identity.',
 'Special usage bypasses the stated Disable gate only; other gates still apply. Later move rejection does not restore completed Herb healing or consumption.'
], 'Live unchanged holder after eligible Herb: count0/identityX, ordinary X rejected.', 'Positive count without Herb can expire; actual reinitialization/Transform clears identity; another move retains its own gates.')
receipt('F-SASH',159,[(MV+'002_Move_Usage.rb',[[184,227],[337,373]])],[
 'Substitute, disguise and ice-face paths precede lethal target handling. Nonlethal/Endure precede the full-HP survival branch.',
 'Only damage clamped to target HP equal to totalHP enters Sturdy, then active Sash, then active Band10% in that order.',
 'Survival records subtract1; later success feedback consumes Sash and leaves Band. These are direct core branches, outside registry emptiness.'
], 'Lethal full-HP target, no earlier survival: Sash leaves1 and later consumes.', 'Starting below fullHP does not enter this snapshot Band branch; Band succeeds only its10% draw and remains held.')
receipt('F-FLINCH',160,[(CALC,[[503,514]]),(BM+'007_Battler_UseMove.rb',[[721,730]])],[
 'Already-flinching moves and non-Mold-Breaker Shield Dust return0. Active Stench or KingsRock/RazorFang queried with allow-fainted gives10.',
 'Active SereneGrace or side Rainbow doubles10 once to20; actual application rejects fainted target and substitute.',
 'Allow-fainted on the attacker item/ability query does not erase the target gate; this query does not consume the item.'
], 'Eligible target and active KingsRock gives10.', 'Rainbow or SereneGrace gives20; existing move flinch or ShieldDust gives0 before item contribution.')
receipt('F-CHOICE',161,[(BM+'009_Battler_UseMoveSuccessChecks.rb',[[1,100]]),(BM+'007_Battler_UseMove.rb',[[97,113]])],[
 'Choice identity is removed when the stored locked move no longer exists; otherwise the choice check applies under its actual active item/ability premises.',
 'Assault Vest rejects status moves only in commandPhase, except UseMoveTargetIsAboutToUse.',
 'Normal end-turn records last regular move only if the lock is nil and current active choice item or GorillaTactics applies; a numerical item multiplier is a separate consumer.'
], 'Command status selection with active Vest rejects.', 'Outside commandPhase the Vest check alone does not reject; choice locking still depends on the actual recorded identity and current premises.')
receipt('F-TYPE',162,[(BATTLER,[[499,510]]),(CALC,[[32,79]])],[
 'Active IronBall grounds before levitation checks; active Balloon supplies airborne state until actual removal.',
 'A Ground attack against a Flying target with active IronBall returns normal overall type multiplier at the explicit earlier branch.',
 'RingTarget changes only originally immune single-type entries to normal; it does not flatten all type multipliers or restore a popped Balloon.'
], 'Flying active IronBall holder meets the explicit Ground normal-return branch.', 'RingTarget on a nonimmune type leaves that component unchanged; absent Balloon does not retain its airborne contribution.')
receipt('F-PROTECT',163,[(BATTLER,[[535,594],[602,609]])],[
 'Effective-weather query maps sun/rain and their strong variants to None for active UtilityUmbrella; unrelated weather remains.',
 'SafetyGoggles excludes applicable powder and sand/hail vulnerability at their own central gates.',
 'ProtectivePads refuses contact-effect permission; contact marking and ordinary damage remain separate from that permission.'
], 'An active umbrella holder has no effective sunny/rainy weather.', 'Umbrella does not erase sand; Pads does not change the original contact flag into a noncontact attack.')
receipt('F-DIRECT',164,[(BM+'003_Battler_ChangeSelf.rb',[[37,52]]),(BT+'011_Battle_EndOfRoundPhase.rb',[[170,187],[288,307]]),(MV+'013_MoveEffects_SwitchingActing.rb',[[261,295]]),(MV+'008_MoveEffects_MoveAttributes.rb',[[751,815]]),(MV+'004_Move_BaseEffects.rb',[[308,349]])],[
 'Named drain and AquaRing/Ingrain recovery requests apply active BigRoot times1.3 then floor at their explicit point, retaining canHeal and other local premises.',
 'Binding rejects fainted/substitute/already-trapped targets; GripClaw sets8 in generation5+ else6, versus random5or6 without it, then records move/user before feedback.',
 'End-round trapping decrements first; count0 emits freedom and returns. Otherwise ordinary denominator8 in generation6+ else16, active trapping-user BindingBand denominator6 else8.',
 'Each named wall starts5; current active LightClay gives8 subject to the wall move own qualification. AuroraVeil still requires its actual Hail gate.',
 'PowerHerb quick-charge commits its effect and consumption before later damage; it is not a blanket multiplier or guaranteed complete move success.'
], 'Eligible current generation wall with active LightClay records8; GripClaw records8 before its first round-end decrement.', 'Removing Claw returns the5or6 draw; an expiring trap never deals that final tick; later damage failure cannot refund reached PowerHerb consumption.')
receipt('F-ATTRACT',165,[(BM+'004_Battler_Statuses.rb',[[506,562]])],[
 'Attract commits the source index and feedback before checking the target active DestinyKnot.',
 'Reflection calls the original source canAttract with the holder; living pair, no existing attraction, opposite non-genderless genders and applicable ability/allied veil guards still matter.',
 'Recursive reflection stops when the earlier recipient is already attracted; item is not consumed, then item/ability cure consumers run in order.'
], 'Eligible opposite pair and active Knot reflects once after first commit.', 'Already-attracted would-be recipient fails the central query; mere continuing attraction is not a fresh reflect event.')
receipt('F-BOOTS',166,[(BT+'005_Battle_ActionSwitching.rb',[[425,468]])],[
 'StealthRock and Spikes each query active Boots at their own gate, with indirect-damage/type or airborne conditions retained.',
 'Live grounded Poison type absorbs ToxicSpikes and clears layers before the non-Poison poison/Boots branch.',
 'StickyWeb retains live/grounded/Boots and lower-speed eligibility gates; its actual stage path may trigger restore later. No universal early return skips all hazards.'
], 'Grounded Poison Boots holder absorbs existing ToxicSpikes.', 'A non-Poison eligible Boots holder avoids poison; no hazard branch consumes Boots.')
receipt('F-REWARD',167,[(BT+'003_Battle_ExpAndMoveLearning.rb',[[1,58],[59,228]]),(BT+'005_Battle_ActionSwitching.rb',[[377,380]])],[
 'Bag EXPALL presence is a reward distribution input, distinct from selected held ExpShare and the held ItemEffects EXP/EV families.',
 'Reward held current/initial-item selection uses its explicit persistent party logic, not active field-item suppression.',
 'Entry money marker checks current AMULETCOIN/LUCKINCENSE identity for the owned player entrant without hasActiveItem; eventual results/world use remains with the original owner.'
], 'Owned player entrant with current AmuletCoin marks the battle money flag.', 'MagicRoom activity suppression alone is not a predicate of this current-identity marker; bag EXPALL never becomes a held handler.')
dump('evidence/finite-body-reception.json',dict(schema='gr8-item-finite-operative-reception/v1',
    rule='Manual necessary joins for every routed current operative clause. These are outside the frozen primary-handler meaning count and cannot approve whole foreign primary files.',
    receipts=finite,receipt_count=len(finite),source_execution='NOT_EXECUTED'))
finite_by_line={r['operative']['line']:r['id'] for r in finite}
