import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import urllib.request

base=pathlib.Path(__file__).resolve().parent
target=base/'received'
target.mkdir(exist_ok=True)
prefix='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/receive_external_h_early_qualifications/receivers/fanout-v1/'
bindings={
 'r5_u01_u02':'f62c26cd86e38e45429b1a0b9fd637b8c10fff59',
 'r5_u03_u06_core':'93b0c4e457f10ffd4df3bf97d543254c232bfc68',
 'r5_tail_shared_policy':'76471376a7b0a42cfcf030a404fc91afb0a94835'}

def recover(item):
    name,commit=item
    path=prefix+name+'/reception-ledger.json'
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+path
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    with urllib.request.urlopen(url,timeout=50) as response:
        data=response.read()
        status=response.status
    json.loads(data)
    dest=target/(name+'.json')
    if dest.exists():
        raise RuntimeError('Refusing to replace existing recovery')
    dest.write_bytes(data)
    return {'name':name,'commit':commit,'path':path,'url':url,'http_status':status,
      'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
      'computed_git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
      'started_utc':started,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'semantic_credit':'NONE_FROM_RECOVERY; selected complete fact objects must be actually read'}

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results=list(pool.map(recover,bindings.items()))
(target/'recovery.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False,indent=2))
