import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent
p = argparse.ArgumentParser()
p.add_argument('path')
p.add_argument('start', type=int)
p.add_argument('end', type=int)
p.add_argument('--object', default='8ea169fbd0f33f378b5d732fd6bea59e854e04a6')
p.add_argument('--repo', default='/Users/dingshinn/Desktop/pokemon-framework-reference')
p.add_argument('--kind', choices=['full_text_read','structural_read','inventory_only'], default='full_text_read')
a = p.parse_args()
if a.object == 'workspace':
    raw = Path(a.path).read_bytes()
    source_id = 'workspace:' + a.path
else:
    r = subprocess.run(['git','-C',a.repo,'show',a.object+':'+a.path], capture_output=True, check=True)
    raw = r.stdout
    source_id = a.object+':'+a.path
lines = raw.decode('utf-8').splitlines()
if not (1 <= a.start <= a.end <= len(lines)):
    raise ValueError('range outside document')
ledger = ROOT/'reading-ledger.jsonl'
seq = len(ledger.read_text().splitlines())+1 if ledger.exists() else 1
shown = '\n'.join(f'{i}: {lines[i-1]}' for i in range(a.start,a.end+1))+'\n'
log = ROOT/'logs'/f'read-{seq:03}.txt'
log.write_text(shown)
entry = {'sequence':seq,'source':source_id,'start_line':a.start,'end_line':a.end,'total_lines':len(lines),'sha256':hashlib.sha256(raw).hexdigest(),'kind':a.kind,'semantic_status':'not_automatically_passed','stdout_log':str(log.relative_to(ROOT))}
with ledger.open('a') as f:
    f.write(json.dumps(entry,ensure_ascii=False)+'\n')
print(shown,end='')
