"""Record the actual public audit/publish subprocess I/O; no reference execution."""
from pathlib import Path
import datetime,json,subprocess,sys
output=Path(sys.argv[1]);argv=sys.argv[2:]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p.communicate()
row={'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cwd':str(Path.cwd()),'argv':argv,'command_pid':p.pid,'exit_code':p.returncode,'stdout':out.decode(),'stderr':err.decode()}
output.write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
print(out.decode(),end='');print(err.decode(),end='',file=sys.stderr)
sys.exit(p.returncode)
