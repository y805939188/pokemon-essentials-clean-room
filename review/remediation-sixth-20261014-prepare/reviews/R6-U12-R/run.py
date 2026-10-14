import sys,subprocess,json,datetime
from pathlib import Path
root=Path(__file__).resolve().parent
name=sys.argv[1];argv=sys.argv[2:]
t0=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=subprocess.run(argv,capture_output=True)
root.joinpath(name+'.stdout.txt').write_bytes(r.stdout)
root.joinpath(name+'.stderr.txt').write_bytes(r.stderr)
rec={'argv':argv,'cwd':str(Path.cwd()),'start_utc':t0,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':r.returncode,'stdout':name+'.stdout.txt','stderr':name+'.stderr.txt','kind':'PROCESS_CAPTURE'}
root.joinpath(name+'.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(rec,ensure_ascii=False));print(r.stdout.decode(),end='');print(r.stderr.decode(),end='',file=sys.stderr)
sys.exit(r.returncode)
