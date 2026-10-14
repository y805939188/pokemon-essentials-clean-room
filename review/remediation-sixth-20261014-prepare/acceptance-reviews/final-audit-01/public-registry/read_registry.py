import datetime, hashlib, json, pathlib, subprocess, sys, traceback

BASE = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OWNED = BASE / 'review/remediation-sixth-20261014-prepare/acceptance-reviews/final-audit-01/public-registry'
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
path = sys.argv[1]
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1
hi = int(sys.argv[3]) if len(sys.argv) > 3 else None
commit = sys.argv[4] if len(sys.argv) > 4 else '229260cfd5177581bb88bafd84770ceb1c11b117'
meta = {'utc_start': started, 'cwd': str(pathlib.Path.cwd()), 'argv': sys.argv,
        'commit': commit, 'path': path}
try:
    if path.startswith(str(OWNED.relative_to(BASE))):
        raw = (BASE / path).read_bytes()
        entry, tree = 'UNTRACKED_OWNED_ARTIFACT', None
    else:
        raw = subprocess.check_output(['git', 'show', commit + ':' + path])
        entry = subprocess.check_output(['git', 'ls-tree', commit, '--', path], text=True).strip()
        tree = subprocess.check_output(['git', 'rev-parse', commit + '^{tree}'], text=True).strip()
    lines = raw.decode().splitlines()
    hi = len(lines) if hi is None else min(hi, len(lines))
    meta.update({'tree': tree, 'mode_type_blob_path': entry, 'bytes': len(raw),
                 'sha256': hashlib.sha256(raw).hexdigest(),
                 'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest(),
                 'lines': len(lines), 'range': [lo, hi],
                 'full_payload_emitted': lo == 1 and hi == len(lines), 'exit': 0, 'stderr': ''})
    payload = '\n'.join(str(i + 1) + ':' + lines[i] for i in range(lo - 1, hi)) + '\n'
except Exception:
    meta.update({'exit': 1, 'stderr': traceback.format_exc()})
    payload = ''
meta['utc_end'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
text = json.dumps(meta, ensure_ascii=False) + '\n' + payload
transcript = OWNED / ('read-' + datetime.datetime.now(datetime.timezone.utc).strftime('%H%M%S%f') + '.txt')
transcript.write_text(text)
meta['stdout_path'] = str(transcript.relative_to(BASE))
meta['stdout_sha256'] = hashlib.sha256(text.encode()).hexdigest()
with (OWNED / 'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(meta, ensure_ascii=False) + '\n')
print(text, end='')
sys.exit(meta['exit'])
