"""Append the completed original/current comparison layer; never rebuild source review."""
import sys, json, hashlib, datetime, collections, runpy
from pathlib import Path
sys.dont_write_bytecode = True
globals().update(runpy.run_path(Path(__file__).with_name('original-ledger.py')))

def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True).encode()).hexdigest()

x = read('original-comparison.json')
cov = read('reading-coverage.json')
src = read('source-to-spec.json')
rev = read('spec-to-source.json')
prog = read('progress.json')
assert prog['complete'] is False
assert all(not f['unreviewed_comparison_ranges'] for f in x['files'])
assert not x['new_findings']
core = {
    'reading_coverage_sources': digest(cov['sources']),
    'reading_coverage_formal_specs': digest(cov['specifications']),
    'canonical_capabilities': digest(src['capabilities']),
    'source_files_and_precise_links': digest(src['source_files']),
    'formal_specs_and_clauses': digest(rev['specifications']),
    'source_anchor_groups': digest(rev['source_anchor_groups']),
}
assert 'preserved_prior_core_sha256' not in x, 'One-time finalization; do not reset preserved review'
x['preserved_prior_core_sha256'] = core
formal = {s['path']: s for s in rev['specifications']}
group_inverse = collections.defaultdict(set)
current_inverse = collections.defaultdict(list)
forward = []
disposition_lines = collections.Counter()

def groups_for(receiver):
    a, b = receiver['lines']
    spec = formal[receiver['path']]
    assert 1 <= a <= b <= spec['line_count']
    return sorted({c['source_anchor_group_ref'] for c in spec['clause_mappings']
                   if c['lines'][0] <= b and c['lines'][1] >= a})

def index_record(file, record_id, ranges, disposition, receivers):
    refs = set()
    for r in receivers:
        gs = groups_for(r)
        r['existing_formal_comparison_group_refs'] = gs
        refs.update(gs)
        key = (r['path'], *r['lines'])
        current_inverse[key].append({'original_path': file['path'], 'original_version': file['version'],
                                    'original_ranges': ranges, 'comparison_id': record_id,
                                    'disposition': disposition})
    for g in refs:
        group_inverse[g].add(record_id)
    forward.append({'comparison_id': record_id, 'original_path': file['path'],
                    'original_version': file['version'], 'original_ranges': ranges,
                    'disposition': disposition, 'existing_formal_comparison_group_refs': sorted(refs)})
    return sorted(refs)

for f in x['files']:
    exact = set()
    for i, pair in enumerate(f['qualified_exact_reuse'], 1):
        rid = f['id'] + '-R' + str(i).zfill(3)
        pair['id'] = rid
        rec = {'path': f['formal_path'], 'version': f['formal_version'],
               'lines': pair['formal_lines'], 'kind': 'qualified_exact_bytes_reuse'}
        pair['formal_comparison_group_refs'] = index_record(
            f, rid, [pair['original_lines']], 'qualified_exact_bytes_reuse', [rec])
        exact.update(points([pair['original_lines']]))
    read_points = set()
    for c in f['comparisons']:
        nums = points(c['original_ranges'])
        assert not read_points & nums
        read_points.update(nums)
        disposition_lines[c['disposition']] += len(nums)
        c['existing_formal_comparison_group_refs'] = index_record(
            f, c['id'], c['original_ranges'], c['disposition'], c['current_receivers'])
    assert not exact & read_points
    assert exact | read_points == set(range(1, f['line_count'] + 1))
    assert read_points == points(f['physical_read_ranges_new'])
    assert points(f['semantic_compared_ranges']) == exact | read_points
    f['review_extent'] = 'full'
    f['evidence_level'] = 'original_and_current_static_semantic_comparison_with_qualified_exact_reuse'
    f['reading_interpretation'] = ('Physical reading is claimed only for physical_read_ranges_new. '
        'Exact byte ranges reuse the prior formal comparison. Prior roster identity projections '
        'never stand in for unread cells or complete original rows.')

x['current_to_original'] = [
    {'current_path': p, 'current_version': x['specification_baseline']['commit'], 'current_lines': [a,b],
     'original_comparisons': entries}
    for (p,a,b), entries in sorted(current_inverse.items())]
x['comparison_to_existing_source_groups'] = forward
x['existing_source_group_to_original_comparisons'] = [
    {'group_id': g, 'comparison_ids': sorted(ids)} for g,ids in sorted(group_inverse.items())]
x['navigation_counts_only'].update({
    'actual_original_difference_lines_read_and_compared': 2919,
    'unclosed_original_lines': 0,
    'disposition_line_counts': dict(disposition_lines),
    'new_independent_fact_candidates': 0,
})
x['completion_interpretation'] = ('All 14 B5 originals are closed for fact transfer, with every non-reused '
    'difference actually read. This does not add source/current clauses, new capabilities, runtime evidence, '
    'or final required sign-off. Existing confirmed gaps retain their prior finding identities.')
x['complete'] = True
x['completed_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()

root_report = ROOT.parent.parent / 'counterevidence/root-M08/report.md'
correction = {
    'id': 'ROOT-M08-SHADOW-PARAMETER-CORRECTION',
    'authority': 'root independent counterevidence; consumed unchanged, not reopened by M08',
    'path': str(root_report.relative_to(Path.cwd())),
    'lines': [11,13],
    'content_sha256': hashlib.sha256(root_report.read_bytes()).hexdigest(),
    'effective_conclusion': ('ShadowHalf/ShadowEnd pass false for animation, while damage registration '
        'retains its default true. Positive losses set tookDamageThisRound and tookMoveDamageThisRound '
        'and can set the crossed-half-HP marker. The receiving-contract gap remains confirmed. '
        'Optional SHADOWSHED missing-effect binding has also been independently checked; default '
        'activation is not claimed.'),
    'supersedes': ('Any earlier M08 statement that these two effects disable damage registration, '
        'or that the Shadow supplement/SHADOWSHED projection still awaits its first root countercheck. '
        'Earlier candidate evidence is retained for audit, with this effective correction taking precedence.'),
    'related_findings': ['GR5-M08-001', 'GR5-M08-003'],
    'execution_status': 'NOT_EXECUTED',
    'required_revision_signed_off_by_M08': False,
}
x['effective_parent_corrections'] = [correction]
cov['original_specification_comparison'] = {
    'artifact': 'original-comparison.json', 'trigger': 'GCV-E001', 'review_extent': 'full',
    'evidence_level': 'static_semantic_original_fact_transfer_comparison',
    'not_a_new_source_or_capability_denominator': True,
    'preserved_denominators': x['preserved_denominators'],
    'files': [{
        'id': f['id'], 'path': f['path'], 'version': f['version'], 'content_sha256': f['sha256'],
        'line_count': f['line_count'], 'material_availability': 'available', 'review_extent': 'full',
        'physical_read_ranges_this_followup': f['physical_read_ranges_new'],
        'qualified_reuse': f['qualified_exact_reuse'],
        'prior_literal_projections': f['prior_literal_projections'],
        'semantic_compared_ranges': f['semantic_compared_ranges'], 'unreviewed_comparison_ranges': [],
        'comparison_ids': [c['id'] for c in f['comparisons']],
        'evidence_level': f['evidence_level'], 'reading_interpretation': f['reading_interpretation'],
        'execution_status': 'NOT_EXECUTED',
    } for f in x['files']],
}
rev['original_comparison_projection'] = {
    'artifact': 'original-comparison.json', 'review_extent': 'full',
    'mapping_kind': 'original_fact_transfer_via_existing_current_clause_groups',
    'not_new_formal_specs_or_source_anchors': True,
    'original_to_current_and_source_groups': forward,
    'current_to_original': x['current_to_original'],
}
src['original_comparison_projection'] = {
    'artifact': 'original-comparison.json', 'review_extent': 'full',
    'mapping_kind': 'inverse_navigation_projection_of_existing_source_comparison_groups',
    'not_new_capabilities_or_fresh_source_proof': True,
    'source_group_to_original': x['existing_source_group_to_original_comparisons'],
}
for o in (cov, rev, src):
    o['effective_parent_corrections'] = [correction]
findings = read('findings.json')
findings['bounded_original_comparison_followup'] = {
    'artifact': 'original-comparison.json', 'complete': True, 'new_findings': [],
    'prior_findings_preserved': x['prior_findings_preserved'],
    'effective_parent_corrections': [correction],
    'required_revision_signed_off': False,
}
for f in findings['findings']:
    if f['id'] in correction['related_findings']:
        f['review_resolution']['effective_parent_supplement'] = correction
        f['review_resolution']['next'] = ('Root canonical integration with already completed independent '
            'counterevidence and the effective Shadow correction; no repeat audit of this same scope. '
            'M08 does not issue final required sign-off.')
prog['last_completed_finite_range'] = 'GCV-E001: all 14 originals, 935 exact-byte reuse lines + 2919 actually read/compared difference lines; no remaining interval or new candidate.'
prog['current_range'] = 'Bounded original comparison and mapping completed; artifact validation pending'
prog['next_actual_range'] = 'Artifact-only validation; no source semantic reread or behavior execution'
prog['bounded_followup']['comparison_complete'] = True
prog['bounded_followup']['artifact'] = 'original-comparison.json'
prog['bounded_followup']['new_findings'] = []
prog['bounded_followup']['preserved_denominators'] = x['preserved_denominators']
prog['parent_counterevidence_boundary'] = ('Root counterevidence for original001–003 and subsequent Shadow '
    'supplement/optionalSHADOWSHED is preserved. Shadow animation-vs-registration correction is effective. '
    'Canonical integration remains root-owned; M08 has no final required sign-off.')
prog['effective_parent_corrections'] = [correction]
prog['updated_at'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
for name, obj in [('original-comparison.json',x),('reading-coverage.json',cov),('source-to-spec.json',src),
                  ('spec-to-source.json',rev),('findings.json',findings),('progress.json',prog)]:
    write(name,obj)
print(json.dumps({'original_comparison_complete':True,'progress_complete':False,
                  'original_files':len(x['files']),'difference_lines':sum(disposition_lines.values()),
                  'new_findings':0,'prior_core_digests_recorded':len(core)},ensure_ascii=False))
