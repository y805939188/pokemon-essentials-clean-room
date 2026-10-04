"""Metadata/document regression checks, no reference import or behavior execution.
Run from the author repository root, using the exact detached reference:
python review/remediation/20261003-prepare/batches/B04/author-round-2/self-check.py --reference PATH
"""
from pathlib import Path
import argparse,csv,hashlib,json,re,subprocess,collections
BASE='6452c0e03025605222f3de9a272221e2b82eeda4'
PREV='da6daba7d6c6365d4578d7173a6d8316acae8bb8'
REVIEW='f0d89a0989cf16d7ea2592fdf75a968b553caefa'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
PREFIX='review/remediation/20261003-prepare/batches/B04/'
OUT=Path(PREFIX+'author-round-2')
p=argparse.ArgumentParser();p.add_argument('--reference',type=Path,required=True);args=p.parse_args()
def git(*a):return subprocess.check_output(['git',*a])
def sha(b):return hashlib.sha256(b).hexdigest()
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def doc(name):return json.loads((OUT/name).read_text())
checks=[]
def check(name,condition,details=None):
 if not condition:raise AssertionError((name,details))
 checks.append(dict(name=name,details=details))
def match(b,row):return len(b)==row['bytes'] and sha(b)==row['sha256'] and blob(b)==row['git_blob']
check('branch',git('branch','--show-current').decode().strip()=='remediation/20261003-prepare/batch-B04')
check('first handoff ancestor',subprocess.run(['git','merge-base','--is-ancestor',PREV,'HEAD']).returncode==0)
auth=doc('authorization-and-limits.json');allowed=set(auth['allowed_changed_formal_paths'])
changed=set(git('diff','--name-only',PREV).decode().splitlines());untracked=set(git('ls-files','--others','--exclude-standard').decode().splitlines())
check('six formal deltas only',{x for x in changed if not x.startswith(PREFIX)}==allowed and len(allowed)==6)
check('no original round1/report/public/plan/history writes',all(x in allowed or x.startswith(PREFIX+'author-round-2/') or x.startswith(PREFIX+'freeze-stage-2/') for x in changed|untracked))
check('no Ruby/reference/ignore payload',not any(x.endswith('.rb') or x.startswith('reference/') or x.endswith('.gitignore') for x in changed|untracked))
for old in git('ls-tree','-r','--name-only',PREV,PREFIX+'author-round-1',PREFIX+'freeze-stage-1').decode().splitlines():
 check('historical bytes '+old,Path(old).read_bytes()==git('show',PREV+':'+old))

gate=json.loads(Path(PREFIX+'author-round-1/read-freeze-gate.json').read_text())
for row in gate['identities_checked']:
 b=git('show',row['commit']+':'+row['path']);check('fixed input '+row['path'],len(b)==row['bytes'] and sha(b)==row['sha256'] and blob(b)==row['blob'])
check('planned74/identity103',gate['planned_reads']==74 and len(gate['identities_checked'])==103)
handshake=json.loads(git('show',BASE+':review/remediation/20261003-prepare/batches/B06/acceptance-stage-1/downstream-handshake.json'))
controls=json.loads(Path(PREFIX+'author-round-1/finding-controls.json').read_text())
for row in handshake['B04']['contribution_controls']:
 for key in ['original','acceptance']:
  b=json.dumps(controls[row['id']][key],ensure_ascii=False,sort_keys=True,separators=(',',':')).encode();check('original/acceptance '+row['id']+' '+key,sha(b)==row[key+'_object_sha256'])
check('35 full controls/23 primary',len(controls)==35 and len(handshake['B04']['primary_finding_ids'])==23)
report=doc('review-input-bindings.json')
for row in report['artifact_identities']:check('report artifact '+row['path'],match(git('show',REVIEW+':'+row['path']),row))
check('full report parent equals old handoff',git('show','-s','--format=%P',REVIEW).decode().strip()==PREV)
check('two existing roots no double count',{r['id'] for r in report['two_complete_observations']}=={'R-B04-1-001','R-B04-1-002'} and doc('review-observation-responses.json')['new_canonical_ids']==0)

artifacts=doc('formal-artifact-identities.json')['files']
for row in artifacts:
 check('formal previous '+row['path'],match(git('show',PREV+':'+row['path']),row['previous']))
 check('formal candidate '+row['path'],match(Path(row['path']).read_bytes(),row['candidate']))
 if not row['changed']:check('seven other formal bytes '+row['path'],row['previous']==row['candidate'])
check('formal delta exact',(OUT/'formal-delta.diff').read_bytes()==git('diff','--full-index','--unified=0',PREV,'--',*auth['allowed_changed_formal_paths']))
for r in doc('original-sync-ledger.json')['entries']:
 if r['changed']:check('original delta '+r['original'],Path(r['diff']['path']).read_bytes()==git('diff','--full-index','--unified=0',PREV,'--',r['original']))
 else:check('three original mirrors untouched '+r['original'],Path(r['original']).read_bytes()==git('show',PREV+':'+r['original']))

row_re=re.compile(r'^\| ([A-Z][A-Z0-9-]*) \|')
def rows(text):return [x for x in text.splitlines() if row_re.match(x) and not x.startswith('| ID |')]
exceptions={'engine-overworld-wp11-15-59-60.md':{'B04-R13','B04-R14'},'engine-overworld-wp16.md':{'B04-W01'},'user-interface-wp17-63-65-66-67-68-69-70-71.md':set()}
new=[]
for r in artifacts:
 path=r['path']
 if '/test-catalog/' not in path:continue
 old=rows(git('show',PREV+':'+path).decode());current=rows(Path(path).read_text());ids=[row_re.match(x)[1] for x in old];omit=exceptions[Path(path).name]
 protected=[x for x in old if row_re.match(x)[1] not in omit];after=[x for x in current if row_re.match(x)[1] in set(ids) and row_re.match(x)[1] not in omit]
 check('other catalog rows bytes/order/multiplicity '+path,protected==after,dict(protected_rows=len(protected)))
 check('existing IDs retained '+path,set(ids)<=set(row_re.match(x)[1] for x in current))
 for x in current:
  tid=row_re.match(x)[1]
  if tid not in set(ids):new.append(tid)
  if tid not in set(ids) or tid in omit:check('changed/new row has three cells '+tid,len(re.split(r'(?<!\\)\|',x))==5)
check('three new rows',len(new)==3 and set(new)=={'B04-W24','B04-R27','B04-R28'})

responses=doc('finding-responses.json')['responses'];check('35 current response identities',set(x['id'] for x in responses)==set(controls) and len(responses)==35)
for row in responses:
 check('candidate not approved '+row['id'],row['state']=='AUTHOR_ROUND2_CANDIDATE_UNREVIEWED' and row['canonical_state']=='OPEN' and not row['new_approval'])
 for r in row['clauses']:check('current clause locator '+row['id']+' '+r['section'],Path(r['path']).read_text().splitlines()[r['line']-1].lstrip('# ')==r['heading'])
 for r in row['static_designs']:check('current static design locator '+r['id'],Path(r['path']).read_text().splitlines()[r['line']-1]==r['fixture_and_expected'])

# Existing body regions outside the two clauses stay byte-identical. Boundaries
# are document headings, never inferred behavioral execution or model results.
def split_resource(text):return text.split('### 5.1 位图访问的分入口失败',1)
for path in [p for p in allowed if 'wp15-resource' in p]:
 before=git('show',PREV+':'+path).decode();now=Path(path).read_text();pre_old,body_old=split_resource(before);pre_now,body_now=split_resource(now)
 if path.startswith('specs/'):pre_now='\n'.join(x for x in pre_now.split('\n') if not x.startswith('> B04 第二轮候选'))
 check('WP15 outside failure clause '+path,pre_now==pre_old and body_now.split('\n## 6.',1)[1]==body_old.split('\n## 6.',1)[1])
for path in [p for p in allowed if 'wp16-world' in p]:
 before=git('show',PREV+':'+path).decode();now=Path(path).read_text();now=re.sub(r'### 3\.2\.1 容量折叠的条件播放边界\n.*?(?=### 3\.3 色调与颜色叠加)','',now,flags=re.S)
 now=now.replace('中间展开图可能按纹理容量分两列，不改变源帧数；条件播放计数和请求分叉另见§3.2.1，不能由源帧数一概推出播放循环。','中间展开图可能按纹理容量分两列，不改变源帧数。')
 if path.startswith('specs/'):now='\n'.join(x for x in now.split('\n') if not x.startswith('> B04 第二轮候选'))
 check('WP16 all other prose/data unchanged '+path,now==before)

for key,expected in [('B04_to_B07',2),('B04_to_B06',3)]:
 readers=doc('interface-handoff.json')[key]['changed_readers'];check('five dependency readers '+key,len(readers)==5 and sum(x['changed_since_round1'] for x in readers)==expected)
 for r in readers:check('dependency candidate identity '+r['path'],match(Path(r['path']).read_bytes(),r))
for p in ['deliverables/final-specification-set/creature-rpg/wp24-player-trainers-partners.md','deliverables/final-specification-set/engine-overworld/wp13-map-events-npc-followers.md','deliverables/final-specification-set/creature-rpg/wp28-item-use-and-training.md','deliverables/final-specification-set/creature-rpg/wp30-growth-learning-and-friendship.md']:
 check('accepted dependency unchanged '+p,Path(p).read_bytes()==git('show',BASE+':'+p))
check('zero execution/closures/new roots and actual config unverified',all(auth[k]==0 for k in ['runtime_observations','proven_demo_chains','vector_executions','reference_execution','canonical_closed','new_canonical_ids']) and auth['canonical_required_open']==229 and auth['effective_configuration']=='UNVERIFIED')

ref=args.reference.resolve()
check('reference commit and clean',subprocess.check_output(['git','-C',str(ref),'rev-parse','HEAD']).decode().strip()==REF and not subprocess.check_output(['git','-C',str(ref),'status','--porcelain']))
data_cache={}
for log in [Path(PREFIX+'author-round-1/source-reading-log.tsv'),OUT/'source-reading-log.tsv']:
 for r in csv.DictReader(log.open(),delimiter='\t'):
  path=r['path']
  if path not in data_cache:
   data=(ref/path).read_bytes();check('reference fixed bytes '+path,data==subprocess.check_output(['git','-C',str(ref),'show',REF+':'+path]));data_cache[path]=data
  data=data_cache[path];lines=data.splitlines(keepends=True);a,b=int(r['first']),int(r['last']);check('source bounds '+path,r['commit']==REF and 1<=a<=b<=len(lines) and len(lines)==int(r['actual_lines']))
  check('source full and range hash '+path,sha(data)==r['full_sha256'] and blob(data)==r['full_blob'] and sha(b''.join(lines[a-1:b]))==r['range_sha256'])
for directory,commit in [('/workspace/pokemon-essentials-clean-room','e1e01bb18d824931e54f182dd61af5a9f908ba85')]:
 check('main workspace unchanged',subprocess.check_output(['git','-C',directory,'rev-parse','HEAD']).decode().strip()==commit and not subprocess.check_output(['git','-C',directory,'status','--porcelain']))
check('diff whitespace',subprocess.run(['git','diff','--check',PREV],capture_output=True).returncode==0)
print(json.dumps(dict(state='AUTHOR_DOCUMENT_IDENTITY_REGRESSION_CHECKS_COMPLETED',independent_approval=False,check_count=len(checks),checks=checks,reference_execution=0,vector_executions=0,model_effective='UNVERIFIED'),ensure_ascii=False,indent=2))
