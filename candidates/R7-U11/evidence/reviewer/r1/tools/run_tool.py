"""Record real public command I/O; never execute restored author/reference programs."""
import datetime,hashlib,json,os,pathlib,subprocess,sys
root=pathlib.Path(__file__).resolve().parents[1]
name=sys.argv[1];args=sys.argv[2:];start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd='/workspace/r7-u11-reviewer-checkout');out,err=p.communicate()
for suffix,data in [('stdout',out),('stderr',err)]:
 with (root/'logs'/f'{name}.{suffix}').open('xb') as f:f.write(data)
row={'args':args,'cwd':'/workspace/r7-u11-reviewer-checkout','start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'wrapper_pid':os.getpid(),'subprocess_pid':p.pid,'exit_code':p.returncode,'stdout':{'file':f'logs/{name}.stdout','bytes':len(out),'sha256':hashlib.sha256(out).hexdigest()},'stderr':{'file':f'logs/{name}.stderr','bytes':len(err),'sha256':hashlib.sha256(err).hexdigest()},'qualification':'Actual subprocess I/O. PID and exit status are not model configuration or semantic acceptance.'}
with (root/'logs'/f'{name}.json').open('x') as f:json.dump(row,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps(row,ensure_ascii=False));sys.stdout.write(out.decode(errors='replace'));sys.stderr.write(err.decode(errors='replace'));sys.exit(p.returncode)
