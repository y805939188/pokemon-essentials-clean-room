"""Reviewer-owned byte/text/hash checks; never imports or executes reference code."""
from pathlib import Path
import hashlib, json, re, subprocess
from decimal import Decimal, localcontext

ROOT = Path('/Users/dingshinn/Desktop/pokemon-framework-reference')
OLD = ROOT / 'review/wp58-wp62-wp38-review-2026-09-30'
PREV = OLD / 'recheck-v2'
OUT = OLD / 'closure-review'
DEL = ROOT / 'review/wp58-wp62-wp38-delivery-2026-09-29'
REF = ROOT / 'reference/pokemon-essentials'
COMMIT = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'

def meta(p):
    b = p.read_bytes()
    return {'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)}

def match(p, d):
    return p.is_file() and meta(p) == {k: d[k] for k in ('sha256', 'bytes')}

def read(p):
    return json.loads(p.read_text())

def save(n, d):
    (OUT/n).write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n')

fixed = read(OUT/'input-manifest.json')
assert len(fixed['inputs']) == 828
assert all(match(ROOT/x['path'], x) and match(OUT/'input-snapshot'/x['path'], x) for x in fixed['inputs'])
prior = []
for name in ['wp58-wp62-wp38-review-2026-09-30/recheck-v2', 'wp58-wp62-wp38-review-2026-09-30', 'wp55-wp57-closure-review-2026-09-29',
             'wp55-wp57-recheck-2026-09-29', 'wp55-wp57-review-2026-09-28',
             'wp52b-wp52c-wp54-recheck-2026-09-28', 'wp52b-wp52c-wp54-review-2026-09-28',
             'wp50-wp51-wp52a-recheck-2026-09-28', 'wp50-wp51-wp52a-review-2026-09-28',
             'wp46-wp47-review-2026-09-27', 'wp42-wp48-wp49-recheck-2026-09-27']:
    d = ROOT/'review'/name
    inp = read(d/'input-manifest.json')['inputs']
    arts = read(d/'final-checks.json')['artifacts']
    bad_s = [x['path'] for x in inp if not match(d/'input-snapshot'/x['path'], x)]
    bad_a = [x['path'] for x in arts if not match(ROOT/x['path'], x)]
    assert not bad_s and not bad_a
    prior.append({'review': name, 'snapshots': len(inp), 'listed_artifacts_excluding_final_checks': len(arts),
                  'changed_snapshots': bad_s, 'changed_artifacts': bad_a})

diffs = []
for p in sorted((PREV/'revision-diffs').glob('*.diff')):
    ls = p.read_text().splitlines(keepends=True)
    base, target = ls[0][4:].strip(), ls[1][4:].strip()
    src = (ROOT/base).read_text().splitlines(keepends=True)
    res, pos, i = [], 0, 2
    while i < len(ls):
        m = re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', ls[i])
        assert m, (p, i)
        start = int(m[1])-1 if int(m[1]) else 0
        res += src[pos:start]; pos = start; i += 1
        while i < len(ls) and not ls[i].startswith('@@ '):
            line = ls[i]; i += 1
            if line.startswith('\\'): continue
            if line[0] in ' -':
                assert src[pos] == line[1:], (p, pos)
                pos += 1
            if line[0] in ' +': res.append(line[1:])
    res += src[pos:]
    exact = ''.join(res).encode() == (ROOT/target).read_bytes()
    assert exact
    diffs.append({'path': str(p.relative_to(ROOT)), **meta(p), 'base': base, 'target': target, 'exact': exact})
assert len(diffs) == 7
save('diff-checks.json', diffs)

selfd = read(DEL/'self-checks.json'); bd = read(DEL/'boundary-checks.json')
embedded = []
for key in ('artifacts', 'backfill_current'):
    for path, d in selfd[key].items():
        embedded.append({'kind': key, 'path': path, 'matches': match(ROOT/path, d)})
scenarios, inline = {}, []
for d in selfd['packages']:
    p = ROOT/d['file']; txt = p.read_text()
    embedded.append({'kind': 'packages', 'path': d['file'], 'matches': match(p, d)})
    count = len(re.findall(r'^\| W\d+ \|', txt, re.M))
    assert count == d['local_checks']['scenarios']
    scenarios[d['package']] = count
    for m in re.finditer(r'\]\(([^)]+\.md)\)（[^`]*`([0-9a-f]{64})`，([\d,]+)字节', txt):
        path, h, n = m.groups(); data = {'sha256': h, 'bytes': int(n.replace(',', ''))}
        inline.append({'file': d['file'], 'target': path, 'matches': match(p.parent/path, data)})
bindings = [{**x, 'matches': match(ROOT/x['sender'], x)} for x in bd['bindings']]
assert all(x['matches'] for x in embedded+inline+bindings)
assert len(inline) == 17 and len(bindings) == 17
registered_json = [x['path'] for x in fixed['manifest_rows'] if x['path'].endswith('.json')]
for p in registered_json: read(ROOT/p)
links = []
for p in list((ROOT/'specs').rglob('*.md'))+[ROOT/'planning/feature-matrix.md']:
    for dest in re.findall(r'\]\(([^)]+)\)', p.read_text()):
        if re.match(r'\w+://', dest) or dest.startswith('#'): continue
        dest = re.sub(r':\d+$', '', dest.strip('<>').split('#')[0])
        if not dest: continue
        assert (p.parent/dest).exists(), (p, dest)
        links.append({'file': str(p.relative_to(ROOT)), 'target': dest})
save('integrity-checks.json', {'prior': prior, 'diffs_exact': len(diffs), 'fixed_inputs_stable': 828,
    'inline_bindings': inline, 'boundary_bindings': bindings, 'embedded_identities': embedded,
    'scenario_counts_only': scenarios, 'registered_JSON_valid': len(registered_json),
    'spec_matrix_links_exist': len(links), 'note': 'Identity/count checks are separate from behavioral conclusions.'})

# Source identity checks are deliberately separate from the ranges actually reread.
source_paths = {x['path'] for x in read(OLD/'source-checks.json')['paths']}
source_paths |= {'reference/pokemon-essentials/'+x['path'] for x in selfd['source_identities']}
sources = []
for path in sorted(source_paths):
    p = ROOT/path; rel = str(p.relative_to(REF))
    blob = subprocess.run(['git', '--no-optional-locks', '-C', str(REF), 'show', COMMIT+':'+rel],
                          capture_output=True, check=True).stdout
    assert blob == p.read_bytes(), path
    sources.append({'path': path, **meta(p), 'commit_blob_equal': True})
assert all(match(REF/x['path'], x) for x in selfd['source_identities'])
save('source-checks.json', {'commit': COMMIT, 'delivery_source_identities': len(selfd['source_identities']),
    'paths': sources, 'note': 'Blob verification only. Reread ranges and judgments are in static-checks.json/report.md.'})

# Two fixed decimal examples only; no executable capture/recording model.
with localcontext() as c:
    c.prec = 70
    y30 = int(Decimal(65536)/(Decimal(255)/Decimal(30))**(Decimal(3)/Decimal(16)))
    y90 = int(Decimal(65536)/(Decimal(255)/Decimal(90))**(Decimal(3)/Decimal(16)))
save('constant-checks.json', {'reference_not_executed': True,
    'R01_status_example': {'raw': '44.85', 'after_status': '112.125', 'correct_floor': 112, 'wrong_early_floor': 110},
    'C01_W07': {'given': 'Full HP, no actual status, modified rate90', 'x_fixed_arithmetic': 90//3,
        'y_for_x30': y30, 'independent_y_for_x90': y90,
        'result': 'CLOSED: v3 now distinguishes full-HP rate90 yielding x30/y43874 from the independent x90/y53910 constant.'}})
head = subprocess.run(['git', '--no-optional-locks', '-C', str(REF), 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True).stdout.strip()
status = subprocess.run(['git', '--no-optional-locks', '-C', str(REF), 'status', '--porcelain'], capture_output=True, text=True, check=True).stdout
assert head == COMMIT and not status
save('reference-checks.json', {'HEAD': head, 'ordinary_git_status': status})
print(json.dumps({'fixed':828, 'manifest':826, 'TSV':730, 'diffs_exact':7, 'prior_snapshots':[x['snapshots'] for x in prior],
    'inline_bindings':len(inline), 'boundary_bindings':len(bindings), 'JSON':len(registered_json), 'links':len(links),
    'source_blobs':len(sources), 'delivery_sources':len(selfd['source_identities']), 'scenarios':scenarios,
    'W07_fullHP_x':30, 'W07_fullHP_y':y30, 'reference_clean':True}, ensure_ascii=False, indent=2))
