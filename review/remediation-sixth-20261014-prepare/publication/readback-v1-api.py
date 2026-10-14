import argparse, concurrent.futures, datetime, hashlib, json, subprocess, urllib.parse, urllib.request
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('commit');p.add_argument('label');a=p.parse_args()
repo=Path('/workspace/pokemon-essentials-clean-room');out=Path('/workspace/r6-publication-scratch');prefix='review/remediation-sixth-20261014-prepare';repository='y805939188/pokemon-essentials-clean-room';branch='codex/remediation-sixth-20261014-8ea169f-cloud';base='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
def git(*args):return subprocess.check_output(['git',*args],cwd=repo)
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'r6-fixed-payload-readback','Accept':'application/vnd.github+json'})
 with urllib.request.urlopen(req,timeout=35) as r:return r.read()
def identity(data):return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
remote=git('ls-remote','origin','refs/heads/'+branch).decode().strip();assert remote.split()[0]==a.commit
core_tree=git('rev-parse',a.commit+'^{tree}').decode().strip();package_tree=git('rev-parse',a.commit+':'+prefix).decode().strip()
commit_api=json.loads(get('https://api.github.com/repos/'+repository+'/git/commits/'+a.commit));assert commit_api['sha']==a.commit and commit_api['tree']['sha']==core_tree
api_bytes=get('https://api.github.com/repos/'+repository+'/git/trees/'+package_tree+'?recursive=1');api=json.loads(api_bytes);assert not api['truncated'] and api['sha']==package_tree
(out/(a.label+'.remote-package-tree.json')).write_bytes(api_bytes)
api_rows={x['path']:x for x in api['tree']};children={}
for path,row in api_rows.items():
 parent=path.rpartition('/')[0];children.setdefault(parent,[]).append((path.rpartition('/')[2],row))
for parent,items in sorted(children.items(),key=lambda x:x[0].count('/'),reverse=True):
 data=b''
 for name,row in sorted(items,key=lambda x:x[0].encode()+ (b'/' if x[1]['type']=='tree' else b'')):
  data+=row['mode'].lstrip('0').encode()+b' '+name.encode()+b'\0'+bytes.fromhex(row['sha'])
 actual=hashlib.sha1(b'tree '+str(len(data)).encode()+b'\0'+data).hexdigest()
 expected=package_tree if parent=='' else api_rows[parent]['sha'];assert actual==expected,(parent,actual,expected)
local={}
for line in git('ls-tree','-rz',a.commit,'--',prefix).split(b'\0'):
 if not line:continue
 meta,path=line.split(b'\t',1);mode,kind,blob=meta.decode().split();path=path.decode();relative=path[len(prefix)+1:]
 row=api_rows[relative];assert (mode,kind,blob)==(row['mode'],row['type'],row['sha'])
 data=git('cat-file','blob',a.commit+':'+path);local[path]={'path':path,'mode':mode,'type':kind,**identity(data)}
changed=set(git('diff-tree','--no-commit-id','--name-only','-r',base,a.commit).decode().splitlines());assert changed==set(local)
if a.label=='final':
 prior=json.loads((out/'core-readback.json').read_text());prior_rows={x['path']:x for x in prior['entries']};needed=[]
 for path,row in local.items():
  if path in prior_rows:
   assert all(row[k]==prior_rows[path][k] for k in ['mode','type','bytes','sha256','git_blob'])
  else:needed.append(row)
else:needed=list(local.values())
results=[];failures=[]
def fetch(row):
 url='https://raw.githubusercontent.com/'+repository+'/'+a.commit+'/'+urllib.parse.quote(row['path'],safe='/')
 try:
  data=get(url);actual=identity(data);assert all(actual[k]==row[k] for k in actual),(row['path'],actual)
  return {**row,'commit':a.commit,'workspace_tree':core_tree,'package_tree':package_tree,'read_scope':'all bytes','source':'fresh fixed-commit raw remote payload; remote Git tree reconstructed from complete API entries','semantic_PASS':False},None
 except Exception as error:return None,{'path':row['path'],'error':str(error),'commit':a.commit}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
 for i,(row,error) in enumerate(pool.map(fetch,needed),1):
  if error:failures.append(error)
  else:results.append(row)
  if i%50==0:print(json.dumps({'label':a.label,'completed':i,'total':len(needed),'failed':len(failures)}),flush=True)
value={'schema':'r6.cloud.remote-readback.v1','commit':a.commit,'workspace_tree':core_tree,'package_tree':package_tree,'remote_branch_line':remote,'remote_API_tree_native_hashes_reconstructed':True,'path_mode_type_blob_complete_remote_tree_match':True,'started_at':started,'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'new_files_read':len(results),'new_bytes_read':sum(x['bytes'] for x in results),'fresh_readback_needed':len(needed),'unchanged_core_payloads_reused_from_exact_prior_remote_receipt':len(local)-len(needed),'all_new_full_bytes_match':not failures,'failures':failures,'entries':results,'new_reference_execution':0,'new_semantic_PASS':False,'required_closed':0}
(out/(a.label+'-readback.json')).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in value.items() if k not in ['entries','failures']},ensure_ascii=False),flush=True)
if failures:print(json.dumps(failures,ensure_ascii=False),flush=True);raise SystemExit(1)
