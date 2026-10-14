"""Finite group-A composition/identity audit; never executes reference or author tools."""
from pathlib import Path
import concurrent.futures
import datetime
import difflib
import hashlib
import json
import subprocess
import urllib.parse
import urllib.request

ROOT = Path('/workspace/pokemon-essentials-clean-room')
P = 'review/remediation-sixth-20261014-prepare'
OUT = ROOT / (P + '/actual-reviews/group-A/payload-audit')
ACTUAL = '86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
TREE = '67e8c55d520fa8cad2928cb4b95e24c3ed602d5a'
FORMAL = 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REF_TREE = '7589c800b61ba13a13040ed0d686979b80a84fd0'
INPUT = P + '/integration/U01-U14-final-composite-20261014/actual-review-input.json'
GROUP = ['R6-U01', 'R6-U03', 'R6-U14']
REMOTE = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
DB = Path('/tmp/r6-actual-a-payload-20261014.git')
REFDB = Path('/tmp/r6-u01-r-reference.git')
SCRATCH = Path('/tmp/r6-actual-a-payload-20261014-bodies')
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'logs').mkdir(exist_ok=True)
SCRATCH.mkdir(exist_ok=True)
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
START = now()
commands = []
checks = []

def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}

def matches(actual, declared):
    return all(actual[k] == declared[k] for k in ['bytes', 'sha256', 'git_blob'])

def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def capture(argv, reference_payload=False, ok=(0,), input_bytes=None):
    begin = now()
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, input=input_bytes)
    n = len(commands) + 1
    stdout = ((SCRATCH if reference_payload else OUT / 'logs') / f'{n:04d}.stdout')
    stderr = OUT / 'logs' / f'{n:04d}.stderr'
    stdout.write_bytes(result.stdout)
    stderr.write_bytes(result.stderr)
    commands.append({'argv': argv, 'cwd': str(ROOT), 'utc_start': begin, 'utc_end': now(),
                     'exit_code': result.returncode, 'stdout_path': str(stdout), 'stderr_path': str(stderr),
                     'stdout_identity': identity(result.stdout), 'stderr_identity': identity(result.stderr),
                     'reference_payload_archive': 'temporary read-only payload, no reference execution' if reference_payload else None,
                     'reference_behavior_execution': False,
                     'stdin_identity': identity(input_bytes) if input_bytes is not None else None})
    (OUT / 'commands.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in commands))
    if result.returncode not in ok:
        raise RuntimeError({'argv': argv, 'exit_code': result.returncode,
                            'stderr': result.stderr.decode(errors='replace')})
    return result.stdout

def git(*args):
    return capture(['git', *args])

def remote_git(*args):
    return capture(['git', '--git-dir=' + str(DB), *args])

def ref_git(*args, reference_payload=False):
    return capture(['git', '--git-dir=' + str(REFDB), *args], reference_payload=reference_payload)

def blob(commit, path):
    return git('show', commit + ':' + path)

def parse_tree(raw):
    rows = []
    for entry in raw.split(b'\0'):
        if entry:
            meta, path = entry.split(b'\t', 1)
            mode, kind, oid = meta.decode().split()
            rows.append({'path': path.decode(), 'mode': mode, 'type': kind, 'oid': oid})
    return rows

def local_entries(commit, path=''):
    return parse_tree(git('ls-tree', '-r', '-z', commit, '--', path))

def remote_entries(commit, path=''):
    return parse_tree(remote_git('ls-tree', '-r', '-z', commit, '--', path))

def check(name, condition, detail=None):
    checks.append({'check': name, 'result': 'PASS_MECHANICAL' if condition else 'FAIL_MECHANICAL', 'detail': detail})
    write('checks.json', checks)
    if not condition:
        print('MECHANICAL_DIFFERENCE', name, json.dumps(detail, ensure_ascii=False), flush=True)

try:
    head_start = git('rev-parse', 'HEAD').decode().strip()
    branch_start = git('branch', '--show-current').decode().strip()
    refs_start = git('show-ref').decode()
    check('frozen_HEAD_and_review_branch', head_start == ACTUAL and branch_start == 'codex/remediation-sixth-actual-a-20261014',
          {'HEAD': head_start, 'branch': branch_start})
    check('actual_whole_tree_and_formal_tree', git('rev-parse', ACTUAL + '^{tree}').decode().strip() == TREE and
          git('rev-parse', ACTUAL + ':deliverables/final-specification-set').decode().strip() == FORMAL,
          {'whole_tree': TREE, 'formal_tree': FORMAL})
    check('root_AGENTS_preserved', blob(ACTUAL, 'AGENTS.md') == blob(PREP, 'AGENTS.md'))
    input_bytes = blob(ACTUAL, INPUT)
    data = json.loads(input_bytes)
    check('actual_review_input_full_local_body_binding', input_bytes == (ROOT / INPUT).read_bytes() and
          identity(input_bytes)['git_blob'] == local_entries(ACTUAL, INPUT)[0]['oid'], identity(input_bytes))
    check('actual_input_fixed_refs_and_nonacceptance', data['fixed_main'] == MAIN and data['preparation_commit'] == PREP and
          data['fixed_reference_commit'] == REF and data['fixed_reference_tree'] == REF_TREE and
          data['INTEGRATED_PASS'] is None and data['formal_acceptance'] is None and data['CLOSED'] is False and
          data['new_source_execution'] == data['new_independent_behavior_model_execution'] == data['host_Demo_real_save_execution'] == 0,
          {k: data[k] for k in ['fixed_main', 'fixed_reference_commit', 'fixed_reference_tree', 'INTEGRATED_PASS',
                              'formal_acceptance', 'CLOSED', 'new_source_execution', 'new_independent_behavior_model_execution', 'host_Demo_real_save_execution']})
    batches = [x for x in data['batches'] if x['batch'] in GROUP]
    contracts = {}
    ids = []
    for batch in batches:
        contract_bytes = blob(ACTUAL, batch['contract_path'])
        contract = json.loads(contract_bytes)
        contracts[batch['batch']] = contract
        ids.extend(contract['required_ids'])
        check('complete_contract_identity:' + batch['batch'], matches(identity(contract_bytes), batch['contract_identity']) and
              contract_bytes == blob(PREP, batch['contract_path']) and contract['required_ids'] == batch['required_ids'] and
              contract['required_ids'] == [x['id'] for x in contract['scope_contracts']] and
              contract['candidate_formal_paths'] == batch['all_candidate_allowlist_paths'],
              {'identity': identity(contract_bytes), 'required_ids': contract['required_ids'], 'paths': contract['candidate_formal_paths']})
    group_paths = sorted({p for c in contracts.values() for p in c['candidate_formal_paths']})
    file_rows = [x for x in data['files'] if x['path'] in group_paths]
    unchanged = [x for x in data['unchanged_prospective_paths'] if x['path'] in group_paths]
    check('exact_11_ID_and_22_file_scope', len(ids) == len(set(ids)) == 11 and len(group_paths) == 22 and
          len(file_rows) == 21 and len(unchanged) == 1 and set(ids) <= set(data['required_ids']),
          {'ids': ids, 'paths': group_paths, 'changed_file_records': len(file_rows), 'unchanged': unchanged})
    extraction = {'actual_commit': ACTUAL, 'actual_whole_tree': TREE, 'actual_formal_tree': FORMAL,
                  'input_path': INPUT, 'input_identity': identity(input_bytes), 'group': GROUP, 'required_ids': ids,
                  'batches': batches, 'files': file_rows, 'unchanged_prospective_paths': unchanged,
                  'resolutions': [x for x in data['resolutions'] if x['path'] in group_paths],
                  'root_edits': [x for x in data['root_edits'] if x['path'] in group_paths],
                  'review_requirements': data['review_requirements'], 'reading_qualification': data['reading_qualification'],
                  'file_stability_qualification': data['file_stability_qualification'],
                  'administrative_sync': data['administrative_sync'],
                  'per_ID_original_seven_groups': [dict(batch=u, **s) for u, c in contracts.items() for s in c['scope_contracts']]}
    write('actual-input-group-A-extraction.json', extraction)

    # Fixed final formal scope is audited across all 53 modified files, including A's 21.
    formal_delta = git('diff', '--name-status', MAIN, ACTUAL, '--', 'deliverables/final-specification-set').decode().splitlines()
    actual_changed = [x.split('\t')[1] for x in formal_delta]
    check('actual_global_formal_scope_is_exact_53_input_files', len(actual_changed) == 53 and
          set(actual_changed) == {x['path'] for x in data['files']} and all(x.startswith('M\t') for x in formal_delta), formal_delta)
    prior = data['pre_integration_commit']
    prior_delta = git('diff', '--name-only', prior, ACTUAL, '--', 'deliverables/final-specification-set').decode().splitlines()
    check('prior_actual_delta_metadata_complete', set(prior_delta) ==
          {x['path'] for x in data['delta_from_prior_actual']['changed_formal_paths']} and len(prior_delta) == 8,
          {'paths': prior_delta, 'metadata': data['delta_from_prior_actual']})
    check('all_group_A_full_files_unchanged_from_prior_actual', not (set(prior_delta) & set(group_paths)),
          {'intersection': sorted(set(prior_delta) & set(group_paths)), 'qualification': 'Byte stability does not substitute direct final semantic review.'})
    global_ids = []
    for item in data['files']:
        original = blob(MAIN, item['path'])
        current = blob(ACTUAL, item['path'])
        previous = blob(prior, item['path'])
        meta = local_entries(ACTUAL, item['path'])[0]
        good = (matches(identity(original), item['baseline']) and matches(identity(current), item['actual']) and
                matches(identity(previous), item['previous_actual']) and meta['mode'] == item['mode'] == '100644' and
                meta['type'] == item['type'] == 'blob' and meta['oid'] == identity(current)['git_blob'])
        global_ids.append({'path': item['path'], 'baseline': identity(original), 'previous_actual': identity(previous),
                           'actual': identity(current), 'mode': meta['mode'], 'type': meta['type'], 'full_metadata_match': good})
    check('all_53_formal_baseline_previous_actual_metadata', all(x['full_metadata_match'] for x in global_ids))
    write('whole-formal-scope-and-identities.json', {'global_changed_paths': actual_changed, 'files': global_ids})

    # Fetch only into a fresh independent database. Project refs remain untouched.
    relevant_contributions = [c for f in file_rows for c in f['contributions']]
    contributing_batches = {x['batch'] for x in relevant_contributions} | set(GROUP)
    all_batches = {x['batch']: x for x in data['batches']}
    fetch_commits = {ACTUAL} | {all_batches[u]['candidate_published_commit'] for u in contributing_batches} | {
        x['independent_review']['review_commit'] for x in batches}
    check('fresh_independent_database_absent', not DB.exists(), str(DB))
    if DB.exists():
        raise RuntimeError('Independent object store already exists; choose another fresh path.')
    capture(['git', 'init', '--bare', str(DB)])
    remote_git('fetch', '--depth=1', '--filter=blob:none', REMOTE, *sorted(fetch_commits))
    check('fresh_remote_actual_tree', remote_git('rev-parse', ACTUAL + '^{tree}').decode().strip() == TREE and
          remote_git('rev-parse', ACTUAL + ':deliverables/final-specification-set').decode().strip() == FORMAL and
          not (DB / 'objects/info/alternates').exists(), {'remote': REMOTE, 'commits_fetched': sorted(fetch_commits)})
    tree_bindings = []
    candidate_trees = {}
    for u in sorted(contributing_batches):
        batch = all_batches[u]
        commit = batch['candidate_published_commit']
        mirror = P + '/candidates/' + u + '/mirror'
        workspace_tree = remote_git('rev-parse', commit + '^{tree}').decode().strip()
        mirror_tree = remote_git('rev-parse', commit + ':' + mirror).decode().strip()
        rows = remote_entries(commit, mirror)
        candidate_trees[u] = {x['path']: x for x in rows}
        check('candidate_complete_workspace_and_mirror_tree:' + u, workspace_tree == batch['candidate_workspace_tree'] and
              mirror_tree == batch['candidate_mirror_tree'] and {x['path'][len(mirror) + 1:] for x in rows} ==
              set(batch['all_candidate_allowlist_paths']), {'workspace_tree': workspace_tree, 'mirror_tree': mirror_tree, 'files': len(rows)})
        tree_bindings.append({'batch': u, 'candidate_commit': commit, 'workspace_tree': workspace_tree,
                              'mirror_tree': mirror_tree, 'all_mirror_entries': rows})
    for batch in batches:
        review = batch['independent_review']
        rcommit = review['review_commit']
        report_dir = str(Path(review['report_path']).parent)
        rtree = remote_git('rev-parse', rcommit + '^{tree}').decode().strip()
        d_tree = remote_git('rev-parse', rcommit + ':' + report_dir).decode().strip()
        check('review_commit_directory_tree_binding:' + batch['batch'], rtree == review['review_workspace_tree'] and
              d_tree == review['review_directory_tree'] and review['candidate_published_commit'] == batch['candidate_published_commit'] and
              review['mirror_tree'] == batch['candidate_mirror_tree'] and review['scope_ids'] == batch['required_ids'],
              {'review_commit': rcommit, 'workspace_tree': rtree, 'report_directory_tree': d_tree})
        report_entry = remote_entries(rcommit, review['report_path'])[0]
        check('review_report_path_mode_type_blob_binding:' + batch['batch'], report_entry['oid'] == review['report_identity']['git_blob'] and
              report_entry['mode'] == '100644' and report_entry['type'] == 'blob', report_entry)
    write('candidate-and-review-complete-tree-bindings.json', tree_bindings)

    # Full raw readback: input, three contracts/reports, all 22 actual formal files,
    # all 26 A mirrors, and every other candidate contribution to A's shared files.
    jobs = {}
    def job(commit, path, expected=None, role=None):
        key = (commit, path)
        if key not in jobs:
            jobs[key] = {'commit': commit, 'path': path, 'expected': expected, 'roles': []}
        if expected is not None:
            jobs[key]['expected'] = expected
        if role is not None:
            jobs[key]['roles'].append(role)
    job(ACTUAL, INPUT, identity(input_bytes), 'final_actual_input')
    for batch in batches:
        job(ACTUAL, batch['contract_path'], batch['contract_identity'], 'complete_group_contract')
        review = batch['independent_review']
        job(review['review_commit'], review['report_path'], review['report_identity'], 'complete_original_independent_report')
        for path in batch['all_candidate_allowlist_paths']:
            mirror = P + '/candidates/' + batch['batch'] + '/mirror/' + path
            oid = candidate_trees[batch['batch']][mirror]['oid']
            declaration = next((c['identity'] for c in relevant_contributions if c['batch'] == batch['batch'] and c['candidate_path'] == mirror), None)
            job(batch['candidate_published_commit'], mirror, declaration or {'git_blob': oid}, 'complete_group_candidate_mirror')
    for f in file_rows:
        job(ACTUAL, f['path'], f['actual'], 'complete_actual_formal')
        for c in f['contributions']:
            job(c['candidate_commit'], c['candidate_path'], c['identity'], 'shared_candidate_contribution')
    for f in unchanged:
        job(ACTUAL, f['path'], f['identity'], 'unchanged_actual_consumer')
    def fetch(item):
        url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + item['commit'] + '/' + urllib.parse.quote(item['path'], safe='/')
        attempts = []
        body = None
        for n in range(1, 4):
            begin = now()
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'group-A-independent-mechanical-audit'}), timeout=25) as response:
                    candidate = response.read()
                    status = response.status
                actual = identity(candidate)
                expected = item['expected']
                match = expected is None or all(actual[k] == v for k, v in expected.items())
                attempts.append({'attempt': n, 'utc_start': begin, 'utc_end': now(), 'url': url,
                                 'http_status': status, 'exit_code': 0 if match else 1, 'full_body_identity': actual,
                                 'result': 'FULL_BODY_MATCH' if match else 'IDENTITY_MISMATCH'})
                if match:
                    body = candidate
                    (SCRATCH / actual['git_blob']).write_bytes(body)
                    break
            except Exception as ex:
                attempts.append({'attempt': n, 'utc_start': begin, 'utc_end': now(), 'url': url,
                                 'exit_code': 1, 'result': 'FAILED_RETAINED', 'error': repr(ex)})
        return (item['commit'], item['path']), body, dict(item, attempts=attempts)
    bodies = {}
    raw_receipts = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for key, body, receipt in pool.map(fetch, jobs.values()):
            bodies[key] = body
            raw_receipts.append(receipt)
    write('remote-full-body-readback.json', {'actual_commit': ACTUAL, 'actual_tree': TREE, 'actual_formal_tree': FORMAL,
                                           'readback_file_count': len(raw_receipts), 'receipts': raw_receipts})
    check('all_fixed_remote_bodies_match_complete_identities', all(b is not None for b in bodies.values()),
          {'count': len(bodies), 'failed': [list(k) for k, v in bodies.items() if v is None]})
    if any(b is None for b in bodies.values()):
        raise RuntimeError('Remote body readback incomplete; retained failed attempts.')
    packed = {}
    for body in bodies.values():
        packed[identity(body)['git_blob']] = body
    fast_import = bytearray()
    for n, body in enumerate(packed.values(), 1):
        fast_import.extend(b'blob\nmark :' + str(n).encode() + b'\ndata ' + str(len(body)).encode() + b'\n' + body + b'\n')
    capture(['git', '--git-dir=' + str(DB), 'fast-import', '--quiet', '--done'], input_bytes=bytes(fast_import) + b'done\n')
    print('REMOTE_REPORT_BODIES_READY', str(DB), flush=True)
    check('remote_actual_input_complete_bytes_equal', bodies[(ACTUAL, INPUT)] == input_bytes, identity(input_bytes))
    for path in group_paths:
        check('remote_actual_formal_complete_body:' + path, bodies[(ACTUAL, path)] == blob(ACTUAL, path))

    # Full candidate changes are inventoried as blocks, then located in the actual body.
    # This proves receipt only; root performs source facts/counterexamples/interface semantics.
    block_rows = []
    shared_metadata = []
    group_candidate_rows = []
    for batch in batches:
        u = batch['batch']
        changed_count = 0
        for path in batch['all_candidate_allowlist_paths']:
            mirror = P + '/candidates/' + u + '/mirror/' + path
            current = bodies[(batch['candidate_published_commit'], mirror)]
            original = blob(MAIN, path)
            changed = current != original
            changed_count += changed
            declared = [c for c in relevant_contributions if c['batch'] == u and c['candidate_path'] == mirror]
            check('group_candidate_receipt_record_complete:' + u + ':' + path,
                  len(declared) == (1 if changed else 0),
                  {'changed_from_baseline': changed, 'contribution_records': len(declared), 'candidate_identity': identity(current)})
            group_candidate_rows.append({'batch': u, 'path': path, 'candidate_path': mirror, 'candidate_commit': batch['candidate_published_commit'],
                                          'candidate_identity': identity(current), 'baseline_identity': identity(original),
                                          'changed': changed, 'recorded_actual_receipt': len(declared) == 1})
        check('group_candidate_changed_counts:' + u, changed_count == {'R6-U01': 7, 'R6-U03': 3, 'R6-U14': 14}[u], changed_count)
    for f in file_rows:
        actual_lines = bodies[(ACTUAL, f['path'])].decode().splitlines(keepends=True)
        actual_text = ''.join(actual_lines)
        original = blob(MAIN, f['path']).decode().splitlines(keepends=True)
        shared_metadata.append({'path': f['path'], 'actual_identity': f['actual'], 'all_contributions': f['contributions'],
                                'pending_primary_writers': f['pending_primary_writers'],
                                'resolutions': [r for r in data['resolutions'] if r['path'] == f['path']],
                                'root_edits': [r for r in data['root_edits'] if r['path'] == f['path']]})
        for c in f['contributions']:
            candidate_body = bodies[(c['candidate_commit'], c['candidate_path'])]
            candidate_lines = candidate_body.decode().splitlines(keepends=True)
            meta = candidate_trees[c['batch']][c['candidate_path']]
            check('shared_candidate_full_body_identity:' + c['batch'] + ':' + f['path'],
                  matches(identity(candidate_body), c['identity']) and meta['oid'] == c['identity']['git_blob'] and meta['mode'] == '100644' and meta['type'] == 'blob')
            for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(a=original, b=candidate_lines, autojunk=False).get_opcodes():
                if tag == 'equal':
                    continue
                new = ''.join(candidate_lines[j1:j2])
                old = ''.join(original[i1:i2])
                positions = []
                cursor = 0
                while new and (at := actual_text.find(new, cursor)) >= 0:
                    positions.append(actual_text[:at].count('\n') + 1)
                    cursor = at + max(1, len(new))
                resolution = next((r for r in data['resolutions'] if r['path'] == f['path'] and
                                   'actual_line' in r and r['candidate_lines'].get(c['batch']) in new and
                                   r['actual_line'] in actual_text), None)
                allowed_editorial = (f['path'].endswith('/generic-kernel-wp02-03-04.md') and
                                      tag == 'insert' and new.strip() and new.strip() in actual_text and
                                      any(e['path'] == f['path'] and e.get('semantic_change') is False for e in data['root_edits']))
                if new:
                    good = bool(positions) or resolution is not None or allowed_editorial
                    method = 'EXACT_COMPLETE_BLOCK' if positions else 'EXACT_DECLARED_SHARED_NAVIGATION_RESOLUTION' if resolution else 'DECLARED_BLANK_LINE_EDITORIAL' if allowed_editorial else 'UNLOCATED_BLOCK'
                else:
                    good = not old.strip() or old not in actual_text
                    method = 'DELETED_OLD_BLOCK_ABSENT_OR_WHITESPACE_ONLY' if good else 'OLD_BLOCK_STILL_PRESENT'
                row = {'batch': c['batch'], 'path': f['path'], 'candidate_commit': c['candidate_commit'],
                       'opcode': tag, 'baseline_line_range': [i1 + 1, i2], 'candidate_line_range': [j1 + 1, j2],
                       'old_identity': identity(old.encode()), 'new_identity': identity(new.encode()),
                       'candidate_new_complete_block': new, 'actual_start_lines': positions,
                       'method': method, 'declared_resolution': resolution, 'receipt_match': good,
                       'qualification': 'Mechanical block receipt; no new behavior execution or semantic acceptance.'}
                block_rows.append(row)
                check('candidate_block_received:' + c['batch'] + ':' + f['path'] + ':' + str(j1 + 1), good, row)
    write('all-group-and-shared-candidate-block-receipts.json', block_rows)
    write('shared-composition-complete-metadata.json', shared_metadata)
    write('group-candidate-complete-mirror-identities.json', group_candidate_rows)
    # Per-ID locators join exact contract write sets to these actual receipt records.
    by_id = []
    for u, contract in contracts.items():
        for s in contract['scope_contracts']:
            write_set = s['minimum_revision_contract']['candidate_formal_write_set']
            selected = [x for x in block_rows if x['batch'] == u and x['path'] in write_set]
            by_id.append({'batch': u, 'id': s['id'], 'actual_commit': ACTUAL, 'actual_formal_tree': FORMAL,
                          'exact_contract_formal_write_set': write_set,
                          'actual_file_identities': [{'path': path, **identity(bodies[(ACTUAL, path)])} for path in write_set],
                          'received_candidate_block_count': len(selected),
                          'candidate_blocks_all_received': all(x['receipt_match'] for x in selected),
                          'semantic_verdict': 'ROOT_DIRECT_REVIEW_PENDING_NOT_DELEGATED',
                          'unchanged_baseline_controls': [x['path'] for x in group_candidate_rows if x['batch'] == u and not x['changed'] and x['path'] in write_set]})
    write('per-ID-mechanical-receipt-map.json', by_id)

    # Source metadata/full hashes only. No source program, data deserialization or host loaded.
    frozen = json.loads(blob(PREP, P + '/inputs/frozen-inputs.json'))
    previous_source_paths = set(contracts['R6-U01']['read_only_reference_paths']) | {
        'PBS/pokemon_forms.txt', 'Data/Scripts/011_Battle/003_Battle/012_Battle_Pokedex.rb'}
    # Reuse exact declared paths from the previous independent U01 source identity receipt.
    prior_source_path = P + '/candidates/R6-U01/evidence/source-payload-identities.json'
    u01_commit = all_batches['R6-U01']['candidate_published_commit']
    source_metadata = remote_entries(u01_commit, prior_source_path)[0]
    source_job = {'commit': u01_commit, 'path': prior_source_path, 'expected': {'git_blob': source_metadata['oid']}, 'roles': ['prior_source_identity_list']}
    _, source_list_body, source_list_receipt = fetch(source_job)
    write('prior-U01-source-identity-list-readback.json', source_list_receipt)
    if source_list_body is None:
        raise RuntimeError('U01 source identity list unavailable')
    check('prior_source_identity_list_full_body_tree_binding', identity(source_list_body)['git_blob'] == source_metadata['oid'],
          {'metadata': source_metadata, 'full_identity': identity(source_list_body)})
    prior_source_list = json.loads(source_list_body)
    previous_source_paths = {x['path'] for x in prior_source_list}
    source_paths = sorted(previous_source_paths | {p for c in contracts.values() for p in c['read_only_reference_paths']})
    ref_tree = ref_git('rev-parse', REF + '^{tree}').decode().strip()
    check('read_only_reference_fixed_tree', ref_tree == REF_TREE)
    source_receipts = []
    for path in source_paths:
        baseline = next(x for x in frozen['source_materials'] if x['path'] == path)
        metadata = parse_tree(ref_git('ls-tree', '-z', REF, '--', path))[0]
        body = ref_git('show', REF + ':' + path, reference_payload=True)
        actual = identity(body)
        prior_row = next((x for x in prior_source_list if x['path'] == path), None)
        good = matches(actual, baseline) and metadata['oid'] == actual['git_blob'] and metadata['mode'] == baseline['mode'] and metadata['type'] == 'blob'
        if prior_row:
            good = good and matches(actual, prior_row) and prior_row['commit'] == REF and prior_row['tree'] == REF_TREE
        source_receipts.append({'path': path, 'reference_commit': REF, 'reference_tree': REF_TREE, **actual,
                                'mode': metadata['mode'], 'type': metadata['type'],
                                'reused_prior_U01_source': prior_row is not None, 'all_identity_metadata_match': good,
                                'reference_loaded_or_executed': False})
    check('all_source_original_identity_metadata_match', len(prior_source_list) == 13 and
          all(x['all_identity_metadata_match'] for x in source_receipts),
          {'source_count': len(source_receipts), 'prior_U01_count': len(prior_source_list),
           'additional_source_count': sum(not x['reused_prior_U01_source'] for x in source_receipts)})
    write('source-fixed-original-identities.json', source_receipts)

    # Preserve all old report layers/candidate snapshots/public audit and main/reference refs.
    for protected in ['AGENTS.md', 'reference', P + '/candidates', 'planning/feature-matrix.md']:
        delta = git('diff', '--name-status', PREP, ACTUAL, '--', protected).decode().splitlines()
        check('frozen_integrated_protected_path:' + protected, not delta, delta)
    old_trace = blob(PREP, 'audit/source-traceability.md')
    current_trace = blob(ACTUAL, 'audit/source-traceability.md')
    prior_trace = blob(prior, 'audit/source-traceability.md')
    check('public_existing_layers_preserved_and_group_A_final_not_changed', current_trace.startswith(old_trace) and current_trace == prior_trace,
          {'baseline_identity': identity(old_trace), 'actual_identity': identity(current_trace),
           'qualification': 'Existing U04 pending-review append predates final composition; no extra public equality/administrative acceptance gate.'})
    old_review_delta = git('diff', '--name-status', MAIN, ACTUAL, '--', 'review').decode().splitlines()
    changed_existing_old = [x for x in old_review_delta if not x.startswith('A\t') and not x.split('\t')[1].startswith(P + '/')]
    check('old_historical_review_reports_preserved', not changed_existing_old, changed_existing_old)
    old_main_tree = git('rev-parse', MAIN + '^{tree}').decode().strip()
    remote_main = git('ls-remote', '--heads', REMOTE, 'refs/heads/main').decode().strip()
    check('remote_main_still_frozen_main', remote_main.split()[0] == MAIN, remote_main)
    check('fixed_main_original_tree_preserved', old_main_tree == data['fixed_main_workspace_tree'], old_main_tree)
    status = git('status', '--porcelain', '--untracked-files=all').decode().splitlines()
    own_scope = P + '/actual-reviews/group-A/'
    check('current_worktree_writes_only_group_A', all(x.startswith('?? ') and x[3:].startswith(own_scope) for x in status), status)
    check('project_HEAD_branch_and_refs_not_changed_by_audit', git('rev-parse', 'HEAD').decode().strip() == head_start and
          git('branch', '--show-current').decode().strip() == branch_start and git('show-ref').decode() == refs_start)
    check('reference_original_tree_still_fixed', ref_git('rev-parse', REF + '^{tree}').decode().strip() == REF_TREE)
    summary = {'result': 'PASS_MECHANICAL_INTEGRITY' if all(c['result'] == 'PASS_MECHANICAL' for c in checks) else 'FAIL_MECHANICAL_INTEGRITY',
               'utc_start': START, 'utc_end': now(), 'actual_commit': ACTUAL, 'actual_workspace_tree': TREE,
               'actual_formal_tree': FORMAL, 'input_identity': identity(input_bytes), 'scope_batches': GROUP,
               'scope_IDs': ids, 'scope_ID_count': len(ids), 'actual_group_files': len(group_paths),
               'actual_group_changed_files': len(file_rows), 'global_actual_changed_files': len(actual_changed),
               'group_candidate_full_mirrors': len(group_candidate_rows), 'all_shared_candidate_contributions': len(relevant_contributions),
               'candidate_block_receipts': len(block_rows), 'candidate_block_receipts_all_match': all(x['receipt_match'] for x in block_rows),
               'remote_complete_body_files': len(raw_receipts) + 1, 'source_identity_payloads': len(source_receipts),
               'reused_source_payloads': len(prior_source_list), 'mechanical_check_count': len(checks),
               'command_receipts': len(commands), 'failed_checks': [x for x in checks if x['result'] != 'PASS_MECHANICAL'],
               'actual_effective_model_configuration': 'UNVERIFIED', 'reference_model_host_save_execution': 0,
               'semantic_adjudication': 'ROOT_DIRECT_REVIEW_ONLY', 'INTEGRATED_PASS': 'NOT_GRANTED_BY_THIS_AUDIT',
               'formal_acceptance': 'NOT_GRANTED_BY_THIS_AUDIT', 'CLOSED': False, 'remaining_blockers': []}
    write('summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False), flush=True)
except Exception as error:
    write('failure.json', {'utc': now(), 'error': repr(error), 'completed_checks': len(checks),
                           'command_receipts': len(commands), 'reference_behavior_execution': 0})
    raise
