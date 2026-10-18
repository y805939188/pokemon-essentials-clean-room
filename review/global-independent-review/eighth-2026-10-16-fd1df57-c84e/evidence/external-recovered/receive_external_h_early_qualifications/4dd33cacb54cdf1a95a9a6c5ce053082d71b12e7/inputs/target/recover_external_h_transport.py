"""Bounded local gzip restoration; no restored code is imported or executed."""
from pathlib import Path
import datetime
import gzip
import hashlib
import io
import json
import argparse
import re

TASK = Path(__file__).resolve().parent
ROOT = Path('/workspace/pokemon-essentials-clean-room/review/global-independent-review/seventh-2026-10-14-e646432-7a91')
CORE = ROOT / 'publication-transport/core'
DEST = TASK / 'recovered-transport'
SELECT = ['tasks/R7-H08/findings.json', 'tasks/R7-H08/report.md',
          'history/recovery-identity-verification.json',
          'tasks/R7-C17/limits-and-alias-reception.json',
          'tasks/R7-C17/current56-contract-reception.json']

def digest(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--name', default='transport')
    parser.add_argument('--select', nargs='+')
    args = parser.parse_args()
    if not re.fullmatch('[a-z0-9_-]+', args.name):
        raise ValueError('unsafe destination name')
    destination = TASK / ('recovered-' + args.name)
    selection = args.select or SELECT
    if destination.exists() or destination.is_symlink() or any(p.is_symlink() for p in destination.parents):
        raise ValueError('isolated destination must be absent and contain no symlinks')
    index = json.loads((CORE/'payload-index.json').read_text())
    logical = {r['logical_path']: r for r in index['logical_files']}
    encoded = {r['transport_path']: r for r in index['compressed_objects']}
    destination.mkdir()
    receipts = []
    for path in selection:
        relative = Path(path)
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('unsafe path')
        row = logical[path]
        transport = Path(row['transport_path'])
        if transport.is_absolute() or '..' in transport.parts:
            raise ValueError('unsafe transport path')
        compressed = (CORE/transport).read_bytes()
        expected = encoded[str(transport)]
        comp_id = digest(compressed)
        assert comp_id['bytes'] == expected['transport_bytes']
        assert comp_id['sha256'] == expected['transport_sha256']
        assert comp_id['git_blob_content_id'] == expected['transport_git_blob_content_id']
        with gzip.GzipFile(fileobj=io.BytesIO(compressed)) as stream:
            data = stream.read(row['bytes'] + 1)
        actual = digest(data)
        for key, value in actual.items():
            assert value == row[key], (path, key)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('xb') as f:
            f.write(data)
        receipts.append({'logical': row, 'encoded': expected,
                         'local_path': str(target), 'decoded_identity': actual,
                         'semantic_credit': False, 'restored_code_executed': False})
    (TASK/(args.name+'-recovery-manifest.json')).write_text(json.dumps({'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'source_C2': '4580645dfbfec4a3c7ccbad56ae293cc619b0d25', 'files': receipts}, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'restored': len(receipts), 'decoded_bytes': sum(r['decoded_identity']['bytes'] for r in receipts), 'semantic_credit': False}))

if __name__ == '__main__':
    main()
