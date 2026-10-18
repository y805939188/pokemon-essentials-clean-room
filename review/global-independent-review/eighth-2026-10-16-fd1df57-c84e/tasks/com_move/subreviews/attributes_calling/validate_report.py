from pathlib import Path
import hashlib,json,datetime,shutil
P=Path(__file__).resolve().parent
E=P/'evidence'
# Earlier repeated materialization recaptured the same immutable source bytes
# under reused names. Resolve every original event by its recorded SHA, and
# preserve one exact-byte archive per distinct stdout. Never invent absent IO.
events=[json.loads(l) for l in (E/'commands.jsonl').read_text().splitlines()]
files={}
for f in E.glob('*.stdout'):
    files.setdefault(hashlib.sha256(f.read_bytes()).hexdigest(),f)
resolution=[]
for i,e in enumerate(events,1):
    sha=e['stdout_sha256'];f=files.get(sha)
    if f:
        archive=E/('stdout-'+sha+'.raw')
        if not archive.exists():shutil.copyfile(f,archive)
        resolution.append({'event':i,'id':e['id'],'start_utc':e['start_utc'],'original_stdout':e['stdout'],
          'resolved_stdout':str(archive.relative_to(P)),'sha256':sha,'bytes':archive.stat().st_size,
          'original_locator_matches':hashlib.sha256((P/e['stdout']).read_bytes()).hexdigest()==sha})
    else:
        resolution.append({'event':i,'id':e['id'],'sha256':sha,'recovery':'UNAVAILABLE','reason':'No extant exact bytes; do not reconstruct semantic IO.'})
(E/'io-location-resolution.json').write_text(json.dumps({'events':resolution,'reason':'Repeated raw source captures reused filenames before unique-name guard was added. Original event UTC/exit/SHA remain in commands.jsonl; exact payload bytes are bound here without changing original events.'},ensure_ascii=False,indent=2)+'\n')
missing=[x for x in resolution if x.get('recovery')=='UNAVAILABLE']
assert not missing,missing
for n in ['progress','identities','reading-ledger','forward-mapping','reverse-mapping','interfaces','proposals']:
    json.loads((P/(n+'.json')).read_text())
rev=json.loads((P/'reverse-mapping.json').read_text())
assert len(rev['assertions'])==len({x['id'] for x in rev['assertions']})==1432
assert not rev['formal_missing_breakdown_lines']
assert all(x['equal'] for x in rev['data_checks']['blacklist_cells'])
assert len(rev['data_checks']['blacklist_cells'])==441
assert len(rev['data_checks']['held_mapping_rows'])==38
assert len(rev['data_checks']['natural_gift_rows'])==67
assert sum(x['primary'] for x in rev['vectors'])==52
assert len(rev['vectors'])==108
forward=json.loads((P/'forward-mapping.json').read_text())
assert len(forward['units'])==125
ids=json.loads((P/'identities.json').read_text())
assert all(x.get('actual_matches_fixed_bytes',True) for x in ids['payloads'])
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'static_artifact_checks':'PASS',
        'behavior_execution':'NOT_EXECUTED','source_units':125,'assertions':1432,'primary_vectors':52,
        'catalog_vectors':108,'blacklist_cells':441,'raw_io_resolved_events':len(resolution),'missing_io_events':0,
        'open_final_reception_interfaces':3,'update_status':'UPDATE_NOT_STARTED'}
(E/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
