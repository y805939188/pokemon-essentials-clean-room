#!/usr/bin/env python3
"""Rebuild and verify finite specification proposals, never execute reference behavior."""
import argparse, difflib, hashlib, json, subprocess, tempfile
from pathlib import Path
parser = argparse.ArgumentParser()
parser.add_argument('--repo', default=str(Path(__file__).resolve().parents[4]))
args = parser.parse_args()
repo = Path(args.repo)
author = Path(__file__).resolve().parent
B5 = '9366d9d17aaeac3b4414236468affa650fb3dd27'
prepare = '93524fe5cf396de2bd01f3c5c1e08ba4b874bc68'
def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest())
def blob(path, ref=B5):
    return subprocess.check_output(['git', 'show', ref + ':' + path], cwd=repo)
target_manifest = json.loads((author / 'candidate-target-identities.json').read_text())
targets = target_manifest['targets']
base = {row['target_path']: blob(row['target_path']) for row in targets}
proposed = dict(base)
for row in targets:
    assert identity(base[row['target_path']]) == row['B5_identity']
    if row['mode'] == 'direct_mirror':
        proposed[row['target_path']] = (author / 'formal' / row['target_path']).read_bytes()
fragments = json.loads((author / 'fragment-manifest.json').read_text())['fragments']
for row in fragments:
    old = row['base_text'].encode()
    assert hashlib.sha256(old).hexdigest() == row['base_text_sha256']
    assert base[row['target_path']].count(old) == 1
    data = (author / row['payload_file']).read_bytes()
    payload = data[row['payload_byte_offset']:row['payload_byte_offset'] + row['payload_bytes']]
    assert len(payload) == row['payload_bytes']
    assert hashlib.sha256(payload).hexdigest() == row['payload_sha256']
    assert proposed[row['target_path']].count(old) == 1
    proposed[row['target_path']] = proposed[row['target_path']].replace(old, payload, 1)
for row in targets:
    assert identity(proposed[row['target_path']]) == row['proposed_identity']
patch = ''.join(''.join(difflib.unified_diff(base[path].decode().splitlines(True),
    proposed[path].decode().splitlines(True), fromfile='a/' + path, tofile='b/' + path,
    n=3)) for path in target_manifest['patch_order'])
assert (author / 'formal-diff.patch').read_bytes() == patch.encode()
with tempfile.TemporaryDirectory(prefix='r5-u07-rebuild-', dir='/tmp') as directory:
    scratch = Path(directory)
    for path, data in base.items():
        file = scratch / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_bytes(data)
    subprocess.run(['git', 'apply', '--check', str(author / 'formal-diff.patch')], cwd=scratch, check=True)
    subprocess.run(['git', 'apply', str(author / 'formal-diff.patch')], cwd=scratch, check=True)
    for path, data in proposed.items():
        assert (scratch / path).read_bytes() == data
responses = json.loads((author / 'finding-responses.json').read_text())
assert len(responses['findings']) == 7
assert sum(len(row['acceptance_map']) for row in responses['findings']) == 33
assert all(row['new_execution'] == 0 and not row['closed'] for row in responses['findings'])
for file in author.rglob('*.json'):
    json.loads(file.read_bytes())
manifest_path = author / 'candidate-manifest.json'
if manifest_path.exists():
    for row in json.loads(manifest_path.read_text())['artifacts']:
        assert identity((author / row['path']).read_bytes()) == row['identity'], row['path']
# Live formal/registration and all frozen package files remain prepare bytes.
assert subprocess.check_output(['git', 'rev-parse', 'HEAD:deliverables/final-specification-set'], cwd=repo).decode().strip() == 'd5a462b4c6f8b78c3264a25d6b5495230fa265e2'
changed = subprocess.check_output(['git', 'diff', '--name-only', prepare], cwd=repo).decode().splitlines()
assert all(path.startswith('review/remediation-fifth-20261013-prepare/candidates/R5-U07/author/') for path in changed)
print(json.dumps({'level': 'TOOL_VALIDATION', 'reconstructed_targets': len(proposed),
                  'fragments': len(fragments), 'criteria': 33, 'required_ids': 7,
                  'patch_rebuild': 'PASS', 'artifact_integrity': 'PASS',
                  'write_scope': 'PASS', 'new_behavior_execution': 0}, ensure_ascii=False))
