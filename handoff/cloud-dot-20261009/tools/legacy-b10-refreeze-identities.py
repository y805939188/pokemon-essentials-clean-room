"""New private frozen-document identity bookkeeping; no quality or write authorization."""
from pathlib import Path
import argparse,datetime,hashlib,json,re,subprocess
p=argparse.ArgumentParser()
p.add_argument('--worktree',required=True)
p.add_argument('--accepted-commit',required=True)
p.add_argument('--published-branch',required=True)
p.add_argument('--publication-receipt',required=True)
p.add_argument('--output',required=True)
a=p.parse_args()
W=Path(a.worktree);C=a.accepted_commit
A='d48197f365c39925f795c1d325988c0d74e59979'
B='1e6b11a47370f1c7c4659a32443fc1afda597bac'
P='41fffb540c6483f5296ea0d33b789b75180d27ed'
assert re.fullmatch('[0-9a-f]{40}',C) and C not in {A,B,P}
assert a.published_branch.startswith('codex/remediation-20261003-prepare/')
def git(*args):return subprocess.check_output(['git',*args],cwd=W)
def ident(c,path):
 b=git('show',c+':'+path)
 return {'commit':c,'path':path,'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)}
assert git('rev-list','--parents','-n','1',C).decode().strip().split()==[C,A]
assert git('remote','get-url','origin').decode().strip()=='https://github.com/y805939188/pokemon-essentials-clean-room.git'
assert git('remote','get-url','--push','origin').decode().strip()=='https://github.com/y805939188/pokemon-essentials-clean-room.git'
remote=git('ls-remote','--heads','origin','refs/heads/'+a.published_branch).decode().strip().split()
assert remote==[C,'refs/heads/'+a.published_branch]
receipt_path=Path(a.publication_receipt);receipt=json.loads(receipt_path.read_text())
commit_fields=[receipt[k] for k in ['acceptance_commit','report_commit'] if k in receipt]
assert commit_fields and all(x==C for x in commit_fields)
assert receipt['push_succeeded'] is True
q='review/remediation-20261003-prepare/'
plan=json.loads(git('show',P+':'+q+'batches.json'))[9]
cp='review/remediation/20261003-prepare/batches/B09/acceptance-stage-1/B10-downstream-contract.json'
contract=json.loads(git('show',B+':'+cp))
assert plan['id']=='B10' and len(plan['read_paths'])==53 and len(plan['write_paths'])==8
assert [x['path'] for x in contract['planned_reads']]==plan['read_paths']
assert contract['allowed_formal_write_paths']==plan['write_paths']
assert len(contract['allowed_write_input_identities'])==8
reads=[]
for i,x in enumerate(contract['planned_reads'],1):
 assert x['planned_index']==i
 old=x['accepted_current_input'];historic=old.get('commit')
 before=ident(historic or B,x['path'])
 assert all(before[k]==old[k] for k in ['path','git_blob','sha256','bytes'])
 current=ident(historic or C,x['path'])
 reads.append({'planned_index':i,'path':x['path'],'role':'FIXED_HISTORICAL_INPUT' if historic else 'CURRENT_ACCEPTED_INPUT','current_frozen_identity':current,'prior_B09_input':before,'changed_since_B09':current['sha256']!=before['sha256'],'semantic_consumption_from_identity_check':False})
writes=[]
for x in contract['allowed_write_input_identities']:
 before=ident(B,x['path']);assert all(before[k]==x[k] for k in ['path','git_blob','sha256','bytes'])
 current=ident(C,x['path'])
 writes.append({'path':x['path'],'current_write_input':current,'prior_B09_write_input':before,'changed_since_B09':current['sha256']!=before['sha256'],'write_authorization_from_identity_check':False})
originals=[]
for x in contract['potential_original_sync_contract']:
 current=ident(C,x['original_path'])
 originals.append({'final_path':x['final_path'],'original_path':x['original_path'],'current_original_input':current,'write_authorized':False,'bounded_proposal_and_coordinator_scope_amendment_required':True})
o=Path(a.output);assert not o.exists()
result={'role':'ROOT_MECHANICAL_REFREEZE_IDENTITIES_ONLY_NO_QUALITY_APPROVAL','status':'IDENTITIES_REFROZEN_NOT_SEMANTIC_READING_NOT_FORMAL_SCOPE','run_id':'20261003-prepare','batch':'B10','accepted_B14_commit':C,'accepted_B14_tree':git('rev-parse',C+'^{tree}').decode().strip(),'reviewed_B14_ACT':A,'prior_B09_C':B,'PLAN':P,'original_contract_identity':ident(B,cp),'publication_receipt_sha256':hashlib.sha256(receipt_path.read_bytes()).hexdigest(),'independent_remote_ref_check':{'sha':C,'ref':remote[1],'method':'ordinary GitHub ls-remote'},'planned_read_count':53,'planned_reads':reads,'write_input_count':8,'write_inputs':writes,'potential_original_sync_inputs':originals,'extra_current_handoff_reading_required':'Complete B14 acceptance package, all applicable gate and B10 dependency contracts at their own immutable identities; identity checks do not discharge semantic reading.','scope_authorization':False,'quality_approval':False,'runtime_observations':0,'proven_demo_chains':0,'executed_behavior_vectors':0,'UTC':datetime.datetime.now(datetime.timezone.utc).isoformat()}
o.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'role':result['role'],'accepted_B14_commit':C,'planned_reads':53,'write_inputs':8,'changed_planned_reads':sum(x['changed_since_B09'] for x in reads),'quality_approval':False}))
