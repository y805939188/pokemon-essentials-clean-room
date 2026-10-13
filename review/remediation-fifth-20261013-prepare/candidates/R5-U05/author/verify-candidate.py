#!/usr/bin/env python3
"""Validate candidate artifacts only; never execute reference or a score model."""
import difflib
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / '.git').exists())
BASE = '9366d9d17aaeac3b4414236468affa650fb3dd27'
START = '93524fe5cf396de2bd01f3c5c1e08ba4b874bc68'
BODY = 'deliverables/final-specification-set/combat-requirements/wp52-b-field-damage-healing-and-target-evaluation.md'
TESTS = 'deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


manifest = json.loads((HERE / 'candidate-manifest.json').read_text())
listed = {r['path'] for r in manifest['artifacts']}
actual = {str(p.relative_to(HERE)) for p in HERE.rglob('*') if p.is_file()}
assert actual == listed | {'candidate-manifest.json'}, 'unlisted/missing payload'
for row in manifest['artifacts']:
    data = (HERE / row['path']).read_bytes()
    data.decode('utf-8')
    assert identity(data) == {k: row[k] for k in identity(data)}, row['path']
    if row['path'].endswith('.json'):
        json.loads(data)

prefix = str(HERE.relative_to(REPO)) + '/'
changed = git('diff', '--name-only', START, 'HEAD').decode().splitlines()
changed += git('diff', '--name-only', 'HEAD').decode().splitlines()
changed += git('ls-files', '--others', '--exclude-standard').decode().splitlines()
assert all(p.startswith(prefix) for p in changed), 'write outside R5-U05 allowlist'
assert git('rev-parse', 'HEAD:deliverables/final-specification-set').strip().decode() == manifest['fixed_inputs']['B5']['formal_tree']
assert git('diff', START, 'HEAD', '--', 'review/remediation-fifth-20261013-prepare/contracts') == b''

patch = ''
old = {}
new = {}
for path in [BODY, TESTS]:
    old[path] = git('show', BASE + ':' + path)
    new[path] = (HERE / 'formal' / path).read_bytes()
    patch += ''.join(difflib.unified_diff(old[path].decode().splitlines(True),
                     new[path].decode().splitlines(True), fromfile='a/' + path, tofile='b/' + path, n=3))
assert patch.encode() == (HERE / 'formal-diff.patch').read_bytes(), 'patch/mirror mismatch'
with tempfile.TemporaryDirectory(prefix='r5-u05-replay-') as scratch:
    dest = Path(scratch)
    for path, data in old.items():
        p = dest / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
    subprocess.run(['git', 'apply', '--check', str(HERE / 'formal-diff.patch')], cwd=dest, check=True)
    subprocess.run(['git', 'apply', str(HERE / 'formal-diff.patch')], cwd=dest, check=True)
    for path, data in new.items():
        assert (dest / path).read_bytes() == data, 'replay byte mismatch'

old_rows = [l for l in old[TESTS].decode().splitlines() if l.startswith('| ') and not l.startswith('| ID')]
new_rows = new[TESTS].decode().splitlines()
assert all(l in new_rows for l in old_rows), 'existing vector/table row modified'
def be_rows(text):
    return [l for l in text.splitlines() if re.match(r'^\| B\d+[a-z]? \|', l)]
assert len(be_rows(old[TESTS].decode())) == 67
assert len(be_rows(new[TESTS].decode())) == 75
ids = [l.split('|')[1].strip() for l in be_rows(new[TESTS].decode())]
assert len(ids) == len(set(ids))
assert [v['id'] for v in json.loads((HERE / 'finding-responses.json').read_text())['findings'][0]['vectors']] == [f'B{i}' for i in range(64, 72)]
assert len(json.loads((HERE / 'finding-responses.json').read_text())['findings'][0]['mandatory_criteria']) == 4

report = {'evidence_level': 'TOOL_VALIDATION', 'status': 'PASS_ARTIFACT_CHECKS_ONLY',
          'artifacts_verified': len(listed), 'patch_replay': 'BYTE_IDENTICAL',
          'existing_table_rows': 'BYTE_PRESERVED', 'BE_before_after': [67, 75],
          'scope': 'R5-U05 author directory only', 'behavior_execution': 0,
          'semantic_or_independent_review_verdict': False}
print(json.dumps(report, ensure_ascii=False, indent=2))
