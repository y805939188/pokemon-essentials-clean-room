"""Produce reversible, field-bounded evidence; generation grants no read credit.

This reads Git bytes as data. It never loads Ruby, runs a compiler, or executes a
recovered program. Unselected rule fields are preserved in raw evidence but are
not granted semantic coverage by the projection.
"""
from pathlib import Path
import json
import subprocess
import hashlib
import re
from collections import defaultdict

T = Path(__file__).resolve().parent
OUT = T / 'continuation/pbs-field-binding'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
DB = '/tmp/r8-elr-reception-reference.git'
OUT.mkdir(parents=True, exist_ok=True)

def put(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

packet = json.loads((T / 'evidence/pbs-current/localization-field-contribution.v1.json').read_text())
paths = [x['path'] for k in ['own_six_paths', 'additional_two_complete_prior_receptions', 'remaining_27_paths'] for x in packet[k]]
assert len(paths) == len(set(paths)) == 35
scope = {
    'abilities': ['Name', 'Description'], 'moves': ['Name', 'Description'],
    'items': ['Name', 'NamePlural', 'PortionName', 'PortionNamePlural', 'Description'],
    'types': ['Name'], 'ribbons': ['Name', 'Description'],
    'pokemon': ['Name', 'FormName', 'Category', 'Pokedex'],
    'pokemon_forms': ['Name', 'FormName', 'Category', 'Pokedex'],
    'trainer_types': ['Name'],
}
corpus = {}
for path in sorted((T / 'evidence/primary-reference').glob('*.txt')):
    lines = path.read_text(encoding='utf-8-sig').splitlines()
    for n in range((len(lines)-4)//2):
        for i, field in enumerate(['key', 'value']):
            corpus.setdefault(lines[2*n+4+i], [path.stem, n+1, field])

literals = {}; unique = {}; sources = []; warnings = []; layout = []
for pi, path in enumerate(paths):
    data = subprocess.check_output(['git', '--git-dir='+DB, 'show', R+':'+path])
    ent = subprocess.check_output(['git', '--git-dir='+DB, 'ls-tree', R, '--', path]).decode().split()
    dest = OUT / 'raw' / path
    dest.parent.mkdir(parents=True, exist_ok=True); dest.write_bytes(data)
    family = Path(path).stem.replace('_shadow_pkmn', '')
    fields = scope[family]
    lines = data.decode('utf-8-sig').splitlines()
    rows = []; current = None
    for ln, physical in enumerate(lines, 1):
        if physical.startswith('#') or not physical.strip(): continue
        text = physical.split('#', 1)[0].strip()
        match = re.fullmatch(r'\[(.*)\]', text)
        if match:
            if current is not None: current['end'] = ln-1
            current = {'header': match[1], 'start': ln, 'end': len(lines), 'fields': {}, 'all_required_occurrences': []}
            rows.append(current); continue
        match = re.fullmatch(r'(\w+)\s*=\s*(.*)', text)
        if not match:
            warnings.append([path, ln, 'NONMATCHING_PREPPED_LINE', text]); continue
        key, value = match.groups()
        if key not in fields: continue
        assert current is not None
        current['all_required_occurrences'].append([ln, key, value])
        current['fields'][key] = [ln, value]
        if key not in {'Description', 'Pokedex', 'FormName'} and (',' in value or '\\"' in value):
            warnings.append([path, ln, 'S_FIELD_NEEDS_TOKENIZER_REVIEW', key, value])
    refs = []
    for row in rows:
        semantic = [family, row['header'], {k: (row['fields'][k][1] if k in row['fields'] else None) for k in fields}]
        key = json.dumps(semantic, ensure_ascii=False, separators=(',', ':'))
        if key not in unique:
            ui = len(unique)+1
            fields_ref = {}
            for k, value in semantic[2].items():
                if value is None: fields_ref[k] = None
                elif value in corpus: fields_ref[k] = {'CORPUS_EXACT_LITERAL': corpus[value]}
                else:
                    if value not in literals: literals[value] = 'L'+str(len(literals)+1)
                    fields_ref[k] = {'NEW_LITERAL': literals[value]}
            unique[key] = {'id': ui, 'family': family, 'header': row['header'], 'fields': fields_ref, 'contexts': []}
        item = unique[key]; item['contexts'].append(pi)
        refs.append(item['id'])
        layout.append({'path_index': pi, 'unit': item['id'], **row})
    sources.append({'index': pi, 'path': path, 'commit': R, 'mode': ent[0], 'git_blob': ent[2], 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'lines': len(lines), 'activation': 'TOPLEVEL_DEFAULT_DISCOVERY' if len(Path(path).parts)==2 else 'INACTIVE_BACKUP_REQUIRES_EXPLICIT_VALID_SELECTION', 'required_fields': fields, 'record_count': len(rows), 'ordered_units': refs})

put('sources-and-order.json', sources)
put('raw-required-fields-and-positions.json', layout)
put('unique-necessary-records.json', list(unique.values()))
put('new-literals.json', {v: k for k,v in literals.items()})
put('warnings.json', warnings)
put('generation.json', {'schema': 'gr8-elr-pbs-field-binding/v1', 'source_commit': R, 'paths': len(paths), 'raw_records': len(layout), 'unique_necessary_records': len(unique), 'new_literal_count': len(literals), 'warnings': len(warnings), 'raw_literal_matching_is_reading': False, 'corpus_references_credit': 'PENDING actual complete worker reception; exact equality alone grants zero reading', 'semantics': 'Only required localization raw fields, explicit omission, section identity and activation. Duplicate ordinary fields take last; all occurrences retained separately. s tokenizer warnings require actual review. Forms Name is outside active schema, so raw presence must not imply consumed field. Effective constructor/BASE values in original contribution remain separately received.', 'source_FULL': False, 'business': 'NOT_EXECUTED', 'UPDATE_NOT_STARTED': True})
print(json.dumps({'paths': len(paths), 'records': len(layout), 'unique': len(unique), 'new_literals': len(literals), 'warning_count': len(warnings)}, ensure_ascii=False))
