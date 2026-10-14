"""Review-owned finite object, document delta, row and scope audit.

Reads frozen Git payloads. Never imports author code or executes reference code.
"""
from pathlib import Path
from collections import Counter
import ast, datetime, difflib, hashlib, json, re, subprocess

ROOT = Path(__file__).resolve().parent
REPO = Path('/workspace/pokemon-essentials-clean-room')
OLD = '00b45de642f07cee9953e42f04cce9c35d77346f'
REVIEW = '3ef4854ef43eac92fd1dc57350e4cf6aa160082b'
NEW = '9971fe84896786645cdcda3ab45e5caf7785cabc'
BASE = 'review/remediation-sixth-20261014-prepare/'
PREFIX = BASE + 'candidates/R6-U13/'
TARGET = PREFIX + 'mirror/deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'
COMMANDS = []

def git(*args):
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    p = subprocess.run(['git', *args], cwd=REPO, capture_output=True)
    COMMANDS.append({'argv': ['git', *args], 'cwd': str(REPO), 'utc_start': start,
                     'utc_end': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                     'exit': p.returncode, 'stdout_bytes': len(p.stdout),
                     'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(),
                     'stderr': p.stderr.decode('utf-8')})
    assert p.returncode == 0, p.stderr.decode('utf-8')
    return p.stdout

def digest(b):
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}

def blob(c, p):
    return git('show', c + ':' + p)

def dump(name, data):
    (ROOT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

assert git('rev-parse', NEW + '^{tree}').decode().strip() == '93ebe95d038954fd0dfb14fd07ac2f95a2485baf'
prior_verdict = json.loads(blob(REVIEW, BASE + 'reviews/R6-U13-R/verdict.json'))
assert prior_verdict['candidate_commit'] == OLD and prior_verdict['verdict'] == 'FAIL'
entries = []
for raw in git('ls-tree', '-r', '-z', NEW, '--', PREFIX).split(b'\0'):
    if not raw:
        continue
    metadata, path = raw.decode().split('\t')
    mode, kind, oid = metadata.split()
    b = blob(NEW, path)
    assert mode == '100644' and kind == 'blob' and digest(b)['git_blob'] == oid
    entries.append({'path': path, 'mode': mode, 'type': kind, **digest(b)})
assert len(entries) == 30
dump('candidate-payloads.json', entries)

changes = git('diff', '--name-status', OLD, NEW).decode().splitlines()
assert len(changes) == 18
assert all(z.split('\t')[0] in ['M', 'A'] and z.split('\t')[1].startswith(PREFIX) for z in changes)
full_diff = git('diff', '--unified=3', OLD, NEW, '--', PREFIX)
(ROOT / 'candidate-repair.diff').write_bytes(full_diff)
mirror_changes = [z.split('\t')[1] for z in changes if '/mirror/' in z]
assert mirror_changes == [TARGET]
mirrors = [e for e in entries if '/mirror/' in e['path']]
assert len(mirrors) == 8
bindings = []
for e in mirrors:
    old, new = blob(OLD, e['path']), blob(NEW, e['path'])
    bindings.append({'path': e['path'], 'old': digest(old), 'new': digest(new),
                     'byte_equal': old == new})
assert sum(x['byte_equal'] for x in bindings) == 7
old, new = blob(OLD, TARGET), blob(NEW, TARGET)
old_lines, new_lines = old.decode().splitlines(), new.decode().splitlines()
assert len(old_lines) == len(new_lines)
changed_lines = [i + 1 for i, (a, b) in enumerate(zip(old_lines, new_lines)) if a != b]
assert changed_lines == [40]
assert old_lines[39].startswith('| SF30 |') and new_lines[39].startswith('| SF30 |')
old_cols, new_cols = old_lines[39].split('|'), new_lines[39].split('|')
assert len(old_cols) == len(new_cols) == 5
assert new_cols[2].strip().startswith(old_cols[2].strip())
assert new_cols[3].strip().startswith(old_cols[3].strip())
assert old.split(b'## BP\xef\xbc\x9a', 1)[1] == new.split(b'## BP\xef\xbc\x9a', 1)[1]
dump('delta-and-mirror-bindings.json', {'old_candidate': OLD, 'old_FAIL_report': REVIEW,
     'new_candidate': NEW, 'new_tree': '93ebe95d038954fd0dfb14fd07ac2f95a2485baf',
     'all_changed_paths': changes, 'mirror_bindings': bindings,
     'changed_physical_lines': changed_lines, 'old_SF30': old_lines[39],
     'new_SF30': new_lines[39], 'unchanged_non_SF_suffix': True,
     'unchanged_menu_column_prefixes': True, 'semantic_scope': 'Identity and exact text delta only.'})

catalogue = PREFIX + 'mirror/deliverables/final-specification-set/test-catalog/combat-requirements-wp54-55-56-58.md'
text = blob(NEW, catalogue).decode()
sections = re.split(r'^## ', text, flags=re.M)[1:]
audits = []
for name, count in [('QC', 49), ('WS', 36), ('PA', 32), ('RC', 29), ('SF', 40)]:
    section = new.decode() if name == 'SF' else next(s for s in sections if s.startswith(name + '：'))
    pattern = r'^\| SF\d' if name == 'SF' else r'^\| [QWP]\d'
    raw = [l for l in section.splitlines() if re.match(pattern, l)]
    ids = [l.split('|')[1].strip() for l in raw]
    duplicates = {k: v for k, v in Counter(ids).items() if v > 1}
    assert len(raw) == len(set(ids)) == count and not duplicates
    audits.append({'series': name, 'raw_count': len(raw), 'unique_count': len(set(ids)),
                   'duplicates': duplicates, 'raw_ids': ids})
injected = new_lines + [new_lines[39]]
raw_ids = [l.split('|')[1].strip() for l in injected if l.startswith('| SF')]
assert Counter(raw_ids)['SF30'] == 2
dump('raw-row-audit.json', {'audits': audits,
     'in_memory_duplicate_control': {'SF30_count': 2, 'detected_before_any_index': True},
     'reference_or_author_code_execution': False,
     'scope': 'Review-owned raw text counting and exact changes; no behavioral model.'})

old_history = json.loads(blob(OLD, PREFIX + 'evidence/historical-regression.json'))
new_history = json.loads(blob(NEW, PREFIX + 'evidence/historical-regression.json'))
preserved = ['input', 'fixed_historical_files', 'affected_path_navigation',
             'R3_R4_exact_scopes_read', 'R2_exact_owner_contribution_bindings_read',
             'R2_B13_controls', 'R2_B12_qualified_scope_read', 'denominators_preserved']
assert all(old_history[k] == new_history[k] for k in preserved)
r5 = []
assert len(old_history['R5_exact_scopes_read']) == len(new_history['R5_exact_scopes_read']) == 3
for before, after in zip(old_history['R5_exact_scopes_read'], new_history['R5_exact_scopes_read']):
    assert before['id'] == after['id']
    assert before['qualified_scope'] == after['qualified_scope']
    assert before['binding_blob'] == after['binding_blob']
    assert after['retrieval_transition']['original_failure_cause'] == 'UNKNOWN_NOT_RECONSTRUCTED'
    assert 'did not establish path absence' in after['retrieval_note']
    data = blob(after['source_commit'], after['source_path'])
    assert all(digest(data)[k] == after[k] for k in digest(data))
    entry = git('ls-tree', after['source_commit'], '--', after['source_path']).decode().strip()
    assert entry == after['git_entry']
    r5.append({'id': after['id'], 'commit': after['source_commit'], 'path': after['source_path'],
               'git_entry': entry, **digest(data), 'scope_unchanged': True,
               'prior_failure_cause': 'UNKNOWN_NOT_RECONSTRUCTED'})
scripts = ['bind_history.py', 'verify_candidate.py', 'edit_candidate.py', 'repair-01/check_repair.py']
syntax = []
for p in scripts:
    source = blob(NEW, PREFIX + 'evidence/' + p)
    ast.parse(source.decode())
    syntax.append({'path': PREFIX + 'evidence/' + p, **digest(source),
                   'AST_parse_only': True, 'executed_or_imported': False})
assert b'Original contract path was not present' not in blob(NEW, PREFIX + 'evidence/bind_history.py')
dump('history-delta-audit.json', {'unchanged_qualified_fields': preserved, 'R5': r5,
     'scripts_syntax': syntax, 'old_bad_generator_literal_removed': True,
     'semantic_notes': 'New retrieval wording and tool claims reviewed separately; no prior failure cause reconstructed.'})
assert blob(NEW, 'AGENTS.md') == blob(REVIEW, 'AGENTS.md')
for p in [BASE + 'contracts/R6-U13.json', BASE + 'prompts/R6-U13-R.md']:
    assert blob(NEW, p) == blob(REVIEW, p)
assert git('rev-parse', NEW + ':deliverables/final-specification-set') == git('rev-parse', REVIEW + ':deliverables/final-specification-set')
dump('audit-command-receipts.json', COMMANDS)
dump('root-check-summary.json', {'new_candidate': NEW, 'new_tree': '93ebe95d038954fd0dfb14fd07ac2f95a2485baf',
     'candidate_payload_count': 30, 'candidate_bytes': sum(e['bytes'] for e in entries),
     'changed_paths': 18, 'seven_mirrors_exactly_unchanged': True,
     'one_SF30_line_only': True, 'qualified_history_fields_unchanged': True,
     'current_formal_prompt_contract_AGENTS_unchanged': True,
     'raw_row_counts': {a['series']: a['raw_count'] for a in audits},
     'no_duplicate_catalogue_IDs': True, 'reference_execution': 0,
     'author_script_execution': 0, 'host_execution': 0, 'real_save_load': 0})
print(json.dumps({'payloads': len(entries), 'bytes': sum(e['bytes'] for e in entries),
                  'changed_paths': 18, 'mirror_delta': 'SF30_LINE40_ONLY',
                  'unchanged_other_mirrors': 7, 'errors': 0}))
