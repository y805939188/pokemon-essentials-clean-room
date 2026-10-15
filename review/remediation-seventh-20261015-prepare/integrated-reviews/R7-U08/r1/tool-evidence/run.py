import sys,json,subprocess,datetime,hashlib,os
from pathlib import Path
base=Path(os.environ.get('R7_U08_TOOL_LOG_DIR',str(Path(__file__).parent)));base.mkdir(parents=True,exist_ok=True);name=sys.argv[1];cmd=sys.argv[2:]
start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE);pid=p.pid;out,err=p.communicate()
(base/(name+'.stdout')).write_bytes(out);(base/(name+'.stderr')).write_bytes(err)
row={'argv':cmd,'cwd':str(Path.cwd()),'tool_pid':pid,'recorder_pid':os.getpid(),'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode,'stdout':{'bytes':len(out),'sha256':hashlib.sha256(out).hexdigest()},'stderr':{'bytes':len(err),'sha256':hashlib.sha256(err).hexdigest()},'configuration_credit':False,'behavior_execution_credit':False}
(base/(name+'.json')).write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n');print(json.dumps(row,ensure_ascii=False));sys.stdout.buffer.write(out);sys.stderr.buffer.write(err);sys.exit(p.returncode)
