#!/usr/bin/env python3
"""Verify only the authorized source-restoration delta and preserved review history."""
from pathlib import Path, PurePosixPath
import difflib
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent
ROOT = PREVIOUS.parents[1]
OLD = 'ed66a2b7aafc9da3846d48e412b4918c147ec14a'
NEW = '67d0e170bfe775c017a6c3d5d6189b49a658981e'
OLD_REVIEW = 'b81b9cee1d3bdeed74977bf3966b911dc5e8dd10'
BASE = '8075cc7714e64fd2c170cc397d9efa94811da57b'
PREFIX = 'planning/framework-roadmap/'
REVIEW_PREFIX = 'review/framework-roadmap-v1-20261017/'
QUICK = PREFIX + 'QUICK-PLAN.md'

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def doc(ref, path):
    return git('show', f'{ref}:{path}')

def identity(data):
    return {'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest(),
            'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data), 'lines': len(data.splitlines())}

changed = git('diff', '--name-status', OLD, NEW).decode().splitlines()
assert changed == ['M\t' + QUICK], changed
assert git('diff', '--numstat', OLD, NEW).decode().splitlines() == ['1\t1\t' + QUICK]
parents = git('show', '-s', '--format=%P', NEW).decode().strip().split()
assert parents == [OLD], parents
old_text = doc(OLD, QUICK).decode('utf-8')
new_text = doc(NEW, QUICK).decode('utf-8')
source = (PREVIOUS / 'source-inputs/quick-source.txt').read_text(encoding='utf-8')
old_lines, new_lines, source_lines = old_text.splitlines(), new_text.splitlines(), source.splitlines()
assert len(old_lines) == len(new_lines) == 47
line_changes = [i + 1 for i, (a, b) in enumerate(zip(old_lines, new_lines)) if a != b]
assert line_changes == [33], line_changes
assert new_lines[32] == source_lines[19]
assert new_text == old_text.replace(old_lines[32], source_lines[19], 1)
assert '通过对照测试发现差异，就修正规格并加入回归测试；后置功能继续保留在清单中。' in new_lines[32]

documents = {}
texts = {}
for name in ['DETAILED-PLAN.md', 'QUICK-PLAN.md', 'README.md']:
    before, after = doc(OLD, PREFIX + name), doc(NEW, PREFIX + name)
    if name != 'QUICK-PLAN.md':
        assert before == after, name
    texts[name] = after.decode('utf-8')
    assert '版本：v1.0 · 日期：2026-10-17' in texts[name]
    old_meta = [x for x in before.decode('utf-8').splitlines() if x.startswith(('版本：', '配套文档：'))]
    new_meta = [x for x in texts[name].splitlines() if x.startswith(('版本：', '配套文档：'))]
    assert old_meta == new_meta, name
    documents[name] = {'old': identity(before), 'new': identity(after),
                       'byte_identical': before == after, 'document_metadata_identical': True}

links = []
for name, text in texts.items():
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', text):
        target = match.group(2)
        if target.startswith('https://'):
            assert target == f'https://github.com/y805939188/pokemon-essentials-clean-room/commit/{BASE}'
            git('cat-file', '-e', BASE + '^{commit}')
        else:
            assert target in ['DETAILED-PLAN.md', 'QUICK-PLAN.md', 'README.md']
            git('cat-file', '-e', NEW + ':' + str(PurePosixPath(PREFIX) / target))
        links.append({'document': name, 'line': text.count('\n', 0, match.start()) + 1,
                      'target': target, 'result': 'PASS'})
assert len(links) == 7

def normalized_quick(text):
    values = []
    for line in text.splitlines():
        line = re.sub(r'^#{1,6} ', '', line.strip())
        if not line or line.startswith(('版本：', '配套文档：', '认可，这几处补充')):
            continue
        if line == 'TS／MZ／Showdown 宝可梦游戏开发框架：7 步简化计划':
            continue
        values.append(line)
    return values

a, b = normalized_quick(source), normalized_quick(new_text)
assert len(a) == len(b) == 21
matcher = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
equal = sum(i2 - i1 for tag, i1, i2, j1, j2 in matcher.get_opcodes() if tag == 'equal')
assert equal == 16, equal
remaining_differences = [{'kind': tag, 'source': a[i1:i2], 'candidate': b[j1:j2]}
                         for tag, i1, i2, j1, j2 in matcher.get_opcodes() if tag != 'equal']

history = []
for path in git('ls-tree', '-r', '--name-only', OLD_REVIEW, '--', REVIEW_PREFIX).decode().splitlines():
    previous = doc(OLD_REVIEW, path)
    current = (ROOT / path).read_bytes()
    assert previous == current, path
    history.append({'path': path, **identity(previous), 'preserved_byte_identical': True})
assert len(history) == 10

result = {'verdict': 'PASS', 'scope': 'Final source-preservation fidelity only; no architecture review or implementation acceptance.',
          'old_candidate': OLD, 'new_candidate': NEW, 'new_candidate_parents': parents,
          'prior_FAIL_review_commit': OLD_REVIEW, 'candidate_changed_paths': changed,
          'changed_physical_lines': line_changes, 'F01_closed': True,
          'restored_quick_line_33': new_lines[32], 'source_quick_line_20': source_lines[19],
          'restored_line_exact_source_match': True,
          'all_other_repository_paths_unchanged_between_candidates': True,
          'documents': documents, 'links': links,
          'quick_full_text_comparison': {'source_nonempty_lines': len(a), 'candidate_nonempty_lines': len(b),
                                         'equal_after_format_normalization': equal,
                                         'remaining_exact_differences': remaining_differences},
          'previous_review_artifacts_preserved': history,
          'original_source_wording_difference': 'The detailed source requires classifying differences before fixing the corresponding content; the quick source says to fix the specification. Both original formulations are preserved. PASS authorizes faithful storage, not an inferred substantive reconciliation.',
          'ruby_executions': 0, 'prototype_executions': 0}
(HERE / 'checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(HERE / 'candidate-change.patch').write_bytes(git('diff', '--unified=0', OLD, NEW, '--', QUICK))
print(json.dumps({'verdict': 'PASS', 'changed_paths': len(changed), 'changed_lines': line_changes,
                  'restored_line_exact_source_match': True, 'previous_FAIL_files_preserved': len(history),
                  'links_checked': len(links)}, ensure_ascii=False))
