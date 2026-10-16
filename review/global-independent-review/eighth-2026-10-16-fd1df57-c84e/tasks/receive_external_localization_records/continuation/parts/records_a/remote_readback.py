"""Read only the selected report delta from a separately fetched blob-filtered remote store.
Usage: python remote_readback.py COMMIT BASE_COMMIT RECEIPT_PATH_OR_DASH
Fetch COMMIT with --filter=blob:none into REMOTE before invoking. This tool never runs reference code.
"""
import sys,subprocess,pathlib,json,hashlib,datetime,glob,collections
ROOT=pathlib.Path('/workspace/pokemon-essentials-clean-room')
PREFIX='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/receive_external_localization_records/continuation/parts/records_a/'
REMOTE=pathlib.Path('/tmp/r8-elr-records-a-remote-readback.git')
commit,base,destination=sys.argv[1:]
def git(root,*args):return subprocess.check_output(['git','-C',str(root),*args])
def parse_tree(root):
 result=[]
 for entry in git(root,'ls-tree','-r','-z',commit,'--',PREFIX).split(b'\0'):
  if not entry:continue
  meta,path=entry.split(b'\t');mode,kind,blob=meta.decode().split()
  assert kind=='blob'
  result.append({'path':path.decode(),'mode':mode,'git_blob':blob})
 return result
expected=parse_tree(ROOT);actual=parse_tree(REMOTE);assert expected==actual
local_tree=git(ROOT,'rev-parse',commit+'^{tree}').decode().strip()
remote_tree=git(REMOTE,'rev-parse',commit+'^{tree}').decode().strip();assert local_tree==remote_tree
local_task_tree=git(ROOT,'rev-parse',commit+':'+PREFIX.rstrip('/')).decode().strip()
remote_task_tree=git(REMOTE,'rev-parse',commit+':'+PREFIX.rstrip('/')).decode().strip();assert local_task_tree==remote_task_tree
changed=git(ROOT,'diff','--name-only',base,commit).decode().splitlines();assert changed and all(x.startswith(PREFIX) for x in changed)
selected=[x for x in expected if x['path'] in changed];assert len(selected)==len(changed)
# A promisor no-blob fetch contains commit/tree metadata. Enumerate existing object IDs without requesting missing blobs.
existing=set()
for line in git(REMOTE,'cat-file','--batch-all-objects','--batch-check=%(objectname) %(objecttype)').decode().splitlines():
 oid,typ=line.split();existing.add(oid)
missing=[x['git_blob'] for x in selected if x['git_blob'] not in existing]
fetch_result=None
if missing:
 p=subprocess.run(['git','-C',str(REMOTE),'fetch','--no-tags','--filter=blob:none','origin',*missing],capture_output=True)
 fetch_result={'argv':['git','-C',str(REMOTE),'fetch','--no-tags','--filter=blob:none','origin',*missing],'exit_code':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()};assert p.returncode==0,fetch_result
files=[]
for row in selected:
 data=git(REMOTE,'cat-file','blob',row['git_blob']);local=git(ROOT,'cat-file','blob',row['git_blob'])
 assert data==local
 blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest();assert blob==row['git_blob']
 files.append({**row,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'full_remote_blob_read':True})
result={'schema':'records-a-delta-remote-readback/v1','verified_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commit':commit,'base_commit':base,'checkout_tree':remote_tree,'task_tree':remote_task_tree,'task_prefix':PREFIX,'all_task_path_mode_blob_entries_match':True,'task_payload_count':len(actual),'delta_file_count':len(files),'delta_bytes':sum(x['bytes'] for x in files),'delta_files':files,'task_full_mode_blob_set':actual,'only_delta_blob_ids_requested':missing,'fetch_io':fetch_result,'isolation':{'remote_store':str(REMOTE),'object_alternates_used':False,'initial_metadata_fetch':'git fetch --filter=blob:none --depth=1 origin fixed C; no old input blobs requested','unchanged_inputs':'reuse fixed identity; no 213-payload recovery or raw input re-download'},'prior_failed_api_attempt':{'tool_chunk':'e3a667','exit_code':1,'reason':'HTTPS proxy tunnel returned 403 for api.github.com tree endpoint; no approval rejection','replacement':'ordinary authorized Git promisor transport; metadata then only selected report blobs'},'qualification':'TOOL_VALIDATION only; no new semantic reading or reference behavior credit','UPDATE_NOT_STARTED':True}
if destination!='-':
 out=pathlib.Path(destination).resolve();assert out.is_relative_to(ROOT/PREFIX)
 out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['commit','base_commit','checkout_tree','task_tree','task_payload_count','delta_file_count','delta_bytes','all_task_path_mode_blob_entries_match']},ensure_ascii=False))
