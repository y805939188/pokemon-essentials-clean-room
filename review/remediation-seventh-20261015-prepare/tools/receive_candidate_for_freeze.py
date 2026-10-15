"""Receive exact candidate bytes and scope for independent review; no semantic PASS."""
import argparse
import concurrent.futures
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

PROJECT = Path(__file__).resolve().parents[3]
ROOT = Path(__file__).resolve().parents[1]
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
CONTRACT = 'f622356f3beb9e84ea8cff9db07c7fb382565d3f'
REPOSITORY = 'y805939188/pokemon-essentials-clean-room'


def git(*args):
    return subprocess.check_output(['git', '-C', str(PROJECT), *args])


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}


def match(data, declared):
    actual = identity(data)
    expected = {'bytes': declared['bytes'], 'sha256': declared['sha256'],
                'git_blob': declared.get('git_blob', declared.get('git_blob_content_id'))}
    assert actual == expected, (actual, expected)
    return actual


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('x') as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch', required=True)
    parser.add_argument('--candidate', required=True)
    parser.add_argument('--expected-tree', required=True)
    parser.add_argument('--author-identifier', required=True)
    parser.add_argument('--branch', required=True)
    parser.add_argument('--expected-files', type=int, required=True)
    parser.add_argument('--expected-bytes', type=int, required=True)
    args = parser.parse_args()
    bid = args.batch
    prefix = f'candidates/{bid}/'
    contract_path = f'review/remediation-seventh-20261015-prepare/delegation/contracts/{bid}.json'
    contract_bytes = git('show', CONTRACT+':'+contract_path)
    contract = json.loads(contract_bytes)
    allowed = {row['candidate_path']: row for row in contract['paths']}
    tree = git('rev-parse', args.candidate+'^{tree}').decode().strip()
    assert tree == args.expected_tree
    tip = git('ls-remote', 'origin', 'refs/heads/'+args.branch).decode().strip()
    assert tip.split()[0] == args.candidate
    assert subprocess.run(['git', '-C', str(PROJECT), 'merge-base', '--is-ancestor', B, args.candidate]).returncode == 0
    raw = git('diff', '--name-status', '--no-renames', '-z', B, args.candidate).decode().strip('\0').split('\0')
    changes = list(zip(raw[::2], raw[1::2]))
    assert len(raw) == 2*len(changes) and len(changes) == args.expected_files
    assert all(status == 'A' and path.startswith(prefix) for status, path in changes)
    assert all(path in allowed or path.startswith(prefix+'evidence/author/') for _, path in changes)
    expected = {path: git('show', args.candidate+':'+path) for _, path in changes}
    assert sum(map(len, expected.values())) == args.expected_bytes
    local = Path('/workspace/r7-candidate-reception') / (bid+'-'+args.candidate)
    local.mkdir(parents=True, exist_ok=False)

    def receive(path):
        url = f'https://raw.githubusercontent.com/{REPOSITORY}/{args.candidate}/'+urllib.parse.quote(path)
        attempts = []
        for attempt in range(1, 4):
            start = datetime.datetime.now(datetime.timezone.utc).isoformat()
            try:
                with urllib.request.urlopen(url, timeout=40) as response:
                    data = response.read(len(expected[path])+1)
                    status = response.status
                assert data == expected[path], path
                attempts.append({'attempt': attempt, 'start_utc': start, 'http_status': status, 'complete_byte_match': True})
                target = local/path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                return {'path': path, **identity(data), 'url': url, 'attempts': attempts}
            except (urllib.error.URLError, TimeoutError) as error:
                attempts.append({'attempt': attempt, 'start_utc': start, 'error': str(error)})
                if attempt == 3:
                    raise
                time.sleep(attempt)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        remote = list(pool.map(receive, expected))
    author_manifest_path = prefix+'evidence/author/artifact-manifest.json'
    manifest = json.loads(expected[author_manifest_path])
    assert manifest['base_commit'] == B
    declarations = manifest.get('files')
    if declarations is None:
        declarations = manifest['mirrors'] + [{'path': path, **record} for path, record in manifest['evidence_inventory'].items()]
    assert {row['path'] for row in declarations} == set(expected)-{author_manifest_path}
    for row in declarations:
        match(expected[row['path']], row.get('new_identity', row.get('candidate_identity', row)))
    mirror_rows = []
    diffs = []
    for path, data in expected.items():
        if path not in allowed:
            continue
        target = path[len(prefix):]
        original = git('show', B+':'+target)
        declaration = next(row for row in declarations if row['path'] == path)
        base = declaration.get('base_target_identity', declaration.get('base_identity'))
        match(original, base)
        mirror_rows.append({'path': path, 'formal_target': target, **identity(data), 'base_B_identity': identity(original), 'write_classification': allowed[path]['classification']})
        diffs.extend(difflib.unified_diff(original.decode().splitlines(True), data.decode().splitlines(True), fromfile='a/'+target, tofile='b/'+target))
    assert {row['path'] for row in mirror_rows} == {path for path, row in allowed.items() if row['classification'] == 'required'}
    per_id = json.loads(expected[prefix+'evidence/author/per-id.json'])
    records = per_id.get('records', [per_id])
    assert {row.get('id', row.get('record_id')) for row in records} == set(contract['required_ids'])
    assert all(row['status'] == 'CANDIDATE_READY_NOT_REVIEWED' for row in records)
    if 'actual_thread' in per_id:
        author_context = per_id['actual_thread']
        self_task_qualification = per_id.get('actual_task_id')
    elif 'task_context' in per_id:
        author_context = per_id['task_context']['actual_thread_id_from_environment']
        self_task_qualification = per_id['task_context']['platform_task_id']
    else:
        context = json.loads(expected[prefix+'evidence/author/execution-context.json'])
        author_context = context['actual_author_platform_context_id']
        self_task_qualification = context['actual_author_platform_task_id']
    internal_context_exposed = not author_context.startswith(('NOT_EXPOSED', 'UNVERIFIED'))
    if internal_context_exposed:
        assert author_context == args.author_identifier
    folder = ROOT/'candidate-freezes'/bid
    folder.mkdir(parents=True, exist_ok=False)
    (folder/'mirror-diffs.patch').write_text(''.join(diffs))
    dump(folder/'remote-readback.json', {'schema': 'r7.actual-candidate-reception.v1', 'candidate_commit': args.candidate, 'candidate_tree': tree, 'branch_tip_at_reception': tip, 'files': remote, 'counts': {'files': len(remote), 'bytes': sum(row['bytes'] for row in remote)}, 'local_exact_byte_copy': str(local), 'qualification': 'Actual independent HTTP byte reception plus scope/identity checks only. No candidate semantic PASS.'})
    file_rows = []
    mirrors = {row['path']: row for row in mirror_rows}
    for path, data in expected.items():
        row = {'path': path, **identity(data), 'role': 'candidate_mirror' if path in mirrors else 'author_evidence', 'base_B_identity_or_explicit_new_file': mirrors[path]['base_B_identity'] if path in mirrors else 'NEW_AUTHOR_EVIDENCE_FILE'}
        if path in mirrors:
            row.update(formal_target=mirrors[path]['formal_target'], write_classification=mirrors[path]['write_classification'])
        file_rows.append(row)
    conditional = per_id.get('conditional_targets', {'adopted': [], 'qualification': 'No conditional target exists for this batch'})
    context_qualification = 'Parent task identifier matches actual thread reported by author; opaque platform task ID was not exposed inside author container.' if internal_context_exposed else 'Parent provided the externally created author cloud-thread/task identifier and result linkage. Author container did not expose its internal context/task ID; do not fabricate a match. Require a separately created different reviewer cloud thread and preserve this qualification.'
    freeze = {'schema': 'r7.actual-candidate-input-freeze.v1', 'batch_id': bid, 'required_ids': contract['required_ids'], 'fixed_B': B, 'fixed_B_tree': '84f79ec6e772aacbf3a464fde68cdc5a280e2950', 'original_contract_commit_path_identity': {'commit': CONTRACT, 'path': contract_path, **identity(contract_bytes)}, 'author_task_id': args.author_identifier, 'author_context_and_qualification': {'parent_supplied_task_identifier': args.author_identifier, 'author_reported_actual_thread': author_context, 'author_local_platform_task_id_field': self_task_qualification, 'internal_context_exposed': internal_context_exposed, 'qualification': context_qualification}, 'author_output_branch': args.branch, 'candidate_commit': args.candidate, 'candidate_tree': tree, 'complete_diff_against_B': [{'status': status, 'path': path} for status, path in changes], 'candidate_and_author_evidence_file_identities': file_rows, 'counts': {'files': len(file_rows), 'bytes': sum(row['bytes'] for row in file_rows), 'mirrors': len(mirror_rows), 'evidence': len(file_rows)-len(mirror_rows)}, 'author_manifest_coverage': {'declared_other_files': len(declarations), 'self_manifest_bound_here': {'path': author_manifest_path, **identity(expected[author_manifest_path])}, 'declared_and_actual_identities_match': True}, 'conditional_sync_justifications': conditional, 'input_reception_complete': True, 'complete_candidate_remote_readback': str((folder/'remote-readback.json').relative_to(PROJECT)), 'mirror_diff_evidence': str((folder/'mirror-diffs.patch').relative_to(PROJECT)), 'unmet_dependencies': ['Different-context independent ultra candidate semantic review', 'R7-I clause-level integration and shared receiver reception', 'New independent R7-IR actual integrated commit/tree review', 'Formal acceptance and exact direct/transitive dependencies and historical regressions before CLOSED'], 'freeze_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'requested_and_effective_configuration_qualification': {'requested_author': 'gpt-6.1-sol xhigh/default normal speed; Fast forbidden', 'effective_author': 'UNVERIFIED', 'requested_reviewer': 'gpt-6.1-sol ultra/default normal speed; Fast forbidden', 'effective_reviewer': 'NOT_CREATED_UNVERIFIED'}, 'execution': {'behavior_vectors': 'NOT_EXECUTED', 'reference_or_full_model_execution_by_integrator': 0, 'host_Demo_native_media_real_save_replay': 0, 'tool_checks_here': 'Diff scope, complete transfer, byte identity and manifest binding only'}, 'L01_L14': 'RETAINED', 'candidate_semantic_PASS': False, 'integrated_PASS': False, 'ACCEPTED': False, 'CLOSED': False, 'self_binding': 'This file own publishing commit/tree is supplied externally by a successor concrete reviewer dispatch; never use a floating HEAD.'}
    dump(folder/'candidate-input.json', freeze)
    artifacts = [{'repository': REPOSITORY, 'commit': args.candidate, 'path': row['path'], 'local_path': 'candidate/'+row['path'], 'bytes': row['bytes'], 'sha256': row['sha256'], 'git_blob_content_id': row['git_blob']} for row in file_rows]
    dump(folder/'candidate-restore'/f'{bid}.json', {'schema': 'r7.bounded-candidate-byte-restore.v1', 'batch_id': bid, 'contract_commit': CONTRACT, 'evidence_publication_commit': args.candidate, 'unresolved_reference_fields': [], 'artifacts': artifacts, 'evidence': [], 'fixed_read_inputs': [], 'future_paths_not_downloaded': [], 'qualification': 'Use fixed restore_container_context.py658488c8 to restore only actual frozen candidate bytes into a new reviewer input directory. Original semantic contract/source recovery is a separate invocation.'})
    print(json.dumps({'batch': bid, 'candidate': args.candidate, 'tree': tree, 'files': len(file_rows), 'bytes': sum(row['bytes'] for row in file_rows), 'mirrors': len(mirror_rows), 'freeze_path': str(folder/'candidate-input.json'), 'candidate_semantic_PASS': False}))


if __name__ == '__main__':
    main()
