#!/usr/bin/env python3
"""Finite byte/structure/regression checks; does not execute R or model AI."""
from pathlib import Path
import sys, subprocess, json, hashlib, re, difflib
ROOT=Path(__file__).resolve().parents[5]
PREP=ROOT/'review/remediation-sixth-20261014-prepare'
EV=Path(__file__).resolve().parent
BASE='469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN='8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
REF='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
RDB='/tmp/r6-u04-reference-objects'
checks=[]
def ck(name,condition,detail=None):
    checks.append({'check':name,'result':'PASS' if condition else 'FAIL','detail':detail})
    if not condition: raise AssertionError(name)
def git(repo,*args): return subprocess.check_output(['git','-C',str(repo),*args])
def blob(repo,c,p): return git(repo,'cat-file','blob',c+':'+p)
def ident(b):return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}
contract=json.loads((PREP/'contracts/R6-U04.json').read_text())
prompt=(PREP/'prompts/R6-U04-A.md').read_bytes()
ck('prompt-fixed-identity',ident(prompt)=={'bytes':221692,'sha256':'f1bc00612214728cdeb5cebd82c71f21f857e329fe6a13d0cf0eacec1ae30974','git_blob':'bc8e0d52dd27bb4c2206aceda153f58cc2517db7'})
embedded=prompt.decode().split('## 本批确定合同')[1].split('```json\n',1)[1].split('\n```',1)[0]
ck('standalone-contract-is-full-read-embedded-contract',embedded==(PREP/'contracts/R6-U04.json').read_text().rstrip('\n'))
ck('fixed-R-tree',git(RDB,'rev-parse',REF+'^{tree}').decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0')
inputs=json.loads((PREP/'inputs/frozen-inputs.json').read_text())
input_ids=[]
for kind,paths in [('source',contract['read_only_reference_paths']),('formal',contract['candidate_formal_paths'])]:
    rows=inputs['source_materials' if kind=='source' else 'formal_materials']
    for p in paths:
        row=next(x for x in rows if x['path']==p)
        b=blob(RDB if kind=='source' else ROOT,REF if kind=='source' else MAIN,p)
        ck('identity:'+kind+':'+p,all(ident(b)[k]==row[k] for k in ident(b)))
        entry=git(RDB if kind=='source' else ROOT,'ls-tree',REF if kind=='source' else MAIN,'--',p).decode().strip()
        ck('mode-and-type:'+kind+':'+p,entry.startswith('100644 blob '))
        input_ids.append({'kind':kind,'path':p,'commit':REF if kind=='source' else MAIN,'entry':entry,**ident(b)})
MIRROR=PREP/'candidates/R6-U04/mirror'
texts={}
removed={}
for p in contract['candidate_formal_paths']:
    old=blob(ROOT,MAIN,p).decode();new=(MIRROR/p).read_text();texts[p]=(old,new)
    ck('prepared-mirror-was-baseline:'+p,blob(ROOT,BASE,str((MIRROR/p).relative_to(ROOT)))==old.encode())
    ck('actual-formal-untouched:'+p,(ROOT/p).read_bytes()==old.encode())
    deletions=[l[2:] for l in difflib.ndiff(old.splitlines(),new.splitlines()) if l.startswith('- ')]
    removed[p]=deletions
    permitted=('MoveFailureCheck：StartSunWeather','| TypeAndPowerDependOnUserBerry |','| HitOncePerUserTeamMember |','示例场景 75 条','- 保留：新 B 中','## BE：','| B16 |')
    ck('only-declared-existing-lines-replaced:'+p,all(l.startswith(permitted) for l in deletions),deletions)
bodypath=next(p for p in texts if 'field-damage' in p)
coverpath=next(p for p in texts if 'effect-coverage' in p)
testpath=next(p for p in texts if '/test-catalog/' in p)
oldbody,body=texts[bodypath];oldcover,cover=texts[coverpath];oldtests,tests=texts[testpath]
ck('exact-deletion-counts',[len(removed[p]) for p in contract['candidate_formal_paths']]==[1,4,2])
# All old test rows remain exact, except B16 gains an explicit prediction premise.
for line in oldtests.splitlines():
    if not line.startswith('| ') or line.startswith('| B16 |'):continue
    ck('existing-test-row-preserved:'+line.split('|')[1].strip()+':'+hashlib.sha256(line.encode()).hexdigest()[:10],line in tests)
ck('B16-output-unchanged',next(l for l in oldtests.splitlines() if l.startswith('| B16 |')).split('|')[3]==next(l for l in tests.splitlines() if l.startswith('| B16 |')).split('|')[3])
ck('AB-AI-AE-content-preserved',oldtests.split('## BE：')[0]==tests.split('## BE：')[0])
ck('CE-content-preserved',oldtests.split('## CE：')[1]==tests.split('## CE：')[1])
be=tests.split('## BE：')[1].split('## CE：')[0]
ids=re.findall(r'^\| (B\d+[a-z]?) \|',be,re.M)
ck('BE-86-unique-rows',len(ids)==86 and len(set(ids))==86,ids)
ck('all-11-new-vectors',all('B'+str(i) in ids for i in range(72,83)))
ck('body-and-catalog-count-agree','示例场景 86 条' in body and '共 86 条' in tests)
# Locator-only coverage repair preserves all data identifiers, copies and scores.
ck('coverage-identifiers-and-copy-order-preserved',re.findall(r'[A-Za-z][A-Za-z0-9_]*',oldcover)==re.findall(r'[A-Za-z][A-Za-z0-9_]*',cover))
ck('coverage-one-line-only',sum(1 for l in difflib.ndiff(oldcover.splitlines(),cover.splitlines()) if l.startswith('- '))==1)
line=next(l for l in cover.splitlines() if l.startswith('MoveFailureCheck：StartSunWeather'))
ck('weather-terrain-retain-5.1','RemoveTerrain（均 §5.1）；AddSpikes' in line)
ck('all-four-hazard-failures-to-5.2','AddSpikesToFoeSide；AddToxicSpikesToFoeSide；AddStealthRocksToFoeSide；AddStickyWebToFoeSide（均 §5.2）' in line)
ck('hazard-behavior-remains-exact',next(l for l in oldbody.splitlines() if l.startswith('撒菱满 3'))==next(l for l in body.splitlines() if l.startswith('撒菱满 3')))
# Explicit source/consumer presence, human conclusions remain SOURCE_STATIC/DERIVED_VECTOR.
ck('beatup-boundary-and-continuation',all(t in body for t in ['围攻空名单的候选评分边界','故 n=0','人数 n 作除法','保留包装外该目标候选初值 100','通用伤害近似仍独立执行']))
ck('naturalgift-missing-versus-readable-item',all(t in body for t in ['自然之恩无当前持物的候选评分边界','未取得正常基数 1 或 0','有当前持物时','低于中等技能']))
ck('diagnostic-return-is-qualified',body.count('诊断器自身失败后继续')==2)
# Literal constant arithmetic only, no behavioural state machine or R execution.
ck('constant-B16-27',(5+100//10)+(5+75//10)==27)
ck('constant-B74-P15-and-break-limit0',5+100//10==15 and 123*(1-1)//1==0)
ck('constant-GR015-old-new-table', [16,8,4,3,2][min(5,4)]==2 and [24,8,2,1][min(5,3)]==1 and 100+15==115)
ck('constant-life-dew-107-95',100+15*50//100==107 and 100-5==95)
item=blob(RDB,REF,'PBS/items.txt').decode()
oran=item.split('[ORANBERRY]')[1].split('#-------------------------------')[0]
ck('B79-default-ORAN-full-value','NaturalGift_POISON_80' in oran and 'Berry' in oran)
# Shared interfaces remain the fixed accepted baseline, no hidden edits.
interfaces=['combat-requirements/wp51-ai-action-selection-and-skill.md','combat-requirements/wp52-a-generic-numerical-and-status-evaluation.md','combat-requirements/wp47-a-move-attributes-targeting-and-calling.md','pokemon-rules/wp46-damage-multihit-and-healing.md']
for p in interfaces:
    path='deliverables/final-specification-set/'+p
    ck('upstream-interface-unchanged:'+p,(ROOT/path).read_bytes()==blob(ROOT,MAIN,path))
# Keep historical constraints explicit; no wholesale historical PASS inference.
for marker in ['| PowerHigherWithLessPP |','磨砺 EnsureNextCriticalHit','默认 GEOMANCY','| 自身与盟友各 1/4 恢复','撒菱满 3','痛楚平分']:
    line=next(l for l in oldbody.splitlines() if marker in l)
    ck('precise-historical-span-unchanged:'+marker,line in body)
allow=[str((MIRROR/p).relative_to(ROOT)) for p in contract['candidate_formal_paths']]
changed=git(ROOT,'diff','--name-only',BASE).decode().splitlines()
untracked=git(ROOT,'ls-files','--others','--exclude-standard').decode().splitlines()
ck('write-allowlist',all(p in allow or p.startswith(str(EV.relative_to(ROOT))+'/') for p in changed+untracked),changed+untracked)
ck('independent-review-not-self-certified',not any('CANDIDATE_PASS' in x for x in [body,cover,tests]))
result={'status':'AUTHOR_STATIC_CHECKS_PASS_PENDING_NONAUTHOR_REVIEW','checks':checks,'check_count':len(checks),'input_identities':input_ids,'evidence_levels':{'SOURCE_STATIC':'new source/contract reading recorded separately','DERIVED_VECTOR':'11 designed vectors; no execution','TOOL_VALIDATION':'this process: bytes, preserved rows, locators, literal arithmetic','ISOLATED_REFERENCE_EXECUTION':'NOT_EXECUTED','INDEPENDENT_MODEL':'NOT_EXECUTED','COMPLETE_HOST_DEMO':'NOT_EXECUTED'},'note':'Not an independent review, final selection test, integrated acceptance or closure.'}
print(json.dumps(result,ensure_ascii=False,indent=2))
