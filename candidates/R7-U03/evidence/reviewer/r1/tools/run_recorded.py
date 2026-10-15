"""Record reviewer's actual public-safe command I/O; never execute restored programs."""
import subprocess,sys,json,os,datetime,pathlib
root=pathlib.Path(__file__).resolve().parents[1]/'commands'
root.mkdir(exist_ok=True)
name=sys.argv[1]; command=sys.argv[2:]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
a,b=p.communicate()
(root/(name+'.stdout')).write_bytes(a);(root/(name+'.stderr')).write_bytes(b)
row=dict(command=command,cwd=os.getcwd(),start_utc=start,end_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),wrapper_pid=os.getpid(),process_pid=p.pid,exit_code=p.returncode,qualification='Actual tool process only; not model/configuration or behavior certification.')
(root/(name+'.json')).write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
sys.stdout.buffer.write(a);sys.stderr.buffer.write(b);sys.exit(p.returncode)
