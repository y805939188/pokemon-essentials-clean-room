"""Independent local-object structural audit. Never a game semantic PASS."""
import collections
import datetime
import hashlib
import json
import pathlib
import subprocess

OUT = pathlib.Path(__file__).resolve().parent
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
CAND = '13fddb0a217b36974c75657aa68da0caf104ee48'
PRE = 'review/remediation-fifth-20261013-prepare/'
CP = PRE + 'registration/successors/20261014-final-closure-candidate/closure-candidate.json'
AP = PRE + 'registration/successors/20261014-final-activation/activation-receipt.json'
ACCP = PRE + 'registration/successors/20261014-u08-formal-acceptance/U08-formal-acceptance.json'
ACT = 'debf59f3c5370df253706969fd4dd1c103300bf2'
ACTP = PRE + 'reviews/R5-U08/actual/round-01/criteria-results.json'
cache = {}
checks = []
units = []

def canon(v):
    return hashlib.sha256(json.dumps(v, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

def leaves(v, ptr=''):
    if isinstance(v, dict):
        for k, x in v.items():
            yield from leaves(x, ptr + '/' + k.replace('~', '~0').replace('/', '~1'))
    elif isinstance(v, list):
        for i, x in enumerate(v):
            yield from leaves(x, ptr + '/' + str(i))
    else:
        yield ptr, v

def load(ref, path):
    assert len(ref) == 40 and all(c in '0123456789abcdef' for c in ref)
    assert path.startswith(PRE) and '..' not in pathlib.PurePosixPath(path).parts
    key = (ref, path)
    if key not in cache:
        data = subprocess.check_output(['git', 'show', ref + ':' + path])
        value = json.loads(data) if path.endswith('.json') else data.decode()
        blob = subprocess.check_output(['git', 'rev-parse', ref + ':' + path], text=True).strip()
        flat = list(leaves(value))
        cache[key] = (data, value, blob, len(flat))
        ld = {'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'ref': ref,
              'path': path, 'bytes': len(data), 'lines': len(data.splitlines()),
              'sha256': hashlib.sha256(data).hexdigest(), 'git_blob': blob,
              'mode': 'FULL_STRUCTURAL_PARSE_ALL_NODES', 'primitive_leaf_count': len(flat),
              'semantic_status': 'NO_AUTOMATIC_SEMANTIC_PASS'}
        with (OUT / 'reading-ledger.jsonl').open('a') as f:
            f.write(json.dumps(ld, ensure_ascii=False) + '\n')
    return cache[key][1]

def point(v, ptr):
    for k in ptr.strip('/').split('/') if ptr else []:
        k = k.replace('~1', '/').replace('~0', '~')
        v = v[int(k)] if isinstance(v, list) else v[k]
    return v

def test(name, ok, detail=None):
    checks.append({'check': name, 'matched': bool(ok), 'detail': detail})

def descriptor(d, default_ref=None):
    ref = d.get('commit', default_ref)
    load(ref, d['path'])
    data, value, blob, _ = cache[(ref, d['path'])]
    for k, actual in [('bytes', len(data)), ('sha256', hashlib.sha256(data).hexdigest()), ('git_blob', blob)]:
        if k in d:
            test(ref + ':' + d['path'] + '/' + k, actual == d[k])
    if 'pointer' in d and 'record_sha256' in d:
        test(ref + ':' + d['path'] + d['pointer'], canon(point(value, d['pointer'])) == d['record_sha256'])
    return value

a = load(MAIN, AP)
c = load(CAND, CP)
acc = load(CAND, ACCP)
actual = load(ACT, ACTP)
initial = load(CAND, PRE + 'registration/initial-ledger.json')
ledger = load(CAND, PRE + 'registration/successors/20261014-u08-formal-acceptance/current-ledger.json')
test('candidate_external_tree', subprocess.check_output(['git', 'rev-parse', CAND + '^{tree}'], text=True).strip() == a['closing_candidate']['tree'])
for d in a['closing_candidate']['core_payloads']:
    descriptor(d)
for d in [a['independent_closing_byte_review']['report'], a['independent_closing_byte_review']['gate_results'], a['unique_U08_acceptance']['receipt'], a['unique_U08_acceptance']['shared21']]:
    descriptor(d)
test('canonical92_identity_set', {r['id'] for r in c['records']} == {r['id'] for r in initial['findings']} and len({r['id'] for r in c['records']}) == 92)
test('selection_is_complete_ordered92', len(a['state_resolution']['selection']) == 92)
for i, r in enumerate(c['records']):
    selected = a['state_resolution']['selection'][i]
    test(r['id'] + '/selection', selected['id'] == r['id'] and selected['record_index'] == i and selected['selected_state_pointer'] == f'/records/{i}/proposed_only_after_valid_activation')
    test(r['id'] + '/canonical_selected_state_hash', canon(r['proposed_only_after_valid_activation']) == selected['selected_state_record_sha256'])
    test(r['id'] + '/canonical_entire_scope_hash', canon(r) == selected['scope_record_sha256'])
    test(r['id'] + '/proposed_closed', r['proposed_only_after_valid_activation'] == {'status': 'CLOSED', 'final_CLOSED': True})
    test(r['id'] + '/old_snapshot_retained', r['current_effective'] == {'status': 'OPEN_REQUIRED', 'final_CLOSED': False})
    packet = descriptor(r['frozen_required_scope'])
    scope = point(packet, r['frozen_required_scope']['pointer'])
    test(r['id'] + '/frozen_id_owner_severity', (scope['id'], scope['severity'], scope['batch_owner']) == (r['id'], r['severity'], r['batch']))
    descriptor(r['original_owner_acceptance'])
    binding = point(acc, r['current_U08_accepted_finding_binding']['pointer'])
    test(r['id'] + '/accepted_scope_record_hash', canon(binding) == r['current_U08_accepted_finding_binding']['record_sha256'])
    fact = point(actual, binding['pointer'])
    test(r['id'] + '/actual_finding_hash', canon(fact) == binding['record_sha256'])
    for field, arr in [('native_static_conditions', acc['accepted_native410_bindings']), ('original_schema_checks', acc['accepted_schema568_bindings'])]:
        for d in r[field]:
            record = point(acc, d['pointer'])
            test(r['id'] + d['pointer'], canon(record) == d['record_sha256'] and record['finding_id'] == r['id'] and record['criterion_id'] == d['criterion_id'])
            rp = record.get('actual_result_pointer')
            if rp:
                test(r['id'] + '/actual' + rp, canon(point(actual, rp)) == record['actual_record_sha256'])
            if 'native_selector' in record:
                selector = record['native_selector']
                original = load(selector['commit'], selector['path'])
                test(r['id'] + '/native' + selector['pointer'], canon(point(original, selector['pointer'])) == selector['frozen_record_sha256'])
    test(r['id'] + '/native_original_count', len(r['native_static_conditions']) == len(scope['acceptance_criteria']['static']) == binding['native_static_count'])
    test(r['id'] + '/schema_count', len(r['original_schema_checks']) == binding['schema_check_count'])
    test(r['id'] + '/qualified_cases', r['qualified_case_scope_preserved'] == binding['qualified_case_scope_preserved'])
    descriptor(r['current_dependency_binding'])
    test(r['id'] + '/erratum_flag', r['SC_false_capture_body_LF_excluded'] == binding['SC_false_capture_body_LF_excluded'])
    units.append({'id':r['id'], 'severity':r['severity'], 'batch':r['batch'],
        'title':scope['title'], 'scope_pointer':r['frozen_required_scope'],
        'native_static':scope['acceptance_criteria']['static'],
        'preserve':scope['acceptance_criteria'].get('preserve', []),
        'optional':scope['acceptance_criteria'].get('optional', []),
        'must_execute':scope['acceptance_criteria'].get('must_execute', []),
        'preconditions':scope.get('preconditions'), 'excluded_claims':scope.get('excluded_claims'),
        'evidence_level':scope.get('evidence_level'), 'execution_status':scope.get('execution_status'),
        'actual_scope_reason':fact['independent_current_reason'],
        'current_sync_results':fact['current_sync_results'],
        'shared':r['current_precise_shared_receipt_ids'],
        'additional_consumer':r['additional_current_aggregate_consumer_receipt_ids'],
        'dependency_scope':point(ledger, r['current_dependency_binding']['pointer']),
        'SC_false_capture_body_LF_excluded':r['SC_false_capture_body_LF_excluded'],
        'candidate_raw_text_human_full_read':False,
        'candidate_full_structure_reviewed':True, 'game_semantics_revalidated':False})

shared = load(CAND, a['unique_U08_acceptance']['shared21']['path'])
for row in shared['receipts']:
    descriptor(row['independent_result']['file_identity'])
    descriptor(row['independent_result'])
test('shared21_unique', len(shared['receipts']) == len({r['receipt_id'] for r in shared['receipts']}) == 21)
native = sum(len(r['native_static_conditions']) for r in c['records'])
schema = sum(len(r['original_schema_checks']) for r in c['records'])
observed = {'required': len(c['records']), 'P2': sum(r['severity']=='P2' for r in c['records']),
            'P3': sum(r['severity']=='P3' for r in c['records']), 'native_static': native,
            'schema':schema, 'additional_schema_units':schema-native, 'shared':len(shared['receipts'])}
result = {'level':'LOCAL_OBJECT_TOOL_VALIDATION_ONLY', 'observed_counts':observed,
          'all_checks':len(checks), 'mismatches':[r for r in checks if not r['matched']],
          'no_game_semantic_PASS':True, 'new_reference_execution':0, 'new_model_execution':0,
          'new_hostDemo_execution':0, 'parsed_inputs':[{'ref':r,'path':p,'bytes':len(v[0]),'all_primitive_leaves':v[3]} for (r,p),v in cache.items()]}
(OUT/'activation-structural-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
(OUT/'activation-check-details.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in checks))
(OUT/'qualification-units.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in units))
print(json.dumps({k:v for k,v in result.items() if k != 'parsed_inputs'},ensure_ascii=False,indent=2))
