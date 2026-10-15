"""Reviewer-owned byte/range audit; never imports or runs restored programs."""
import datetime
import difflib
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path('/workspace/r7-u07-reviewer-r1')
OUT = ROOT / 'candidates/R7-U07/evidence/reviewer/r1'
BOOT = Path('/workspace/r7-review-bootstrap/R7-U07-r1')
CONTEXT = Path('/workspace/r7-context/R7-U07-reviewer')
INPUT = Path('/workspace/r7-review-input/R7-U07-r1-2649ed2bd2cc3afdfa636cd643fc1975de5eae32')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
C = '2649ed2bd2cc3afdfa636cd643fc1975de5eae32'
F = 'aa369555b0e8b6c8b077f964b54ed63d3b924f26'
D = '95c260d8f3fb4a171675dde877137fcd4c2f1c8d'


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def check(data, expected):
    actual = identity(data)
    for key in actual:
        other = expected.get(key, expected.get('git_blob_content_id') if key == 'git_blob' else None)
        if other is not None:
            assert actual[key] == other, (key, actual[key], other)
    return actual


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def walk(obj):
    if isinstance(obj, dict):
        yield obj
        for value in obj.values():
            yield from walk(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from walk(value)


def main():
    assert git('branch', '--show-current').decode().strip() == 'codex/r7-u07-reviewer-20261015-r1'
    freeze = json.loads((BOOT / 'candidate-input.json').read_text())
    assert git('rev-parse', F + '^{tree}').decode().strip() == '08bd0f362c74ef7645b5bbd70b557489c122ae29'
    assert git('rev-parse', C + '^{tree}').decode().strip() == freeze['candidate_tree']
    assert git('rev-parse', B + ':deliverables/final-specification-set').decode().strip() == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
    prefix = 'review/remediation-seventh-20261015-prepare/'
    bootstrap = []
    for rel, remote in [('reviewer-dispatch.md', 'candidate-freezes/R7-U07/reviewer-dispatch.md'),
                        ('candidate-freeze-requirements.json', 'delegation/parallel-dispatch/candidate-freeze-requirements.json')]:
        data = (BOOT / rel).read_bytes()
        assert data == git('show', D + ':' + prefix + remote)
        bootstrap.append({'commit': D, 'path': prefix + remote, **identity(data)})
    for rel in ['candidate-input.json', 'candidate-restore/R7-U07.json', 'mirror-diffs.patch', 'remote-readback.json']:
        data = (BOOT / rel).read_bytes()
        assert data == git('show', F + ':' + prefix + 'candidate-freezes/R7-U07/' + rel)
        bootstrap.append({'commit': F, 'path': prefix + 'candidate-freezes/R7-U07/' + rel, **identity(data)})
    for rel in ['tools/restore_container_context.py', 'recovery/batches/R7-U07.json', 'recovery/independent-containers.md']:
        data = (Path('/workspace/r7-bootstrap/R7-U07-reviewer') / rel).read_bytes()
        assert data == git('show', '658488c81f1f3181a488298ab27850c8af951d73:' + prefix + rel)
        bootstrap.append({'commit': '658488c81f1f3181a488298ab27850c8af951d73', 'path': prefix + rel, **identity(data)})
    changed = [dict(zip(['status', 'path'], row.split('\t', 1))) for row in git('diff', '--name-status', B, C).decode().splitlines()]
    assert changed == freeze['complete_diff_against_B']
    assert len(changed) == 32 and all(row['status'] == 'A' and row['path'].startswith('candidates/R7-U07/') for row in changed)
    candidate_files = []
    modes = {}
    for row in git('ls-tree', '-r', C, 'candidates/R7-U07').decode().splitlines():
        meta, path = row.split('\t'); mode, typ, blob = meta.split(); modes[path] = (mode, typ, blob)
    for expected in freeze['candidate_and_author_evidence_file_identities']:
        path = expected['path']; data = (INPUT / 'candidate' / path).read_bytes()
        actual = check(data, expected)
        assert data == git('show', C + ':' + path)
        assert modes[path] == ('100644', 'blob', actual['git_blob'])
        candidate_files.append({'path': path, **actual, 'mode': modes[path][0], 'raw_vs_actual_git_bytes': True})
    assert len(candidate_files) == 32 and sum(row['bytes'] for row in candidate_files) == 241426
    root_readback = json.loads((BOOT / 'remote-readback.json').read_text())
    assert root_readback['candidate_commit'] == C and root_readback['candidate_tree'] == freeze['candidate_tree']
    assert {row['path'] for row in root_readback['files']} == set(modes)
    for row in root_readback['files']:
        check((INPUT / 'candidate' / row['path']).read_bytes(), row)
        assert row['git_mode'] == '100644'
    original_plan = json.loads(Path('/workspace/r7-bootstrap/R7-U07-reviewer/recovery/batches/R7-U07.json').read_text())
    restored = []
    for expected in original_plan['artifacts'] + original_plan['evidence'] + original_plan['fixed_read_inputs']:
        data = (CONTEXT / expected['local_path']).read_bytes()
        restored.append({'local_path': expected['local_path'], **check(data, expected)})
    assert len(restored) == 23 and sum(row['bytes'] for row in restored) == 5526711
    author = INPUT / 'candidate/candidates/R7-U07/evidence/author'
    manifest = json.loads((author / 'artifact-manifest.json').read_text())
    for row in manifest['files']:
        check((INPUT / 'candidate' / row['path']).read_bytes(), row['after'])
        if row.get('baseline_path'):
            check(git('show', B + ':' + row['baseline_path']), row['before'])
    assert len(manifest['files']) == 31
    assert {row['path'] for row in manifest['files']} | {'candidates/R7-U07/evidence/author/artifact-manifest.json'} == {row['path'] for row in candidate_files}
    author_id = json.loads((author / 'per-id.json').read_text())['actual_context']['thread_id']
    reviewer_id = os.environ.get('CODEX_THREAD_ID', 'NOT_EXPOSED')
    assert author_id == freeze['author_task_id'] == '01a13f7f-7ae8-735b-86d1-876a3b9fe03b'
    assert reviewer_id == '01a13ff0-841d-7542-9d3a-d87b0e0cb00d' and author_id != reviewer_id
    changes = []
    for expected in freeze['candidate_and_author_evidence_file_identities'][:2]:
        old = git('show', B + ':' + expected['formal_target'])
        new = (INPUT / 'candidate' / expected['path']).read_bytes()
        check(old, expected['base_B_identity_or_explicit_new_file'])
        ops = [list(row) for row in difflib.SequenceMatcher(None, old.splitlines(keepends=True), new.splitlines(keepends=True), autojunk=False).get_opcodes() if row[0] != 'equal']
        changes.append({'formal_target': expected['formal_target'], 'before': identity(old), 'after': identity(new), 'zero_based_half_open_line_opcodes': ops})
    assert changes[0]['zero_based_half_open_line_opcodes'] == [['replace', 92, 93, 92, 95], ['replace', 123, 124, 125, 126]]
    assert changes[1]['zero_based_half_open_line_opcodes'] == [['insert', 103, 103, 103, 116]]
    contract = json.loads((CONTEXT / 'dispatch/delegation/contracts/R7-U07.json').read_text())
    raw_root = CONTEXT / 'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs'
    refs = {}
    for row in walk(contract):
        if all(key in row for key in ['input_sha256', 'raw_member_byte_offsets', 'raw_member_sha256', 'json_pointer']):
            refs[(row['input_sha256'], row['json_pointer'])] = row
    checked_refs = []
    for (digest, pointer), row in refs.items():
        raw = (raw_root / (digest + '.raw')).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest
        lo, hi = row['raw_member_byte_offsets']; member = raw[lo:hi]
        assert len(member) == row['raw_member_bytes']
        assert hashlib.sha256(member).hexdigest() == row['raw_member_sha256']
        obj = json.loads(raw)
        for part in pointer.lstrip('/').split('/'):
            part = part.replace('~1', '/').replace('~0', '~')
            obj = obj[int(part)] if isinstance(obj, list) else obj[part]
        assert json.loads(member) == obj
        canonical = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
        assert hashlib.sha256(canonical).hexdigest() == row['canonical_sha256']
        checked_refs.append({'pointer': pointer, 'input_sha256': digest, 'byte_offsets': [lo, hi], 'bytes': len(member), 'raw_sha256': row['raw_member_sha256'], 'canonical_and_raw_checked': True})
    assert len(checked_refs) == 6
    for p in author.rglob('*.json'):
        json.loads(p.read_text())
    skills = {'accessible_paths': {}, 'fixed_dispatch_git_paths': git('ls-tree', '-r', '--name-only', D, '.agents', '.codex').decode().splitlines()}
    for p in ['/workspace/.agents/skills', '/workspace/pokemon-essentials-clean-room/.agents/skills', '/home/agent/.agents/skills']:
        skills['accessible_paths'][p] = 'PRESENT' if Path(p).exists() else 'ABSENT'
    result = {'schema': 'r7.u07.reviewer-byte-audit.v1', 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'pid': os.getpid(), 'reviewer_context': reviewer_id, 'author_context': author_id,
              'result': 'TOOL_VALIDATION_PASS', 'semantic_verdict_by_this_script': False, 'behavior_execution': 'NOT_EXECUTED',
              'bootstrap': bootstrap, 'candidate_commit': C, 'candidate_tree': freeze['candidate_tree'],
              'complete_diff_against_B': changed, 'candidate_files': candidate_files,
              'candidate_files_count': len(candidate_files), 'candidate_bytes': 241426,
              'original_restored_files': restored, 'original_files_count': 23, 'original_bytes': 5526711,
              'author_manifest_declared_nonself_count': 31, 'author_manifest_self_bound_by_fixed_commit': True,
              'mirror_changes': changes, 'existing_catalog_bytes_preserved': True,
              'raw_binding_checks': checked_refs, 'skills_probe': skills}
    dump('receipts/byte-audit.json', result)
    print(json.dumps({key: result[key] for key in ['result', 'reviewer_context', 'author_context', 'candidate_files_count', 'candidate_bytes', 'original_files_count', 'original_bytes', 'existing_catalog_bytes_preserved']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
