"""Explicit ordinary publication of this batch only, then full immutable remote-file readback.
Publication receipts live outside the candidate commit to avoid a self-referential commit/hash.
"""
from pathlib import Path
import concurrent.futures,datetime,hashlib,json,os,subprocess,urllib.error,urllib.parse,urllib.request,time
B='e646432c644dec04d306842cc5a559a29c718fbc'; BRANCH='codex/r7-u11-author-20261015-wave1'; PREFIX='candidates/R7-U11/'
OUT=Path('/workspace/r7-bootstrap/R7-U11-author/final-publication-receipt.json')
assert not OUT.exists(),'Protect prior publication receipt'
r={'schema':'r7.u11.publication-readback.v1','branch':BRANCH,'base_commit':B,'start_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commands':[],'remote_files':[],'status':'STARTED','private_model_streams_published':False}
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save():OUT.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
def run(argv):
 start=utc();p=subprocess.Popen(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE);a,b=p.communicate()
 row={'argv':argv,'cwd':os.getcwd(),'pid':p.pid,'start_utc':start,'end_utc':utc(),'exit_code':p.returncode,'stdout':a.decode(),'stderr':b.decode()};r['commands'].append(row);save()
 print(json.dumps(row,ensure_ascii=False),flush=True)
 if p.returncode:raise RuntimeError('Command failed; original I/O preserved')
 return a.decode().strip()
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_content_id':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
try:
 assert run(['git','branch','--show-current'])==BRANCH
 assert run(['git','rev-parse','HEAD'])==B
 assert run(['git','diff',B,'--name-only'])==''
 assert run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH])==''
 untracked=run(['git','ls-files','--others','--exclude-standard']).splitlines();assert untracked and all(p.startswith(PREFIX) for p in untracked)
 run(['git','add','--','candidates/R7-U11'])
 paths=run(['git','diff','--cached','--name-only']).splitlines();assert paths==sorted(untracked) and all(p.startswith(PREFIX) for p in paths)
 run(['git','diff','--cached','--check'])
 run(['git','commit','-m','Prepare isolated R7-U11 loader classification and text-tool request candidates'])
 commit=run(['git','rev-parse','HEAD']);tree=run(['git','rev-parse','HEAD^{tree}']);r['commit']=commit;r['tree']=tree
 assert run(['git','rev-parse','HEAD^'])==B
 changed=run(['git','diff',B,commit,'--name-only']).splitlines();assert changed==paths
 assert run(['git','rev-parse','HEAD:deliverables/final-specification-set'])=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
 run(['git','push','origin','HEAD:refs/heads/'+BRANCH])
 remote=run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH]);assert remote.split()[0]==commit
 run(['git','fetch','--no-tags','origin','refs/heads/'+BRANCH]);assert run(['git','rev-parse','FETCH_HEAD'])==commit
 assert run(['git','rev-parse','FETCH_HEAD^{tree}'])==tree
 expected={p:Path(p).read_bytes() for p in paths}
 def fetch(p):
  url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(p);attempts=[]
  for attempt in range(1,4):
   start=utc()
   try:
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'R7-U11-author-immutable-readback'}),timeout=40) as response:
     data=response.read(len(expected[p])+1);status=response.status
    assert data==expected[p],('remote complete byte mismatch',p)
    attempts.append({'attempt':attempt,'start_utc':start,'end_utc':utc(),'http_status':status})
    return {'path':p,'url':url,**ident(data),'full_byte_match':True,'attempts':attempts}
   except (urllib.error.URLError,TimeoutError) as err:
    attempts.append({'attempt':attempt,'start_utc':start,'end_utc':utc(),'error':str(err)})
    if attempt==3:raise
    time.sleep(attempt)
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
  for row in pool.map(fetch,paths):
   r['remote_files'].append(row);save();print(json.dumps({'remote_file':row},ensure_ascii=False),flush=True)
 assert run(['git','ls-remote','--heads','origin','refs/heads/'+BRANCH]).split()[0]==commit
 assert run(['git','status','--porcelain=v1'])==''
 r['status']='CANDIDATE_READY_NOT_REVIEWED';r['freeze']='STOP_WRITING_WAIT_FOR_R7_I_AND_DIFFERENT_CONTEXT_ULTRA_REVIEW';r['remote_file_count']=len(paths);r['remote_total_bytes']=sum(x['bytes'] for x in r['remote_files']);r['end_utc']=utc();save()
 print(json.dumps({k:r[k] for k in ['status','commit','tree','branch','remote_file_count','remote_total_bytes','freeze']},ensure_ascii=False),flush=True)
except BaseException as err:
 r['status']='PUBLICATION_OR_READBACK_BLOCKED';r['error']=str(err);r['end_utc']=utc();save();raise
