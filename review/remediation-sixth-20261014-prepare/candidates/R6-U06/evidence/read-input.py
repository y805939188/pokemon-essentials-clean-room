#!/usr/bin/env python3
"""Read fixed Git blobs; record exact scopes. Does not execute reference code."""
import datetime
import hashlib
import json
import subprocess
import sys
from pathlib import Path

EVIDENCE = Path(__file__).resolve().parent
PROJECT = EVIDENCE.parents[4]
REFER = Path('/tmp/r6-u06-reference.git')
COMMITS = {'source': '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
           'formal': '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'}
kind, path, *ranges = sys.argv[1:]
repo = REFER if kind == 'source' else PROJECT
commit = COMMITS[kind]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
argv = ['git', '-C', str(repo), 'cat-file', 'blob', commit + ':' + path]
p = subprocess.run(argv, capture_output=True, check=False)
if p.returncode:
    raise SystemExit(p.stderr.decode())
b = p.stdout
entry = subprocess.check_output(['git', '-C', str(repo), 'ls-tree', commit, '--', path], text=True).strip()
mode, typ, blobpath = entry.split(' ', 2)
blob, _ = blobpath.split('\t', 1)
lines = b.decode().splitlines()
scopes = [tuple(map(int, x.split(':'))) for x in ranges] if ranges else [(1, len(lines))]
output = f'FIXED_INPUT {kind} {path} {commit} {mode} {typ} {blob}\n'
for a, z in scopes:
    assert 1 <= a <= z <= len(lines), (a, z, len(lines))
    output += f'COMPLETE_RANGE {a}:{z}\n'
    output += '\n'.join(f'{i}: {lines[i-1]}' for i in range(a, z+1)) + '\n'
row = dict(kind=kind, path=path, repository=str(repo), commit=commit, mode=mode,
           type=typ, bytes=len(b), sha256=hashlib.sha256(b).hexdigest(), git_blob=blob,
           ranges=scopes, file_lines=len(lines), argv=argv, cwd=str(Path.cwd()),
           started_utc=started, ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
           exit=p.returncode, stderr=p.stderr.decode(), stdout_sha256=hashlib.sha256(output.encode()).hexdigest(),
           evidence_level='SOURCE_STATIC' if kind == 'source' else 'FORMAL_READ',
           emission_does_not_prove_semantic_read=True, reference_execution=False)
with (EVIDENCE/'reading-scopes.jsonl').open('a') as f:
    f.write(json.dumps(row, ensure_ascii=False)+'\n')
print(output, end='')
