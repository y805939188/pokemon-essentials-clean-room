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
 return [values.index(x) if x in values else x for x in xs]
def decode_ids(xs,values):return [values[x] if isinstance(x,int) else x for x in xs]
rows=[]
for r in original['rows']:
 v=dict(r);text=r['full_assertion']
 v['full_assertion']=known_text[text] if text in known_text else text
 v['section']=index_append(sections,r['section'])
 v['spec_identity']=index_append(specs,r['spec_identity'])
 v['primary_families']=encode_ids(r['primary_families'],family_ids)
 v['source_identity_units']=encode_ids(r['source_identity_units'],unit_ids)
 subs=[]
 for a in r['subassertions']:
  b=dict(a);pos=text.find(a['text']);assert pos>=0
  b['text']=[pos,pos+len(a['text'])]
  b['supporting_source_families']=encode_ids(a['supporting_source_families'],family_ids)
  b['specific_source_identities']=encode_ids(a['specific_source_identities'],unit_ids)
  subs.append(b)
 v['subassertions']=subs;rows.append(v)
encoded=dict(original);encoded['rows']=rows
reconstructed=dict(encoded);outrows=[]
for r in rows:
 v=dict(r);a=r['full_assertion'];text=known[a]['full_assertion'] if isinstance(a,int) else a
 v['full_assertion']=text;v['section']=sections[r['section']];v['spec_identity']=specs[r['spec_identity']]
 v['primary_families']=decode_ids(r['primary_families'],family_ids);v['source_identity_units']=decode_ids(r['source_identity_units'],unit_ids)
 subs=[]
 for a in r['subassertions']:
  b=dict(a);i,j=a['text'];b['text']=text[i:j]
  b['supporting_source_families']=decode_ids(a['supporting_source_families'],family_ids);b['specific_source_identities']=decode_ids(a['specific_source_identities'],unit_ids);subs.append(b)
 v['subassertions']=subs;outrows.append(v)
reconstructed['rows']=outrows;assert reconstructed==original
view={'schema':'gr8-ability-reverse-exact-component-view/v1','qualification':'All currentfieldvalues exactly reconstructed. Integer full_assertion references321 complete objects alreadyactuallyread; integerIDs in source/family arrays reference463 identity or80family order actuallyread, strings remainliteral. Section/spec are integerindices into complete dictionaries. Subassertiontext [start,end] is literalcodepoint slice ofits complete parent full_assertion, no normalization/truncation. Readingwholeparent plus everybinding remains required; generation0reading,0source/fullformal/atomicacceptance.','source':{k:identity[k] for k in ['original_path','snapshot','bytes','sha256','captured_utc']},'earlier_full_assertions':{'path':'ability-concrete-formal-selected-exact.json','sha256':hashlib.sha256((OWN/'ability-concrete-formal-selected-exact.json').read_bytes()).hexdigest(),'array':'/distinct_complete_concrete_formal_assertions','actual_receipts':[f'ability321-concrete-formal-full-selected-{i:02}.receipt.json' for i in range(1,9)]},'unit_identity_order':'ability463-exact-component-binding-compact-view.json /rows literal_unit_id inoriginalorder','family_order':'ability80-caller24-selected-exact-projection.json /current_selected_value/families','all_sections':sections,'all_spec_identities':specs,'value':encoded}
target=OWN/'ability-reverse-exact-component-v2-view.json';assert not target.exists();target.write_text(json.dumps(view,ensure_ascii=False,indent=1)+'\n')
proof={'start_utc':start,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':0,'source_bytes':len(raw),'source_sha256':identity['sha256'],'output':target.name,'bytes':target.stat().st_size,'lines':len(target.read_text().splitlines()),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'all_decode_equals_original':True,'generation_reading_credit':0,'behavior':'NOT_EXECUTED'}
(OWN/'ability-reverse-exact-component-v2-generation.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof))
