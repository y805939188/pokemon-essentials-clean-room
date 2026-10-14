import sys, subprocess, json, hashlib, datetime, urllib.request, urllib.parse
from pathlib import Path
root=Path(__file__).resolve().parent
commit,path,start,end=sys.argv[1:5]
start,end=int(start),int(end)
t0=datetime.datetime.now(datetime.timezone.utc).isoformat()
argv=['git','show',commit+':'+path]
r=subprocess.run(argv,capture_output=True)
transport='LOCAL_GIT_OBJECT'
if r.returncode:
 transport='RAW_HTTPS_FIXED_COMMIT'
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path)
 with urllib.request.urlopen(url,timeout=45) as f:data=f.read()
else:data=r.stdout
lines=data.decode().splitlines()
end=len(lines) if end==0 else end
assert 1<=start<=end<=len(lines),(start,end,len(lines))
blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
out='\n'.join(f'{i+1}: {lines[i]}' for i in range(start-1,end))+'\n'
rec={'commit':commit,'path':path,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':blob,'total_lines':len(lines),'range':[start,end],'argv':argv,'cwd':str(Path.cwd()),'start_utc':t0,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':r.returncode,'stderr':r.stderr.decode(),'rendered_sha256':hashlib.sha256(out.encode()).hexdigest(),'kind':'SEMANTIC_READ_OUTPUT_RANGE_ONLY','transport':transport,'local_attempt_exit':r.returncode}
with root.joinpath('read-segments.jsonl').open('a') as f: f.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(json.dumps({k:rec[k] for k in ['commit','path','total_lines','range','git_blob']},ensure_ascii=False))
print(out,end='')
