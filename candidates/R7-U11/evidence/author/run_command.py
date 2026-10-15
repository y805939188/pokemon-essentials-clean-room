"""Capture public-safe command I/O; no shell interpolation or model transcript."""
import datetime,json,os,subprocess,sys
from pathlib import Path
name,*argv=sys.argv[1:]
assert name.replace('-','').isalnum() and argv
root=Path(__file__).resolve().parent/'logs'; root.mkdir(exist_ok=True)
assert not (root/(name+'.json')).exists(), 'Never overwrite an earlier command receipt'
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
start=utc(); p=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p.communicate()
(root/(name+'.stdout')).write_bytes(out); (root/(name+'.stderr')).write_bytes(err)
r={'schema':'r7.u11.public-command.v1','name':name,'argv':argv,'cwd':os.getcwd(),'wrapper_pid':os.getpid(),'child_pid':p.pid,'start_utc':start,'end_utc':utc(),'exit_code':p.returncode,'stdout':name+'.stdout','stderr':name+'.stderr','qualification':'Actual process I/O only; no model configuration or behavioral acceptance inferred.'}
(root/(name+'.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
sys.stdout.buffer.write(out); sys.stderr.buffer.write(err); sys.exit(p.returncode)
