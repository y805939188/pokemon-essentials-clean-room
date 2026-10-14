"""Fixed-input read-only range emitter; writes only R6-DX logs/ledger.
No reference code is executed; emitted source ranges are audit evidence, not specs.
"""
import sys, json, hashlib, subprocess, datetime
from pathlib import Path
ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-DX/debug'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
p = Path(sys.argv[1])
start, end = int(sys.argv[2]), int(sys.argv[3])
if p.is_absolute() or '..' in p.parts:
    raise SystemExit('invalid relative path')
is_ref = str(p).startswith('reference/pokemon-essentials/')
repo = ROOT / 'reference/pokemon-essentials' if is_ref else ROOT
rel = str(p.relative_to('reference/pokemon-essentials')) if is_ref else str(p)
revision = REF if is_ref else MAIN
if not (is_ref or str(p).startswith('deliverables/final-specification-set/') or str(p) == 'AGENTS.md'):
    raise SystemExit('input outside assigned frozen-input families')
data = subprocess.check_output(['git', '-C', str(repo), 'show', revision + ':' + rel])
if (ROOT / p).read_bytes() != data:
    raise SystemExit('working input differs from fixed blob')
lines = data.decode('utf-8-sig').splitlines()
if not 1 <= start <= end <= len(lines):
    raise SystemExit('range out of bounds')
stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
key = hashlib.sha256((str(p) + str(start) + str(end) + stamp).encode()).hexdigest()[:16]
log = OUT / 'logs' / (key + '.txt')
log.parent.mkdir(parents=True, exist_ok=True)
rendered = '\n'.join(f'{n}: {lines[n-1]}' for n in range(start, end+1)) + '\n'
log.write_text(rendered)
record = {'timestamp': stamp, 'path': str(p), 'revision': revision, 'sha256': hashlib.sha256(data).hexdigest(), 'start': start, 'end': end, 'total_lines': len(lines), 'mode': 'emitted_for_manual_semantic_read', 'semantic_pass': False, 'log': str(log.relative_to(ROOT))}
with (OUT / 'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(record, ensure_ascii=False) + '\n')
print(json.dumps(record, ensure_ascii=False))
print(rendered, end='')
