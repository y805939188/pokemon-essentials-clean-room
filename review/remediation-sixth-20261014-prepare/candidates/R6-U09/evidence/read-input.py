#!/usr/bin/env python3
"""Emit frozen text for author reading and record the exact range, without execution."""
import datetime
import hashlib
import json
import pathlib
import sys

evidence = pathlib.Path(__file__).resolve().parent
prepare = evidence.parents[2]
repo = prepare.parents[1]
paths = [json.loads(x['stdout'])['path'] for x in json.loads((evidence / 'input-retrieval.json').read_text()) if x['exit'] == 0]
paths += [str(x) for x in pathlib.Path('/workspace/r6-input-cache/frozen-payloads').rglob('*') if x.is_file()]
paths += [str(x) for x in (prepare / 'inputs/evidence').rglob('*') if x.is_file()]
query, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
matches = sorted(set(x for x in paths if x.endswith(query)))
if len(matches) != 1:
    raise SystemExit(f'Expected one input: {matches}')
p = pathlib.Path(matches[0]); data = p.read_bytes(); lines = data.decode('utf-8-sig').splitlines()
last = min(last, len(lines))
assert 1 <= first <= last
out = '\n'.join(f'{n}: {lines[n-1]}' for n in range(first, last+1)) + '\n'
record = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'cwd':str(repo),
          'argv':sys.argv, 'path':str(p), 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest(),
          'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
          'range':[first,last], 'total_lines':len(lines), 'emitted_sha256':hashlib.sha256(out.encode()).hexdigest(),
          'level':'TEXT_EMITTED_FOR_AUTHOR_READ', 'semantic_pass':False, 'execution':False, 'exit':0, 'stderr':''}
with (evidence / 'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(record,ensure_ascii=False)+'\n')
print(str(p)); print(out,end='')
