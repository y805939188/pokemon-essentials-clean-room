"""Read fixed public source bodies into memory for cloud-transfer identity evidence only."""
from pathlib import Path
import json,csv,hashlib,urllib.request,urllib.parse,concurrent.futures,datetime
OUT=Path(__file__).resolve().parent
ref={x['path']:x for x in csv.DictReader((OUT/'reference-file-inventory.tsv').open(),delimiter='\t')}
commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
paths=sorted({e['path'] for x in json.loads((OUT/'findings.json').read_text()) for e in x['source_evidence']})
def get(p):
 url='https://raw.githubusercontent.com/Maruno17/pokemon-essentials/'+commit+'/'+urllib.parse.quote(p,safe='/')
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Codex-clean-room-review-readback'})
  with urllib.request.urlopen(req,timeout=25) as r:b=r.read()
  sha=hashlib.sha256(b).hexdigest();blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
  return {'path':p,'url':url,'bytes':len(b),'sha256':sha,'git_blob':blob,'match':str(len(b))==ref[p]['bytes'] and sha==ref[p]['sha256'] and blob==ref[p]['git_blob'],'body_fetched':True}
 except Exception as e:return {'path':p,'url':url,'match':False,'body_fetched':False,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(get,paths))
result={'kind':'FIXED_REFERENCE_CRITICAL_SOURCE_CLOUD_READBACK','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repo':'Maruno17/pokemon-essentials','commit':commit,'tree':'7589c800b61ba13a13040ed0d686979b80a84fd0','scope':'All unique source_evidence paths of current25 canonical retained IDs; raw bytes fetched only, not evaluated/executed/rendered. Remaining432 bodies not claimed.','path_count':len(records),'matched':sum(x['match'] for x in records),'records':records,'behavior_execution':0}
(OUT/'reference-critical-source-readback.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'paths':len(records),'matched':result['matched'],'errors':[x for x in records if not x['match']]},ensure_ascii=False))
