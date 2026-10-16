"""Serialize this receiver's hand-authored finite review; never run reference code."""
import datetime
import hashlib
import json
import pathlib
import subprocess

OUT = pathlib.Path(__file__).resolve().parent
PROJECT = OUT.parents[6]
REFERENCE = pathlib.Path('/workspace/pokemon-essentials')
TASK = OUT.parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
READER = '/root/core_atomic_reception/core_round_reset_producer_tail'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
B8 = 'fd1df570cad987dc3852a3b958f03916e317f7fe'

def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args]).decode().strip()

paths = {
 'battle': '001_Battle/001_Battle.rb',
 'priority': '001_Battle/004_Battle_ActionAttacksPriority.rb',
 'switch': '001_Battle/005_Battle_ActionSwitching.rb',
 'run': '001_Battle/007_Battle_ActionRunning.rb',
 'attack': '001_Battle/010_Battle_AttackPhase.rb',
 'eor': '001_Battle/011_Battle_EndOfRoundPhase.rb',
 'battler': '002_Battler/001_Battle_Battler.rb',
 'init': '002_Battler/002_Battler_Initialize.rb',
 'hp': '002_Battler/003_Battler_ChangeSelf.rb',
 'status': '002_Battler/004_Battler_Statuses.rb',
 'stages': '002_Battler/005_Battler_StatStages.rb',
 'abilityitem': '002_Battler/006_Battler_AbilityAndItem.rb',
 'use': '002_Battler/007_Battler_UseMove.rb',
 'target': '002_Battler/008_Battler_UseMoveTargeting.rb',
 'success': '002_Battler/009_Battler_UseMoveSuccessChecks.rb',
 'trigger': '002_Battler/010_Battler_UseMoveTriggerEffects.rb',
 'usage': '003_Move/002_Move_Usage.rb',
 'calc': '003_Move/003_Move_UsageCalculations.rb',
 'base': '003_Move/004_Move_BaseEffects.rb',
 'misc': '003_Move/005_MoveEffects_Misc.rb',
 'statmoves': '003_Move/006_MoveEffects_BattlerStats.rb',
 'other': '003_Move/007_MoveEffects_BattlerOther.rb',
 'attr': '003_Move/008_MoveEffects_MoveAttributes.rb',
 'multi': '003_Move/009_MoveEffects_MultiHit.rb',
 'heal': '003_Move/010_MoveEffects_Healing.rb',
 'change': '003_Move/012_MoveEffects_ChangeMoveEffect.rb',
 'acting': '003_Move/013_MoveEffects_SwitchingActing.rb',
 'effects': '007_Other battle code/001_PBEffects.rb',
 'field': '007_Other battle code/002_Battle_ActiveField.rb',
 'abilities': '007_Other battle code/008_Battle_AbilityEffects.rb',
 'items': '007_Other battle code/009_Battle_ItemEffects.rb',
 'aichoose': '005_AI/005_AI_ChooseMove.rb',
 'aibattler': '005_AI/010_AIBattler.rb',
 'aimove': '005_AI/011_AIMove.rb',
 'aimisc': '006_AI MoveEffects/001_AI_MoveEffects_Misc.rb',
 'aiattr': '006_AI MoveEffects/004_AI_MoveEffects_MoveAttributes.rb',
 'aichange': '006_AI MoveEffects/008_AI_MoveEffects_ChangeMoveEffect.rb',
 'aiacting': '006_AI MoveEffects/009_AI_MoveEffects_SwitchingActing.rb',
}
# Correct physical spelling is frozen here, independently of the conceptual key.
paths['run'] = '001_Battle/007_Battle_ActionRunning.rb'
paths = {k: 'Data/Scripts/011_Battle/' + v for k, v in paths.items()}

# These are actual read ranges, not an enumeration-to-reading promotion.
read_ranges = {
 'battle': [[448,450]], 'priority': 'FULL', 'switch': [[38,71],[316,374]],
 'run': [[5,22],[60,159]], 'attack': 'FULL', 'eor': [[5,49],[597,781]],
 'battler': [[1,50],[107,112],[309,324],[611,621]], 'init':'FULL',
 'hp': [[5,35],[54,99],[129,151],[189,228]], 'status': [[571,574]],
 'stages': [[26,45],[176,196],[376,386]], 'abilityitem': [[45,49],[384,388]],
 'use': 'FULL', 'target': 'FULL', 'success': [[183,595]],
 'trigger': [[5,82],[177,217]], 'usage': [[1,127],[184,227],[232,238],[369,404]],
 'calc': [[5,27],[283,484]], 'base': [[394,412],[436,491],[530,626]],
 'misc': [[169,187]], 'statmoves': [[93,111],[1650,1664],[1673,1687],[1696,1710],[1719,1734],[1745,1761],[1778,1789]],
 'other': [[240,244]], 'attr': [[349,362],[554,559],[576,601],[682,691],[852,972],[978,989],[994,996],[1002,1032],[1584,1620]],
 'multi': [[483,499]], 'heal': [[69,78]],
 'change': [[5,32],[360,526],[654,689],[1207,1226]], 'acting': [[406,419],[442,486]],
 'effects': 'FULL', 'field': 'FULL',
 'abilities': [[367,408],[829,870],[1691,1707],[2188,2195],[2291,2302]],
 'items': [[447,471],[634,671],[1669,1690]],
 'aichoose': [[91,127]], 'aibattler': [[317,326]], 'aimove': [[68,75]],
 'aimisc': [[517,531]], 'aiattr': [[233,246],[1043,1047],[1084,1088],[1129,1133]],
 'aichange': [[196,200],[240,244]], 'aiacting': [[406,410]]
}

common = {
 'source_commit': R, 'source_tree':'7589c800b61ba13a13040ed0d686979b80a84fd0',
 'formal_commit': B8, 'formal_tree':'f292698cdd4a8e725525a9be6dc34b75faaf151e',
 'actual_receiver': READER, 'evidence':'SOURCE_STATIC', 'business_execution':'NOT_EXECUTED',
 'scope': 'Only the three existing WP42 §5.3 reset rows: actual finite producers, state, reached consumers, qualified tail and next read. No all-Move/AI/ability/item/system approval.',
 'premise': 'Fixed R valid ordinary objects and identities; no plugin mutation or concurrent mutation. The actual call must reach the indicated write. Dynamic Protect @effect is resolved by the complete constructors and base definition, not by a missing literal assignment.',
 'battler_tail': 'pbEndOfRoundPhase reaches lines 710 onward after the three positive-decision returns and continual checks. allBattlers snapshots existing nonfainted battlers at this point; each is reset sequentially. A replacement is the then-current occupant. The two side resets and field resets follow separately.',
 'ordinary': 'Reached live-battler tail performs each specified write. Side 0 then side 1 and field are processed even though their flags are not properties of one surviving battler.',
 'refused_or_failed': 'Refusal before a producer write leaves that write unperformed. Earlier counters or flags already written by the reached prefix can remain; reset does not require the move to have succeeded.',
 'cancel': 'Command/UI cancellation before a move executes produces no move effect through these definitions. pbCancelMoves is a separate reached cleanup and does not clear this entire tail list. It must not be treated as an EOR-tail substitute.',
 'exception_partial_commit': 'The complete EOR and use/hit methods contain no rollback/ensure transaction for this list. If a callback/message/animation raises, writes before that point remain, later writes need not occur. No host continuation or recovery behavior is asserted.',
 'faint_boundary': 'allBattlers excludes HP <= 0. Formal pbFaint can already have called pbInitEffects(false), which clears these battler fields and replaces attacker arrays before EOR early return. Merely skipping a later tail does not undo those earlier resets.',
 'persistence': 'These are battler effects/history or battle side/field runtime fields. Tail reset is not HP/status/stage/item/party rollback, serialization, or reload. HP producer writes through to the party creature; the tail does not reverse it. Full save/reload remains outside this finite contract and NOT_EXECUTED.',
 'independence': 'New real receiver for this finite slice; original parent FULL_FILE_READ identities are retained only in selected original objects. No claim that the receiver read every source file completely; no finding counterproposal vote.'
}

# Each tuple is a hand-authored, complete producer -> current consumption -> next-read explanation.
# A source locator uses the path key above, then an inclusive range of a complete method/class.
data607 = [
 ('BanefulBunker','base:436-491; attr:864-869','Protect base writes the constructor-selected battler flag only after its failure gates; duplicate/last-in-round/rate refusal does not execute the setter.','success:303-530','Stops qualifying protectable moves and can poison a qualifying contact attacker; after false, this flag no longer supplies that protection.'),
 ('Electrify','attr:1584-1598','Target-specific effect sets true after duplicate/already-moved gates; no setter on a rejected target.','calc:13-27','Existing Electric type data is required; true overrides the calculated type. After false, base type and any other type modifiers decide.'),
 ('Endure','base:436-491; attr:682-691','Protect base resolves the Endure constructor effect and sets the battler flag on the reached general effect.','usage:184-227','A lethal hit uses this flag after nonlethal-move handling; after false, Endure itself supplies no HP-1 survival.'),
 ('Flinch','status:571-574; use:583-761','The shared flinch producer rejects active Inner Focus unless Mold Breaker; move/item/ability paths call it.','success:183-297','A reached ordinary action can be prevented and mark failure; false removes this flinch reason. Special skipped accuracy/status checks have their own gate.'),
 ('FocusPunch','misc:169-187; attack:106-184','Attack phase charge-message dispatch sets readiness before move execution; same class reads readiness and tookMoveDamageThisRound.','misc:169-187','Readiness false alone does not create a prior-charge damage failure; next attack phase may charge again.'),
 ('HelpingHand','change:431-447','Target must be nonfainted, not already helped, and still eligible to act; reached target effect sets true.','calc:283-484; aichange:240-244','Damage power multiplier reads true except Confusion; false removes this contribution and the duplicate-effect refusal.'),
 ('KingsShield','base:436-491; attr:875-880','Dynamic Protect base writes this resolved constructor flag.','success:303-530','Qualifying damaging protectable moves can be blocked and contact Attack loss requested; false removes this protection source.'),
 ('MagicBounce','success:303-530; use:361-578','Targeted or nontargeted eligible status reflection sets the used flag; the ability gate and old false value are both checked.','success:303-530; use:361-578','Used flag suppresses a second Magic Bounce use through that branch; false permits a later qualified reflection. Ability itself is not removed.'),
 ('MagicCoat','change:1207-1212','General effect sets true. A qualified reflection can consume it earlier by setting false.','success:303-530; use:361-578','Both targeted and nontargeted reflection branches read/consume it; false removes this temporary reflection source.'),
 ('Obstruct','base:436-491; attr:888-893','Dynamic Protect base writes the Obstruct flag after the shared gates.','success:303-530','Qualifying damaging contact moves can be blocked and Defense loss requested; false removes this source.'),
 ('Powder','change:360-376','Duplicate rejected; reached target effect sets true.','use:147-578; aichange:196-200','A Fire move reads Powder after usage counters/start-use. It marks failure and may damage the user; after false, Powder does not intercept the next Fire move.'),
 ('Prankster','priority:141-260; abilities:829-836','PriorityChange on a status move sets saved origin true; rough AI priority explicitly untriggers it after its own query.','success:303-530; aimove:68-75','The generation-7+ opposing Dark immunity reads this saved origin. Tail false is not removal of the ability; next priority calculation can set it again.'),
 ('PriorityAbility','priority:141-260; abilities:848-870','After computing bracket values, both saved flags are cleared, then nonzero selected ability subpriority sets this one.','attack:6-14','The attack message/use dispatcher reads the saved flag and current ability activity. Tail false does not clear the cached priority entry; a later calculation can rewrite it.'),
 ('PriorityItem','priority:141-260; items:634-671','Selected item subpriority sets this when ability has no bracket effect or the faster item overrides a slower ability.','attack:6-14','Message/use dispatch checks this in the elsif after ability source and current item activity; consumption can occur there. Tail false does not refund any item.'),
 ('Protect','base:436-491; attr:852-857','Constructor sets Protect identity; shared general effect sets it dynamically after failure gates.','success:303-530','Qualifying protectable moves are stopped; false removes the Protect source. ProtectRate is not reset by this C0607 tail row.'),
 ('RagePowder','change:5-15','Redirection general effect sets FollowMe order and sets RagePowder only when the move is powder-classified.','target:96-154; aichoose:91-127','Real targeting checks powder eligibility plus FollowMe order. Clearing both tail fields removes this redirection; AI finite scoring reads are kept distinct from execution.'),
 ('Roost','heal:69-78; base:394-412','Healing failure can reject full HP before the general effect. Reached parent recovery/message occurs before the Roost setter, so an error in that prefix can omit the flag.','battler:309-324; hp:129-151','Type queries temporarily omit Flying and add Normal if otherwise empty; false exposes then-current underlying types, not a saved-original-type restore. Other type setters can clear it earlier.'),
 ('SpikyShield','base:436-491; attr:899-904','Dynamic Protect base writes the resolved SpikyShield flag.','success:303-530','Qualifying moves are blocked, with qualifying contact recoil; false removes this protection source.'),
 ('Counter + CounterTarget','usage:369-404','A recorded non-Substitute physical hit stores damage and the user index, including the separate target pointer.','change:453-473','Pointer < 0 prevents adding a target; otherwise fixed damage uses the stored value. Tail -1 for both prevents an old hit target from being reused.'),
 ('MirrorCoat + MirrorCoatTarget','usage:369-404','A recorded non-Substitute special hit stores damage and its user index separately.','change:479-499','Pointer < 0 prevents adding a target. Tail -1 for both drops the old target/damage pair; no party HP is restored.'),
 ('FirstPledge','base:530-626; change:654-689','Setup general effect clears own token, then writes the waiting ally token and MoveNext; normal combo use reads token in base type/start-use and consumes it only in general effect.','base:530-626; use:147-761','All-target failure occurs before general consumption; after-all-hits still runs and may write combo side effects. Token can remain until live tail nil; next start-use then cannot form a combo from that stale token.'),
 ('FollowMe','change:5-15','Reached redirection setter chooses an ordering counter greater than current ally counters.','target:96-154; aichoose:91-127','Real single-foe redirection selects lower positive valid counter after Spotlight. Tail 0 removes this candidate; RagePowder is separately cleared.'),
 ('Snatch','change:1217-1226','General effect chooses a positive ordering counter above existing live battlers.','target:9-31','Eligible snatchable status use selects the lowest nonzero counter, consumes it to 0, changes user, target and Mold Breaker; tail 0 removes any unused candidate.'),
 ('Spotlight','change:21-32','Target effect sets an ordering counter greater than its current allies.','target:96-154; aichoose:91-127','Real redirection considers valid positive Spotlight before FollowMe/Rage Powder; tail 0 removes it. AI reads are a separate heuristic, not proof of identical execution.')
]
data609 = [
 ('lastHPLost','usage:369-404','Every reached damage-record operation stores this hit damage, with Substitute distinctions handled per field.','aimisc:517-531','AI Substitute score reads the raw last damage threshold; tail 0 removes that last-hit contribution for the next read.'),
 ('lastHPLostFromFoe','usage:369-404','Only when recorded user opposes target is this damage updated; ally damage does not overwrite it through this branch.','change:505-526','Metal Burst reads 1.5 times this amount after choosing the last foe attacker; tail 0 plus empty foe history prevents old damage reuse.'),
 ('droppedBelowHalfHP','hp:5-35; hp:54-62','Registered HP loss sets true only across the strict below-half boundary; recovery to half or more clears it. Effect-damage entry clears before/after its reached reactions.','abilityitem:45-49; abilities:367-408; abilities:2188-2195; trigger:177-217','Emergency Exit/Wimp Out entry and Berserk read it under their own gates. False skips the former field gate and Berserk half-cross check; no lost HP is refunded.'),
 ('statsDropped','stages:176-196; stages:376-386; statmoves:93-111,1650-1789','Positive actual basic stage loss, selected direct stage replacement/reversal and reset-from-positive paths set true. Several action/entry paths clear it earlier.','abilityitem:384-388; items:447-471; trigger:177-217; switch:316-374','Eject Pack entry requires true and active item; clearing prevents stale event reuse. This is separate from statsLoweredThisRound and does not restore stages or consumed item.'),
 ('tookMoveDamageThisRound','hp:5-21; usage:369-404','Registered positive HP loss sets true; damage recording separately sets it for positive non-Substitute damage. The field name does not prove every producer was direct move damage.','misc:169-187','Focus Punch readiness plus this flag can fail. Tail false permits next-round focus unless fresh damage sets it again; HP remains changed.'),
 ('tookDamageThisRound','hp:5-21; usage:369-404','Registered positive HP loss and positive recorded hit damage set true; record may include Substitute damage for this field.','attr:586-591','Assurance reads this marker for doubled base power. Tail false removes the previous-round contribution, not damage itself.'),
 ('tookPhysicalHit','trigger:5-82','The Shell Trap reaction sets true only for an opposing physical hit, actual positive non-Substitute HP loss, and a selected still-unmoved trap action; also requests MoveNext.','acting:442-464','Shell Trap use-message/failure reads this flag. Tail false removes a prior-round trigger; ShellTrap effect has a separate action-end reset.'),
 ('statsRaisedThisRound','stages:26-45; stages:376-386; statmoves:93-111,1650-1789; abilities:1691-1707; items:1669-1690','Positive basic stage gain, direct comparisons/swaps/reversal, Anger Point and White Herb reached writes can set this history flag.','other:240-244','Burning Jealousy additional effect delegates burn only if this marker is true. Tail false removes that previous-round condition; raised stages remain.'),
 ('statsLoweredThisRound','stages:176-196; stages:376-386; statmoves:93-111,1650-1789','Actual basic loss and direct comparison/reset/reversal paths mark lowering; same paths may separately mark statsDropped.','attr:596-601','Lash Out doubles when this history is true. Tail false removes previous-round doubling while actual stages are retained.'),
 ('canRestoreIceFace','hp:189-228','Weather-change form check marks eligible nontransformed, living Eiscue form 1 with raw Ice Face when effective weather is Hail and this is not an ability-change call.','eor:5-49; abilities:2291-2302','EOR weather dispatch plus active ability/effective Hail reads this token and form; tail false removes stale restoration permission. No generic reset of form is inferred.'),
 ('lastRoundMoveFailed <- lastMoveFailed','use:147-578; success:183-297; attack:16-90; base:530-626','Use entry resets current failure; reached denial/failure paths can set true, while Call/SwitchOut/UseItem set false and Pledge setup sets true. Not all failed hits set the same value (protected-only target loop is special).','attr:554-559','Tail copies current failure to prior-round failure without clearing current. Stomping Tantrum reads the copied value next round, not an arbitrary success/failed label inferred from animation.'),
 ('lastAttacker','usage:369-404','Reached record appends user index (not restricted to opposing users); the array is initialized independently.','attr:576-581','Revenge/Avalanche membership reads target index. Tail clears this same array in place; an existing alias sees empty history.'),
 ('lastFoeAttacker','usage:369-404','Reached record appends only opposing user indices to a separate array.','change:505-526','Metal Burst selects the last recorded opposing index. Tail clears the same array in place, so no old target is selected.')
]
data610 = [
 ('side.CraftyShield','attr:930-944','Rejects already-active side flag and last-in-round; reached general effect sets own side true.','success:303-530; aiattr:1043-1047','Status protection check reads true under its target gates; tail false permits a later valid new use and removes old side protection.'),
 ('side.MatBlock','attr:909-925','First-turn and last-in-round checks precede the general side setter.','success:303-530','Qualifying damaging moves read the side flag; tail false removes this source. First-turn qualification itself is not reset.'),
 ('side.QuickGuard','base:436-491; attr:950-958','Constructor resolves sidedEffect and QuickGuard; base reads/writes side effects dynamically.','success:303-530; aiattr:1084-1088','Reads saved positive move priority with protectability and bypass gates; false removes old guard but does not change move priority.'),
 ('side.WideGuard','base:436-491; attr:964-972','Constructor selects WideGuard side effect; shared failure/general methods implement the actual setter.','success:303-530; aiattr:1129-1133','Reads multi-target/other gates and generation rules. Tail false removes old guard; unrelated field state is retained.'),
 ('side.Round','acting:470-486; use:583-761','Successful entry to hit body reaches general setter and may advance a compatible unmoved ally. All-target failure before general leaves a starting false Round false.','acting:470-486','Base damage reads existing side flag before this use sets it; tail false means first next-round Round has no stale doubling. MoveNext is not one of these side resets.'),
 ('side.EchoedVoiceUsed / EchoedVoiceCounter','attr:349-362; use:147-578','Usage-counter override increments once per side-round (capped 5), then sets Used true, before subsequent target/failure/hit checks. Failures before usage-counter entry differ.','attr:349-362; aiattr:233-246','Tail tests old Used first: false => Counter 0; true => retain Counter. It then clears Used. Next use increments retained count; next unused tail resets count. Do not clear Used before testing it.'),
 ('field.IonDeluge','attr:1604-1620','Nondamaging use rejects already active/last-in-round; damaging variant bypasses that failure branch. Reached general setter is idempotent when already true.','calc:13-27','With Electric type data present, true changes Normal calculated move type; tail false removes this field contribution. Electrify is separate.'),
 ('field.FusionBolt','change:381-426; usage:12-18','Fusion Bolt caches the opposite flag before shared usage-counter reset clears BOTH field flags, then its reached general effect sets Bolt true. Other moves also clear both on counter entry.','change:406-426','Fusion Flare caches Bolt before clearing. An all-target failed Bolt has already cleared both but never reaches its general true setter. EOR false prevents carrying a successful Bolt token across the tail.'),
 ('field.FusionFlare','change:381-426; usage:12-18','Fusion Flare symmetrically caches Bolt before parent clears both; reached general sets Flare true. This is a per-use sequence as well as EOR lifetime.','change:381-401','Fusion Bolt multiplier/animation uses its cached opposite flag. Tail false removes only the shared field token, not a move object cache already computed for a use.'),
 ('field.FairyLock','acting:406-419','Duplicate positive lock rejected; reached general sets 2.','battler:611-621; switch:38-71; run:5-22,60-159; aiacting:406-410','Positive field value participates in trappedInBattle. Certain switching/escape and Ghost bypasses precede it; duringBattle run bypasses that trapping block. Tail decrements only positive: 2->1, next reached tail 1->0; zero/negative unchanged.')
]

original = json.loads((OUT/'selected-manual-atomic-clauses.json').read_text())
orig = {r['id']:r for r in original['rows']}
rows=[]
for locator, dataset in [('CORE-C0607',data607),('CORE-C0609',data609),('CORE-C0610',data610)]:
    for n,(field,producer_units,producer,consumer_units,consumer) in enumerate(dataset,1):
        atom=f'CAR-C{locator[-4:]}-{n:02d}'
        old=orig[atom]
        reset = old['assertion']
        rows.append({'id':atom,'old_locator':locator,'formal':old['spec'], 'field':field,
                     'original_assertion':reset,'original_reader':original['reader'],
                     'actual_receiver':READER,'producer_units':producer_units,'producer':producer,
                     'consumer_units':consumer_units,'consumption_and_next_read':consumer,
                     'reset_unit':'eor:710-778','reset':reset,'common_contract':'common',
                     'status':'RECEIVED_BOUNDED_RESET_CHAIN','premise_checked':True,
                     'blocking_open':[], 'parent_reception':'PENDING_PARENT_RECEPTION',
                     'evidence':'SOURCE_STATIC','business_execution':'NOT_EXECUTED'})

save('manual-atomic-clauses.json',{'schema':'round-reset-finite-atoms/v1','updated_utc':NOW,
    'reader':READER,'frozen_original_atom_count':47,'new_atom_count':0,'old_locator_count':3,
    'global_atomic_denominator':'NOT_FROZEN_BY_THIS_RECEIVER','common':common,'rows':rows})
save('sourcefact-consumer-receptions.json',{'schema':'round-reset-chain-receptions/v1',
    'updated_utc':NOW,'source_path_keys':paths,'common':common,'rows':rows,
    'counts':{'existing_atoms':47,'bounded_received':47,'blocking_open':0,'new_findings':0,'votes':0},
    'qualification':'Actual source methods/classes and finite direct AI readers listed. This is a semantic reception of reset meaning only; no inherited source FULL, no full family correctness or global closure.'})

units=[]
identities=[]
for key,path in paths.items():
    payload=(REFERENCE/path).read_bytes()
    frozen=subprocess.check_output(['git','-C',str(REFERENCE),'show',R+':'+path])
    assert payload==frozen, path
    identity={'key':key,'repo':str(REFERENCE),'commit':R,'tree':common['source_tree'],
              'path':path,'bytes':len(payload),'sha256':hashlib.sha256(payload).hexdigest(),
              'git_blob':git(REFERENCE,'rev-parse',R+':'+path),'working_bytes_equal_frozen':True}
    identities.append(identity)
    ranges=read_ranges[key]
    if ranges=='FULL': ranges=[[1,len(payload.splitlines())]]
    units.append({'source_key':key,'path':path,'actual_reader':READER,'ranges':ranges,
                  'qualification':'FULL_FILE_READ' if read_ranges[key]=='FULL' else 'COMPLETE_NAMED_METHODS_CLASSES_OR_REGISTRATIONS_ONLY',
                  'unread_file_remainder':'Not claimed as read or approved; outside these precise reset joins.' if read_ranges[key]!='FULL' else 'none',
                  'identity_key':key,'evidence_logs':'source-*.io.json; exact raw stdout contains path/range or argv range',
                  'business_execution':'NOT_EXECUTED'})

formal_path='deliverables/final-specification-set/combat-requirements/wp42-growth-end-of-round-and-battle-outcomes.md'
formal=(PROJECT/formal_path).read_bytes()
frozen=subprocess.check_output(['git','-C',str(PROJECT),'show',B8+':'+formal_path])
assert formal==frozen
identities.append({'key':'formal-wp42','repo':str(PROJECT),'commit':B8,'tree':common['formal_tree'],
    'path':formal_path,'bytes':len(formal),'sha256':hashlib.sha256(formal).hexdigest(),
    'git_blob':git(PROJECT,'rev-parse',B8+':'+formal_path),'working_bytes_equal_frozen':True})

for name in ['manual-atomic-clauses.json','old-locator-disposition.json']:
    parent=TASK/name
    current=json.loads(parent.read_text())
    selected=json.loads((OUT/('selected-'+name)).read_text())
    selected_keys={r.get('old_locator',r['id']) for r in selected['rows']}
    actual=[r for r in current['rows'] if r.get('old_locator',r['id']) in selected_keys]
    payload=parent.read_bytes()
    identities.append({'key':'parent-'+name,'repo':str(PROJECT),'path':str(parent.relative_to(PROJECT)),
        'purpose':'Selected original objects and common fields only; parent mutable task file, not B8 formal',
        'captured_identity_utc':NOW,'bytes':len(payload),'sha256':hashlib.sha256(payload).hexdigest(),
        'selected_snapshot_path':'selected-'+name,'selected_rows_equal_current_at_identity_capture':actual==selected['rows'],
        'git_blob':'WORKTREE_MUTABLE_NOT_FROZEN_COMMIT','reading':'FULL_SELECTED_OBJECTS_AND_COMMON_ONLY'})
save('input-identities.json',{'schema':'round-reset-input-identities/v1','captured_utc':NOW,
    'source_head':git(REFERENCE,'rev-parse','HEAD'),'source_head_tree':git(REFERENCE,'rev-parse','HEAD^{tree}'),
    'B8':B8,'formal_tree':common['formal_tree'],'identities':identities,
    'protection':'Only this subreview directory written. R/formal/canonical/other task paths read only. No commit/push/install/spawn or reference execution.'})
save('reading-ledger.json',{'schema':'round-reset-reading-ledger/v1','reader':READER,'updated_utc':NOW,
    'contracts':[
      {'path':'AGENTS.md','reading':'FULL_READ'},
      {'path':'inputs/review-SKILL.md','reading':'FULL_READ','scope':'Explicitly excludes audit reports; no formal revision performed.'},
      {'path':'inputs/eighth-global-review-prompt.md','reading':'FULL_READ_IN_1_140_AND_141_END_BLOCKS'},
      {'path':'tasks/coverage_acceptance_incremental/dispatch/core_atomic_reception.md','reading':'FULL_READ'},
    ],'selected_objects':{'atoms':47,'old_dispositions':3,
       'reading':'Every selected original object field read. Repeated identical fields shown once as lossless common plus each residual row; original complete snapshots preserved.',
       'initial_truncation':'An oversized first display and combined output were truncated. They grant no missing-read credit. Lossless per-locator common/residual outputs repaired the selected-object reads.',
       'logs':['selected-c0607-complete-lossless.io.json','selected-c0609-complete-lossless.io.json','selected-c0610-complete-lossless.io.json','selected-old-disposition.io.json']},
    'formal':{'path':formal_path,'reading':'FULL_READ','logs':['formal-wp42-1-140.io.json','formal-wp42-141-end.io.json'],
       'review_scope':'Only lines149/151/152 and necessary common §5.1/5.3/§8 premise; full reading is not whole-document acceptance.'},
    'source_units':units,'original_source_reader_preservation':'Selected original source_units keep /root/core_atomic_reception as their full-file reader. This receiver has only the precise ranges above.',
    'semantic_credit_not_granted_for':['rg hits alone','helper success','file/hash equality','method enumeration','truncated output','other reader FULL label']})

old=json.loads((OUT/'selected-old-locator-disposition.json').read_text())
save('old-locator-disposition.json',{'schema':'round-reset-old-locator-reception/v1','reader':READER,'rows':[
 {'id':r['id'],'original_snapshot':'selected-old-locator-disposition.json#/rows/'+str(i),
  'formal_text_read':r['formal_text_read'],'existing_atom_ids':r['manual_atom_ids'],
  'decomposition':'PRESERVED_24_13_10_EXISTING_SEMANTIC_CHILDREN; NO_NEW_ATOM',
  'all_reset_children_locally_received':True,'reset_chain_support':'SUPPORTED_SOURCE_STATIC_WITH_EXPLICIT_REACHED_PREFIX',
  'blocking_open':[],'parent_canonical_status':'UNCHANGED_PENDING_PARENT_RECEPTION',
  'excluded_claims':['All move family effects approved','all AI heuristics equal live execution','full EOR callback domain approved','runtime equivalence','serialization/reload proof']}
 for i,r in enumerate(old['rows'])]})

vectors=[
 {'id':'RRPT-V01','case':'ordinary reached tail','input':'One existing live battler with the listed true flags, positive counters/history, current failure true; both sides with guard/Round/Echo state; FairyLock2.',
  'expected':'Live listed flags false, Counter/Mirror pairs -1, FirstPledge nil, redirection/snatch counters0; damage numbers0; history flags false; prior failure true while current true; both attacker arrays same identity but empty. Side guard/Round false, Echo rule depends on old Used. Ion/Fusion false and FairyLock1. HP/stages/items not restored.'},
 {'id':'RRPT-V02','case':'explicit early EOR return','input':'Decision positive at any one of the three checks before tail, no earlier reset/reinitialization of the selected field.',
  'expected':'That invocation does not execute these tail writes. Existing earlier HP/messages/reset prefixes remain. Formal faint reinitialization, if actually reached before the return, remains a separate earlier clear.'},
 {'id':'RRPT-V03','case':'refused producer','input':'Protect family rejected by repeated effect/last-action/rate gate; Roost at full HP; Electrify target already moved.',
  'expected':'The rejected general/target setter is not reached. ProtectRate or earlier counters/messages can already have changed according to prefix; no inferred global rollback.'},
 {'id':'RRPT-V04','case':'Echo all-target failure after counters','input':'Own side Counter0/Usedfalse; valid Echo use reaches usage counters, then every target is unaffected/missed.',
  'expected':'Counter1/Usedtrue before target failure; ordinary tail retains Counter1 and sets Usedfalse; next reached same-side Echo counter entry gives2. A following round without Echo ends Counter0. Failure before counter entry does not write Used.'},
 {'id':'RRPT-V05','case':'Round first success versus allfail','input':'Side Roundfalse, valid selected Round. Compare one first-hit body reaches general with all-target failure before it.',
  'expected':'Success sets Roundtrue and can advance matching ally; allfail prefix does not newly set it. Tail false removes earlier Round token before next round. Existing true from a prior successful same-round use remains until another actual reset.'},
 {'id':'RRPT-V06','case':'Fusion cached token and allfail','input':'Field Flaretrue, Boltfalse; next Fusion Bolt reaches counters. Compare normal first-hit body with every target failing.',
  'expected':'Both cache prior Flaretrue then clear both shared flags in parent counters. Normal general sets Bolttrue; allfail skips that setter, leaves both false. Tail clears both. Cached per-use power/animation state is distinct from shared token.'},
 {'id':'RRPT-V07','case':'Pledge normal combo versus allfail','input':'Waiting live ally has matching FirstPledge token. Next Pledge start-use confirms combo; compare successful hit body with all targets rejected.',
  'expected':'Normal general clears own token; allfail returns before general so token can remain. After-all-hits still runs per listed target and its combo callback may set side combination effect. Later reached live tail clears token nil in either case. Do not infer allfail had no side effects.'},
 {'id':'RRPT-V08','case':'damage/history and persistent HP','input':'A recorded opposing hit with positive damage; then reached live tail.',
  'expected':'Damage/attacker fields record the hit under their specific Substitute/category/opposition gates. Tail zeros damage history and clears attacker arrays in place. Actual HP write to creature remains; no healing occurs.'},
 {'id':'RRPT-V09','case':'copy rather than clear failure','input':'Current lastMoveFailed true at tail; prior failure false.',
  'expected':'Prior failure becomes true; current remains true. Next Stomping Tantrum base-damage reader sees prior true. A new use can reset current without rewriting prior until tail.'},
 {'id':'RRPT-V10','case':'FairyLock boundary','input':'Reached field tail values2,1,0,-1 separately.',
  'expected':'Results1,0,0,-1. Positive trapping remains subject to the caller bypass ordering; duringBattle run does not use the ordinary trapping block.'},
 {'id':'RRPT-V11','case':'cancellation','input':'Move selection cancelled before action execution, or pbCancelMoves reached after first-hit all-target failure.',
  'expected':'Selection cancellation does not execute move-specific setters. pbCancelMoves does not run the whole EOR list; already written Echo/Fusion counter prefix remains until a relevant later actual clear.'},
 {'id':'RRPT-V12','case':'exception prefix','input':'A producer flag/counter is written, then its message/animation/callback raises, or EOR raises between two listed sequential tail writes.',
  'expected':'No rollback in these full methods: completed writes remain and later writes are not guaranteed. External diagnostic handling/continuation and real host recovery remain unobserved.'}
]
for v in vectors: v.update({'evidence':'DERIVED_VECTOR_FROM_SOURCE_STATIC','execution':'NOT_EXECUTED','observed_output':None})
save('vectors.json',{'schema':'round-reset-derived-vectors/v1','vectors':vectors,'reference_processes':0,'model_processes':0})

save('interfaces.json',{'schema':'round-reset-interfaces/v1','common':common,
 'interfaces':[
  {'id':'RRPT-I01','join':'Actual move/counter/HP/stat producer -> runtime battler/side/field state','reception':'RECEIVED_FINITE_DEFINITIONS','rows':'all47'},
  {'id':'RRPT-I02','join':'Shared Protect constructor identity -> dynamic @effect writer -> target protection','reception':'RECEIVED','rows':['CAR-C0607-01','CAR-C0607-03','CAR-C0607-07','CAR-C0607-10','CAR-C0607-15','CAR-C0607-18','CAR-C0610-03','CAR-C0610-04']},
  {'id':'RRPT-I03','join':'usage counters -> move failure/target checks -> first-hit body -> general -> after-all-hits','reception':'RECEIVED','nuance':'Echo writes before later failure; Round/Fusion/Pledge general writes require reached hit body; Pledge after-all-hits does not share that gate.'},
  {'id':'RRPT-I04','join':'three EOR decision exits -> current-live allBattlers tail -> both sides -> field -> normal return','reception':'RECEIVED','nuance':'Not a finally block; faint/init reset is earlier independent behavior.'},
  {'id':'RRPT-I05','join':'tail values -> subsequent live move/type/guard/retaliation/ability/item readers and finite AI direct readers','reception':'RECEIVED_FINITE_DIRECT_READERS','nuance':'AI heuristics and live execution remain distinct; no all-AI approval.'},
  {'id':'RRPT-I06','join':'runtime reset -> party creature/save/reload','reception':'NO_RESET_TO_PARTY_ROLLBACK_JOIN_IN_THIS_TAIL','open':'Full serialization/reload not established; outside this reset contract and NOT_EXECUTED.'}
 ]})
save('coverage-gaps.json',{'schema':'round-reset-coverage-gaps/v1','finite_slice':{'old_locators':3,'existing_atoms':47,'locally_received':47,'new_atoms':0,'blocking_open':[]},
 'open_boundaries':[
  {'id':'RRPT-OPEN-RUNTIME','status':'NOT_EXECUTED','scope':'Actual R gameplay, exceptional callbacks, UI cancellation, native/Ruby host and save/reload','blocking_for_static_reset_reception':False,'recovery':'Separate authorized controlled runtime observation; do not relabel static derived vectors as observations.'},
  {'id':'RRPT-OPEN-PARENT','status':'PENDING_PARENT_RECEPTION','scope':'Integration of exactly these47 existing atoms/3 old rows into parent canonical files','blocking_for_parent_closure':True,'recovery':'Parent reads this complete finite contribution and binds exact identities; this receiver never edits canonical state.'},
  {'id':'RRPT-EXCLUDED-GLOBAL','status':'OUTSIDE_FINITE_SCOPE','scope':'All remaining methods in the source files, whole Move/AI/ability/item families, every EOR callback and system gates','blocking_for_static_reset_reception':False,'recovery':'Continue their own named domain tasks; no added global gate is imposed on the three reset rows.'}
 ],'new_findings':[],'finding_votes':[]})
save('next-dispatch.json',{'schema':'round-reset-next-dispatch/v1','state':'FINITE_SLICE_READY_FOR_PARENT_RECEPTION','new_source_reader_required_for_these47_reset_joins':False,
 'parent_action':'Read review.md, manual-atomic-clauses.json common+47rows, sourcefact-consumer-receptions.json, identities and precise source read ledger. Receive only qualified reset joins. Preserve original readers, EOR reach gates, after-all-hits nuance, NOT_EXECUTED and external open boundaries. Canonical edits remain parent responsibility.',
 'no_new_findings_no_vote':True,'no_reopen_of_completed4506':True,'update_started':False})
save('progress.json',{'schema':'round-reset-progress/v1','task':READER,'parent':'/root/core_atomic_reception','updated_utc':NOW,
 'status':'COMPLETED_FINITE_SLICE_PENDING_PARENT_RECEPTION','logical_platform_entry':READER,
 'requested_configuration':{'model':'gpt-6.1-sol','reasoning_effort':'ultra','service_tier':'default','speed':'normal','fast':False},
 'actual_configuration':{k:'UNVERIFIED' for k in ['model','reasoning_effort','service_tier','speed','fast']},
 'configuration_note':'No authoritative configuration echo; no authentication/quota inspection was attempted.',
 'counts':{'old_locators':3,'existing_atoms':47,'new_atoms':0,'bounded_locally_received':47,'findings':0,'votes':0,'reference_behavior_processes':0,'independent_model_processes':0},
 'execution':'NOT_EXECUTED','update_state':'UPDATE_NOT_STARTED','write_scope':str(OUT),'parent_canonical_files_modified':False,
 'log_query':'Read *.io.json in this directory. Each has actual argv/cwd/start/end UTC/stdout/stderr/underlying exit. Platform transcript contains initial bootstrap calls; capture-contracts.io.json preserves full re-captured contract bytes.'})

io=[]
for file in sorted(OUT.glob('*.io.json')):
    rec=json.loads(file.read_text())
    io.append({'path':file.name,'label':rec['label'],'argv':rec['argv'],'started_utc':rec['started_utc'],'ended_utc':rec['ended_utc'],'exit_code':rec['exit_code'],
               'stdout_bytes':len(rec['stdout'].encode()),'stderr_bytes':len(rec['stderr'].encode()),
               'qualification':rec['qualification']})
save('execution-ledger.json',{'schema':'round-reset-execution-ledger/v1','updated_utc':NOW,'entries':io,
    'reference_behavior_processes':0,'model_behavior_processes':0,'business_execution':'NOT_EXECUTED','update_started':False,
    'retained_tool_failures':[
      {'log':'source-attr-classes.io.json','reason':'Requested range extended beyond physical EOF after all intended Electrify/IonDeluge class lines were printed; actual Python IndexError/exit1 retained. Exact1584-1620 subsequently re-read in source-registration-completions.io.json.'},
      {'log':'source-types-flinch-sets.io.json','reason':'Requested statuses579 exceeded EOF575; actual exit1 retained. Later sources had not executed and were re-read in source-required-misc.io.json.'},
      {'log':'source-ai-direct-reads.io.json','reason':'Zero stdout due to wrong handler registration regex; no absence/read credit granted. Corrected full selected registrations in source-ai-direct-reads-corrected.io.json.'}
    ],'bootstrap':'Initial AGENTS/skill/prompt/dispatch/identity and selected extraction command outputs are in platform transcript; full contract re-capture is local. No missing bootstrap output was fabricated.'})

print(json.dumps({'written_utc':NOW,'rows':len(rows),'source_payloads':len(paths),'source_file_identity_match':True,'formal_identity_match':True,'business_execution':'NOT_EXECUTED','update_state':'UPDATE_NOT_STARTED'},ensure_ascii=False))
