import datetime, hashlib, json, pathlib, subprocess

P = pathlib.Path(__file__).resolve().parent
candidate = P / 'candidate-switch-entry-priority-order.v1.json'
original = candidate.read_bytes()
assert len(original) == 86864
assert hashlib.sha256(original).hexdigest() == '624e4eff02336d7c6f9c5c6b3f6d8b1568baebd1c67c16b590dd463bcd04ba55'
obj = json.loads(original)
unit = obj['sections']['2_complete_inputs_and_actual_read']['complete_source_units'][6]
assert unit['range'] == [136, 277]
raw = subprocess.check_output(['git', '-C', unit['repo'], 'show', unit['commit'] + ':' + unit['path']])
assert len(raw) == unit['bytes']
assert hashlib.sha256(raw).hexdigest() == unit['sha256']
lines = raw.decode().splitlines(keepends=True)
assert ''.join(lines[135:277]) == unit['content']
assert lines[277] == '  end\n'
corrected = dict(unit)
corrected['range'] = [136, 278]
corrected['content'] = ''.join(lines[135:278])
packet = {
    'schema': 'r8-core-entry-priority-source-unit6-structural-clarifier-v1',
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'reader': '/root/core_atomic_reception',
    'candidate_id': obj['id'],
    'original_candidate': {'path': str(candidate), 'bytes': len(original), 'sha256': hashlib.sha256(original).hexdigest(), 'preserved_unchanged': True},
    'exact_pointer': '/sections/2_complete_inputs_and_actual_read/complete_source_units/6',
    'correction': 'The original 136–277 selected unit includes complete pbCalculatePriority but ends at pbPriority return ret, omitting pbPriority closing end. The complete combined structural unit is 136–278. Line 279 closes class Battle and is outside the two-method unit.',
    'added_actual_source_line': {'line': 278, 'text': lines[277]},
    'complete_corrected_source_unit': corrected,
    'scope': 'Structural/source-range correction only. All candidate semantic statements, strongest rebuttal and pending classification remain unchanged. No new finding, vote, context or whole-file read is credited by this supplement. Original source whole-file reading remains the original reader credit.',
    'business_execution': 'NOT_EXECUTED',
    'UPDATE_NOT_STARTED': True,
}
out = P / 'candidate-switch-entry-priority-order.unit6-closure-clarifier.v1.json'
encoded = (json.dumps(packet, ensure_ascii=False, indent=2) + '\n').encode()
out.write_bytes(encoded)
print(json.dumps({'path': str(out), 'bytes': len(encoded), 'sha256': hashlib.sha256(encoded).hexdigest(), 'utc': packet['utc']}, ensure_ascii=False))
