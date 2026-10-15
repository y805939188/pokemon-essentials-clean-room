"""Bounded file/document audit only; never execute reference or behavior models."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

REPO = Path(__file__).resolve().parents[4]
ROOT = REPO / 'candidates/R7-U09'
CTX = Path('/workspace/r7-context/R7-U09-author')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'


def ident(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)


def main():
    contract = json.loads((CTX / 'dispatch/delegation/contracts/R7-U09.json').read_bytes())
    assert git('branch', '--show-current').decode().strip() == 'codex/r7-u09-author-20261015-wave1'
    assert git('rev-parse', B + ':deliverables/final-specification-set').decode().strip() == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
    mirrors = []
    for row in contract['paths']:
        old = git('show', B + ':' + row['path'])
        assert old == (CTX / 'inputs/project' / row['path']).read_bytes()
        new = (REPO / row['candidate_path']).read_bytes()
        a, b = old.decode().splitlines(keepends=True), new.decode().splitlines(keepends=True)
        restored = []
        if '/pokemon-rules/' in row['path']:
            for line in b:
                if line.startswith('| 摘要打开的完整单条图鉴 |'):
                    continue
                if line.startswith('| 战斗包装·实际出场登记'):
                    line = next(x for x in a if x.startswith('| 战斗包装·出场登记'))
                restored.append(line)
        elif '/user-interface/' in row['path']:
            for line in b:
                if line.startswith('- **摘要「View Pokédex」**'):
                    line = next(x for x in a if x.startswith('- **摘要「View Pokédex」**'))
                restored.append(line)
        else:
            for line in b:
                if line.startswith('| GR7-M14-'):
                    continue
                if line.startswith('## PD：'):
                    line = next(x for x in a if x.startswith('## PD：'))
                restored.append(line)
        assert ''.join(restored).encode() == old, 'unapproved clause change: ' + row['path']
        mirrors.append({'path': row['candidate_path'], 'baseline': ident(old), 'candidate': ident(new),
                        'all_other_baseline_bytes_preserved': True})
    catalog = (ROOT / contract['paths'][1]['path']).read_text()
    per_id = json.loads((ROOT / 'evidence/author/per-id.json').read_text())
    vector_ids = []
    for record in per_id['records']:
        assert record['status'] == 'CANDIDATE_READY_NOT_REVIEWED'
        for v in record['vectors']:
            vector_ids.append(v['id'])
            assert catalog.count('| ' + v['id'] + ' |') == 1
            assert v['execution'] == 'NOT_EXECUTED'
    assert len(vector_ids) == len(set(vector_ids)) == 14
    all_paths = git('diff', '--name-only', B).decode().splitlines()
    all_paths += git('ls-files', '--others', '--exclude-standard').decode().splitlines()
    assert all(p.startswith('candidates/R7-U09/') for p in all_paths)
    allowed = {x['candidate_path'] for x in contract['paths']}
    assert all(p in allowed or p.startswith('candidates/R7-U09/evidence/author/') for p in all_paths)
    plan = json.loads(Path('/workspace/r7-bootstrap/R7-U09-author/recovery/batches/R7-U09.json').read_bytes())
    restored_count = 0
    for key in ('artifacts', 'evidence', 'fixed_read_inputs'):
        for row in plan[key]:
            actual = ident((CTX / row['local_path']).read_bytes())
            assert all(actual[k] == row[k] for k in actual)
            restored_count += 1
    assert restored_count == 25
    raw_count = 0
    seen = set()

    def raw_refs(value):
        nonlocal raw_count
        if isinstance(value, dict):
            if 'raw_member_byte_offsets' in value and 'input_sha256' in value:
                key = (value['input_sha256'], tuple(value['raw_member_byte_offsets']))
                if key not in seen:
                    seen.add(key)
                    raw = CTX / 'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs' / (key[0] + '.raw')
                    start, end = key[1]
                    data = raw.read_bytes()[start:end]
                    assert len(data) == value['raw_member_bytes']
                    assert hashlib.sha256(data).hexdigest() == value['raw_member_sha256']
                    json.loads(data)
                    raw_count += 1
            for item in value.values():
                raw_refs(item)
        elif isinstance(value, list):
            for item in value:
                raw_refs(item)

    raw_refs(contract)
    assert raw_count == 12
    manifest_verified = None
    manifest_path = ROOT / 'evidence/author/artifact-manifest.json'
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        actual_paths = {str(p.relative_to(REPO)) for p in ROOT.rglob('*') if p.is_file() and p != manifest_path}
        assert actual_paths == {x['path'] for x in manifest['files']}
        for row in manifest['files']:
            assert ident((REPO / row['path']).read_bytes()) == row['identity']
        manifest_verified = len(manifest['files'])
    print(json.dumps({'phase': 'TOOL_VALIDATION', 'result': 'CHECKS_OK', 'mirrors': mirrors,
                      'preserved': ['all baseline clauses outside exact edits', 'PD24', 'PD25', 'R4-PD01–05', 'R6-PD01–03'],
                      'vector_rows': 14, 'behavior_vectors_executed': 0, 'restored_files_verified': restored_count,
                      'raw_contract_members_verified': raw_count, 'manifest_files_verified': manifest_verified,
                      'reference_execution': 0, 'host_Demo_native_media_real_save_replay': 0,
                      'semantic_review': 'NOT_PERFORMED_BY_NON_AUTHOR'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
