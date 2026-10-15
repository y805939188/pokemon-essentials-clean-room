"""Independent R7-U09 byte/scope audit. Does not execute reference or author code.

All semantic conclusions belong to report.md/per-id.json, not this audit.
Only reviewer evidence files in this directory may be produced by this script.
"""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import re
import subprocess

ROOT = Path('/workspace/r7-u09-reviewer-checkout')
OUT = Path(__file__).resolve().parent
CONTEXT = Path('/workspace/r7-context/R7-U09-reviewer')
BOOT = Path('/workspace/r7-review-bootstrap/R7-U09-r1')
INPUT = Path('/workspace/r7-review-input/R7-U09-r1-fe8219b851363860704048642ff30f4fa1e31f97')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
C = 'fe8219b851363860704048642ff30f4fa1e31f97'
F = 'aa369555b0e8b6c8b077f964b54ed63d3b924f26'
D = '95c260d8f3fb4a171675dde877137fcd4c2f1c8d'
PREFIX = 'candidates/R7-U09/'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


def check(data, expected):
    actual = identity(data)
    for k, v in actual.items():
        key = 'git_blob_content_id' if k == 'git_blob' and 'git_blob_content_id' in expected else k
        if key in expected:
            assert expected[key] == v, (key, expected[key], v)
    return actual


def load(path):
    return json.loads(path.read_bytes())


def pointer(obj, value):
    for k in value.strip('/').split('/'):
        k = k.replace('~1', '/').replace('~0', '~')
        obj = obj[int(k)] if isinstance(obj, list) else obj[k]
    return obj


def audit():
    assert git('rev-parse', C + '^{tree}').decode().strip() == 'd2634c926b236d38896b809651343cae67dd0f5b'
    assert git('rev-parse', F + '^{tree}').decode().strip() == '08bd0f362c74ef7645b5bbd70b557489c122ae29'
    assert git('rev-parse', D + '^{tree}').decode().strip() == '577c350364bb4e2eb712325a9095d53d29eeeeb3'
    assert git('rev-parse', B + ':deliverables/final-specification-set').decode().strip() == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
    freeze_path = 'review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U09/'
    for name in ['candidate-input.json', 'remote-readback.json', 'mirror-diffs.patch']:
        assert (BOOT / 'freeze' / name).read_bytes() == git('show', F + ':' + freeze_path + name)
    assert (BOOT / 'reviewer-dispatch.md').read_bytes() == git('show', D + ':' + freeze_path + 'reviewer-dispatch.md')
    freeze = load(BOOT / 'freeze/candidate-input.json')
    assert freeze['input_reception_complete'] and freeze['candidate_commit'] == C
    actual_diff = [dict(zip(['status', 'path'], line.split('\t'))) for line in git('diff', '--name-status', B, C).decode().splitlines()]
    assert actual_diff == freeze['complete_diff_against_B']
    assert len(actual_diff) == 13 and all(r['status'] == 'A' and r['path'].startswith(PREFIX) for r in actual_diff)
    files = []
    for row in freeze['candidate_and_author_evidence_file_identities']:
        p = row['path']; data = (INPUT / 'candidate' / p).read_bytes()
        actual = check(data, row)
        mode, typ, blob_path = git('ls-tree', C, '--', p).decode().strip().split(' ', 2)
        blob, got_path = blob_path.split('\t')
        assert (mode, typ, blob, got_path) == ('100644', 'blob', actual['git_blob'], p)
        assert data == git('show', C + ':' + p)
        files.append({'path': p, 'mode': mode, **actual, 'frozen_identity_and_actual_git_blob_equal': True})
    assert len(files) == 13 and sum(r['bytes'] for r in files) == 357409
    manifest = load(INPUT / 'candidate' / PREFIX / 'evidence/author/artifact-manifest.json')
    for row in manifest['files']:
        check((INPUT / 'candidate' / row['path']).read_bytes(), row['identity'])
    assert len(manifest['files']) == 12
    restored = []
    for plan_path, dest in [(Path('/workspace/r7-bootstrap/R7-U09-reviewer/recovery/batches/R7-U09.json'), CONTEXT),
                            (BOOT / 'candidate-restore/R7-U09.json', INPUT)]:
        plan = load(plan_path); rows = plan['artifacts'] + plan['evidence'] + plan['fixed_read_inputs']
        for row in rows:
            check((dest / row['local_path']).read_bytes(), row)
        restored.append({'destination': str(dest), 'files': len(rows), 'bytes': sum(r['bytes'] for r in rows)})
    mirrors = []; changes = []
    allowed_targets = {row['path'] for row in load(CONTEXT / 'dispatch/delegation/contracts/R7-U09.json')['paths']}
    for row in freeze['candidate_and_author_evidence_file_identities']:
        if row['role'] != 'candidate_mirror':
            continue
        p = row['formal_target']; assert p in allowed_targets
        base = git('show', B + ':' + p)
        assert base == (CONTEXT / 'inputs/project' / p).read_bytes()
        check(base, row['base_B_identity_or_explicit_new_file'])
        candidate = (INPUT / 'candidate' / row['path']).read_bytes()
        original_lines = base.splitlines(keepends=True); lines = candidate.splitlines(keepends=True)
        reconstructed = []
        for line in lines:
            if p.endswith('wp62-pokedex-records-regions-and-content.md'):
                if line.startswith('| 摘要打开的完整单条图鉴 |'.encode()):
                    continue
                if line.startswith('| 战斗包装·实际出场登记'.encode()):
                    line = original_lines[37]
            elif p.endswith('wp66-b-storage-and-pokedex-ui.md'):
                if line.startswith('- **摘要「View Pokédex」**'.encode()):
                    line = original_lines[253]
            else:
                if re.match(rb'\| GR7-M14-00[12]-C[1-7] \|', line):
                    continue
                if line.startswith('## PD：'.encode()):
                    line = original_lines[116]
            reconstructed.append(line)
        assert b''.join(reconstructed) == base, p
        for tag, a, b, c, d in difflib.SequenceMatcher(a=original_lines, b=lines, autojunk=False).get_opcodes():
            if tag != 'equal':
                changes.append({'path': p, 'operation': tag, 'B_lines': [a + 1, b], 'candidate_lines': [c + 1, d]})
        mirrors.append({'path': row['path'], 'baseline': identity(base), 'candidate': identity(candidate),
                        'outside_exact_authorized_edits_is_byte_identical_to_B': True})
    contract = load(CONTEXT / 'dispatch/delegation/contracts/R7-U09.json')
    raw_by_sha = {p.stem: p.read_bytes() for p in (CONTEXT / 'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs').glob('*.raw')}
    checked = {}
    def walk(x):
        if isinstance(x, dict):
            if 'raw_member_byte_offsets' in x:
                key = (x['input_sha256'], x['json_pointer'])
                raw = raw_by_sha[key[0]]; lo, hi = x['raw_member_byte_offsets']; part = raw[lo:hi]
                assert len(part) == x['raw_member_bytes']
                assert hashlib.sha256(part).hexdigest() == x['raw_member_sha256']
                assert json.loads(part) == pointer(json.loads(raw), key[1])
                checked[key] = {'input_sha256': key[0], 'pointer': key[1], 'bytes': len(part),
                                'sha256': hashlib.sha256(part).hexdigest(), 'slice_and_parsed_member_equal': True}
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(contract)
    assert len(checked) == 12
    vectors = load(INPUT / 'candidate' / PREFIX / 'evidence/author/per-id.json')
    catalog = next(r for r in files if '/test-catalog/' in r['path'])
    lines = (INPUT / 'candidate' / catalog['path']).read_text().splitlines()
    vector_rows = []
    for record in vectors['records']:
        for v in record['vectors']:
            assert v['execution'] == 'NOT_EXECUTED' and 'NOT_EXECUTED' in v['candidate_row']
            assert lines[v['candidate_line'] - 1] == v['candidate_row']
            assert sum(line.startswith('| ' + v['id'] + ' |') for line in lines) == 1
            vector_rows.append({'id': v['id'], 'line': v['candidate_line'], 'execution': 'NOT_EXECUTED'})
    assert len(vector_rows) == 14
    index = load(CONTEXT / 'evidence/tasks/R7-C13/identity-index.json')['identities']
    by_path = {r['path']: r for r in index if r.get('repository_id') == 'reference'}
    selected_tree = load(BOOT / 'selected-reference-tree.json')
    assert selected_tree['tree'] == '7589c800b61ba13a13040ed0d686979b80a84fd0'
    tree_rows = {r['path']: r for r in selected_tree['files']}
    extra = []
    for p in sorted((BOOT / 'supplemental-reference').rglob('*')):
        if p.is_file():
            relative = p.relative_to(BOOT / 'supplemental-reference').as_posix()
            actual = identity(p.read_bytes())
            entry = tree_rows[relative]
            assert (actual['git_blob'], actual['bytes']) == (entry['sha'], entry['size'])
            assert entry['type'] == 'blob' and entry['mode'] == '100644'
            if relative in by_path:
                check(p.read_bytes(), by_path[relative])
            extra.append({'path': relative, **actual, 'fixed_reference_tree_entry_match': True,
                          'original_identity_index_match': relative in by_path})
    species = (BOOT / 'supplemental-reference/PBS/pokemon.txt').read_text(encoding='utf-8-sig')
    headers = re.findall(r'^\[([^\]]+)\]', species, re.M)
    assert headers.index('CHIKORITA') + 1 == 152
    return {'schema': 'r7.u09-reviewer-mechanical-audit.v1', 'phase': 'TOOL_VALIDATION',
            'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'result': 'CHECKS_OK',
            'dispatch_commit': D, 'freeze_commit': F, 'candidate_commit': C,
            'candidate_tree': 'd2634c926b236d38896b809651343cae67dd0f5b',
            'candidate_files': files, 'complete_B_diff': actual_diff, 'restored': restored,
            'manifest_nonself_files_checked': 12, 'mirrors': mirrors, 'changed_spans': changes,
            'raw_members': list(checked.values()), 'vector_rows': vector_rows,
            'supplemental_reference': extra, 'CHIKORITA_base_header_ordinal': 152,
            'behavior_vectors_executed': 0, 'reference_author_programs_executed': 0,
            'semantic_result': 'No semantic result is inferred from these mechanical checks.'}


if __name__ == '__main__':
    result = audit()
    (OUT / 'audit-result.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'result': result['result'], 'phase': result['phase'],
                      'candidate_files': len(result['candidate_files']),
                      'candidate_bytes': sum(r['bytes'] for r in result['candidate_files']),
                      'raw_members': len(result['raw_members']), 'vector_rows': len(result['vector_rows']),
                      'reference_author_programs_executed': 0, 'behavior_vectors_executed': 0}, ensure_ascii=False))
