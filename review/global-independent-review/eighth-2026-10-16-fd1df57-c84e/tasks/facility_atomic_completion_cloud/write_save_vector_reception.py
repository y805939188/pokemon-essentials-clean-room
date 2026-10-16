"""Freeze explicitly authored SF children; this is documentation I/O only."""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent

def child(cid, meaning, sources, boundary='STATIC_RECONCILED_UNDER_STATED_PREMISES'):
    return dict(id=cid, meaning=meaning, sources=sources, status=boundary,
                execution='NOT_EXECUTED', reader='/root/facility_atomic_completion_cloud')

shared = ['S21 Pause321 Save254–272/Quit304–321', 'S22 SaveUI100–129',
          'S07 Game.save105–126', 'S15 SaveData.compile/write wrapper54–62',
          'S17 Value.save/compile_save_hash', 'S16 global/player/stats registration',
          'R12 Safari state and getters', 'R18 BugContest state and getters']
cases = [
 dict(id='SF30a–c', exact_formal='F08 line40; F06 §8.3', children=[
   child('SF30a', 'Active Safari in its region excludes dedicated Save while ordinary Quit Game and the Safari-specific Quit remain independently visible.', ['S21 Save condition254–260/Quit304–321', 'R12 Quit Safari178–196']),
   child('SF30b', 'Active BugContest excludes dedicated Save and Bag; ordinary Quit Game and Quit Contest remain independently visible.', ['S21 Bag189–205/Save254–260/Quit304–321', 'R18 Quit Contest426–441']),
   child('SF30c', 'With both mode queries false, existing system and saving permitted, the dedicated Save condition passes.', ['S21 Save254–260']),
 ]),
 dict(id='SF30d', exact_formal='F08 line40; F06 §8.4',
      premise='Both sessions normally ended; all registered values and outer types valid; successful ordinary serialization/read, default current converter context, and correct boot/load protocol; no unrelated intervening mutation. Native success is a premise, not an observed result.', children=[
   child('SF30d.1', 'Safari end fields and successful Contest end fields remain within their existing state objects in the global metadata object.', ['R12 pbEnd48–58', 'R18 pbEnd205–226', 'S19 accessors31–34']),
   child('SF30d.2', 'The whole global object is supplied without mode-state projection to compile_save_hash and restored by the registered whole-object assignment.', ['S16 global76–81', 'S17 compile_save_hash278–283/Value.load40–45', 'S15 read/write24–61']),
   child('SF30d.3', 'Mode catch/count/win statistics are writes to the live stats object, which has its own whole-object saved/load registration.', ['R12 pbSafariBattle151–155', 'R18 pbStart195/pbEnd214', 'S16 stats119–127']),
   child('SF30d.4', 'No default registered conversion names or repairs the inner Safari or Contest state; this does not prove arbitrary old inner-format compatibility.', ['S05 complete14 conversion bodies1–420', 'S06 entireengine1–223', 'independent fullR registration census:5d11ec']),
   child('SF30d.5', 'Runtime equivalence of saved monotonic timer origin, wall-clock checks and actual native roundtrip remains unknown and unexecuted.', ['R18 expired?/pbContestHeld?/timer_start', 'S15 Marshal request'], 'EXPLICIT_RUNTIME_UNKNOWN_NOT_EXECUTED'),
 ]),
 dict(id='SF30e', exact_formal='F08 line40; F06 §8.4',
      premise='Fixed default Data/Scripts registrations; exclude plugins/dynamic additions and later overrides.', children=[
   child('SF30e.1', 'All actual default register_conversion calls are the fourteen declarations in the fully read420-line source; comments/examples are separately excluded.', ['S05', 'independent allData/Scripts search5d11ec']),
   child('SF30e.2', 'All fourteen complete bodies contain no dedicated Safari or BugContest conversion; full conversion engine and whole-object restore do not provide an implicit inner-field migration.', ['S05 all14', 'S06 full223', 'S16 global76–81']),
   child('SF30e.3', 'Ordinary load can still execute unrelated selected conversions; the bounded absence is not a claim of no migration anywhere or for arbitrary versions/plugins.', ['S06 get_conversions/run_conversions', 'S15 read_from_file']),
 ]),
 dict(id='SF36', exact_formal='F08 line46; F06 §8.3/§8.4',
      premise='Active valid Safari in-region; all normal player/map/registered values, serialization graph, resources, confirmations and write dependencies succeed; accept exit/save/required overwrite; no unrelated callback or mutation.', children=[
   child('SF36.1', 'Dedicated Save is absent while ordinary and mode-specific exits retain their own conditions.', ['S21 Save/Quit', 'R12 mode Quit']),
   child('SF36.2', 'The save supplier retains active Safari and its start/balls/steps/captures/decision/activity fields in the whole global object.', ['S16 global76–81', 'R12 SafariState field writes/getter', 'S17 compile_save_hash']),
   child('SF36.3', 'The accepted ordinary exit calls no Safari clear/end; the serializer input therefore retains these values under the explicit no-other-callback premise.', ['S21 Quit304–321', 'S22 Save100–129', 'S07 save105–126']),
   child('SF36.4', 'After normal save-screen return, the ordinary exit closes its menu and sets scene nil.', ['S21 Quit304–321']),
   child('SF36.5', 'No native writer, isolated fake writer, game exit or reload was executed by this review.', ['execution register'], 'NOT_EXECUTED'),
 ]),
 dict(id='SF37', exact_formal='F08 line47; F06 §8.3/§8.4',
      premise='Active not-expired valid Contest, selected S, stored spares, retained K and monotonic origin; otherwise same successful save and no-other-callback premises as SF36.', children=[
   child('SF37.1', 'Player supplier returns the live player whose party is still the selected singleton [S].', ['R18 pbStart171–196', 'S16 player3–8']),
   child('SF37.2', 'Global supplier retains the active Contest object with spares/K/origin and remaining session fields.', ['R18 pbStart/lastPokemon/timer_start', 'S16 global76–81']),
   child('SF37.3', 'Ordinary exit and save perform no Contest party append, end or judge call.', ['S21 Quit304–321', 'S22 Save100–129', 'S07 save105–126']),
   child('SF37.4', 'Timer display, separate battle budget and postload monotonic origin semantics are not inferred from inclusion in the saved object graph.', ['R18 TimerDisplay/expired?', 'R02 battle budget', 'S15 write request'], 'EXPLICIT_SEPARATE_BOUNDARIES_NOT_EXECUTED'),
 ]),
 dict(id='SF38', exact_formal='F08 line48; F06 §8.3',
      premise='Active either mode; refuse initial normal Quit Game confirmation; resources/confirmation return normally; no unrelated callback.', children=[
   child('SF38.1', 'Refusal executes menu refresh/show and returns false.', ['S21 Quit304–321']),
   child('SF38.2', 'Refusal does not enter save-screen construction, normal Game.save, Safari end or Contest judging.', ['S21 Quit304–321']),
   child('SF38.3', 'These ordinary-exit effects remain distinct from accepted Safari-specific Quit or Quit Contest.', ['R12 Quit178–196', 'R18 Quit422–441']),
 ]),
 dict(id='SF39', exact_formal='F08 line49; F06 §8.3',
      premise='Accept normal Quit Game; either refuse initial save or refuse necessary overwrite; no unrelated callback and confirmations return normally.', children=[
   child('SF39.1', 'Initial save refusal reaches the shared screen tail with false and never calls Game.save.', ['S22 Save100–129']),
   child('SF39.2', 'Refused overwrite returns false before clearing begun_new_game or calling Game.save.', ['S22 Save103–114']),
   child('SF39.3', 'Exit ignores either false result and still closes the menu and sets scene nil.', ['S21 Quit304–321']),
   child('SF39.4', 'No normal writer was called for this attempt, and no unrelated earlier state is automatically restored.', ['S22 Save100–129', 'S21 Quit304–321']),
 ]),
 dict(id='SF40a', exact_formal='F08 line50; F06 §8.3',
      premise='Accept normal exit/save/required overwrite; valid values until a specified IOError/SystemCallError inside the rescued save region; feedback/resources subsequently return normally; no unrelated callback.', children=[
   child('SF40a.1', 'begun_new_game is cleared before Game.save is called.', ['S22 line114']),
   child('SF40a.2', 'safesave, count increment, magic and recent time precede the rescued writer region.', ['S07 save105–126']),
   child('SF40a.3', 'The caught error decrements only save_count and returns false; the remaining listed prefixes are not rolled back.', ['S07 rescue120–123']),
   child('SF40a.4', 'After failed-save feedback returns, the shared screen returns false and the ordinary exit still performs its scene-nil tail.', ['S22 failure branch/tail', 'S21 Quit tail']),
   child('SF40a.5', 'If wb opening/write was reached, truncation or partial output is possible; if the caught error instead follows a completed dump, a fully written file is also possible. No transaction is promised.', ['S15 save_to_file54–62', 'S07 frame_reset/rescue']),
 ]),
 dict(id='SF40b', exact_formal='F08 line50; F06 §8.3',
      premise='Accept normal confirmations; a named unrescued supplier/type/callback exception occurs; ordinary core code only.', children=[
   child('SF40b.1', 'Already completed begun_new_game/safesave/count/magic/time or earlier supplier prefixes remain; no generic rollback block exists.', ['S22 line114', 'S07 save105–126', 'S17 Value.save/compile_save_hash']),
   child('SF40b.2', 'A value-type error during compile occurs before destination wb opening.', ['S17 Value.save and validation', 'S15 save_to_file54–62']),
   child('SF40b.3', 'Uncaught failure need not reach shared-screen disposal, return or ordinary Quit Game menu/scene-nil tail.', ['S22 Save100–129', 'S21 Quit304–321']),
   child('SF40b.4', 'This is a static failure-prefix derivation; no exception, disk failure or host exit was executed.', ['execution register'], 'NOT_EXECUTED'),
 ]),
]
packet = dict(schema='facility-sf-save-finite-child-reception/v1', frozen_utc=datetime.now(timezone.utc).isoformat(),
              reader='/root/facility_atomic_completion_cloud', B8='fd1df570cad987dc3852a3b958f03916e317f7fe',
              R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b', identities='reading-ledger.json S05–S07/S15–S17/S19–S25 and original R12/R18/F06/F08',
              provider='evidence/kernel-save-conversion-provider.v1.json; all13facts/8completeunits received with exact fixedR comparison',
              actual_own_read='All original R12/R18/F06/F08; complete SaveData82/Value284/SaveValues127/Conversion223/Conversions420/Start126/Pause321/Save139/SceneMap252; complete message confirmation/update methods and finite frame/step callbacks.',
              shared_sources=shared, cases=cases,
              exception_update_gate='Messages mark message_window_showing; nonfaded pause/command loops can run miniupdate→spritesets→on_frame_update; Contest expiry has no in_menu gate. Explicit no-unrelated-callback premises are therefore necessary rather than inferred from a displayed menu.',
              source_state_vs_runtime='Whole graph is a statically supplied value. No native serialization, clock equivalence, UI pixels, actual host exit or persisted roundtrip asserted.',
              whole_FAC_I10_status='FINITE_STATIC_SAVE_VECTOR_RECEIVED; full runtime/persistent compatibility not closed',
              whole_original22R8F_atomic_census='OPEN; no automatic wholeWP53/WP55/KERNEL/global acceptance',
              business='NOT_EXECUTED', UPDATE_NOT_STARTED=True)
(ROOT / 'save-vector-reception.v1.json').write_text(json.dumps(packet, ensure_ascii=False, indent=2) + '\n')
print('Manually authored save cases',len(cases),'children',sum(len(x['children']) for x in cases))
