"""Mechanical identity/partition/claim check. Provides no semantic or business-execution credit."""
from pathlib import Path
import subprocess,hashlib,json,datetime
T=Path(__file__).resolve().parent;ROOT=T.parents[1];REPO=Path('/workspace/pokemon-essentials-clean-room');PREFIX=str(T.relative_to(REPO))+'/'
def load(p):return json.loads(p.read_text())
def call(args):
 p=subprocess.run(args,capture_output=True);assert p.returncode==0,(args,p.stderr);return p.stdout
f=load(T/'frozen-denominator.json');r=load(T/'reception-ledger.json');s=load(T/'continuation-contracts.json');reads=load(T/'reading-ledger.json')
assert len(f['objects'])==len(r['objects'])==1045
assert {x['id']for x in f['objects']}=={x['id']for x in r['objects']}
integrated=r['schema']=='gr8-cp-independent-reception/v2'
finished=r['status']=='FINITE_RECEPTION_COMPLETE_MAIN_ADJUDICATION_PENDING'
complete=sum(x['status'] in ['COMPLETE_FINITE_RECEPTION','COMPLETE_FINITE_CONTRIBUTION_RECEIVED'] for x in r['objects'])
assert complete==(1045 if finished else 879 if integrated else 3)
assert sum(x['status']=='SOURCE_CHECKED_FORMAL_RECEPTION_OPEN'for x in r['objects'])==(0 if integrated else 677)
assert sum(x['status']=='AVAILABLE_NOT_READ_NOT_RECEIVED'for x in r['objects'])==(0 if finished else 166 if integrated else 365)
parts=[v for j in s['jobs']for v in j['ids']];assert len(parts)==len(set(parts))==1045 and set(parts)=={x['id']for x in f['objects']}
assert sorted(x for j in s['jobs']for x in j['groups'])==[f'EXTCP-F{x:03}'for x in range(1,80)]
for j in s['jobs']:
 for key in ['prompt','readset']:
  b=(T/j[key]).read_bytes();i=j[key+'_identity'];assert len(b)==i['bytes']and hashlib.sha256(b).hexdigest()==i['sha256']and hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==i['git_blob']
for x in load(T/'recovery.json')['files']:
 b=(T/x['local_path']).read_bytes();assert len(b)==x['bytes']and hashlib.sha256(b).hexdigest()==x['sha256']and hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob']
ref=[]
for x in load(T/'reference-identities.json'):
 row=call(['git','--git-dir=/tmp/r8-cp-reference-R.git','ls-tree','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','--',x['path']]).decode().strip();meta,path=row.split('\t',1);mode,typ,oid=meta.split();assert mode==x['mode']and typ=='blob'and oid==x['blob']and path==x['path']
 b=(T/x['local_path']).read_bytes();assert len(b)==x['bytes']and hashlib.sha256(b).hexdigest()==x['sha256'];ref.append({'path':path,'mode':mode,'blob':oid})
assert call(['git','--git-dir=/tmp/r8-cp-reference-R.git','rev-parse','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b^{tree}']).decode().strip()=='7589c800b61ba13a13040ed0d686979b80a84fd0'
assert call(['git','rev-parse','HEAD:deliverables/final-specification-set']).decode().strip()=='f292698cdd4a8e725525a9be6dc34b75faaf151e'
changed=call(['git','diff','--name-only','40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232']).decode().splitlines();assert all(x.startswith(PREFIX)for x in changed)
unknown=call(['git','ls-files','--others','--exclude-standard']).decode().splitlines();assert all(x.startswith(PREFIX)for x in unknown)
# Every semantic view group is reversible: only identity/key order whitespace differ.
a=load(T/'recovered/18d21310bdc360c87d7ffd886df7d06aef8604a7/atomic-assertions.json')['assertions']
assert len(list((T/'views').glob('EXTCP-F*.json')))==79
for i in range(1,80):
 g=f'EXTCP-F{i:03}';assert load(T/'views'/f'{g}.json')==[x for x in a if x['group']==g]
result={'schema':'gr8-cp-package-validation/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'MECHANICAL_CHECKS_PASS_MAIN_ADJUDICATION_PENDING'if finished else'MECHANICAL_CHECKS_PASS_SEMANTIC_TASK_INCOMPLETE','primary_objects':1045,'source_checked':680,'source_checked_scope':'root initial direct source checks, not provider sum; new candidate-only ranges separately recorded','source_object_unread_scope':'objects without actual received independent verification; root direct line gaps remain separately recorded','complete_finite_receptions':complete,'unread_source':0 if finished else 166 if integrated else 365,'remaining_final':1045-complete,'split_partition_exact':True,'split_jobs':6,'source_modes_checked':ref,'restored31_identity_match':True,'writes_outside_exclusive_directory':[],'behavior_execution':'NOT_EXECUTED','semantic_credit_from_tool':0,'task_final':'MAIN_REVIEWER_ONLY_PENDING','UPDATE_NOT_STARTED':True}
(T/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k]for k in ['status','primary_objects','source_checked','complete_finite_receptions','remaining_final','split_jobs']}))
