import datetime,json,os,subprocess,sys
from pathlib import Path
out=Path(sys.argv[1]);argv=sys.argv[2:]
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
r={'schema':'r7.u07.reviewer-public-command-io.v1','start_utc':utc(),'cwd':os.getcwd(),'argv':argv,'recorder_pid':os.getpid(),'actual_context':os.environ.get('CODEX_THREAD_ID','NOT_EXPOSED'),'qualification':'Actual public tool I/O; no configuration or behavior attestation.'}
p=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True);r['child_pid']=p.pid
r['stdout'],r['stderr']=p.communicate();r['exit_code']=p.returncode;r['end_utc']=utc()
out.parent.mkdir(parents=True,exist_ok=True)
with out.open('x') as f:json.dump(r,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps(r,ensure_ascii=False,indent=2));sys.exit(p.returncode)
