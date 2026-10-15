"""Record public tool I/O only. Does not invoke models or execute restored code."""
import datetime,json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parent
label=sys.argv[1]; argv=sys.argv[2:]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.Popen(argv,cwd='/workspace/r7-u07-reviewer-r2',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p.communicate()
record={'schema':'r7.u07.r2.public-tool-io.v1','start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'context':{k:os.environ.get(k,'NOT_EXPOSED') for k in ['CODEX_THREAD_ID','CODEX_SESSION_ID']},'logger_pid':os.getpid(),'command_pid':p.pid,'argv':argv,'cwd':'/workspace/r7-u07-reviewer-r2','stdout':out.decode('utf-8','replace'),'stderr':err.decode('utf-8','replace'),'exit_code':p.returncode,'qualification':'TOOL_VALIDATION; no model configuration or behavior execution certification'}
with (root/'logs'/(label+'.json')).open('x') as f: json.dump(record,f,ensure_ascii=False,indent=2);f.write('\n')
sys.stdout.buffer.write(out);sys.stderr.buffer.write(err)
raise SystemExit(p.returncode)
