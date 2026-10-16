"""Lossless report payload transport. This tool never changes source payloads.

The coordinating reviewer must freeze the semantic report before pack. A transport
round trip certifies bytes, never semantic reading or behavior.
"""
import argparse
import concurrent.futures
import datetime
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
CHUNK = 1024 * 1024


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def identity(path):
    size = path.stat().st_size
    sha = hashlib.sha256()
    blob = hashlib.sha1(b'blob ' + str(size).encode() + b'\0')
    with path.open('rb') as f:
        while data := f.read(CHUNK):
            sha.update(data)
            blob.update(data)
    if size != path.stat().st_size:
        raise RuntimeError('payload changed size during read: ' + str(path))
    return {'bytes': size, 'sha256': sha.hexdigest(), 'git_blob_content_id': blob.hexdigest()}


def safe_relative(value):
    path = Path(value)
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise ValueError('unsafe logical path: ' + value)
    return path


def projection(source, target):
    dropped = {}
    count = 0
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError('projection path collision: ' + str(target))
    with source.open('r', encoding='utf8') as inp, target.open('w', encoding='utf8') as out:
        for line in inp:
            event = json.loads(line)
            item_type = event.get('item', {}).get('type')
            event_type = event.get('type')
            if item_type == 'reasoning' or event_type in ('turn.completed',):
                key = item_type or event_type
                dropped[key] = dropped.get(key, 0) + 1
                continue
            # Retain actual tool commands, results, public agent messages, thread
            # identities, errors and lifecycle. No invented timestamps or exits.
            out.write(json.dumps(event, ensure_ascii=False, separators=(',', ':')) + '\n')
            count += 1
    return {'source': identity(source), 'retained_events': count,
            'excluded_event_counts': dropped, 'projection': identity(target)}


def payload_purpose(rel):
    parts = rel.parts
    suffix = rel.suffix.lower()
    kind = {'.json': 'structured_json', '.jsonl': 'structured_json_lines',
            '.md': 'text_report', '.py': 'audit_tool_source', '.rb': 'decoded_reference_program_evidence',
            '.il': 'decoded_managed_program_evidence', '.glsl': 'decoded_shader_evidence',
            '.tsv': 'structured_table', '.csv': 'structured_table',
            '.stdout': 'actual_tool_stdout', '.stderr': 'actual_tool_stderr'}.get(suffix, 'typed_by_original_ledger_or_file_identity')
    if 'snapshots' in parts or 'inputs' in parts:
        purpose = 'Preserved versioned input/intermediate index; original generation-time scope and final canonical receiver overlay decide semantic validity. No automatic whole-file approval.'
    elif 'logs' in parts or suffix in ('.stdout', '.stderr'):
        purpose = 'Actual command/output evidence; retain failures and missing original metadata. Original reader/phase ledger determines reading and execution scope.'
    elif rel.name in ('reading-ledger.json', 'forward-map.json', 'reverse-map.json', 'report.md', 'findings.json', 'task.json'):
        purpose = 'Named task review/reading/mapping/proposal payload; final non-proposer/root reception and canonical indexes determine current accepted scope, not task status alone.'
    elif 'temporary' in parts:
        purpose = 'Isolated R7 tool fixture or derived check; exact owner/command qualifies it. No production game/model/host credit.'
    else:
        purpose = 'Frozen R7 report, tool, identity, execution or reception evidence. Exact original ledger and final canonical overlay retain purpose, ranges, premises and generation-time qualification.'
    return kind, purpose


def pack(args):
    out = Path(args.output).resolve()
    if out.exists():
        raise FileExistsError('new unique output directory required')
    if ROOT not in out.parents:
        raise ValueError('transport output must remain inside this R7 report')
    paths = []
    for p in ROOT.rglob('*'):
        if not p.is_file() or p.is_symlink():
            continue
        rel = p.relative_to(ROOT)
        if '__pycache__' in rel.parts or p.name in ('.DS_Store',):
            continue
        if rel.parts[0] in ('publication-transport', 'publication-staging'):
            continue
        paths.append((p, rel))
    out.mkdir(parents=True)
    entries = []
    excluded = []
    objects = {}
    for ordinal, (path, rel) in enumerate(sorted(paths, key=lambda x: str(x[1]))):
        before = path.stat()
        if path.name == 'events.jsonl':
            projection_rel = Path('platform-io') / (str(rel).replace('/', '__') + '.jsonl')
            result = projection(path, out / projection_rel)
            excluded.append({'logical_path': str(rel), 'disposition': 'LOCAL_RAW_PLATFORM_STREAM',
                             'reason': 'Raw stream contains private reasoning; original remains unchanged locally. All public tool I/O is projected separately.',
                             'identity': result['source'], 'public_projection_path': str(projection_rel),
                             'public_projection_identity': result['projection'],
                             'retained_events': result['retained_events'], 'excluded_event_counts': result['excluded_event_counts']})
            if before.st_mtime_ns != path.stat().st_mtime_ns:
                raise RuntimeError('active platform stream, freeze first: ' + str(rel))
            continue
        ident = identity(path)
        after = path.stat()
        if before.st_mtime_ns != after.st_mtime_ns or before.st_size != after.st_size:
            raise RuntimeError('active payload, freeze first: ' + str(rel))
        transport_rel = Path('objects') / ident['sha256'][:2] / (ident['sha256'] + '.gz')
        kind, purpose = payload_purpose(rel)
        entries.append({'logical_path': str(rel), **ident, 'transport_path': str(transport_rel),
                        'mode': before.st_mode & 0o777,
                        'encoding': 'gzip',
                        'payload_type': kind, 'purpose': purpose,
                        'reading_scope_authority': 'Original named ledger/task plus final root/C17 canonical reception; preserved earlier UNREAD/WAIT is not silently rewritten.',
                        'transport_reading_status': 'IDENTITY_AND_FULL_BYTE_ROUNDTRIP_ONLY',
                        'content_blob_qualification': 'Git blob content identity of decoded logical bytes; tree membership is the compressed transport path, not this logical original path.'})
        objects.setdefault(ident['sha256'], (path, out / transport_rel, ident))
        if ordinal % 1000 == 0:
            print(json.dumps({'phase': 'index', 'files': ordinal, 'utc': utc()}), flush=True)

    def encode(row):
        path, target, ident = row
        target.parent.mkdir(parents=True, exist_ok=True)
        with path.open('rb') as inp, target.open('wb') as raw:
            with gzip.GzipFile(filename='', mode='wb', fileobj=raw, compresslevel=6, mtime=0) as gz:
                shutil.copyfileobj(inp, gz, CHUNK)
        sha = hashlib.sha256()
        size = 0
        with gzip.open(target, 'rb') as decoded:
            while data := decoded.read(CHUNK):
                size += len(data)
                sha.update(data)
        if size != ident['bytes'] or sha.hexdigest() != ident['sha256']:
            raise RuntimeError('round trip mismatch: ' + str(path))
        compressed = identity(target)
        if compressed['bytes'] >= 100 * 1024 * 1024:
            raise RuntimeError('transport object too large for ordinary GitHub publication: ' + str(target))
        return {'sha256': ident['sha256'], 'transport_path': str(target.relative_to(out)), **{f'transport_{k}': v for k, v in compressed.items()}}

    compressed = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i, row in enumerate(pool.map(encode, objects.values()), 1):
            compressed.append(row)
            if i % 500 == 0:
                print(json.dumps({'phase': 'encode-and-verify', 'unique_objects': i, 'utc': utc()}), flush=True)
    index = {'schema': 'r7.lossless-report-transport.v1', 'created_utc': utc(),
             'semantic_qualification': 'TRANSPORT_ONLY; not reading, execution, completion or approval',
             'logical_files': entries, 'compressed_objects': compressed, 'local_only_platform_streams': excluded,
             'counts': {'logical_files': len(entries), 'unique_objects': len(objects),
                        'decoded_bytes': sum(e['bytes'] for e in entries),
                        'unique_decoded_bytes': sum(row[2]['bytes'] for row in objects.values()),
                        'compressed_bytes': sum(e['transport_bytes'] for e in compressed)}}
    (out / 'payload-index.json').write_text(json.dumps(index, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(index['counts']), flush=True)


def verify_or_restore(args):
    base = Path(args.package).resolve()
    data = json.loads((base / 'payload-index.json').read_text())
    object_index = {x['sha256']: x for x in data['compressed_objects']}
    target = Path(args.destination).resolve() if getattr(args, 'destination', None) else None
    if target:
        if target.exists():
            raise FileExistsError('restore requires a new empty directory')
        if target == ROOT or target in ROOT.parents:
            raise ValueError('cannot restore over source or report workspace')
        target.mkdir(parents=True)
    checked = {}
    for record in data['logical_files']:
        rel = safe_relative(record['logical_path'])
        transport = safe_relative(record['transport_path'])
        source = base / transport
        if record['sha256'] not in checked:
            compressed = identity(source)
            expected = object_index[record['sha256']]
            for key in ('bytes', 'sha256', 'git_blob_content_id'):
                if compressed[key] != expected['transport_' + key]:
                    raise RuntimeError('compressed identity mismatch: ' + str(transport))
            sha = hashlib.sha256()
            blob = hashlib.sha1(b'blob ' + str(record['bytes']).encode() + b'\0')
            size = 0
            with gzip.open(source, 'rb') as inp:
                while chunk := inp.read(CHUNK):
                    size += len(chunk)
                    sha.update(chunk)
                    blob.update(chunk)
            checked[record['sha256']] = {'bytes': size, 'sha256': sha.hexdigest(), 'git_blob_content_id': blob.hexdigest()}
        if any(record[k] != checked[record['sha256']][k] for k in ('bytes', 'sha256', 'git_blob_content_id')):
            raise RuntimeError('decoded identity mismatch: ' + str(rel))
        if target:
            destination = target / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            with gzip.open(source, 'rb') as inp, destination.open('wb') as out:
                shutil.copyfileobj(inp, out, CHUNK)
            if 'mode' in record:
                os.chmod(destination, record['mode'])
    print(json.dumps({'utc': utc(), 'logical_files_verified': len(data['logical_files']), 'unique_objects_verified': len(checked),
                      'restored_to': str(target) if target else None, 'qualification': 'TRANSPORT_ONLY'}))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='action', required=True)
    p = sub.add_parser('pack'); p.add_argument('--output', required=True); p.add_argument('--workers', type=int, default=4)
    for action in ('verify', 'restore'):
        p = sub.add_parser(action); p.add_argument('--package', required=True)
        if action == 'restore': p.add_argument('--destination', required=True)
    args = ap.parse_args()
    pack(args) if args.action == 'pack' else verify_or_restore(args)


if __name__ == '__main__':
    main()
