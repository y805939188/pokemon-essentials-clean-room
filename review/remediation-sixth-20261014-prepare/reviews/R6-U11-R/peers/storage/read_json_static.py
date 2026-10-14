import datetime, hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT / 'review/remediation-sixth-20261014-prepare/reviews/R6-U11-R/peers/storage'
kind, revision, path, *pointers = sys.argv[1:]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
argv = ['git', 'show', revision + ':' + path] if kind == 'git' else None
if argv:
    proc = subprocess.run(argv, cwd=ROOT, capture_output=True, check=True)
    payload = proc.stdout
    entry = subprocess.run(['git', 'ls-tree', revision, '--', path], cwd=ROOT, capture_output=True, check=True).stdout.decode().strip()
else:
    payload = (ROOT / path).read_bytes()
    entry = 'filesystem regular file; Git blob computed without write'
value = json.loads(payload)
selected = {}
for pointer in pointers:
    node = value
    for bit in pointer.lstrip('/').split('/') if pointer else []:
        key = bit.replace('~1', '/').replace('~0', '~')
        node = node[int(key)] if isinstance(node, list) else node[key]
    selected[pointer or 'ROOT'] = node
record = {'utc_start': started, 'utc_end': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'cwd': str(ROOT), 'reader_argv': sys.argv, 'source_argv': argv, 'kind': kind, 'commit': revision if argv else None, 'path': path, 'bytes': len(payload), 'lines': len(payload.decode().splitlines()), 'sha256': hashlib.sha256(payload).hexdigest(), 'git_blob': hashlib.sha1(b'blob ' + str(len(payload)).encode() + b'\0' + payload).hexdigest(), 'git_entry': entry, 'complete_json_nodes_read': pointers, 'evidence_level': 'STATIC_DOCUMENT_READ', 'exit': 0, 'source_stderr': ''}
with (OUT / 'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(record, ensure_ascii=False) + '\n')
print(json.dumps(record, ensure_ascii=False))
print(json.dumps(selected, ensure_ascii=False, indent=2))
