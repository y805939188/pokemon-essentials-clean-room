import sys,json,subprocess
from pathlib import Path
root=Path(__file__).resolve().parent
req=json.loads(sys.argv[1])
log=root/'read-log.jsonl'
for r in req:
 p=r['path']; rev=r.get('revision')
 s=subprocess.check_output(['git','show',rev+':'+p],text=True) if rev else Path(p).read_text()
 ls=s.splitlines();ranges=r.get('ranges',[[1,len(ls)]])
 print('FILE '+p+(' @'+rev if rev else ''))
 for a,b in ranges:
  for n in range(a,min(b,len(ls))+1):print(str(n)+': '+ls[n-1])
 with log.open('a') as o:o.write(json.dumps(dict(r,ranges=ranges,line_count=len(ls)),ensure_ascii=False)+'\n')
