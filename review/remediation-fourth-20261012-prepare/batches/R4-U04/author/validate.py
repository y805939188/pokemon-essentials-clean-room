"""R4-U04 integrity/scope validation only; no behavior/reference/model execution."""
import hashlib
import json
import platform
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
AUTHOR = Path(__file__).resolve().parent
PREP = ROOT / 'review/remediation-fourth-20261012-prepare'
BASE = '1f36475d22120a0d1175967d5b17d71fe8311d88'
START = '08a57fb55118914a74ac1ffaf617647c01df8938'
REFERENCE_STORE = Path('/tmp/r4-u04-reference.git')


def git(*args, source=False):
    return subprocess.check_output(
        ['git', '-C', str(REFERENCE_STORE if source else ROOT), *args]
    )


def identity(path, data):
    return {
        'path': path,
        'bytes': len(data),
        'sha256': hashlib.sha256(data).hexdigest(),
        'git_blob': subprocess.check_output(
            ['git', 'hash-object', '--stdin'], input=data
        ).decode().strip()
    }


def section(text, start, end):
    return text[text.index(start):text.index(end, text.index(start))]


started = datetime.now(timezone.utc).isoformat()
contract = json.loads((PREP / 'tasks/R4-U04/batch-contract.json').read_text())
scope = json.loads((PREP / 'tasks/R4-U04/read-scope.json').read_text())
allowed = set(contract['allowed_formal_write_paths'])
evidence_root = AUTHOR.relative_to(ROOT).as_posix() + '/'
tracked = set(git('diff', '--name-only', START, '--').decode().splitlines())
untracked = set(git('ls-files', '--others', '--exclude-standard').decode().splitlines())
changed = sorted(tracked | untracked)
assert changed and all(p in allowed or p.startswith(evidence_root) for p in changed), changed
assert {p for p in changed if p.startswith('deliverables/')} == allowed
subprocess.run(['git', '-C', str(ROOT), 'diff', '--check'], check=True)

source_records = []
for anchor in scope['source']:
    data = git('show', anchor['commit'] + ':' + anchor['path'], source=True)
    item = identity(anchor['path'], data)
    assert {k: item[k] for k in anchor['identity']} == anchor['identity']
    source_records.append(item)

formal_before, formal_after = [], []
for path in sorted(allowed):
    before = git('show', BASE + ':' + path)
    assert before == git('show', START + ':' + path)
    formal_before.append(identity(path, before))
    formal_after.append(identity(path, (ROOT / path).read_bytes()))

wp28, catalog = contract['allowed_formal_write_paths']
old = git('show', BASE + ':' + wp28).decode()
new = (ROOT / wp28).read_text()
pp_old = section(old, '### 5.2 PP 与 PP 成长', '### 5.3 EV 与培养')
pp_new = section(new, '### 5.2 PP 与 PP 成长', '### 5.3 EV 与培养')
assert pp_old[pp_old.index('- PPUP/PPMAX：'):] == pp_new[pp_new.index('- PPUP/PPMAX：'):]
reconstructed = new.replace(pp_new, pp_old, 1).replace(
    '| PP | ETHER/MAXETHER/ELIXIR/MAXELIXIR/LEPPABERRY |',
    '| PP | ETHER/MAXETHER/ELIXIR/MAXELIXIR/LEPPA |', 1)
assert reconstructed.encode() == old.encode(), 'WP28 changed beyond PP clause and identity row'

old_cat = git('show', BASE + ':' + catalog).decode()
new_cat = (ROOT / catalog).read_text()
old_iu07 = next(line for line in old_cat.splitlines() if line.startswith('| IU-07 |'))
new_iu07 = next(line for line in new_cat.splitlines() if line.startswith('| IU-07 |'))
added = section(new_cat, '### R4-U04 主动 PP 补给', '## SH：')
assert new_cat.replace(added, '', 1).replace(new_iu07, old_iu07, 1).encode() == old_cat.encode()
ids = [line.split('|')[1].strip() for line in added.splitlines() if line.startswith('| R4-U04-PP')]
assert ids == [f'R4-U04-PP{i:02}' for i in range(1, 8)]
for line in pp_new.splitlines():
    if line.startswith('|'):
        assert len(line.split('|')) == 6, 'PP table column integrity'
for line in added.splitlines():
    if line.startswith('|'):
        assert len(line.split('|')) == 5, 'vector table column integrity'

formal_paths = git('ls-tree', '-r', '--name-only', START, '--', 'deliverables/final-specification-set').decode().splitlines()
preserved_formal = [p for p in formal_paths if p not in allowed]
assert len(formal_paths) == 131
for path in preserved_formal:
    assert (ROOT / path).read_bytes() == git('show', BASE + ':' + path)

parsed = []
for path in sorted(AUTHOR.rglob('*.json')):
    json.loads(path.read_text())
    parsed.append(path.relative_to(ROOT).as_posix())
result = {
    'evidence_level': 'TOOL_VALIDATION',
    'status': 'SUCCESS_INTEGRITY_AND_SCOPE_ONLY',
    'behavior_execution_status': 'NOT_EXECUTED_THIS_UPDATE',
    'command': 'python review/remediation-fourth-20261012-prepare/batches/R4-U04/author/validate.py',
    'versions': {'python': platform.python_version(), 'git': git('--version').decode().strip()},
    'started_at': started, 'finished_at': datetime.now(timezone.utc).isoformat(),
    'exit_code': 0,
    'input_commit': START, 'input_tree': git('rev-parse', START + '^{tree}').decode().strip(),
    'formal_base': BASE,
    'reference_commit': scope['reference_commit'],
    'source_full_byte_identities_checked': source_records,
    'formal_before': formal_before, 'formal_after_working_bytes': formal_after,
    'whole_delta_allowlist': {'allowed_formal': sorted(allowed), 'allowed_evidence_prefix': evidence_root, 'checked_changed_paths': changed, 'outside_scope': []},
    'preservation_checks': {
        'other_129_formal_files_match_B_complete_bytes': True,
        'WP28_reconstructed_B_exactly_after_reverting_PP_change_and_identity_row': True,
        'PPUP_PPMAX_and_battle_sync_original_bytes': True,
        'catalog_reconstructed_B_exactly_after_reverting_IU07_and_new_vector_section': True,
        'existing_IU_except_IU07_and_U03_IF_and_all_other_catalog_content': True,
        'protected_reference_delivery_old_reports_main_not_modified_by_delta': True
    },
    'json_files_parsed': parsed,
    'vector_id_and_table_structure_checked': ids,
    'side_effects': ['write author/validation.json only; read local git objects and formal/source bytes'],
    'limits': ['No vector evaluated by this script; no reference, behavior model, UI, host, or Demo executed.', 'Author validation is not independent candidate/actual PASS or acceptance.']
}
(AUTHOR / 'validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'status': result['status'], 'changed_paths': changed, 'source_files': len(source_records), 'unchanged_formal_files': len(preserved_formal), 'behavior_execution_status': result['behavior_execution_status']}, ensure_ascii=False))
