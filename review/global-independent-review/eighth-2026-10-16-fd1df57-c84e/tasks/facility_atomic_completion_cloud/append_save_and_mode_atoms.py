# Historical manual authoring transcript only. Frozen JSON includes subsequent explicit corrections; do not rerun over the final evidence.
"""Serialize manually written finite assertions; never infer reading or closure."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
f = json.loads((ROOT / 'forward-mapping.json').read_text())
r = json.loads((ROOT / 'reverse-mapping.json').read_text())
assert len(f['atoms']) == 241, 'Run once against the frozen first manual batch.'

def group(source, unit, receivers, assertions, premise=None, joins=()):
    for assertion in assertions:
        a = dict(id='FAC-A%04d' % (len(f['atoms']) + 1), source=source,
                 unit_locator=unit, assertion=assertion, formal_receivers=receivers,
                 premise=premise or 'Fixed R/B8; no later override; ordinary valid inputs and named calls return normally through the observation point. Static source only.',
                 pending_dependencies=list(joins),
                 status='LOCAL_FACT_WITH_NAMED_JOIN_OPEN' if joins else 'BOUNDED_SOURCE_AND_FORMAL_RECONCILED',
                 evidence='SOURCE_STATIC', execution='NOT_EXECUTED', reader='/root/facility_atomic_completion_cloud')
        f['atoms'].append(a)
        for receiver in receivers:
            r['mappings'].append(dict(formal_clause=receiver, atomic_assertion=a['id'], meaning=assertion,
                                     source=source, source_unit=unit, premise=a['premise'], status=a['status'], pending_dependencies=list(joins)))

group('R12', 'SafariState.initialize/pbStart/pbEnd/pbReceptionMap', ['F06 §3', 'F08 SF01/SF32'], [
 'A new Safari state has nil start position.',
 'A new Safari state has zero ball budget.',
 'A new Safari state has zero capture count.',
 'A new Safari state is inactive.',
 'A new Safari state has zero steps.',
 'A new Safari state has zero decision.',
 'Starting Safari stores the current map, x, y and direction in a new start array.',
 'Starting Safari copies the supplied ball count without validating nonnegativity.',
 'Starting Safari marks the state active before copying configured steps.',
 'Starting Safari copies SAFARI_STEPS, including zero or negative configured values.',
 'Starting Safari does not reset the previous capture count.',
 'Starting Safari does not reset the previous decision.',
 'An active reception-map query reads the first saved start coordinate.',
 'An inactive reception-map query returns zero.',
 'Ending Safari clears the start position.',
 'Ending Safari resets ball budget, captures, steps and decision to zero.',
 'Ending Safari marks the state inactive.',
 'Ending Safari requests a map refresh after clearing its state.'
])
group('R12', 'pbSafariState/pbInSafari?/pbGoToStart/event handlers', ['F06 §3.2/§3.3/§10', 'F08 SF04/SF05/SF06/SF33'], [
 'The Safari getter creates a new state only when the stored field is falsey.',
 'The Safari getter returns an existing truthy field without class or inner-field validation.',
 'A valid Safari region requires an active state.',
 'The saved reception map is accepted as Safari region independently of the SafariMap flag.',
 'A current SafariMap flag also accepts a map while the session is active.',
 'The enter-map handler ends Safari whenever the current region query is false.',
 'The transfer-step handler skips when handled[0] is truthy.',
 'A configuration of exactly zero disables Safari step decrement.',
 'The step handler skips when outside the Safari region.',
 'The step handler skips when the session decision is nonzero.',
 'An eligible step decrements the stored steps before testing whether they remain positive.',
 'A negative step configuration can therefore end Safari on the first eligible step.',
 'The expiration messages run before decision is set to one.',
 'Expiration sets decision one before requesting return to the start.',
 'Expiration sets handled[0] true only after the return request completes.',
 'Return to start performs transfer only when the current scene is a Scene_Map.',
 'Safari return uses saved map/x/y but forces direction two instead of the saved direction.',
 'The transfer flags are written before bike dismount and scene transfer.',
 'Outside a map scene, the return helper performs no transfer and does not undo an already written decision.'
])
group('R12', 'Safari calling-wild hook and pbSafariBattle', ['F06 §4.1/§4.5/§8.1', 'F08 SF07/SF08/SF34'], [
 'The Safari battle hook declines a handled value of either true or false.',
 'The Safari battle hook accepts only a nil handled slot and an active valid region.',
 'A non-Pokemon argument is passed through wild generation before building the foe party.',
 'A Pokemon argument is used directly without an additional generation call.',
 'The Safari wrapper passes the scalar live player object to the SafariBattle constructor.',
 'The battle receives a copy of the current outer Safari ball budget.',
 'The wrapper prepares the battle before entering its animation block.',
 'The Safari wrapper itself does not emit the ordinary on_start_battle notification.',
 'Input is updated before the battle ball budget is copied back to the outer session.',
 'The postbattle exhaustion condition accepts zero or negative ball budgets.',
 'Decision two suppresses only the out-of-balls message in the exhaustion branch.',
 'The exhaustion branch sets session decision one and requests return to start.',
 'Capture decision four increments total Safari catches.',
 'Capture decision four increments the session capture count.',
 'Capture decision four updates the greatest per-session capture statistic after increment.',
 'The wrapper writes the core decision to game variable one after the exhaustion transfer.',
 'The wild-end notification runs after state/statistic/variable writes and any exhaustion transfer.',
 'The Safari wrapper returns the core integer decision.'
], joins=('Full world/creature wild generation/event-order/radar/ordinary capture producer contracts remain FAC-I09.',))
group('R18', 'BugContestState.initialize/clear/queries', ['F06 §5.1/§5.3/§7.3/§10', 'F08 SF21/SF26/SF32'], [
 'BugContest initialization calls clear before assigning lastContest nil.',
 'Clear resets ball budget and decision to zero.',
 'Clear resets ended and inProgress to false.',
 'Clear removes the retained Pokemon and replaces otherparty with an empty array.',
 'Clear replaces contestants and places with empty arrays.',
 'Clear clears the judging start and replaces contest/reception map collections with empty arrays.',
 'Clear does not clear lastContest, chosenPokemon or timer_start.',
 'Held-recently returns false without a lastContest timestamp.',
 'Held-recently compares wall-clock seconds since lastContest with a strict 24-hour bound.',
 'Expiry requires an active state whose decision is zero.',
 'A nonpositive TIME_ALLOWED disables expiry.',
 'Positive-time expiry uses System.uptime minus timer_start with an inclusive threshold.',
 'The active query directly returns the inProgress field.',
 'Decided is true for active nonzero decision or an ended state.',
 'The player-place query examines only the first three stored place entries.',
 'The player-place query returns three when those entries contain no negative contestant index.',
 'The place-information query uses the supplied place index without a first-three restriction.',
 'The place-information query writes name, species name and score to variables one, two and three in that order.',
 'An empty or out-of-range place entry fails at its read rather than producing a fabricated default.'
])
group('R18', 'BugContestState.pbStart/pbEnd', ['F06 §5.2/§10', 'F08 SF03/SF18/SF20/SF31'], [
 'Start copies ball budget and marks the session active before selecting the chosen party member.',
 'Start clears retained Pokemon and lastContest before selecting the chosen party member.',
 'Start writes the monotonic timer origin and a fresh places array before selecting the chosen party member.',
 'An unset chosen index fails in the indexed party lookup after those preceding writes.',
 'A positive out-of-range chosen index yields nil and can still finish start with a singleton nil party.',
 'All members whose indices differ from the chosen index are appended to otherparty in original order.',
 'Opponent contestant identities are sampled with duplicate rejection until min(5, eight names) distinct values have been retained.',
 'Contestant selection has no bounded iteration count.',
 'The player party is replaced by the selected singleton after opponent contestant selection.',
 'Start resets decision and ended only after replacing the player party.',
 'Start increments the bug-contest count at the final tail.',
 'End returns immediately when the session is inactive.',
 'End appends the stored otherparty members to the current player party before its interruption branch.',
 'An interrupted end sets ended false and skips nickname/storage of the retained Pokemon.',
 'A normal end calls final nickname/storage for a nonnil retained Pokemon before setting ended true.',
 'The win statistic queries the first-three place result even for interrupted end.',
 'Ending before judging can therefore fail after party append but before clearing activity fields.',
 'Successful end clears ball budget, inProgress, decision, retained Pokemon and temporary party.',
 'Successful end clears contest and reception maps without clearing the places array or judging start.',
 'Successful end stores wall-clock lastContest only after these state writes.',
 'Successful end requests map refresh last.'
], joins=('Final nickname/storage producer and all Pokemon/party capacity effects remain FAC-I09; wall and monotonic runtime behavior NOT_EXECUTED.',))
group('R18', 'pbJudge/pbStartJudging/TimerDisplay/frame and map hooks', ['F06 §5.3/§5.5/§7.2/§7.3', 'F08 SF21/SF22/SF24/SF25/SF26'], [
 'Judging adds the retained player Pokemon as contestant minus one when it exists.',
 'A map without BugContest encounters falls back to Land before eligibility is tested.',
 'An empty map/type candidate collection raises before generating opponent Pokemon.',
 'Each opponent independently samples one eligible map/type pair.',
 'An empty encounter result raises before Pokemon construction for that opponent.',
 'Opponent judging Pokemon are created through Pokemon.new and do not pass through the wild-generation notification entry.',
 'Opponent judging HP is sampled from one inclusive to totalhp exclusive.',
 'Fewer than three total judge candidates raises before sorting or place append.',
 'Judging sorts by descending score without adding an explicit tie-break criterion.',
 'Judging appends the best three entries to the existing places array.',
 'StartJudging writes decision one before the judge call.',
 'StartJudging transfers only after successful judging and only in a map scene.',
 'An absent judging start can fail after places have already been appended.',
 'The timer display clamps a negative remaining time to zero.',
 'The timer display updates its text only when the integer displayed time changes.',
 'The map/spriteset hook creates a timer only for active, undecided state and TIME_ALLOWED unequal to zero.',
 'A negative time configuration thus permits a 00:00 display while the expiry query stays false.',
 'The frame expiry callback defers judging while a move route is forced, a map interpreter is running, or a message window is showing.',
 'The expiry callback has no separate in_menu condition.',
 'The leave-map hook calls interrupted end only for an active state and an off-limits destination.',
 'The enter-map hook delegates to clear-if-ended; that helper clears only when inactive and away from the saved judging map.'
], joins=('World encounter lookup and full event-order receipts remain FAC-I09; tie ordering and actual host timer behavior remain expressly unproved.',))
group('S19', 'GlobalMetadata.initialize/special-mode accessors', ['F06 §8.4', 'F08 SF30d/SF36/SF37'], [
 'The global metadata object exposes both special-mode fields as ordinary accessors.',
 'Global metadata initialization assigns nil to Safari state and BugContest state.',
 'Global metadata initialization can fail in earlier Phone/regional-dex/DayCare suppliers before reaching the special-mode nil assignments.',
 'The same global metadata object also exposes challenge and lastbattle fields.'
])
group('S16', 'SaveData global_metadata registration76–81', ['F06 §8.4', 'F08 SF30d/SF36/SF37'], [
 'The global_metadata save supplier returns the live global metadata object.',
 'The global_metadata registration validates the outer PokemonGlobalMetadata class.',
 'The registration restore callback assigns the stored whole object to the live global.',
 'The registration new-game supplier requests a new PokemonGlobalMetadata object.',
 'This registration is neither bootup nor reset-on-new-game, so its actual loaded flag participates in the surrounding load protocol.',
 'The outer registration adds no SafariState or BugContestState inner-field repair or inner class validation.'
])
group('S15', 'SaveData read/get_data/save_to_file', ['F06 §8.4', 'F08 SF30d/SF36/SF37/SF40'], [
 'A serialized first Hash is treated as the already keyed save-data representation.',
 'A non-Hash first object sends the complete sequential stream through the old-format conversion path.',
 'The default declarations currently provide no old-format callbacks for the seventeenth registered value either; old sequential adaptation is not a mode-specific inner-object migrator.',
 'The save wrapper compiles and validates the data Hash before opening the destination for writing.',
 'The writer opens in wb mode and requests Marshal.dump of the whole Hash.',
 'A whole-object dump request establishes the static input graph, without proving native serialization or later monotonic-clock equivalence.'
])
group('S06', 'SaveData Conversion complete engine/get/run/single', ['F06 §8.4', 'F08 SF30e'], [
 'Conversion selection snapshots the saved Essentials version or default 18.1.',
 'Conversion selection snapshots the saved game version or default 0.0.0.',
 'Essentials conversions are considered before game conversions.',
 'Trigger version keys are sorted through PluginManager.compare_versions.',
 'Registrations at one trigger version retain registration order.',
 'A conversion runs only when the supplied saved version is strictly less than its trigger version.',
 'No selected conversions returns false before backup creation.',
 'A selected full conversion first writes a backup at SaveData::FILE_PATH plus .bak.',
 'The backup uses the default path even when an outer reader was passed a different source path.',
 'Each per-value callback requires the corresponding key before it is called.',
 'Per-value callbacks run before a conversion whole-data callback.',
 'Successful earlier conversion writes are not rolled back when a later callback raises.',
 'Current version markers are written only after all selected callbacks and the final success log.',
 'A later outer write failure does not undo already advanced in-memory version markers.',
 'Single-value conversion reuses selection but calls only that key-specific callback.',
 'Single-value conversion does not run whole-data callbacks or write a backup.',
 'Single-value conversion does not advance the supplied context version markers.'
], joins=('PluginManager version comparison exact general source owner remains KERNEL; finite packet preserves its callable ordering without native execution.',))
group('S05', 'All14 defaults and independent fullR registration census', ['F06 §8.4', 'F08 SF30e'], [
 'The fixed default tree has fourteen actual register_conversion calls, all in the completely read default conversion file.',
 'The complete default conversion bodies contain no dedicated Safari-state conversion.',
 'The complete default conversion bodies contain no dedicated BugContest-state conversion.',
 'This absence does not establish arbitrary old inner state compatibility or exclude plugin/dynamically registered conversions.'
], premise='Fixed default Data/Scripts census and full14 bodies; exclude later overrides, plugins and dynamic additions; indirect generic callbacks are not asserted to repair inner mode objects.')
group('S07', 'Game.load/start_new/save', ['F06 §8.3/§8.4', 'F08 SF30d/SF36/SF37/SF40'], [
 'Game.load validates a Hash before loading registered values.',
 'Loading all registered values precedes the uptime/session/map/autoplay/update/scene tail.',
 'Normal title return marks nonboot/nonreset values unloaded before the next title call, making global metadata eligible for a subsequent normal new-game load.',
 'An arbitrary direct start_new call is not a guarantee that an already loaded global is replaced.',
 'Game.save validates the destination string and Boolean safe argument before its state writes.',
 'Game.save assigns safesave before incrementing save_count.',
 'Game.save updates magic number and recent-save time before entering the rescued writer region.',
 'Only IOError and SystemCallError in that rescued region decrement save_count and return false.',
 'Those caught failures do not restore safesave, magic number or recent-save time.',
 'Other supplier/type/callback exceptions can propagate after already committed prefixes.',
 'Successful normal saving resets the graphics frame counter before returning true.'
])
group('S21', 'Pause menu Save/Bag/Quit Game', ['F06 §8.3', 'F08 SF30a–c/SF36/SF37/SF38/SF39/SF40'], [
 'The dedicated Save item requires an existing game system.',
 'The dedicated Save item requires saving not disabled.',
 'The dedicated Save item additionally requires false Safari-region and false active-contest queries.',
 'The Bag item is hidden during any active BugContest state.',
 'The ordinary Quit Game item has no Safari or BugContest condition.',
 'Quit Game hides the menu before asking for exit confirmation.',
 'Refusing exit refreshes and shows the menu, then returns false without calling the normal save screen.',
 'Accepting exit constructs the shared save screen and calls it.',
 'Accepting exit ignores the save screen Boolean return.',
 'After a normal save-screen return, exit closes the menu, assigns the global scene nil and returns true.',
 'The normal Quit Game handler contains no Safari end or BugContest judge/end call.',
 'An uncaught exception in the save screen can prevent the exit tail.'
])
group('S22', 'PokemonSaveScreen.pbSaveScreen', ['F06 §8.3/§10', 'F08 SF36/SF37/SF39/SF40'], [
 'The shared save screen starts its scene before asking whether to save.',
 'Refusing the initial save prompt leaves ret false and ends the screen normally.',
 'An existing save together with begun_new_game prompts for serious overwrite confirmation.',
 'Refusing overwrite ends the screen and returns false before Game.save.',
 'Accepting required confirmations clears begun_new_game before calling Game.save.',
 'A true Game.save result yields a saved message and a true return.',
 'A false Game.save result yields a failed message and a false return.',
 'All these Boolean paths end the save-screen scene normally.',
 'An unrescued Game.save exception does not receive this normal scene-cleanup tail.',
 'Neither refusal path calls the normal writer or implicitly reverses unrelated earlier state changes.'
])
group('S20', 'Scene_Map.call_menu/miniupdate/updateSpritesets', ['F06 §8.3/§10', 'F08 SF36/SF37/SF38/SF39/SF40'], [
 'call_menu marks in_menu true before constructing and starting the pause menu.',
 'call_menu resets in_menu false only after that menu call returns normally.',
 'miniupdate marks in_mini_update true before player/map/system/screen updates.',
 'miniupdate can process requested transfers before updating spritesets.',
 'updateSpritesets emits on_frame_update after sprites and map renderer updates.',
 'miniupdate clears in_mini_update only after updateSpritesets returns normally.',
 'The normal title path marks values unloaded before setting the next title scene.',
 'Ordinary Quit Game setting scene nil follows a different tail from the title_screen_calling unload branch.'
])
group('S23', 'pbUpdateSceneMap/CreateDisposeMessage/Display/ShowCommands/Confirm', ['F06 §8.3/§10', 'F08 SF36/SF37/SF38/SF39/SF40'], [
 'pbUpdateSceneMap invokes miniupdate only for a map scene while not faded.',
 'Creating a normal message window marks message_window_showing true.',
 'Disposing a normal message window clears message_window_showing before disposing the window.',
 'Letter-by-letter message loops can request map miniupdates.',
 'The command-selection loop can request map miniupdates while waiting for input.',
 'The normal yes/no confirmation treats command index zero as true.',
 'The serious confirmation reverses the displayed choice order and treats index one as true.',
 'The normal confirmation cancel mapping selects No.',
 'The serious confirmation cancel mapping selects No as well.',
 'The source update chain therefore supports explicit no-unrelated-callback premises; the presence of a menu alone does not freeze every frame callback.'
])
group('R12', 'Safari pause info and mode-specific Quit', ['F06 §8.3', 'F08 SF27/SF30'], [
 'Safari pause information first calls the aliased prior information method.',
 'Safari pause information appears only within the Safari region.',
 'Nonpositive configured Safari steps show only the ball budget.',
 'Positive configured steps show remaining steps, configured steps and balls.',
 'The Safari-specific Quit item appears only in the Safari region.',
 'Its accepted confirmation ends the menu before writing decision one and requesting return.',
 'Its refused confirmation refreshes and reopens the menu and returns false.'
])
group('R18', 'BugContest pause info and mode-specific Quit Contest', ['F06 §8.3', 'F08 SF27/SF30'], [
 'Contest pause information first calls the previous aliased information method.',
 'An active contest with retained Pokemon shows species name, level and ball budget.',
 'An active contest without retained Pokemon shows None and ball budget.',
 'Quit Contest visibility requires active contest state.',
 'Accepted Quit Contest confirmation ends the menu and calls StartJudging rather than interrupted end.',
 'Refused Quit Contest confirmation refreshes and reopens the menu and returns false.'
])

# Preserve the first batch's explicit external producer qualifications across regenerations.
for a in f['atoms']:
    if a['source'] == 'S01' and not a['pending_dependencies']:
        a['pending_dependencies'] = ['Current WP19/WP21 and CRE-A mandatory form/species companion reception remains open.']
        a['status'] = 'LOCAL_FACT_WITH_NAMED_JOIN_OPEN'
        for m in r['mappings']:
            if m['atomic_assertion'] == a['id']:
                m['pending_dependencies'] = list(a['pending_dependencies'])
                m['status'] = a['status']
ledger = json.loads((ROOT / 'reading-ledger.json').read_text())
for x in ledger['supplemental']:
    f['source_identities'][x['id']] = {k:v for k,v in x.items() if k in ['repo','commit','tree','path','bytes','sha256','blob']}
f['bounded_denominator'] = len(f['atoms'])
r['true_bounded_assertions'] = len(f['atoms'])
(ROOT / 'forward-mapping.json').write_text(json.dumps(f, ensure_ascii=False, indent=2) + '\n')
(ROOT / 'reverse-mapping.json').write_text(json.dumps(r, ensure_ascii=False, indent=2) + '\n')
print(len(f['atoms']), 'manually authored finite atoms;', len(r['mappings']), 'bindings; exhaustive original census remains OPEN')
