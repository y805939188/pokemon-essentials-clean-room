"""Publish exact already frozen C34 blobs; record ordinary commit/push and independent transport proof."""
from pathlib import Path
import datetime,hashlib,json,subprocess
REPO=Path('/workspace/pokemon-essentials-clean-room');RR=REPO/'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e';PUB=RR/'publication';IO=PUB/'checkpoint-34-io'
HEAD='c7fec918d511a0ead8ab325c934e9346d7c43cac';BRANCH='codex/review-eighth-20261016-fd1df57-c84e';PREFIX=str(RR.relative_to(REPO))+'/'
EXPECTED_CANDIDATE_SHA='5a2900f9e9d067982776be87c4cfa23087dd67014730ea9b1f4970af6dc0031f'
events=[]
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def put(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def run(args,label,stdin=None):
 start=utc();q=subprocess.run(args,cwd=REPO,input=stdin,capture_output=True);end=utc()
 (IO/(label+'.stdout')).write_bytes(q.stdout);(IO/(label+'.stderr')).write_bytes(q.stderr)
 e={'args':args,'start_utc':start,'end_utc':end,'exit':q.returncode,'stdout':'publication/checkpoint-34-io/'+label+'.stdout','stderr':'publication/checkpoint-34-io/'+label+'.stderr','stdout_bytes':len(q.stdout),'stdout_sha256':sha(q.stdout),'stderr_bytes':len(q.stderr),'stderr_sha256':sha(q.stderr)}
 if stdin is not None:e.update(stdin_bytes=len(stdin),stdin_sha256=sha(stdin))
 put(IO/(label+'.operation.json'),e);events.append(e)
 assert q.returncode==0,e
 return q.stdout
def git(*args,label,stdin=None):return run(['git','-C',str(REPO),*args],label,stdin)
assert git('rev-parse','HEAD',label='publish-guard-head').decode().strip()==HEAD
assert git('branch','--show-current',label='publish-guard-branch').decode().strip()==BRANCH
assert not git('diff','--cached','--name-only','-z',label='publish-guard-index')
candidate=PUB/'checkpoint-34-candidates.json';raw=candidate.read_bytes();assert sha(raw)==EXPECTED_CANDIDATE_SHA
frozen=json.loads(raw);assert frozen['baseline_HEAD']==HEAD and frozen['root_registry_count']==27
rows=list(frozen['files']);oid=git('hash-object','-w','--stdin',label='publish-selection-envelope',stdin=raw).decode().strip()
rows.append({'path':str(candidate.relative_to(REPO)),'mode':'100644','type':'blob','blob':oid,'bytes':len(raw),'sha256':sha(raw)})
assert len({x['path'] for x in rows})==len(rows)
assert all(x['path'].startswith(PREFIX) and x['mode']=='100644' and x['type']=='blob' and x['bytes']<100000000 for x in rows)
assert all(not any(c.endswith('.git') for c in Path(x['path']).parts) and 'tmp_pack_' not in x['path'] and '__pycache__' not in Path(x['path']).parts for x in rows)
# Read the frozen objects, independent of any now-newer worktree bytes written by root.
proc=subprocess.Popen(['git','-C',str(REPO),'cat-file','--batch'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
start=utc()
try:
 for x in rows:
  proc.stdin.write((x['blob']+'\n').encode());proc.stdin.flush();header=proc.stdout.readline().decode().split();assert header==[x['blob'],'blob',str(x['bytes'])]
  b=proc.stdout.read(x['bytes']);assert len(b)==x['bytes'] and proc.stdout.read(1)==b'\n' and sha(b)==x['sha256']
finally:
 proc.stdin.close();err=proc.stderr.read();exitcode=proc.wait()
put(IO/'publish-frozen-objects.operation.json',{'args':['git','-C',str(REPO),'cat-file','--batch'],'start_utc':start,'end_utc':utc(),'exit':exitcode,'objects':len(rows),'all_full_blob_SHA_bytes_exact':exitcode==0,'stderr':err.decode(errors='replace'),'qualification':'Frozen exact local objects only, no current worktree substitution and no semantic credit.'})
assert exitcode==0
data=b''.join((x['mode']+' '+x['blob']+'\t'+x['path']).encode()+b'\0' for x in rows)
git('update-index','-z','--index-info',label='publish-exact-update-index',stdin=data)
staged={p.decode() for p in git('diff','--cached','--name-only','-z',label='publish-staged-paths').split(b'\0') if p};assert staged=={x['path'] for x in rows}
tree=git('write-tree',label='publish-index-tree').decode().strip()
formal=git('rev-parse',tree+':deliverables/final-specification-set',label='publish-formal-tree-guard').decode().strip();assert formal=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
delta=git('diff','--name-only','-z',HEAD,tree,label='publish-tree-delta').split(b'\0');assert all(not p or p.decode().startswith(PREFIX) for p in delta)
assert git('rev-parse','HEAD',label='publish-final-parent-guard').decode().strip()==HEAD
remote_before=git('ls-remote','origin','refs/heads/'+BRANCH,label='publish-remote-before').decode().split();assert remote_before==[HEAD,'refs/heads/'+BRANCH]
git('commit','-m','review: checkpoint 34 completed receivers and metadata evidence',label='publish-commit')
commit=git('rev-parse','HEAD',label='publish-commit-id').decode().strip();assert commit!=HEAD
assert git('rev-parse','HEAD^{tree}',label='publish-commit-tree').decode().strip()==tree
assert git('rev-parse','HEAD^',label='publish-commit-parent').decode().strip()==HEAD
assert not git('diff','--cached','--name-only','-z',label='publish-postcommit-index')
reporttree=git('rev-parse',commit+':'+PREFIX.rstrip('/'),label='publish-report-tree').decode().strip()
git('push','origin','HEAD:refs/heads/'+BRANCH,label='publish-push')
remote_after=git('ls-remote','origin','refs/heads/'+BRANCH,label='publish-remote-after').decode().split();assert remote_after==[commit,'refs/heads/'+BRANCH]
push_receipt={'schema':'gr8-checkpoint34-ordinary-commit-push-receipt/v1','utc':utc(),'status':'PUSH_SUCCEEDED_REMOTE_REF_EXACT','parent':HEAD,'commit':commit,'workspace_tree':tree,'report_tree':reporttree,'branch':BRANCH,'remote_ref':'refs/heads/'+BRANCH,'remote_ref_exact':True,'candidate_sha256':EXPECTED_CANDIDATE_SHA,'committed_paths':len(rows),'committed_payload_bytes':sum(x['bytes'] for x in rows),'frozen_registry_count':27,'local_actual_contexts':61,'external_actual_contexts':64,'known_actual_contexts':125,'new_contexts':0,'new_votes':0,'semantic_credit':'NONE; existing root receipts preserve original actual source-reader credit','whole_review_complete':False,'whole_required':None,'whole_history_canonical':'UNFROZEN','UPDATE_NOT_STARTED':True,'post_freeze_root_new_files_not_staged':True,'events':events}
put(PUB/'checkpoint-34-push-receipt.json',push_receipt)
print(json.dumps({'status':push_receipt['status'],'commit':commit,'tree':tree,'report_tree':reporttree,'ref':'refs/heads/'+BRANCH,'committed_paths':len(rows),'bytes':push_receipt['committed_payload_bytes']},ensure_ascii=False),flush=True)
baseline='publication/r8-qualified-primary21-and-recoveries-readback-33.json';base=json.loads((RR/baseline).read_bytes());assert base['status']=='VERIFIED' and base['commit']==HEAD
name='r8-four-receivers-and-metadata-readback-34'
assert not (Path('/workspace/scratch')/name/'remote.git').exists()
trusted=PUB/'incremental-remote-readback.py';trusted_sha=sha(trusted.read_bytes())
out=run(['python',str(trusted),commit,name,baseline],'publish-fresh-remote-readback')
proof=PUB/(name+'.json');receipt=json.loads(proof.read_bytes());assert receipt['status']=='VERIFIED' and receipt['commit']==commit and receipt['report_tree']==reporttree
assert receipt['compressed_original_count']==116 and receipt['verifier_source_sha256']==trusted_sha
done={'schema':'gr8-checkpoint34-complete-publication-status/v1','utc':utc(),'status':'COMMIT_PUSH_AND_FRESH_REMOTE_READBACK_VERIFIED','commit':commit,'workspace_tree':tree,'report_tree':reporttree,'remote_ref':'refs/heads/'+BRANCH,'candidate_sha256':EXPECTED_CANDIDATE_SHA,'push_receipt':'publication/checkpoint-34-push-receipt.json','readback_receipt':{'path':'publication/'+proof.name,'bytes':proof.stat().st_size,'sha256':sha(proof.read_bytes())},'remote_files':receipt['count'],'remote_bytes':receipt['bytes'],'full_new_remote_blob_count':receipt['full_new_remote_blob_count'],'reused_verified_blob_count':receipt['reused_verified_blob_count'],'compressed_original_count':receipt['compressed_original_count'],'compressed_original_bytes':receipt['compressed_original_bytes'],'source_policy':receipt['seed_policy'],'frozen_registry_count':27,'new_contexts':0,'new_votes':0,'new_semantic_credit':0,'business_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'whole_review_complete':False,'whole_required':None,'whole_history_canonical':'UNFROZEN','proof_files_created_after_commit':'Own C34 receipt/IO/readback are local successors, not falsely claimed inside same commit.'}
put(PUB/'checkpoint-34-completed.json',done)
print(json.dumps(done,ensure_ascii=False),flush=True)
