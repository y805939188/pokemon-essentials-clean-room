"""Audit-only range reader. Reads bound repository inputs; writes only beside itself.

Emitting a range records text access, never semantic approval. No source execution.
"""
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OUT = pathlib.Path(__file__).resolve().parent
path = pathlib.Path(sys.argv[1])
if path.is_absolute() or '..' in path.parts:
    raise SystemExit('relative repository path required')
allowed = (
    'reference/pokemon-essentials/Data/Scripts/011_Battle/',
    'deliverables/final-specification-set/',
    'reference/pokemon-essentials/Data/Scripts/003_Game processing/005_Event_Handlers.rb',
    'reference/pokemon-essentials/Data/Scripts/001_Technical/001_Debugging/001_PBDebug.rb',
    'reference/pokemon-essentials/Data/Scripts/010_Data/001_GameData.rb',
    'reference/pokemon-essentials/PBS/moves.txt',
)
if str(path) != 'AGENTS.md' and not str(path).startswith(allowed):
    raise SystemExit('input outside bound review scope')
raw = (ROOT / path).read_bytes()
lines = raw.decode('utf-8-sig').splitlines()
start, end = int(sys.argv[2]), int(sys.argv[3])
if not 1 <= start <= end <= len(lines):
    raise SystemExit('invalid line range')
digest = hashlib.sha256(raw).hexdigest()
log_dir = OUT / 'logs'
log_dir.mkdir(exist_ok=True)
name = f'{path.name}.{start:04d}-{end:04d}.txt'
body = '\n'.join(f'{i}: {lines[i-1]}' for i in range(start, end+1)) + '\n'
(log_dir / name).write_text(body)
record = dict(path=str(path), start=start, end=end, total_lines=len(lines), sha256=digest,
              evidence='static_source_or_formal_text', stage='range_emitted_not_semantic_pass',
              log='logs/' + name)
with (OUT / 'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(record, ensure_ascii=False) + '\n')
print(body, end='')
