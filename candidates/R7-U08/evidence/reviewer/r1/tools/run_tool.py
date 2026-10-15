"""Record real bounded reviewer tool I/O. Never execute restored author/reference programs."""
import datetime,hashlib,json,os,pathlib,subprocess,sys
root=pathlib.Path(__file__).resolve().parents[1]
name=sys.argv[1];argv=sys.argv[2:]
assert name.replace('-','').replace('_','').isalnum()
out=root/'tool-evidence'/name
assert not out.with_suffix('.json').exists()
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
start=now(); p=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
a,b=p.communicate()
out.with_suffix('.stdout').write_bytes(a);out.with_suffix('.stderr').write_bytes(b)
d={'argv':argv,'cwd':os.getcwd(),'start_utc':start,'end_utc':now(),'pid':p.pid,'exit_code':p.returncode,'stdout':{'bytes':len(a),'sha256':hashlib.sha256(a).hexdigest()},'stderr':{'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()},'qualification':'Actual tool execution, not behavior/reference/model certification'}
out.with_suffix('.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
sys.stdout.buffer.write(a);sys.stderr.buffer.write(b);sys.exit(p.returncode)
