"""Independent static Markdown/JSON/Git checks; no game/framework execution."""
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

REPO = Path('/workspace/r8-disposition-r1-review')
OUT = REPO / 'review/r8-disposition-r1-independent-5666b7b-20261017/agents'
BASE = 'planning/implementation-routing/r8-20261017/'
NEW = '5666b7b912e2fb79b5119283ee6a37401a7071db'
OLD = 'd62b41f4d620e50bb04c80a7505374bd284d8210'
REVIEW = 'a0352c7fba38391afc535525988245701d5ce202'
CURRENT = '908273093e1f6b27fc58249417675dd62d146224'
SOURCE = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
PREV = 'review/r8-disposition-independent-d62b41f-20261017/'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=REPO)

def obj(commit, path):
    return git('show', f'{commit}:{path}')

def j(commit, path):
    return json.loads(obj(commit, path))

def identity(commit, path):
    data = obj(commit, path)
    return dict(commit=commit, path=path, bytes=len(data),
                sha256=hashlib.sha256(data).hexdigest(),
                git_blob=git('rev-parse', f'{commit}:{path}').decode().strip(),
                line_count=len(data.splitlines()))

manifest = j(NEW, BASE + 'routing-manifest.json')
old_manifest = j(OLD, BASE + 'routing-manifest.json')
previous = j(REVIEW, PREV + 'agents/world-ui-results.json')
previous_catalog = j(REVIEW, PREV + 'agents/world-catalog-full-results.json')
sections = j(NEW, BASE + 'section-coverage.json')['sections']
old_sections = j(OLD, BASE + 'section-coverage.json')['sections']
old_by = {f['feature_id']: f for f in old_manifest['features']}
active_by = {f['feature_id']: f for f in manifest['features']}
retired_by = {f['feature_id']: f for f in manifest['retired_features']}
scope_paths = {d['path'] for d in previous['documents']}
catalog_paths = {d['path'] for d in previous_catalog['documents']}
old_ids = [f['feature_id'] for f in previous['feature_results']]
active = [f for f in manifest['features'] if f['source']['document'] in scope_paths]
retired = [f for f in manifest['retired_features'] if f['source']['document'] in scope_paths]
metadata = [f for f in manifest['metadata_records'] if f['source']['document'] in scope_paths]
errors = []
dispositions = []
for fid in old_ids:
    occurrences = int(fid in active_by) + int(fid in retired_by)
    disposition = 'active' if fid in active_by else 'retired'
    f = active_by.get(fid, retired_by.get(fid))
    source_same = f is not None and f['source'] == old_by[fid]['source']
    retired_exact = disposition != 'retired' or {k:v for k,v in f.items() if k != 'retirement'} == old_by[fid]
    row = dict(feature_id=fid, occurrence_count=occurrences, disposition=disposition,
               immutable_source_equal=source_same, retired_full_old_row_equal=retired_exact)
    dispositions.append(row)
    if occurrences != 1 or not source_same or not retired_exact:
        errors.append(row)

identities = []
for path in sorted(scope_paths | catalog_paths):
    ids = [identity(c, path) for c in [SOURCE, OLD, NEW, CURRENT]]
    same = len({i['sha256'] for i in ids}) == 1
    worktree_same = (REPO/path).read_bytes() == obj(NEW, path)
    identities.append(dict(path=path, identities=ids, all_four_equal=same,
                           candidate_worktree_equal=worktree_same))
    if not same or not worktree_same:
        errors.append(dict(path=path, identity_failure=True))

overlaps = []
for path in scope_paths:
    lines = {}
    for f in active:
        if f['source']['document'] != path:
            continue
        for a,z in f['functional_scope']['line_ranges']:
            for line in range(a,z+1):
                if line in lines:
                    overlaps.append(dict(path=path, line=line, ids=[lines[line],f['feature_id']]))
                lines[line] = f['feature_id']

views = {domain:obj(NEW, BASE+f'views/{domain}.md').decode().splitlines()
         for domain in ['engine-overworld','user-interface']}
view_checks = []
state_checks = []
for f in active:
    domain = f['source']['document'].split('/')[-2]
    rows = [line for line in views[domain] if line.startswith('| '+f['feature_id']+' / ')]
    good = len(rows) == 1 and all(x in rows[0] for x in
        [f['future_plan']['destination'], CURRENT, f['destination_verification']['status'],
         f['implementation']['status'], f['implementation']['acceptance_status']])
    view_checks.append(dict(feature_id=f['feature_id'], occurrence_count=len(rows), key_fields_match=good))
    if not good:errors.append(dict(feature_id=f['feature_id'], view_failure=True))
    source_data=obj(f['source']['commit'],f['source']['document']).decode().splitlines(keepends=True)
    unit=''.join(''.join(source_data[a-1:z]) for a,z in f['source']['line_ranges'])
    unit_matches=hashlib.sha256(unit.encode()).hexdigest()==f['source']['unit_sha256']
    state_ok=(f['destination_verification']['status']=='待验证' and
              f['implementation']['status']=='未实现' and
              f['implementation']['acceptance_status']=='未验收' and
              f['future_plan']['stage']=='待定' and f['future_plan']['stage_approval']=='未批准' and
              f['current_applicability']['snapshot_commit']==CURRENT and
              not f['upstream']['accepted_events'])
    state_checks.append(dict(feature_id=f['feature_id'],state_separation=state_ok,
        source_unit_hash_equal=unit_matches,upstream_status=f['upstream']['status'],
        batches=f['upstream']['batches']))
    if not unit_matches or not state_ok:
        errors.append(dict(feature_id=f['feature_id'],source_or_state_failure=True))

catalog_checks = []
old_sec_by = {(x['path'],x['line_start'],x['title']):x for x in old_sections}
for index, section in enumerate(sections):
    if section['path'] not in catalog_paths:
        continue
    old_section = old_sec_by[(section['path'],section['line_start'],section['title'])]
    catalog_checks.append(dict(section_index=index, path=section['path'],
        title=section['title'], line_ranges=[[section['line_start'],section['line_end']]],
        added_feature_refs=sorted(set(section['feature_refs'])-set(old_section['feature_refs'])),
        removed_feature_refs=sorted(set(old_section['feature_refs'])-set(section['feature_refs'])),
        feature_refs=section['feature_refs'], metadata_refs=section.get('metadata_refs',[]),
        retired_feature_refs=section.get('retired_feature_refs',[])))

object_checks = {c:git('cat-file','-t',c).decode().strip() for c in
    [NEW,OLD,REVIEW,CURRENT,'861f7a44a6f763c265a11761ab17a8ec3b55f304',
     '548d6bb9a21d0967680445c013e66d9d5661d2d6',SOURCE,
     '4575e80d041ab0c74a42e2e36399d05791dbaa5b']}
evidence = dict(candidate_commit=NEW, old_candidate=OLD, old_review=REVIEW,
    current_snapshot=CURRENT, object_checks=object_checks,
    formal_trees={c:git('rev-parse',c+':deliverables/final-specification-set').decode().strip()
                  for c in [NEW,CURRENT,SOURCE]},
    scope_counts=dict(old_features=len(old_ids), active_features=len(active),
        new_features=sum(f['feature_id'] not in old_by for f in active), retired_features=len(retired),
        metadata_records=len(metadata), documents=len(scope_paths), catalog_documents=len(catalog_paths),
        catalog_sections=len(catalog_checks)),
    dispositions=dispositions, document_identities=identities,
    functional_range_overlaps=overlaps, view_checks=view_checks, state_checks=state_checks,
    catalog_checks=catalog_checks, errors=errors,
    tool_scope='Only Python JSON/hash and Git read operations; no author/business code executed')
(OUT/'world-ui-static-evidence.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(counts=evidence['scope_counts'],errors=len(errors),overlaps=len(overlaps)),ensure_ascii=False))
