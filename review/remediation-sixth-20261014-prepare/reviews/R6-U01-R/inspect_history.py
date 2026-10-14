"""Read bounded historical qualifications from immutable remote text payloads."""
import hashlib
import json
import pathlib
import urllib.request

P = pathlib.Path('review/remediation-sixth-20261014-prepare')
E = P / 'candidates/R6-U01/evidence'
OUT = pathlib.Path(__file__).resolve().parent
scratch = pathlib.Path('/tmp/r6-u01-r-history')
scratch.mkdir(exist_ok=True)

def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}

originals = {}
receipts = []
for row in json.loads((E / 'history-input-identities.json').read_text()):
    url = 'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/' + row['commit'] + '/' + row['path']
    target = scratch / pathlib.Path(row['path']).name
    if target.exists():
        data = target.read_bytes()
    else:
        with urllib.request.urlopen(url, timeout=45) as response:
            data = response.read()
        target.write_bytes(data)
    got = identity(data)
    assert all(got[k] == row[k] for k in got), (row['path'], got)
    originals[target.name] = json.loads(data)
    receipts.append({'url': url, 'commit': row['commit'], 'path': row['path'], **got,
                     'scope': 'full-byte validation, selected exact fields read semantically; not entire archive semantic review'})

qualified = json.loads((E / 'historical-qualified-scopes.json').read_text())
legacy = originals['regression-legacy-scope.json']
fourth = originals['regression-fourth-17.json']
checks = []
for section, original_section, key in [('contributions', legacy['contributions'], 'record_key'),
                                       ('GR4', fourth['records'], 'id')]:
    for projection in qualified[section]:
        original = next(x for x in original_section if x[key] == projection[key])
        for field, value in projection.items():
            assert original[field] == value, (section, projection[key], field)
        checks.append({'section': section, 'key': projection[key], 'all_projected_fields_equal_original': True})

boundary = json.loads((E / 'fifth-closure-boundary-projection.json').read_text())
closure = originals['closure-candidate.json']
print('closure boundary fields', list(boundary))
for field, value in boundary.items():
    if field == 'records':
        for record in value:
            original = next(x for x in closure['records'] if x.get('id', x.get('finding_id')) == record.get('id', record.get('finding_id')))
            assert original == record
    else:
        assert closure[field] == value, field
checks.append({'section': 'fifth-selected-closure', 'all_projected_fields_equal_original': True})

report = {'evidence': 'TOOL_VALIDATION', 'source_identities': receipts, 'checks': checks,
          'qualified_scopes': qualified, 'fifth_boundary': boundary,
          'execution_of_reference_or_behavior_model': 0}
(OUT / 'history-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'checks': checks, 'full_byte_payloads': len(receipts)}, ensure_ascii=False))
