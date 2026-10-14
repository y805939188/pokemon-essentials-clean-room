#!/usr/bin/env python3
"""Read fixed Git text without evaluating it; record identity and displayed range."""
import datetime, hashlib, json, pathlib, subprocess, sys

OWN = pathlib.Path(__file__).resolve().parent
repo, commit, path, first, last = sys.argv[1:]
first, last = int(first), int(last)
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
argv = ['git', '-C', repo, 'show', commit + ':' + path]
p = subprocess.run(argv, capture_output=True)
if p.returncode:
    sys.stderr.buffer.write(p.stderr)
    raise SystemExit(p.returncode)
data = p.stdout
lines = data.decode('utf-8').splitlines()
last = len(lines) if last == 0 else last
assert 1 <= first <= last <= len(lines), (first, last, len(lines))
row = dict(argv=argv, cwd=str(pathlib.Path.cwd()), started_utc=started,
           ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
           exit=p.returncode, stderr=p.stderr.decode(), repository=repo,
           commit=commit, path=path, bytes=len(data),
           sha256=hashlib.sha256(data).hexdigest(),
           git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
           read_range=[first,last], total_lines=len(lines),
           level='DISPLAYED_TEXT_FOR_INDEPENDENT_SEMANTIC_READING',
           source_execution=False)
with (OWN/'read-events.jsonl').open('a') as f:
    f.write(json.dumps(row,ensure_ascii=False)+'\n')
print(json.dumps({k:row[k] for k in ['commit','path','read_range','total_lines','git_blob']},ensure_ascii=False))
for n in range(first,last+1): print(f'{n}: {lines[n-1]}')
