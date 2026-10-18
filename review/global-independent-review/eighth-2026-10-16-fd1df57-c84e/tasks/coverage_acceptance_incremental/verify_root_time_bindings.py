import datetime
import hashlib
import json
import pathlib
import subprocess

OWN = pathlib.Path(__file__).resolve().parent
REPO = OWN.parents[4]
NOW = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
started = NOW()
binding = json.loads((OWN / 'delta-inputs/root24-utc-correction/root-decision-first-recorded-bindings.json').read_text())
versions = []
all_records = {}
for src in binding['available_history_sources']:
    result = subprocess.run(['git', 'show', src['commit'] + ':' + src['path']], cwd=REPO,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    item = {'source': src, 'exit_code': result.returncode,
            'stdout_bytes': len(result.stdout), 'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
            'stderr': result.stderr.decode('utf-8', errors='replace')}
    assert result.returncode == 0, item
    item['git_blob_computed'] = hashlib.sha1(b'blob ' + str(len(result.stdout)).encode() + b'\0' + result.stdout).hexdigest()
    assert item['stdout_bytes'] == src['bytes']
    assert item['stdout_sha256'] == src['sha256']
    assert item['git_blob_computed'] == src['blob']
    obj = json.loads(result.stdout)
    all_records[src['commit']] = obj['records']
    item['record_count'] = len(obj['records'])
    versions.append(item)
verified = []
for record_id, spec in binding['records'].items():
    if 'first_available_fixed_report_binding' not in spec:
        verified.append({'record_id': record_id, 'status': 'LOCAL_COUNTER_BINDING_ONLY_NOT_PUBLISHED'})
        continue
    source = spec['first_available_fixed_report_binding']
    index = int(spec['json_locator'][8:-1])
    record = all_records[source['commit']][index]
    identity_values = [record.get(key) for key in ['id', 'record_id', 'proposal_id', 'finding_id']]
    assert record_id in identity_values, (record_id, index, identity_values)
    assert record['decision_utc'] == spec['first_recorded_decision_utc_in_available_report_history']
    earlier = [v for v in binding['available_history_sources'] if v['commit'] != source['commit']]
    source_index = next(i for i, v in enumerate(binding['available_history_sources']) if v['commit'] == source['commit'])
    for old in binding['available_history_sources'][:source_index]:
        assert not any(record_id in [r.get(k) for k in ['id', 'record_id', 'proposal_id', 'finding_id']]
                       for r in all_records[old['commit']])
    verified.append({'record_id': record_id, 'status': 'EXACT_ID_TIME_AND_FIRST_IN_FIVE_AVAILABLE_VERSIONS_VERIFIED',
                     'commit': source['commit'], 'json_locator': spec['json_locator']})
out = {'schema': 'gr8-root-time-binding-identity-check/v1', 'began_utc': started, 'ended_utc': NOW(),
       'versions': versions, 'records': verified,
       'semantic_historical_body_read_credit': False, 'source_read_credit': False,
       'qualification': 'Identity, array locator and recorded timestamp only. These are earliest available five report versions, not authoritative first platform operation UTC.'}
target = OWN / 'root-time-binding-verification.json'
target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output': str(target), 'versions': len(versions), 'fixed_records': len(verified) - 1,
                  'local_only_records': 1, 'mismatches': 0, 'exit_code': 0, 'began_utc': started, 'ended_utc': out['ended_utc']}))
