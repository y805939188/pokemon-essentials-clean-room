"""Selective authorized review publication and fixed-commit remote byte readback."""
from pathlib import Path
import json,subprocess,hashlib,tempfile,datetime,sys,urllib.request,urllib.parse
OUT=Path(__file__).resolve().parent
REPO=OUT.parents[2]
BRANCH='codex/review-third-20261012-86b4d7e-a731'
REMOTE='https://github.com/y805939188/pokemon-essentials-clean-room.git'
mode=sys.argv[1]
def run(*args,cwd=REPO):return subprocess.check_output(list(args),cwd=cwd,stderr=subprocess.STDOUT).decode().strip()
def paths():return sorted(str(p.relative_to(REPO)) for p in OUT.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
prefix=str(OUT.relative_to(REPO))+'/'
if run('git','rev-parse','--abbrev-ref','HEAD')!=BRANCH:raise SystemExit('Unexpected local branch; preserve and abort')
if run('git','rev-parse','main')!='86b4d7e1d8645e75af91a215240f8786a5bb4ca8':raise SystemExit('main changed; preserve and report')
before=run('git','diff','--cached','--name-only').splitlines()
if any(not p.startswith(prefix) for p in before):raise SystemExit('Unknown staged changes; preserve and abort')
selected=paths()
subprocess.check_call(['git','add','--',*selected],cwd=REPO)
staged=run('git','diff','--cached','--name-only').splitlines()
if any(p not in selected or not p.startswith(prefix) for p in staged):raise SystemExit('Selective staged scope invalid; preserve index')
if staged:
 run('git','commit','--quiet','-m',{'snapshot':'docs: freeze independent third review reports and handoff manifest','handoff':'docs: publish complete third update handoff from verified snapshot','final':'docs: record verified handoff publication and review completion'}[mode])
head=run('git','rev-parse','HEAD');tree=run('git','rev-parse','HEAD^{tree}')
print(json.dumps({'mode':mode,'committed_HEAD':head,'tree':tree,'selected_files':len(selected),'staged_files':len(staged)},ensure_ascii=False),flush=True)
push=run('git','push','-u','origin','HEAD:refs/heads/'+BRANCH)
live=run('git','ls-remote','origin','refs/heads/'+BRANCH,'refs/heads/main')
refs={line.split('\t')[1]:line.split('\t')[0] for line in live.splitlines()}
if refs.get('refs/heads/'+BRANCH)!=head:raise SystemExit('Remote branch readback mismatch')
if refs.get('refs/heads/main')!='86b4d7e1d8645e75af91a215240f8786a5bb4ca8':raise SystemExit('Remote main changed externally; record exact state')
tmp=Path(tempfile.mkdtemp(prefix='gr3-remote-readback-'))
run('git','init','--bare','--quiet',str(tmp))
run('git','fetch','--quiet','--depth=1',REMOTE,head,cwd=tmp)
remote_tree=run('git','rev-parse',head+'^{tree}',cwd=tmp)
if remote_tree!=tree:raise SystemExit('Actual fetched remote commit tree mismatch')
raw=subprocess.check_output(['git','ls-tree','-r','-z',head],cwd=tmp)
entries={}
for item in raw.split(b'\0'):
 if not item:continue
 meta,path=item.split(b'\t',1);entries[path.decode()]=meta.decode().split()[-1]
records=[]
for p in selected:
 blob=entries[p];body=subprocess.check_output(['git','cat-file','blob',blob],cwd=tmp)
 local=(REPO/p).read_bytes();sha=hashlib.sha256(body).hexdigest()
 ok=body==local
 records.append({'path':p,'git_blob':blob,'bytes':len(body),'sha256':sha,'matches_frozen_local_bytes':ok,'url':'https://github.com/y805939188/pokemon-essentials-clean-room/blob/'+head+'/'+p,'raw_url':'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+head+'/'+p})
 if not ok:raise SystemExit('Remote bytes mismatch '+p)
http=[]
for name in ['final-report.md','findings.json','cloud-third-update-handoff-manifest.json','cloud-third-update-handoff-prompt.md']:
 target=OUT/name
 if not target.exists():continue
 path=str(target.relative_to(REPO));url='https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/'+head+'/'+urllib.parse.quote(path,safe='/')
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Codex-third-review-readback'}),timeout=30) as r:body=r.read()
  http.append({'path':path,'url':url,'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest(),'matches_local':body==target.read_bytes()})
 except Exception as e:http.append({'path':path,'url':url,'matches_local':False,'error':str(e),'git_body_verified':True})
receipt={'kind':'ACTUAL_FIXED_REVIEW_PUBLICATION_READBACK','mode':mode,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'published' if all(x['matches_local'] for x in http) else 'partial','repo':'y805939188/pokemon-essentials-clean-room','remote':REMOTE,'ref':'refs/heads/'+BRANCH,'commit':head,'tree':tree,'main_live':refs['refs/heads/main'],'main_not_modified_by_review':True,'push_result':push,'remote_branch_matches':True,'actual_remote_fetched_tree_matches':True,'readback_scope':'Every selected new review artifact body at exact fetched remote commit, bytes+SHA256+blob; additionally necessary report/findings/manifest/prompt actual HTTP raw body verification; not a cached branch assertion','file_count':len(records),'all_files_match':True,'files':records,'http_readback':http,'isolated_readback_git_directory':str(tmp),'temporary_cleanup':'No removal; isolated recoverable readback checkout retained, no old candidates/user files cleaned','formal_source_input_identity':'D/S/R unchanged; publication tree is report identity only','future_update_not_started':True,'self_reference':'Receipt generated after fixed snapshot is verified. Its own later publication commit/hash supplied externally, never recursively embedded.'}
name={'snapshot':'publication-snapshot-receipt.json','handoff':'publication-handoff-receipt.json','final':'publication-final-readback-local.json'}[mode]
receipt_path=tmp/name if mode=='final' else OUT/name
receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'published':mode,'status':receipt['status'],'commit':head,'tree':tree,'all_remote_bodies_match':len(records),'http_matched':sum(x['matches_local'] for x in http),'http_count':len(http),'main':refs['refs/heads/main'],'receipt':str(receipt_path)},ensure_ascii=False),flush=True)
