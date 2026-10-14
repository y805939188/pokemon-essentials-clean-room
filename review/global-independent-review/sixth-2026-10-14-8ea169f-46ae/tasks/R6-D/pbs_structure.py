"""Inert all-record PBS audit, not compiler execution or semantic approval."""
import collections
import hashlib
import json
import pathlib
import re
from read_range import ROOT, OUT, verify

verify()
REF = ROOT / 'reference/pokemon-essentials'
SKIP = {'pokemon.txt', 'pokemon_forms.txt', 'pokemon_metrics.txt', 'moves.txt',
        'abilities.txt', 'items.txt', 'berry_plants.txt', 'types.txt',
        'types_shadow_pkmn.txt', 'items_shadow_pkmn.txt', 'shadow_pokemon.txt', 'moves_shadow_pkmn.txt'}

def parse(path):
    raw = path.read_bytes()
    lines = raw.decode('utf-8-sig').splitlines()
    data = dict(path=str(path.relative_to(REF)), sha256=hashlib.sha256(raw).hexdigest(),
                lines=len(lines), records=[], unsectioned=[])
    current = None
    for number, line in enumerate(lines, 1):
        value = line.strip()
        if not value or value.startswith('#'):
            continue
        header = re.fullmatch(r'\[([^]]+)\]\s*(?:#.*)?', value)
        if header:
            current = dict(ordinal=len(data['records']), identity=header[1], start_line=number,
                           end_line=number, fields=[], rows=[])
            data['records'].append(current)
        elif current is not None:
            current['end_line'] = number
            if '=' in value:
                key, val = value.split('=', 1)
                current['fields'].append(dict(line=number, key=key.strip(), value=val.strip()))
            else:
                current['rows'].append(dict(line=number, value=value))
        else:
            data['unsectioned'].append(dict(line=number, value=value))
    return data

def identities(name):
    return {r['identity'] for r in parse(REF / 'PBS' / name)['records']}

all_paths = sorted((REF / 'PBS').rglob('*.txt'))
selected = [p for p in all_paths if p.name not in SKIP]
data = [parse(p) for p in selected]
catalog = {d['path']: d for d in data}
species = identities('pokemon.txt')
items = identities('items.txt')
moves = identities('moves.txt')
types = identities('trainer_types.txt')
nature_source = REF / 'Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb'
natures = set(re.findall(r':id\s*=>\s*:(\w+)', nature_source.read_text()))
stat_names = {'HP', 'ATK', 'DEF', 'SA', 'SPATK', 'SD', 'SPDEF', 'SPD'}
exceptions = []
families = []
for d in data:
    name = pathlib.Path(d['path']).name
    if name.endswith('_pkmn.txt') or name.endswith('_pkmn_single.txt') or name == 'battle_tower_pokemon.txt':
        rows = d['unsectioned']
        for ordinal, row in enumerate(rows):
            atoms = [s.strip() for s in row['value'].split(';')]
            row['ordinal'] = ordinal
            row['atoms'] = atoms
            row['ref_checks'] = {}
            if len(atoms) < 5:
                exceptions.append(dict(path=d['path'], line=row['line'], reason='fewer_than_five_fields'))
                continue
            row['ref_checks'] = dict(species=atoms[0] in species,
                                      item=atoms[1] in items or not atoms[1],
                                      nature=atoms[2] in natures or not atoms[2])
            evs = [s.strip().upper() for s in atoms[3].split(',')]
            row['ignored_EV'] = [s for s in evs if s not in stat_names]
            row['EV_duplicates'] = {k: v for k, v in collections.Counter(evs).items() if v > 1}
            supplied_moves = [s.strip() for s in atoms[4].split(',')]
            row['move_checks'] = [dict(value=s, defined=s in moves) for s in supplied_moves]
            bad_moves = [s for s in supplied_moves[:4] if s and s not in moves]
            if (not all(row['ref_checks'].values()) or row['ignored_EV'] or row['EV_duplicates']
                or bad_moves or len(atoms) != 5 or len(supplied_moves) > 4):
                exceptions.append(dict(path=d['path'], **row))
        family = 'facility_pokemon'
    elif '_trainers' in name:
        pair = name.replace('battle_tower_trainers', 'battle_tower_pokemon').replace('_trainers', '_pkmn')
        pool_size = len(catalog['PBS/'+pair]['unsectioned'])
        for r in d['records']:
            fields = {v['key']: v['value'] for v in r['fields']}
            nums = [int(n.strip()) for n in fields.get('PokemonNos', '').split(',') if n.strip()]
            r['consumer_checks'] = dict(type_defined=fields.get('Type') in types, pair=pair,
                pool_size=pool_size, candidate_count=len(nums), minimum=min(nums) if nums else None,
                maximum=max(nums) if nums else None, all_indices_valid=all(0 <= n < pool_size for n in nums),
                duplicates={k: v for k, v in collections.Counter(nums).items() if v > 1},
                all_six_fields=set(fields) == {'Type', 'Name', 'BeginSpeech', 'EndSpeechWin', 'EndSpeechLose', 'PokemonNos'})
            c = r['consumer_checks']
            if not c['type_defined'] or not c['all_indices_valid'] or not c['all_six_fields'] or c['duplicates']:
                exceptions.append(dict(path=d['path'], identity=r['identity'], **c))
        family = 'facility_trainers'
    else:
        family = name.removesuffix('.txt')
    d['family'] = family
    (OUT / ('structure-' + d['path'][4:].replace('/', '--').replace(' ', '_') + '.json')).write_text(
        json.dumps(d, ensure_ascii=False, indent=2)+'\n')
    families.append(dict(path=d['path'], family=family, lines=d['lines'], sha256=d['sha256'],
                         records=len(d['records']), unsectioned_rows=len(d['unsectioned']),
                         fields=sum(len(r['fields']) for r in d['records']), stage='structure_only'))
digest = dict(files=families, exceptions=exceptions, semantic_approval=False)
(OUT / 'pbs-special-structure.json').write_text(json.dumps(digest, ensure_ascii=False, indent=2)+'\n')
with (OUT / 'reading-ledger.jsonl').open('a') as stream:
    for d in families:
        stream.write(json.dumps(dict(d, method='inert_structural_parser', coverage='all_physical_records_and_fields'))+'\n')
with (OUT / 'command-log.jsonl').open('a') as stream:
    stream.write(json.dumps(dict(operation='pbs_structure.py', input_commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
        selected_files=len(data), output_directory=str(OUT), exit=0, semantic_approval=False))+'\n')
for d in families:
    print(d)
print('EXCEPTIONS', len(exceptions))
for row in exceptions:
    print(json.dumps(row, ensure_ascii=False))
