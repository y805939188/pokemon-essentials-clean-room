from pathlib import Path
import sys,json,datetime
root=Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
out=root/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-O'
inv=json.loads((out/'inventory.json').read_text())
kind=sys.argv[1]
for arg in sys.argv[2:]:
 a=arg.split(':'); idx=int(a[0]); ent=inv[kind][idx]; lines=(root/ent['path']).read_text().splitlines(); start=int(a[1]) if len(a)>1 else 1; end=int(a[2]) if len(a)>2 else len(lines)
 print('FILE '+ent['path']+' RANGE '+str(start)+'-'+str(end))
 for n in range(start,end+1): print(str(n)+': '+lines[n-1])
 with (out/'command-log.jsonl').open('a') as f:f.write(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':'read-range.py '+kind+' '+arg,'path':ent['path'],'start':start,'end':end,'result':'Printed full requested range; semantic assessment separately recorded in ledger.'},ensure_ascii=False)+'\n')
