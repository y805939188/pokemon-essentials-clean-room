"""Capture actual helper tool process and raw streams in this task directory."""
from pathlib import Path
import subprocess,sys,json,datetime
root=Path(__file__).resolve().parent
name=sys.argv[1];args=sys.argv[2:]
assert name.replace('-','').replace('_','').isalnum()
assert not (root/(name+'.json')).exists()
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.run(args,cwd=root,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
end=datetime.datetime.now(datetime.timezone.utc).isoformat()
(root/(name+'.stdout')).write_bytes(p.stdout)
(root/(name+'.stderr')).write_bytes(p.stderr)
(root/(name+'.json')).write_text(json.dumps({'argv':args,'cwd':str(root),'start_utc':start,'end_utc':end,'exit':p.returncode,'phase':'TOOL_VALIDATION','business':'NOT_EXECUTED'},indent=2)+'\n')
sys.stdout.buffer.write(p.stdout);sys.stderr.buffer.write(p.stderr);sys.exit(p.returncode)
