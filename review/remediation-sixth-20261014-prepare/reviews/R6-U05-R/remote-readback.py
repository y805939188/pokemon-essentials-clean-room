"""Full pinned remote report payload readback, using no configuration probe."""
import concurrent.futures, datetime, hashlib, json, subprocess, sys, urllib.parse, urllib.request
from pathlib import Path
D=Path(__file__).resolve().parent;ROOT=D.parents[3]
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def identity(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def git(*args):
 start=now()
 p=subprocess.run(['git',*args],cwd=ROOT,capture_output=True)
 rec={'utc_start':start,'utc_end':now(),'cwd':str(ROOT),'argv':['git',*args],'stdout':p.stdout.decode(),'stderr':p.stderr.decode(),'independent_exit_code':p.returncode}
 transport.append(rec)
 if p.returncode:raise RuntimeError(rec)
 return p.stdout
commit=sys.argv[1];output=sys.argv[2];branch='codex/remediation-sixth-r6-u05-review-20261014';directory=str(D.relative_to(ROOT));transport=[];t0=now()
remote=git('ls-remote','origin','refs/heads/'+branch).decode().strip().split()
assert remote==[commit,'refs/heads/'+branch],remote
git('fetch','--no-tags','origin',branch)
assert git('rev-parse','FETCH_HEAD').decode().strip()==commit
assert git('cat-file','-t',commit).decode().strip()=='commit'
tree=git('rev-parse',commit+'^{tree}').decode().strip()
directory_tree=git('rev-parse',commit+':'+directory).decode().strip()
entries=[]
for entry in git('ls-tree','-r','-z','--full-tree',commit,'--',directory).split(b'\0'):
 if not entry:continue
 meta,path=entry.split(b'\t',1);mode,kind,blob=meta.decode().split();path=path.decode()
 assert mode=='100644' and kind=='blob'
 expected=git('show',commit+':'+path)
 entries.append({'path':path,'mode':mode,'git_object_type':kind,'git_blob':blob,'expected_identity':identity(expected),'expected_bytes':expected})
actual_changed=git('diff','--name-only','64c77cf1733ab7db300e9f5ac7c79a2886c8ac68',commit).decode().splitlines()
assert sorted(actual_changed)==sorted(x['path'] for x in entries),actual_changed
def read(entry):
 url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+commit+'/'+urllib.parse.quote(entry['path']);start=now()
 with urllib.request.urlopen(url,timeout=40) as response:b=response.read();status=response.status
 actual=identity(b)
 assert b==entry['expected_bytes'] and actual==entry['expected_identity'] and actual['git_blob']==entry['git_blob'],entry['path']
 return {k:v for k,v in entry.items() if k!='expected_bytes'}|{'utc_start':start,'utc_end':now(),'url':url,'http_status':status,'full_remote_identity':actual,'raw_bytes_compared':True,'result':'PASS'}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:receipts=list(pool.map(read,entries))
result={'schema':'r6.u05.independent-review.full-remote-readback.v1','utc_start':t0,'utc_end':now(),'cwd':str(ROOT),'argv':sys.argv,'result':'PASS','commit':commit,'workspace_tree':tree,'review_directory':directory,'review_directory_tree':directory_tree,'remote_branch':'refs/heads/'+branch,'remote_commit_advertisement_verified':True,'transport':transport,'payload_count':len(receipts),'payload_bytes':sum(x['full_remote_identity']['bytes'] for x in receipts),'complete_payloads':receipts,'mode_type_path_tree_basis':'The remote advertises the exact immutable commit; a read-only fetch confirms FETCH_HEAD. That Git commit content-addresses its tree/modes/path/blob objects, and every report blob (including manifests) is independently fetched in full at the pinned remote commit and compared as original bytes/bytes/SHA256/Git blob. Not a remote-tracking-ref-only check.','self_identity':'This receipt binds an already existing commit; it is not part of that commit and makes no self-hash claim.'}
if output!='--stdout-only':
 target=D/output
 assert target.parent==D and target.suffix=='.json'
 target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
summary={k:result[k] for k in ['utc_start','utc_end','result','commit','workspace_tree','review_directory_tree','payload_count','payload_bytes']}
summary['all_payloads_original_bytes_SHA256_blob_mode_type_path_tree']='PASS';summary['independent_exit_code']=0
print(json.dumps(summary,ensure_ascii=False))
