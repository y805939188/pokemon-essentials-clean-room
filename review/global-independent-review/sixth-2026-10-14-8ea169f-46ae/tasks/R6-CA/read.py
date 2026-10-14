"""Read-only range display. Writes evidence only below this task directory.
Input: an existing UTF-8 text file below workspace; explicit inclusive line range.
Output: numbered range to stdout and logs; append physical-read ledger, never PASS.
Does not execute any input or import project code.
"""
import sys, json, hashlib, datetime
from pathlib import Path

WORK = Path('/Users/dingshinn/Desktop/pokemon-framework-reference').resolve()
OUT = Path(__file__).resolve().parent
p = (WORK / sys.argv[1]).resolve()
assert p.is_relative_to(WORK) and p.is_file()
first, last = int(sys.argv[2]), int(sys.argv[3])
raw = p.read_bytes()
lines = raw.decode('utf-8-sig').splitlines()
assert 1 <= first <= last <= len(lines), (first, last, len(lines))
content = '\n'.join(f'{i}: {lines[i-1]}' for i in range(first, last+1)) + '\n'
logs = OUT / 'logs'
logs.mkdir(exist_ok=True)
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
name = stamp + '-' + p.name.replace(' ', '_') + f'-{first}-{last}.txt'
(logs / name).write_text(content)
entry = dict(event='physical_read', path=str(p.relative_to(WORK)), start=first,
             end=last, total_lines=len(lines), sha256=hashlib.sha256(raw).hexdigest(),
             log='logs/'+name, semantics='PENDING_EXPLICIT_REVIEW', timestamp=stamp)
with (OUT/'reading-ledger.jsonl').open('a') as f:
    f.write(json.dumps(entry, ensure_ascii=False)+'\n')
print(content, end='')
