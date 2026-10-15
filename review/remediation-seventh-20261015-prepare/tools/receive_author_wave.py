"""Receive bounded immutable author bundles. No model tasks or semantic PASS."""
from pathlib import Path
import concurrent.futures
import datetime
import difflib
import hashlib
import json
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

P = Path(__file__).resolve().parents[1]
PROJECT = P.parents[1]
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
C = 'f622356f3beb9e84ea8cff9db07c7fb382565d3f'
REPO = 'y805939188/pokemon-essentials-clean-room'


def git(*args):
    return subprocess.check_output(['git', '-C', str(PROJECT), *args])


def ident(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}


def declared_identity(value):
    if not isinstance(value, dict):
        return None
    size = value.get('bytes', value.get('size'))
    sha = value.get('sha256')
    blob = value.get('git_blob', value.get('git_blob_content_id', value.get('content_git_blob')))
    if isinstance(size, int) and isinstance(sha, str) and isinstance(blob, str):
        return {'bytes': size, 'sha256': sha, 'git_blob': blob}
    return None


def manifest_records(value, known):
    result = {path: [] for path in known}
    def visit(x, key=None):
        if isinstance(x, dict):
            path = next((x[k] for k in ['candidate_path', 'path', 'artifact_path', 'file'] if isinstance(x.get(k), str) and x[k] in known), key if key in known else None)
            if path:
                result[path].append(x)
            for k, child in x.items():
                visit(child, k)
        elif isinstance(x, list):
            for child in x:
                visit(child)
    visit(value)
    return result


def candidate_identity(record):
    for key in ['new_identity', 'candidate_identity', 'candidate', 'after', 'new', 'identity']:
        value = declared_identity(record.get(key))
        if value:
            return value
    return declared_identity(record)


def target_base_identity(records):
    for record in records:
        explicit_mirror = any(k in record for k in ['candidate_path', 'original_path', 'formal_target', 'base_path', 'baseline_path', 'base_target_identity', 'original_B'])
        if not explicit_mirror:
            continue
        for key in ['base_target_identity', 'base_identity', 'original_B', 'base', 'baseline', 'before', 'original']:
            value = declared_identity(record.get(key))
            if value:
                return value
    return None


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def receive(task):
    bid, commit = task['batch_id'], task['candidate_commit']
    prefix = f'candidates/{bid}/'
    folder = P/'candidate-freezes'/bid
    if task['freeze_version'] != 'initial':
        folder = folder/'versions'/task['freeze_version']
    assert not folder.exists(), 'Existing freeze preserved: '+str(folder)
    contract_path = f'review/remediation-seventh-20261015-prepare/delegation/contracts/{bid}.json'
    contract_bytes = git('show', C+':'+contract_path)
    contract = json.loads(contract_bytes)
    allowed = {r['candidate_path']: r for r in contract['paths']}
    assert git('rev-parse', commit+'^{tree}').decode().strip() == task['candidate_tree']
    raw = git('diff', '--name-status', '--no-renames', '-z', B, commit).decode().strip('\0').split('\0')
    diff = list(zip(raw[::2], raw[1::2]))
    assert len(raw) == 2*len(diff) and len(diff) == task['expected_files']
    assert all(status == 'A' and (path in allowed or path.startswith(prefix+'evidence/author/')) for status, path in diff)
    modes = {line.split('\t', 1)[1]: line.split()[0] for line in git('ls-tree', '-r', commit, prefix).decode().splitlines()}
    assert set(modes) == {path for _, path in diff} and set(modes.values()) <= {'100644', '100755'}
    expected = {path: git('show', commit+':'+path) for _, path in diff}
    total = sum(map(len, expected.values()))
    if task['expected_bytes_parent'] is not None:
        assert total == task['expected_bytes_parent']
    local = Path('/workspace/r7-author-wave-reception')/(bid+'-'+commit)
    local.mkdir(parents=True, exist_ok=True)
    def download(path):
        url = f'https://raw.githubusercontent.com/{REPO}/{commit}/'+urllib.parse.quote(path)
        attempts = []
        for n in range(1, 4):
            try:
                with urllib.request.urlopen(url, timeout=40) as response:
                    data = response.read(len(expected[path])+1)
                    code = response.status
                assert data == expected[path], path
                target = local/path
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.exists():
                    assert target.read_bytes() == data, 'Preserve conflicting existing bytes'
                else:
                    target.write_bytes(data)
                attempts.append({'attempt': n, 'http_status': code, 'complete_byte_match': True})
                return {'path': path, **ident(data), 'git_mode': modes[path], 'url': url, 'attempts': attempts}
            except (urllib.error.URLError, TimeoutError) as error:
                attempts.append({'attempt': n, 'error': str(error)})
                if n == 3:
                    raise
                time.sleep(n)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        remote = list(pool.map(download, expected))
    manifest_path = prefix+'evidence/author/artifact-manifest.json'
    manifest = json.loads(expected[manifest_path])
    declarations = manifest_records(manifest, expected)
    validated = []
    undeclared = []
    for path, data in expected.items():
        values = [candidate_identity(row) for row in declarations[path]]
        values = [value for value in values if value is not None]
        for value in values:
            assert ident(data) == value, ('Candidate declared identity mismatch', bid, path)
        if values:
            validated.append(path)
        elif path != manifest_path:
            undeclared.append(path)
    mirrors = []
    patches = []
    for path in expected:
        if path not in allowed:
            continue
        target = path[len(prefix):]
        before = subprocess.run(['git', '-C', str(PROJECT), 'show', B+':'+target], capture_output=True)
        if before.returncode:
            assert target == 'review/remediation-seventh-20261015-prepare/current-navigation-errata.json'
            baseline = {'exists': False, 'qualification': 'Approved prospective current navigation errata target absent at fixed B; not a missing readable input.'}
            original = b''
        else:
            original = before.stdout
            baseline = ident(original)
            declaration = target_base_identity(declarations[path])
            if declaration:
                assert baseline == declaration, ('Declared formal-target B identity mismatch', bid, target)
        mirrors.append({'path': path, 'formal_target': target, **ident(expected[path]), 'git_mode': modes[path], 'base_B_identity_or_explicit_new_file': baseline, 'write_classification': allowed[path]['classification']})
        patches.extend(difflib.unified_diff(original.decode().splitlines(True), expected[path].decode().splitlines(True), fromfile='a/'+target, tofile='b/'+target))
    required = {path for path, row in allowed.items() if row['classification'] == 'required'}
    assert required <= {row['path'] for row in mirrors}
    per_id = json.loads(expected[prefix+'evidence/author/per-id.json'])
    encoded_per_id = json.dumps(per_id, ensure_ascii=False)
    assert all(rid in encoded_per_id for rid in contract['required_ids'])
    folder.mkdir(parents=True, exist_ok=False)
    mirror_paths = {row['path']: row for row in mirrors}
    files = []
    for path, data in expected.items():
        row = {'path': path, **ident(data), 'git_mode': modes[path], 'role': 'candidate_mirror' if path in mirror_paths else 'author_evidence', 'base_B_identity_or_explicit_new_file': mirror_paths[path]['base_B_identity_or_explicit_new_file'] if path in mirror_paths else 'NEW_AUTHOR_EVIDENCE_FILE'}
        if path in mirror_paths:
            row.update(formal_target=mirror_paths[path]['formal_target'], write_classification=mirror_paths[path]['write_classification'])
        files.append(row)
    write_json(folder/'remote-readback.json', {'schema': 'r7.author-wave-actual-full-byte-readback.v1', 'candidate_commit': commit, 'candidate_tree': task['candidate_tree'], 'files': remote, 'counts': {'files': len(files), 'bytes': total}, 'local_exact_bytes': str(local), 'qualification': 'Complete immutable HTTP bytes equal actual Git blobs; no semantic PASS or execution credit.'})
    (folder/'mirror-diffs.patch').write_text(''.join(patches))
    freeze = {'schema': 'r7.actual-candidate-input-freeze.v1', 'batch_id': bid, 'review_round': task['review_round'], 'freeze_version': task['freeze_version'], 'required_ids': contract['required_ids'], 'fixed_B': B, 'original_contract_commit_path_identity': {'commit': C, 'path': contract_path, **ident(contract_bytes)}, 'author_task_id': task['author_identifier'], 'author_context_and_qualification': {'parent_supplied_task_identifier': task['author_identifier'], 'internal_context': 'Not inferred across heterogeneous author evidence; actual report/per-ID/context files fully retained.', 'qualification': 'External task/result mapping supplied by parent. Read exact author evidence to preserve exposed or NOT_EXPOSED internal identity, never equate opaque IDs by role name.'}, 'author_output_branch': task['branch'], 'candidate_commit': commit, 'candidate_tree': task['candidate_tree'], 'complete_diff_against_B': [{'status': a, 'path': b} for a,b in diff], 'candidate_and_author_evidence_file_identities': files, 'counts': {'files': len(files), 'bytes': total, 'mirrors': len(mirrors), 'evidence': len(files)-len(mirrors)}, 'parent_byte_count_or_qualification': task['expected_bytes_parent'] if task['expected_bytes_parent'] is not None else 'Not supplied by parent; exact immutable Git sum and complete HTTP comparison independently computed here.', 'author_manifest_coverage': {'validated_declared_files': validated, 'nonself_without_individual_identity_in_author_manifest': undeclared, 'qualification': 'All declared identities were checked. Root exhaustive actual file table binds every file including manifest and any evidence the author explicitly bound only through final commit/tree/readback. No claim that original manifest listed more than it did; reviewer must assess administrative completeness.'}, 'conditional_sync_justifications': 'Read exact author per-ID/report and original contract; conditional targets are not automatically optional adoption.', 'input_reception_complete': True, 'complete_candidate_remote_readback': str((folder/'remote-readback.json').relative_to(PROJECT)), 'mirror_diff_evidence': str((folder/'mirror-diffs.patch').relative_to(PROJECT)), 'freeze_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'unmet_dependencies': ['New independent ultra candidate review of this exact version', 'R7-I clause-level integration/shared receivers', 'Fresh R7-IR of actual cumulative integrated bytes', 'Formal acceptance and exact dependencies/regressions before closure'], 'requested_and_effective_configuration_qualification': {'requested_author': 'gpt-6.1-sol xhigh/default normal speed; Fast forbidden', 'effective_author': 'UNVERIFIED', 'requested_reviewer': 'gpt-6.1-sol ultra/default normal speed; Fast forbidden', 'effective_reviewer': 'NOT_CREATED_UNVERIFIED'}, 'execution': {'behavior_vectors': 'NOT_EXECUTED', 'root_checks': 'TOOL_VALIDATION: complete bytes, mode, scope, manifest declarations and B identity only', 'new_reference_model_host_Demo_native_media_save_replay': 0}, 'L01_L14': 'RETAINED', 'candidate_semantic_PASS': False, 'integrated_PASS': False, 'ACCEPTED': False, 'CLOSED': False, 'self_binding': 'Own freeze commit/tree provided by successor exact reviewer dispatch, never guessed.'}
    if bid == 'R7-U01':
        freeze['previous_failed_candidate_retained'] = {'candidate': 'de550bb9fe5d2b80312b1a4f6f166d2a6aa5fc67', 'freeze_commit': '58c6427f2ba48aa7dd3b59d4ab1e40c54394fd3a', 'review_commit': '1a479cf49386a0aabe2ccd96aef92abb16620143', 'verdicts': {'GR7-M01-001': 'PASS_SCOPED_CANDIDATE_OLD_VERSION_ONLY', 'GR7-J01-001': 'FAIL_SCOPED_CANDIDATE'}, 'requirement': 'Review repaired current full candidate, correction and legal existing/default4000/missing record counterexamples. No old PASS carried to this version; no old U01 integration.'}
    write_json(folder/'candidate-input.json', freeze)
    artifacts = [{'repository': REPO, 'commit': commit, 'path': row['path'], 'local_path': 'candidate/'+row['path'], 'bytes': row['bytes'], 'sha256': row['sha256'], 'git_blob_content_id': row['git_blob']} for row in files]
    write_json(folder/'candidate-restore'/f'{bid}.json', {'schema': 'r7.bounded-candidate-byte-restore.v1', 'batch_id': bid, 'contract_commit': C, 'evidence_publication_commit': commit, 'unresolved_reference_fields': [], 'artifacts': artifacts, 'evidence': [], 'fixed_read_inputs': [], 'future_paths_not_downloaded': [], 'qualification': 'Actual full frozen candidate bytes only. Original source/contract recovery is separate; no semantic credit.'})
    return {'batch_id': bid, 'review_round': task['review_round'], 'candidate_commit': commit, 'candidate_tree': task['candidate_tree'], 'candidate_input_path': str((folder/'candidate-input.json').relative_to(PROJECT)), 'restore_plan_path': str((folder/'candidate-restore'/f'{bid}.json').relative_to(PROJECT)), 'files': len(files), 'bytes': total, 'mirrors': len(mirrors), 'manifest_nonself_identity_deferrals': len(undeclared), 'author_identifier': task['author_identifier'], 'candidate_PASS': False}


def main():
    config = json.loads((P/'intake/20261015-author-wave/parent-receipt.json').read_bytes())
    results = []
    errors = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        futures = {pool.submit(receive, task): task for task in config['entries']}
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                results.append(result)
                print(json.dumps(result), flush=True)
            except Exception as error:
                task = futures[future]
                entry = {'batch_id': task['batch_id'], 'candidate_commit': task['candidate_commit'], 'error': str(error), 'type': type(error).__name__}
                errors.append(entry)
                print(json.dumps(entry), flush=True)
    write_json(P/'intake/20261015-author-wave/reception-summary.json', {'schema': 'r7.author-wave-reception-summary.v1', 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'results': sorted(results, key=lambda x:x['batch_id']), 'errors': errors, 'tasks_created_here': 0, 'semantic_PASS': False})
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
