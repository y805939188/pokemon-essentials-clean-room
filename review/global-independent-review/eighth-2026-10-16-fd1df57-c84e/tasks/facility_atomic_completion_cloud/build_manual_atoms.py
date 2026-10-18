# Historical manual authoring transcript only. Frozen JSON includes subsequent explicit corrections; do not rerun over the final evidence.
"""Serialize manually authored semantic assertions; this does not infer assertions."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
ledger = json.loads((ROOT / 'reading-ledger.json').read_text())
identities = {x['id']: x for x in ledger['original_inputs']}
identities.update({x['id']: x for x in ledger['supplemental']})
atoms = []

def add(source, unit, formal, assertion, premise='Fixed R/B8, no later override; accessed dependencies return normally to this observation point.', joins=()):
    sid = 'FAC-A%04d' % (len(atoms) + 1)
    atoms.append({'id': sid, 'source': source, 'unit_locator': unit, 'assertion': assertion,
                  'formal_receivers': formal, 'premise': premise,
                  'pending_dependencies': list(joins),
                  'status': 'BOUNDED_SOURCE_AND_FORMAL_RECONCILED' if not joins else 'LOCAL_FACT_WITH_NAMED_JOIN_OPEN',
                  'evidence': 'SOURCE_STATIC', 'execution': 'NOT_EXECUTED',
                  'reader': '/root/facility_atomic_completion_cloud'})

def group(source, unit, formal, assertions, **kw):
    for assertion in assertions:
        add(source, unit, formal, assertion, **kw)

F55 = ['F03 §2.1']
group('R07', 'BattleChallenge.initialize/set/register', F55, [
 'A newly created challenge has current identity -1.',
 'Setting a challenge stores the supplied identity.',
 'Setting a challenge stores the supplied number of rounds.',
 'Setting a challenge stores the supplied rules reference.',
 'The substring double supplies the immediate double-battle registration argument.',
 'A factory prefix selects the immediate Factory registration branch.',
 'An open suffix selects immediate mode 1; other identities select mode 0.',
 'Setting a challenge requests the debug-gated cup-writing tool after registration.',
 'A missing type record is created lazily for its identity.',
 'Registration does not populate the type record layout reader.',
 'Registration does not populate the type record team-size reader.',
 'Registration does not populate the type record battle-type reader.',
 'Registration does not populate the type record mode reader.',
 'Factory registration installs extra rental/session data.',
 'Factory registration changes the immediate rule-generation count to 3.',
 'Factory registration changes the immediate rule-generation battle type to Tower.',
 'Registration retains an already nonempty rules reference.',
 'The debug writer returns without a prompt when debug mode is false.'
])
group('R07', 'BattleChallenge.modeToRules', ['F03 §2.1','F02 §2'], [
 'Palace type selects the Palace battle producer.',
 'Arena type selects the Arena battle producer.',
 'Arena mode generation forces the single-battle argument.',
 'Other types select the Tower battle producer.',
 'Mode 1 gives the Standard member maximum equal to configured maximum level.',
 'Mode 1 installs enemy-only open adjustment with lower parameter 30.',
 'Mode 2 gives the Standard member maximum equal to configured maximum level.',
 'Mode 2 installs enemy-only open adjustment with lower parameter 60.',
 'Other modes give the Standard member maximum 50.',
 'Other modes install enemy-only open adjustment with lower parameter 50.',
 'Generated mode rules append the selected single/double layout rule.'
])
group('R07', 'BattleChallenge.start; BattleChallengeData.pbStart', ['F03 §2.2','F03 §2.3','F03 §4','F07 WS-W09/W10'], [
 'The outer current identity is assigned before the inner start call.',
 'Start writes inProgress true before validating round count.',
 'Start writes resting false before validating round count.',
 'Start writes decision 0 before validating round count.',
 'Start copies the type current swap count before validating round count.',
 'Start copies the type current win count before validating round count.',
 'Start writes battleNumber 1 before validating round count.',
 'Start clears the selected trainer list before validating round count.',
 'A nonpositive round count raises before writing numRounds.',
 'A positive round count is stored as numRounds.',
 'The next trainer draw uses wins plus the number already selected.',
 'An already selected trainer index is rejected without appending it.',
 'Trainer selection repeats until the requested list length is reached.',
 'Trainer selection has no iteration bound.',
 'The start-location snapshot is written after trainer-list completion.',
 'The old party snapshot retains the current party reference.',
 'A truthy selected-party reference replaces the active party at start.',
 'An empty selected list is truthy for the start replacement.',
 'The safe-save request follows active-party replacement.',
 'Start issues the save request while decision remains 0.'
])
group('R07', 'BattleChallengeData.setParty; BattleChallenge.data', ['F03 §2.2','F03 §2.3','F07 WS-W12/W32/W35'], [
 'Active-session party submission immediately replaces the active player party.',
 'Party submission updates the selected-party reference.',
 'Inactive-session party submission leaves the active player party unchanged.',
 'The data query returns nil before identity comparison when the session is inactive.',
 'For an active string identity, comparison against numeric zero precedes record cloning.',
 'The active string-versus-zero comparison has no locally handled failure.'
])
group('R08', 'pbEntryScreen', ['F03 §2.3','F01 §2.3','F07 WS-W28/W29/W35'], [
 'A nil selection result does not call party submission.',
 'A nil selection result leaves a previously selected party reference intact.',
 'An empty list selection result calls party submission.',
 'An empty list selection result makes the wrapper return boolean false.',
 'A nonempty list selection result makes the wrapper return boolean true.',
 'A nil selection result makes the wrapper return nil rather than boolean false.'
], premise='Direct wrapper/tool or replacement UI supplies the stated result; default multi-entry UI cannot confirm an empty list because of its lower bound.')
group('R07', 'BattleChallengeData.pbAddWin/pbAddSwap/pbMatchOver?', ['F03 §2.2','F07 WS-W18/W23/W26/W27'], [
 'Inactive-session add-win leaves the battle number unchanged.',
 'Inactive-session add-win leaves the win count unchanged.',
 'Active-session add-win increases battle number by one.',
 'Active-session add-win increases win count by one.',
 'Add-swap increases swaps only during an active session.',
 'Match-over is true when the session is inactive.',
 'Match-over is true when decision is nonzero.',
 'Match-over is true when battleNumber exceeds numRounds.',
 'The in-challenge query exposes inProgress even while resting.',
 'nextTrainer reads selected trainer position battleNumber minus one.'
])
group('R07', 'BattleChallengeData.pbRest/pbGoOn/pbSaveInProgress', ['F03 §2.4','F03 §4','F07 WS-W17/W33/W34'], [
 'Inactive-session rest returns without setting resting.',
 'Active-session rest writes resting true.',
 'Inactive-session continue returns without clearing resting.',
 'Active-session continue writes resting false.',
 'Rest requests a safe save through the start-location helper.',
 'Continue requests a safe save through the start-location helper.',
 'The helper snapshots the live map identity before temporary replacement.',
 'The helper snapshots live x before temporary replacement.',
 'The helper snapshots live y before temporary replacement.',
 'The helper snapshots live facing before temporary replacement.',
 'The helper temporarily writes the start map identity.',
 'The helper temporarily writes the start position.',
 'The helper temporarily sets facing up.',
 'A normally returned save restores the snapshotted map identity.',
 'A normally returned save restores the snapshotted position.',
 'A normally returned save restores the snapshotted facing.',
 'A boolean false save return still reaches the helper restoration statements.',
 'An uncaught save exception skips the subsequent helper restoration statements.'
])
group('R07', 'BattleChallengeData.pbCancel/reset', ['F03 §2.3','F07 WS-W13/W36'], [
 'Cancel restores the old party reference when that reference exists.',
 'Cancel leaves the active party unchanged when no old-party reference exists.',
 'Cancel does not issue a save request.',
 'Cancel does not request map refresh.',
 'Cancel retains the outer current challenge identity.',
 'Cancel retains registered outer rules.',
 'Cancel retains the inner numRounds value.',
 'Cancel does not update any type win/swap record.'
])
for field, value in [('inProgress','false'),('resting','false'),('start','nil'),('decision','0'),('wins','0'),('swaps','0'),('battleNumber','0'),('trainers','empty list'),('oldParty','nil'),('party','nil'),('extraData','nil')]:
    add('R07','BattleChallengeData.reset',['F03 §2.3'],f'Reset sets {field} to {value}.')
group('R07', 'BattleChallenge.pbEnd; BattleChallengeData.pbEnd', ['F03 §2.3','F03 §2.4','F07 WS-W14/W15/W16/W30/W36'], [
 'Outer end saves the active type counters before clearing currentChallenge.',
 'Outer end clears currentChallenge to -1 before invoking inner end.',
 'Inner end unconditionally writes the old-party value to the active party.',
 'Inner end checks inProgress after the unconditional party write.',
 'Inactive inner end returns before reset.',
 'Inactive inner end returns before requesting map refresh.',
 'Inactive inner end returns before requesting save.',
 'Active inner end snapshots whether decision is nonzero before reset.',
 'Active inner end resets the immediate session data.',
 'Active inner end requests map refresh after reset.',
 'Active inner end requests save only for the snapshotted nonzero decision.',
 'Cancel followed by outer end can recover counters under the retained outer identity.',
 'Cancel followed by inner end can write nil to the active party.'
])
group('R07', 'BattleChallengeType.initialize/saveWins', ['F03 §2.2','F03 §2.3','F07 WS-W14/W15/W16/W36'], [
 'A new type currentWins is zero.', 'A new type previousWins is zero.', 'A new type maxWins is zero.',
 'A new type currentSwaps is zero.', 'A new type previousSwaps is zero.', 'A new type maxSwaps is zero.',
 'Undecided end resets currentWins to zero.', 'Undecided end resets currentSwaps to zero.',
 'Undecided end retains previousWins.', 'Undecided end retains previousSwaps.',
 'Undecided end retains maxWins.', 'Undecided end retains maxSwaps.',
 'Winning end writes currentWins from session wins.', 'Winning end writes currentSwaps from session swaps.',
 'Other nonzero decisions reset currentWins to zero.', 'Other nonzero decisions reset currentSwaps to zero.',
 'A decided end updates maxWins to the greater of old maximum and session wins.',
 'A decided end updates maxSwaps to the greater of old maximum and session swaps.',
 'A decided end writes previousWins from session wins.',
 'A decided end writes previousSwaps from session swaps.'
])
group('R08', 'pbGetBTTrainers/pbGetBTPokemon', ['F03 §2.5'], [
 'A load exception is locally replaced by an empty list.',
 'Selection prefers the first nondefault entry containing the challenge identity.',
 'If no nondefault entry matches, selection returns the first default entry.',
 'If no entry matches and no default exists, selection returns an empty list.',
 'Trainer selection and template selection perform separate loads.'
])
group('R09', 'pbGenerateBattleTrainer', ['F03 §2.5','F03 §4','F07 WS-W06/W07/W31','F07 GR7-M12-001-C1–C6'], [
 'Opponent creation uses ruleset suggestedLevel.',
 'Opponent IV strength is determined by trainer index.',
 'A candidate list no longer than suggestedNumber is constructed in source order.',
 'The short candidate-list branch returns without filling missing team slots.',
 'The short candidate-list branch returns without final team validation.',
 'A zero-length candidate list performs no individual creation.',
 'An attempted missing template fails at its individual-creation receiver.',
 'A longer candidate list is sampled with replacement.',
 'Each retry clears the current opponent party before repopulating it.',
 'The long branch stops only when final ruleset validation succeeds.',
 'The long branch has no retry bound.'
])
group('R10', 'pbOrganizedBattleEx', ['F01 §4.2','F03 §3','F03 §4','F05 §2'], [
 'The debug shortcut clears the temporary battle record.',
 'The debug shortcut returns true before healing the player party.',
 'The normal path heals the player party before level adjustment.',
 'The normal path obtains the adjustment result before snapshotting player items.',
 'The normal path snapshots opponent items after level adjustment returns.',
 'The battle is created after the item snapshots.',
 'The created battle internalBattle flag is set false before preparation.',
 'The wrapper applies world preparation after local battle creation.',
 'A normal battle return reaches EXP restoration before player cleanup.',
 'A normal battle return cleans up all player members before opponent members.',
 'Cleanup heals each member before removing Mega state.',
 'Cleanup removes Mega state before removing Primal state.',
 'Cleanup restores the saved item by current position.',
 'A missing saved item position is assigned as nil.',
 'The temporary battle record is cleared after both parties finish normal cleanup.',
 'A win result permits a new record dump into the temporary record.',
 'A loss result permits a new record dump into the temporary record.',
 'A draw result permits a new record dump into the temporary record.',
 'Result 1 increments trainer battles won.',
 'Result 2 increments trainer battles lost.',
 'Result 3 increments trainer battles lost.',
 'Result 5 increments trainer battles lost.',
 'Only result 1 makes the wrapper return true.',
 'The wrapper does not write the session decision.',
 'The wrapper does not increment session wins.',
 'The wrapper does not increment session battleNumber.',
 'An uncaught battle error bypasses normal cleanup.',
 'A construction error occurs before the final temporary-record clearing.'
])
group('S10', 'Battle.pbGainExp/pbGainEVsOne', ['F03 §3','F01 §4.2'], [
 'Ordinary growth returns before awarding EVs when internalBattle is false.',
 'The direct EV-award helper has no internalBattle guard of its own.',
 'The direct EV helper computes each-stat remaining capacity from EV_STAT_LIMIT.',
 'The direct EV helper computes remaining total capacity from EV_LIMIT.'
], joins=('GR8-CRE-001.v2 existing finite direct-helper adjudication reception',))
group('R08', 'PBPokemon.fromInspected/createPokemon', ['F03 §2.5'], [
 'An unknown item literal parses to nil.',
 'An unknown move literal is omitted from the accepted move list.',
 'Accepted moves retain their source order after unknown moves are omitted.',
 'The parser considers at most the configured maximum move slots.',
 'If no recognized move remains, the parser uses the first move registry key.',
 'Individual creation disables ordinary default-move filling.',
 'Individual creation runs the normal creature constructor before assigning the template item.',
 'Individual creation redraws a 32-bit personal identity after the normal constructor.',
 'Individual creation assigns the template nature.',
 'Individual creation sets happiness to zero.',
 'RETURN is replaced with FRUSTRATION only when FRUSTRATION exists.',
 'An empty EV emphasis list does not assign template EVs.',
 'Each listed EV emphasis receives EV_LIMIT divided by emphasis-list length.',
 'Repeated EV entries remain part of the divisor.',
 'Individual creation writes the supplied IV to every main stat.',
 'Individual creation recalculates stats after the IV assignments.'
])
group('S01', 'Pokemon.initialize/ability_index/ability_id/form=/item=', ['F03 §2.5','F01 §3'], [
 'An explicit nil trainer argument produces a default Owner record.',
 'A trainer object produces a new Owner populated from that trainer.',
 'Default ability-index selection is based on personal-identity parity.',
 'A defined ability-index value is retained rather than recalculated.',
 'Changing form clears the cached ability value.',
 'Changing form does not clear ability_index.',
 'Changing form invokes the form-change handler before the final stat recalculation.',
 'Changing form can register the creature in the live player Pokedex.',
 'A truthy forced form bypasses ordinary simple-form lookup.',
 'An unknown nonnil item assignment leaves the old item unchanged.',
 'A nil item assignment clears the held item identity.'
])
group('R07', 'BattleFactoryData.pbChooseRentals/pbPrepareSwaps/pbChooseSwaps', ['F03 §2.6'], [
 'Rental confirmation increments swaps through the active-session counter.',
 'Rental confirmation submits the selected object-reference list.',
 'Preparing swaps retains the previous opponent-party reference.',
 'Successful swap increments swaps through the active-session counter.',
 'An unsuccessful swap does not increment swaps.',
 'Swap selection submits the current rental list even when no swap succeeds.',
 'Factory opponent candidates are created with a nil trainer argument.',
 'Assigning a candidate to an opponent party does not itself rewrite its Owner record.'
])
group('R10', 'pbRecordLastBattle/pbPlayBattle', ['F05 §1','F05 §2','F05 §6'], [
 'Record promotion assigns the current temporary record into the global last-battle field.',
 'Record promotion clears the temporary record after the global assignment.',
 'A nil playback argument returns before creating a scene.',
 'A nonnil playback argument creates a scene before deserializing the record.',
 'The playback scene is marked abortable before deserialization.',
 'Playback dispatch recognizes recorded type 0.',
 'Playback dispatch recognizes recorded type 1.',
 'Playback dispatch recognizes recorded type 2.',
 'An unrecognized type leaves no selected playback battle object.',
 'Playback does not call the organized-battle restoration wrapper.'
])
group('R05', 'RecordedBattleModule.pbGetTrainerInfo', ['F05 §3'], [
 'A nil trainer argument returns nil.',
 'An array trainer argument produces one metadata entry per array member.',
 'Player metadata clones the name.',
 'Player metadata clones the badges collection.',
 'NPC metadata substitutes ellipsis for a missing lose text.',
 'NPC metadata substitutes ellipsis for a missing win text.',
 'A direct nonarray trainer argument reaches an unbound index-name expression before either bare-trainer return.'
], joins=('GR8-FAC-001 candidate scope adjudication by actual different nonauthor',))

forward = {'schema':'gr8-facility-manual-assertions/v1','method':'Each assertion above was manually authored from the new actual full reading, not split by punctuation or synthesized from old locator counts.', 'atoms':atoms,
 'bounded_denominator':len(atoms),'full_original_atomic_census':'OPEN; these atoms do not exhaust all22R/8F meanings.',
 'source_identities':{k:{a:v for a,v in x.items() if a in ['repo','commit','tree','path','bytes','sha256','blob']} for k,x in identities.items()},
 'execution':'NOT_EXECUTED','update_started':False}
(ROOT/'forward-mapping.json').write_text(json.dumps(forward,ensure_ascii=False,indent=2)+'\n')
reverse=[]
for a in atoms:
    for receiver in a['formal_receivers']:
        reverse.append({'formal_clause':receiver,'atomic_assertion':a['id'],'meaning':a['assertion'],'source':a['source'],'source_unit':a['unit_locator'],'premise':a['premise'],'status':a['status'],'pending_dependencies':a['pending_dependencies']})
(ROOT/'reverse-mapping.json').write_text(json.dumps({'schema':'gr8-facility-manual-reverse/v1','mappings':reverse,'true_bounded_assertions':len(atoms),'full_formal_atomic_denominator':'OPEN_NOT_CLAIMED','shared_catalog_external_meanings':'All retained in next-dispatch.json; none removed to change denominator.','execution':'NOT_EXECUTED'},ensure_ascii=False,indent=2)+'\n')
print('manually authored bounded assertions:',len(atoms),'reverse bindings:',len(reverse))
