#!/usr/bin/env python3
"""Validate only audit artifacts and immutable byte identities; never evaluate reference code."""
from pathlib import Path
import json, hashlib, datetime, subprocess, traceback
base=Path(__file__).resolve().parent
rr=base.parent.parent
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
out=err=''
code=0
try:
    ids=json.loads((base/'identities.json').read_text())['files']
    assert len(ids)==29
    for x in ids:
        data=(Path(x['repo'])/x['path']).read_bytes()
        assert len(data)==x['bytes'] and hashlib.sha256(data).hexdigest()==x['sha256'],x['path']
        frozen=subprocess.run(['git','-C',x['repo'],'show',x['commit']+':'+x['path']],capture_output=True,check=True).stdout
        assert data==frozen,x['path']
    assert sum('clean-room' not in x['repo'] for x in ids)==20
    it=json.loads((base/'interfaces.json').read_text())
    assert len(it['accepted_scoped'])==15 and not it['open_interfaces']
    assert len({x['id'] for x in it['accepted_scoped']})==15
    p=json.loads((base/'pbs-reload-reception.v1.json').read_text())
    assert len(p['manual_semantic_facets'])==6
    assert p['necessary_available_unread']==p['necessary_consumer_unreceived']==0
    for x in p['root_qualification_bindings']:
        raw=(rr/x['path']).read_bytes()
        assert len(raw)==x['bytes'] and hashlib.sha256(raw).hexdigest()==x['sha256']
    checked=[]
    old_mutable=[]
    for x in p['actual_read_receipts']:
        if x['credit']=='EXPLORATORY_TRUNCATED_NO_ACCEPTANCE_CREDIT': continue
        io=json.loads((base/x['io']).read_text())
        assert io['exit_code']==0
        path=Path(x.get('provider_path',x.get('path')))
        if not path.is_absolute():path=Path('/workspace/pokemon-essentials-clean-room')/path
        raw=path.read_bytes()
        matches=len(raw)==x['original_identity']['bytes'] and hashlib.sha256(raw).hexdigest()==x['original_identity']['sha256']
        if not matches:
            assert x['io']=='io/REC_PBS_BATTLE_OP.json'
            current=next(y for y in p['actual_read_receipts'] if y['io']=='io/REC_PBS_BATTLE_OP_CURRENT.json')
            assert len(raw)==current['original_identity']['bytes'] and hashlib.sha256(raw).hexdigest()==current['original_identity']['sha256']
            old_mutable.append({'old_read':x['io'],'current_read':current['io'],'disposition':'Original historical input identity retained; concurrently revised artifact fully reread in same context. Not source drift or business execution.'})
        else: checked.append(x['io'])
    u=json.loads((base/'unread-and-boundaries.v2.json').read_text())
    assert len(u['paths'])==62 and all(not x['own_raw_full_added_by_this_receipt'] for x in u['paths'])
    l=json.loads((base/'reading-ledger.json').read_text())
    assert (l['full_read'],l['unread_files'],l['named_scoped_interfaces'])==(29,0,15)
    f=json.loads((base/'forward-mapping.json').read_text())
    assert len(f['manual_units'])==65 and f['manual_fact_count']==196
    rev=json.loads((base/'reverse-mapping.json').read_text())
    assert (rev['manual_groups'],rev['manual_subassertions'])==(72,273)
    assert len(rev['vectors'])==285
    parsed=0
    for path in base.rglob('*.json'):
        json.loads(path.read_text());parsed+=1
    out=json.dumps({'status':'PASS_STATIC_ARTIFACT_AND_FIXED_IDENTITY_ONLY','primary_files':29,'primary_bytes':sum(x['bytes'] for x in ids),
        'source_units':65,'source_facts':196,'formal_groups':72,'formal_branches':273,'catalog_rows':285,'interfaces':15,
        'necessary_unreceived':0,'receipt_current_bytes_checked':len(checked),'mutable_audit_artifact_reread':old_mutable,
        'outer_paths_personal_credit_preserved':62,'JSON_parse_checked':parsed,'business_runs':0,'new_contexts':0,'UPDATE_NOT_STARTED':True},ensure_ascii=False)+'\n'
except Exception:
    err=traceback.format_exc();code=1
end=datetime.datetime.now(datetime.timezone.utc).isoformat()
obj={'operation':'STATIC_REPORT_AND_FROZEN_IDENTITY_VALIDATION_NOT_BUSINESS_EXECUTION','start_utc':start,'end_utc':end,
     'stdout':out,'stderr':err,'exit_code':code,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,
     'qualification':'Checks existing bytes/JSON/counts/declared scope only. Source and business never evaluated; original stdout/stderr/exit/UTC retained.'}
(base/'validation.v2.json').write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print(out,end='');print(err,end='')
raise SystemExit(code)
