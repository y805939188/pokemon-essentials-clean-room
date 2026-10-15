import sys,subprocess,json,os,datetime,hashlib
from pathlib import Path
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
root=Path(__file__).resolve().parents[1]
name=sys.argv[1]; cmd=sys.argv[2:]
start=utc(); p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE); out,err=p.communicate()
for suffix,data in [('stdout',out),('stderr',err)]: (root/'logs'/(name+'.'+suffix)).write_bytes(data)
row={'command':cmd,'cwd':os.getcwd(),'pid':p.pid,'audit_pid':os.getpid(),'start_utc':start,'end_utc':utc(),'exit_code':p.returncode,'stdout':{'path':'logs/'+name+'.stdout','bytes':len(out),'sha256':hashlib.sha256(out).hexdigest()},'stderr':{'path':'logs/'+name+'.stderr','bytes':len(err),'sha256':hashlib.sha256(err).hexdigest()},'tool_validation_only':True,'behavior_execution':'NOT_EXECUTED'}
(root/'logs'/(name+'.json')).write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
sys.stdout.buffer.write(out);sys.stderr.buffer.write(err);sys.exit(p.returncode)
