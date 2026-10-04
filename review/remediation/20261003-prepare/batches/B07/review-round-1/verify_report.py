"""Validate reviewer documents only; never execute reference or behavioral cases."""
import hashlib
import json
import pathlib
import re
import subprocess

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[5]
REF = pathlib.Path('/workspace/reference-pokemon-essentials-B07')
EXPECTED = 'a22df6b1d9465b68e45558c57bc69c61939baeaf'
LOCK_SHA = '7862ddc6c2c1cc299e83a8821ce134824c6f72657d443397b449cf0f693091c2'
results = []

def check(name, ok, evidence):
    results.append({'check': name, 'status': 'PASS' if ok else 'FAIL', 'evidence': evidence})

def git(*args, root=REPO):
    return subprocess.check_output(['git', '-C', str(root), *args]).decode().strip()

data = json.loads((HERE / 'finding-dispositions.json').read_text())
records = data['records']
expected_ids = 'A020 A024 A026 A039 A040 A041 A043 A044 A045 A046 A047 A048 A049 A050 A051 B008 B013 C003 D023'.split()
check('19 exact IDs, 12 primary, scoped PASS and no closure',
      set(r['id'] for r in records) == {'GIR-FD82-' + x for x in expected_ids}
      and len(records) == 19 and sum(r['B07_primary'] for r in records) == 12
      and all(r['verdict'] == 'PASS_SCOPED' and r['canonical_status'] == 'OPEN'
              and not r['canonical_closure'] for r in records), len(records))
check('independent evidence lock unchanged',
      hashlib.sha256((HERE / 'independent-first-lock.md').read_bytes()).hexdigest() == LOCK_SHA, LOCK_SHA)
logs = json.loads((HERE / 'source-reading-log.json').read_text())
by_path = {r['path']: r for r in logs['files']}
uncovered = []
for r in records:
    for loc in r['independent_reference_locators']:
        for interval in loc['line_ranges'].split(';'):
            low, high = map(int, interval.split('-'))
            covered = any(a <= low <= high <= b for a, b in by_path[loc['path']]['opened_text_ranges'])
            if not covered:
                uncovered.append([r['id'], loc['path'], interval])
check('all cited reference ranges were independently opened', not uncovered, uncovered)
bad_hash = []
for r in logs['files']:
    raw = (REF / r['path']).read_bytes()
    if len(raw) != r['bytes'] or hashlib.sha256(raw).hexdigest() != r['sha256']:
        bad_hash.append(r['path'])
check('own reference log hash/byte identities', not bad_hash, {'files': len(by_path), 'failed': bad_hash})
c003 = next(r for r in records if r['id'] == 'GIR-FD82-C003')
check('C003 four roots/eight extensions retained',
      len(c003['root_adjudications']) == 4 and len(c003['all_extensions_controls']) == 8,
      {'roots':len(c003['root_adjudications']), 'extensions':len(c003['all_extensions_controls'])})
bad_link = []
for path in HERE.glob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
        if not target.startswith(('https://', 'http://')) and not (path.parent / target).is_file():
            bad_link.append([path.name, target])
check('report relative links resolve', not bad_link, bad_link)
json_files = sorted(HERE.glob('*.json'))
for path in json_files:
    json.loads(path.read_text())
events = [json.loads(x) for x in (HERE / 'reading-events.jsonl').read_text().splitlines()]
check('review JSON and reading events parse', True, {'json_files':len(json_files), 'reading_events':len(events)})
receipt = json.loads((HERE / 'model-and-scope-receipt.json').read_text())
check('zero execution and configuration remains UNVERIFIED',
      receipt['actual_effective_configuration'] == 'UNVERIFIED'
      and not receipt['configuration_confirmation_gate_added']
      and all(receipt[k] == 0 for k in ['runtime_observations','behavior_vectors_executed','reference_execution','demo_chains_proven','canonical_closures']),
      receipt['requested_configuration'])
check('report HEAD remains exact candidate before committing', git('rev-parse', 'HEAD') == EXPECTED, git('rev-parse', 'HEAD'))
check('reference exact and clean',
      git('rev-parse', 'HEAD', root=REF) == logs['reference_commit']
      and not git('status', '--porcelain', root=REF), logs['reference_commit'])
prefix = str(HERE.relative_to(REPO)) + '/'
status = git('status', '--porcelain', '--untracked-files=all').splitlines()
bad_status = [line for line in status if not line[3:].startswith(prefix)]
check('only allowed new review directory modified', not bad_status,
      {'paths':len(status),'outside_allowed_paths':bad_status})
result = {'kind':'REVIEW_DOCUMENT_BOOKKEEPING_ONLY','candidate':EXPECTED,
          'results':results,'all_pass':all(r['status'] == 'PASS' for r in results),
          'behavior_vectors_executed':0,'reference_execution':0}
(HERE / 'report-validation.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'all_pass':result['all_pass'],'checks':len(results),
                  'failed':[r['check'] for r in results if r['status'] != 'PASS']}))
raise SystemExit(0 if result['all_pass'] else 1)
