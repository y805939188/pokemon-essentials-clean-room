import datetime,json,os,pathlib,subprocess,sys
root=pathlib.Path('/workspace/r7-ir-R7-U06')
name=sys.argv[1];argv=sys.argv[2:]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.Popen(argv,cwd=root/'result',stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
out,err=p.communicate()
j={'argv':argv,'cwd':str(root/'result'),'wrapper_pid':os.getpid(),'tool_pid':p.pid,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'stdout':out,'stderr':err,'exit_code':p.returncode,'qualification':'Tool I/O only; no effective model or behavior certification.'}
(root/'bootstrap-evidence'/f'{name}.json').write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')
print(out,end='');print(err,end='',file=sys.stderr);sys.exit(p.returncode)
