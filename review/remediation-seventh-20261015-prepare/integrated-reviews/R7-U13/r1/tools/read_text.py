"""Print bounded full-content read segments and preserve a literal read ledger."""
from pathlib import Path
import datetime,hashlib,json,os,sys
root=Path(__file__).resolve().parent
p=Path(sys.argv[1]);start=int(sys.argv[2]) if len(sys.argv)>2 else 1
lines=p.read_text().splitlines(keepends=True);end=int(sys.argv[3]) if len(sys.argv)>3 else len(lines)
chunk=''.join(lines[start-1:end]);data=p.read_bytes()
print(f'FILE {p} L{start}-{min(end,len(lines))}/{len(lines)}')
for i,line in enumerate(lines[start-1:end],start):print(f'{i}: {line}',end='' if line.endswith('\n') else '\n')
row=dict(path=str(p),start_line=start,end_line=min(end,len(lines)),total_lines=len(lines),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),segment_sha256=hashlib.sha256(chunk.encode()).hexdigest(),utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),pid=os.getpid(),qualification='Literal text exposed for current reviewer content reading; identity is separate from semantic judgment.')
with (root/'reading-ledger.jsonl').open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
