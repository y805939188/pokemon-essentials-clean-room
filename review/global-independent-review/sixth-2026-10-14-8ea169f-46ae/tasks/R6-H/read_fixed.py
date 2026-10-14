"""Read-only fixed Git-object interval emitter; output is review evidence only."""
import argparse
import hashlib
import json
import pathlib
import subprocess
import datetime

ROOT = pathlib.Path(__file__).resolve().parent
REFS = {
    'main': '8ea169fbd0f33f378b5d732fd6bea59e854e04a6',
    'core': 'b67f542b47ad33ac23053a21f62748077c167a23',
    'candidate': '13fddb0a217b36974c75657aa68da0caf104ee48',
    'fifth': 'f49d870c6fd616ab6736754a218a4553b5acac7f',
    'u1': '37a19bcc88551d98de22100fe81aad46cf5b818d',
    'u2': '8191a13a437b902b23c517f3ef10742eee7b8081',
    'u3': 'b1589101dd8afc37afa4fa83d0d2159079483066',
    'u4': '86650115788158f5ad4fc680e63ad4355ede0ab2',
    'u5': '92f924edbba3f658a73ffff7f4c7f8f5da971830',
    'u6': '75cddf342ec5301b03ddeacc0264f58dc8c8edcb',
    'u7': '123500de1c189458757e8d3d4abf8604428f6eb2',
    'u8': 'debf59f3c5370df253706969fd4dd1c103300bf2',
    'closing': '044c3483229e7e76bedf1fc244fc84d274bf059c',
}
p = argparse.ArgumentParser()
p.add_argument('ref', choices=REFS)
p.add_argument('path')
p.add_argument('start', type=int)
p.add_argument('end', type=int)
a = p.parse_args()
assert a.start >= 1 and a.end >= a.start
assert not a.path.startswith('/') and '..' not in pathlib.PurePosixPath(a.path).parts
obj = REFS[a.ref] + ':' + a.path
r = subprocess.run(['git', 'show', obj], capture_output=True, check=True)
lines = r.stdout.decode('utf-8').splitlines()
assert a.start <= len(lines) and a.end <= len(lines)
out = ''.join(f'{i}: {lines[i-1]}\n' for i in range(a.start, a.end+1))
key = hashlib.sha256((obj+f':{a.start}:{a.end}').encode()).hexdigest()[:20]
logs = ROOT / 'read-logs'
logs.mkdir(exist_ok=True)
log = logs / (key + '.txt')
log.write_text(out)
entry = {
    'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'ref': REFS[a.ref], 'path': a.path, 'range': [a.start, a.end],
    'total_lines': len(lines), 'sha256': hashlib.sha256(r.stdout).hexdigest(),
    'mode': 'fulltext_interval_emitted', 'semantic_status': 'PENDING_MANUAL_REVIEW',
    'exit_code': r.returncode, 'log': str(log.relative_to(ROOT)),
}
with (ROOT / 'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(entry, ensure_ascii=False) + '\n')
print(json.dumps(entry, ensure_ascii=False))
print(out, end='')
