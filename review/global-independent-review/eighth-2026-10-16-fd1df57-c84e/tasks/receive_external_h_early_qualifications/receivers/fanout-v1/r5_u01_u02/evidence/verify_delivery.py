"""Finite document consistency and protected-tree checks, with zero semantic credit."""
from pathlib import Path
import subprocess,json,gzip,collections,hashlib
W=Path(__file__).resolve().parents[1];T=W.parents[2];P=Path('/workspace/pokemon-essentials-clean-room');R=Path('/workspace/pokemon-essentials')
def read(p):return json.loads(p.read_text())
def git(repo,*a):return subprocess.check_output(['git','-C',str(repo),*a]).decode().strip()
readset=read(T/'delegation/fanout-v1/shards/r5_u01_u02/readset.json');pop=readset['primary_semantic_population'];f=read(W/'frozen-units.json');r=read(W/'reception-ledger.json');d=read(W/'evidence/adjudications.json');i=read(W/'interfaces.json');u=read(W/'unreceived.json');p=read(W/'progress.json')
assert [x['id']for x in f['records']]==pop['R5_ids']==[x['id']for x in r['records']]
assert [x['criterion_id']for x in r['criterion_results']]==pop['R5_criteria']
assert len(d['records'])==len({x['id']for x in d['records']})==48
assert sum(len(x['checks'])for x in d['records'])==294
assert sum(len(x['criterion_ids'])for x in f['records'])==294
assert sum(x['native_static_conditions']for x in f['records'])==192
assert len(r['records'][:34])==34 and len(r['criterion_results'][:248])==248
assert len(i['outbound_per_producer'])==48
assert {x['producer_id']for x in i['outbound_per_producer']}==set(pop['R5_ids'])
assert all(not x['whole_interface_signature']for x in i['outbound_per_producer']+i['incoming_or_global'])
assert len(u['necessary_interface_unreceived'])==2
assert u['local_available_required_unread']==u['local_primary_unreceived']==u['local_criterion_unreceived']==[]
assert not p['ready_for_coordinator_consolidation'] and p['UPDATE_NOT_STARTED'] and p['new_behavior_execution']==0
assert not read(W/'findings.json')['new_required_proposals']
obj=json.loads(gzip.decompress((W/'evidence/object-identities.json.gz').read_bytes()));assert len(obj)==784
assert {x['index']for x in obj}==set(range(784))
assert git(P,'branch','--show-current')=='codex/r8-final-early-r5-u01-u02-20261016'
assert git(P,'rev-parse','HEAD:deliverables/final-specification-set')=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
assert git(R,'rev-parse','HEAD')=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
assert git(R,'rev-parse','HEAD^{tree}')=='7589c800b61ba13a13040ed0d686979b80a84fd0'
root=str(W.relative_to(P))+'/'
changed=git(P,'diff','--name-only','9abf7bfc87274fb37f08d9f77a1bcb53f53d3ecd','--').splitlines()
assert all(x.startswith(root)for x in changed),changed
for q in W.rglob('*'):
 if '.local'in q.parts or 'inputs-recovered-1'in q.parts:continue
 assert not q.is_symlink(),q
for name in readset['required_outputs']:assert (W/name).is_file(),name
files=[]
for q in sorted(W.rglob('*')):
 if q.is_file() and '.local'not in q.parts and 'inputs-recovered-1'not in q.parts and '__pycache__'not in q.parts:
  if q.name in ['verification.json','publication.json']:continue
  files.append({'path':str(q.relative_to(W)),'bytes':q.stat().st_size})
result={'schema':'gr8.r5-u01-u02.delivery-validation/v1','primary_exact_set_and_order':48,'criterion_exact_set_and_order':294,'native_conditions':192,'complete_objects_identity_manifest':784,'incoming_interfaces_open':2,'outbound_producer_contributions':48,'new_B8_required':0,'protected_formal_tree_unchanged':True,'R_commit_tree_unchanged':True,'branch_exact':True,'exclusive_write_set_check':True,'symlink_count':0,'files':files,'generated_validation_semantic_credit':0,'new_behavior_execution':0}
(W/'evidence/verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k!='files'}))
