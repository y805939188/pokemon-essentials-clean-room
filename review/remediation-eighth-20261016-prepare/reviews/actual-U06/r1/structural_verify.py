#!/usr/bin/env python3
"""Static metadata checks only; grants no semantic or execution credit."""
import collections
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent
RR = 'review/global-independent-review/eighth-2026-10-16-fd1df57-c84e'
R8 = 'review/remediation-eighth-20261016-prepare'
ACTUAL = '0eee6d141f33758eda34bd8ebad94a3e2b617f5a'
BINDING = '5ff355c53b73171a0277c95af97e1cbd40eb8b28'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def load(path, commit=ACTUAL):
    return json.loads(git('show', f'{commit}:{path}'))

def sha(data):
    return hashlib.sha256(data).hexdigest()

manifest = load(f'{R8}/integration/U06/actual-review-input.json', BINDING)
batch = manifest['batches'][0]
expected = batch['required_ids'] + batch['selected_optional_ids']
contracts = load(f'{RR}/handoff/contracts.zh.json')
readset = load(f'{RR}/handoff/batches/R8-U06/readset.json')
dispositions = load(f'{R8}/candidates/R8-U06/evidence/dispositions.json')
candidate_result = load(batch['candidate_review_result_path'])
changes = load(f'{R8}/integration/U06/actual-changes.json')

alignment = []
for item in readset['contracts']:
    value = contracts
    for part in item['pointer'].strip('/').split('/'):
        value = value[int(part)] if isinstance(value, list) else value[part]
    alignment.append({'id': item['id'], 'pointer': item['pointer'],
                      'resolved_id': value.get('id'),
                      'identity_matches': value.get('id') == item['id'],
                      'semantic_read': False})

target_links = []
anchors = []
for path in batch['actual_target_paths']:
    text = git('show', f'{ACTUAL}:{path}').decode()
    ids = re.findall(r'<a\s+id="([^"]+)"\s*>', text)
    counts = collections.Counter(ids)
    anchors.append({'path': path, 'explicit_anchor_counts': dict(counts),
                    'duplicate_explicit_anchors': [key for key, n in counts.items() if n > 1]})
    for match in re.finditer(r'\[[^\]]*\]\(([^)]+)\)', text):
        href = match.group(1)
        if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', href) or href.startswith('#'):
            continue
        clean = href.split('#', 1)[0].split('?', 1)[0]
        relative = PurePosixPath(path).parent / clean
        normalized = []
        for part in relative.parts:
            if part == '..':
                normalized.pop()
            elif part != '.':
                normalized.append(part)
        dest = '/'.join(normalized)
        result = subprocess.run(['git', 'cat-file', '-e', f'{ACTUAL}:{dest}'], cwd=ROOT,
                                capture_output=True)
        target_links.append({'source': path, 'line': text[:match.start()].count('\n') + 1,
                             'href': href, 'resolved_path': dest, 'exists': result.returncode == 0,
                             'qualification': 'FILE_EXISTENCE_ONLY; section meaning not reviewed'})

datasets = {'manifest': expected,
            'readset_contracts': [x['id'] for x in readset['contracts']],
            'author_dispositions': [x['id'] for x in dispositions['records']],
            'candidate_results': [x['id'] for x in candidate_result['records']],
            'actual_changes': [x['id'] for x in changes['records']]}
result = {
    'schema': 'r8-u06-actual-structural-checks/v1',
    'qualification': 'TOOL_VALIDATION_ONLY_NO_SEMANTIC_PASS',
    'artifact_commit': ACTUAL, 'input_binding_commit': BINDING,
    'record_sets': datasets,
    'all_record_sets_exact_14_ids': all(set(v) == set(expected) and len(v) == 14 for v in datasets.values()),
    'contract_pointer_alignment': alignment,
    'relative_markdown_links': target_links,
    'all_relative_markdown_file_targets_exist': all(x['exists'] for x in target_links),
    'explicit_anchor_inventory': anchors,
    'duplicate_explicit_anchor_total': sum(len(x['duplicate_explicit_anchors']) for x in anchors),
    'candidate_report_declared_pass': candidate_result['summary']['candidate_PASS'],
    'candidate_report_bound_candidate': candidate_result['candidate_commit'],
    'candidate_review_eligibility_confirmed': False,
    'candidate_or_author_full_read_credit_transferred': False,
    'actual_integrated_PASS': False,
    'business_execution': 'NOT_EXECUTED',
}
(OUT / 'structural-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['all_record_sets_exact_14_ids',
      'all_relative_markdown_file_targets_exist', 'duplicate_explicit_anchor_total']}, ensure_ascii=False))
