"""Exact current reverse JSON component view; no source/code execution or reading credit."""
import json,hashlib,datetime
from pathlib import Path
OWN=Path(__file__).resolve().parent;BASE=OWN.parent.parent
start=datetime.datetime.now(datetime.timezone.utc).isoformat();ledger=json.loads((OWN/'reading-ledger.json').read_text());identity=ledger['snapshot_payloads'][35]
raw=(BASE/identity['snapshot']).read_bytes();assert len(raw)==identity['bytes'] and hashlib.sha256(raw).hexdigest()==identity['sha256'];original=json.loads(raw)
known=json.loads((OWN/'ability-concrete-formal-selected-exact.json').read_text())['distinct_complete_concrete_formal_assertions']
unit=json.loads((BASE/ledger['snapshot_payloads'][30]['snapshot']).read_text())['source_unit_fact_rows']
family=json.loads((BASE/ledger['snapshot_payloads'][38]['snapshot']).read_text())['families']
unit_ids=[x['id'] for x in unit];family_ids=[x['id'] for x in family]
known_text={x['full_assertion']:i for i,x in enumerate(known)}
sections=[];specs=[]
def index_append(values,x):
 if x not in values:values.append(x)
 return values.index(x)
def encode_ids(xs,values):
 return [{'$known_id':values.index(x)} if x in values else x for x in xs]
def decode_ids(xs,values):return [values[x['$known_id']] if isinstance(x,dict) and set(x)=={'$known_id'} else x for x in xs]
rows=[]
for r in original['rows']:
 v=dict(r);text=r['full_assertion']
 v['full_assertion']={'$earlier_full_assertion_ordinal':known_text[text]} if text in known_text else text
 v['section']={'$section_ordinal':index_append(sections,r['section'])}
 v['spec_identity']={'$spec_identity_ordinal':index_append(specs,r['spec_identity'])}
 v['primary_families']=encode_ids(r['primary_families'],family_ids)
 v['source_identity_units']=encode_ids(r['source_identity_units'],unit_ids)
 subs=[]
 for a in r['subassertions']:
  b=dict(a);pos=text.find(a['text']);assert pos>=0
  b['text']={'$parent_full_assertion_slice':[pos,pos+len(a['text'])]}
  b['supporting_source_families']=encode_ids(a['supporting_source_families'],family_ids)
  b['specific_source_identities']=encode_ids(a['specific_source_identities'],unit_ids)
  subs.append(b)
 v['subassertions']=subs;rows.append(v)
encoded=dict(original);encoded['rows']=rows
reconstructed=dict(encoded);outrows=[]
for r in rows:
 v=dict(r);a=r['full_assertion'];text=known[a['$earlier_full_assertion_ordinal']]['full_assertion'] if isinstance(a,dict) else a
 v['full_assertion']=text;v['section']=sections[r['section']['$section_ordinal']];v['spec_identity']=specs[r['spec_identity']['$spec_identity_ordinal']]
 v['primary_families']=decode_ids(r['primary_families'],family_ids);v['source_identity_units']=decode_ids(r['source_identity_units'],unit_ids)
 subs=[]
 for a in r['subassertions']:
  b=dict(a);i,j=a['text']['$parent_full_assertion_slice'];b['text']=text[i:j]
  b['supporting_source_families']=decode_ids(a['supporting_source_families'],family_ids);b['specific_source_identities']=decode_ids(a['specific_source_identities'],unit_ids);subs.append(b)
 v['subassertions']=subs;outrows.append(v)
reconstructed['rows']=outrows;assert reconstructed==original
view={'schema':'gr8-ability-reverse-exact-component-view/v1','qualification':'All currentfieldvalues exactly reconstructed. Earlier full_assertion ordinal references321 complete objects alreadyactuallyread; $known_id ordinal references463 identity or80family order actuallyread. Each subassertiontext is literalcodepoint slice ofits complete parent full_assertion, no normalization/truncation. Readingwholeparent plus everybinding remains required; generation0reading,0source/fullformal/atomicacceptance.','source':{k:identity[k] for k in ['original_path','snapshot','bytes','sha256','captured_utc']},'earlier_full_assertions':{'path':'ability-concrete-formal-selected-exact.json','sha256':hashlib.sha256((OWN/'ability-concrete-formal-selected-exact.json').read_bytes()).hexdigest(),'array':'/distinct_complete_concrete_formal_assertions','actual_receipts':[f'ability321-concrete-formal-full-selected-{i:02}.receipt.json' for i in range(1,9)]},'unit_identity_order':'ability463-exact-component-binding-compact-view.json /rows literal_unit_id inoriginalorder','family_order':'ability80-caller24-selected-exact-projection.json /current_selected_value/families','all_sections':sections,'all_spec_identities':specs,'value':encoded}
target=OWN/'ability-reverse-exact-component-view.json';assert not target.exists();target.write_text(json.dumps(view,ensure_ascii=False,indent=1)+'\n')
proof={'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0,'source_bytes':len(raw),'source_sha256':identity['sha256'],'output':target.name,'bytes':target.stat().st_size,'lines':len(target.read_text().splitlines()),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'all_decode_equals_original':True,'generation_reading_credit':0,'behavior':'NOT_EXECUTED'}
(OWN/'ability-reverse-exact-component-generation.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
