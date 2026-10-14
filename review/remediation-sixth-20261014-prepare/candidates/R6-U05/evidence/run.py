#!/usr/bin/env python3
import sys, subprocess, datetime, json
from pathlib import Path
root=Path(__file__).resolve().parent
label=sys.argv[1]
argv=sys.argv[2:]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.run(argv,capture_output=True,text=True)
record={'argv':argv,'cwd':str(Path.cwd()),'utc_start':start,'utc_end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
out=root/'commands'/ (label+'.json')
out.parent.mkdir(exist_ok=True)
if out.exists(): raise SystemExit('Do not overwrite prior attempts')
out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(p.stdout,end=''); print(p.stderr,end='',file=sys.stderr)
raise SystemExit(p.returncode)
