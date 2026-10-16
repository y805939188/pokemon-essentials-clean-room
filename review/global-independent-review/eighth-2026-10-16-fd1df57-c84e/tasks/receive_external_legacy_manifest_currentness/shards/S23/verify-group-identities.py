"""Read-only identity/alias validation. This never grants semantic credit."""
from pathlib import Path
import csv, datetime, hashlib, json, subprocess

HERE = Path(__file__).resolve().parent
TASK = HERE.parents[1]
ROOT = TASK.parents[1]
REPO = ROOT.parents[2]
REF = Path('/workspace/pokemon-essentials')
INPUT = HERE / 'inputs/target-93d7df7f'

def read(name):
    return json.loads((INPUT / name).read_text())

def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])

def verify(item):
    repo = REF if item['repository'] == 'Maruno17/pokemon-essentials' else REPO
    data = git(repo, 'show', item['commit'] + ':' + item['path'])
    mode, kind, blob = git(repo, 'ls-tree', item['commit'], '--', item['path']).split(b'\t')[0].decode().split()
    assert kind == 'blob'
    assert (mode, blob, len(data), hashlib.sha256(data).hexdigest()) == (item['mode'], item.get('blob', item.get('git_blob')), item['bytes'], item['sha256'])
    assert git(repo, 'rev-parse', item['commit'] + '^{tree}').decode().strip() == item['tree']
    return {'repository': item['repository'], 'commit': item['commit'], 'path': item['path'], 'mode': mode, 'blob': blob, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def main():
    contracts = [json.loads((TASK / ('split-contracts/' + s + '.complete.json')).read_text()) for s in ['S21', 'S22', 'S23']]
    common = [k for k in contracts[0] if all(c[k] == contracts[0][k] for c in contracts)]
    parent = json.loads((ROOT / 'delegation/readsets/receive_external_legacy_manifest_currentness.complete.json').read_text())
    parent_aliases = [k for k in parent if k in contracts[0] and parent[k] == contracts[0][k]]
    assert read('evidence-catalog.json') == contracts[0]['source_evidence_catalog']
    cache_aliases = []
    for row in contracts[0]['files']:
        rel = row['relative_to_target_task']
        assert (INPUT / rel).read_bytes() == (TASK / 'inputs/target-93d7df7f' / rel).read_bytes()
        cache_aliases.append(rel)
    identities = {}
    def once(item):
        key = (item['repository'], item['commit'], item['path'])
        if key not in identities:
            identities[key] = verify(item)
    for item in read('evidence-catalog.json')['items']:
        once(item)
    routes = read('current-primary-contribution-routes.v2.json')
    for provider in routes['providers']:
        for item in provider.get('fixed_items', []):
            once(item)
        if 'fixed_readset' in provider:
            once(provider['fixed_readset'])
    for route in routes['formal_routes']:
        once(route['fixed_readset'])
        once(route['current_formal_identity'])
    formal = {r['path'] for r in routes['formal_routes']}
    actual = set(git(REPO, 'ls-tree', '-r', '--name-only', contracts[0]['fixed_B8'], '--', 'deliverables/final-specification-set/').decode().splitlines())
    assert len(routes['formal_routes']) == len(formal) == 131 and formal == actual
    worlds = []
    for provider in read('world-interface-reception.v2.json')['fixed_contributions']:
        once(provider['identity'])
        payload = json.loads(git(REPO, 'show', provider['identity']['commit'] + ':' + provider['identity']['path']))
        for row in provider['records']:
            obj = payload
            for part in row['pointer'].strip('/').split('/'):
                obj = obj[int(part)] if isinstance(obj, list) else obj[part]
            assert obj == row['record']
            worlds.append({'id': row['id'], 'pointer': row['pointer'], 'exact_value_equal': True})
    semantic = read('semantic-purpose-review.v2.json')
    events = {e['id']: e for e in semantic['units']}
    tsv = {int(r['round']): r for r in csv.DictReader((INPUT / 'event-judgments.v2.tsv').open(), delimiter='\t')}
    physical = read('frozen-primary-structure.json')
    raw = git(REPO, 'show', contracts[0]['fixed_B8'] + ':planning/review-manifest-2026-09-19.md')
    lines = raw.splitlines(keepends=True)
    paragraph = read('purpose-dispositions.json')
    byline = {u['line']: u for u in paragraph['units']}
    shards = {}
    for n in range(1, 21):
        c = json.loads((TASK / f'split-contracts/S{n:02}.complete.json').read_text())
        for e in c['events_all_fields']:
            eid = e['id']
            assert e == events[eid]
            assert eid not in shards
            shards[eid] = f'S{n:02}'
        for p in c['paragraph_dispositions_all_fields']:
            assert p == byline[p['line']]
    assert set(events) - set(shards) == {f'LM-E{n:03}' for n in [66,67,68,69,70,71,72,169]}
    alias_rows = []
    for e in semantic['units']:
        assert tsv[e['round']]['current_purpose_judgment'] == e['reader_judgment']
        for n in e['primary_line_ids']:
            u = byline[int(n[4:])]
            assert u['current_purpose_reason'] == e['reader_judgment']
            assert u['actual_successor_events'] == e['actual_successor_events']
            assert u['current_formal_routes'] == e['current_formal_routes']
        alias_rows.append({'event': e['id'], 'semantic_owner': shards.get(e['id'], 'S22'), 'tsv_reason_equals_event_reason_equals_all_paragraph_reasons': True, 'successors_and_routes_equal': True, 'semantic_credit_from_check': 0})
    for u in physical['units']:
        part = raw[u['byte_start']:u['byte_end']]
        assert len(part) == u['bytes'] and hashlib.sha256(part).hexdigest() == u['sha256']
        p = byline[u['line']]
        assert all(p[k] == u[k] for k in ['id', 'line', 'byte_start', 'byte_end', 'bytes', 'sha256'])
    assert json.loads(read('core-readback-execution-attempt2.json')['stdout']) == read('core-remote-readback.json')
    result = {'schema': 'r8-lmc-group5-identity-alias-validation/v1', 'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'semantic_credit': 0,
        'common_contract_fields': common, 'parent_readset_exact_field_aliases': parent_aliases,
        'target_parent_cache_exact_byte_aliases': cache_aliases, 'catalog_exact_value_alias_to_shared_contract': True,
        'verified_unique_git_inputs': list(identities.values()), 'world_record_exact_aliases': worlds,
        'formal_routes_exact_131_file_set': True, 'event_field_aliases': alias_rows,
        'all_1413_physical_and_purpose_identity_fields_equal': True,
        'attempt2_stdout_exact_value_alias_to_core_remote_readback': True,
        'purpose': 'Identity/field routing only. S01–S20 event prose is not semantically accepted here; no author FULL_READ transferred.'}
    (HERE / 'identity-and-field-aliases.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'identity_inputs': len(identities), 'world_records': len(worlds), 'route_files': len(formal), 'event_aliases': len(alias_rows), 'semantic_credit': 0}))

if __name__ == '__main__':
    main()
