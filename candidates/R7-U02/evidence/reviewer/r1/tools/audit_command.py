"""Capture explicit review tool commands; never record credentials or private model streams."""
import datetime,json,os,pathlib,subprocess,sys
root=pathlib.Path(__file__).resolve().parents[1]
name=sys.argv[1]; argv=sys.argv[2:]
assert name and '/' not in name
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
out,err=p.communicate()
(root/'logs'/f'{name}.stdout').write_bytes(out)
(root/'logs'/f'{name}.stderr').write_bytes(err)
r={'argv':argv,'cwd':os.getcwd(),'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'recorder_pid':os.getpid(),'child_pid':p.pid,'exit_code':p.returncode,'stdout_bytes':len(out),'stderr_bytes':len(err),'qualification':'Complete tool I/O; no model stream; exit status is not semantic acceptance.'}
(root/'logs'/f'{name}.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
sys.stdout.buffer.write(out);sys.stderr.buffer.write(err);sys.exit(p.returncode)
