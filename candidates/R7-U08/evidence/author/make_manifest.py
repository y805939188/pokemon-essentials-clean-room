"""Inventory complete mirrors and supporting evidence, excluding this manifest itself."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parents[2]
B = 'e646432c644dec04d306842cc5a559a29c718fbc'


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


mirrors = []
for target in sorted((root / 'deliverables').rglob('*.md')):
    p = str(target.relative_to(root))
    old = subprocess.check_output(['git', 'show', f'{B}:{p}'])
    mirrors.append({'base_path': p, 'candidate_path': 'candidates/R7-U08/' + p,
                    'base_commit': B, 'base': identity(old), 'candidate': identity(target.read_bytes()),
                    'kind': 'COMPLETE_BASE_MIRROR_WITH_BOUNDED_CLAUSE_EDITS'})
evidence = []
for p in sorted((root / 'evidence/author').rglob('*')):
    if p.is_file() and p.name != 'artifact-manifest.json':
        evidence.append({'path': 'candidates/R7-U08/' + str(p.relative_to(root)),
                         **identity(p.read_bytes())})
manifest = {'schema': 'r7.u08.author-artifact-manifest.v1',
            'status': 'CANDIDATE_READY_NOT_REVIEWED',
            'generated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'baseline_B': B, 'formal_tree': 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c',
            'unique_branch': 'codex/r7-u08-author-20261015-wave1',
            'mirrors': mirrors, 'supporting_evidence': evidence,
            'manifest_self_identity': 'Bound by actual candidate Git tree and full immutable remote readback; excluded from its own content inventory.',
            'exact_edit_scope': 'WP67-A B196/247/248; WP67-B B141; catalogue B440 plus four rows immediately after B398. No other original lines differ.',
            'read_set': 'reading-ledger.json + input-identities.json + original frozen full contract',
            'write_set': [r['candidate_path'] for r in mirrors] + ['candidates/R7-U08/evidence/author/**'],
            'conditional_or_optional_writes': [], 'semantic_acceptance': False}
(root / 'evidence/author/artifact-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'mirrors': len(mirrors), 'supporting_files': len(evidence),
                  'manifest': 'candidates/R7-U08/evidence/author/artifact-manifest.json'}))
