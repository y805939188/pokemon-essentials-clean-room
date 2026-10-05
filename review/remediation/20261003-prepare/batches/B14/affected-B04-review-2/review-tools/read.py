# Fresh static text read/range logger; never executes reference behavior.
import sys,json,hashlib,subprocess,datetime
kind,path,ran=sys.argv[1:4];c=sys.argv[4] if len(sys.argv)>4 else 'af39efbf32549be964cb083bd49bed6d1d5c0d2a'
root='/tmp/b14-b04-round2-reference' if kind=='reference' else '/workspace/b14-affected-b04-review-2'
if kind=='reference':c='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
b=subprocess.check_output(['git','-C',root,'show',c+':'+path]);lines=b.decode().splitlines(keepends=True);lo,hi=map(int,ran.split(':'));picked=''.join(lines[lo-1:hi]);blob=subprocess.check_output(['git','-C',root,'rev-parse',c+':'+path]).decode().strip()
event=dict(repository=kind,commit=c,path=path,git_blob=blob,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),lines=[lo,min(hi,len(lines))],range_sha256=hashlib.sha256(picked.encode()).hexdigest(),method='STATIC_TEXT_READ_NO_EXECUTION',UTC=datetime.datetime.now(datetime.timezone.utc).isoformat())
with open('/tmp/b14-b04-round2-audit/reading-events.jsonl','a') as f:f.write(json.dumps(event,ensure_ascii=False)+'\n')
print(path+' @ '+c+' '+ran)
for i,l in enumerate(lines[lo-1:hi],lo):print(str(i)+'\t'+l,end='')
