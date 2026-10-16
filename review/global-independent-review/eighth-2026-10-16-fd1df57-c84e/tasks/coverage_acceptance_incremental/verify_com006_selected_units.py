import json,hashlib,subprocess,datetime,sys,traceback
from pathlib import Path
OWN=Path(__file__).resolve().parent
out=OWN/'com006-own-fixed-git-selected-units.json'
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
operations=[]
def run(args,repo):
 p=subprocess.run(args,cwd=repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 operations.append({'argv':args,'cwd':repo,'exit':p.returncode,'stdout_bytes':len(p.stdout),'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr':p.stderr.decode('utf8','replace')})
 if p.returncode:raise RuntimeError(str(operations[-1]))
 return p.stdout
try:
 src=OWN/'delta-inputs/root-COM006-developer-0807/00-root-com006-counterreview.json'
 raw=src.read_bytes();j=json.loads(raw);units=[]
 def walk(v,ptr=''):
  if isinstance(v,dict):
   if all(k in v for k in ('path','range','content','bytes','sha256','git_blob')) and isinstance(v['content'],str):units.append((ptr,v))
   for k,x in v.items():walk(x,ptr+'/'+str(k))
  elif isinstance(v,list):
   for i,x in enumerate(v):walk(x,ptr+'/'+str(i))
 walk(j)
 checked=[]
 for ptr,u in units:
  p=u['path'];repo=u.get('repo')
  if not repo:repo='/workspace/pokemon-essentials-clean-room' if '/pokemon-essentials-clean-room/' in p or p.startswith('deliverables/') else '/workspace/pokemon-essentials'
  if p.startswith(repo+'/'):p=p[len(repo)+1:]
  commit='fd1df570cad987dc3852a3b958f03916e317f7fe' if repo.endswith('clean-room') else '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
  body=run(['git','show',commit+':'+p],repo)
  blob=run(['git','rev-parse',commit+':'+p],repo).decode().strip()
  a,b=u['range'];selected=b''.join(body.splitlines(keepends=True)[a-1:b]);provided=u['content'].encode()
  assert len(body)==u['bytes'] and hashlib.sha256(body).hexdigest()==u['sha256'] and blob==u['git_blob'],ptr
  exact=selected==provided
  terminal_only=selected.rstrip(b'\n')==provided.rstrip(b'\n')
  assert exact or terminal_only,ptr
  checked.append({'pointer':ptr,'repo':repo,'commit':commit,'path':p,'range':[a,b],'full_file_bytes':len(body),'full_file_sha256':hashlib.sha256(body).hexdigest(),'git_blob':blob,'selected_bytes':len(selected),'selected_sha256':hashlib.sha256(selected).hexdigest(),'embedded_bytes':len(provided),'selected_exact':exact,'only_terminal_LF_difference':not exact and terminal_only,'full_source_file_credit':False})
 proof={'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0,'counter_source_bytes':len(raw),'counter_source_sha256':hashlib.sha256(raw).hexdigest(),'checks':checked,'operations':operations,'semantic_basis':'All embedded content and all remaining fields actually read in five complete expanded-view windows; this process only verifies exact fixed identities and selected units. No target execution.','business':'NOT_EXECUTED','full_source_file_credit':0}
 out.write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'proof':str(out),'exit':0,'selected_units':len(checked),'unique_paths':len(set((x['repo'],x['path']) for x in checked)),'all_fixed_identity_and_content_match':True,'actual_utc':proof['end_utc']},ensure_ascii=False))
except Exception as e:
 proof={'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':1,'error':repr(e),'operations':operations}
 out.write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n');traceback.print_exc();sys.exit(1)
