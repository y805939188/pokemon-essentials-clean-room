#!/usr/bin/env python3
"""Capture document-workflow commands; never executes reference Ruby or a game model."""
import sys,json,subprocess,datetime,pathlib,hashlib
base=pathlib.Path(__file__).resolve().parent
name=sys.argv[1];argv=sys.argv[2:];assert name and argv
out=base/'io';out.mkdir(exist_ok=True)
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
end=datetime.datetime.now(datetime.timezone.utc).isoformat()
(out/(name+'.stdout')).write_bytes(r.stdout);(out/(name+'.stderr')).write_bytes(r.stderr)
event={'id':name,'argv':argv,'start_utc':start,'end_utc':end,'exit':r.returncode,'stdout':'io/'+name+'.stdout','stdout_bytes':len(r.stdout),'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr':'io/'+name+'.stderr','stderr_bytes':len(r.stderr),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest(),'kind':'TOOL_VALIDATION_OR_TRANSPORT','business_execution':'NOT_EXECUTED'}
with (base/'commands.jsonl').open('a') as f:f.write(json.dumps(event,ensure_ascii=False)+'\n')
sys.stdout.buffer.write(r.stdout);sys.stderr.buffer.write(r.stderr);sys.exit(r.returncode)
