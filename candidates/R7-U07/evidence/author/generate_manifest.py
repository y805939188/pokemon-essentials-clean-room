"""Inventory authorized candidate payloads; manifest self-identity is external."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[4]
PREFIX = ROOT / 'candidates/R7-U07'
BASE = 'e646432c644dec04d306842cc5a559a29c718fbc'
TARGET = PREFIX / 'evidence/author/artifact-manifest.json'


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


rows = []
for path in sorted(PREFIX.rglob('*')):
    if not path.is_file() or path == TARGET:
        continue
    assert not path.is_symlink()
    relative = str(path.relative_to(PREFIX))
    row = {'path': str(path.relative_to(ROOT)), 'after': identity(path.read_bytes())}
    if relative.startswith('deliverables/'):
        row['role'] = 'complete_frozen_B_mirror_with_bounded_revision'
        row['baseline_path'] = relative
        row['baseline_commit'] = BASE
        row['before'] = identity(subprocess.check_output(['git', 'show', f'{BASE}:{relative}'], cwd=ROOT))
        row['allowed_scope'] = 'WP55 §2.5 final sentence/boundary and §4 cross-link' if '/wp55-' in relative else 'Only supplemental zero-versus-positive-missing vectors; original catalog bytes preserved'
    else:
        assert relative.startswith('evidence/author/')
        row['role'] = 'author_evidence_or_artifact_validation_tool'
        row['before'] = None
    rows.append(row)
stdout = f'Artifact manifest: {len(rows)} payload files; self excluded, identity bound by commit/tree and remote readback.'
record = {'schema': 'r7.u07.author-artifact-manifest.v1',
          'state': 'CANDIDATE_READY_NOT_REVIEWED', 'base_commit': BASE,
          'base_formal_tree': 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c',
          'branch': 'codex/r7-u07-author-20261015-wave1',
          'fixed_dispatch_commit': '6ec1d09e9c470954964d72761c83a760ef4f0364',
          'fixed_dispatch_blob': '2c6592135c8e7d1aa6fa0f851b8ef91056bb27a7',
          'actual_context': os.environ.get('CODEX_THREAD_ID'),
          'files': rows, 'payload_files': len(rows),
          'self_identity': {'path': str(TARGET.relative_to(ROOT)),
                            'qualification': 'Intentionally excluded from recursive hashes. The actual final commit/tree and complete remote readback externally bind this file.'},
          'generation': {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                         'cwd': str(ROOT), 'argv': sys.argv, 'pid': os.getpid(),
                         'stdout': stdout, 'stderr': '', 'exit_code': 0},
          'qualification': 'Identity and allowed-scope inventory only; no independent PASS, formal acceptance, closure, or reference/host execution.'}
TARGET.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(stdout)
