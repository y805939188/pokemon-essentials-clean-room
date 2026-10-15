import concurrent.futures,datetime,hashlib,json,os,pathlib,subprocess,sys,time,urllib.parse,urllib.request
C=pathlib.Path('/workspace/r7-ir-R7-U01/checkout');P='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U01/r1/';BR='codex/r7-ir-u01-20261015-r1';B='e646432c644dec04d306842cc5a559a29c718fbc';commit=sys.argv[1];receipt=pathlib.Path(sys.argv[2]);commands=[]
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def run(a):
 start=now();p=subprocess.Popen(a,cwd=C,stdout=subprocess.PIPE,stderr=subprocess.PIPE);out,err=p.communicate();commands.append({'argv':a,'cwd':str(C),'tool_pid':p.pid,'start_utc':start,'end_utc':now(),'exit_code':p.returncode,'stdout':out.decode(),'stderr':err.decode()});assert p.returncode==0,(a,p.returncode,err.decode());return out
def git(*a):return run(['git',*a])
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
start=now();assert len(commit)==40 and git('rev-parse',commit).decode().strip()==commit
before=git('ls-remote','--heads','origin','refs/heads/'+BR).decode().strip();assert before.split()[0]==commit
git('fetch','--no-tags','origin','refs/heads/'+BR);assert git('rev-parse','FETCH_HEAD').decode().strip()==commit
tree=git('rev-parse',commit+'^{tree}').decode().strip()
changes=git('diff','--name-status',B,commit).decode().splitlines();assert changes and all(x.startswith('A\t'+P) for x in changes)
entries=[]
for line in git('ls-tree','-r',commit,'--',P).decode().splitlines():
 mode,kind,rest=line.split(' ',2);blob,path=rest.split('\t',1);assert kind=='blob' and mode=='100644';entries.append((mode,blob,path))
assert {x.split('\t')[1] for x in changes}=={x[2] for x in entries}
def fetch(entry):
 mode,blob,path=entry;expected=subprocess.check_output(['git','show',commit+':'+path],cwd=C);wanted=identity(expected);assert wanted['git_blob']==blob
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path,safe='/');attempts=[]
 for n in range(1,4):
  t=now()
  try:
   with urllib.request.urlopen(url,timeout=60) as response:b=response.read();status=response.status
   attempts.append({'attempt':n,'start_utc':t,'end_utc':now(),'http_status':status,**identity(b),'complete_byte_match':b==expected})
   assert status==200 and b==expected,(path,'response differs');break
  except Exception as e:
   attempts.append({'attempt':n,'start_utc':t,'end_utc':now(),'error':str(e)})
   if n==3:raise
   time.sleep(2*n)
 return {'path':path,'git_mode':mode,**wanted,'url':url,'attempts':attempts}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:files=list(pool.map(fetch,entries))
after=git('ls-remote','--heads','origin','refs/heads/'+BR).decode().strip();assert after==before
result={'schema':'r7.u01.complete-remote-readback.v1','start_utc':start,'end_utc':now(),'tool_pid':os.getpid(),'branch':BR,'base':B,'result_commit':commit,'result_tree':tree,'remote_tip_before':before,'remote_tip_after':after,'files':files,'counts':{'files':len(files),'bytes':sum(x['bytes'] for x in files)},'commands':commands,'status':'COMPLETE_REMOTE_READBACK_EXACT','qualification':'All immutable remote response bytes compared to actual commit blobs; modes/complete path universe bound by remote fetched commit/tree. Transport only, no semantic/runtime/config certification. Receipt stored externally to the commit it verifies; no self-reference.'}
receipt.parent.mkdir(parents=True,exist_ok=True);receipt.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','branch','result_commit','result_tree','counts']},ensure_ascii=False,indent=2))
