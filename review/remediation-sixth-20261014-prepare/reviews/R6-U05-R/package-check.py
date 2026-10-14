"""Check the review package, without evaluating reference behavior."""
import hashlib, json, re, subprocess, sys
from pathlib import Path
D=Path(__file__).resolve().parent; ROOT=D.parents[3]; PRE=D.parents[1]
def load(p):return json.loads(p.read_bytes())
def canon(x):return hashlib.sha256(json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
v=load(D/'verdict.json'); c=load(PRE/'contracts/R6-U05.json'); vector=load(D/'vector-review.json'); e=load(D/'execution.json')
checks=[]
def check(name,x):checks.append({'name':name,'pass':bool(x)})
check('four exact required IDs', [x['id'] for x in v['per_id']]==c['required_ids'])
check('candidate only verdict',v['result']=='PASS' and v['candidate_event']=='CANDIDATE_PASS' and v['integrated_PASS']=='NOT_PERFORMED' and v['formal_acceptance']=='NOT_PERFORMED' and v['CLOSED']=='NOT_REGISTERED')
for s,r in zip(c['scope_contracts'],v['per_id']):
 check('full frozen contract '+s['id'],r['frozen_complete_contract']==s and r['original_scope_contract_binding']['canonical_record_sha256']==canon(s))
 check('seven groups '+s['id'],sorted(r['seven_groups'])==sorted(['identity_and_verdict','bidirectional_evidence','premises_and_counterexample','minimum_revision_contract','acceptance_and_regression','independent_adjudication','dependencies_and_receivers']))
 check('no new revisions '+s['id'],r['seven_groups']['identity_and_verdict']['minimal_necessary_revision']==[])
check('23 unique unexecuted derived vectors',len(vector['vectors'])==23 and len({x['id'] for x in vector['vectors']})==23 and all(x['level']=='DERIVED_VECTOR' and x['executed'] is False and x['actual_reference_result']==x['actual_model_result']==x['actual_host_result']=='NOT_EXECUTED' for x in vector['vectors']))
check('all runtime levels zero',all(e['new_execution_counts'][k]==0 for k in ['reference_or_isolated_original_definitions','reference_observation_with_surrogates','independent_full_behavior_model','full_host_Demo','real_save','production_service','derived_vectors_executed']))
check('actual configuration unverified',set(e['reviewer']['actual_configuration'].values())=={'UNVERIFIED'})
for f in D.rglob('*'):
 if f.is_file():
  if f.suffix=='.json':load(f)
  elif f.suffix=='.jsonl':
   for line in f.read_text().splitlines():json.loads(line)
check('all JSON/JSONL parse',True)
links=re.findall(r'\]\(([^)]+)\)',(D/'review.md').read_text())
check('all local report links exist',all((D/p).is_file() for p in links))
branch=git('branch','--show-current').decode().strip()
check('independent branch',branch=='codex/remediation-sixth-r6-u05-review-20261014')
owned=str(D.relative_to(ROOT))+'/'
status=git('status','--porcelain','-uall').decode().splitlines()
check('only owned new/modified tracked and untracked worktree paths',all(x[3:].startswith(owned) for x in status))
check('protected existing worktree bytes unchanged',git('diff','--name-only').decode().strip()=='')
check('author mirror exact',git('rev-parse','HEAD:'+str((PRE/'candidates/R6-U05/mirror').relative_to(ROOT))).decode().strip()==v['candidate_binding']['mirror_tree'])
check('formal subtree exact',git('rev-parse','HEAD:deliverables/final-specification-set').decode().strip()==v['candidate_binding']['formal_tree'])
result={'level':'TOOL_VALIDATION_REPORT_PACKAGE_ONLY','checks':checks,'count':len(checks),'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'semantic_verdict':'Root direct review in verdict.json; this checker is not behavioral execution.'}
(D/'package-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'count':result['count'],'passed':result['passed'],'failed':result['failed']}))
for x in checks:
 if not x['pass']:print(json.dumps(x))
sys.exit(0 if result['failed']==0 else 1)
