"""Full immutable remote payload readback; transport evidence, no semantic credit."""
import pathlib,subprocess,json,hashlib,datetime,urllib.request,urllib.error,concurrent.futures,sys
ROOT=pathlib.Path(__file__).resolve().parents[5];BASE='4575e80d041ab0c74a42e2e36399d05791dbaa5b';BRANCH='codex/r8-u07-revision-20261017';PREFIX='review/remediation-eighth-20261016-prepare/candidates/R8-U07/'
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
commit=sys.argv[1];output=pathlib.Path(sys.argv[2]);assert len(commit)==40
ref_before=git('ls-remote','origin','refs/heads/'+BRANCH).decode().strip().split()[0];assert ref_before==commit
paths=git('diff','--name-only',BASE,commit).decode().splitlines();assert paths and all(p.startswith(PREFIX) for p in paths)
def get(path):
 b=git('show',commit+':'+path);mode,typ,bid=git('ls-tree',commit,'--',path).decode().split('\t')[0].split();assert typ=='blob' and mode=='100644';url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+path;attempts=[]
 for attempt in range(3):
  start=datetime.datetime.now(datetime.timezone.utc).isoformat()
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'Cache-Control':'no-cache','User-Agent':'R8-U07-fixed-commit-readback'}),timeout=45) as resp:
    actual=resp.read();status=resp.status
   attempts.append({'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'HTTP':status,'bytes':len(actual)})
   assert status==200 and actual==b
   return {'path':path,'mode':mode,'bytes':len(actual),'sha256':hashlib.sha256(actual).hexdigest(),'blob':bid,'url':url,'complete_response_equals_git_blob':True,'attempts':attempts}
  except Exception as ex:
   attempts.append({'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'error':type(ex).__name__+': '+str(ex)})
 return {'path':path,'FAILED':True,'attempts':attempts}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:rows=list(ex.map(get,paths))
ref_after=git('ls-remote','origin','refs/heads/'+BRANCH).decode().strip().split()[0]
result={'schema':'r8-u07-complete-fixed-commit-remote-readback.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':commit,'tree':git('rev-parse',commit+'^{tree}').decode().strip(),'branch':BRANCH,'base':BASE,'remote_ref_before':ref_before,'remote_ref_after':ref_after,'files':rows,'file_count':len(rows),'bytes':sum(x.get('bytes',0) for x in rows),'status':'VERIFIED' if ref_after==commit and all(x.get('complete_response_equals_git_blob') for x in rows) else 'FAILED','semantic_credit':'NONE; full transport/identity only'}
output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='files'}));sys.exit(0 if result['status']=='VERIFIED' else 1)
