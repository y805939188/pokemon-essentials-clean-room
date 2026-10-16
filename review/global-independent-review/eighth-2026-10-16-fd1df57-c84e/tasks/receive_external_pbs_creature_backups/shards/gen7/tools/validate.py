"""Validate this report's identities/counts; no source execution or semantic credit."""
from pathlib import Path
import hashlib,json,subprocess
out=Path(__file__).resolve().parents[1]
root=next(x for x in out.parents if (x/'.git').exists())
def read(p):return json.loads(p.read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
identities=read(out/'identities.json')
r=read(root/identities['contract_readset']['path'])
ledger=read(out/'record-reception-ledger.json')['records']
assert [x['id'] for x in ledger]==[x['frozen']['id'] for x in r['owned_records']]
assert len(ledger)==1059 and sum(x['explicit_fields'] for x in ledger)==20488 and sum(x['omissions'] for x in ledger)==19774
assert sum(x['literal_read'] for x in ledger)==262
assert not any(x['full_contract_reception'] for x in ledger)
for x in ledger:
 if x['literal_read']:
  src=next(v for v in r['owned_primary_files'] if v['id']==x['identity_id'])
  unit=(Path(src['repo'])/src['path']).read_bytes()[slice(*x['byte_offsets_half_open'])]
  assert sha(unit)==x['source_unit_sha256']
  assert unit.decode() in (out/x['literal_view']).read_text()
for x in identities['normative']+identities['original_target_aliases']+identities['source_and_formal']:
 repo=Path(x.get('repo',root));p=repo/x['path'];b=p.read_bytes()
 assert len(b)==x['bytes'] and sha(b)==x['sha256'],str(p)
 assert subprocess.check_output(['git','-C',str(repo),'hash-object','--stdin'],input=b).decode().strip()==x['blob']
a=read(out/'atomic-reception.json')['records']
assert [x['id'] for x in a]==[x['id'] for x in r['owned_atoms']]
assert len(a)==58 and not any(x['full_contract_accepted'] for x in a)
assert sum(x['receiver_status']=='FINITE_FIELD_RULE_CORROBORATED_RECEPTION_CONDITIONAL' for x in a)==42
assert len(read(out/'interfaces.json')['records'])==2
assert all(x['status']=='INCOMPLETE' for x in read(out/'interfaces.json')['records'])
for p in out.rglob('*.json'):read(p)
print(json.dumps({'status':'PASS_TOOL_VALIDATION_ONLY','records':1059,'literal_read':262,'literal_unread':797,'complete_record_reception':0,'complete_atom_reception':0,'semantic_credit':0,'behavior_executions':0}))
