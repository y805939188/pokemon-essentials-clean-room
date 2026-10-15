"""Check complete package identity and allowlist before publication."""
import ast
import hashlib
import json
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[4]
PREFIX='candidates/R7-U03/'
B='e646432c644dec04d306842cc5a559a29c718fbc'
assert subprocess.check_output(['git','branch','--show-current'],cwd=ROOT).decode().strip()=='codex/r7-u03-author-20261015-wave1'
subprocess.run(['git','merge-base','--is-ancestor',B,'HEAD'],cwd=ROOT,check=True)
manifest=json.loads((ROOT/PREFIX/'evidence/author/artifact-manifest.json').read_bytes())
for row in manifest['evidence_and_mirror_inventory']:
    data=(ROOT/row['path']).read_bytes()
    assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256'],row['path']
    assert hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()==row['git_blob_content_id']
for p in (ROOT/PREFIX).rglob('*.json'):json.loads(p.read_bytes())
for p in (ROOT/PREFIX).rglob('*.py'):ast.parse(p.read_text())
for path in subprocess.check_output(['git','diff','--name-only',B],cwd=ROOT).decode().splitlines():
    assert path.startswith(PREFIX),path
for path in subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT).decode().splitlines():
    assert path.startswith(PREFIX),path
for row in manifest['mirrors']:
    data=(ROOT/row['candidate_path']).read_bytes()
    assert len(data)==row['new']['bytes'] and hashlib.sha256(data).hexdigest()==row['new']['sha256']
    old=subprocess.check_output(['git','show',B+':'+row['original_path']],cwd=ROOT)
    assert len(old)==row['original_B']['bytes'] and hashlib.sha256(old).hexdigest()==row['original_B']['sha256']
print(json.dumps(dict(result='PACKAGE_IDENTITIES_SCOPE_AST_JSON_VERIFIED',mirrors=5,
    inventory_files_verified=len(manifest['evidence_and_mirror_inventory']),stage='TOOL_VALIDATION',semantic_PASS=False)))
