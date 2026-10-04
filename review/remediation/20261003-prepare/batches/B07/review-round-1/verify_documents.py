"""R-B07 Git/document bookkeeping only. Never executes reference or behavior cases."""
import collections
import difflib
import hashlib
import json
import pathlib
import re
import subprocess

REPO = pathlib.Path(__file__).resolve().parents[6]
OUT = pathlib.Path(__file__).resolve().parent
BATCH = OUT.parent
BASE = '219cc3c182750155e9dbf2cb619f420b3922de27'
CAND = 'a22df6b1d9465b68e45558c57bc69c61939baeaf'
PLAN = '41fffb540c6483f5296ea0d33b789b75180d27ed'
ORIG = '93e10babe0b9c9ef8b3f5277754541b447beeeb4'
REF = pathlib.Path('/workspace/reference-pokemon-essentials-B07')
REF_SHA = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
results = []
identities = []

def git(*args, root=REPO):
    return subprocess.check_output(['git', '-C', str(root), *args])

def content(commit, path, root=REPO):
    return git('show', commit + ':' + path, root=root)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def canonical(value):
    return sha(json.dumps(value, ensure_ascii=False, sort_keys=True,
                          separators=(',', ':')).encode())

def check(name, passed, evidence):
    results.append({'check': name, 'status': 'PASS' if passed else 'FAIL', 'evidence': evidence})

def json_input(path, commit=CAND):
    return json.loads(content(commit, path))

def verify_identity(record, default=CAND, root=REPO):
    commit = record.get('commit', default)
    data = content(commit, record['path'], root=root)
    actual = {'commit': commit, 'path': record['path'],
              'git_blob': git('rev-parse', commit + ':' + record['path'], root=root).decode().strip(),
              'sha256': sha(data), 'bytes': len(data)}
    ok = all(actual[k] == record[k] for k in ['git_blob', 'sha256', 'bytes'])
    identities.append({**actual, 'claimed_identity_matches': ok})
    return ok

prefix = 'review/remediation/20261003-prepare/batches/B07/'
contract = json_input('review/remediation/20261003-prepare/batches/B04/acceptance-stage-1/downstream-handshake.json', BASE)
inputs = json_input(prefix + 'input-identities.json')
dep = json_input(prefix + 'dependency-manifest.json')
accept = json_input(prefix + 'acceptance-map.json')
sync = json_input(prefix + 'original-sync-plan.json')
source_log = json_input(prefix + 'source-reading-log.json')
orig = json_input('review/global-independent-review/2026-10-03-fd82a639/findings.json', ORIG)
planned = json_input('review/remediation-20261003-prepare/finding-acceptance.json', PLAN)
orig_by_id = {x['id']: x for x in orig}
planned_by_id = planned
check('candidate has exact single parent', git('rev-list', '--parents', '-n', '1', CAND).decode().split() == [CAND, BASE], [CAND, BASE])
check('116 declared inputs match immutable Git bytes', len(inputs['checks']) == 116 and all([verify_identity(x) for x in inputs['checks']]), {'count': len(inputs['checks'])})
groups = [('planned_reads', 'planned_reads'), ('additional_read_only_B04_formal_inputs', 'additional_read_only_B04_formal_inputs'), ('additional_frozen_read_only_evidence', 'additional_frozen_read_only_evidence'), ('current_management_reads', 'current_management_reads'), ('fixed_plan_identities', 'fixed_plan_identities')]
group_results = {}
for author_group, control_group in groups:
    a = [x for x in inputs['checks'] if x['group'] == author_group]
    c = contract[control_group]
    keys = ['path', 'git_blob', 'sha256', 'bytes']
    group_results[author_group] = (len(a) == len(c) and all(all(x[k] == y[k] for k in keys) and x['commit'] == y.get('commit', BASE) for x, y in zip(a, c)))
check('input lists bind to parent authoritative contract', all(group_results.values()), group_results)
check('dependency input identity fields equal independently verified input list', [{k: v for k, v in x.items() if k != 'candidate_relationship'} for x in dep['fixed_input_identities116']] == inputs['checks'], 116)
outputs = dep['outputs14']
output_ok = len(outputs) == 14 and all([verify_identity(x['baseline'], BASE) and verify_identity(x['candidate'], CAND) for x in outputs])
check('14 output before/after identities', output_ok, {'count': len(outputs)})
formal = contract['allowed_formal_write_paths']
original_paths = [x['original_path'] for x in contract['potential_original_sync_contract6']]
changes = [x.split('\t') for x in git('diff', '--name-status', BASE, CAND).decode().splitlines()]
mods = [p for s, p in changes if s == 'M']
adds = [p for s, p in changes if s == 'A']
check('complete unfiltered diff is 8 formal + 6 originals + 11 B07 evidence additions', set(mods) == set(formal + original_paths) and len(mods) == 14 and len(adds) == 11 and all(p.startswith(prefix) for p in adds) and len(changes) == 25, {'changes': changes})
check('author evidence JSON all parses', all([isinstance(json_input(p), (dict, list)) for p in adds if p.endswith('.json')]), [p for p in adds if p.endswith('.json')])
contributions = accept['contributions']
control_by_id = {x['id']: x for x in contract['contribution_controls']}
control_results = []
for x in contributions:
    o = orig_by_id[x['id']]
    a = planned_by_id[x['id']]
    c = control_by_id[x['id']]
    expected_extensions = [{k: e.get(k) for k in ['report', 'raw_id', 'adjudication', 'root_review']} for e in o.get('extensions', [])]
    checks = {
        'original_hash': canonical(o) == x['original_complete_object_sha256'] == c['original_complete_object_sha256'],
        'acceptance_hash': canonical(a) == x['acceptance_object_sha256'] == c['acceptance_object_sha256'],
        'contract_full_original': o == c['complete_original_object'],
        'contract_full_acceptance': a == c['complete_approved_acceptance'],
        'qualifications': x['current_qualifications'] == o.get('current_qualifications'),
        'effective_constraints': x['effective_case_constraints'] == o.get('effective_case_constraints'),
        'root_adjudications': x['root_adjudications'] == o.get('root_adjudications', []),
        'extensions': x['all_extension_controls'] == expected_extensions,
        'ownership': all(x[k] == c[k] for k in ['B07_primary', 'priority', 'primary_owner', 'all_contributors', 'accepted_other_contributors', 'other_contributors_pending'])
    }
    control_results.append({'id': x['id'], 'checks': checks, 'extensions': len(expected_extensions)})
check('19 complete original and plan controls, roots/extensions/qualifications and ownership', len(contributions) == 19 and sum(x['B07_primary'] for x in contributions) == 12 and set(x['id'] for x in contributions) == set(contract['contribution_finding_ids']) and all(all(x['checks'].values()) for x in control_results), control_results)
patch = content(CAND, prefix + 'original-sync.patch')
patch_ok = subprocess.run(['git', '-C', str(REPO), 'apply', '--check', '--reverse', '-'], input=patch, capture_output=True)
sync_results = []
for x in sync['files']:
    p = x['path']
    before = content(BASE, p)
    after = content(CAND, p)
    d = ''.join(difflib.unified_diff(before.decode().splitlines(keepends=True), after.decode().splitlines(keepends=True), fromfile='a/' + p, tofile='b/' + p))
    normalized = ''.join('\n' if line == ' \n' else line for line in d.splitlines(keepends=True))
    part = re.search(r'^--- a/' + re.escape(p) + r'\n.*?(?=^--- a/|\Z)', patch.decode(), re.M | re.S).group(0)
    sync_results.append({'path': p, 'before': sha(before) == x['before_sha256'], 'after': sha(after) == x['after_sha256'], 'diff': sha(normalized.encode()) == x['diff_sha256'] and part.rstrip('\n') == normalized.rstrip('\n'), 'diff_format': 'normalized difflib unified; optional blank context prefix removed; inter-file separator excluded'})
check('six original sync paths/hash-exact hunks and reverse validation without application', len(sync_results) == 6 and set(x['path'] for x in sync_results) == set(original_paths) and all(x['before'] and x['after'] and x['diff'] for x in sync_results) and patch_ok.returncode == 0, {'paths': sync_results, 'reverse_check_returncode': patch_ok.returncode, 'stderr': patch_ok.stderr.decode()})
new_expected = [*(f'IU-{i}' for i in range(49, 60)), 'SH-27', 'SH-28', *(f'GR-{i}' for i in range(45, 54)), 'BE36', 'BE37', *(f'CX{i}' for i in range(39, 43))]
changed_expected = ['SH-08', 'GR-15', *(f'GR-{i}' for i in range(30, 35)), 'CX22']
new_seen, changed_seen, catalog_results = [], [], []
for p in formal[-2:]:
    old = content(BASE, p).decode()
    new = content(CAND, p).decode()
    def rows(s):
        return [(m.group(1), m.group(0)) for m in re.finditer(r'^\| ((?:BG|IU|SH|GR|DC)-\d+|(?:BE|CX|RM|CP)\d+) \|.*$', s, re.M)]
    before, after = rows(old), rows(new)
    old_ids = [i for i, _ in before]
    filtered = [(i, row) for i, row in after if i in old_ids]
    seq_ok = [i for i, _ in filtered] == old_ids
    changed = [i for (i, a), (_, b) in zip(before, filtered) if a != b]
    added = [i for i, _ in after if i not in old_ids]
    changed_seen += changed
    new_seen += added
    protected = {}
    for section in (['BG', 'DC'] if 'creature-rpg' in p else ['RM', 'CP']):
        def section_text(s):
            match = re.search(r'^## ' + section + r'\b.*?(?=^## |\Z)', s, re.M | re.S)
            return match.group(0).encode() if match else b''
        a, b = section_text(old), section_text(new)
        protected[section] = {'equal': a == b, 'sha256': sha(a), 'bytes': len(a)}
    catalog_results.append({'path': p, 'old_sequence_and_occurrences_preserved': seq_ok, 'new_rows': added, 'changed_old_rows': changed, 'protected_sections': protected})
check('catalog new28/changed8, whole old order/duplicates and protected sections', collections.Counter(new_seen) == collections.Counter(new_expected) and collections.Counter(changed_seen) == collections.Counter(changed_expected) and all(x['old_sequence_and_occurrences_preserved'] and all(v['equal'] for v in x['protected_sections'].values()) for x in catalog_results), catalog_results)
reference_origin = git('remote', 'get-url', 'origin', root=REF).decode().strip()
check('reference exact commit/tree/origin and clean checkout', git('rev-parse', 'HEAD', root=REF).decode().strip() == REF_SHA and git('rev-parse', 'HEAD^{tree}', root=REF).decode().strip() == '7589c800b61ba13a13040ed0d686979b80a84fd0' and reference_origin.removesuffix('.git') == 'https://github.com/Maruno17/pokemon-essentials' and not git('status', '--porcelain', root=REF), {'commit': REF_SHA, 'tree': git('rev-parse', 'HEAD^{tree}', root=REF).decode().strip(), 'origin': reference_origin, 'status': git('status', '--porcelain', root=REF).decode()})
source_results = []
for x in source_log['files']:
    data = content(REF_SHA, x['path'], REF)
    n = len(data.decode('utf-8-sig').splitlines())
    seen = []
    for k in ['inspected_ranges', 'remaining_ranges_unread']:
        for a, b in x[k]:
            seen.extend(range(a, b + 1))
    source_results.append({'path': x['path'], 'identity': verify_identity(x, REF_SHA, REF), 'line_count': n == x['line_count'], 'range_partition': sorted(seen) == list(range(1, n + 1))})
check('author reference log identities and line partitions independently verified', all(x['identity'] and x['line_count'] and x['range_partition'] for x in source_results), {'files': len(source_results), 'failed': [x for x in source_results if not all(x[k] for k in ['identity', 'line_count', 'range_partition'])], 'limits': source_log['named_retained_limits']})
trace = content(CAND, prefix + 'traceability.tsv').decode().splitlines()
check('traceability 19 original IDs and control hashes', len(trace) == 20 and set(line.split('\t')[0] for line in trace[1:]) == set(control_by_id) and all(line.split('\t')[5] == canonical(orig_by_id[line.split('\t')[0]]) for line in trace[1:]), {'rows': len(trace) - 1})
dc = subprocess.run(['git', '-C', str(REPO), 'diff', '--check', BASE, CAND], capture_output=True)
check('candidate whitespace check', dc.returncode == 0, dc.stdout.decode() + dc.stderr.decode())
report = {'kind': 'INDEPENDENT_DOCUMENT_AND_GIT_BOOKKEEPING_ONLY', 'candidate': CAND, 'parent': BASE, 'plan': PLAN, 'original_controls': ORIG, 'reference': REF_SHA, 'results': results, 'all_pass': all(x['status'] == 'PASS' for x in results), 'runtime_observations': 0, 'behavior_vectors_executed': 0, 'reference_execution': 0, 'demo_chains_proven': 0, 'limitations': 'Hashes, JSON and row comparisons are document bookkeeping, not reference execution or independent proof of all semantic claims. Authorization source confidence is assessed separately in report.md.'}
(OUT / 'document-checks.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
(OUT / 'verified-identities.json').write_text(json.dumps({'records': identities}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'all_pass': report['all_pass'], 'checks': len(results), 'failed': [x for x in results if x['status'] != 'PASS']}, ensure_ascii=False, indent=2))
