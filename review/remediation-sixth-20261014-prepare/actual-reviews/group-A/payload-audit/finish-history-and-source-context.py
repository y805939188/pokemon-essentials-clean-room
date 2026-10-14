"""Finish exact case extraction and supplement source consumer metadata; never executes source."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

ROOT = Path('/workspace/pokemon-essentials-clean-room')
P = 'review/remediation-sixth-20261014-prepare'
OUT = ROOT / (P + '/actual-reviews/group-A/payload-audit')
H = OUT / 'historical-packets'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REFDB = '/tmp/r6-u01-r-reference.git'
SCRATCH = Path('/tmp/r6-actual-a-source-context')
SCRATCH.mkdir(exist_ok=True)
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
identity = lambda b: {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(), 'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}
commands = [json.loads(x) for x in (OUT / 'commands.jsonl').read_text().splitlines()]
checks = json.loads((OUT / 'checks.json').read_text())
receipts = json.loads((OUT / 'original-history-and-finite-packet-identities.json').read_text())

def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def capture(argv, source=False):
    begin = now()
    r = subprocess.run(argv, cwd=ROOT, capture_output=True)
    n = len(commands) + 1
    stdout = (SCRATCH if source else OUT / 'logs') / f'{n:04d}.stdout'
    stderr = OUT / 'logs' / f'{n:04d}.stderr'
    stdout.write_bytes(r.stdout)
    stderr.write_bytes(r.stderr)
    commands.append({'argv': argv, 'cwd': str(ROOT), 'utc_start': begin, 'utc_end': now(), 'exit_code': r.returncode,
                     'stdout_path': str(stdout), 'stderr_path': str(stderr), 'stdout_identity': identity(r.stdout),
                     'stderr_identity': identity(r.stderr), 'reference_behavior_execution': False})
    (OUT / 'commands.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in commands))
    assert r.returncode == 0, r.stderr
    return r.stdout

def check(name, good, detail):
    checks.append({'check': name, 'result': 'PASS_MECHANICAL' if good else 'FAIL_MECHANICAL', 'detail': detail})

def load_packet(name):
    return json.loads((H / name).read_bytes())

parsed = {(x['commit'], x['path']): json.loads(Path(x['local_full_body_path']).read_bytes())
          for x in receipts if x['path'].endswith('.json')}
u03_history = load_packet('U03-R-historical-review.json')
u03_input = load_packet('U03-C-historical-regression-input.json')
r2_binding = load_packet('U03-C-R2-B21-regression-binding.json')
r2_data = parsed[(r2_binding['commit'], r2_binding['path'])]
r2_index = next(i for i, x in enumerate(r2_data['cases']) if x['id'] == 'B21-CASE-DISPATCH')
r2_case = r2_data['cases'][r2_index]
closure_key = next(key for key in parsed if key[1].endswith('/closure-candidate.json'))
packet_key = next(key for key in parsed if key[1].endswith('/contracts/R5-U02/task-packet.json'))
closure_records = []
for record in u03_history['original_selected_candidate_records']:
    index = next(i for i, x in enumerate(parsed[closure_key]['records']) if x['id'] == record['id'])
    original = parsed[closure_key]['records'][index]
    closure_records.append({'commit': closure_key[0], 'path': closure_key[1], 'pointer': '/records/' + str(index),
                            'id': record['id'], 'complete_original_record': original, 'complete_review_record_equal': original == record})
packet_records = []
for record in u03_history['original_packet_records']:
    index = next(i for i, x in enumerate(parsed[packet_key]['findings']) if x['id'] == record['id'])
    original = parsed[packet_key]['findings'][index]
    packet_records.append({'commit': packet_key[0], 'path': packet_key[1], 'pointer': '/findings/' + str(index),
                           'id': record['id'], 'complete_original_record': original, 'complete_review_record_equal': original == record})
write('U03-verified-full-original-history-fields.json', {'scope_counts': u03_history['scope_counts'],
      'R2_original_binding': r2_binding, 'R2_actual_JSON_pointer': '/cases/' + str(r2_index),
      'R2_original_named_locator': r2_binding['semantic_read_pointer'], 'R2_complete_actual_original_case': r2_case,
      'R5_original_packet_records': packet_records, 'R5_closure_records': closure_records,
      'exact_prior_span_records': u03_input['relevant_file_spans'], 'immediate_interpreter_fishing_qualification': u03_input['immediate_interpreter_fishing_qualification'],
      'actual_activation_selection': u03_history['actual_activation_selection'], 'no_new_reference_execution': True})
fixture_key = next(key for key in parsed if key[1].endswith('/fishing-random-boundaries-results.json'))
image_key = next(key for key in parsed if key[1].endswith('/localized-image-matrix.json'))
newline_key = next(key for key in parsed if key[1].endswith('/newline-key-diagnostic.json'))
check('original_U03_seven_complete_fixture_records_located', isinstance(parsed[fixture_key], list) and len(parsed[fixture_key]) == 7,
      {'commit': fixture_key[0], 'path': fixture_key[1], 'cases': [x['case'] for x in parsed[fixture_key]], 'new_execution': 0})
check('original_U14_complete_48_image_and_three_newline_records_located', isinstance(parsed[image_key], list) and len(parsed[image_key]) == 48 and len(parsed[newline_key]) == 3,
      {'image_commit': image_key[0], 'image_path': image_key[1], 'image_records': len(parsed[image_key]),
       'newline_commit': newline_key[0], 'newline_path': newline_key[1], 'diagnostic_records': len(parsed[newline_key]), 'new_execution': 0})
finite = [r for r in receipts if any(role.startswith(('U03_original_seven', 'U03_original_counter', 'U14_original_diagnostic')) for role in r['roles'])]
write('finite-fixtures-binary-newline-image-locators.json', {'original_complete_packets': finite,
      'complete_seven_original_fixture_records': parsed[fixture_key], 'complete_48_original_image_matrix_records': parsed[image_key],
      'complete_three_original_newline_records': parsed[newline_key],
      'candidate_newline_byte_check': {'commit': '12a35f0d4635524ab2148c0979a1a4d69eeb982e',
        'path': P + '/candidates/R6-U14/evidence/newline-byte-validation.json', 'local_path': str(H / 'U14-C-newline-byte-validation.json'),
        'complete_payload': load_packet('U14-C-newline-byte-validation.json')},
      'U03_seven_original_counter_materials': load_packet('U03-R-original-evidence-binding.json')['seven_payloads'],
      'qualification': 'Original seven fixture execution remains historical evidence. This audit never executes the harness/reference. Matrix/membership does not certify host, pixels or all-language behavior.'})

# Only metadata/full hashes of explicitly identified original source consumers.
existing_sources = json.loads((OUT / 'source-fixed-original-identities.json').read_text())
existing_paths = {x['path'] for x in existing_sources}
u03_reads = load_packet('U03-C-reading-ledger.json')['reads']
extra = {x['path'] for x in u03_reads if x.get('commit') == REF and x.get('path', '').startswith('Data/Scripts/')}
extra |= {x['payload']['path'] for x in load_packet('U14-R-reading-and-independence.json')['root_source_context_reads']}
extra |= {'Data/Scripts/007_Objects and windows/001_RPG_Cache.rb',
          'Data/Scripts/007_Objects and windows/008_AnimatedBitmap.rb',
          'Data/Scripts/007_Objects and windows/011_Messages.rb',
          'Data/Scripts/001_Technical/006_RPG_Sprite.rb',
          'Data/Scripts/009_Scenes/002_EventScene.rb',
          'Data/Scripts/010_Data/002_PBS data/009_Species_files.rb',
          'Data/Scripts/010_Data/002_PBS data/015_Trainer.rb',
          'Data/Scripts/011_Battle/004_Scene/006_Battle_Scene_Objects.rb',
          'Data/Scripts/020_Debug/001_Editor screens/004_EditorScreens_SpritePositioning.rb',
          'Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb'}
frozen = json.loads((ROOT / (P + '/inputs/frozen-inputs.json')).read_bytes())
extra_rows = []
for path in sorted(extra - existing_paths):
    bound = next(x for x in frozen['source_materials'] if x['path'] == path)
    meta_raw = capture(['git', '--git-dir=' + REFDB, 'ls-tree', '-z', REF, '--', path]).split(b'\0')[0]
    meta, _ = meta_raw.split(b'\t')
    mode, kind, oid = meta.decode().split()
    body = capture(['git', '--git-dir=' + REFDB, 'show', REF + ':' + path], source=True)
    actual = identity(body)
    good = all(actual[k] == bound[k] for k in ['bytes', 'sha256', 'git_blob']) and mode == bound['mode'] and kind == 'blob' and oid == actual['git_blob']
    extra_rows.append({'path': path, 'reference_commit': REF, 'reference_tree': '7589c800b61ba13a13040ed0d686979b80a84fd0',
                       **actual, 'mode': mode, 'type': kind, 'all_identity_metadata_match': good,
                       'source_semantic_read_credit': False, 'source_reference_behavior_execution': 0,
                       'qualification': 'Identity of predecessor source consumers only; root decides relevance and semantics.'})
check('additional_identified_source_consumers_full_identity_metadata', all(x['all_identity_metadata_match'] for x in extra_rows),
      {'extra_consumer_paths': len(extra_rows), 'combined_source_metadata': len(existing_sources) + len(extra_rows)})
write('additional-source-consumer-identities.json', extra_rows)
status = capture(['git', 'status', '--porcelain', '--untracked-files=all']).decode().splitlines()
check('final_group_A_only_writes_and_no_tracked_modification', all(x.startswith('?? ') and x[3:].startswith(P + '/actual-reviews/group-A/') for x in status),
      {'files_seen': len(status), 'outside_group_A_or_tracked_changes': [x for x in status if not x.startswith('?? ') or not x[3:].startswith(P + '/actual-reviews/group-A/')]})
write('history-extraction-lookup-correction.json', {'utc': now(), 'initial_process_exit_code': 1,
      'error': "ValueError: invalid literal for int() with base 10: 'B21-CASE-DISPATCH'",
      'origin': 'Historical named /cases/B21-CASE-DISPATCH locator applied to actual list; complete case resolved by id at /cases/6.',
      'exact_initial_failure_UTC': 'UNVERIFIED_NOT_SEPARATELY_CAPTURED', 'corrected': True,
      'new_history_fetch_or_reference_execution_for_correction': 0, 'policy_or_admin_requirement_added': False})
write('checks.json', checks)
summary = json.loads((OUT / 'summary.json').read_text())
summary.update({'utc_end': now(), 'mechanical_check_count': len(checks), 'command_receipts': len(commands),
                'historical_packet_readbacks': 23, 'original_history_and_finite_packets': len(receipts),
                'verified_U14_original_qualification_fields': 118, 'verified_U14_original_case_fields': 78,
                'source_identity_payloads': len(existing_sources), 'additional_source_consumer_identity_payloads': len(extra_rows),
                'combined_source_identity_payloads': len(existing_sources) + len(extra_rows),
                'failed_checks': [x for x in checks if x['result'] != 'PASS_MECHANICAL'], 'remaining_blockers': []})
summary['result'] = 'PASS_MECHANICAL_INTEGRITY' if not summary['failed_checks'] else 'FAIL_MECHANICAL_INTEGRITY'
write('summary.json', summary)
print(json.dumps({'result': summary['result'], 'checks': len(checks), 'commands': len(commands),
                  'original_packets': len(receipts), 'source_metadata_total': summary['combined_source_identity_payloads'],
                  'failed': summary['failed_checks']}, ensure_ascii=False))
