"""Independent read-only identity checks. No project/author code is imported or run."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import difflib
import hashlib
import json
import re
import subprocess

ROOT = Path('/workspace/pokemon-essentials-clean-room')
BASE = Path('review/remediation-sixth-20261014-prepare')
OUT = ROOT / BASE / 'reviews/R6-U13-R/variants/identity-check'
FREEZE = '00b45de642f07cee9953e42f04cce9c35d77346f'
FREEZE_TREE = '6708f580d5a02f874a1a24a95d7c0649b10c393b'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
CORE = '5210b009db5191f307301115845e31475cd798ef'
REPORT = 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae'
IDS = ['GR6-F-V001', 'GR6-F-V002', 'GR6-F-V003', 'GR6-F-V004']
commands = []
cache = {}

def now():
    return datetime.now(timezone.utc).isoformat()

def digest(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest(),
            'lines': len(data.splitlines())}

def git(*args):
    argv = ['git', '--no-replace-objects', '--no-optional-locks', '-c', 'core.fsmonitor=false', *args]
    start = now()
    r = subprocess.run(argv, cwd=ROOT, capture_output=True, check=False)
    commands.append({'argv': argv, 'cwd': str(ROOT), 'start_utc': start, 'end_utc': now(),
                     'exit': r.returncode, 'stdout_bytes': len(r.stdout),
                     'stdout_sha256': hashlib.sha256(r.stdout).hexdigest(),
                     'stderr': r.stderr.decode('utf-8', errors='replace')})
    return r

def obj(commit, path):
    key = (commit, path)
    if key not in cache:
        r = git('show', commit + ':' + path)
        rec = {'commit': commit, 'path': path, 'read_exit': r.returncode,
               'error': r.stderr.decode('utf-8', errors='replace')}
        if r.returncode == 0:
            rec['actual'] = digest(r.stdout)
            t = git('ls-tree', '-z', commit, '--', path)
            entries = t.stdout.split(b'\0')
            for entry in entries:
                if entry and b'\t' in entry:
                    meta, name = entry.split(b'\t', 1)
                    mode, kind, blob = meta.decode().split()
                    if name.decode() == path:
                        rec['actual'].update(mode=mode, git_type=kind, tree_blob=blob)
            cache[key] = (r.stdout, rec)
        else:
            cache[key] = (None, rec)
    return cache[key]

def matches(expected, actual):
    keys = ['bytes', 'sha256', 'git_blob', 'lines', 'mode']
    return {k: actual.get(k) == expected[k] for k in keys
            if k in expected and (k != 'lines' or isinstance(expected[k], int))}

def check_object(expected):
    data, result = obj(expected['commit'], expected['path'])
    result = dict(result)
    result['expected'] = expected
    if data is not None:
        checks = matches(expected, result['actual'])
        checks['tree_blob_matches_content_blob'] = result['actual'].get('tree_blob') == result['actual']['git_blob']
        if expected.get('type') in ['blob', 'tree', 'commit', 'tag']:
            checks['declared_git_type'] = expected['type'] == result['actual'].get('git_type')
        elif 'type' in expected:
            try:
                data.decode('utf-8')
                text = b'\0' not in data
            except UnicodeDecodeError:
                text = False
            checks['declared_text_type'] = expected['type'] == ('text' if text else 'binary')
        result['checks'] = checks
        result['identity_pass'] = all(checks.values())
    else:
        result['identity_pass'] = False
    return result

def walk(v, pointer=''):
    yield pointer, v
    if isinstance(v, dict):
        for k, x in v.items():
            yield from walk(x, pointer + '/' + k.replace('~', '~0').replace('/', '~1'))
    elif isinstance(v, list):
        for i, x in enumerate(v):
            yield from walk(x, pointer + '/' + str(i))

def pointer_get(v, pointer):
    for k in pointer.split('/')[1:]:
        k = k.replace('~1', '/').replace('~0', '~')
        v = v[int(k)] if isinstance(v, list) else v[k]
    return v

def json_hashes(v):
    result = {}
    for ascii_flag in [False, True]:
        for sorted_flag in [False, True]:
            for compact in [False, True]:
                name = f'ensure_ascii={ascii_flag},sort_keys={sorted_flag},compact={compact}'
                args = {'ensure_ascii': ascii_flag, 'sort_keys': sorted_flag}
                if compact:
                    args['separators'] = (',', ':')
                result[name] = hashlib.sha256(json.dumps(v, **args).encode()).hexdigest()
    return result

started = now()
prompt_path = BASE / 'prompts/R6-U13-R.md'
contract_path = BASE / 'contracts/R6-U13.json'
prompt_data, prompt_object = obj(FREEZE, str(prompt_path))
contract_data, contract_object = obj(FREEZE, str(contract_path))
prompt = prompt_data.decode('utf-8')
blocks = re.findall(r'```json\n(.*?)\n```', prompt, re.S)
contract = json.loads(contract_data)
embedded_contract = json.loads(blocks[0])
recovery = json.loads(blocks[1])
index_data, index_object = obj(FREEZE, str(BASE / 'inputs/evidence/index.json'))
index = json.loads(index_data)
frozen_inputs_data, frozen_inputs_object = obj(FREEZE, str(BASE / 'inputs/frozen-inputs.json'))
frozen_inputs = json.loads(frozen_inputs_data)

bindings = []
for spec, expected in [('HEAD', FREEZE), ('HEAD^{tree}', FREEZE_TREE), (FREEZE + '^{tree}', FREEZE_TREE),
                       (MAIN + '^{tree}', '6ab3429170d2762607fbc2237014c3a160449fa1'),
                       (MAIN + ':deliverables/final-specification-set', '1046fbb657882e84b3dfc6d017943a9edf7782e5'),
                       (REF + '^{tree}', '7589c800b61ba13a13040ed0d686979b80a84fd0'),
                       (FREEZE + ':deliverables/final-specification-set', '1046fbb657882e84b3dfc6d017943a9edf7782e5')]:
    r = git('rev-parse', '--verify', spec)
    actual = r.stdout.decode().strip()
    bindings.append({'spec': spec, 'expected': expected, 'actual': actual, 'exit': r.returncode,
                     'pass': r.returncode == 0 and actual == expected})
origin = git('config', '--get', 'remote.origin.url')
reference_locations = [{'path': p, 'exists': Path(p).exists(),
                        'git_exists': (Path(p) / '.git').exists()}
                       for p in [str(ROOT / 'reference/pokemon-essentials'), '/workspace/pokemon-essentials-reference-r6']]

payload_rows = []
id_evidence = {}
for scope in contract['scope_contracts']:
    if scope['id'] not in IDS:
        continue
    id_evidence[scope['id']] = sorted({v for _, v in walk(scope) if isinstance(v, str) and v.startswith('EV-')})
    for pointer, value in walk(scope):
        if isinstance(value, dict) and isinstance(value.get('payload_identity'), dict):
            identity = value['payload_identity']
            check = check_object(identity)
            check.update(id=scope['id'], contract_pointer=pointer + '/payload_identity',
                         locator=value.get('locator'), payload_role=value.get('payload_role'))
            expected_tree = ('7589c800b61ba13a13040ed0d686979b80a84fd0' if identity['commit'] == REF
                             else '1046fbb657882e84b3dfc6d017943a9edf7782e5' if identity['commit'] == MAIN else None)
            check['declared_tree_pass'] = identity.get('tree') == expected_tree
            payload_rows.append(check)

common_rows = []
for ev, metadata in recovery.items():
    original_expected = dict(metadata)
    original_expected['path'] = REPORT + '/' + metadata['path']
    original = check_object(original_expected)
    local_path = BASE / 'inputs/evidence' / metadata['path']
    data, frozen_rec = obj(FREEZE, str(local_path))
    worktree = ROOT / local_path
    actual = digest(worktree.read_bytes()) if worktree.is_file() else None
    blob_result = git('cat-file', 'blob', metadata['git_blob'])
    blob_actual = digest(blob_result.stdout) if blob_result.returncode == 0 else None
    blob_checks = matches(metadata, blob_actual or {})
    row = {'evidence_id': ev, 'full_prompt_metadata': metadata, 'original_object': original,
           'declared_blob_recovery': {'exit': blob_result.returncode, 'actual': blob_actual,
                                      'checks': blob_checks, 'identity_pass': blob_result.returncode == 0 and all(blob_checks.values()),
                                      'path_binding': 'UNVERIFIED_IF_ORIGINAL_COMMIT_PATH_UNAVAILABLE'},
           'frozen_cache_object': frozen_rec, 'worktree_cache_actual': actual,
           'metadata_equals_index': all(index.get(ev, {}).get(k) == v for k, v in metadata.items()),
           'recovery_command_matches_metadata': metadata['recovery'] ==
               'git show ' + metadata['commit'] + ':' + REPORT + '/' + metadata['path'],
           'frozen_cache_checks': matches(metadata, frozen_rec.get('actual', {})),
           'worktree_cache_checks': matches(metadata, actual or {})}
    row['cache_identity_pass'] = data is not None and actual is not None and all(row['frozen_cache_checks'].values()) and all(row['worktree_cache_checks'].values())
    common_rows.append(row)

manifest_path = BASE / 'candidates/R6-U13/evidence/candidate-manifest.json'
manifest_data, manifest_object = obj(FREEZE, str(manifest_path))
manifest = json.loads(manifest_data)
manifest_rows = []
diffs = []
for entry in manifest:
    baseline = check_object({'commit': MAIN, 'path': entry['formal_path'], **entry['baseline']})
    candidate = check_object({'commit': FREEZE, 'path': entry['candidate_path'], **entry['candidate']})
    worktree_data = (ROOT / entry['candidate_path']).read_bytes()
    worktree_actual = digest(worktree_data)
    row = {'formal_path': entry['formal_path'], 'candidate_path': entry['candidate_path'],
           'baseline_object': baseline, 'candidate_object': candidate,
           'worktree_actual': worktree_actual, 'worktree_checks': matches(entry['candidate'], worktree_actual)}
    row['identity_pass'] = baseline['identity_pass'] and candidate['identity_pass'] and all(row['worktree_checks'].values())
    manifest_rows.append(row)
    baseline_data, _ = obj(MAIN, entry['formal_path'])
    candidate_data, _ = obj(FREEZE, entry['candidate_path'])
    diffs.extend(difflib.unified_diff(baseline_data.decode().splitlines(keepends=True),
                                    candidate_data.decode().splitlines(keepends=True),
                                    fromfile=MAIN + ':' + entry['formal_path'],
                                    tofile=FREEZE + ':' + entry['candidate_path']))

mirror_root = str(BASE / 'candidates/R6-U13/mirror') + '/'
t = git('ls-tree', '-rz', FREEZE, '--', mirror_root)
mirror_files = []
for entry in t.stdout.split(b'\0'):
    if entry:
        meta, path = entry.split(b'\t', 1)
        mode, kind, blob = meta.decode().split()
        path = path.decode()
        mirror_files.append({'path': path, 'formal_path': path[len(mirror_root):],
                             'mode': mode, 'type': kind, 'git_blob': blob})
allowed = set(contract['candidate_formal_paths'])
actual_paths = {x['formal_path'] for x in mirror_files}
manifest_paths = {x['formal_path'] for x in manifest}
scope_check = {'allowed_formal_paths': sorted(allowed), 'frozen_mirror_paths': mirror_files,
               'extra_mirror_paths': sorted(actual_paths - allowed),
               'missing_mirror_paths': sorted(allowed - actual_paths),
               'manifest_extra_paths': sorted(manifest_paths - allowed),
               'manifest_missing_paths': sorted(allowed - manifest_paths),
               'all_mirrors_changed_from_fixed_main': all(x['baseline']['git_blob'] != x['candidate']['git_blob'] for x in manifest),
               'whole_U13_scope_pass': actual_paths == allowed == manifest_paths,
               'V001_V004_write_union': sorted({p for x in contract['scope_contracts'] if x['id'] in IDS
                                              for p in x['minimum_revision_contract']['candidate_formal_write_set']})}

original_proposals = []
for path in [REPORT + '/tasks/R6-F/variants/findings.json', REPORT + '/findings/normative-records.json']:
    data, rec = obj(CORE, path)
    original_proposals.append(rec)
historical_core_objects = []
for object_id in [CORE, 'c0ff33024aea424c68d29f9778fe7c8e807d21e8']:
    r = git('cat-file', '-t', object_id)
    historical_core_objects.append({'object_id': object_id, 'exit': r.returncode,
                                    'type': r.stdout.decode().strip(),
                                    'error': r.stderr.decode('utf-8', errors='replace')})

hist_path = BASE / 'candidates/R6-U13/evidence/historical-regression.json'
hist_data, hist_object = obj(FREEZE, str(hist_path))
hist = json.loads(hist_data)
history_rows = []
hist_expected = {'commit': FREEZE, **hist['input']}
history_rows.append({'role': 'historical_regression_input_cache', 'check': check_object(hist_expected)})
hist_refs = {}
for pointer, value in walk(hist):
    if isinstance(value, dict) and isinstance(value.get('commit'), str) and isinstance(value.get('path'), str):
        hist_refs.setdefault((value['commit'], value['path'], value.get('git_blob')), []).append((pointer, value))
fixed_hist = hist['fixed_historical_files']
for name, value in fixed_hist['files'].items():
    expected = {'commit': fixed_hist['commit'], 'path': 'review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/' + name, **value}
    hist_refs.setdefault((expected['commit'], expected['path'], expected.get('git_blob')), []).append(('/fixed_historical_files/files/' + name, expected))

parsed_history = {}
for (commit, path, blob), refs in hist_refs.items():
    expected = refs[0][1]
    check = check_object(expected)
    data, _ = obj(commit, path)
    recovery_kind = 'COMMIT_PATH' if data is not None else 'UNAVAILABLE'
    if data is None and blob:
        r = git('cat-file', 'blob', blob)
        if r.returncode == 0:
            data = r.stdout
            actual = digest(data)
            check['blob_recovery_actual'] = actual
            check['blob_recovery_checks'] = matches(expected, actual)
            check['blob_identity_pass'] = all(check['blob_recovery_checks'].values())
            recovery_kind = 'DECLARED_BLOB_ONLY_PATH_BINDING_UNVERIFIED'
        else:
            check['blob_recovery_error'] = r.stderr.decode('utf-8', errors='replace')
    pointer_checks = []
    if data is not None:
        try:
            parsed = json.loads(data)
            parsed_history[(commit, path, blob)] = parsed
            for location, ref in refs:
                if isinstance(ref.get('pointer'), str):
                    pr = {'author_evidence_pointer': location, 'declared_pointer': ref['pointer']}
                    try:
                        target = pointer_get(parsed, ref['pointer'])
                        pr['pointer_resolves'] = True
                        if 'record_sha256' in ref:
                            variants = json_hashes(target)
                            pr['declared_record_sha256'] = ref['record_sha256']
                            pr['matching_json_serializations'] = [k for k, h in variants.items() if h == ref['record_sha256']]
                            pr['record_digest_pass'] = bool(pr['matching_json_serializations'])
                    except (KeyError, IndexError, ValueError, TypeError) as e:
                        pr.update(pointer_resolves=False, error=str(e))
                    pointer_checks.append(pr)
        except (json.JSONDecodeError, UnicodeDecodeError):
            check['json_parse'] = 'UNAVAILABLE_NON_JSON'
    history_rows.append({'role': 'historical_declared_binding', 'author_evidence_locations': [x[0] for x in refs],
                         'recovery_kind': recovery_kind, 'check': check, 'pointer_checks': pointer_checks})

hist_blob_rows = []
for pointer, value in walk(hist):
    if isinstance(value, dict) and 'binding_blob' in value and 'bytes' in value and 'sha256' in value:
        blob = value['binding_blob']
        r = git('cat-file', 'blob', blob)
        result = {'author_evidence_pointer': pointer, 'binding_blob': blob, 'exit': r.returncode,
                  'expected': {k: value[k] for k in ['bytes', 'sha256', 'git_blob', 'pointer'] if k in value}}
        if r.returncode == 0:
            result['actual'] = digest(r.stdout)
            result['checks'] = matches(value, result['actual'])
            result['identity_pass'] = all(result['checks'].values())
            try:
                target = pointer_get(json.loads(r.stdout), value['pointer'])
                result['declared_pointer_resolves'] = True
                if 'qualified_scope' in value and isinstance(target, dict):
                    result['qualified_scope_equal_to_original_full_record'] = value['qualified_scope'] == target
                    result['qualified_scope_is_exact_projection'] = all(target.get(k) == v for k, v in value['qualified_scope'].items())
            except (KeyError, IndexError, ValueError, TypeError) as e:
                result['pointer_error'] = str(e)
        else:
            result['error'] = r.stderr.decode('utf-8', errors='replace')
        hist_blob_rows.append(result)

summary = {
    'contract_prompt_structure_equal': contract == embedded_contract,
    'bindings_pass': all(x['pass'] for x in bindings),
    'payload_identity_occurrences': len(payload_rows),
    'payload_unique_commit_paths': len({(x['commit'], x['path']) for x in payload_rows}),
    'payload_failures': [x for x in payload_rows if not x['identity_pass'] or not x['declared_tree_pass']],
    'common_metadata_entries': len(common_rows),
    'common_cache_pass_count': sum(x['cache_identity_pass'] for x in common_rows),
    'common_original_object_pass_count': sum(x['original_object']['identity_pass'] for x in common_rows),
    'common_declared_blob_pass_count': sum(x['declared_blob_recovery']['identity_pass'] for x in common_rows),
    'common_index_equal_count': sum(x['metadata_equals_index'] for x in common_rows),
    'manifest_entries': len(manifest_rows),
    'manifest_pass_count': sum(x['identity_pass'] for x in manifest_rows),
    'mirror_scope_pass': scope_check['whole_U13_scope_pass'],
    'history_binding_rows': len(history_rows),
    'history_recovery_kinds': dict(Counter(x.get('recovery_kind', 'CACHE') for x in history_rows)),
    'history_binding_blob_rows': len(hist_blob_rows),
    'history_binding_blob_identity_pass_count': sum(x.get('identity_pass', False) for x in hist_blob_rows),
    'historical_cache_payload_pass': history_rows[0]['check']['identity_pass'],
    'historical_readable_binding_mismatches': [x for x in history_rows if x['check']['read_exit'] == 0 and not x['check']['identity_pass']],
    'semantic_read_or_behavioral_verdict': 'NOT_PERFORMED_BY_IDENTITY_CHECK; hashes/JSON parsing do not establish semantic PASS',
}
result = {'task': '/root/variants/identity_check', 'started_utc': started, 'completed_utc': now(),
          'cwd': str(ROOT), 'freeze_commit': FREEZE, 'freeze_tree': FREEZE_TREE,
          'write_allowlist': str(OUT), 'requested_configuration': contract['reviewer'],
          'actual_configuration': dict.fromkeys(['model', 'effort', 'tier', 'speed', 'uuid'], 'UNVERIFIED'),
          'configuration_obstacle': 'No effective platform configuration echo was available; no CLI probe was run.',
          'reference_locations': reference_locations,
          'reference_objects_available_in_project_database': all(x['pass'] for x in bindings if x['spec'].startswith(REF)),
          'project_origin': origin.stdout.decode().strip(), 'fixed_bindings': bindings,
          'input_object_identities': {'prompt': prompt_object, 'contract': contract_object,
                                      'evidence_index': index_object, 'frozen_inputs': frozen_inputs_object,
                                      'candidate_manifest': manifest_object, 'author_historical_evidence': hist_object},
          'summary': summary, 'per_ID_counter_evidence_ids': id_evidence,
          'contract_payload_identity_checks': payload_rows, 'full_common_recovery_metadata_checks': common_rows,
          'candidate_manifest_payload_checks': manifest_rows, 'mirror_difference_scope': scope_check,
          'original_proposal_object_recovery': original_proposals,
          'historical_core_object_availability': historical_core_objects,
          'historical_qualification_identity_checks': history_rows,
          'historical_R5_declared_blob_checks': hist_blob_rows,
          'command_receipts': commands,
          'scope_limits': ['No branch switch, commit, author script, CLI probe, reference execution, source/formal/candidate edits.',
                           'Hash identity is separate from new semantic reading and historical behavioral regression.',
                           'Missing source worktree is recorded; immutable R objects are read through the project object database.',
                           'Declared-blob recovery cannot independently establish an unavailable commit/path association.']}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'identity-check.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
(OUT / 'fixed-main-to-candidate.diff').write_text(''.join(diffs))
print(json.dumps(summary, ensure_ascii=False, indent=2))
print('deliverable', str(OUT / 'identity-check.json'))
print('deliverable', str(OUT / 'fixed-main-to-candidate.diff'))
