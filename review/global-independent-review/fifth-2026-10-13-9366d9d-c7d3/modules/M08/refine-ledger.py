"""Materialize explicit reviewer-authored comparisons; never execute reference behavior."""
import sys, hashlib, re
from pathlib import Path
sys.dont_write_bytecode = True
from ledger import read, write, complement

def anchor(suffix, *ranges):
    cov = read('reading-coverage.json')
    matches = [f for f in cov['sources'] if f['path'].endswith(suffix)]
    if len(matches) != 1:
        raise ValueError((suffix, len(matches)))
    f = matches[0]
    for a, b in ranges:
        assert 1 <= a <= b <= f['line_count'], (suffix, a, b)
    return {'path': f['path'], 'version': f['version'], 'lines': [list(r) for r in ranges]}

def methods(suffix, *names):
    """Locate exact already-reviewed method bodies for provenance, not semantic proof."""
    cov = read('reading-coverage.json')
    f = next(f for f in cov['sources'] if f['path'].endswith(suffix))
    lines = (Path(cov['source_baseline']['root']) / f['path']).read_text().splitlines()
    result = []
    for name in names:
        hits = [(i, re.match(r'^(\s*)def\s+' + re.escape(name) + r'(?=\s|\(|;|$)', line)) for i, line in enumerate(lines)]
        hits = [(i,m) for i,m in hits if m]
        if len(hits) != 1:
            raise ValueError((suffix, name, len(hits)))
        i,m = hits[0]
        if re.search(r';.*\bend\s*$', lines[i]):
            end = i
        else:
            end = next(j for j in range(i+1, len(lines)) if lines[j] == m[1] + 'end')
        result.append({**anchor(suffix, (i+1,end+1)), 'entry': name})
    return result

def effects(*names):
    caps = {c['id']: c for c in read('source-to-spec.json')['capabilities']}
    return [a for name in names for a in caps['M08-MOVE-' + name]['source_anchors']]

def registry(*ids):
    caps = {c['id']: c for c in read('source-to-spec.json')['capabilities']}
    return [a for cid in ids for a in caps[cid]['source_anchors']]

def named_rows(suffix, ranges, prefix, note, shared=None):
    """Index already-compared named rows. Caller must supply the finite review result."""
    rev = read('spec-to-source.json')
    spec = next(f for f in rev['specifications'] if f['path'].endswith(suffix))
    caps = {c['id']: c for c in read('source-to-spec.json')['capabilities']}
    closed = []
    for row in spec['clause_mappings']:
        n = row['lines'][0]
        if not any(a <= n <= b for a,b in ranges):
            continue
        ids = [cid for cid in row['shared_rule_ids'] if cid in caps]
        if not ids:
            continue
        refs = [a for cid in ids for a in caps[cid]['source_anchors']] + row['data_anchors'] + (shared or [])
        issues = list(dict.fromkeys(fid for cid in ids for fid in caps[cid].get('related_findings', [])))
        status = 'partial' if issues else 'supported'
        close(suffix, n, n, prefix + '-ROW-' + str(n), refs, note,
              status, issues[0] if issues else None)
        closed.append(n)
    return closed

def close(suffix, start, end, rule, anchors, note, status='supported', finding=None):
    """Apply a human/model-authored finite comparison to every actual clause in range."""
    rev = read('spec-to-source.json')
    spec = next(f for f in rev['specifications'] if f['path'].endswith(suffix))
    gid = 'M08-CLOSED-' + rule
    group = {'source_anchors': anchors, 'specification_path': spec['path'],
             'specification_lines': [start, end], 'comparison': note,
             'review_extent': 'full', 'capability_status': status,
             'evidence_level': 'static_semantic_clause_comparison',
             'supported_boundary': 'supported_static: only the stated rule and finite R/B5 sources; no reference/model execution or M07/M09 sign-off' if status == 'supported' else None,
             'related_findings': [finding] if finding else []}
    rev.setdefault('source_anchor_groups', {})[gid] = group
    for c in spec['clause_mappings']:
        if start <= c['lines'][0] and c['lines'][1] <= end:
            c['source_anchor_group_ref'] = gid
            c['review_extent'] = 'full'
            c['capability_status'] = status
            c['evidence_level'] = 'static_semantic_clause_comparison'
            c['related_findings'] = [finding] if finding else []
            c['comparison_note'] = note
    spec['clause_mapping_status'] = ('complete_finite_clause_comparison' if all(c['review_extent'] == 'full' and c['evidence_level'] == 'static_semantic_clause_comparison' for c in spec['clause_mappings']) else 'in_progress_precise_clause_comparison')
    write('spec-to-source.json', rev)

def dependency_spec(path, ranges, result, anchors):
    """Record current cross-domain contract actually read; does not sign off other owners."""
    cov = read('reading-coverage.json')
    content = Path(path).read_bytes(); n = len(content.splitlines())
    record = {'path': path, 'version': cov['specification_baseline']['commit'],
              'content_sha256': hashlib.sha256(content).hexdigest(), 'line_count': n,
              'scope_role': 'counterevidence_and_consumer_projection_only',
              'review_extent': 'full' if not complement(n, ranges) else 'partial',
              'material_availability': 'available', 'body_read_ranges': ranges,
              'evidence_level': 'static_current_contract_counterevidence',
              'semantic_scope': result, 'source_mappings': anchors,
              'unreviewed_ranges': complement(n, ranges),
              'boundary': 'Full body reading is for the named M08 boundary; no global sign-off for another owner.'}
    for name in ['reading-coverage.json', 'spec-to-source.json']:
        x = read(name)
        entries = x.setdefault('dependency_specifications', [])
        entries[:] = [f for f in entries if f['path'] != path]
        entries.append(record); write(name, x)

def add_source(path, ranges, description, specs, status):
    cov = read('reading-coverage.json'); body = (Path(cov['source_baseline']['root']) / path).read_bytes()
    n = len(body.splitlines())
    f = {'path': path, 'version': cov['source_baseline']['commit'], 'content_sha256': hashlib.sha256(body).hexdigest(),
         'line_count': n, 'scope_role': 'necessary_dependency_or_consumer_projection',
         'review_extent': 'full' if not complement(n, ranges) else 'partial',
         'material_availability': 'available', 'evidence_level': 'static_semantic_review',
         'body_read_ranges': ranges, 'unreviewed_ranges': complement(n, ranges),
         'effect_entry_inventory': [], 'semantic_ranges': [
             {'lines': r, 'entries_and_rules': description, 'semantic_comparison': description,
              'specification_anchors': specs, 'capability_status': status,
              'evidence_level': 'static_source_and_contract_comparison'} for r in ranges]}
    cov['sources'] = [s for s in cov['sources'] if s['path'] != path] + [f]
    write('reading-coverage.json', cov)

def synchronize():
    cov = read('reading-coverage.json'); rev = read('spec-to-source.json'); src = read('source-to-spec.json')
    src['source_files'] = [{k: f[k] for k in ['path','version','review_extent','material_availability','evidence_level','unreviewed_ranges']} |
        {'actual_semantic_ranges': f['semantic_ranges'], 'data_semantic_ranges': f.get('data_semantic_ranges', [])} for f in cov['sources']]
    src['precise_contract_comparisons'] = {gid: v for gid,v in rev['source_anchor_groups'].items() if gid.startswith('M08-CLOSED-')}
    write('source-to-spec.json', src)
    for f in cov['specifications']:
        current = next(s for s in rev['specifications'] if s['path'] == f['path'])
        f['precise_clause_comparison_status'] = current.get('clause_mapping_status')
    write('reading-coverage.json', cov)
    p = read('progress.json')
    p['not_reviewed']['strict_anonymous_clause_closure'] = [{'path': f['path'], 'lines': c['lines'], 'section': c['section'], 'row_or_vector': c['vector_or_row_id']} for f in rev['specifications'] for c in f['clause_mappings'] if c['evidence_level'] != 'static_semantic_clause_comparison']
    p['not_reviewed']['remaining_source_intervals'] = [{'path': f['path'], 'review_extent': f['review_extent'], 'unreviewed_ranges': f['unreviewed_ranges'], 'scope_role': f['scope_role']} for f in cov['sources'] if f['unreviewed_ranges']]
    write('progress.json', p)
