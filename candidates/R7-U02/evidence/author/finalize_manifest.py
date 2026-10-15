"""Freeze all candidate files except this manifest's recursive self-identity."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess


REPO = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
BASE = 'e646432c644dec04d306842cc5a559a29c718fbc'


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


def main():
    mirrors = json.loads((OUT / 'mirror-identities.json').read_bytes())['mirrors']
    lookup = {r['path']: r for r in mirrors}
    rows = []
    for path in sorted((REPO / 'candidates/R7-U02').rglob('*')):
        if not path.is_file() or path == OUT / 'artifact-manifest.json':
            continue
        assert not path.is_symlink()
        rel = path.relative_to(REPO).as_posix()
        row = {'path': rel, 'candidate': identity(path.read_bytes())}
        if rel in lookup:
            row.update({'base_commit': BASE, 'base_path': lookup[rel]['base_path'], 'base': lookup[rel]['base'],
                        'hunks': lookup[rel]['hunks'], 'record_scopes': lookup[rel]['record_scopes']})
            assert row['candidate'] == lookup[rel]['candidate']
        else:
            assert rel.startswith('candidates/R7-U02/evidence/author/')
            row['base'] = {'state': 'ABSENT_AT_B'}
        rows.append(row)
    manifest = {'schema': 'r7.u02.author-artifact-manifest.v1',
                'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'state': 'CANDIDATE_READY_NOT_REVIEWED', 'base_commit': BASE,
                'branch': 'codex/r7-u02-author-20261015-wave1',
                'files': rows, 'files_with_explicit_identity': len(rows),
                'recursive_self': {'path': 'candidates/R7-U02/evidence/author/artifact-manifest.json',
                    'identity_binding': 'Final candidate Git commit/tree and external complete remote-readback receipt. A manifest cannot contain its own content hash.'},
                'final_publication_envelope': '/workspace/r7-bootstrap/R7-U02-author/final-publication/publication-final.json',
                'publication_note': 'Envelope contains ordinary push I/O, remote ref before/after, GitHub commit/tree/parent and complete immutable raw readback for every changed file, including this manifest. No candidate writes after final commit.'}
    (OUT / 'artifact-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'files_with_explicit_identity': len(rows), 'plus_manifest_self_bound_by_commit': 1,
                      'manifest': identity((OUT / 'artifact-manifest.json').read_bytes())}))


if __name__ == '__main__':
    main()
