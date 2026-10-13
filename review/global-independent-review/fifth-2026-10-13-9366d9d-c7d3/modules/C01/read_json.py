import json,sys,subprocess
from pathlib import Path
root=Path(__file__).resolve().parent
for r in json.loads(sys.argv[1]):
 raw=subprocess.check_output(['git','show',r['revision']+':'+r['path']],text=True) if r.get('revision') else Path(r['path']).read_text()
 d=json.loads(raw);print('FILE',r['path'],r.get('revision',''))
 for pointer in r['pointers']:
  v=d
  for k in pointer.split('/')[1:]:v=v[int(k)] if isinstance(v,list) else v[k.replace('~1','/').replace('~0','~')]
  print('POINTER',pointer); print(json.dumps(v,ensure_ascii=False,indent=2))
 with (root/'json-read-log.jsonl').open('a') as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
