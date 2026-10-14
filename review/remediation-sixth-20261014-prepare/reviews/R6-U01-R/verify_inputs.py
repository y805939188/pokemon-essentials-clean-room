"""Reviewer-owned static checks. No author code or behavioral model is executed."""
import difflib
import hashlib
import json
import pathlib
import re
import shutil
import subprocess

PREP = '469a268b92daed7b4d28d7fd0da75520cbb7228f'
MAIN = '8ea169fbd0f33f378b5d732fd6bea59e854e04a6'
CAND = '0f2bf0318405ab281682023c6cf0a68eabdd73ad'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
P = pathlib.Path('review/remediation-sixth-20261014-prepare')
OUT = pathlib.Path(__file__).resolve().parent
M = P / 'candidates/R6-U01/mirror'
git = lambda *args: subprocess.check_output(['git', *args])
ident = lambda b: {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
                   'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}
checks = []
def check(name, predicate, detail):
    checks.append({'name': name, 'result': 'PASS_TOOL_VALIDATION' if predicate else 'FAIL', 'detail': detail})
    assert predicate, name

prompt = git('show', PREP + ':' + str(P / 'prompts/R6-U01-R.md'))
check('fixed_prompt_full_bytes', ident(prompt) == {'bytes': 253260,
      'sha256': 'b5a05fd0a671414092c59658323b7f4d6219e5b09f84dfb3b4a073bc6e50db3b',
      'git_blob': '354415efbda685b91a2e07f888a1fbdd6e611feb'}, ident(prompt))
contract_bytes = git('show', PREP + ':' + str(P / 'contracts/R6-U01.json'))
contract = json.loads(contract_bytes)
blocks = re.findall(r'```json\n(.*?)\n```', prompt.decode(), re.S)
check('prompt_contract_complete_equality', json.loads(blocks[0]) == contract, 'All fields, including original_full_proposal; no summary substituted')
recovery = json.loads(blocks[1])
common = {k: next(iter(recovery.values()))[k] for k in ['commit', 'report_directory_tree', 'purpose', 'final_binding_refreshed_at']}
for key, row in recovery.items():
    assert all(row[k] == v for k, v in common.items())
    assert row['recovery'] == 'git show ' + row['commit'] + ':review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/' + row['path']
    raw = (P / 'inputs/evidence' / row['path']).read_bytes()
    assert all(ident(raw)[k] == row[k] for k in ident(raw)), key
check('complete_prompt_recovery_metadata', True, {'objects': len(recovery), 'all_metadata_and_cached_bytes_validated': True,
      'semantic_credit': 'Three K proposals and six K decision/counter payloads only; other-domain bodies are not credited as semantic reads'})

inputs = json.loads((P / 'inputs/frozen-inputs.json').read_text())
mirrors = []
source_rows = []
diffs = []
for path in contract['candidate_formal_paths']:
    before = git('show', MAIN + ':' + path)
    formal_row = next(x for x in inputs['formal_materials'] if x['path'] == path)
    check('formal_identity:' + path, all(ident(before)[k] == formal_row[k] for k in ident(before)), ident(before))
    after = git('show', CAND + ':' + str(M / path))
    check('candidate_worktree:' + path, (M / path).read_bytes() == after, ident(after))
    check('original_unchanged:' + path, pathlib.Path(path).read_bytes() == before, 'Actual formal bytes remain fixed main')
    mirrors.append({'formal_path': path, 'candidate_path': str(M / path), 'baseline_commit': MAIN,
                    'candidate_commit': CAND, 'baseline': ident(before), 'candidate': ident(after),
                    'mode': '100644', 'type': 'blob', 'changed': before != after,
                    'baseline_lines': len(before.splitlines()), 'candidate_lines': len(after.splitlines())})
    if before != after:
        diffs.extend(difflib.unified_diff(before.decode().splitlines(True), after.decode().splitlines(True),
                                        fromfile=MAIN + ':' + path, tofile=CAND + ':' + str(M / path)))
    if '/test-catalog/' in path:
        rowid = lambda line: re.match(r'^\|\s*([A-Za-z][\w-]*\d)\s*\|', line)
        old = [(rowid(x).group(1), x) for x in before.decode().splitlines() if rowid(x)]
        new = [(rowid(x).group(1), x) for x in after.decode().splitlines() if rowid(x)]
        new_dict = dict(new)
        check('all_previous_catalogue_rows:' + path, all(new_dict.get(k) == v for k, v in old),
              {'old_rows': len(old), 'new_rows': len(new) - len(old), 'scope': 'Exact old row bytes; not old runtime PASS transfer'})
        check('unique_row_ids:' + path, len(new) == len(new_dict), 'No duplicated new or old vector ID')
for row in json.loads((P / 'candidates/R6-U01/evidence/source-payload-identities.json').read_text()):
    original_row = next(x for x in inputs['source_materials'] if x['path'] == row['path'])
    raw = subprocess.check_output(['git', '-C', '/tmp/r6-u01-r-reference.git', 'show', REF + ':' + row['path']])
    check('source_full_bytes:' + row['path'], all(ident(raw)[k] == original_row[k] == row[k] for k in ident(raw)), ident(raw))
    source_rows.append({'commit': REF, 'tree': '7589c800b61ba13a13040ed0d686979b80a84fd0', 'path': row['path'],
                        'mode': row['mode'], 'type': row['type'], **ident(raw), 'lines': len(raw.splitlines())})
check('seven_changed_two_preserved', sum(x['changed'] for x in mirrors) == 7, [x['formal_path'] for x in mirrors if not x['changed']])
check('formal_tree_protection', git('rev-parse', CAND + ':deliverables/final-specification-set').strip() == git('rev-parse', MAIN + ':deliverables/final-specification-set').strip(), 'All 131 formal files protected')
for span in json.loads((P / 'candidates/R6-U01/evidence/historical-span-preservation.json').read_text()):
    lo, hi = span['baseline_lines']
    data = b''.join(git('show', MAIN + ':' + span['path']).splitlines(True)[lo - 1:hi])
    after = git('show', CAND + ':' + str(M / span['path']))
    check('historical_span:' + span['path'] + ':' + str(lo) + '-' + str(hi),
          data in after and len(data) == span['bytes'] and hashlib.sha256(data).hexdigest() == span['sha256'], span)
for i in range(1, 4):
    for name in [f'findings/independent-K-{i:03d}.json', f'tasks/R6-O/counter-K-{i:03d}.json']:
        row = next(x for x in recovery.values() if x['path'] == name)
        raw = (P / 'inputs/evidence' / name).read_bytes()
        check('original_counter_identity:' + name, all(ident(raw)[k] == row[k] for k in ident(raw)), row)

shared = json.loads((P / 'candidates/R6-U01/evidence/shared-context.json').read_text())
graph = json.loads((P / 'inputs/file-conflict-graph.json').read_text())
dependencies = json.loads((P / 'inputs/dependency-graph.json').read_text())
check('original_shared_edges', shared['file_conflicts']['edges'] == [x for x in graph['edges'] if x.get('from') == 'R6-U01' or x.get('to') == 'R6-U01'], 'Source graph exact U01 slice')
check('original_receivers', shared['file_conflicts']['file_receivers'] == {k: v for k, v in graph['file_receivers'].items() if k in contract['candidate_formal_paths']}, 'No changed receiver set')
check('original_dependency_edges', shared['dependency_graph']['edges'] == [x for x in dependencies['edges'] if 'R6-U01' in json.dumps(x) or any(k in json.dumps(x) for k in contract['required_ids'])], 'No author blocking interbatch edge; integration gates remain')

result = {'evidence': 'TOOL_VALIDATION', 'behavior_execution': 0, 'checks': checks,
          'prompt_identity': ident(prompt), 'contract_identity': ident(contract_bytes),
          'mirrors': mirrors, 'source_payloads': source_rows, 'Ruby_available': shutil.which('ruby'),
          'formal_tree': git('rev-parse', MAIN + ':deliverables/final-specification-set').decode().strip(),
          'read_scope': 'All nine formal files read semantically; full eleven Ruby units plus named complete Shellos PBS records; metadata validation is separate.'}
(OUT / 'static-verification.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
(OUT / 'candidate-diff.patch').write_text(''.join(diffs))
(OUT / 'prompt-recovery-metadata.json').write_text(json.dumps({'common_fields': common,
     'recovery_formula': 'git show <common.commit>:review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/<row.path>',
     'rows': {k: {f: v for f, v in row.items() if f not in common and f != 'recovery'} for k, row in recovery.items()}}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'checks': len(checks), 'all_pass': True, 'mirrors': len(mirrors), 'sources': len(source_rows),
                  'full_prompt_metadata': len(recovery), 'behavior_execution': 0}, ensure_ascii=False))
