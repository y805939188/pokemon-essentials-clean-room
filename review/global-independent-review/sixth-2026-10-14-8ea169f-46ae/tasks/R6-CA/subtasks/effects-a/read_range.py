"""Audit-only range reader. Explicit input path/range; output remains in this directory."""
import sys, pathlib, hashlib, json, datetime
root=pathlib.Path(__file__).resolve().parent
p=pathlib.Path(sys.argv[1]); start=int(sys.argv[2]); end=int(sys.argv[3])
raw=p.read_bytes(); lines=raw.decode().splitlines()
assert 1 <= start <= end <= len(lines)
tag=p.name.replace(' ','_')+f'.{start}-{end}'
out='\n'.join(f'{i}: {lines[i-1]}' for i in range(start,end+1))+'\n'
(root/'logs').mkdir(exist_ok=True)
(root/'logs'/f'{tag}.txt').write_text(out)
with (root/'reading-ledger.jsonl').open('a') as f:
 f.write(json.dumps({'path':str(p),'start':start,'end':end,'sha256':hashlib.sha256(raw).hexdigest(),'stage':'continuous_range_output','semantic_pass_implied':False,'log':'logs/'+tag+'.txt','time':datetime.datetime.now(datetime.timezone.utc).isoformat()})+'\n')
print(out,end='')
