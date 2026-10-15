"""Read selected JSON evidence at explicit pointers; no behavior execution."""
import json,sys,datetime,os
from pathlib import Path
from run_logged import identity
p=Path(sys.argv[1]);d=json.loads(p.read_bytes());selections=[]
for ptr in sys.argv[2:] or ['']:
    x=d
    for k in ptr.strip('/').split('/') if ptr else []:
        k=k.replace('~1','/').replace('~0','~');x=x[int(k)] if isinstance(x,list) else x[k]
    selections.append({'pointer':ptr,'value':x})
row={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pid':os.getpid(),'path':str(p),'identity':identity(p.read_bytes()),'selected_pointers':[s['pointer'] for s in selections],'scope':'Selected JSON content, not a claim of whole-file semantic reading'}
with (Path(__file__).parent/'json-reading-ledger.jsonl').open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
print(json.dumps({'file':str(p),'selections':selections},ensure_ascii=False,indent=2))
