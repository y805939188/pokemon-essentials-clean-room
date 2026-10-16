"""Mechanical semantic-object inventory. This tool never assigns semantic acceptance."""
from pathlib import Path
import collections
import hashlib
import json
import re

TASK = Path(__file__).resolve().parents[1]
INPUT = TASK / 'recovered-target'

def read(name):
    return json.loads((INPUT / name).read_text())

def dump(name, value):
    (TASK / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def main():
    forward = read('forward-mapping.json')
    ledger = read('reading-ledger.json')
    identities = read('identities.json')['payloads']
    contracts = read('field-contracts.json')
    reverse = read('reverse-mapping.json')
    primary = {x['identity_id']: x for x in ledger['primary']}
    objects = []
    for r in forward['records']:
        f = primary[r['identity_id']]
        original = next(s for s in f['all_sections'] if s['id'] == r['section_id'])
        assert r['source_lines'] == original['lines']
        objects.append(dict(id=r['section_id'], kind=r['kind'], identity_id=r['identity_id'],
                            section=original['section'], source_lines=r['source_lines'],
                            byte_offsets_half_open=original['byte_offsets_half_open'],
                            field_count=len(r['fields']), omission_count=len(r['omitted']),
                            forward_pointer='/records/' + str(len(objects)),
                            source_identity_pointer='/primary_identities/' + r['identity_id'],
                            status='FROZEN_NOT_READ_BY_INVENTORY'))
    assert len(objects) == len({x['id'] for x in objects}) == 6712
    assert sum(x['field_count'] for x in objects) == 89067
    assert sum(x['omission_count'] for x in objects) == 75313
    atoms = [a for c in contracts['contracts'] for a in c['atoms']] + forward['global_assertions']
    assert len(atoms) == len(reverse['atomic_assertions']) == 212
    for a, b in zip(atoms, reverse['atomic_assertions']):
        for key, value in a.items():
            assert b[key] == value, (a['id'], key)
    frozen = dict(schema='r8-reception-frozen-denominator/v1', contract_commit='40f45dddcdea5522b4bf7d0fea1a0f74f7d3d232',
                  target_commit='b6f12ecfbe006ef0f2ea463d6689d78094915e75',
                  counts=dict(records=len(objects), kinds=dict(collections.Counter(x['kind'] for x in objects)),
                              fields=89067, omissions=75313, field_contracts=45, atoms=212, headers=4, interfaces=12),
                  population_rule='Separate denominators; no sum of files/records/fields/atoms and no automatic semantic credit.',
                  primary_identities={k:v for k,v in identities.items() if k.startswith('P')},
                  records=objects, atoms=atoms, headers=contracts['headers'], interfaces=read('interfaces.json')['interfaces'],
                  source_and_formal_definitions={k:v for k,v in identities.items() if k.startswith('D')},
                  semantic_credit=0)
    dump('frozen-denominator.json', frozen)
    metric = Path('/workspace/pokemon-essentials/PBS/Gen 5 backup/pokemon_metrics.txt')
    data = metric.read_bytes()
    assert hashlib.sha256(data).hexdigest() == identities['P04']['sha256']
    rows = []
    for n, line in enumerate(data.decode('utf-8-sig').splitlines(), 1):
        s = line.strip()
        if not s or s.startswith('#'):
            continue
        if s.startswith('['):
            rows.append(dict(section=s[1:-1], line=n, fields={}))
        else:
            key, value = [x.strip() for x in s.split('=',1)]
            assert key not in rows[-1]['fields']
            rows[-1]['fields'][key] = dict(line=n, value=value)
    assert len(rows) == 674
    for r in rows:
        assert list(r['fields']) == ['BackSprite','FrontSprite','ShadowX','ShadowSize']
    dump('metrics-literal-view.json', dict(schema='r8-exact-metrics-view/v1', input_sha256=hashlib.sha256(data).hexdigest(),
        meaning='Every literal property retained. Omitted FrontSpriteAltitude is not an explicit zero; default comes from the independently read constructor.',
        aliases=['P04','P08','P12','P16'], rows=rows, generated_semantic_credit=0))
    print(json.dumps(frozen['counts']))

if __name__ == '__main__':
    main()
