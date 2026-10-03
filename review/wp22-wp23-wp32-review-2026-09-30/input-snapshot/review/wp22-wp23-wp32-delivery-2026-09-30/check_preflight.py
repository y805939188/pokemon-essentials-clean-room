"""Own text/hash audit only; never imports or executes reference material."""
from pathlib import Path
import csv, hashlib, json, re, subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
CLOSURE = ROOT / 'review/wp58-wp62-wp38-review-2026-09-30/closure-review'

def identity(p):
    b = p.read_bytes()
    return {'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)}

def check(rows, base):
    bad = []
    for row in rows:
        p = base / row['path']
        expected = {k: row[k] for k in ('sha256', 'bytes')}
        actual = identity(p) if p.is_file() else None
        if expected != actual:
            bad.append({'path': row['path'], 'expected': expected, 'actual': actual})
    return {'count': len(rows), 'mismatches': bad}

fixed = json.loads((CLOSURE / 'input-manifest.json').read_text())
result = {'role': 'extractor static preflight', 'date': '2026-09-30'}
result['fixed_current'] = check(fixed['inputs'], ROOT)
result['fixed_snapshot'] = check(fixed['inputs'], CLOSURE / 'input-snapshot')
tsv = list(csv.DictReader((CLOSURE / 'current-hashes.tsv').open(), delimiter='\t'))
for row in tsv:
    row['bytes'] = int(row['bytes'])
result['closure_tsv'] = check(tsv, ROOT)
result['input_manifest_tsv_same_set'] = sorted(tsv, key=lambda x:x['path']) == sorted(fixed['inputs'], key=lambda x:x['path'])
report = (CLOSURE / 'report.md').read_text().split('## 2.')[0]
core = []
for name, sha, size in re.findall(r'^\| ([^|]+) \| `([a-f0-9]{64})` \| ([\d,]+) \|$', report, re.M):
    matches = [r for r in fixed['inputs'] if r['sha256'] == sha and r['bytes'] == int(size.replace(',',''))]
    assert len(matches) == 1, (name, matches)
    core.append({'object': name, **matches[0], 'actual': identity(ROOT / matches[0]['path'])})
assert len(core) == 9
result['report_section1_nine'] = core
result['dependencies'] = check(list(json.loads((CLOSURE/'next-batch-checks.json').read_text())['current_dependency_identities'].values()), ROOT)
final = json.loads((CLOSURE/'final-checks.json').read_text())
result['closure_originals'] = check(final['artifacts'], ROOT)
result['prior'] = []
for prior in final['prior']:
    directory = ROOT/'review'/prior['review']
    manifest = json.loads((directory/'input-manifest.json').read_text())
    rows = manifest['inputs']
    previous_final = json.loads((directory/'final-checks.json').read_text())
    result['prior'].append({'review':prior['review'], 'snapshots':check(rows, directory/'input-snapshot'),
                            'originals':check(previous_final.get('artifacts',[]), ROOT)})
result['reference'] = {
    'HEAD':subprocess.check_output(['git','-C',str(ROOT/'reference/pokemon-essentials'),'rev-parse','HEAD'],text=True).strip(),
    'ordinary_git_status':subprocess.check_output(['git','-C',str(ROOT/'reference/pokemon-essentials'),'status','--porcelain'],text=True)}
result['workspace_git'] = 'Workspace root is not a Git repository; reference has its own repository.'
result['execution'] = 'Own text/hash/JSON and read-only Git metadata only; no reference execution.'
(OUT/'preflight-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
protected = []
for p in sorted(ROOT.rglob('*')):
    rel = p.relative_to(ROOT)
    if not p.is_file() or '.git' in rel.parts or OUT in p.parents:
        continue
    protected.append({'path':str(rel),**identity(p)})
with (OUT/'preexisting-files.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['sha256','bytes','path'],delimiter='\t',lineterminator='\n')
    w.writeheader();w.writerows(protected)
print(json.dumps({'core':core,'current':result['fixed_current'],'snapshot':result['fixed_snapshot'],
                  'prior':result['prior'],'originals':result['closure_originals'],
                  'dependencies':result['dependencies'],'protected_files':len(protected),
                  'reference':result['reference']},ensure_ascii=False,indent=2))
