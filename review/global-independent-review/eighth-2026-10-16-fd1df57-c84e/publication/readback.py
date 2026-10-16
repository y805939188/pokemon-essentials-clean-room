from pathlib import Path
import subprocess,sys,json,hashlib,datetime,os
root=Path(__file__).resolve().parents[1];repo=root.parents[2]
commit=sys.argv[1];name=sys.argv[2]
scratch=Path('/workspace/scratch')/name
if scratch.exists():raise SystemExit('readback target already exists; use new isolated name')
scratch.mkdir(mode=0o700)
cache=scratch/'input-object-cache';(cache/'info').mkdir(parents=True)
(cache/'pack').symlink_to(repo/'.git/objects/pack',target_is_directory=True)
bare=scratch/'remote.git'
events=[]
def run(args,check=True):
 p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 events.append({'command':args,'exit':p.returncode,'stdout':p.stdout.decode('utf-8','replace')[:2000],'stderr':p.stderr.decode('utf-8','replace')[:2000]})
 if check and p.returncode:raise RuntimeError(events[-1])
 return p
run(['git','init','--bare',str(bare)])
(bare/'objects/info/alternates').write_text(str(cache)+'\n')
before=run(['git','-C',str(bare),'cat-file','-e',commit],False)
if before.returncode==0:raise SystemExit('target already in input cache; not a new remote transfer')
B8='fd1df570cad987dc3852a3b958f03916e317f7fe'
run(['git','-C',str(bare),'cat-file','-e',B8])
run(['git','-C',str(bare),'update-ref','refs/inputs/b8',B8])
run(['git','-C',str(bare),'fetch','--no-tags','https://github.com/y805939188/pokemon-essentials-clean-room.git',commit])
prefix=str(root.relative_to(repo))
tree=run(['git','-C',str(bare),'rev-parse',commit+':'+prefix]).stdout.decode().strip()
listing=run(['git','-C',str(bare),'ls-tree','-r','-z',commit,'--',prefix]).stdout
rows=[]
for record in listing.split(b'\0'):
 if not record:continue
 head,path=record.split(b'\t',1);mode,typ,blob=head.decode().split();p=path.decode()
 local=subprocess.check_output(['git','-C',str(repo),'cat-file','blob',blob])
 remote=subprocess.check_output(['git','-C',str(bare),'cat-file','blob',blob])
 assert local==remote
 assert subprocess.check_output(['git','hash-object','--stdin'],input=remote).decode().strip()==blob
 rows.append({'path':p,'mode':mode,'type':typ,'blob':blob,'bytes':len(remote),'sha256':hashlib.sha256(remote).hexdigest(),'readback':'FULL_REMOTE_BLOB_BYTES_VERIFIED'})
receipt={'schema':'gr8-remote-readback/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':commit,'report_tree':tree,'remote':'https://github.com/y805939188/pokemon-essentials-clean-room.git','isolated_git_dir':str(bare),'old_input_cache':'Only preexisting packed input objects, excluding current report loose objects; target commit proved absent before fetch','files':rows,'count':len(rows),'bytes':sum(x['bytes'] for x in rows),'status':'VERIFIED','semantic_credit':'NONE: transport byte verification only','events':events,'update_started':False}
out=root/'publication'/(name+'.json');out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['commit','report_tree','count','bytes','status']},ensure_ascii=False))
