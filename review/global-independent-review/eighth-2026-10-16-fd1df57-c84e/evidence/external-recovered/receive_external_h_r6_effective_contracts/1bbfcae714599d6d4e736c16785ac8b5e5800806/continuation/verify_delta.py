"""Verify only new/changed remote report payloads; reuse the complete P0 identity cache.
The full path/mode/blob/tree set is still checked. No semantic credit is created.
"""
import pathlib,subprocess,json,hashlib,datetime,sys
T=pathlib.Path(__file__).resolve().parents[1];repo=T.parents[4];C=sys.argv[1];stage=sys.argv[2];assert stage in ['core','final'];assert len(C)==40
J=T/'runtime/readback-final.git';G=['git','--git-dir='+str(J)];L=['git','-C',str(repo)];P0='ab5b6b416d1f833490772fdecacf1cd8be815d65';prefix=str(T.relative_to(repo))+'/'
cache=json.loads((T/'runtime/final-readback.json').read_text());assert cache['commit']==P0 and cache['status']=='VERIFIED' and cache['file_count']==1451
baseline={x['path']:x for x in cache['files']};events=[]
reuse_commit=P0
if stage=='final':
 prior=json.loads((T/'continuation/publication/core-delta-readback.json').read_text());assert prior['status']=='VERIFIED' and not prior['removed_paths']
 baseline.update({x['path']:x for x in prior['changed_files']});reuse_commit=prior['commit'];assert len(baseline)==prior['file_count']
assert subprocess.run(G+['cat-file','-e',C+'^{commit}'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode!=0,'new commit already in verification cache'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def ident(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())
def run(a):
 t=now();p=subprocess.run(a,capture_output=True);events.append(dict(args=a,start_utc=t,end_utc=now(),exit=p.returncode,stdout=p.stdout.decode(errors='backslashreplace') if len(p.stdout)<10000 else dict(bytes=len(p.stdout),sha256=hashlib.sha256(p.stdout).hexdigest(),purpose='complete tree listing compared byte-for-byte; no giant repeated log'),stderr=p.stderr.decode(errors='backslashreplace')));assert p.returncode==0,(a,p.stderr);return p.stdout
run(G+['fetch','--no-tags','--depth=1','https://github.com/y805939188/pokemon-essentials-clean-room.git',C])
listing=run(G+['ls-tree','-r','-z',C,'--',prefix]);assert listing==subprocess.check_output(L+['ls-tree','-r','-z',C,'--',prefix])
changed=[];reused=[];paths=set()
for line in listing.split(b'\0'):
 if not line:continue
 meta,path=line.split(b'\t',1);mode,typ,oid=meta.decode().split();path=path.decode();assert typ=='blob';paths.add(path)
 if path in baseline and baseline[path]['mode']==mode and baseline[path]['git_blob']==oid:reused.append(path);continue
 data=subprocess.check_output(G+['cat-file','blob',oid]);assert data==subprocess.check_output(L+['cat-file','blob',oid]);z=ident(data);assert z['git_blob']==oid;changed.append(dict(path=path,mode=mode,**z))
removed=sorted(set(baseline)-paths);assert not removed,'input or prior evidence removed'
tree=run(G+['rev-parse',C+'^{tree}']).decode().strip();task=run(G+['rev-parse',C+':'+prefix.rstrip('/')]).decode().strip();assert tree==subprocess.check_output(L+['rev-parse',C+'^{tree}']).decode().strip();assert task==subprocess.check_output(L+['rev-parse',C+':'+prefix.rstrip('/')]).decode().strip()
assert run(G+['rev-parse',C+':deliverables/final-specification-set']).decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
# All gzip/decoded input payloads remain exact P0 blob/mode identities. Do not decode them repeatedly.
assert not any(('/recovered/' in x['path'] or '/decoded/' in x['path'] or x['path'].endswith('/decoded-index.json')) for x in changed)
verified=dict(schema='r8-continuation-incremental-publication/v1',status='VERIFIED',commit=C,checkout_tree=tree,task_tree=task,prefix=prefix,file_count=len(paths),bytes=sum(x['bytes'] for x in changed)+sum(baseline[p]['bytes'] for p in reused),changed_fully_remote_read_count=len(changed),changed_bytes=sum(x['bytes'] for x in changed),changed_files=changed,reused_verified_file_count=len(reused),reuse_baseline_commit=reuse_commit,reused_P0_identity_set_sha256=hashlib.sha256(json.dumps([baseline[p] for p in sorted(reused)],sort_keys=True,separators=(',',':')).encode()).hexdigest(),verified_input_cache=dict(commit=P0,checkout_tree=cache['checkout_tree'],task_tree=cache['task_tree'],full_verified_files=1451,full_verified_bytes=cache['bytes'],all52_decoded_identities_retained=True,proof='First publication final response plus unchanged published publication/core-binding.json and this environment runtime/final-readback.json'),complete_path_mode_blob_set_and_tree_equal=True,removed_paths=removed,events=events,semantic_status='INCOMPLETE',semantic_credit=0,utc_end=now())
where=T/'continuation/publication/core-delta-readback.json' if stage=='core' else T/'runtime/continuation-final-readback.json';where.parent.mkdir(exist_ok=True);where.write_text(json.dumps(verified,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:verified[k] for k in ['status','commit','checkout_tree','task_tree','file_count','bytes','changed_fully_remote_read_count','changed_bytes','reused_verified_file_count','semantic_status']},ensure_ascii=False))
