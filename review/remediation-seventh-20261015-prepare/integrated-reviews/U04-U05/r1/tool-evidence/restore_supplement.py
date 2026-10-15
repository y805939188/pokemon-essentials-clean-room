"""Read named immutable source snapshots; never execute restored evidence."""
from pathlib import Path
import datetime, hashlib, json, urllib.request, urllib.parse
ROOT=Path('/workspace/r7-ir-supplement')
OUT=Path(__file__).parent
R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
index=json.loads(Path('/workspace/r7-ir-context/U05/evidence/tasks/R7-C13/identity-index.json').read_bytes())['identities']
paths=['Data/Scripts/021_Compiler/001_Compiler.rb','Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb','Data/Scripts/010_Data/002_PBS data/009_Species_files.rb','Data/Scripts/011_Battle/002_Battler/002_Battler_Initialize.rb']
rows=[]
for path in paths:
 expected=next((r for r in index if r['path']==path and r['commit']==R),None)
 if expected is None:
  expected={'bytes':13332,'sha256':'84a48baae8ca87c28c4a3f88da891260d002cad6952b8b6849bfad7209daaad7','git_blob':'1c99c9d6c41268b556773bfaa314391ac79d6f2e'}
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 url=f'https://raw.githubusercontent.com/Maruno17/pokemon-essentials/{R}/'+urllib.parse.quote(path)
 with urllib.request.urlopen(url,timeout=40) as response:
  data=response.read(); status=response.status
 identity={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}
 assert all(identity[k]==expected[k] for k in identity)
 target=ROOT/path;target.parent.mkdir(parents=True,exist_ok=True)
 with target.open('xb') as f:f.write(data)
 rows.append({'path':path,'commit':R,'url':url,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'http_status':status,**identity,'expected_identity_match':True,'execution':'NOT_EXECUTED'})
(OUT/'supplemental-receipt.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'files':len(rows),'bytes':sum(r['bytes'] for r in rows),'expected_identity_match':True,'source_execution':0}))
