#!/usr/bin/env python3
"""Independent static Markdown/JSON/Git evidence; never executes game code."""
import collections, hashlib, json, pathlib, re, subprocess, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = pathlib.Path(__file__).resolve().parent
CANDIDATE = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
BASE = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
DELIVERY = '4575e80d041ab0c74a42e2e36399d05791dbaa5b'
P = 'planning/implementation-routing/r8-20261017/'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def parse(data):
    lines = data.decode().splitlines(keepends=True)
    headings, slugs, fence = [], collections.Counter(), None
    for n, line in enumerate(lines, 1):
        fm = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if fm:
            mark = fm[1][0]
            if fence is None:
                fence = (mark, len(fm[1]))
            elif mark == fence[0] and len(fm[1]) >= fence[1]:
                fence = None
            continue
        if fence:
            continue
        m = re.match(r'^(#{1,6})[ \t]+(.+?)[ \t]*\n?$', line)
        if not m:
            continue
        title = re.sub(r'[ \t]+#+[ \t]*$', '', m[2])
        label = re.sub(r'<[^>]*>', '', title)
        label = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', label).lower()
        label = ''.join(c for c in label if c in ' -_' or unicodedata.category(c)[0] in 'LN').replace(' ', '-')
        anchor = label + (f'-{slugs[label]}' if slugs[label] else '')
        slugs[label] += 1
        headings.append(dict(level=len(m[1]), title=title, anchor=anchor, line_start=n, heading_sha256=sha(line.encode())))
    for i, h in enumerate(headings):
        h['line_end'] = next((x['line_start']-1 for x in headings[i+1:] if x['level'] <= h['level']), len(lines))
    return lines, headings

manifest_data = git('show', f'{CANDIDATE}:{P}routing-manifest.json')
manifest = json.loads(manifest_data)
coverage = json.loads(git('show', f'{CANDIDATE}:{P}section-coverage.json'))
view = git('show', f'{CANDIDATE}:{P}views/combat-requirements.md').decode().splitlines()
features = [x for x in manifest['features'] if re.search(r'/wp5[12]', x['source']['document'])]
paths = sorted({f['source']['document'] for f in features})
catalog = 'deliverables/final-specification-set/test-catalog/combat-requirements-wp49-51-52.md'
paths.append(catalog)
records, checks, all_sections = [], [], []
for path in paths:
    data = git('show', f'{CANDIDATE}:{path}')
    lines, headings = parse(data)
    sections = [x for x in coverage['sections'] if x['path'] == path]
    actual = [{k: x[k] for k in ('level','title','anchor','line_start','line_end','heading_sha256')} for x in sections]
    passed = actual == headings
    checks.append(dict(check='independent_heading_coverage', path=path, passed=passed))
    record = dict(path=path, bytes=len(data), sha256=sha(data), git_blob=git('rev-parse',f'{CANDIDATE}:{path}').decode().strip(), lines=len(lines), headings=len(headings), full_body_read=True, full_body_read_ranges=[[1,len(lines)]], same_bytes_at_base=data==git('show',f'{BASE}:{path}'), same_bytes_at_delivery=data==git('show',f'{DELIVERY}:{path}'), heading_mapping_pass=passed)
    record['source_read_chunks'] = {'wp51-ai-action-selection-and-skill.md': [[1,90],[91,160]], 'wp51-ai-decision-defaults.md':[[1,92]], 'wp52-a-evaluation-coverage-and-data.md':[[1,92],[93,200],[201,260]], 'wp52-a-generic-numerical-and-status-evaluation.md':[[1,90],[91,177],[178,253]], 'wp52-b-effect-coverage.md':[[1,60],[61,111]], 'wp52-b-field-damage-healing-and-target-evaluation.md':[[1,80],[81,165],[166,248]], 'wp52-c-item-control-coverage-and-data.md':[[1,90],[91,191]], 'wp52-c-items-calling-and-control-evaluation.md':[[1,80],[81,150],[151,208]], 'combat-requirements-wp49-51-52.md':[[1,95],[96,175],[176,265],[266,349]]}[path.rsplit('/',1)[1]]
    records.append(record)
    all_sections.extend(sections)
    for f in [f for f in features if f['source']['document'] == path]:
        s = f['source']
        selected = [h for h in headings if h['anchor'] == s['anchor']]
        unit = ''.join(''.join(lines[a-1:b]) for a,b in s['line_ranges']).encode()
        row = [i+1 for i,l in enumerate(view) if l.startswith('| '+f['feature_id']+' /')]
        fcheck = dict(feature_id=f['feature_id'], source_commit_ok=s['commit']==BASE, file_sha256_ok=s['file_sha256']==sha(data), blob_ok=s['file_git_blob']==record['git_blob'], anchor_ok=len(selected)==1 and selected[0]['title']==s['heading'] and selected[0]['level']==s['heading_level'] and selected[0]['heading_sha256']==s['heading_sha256'], unit_hash_ok=sha(unit)==s['unit_sha256'], within_owner_range=len(selected)==1 and all(selected[0]['line_start']<=a<=b<=selected[0]['line_end'] for a,b in s['line_ranges']), current_snapshot_ok=f['current_applicability']['snapshot_commit']==DELIVERY, generated_row_count=len(row), generated_row_line=row[0] if row else None)
        checks.append(fcheck)

evidence = dict(candidate=CANDIDATE, base=BASE, delivery=DELIVERY, candidate_formal_tree=git('rev-parse', f'{CANDIDATE}:deliverables/final-specification-set').decode().strip(), requested_configuration=dict(model='gpt-6.1-sol',effort='ultra',service_tier='default',Fast='off'), actual_configuration={k:'UNVERIFIED' for k in ('model','effort','service_tier','speed','Fast','opaque_platform_task_id')}, canonical_task='/root/combat_semantics/combat_ai', counts=dict(body_documents=8,catalog_documents=1,body_lines=sum(r['lines'] for r in records[:-1]),body_headings=sum(r['headings'] for r in records[:-1]),catalog_lines=records[-1]['lines'],catalog_headings=records[-1]['headings'],features=len(features)), reading_ledger=records, identity_checks=checks, selected_sections=all_sections, selected_features=features, unique_routing_rationales=sorted({f['future_plan']['rationale'] for f in features}), unique_questions=sorted({q for f in features for q in f['future_plan']['questions']}), changed_paths_from_delivery=git('diff','--name-only',DELIVERY,CANDIDATE).decode().splitlines(), scope_limit='Root handles complete schema/tool validation, global protection and commit/push. No Ruby/game/framework/business vector was run.')
(OUT/'combat-ai-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(candidate=CANDIDATE,counts=evidence['counts'],identity_checks=len(checks),heading_mismatches=sum(not x['passed'] for x in checks if 'passed' in x),feature_identity_failures=[x for x in checks if 'feature_id' in x and (not all(v for k,v in x.items() if k.endswith('_ok') or k=='within_owner_range') or x['generated_row_count']!=1)],source_bytes_preserved=all(x['same_bytes_at_base'] and x['same_bytes_at_delivery'] for x in records),evidence_file=str(OUT/'combat-ai-evidence.json')),ensure_ascii=False,indent=2))
