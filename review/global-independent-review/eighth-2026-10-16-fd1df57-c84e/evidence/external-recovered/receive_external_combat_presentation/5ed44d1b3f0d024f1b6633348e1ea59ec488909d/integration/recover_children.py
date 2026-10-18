"""Materialize exact received child contributions, inert. Never run their scripts."""
from pathlib import Path
import json,subprocess,hashlib,datetime
I=Path(__file__).resolve().parent;T=I.parent;REPO=Path('/workspace/pokemon-essentials-clean-room');BASE='35d85e4484b892ebc32542346861440638d2183c'
jobs=[('02_ball_base_fields','6211852c0e336a1b9cbfe8ad1a88339bf468ba99','01a1448f-0b8b-7503-bae7-c58207e7e02e'),('05_capture_debug','2449ed418d2989ce23c5fa7e1b701752959e7016','01a1448f-8f07-7153-b52f-dce2884bb01f'),('03_fixed_choreography','352db17277eb3ac7e02df7941b22dab3148d44f1','01a1448f-2c03-7067-b26b-e3b7ae7bc020'),('04_author_player','a19dcfcaba117a746545760e888e224695b1bbe9','01a1448f-6d0a-77fc-93d8-7b9584bf002b'),('06_qualifications_interfaces','eac03270058d839991c437057b3451349b7c6122','01a1448f-4df5-7077-9f61-af423646e00c'),('01_scene_input_objects','138e64befb32256ab17bfbcec6dd01f2f1b8ea81','01a1448e-e922-7356-b21d-4ac7812a5024')]
def git(*args):return subprocess.check_output(['git',*args])
receipts=json.loads((I/'received-identities.json').read_text())['children'] if (I/'received-identities.json').exists() else []
for job,c,context in jobs:
 if any(x['job']==job and x['commit']==c for x in receipts):continue
 prefix=str(T.relative_to(REPO))+'/continuation-results/'+job+'/'
 changed=git('diff','--name-only',BASE,c).decode().splitlines();assert all(p.startswith(prefix)for p in changed)
 checkout=git('rev-parse',c+'^{tree}').decode().strip();tree=git('rev-parse',c+':'+prefix.rstrip('/')).decode().strip()
 dest=I/'received'/job/c;assert not dest.exists();dest.mkdir(parents=True)
 files=[]
 for row in git('ls-tree','-rz',c,'--',prefix).split(b'\0'):
  if not row:continue
  meta,path=row.split(b'\t',1);mode,typ,oid=meta.decode().split();path=path.decode();assert mode=='100644'and typ=='blob';raw=git('cat-file','blob',oid);assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==oid
  rel=path[len(prefix):];p=dest/rel;p.parent.mkdir(exist_ok=True,parents=True);p.write_bytes(raw)
  files.append({'remote_path':path,'relative':rel,'local_path':str(p.relative_to(T)),'mode':mode,'blob':oid,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
 receipts.append({'job':job,'commit':c,'checkout_tree':checkout,'task_tree':tree,'context_parent_supplied':context,'origin_fetch':'ordinary exact commit fetch; see fixed input receipt and actual tool4ac246/8c0de2','expected_trees':'Observed from fixed parent-supplied commit, not separately supplied in dispatch','files':files,'only_child_exclusive_write_set_changed_since_frozen35d85e4':True,'transport_credit':'IDENTITY_ONLY','recovered_code_executed':False})
(I/'received-identities.json').write_text(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'binding_commit':BASE,'children':receipts,'UPDATE_NOT_STARTED':True},ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'job':r['job'],'commit':r['commit'],'tree':r['task_tree'],'files':len(r['files']),'bytes':sum(f['bytes']for f in r['files'])}for r in receipts]))
