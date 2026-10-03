"""Static audit of review inputs. Does not execute reference behavior."""
from pathlib import Path
import collections
import hashlib
import json
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
AUTHOR = ROOT / 'review/wp79-coverage-review-2026-10-03/revision-v5'
rows = json.loads((AUTHOR / 'source-judgments.json').read_text())['rows']
source_root = ROOT / 'reference/pokemon-essentials/Data/Scripts'
actual = {str(p.relative_to(source_root)) for p in source_root.rglob('*.rb')}
paths = [r['path'] for r in rows]
groups = collections.Counter()
for r in rows:
    for g in ('已补提取', '已覆盖', '部分覆盖', '行为层', '不适用', '仅定位', '未引用'):
        if r['judgment'].startswith(g):
            groups[g] += 1
            break
    else:
        groups['unclassified'] += 1
bad_candidates = []
candidate_rows = 0
for r in rows:
    refs = r.get('candidate_refs', [])
    if refs:
        candidate_rows += 1
    for ref in refs:
        p = ROOT / 'specs' / (ref if ref.endswith('.md') else ref + '.md')
        if not p.is_file():
            bad_candidates.append({'source': r['path'], 'candidate': ref})

patterns = {
    'instance_assignment': r'(?<!\w)@@?[A-Za-z_]\w*\s*(?:\+=|-=|\|\|=|=(?!=))',
    'global_assignment': r'\$[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*\s*(?:\+=|-=|\|\|=|=(?!=))',
    'conditional_return': r'\breturn\s+(?:(?:true|false|nil)\s+)?(?:if|unless)\b',
    'elsif_keyword': r'\belsif\b',
    'if_negation': r'\bif\s+!',
    'increment': r'\+=',
    'equality': r'==|!=',
    'hash_arrow': r'=>',
    'safe_navigation': r'&\.',
    'block_arguments': r'\bdo\s*\|',
    'rand_call': r'\brand\s*\(',
    'named_source_call': r'\b(?:pb[A-Z]\w*|Graphics\.\w+|Input\.\w+)\s*\(',
}
new_texts = sorted(AUTHOR.iterdir()) + [ROOT / 'planning/coverage.md', ROOT / 'specs/overworld/wp16-pre-battle-transitions-appendix.md']
scan_hits = []
for p in new_texts:
    if not p.is_file():
        continue
    for n, line in enumerate(p.read_text().splitlines(), 1):
        for label, pattern in patterns.items():
            if re.search(pattern, line):
                scan_hits.append({'path': str(p.relative_to(ROOT)), 'line': n, 'pattern': label})

links, bad_links = 0, []
for p in [AUTHOR / n for n in ('revision-response.md', 'report.md', 'delivery-summary.md')] + [ROOT / 'planning/coverage.md']:
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', p.read_text()):
        if re.match(r'^[a-z]+:', target) or target.startswith('#'):
            continue
        links += 1
        local = unquote(target.split('#', 1)[0]).strip('<>')
        if not (p.parent / local).resolve().exists():
            bad_links.append({'file': str(p.relative_to(ROOT)), 'target': target})

ui = json.loads((AUTHOR / 'ui-scenario-relations.json').read_text())['rows']
ui_spec_checks = []
for r in ui:
    resolved = []
    for ref in re.findall(r'(?:ui|developer-experience|combat|overworld|kernel|creature-rpg|pokemon-rules)/[A-Za-z0-9_-]+', r['spec']):
        p = ROOT / 'specs' / (ref + '.md')
        resolved.append({'spec': ref, 'exists': p.is_file()})
    ui_spec_checks.append({'entry': r['entry'], 'scenario_ids': r['scenario_ids'], 'has_contract_ref': bool(r.get('contract_ref')), 'paths': resolved})
config = json.loads((ROOT / 'review/wp79-coverage-review-2026-10-03/revision-v4/config-details.json').read_text())['rows']
config_top = [r['file'] for r in config if r['file'].endswith('.txt')]
pbs_top = {p.name for p in (ROOT / 'reference/pokemon-essentials/PBS').glob('*.txt')}
before = {r['path']: r for r in json.loads((ROOT / 'review/wp79-stage-review-2026-10-03/recheck-v4/input-manifest.json').read_text())['inputs']}
appendixes = {}
for name in ('specs/ui/wp65-trainer-card-appendix.md', 'specs/ui/wp65-controls-help-appendix.md', 'specs/kernel/wp07-deprecation-appendix.md'):
    data = (ROOT / name).read_bytes()
    h = hashlib.sha256(data).hexdigest()
    appendixes[name] = {'sha256': h, 'bytes': len(data), 'unchanged_since_v4_review': h == before[name]['sha256'] and len(data) == before[name]['bytes']}

result = {
    'method': 'Static set, identity, link and pattern checks; semantic conclusions require manual reading.',
    'source_rows': len(rows), 'source_unique': len(paths) == len(set(paths)),
    'source_paths_match': set(paths) == actual,
    'source_columns': sorted(set(k for r in rows for k in r)),
    'judgment_groups': dict(groups),
    'candidate_ref_nonempty_rows': candidate_rows, 'bad_candidate_paths': bad_candidates,
    'empty_remaining': [r['path'] for r in rows if not r.get('remaining')],
    'ai_rows': sum('/005_AI/' in r['path'] or '/006_AI MoveEffects/' in r['path'] for r in rows),
    'ui_rows': len(ui), 'ui_spec_checks': ui_spec_checks,
    'config_rows': len(config), 'config_top_files': len(config_top),
    'config_top_paths_match': set(config_top) == pbs_top,
    'config_duplicate_top_files': [p for p, n in collections.Counter(config_top).items() if n > 1],
    'scan_scope': [str(p.relative_to(ROOT)) for p in new_texts if p.is_file()],
    'scan_patterns': list(patterns), 'scan_hits': scan_hits,
    'scan_limitation': 'No pattern match is not a global clean-room guarantee; current response also manually read. Approved unchanged documents are not reopened.',
    'links_checked': links, 'bad_links': bad_links,
    'specs_count': len(list((ROOT / 'specs').rglob('*.md'))), 'appendixes': appendixes,
}

prior_author = ROOT / 'review/wp79-coverage-review-2026-10-03/revision-v4'
prior_rows = {r['path']: r for r in json.loads((prior_author / 'source-judgments.json').read_text())['rows']}
result['source_rows_changed_since_v4'] = [r['path'] for r in rows if r != prior_rows[r['path']]]
prior_ui = json.loads((prior_author / 'ui-scenario-relations.json').read_text())['rows']
result['prior_16_ui_rows_preserved'] = all(r in ui for r in prior_ui)
result['new_ui_rows'] = [r for r in ui if r not in prior_ui]
appendix = ROOT / 'specs/overworld/wp16-pre-battle-transitions-appendix.md'
result['new_appendix_scenario_ids'] = re.findall(r'^\| (BT\d+) \|', appendix.read_text(), re.M)
coverage = (ROOT / 'planning/coverage.md').read_text().split('### 2.2', 1)[1].split('### 2.3', 1)[0]
counter = collections.Counter(line for line in coverage.splitlines() if line.startswith('|'))
result['coverage_sec22_duplicate_rows'] = [{'label': line.split('|')[1].strip(), 'occurrences': count} for line, count in counter.items() if count > 1]
result['new_appendix_identity'] = {'sha256': hashlib.sha256(appendix.read_bytes()).hexdigest(), 'bytes': appendix.stat().st_size}

result['scan_manual_adjudication'] = [{'path': h['path'], 'line': h['line'], 'pattern': h['pattern'], 'classification': 'audit_locator_not_copied_source_statement', 'reason': 'Function audit name followed by a parenthesized source file and line range, not executable argument text.'} for h in scan_hits if h['path'].endswith('/revision-v5/checks.json') and h['line'] == 36 and h['pattern'] == 'named_source_call']
result['confirmed_source_expression_hits'] = [h for h in scan_hits if not any(all(h[k] == a[k] for k in ('path','line','pattern')) for a in result['scan_manual_adjudication'])]


(OUT / 'independent-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k not in ('ui_spec_checks', 'scan_scope', 'appendixes')}, ensure_ascii=False, indent=2))
