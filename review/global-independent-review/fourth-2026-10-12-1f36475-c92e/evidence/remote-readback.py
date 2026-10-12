import pathlib,subprocess,json,hashlib,datetime,tempfile,sys,tarfile
W=pathlib.Path('/Users/dingshinn/.codex/worktrees/review-fourth-1f36475/pokemon-framework-reference');ROOT='review/global-independent-review/fourth-2026-10-12-1f36475-c92e';BR='codex/review-fourth-20261012-1f36475-c92e';URL='https://github.com/y805939188/pokemon-essentials-clean-room.git'
commit=sys.argv[1];out=pathlib.Path(sys.argv[2]);bare=pathlib.Path(sys.argv[3]) if len(sys.argv)>3 else pathlib.Path(tempfile.mkdtemp(prefix='gr4-c92e-remote-'))/'objects.git'
commands=[]
def run(a,cwd=None,input=None):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.run(a,cwd=cwd,input=input,capture_output=True);commands.append({'command':a,'cwd':str(cwd or W),'started_at':start,'exit_code':p.returncode,'stdout':p.stdout.decode(errors='replace')[:3000],'stderr':p.stderr.decode(errors='replace')[-5000:]})
 if p.returncode:raise RuntimeError(commands[-1])
 return p.stdout
def git(*a,cwd=W):return run(['git',*a],cwd)
new=not bare.exists()
if new:
 bare.parent.mkdir(parents=True,exist_ok=True);git('init','--bare',str(bare));git('remote','add','origin',URL,cwd=bare)
print('FETCH_REMOTE',str(bare),flush=True)
git('fetch','--no-tags','--depth=6','--filter=blob:none','origin','refs/heads/'+BR+':refs/remotes/origin/review',cwd=bare)
actual=git('rev-parse','refs/remotes/origin/review',cwd=bare).decode().strip();assert actual==commit,(actual,commit)
tree=git('rev-parse',commit+'^{tree}',cwd=bare).decode().strip();assert tree==git('rev-parse',commit+'^{tree}').decode().strip()
def entries(cwd):
 rows=[]
 for x in git('ls-tree','-r','-z',commit,'--',ROOT,cwd=cwd).split(b'\0'):
  if not x:continue
  meta,path=x.split(b'\t',1);mode,kind,oid=meta.decode().split();assert kind=='blob';rows.append({'path':path.decode(),'mode':mode,'git_blob':oid})
 return rows
remote=entries(bare);local=entries(W);assert remote==local
# Batch missing objects through normal Git fetch, no local objects/alternates copied.
uniq=sorted({x['git_blob'] for x in remote});print('READ_FULL_ARTIFACTS',len(remote),flush=True)
run(['git','-c','fetch.negotiationAlgorithm=noop','fetch','--no-tags','--no-write-fetch-head','origin','--stdin'],bare,('\n'.join(uniq)+'\n').encode())
archive=bare.parent/(commit+'.tar');git('archive','--format=tar','--output='+str(archive),commit,ROOT,cwd=bare)
rows=[];required={ROOT+'/'+x for x in ['final-report.md','findings.json','cloud-fourth-update-handoff-prompt.md','cloud-fourth-update-handoff-manifest.json']};required_present=[]
with tarfile.open(archive) as tf:
 members={m.name:m for m in tf.getmembers() if m.isfile()}
 assert set(members)=={x['path'] for x in remote}
 for x in remote:
  b=tf.extractfile(members[x['path']]).read();lb=git('show',commit+':'+x['path']);assert b==lb,x['path'];blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest();assert blob==x['git_blob'];rows.append({**x,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'full_remote_bytes_read':True})
  if x['path'] in required or x['path'].endswith('/publication-receipt.json') or x['path'].endswith('/publication-receipt.md'):
   b.decode('utf-8')
   if x['path'].endswith('.json'):json.loads(b)
   required_present.append(x['path'])
assert required.issubset(required_present)
result={'schema_version':'1.0','status':'PASS_FULL_REMOTE_BYTES','completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'remote_url':URL,'branch':BR,'commit':actual,'tree':tree,'fresh_remote_object_store':str(bare),'store_created_this_run':new,'local_objects_or_alternates_copied':False,'verification':'Server-advertised branch fetched into isolated Git object store; complete report blobs fetched from origin, archive bytes compared byte-for-byte with fixed local commit; SHA256/blob/bytes and trees checked. Not HTTP200 or only-local hashing.','files_count':len(rows),'total_bytes':sum(x['bytes'] for x in rows),'required_files_fully_read_utf8_or_json_parsed':required_present,'artifacts':rows,'commands':commands,'exit_code':0,'side_effects':'Only isolated temporary Git objects/archive and named output receipt; no user/source/formal/main writes'}
out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['status','commit','tree','files_count','total_bytes','fresh_remote_object_store']},ensure_ascii=False),flush=True)
