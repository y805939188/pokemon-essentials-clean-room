"""Create lossless leaf views with explicit exact-value aliases; grants no read credit."""
from pathlib import Path
import json, hashlib, ast

O = Path(__file__).resolve().parent
T = O.parents[1]
R = T.parents[1]
source = T / 'continuation/06_qualifications_interfaces/readset.complete.json'
d = json.loads(source.read_text())

def leaves(x, path='$'):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from leaves(v, path + '/' + k)
    elif isinstance(x, list):
        for k, v in enumerate(x):
            yield from leaves(v, path + '/' + str(k))
    else:
        yield path, x

def dump(name, obj):
    (O / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

seen, aliases, rows = {}, [], []
for path, value in leaves(d):
    key = json.dumps(value, ensure_ascii=False, sort_keys=True)
    if key in seen:
        aliases.append({'at': path, 'same_value_as': seen[key]})
    else:
        seen[key] = path
        rows.append({'at': path, 'value': value})
(O / 'readset-unique-leaves.jsonl').write_text(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in rows))
dump('readset-exact-value-aliases.json', aliases)

payload = T / 'recovered' / d['target_commit']
constants = []
for p in sorted(payload.glob('*.py')):
    tree = ast.parse(p.read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            constants.append({'file': p.name, 'line': node.lineno, 'value': node.value})
dump('script-string-literals.json', constants)

coverage = d['qualification_obligations']['coverage_full']
groups = {}
for x in coverage['files']:
    scope = {k:v for k,v in x.items() if k not in ['side','path','readsets']}
    key = json.dumps(scope, ensure_ascii=False, sort_keys=True)
    groups.setdefault(key, []).append({k:x[k] for k in ['side','path','readsets'] if k in x})
dump('coverage-purpose-groups.json', [{'qualification': json.loads(k), 'members': v} for k,v in groups.items()])
dump('view-generation.json', {'readset_bytes':len(source.read_bytes()), 'readset_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'unique_leaf_values':len(rows), 'exact_value_aliases':len(aliases), 'script_literals':len(constants),
    'coverage_objects':len(coverage['files']), 'purpose_groups':len(groups), 'semantic_credit':0, 'recovered_code_executed':False})
print(json.dumps(json.loads((O/'view-generation.json').read_text())))
