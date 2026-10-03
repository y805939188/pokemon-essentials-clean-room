"""Independent text/identity checks only; never imports reference code."""
from pathlib import Path
import collections
import hashlib
import json
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
AUTHOR = ROOT / 'review/wp80-delivery-2026-10-03'

def identity(path):
    p = ROOT / path
    if not p.is_file():
        return {'missing': True}
    data = p.read_bytes()
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

def compare(rows):
    changed = []
    for row in rows:
        actual = identity(row['path'])
        if any(actual.get(k) != row[k] for k in ('sha256', 'bytes')):
            changed.append({'path': row['path'], 'expected': row, 'actual': actual})
    paths = [x['path'] for x in rows]
    return {'checked': len(rows), 'unchanged': len(rows)-len(changed), 'changed': changed,
            'duplicates': [p for p,n in collections.Counter(paths).items() if n>1]}

result = {'method': 'Read-only text and SHA-256 inspection; no reference execution.'}
tsv = ROOT/'review/wp18-wp20-delivery-2026-09-26/current-hashes.tsv'
tsv_rows = []
for line in tsv.read_text().splitlines():
    if not line or line.startswith('#'):
        continue
    h, size, p = line.split('\t')
    tsv_rows.append({'path':p,'sha256':h,'bytes':int(size)})
result['tsv'] = compare(tsv_rows)
manifest = (ROOT/'planning/review-manifest-2026-09-19.md').read_text().split('## 2.',1)[0]
manifest_rows, nohash, unmatched, badshort = [], [], [], []
for line in manifest.splitlines():
    if not line.startswith('| `'):
        continue
    p = re.search(r'^\| `([^`]+)`',line)[1]
    m = re.search(r'\| `([0-9a-f]{8})` \| `([0-9a-f]{64})` \| ([\d,]+) \|$',line)
    if m:
        short, h, size = m.groups()
        manifest_rows.append({'path':p,'sha256':h,'bytes':int(size.replace(',',''))})
        if short != h[:8]: badshort.append(p)
    else:
        nohash.append({'path':p,'row':line})
result['manifest_sec1'] = compare(manifest_rows)
result['manifest_sec1'].update({'nohash_rows':nohash,'bad_short_hashes':badshort})
for label, file in [('review_start_protection',OUT/'protected-inputs.json'),('wp78_pass_protection',ROOT/'review/wp78-stage-review-2026-10-03/recheck-v6/protected-inputs.json'),('wp80_b01_v2_protection',ROOT/'review/wp80-batch-01-review-2026-10-03/recheck-v2/protected-inputs.json'),('wp79_pass_protection',ROOT/'review/wp79-stage-review-2026-10-03/recheck-v6/protected-inputs.json')]:
    result[label] = compare(json.loads(file.read_text()))
result['review_input_freeze'] = compare(json.loads((OUT/'input-manifest.json').read_text())['inputs'])
result['WP79_accepted_specs'] = compare(json.loads((ROOT/'review/wp79-stage-review-2026-10-03/recheck-v6/accepted-baseline.json').read_text())['accepted_spec_files'])
result['prior_109_specs'] = compare([r for r in json.loads((ROOT/'review/wp78-stage-review-2026-10-03/recheck-v6/input-manifest.json').read_text())['inputs'] if r['path'].startswith('specs/')])
ref=ROOT/'reference/pokemon-essentials'
result['reference'] = {'head':subprocess.check_output(['git','--no-optional-locks','-C',str(ref),'rev-parse','HEAD'],text=True).strip(),
    'status':subprocess.check_output(['git','--no-optional-locks','-C',str(ref),'status','--porcelain','--untracked-files=all'],text=True)}
result['registry_identities']={str(p.relative_to(ROOT)):identity(str(p.relative_to(ROOT))) for p in [tsv,ROOT/'planning/review-manifest-2026-09-19.md',ROOT/'planning/feature-matrix.md', ROOT/'planning/extraction-plan.md',ROOT/'planning/coverage.md']}
(OUT/'mechanical-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
for k,v in result.items():
    if isinstance(v,dict) and 'checked' in v:
        print(k, 'checked',v['checked'],'unchanged',v['unchanged'],'changed',[x['path'] for x in v['changed']], 'duplicates',v['duplicates'])
    else:
        print(k,v)
