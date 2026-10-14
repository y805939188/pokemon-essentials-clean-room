"""Compile existing authored review records; do not create semantic PASS verdicts."""
import json
from pathlib import Path

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
BASE = ROOT / 'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae'
OUT = BASE / 'tasks/R6-UI'
binding = json.loads((OUT / 'input-binding.json').read_text())
units = json.loads((OUT / 'structural-inventory.json').read_text())
blocks = json.loads((BASE / 'inventory/formal-block-denominator.json').read_text())

def rows(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]

def source_record(row):
    value = row.get('unit') or row.get('source') or row.get('source_unit')
    if not value:
        return None
    path = value.get('path')
    if path and path.startswith('Data/Scripts/'):
        path = 'reference/pokemon-essentials/' + path
    span = value.get('lines') or ([value['start_line'], value['end_line']] if 'start_line' in value else None)
    return (path, span) if span else None

all_forward, all_reverse = [], []
for owner in ['root', 'party', 'storage', 'bag']:
    for row in rows(OUT / owner / 'forward-matrix.jsonl'):
        all_forward.append({'reader_partition':owner,'authored_record':row})
    for row in rows(OUT / owner / 'reverse-matrix.jsonl'):
        all_reverse.append({'reader_partition':owner,'authored_record':row})

coverage = []
for i, unit in enumerate(units, 1):
    path = 'reference/pokemon-essentials/' + unit['path']
    matches = []
    for row in all_forward:
        source = source_record(row['authored_record'])
        if source and source[0] == path and source[1][0] <= unit['end_line'] and unit['start_line'] <= source[1][1]:
            matches.append({'partition':row['reader_partition'],'record_id':row['authored_record'].get('unit_id') or row['authored_record'].get('id'),'matrix':row['reader_partition']+'/forward-matrix.jsonl'})
    coverage.append({'structural_unit_id':f'UI-STRUCT-{i:04}', 'unit':unit, 'authored_semantic_records':matches,'binding_status':'BOUND_TO_EXISTING_REVIEW_RECORD' if matches else 'BLOCKED_UNBOUND', 'automatic_semantic_verdict':False})

def clause_id(row):
    if 'clause_id' in row:
        return row['clause_id']
    if 'formal_clause_id' in row:
        return row['formal_clause_id']
    if row.get('public_denominator_id'):
        return row['public_denominator_id']
    if isinstance(row.get('formal_clause'),dict):
        return row['formal_clause'].get('id')
    return None

bound_clause_ids = {clause_id(x['authored_record']) for x in all_reverse}
primary_paths = {x['path'] for x in binding['formal_inventory'] if '/user-interface/' in x['path']}
primary_blocks = [x for x in blocks if x['path'] in primary_paths]
missing = [x for x in primary_blocks if x['id'] not in bound_clause_ids]

for name, values in [('forward-matrix.jsonl',all_forward),('reverse-matrix.jsonl',all_reverse)]:
    (OUT / name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in values))
(OUT / 'source-unit-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
result = {'source_files':len(binding['source_inventory']),'source_lines':sum(x['lines'] for x in binding['source_inventory']),'structural_units':len(units),'unbound_structural_units':sum(not x['authored_semantic_records'] for x in coverage),'primary_formal_files':len(primary_paths),'primary_formal_lines':sum(x['lines'] for x in binding['formal_inventory'] if x['path'] in primary_paths),'public_primary_clause_denominator':len(primary_blocks),'missing_primary_reverse_clause_ids':missing,'authored_forward_records':len(all_forward),'authored_reverse_records':len(all_reverse),'semantic_verdicts_produced_by_compiler':0,'test_catalog_whole_read':'root delivery+separate semantic ledger; per-line bindings tracked separately, external ownership retained'}
(OUT / 'assembly-validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
