import pathlib,subprocess,json,hashlib,datetime,collections,shutil,os
P=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
W=pathlib.Path('/Users/dingshinn/.codex/worktrees/review-fourth-1f36475/pokemon-framework-reference')
O=W/'review/global-independent-review/fourth-2026-10-12-1f36475-c92e'
R=P/'reference/pokemon-essentials'
B='1f36475d22120a0d1175967d5b17d71fe8311d88'
def run(args,cwd=P):
 p=subprocess.run(args,cwd=cwd,capture_output=True);return {'command':args,'exit_code':p.returncode,'stdout':p.stdout.decode(errors='replace'),'stderr':p.stderr.decode(errors='replace')}
def git(*a,cwd=P):return subprocess.check_output(['git',*a],cwd=cwd)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
def save(name,x): (O/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def inventory(root,tracked):
 out=[]
 for p in sorted(root.rglob('*')):
  if '.git' in p.relative_to(root).parts or not p.is_file():continue
  rel=str(p.relative_to(root));out.append({'path':rel,'tracked':rel in tracked,**ident(p.read_bytes())})
 return out
formal=json.loads(git('show',B+':delivery/2026-10-12/formal-identities.json'))['records']
checks=[]
for q in formal:
 path=q['path']; b=git('show',B+':'+path); exp=q['accepted_bytes'];actual=ident(b)
 checks.append({'path':path,**actual,'expected':exp,'baseline_matches':all(actual[k]==exp[k] for k in actual),'main_working_matches':(P/path).read_bytes()==b,'isolated_working_matches':(W/path).read_bytes()==b})
save('evidence/formal-identity-check.json',checks)
tracked=git('ls-files','-z',cwd=R).decode().strip('\0').split('\0')
ref=inventory(R,set(tracked))
for q in ref:
 if q['tracked']:
  b=git('show','HEAD:'+q['path'],cwd=R);q['tracked_bytes_match']=ident(b)=={k:q[k] for k in ['bytes','sha256','git_blob']}
save('evidence/reference-inventory.json',ref)
untracked=git('ls-files','--others','--exclude-standard','-z').decode().strip('\0').split('\0')
protected=[{'path':p,**ident((P/p).read_bytes())} for p in untracked if p and (P/p).is_file()]
save('evidence/protected-untracked.json',protected)
ignored=git('ls-files','--others','--ignored','--exclude-standard','--directory','-z').decode().strip('\0').split('\0')
protection={'tracked_diff':run(['git','diff','--name-status']),'staged_diff':run(['git','diff','--cached','--name-status']),'index_tree':git('write-tree').decode().strip(),'stash_refs':git('stash','list','--format=%H').decode().splitlines(),'untracked_file_count':len(protected),'ignored_paths':[x for x in ignored if x],'worktrees':git('worktree','list','--porcelain').decode(),'main_branch':git('branch','--show-current').decode().strip(),'head':git('rev-parse','HEAD').decode().strip(),'protection_rule':'Do not modify, reset, clean, stash, rename, delete or stage original content. Only new review directory is writable.'}
save('evidence/workspace-protection-before.json',protection)
nav={}
for name in ['CURRENT-DELIVERY.md','delivery/2026-10-12/README.md','delivery/2026-10-12/current-status.json','delivery/2026-10-12/formal-identities.json','delivery/2026-10-12/evidence-navigation.json','delivery/2026-10-12/cleanup-report.md','delivery/2026-10-12/archive-and-retirement-inventory.json']:
 b=git('show',B+':'+name);nav[name]=ident(b)
base={'schema_version':'1.0','observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repository_root':str(P),'repository':'y805939188/pokemon-essentials-clean-room','remote':git('remote','get-url','origin').decode().strip(),'branch':git('branch','--show-current').decode().strip(),'refs':{n:git('rev-parse',n).decode().strip() for n in ['HEAD','main','origin/main','delivery/third-round-clean-20261012']},'formal_baseline':{'commit':B,'tree':git('rev-parse',B+'^{tree}').decode().strip()},'remote_observation':run(['git','ls-remote','origin','refs/heads/main','refs/tags/delivery/third-round-clean-20261012']),'review_workspace':str(W),'review_branch':git('branch','--show-current',cwd=W).decode().strip(),'readiness':'PARTIAL_READY','formal_identity':{'count':len(checks),'all_match':all(x['baseline_matches'] and x['main_working_matches'] and x['isolated_working_matches'] for x in checks)},'navigation_identities':nav,'reference_baseline':{'path':str(R),'form':'Independent nested Git repository, absent from parent Git tree; read-only','commit':git('rev-parse','HEAD',cwd=R).decode().strip(),'tree':git('rev-parse','HEAD^{tree}',cwd=R).decode().strip(),'remote':git('remote','get-url','origin',cwd=R).decode().strip(),'status':run(['git','status','--porcelain=v1'],R),'tracked_count':len(tracked),'tracked_bytes_match':all(x.get('tracked_bytes_match',True) for x in ref),'total_non_git_files':len(ref),'overlay':[x for x in ref if not x['tracked']],'top_level_counts':dict(collections.Counter(x['path'].split('/')[0] for x in ref))},'tools':{x:run([x,'--version']) for x in ['git','python3','ruby','codex']},'host_programs':{x:shutil.which(x) for x in ['wine','wine64','mkxp','mkxp-z']},'material_limits':['No Graphics or Audio directories, map files or complete Demo database in reference directory.','Root knownpoint.bmp and selpoint.bmp are present; their current identities are in reference inventory.','Scripts.rxdata and messages_core.dat exist; presence does not establish parseability or playability.','Windows executables and bundled DLLs exist; no Wine/mkxp executable on PATH. Ruby 2.6.10 available for isolated selected pure paths; no execution claim yet.'],'review_model_request':{'model':'gpt-6-astra','reasoning_effort':'ultra','service_tier':'default','fast':False,'main_request_source':'user instruction for current chat','actual_echo':'UNVERIFIED','built_in_agent_interface':'Only priority advertised; will not silently use priority. CLI per-invocation explicit parameter request is planned; no global configuration changes.'},'behavior_execution':'NOT_EXECUTED'}
save('baseline.json',base)
print(json.dumps({'readiness':base['readiness'],'formal':base['formal_identity'],'reference':{k:base['reference_baseline'][k] for k in ['commit','tree','tracked_count','tracked_bytes_match','total_non_git_files']},'protected_untracked':len(protected),'overlay':[x['path'] for x in base['reference_baseline']['overlay']]},ensure_ascii=False))
