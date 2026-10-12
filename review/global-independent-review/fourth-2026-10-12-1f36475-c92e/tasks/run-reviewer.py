import pathlib,subprocess,json,datetime,sys,threading
module=sys.argv[1]
w=pathlib.Path('/Users/dingshinn/.codex/worktrees/review-fourth-1f36475/pokemon-framework-reference')
o=w/'review/global-independent-review/fourth-2026-10-12-1f36475-c92e'
logs=pathlib.Path('/tmp/gr4-c92e-cli');logs.mkdir(exist_ok=True)
cmd=['codex','exec','--json','-m','gpt-6-astra','-c','model_reasoning_effort="ultra"','-c','service_tier="default"','-C',str(w),'-o',str(o/'modules'/module/'last-message.md'),'-']
receipt={'schema_version':'1.0','module':module,'parent_thread_id':'01a12fc2-e8c0-7e43-a721-ccfe659d75c8','command':cmd,'requested':{'model':'gpt-6-astra','reasoning_effort':'ultra','service_tier':'default','fast':False},'actual_echo':'UNVERIFIED','started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'log':str(logs/(module+'.jsonl')),'stderr_log':str(logs/(module+'.stderr.log')),'status':'STARTING','thread_id':None}
def save():
 (o/'tasks'/(module+'-launch.json')).write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
with open(logs/(module+'.stderr.log'),'w') as err,open(logs/(module+'.jsonl'),'w') as log:
 p=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err,text=True,cwd=w)
 receipt['pid']=p.pid;receipt['status']='REQUEST_SUBMITTED';save();print(json.dumps(receipt,ensure_ascii=False),flush=True)
 p.stdin.write((o/'tasks'/(module+'-prompt.txt')).read_text());p.stdin.close()
 for line in p.stdout:
  log.write(line);log.flush()
  try:x=json.loads(line)
  except ValueError:continue
  if x.get('type')=='thread.started':receipt['thread_id']=x.get('thread_id');save();print(line.strip(),flush=True)
  if x.get('type') in ['error','turn.failed','turn.completed','turn.started']:
   if x['type']=='turn.started':receipt['status']='RUNNING_REQUEST_ACCEPTED';save()
   if x['type'] in ['error','turn.failed']:receipt.setdefault('errors',[]).append(x);save()
   print(line.strip(),flush=True)
 receipt['exit_code']=p.wait();receipt['finished_at']=datetime.datetime.now(datetime.timezone.utc).isoformat();receipt['status']='PROCESS_COMPLETED' if p.returncode==0 else 'PROCESS_FAILED';save()
 print(json.dumps({'module':module,'exit_code':p.returncode,'thread_id':receipt['thread_id'],'stderr':(logs/(module+'.stderr.log')).read_text()[-6000:]},ensure_ascii=False),flush=True)
