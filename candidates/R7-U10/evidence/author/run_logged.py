import sys,subprocess,json,datetime,os
from pathlib import Path
label=sys.argv[1];argv=sys.argv[2:]
root=Path('/workspace/pokemon-essentials-clean-room')
logs=root/'candidates/R7-U10/evidence/author/logs'
assert label.replace('-','').isalnum()
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.Popen(argv,cwd=root,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p.communicate()
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
for suffix,data in [('stdout',out),('stderr',err)]:
 (logs/(label+'.'+suffix)).write_bytes(data)
record={'label':label,'argv':argv,'cwd':str(root),'start_utc':start,'end_utc':stamp,'tool_subprocess_pid':p.pid,'logger_pid':os.getpid(),'exit_code':p.returncode,'stdout':label+'.stdout','stderr':label+'.stderr','qualification':'Actual public command I/O only; no model stream; tool success is not semantic or host acceptance.'}
(logs/(label+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
sys.stdout.buffer.write(out);sys.stderr.buffer.write(err)
raise SystemExit(p.returncode)
