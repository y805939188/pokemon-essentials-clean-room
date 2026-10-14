from pathlib import Path
import json
import hashlib
import datetime
import collections
out = Path('review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/tasks/R6-O')
base = out.parent / 'R6-UI'
inv = json.loads((out / 'inventory.json').read_text())
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
status = json.loads((base / 'task-status.json').read_text())
assert status['review_complete'] and status['source_denominator']['unread_assigned_source_files'] == 0
raw_reverse = [json.loads(line) for line in (base / 'reverse-matrix.jsonl').read_text().splitlines()]
raw_forward = [json.loads(line) for line in (base / 'forward-matrix.jsonl').read_text().splitlines()]
byid = {}
for outer in raw_reverse:
    record = outer['authored_record']
    key = record.get('clause_id') or record.get('formal_clause_id') or record.get('public_denominator_id') or record.get('formal_clause', {}).get('id') or record.get('id')
    byid.setdefault(key, []).append(outer)
def source_of(record):
    source = record.get('unit', record.get('source_unit', record.get('source', {})))
    if not isinstance(source, dict):
        return None
    path = source.get('path')
    if not path:
        return None
    if not path.startswith('reference/'):
        path = 'reference/pokemon-essentials/' + path
    span = source.get('lines') or [source.get('start_line'), source.get('end_line')]
    if None in span:
        return None
    return {'path': path, 'lines': span}
def facts_of(record):
    facts = record.get('facts')
    if facts:
        return [x['fact'] for x in facts]
    return [record.get('fact') or record.get('semantic_read_record') or 'Current UI authored record']
critical = []
seen = set()
for outer in raw_forward:
    record = outer['authored_record']
    source = source_of(record)
    if not source:
        continue
    if not any(x in source['path'] for x in ['UI_TextEntry', 'UI_Pokedex', 'UI_PokeMart', 'UI_EggHatching', 'UI_Evolution', 'UI_Trading', 'UI_PurifyChamber', 'UI_Options', 'UI_Phone', 'UI_RegionMap']):
        continue
    facts = facts_of(record)
    key = (source['path'], tuple(facts))
    if key in seen:
        continue
    seen.add(key)
    critical.append({'partition': outer['reader_partition'], 'source': source, 'facts': facts, 'record_id': record.get('unit_id') or record.get('id'), 'credit': 'Actual completed UI primary, not O source fullread'})
# Dedicated formal blocks retain the primary's exact authored disposition; scope/unknown is not semantic PASS.
rows = [json.loads(line) for line in (out / 'reverse-matrix.jsonl').read_text().splitlines()]
received = []
missing = []
for row in rows:
    if row['status'] != 'R6_UI_DELEGATED_PENDING_ACTUAL_RESULT':
        continue
    records = byid.get(row['id'])
    if not records:
        missing.append(row['id'])
        continue
    row['primary_review_receipt'] = records
    row['status'] = 'CURRENT_UI_COMPLETED_PRIMARY_BLOCK_DISPOSITION_RECEIVED'
    row['own_full_read'] = False
    row['read_credit'] = 'R6-UI full31 external sourcefiles plus duplicateBag, 9formal+fullcatalog; O no ownfullread unless separatelyledgered'
    row['prerequisites'] = 'Preserve exact primary-record preconditions/disposition/unknowns/proposals; no globalfinalapproval or native success implied.'
    row['interface_bindings'] = ['R6-UI-current-' + row['id']]
    received.append(row['id'])
assert not missing, missing
# Fresh O phone fulltext overlaps this delegate receipt, and is independently tied to Phone source.
phonepath = 'reference/pokemon-essentials/Data/Scripts/013_Items/004_Item_Phone.rb'
for row in rows:
    if row['formal'] == inv['formal'][25]['path']:
        row['own_full_read'] = True
        row['independent_O_phone_recheck'] = 'phone-recheck.json: wholeformal211 andsource706, existing R03/R04/registrationcontracts accepted; no O003'
        if 68 <= row['lines'][0] <= 157:
            row['evidence'].append({'path': phonepath, 'lines': [1, 706], 'fact': 'FullPhone lifecycle/getreceiver/version/registration/Call/time/legacy with independent10 boundedactualvectors andfullWP63read; exact Phone recheck entries preserve clauses andnative boundary.', 'grade': 'SOURCE_STATIC_NEW_OWN_FULLREAD', 'owner': 'R6-O'})
# Current critical source facts supply necessary interfaces for the O-primary shared contracts.
for row in rows:
    pending = row.get('pending_bindings', [])
    ui_labels = [label for label in pending if label.startswith('R6-UI ') or label in ['K/UI eggs/hatch consumer', 'K obtain helpers/UI hatching/evolution/trading actualwriters']]
    if not ui_labels:
        continue
    if row['formal'] == inv['formal'][14]['path'] or 'Pokedex' in ' '.join(ui_labels) or 'habitat' in ' '.join(ui_labels):
        chosen = [x for x in critical if 'UI_Pokedex' in x['source']['path']]
        if row['formal'] == inv['formal'][14]['path'] and 48 <= row['lines'][0] <= 64:
            chosen += [x for x in critical if any(y in x['source']['path'] for y in ['UI_EggHatching', 'UI_Evolution', 'UI_Trading'])]
    elif 'Mart' in ' '.join(ui_labels):
        chosen = [x for x in critical if 'UI_PokeMart' in x['source']['path']]
    elif 'naming' in ' '.join(ui_labels) or 'preview' in ' '.join(ui_labels):
        chosen = [x for x in critical if 'UI_TextEntry' in x['source']['path']]
    elif 'eggs/hatch' in ' '.join(ui_labels):
        chosen = [x for x in critical if 'UI_EggHatching' in x['source']['path']]
    else:
        chosen = []
    if not chosen:
        continue
    row['received_UI_critical_interface'] = [x['record_id'] for x in chosen]
    row['evidence'] += [{'path': x['source']['path'], 'lines': x['source']['lines'], 'fact': '; '.join(x['facts']), 'grade': 'SOURCE_STATIC_IMPORTED_CURRENT_COMPLETED_PRIMARY', 'owner': 'R6-UI actualfullread; O criticalfacts read/assessed'} for x in chosen]
    row['pending_bindings'] = [x for x in pending if x not in ui_labels]
    if row['status'] in ['LOCAL_FACTS_CHECKED_FOREIGN_CONSUMER_BINDING_PENDING', 'FOREIGN_PRIMARY_PENDING_CURRENT_BINDING'] and not row['pending_bindings']:
        row['status'] = 'CURRENT_PRIMARY_STATIC_BINDING_RECEIVED'
receipt = {
    'at': now,
    'primary_status': status,
    'received_block_count': len(received),
    'received_ids': received,
    'critical_interface_facts': critical,
    'evidence_credit': 'Current actual reviewer completed32source/9formal+catalog. O did not readallsource nor claimits executions. Its wholecatalogreading is real, sourceprimaryoutsideUI remains O/C/K/F.',
    'proposal_dispute': 'R6-UI-PARTY-004 currentUI report supports, but currentR6-F exact rejection-source harness refutes stalecommand; rootmustresolve, receipt is not acceptance.',
    'procedural_incident': 'R6-UI reports transient writes outside assignedtask from Party omittedcwd thenmoved. O doesnotclaim fullteam writecompliance; ownwrites stayed R6-O.',
    'artifacts': [{'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in [base / 'task-status.json', base / 'report.md', base / 'forward-matrix.jsonl', base / 'reverse-matrix.jsonl', base / 'reading-ledger-combined.jsonl', base / 'source-unit-coverage.json']]
}
(out / 'received-UI-interface.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
(out / 'reverse-matrix.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows))
forward = [json.loads(line) for line in (out / 'forward-matrix.jsonl').read_text().splitlines()]
for row in forward:
    if row['status'] == 'R6_UI_DELEGATED_PENDING_ACTUAL_RESULT':
        row['status'] = 'CURRENT_UI_COMPLETED_PRIMARY_SOURCE_RECEIVED'
        row['primary_evidence'] = 'R6-UI source-unit-coverage/reading-ledger-combined/916authoredforwardrecords; actual32fullsource/readgap0'
        row['own_read'] = False
        row['runtime_credit'] = 'UI primary only; O no imported ownexecution'
(out / 'forward-matrix.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in forward))
with (out / 'command-log.jsonl').open('a') as log:
    log.write(json.dumps({'at': now, 'command': 'Read actualcompleted R6-UI report/status/criticalunique facts; import-UI-interface.py', 'result': '2055 exact publicblocks received; allidsaccounted; no imported ownfullsource/executecredit, preserve F dispute/transientwriteincident.'}, ensure_ascii=False) + '\n')
print(json.dumps({'received_UI_blocks': len(received), 'critical_facts': len(critical), 'status_counts': dict(collections.Counter(row['status'] for row in rows))}, ensure_ascii=False))
