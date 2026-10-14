import subprocess,sys,json,hashlib,datetime,urllib.request
from pathlib import Path
root=Path(__file__).resolve().parent
commit,path,pointer=sys.argv[1:4]
t0=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=subprocess.run(['git','show',commit+':'+path],capture_output=True)
transport='LOCAL_GIT_OBJECT'
if r.returncode:
 transport='RAW_HTTPS_FIXED_COMMIT';url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
 with urllib.request.urlopen(url,timeout=45) as f:data=f.read();status=f.status
else:data=r.stdout;status=None
d=json.loads(data)
for k in pointer.strip('/').split('/') if pointer else []:d=d[int(k)] if isinstance(d,list) else d[k]
canonical=json.dumps(d,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
rec={'commit':commit,'path':path,'pointer':pointer,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),'transport':transport,'local_attempt_exit':r.returncode,'local_attempt_stderr':r.stderr.decode(),'http_status':status,'start_utc':t0,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'node_sha256':hashlib.sha256(canonical).hexdigest(),'semantic_credit':'SELECTED_COMPLETE_NODE_ONLY'}
with root.joinpath('read-nodes.jsonl').open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(json.dumps(rec,ensure_ascii=False));out=json.dumps(d,ensure_ascii=False,indent=2).splitlines();start,end=(map(int,sys.argv[4:6]) if len(sys.argv)>4 else (1,len(out)));assert 1<=start<=end<=len(out);print('\n'.join(str(i+1)+': '+out[i] for i in range(start-1,end)))
