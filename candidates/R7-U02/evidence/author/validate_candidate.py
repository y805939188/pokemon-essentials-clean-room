"""Check candidate boundaries and unchanged historical bytes, not game behavior."""
import difflib
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
BASE = 'e646432c644dec04d306842cc5a559a29c718fbc'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def main():
    manifest = json.loads((OUT / 'mirror-identities.json').read_bytes())
    append_only = []
    for row in manifest['mirrors']:
        original = git('show', BASE + ':' + row['base_path'])
        candidate = (ROOT / row['path']).read_bytes()
        if row['base_path'].endswith('/wp17-messages-windows-input.md'):
            ops = [(tag, a, b) for tag, a, b, c, d in difflib.SequenceMatcher(
                None, original.splitlines(True), candidate.splitlines(True), autojunk=False).get_opcodes() if tag != 'equal']
            assert ops == [('replace', 166, 167), ('replace', 265, 266)], ops
        else:
            assert candidate.startswith(original)
            append_only.append(row['base_path'])
        assert (ROOT / row['base_path']).read_bytes() == original
    assert git('diff', '--name-only', BASE, '--', '.', ':!candidates/R7-U02/').strip() == b''
    assert not git('diff', '--name-only', '--', '.', ':!candidates/R7-U02/').strip(), 'Tracked baseline files must remain untouched'
    extra_untracked = git('ls-files', '--others', '--exclude-standard').decode().splitlines()
    assert all(x.startswith('candidates/R7-U02/') for x in extra_untracked), extra_untracked
    for p in (ROOT / 'candidates/R7-U02').rglob('*'):
        assert not p.is_symlink()
    wp = (ROOT / 'candidates/R7-U02/deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md').read_text()
    assert '每个交互正常结束后' not in wp
    assert '这些清理只位于正常出口' in wp
    assert '### 3.3.1 局部两行消息入口与业务前缀' in wp
    assert 'CC04 实际注册/宿主查询桥仍未读' in wp
    assert 'bindingNames' in wp and '只供显示' in wp
    binary = json.loads((OUT / 'binary-static.json').read_bytes())
    for category, marker in [('buttons', '| 按钮（15）'), ('axes', '| 轴（6）')]:
        line = next(x for x in wp.splitlines() if x.startswith(marker))
        assert re.findall(r'`([^`]+)`', line) == [x['name'] for x in binary['vocabularies'][category]]
    per_id = json.loads((OUT / 'per-id.json').read_bytes())
    vectors = [v for r in per_id['records'] for v in r['candidate_vectors']]
    assert len(vectors) == 51
    assert all(v['execution'] == 'NOT_EXECUTED' and v['non_author_semantic_review'] == 'PENDING' for v in vectors)
    assert [len(r['candidate_vectors']) for r in per_id['records']] == [12, 13, 26]
    assert per_id['context']['actual_context_thread_id'] == '01a13f7f-17e2-7472-80c4-d2b7eac2703d'
    assert per_id['context']['effective_configuration'] == {k: 'UNVERIFIED' for k in ['model', 'effort', 'service_tier', 'speed']}
    assert all(all(x == 'OPEN_NOT_REACHED' for x in r['gates'].values()) for r in per_id['records'])
    formal = git('rev-parse', 'HEAD:deliverables/final-specification-set').decode().strip()
    assert formal == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
    results = {'qualification': 'AUTHOR_TOOL_VALIDATION_ONLY; not independent semantic PASS or closure.',
               'mirrors': 4, 'append_only_originals_exact': append_only,
               'WP17_changed_base_lines': [167, 266], 'all_other_WP17_bytes_preserved': True,
               'formal_files_changed': 0, 'candidate_vector_rows': 51,
               'vector_rows_per_record': [12, 13, 26], 'all_vectors_execution': 'NOT_EXECUTED',
               'old_catalog_rows_and_matrix_audit_bytes_exact_prefix': True,
               'formal_tree_unchanged': formal, 'effective_configuration': 'UNVERIFIED',
               'status': 'CHECKS_COMPLETED', 'semantic_acceptance': False}
    (OUT / 'validation.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(results, ensure_ascii=False))


if __name__ == '__main__':
    main()
