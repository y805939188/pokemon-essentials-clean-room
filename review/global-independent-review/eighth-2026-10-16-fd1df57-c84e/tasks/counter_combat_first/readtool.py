import sys, pathlib, subprocess, datetime, hashlib, json
ROOT=pathlib.Path(__file__).resolve().parent
UTC=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
start=UTC()
mode=sys.argv[1]
entry={'started_utc':start,'argv':sys.argv,'kind':'TOOL_VALIDATION' if mode=='cmd' else 'SOURCE_STATIC_READ'}
if mode=='cmd':
    p=subprocess.run(sys.argv[2:],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out=p.stdout.decode('utf-8',errors='replace');err=p.stderr.decode('utf-8',errors='replace')
    entry.update(stdout=out,stderr=err,exit_code=p.returncode)
else:
    repo,commit,path=sys.argv[2:5]
    args=['git','-C',repo,'show',commit+':'+path] if commit!='WORKTREE' else ['cat',str(pathlib.Path(repo)/path)]
    p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    data=p.stdout;lines=data.decode('utf-8').splitlines()
    a=int(sys.argv[5]) if len(sys.argv)>5 else 1
    b=int(sys.argv[6]) if len(sys.argv)>6 else len(lines)
    out='\n'.join(f'{i+1:5d} {line}' for i,line in enumerate(lines) if a<=i+1<=b)+'\n'
    err=p.stderr.decode('utf-8',errors='replace')
    blob=subprocess.run(['git','-C',repo,'rev-parse',commit+':'+path],capture_output=True,text=True).stdout.strip() if commit!='WORKTREE' else None
    entry.update(repo=repo,commit=commit,path=path,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),blob=blob,total_lines=len(lines),range=[a,min(b,len(lines))],stdout=out,stderr=err,exit_code=p.returncode)
entry['ended_utc']=UTC()
io=ROOT/'io';io.mkdir(exist_ok=True)
idx=len(list(io.glob('*.json')))+1
dest=io/f'{idx:04d}.json'
dest.write_text(json.dumps(entry,ensure_ascii=False,indent=2)+'\n')
print(f'IO_RECORD={dest.relative_to(ROOT)}')
print(out,end='')
if err: print('STDERR: '+err)
sys.exit(p.returncode)
