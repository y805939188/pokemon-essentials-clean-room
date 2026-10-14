#!/usr/bin/env python3
"""Finite input reading and command receipts; no reference execution."""
from pathlib import Path
import sys, subprocess, hashlib, json, datetime
ROOT=Path(__file__).resolve().parents[5]
E=Path(__file__).resolve().parent
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
identity=lambda b:{'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
start=now()
args=sys.argv[1:]
if args[0]=='read':
 p=Path(args[1]); p=p if p.is_absolute() else ROOT/p
 b=p.read_bytes(); lines=b.decode('utf-8-sig').splitlines(keepends=True)
 lo=int(args[2]) if len(args)>2 else 1; hi=int(args[3]) if len(args)>3 else len(lines)
 assert 1<=lo<=hi<=len(lines),(lo,hi,len(lines))
 out=('FILE '+str(p)+' LINES '+str(lo)+'-'+str(hi)+'/'+str(len(lines))+'\n'+''.join(f'{n}: '+lines[n-1] for n in range(lo,hi+1))).encode()
 err=b''; code=0
 details={'input':str(p),'input_identity':identity(b),'range':[lo,hi],'total_lines':len(lines),'evidence_level':'SOURCE_STATIC_READING' if '/Maruno17/' in str(p) else 'SEMANTIC_READING','execution_of_reference':False}
else:
 try:
  r=subprocess.run(args,cwd=ROOT,capture_output=True);out=r.stdout;err=r.stderr;code=r.returncode
 except OSError as ex:
  out=b'';err=(type(ex).__name__+': '+str(ex)+'\n').encode();code=127
 details={'evidence_level':'TOOL_VALIDATION','execution_of_reference':False}
record={'argv':['python3',str(Path(__file__).resolve()),*args],'cwd':str(ROOT),'utc_start':start,'utc_end':now(),'exit_code':code,'stdout_identity':identity(out),'stderr_identity':identity(err),**details}
num=len((E/'commands.jsonl').read_text().splitlines())+1 if (E/'commands.jsonl').exists() else 1
logs=Path('/tmp/r6-u01-a-logs');logs.mkdir(exist_ok=True)
for kind,data in [('stdout',out),('stderr',err)]:
 p=logs/f'{num:04d}.{kind}';p.write_bytes(data);record[kind+'_path']=str(p)
with (E/'commands.jsonl').open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
sys.stdout.buffer.write(out);sys.stderr.buffer.write(err)
sys.exit(code)
