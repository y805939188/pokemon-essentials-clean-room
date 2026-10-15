"""Read every result artifact from an immutable remote commit; compare all bytes."""
import concurrent.futures,datetime,hashlib,json,pathlib,subprocess,sys,urllib.parse,urllib.request
commit=sys.argv[1];dest=pathlib.Path(sys.argv[2]);assert len(commit)==40
prefix='candidates/R7-U02/evidence/reviewer/r1/'
def git(*args):return subprocess.check_output(['git',*args])
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
branch='refs/heads/codex/r7-u02-reviewer-20261015-r1';before=git('ls-remote','--heads','origin',branch).decode();assert before.split()[0]==commit
changed=git('diff','--name-only','e646432c644dec04d306842cc5a559a29c718fbc',commit).decode().splitlines();assert all(p.startswith(prefix) for p in changed)
rows=[]
for line in git('ls-tree','-r',commit,prefix).decode().splitlines():
 meta,p=line.split('\t');mode,typ,blob=meta.split();assert mode=='100644' and typ=='blob';rows.append((p,blob))
assert sorted(p for p,_ in rows)==sorted(changed)
dest.mkdir(parents=True,exist_ok=False)
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
def one(row):
 p,blob=row;url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(p)
 begin=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with urllib.request.urlopen(url,timeout=40) as response:d=response.read();status=response.status
 expected=git('show',commit+':'+p);assert d==expected
 i=ident(d);assert i['git_blob']==blob
 q=dest/'files'/p;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(d)
 return {'path':p,**i,'mode':'100644','url':url,'http_status':status,'start_utc':begin,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'full_bytes_match':True}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:result=list(pool.map(one,rows))
after=git('ls-remote','--heads','origin',branch).decode();assert before==after
r={'schema':'r7.u02.reviewer-complete-remote-readback.v1','commit':commit,'tree':git('rev-parse',commit+'^{tree}').decode().strip(),'branch':branch,'ref_before':before,'ref_after':after,'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':result,'file_count':len(result),'bytes':sum(x['bytes'] for x in result),'complete_changed_file_set_verified':True,'all_full_bytes_match':True,'scope_only_reviewer_r1':True,'qualification':'Transport and identity only; no new semantic or runtime credit.'}
(dest/'remote-readback.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['commit','tree','file_count','bytes','complete_changed_file_set_verified','all_full_bytes_match','scope_only_reviewer_r1']}))
