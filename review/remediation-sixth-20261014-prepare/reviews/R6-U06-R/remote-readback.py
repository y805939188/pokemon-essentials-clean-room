import sys,json,hashlib,datetime,subprocess,urllib.request,urllib.parse,concurrent.futures
from pathlib import Path

ROOT=Path(__file__).resolve().parent
commit,base,branch,prefix,label=sys.argv[1:]
assert len(commit)==40 and label.replace('-','').isalnum()
out=ROOT/(label+'.json'); assert not out.exists()
url='https://github.com/y805939188/pokemon-essentials-clean-room.git'
cache=ROOT/('.remote-'+label+'.git')
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def git(*args):return subprocess.check_output(['git',*args])
start=now(); commands=[]
for argv in [['git','init','--bare',str(cache)],['git','-C',str(cache),'fetch','--depth=1','--filter=blob:none','--no-tags',url,commit]]:
    t=now();p=subprocess.run(argv,capture_output=True)
    commands.append(dict(argv=argv,cwd=str(Path.cwd()),start_utc=t,end_utc=now(),exit_code=p.returncode,stdout=p.stdout.decode(errors='replace'),stderr=p.stderr.decode(errors='replace')))
    if p.returncode: out.write_text(json.dumps(dict(result='FAIL',commands=commands),indent=2)+'\n');sys.exit(1)
tree=git('rev-parse',commit+'^{tree}').decode().strip()
remote_tree=git('-C',str(cache),'rev-parse',commit+'^{tree}').decode().strip()
directory_tree=git('rev-parse',commit+':'+prefix.rstrip('/')).decode().strip()
paths=git('diff','--name-only',base,commit).decode().splitlines()
assert paths and all(p.startswith(prefix) for p in paths)
def read(path):
    expected=git('show',commit+':'+path)
    entry=git('ls-tree',commit,'--',path).decode().strip()
    remote_entry=git('-C',str(cache),'ls-tree',commit,'--',path).decode().strip()
    mode,typ,tail=entry.split(' ',2);blob=tail.split('\t')[0]
    raw='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path,safe='/')
    attempts=[];data=None
    for number in range(1,4):
        t=now()
        try:
            with urllib.request.urlopen(raw,timeout=25) as response:
                data=response.read();status=response.status
            attempts.append(dict(attempt=number,start_utc=t,end_utc=now(),status=status,bytes=len(data)))
            break
        except Exception as ex:attempts.append(dict(attempt=number,start_utc=t,end_utc=now(),error=repr(ex)))
    actual_blob=None if data is None else hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    return dict(path=path,mode=mode,type=typ,bytes=len(expected),sha256=hashlib.sha256(expected).hexdigest(),git_blob=blob,
                remote_bytes=None if data is None else len(data),remote_sha256=None if data is None else hashlib.sha256(data).hexdigest(),remote_git_blob=actual_blob,
                remote_tree_entry=remote_entry,exact=data==expected and actual_blob==blob and entry==remote_entry,attempts=attempts)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(read,paths))
remote=git('ls-remote','--heads',url,branch).decode().strip()
result=dict(evidence_level='TOOL_VALIDATION_REMOTE_FULL_BYTES',commit=commit,base=base,tree=tree,remote_tree=remote_tree,directory_tree=directory_tree,
            branch=branch,ls_remote=remote,branch_exact=bool(remote) and remote.split()[0]==commit,tree_exact=tree==remote_tree,
            prefix=prefix,path_count=len(rows),byte_count=sum(x['bytes'] for x in rows),all_payloads_exact=all(x['exact'] for x in rows),undeclared_paths=[],
            cwd=str(Path.cwd()),argv=sys.argv,start_utc=start,end_utc=now(),commands=commands,rows=rows,
            semantic_limit='Full remote byte/hash/object binding only; does not execute source, vectors, model, host, Demo or save. Final report publication identity externally bound, no recursive self-hash.')
result['result']='PASS' if result['branch_exact'] and result['tree_exact'] and result['all_payloads_exact'] else 'FAIL'
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['commands','rows']},ensure_ascii=False));sys.exit(0 if result['result']=='PASS' else 1)
