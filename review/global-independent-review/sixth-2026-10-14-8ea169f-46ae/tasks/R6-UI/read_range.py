"""Frozen-input range delivery only; it never declares semantic review passed."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-UI'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
parser = argparse.ArgumentParser()
parser.add_argument('path')
parser.add_argument('start', type=int)
parser.add_argument('end', type=int)
parser.add_argument('--owner', default='root')
args = parser.parse_args()
assert args.owner.replace('_', '').isalnum()
assert '..' not in Path(args.path).parts
if args.path.startswith('reference/pokemon-essentials/'):
    repo, rev = ROOT / 'reference/pokemon-essentials', REF
    rel = args.path.removeprefix('reference/pokemon-essentials/')
elif args.path.startswith('deliverables/final-specification-set/'):
    repo, rev, rel = ROOT, MAIN, args.path
else:
    raise ValueError('Only fixed reference or formal input allowed')
data = subprocess.run(['git', '-C', str(repo), 'show', f'{rev}:{rel}'], check=True, capture_output=True).stdout
lines = data.decode('utf-8').splitlines()
if args.end == 0:
    args.end = len(lines)
assert 1 <= args.start <= args.end <= len(lines)
header = {'path': args.path, 'commit': rev, 'range': [args.start, args.end], 'total_lines': len(lines), 'sha256': hashlib.sha256(data).hexdigest(), 'owner': args.owner, 'stage': 'delivered_for_semantic_read', 'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat()}
body = json.dumps(header, ensure_ascii=False) + '\n' + '\n'.join(f'{i}: {lines[i-1]}' for i in range(args.start, args.end+1)) + '\n'
logdir = OUT / args.owner / 'read-logs'
logdir.mkdir(parents=True, exist_ok=True)
name = args.path.replace('/', '__') + f'.{args.start}-{args.end}.txt'
(logdir / name).write_text(body)
with (OUT / args.owner / 'delivery-ledger.jsonl').open('a') as handle:
    handle.write(json.dumps(header, ensure_ascii=False) + '\n')
print(body, end='')
