"""Full exact-byte HTTPS readback for every reviewer file in a fixed pushed commit."""
import concurrent.futures,datetime,hashlib,json,subprocess,sys,time,urllib.error,urllib.parse,urllib.request
from pathlib import Path
root=Path('/workspace/r7-u07-reviewer-r2');prefix='candidates/R7-U07/evidence/reviewer/r2/';branch='codex/r7-u07-reviewer-20261015-r2';base='e646432c644dec04d306842cc5a559a29c718fbc'
commit=sys.argv[1];output=Path(sys.argv[2]) if len(sys.argv)>2 else None
assert len(commit)==40 and all(c in '0123456789abcdef' for c in commit)
def git(*args):return subprocess.check_output(['git',*args],cwd=root)
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def ident(d):return {'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(d)}\0'.encode()+d).hexdigest()}
def remote():
 line=git('ls-remote','--heads','origin','refs/heads/'+branch).decode().strip();assert line.split()[0]==commit,line;return line
start=utc();head_before=remote();tree=git('rev-parse',commit+'^{tree}').decode().strip()
changed=[]
for record in git('diff','--name-status',base,commit).decode().splitlines():
 s,p=record.split('\t');assert s=='A' and p.startswith(prefix),(s,p);changed.append(p)
rows=[]
for record in git('ls-tree','-r','-z',commit,prefix).split(b'\0'):
 if not record:continue
 meta,p=record.split(b'\t');mode,kind,blob=meta.decode().split();p=p.decode();assert kind=='blob' and mode=='100644'
 d=git('show',commit+':'+p);assert ident(d)['git_blob']==blob;rows.append({'path':p,'git_mode':mode,**ident(d)})
assert {r['path'] for r in rows}==set(changed)
def read(row):
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(row['path']);attempts=[]
 for n in range(1,4):
  stamp=utc()
  try:
   with urllib.request.urlopen(url,timeout=45) as response:d=response.read(row['bytes']+1);status=response.status
   assert ident(d)=={k:row[k] for k in ['bytes','sha256','git_blob']},row['path']
   attempts.append({'attempt':n,'start_utc':stamp,'end_utc':utc(),'http_status':status,'complete_byte_match':True})
   return {**row,'url':url,'attempts':attempts}
  except (urllib.error.URLError,TimeoutError) as e:
   attempts.append({'attempt':n,'start_utc':stamp,'end_utc':utc(),'error':str(e)})
   if isinstance(e,urllib.error.HTTPError) and e.code not in [429,500,502,503,504]:raise
   if n==3:raise
   time.sleep(n)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:received=list(pool.map(read,rows))
head_after=remote()
result={'schema':'r7.u07.r2.actual-complete-remote-readback.v1','start_utc':start,'end_utc':utc(),'commit':commit,'tree':tree,'branch':branch,'remote_head_before':head_before,'remote_head_after':head_after,'files':received,'files_count':len(received),'bytes_count':sum(r['bytes'] for r in received),'all_complete_byte_matches':True,'complete_diff_against_B_only_new_reviewer_r2_files':True,'qualification':'TOOL_VALIDATION: complete remote transport and exact fixed commit/tree/file identities only; no behavior/integration/acceptance/closure elevation'}
if output:
 assert output.resolve().is_relative_to((root/prefix).resolve())
 with output.open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
