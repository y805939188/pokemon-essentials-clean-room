"""Check candidate identity, exact edit boundaries and unchanged controls.

This checks documents and Git objects. It executes no reference code, game,
behavior model, animation, native media, or save replay.
"""
import difflib
import hashlib
import json
from pathlib import Path
import subprocess

B = 'e646432c644dec04d306842cc5a559a29c718fbc'
ROOT = Path(__file__).resolve().parents[2]
CONTEXT = Path('/workspace/r7-context/R7-U08-author')


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


def git(*args):
    return subprocess.check_output(['git', *args])


def main():
    plan = json.loads(Path('/workspace/r7-bootstrap/R7-U08-author/recovery/batches/R7-U08.json').read_bytes())
    for row in plan['artifacts'] + plan['evidence'] + plan['fixed_read_inputs']:
        assert identity((CONTEXT / row['local_path']).read_bytes()) == {
            k: row[k] for k in ('bytes', 'sha256', 'git_blob_content_id')}
    contract = json.loads((CONTEXT / 'dispatch/delegation/contracts/R7-U08.json').read_bytes())
    results = []
    for row in contract['paths']:
        p = row['path']
        old = git('show', f'{B}:{p}')
        new = (ROOT / p).read_bytes()
        assert old == (CONTEXT / 'inputs/project' / p).read_bytes()
        a, b = old.decode().splitlines(keepends=True), new.decode().splitlines(keepends=True)
        edits = [v for v in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes() if v[0] != 'equal']
        if 'test-catalog/' in p:
            assert edits == [('insert', 398, 398, 398, 402), ('replace', 439, 440, 443, 444)], edits
            for i in range(1, 5):
                assert new.decode().count(f'| R7-U08-HP0{i} |') == 1
                assert 'NOT_EXECUTED' in b[397 + i]
            # The entire original catalogue except L13 remains byte-identical.
            assert [l for l in a if not l.startswith('| L13 |')] == [
                l for l in b if not l.startswith(('| L13 |', '| R7-U08-HP'))]
            assert '双满提示返回亦清' in b[443]
            assert '仅尚有下一组合格时询问' in b[443]
            assert '统一净化正常返回后才通用存放' in b[443]
            assert '通用存放正常返回后清中心' in b[443]
        elif 'wp67-a-' in p:
            assert edits == [('replace', 195, 196, 195, 196), ('replace', 246, 248, 246, 248)], edits
            for i in (195, 247):
                assert a[i].replace('闪白', '闪光') == b[i]
            assert 'h≤⌊T/4⌋' in b[246] and 'h≤⌊T/2⌋' in b[246]
            assert '当下显示 HP（补间中可为小数）' in b[246]
            assert '不先把 h 取整' in b[246] and '不以最终实际 HP 代替 h' in b[246]
            for i in range(len(a)):
                if i not in (195, 246, 247):
                    assert a[i] == b[i]
        else:
            assert edits == [('replace', 140, 141, 140, 141)], edits
            assert '先于逐成员视觉演出' in b[140]
            assert '逻辑播放请求，正常返回后才登记' in b[140]
            for i in range(len(a)):
                if i != 140:
                    assert a[i] == b[i]
        for _, _, _, lo, hi in edits:
            assert all(line.rstrip('\n\r') == line.rstrip() for line in b[lo:hi])
        results.append({'path': p, 'base': identity(old), 'candidate': identity(new),
                        'edit_opcodes_zero_based_half_open': edits})
    assert git('branch', '--show-current').decode().strip() == 'codex/r7-u08-author-20261015-wave1'
    assert git('rev-parse', 'HEAD:deliverables/final-specification-set').decode().strip() == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
    paths = git('diff', '--name-only', B).decode().splitlines() + git('ls-files', '--others', '--exclude-standard').decode().splitlines()
    assert paths and all(p.startswith('candidates/R7-U08/') for p in paths)
    assert git('diff', B, '--', 'deliverables', 'audit', 'reference', 'AGENTS.md') == b''
    print(json.dumps({'qualification': 'TOOL_VALIDATION_ONLY', 'restored_files_verified': 39,
                      'exact_document_boundaries_verified': True, 'formal_bytes_unchanged': True,
                      'reference_execution': 0, 'behavior_vector_execution': 'NOT_EXECUTED',
                      'files': results}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
