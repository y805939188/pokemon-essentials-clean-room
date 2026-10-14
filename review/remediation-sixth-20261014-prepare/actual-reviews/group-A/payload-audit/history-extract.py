"""Verify exact historical JSON pointers and locate finite original evidence; no semantic verdict."""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import subprocess
import urllib.parse
import urllib.request

ROOT = Path('/workspace/pokemon-essentials-clean-room')
P = 'review/remediation-sixth-20261014-prepare'
OUT = ROOT / (P + '/actual-reviews/group-A/payload-audit')
H = OUT / 'historical-packets'
DB = '/tmp/r6-actual-a-payload-20261014.git'
REMOTE = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
TEMP = Path('/tmp/r6-actual-a-original-history')
TEMP.mkdir(exist_ok=True)
ORIG = OUT / 'original-finite-evidence'
ORIG.mkdir(exist_ok=True)
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
identity = lambda b: {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(), 'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}
commands = [json.loads(x) for x in (OUT / 'commands.jsonl').read_text().splitlines()]
checks = json.loads((OUT / 'checks.json').read_text())
start = now()

def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def capture(argv):
    begin = now()
    r = subprocess.run(argv, cwd=ROOT, capture_output=True)
    n = len(commands) + 1
    stdout = OUT / 'logs' / f'{n:04d}.stdout'
    stderr = OUT / 'logs' / f'{n:04d}.stderr'
    stdout.write_bytes(r.stdout)
    stderr.write_bytes(r.stderr)
    commands.append({'argv': argv, 'cwd': str(ROOT), 'utc_start': begin, 'utc_end': now(), 'exit_code': r.returncode,
                     'stdout_path': str(stdout), 'stderr_path': str(stderr), 'stdout_identity': identity(r.stdout),
                     'stderr_identity': identity(r.stderr), 'reference_behavior_execution': False})
    (OUT / 'commands.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in commands))
    assert r.returncode == 0, r.stderr
    return r.stdout

def check(name, okay, detail):
    checks.append({'check': name, 'result': 'PASS_MECHANICAL' if okay else 'FAIL_MECHANICAL', 'detail': detail})
    write('checks.json', checks)
    if not okay:
        print('MECHANICAL_DIFFERENCE', name, flush=True)

def load(name):
    return json.loads((H / name).read_bytes())

qualified = load('U14-C-historical-qualified-spans.json')
premises = load('U14-C-historical-case-premises.json')
u03_history_readback = load('U03-R-historical-readback.json')
u03_history = load('U03-R-historical-review.json')
u03_input = load('U03-C-historical-regression-input.json')
u03_r2 = load('U03-C-R2-B21-regression-binding.json')
u03_seven = load('U03-R-original-evidence-binding.json')['seven_payloads']
u03_reads = load('U03-C-reading-ledger.json')['reads']
u14_reads = load('U14-R-reading-and-independence.json')
jobs = {}
def register(item, role):
    key = (item.get('commit', item.get('ref', item.get('origin_commit'))), item.get('path'))
    if key not in jobs:
        jobs[key] = {'commit': key[0], 'path': key[1], 'expected': {k: item[k] for k in ['bytes', 'sha256', 'git_blob'] if k in item}, 'roles': []}
    jobs[key]['roles'].append(role)
for item in qualified['records']:
    register(item['payload'], 'U14_exact_qualification_original')
for item in u03_history_readback:
    register(item, 'U03_original_history_packet')
register(u03_r2, 'U03_R2_selected_complete_case')
for item in u03_reads:
    if 'fishing-random-boundaries' in item.get('path', ''):
        register(item, 'U03_original_seven_fixture')
for item in u14_reads['original_reports_and_diagnostics']:
    register(item, 'U14_original_diagnostic_or_report')
for item in u03_seven:
    register(dict(item, commit=item['origin_commit'], path=item['origin_path']), 'U03_original_counter_material')
commits = sorted({x['commit'] for x in jobs.values()})
capture(['git', '--git-dir=' + DB, 'fetch', '--depth=1', '--filter=blob:none', REMOTE, *commits])
for item in jobs.values():
    entry = capture(['git', '--git-dir=' + DB, 'ls-tree', '-r', '-z', item['commit'], '--', item['path']]).split(b'\0')[0]
    meta, path = entry.split(b'\t')
    mode, kind, oid = meta.decode().split()
    item['tree_metadata'] = {'mode': mode, 'type': kind, 'git_blob': oid}

def fetch(item):
    begin = now()
    cache = Path('/tmp/r6-u01-r-history') / Path(item['path']).name
    body = cache.read_bytes() if cache.exists() else None
    attempts = []
    if body is not None:
        actual = identity(body)
        valid = all(actual[k] == v for k, v in item['expected'].items()) and actual['git_blob'] == item['tree_metadata']['git_blob']
        attempts.append({'method': 'REUSE_COMPLETE_IDENTICAL_PAYLOAD', 'UTC_start': begin, 'UTC_end': now(),
                         'path': str(cache), 'exit_code': 0 if valid else 1, 'identity': actual})
        if not valid:
            body = None
    url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + item['commit'] + '/' + urllib.parse.quote(item['path'], safe='/')
    if body is None:
        for n in range(1, 4):
            begin = now()
            try:
                with urllib.request.urlopen(url, timeout=25) as response:
                    full = response.read()
                    status = response.status
                actual = identity(full)
                valid = all(actual[k] == v for k, v in item['expected'].items()) and actual['git_blob'] == item['tree_metadata']['git_blob']
                attempts.append({'method': 'FULL_FIXED_URL_READBACK', 'attempt': n, 'url': url, 'UTC_start': begin,
                                 'UTC_end': now(), 'HTTP_status': status, 'exit_code': 0 if valid else 1, 'identity': actual})
                if valid:
                    body = full
                    break
            except Exception as ex:
                attempts.append({'attempt': n, 'UTC_start': begin, 'UTC_end': now(), 'exit_code': 1, 'error': repr(ex)})
    if body is not None:
        actual = identity(body)
        archive = TEMP / actual['git_blob']
        archive.write_bytes(body)
        if any(role.startswith(('U03_original_seven', 'U03_original_counter', 'U14_original_diagnostic')) for role in item['roles']):
            target = ORIG / (('U03-' if any(r.startswith('U03') for r in item['roles']) else 'U14-') + Path(item['path']).name)
            target.write_bytes(body)
        else:
            target = archive
    else:
        actual = None
        target = None
    return (item['commit'], item['path']), body, dict(item, attempts=attempts, complete_identity=actual,
                                                   local_full_body_path=str(target), full_body_verified=body is not None,
                                                   behavior_execution=0)
bodies = {}
receipts = []
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    for key, body, receipt in pool.map(fetch, jobs.values()):
        bodies[key] = body
        receipts.append(receipt)
write('original-history-and-finite-packet-identities.json', receipts)
check('all_original_history_and_finite_packets_full_identity', all(b is not None for b in bodies.values()),
      {'packets': len(receipts), 'reused_three_complete_original_payloads': [r['path'] for r in receipts if r['attempts'][0]['method'].startswith('REUSE')]})
assert all(b is not None for b in bodies.values())
parsed = {key: json.loads(body) for key, body in bodies.items() if key[1].endswith('.json')}
def pointer(value, path):
    if not path:
        return value
    for token in path.lstrip('/').split('/'):
        token = token.replace('~1', '/').replace('~0', '~')
        if isinstance(value, list):
            value = value[int(token)] if token.isdigit() else next(x for x in value if x.get('id') == token)
        else:
            value = value[token]
    return value
verified_fields = []
for item in qualified['records']:
    original = parsed[(item['payload']['commit'], item['payload']['path'])]
    actual = pointer(original, item['pointer'])
    verified_fields.append(dict(item, independent_original_pointer_value=actual, complete_field_equal=(actual == item['value']),
                                scope='Qualification extraction only; no new semantic PASS or acceptance transfer.'))
check('all_118_U14_exact_original_qualification_fields', len(verified_fields) == 118 and all(x['complete_field_equal'] for x in verified_fields), len(verified_fields))
write('U14-verified-full-original-qualification-fields.json', {'scope': qualified['scope'], 'records': verified_fields})
verified_premises = []
for item in premises:
    actual = pointer(parsed[(item['commit'], item['path'])], item['pointer'])
    verified_premises.append(dict(item, independent_original_pointer_value=actual, complete_field_equal=(actual == item['value'])))
check('all_78_U14_original_case_premise_fields', len(verified_premises) == 78 and all(x['complete_field_equal'] for x in verified_premises), len(verified_premises))
write('U14-verified-full-original-case-fields.json', verified_premises)
closure_key = next(key for key in parsed if key[1].endswith('/closure-candidate.json'))
closure = parsed[closure_key]
closure_records = []
for record in u03_history['original_selected_candidate_records']:
    index = next(i for i, x in enumerate(closure['records']) if x['id'] == record['id'])
    original = closure['records'][index]
    closure_records.append({'commit': closure_key[0], 'path': closure_key[1], 'pointer': '/records/' + str(index),
                            'id': record['id'], 'complete_original_record': original, 'complete_review_record_equal': original == record})
check('U03_selected_original_closure_records_are_complete', all(x['complete_review_record_equal'] for x in closure_records),
      [x['id'] for x in closure_records])
packet_key = next(key for key in parsed if key[1].endswith('/contracts/R5-U02/task-packet.json'))
packet = parsed[packet_key]
original_packet_records = []
for record in u03_history['original_packet_records']:
    index = next(i for i, x in enumerate(packet['findings']) if x['id'] == record['id'])
    original = packet['findings'][index]
    original_packet_records.append({'commit': packet_key[0], 'path': packet_key[1], 'pointer': '/findings/' + str(index),
                                    'id': record['id'], 'complete_original_record': original, 'complete_review_record_equal': original == record})
check('U03_original_R5_packet_records_are_complete', all(x['complete_review_record_equal'] for x in original_packet_records),
      [x['id'] for x in original_packet_records])
r2_case = pointer(parsed[(u03_r2['commit'], u03_r2['path'])], u03_r2['semantic_read_pointer'])
write('U03-verified-full-original-history-fields.json', {'scope_counts': u03_history['scope_counts'],
      'R2_original_binding': u03_r2, 'R2_complete_actual_original_case': r2_case,
      'R5_original_packet_records': original_packet_records, 'R5_closure_records': closure_records,
      'exact_prior_span_records': u03_input['relevant_file_spans'], 'immediate_interpreter_fishing_qualification': u03_input['immediate_interpreter_fishing_qualification'],
      'actual_activation_selection': u03_history['actual_activation_selection'], 'no_new_reference_execution': True})
finite = [r for r in receipts if any(role.startswith(('U03_original_seven', 'U03_original_counter', 'U14_original_diagnostic')) for role in r['roles'])]
write('finite-fixtures-binary-newline-image-locators.json', {'original_complete_packets': finite,
      'candidate_newline_byte_check': {'commit': '12a35f0d4635524ab2148c0979a1a4d69eeb982e',
        'path': P + '/candidates/R6-U14/evidence/newline-byte-validation.json',
        'local_path': str(H / 'U14-C-newline-byte-validation.json'), 'complete_payload': load('U14-C-newline-byte-validation.json')},
      'U03_seven_original_counter_materials': u03_seven,
      'qualification': 'Original seven fixture execution remains historical evidence. No fixture/harness/reference code is executed by this audit; finite membership/matrix metadata is not host or all-language certification.'})
summary = json.loads((OUT / 'summary.json').read_text())
summary.update({'utc_end': now(), 'mechanical_check_count': len(checks), 'command_receipts': len(commands),
                'historical_packet_readbacks': 23, 'original_history_and_finite_packets': len(receipts),
                'verified_U14_original_qualification_fields': len(verified_fields), 'verified_U14_original_case_fields': len(verified_premises),
                'failed_checks': [c for c in checks if c['result'] != 'PASS_MECHANICAL']})
summary['result'] = 'PASS_MECHANICAL_INTEGRITY' if not summary['failed_checks'] else 'FAIL_MECHANICAL_INTEGRITY'
write('summary.json', summary)
print(json.dumps({'result': summary['result'], 'original_packets': len(receipts), 'verified_qualification_fields': len(verified_fields),
                  'verified_case_fields': len(verified_premises), 'checks': len(checks), 'commands': len(commands), 'failed': summary['failed_checks']}, ensure_ascii=False))
