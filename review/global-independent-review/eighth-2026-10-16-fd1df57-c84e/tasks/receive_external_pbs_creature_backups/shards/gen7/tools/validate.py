"""Exhaustive evidence integrity checks. No source execution or reading credit."""
from pathlib import Path
import hashlib,json,re,subprocess
out=Path(__file__).resolve().parents[1]
root=next(x for x in out.parents if (x/'.git').exists())
def read(p):return json.loads(p.read_text())
def sha(b):return hashlib.sha256(b).hexdigest()
identities=read(out/'identities.json'); r=read(root/identities['contract_readset']['path'])
ledger=read(out/'record-reception-ledger.json')['records']; frozen=r['owned_records']
assert [x['id'] for x in ledger]==[x['frozen']['id'] for x in frozen]
assert len(ledger)==1059 and sum(x['explicit_fields'] for x in ledger)==20488 and sum(x['omissions'] for x in ledger)==19774
assert all(x['literal_read'] and x['finite_local_reception'] and x['omission_dispositions_displayed'] for x in ledger)
assert not any(x['full_contract_reception'] for x in ledger)
raw={};fields_verified=0
for row,contract in zip(ledger,frozen):
 f=contract['frozen']; src=next(v for v in r['owned_primary_files'] if v['id']==row['identity_id']);bs=(Path(src['repo'])/src['path']).read_bytes();unit=bs[slice(*row['byte_offsets_half_open'])]
 assert sha(unit)==row['source_unit_sha256']==contract['source_unit_sha256']
 assert unit.decode() in (out/row['literal_view']).read_text(),row['id']
 d={}
 for line in unit.decode().splitlines():
  m=re.match(r'^(\w+)\s*=\s*(.*)$',line)
  if not m:continue
  k,v=m.groups()
  if k=='Evolution':d.setdefault(k,[]).append(v)
  else:d[k]=v
 raw[row['id']]=d;ls=bs.decode().splitlines()
 for line_no,key,fc,h,count in contract['complete_target_forward_object']['fields']:
  k,value=ls[line_no-1].split('=',1)
  assert k.strip()==key and sha(value.strip().encode())==h,(row['id'],key,line_no)
  fields_verified+=1
 assert len(contract['complete_target_forward_object']['fields'])==row['explicit_fields']
assert fields_verified==20488
forms=read(out/'form-resolution.json')['records'];assert len(forms)==250
for x,y in zip(forms,frozen[809:]):
 i=x['id'];b=x['base'];assert x['reviewed_concrete_binding'] and x['all_raw_values_already_literally_read']
 assert b==y['complete_target_forward_object']['base_section'] and b.startswith('P10:')
 assert len(x['resolved_author_values'])==38 and len(x['origin_policy'])==38
 for key,policy in x['origin_policy'].items():
  value=x['resolved_author_values'][key]
  if policy=='EXPLICIT':assert value==raw[i][key],(i,key)
  elif policy=='BASE_EXPLICIT':assert value==raw[b][key],(i,b,key)
  elif policy=='OWN_EMPTY_PARTIAL_WILD':assert key in ['WildItemCommon','WildItemUncommon','WildItemRare'] and value==[]
  elif policy=='OWN_DEFAULT':assert key in ['FormName','PokedexForm','MegaStone','MegaMove','UnmegaForm','MegaMessage']
  else:assert policy=='BASE_CONSTRUCTOR_DEFAULT' and key not in raw[b]
om=read(out/'base-omission-bindings.json');assert om['reviewed']
for x in om['records']:
 expected=[y['frozen']['id'] for y in frozen[:809] if any(z[0]==x['field'] for z in y['complete_target_forward_object']['omitted'])]
 assert x['base_record_ids']==expected
for x in identities['normative']+identities['original_target_aliases']+identities['source_and_formal']:
 repo=Path(x.get('repo',root));b=(repo/x['path']).read_bytes()
 assert len(b)==x['bytes'] and sha(b)==x['sha256'],x['path']
 assert subprocess.check_output(['git','-C',str(repo),'hash-object','--stdin'],input=b).decode().strip()==x['blob']
for x in identities['continuation_inputs']:
 b=subprocess.check_output(['git','-C',x['repo'],'show',x['commit']+':'+x['path']]);assert len(b)==x['bytes'] and sha(b)==x['sha256']
 mode,typ,blob=subprocess.check_output(['git','-C',x['repo'],'ls-tree',x['commit'],'--',x['path']],text=True).split('\t')[0].split();assert mode==x['mode'] and blob==x['blob'] and typ=='blob'
a=read(out/'atomic-reception.json');assert [x['id'] for x in a['records']]==[x['id'] for x in r['owned_atoms']]
assert len(a['records'])==58 and all(x['finite_local_reception'] for x in a['records']) and not any(x['full_contract_accepted'] for x in a['records'])
assert len(a['headers'])==1 and a['headers'][0]['finite_local_reception']
interfaces=read(out/'interfaces.json')['records'];assert [x['id'] for x in interfaces]==['IF08','CD-I01']
for x,y,z in zip(interfaces,r['owned_interfaces'],r['complete_original_central_interfaces']):
 assert x['complete_original']==y and x['complete_original_central']==z
 assert x['status']=='INCOMPLETE' and not x['four_generation_complete_value_join'] and not x['root_signature']
 assert {y['generation'] for y in x['remaining']}=={'gen8'}
remaining=read(out/'remaining-reception.json')
for k in ['own_primary_literal_unread_ids','own_primary_default_inheritance_remaining_ids','own_atomic_finite_remaining_ids','own_header_finite_remaining_ids','own_necessary_consumer_unread','material_or_permission_blockers']:assert remaining[k]==[]
counts=read(out/'reading-ledger.json')['counts'];assert counts['literal_records_read']==1059 and counts['own_primary_finite_reception_complete']==1059 and counts['owned_atoms_finitely_corroborated']==58
assert read(out/'progress.json')['literal_and_reception_counts']==counts
for p in out.rglob('*.json'):read(p)
for line in (out/'continuation-notes.jsonl').read_text().splitlines():json.loads(line)
assert subprocess.check_output(['git','branch','--show-current'],cwd=root,text=True).strip()=='codex/r8-final-pbs-gen7-20261016'
changes=subprocess.check_output(['git','diff','--name-only','30afe79aabc084e3baf9842cb87b90acbc5c6d0a'],cwd=root,text=True).splitlines()
assert all(x.startswith(str(out.relative_to(root))+'/') for x in changes)
print(json.dumps({'status':'PASS_TOOL_VALIDATION_ONLY','records':1059,'explicit_value_hashes':fields_verified,'omission_dispositions':19774,'concrete_form_bindings':250,'own_primary_finite_reception':1059,'own_atomic_finite_reception':58,'header_finite':1,'full_interfaces_signed':0,'final_root_acceptance':0,'semantic_credit_from_tool':0,'behavior_executions':0}))
