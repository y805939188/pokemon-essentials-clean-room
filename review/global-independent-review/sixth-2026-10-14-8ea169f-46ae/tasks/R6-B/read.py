"""Read only source/formal/evidence ranges and persist presented-text records.
No source execution. A presentation entry is not a semantic PASS.
"""
from pathlib import Path
import hashlib, json, sys, datetime
BASE = Path(__file__).resolve().parent
WORK = BASE.parents[4]
p = (WORK / sys.argv[1]).resolve()
allowed = [WORK/'reference/pokemon-essentials', WORK/'deliverables/final-specification-set', BASE.parents[1], WORK/'AGENTS.md']
if not any(p == q or q in p.parents for q in allowed):
    raise ValueError('outside bound review inputs')
b = p.read_bytes()
lines = b.decode('utf-8', errors='replace').splitlines()
start, end = int(sys.argv[2]), int(sys.argv[3])
if not 1 <= start <= end <= len(lines):
    raise ValueError('range outside file')
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
body = '\n'.join(f'{i}: {lines[i-1]}' for i in range(start,end+1))+'\n'
log = BASE/'logs'/f'{stamp}-{p.name}-{start}-{end}.txt'
log.write_text(body)
row = {'time':stamp,'path':str(p.relative_to(WORK)), 'sha256':hashlib.sha256(b).hexdigest(), 'range':[start,end], 'total_lines':len(lines), 'mode':'full_text_presented', 'semantic_status':'PRESENTED_PENDING_SEMANTIC_ASSESSMENT','log':str(log.relative_to(BASE))}
with (BASE/'reading-ledger.jsonl').open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
print(f'FILE {row["path"]} SHA256 {row["sha256"]} LINES {start}-{end}/{len(lines)}')
print(body,end='')
