"""Independent finite mechanical audit. Does not execute author tools or reference source."""
from pathlib import Path
import concurrent.futures
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import time
import urllib.parse
import urllib.request

ROOT = Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT / 'review/remediation-sixth-20261014-prepare/reviews/R6-U01-R/payload-audit'
P = 'review/remediation-sixth-20261014-prepare'
B = P + '/candidates/R6-U01'
E = B + '/evidence'
M = B + '/mirror'
PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
PUB = '0f2bf0318405ab281682023c6cf0a68eabdd73ad'
PUB_TREE = '7091593ae08af02d265250fa94cb7f552e51fba7'
CORE = 'd13dc8446d0e47c659f81c86413aeafb2279da01'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
REMOTE = 'https://github.com/y805939188/pokemon-essentials-clean-room.git'
DB = Path('/tmp/r6-u01-r-payload-remote.git')
REFDB = Path('/tmp/r6-u01-r-reference.git')
BODYDIR = Path('/tmp/r6-u01-r-payload-bodies')
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'logs').mkdir(exist_ok=True)
BODYDIR.mkdir(exist_ok=True)
commands = []
checks = []
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
started = now()

def ident(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}

def write(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def capture(args, cwd=ROOT, data=None, ok=(0,)):
    begin = now()
    r = subprocess.run(args, cwd=cwd, input=data, capture_output=True)
    n = len(commands) + 1
    base = OUT / 'logs' / f'{n:04d}'
    base.with_suffix('.stdout').write_bytes(r.stdout)
    base.with_suffix('.stderr').write_bytes(r.stderr)
    row = {'argv': [str(x) for x in args], 'cwd': str(cwd), 'utc_start': begin,
           'utc_end': now(), 'exit_code': r.returncode,
           'stdout_path': str(base.with_suffix('.stdout').relative_to(ROOT)),
           'stderr_path': str(base.with_suffix('.stderr').relative_to(ROOT)),
           'stdout_identity': ident(r.stdout), 'stderr_identity': ident(r.stderr),
           'reference_execution': False}
    if data is not None:
        row['stdin_identity'] = ident(data)
    commands.append(row)
    (OUT / 'commands.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in commands))
    if r.returncode not in ok:
        raise RuntimeError({'argv': row['argv'], 'exit_code': r.returncode,
                            'stderr': r.stderr.decode(errors='replace')})
    return r.stdout

def git(*args):
    return capture(['git', *args])

def remote_git(*args):
    return capture(['git', '--git-dir=' + str(DB), *args])

def ref_git(*args):
    return capture(['git', '--git-dir=' + str(REFDB), *args])

def check(name, predicate, detail=None):
    checks.append({'check': name, 'result': 'PASS_MECHANICAL' if predicate else 'FAIL_MECHANICAL',
                   'detail': detail})
    write('checks.json', checks)
    if not predicate:
        print('MECHANICAL_DIFFERENCE', name, json.dumps(detail, ensure_ascii=False), flush=True)

def parse_tree(raw):
    rows = []
    for entry in raw.split(b'\0'):
        if entry:
            meta, path = entry.split(b'\t', 1)
            mode, kind, oid = meta.decode().split()
            rows.append({'path': path.decode(), 'mode': mode, 'type': kind, 'oid': oid})
    return rows

def entries(commit, path, recursive=True, trees=False, remote=False):
    args = ['ls-tree'] + (['-r'] if recursive else []) + (['-t'] if trees else [])
    return parse_tree((remote_git if remote else git)(*args, '-z', commit, '--', path))

def local_body(commit, path):
    return git('show', commit + ':' + path)

def jbody(commit, path):
    return json.loads(local_body(commit, path))

def same_identity(actual, expected):
    return all(actual[k] == expected[k] for k in ('bytes', 'sha256', 'git_blob'))

try:
    root_agent = local_body(PREP, 'AGENTS.md')
    check('applicable_AGENTS_unchanged', root_agent == local_body(PUB, 'AGENTS.md'), ident(root_agent))
    prompt_path = P + '/prompts/R6-U01-R.md'
    prompt = local_body(PREP, prompt_path)
    check('fixed_reviewer_prompt_identity', same_identity(ident(prompt), {
        'bytes': 253260, 'sha256': 'b5a05fd0a671414092c59658323b7f4d6219e5b09f84dfb3b4a073bc6e50db3b',
        'git_blob': '354415efbda685b91a2e07f888a1fbdd6e611feb'}), {'path': prompt_path, **ident(prompt)})
    contract = jbody(PREP, P + '/contracts/R6-U01.json')
    frozen = jbody(PREP, P + '/inputs/frozen-inputs.json')
    check('contract_exact_ID_binding', contract['required_ids'] == ['GR6-K-001', 'GR6-K-002', 'GR6-K-003'],
          {'path': P + '/contracts/R6-U01.json', **ident(local_body(PREP, P + '/contracts/R6-U01.json'))})
    check('candidate_is_direct_core_child', git('rev-parse', PUB + '^').decode().strip() == CORE)
    check('core_is_direct_prepare_child', git('rev-parse', CORE + '^').decode().strip() == PREP)
    check('fixed_candidate_whole_tree', git('rev-parse', PUB + '^{tree}').decode().strip() == PUB_TREE, PUB_TREE)
    delta = git('diff', '--name-status', PREP, PUB).decode().splitlines()
    changes = [{'status': line.split('\t', 1)[0], 'path': line.split('\t', 1)[1]} for line in delta]
    write('actual-prepare-candidate-delta.json', changes)
    check('all_published_changes_inside_candidate', all(x['path'].startswith(B + '/') for x in changes),
          {'changed_paths': len(changes), 'outside': [x for x in changes if not x['path'].startswith(B + '/')]})
    check('no_published_deletions', not any(x['status'] == 'D' for x in changes))
    for protected in ['deliverables/final-specification-set', 'reference', 'AGENTS.md',
                      P + '/task-register.json', P + '/ledger.json']:
        diff = git('diff', '--name-only', PREP, PUB, '--', protected).decode().splitlines()
        check('protected_prepare_path:' + protected, not diff, diff)
    formal_tree = git('rev-parse', PUB + ':deliverables/final-specification-set').decode().strip()
    check('entire_formal_tree_is_frozen_main', formal_tree == frozen['formal_tree'] ==
          git('rev-parse', MAIN + ':deliverables/final-specification-set').decode().strip(), formal_tree)
    payloads = jbody(PUB, E + '/candidate-payload-identities.json')
    replacement_rows = jbody(PUB, E + '/exact-replacements.json')
    mirror_rows = []
    changed_mirrors = []
    for path in contract['candidate_formal_paths']:
        mirror = M + '/' + path
        original = local_body(MAIN, path)
        prep_body = local_body(PREP, mirror)
        current = local_body(PUB, mirror)
        row = next(x for x in payloads if x['formal_path'] == path)
        metas = entries(PUB, mirror, recursive=False)[0]
        frozen_row = next(x for x in frozen['formal_materials'] if x['path'] == path)
        changed = original != current
        if changed:
            changed_mirrors.append(mirror)
        check('mirror_bound_identity:' + path,
              prep_body == original and same_identity(ident(original), row['baseline']) and
              same_identity(ident(original), frozen_row) and same_identity(ident(current), row['candidate']) and
              row['changed'] == changed and metas['mode'] == row['mode'] == '100644' and
              metas['type'] == row['type'] == 'blob' and metas['oid'] == ident(current)['git_blob'], row)
        replay = original.decode()
        for replacement in [x for x in replacement_rows if x['path'] == mirror]:
            check('replacement_unique:' + mirror + ':' + str(len(checks)), replay.count(replacement['old']) == 1)
            replay = replay.replace(replacement['old'], replacement['new'])
        check('complete_declared_replacement_replay:' + path, replay.encode() == current)
        old_rows = {}
        new_rows = []
        if '/test-catalog/' in path:
            pattern = re.compile(r'^\|\s*([A-Za-z][\w-]*\d)\s*\|')
            old_rows = {pattern.match(line).group(1): line for line in original.decode().splitlines()
                        if pattern.match(line)}
            new_rows = [(pattern.match(line).group(1), line) for line in current.decode().splitlines()
                        if pattern.match(line)]
            ns = dict(new_rows)
            check('all_catalogue_rows_unique_and_preserved:' + path, len(ns) == len(new_rows) and
                  all(ns.get(k) == v for k, v in old_rows.items()),
                  {'existing': len(old_rows), 'new': len(new_rows) - len(old_rows),
                   'added_ids': [k for k, _ in new_rows if k not in old_rows]})
        mirror_rows.append({'formal_path': path, 'candidate_path': mirror, 'baseline': ident(original),
                            'candidate': ident(current), 'changed': changed,
                            'mode': metas['mode'], 'type': metas['type']})
    expected_changed = {M + '/' + x for x in contract['candidate_formal_paths']
                        if 'wp21-dynamic' not in x and 'wp27-bag' not in x}
    check('exact_seven_changed_two_baseline_mirrors', set(changed_mirrors) == expected_changed and
          len(mirror_rows) == 9 and len(payloads) == 9,
          {'changed': changed_mirrors, 'unchanged': [x['formal_path'] for x in mirror_rows if not x['changed']]})
    write('mirror-identities-and-delta.json', mirror_rows)
    existing_dirs = entries(PUB, B, trees=True)
    local_entries = [x for x in existing_dirs if x['type'] == 'blob']
    check('candidate_201_paths_122_unique_blobs', len(local_entries) == 201 and
          len({x['oid'] for x in local_entries}) == 122,
          {'paths': len(local_entries), 'unique_blobs': len({x['oid'] for x in local_entries}),
           'tree_entries_including_candidate_root': len(existing_dirs) - len(local_entries)})

    # Empty, independent object store. Exact SHA fetch never reads a local remote-tracking ref.
    check('independent_object_store_absent_at_start', not DB.exists(), str(DB))
    if DB.exists():
        raise RuntimeError('Independent store already exists; choose a fresh path, do not reuse it.')
    capture(['git', 'init', '--bare', str(DB)])
    remote_git('fetch', '--depth=2', '--filter=blob:none', REMOTE, PUB)
    remote_commit = remote_git('rev-parse', 'FETCH_HEAD').decode().strip()
    remote_tree = remote_git('rev-parse', PUB + '^{tree}').decode().strip()
    candidate_tree = remote_git('rev-parse', PUB + ':' + B).decode().strip()
    core_tree = remote_git('rev-parse', CORE + '^{tree}').decode().strip()
    check('fresh_remote_exact_commit_tree', remote_commit == PUB and remote_tree == PUB_TREE,
          {'commit': remote_commit, 'whole_tree': remote_tree, 'candidate_tree': candidate_tree,
           'core_tree': core_tree, 'alternates_file_present': (DB / 'objects/info/alternates').exists()})
    check('independent_store_has_no_alternates', not (DB / 'objects/info/alternates').exists())
    remote_tree_rows = entries(PUB, B, trees=True, remote=True)
    check('all_remote_modes_types_paths_trees_match_local', remote_tree_rows == existing_dirs,
          {'rows': len(remote_tree_rows), 'file_paths': len(local_entries)})
    write('remote-tree-all-entries.json', remote_tree_rows)
    unique = {x['oid']: x for x in local_entries}

    def fetch_blob(item):
        path = item['path']
        url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + PUB + '/' + urllib.parse.quote(path, safe='/')
        attempts = []
        body = None
        for n in range(1, 4):
            begin = now()
            try:
                request = urllib.request.Request(url, headers={'User-Agent': 'R6-U01-R-independent-payload-audit'})
                with urllib.request.urlopen(request, timeout=25) as response:
                    body = response.read()
                    status = response.status
                actual = ident(body)
                matching = actual['git_blob'] == item['oid']
                attempts.append({'attempt': n, 'url': url, 'utc_start': begin, 'utc_end': now(),
                                 'http_status': status, 'exit_code': 0 if matching else 1,
                                 'result': 'FULL_BODY_MATCH' if matching else 'BODY_IDENTITY_MISMATCH',
                                 'actual': actual})
                if matching:
                    (BODYDIR / item['oid']).write_bytes(body)
                    break
                body = None
            except Exception as ex:
                attempts.append({'attempt': n, 'url': url, 'utc_start': begin, 'utc_end': now(),
                                 'exit_code': 1, 'result': 'FAILED_RETAINED', 'error': repr(ex)})
        return item['oid'], body, {'oid': item['oid'], 'path_used': path, 'attempts': attempts}

    bodies = {}
    attempts = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for oid, body, receipt in pool.map(fetch_blob, unique.values()):
            bodies[oid] = body
            attempts.append(receipt)
    write('remote-full-body-attempts.json', attempts)
    check('122_distinct_remote_full_bodies_match_tree_blobs', all(b is not None for b in bodies.values()) and
          len(bodies) == 122, {'distinct_bodies': len(bodies), 'failed_oids': [o for o, b in bodies.items() if b is None]})
    if any(b is None for b in bodies.values()):
        raise RuntimeError('Full remote raw body retrieval incomplete; retained attempts in report.')
    readback = []
    for row in local_entries:
        body = bodies[row['oid']]
        expected = (ROOT / row['path']).read_bytes()
        actual = ident(body)
        readback.append({'path': row['path'], 'mode': row['mode'], 'type': row['type'], **actual,
                         'remote_commit': PUB, 'remote_whole_tree': remote_tree,
                         'remote_candidate_tree': candidate_tree, 'full_bytes_equal_worktree': body == expected,
                         'tree_blob_matches_full_body': actual['git_blob'] == row['oid']})
    check('all_201_path_bodies_equal_frozen_worktree', all(x['full_bytes_equal_worktree'] and
          x['tree_blob_matches_full_body'] for x in readback))
    write('remote-complete-payload-readback.json', {'utc_start': started, 'utc_end': now(),
          'publication_commit': PUB, 'publication_tree': remote_tree, 'candidate_tree': candidate_tree,
          'verified_file_paths': len(readback), 'distinct_full_blob_bodies': len(bodies), 'readback': readback})

    # Complete body pack inserted only in the scratch object database, one recorded command.
    proc = bytearray()
    pack_rows = []
    for oid, body in bodies.items():
        new_oid = hashlib.sha1(b'blob ' + str(len(body)).encode() + b'\0' + body).hexdigest()
        if new_oid != oid:
            raise RuntimeError('Remote body changed before scratch pack generation')
        # fast-import writes these isolated data objects without altering any project branch.
        proc.extend(b'blob\nmark :' + str(len(pack_rows) + 1).encode() + b'\ndata ' + str(len(body)).encode() + b'\n' + body + b'\n')
        pack_rows.append(oid)
    capture(['git', '--git-dir=' + str(DB), 'fast-import', '--quiet', '--done'], data=bytes(proc) + b'done\n')
    batch = capture(['git', '--git-dir=' + str(DB), 'cat-file', '--batch-check=%(objectname) %(objecttype) %(objectsize)'],
                    data=('\n'.join(pack_rows) + '\n').encode()).decode().splitlines()
    check('scratch_store_contains_all_122_remote_bodies', len(batch) == 122 and all(
          line.split() == [oid, 'blob', str(len(bodies[oid]))] for line, oid in zip(batch, pack_rows)))

    # Manifest covers finite core except self; final publication adds two fixed evidence paths.
    by_path = {x['path']: x for x in readback}
    manifest = json.loads(bodies[next(x['oid'] for x in local_entries if x['path'] == E + '/core-manifest.json')])
    core_entries = entries(CORE, B)
    manifest_rows = []
    for item in manifest['items']:
        actual = by_path.get(item['path'])
        match = actual is not None and same_identity(actual, item) and actual['mode'] == item['mode'] and actual['type'] == item['type']
        manifest_rows.append({'path': item['path'], 'published_identity_matches_manifest': match})
    core_paths = {x['path'] for x in core_entries}
    manifest_paths = {x['path'] for x in manifest['items']}
    check('core_manifest_exact_set_and_full_identities', len(manifest_rows) == 198 and
          len(manifest_paths) == len(manifest_rows) and all(x['published_identity_matches_manifest'] for x in manifest_rows) and
          core_paths == manifest_paths | {E + '/core-manifest.json'} and
          manifest['excluded_self'] == [E + '/core-manifest.json'],
          {'core_paths': len(core_paths), 'manifest_items': len(manifest_rows), 'excluded_self': manifest['excluded_self']})
    core_to_publication = git('diff', '--name-status', CORE, PUB).decode().splitlines()
    check('publication_only_adds_two_evidence_paths', set(core_to_publication) == {
          'A\t' + E + '/publication-binding.json', 'A\t' + E + '/publication-runner.py'}, core_to_publication)
    check('core_mirrors_and_manifest_unchanged_at_publication', not git('diff', '--name-only', CORE, PUB, '--', M, E + '/core-manifest.json'))
    write('core-manifest-audit.json', {'core_commit': CORE, 'core_tree': core_tree,
          'core_candidate_tree': git('rev-parse', CORE + ':' + B).decode().strip(),
          'manifest_identity': ident(local_body(PUB, E + '/core-manifest.json')),
          'core_path_count': len(core_paths), 'manifest_items': len(manifest_rows),
          'publication_additions': core_to_publication, 'items': manifest_rows})
    binding = jbody(PUB, E + '/publication-binding.json')
    check('publication_binding_matches_actual_core', binding['core_commit'] == CORE and binding['core_tree'] == core_tree and
          binding['core_candidate_tree'] == git('rev-parse', CORE + ':' + B).decode().strip() and
          same_identity(ident(local_body(PUB, E + '/core-manifest.json')), binding['core_manifest']) and
          binding['candidate_mirror_changes_after_core'] == 0, binding)

    # Reference source is read as blobs only from the parent's separate fixed reference database.
    source_rows = jbody(PUB, E + '/source-payload-identities.json')
    reference_tree = ref_git('rev-parse', REF + '^{tree}').decode().strip()
    check('reference_fixed_commit_tree', reference_tree == frozen['reference_tree'], {'commit': REF, 'tree': reference_tree})
    source_checks = []
    for item in source_rows:
        source_path = item['path']
        body = ref_git('show', REF + ':' + source_path)
        metadata = parse_tree(ref_git('ls-tree', '-z', REF, '--', source_path))[0]
        baseline = next(x for x in frozen['source_materials'] if x['path'] == source_path)
        actual = {'commit': REF, 'tree': reference_tree, 'path': source_path, **ident(body),
                  'mode': metadata['mode'], 'type': metadata['type']}
        match = (same_identity(actual, item) and same_identity(actual, baseline) and item['commit'] == REF and
                 item['tree'] == reference_tree and item['mode'] == metadata['mode'] and item['type'] == metadata['type'] and
                 metadata['oid'] == actual['git_blob'])
        source_checks.append({**actual, 'author_and_frozen_identity_match': match, 'behavior_execution': False})
    check('all_13_source_payloads_match_fixed_original_blobs', len(source_checks) == 13 and
          all(x['author_and_frozen_identity_match'] for x in source_checks), {'source_payloads': len(source_checks)})
    write('source-original-payload-audit.json', source_checks)

    validation = jbody(PUB, E + '/validation.json')
    author_commands = [json.loads(x) for x in local_body(PUB, E + '/commands.jsonl').decode().splitlines()]
    command_log_checks = []
    for n, cmd in enumerate(author_commands, 1):
        streams = {}
        for kind in ('stdout', 'stderr'):
            full = by_path.get(cmd[kind + '_path'])
            streams[kind] = full is not None and same_identity(full, cmd[kind + '_identity'])
        command_log_checks.append({'index': n, 'argv': cmd['argv'], 'utc_start': cmd.get('utc_start', 'UNVERIFIED'),
                                   'utc_end': cmd.get('utc_end', 'UNVERIFIED'), 'exit_code': cmd['exit_code'],
                                   'evidence_level': cmd.get('evidence_level'),
                                   'execution_of_reference': cmd.get('execution_of_reference', 'UNVERIFIED'),
                                   'full_stdout_identity_matches': streams['stdout'],
                                   'full_stderr_identity_matches': streams['stderr']})
    check('all_80_author_command_log_full_payloads_bound', len(command_log_checks) == 80 and all(
          x['full_stdout_identity_matches'] and x['full_stderr_identity_matches'] for x in command_log_checks))
    check('author_115_checks_are_static_tool_assertions', len(validation['checks']) == 115 and
          all(x['result'] == 'PASS_TOOL_CHECK' for x in validation['checks']) and
          validation['evidence_level'] == 'TOOL_VALIDATION' and validation['behavior_execution'] == 0 and
          validation['host_execution'] == 0 and all(x['execution_of_reference'] is False for x in command_log_checks),
          {'checks': len(validation['checks']), 'evidence_level': validation['evidence_level'],
           'behavior_execution': validation['behavior_execution'], 'host_execution': validation['host_execution'],
           'independence': validation['independent_review']})
    check('author_validation_scope_matches_actual_mirrors', set(validation['changed_mirrors']) == set(changed_mirrors) and
          set(validation['preserved_baseline_mirrors']) == {x['formal_path'] for x in mirror_rows if not x['changed']})
    write('author-command-record-audit.json', command_log_checks)
    spans = jbody(PUB, E + '/historical-span-preservation.json')
    span_rows = []
    for item in spans:
        original = local_body(MAIN, item['path']).decode().splitlines(keepends=True)
        lo, hi = item['baseline_lines']
        content = ''.join(original[lo - 1:hi]).encode()
        mirror = local_body(PUB, M + '/' + item['path'])
        span_rows.append({**item, 'independent_full_span_match': content in mirror and
                          len(content) == item['bytes'] and hashlib.sha256(content).hexdigest() == item['sha256'] and
                          item['baseline_commit'] == MAIN})
    check('all_author_historical_preserved_spans_byte_bound', all(x['independent_full_span_match'] for x in span_rows),
          {'span_count': len(span_rows), 'scope': 'mechanical byte preservation only; root owns qualification semantics'})
    write('historical-span-mechanical-audit.json', span_rows)
    availability = {'utc': now(), 'check_method': 'shutil.which (no Ruby process or reference loaded)',
                    'ruby_executable': shutil.which('ruby'), 'reference_execution': 0, 'behavior_execution': 0,
                    'host_UI_Demo_save_execution': 0, 'actual_model_effort_tier_speed': 'UNVERIFIED',
                    'scope': 'Mechanical integrity only; no per-ID semantic adjudication or formal acceptance/CLOSED.'}
    write('limits-and-runtime-availability.json', availability)
    summary = {'result': 'PASS_MECHANICAL_INTEGRITY' if all(x['result'] == 'PASS_MECHANICAL' for x in checks) else 'FAIL_MECHANICAL_INTEGRITY',
               'utc_start': started, 'utc_end': now(), 'prepare_commit': PREP, 'publication_commit': PUB,
               'publication_tree': PUB_TREE, 'candidate_tree': candidate_tree, 'semantic_core_commit': CORE,
               'semantic_core_tree': core_tree, 'actual_changed_mirrors': len(changed_mirrors),
               'unchanged_baseline_mirrors': [x['formal_path'] for x in mirror_rows if not x['changed']],
               'published_delta_paths': len(changes), 'remote_verified_file_paths': len(readback),
               'remote_distinct_full_blob_bodies': len(bodies), 'remote_tree_entries_including_root': len(remote_tree_rows),
               'source_original_payloads': len(source_checks), 'core_manifest_items': len(manifest_rows),
               'author_static_tool_checks': len(validation['checks']), 'author_command_receipts': len(author_commands),
               'mechanical_check_count': len(checks), 'failed_checks': [x for x in checks if x['result'] != 'PASS_MECHANICAL'],
               'command_receipts': len(commands), 'reference_and_behavior_execution': 0,
               'formal_acceptance': 'NOT_GRANTED_BY_THIS_AUDIT', 'CLOSED': 'NOT_REGISTERED',
               'per_ID_verdict': 'OUT_OF_SCOPE_ROOT_DIRECT_REVIEW', 'remaining_blockers': []}
    write('summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False), flush=True)
except Exception as ex:
    write('failure.json', {'utc': now(), 'error': repr(ex), 'checks_completed': len(checks),
                           'command_receipts': len(commands), 'reference_execution': 0})
    raise
