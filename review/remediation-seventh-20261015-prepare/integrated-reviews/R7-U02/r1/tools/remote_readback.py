import concurrent.futures,datetime,hashlib,json,os,subprocess,sys,urllib.parse,urllib.request
from pathlib import Path
commit,output,bare=sys.argv[1:4]
branch='codex/r7-ir-u02-20261015-r1'
prefix='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U02/r1/'
repository='https://github.com/y805939188/pokemon-essentials-clean-room.git'
commands=[]
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def run(argv):
 start=utc();p=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE);out,err=p.communicate()
 commands.append(dict(argv=argv,pid=p.pid,start_utc=start,end_utc=utc(),exit_code=p.returncode,stdout=out.decode(),stderr=err.decode()))
 assert p.returncode==0,commands[-1]
 return out
start=utc()
remote_before=run(['git','ls-remote',repository,'refs/heads/'+branch]).decode().split()[0]
assert remote_before==commit,(remote_before,commit)
assert not Path(bare).exists()
run(['git','init','--bare','--quiet',bare])
run(['git','-C',bare,'fetch','--quiet','--filter=blob:none','--depth=1',repository,'refs/heads/'+branch])
remote_commit=run(['git','-C',bare,'rev-parse','FETCH_HEAD']).decode().strip()
remote_tree=run(['git','-C',bare,'rev-parse','FETCH_HEAD^{tree}']).decode().strip()
local_tree=run(['git','rev-parse',commit+'^{tree}']).decode().strip()
assert remote_commit==commit and remote_tree==local_tree
remote_entries=run(['git','-C',bare,'ls-tree','-rz','FETCH_HEAD','--',prefix])
local_entries=run(['git','ls-tree','-rz',commit,'--',prefix])
assert remote_entries==local_entries
entries=[]
for chunk in remote_entries.split(b'\0'):
 if not chunk:continue
 meta,path=chunk.split(b'\t',1);mode,kind,blob=meta.decode().split();assert kind=='blob' and mode=='100644'
 entries.append((path.decode(),blob,mode))
def check(entry):
 path,blob,mode=entry
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(path,safe='/')
 at=utc()
 with urllib.request.urlopen(url,timeout=60) as response:
  status=response.status;data=response.read()
 assert status==200
 local=subprocess.check_output(['git','show',commit+':'+path])
 actual_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
 assert data==local and actual_blob==blob,path
 return dict(path=path,url=url,http_status=status,start_utc=at,end_utc=utc(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=actual_blob,mode=mode,complete_body_matches=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(check,entries))
remote_after=run(['git','ls-remote',repository,'refs/heads/'+branch]).decode().split()[0]
assert remote_before==remote_after
manifest=json.loads(subprocess.check_output(['git','show',commit+':'+prefix+'artifact-manifest.json']))
by_path={r['path']:r for r in rows}
for r in manifest['files']:
 actual=by_path[prefix+r['path']]
 for k in ['bytes','sha256','git_blob']:assert actual[k]==r[k]
assert len(rows)==len(manifest['files'])+1
result=dict(schema='r7.u02.complete-remote-readback.v1',commit=commit,tree=remote_tree,branch=branch,remote_before=remote_before,remote_after=remote_after,all_files=len(rows),total_bytes=sum(r['bytes'] for r in rows),all_HTTP_200=True,all_complete_bytes_SHA256_blob_mode_match=True,fresh_receive_repository=bare,start_utc=start,end_utc=utc(),pid=os.getpid(),commands=commands,files=rows,qualification='Transport verification only. No behavior execution, semantic PASS, ACCEPTED or CLOSED from these checks.')
Path(output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['commands','files']},ensure_ascii=False))
