import datetime, hashlib, json, pathlib, subprocess, sys
ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT/'review/remediation-sixth-20261014-prepare/actual-reviews/group-D/peers/u10/final-increment'
kind, rev, path, *selectors = sys.argv[1:]
start = datetime.datetime.now(datetime.timezone.utc).isoformat()
argv = ['git', 'show', rev+':'+path] if kind == 'git' else None
if argv:
    p = subprocess.run(argv, cwd=ROOT, capture_output=True)
    if p.returncode:
        rec = {'utc_start': start, 'utc_end': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'cwd': str(ROOT), 'reader_argv': sys.argv, 'source_argv': argv, 'exit': p.returncode, 'stderr': p.stderr.decode(), 'source_execution': False}
        with (OUT/'failed-reads.jsonl').open('a') as f:
            f.write(json.dumps(rec, ensure_ascii=False)+'\n')
        print(json.dumps(rec, ensure_ascii=False)); raise SystemExit(p.returncode)
    data = p.stdout
    entry = subprocess.run(['git', 'ls-tree', rev, '--', path], cwd=ROOT, capture_output=True, check=True).stdout.decode().strip()
else:
    data = (ROOT/path).read_bytes(); entry = 'filesystem regular UTF-8 file'
lines = data.decode().splitlines()
rec = {'utc_start': start, 'utc_end': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'cwd': str(ROOT), 'reader_argv': sys.argv, 'source_argv': argv, 'kind': kind, 'commit': rev if argv else None, 'path': path, 'bytes': len(data), 'lines': len(lines), 'sha256': hashlib.sha256(data).hexdigest(), 'git_blob': hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(), 'git_entry': entry, 'selectors': selectors, 'source_execution': False, 'exit': 0, 'stderr': ''}
output = []
for s in selectors:
    if ':' in s and not s.startswith('/'):
        a,b = map(int, s.split(':')); assert 1 <= a <= b <= len(lines)
        output.append('\n'.join(str(i)+': '+lines[i-1] for i in range(a,b+1)))
    else:
        node = json.loads(data)
        for bit in s.lstrip('/').split('/') if s else []:
            key = bit.replace('~1','/').replace('~0','~'); node = node[int(key)] if isinstance(node,list) else node[key]
        output.append(s+': '+json.dumps(node, ensure_ascii=False, separators=(',',':')))
with (OUT/'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(rec, ensure_ascii=False)+'\n')
print(json.dumps(rec, ensure_ascii=False))
for item in output: print(item)
