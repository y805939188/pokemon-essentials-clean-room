"""Read-only PBS identity/schema census; no reference evaluation or compilation."""
import hashlib, json, pathlib, re, subprocess

ROOT = pathlib.Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
REF = ROOT / 'reference/pokemon-essentials'
COMMIT = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
OUT = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-F/generator'
inputs = {}

def frozen(path):
    raw = subprocess.check_output(['git', '-C', str(REF), 'show', f'{COMMIT}:{path}'])
    assert (REF / path).read_bytes() == raw
    inputs[path] = {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw),
                    'lines': len(raw.decode('utf-8-sig').splitlines())}
    return raw.decode('utf-8-sig')

def sections(path):
    result = []
    current = None
    for line_no, line in enumerate(frozen(path).splitlines(), 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        match = re.fullmatch(r'\[(.+)\]', line)
        if match:
            current = {'id': match[1], 'line': line_no, 'fields': {}}
            result.append(current)
        elif '=' in line and current is not None:
            key, value = line.split('=', 1)
            current['fields'][key.strip()] = value.strip()
    return result

def identities(path):
    return {item['id'].split(',')[0] for item in sections(path)}

root_ids = {kind: identities('PBS/' + filename) for kind, filename in
            [('species', 'pokemon.txt'), ('items', 'items.txt'), ('moves', 'moves.txt'),
             ('types', 'types.txt'), ('trainer_types', 'trainer_types.txt')]}
gen5_ids = {kind: identities('PBS/Gen 5 backup/' + filename) for kind, filename in
            [('species', 'pokemon.txt'), ('items', 'items.txt'), ('moves', 'moves.txt'), ('types', 'types.txt')]}
nature_source = frozen('Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb')
natures = set(re.findall(r':id\s*=>\s*:(\w+)', nature_source))
root_ids['natures'] = natures
gen5_ids['natures'] = natures
gen5_ids['trainer_types'] = root_ids['trainer_types']

reports = []
for entry in sections('PBS/battle_facility_lists.txt'):
    trainer_file = 'PBS/' + entry['fields']['Trainers']
    pokemon_file = 'PBS/' + entry['fields']['Pokemon']
    records = []
    malformed = []
    for line_no, line in enumerate(frozen(pokemon_file).splitlines(), 1):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        fields = line.strip().split(';')
        if len(fields) != 5:
            malformed.append(line_no)
            continue
        records.append((line_no, fields))
    trainers = sections(trainer_file)
    table = {'section': entry['id'], 'config_line': entry['line'],
             'trainers': trainer_file, 'pokemon': pokemon_file,
             'trainer_count': len(trainers), 'pokemon_count': len(records),
             'malformed_field_counts': malformed, 'missing_trainer_fields': [],
             'bad_indices': [], 'unknown_ev_labels': [], 'profiles': {}}
    trainer_required = {'Type', 'Name', 'BeginSpeech', 'EndSpeechWin', 'EndSpeechLose', 'PokemonNos'}
    for trainer in trainers:
        absent = sorted(trainer_required - set(trainer['fields']))
        if absent:
            table['missing_trainer_fields'].append({'line': trainer['line'], 'fields': absent})
        for value in trainer['fields'].get('PokemonNos', '').split(','):
            if value and (not value.isdigit() or int(value) >= len(records)):
                table['bad_indices'].append({'line': trainer['line'], 'index': value})
    for line_no, fields in records:
        unknown = set(fields[3].split(',')) - {'HP', 'ATK', 'DEF', 'SA', 'SPATK', 'SD', 'SPDEF', 'SPD', ''}
        if unknown:
            table['unknown_ev_labels'].append({'line': line_no, 'labels': sorted(unknown)})
    for profile, catalogs in [('root', root_ids), ('gen5_identity_only', gen5_ids)]:
        missing = {key: [] for key in ['species', 'items', 'moves', 'natures', 'trainer_types']}
        for line_no, fields in records:
            for kind, value in [('species', fields[0]), ('items', fields[1]), ('natures', fields[2])]:
                if value and value not in catalogs[kind]:
                    missing[kind].append({'line': line_no, 'id': value})
            for move in fields[4].split(','):
                if move and move not in catalogs['moves']:
                    missing['moves'].append({'line': line_no, 'id': move})
        for trainer in trainers:
            value = trainer['fields'].get('Type', '')
            if value and value not in catalogs['trainer_types']:
                missing['trainer_types'].append({'line': trainer['line'], 'id': value})
        table['profiles'][profile] = missing
    reports.append(table)

result = {'evidence': 'TOOLS_ONLY_PBS_IDENTIFIER_AND_FIELD_CENSUS',
          'not_a_semantic_read': True, 'reference_executed': False,
          'independent_behavior_model_executed': False, 'host_or_demo_executed': False,
          'scope': 'Five active facility lists. Gen5 profile checks backup identifier membership only; trainer type/nature catalogs are shared because no corresponding Gen5 backup exists. No move legality or battle result claim.',
          'commit': COMMIT, 'inputs': inputs, 'lists': reports}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'compatibility-census.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'lists': len(reports), 'counts': [(r['trainer_count'], r['pokemon_count']) for r in reports],
                  'root_unknown': sum(len(v) for r in reports for v in r['profiles']['root'].values()),
                  'gen5_unknown': sum(len(v) for r in reports for v in r['profiles']['gen5_identity_only'].values())}))
