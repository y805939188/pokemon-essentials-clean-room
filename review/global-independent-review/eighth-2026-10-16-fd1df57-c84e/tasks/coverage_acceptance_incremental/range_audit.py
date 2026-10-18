"""Read only frozen ledgers and inventory; write mechanical evidence in this task.

No source program is executed. Ranges are declarations, never semantic acceptance.
"""
import collections
import datetime
import hashlib
import json
from pathlib import Path
import re

BASE = Path('/workspace/pokemon-essentials-clean-room/review/global-independent-review/eighth-2026-10-16-fd1df57-c84e')
OUT = BASE / 'tasks/coverage_acceptance_incremental'
PROJECT = Path('/workspace/pokemon-essentials-clean-room')
REFERENCE = Path('/workspace/pokemon-essentials')
READSET = json.loads((BASE / 'delegation/readsets/coverage-incremental-v2.json').read_text())

def merge(ranges):
    result = []
    for start, end in sorted(ranges):
        if result and start <= result[-1][1] + 1:
            result[-1][1] = max(end, result[-1][1])
        else:
            result.append([start, end])
    return result

def complement(length, ranges):
    result, start = [], 1
    for left, right in merge(ranges):
        if left > start:
            result.append([start, left - 1])
        start = max(start, right + 1)
    if start <= length:
        result.append([start, length])
    return result

def ranges(value):
    if isinstance(value, list):
        if len(value) == 2 and all(type(n) is int for n in value):
            return [value]
        return [r for child in value for r in ranges(child)]
    if isinstance(value, dict):
        return [r for key, child in value.items() if key in ('range', 'lines', 'continuous_lines') for r in ranges(child)]
    if isinstance(value, str) and re.fullmatch(r'\s*\d+\s*[-–]\s*\d+(?:\s*[,;/]\s*\d+\s*[-–]\s*\d+)*\s*', value):
        return [[int(a), int(b)] for a, b in re.findall(r'(\d+)\s*[-–]\s*(\d+)', value)]
    return []

inventory = {}
for name, repo, root in [('reference-inventory.json', 'R', REFERENCE), ('formal-inventory.json', 'F', PROJECT)]:
    for entry in json.loads((BASE / 'tasks/inventory_denominator' / name).read_text()):
        path = entry['path']
        raw = (root / path).read_bytes()
        try:
            raw.decode('utf8')
            textual = b'\0' not in raw
        except UnicodeDecodeError:
            textual = False
        inventory[(repo, path)] = {
            'repo': repo, 'path': path, 'bytes': len(raw),
            'sha256': hashlib.sha256(raw).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest(),
            'lines': len(raw.splitlines()) if textual else None,
            'inventory_identity': entry,
        }

def normalize(path):
    if not isinstance(path, str):
        return None
    for prefix, repo in [('R:', 'R'), ('B8:', 'F'), (str(REFERENCE) + '/', 'R'), (str(PROJECT) + '/', 'F')]:
        if path.startswith(prefix):
            candidate = (repo, path[len(prefix):])
            return candidate if candidate in inventory else None
    matches = [key for key in inventory if key[1] == path]
    return matches[0] if len(matches) == 1 else None

RANGE_KEYS = ('ranges_read', 'read_ranges', 'ranges', 'range', 'read_scope', 'read_range',
              'continuous_ranges', 'source_ranges', 'read_intervals', 'continuous_intervals',
              'continuous_read_ranges', 'own_read_range', 'actual_ranges', 'read_windows',
              'continuous_displays')
STATUS_KEYS = ('read_status', 'reading_status', 'status', 'text_status', 'read_grade',
               'semantic_status', 'read_mode', 'coverage', 'credit')
claims, ambiguous = [], []

def walk(value, selector, frozen, inherited_reader, inherited_attribution='INFERRED_TASK_CONTEXT_ONLY'):
    if isinstance(value, list):
        for index, child in enumerate(value):
            walk(child, selector + '/' + str(index), frozen, inherited_reader, inherited_attribution)
    elif isinstance(value, dict):
        identity = value.get('identity', value.get('input', {}))
        if not isinstance(identity, dict):
            identity = {}
        raw_path = value.get('path', value.get('payload', value.get('identity_path', identity.get('path'))))
        key = normalize(raw_path)
        actor_keys=('actual_reader', 'actual_full_reader', 'reader', 'reviewer', 'owner')
        reader = next((value.get(k) for k in actor_keys if isinstance(value.get(k), str)), inherited_reader)
        raw_actor_fields={k:value[k] for k in actor_keys if k in value}
        if any(isinstance(value.get(k),str) for k in actor_keys):
            attribution='EXPLICIT_ACTOR_FIELD'
        elif raw_actor_fields:
            attribution='EXPLICIT_NULL_OR_NONSTRING_ACTOR_NOT_RESOLVED_BY_FALLBACK'
        else:
            attribution=inherited_attribution
        if key:
            chosen = [(name, value[name]) for name in RANGE_KEYS if name in value]
            declared_ranges = merge([r for _, raw in chosen for r in ranges(raw)])
            status = ';'.join(str(value[k]) for k in STATUS_KEYS if k in value)
            flags = {k: value[k] for k in ('own_full_read', 'receiver_own_full_read', 'not_own_full_source_credit', 'full_read', 'dedup_target', 'associate_from', 'same_bytes_as', 'semantic_credit') if k in value}
            negative = bool(re.search(r'UNREAD|NO_CREDIT|INVENTORY_ONLY|TOOL_ONLY|NOT_READ', status))
            associated = (value.get('receiver_own_full_read') is False or value.get('not_own_full_source_credit') is True or bool(value.get('dedup_target')) or bool(value.get('associate_from')) or 'ASSOCIAT' in status or 'BY_PROVIDER_RECEIVED' in status)
            commit = value.get('commit', value.get('frozen_commit', identity.get('commit')))
            eligible = commit in (None, 'WORKTREE', 'fd1df570cad987dc3852a3b958f03916e317f7fe', '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b')
            length = inventory[key]['lines']
            invalid = [r for r in declared_ranges if r[0] < 1 or r[1] < r[0] or (length is not None and r[1] > length)]
            valid = merge([[max(a, 1), min(b, length)] for a, b in declared_ranges if length is not None and a <= b and b >= 1 and a <= length])
            evidence = {name: raw for name, raw in chosen}
            if declared_ranges or status or flags:
                claims.append({'frozen_original_path': frozen['original_path'], 'frozen_snapshot': frozen['snapshot'], 'frozen_sha256': frozen['sha256'], 'captured_utc': frozen['captured_utc'], 'json_pointer': selector, 'repo': key[0], 'path': key[1], 'reader': reader, 'raw_actor_fields':raw_actor_fields,'reader_attribution':attribution,'named_reader_range_eligible':attribution=='EXPLICIT_ACTOR_FIELD','commit': commit, 'eligible_baseline': eligible, 'declared_status': status, 'flags': flags, 'declared_range_fields': evidence, 'declared_ranges': declared_ranges, 'clipped_ranges': valid, 'out_of_bounds': invalid, 'associated_only': associated, 'excluded_by_negative_read_state': negative, 'exact_range_claim_eligible': eligible and not associated and not negative, 'semantic_acceptance_granted_by_this_audit': False})
            else:
                ambiguous.append({'ledger': frozen['original_path'], 'pointer': selector, 'path': key[1], 'reason': 'NO_READING_RANGE_OR_STATE'})
        for child_key, child in value.items():
            if isinstance(child, (dict, list)) and child_key not in ('identity', 'input', 'inventory_identity', 'continuous_displays'):
                walk(child, selector + '/' + child_key, frozen, reader, attribution)

for frozen in READSET['snapshot_entries']:
    path = frozen['original_path']
    if path.endswith(('reading-ledger.json', '/source-reading.json', '/formal-readset.json', '/read-state.json')):
        data = json.loads((BASE / frozen['snapshot']).read_text())
        walk(data, '', frozen, '/root/' + path.split('/')[1])

files = []
for key, entry in inventory.items():
    own = [c for c in claims if (c['repo'], c['path']) == key and c['exact_range_claim_eligible']]
    union = merge([r for c in own for r in c['clipped_ranges']])
    length = entry['lines']
    unread = complement(length, union) if length is not None else None
    state = 'FINITE_BINARY_STRUCTURE_DISPOSITION_REQUIRED' if length is None else ('DECLARED_FULL_RANGE_UNION' if not unread else ('DECLARED_PARTIAL_RANGES' if union else 'NO_EXACT_ELIGIBLE_RANGES'))
    files.append(dict(entry, declared_reading_state=state, declared_range_union=union,
                      declared_readers=sorted({c['reader'] for c in own}),
                      precise_no_declared_read_ranges=unread,
                      claim_count=len(own), all_claims=[i for i,c in enumerate(claims) if (c['repo'], c['path'])==key],
                      accepted_credit='UNVERIFIED_ATOMIC_AND_ALL_CONSUMER_RECEPTION',
                      accepted_full_file_count_credit=0,
                      audit_qualification='MECHANICAL_DECLARED_RANGE_UNION_ONLY; LEDGER_SEMANTICS_NOT_ALL_HAND_READ; NOT_GLOBAL_OR_DOMAIN_ACCEPTANCE'))

# A source line-domain declaration does not prove that raw text was displayed.
# Preserve associated paths and explicit record/field views separately.
for entry in files:
    key = (entry['repo'], entry['path'])
    matching = [c for c in claims if (c['repo'], c['path']) == key]
    entry['same_bytes_or_provider_associations'] = [c for c in matching if c['associated_only']]
    entry['field_or_record_view_declarations'] = [c for c in matching if 'FIELD' in c['declared_status'] or 'RECORD' in c['declared_status']]
    entry['current_actual_full_text_read_total'] = 'UNVERIFIED_REQUIRES_ALL_LEDGER_AND_REAL_IO_RECEPTION'
    entry['current_complete_semantic_file_acceptance'] = 'NOT_ESTABLISHED_BY_THIS_AUDIT; EXISTING_FINITE_RECEIPTS_NOT_REVOKED'
    entry['audit_own_source_or_formal_full_read'] = False
    named_ranges=merge([r for c in matching if c['exact_range_claim_eligible'] and c['named_reader_range_eligible'] for r in c['clipped_ranges']])
    entry['explicitly_named_reader_declared_range_union']=named_ranges
    entry['explicitly_named_reader_no_declared_read_ranges']=complement(entry['lines'],named_ranges) if entry['lines'] is not None else None
    entry['null_or_only_inferred_reader_claims']=[c for c in matching if not c['named_reader_range_eligible']]

result = {'schema':'gr8-incremental-mechanical-file-coverage/v1',
          'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'denominators':{'R':432,'F':131},
          'counts':{repo:dict(collections.Counter(f['declared_reading_state'] for f in files if f['repo']==repo)) for repo in ('R','F')},
          'files': files, 'claims':claims, 'ambiguous_entries':ambiguous,
          'qualification':'This script parses declarations. It provides no actual full ledger/source semantic reading or acceptance credit.',
          'behavior_execution':'NOT_EXECUTED','update_started':False}
(OUT / 'file-coverage.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'counts':result['counts'],'claims':len(claims),'invalid_ranges':[{'ledger':c['frozen_original_path'],'pointer':c['json_pointer'],'path':c['path'],'invalid':c['out_of_bounds']} for c in claims if c['out_of_bounds']], 'ambiguous':len(ambiguous)},ensure_ascii=False,indent=2))
