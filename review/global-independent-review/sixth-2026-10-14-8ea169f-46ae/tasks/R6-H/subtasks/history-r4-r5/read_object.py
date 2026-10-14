import hashlib, json, subprocess, sys, datetime
from pathlib import Path

OUT = Path(__file__).resolve().parent
ALLOWED = {'8ea169fbd0f33f378b5d732fd6bea59e854e04a6', 'b67f542b47ad33ac23053a21f62748077c167a23', 'f49d870c6fd616ab6736754a218a4553b5acac7f', '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b', 'debf59f3c5370df253706969fd4dd1c103300bf2', '123500de1c189458757e8d3d4abf8604428f6eb2'}
commit, path = sys.argv[1:3]
if commit not in ALLOWED or path.startswith('/') or '..' in path.split('/'):
    raise SystemExit('unbound input')
git = ['git', '-C', 'reference/pokemon-essentials'] if commit == '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' else ['git']
raw = subprocess.check_output(git + ['show', f'{commit}:{path}'])
lines = raw.decode('utf-8').splitlines()
start = int(sys.argv[3]) if len(sys.argv) > 3 else 1
end = min(int(sys.argv[4]), len(lines)) if len(sys.argv) > 4 else len(lines)
if start < 1 or end < start or start > len(lines):
    raise SystemExit('invalid interval')
record = {'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'commit': commit, 'path': path, 'sha256': hashlib.sha256(raw).hexdigest(), 'total_lines': len(lines), 'start_line': start, 'end_line': end, 'mode': 'full_text_presented_for_semantic_review', 'semantic_pass': False, 'tool': 'read_object.py', 'exit_status': 0}
with (OUT / 'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(record, ensure_ascii=False) + '\n')
print(json.dumps(record, ensure_ascii=False))
for number in range(start, end + 1):
    print(f'{number:06d} {lines[number - 1]}')
