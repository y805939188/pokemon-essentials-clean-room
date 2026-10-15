import json, hashlib, os, subprocess, datetime, shutil
from pathlib import Path

ROOT = Path('/workspace/r7-ir-R7-U11')
OUT = Path(__file__).resolve().parents[1]
REPO = ROOT/'review-checkout'
B='e646432c644dec04d306842cc5a559a29c718fbc'
MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
FI='13d76ba61838b13925ba9d41f58a6b047564d926'
def git(*a): return subprocess.check_output(['git',*a],cwd=REPO)
def ident(b): return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_content_id':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def dump(name,x): (OUT/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def check(b,r):
 a=ident(b)
 for k,v in a.items():
  expected=r.get(k,r.get('git_blob') if k=='git_blob_content_id' else None)
  if expected is not None: assert v==expected,(k,v,expected)
 return a
pins={}
for c in [B,MI,FI,'c64774c60d91e522cb515ef71e3e9d4ea6b4712c','f151a507bb43e8c936845c7408ab4bc14138caf0','4467147f9f2e184dba6f61d9fb2699738f365571']:
 pins[c]=git('rev-parse',c+'^{tree}').decode().strip()
assert pins[MI]=='6480ffe3df49bd9776c719f3c9be1c13618fdb0a'
assert pins[FI]=='6747a584b91c86acd4771c1a6dee93260602106f'
assert git('rev-parse',B+':deliverables/final-specification-set').decode().strip()=='ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
assert git('rev-parse',MI+':deliverables/final-specification-set').decode().strip()=='8403869aaeb4726518414b409b3808c3c0780e65'
fi_b=git('show',FI+':review/remediation-seventh-20261015-prepare/integration/wave2/v1/integrated-input.json')
fi=json.loads(fi_b);dump('fixed-integrated-input.json',fi)
allrows=[]
for which,dest in [('original-plans','original'),('actual-plans','actual-input')]:
 pb=(ROOT/which/'R7-U11.json').read_bytes();p=json.loads(pb)
 if which=='actual-plans': assert ident(pb)['sha256']=='5976c6bed653716222bbd683d1dc68199849b98aa322c98c1367c89082d9f0b4'
 rows=p['artifacts']+p['evidence']+p['fixed_read_inputs']
 verified=[]
 for row in rows:
  a=check((ROOT/dest/row['local_path']).read_bytes(),row)
  if row['repository']=='y805939188/pokemon-essentials-clean-room' and row not in p['evidence']:
   assert git('show',row['commit']+':'+row['path'])==(ROOT/dest/row['local_path']).read_bytes()
  verified.append({'local_path':row['local_path'],'commit':row['commit'],'path':row['path'],**a})
 allrows.append({'plan':str(ROOT/which/'R7-U11.json'),'plan_identity':ident(pb),'files':verified,'count':len(verified),'decoded_bytes':sum(r['bytes'] for r in verified)})
 for pth in (ROOT/dest).glob('recovery-receipt-*.json'):
  shutil.copyfile(pth,OUT/(dest+'-'+pth.name))
formal=[]
for row in fi['all_formal_file_identities']:
 b=git('show',MI+':'+row['path']);bb=git('show',B+':'+row['path'])
 a=check(b,row);check(bb,row['base_B_identity']);assert (b!=bb)==row['changed_against_B']
 formal.append({'path':row['path'],**a,'changed_against_B':b!=bb})
assert len(formal)==131
assert sum(r['changed_against_B'] for r in formal)==26
prior=[]
for p in (ROOT/'actual-input/prior-accepted/actual-at-accepted-MI').rglob('*.md'):
 rel=p.relative_to(ROOT/'actual-input/prior-accepted/actual-at-accepted-MI').as_posix()
 assert p.read_bytes()==git('show',MI+':'+rel)
 prior.append({'path':rel,**ident(p.read_bytes()),'qualification':'Exact preservation only; no new semantic PASS.'})
skills={c:git('ls-tree','-r','--name-only',c,'--','.agents','.codex').decode().splitlines() for c in [B,MI,FI]}
skills['workspace_agents_entries']=sorted(x.name for x in Path('/workspace/.agents').iterdir())
dump('input-byte-audit.json',{'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'fixed_B_formal_tree':'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c','MI_formal_tree':'8403869aaeb4726518414b409b3808c3c0780e65','restores':allrows,'formal_131':formal,'prior_accepted_five':prior,'skills':skills,'semantic_credit':False})
print(json.dumps({'restore_counts':[r['count'] for r in allrows],'restore_bytes':[r['decoded_bytes'] for r in allrows],'formal_count':len(formal),'formal_changed':26,'formal_unchanged':105,'prior_preserved':len(prior),'thread_id':os.environ.get('CODEX_THREAD_ID'),'skills':skills},ensure_ascii=False))
