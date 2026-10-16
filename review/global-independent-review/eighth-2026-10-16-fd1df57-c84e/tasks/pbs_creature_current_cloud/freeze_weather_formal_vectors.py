from pathlib import Path
import json, hashlib, datetime, subprocess

B = Path('/workspace/pokemon-essentials-clean-room')
R = Path('/workspace/pokemon-essentials')
P = Path(__file__).resolve().parent
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
BC = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
UTC = datetime.datetime.now(datetime.timezone.utc).isoformat()
READER = '/root/pbs_creature_current_cloud'

def identity(root, path):
    commit = RC if root == R else BC
    raw = (root / path).read_bytes()
    assert raw == subprocess.check_output(['git', 'show', commit + ':' + path], cwd=root)
    return {'repo': str(root), 'path': path, 'commit': commit,
            'tree': '7589c800b61ba13a13040ed0d686979b80a84fd0' if root == R else '751dfde81048c81390f89a65ca1d1a565ba8e1ca',
            'formal_subtree': None if root == R else 'f292698cdd4a8e725525a9be6dc34b75faaf151e',
            'bytes': len(raw), 'lines': len(raw.splitlines()), 'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob': subprocess.check_output(['git', 'rev-parse', commit + ':' + path], cwd=root, text=True).strip()}

def unit(root, path, start, end, io, qualification):
    ident = identity(root, path)
    assert end <= ident['lines']
    return {'identity': ident, 'range': [start, end],
            'text': '\n'.join((root / path).read_text().splitlines()[start - 1:end]) + '\n',
            'actual_reader': READER, 'actual_read_io': io, 'qualification': qualification}

def save_new(name, value):
    path = P / name
    assert not path.exists()
    raw = (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()
    path.write_bytes(raw)
    return {'path': name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

formal_path = 'deliverables/final-specification-set/combat-requirements/wp45-weather-terrain-side-and-position-effects.md'
catalog = 'deliverables/final-specification-set/test-catalog/combat-requirements-wp39-40-41-42-45.md'
world = 'Data/Scripts/010_Data/001_Hardcoded data/012_Weather.rb'
prepare = 'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb'
core = 'Data/Scripts/011_Battle/001_Battle/001_Battle.rb'
change = 'Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb'
weather_packet = json.loads((P / 'shadow-sky-weather-consumer.complete.v1.json').read_text())
weather_raw = (P / 'shadow-sky-weather-consumer.complete.v1.json').read_bytes()
common = [
    'Fixed R/B8 identities, no plugin/redefinition/concurrent mutation; earlier required calls return normally for the normal vector result.',
    'World weather Storm is a supplied valid current input. This does not prove any map event, weather probability or screen transition actually occurs.',
    'The vectors are source-static deductions, not executed tests. Arithmetic listed in the existing formal rows is read and manually bound; no new numerical audit/model is executed.',
    'Weather/terrain setter input is valid and the existing field container exists. Preparation steps before/after these setters may fail; no rollback or complete preparation success is assumed.',
    'The old weather packet and its mandatory source-premise companion remain jointly required. Existing sourceFULL is independent of these contained-source references.'
]
vectors = [
    ('W01', 181, 'World ID Storm supplies terrain Electric when the setting is enabled and no explicit terrain exists; its registered category is Rain, supplying battle Rain. Both setters write default/current/duration-1 directly. An explicit Misty terrain overrides only the terrain path, leaving the no-explicit-weather category path Rain. The source category is Rain, not an invented Storm category registration.',
     ['prepare_battle209–304', 'Weather entire165: Storm83–93/category86', 'Settings17/370', 'defaultTerrain780–784', 'defaultWeather694–698']),
    ('W02', 182, 'The weather-move parent rejects same stored weather. Direct core same-weather entry returns before all writes/callbacks, retaining supplied duration2. No refresh5/8 occurs on that direct same-weather path.', ['SKY02', 'SKY04']),
    ('W03', 183, 'At the reached weather stage, positive temporary Rain1 decrements to0; on normal end-feedback return raw weather becomesNone, forms are checked, and defaultSun restarts with fixedDurationfalse/usernil, producing-1. Subsequent weather feedback/ability/damage sees restoredSun. This row is a normal-return vector; the separate end-message prefix ambiguity is not silently accepted as an exception-order contract.', ['SKY07', 'SKY08', 'SKY16']),
    ('W04', 184, 'An active AirLock on a living battler makes effective weatherNone without clearing rawSandstorm. Positive stored2 decrements to1 independently, rawweather feedback may still occur, and the effectiveNone damage branch does not choose Sandstorm. If that active suppression ceases without another mutation, the same storedweather/duration becomes effective again.', ['SKY06', 'SKY07', 'SKY09', 'SKY11']),
    ('W05', 185, 'The parent ordinary weather move consults rawHeavyRain and rejects overwrite before the core call even while an active AirLock makes battle effective weatherNone. Suppression does not change the raw gate.', ['SKY02', 'SKY06']),
    ('W06', 186, 'The complete primordial-end method returns if rawweather equalsdefault; otherwise rawHarshSun without any active DesolateLand is cleared after its ending feedback, followed by weather-form checks and optional defaultRain restart at-1. DefaultNone remainsNone. The supplied last-source-departure premise is not proof of all caller reachability.', ['SKY16', 'weather core unit694–778/global helpers444–490']),
    ('W07', 187, 'The member effectiveWeather method applies an active UtilityUmbrella only to Sun/HarshSun/Rain/HeavyRain. Under battleSun an effective umbrella returnsNone while an unmasked member retainsSun; battle effective weather staysSun absent global suppression. Sandstorm andShadowSky are outside that item mask.', ['SKY06'])
]
complete_vectors = []
catalog_lines = (B / catalog).read_text().splitlines()
for sid, no, meaning, sources in vectors:
    assert catalog_lines[no - 1].startswith('| ' + sid + ' |')
    complete_vectors.append({'id': sid, 'formal_range': [no, no], 'complete_original_row': catalog_lines[no - 1],
                             'manual_source_join': meaning, 'source_bindings': sources, 'premises': common,
                             'status': 'FINITE_NORMAL_VECTOR_SOURCE_BOUND', 'business': 'NOT_EXECUTED'})

packet = {'schema': 'gr8-pbs-weather-formal-vectors/v1', 'utc': UTC, 'actual_reader': READER,
          'scope': 'Full actual WP45 body reading; only seven weather vector meanings plus exact world/prepare dependency units accepted. Whole WP45 behavior/domain acceptance remains OPEN.',
          'common_premises': common,
          'complete_formal_body': unit(B, formal_path, 1, 232, ['cf83c6', '0d4f1f', '3dc37c', '15da62'], 'All232lines actually read; historical source claims and unrelated domain clauses are not adopted as current execution/semantic credit.'),
          'complete_catalog_common': unit(B, catalog, 1, 4, ['15da62'], 'Complete common test-status premise.'),
          'complete_catalog_weather_section': unit(B, catalog, 177, 187, ['a7e6b3'], 'Seven complete original rows, headers and inputs retained.'),
          'complete_new_source_units': [unit(R, world, 1, 165, ['7ad5b8'], 'Whole original world Weather file actually read; native Tone/particle results not observed.'),
                                        unit(R, prepare, 209, 304, ['dc30a2'], 'Whole prepare_battle method; earlier own entire749-line file credit is separate.'),
                                        unit(R, core, 780, 784, ['9809d6'], 'Whole direct defaultTerrain setter only; following pbStartTerrain fragment is not adopted here.'),
                                        unit(R, change, 189, 228, ['b523ad'], 'Whole weather-form method, preserving the Eiscue new-setting qualifier.'),
                                        unit(R, 'Data/Scripts/001_Settings.rb', 11, 17, ['7ad5b8'], 'Complete generation setting declaration and comments, not entire Settings.'),
                                        unit(R, 'Data/Scripts/001_Settings.rb', 368, 370, ['7ad5b8'], 'Complete weather-to-terrain setting declaration and comments.')],
          'prior_complete_needed_weather_units': [a for a in weather_packet['complete_own_source_units']
                                                  if (a['identity']['path'] == core and a['range'] in [[694, 778], [444, 490]])
                                                  or a['identity']['path'].endswith('/011_Battle_EndOfRoundPhase.rb')
                                                  or (a['identity']['path'].endswith('/001_Battle_Battler.rb') and a['range'] in [[344, 358], [421, 437], [555, 565]])
                                                  or (a['identity']['path'].endswith('/004_Move_BaseEffects.rb') and a['range'] == [496, 525])],
          'prior_finite_source_packet': {'path': 'shadow-sky-weather-consumer.complete.v1.json', 'bytes': len(weather_raw), 'sha256': hashlib.sha256(weather_raw).hexdigest(), 'mandatory_companion': 'mandatory-shadow-sky-source-premises.v1.json'},
          'complete_manual_vector_bindings': complete_vectors,
          'SKY13_exact_qualifier': 'Eiscue canRestoreIceFace is newly set true by this callback only on its listed !ability_changed/EISCUE/ICEFACE/form1/effectiveHail gate. This callback does not clear a previously true flag on ShadowSky/None. The earlier sentence is a new-setting predicate, not a global flag invariant.',
          'unclassified_order_observation': {'id': 'PC-OBS-WEATHER-END-MESSAGE-ORDER-01', 'status': 'UNCLASSIFIED_NOT_FINDING', 'formal': [formal_path, 77], 'source': ['Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb', 9, 19], 'actual': 'positive duration decrement, then ending pbDisplay, then rawNone write', 'strong_no_required': 'The formal list may enumerate normal effects without promising exception-visible interleaving; the seven normal vectors are unchanged.', 'strong_opposing_read': 'If line77 specifies an ordered clear-before-feedback contract, an ending-message failure can distinguish rawShadowSky/duration0 from rawNone/duration0. Complete message-chain/history/independent decision are not yet established.', 'classification_owner': 'root; no new required/optional/context/vote increment'},
          'remaining_open': ['All nonweather WP45 source behavior, caller reachability, native message/animation output and arbitrary extra handlers are not approved by full formal reading.', 'End-message exception-order observation remains unclassified pending complete necessary source/formal/history and independent counterreview.', 'Existing global histories/equivalent incorporation and entire11consumer closures remain OPEN.'],
          'behavior': 'NOT_EXECUTED', 'update': 'UPDATE_NOT_STARTED', 'new_findings': 0, 'new_contexts': 0, 'new_votes': 0}
ref = save_new('weather-formal-w01-w07.complete.v1.json', packet)
ledger = json.loads((P / 'reading-ledger.json').read_text())
assert world not in ledger['dependencies_full_read']
ledger['dependencies_full_read'].append(world)
assert formal_path not in ledger['formal_full_read']
ledger['formal_full_read'].append(formal_path)
ledger['dependencies_partial_read'].append({'path': core, 'lines': [780, 784], 'actual_read_chunks': ['9809d6'], 'qualification': 'Complete direct defaultTerrain setter only; following partial method not adopted.'})
ledger['dependencies_partial_read'].append({'path': 'Data/Scripts/001_Settings.rb', 'lines': [368, 370], 'actual_read_chunks': ['7ad5b8'], 'qualification': 'Complete named setting declaration only.'})
ledger['formal_partial_read'].append({'path': catalog, 'lines': [177, 187], 'actual_read_chunks': ['a7e6b3'], 'qualification': 'Seven complete weather rows; normal-return field/source bindings in weather-formal-w01-w07.complete.v1.json.'})
ledger['updated_utc'] = UTC
(P / 'reading-ledger.json').write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + '\n')
reverse = json.loads((P / 'reverse-mapping.json').read_text())
assert len(reverse['clauses']) == 2799
for v in complete_vectors:
    reverse['clauses'].append({'id': 'PCR-WEATHER-VECTOR-' + v['id'], 'assertion': v['manual_source_join'],
                               'formal': {'path': catalog, 'lines': v['formal_range']}, 'complete_original_row': v['complete_original_row'],
                               'source_packet': ref, 'premises': common, 'actual_reader': READER,
                               'status': v['status'], 'qualification': 'Normal finite row only; no wholeWP45/callback/native/exception-order approval.', 'business': 'NOT_EXECUTED'})
reverse['utc'] = UTC
reverse['weather_formal_vectors'] = ref
reverse['atom_denominator_frozen_so_far'] = len(reverse['clauses'])
(P / 'reverse-mapping.json').write_text(json.dumps(reverse, ensure_ascii=False, indent=2) + '\n')
frozen = save_new('reverse-mapping.v19.frozen.json', reverse)
print(json.dumps({'utc': UTC, 'packet': ref, 'source_full': len(ledger['dependencies_full_read']), 'formal_full': len(ledger['formal_full_read']), 'reverse_current': len(reverse['clauses']), 'frozen_reverse': frozen}, ensure_ascii=False))
