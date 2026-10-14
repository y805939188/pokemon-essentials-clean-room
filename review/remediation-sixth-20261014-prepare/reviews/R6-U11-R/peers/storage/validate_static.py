import datetime, difflib, hashlib, json, pathlib, subprocess

ROOT = pathlib.Path('/workspace/pokemon-essentials-clean-room')
OUT = ROOT / 'review/remediation-sixth-20261014-prepare/reviews/R6-U11-R/peers/storage'
PFX = 'review/remediation-sixth-20261014-prepare/'
FROZEN = 'e93d0e56750a6a16cc50cc68b2c97f11ea255153'
CORE = '54af598ca85211641348e6057ed0c348044787fe'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
R = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def git(*args):
    p = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=True)
    return p.stdout

def ident(payload):
    return {'bytes': len(payload), 'lines': len(payload.decode('utf-8').splitlines()), 'sha256': hashlib.sha256(payload).hexdigest(), 'git_blob': hashlib.sha1(b'blob ' + str(len(payload)).encode() + b'\0' + payload).hexdigest()}

started = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = {'schema': 'r6-u11-storage-independent-static-validation.v1', 'utc_start': started, 'cwd': str(ROOT), 'reader': '/root/storage_review', 'evidence_level': 'TOOL_VALIDATION_ONLY', 'candidate_core': CORE, 'publication': FROZEN, 'main': MAIN, 'reference': R, 'head': git('rev-parse', 'HEAD').decode().strip(), 'branch': git('branch', '--show-current').decode().strip(), 'trees': {v: git('rev-parse', v + '^{tree}').decode().strip() for v in [CORE, FROZEN, MAIN, R]}}
assert result['trees'][FROZEN] == '930b677271ddfb2f8833a0deac79d87b6d01c157'
prompt_path = PFX + 'prompts/R6-U11-R.md'
prompt = (ROOT / prompt_path).read_bytes()
result['prompt'] = {'path': prompt_path, **ident(prompt)}
assert result['prompt']['sha256'] == 'bfc9b60c7b006e1fdd2205b55d0cb21198aa4366e0aa4c4c5eecc82aa111e030'
assert result['prompt']['git_blob'] == 'cd1d62ebaec092af61a76918a4abe6c6d41e1e9d'
contract_path = PFX + 'contracts/R6-U11.json'
contract_bytes = (ROOT / contract_path).read_bytes()
contract = json.loads(contract_bytes)
embedded = json.loads(prompt.decode().split('## 本批确定合同')[1].split('```json\n')[1].split('\n```')[0])
assert embedded == contract
result['contract'] = {'path': contract_path, **ident(contract_bytes), 'embedded_semantic_equal': True}
manifest_path = PFX + 'candidates/R6-U11/evidence/candidate-manifest.json'
manifest = json.loads((ROOT / manifest_path).read_bytes())
result['candidate_manifest_payloads'] = []
for record in manifest['files']:
    data = (ROOT / record['path']).read_bytes()
    actual = ident(data)
    expected_equal = all(actual[k] == record[k] for k in ['bytes', 'sha256', 'git_blob'])
    fixed_equal = data == git('show', CORE + ':' + record['path'])
    frozen_equal = data == git('show', FROZEN + ':' + record['path'])
    assert expected_equal and fixed_equal and frozen_equal, record['path']
    result['candidate_manifest_payloads'].append({'path': record['path'], **actual, 'manifest_equal': expected_equal, 'core_equal': fixed_equal, 'publication_equal': frozen_equal, 'git_entry': git('ls-tree', CORE, '--', record['path']).decode().strip()})
result['formal_checks'] = []
for path in ['deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md', 'deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md', 'deliverables/final-specification-set/user-interface/wp17-messages-windows-input.md']:
    original = git('show', MAIN + ':' + path)
    assert (ROOT / path).read_bytes() == original
    result['formal_checks'].append({'path': path, **ident(original), 'work_equal_fixed_main': True})
result['diffs'] = []
for path in ['deliverables/final-specification-set/user-interface/wp66-b-storage-and-pokedex-ui.md', 'deliverables/final-specification-set/test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md']:
    before = git('show', MAIN + ':' + path).decode().splitlines(keepends=True)
    after = (ROOT / (PFX + 'candidates/R6-U11/mirror/' + path)).read_text().splitlines(keepends=True)
    ops = [{'tag': tag, 'formal_lines': [i + 1, j], 'candidate_lines': [a + 1, b]} for tag, i, j, a, b in difflib.SequenceMatcher(None, before, after, autojunk=False).get_opcodes() if tag != 'equal']
    if '/test-catalog/' in path:
        assert all(o['tag'] == 'insert' for o in ops)
    result['diffs'].append({'path': path, 'opcodes': ops, 'test_catalog_all_original_lines_byte_preserved': all(o['tag'] == 'insert' for o in ops) if '/test-catalog/' in path else None})
index = json.loads(prompt.decode().split('## 精确共同证据对象恢复')[1].split('```json\n')[1].split('\n```')[0])
ids = contract['scope_contracts'][0]['bidirectional_evidence']['counter_evidence_ids']
result['counter_payload_checks'] = []
for ev in ids:
    expected = index[ev]
    path = PFX + 'inputs/evidence/' + expected['path']
    payload = (ROOT / path).read_bytes()
    actual = ident(payload)
    ok = all(actual[k] == expected[k] for k in ['bytes', 'sha256', 'git_blob'])
    assert ok, ev
    result['counter_payload_checks'].append({'id': ev, 'path': path, **actual, 'fixed_expected_equal': True, 'semantics_not_implied_by_hash': True})
result['configuration'] = {'requested_model': 'gpt-6.1-sol', 'requested_effort': 'ultra', 'requested_service_tier': 'default', 'requested_speed': 'default', 'effective_model': 'UNVERIFIED', 'effective_effort': 'UNVERIFIED', 'effective_service_tier': 'UNVERIFIED', 'effective_speed': 'UNVERIFIED', 'platform_uuid': 'UNVERIFIED', 'logical_task': '/root/storage_review', 'reason': 'collaboration task identity is visible; no effective configuration or UUID echo and tool has no service-tier argument; no CLI configuration probe used'}
result['reference_execution'] = 0
result['complete_independent_model_execution'] = 0
result['host_Demo_media_real_save_execution'] = 0
result['utc_end'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
result['exit'] = 0
(OUT / 'input-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'exit': 0, 'manifest_files_validated': len(result['candidate_manifest_payloads']), 'counter_payloads_validated': len(result['counter_payload_checks']), 'head': result['head'], 'branch': result['branch'], 'diffs': result['diffs']}, ensure_ascii=False, indent=2))
