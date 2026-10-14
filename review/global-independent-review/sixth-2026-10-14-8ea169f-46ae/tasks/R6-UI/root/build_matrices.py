"""Bind authored semantic facts to exact structural units and public clause IDs.
This is a record compiler, not a semantic validator. Unbound rows remain explicit.
"""
import json
import posixpath
from pathlib import Path

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
BASE = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae'
OUT = BASE / 'tasks/R6-UI/root'
facts = json.loads((OUT / 'behavioral-facts.json').read_text())
for fact in facts:
    fact['spec_path'] = posixpath.normpath(fact['spec_path'])
units = json.loads((OUT.parent / 'structural-inventory.json').read_text())
notes = json.loads((OUT / 'source-semantic-notes.json').read_text())
blocks = json.loads((BASE / 'inventory/formal-block-denominator.json').read_text())

def overlap(a, b):
    return a[0] <= b[1] and b[0] <= a[1]

forward = []
for number, unit in enumerate(units, 1):
    name = unit['path'].removeprefix('Data/Scripts/016_UI/')
    if name not in notes:
        continue
    path = 'reference/pokemon-essentials/' + unit['path']
    matches = [f for f in facts if f['source_path'] == path and overlap(f['source_lines'], [unit['start_line'], unit['end_line']])]
    forward.append({'unit_id': f'UI-UNIT-{number:04}', 'unit': unit, 'semantic_reader': 'R6-UI/root', 'semantic_read_record': notes[name], 'fact_ids': [f['fact_id'] for f in matches], 'facts': [{'fact_id': f['fact_id'], 'fact': f['fact'], 'consumer': f['consumer'], 'spec_path': f['spec_path'], 'spec_lines': f['spec_lines'], 'preconditions': f['preconditions'], 'verdict': f['verdict']} for f in matches], 'review_state': 'AUTHORED_SEMANTIC_FACT_BOUND' if matches else 'BLOCKED_NO_AUTHORED_FACT', 'runtime_verdict': 'NOT_HOST_VERIFIED'})

docs = {f['spec_path'] for f in facts if f['spec_path'].startswith('deliverables/final-specification-set/user-interface/') and Path(f['spec_path']).name.startswith(('wp63', 'wp65', 'wp67'))}
reverse = []
for block in blocks:
    if block['path'] not in docs:
        continue
    matches = [f for f in facts if f['spec_path'] == block['path'] and overlap(f['spec_lines'], [block['start_line'], block['end_line']])]
    # Unmatched headings, scope statements, dependency lists and summary material
    # are retained as reviewed context; they receive no manufactured behavior PASS.
    reverse.append({'clause_id': block['id'], 'spec_path': block['path'], 'spec_lines': [block['start_line'], block['end_line']], 'semantic_reader': 'R6-UI/root', 'read_state': 'FULL_TEXT_READ', 'fact_ids': [f['fact_id'] for f in matches], 'source': [{'path': f['source_path'], 'lines': f['source_lines'], 'consumer': f['consumer'], 'preconditions': f['preconditions']} for f in matches], 'review_state': 'BEHAVIOR_FACT_COMPARISON' if matches else 'CONTEXT_SCOPE_DEPENDENCY_REVIEWED_NO_AUTOMATIC_PASS', 'pending_proposal': 'R6-UI-001' if block['path'].endswith('wp67-a-battle-interaction-and-presentation.md') and overlap([block['start_line'],block['end_line']],[226,228]) else None, 'runtime_verdict':'NOT_HOST_VERIFIED'})

for name, rows in [('forward-matrix.jsonl', forward), ('reverse-matrix.jsonl', reverse)]:
    (OUT / name).write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows))
(OUT / 'matrix-build-status.json').write_text(json.dumps({'forward_rows': len(forward), 'unbound_source_units': sum(r['review_state'].startswith('BLOCKED') for r in forward), 'reverse_rows': len(reverse), 'behavior_fact_bound_clauses': sum(bool(r['source']) for r in reverse), 'context_dependency_rows': sum(not r['source'] for r in reverse), 'semantic_judgment_generated_by_script': False, 'note': 'Each semantic fact and file note was manually authored after reading; script only links IDs/ranges. Context/dependency rows are not source equivalence PASS.'}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_directory':str(OUT), 'forward_rows':len(forward), 'reverse_rows':len(reverse), 'unbound_source_units':sum(not r['fact_ids'] for r in forward)}))
