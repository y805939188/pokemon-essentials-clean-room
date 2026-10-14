"""Enumerate inert data predicates for independently reviewed consumption rules."""
import collections
import hashlib
import json
import pathlib
import re
from read_range import ROOT, OUT, verify

verify()
REF = ROOT / 'reference/pokemon-essentials'
files = [json.loads(p.read_text()) for p in sorted(OUT.glob('structure-*.json'))]
catalog = {d['path']: d for d in files}

def ids(path):
    text = (REF / path).read_text(encoding='utf-8-sig')
    return set(re.findall(r'^\[([^]]+)\]', text, re.M))

def all_species(prefix='PBS/'):
    found = ids(prefix+'pokemon.txt')
    for value in ids(prefix+'pokemon_forms.txt'):
        identity, form = value.split(',')
        found.add(identity.strip()+'_'+str(int(form.strip())))
    return found

species = all_species()
items = ids('PBS/items.txt')
moves = ids('PBS/moves.txt')
trainer_types = ids('PBS/trainer_types.txt')
schema_root = REF / 'Data/Scripts/010_Data/001_Hardcoded data'
encounter_types = set(re.findall(r':id\s*=>\s*:(\w+)', (schema_root/'013_EncounterType.rb').read_text()))
relations = []
summary = []
for d in files:
    family = d['family']
    if family == 'encounters':
        profile = pathlib.Path(d['path']).parent.as_posix()+'/'
        defined = all_species(profile)
        methods = []
        for rec in d['records']:
            current = None
            for row in rec['rows']:
                values = [v.strip() for v in row['value'].split(',')]
                if values[0] in encounter_types:
                    current = dict(path=d['path'], section=rec['identity'], line=row['line'],
                        method=values[0], explicit_chance=int(values[1]) if len(values)>1 and values[1] else None,
                        slots=[])
                    methods.append(current)
                else:
                    assert current is not None
                    lo = int(values[2]); hi = int(values[3]) if len(values)>3 else lo
                    slot = dict(line=row['line'], weight=int(values[0]), species=values[1],
                        species_defined=values[1] in defined, minimum=lo, maximum=hi,
                        all_numeric_bounds_valid=int(values[0])>0 and 1<=lo<=hi<=100,
                        fields_supplied=len(values))
                    current['slots'].append(slot)
                    relations.append(dict(path=d['path'],section=rec['identity'],field='encounter_slot',**slot))
        for method in methods:
            method['sum_weights'] = sum(s['weight'] for s in method['slots'])
            method['tuple_duplicates'] = [list(t) for t, n in collections.Counter(
                (s['species'],s['minimum'],s['maximum']) for s in method['slots']).items() if n>1]
        (OUT / ('relations-'+d['path'][4:].replace('/', '--').replace(' ', '_')+'.json')).write_text(
            json.dumps(methods, ensure_ascii=False, indent=2)+'\n')
        summary.append(dict(path=d['path'],records=len(d['records']), methods=len(methods),
            slots=sum(len(m['slots']) for m in methods),weight_sums=sorted(set(m['sum_weights'] for m in methods)),
            undefined=[s for m in methods for s in m['slots'] if not s['species_defined']],
            invalid_numeric=[s for m in methods for s in m['slots'] if not s['all_numeric_bounds_valid']],
            duplicate_tuples=[m for m in methods if m['tuple_duplicates']]))
    elif family == 'regional_dexes':
        for rec in d['records']:
            members = [s.strip() for r in rec['rows'] for s in r['value'].split(',')]
            summary.append(dict(path=d['path'],region=rec['identity'],members=len(members),
                duplicates={s:n for s,n in collections.Counter(members).items() if n>1},
                undefined=[s for s in members if s not in species]))
            for r in rec['rows']:
                for token in r['value'].split(','):
                    relations.append(dict(path=d['path'],section=rec['identity'],line=r['line'],field='ordered_species',
                        token=token.strip(),defined=token.strip() in species))
    elif family == 'trainers':
        for rec in d['records']:
            trainer_identity=rec['identity'].split(',')
            relations.append(dict(path=d['path'],line=rec['start_line'],field='trainer_type',
                token=trainer_identity[0],defined=trainer_identity[0] in trainer_types))
            for field in rec['fields']:
                values=[s.strip() for s in field['value'].split(',')]
                domain = {'Pokemon':species,'Moves':moves,'Item':items,'Items':items,'Ball':items}.get(field['key'])
                if domain is None:
                    continue
                tokens=values[:1] if field['key']=='Pokemon' else values
                for token in tokens:
                    relations.append(dict(path=d['path'],section=rec['identity'],line=field['line'],
                        field=field['key'],token=token,defined=token in domain))
    elif family == 'metadata':
        for rec in d['records']:
            for field in rec['fields']:
                domain={'StartItemStorage':items,'TrainerType':trainer_types}.get(field['key'])
                if domain is not None:
                    for token in field['value'].split(','):
                        relations.append(dict(path=d['path'],section=rec['identity'],line=field['line'],
                            field=field['key'],token=token,defined=token in domain))
    elif family == 'battle_facility_lists':
        for rec in d['records']:
            for field in rec['fields']:
                if field['key'] in ('Trainers','Pokemon'):
                    relations.append(dict(path=d['path'],section=rec['identity'],line=field['line'],
                        field=field['key'],token=field['value'],defined=(REF/'PBS'/field['value']).is_file()))
    elif family == 'phone':
        for rec in d['records']:
            if rec['identity'] != 'Default':
                key=rec['identity'].split(',')
                relations.append(dict(path=d['path'],line=rec['start_line'],field='trainer_type',
                    token=key[0],defined=key[0] in trainer_types))
    elif family == 'map_connections':
        map_metadata=ids('PBS/map_metadata.txt')
        defined_maps={int(x) for x in map_metadata}
        for row in d['unsectioned']:
            values=row['value'].split(',')
            relations.append(dict(path=d['path'],line=row['line'],field='six_components',values=values,
                length_valid=len(values)==6,both_metadata_records_exist=int(values[0]) in defined_maps and int(values[3]) in defined_maps,
                opposite_directions=values[4]=={'N':'S','S':'N','W':'E','E':'W'}[values[1]],actual_map_material='MISSING'))

same_bytes=collections.defaultdict(list)
for d in files:
    same_bytes[d['sha256']].append(d['path'])
summary.append(dict(same_byte_groups=[dict(sha256=h,paths=p) for h,p in same_bytes.items() if len(p)>1]))
bad=[r for r in relations if r.get('defined') is False or r.get('all_numeric_bounds_valid') is False]
(OUT/'special-relations.json').write_text(json.dumps(dict(stage='structure_predicates_only',semantic_approval=False,
    relations=relations,summary=summary,bad=bad),ensure_ascii=False,indent=2)+'\n')
with (OUT/'command-log.jsonl').open('a') as stream:
    stream.write(json.dumps(dict(operation='special_relations.py',reference_commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',
        output='special-relations.json',relations=len(relations),bad=len(bad),exit=0,source_execution=0))+'\n')
print(json.dumps(dict(relations=len(relations),bad=bad,summary=summary),ensure_ascii=False,indent=2))
