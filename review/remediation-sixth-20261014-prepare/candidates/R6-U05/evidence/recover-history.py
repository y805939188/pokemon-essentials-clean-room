from pathlib import Path
import json, urllib.request, hashlib
from concurrent.futures import ThreadPoolExecutor
e=Path(__file__).resolve().parent
bindings=json.loads((e/'historical-input-bindings.json').read_text())
def recover(pair):
 path,row=pair
 b=urllib.request.urlopen('https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+row['commit']+'/'+path,timeout=45).read()
 a={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
 assert all(a[k]==row[k] for k in a),(path,a)
 (Path('/tmp')/('r6-u05-'+Path(path).name)).write_bytes(b)
 return {'path':path,'commit':row['commit'],**a}
with ThreadPoolExecutor(max_workers=3) as pool:
 for result in pool.map(recover,bindings['files'].items()): print(json.dumps(result))
