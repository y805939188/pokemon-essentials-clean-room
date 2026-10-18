from pathlib import Path
import json,hashlib,datetime
p=Path(__file__).parent
objects={x.name:json.loads(x.read_text()) for x in p.glob('*.json') if x.name!='artifact-manifest.json'}
atoms=objects['manual-atomic-clauses.json']['rows']
facts=objects['sourcefact-consumer-receptions.json']['facts']
units=objects['reading-ledger.json']['units']
unitids={x['id'] for x in units}; factids={x['id'] for x in facts}
assert len(atoms)==17 and len({x['original_atomic_id'] for x in atoms})==17
assert len(facts)==10 and len(factids)==10
assert len(objects['old-locator-disposition.json']['rows'])==4
assert all(set(x['fact_ids'])<=factids for x in atoms)
assert all(set(x['source_units'])<=unitids for x in facts)
assert all(x['same_fixed_blob'] for x in units)
assert all(x['business_execution']=='NOT_EXECUTED' for x in facts+atoms)
assert len(objects['sourcefact-consumer-receptions.json']['item_family_meanings']['HPHeal'])==16
assert len(objects['sourcefact-consumer-receptions.json']['item_family_meanings']['StatusCure'])==8
assert len(objects['sourcefact-consumer-receptions.json']['form_family_meanings'])==5
assert all(x['cancel'] and x['error_prefix'] and x['persistence_reload'] and x['normal_and_boundary'] for x in facts)
assert len(objects['selected-original-sourcefacts.json']['full_original_source_fact_records'])==7
for n,d in objects.items():
 if n.startswith('selected-'):continue
 if isinstance(d,dict):
  assert d.get('global_pass',False) is False
io=[json.loads(x) for x in (p/'io-ledger.jsonl').read_text().splitlines()]
for x in io:
 for s in ['stdout','stderr']:
  b=(p/(x['name']+'.'+s)).read_bytes();assert len(b)==x[s+'_bytes'];assert hashlib.sha256(b).hexdigest()==x[s+'_sha256']
for r in units:
 if 'actual_ranges' in r:
  assert all(1<=a<=b<=r.get('file_lines',1000000) for a,b in r['actual_ranges'])
print(json.dumps({'validated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'json_files':len(objects),'original_atoms':len(atoms),'facts':len(facts),'source_formal_files':len(units),'captured_io_records_checked':len(io),'exit_distribution':{str(k):sum(x['exit_code']==k for x in io) for k in sorted({x['exit_code'] for x in io})},'business_execution':'NOT_EXECUTED','target_business_runs':0},ensure_ascii=False))
