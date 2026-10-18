#!/usr/bin/env python3
"""Reproduce document-only evidence; a mechanical PASS is not a fidelity PASS."""
from pathlib import Path, PurePosixPath
import difflib
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = '8075cc7714e64fd2c170cc397d9efa94811da57b'
CANDIDATE = 'ed66a2b7aafc9da3846d48e412b4918c147ec14a'
PREFIX = 'planning/framework-roadmap/'
NAMES = ['DETAILED-PLAN.md', 'QUICK-PLAN.md', 'README.md']
EXPECTED = {
    'DETAILED-PLAN.md': '016000db57c445876e47b8cc9a1f1550ab0e7c25',
    'QUICK-PLAN.md': '216ef8509289c653b5d998de567d00e3a3271129',
    'README.md': '39b96e60ba6978d541c4e9e545e5b5fe62212c77',
}

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def norm(text, quick=False):
    rows = []
    for number, original in enumerate(text.splitlines(), 1):
        value = re.sub(r'^#{1,6} ', '', original.strip())
        if not value or value.startswith(('版本：', '配套文档：')):
            continue
        if quick and (value.startswith('认可，这几处补充') or value == 'TS／MZ／Showdown 宝可梦游戏开发框架：7 步简化计划'):
            continue
        rows.append({'line': number, 'text': value})
    return rows

documents = {}
texts = {}
for name in NAMES:
    data = git('show', f'{CANDIDATE}:{PREFIX}{name}')
    actual_blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    assert actual_blob == EXPECTED[name], (name, actual_blob)
    texts[name] = data.decode('utf-8')
    documents[name] = {'bytes': len(data), 'lines': len(data.splitlines()), 'git_blob': actual_blob,
                       'sha256': hashlib.sha256(data).hexdigest(), 'expected_blob_match': True}

coverage = []
patches = []
for source_name, name in [('detailed-source.txt', NAMES[0]), ('quick-source.txt', NAMES[1])]:
    source_data = (HERE / 'source-inputs' / source_name).read_bytes()
    source_text = source_data.decode('utf-8')
    a = norm(source_text, name == NAMES[1])
    b = norm(texts[name], name == NAMES[1])
    matcher = difflib.SequenceMatcher(a=[x['text'] for x in a], b=[x['text'] for x in b], autojunk=False)
    opcodes = []
    equal_count = 0
    for tag, i, j, k, l in matcher.get_opcodes():
        if tag == 'equal':
            pairs = [{'source_line': x['line'], 'candidate_line': y['line']} for x, y in zip(a[i:j], b[k:l])]
            equal_count += len(pairs)
            opcodes.append({'kind': tag, 'pairs': pairs})
        else:
            opcodes.append({'kind': tag, 'source': a[i:j], 'candidate': b[k:l]})
    assert sum(len(x.get('pairs', x.get('source', []))) for x in opcodes) == len(a)
    assert sum(len(x.get('pairs', x.get('candidate', []))) for x in opcodes) == len(b)
    coverage.append({'source': source_name, 'source_sha256': hashlib.sha256(source_data).hexdigest(),
                     'source_physical_lines': len(source_text.splitlines()), 'candidate': name,
                     'source_compared_nonempty_lines': len(a), 'candidate_compared_nonempty_lines': len(b),
                     'equal_after_format_normalization': equal_count,
                     'all_source_and_candidate_compared_lines_accounted_for': True, 'opcodes': opcodes})
    patches.extend(difflib.unified_diff([x['text'] + '\n' for x in a], [x['text'] + '\n' for x in b],
                                      fromfile=source_name, tofile=PREFIX + name))

links = []
for name, text in texts.items():
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', text):
        label, target = match.groups()
        number = text.count('\n', 0, match.start()) + 1
        if target.startswith('https://'):
            assert target == f'https://github.com/y805939188/pokemon-essentials-clean-room/commit/{BASE}'
            git('cat-file', '-e', BASE + '^{commit}')
            resolved = BASE
        else:
            assert '/' not in target and '#' not in target and target in NAMES
            resolved = str(PurePosixPath(PREFIX) / target)
            git('cat-file', '-e', f'{CANDIDATE}:{resolved}')
        links.append({'file': name, 'line': number, 'label': label, 'target': target,
                      'resolved_at_candidate_or_base': resolved, 'result': 'PASS'})
assert len(links) == 7
assert len(re.findall(r'^## [一二三四五六七八九十]+、', texts[NAMES[0]], re.M)) == 17
assert re.findall(r'^## (\d)\.', texts[NAMES[1]], re.M) == list('1234567')
assert re.findall(r'^### 阶段 ([0-6][AB]?)：', texts[NAMES[0]], re.M) == ['0A', '0B', '1', '2', '3', '4', '5', '6']
assert all('版本：v1.0 · 日期：2026-10-17' in text for text in texts.values())

changes = git('diff', '--name-status', BASE, CANDIDATE).decode().splitlines()
assert sorted(changes) == sorted('A\t' + PREFIX + n for n in NAMES), changes
protected = []
for path in ['AGENTS.md', 'specs', 'deliverables/final-specification-set',
             'review/remediation-eighth-20261016-prepare']:
    before = git('rev-parse', f'{BASE}:{path}').decode().strip()
    after = git('rev-parse', f'{CANDIDATE}:{path}').decode().strip()
    assert before == after, path
    protected.append({'path': path, 'base_object': before, 'candidate_object': after, 'unchanged': True})

def save(name, data):
    (HERE / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

save('full-text-comparison.json', {
    'method': 'Every nonempty source and candidate line compared; all differing opcodes retained verbatim. Only blank lines, Markdown heading prefixes, metadata, added quick title and conversational preface are excluded from alignment. Semantic decisions are in report.md and the two audit files.',
    'candidate': CANDIDATE, 'coverage': coverage})
(HERE / 'full-source-diff.patch').write_text(''.join(patches), encoding='utf-8')
save('mechanical-checks.json', {'base': BASE, 'candidate': CANDIDATE,
    'mechanical_result': 'PASS', 'fidelity_verdict': 'FAIL',
    'blocking_finding': 'F01: QUICK-PLAN.md:33 changes the supplied quick source beyond the permitted merge list.',
    'documents': documents, 'candidate_write_set': changes, 'protected_objects': protected,
    'links': links, 'heading_counts': {'detailed_sections': 17, 'quick_steps': 7, 'detailed_stages': 8},
    'version_date_result': 'PASS', 'ruby_or_prototype_executions': 0,
    'scope': 'Document fidelity, cross-version correspondence, links and write sets only.'})
print(json.dumps({'mechanical_result': 'PASS', 'fidelity_verdict': 'FAIL',
    'coverage': [{k: v for k, v in c.items() if k != 'opcodes'} for c in coverage],
    'links': len(links), 'candidate_files': len(changes)}, ensure_ascii=False, indent=2))
