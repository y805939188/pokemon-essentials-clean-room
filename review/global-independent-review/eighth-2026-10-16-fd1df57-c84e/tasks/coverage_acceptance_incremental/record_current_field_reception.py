"""Record an explicitly authored reception after actual reading; no tool grants reading."""
import collections, datetime, hashlib, json, sys
from pathlib import Path
OWN=Path(__file__).resolve().parent
BASE=OWN.parent.parent
index=int(sys.argv[1]); proof_name=sys.argv[2]; key=sys.argv[3]
assert Path(proof_name).name==proof_name and proof_name.endswith('.json')
proof=json.loads((OWN/proof_name).read_text())
assert proof['complete_current_json_fields_read'] is True
ledger=json.loads((OWN/'reading-ledger.json').read_text())
row=ledger['snapshot_payloads'][index]
raw=(BASE/row['snapshot']).read_bytes()
assert hashlib.sha256(raw).hexdigest()==row['sha256']==proof['source']['sha256']
assert len(raw)==row['bytes']==proof['source']['bytes']
row.update(read_state='FULL_CURRENT_JSON_FIELDS_PERSONALLY_READ_EXACT_COLUMNAR_VIEW',
 reader='/root/coverage_acceptance_incremental',source_or_formal_semantic_credit=False,
 exact_unread_scope='NONE_IN_CURRENT_JSON_FIELDS; underlyingsource/formal/consumerclosureseparate',
 actual_read_receipts=proof['actual_receipts'],lossless_view=proof['view']['output'],
 semantic_qualification=proof['ledger_qualification'])
by=collections.defaultdict(list)
for item in ledger['snapshot_payloads']:by[item['sha256']].append(item)
pending=[v[0] for v in by.values() if not any(x['read_state'].startswith(('FULL_','SAME_BYTES_LINK')) for x in v)]
n=len(pending); nbytes=sum(x['bytes'] for x in pending); nfull=len(by)-n
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
ledger.update(current_semantically_read_unique_sha=nfull,
 remaining_not_fully_personally_semantically_read_unique_sha=n,
 remaining_not_fully_personally_semantically_read_unique_bytes=nbytes,updated_utc=now)
ledger[key]=proof
(OWN/'reading-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
for name in ['progress.json','coverage-gaps.json','acceptance-register.json',
 'atomic-and-interface-denominator.json','execution-records.json','next-dispatch.json']:
 path=OWN/name;doc=json.loads(path.read_text());doc[key]=proof;doc['updated_utc']=now
 if name=='progress.json':doc.update(personally_current_semantic_full_frozen_artifacts=nfull,pending_unique_sha=n,pending_unique_bytes=nbytes)
 if name=='next-dispatch.json':
  doc['auditor_remaining_reception'].update(remaining_unique_sha=n,remaining_unique_bytes=nbytes,updated_utc=now)
  doc['latest_original289_pending']=[{k:x[k] for k in ['original_path','snapshot','bytes','sha256','git_blob','read_state']} for x in pending]
 path.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':now,'qualified':nfull,'pending':n,'pending_bytes':nbytes,
 'semantic_pass':False,'proof':proof_name}))
