from pathlib import Path
import json,hashlib,datetime
q=Path(__file__).parent;o=q.parents[1]
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old=json.loads((q/'old-fact.complete.json').read_text());new=json.loads((q/'corrected-fact.complete.json').read_text());c=json.loads((q/'correction.json').read_text())
a=json.loads(json.dumps(old));a['meaning'][4]=new['meaning'][4];assert a==new
assert old['meaning'][4]!=new['meaning'][4]
assert c['mandatory_companion'] and len(c['affected_receivers'])==6
m=json.loads((o/'artifact-manifest.json').read_text())
for r in m['files']:
 p=o/r['path'];assert p.stat().st_size==r['bytes'];assert h(p)==r['sha256']
for r in c['complete_necessary_source_units']:
 p=Path(r['path']);assert p.stat().st_size==r['bytes'];assert h(p)==r['sha256']
for r in [json.loads(x) for x in (q/'io-ledger.jsonl').read_text().splitlines()]:
 for s in ['stdout','stderr']:
  p=q/(r['name']+'.'+s);assert p.stat().st_size==r[s+'_bytes'];assert h(p)==r[s+'_sha256']
print(json.dumps({'validated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'original_immutable_files_verified':len(m['files']),'original_fact_container_sha256':h(o/'sourcefact-consumer-receptions.json'),'changed_fact_fields':['meaning[4]'],'affected_atoms':6,'source_units_verified':6,'business_execution':'NOT_EXECUTED'},ensure_ascii=False))
