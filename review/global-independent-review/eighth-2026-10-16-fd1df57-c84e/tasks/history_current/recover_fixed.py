"""Read-only Git blob extraction into a previously absent isolated directory.

No restored program is run. Repo objects and source files are never modified.
"""
from pathlib import Path
import hashlib
import json
import subprocess
import datetime

REPO = Path('/workspace/pokemon-essentials-clean-room')
TASK = Path(__file__).resolve().parent
DEST = TASK / 'recovered-fixed'
R6 = '9aa72bc99a4cf52c8fb9cad8a637a963341388b0'
C2 = '4580645dfbfec4a3c7ccbad56ae293cc619b0d25'
R6ROOT = 'review/remediation-sixth-20261014-prepare/'
C2ROOT = 'review/global-independent-review/seventh-2026-10-14-e646432-7a91/'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)

def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}

def main():
    if DEST.exists() or DEST.is_symlink() or any(p.is_symlink() for p in DEST.parents):
        raise ValueError('destination exists or includes a symlink')
    selected = [(R6, R6ROOT + p, 'R6/' + p) for p in [
        'completion/final-delivery.json', 'ledger.json', 'task-register.json',
        'reception-queue.json', 'integration/public-sync-20261014/sync-input.json',
        'integration/public-sync-20261014/dependency-status.json',
        'integration/public-sync-20261014/sync-report.md',
        'inputs/optional-records.json', 'inputs/optional-facets.json',
        'inputs/policy-records.json', 'inputs/limit-records.json',
        'inputs/no-required-revision-records.json']]
    selected += [(R6, p, 'R6/' + p) for p in ['planning/feature-matrix.md', 'audit/source-traceability.md']]
    selected += [(C2, C2ROOT + p, 'C2/' + p) for p in [
        'final-report.md', 'canonical-records.json', 'findings.json',
        'reading-ledger.final.json', 'coverage/summary.final.json',
        'history/qualifications.final.json', 'handoff/batch-assignment.json',
        'handoff/dependency-graph.json', 'handoff/file-conflict-graph.json',
        'publication/final-delivery-binding.json']]
    DEST.mkdir()
    manifest = []
    for commit, path, local in selected:
        row = {'commit': commit, 'path': path, 'local_path': str(DEST / local),
               'semantic_credit': False, 'operation': 'Git blob read and exact-byte restoration'}
        try:
            tree_entry = git('ls-tree', commit, '--', path).decode().split()
            if not tree_entry:
                raise ValueError('path missing at exact commit')
            data = git('show', commit + ':' + path)
            row.update(identity(data))
            row.update(mode=tree_entry[0], commit_tree=git('rev-parse', commit + '^{tree}').decode().strip())
            if row['git_blob'] != tree_entry[2]:
                raise ValueError('blob identity mismatch')
            target = DEST / local
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as f:
                f.write(data)
            current = REPO / path
            row['current_identity'] = identity(current.read_bytes()) if current.is_file() else None
            row['same_current_bytes'] = current.is_file() and current.read_bytes() == data
            row['status'] = 'RESTORED_BYTES_VERIFIED'
        except Exception as e:
            row.update(status='MISSING_OR_FAILED', error=str(e))
        manifest.append(row)
    (TASK / 'recovery-manifest.json').write_text(json.dumps({'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'files': manifest}, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'restored': sum(r['status'] == 'RESTORED_BYTES_VERIFIED' for r in manifest), 'failed': [r for r in manifest if r['status'] != 'RESTORED_BYTES_VERIFIED'], 'same_current_bytes': sum(r.get('same_current_bytes', False) for r in manifest)}, ensure_ascii=False))

if __name__ == '__main__':
    main()
