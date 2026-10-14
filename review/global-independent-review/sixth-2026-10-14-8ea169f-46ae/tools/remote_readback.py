"""Fetch the authorized report branch into the pre-R6 object cache and read every report blob."""
import argparse, datetime, hashlib, json, pathlib, subprocess, tempfile, time
ROOT=pathlib.Path(__file__).resolve().parents[1]
REPO=ROOT.parents[2]
REL=str(ROOT.relative_to(REPO))
ap=argparse.ArgumentParser();ap.add_argument('--commit',required=True);ap.add_argument('--label',required=True)
a=ap.parse_args()
scratch=ROOT/'temporary/remote-readback.git'
branch=json.loads((ROOT/'control/session.json').read_text())['branch']
destination=ROOT/'publication'/a.label
destination.mkdir(parents=True,exist_ok=False)
commands=[]
def run(args,local=False):
    argv=['git']+([] if local else ['--git-dir',str(scratch)])+args
    start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
    p=subprocess.run(argv,cwd=REPO,capture_output=True)
    n=len(commands)+1
    blob_output=args[:2]==['cat-file','blob']
    if not blob_output:
        (destination/f'command-{n:03}.stdout').write_bytes(p.stdout)
    (destination/f'command-{n:03}.stderr').write_bytes(p.stderr)
    commands.append({'argv':argv,'cwd':str(REPO),'started_at':start,
       'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'duration_seconds':time.monotonic()-t,
       'exit_code':p.returncode,'stdout':({'full_byte_payload_alias':'Git blob '+args[2],
          'bytes':len(p.stdout),'sha256':hashlib.sha256(p.stdout).hexdigest(),
          'reason':'identical complete payload is retained as the pinned report Git object; no second administrative copy'}
          if blob_output else f'command-{n:03}.stdout'),'stderr':f'command-{n:03}.stderr'})
    if not blob_output or p.returncode:
        (destination/'commands.json').write_text(json.dumps(commands,ensure_ascii=False,indent=2)+'\n')
    if p.returncode:raise RuntimeError(p.stderr.decode(errors='replace'))
    return p.stdout
run(['fetch','--no-tags','--no-write-fetch-head','https://github.com/y805939188/pokemon-essentials-clean-room.git',
     'refs/heads/'+branch+':refs/readback/'+a.label])
tip=run(['rev-parse','refs/readback/'+a.label]).decode().strip()
assert tip==a.commit,(tip,a.commit)
remote_tree=run(['rev-parse',tip+'^{tree}']).decode().strip()
local_tree=run(['rev-parse',a.commit+'^{tree}'],True).decode().strip()
assert remote_tree==local_tree
directory_tree=run(['rev-parse',tip+':'+REL]).decode().strip()
raw=run(['ls-tree','-rz',tip,'--',REL])
local_raw=run(['ls-tree','-rz',a.commit,'--',REL],True)
assert raw==local_raw
entries=[]
objects=[]
for item in raw.split(b'\0'):
    if not item:continue
    meta,path=item.split(b'\t',1);mode,kind,oid=meta.split()
    if kind!=b'blob':continue
    objects.append((path.decode(),oid.decode(),mode.decode()))
request=('\n'.join(x[1] for x in objects)+'\n').encode()
processes=[]
for local in (False,True):
    inp=tempfile.TemporaryFile(dir=ROOT/'temporary');inp.write(request);inp.seek(0)
    err=tempfile.TemporaryFile(dir=ROOT/'temporary')
    argv=['git']+([] if local else ['--git-dir',str(scratch)])+['cat-file','--batch']
    stamp=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
    proc=subprocess.Popen(argv,cwd=REPO,stdin=inp,stdout=subprocess.PIPE,stderr=err)
    processes.append((proc,inp,err,argv,stamp,t,hashlib.sha256()))
def read_blob(ctx,oid):
    proc,inp,err,argv,stamp,t,digest=ctx
    header=proc.stdout.readline();digest.update(header)
    h_oid,h_type,h_len=header.strip().split()
    assert h_oid.decode()==oid and h_type==b'blob'
    remaining=int(h_len);parts=[]
    while remaining:
        part=proc.stdout.read(min(1048576,remaining));assert part
        digest.update(part);parts.append(part);remaining-=len(part)
    delimiter=proc.stdout.read(1);assert delimiter==b'\n';digest.update(delimiter)
    return b''.join(parts)
for p,blob,mode in objects:
    # Two independent object databases: new report objects were absent at cache seed time.
    remote=read_blob(processes[0],blob)
    local=read_blob(processes[1],blob)
    assert remote==local,p
    h=hashlib.sha256(remote).hexdigest()
    recalculated=hashlib.sha1(b'blob '+str(len(remote)).encode()+b'\0'+remote).hexdigest()
    assert recalculated==blob
    entries.append({'path':p,'commit':tip,'workspace_tree':remote_tree,'directory_tree':directory_tree,
       'bytes':len(remote),'sha256':h,'git_blob':blob,'mode':mode,
       'readback':'COMPLETE_REMOTE_OBJECT_BYTES','read_scope':'all bytes',
       'source':'authorized ordinary pushed report branch, differential fetch into pre-R6 cache'})
for proc,inp,err,argv,stamp,t,digest in processes:
    tail=proc.stdout.read();assert not tail;code=proc.wait();err.seek(0);stderr=err.read()
    n=len(commands)+1;(destination/f'command-{n:03}.stderr').write_bytes(stderr)
    commands.append({'argv':argv,'cwd':str(REPO),'started_at':stamp,
      'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'duration_seconds':time.monotonic()-t,
      'exit_code':code,'stdin_sha256':hashlib.sha256(request).hexdigest(),'stdin_blob_order':objects,
      'stdout':{'sha256_complete_batch_stream':digest.hexdigest(),'complete_payload_aliases':'readback.json entries; all Git blobs preserved at pinned report commit',
                'reason':'all byte output consumed and checked; avoid a second copy of every published evidence file'},'stderr':f'command-{n:03}.stderr'})
    inp.close();err.close();assert code==0,(code,stderr)
(destination/'commands.json').write_text(json.dumps(commands,ensure_ascii=False,indent=2)+'\n')
receipt={'schema':'r6.remote-readback.v1','commit':tip,'workspace_tree':remote_tree,
 'report_directory_tree':directory_tree,'report_root':REL,'files':len(entries),
 'bytes':sum(x['bytes'] for x in entries),'entries':entries,'all_full_bytes_match':True,
 'cache_seed':'control/remote-cache-seed.json','old_identical_input_transport_cache_reused':True,
 'new_R6_objects_seeded_before_push':False,'semantic_review_implied':False,
 'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'update_started':False}
(destination/'readback.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='entries'},ensure_ascii=False))
