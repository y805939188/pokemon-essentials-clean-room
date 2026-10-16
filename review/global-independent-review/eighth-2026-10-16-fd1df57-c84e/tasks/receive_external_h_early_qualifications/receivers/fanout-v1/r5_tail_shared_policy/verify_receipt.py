"""Check finite receipt conservation and scope, never semantic truth or runtime."""
import json
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parent
repo = Path('/workspace/pokemon-essentials-clean-room')

def read(name):
    return json.loads((root / name).read_text())

freeze = read('frozen-units.json')
ledger = read('reception-ledger.json')
interfaces = read('interfaces.json')
pending = read('unreceived.json')
progress = read('progress.json')
required = set(freeze['required_outputs'])
assert all((root / name).is_file() for name in required)
ids = freeze['primary_semantic_population']['R5_ids']
criteria = freeze['primary_semantic_population']['R5_criteria']
assert len(ids) == len(set(ids)) == 12
assert len(criteria) == len(set(criteria)) == 78
assert {r['id'] for r in ledger['primary']} == set(ids)
assert {r['id'] for r in ledger['criteria']} == set(criteria)
assert sum(len(r['criteria']) for r in ledger['primary']) == 78
assert {r['primary'] for r in ledger['criteria']} == set(ids)
assert len(ledger['nonmandatory14']) == 14
assert sum(r['original_disposition'] == 'optional' for r in ledger['nonmandatory14']) == 7
assert sum(r['original_disposition'] == 'no_required_revision' for r in ledger['nonmandatory14']) == 7
assert len(ledger['policy6']) == 6
assert len(ledger['limits13']['ids']) == 13
assert len(interfaces['shared21']) == 21
assert len(interfaces['dependency18']) == 18
external = {r['id'] for r in interfaces['external_producers']}
assert len(external) == 80 and not external.intersection(ids)
assert {r['id'] for r in pending['external_primary_receipts_not_received']} == external
assert all(r['state'] == 'OPEN_NO_CURRENT_RECEIPT' for r in interfaces['external_producers'])
assert len(pending['shared_compositions_not_finally_signed']) == 21
assert len(pending['dependency_compositions_not_finally_signed']) == 18
assert progress['task_final_READY'] is False and pending['task_final_READY'] is False
assert progress['behavior_execution'] == ledger['new_behavior_execution'] == 0
assert ledger['UPDATE_NOT_STARTED'] and interfaces['UPDATE_NOT_STARTED'] and pending['UPDATE_NOT_STARTED']
assert read('findings.json')['new_confirmed_B8_required_findings'] == []
assert len(read('findings.json')['independent_reception_adjudications']) == 2
longs = read('evidence/long-value-associations.json')
assert longs['unique_texts'] == longs['path_text_pairs'] == 28
assert longs['occurrences'] == 48
assert all(r['B8_exact_match'] for r in longs['rows'])

base = freeze['output_base_commit']
prefix = str(root.relative_to(repo)) + '/'
changed = subprocess.check_output(['git', '-C', str(repo), 'diff', '--name-only', base, '--']).decode().splitlines()
untracked = subprocess.check_output(['git', '-C', str(repo), 'ls-files', '--others', '--exclude-standard']).decode().splitlines()
assert all(p.startswith(prefix) for p in changed + untracked), (changed, untracked)
assert subprocess.check_output(['git', '-C', str(repo), 'branch', '--show-current']).decode().strip() == freeze['publication_branch']
print('TOOL_VALIDATION: 12/78 exact sets,14/6/13 boundaries,80/21/18 OPEN differences,28/48 associations,exclusive writes preserved; behavior execution 0')
