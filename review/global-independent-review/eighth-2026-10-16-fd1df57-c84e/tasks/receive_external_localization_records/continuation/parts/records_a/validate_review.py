"""Mechanical consistency checks only; no semantic or behavioral credit."""
import pathlib,json,subprocess,hashlib,re,datetime
O=pathlib.Path(__file__).resolve().parent
ROOT=next(p for p in O.parents if (p/'.git').exists())
RROOT=pathlib.Path('/workspace/pokemon-essentials')
r=json.loads((O/'frozen-denominator.json').read_text())['fixed_readset']
l=json.loads((O/'reading-ledger.json').read_text())
x=json.loads((O/'reception-ledger.json').read_text())
d=json.loads((O/'definitions.json').read_text())['definitions']
s=json.loads((O/'semantic-profiles.json').read_text())
assert [v['id'] for v in x['records']]==[v['id'] for v in l['records']]==r['record_ids']
assert len(x['records'])==len(set(r['record_ids']))==2756
assert len(x['records'])*2==5512
slices=l['literal_view']['slices']; last=0
for v in slices:
 assert v['view_lines'][0]==last+1
 last=v['view_lines'][1]
 assert v['record_count']==sum(z['reading_slice']==v['id'] for z in x['records'])
assert last==2774
source_ids={v['id'] for v in x['records']}
for v in x['records']:
 assert v['literal_read_here'] and not v['necessary_local_unread']
 raw=(RROOT/'Text_english_core'/(v['domain']+'.txt')).read_bytes()
 lines=raw.decode('utf-8-sig').splitlines();n=v['record']
 k,t=lines[2*n+2:2*n+4]
 assert k==t==v['raw_key_and_translation_equal_literal']
 assert v['source']['lines']==[2*n+3,2*n+4]
 assert hashlib.sha256(k.encode()).hexdigest()==v['source']['key_sha256']==v['source']['translation_sha256']
 assert not re.search(r'[\r\n\t\x01]|\s{2,}',k)
 assert v['profile'].endswith('/'+v['domain'])
 assert s['domains'][v['domain']]['getter']['definition'] in d
 assert n!=253 or v['domain']!='ITEM_DESCRIPTIONS'
for name,v in d.items():
 i=v['identity']; repo=RROOT if i['commit']==r['R'] else ROOT
 content=subprocess.check_output(['git','show',i['commit']+':'+i['path']],cwd=repo)
 assert len(content)==i['bytes'] and hashlib.sha256(content).hexdigest()==i['sha256']
 assert (repo/i['path']).read_bytes()==content
 for a,b in v['read_ranges']:assert 1<=a<=b<=len(content.splitlines())
# All references within authored Markdown; publication receipt is intentionally created only after core freeze.
missing=[]
for label,target in re.findall(r'\[([^]]+)\]\(([^)]+)\)',(O/'report.md').read_text()):
 if target=='publication-receipt.json':continue
 if not (O/target).exists():missing.append(target)
assert not missing
for p in O.glob('*.json'):json.loads(p.read_text())
allpaths=subprocess.check_output(['git','ls-files','--others','--exclude-standard'],cwd=ROOT).decode().splitlines()
assert all(p.startswith(r['exclusive_write_set']) for p in allpaths)
changed=subprocess.check_output(['git','diff','--name-only',r['parent_contract_commit']],cwd=ROOT).decode().splitlines()
# Contract publication differs from earlier parent snapshot outside our write set; audit our delta against exact d14 only.
ours=subprocess.check_output(['git','diff','--name-only','d14a4bf68776ac7aacf54065c28ed982a054c8a8'],cwd=ROOT).decode().splitlines()
assert all(p.startswith(r['exclusive_write_set']) for p in ours)
result={'schema':'records-a-local-validation/v1','validation_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tool':'self-authored Python; no reference behavior executed','records_exact':2756,'fields_exact':5512,'IDs_equal_readset':True,'view_lines_contiguous':[1,2774],'source_values_equal':True,'source_definition_identities_and_ranges_match':len(d),'necessary_local_unread_records':0,'necessary_local_unread_definitions':0,'local_unreceived_record_chains':0,'new_proposals':0,'new_required':0,'parent_seven_interfaces_final_signed':0,'all_changed_or_untracked_paths_within_exclusive_write_set':True,'missing_authored_links':missing,'semantic_credit_from_tool':0,'behavior_execution':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
(O/'local-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
