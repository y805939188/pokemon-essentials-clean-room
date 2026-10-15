import argparse, concurrent.futures, datetime, hashlib, json, os, pathlib, subprocess, urllib.parse, urllib.request
ap=argparse.ArgumentParser();ap.add_argument('--commit',required=True);ap.add_argument('--output',required=True);ap.add_argument('--git-dir',required=True);args=ap.parse_args()
ROOT=pathlib.Path('/workspace/r7-ir-R7-U06');REPO=ROOT/'result'
PREFIX='review/remediation-seventh-20261015-prepare/integrated-reviews/R7-U06/r1/'
BRANCH='codex/r7-ir-u06-20261015-r1';REF='refs/heads/'+BRANCH
URL='https://github.com/y805939188/pokemon-essentials-clean-room.git'
assert len(args.commit)==40 and all(c in '0123456789abcdef' for c in args.commit)
start=datetime.datetime.now(datetime.timezone.utc).isoformat();commands=[]
def run(argv,cwd=None):
    t=datetime.datetime.now(datetime.timezone.utc).isoformat();p=subprocess.Popen(argv,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE);out,err=p.communicate()
    commands.append({'argv':argv,'cwd':str(cwd) if cwd else None,'tool_pid':p.pid,'start_utc':t,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'stdout':out.decode(),'stderr':err.decode(),'exit_code':p.returncode})
    assert p.returncode==0,(argv,p.returncode,err.decode())
    return out
def git(*xs,cwd=REPO):return run(['git','-c','credential.helper=','-c','http.extraHeader=',*xs],cwd)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
before=git('ls-remote',URL,REF).decode().strip();assert before==args.commit+'\t'+REF,before
gd=pathlib.Path(args.git_dir);assert not gd.exists();gd.mkdir(parents=True)
git('init','--bare',str(gd))
git('--git-dir='+str(gd),'fetch','--no-tags','--depth=1','--filter=blob:none',URL,args.commit)
remote_tree=git('--git-dir='+str(gd),'rev-parse','FETCH_HEAD^{tree}').decode().strip()
local_tree=git('rev-parse',args.commit+'^{tree}').decode().strip();assert remote_tree==local_tree
tree_data=git('--git-dir='+str(gd),'ls-tree','-r','FETCH_HEAD','--',PREFIX).decode()
remote_rows=[]
for line in tree_data.splitlines():
    m,path=line.split('\t');mode,typ,blob=m.split();assert typ=='blob' and mode=='100644' and path.startswith(PREFIX)
    remote_rows.append((path,mode,blob))
local_paths=git('ls-tree','-r','--name-only',args.commit,'--',PREFIX).decode().splitlines()
assert [r[0] for r in remote_rows]==local_paths and remote_rows
def one(row):
    path,mode,blob=row
    local=subprocess.check_output(['git','show',args.commit+':'+path],cwd=REPO)
    url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+args.commit+'/'+urllib.parse.quote(path,safe='/')
    t=datetime.datetime.now(datetime.timezone.utc).isoformat()
    req=urllib.request.Request(url,headers={'User-Agent':'R7-U06-independent-byte-readback','Cache-Control':'no-cache'})
    with urllib.request.urlopen(req,timeout=60) as response:
        status=response.status;data=response.read();final_url=response.url
    assert status==200 and data==local and ident(data)['git_blob']==blob,path
    return {'path':path,'fixed_commit':args.commit,'raw_url':url,'final_url':final_url,'http_status':status,'start_utc':t,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'git_mode':mode,**ident(data),'remote_tree_blob':blob,'local_commit_bytes_equal':True}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    files=list(pool.map(one,remote_rows))
after=git('ls-remote',URL,REF).decode().strip();assert after==before
receipt={'schema':'r7.U06.complete-remote-byte-readback.r1','pid':os.getpid(),'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'branch':BRANCH,'remote_ref':REF,'remote_ref_before':before,'remote_ref_after':after,'commit':args.commit,'remote_tree':remote_tree,'local_tree':local_tree,'fresh_bare_git_directory':str(gd),'all_result_files_including_manifest':len(files),'total_bytes':sum(x['bytes'] for x in files),'files':files,'git_commands':commands,'result':'COMPLETE_FIXED_COMMIT_REMOTE_PER_FILE_BYTES_SHA256_GIT_BLOB_MODE_MATCH','qualification':'Only result evidence byte publication verification; no semantic/runtime/acceptance/closure promotion.'}
out=pathlib.Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['commit','remote_tree','all_result_files_including_manifest','total_bytes','result']},ensure_ascii=False))
