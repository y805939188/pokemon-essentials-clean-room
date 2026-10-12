import pathlib,subprocess,json,hashlib,datetime,sys
r=pathlib.Path(__file__).resolve().parent.parent
P=pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference');W=r.parents[2];R=P/'reference/pokemon-essentials';B='1f36475d22120a0d1175967d5b17d71fe8311d88'
def run(a,cwd=P):
 p=subprocess.run(a,cwd=cwd,capture_output=True,text=True);return {'command':a,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
def git(*a,cwd=P):return subprocess.check_output(['git',*a],cwd=cwd,text=True).strip()
errors=[];before=json.loads((r/'evidence/workspace-protection-before.json').read_text())
for name,cmd in [('tracked',['git','diff','--name-status']),('staged',['git','diff','--cached','--name-status'])]:
 o=run(cmd)
 if o['exit_code'] or o['stdout']:errors.append('main '+name+' changed')
for x in json.loads((r/'evidence/protected-untracked.json').read_text()):
 p=P/x['path']
 if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=x['sha256']:errors.append('protected untracked '+x['path'])
for x in json.loads((r/'evidence/reference-inventory.json').read_text()):
 p=R/x['path']
 if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=x['sha256']:errors.append('reference '+x['path'])
for x in json.loads((r/'evidence/formal-identity-check.json').read_text()):
 for base in [P,W]:
  p=base/x['path']
  if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=x['sha256']:errors.append('formal '+str(p))
if git('stash','list','--format=%H').splitlines()!=before['stash_refs']:errors.append('stash changed')
head=git('rev-parse','HEAD');branch=git('branch','--show-current')
if head!=before['head'] or branch!=before['main_branch']:errors.append('original checkout identity changed')
rs=run(['git','status','--porcelain=v1'],R)
if rs['stdout'] or rs['exit_code']:errors.append('reference tracked/untracked status changed')
branchdiff=run(['git','diff','--name-only',B],W)
if branchdiff['stdout']:
 for p in branchdiff['stdout'].splitlines():
  if not p.startswith('review/global-independent-review/fourth-2026-10-12-1f36475-c92e/'):errors.append('outside authorized report '+p)
out={'schema_version':'1.0','evidence_level':'TOOL_VALIDATION','status':'PASS' if not errors else 'FAIL','observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':['python3','evidence/check-protection.py'],'python':sys.version,'main_head':head,'main_branch':branch,'main_ref':git('rev-parse','main'),'origin_main_local_ref':git('rev-parse','origin/main'),'reference_head':git('rev-parse','HEAD',cwd=R),'reference_tree':git('rev-parse','HEAD^{tree}',cwd=R),'reference_status':rs,'formal131_original_and_isolated_bytes_unchanged':not any(e.startswith('formal ') for e in errors),'reference434_all_non_git_file_bytes_unchanged':not any(e.startswith('reference ') for e in errors),'protected_untracked62_unchanged':not any(e.startswith('protected untracked') for e in errors),'stash_unchanged':'stash changed' not in errors,'other_worktrees':'Listed before; no writes/checkout/cleanup issued against them. No claim of byte-rehashing their entire contents.','main_ignored_content':'Preserved by no write operations. Only R non-Git files have full before/after byte checks; do not infer rehash of all unrelated ignored files.','report_branch_diff_scope':branchdiff,'remote_main_and_tag':run(['git','ls-remote','origin','refs/heads/main','refs/tags/delivery/third-round-clean-20261012']),'errors':errors,'side_effects':'Only this new review receipt; read-only source/formal/protected inputs','exit_code':0 if not errors else 1}
name=sys.argv[1] if len(sys.argv)>1 else 'protection-before-publication.json';(r/'evidence'/name).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['status','main_head','formal131_original_and_isolated_bytes_unchanged','reference434_all_non_git_file_bytes_unchanged','protected_untracked62_unchanged','errors']},ensure_ascii=False));sys.exit(out['exit_code'])
