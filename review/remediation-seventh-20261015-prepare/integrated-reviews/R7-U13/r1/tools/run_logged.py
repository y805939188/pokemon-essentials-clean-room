"""Run explicit ordinary tools; preserve their PID, UTC and exact public I/O."""
from pathlib import Path
import datetime, hashlib, json, os, subprocess, sys
ROOT=Path(__file__).resolve().parent

def identity(data):
 return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())
def utc(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def run(label, argv, cwd=None):
 start=utc()
 p=subprocess.Popen(argv,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 out,err=p.communicate()
 (ROOT/(label+'.stdout')).write_bytes(out)
 (ROOT/(label+'.stderr')).write_bytes(err)
 row=dict(label=label,argv=argv,cwd=str(cwd or Path.cwd()),pid=p.pid,start_utc=start,end_utc=utc(),exit_code=p.returncode,stdout=identity(out),stderr=identity(err),model_configuration_credit=False,behavior_execution_credit=False)
 with (ROOT/'commands.jsonl').open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 sys.stdout.buffer.write(out)
 sys.stderr.buffer.write(err)
 return p.returncode
if __name__=='__main__':sys.exit(run(sys.argv[1],sys.argv[2:]))
