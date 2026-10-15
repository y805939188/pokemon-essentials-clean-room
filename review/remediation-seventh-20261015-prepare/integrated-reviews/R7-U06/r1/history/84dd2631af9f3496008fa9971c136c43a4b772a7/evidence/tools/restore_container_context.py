"""Restore one frozen R7 batch into a new directory; never start author tasks.

Only standard-library HTTPS reads and bounded gzip decoding are performed.
The small batch plan replaces scans of the 80MB handoff or full core index.
Read this file before use. Never execute programs restored as evidence.
"""
import argparse
import concurrent.futures
import datetime
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

ALLOWED_REPOSITORIES = {
    'y805939188/pokemon-essentials-clean-room',
    'Maruno17/pokemon-essentials',
}
TRANSPORT_LOCKS = {}


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}


def verify(data, expected):
    actual = identity(data)
    for key in actual:
        if key in expected and actual[key] != expected[key]:
            raise ValueError(f'{key} mismatch: expected {expected[key]}, got {actual[key]}')
    return actual


def relative(value):
    path = Path(value)
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise ValueError('unsafe relative path: ' + value)
    return path


def target_path(destination, value):
    target = destination / relative(value)
    for ancestor in [target, *target.parents]:
        if ancestor == destination.parent:
            break
        if ancestor.is_symlink():
            raise ValueError('symlink in destination path: ' + str(ancestor))
    target.parent.mkdir(parents=True, exist_ok=True)
    return target


def fetch(row, expected):
    repository, commit, path = row['repository'], row['commit'], row['path']
    if repository not in ALLOWED_REPOSITORIES or not re.fullmatch('[0-9a-f]{40}', commit):
        raise ValueError('unapproved repository or non-fixed commit')
    relative(path)
    url = f'https://raw.githubusercontent.com/{repository}/{commit}/' + urllib.parse.quote(path)
    attempts = []
    for attempt in range(1, 4):
        start = utc()
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'R7-bounded-context-restore'})
            with urllib.request.urlopen(request, timeout=40) as response:
                data = response.read(expected['bytes'] + 1)
                status = response.status
            verify(data, expected)
            attempts.append({'attempt': attempt, 'start_utc': start, 'end_utc': utc(), 'http_status': status, 'complete_byte_match': True})
            return data, {'url': url, 'attempts': attempts}
        except (urllib.error.URLError, TimeoutError) as error:
            attempts.append({'attempt': attempt, 'start_utc': start, 'end_utc': utc(), 'error': str(error)})
            if isinstance(error, urllib.error.HTTPError) and error.code not in (429, 500, 502, 503, 504):
                raise RuntimeError(json.dumps({'url': url, 'attempts': attempts})) from error
            if attempt == 3:
                raise RuntimeError(json.dumps({'url': url, 'attempts': attempts})) from error
            time.sleep(attempt)


def restore_one(destination, row, encoded=False):
    target = target_path(destination, row['local_path'])
    if target.exists():
        actual = verify(target.read_bytes(), row)
        return {'local_path': row['local_path'], **actual, 'status': 'REUSED_EXACT_BYTES', 'semantic_credit': False}
    if encoded:
        compressed_target = target_path(destination, 'transport/' + row['transport_path'])
        with TRANSPORT_LOCKS[row['transport_path']]:
            if compressed_target.exists():
                data = compressed_target.read_bytes()
                verify(data, row['encoded_identity'])
                transport = {'status': 'REUSED_EXACT_ENCODED_BYTES'}
            else:
                data, transport = fetch(row, row['encoded_identity'])
                with compressed_target.open('xb') as stream:
                    stream.write(data)
        with gzip.GzipFile(fileobj=io.BytesIO(data), mode='rb') as stream:
            decoded = stream.read(row['bytes'] + 1)
        actual = verify(decoded, row)
        data = decoded
    else:
        data, transport = fetch(row, row)
        actual = verify(data, row)
    with target.open('xb') as stream:
        stream.write(data)
    return {'local_path': row['local_path'], **actual, 'status': 'RESTORED_EXACT_BYTES', 'transport': transport, 'semantic_credit': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch', required=True, choices=[f'R7-U{i:02}' for i in range(1, 14)])
    parser.add_argument('--destination', required=True)
    parser.add_argument('--plan-directory', type=Path, default=Path(__file__).resolve().parents[1] / 'recovery/batches')
    parser.add_argument('--evidence-only', action='store_true', help='Skip fixed source/formal snapshots only when another verified checkout already supplies them.')
    parser.add_argument('--resume', action='store_true', help='Preserve existing files and reuse only files whose exact expected identity matches.')
    args = parser.parse_args()
    plan_path = args.plan_directory / (args.batch + '.json')
    plan_bytes = plan_path.read_bytes()
    plan = json.loads(plan_bytes)
    if plan['batch_id'] != args.batch or plan['unresolved_reference_fields']:
        raise ValueError('batch mismatch or unresolved evidence references')
    TRANSPORT_LOCKS.update({row['transport_path']: threading.Lock() for row in plan['evidence']})
    raw_destination = Path(args.destination).absolute()
    if raw_destination.is_symlink() or any(p.is_symlink() for p in raw_destination.parents):
        raise ValueError('destination must not contain symlinks')
    destination = raw_destination.resolve()
    destination.mkdir(parents=True, exist_ok=args.resume)
    rows = [(row, False) for row in plan['artifacts']]
    rows += [(row, True) for row in plan['evidence']]
    if not args.evidence_only:
        rows += [(row, False) for row in plan['fixed_read_inputs']]
    paths = [row['local_path'] for row, _ in rows]
    if len(paths) != len(set(paths)):
        raise ValueError('duplicate output paths')
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    receipt = {'schema': 'r7.bounded-container-restoration-receipt.v1', 'batch_id': args.batch,
               'start_utc': utc(), 'destination': str(destination), 'plan': str(plan_path),
               'plan_identity': identity(plan_bytes), 'fixed_contract_commit': plan['contract_commit'],
               'evidence_publication_commit': plan['evidence_publication_commit'], 'files': [],
               'author_tasks_started': 0, 'reviewer_tasks_started': 0, 'semantic_PASS': False,
               'effective_model_configuration': 'UNVERIFIED', 'evidence_only': args.evidence_only,
               'new_host_Demo_native_media_real_save_replay': 0,
               'path_map': {'/workspace/r7-evidence': str(destination/'evidence'),
                            '/workspace/r7-reference': str(destination/'inputs/reference'),
                            'frozen_project_input_paths': str(destination/'inputs/project'),
                            'compact_dispatch': str(destination/'dispatch')},
               'snapshot_qualification': 'Selected immutable files only. This is not a full reference/project Git checkout. Writable candidates stay in the actual author project; never edit these frozen inputs. Do not execute restored programs.',
               'L01_L14': 'RETAINED', 'future_paths_not_downloaded': plan['future_paths_not_downloaded']}
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            futures = [pool.submit(restore_one, destination, row, encoded) for row, encoded in rows]
            errors = []
            for future in futures:
                try:
                    receipt['files'].append(future.result())
                except Exception as error:
                    errors.append(str(error))
            if errors:
                raise RuntimeError(json.dumps(errors))
        receipt['status'] = 'BOUNDED_RESTORE_BYTES_VERIFIED'
    except Exception as error:
        receipt['status'] = 'PARTIAL_RESTORE_PRESERVED'
        receipt['error'] = str(error)
        raise
    finally:
        receipt['end_utc'] = utc()
        receipt['files_verified'] = len(receipt['files'])
        receipt['bytes_verified'] = sum(row['bytes'] for row in receipt['files'])
        with (destination/('recovery-receipt-' + stamp + '.json')).open('x') as stream:
            json.dump(receipt, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
    print(json.dumps({k: receipt[k] for k in ['status', 'batch_id', 'files_verified', 'bytes_verified', 'destination', 'author_tasks_started', 'reviewer_tasks_started']}))


if __name__ == '__main__':
    main()
