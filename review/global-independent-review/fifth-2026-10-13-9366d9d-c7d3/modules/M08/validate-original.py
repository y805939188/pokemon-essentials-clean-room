"""Artifact-only check for GCV-E001; does not read or execute reference source."""
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
findings = read('findings.json')
errors = []

def check(condition, label):
    if not condition:
        errors.append(label)

for name, o in [('original',x),('coverage',cov),('source',src),('specification',rev),('progress',prog),('findings',findings)]:
    check(o.get('schema_version') == 'gr5.review.v1', 'schema:' + name)
core = {
    'reading_coverage_sources': digest(cov['sources']),
    'reading_coverage_formal_specs': digest(cov['specifications']),
    'canonical_capabilities': digest(src['capabilities']),
    'source_files_and_precise_links': digest(src['source_files']),
    'formal_specs_and_clauses': digest(rev['specifications']),
    'source_anchor_groups': digest(rev['source_anchor_groups']),
}
check(core == x['preserved_prior_core_sha256'], 'prior source/current review was changed')
p = x['preserved_denominators']
check(sum(s['scope_role']=='primary' for s in cov['sources']) == p['primary_source_files'] == 28, 'primary files')
check(sum(s['line_count'] for s in cov['sources'] if s['scope_role']=='primary') == p['primary_source_lines'] == 21586, 'primary source lines')
check(len(rev['specifications']) == p['formal_specification_files'] == 18, 'formal files')
check(sum(len(s['clause_mappings']) for s in rev['specifications']) == p['formal_clause_rows'] == 1906, 'formal clauses')
check(len(src['capabilities']) == p['canonical_rule_records'] == 852, 'canonical records')
check(hashlib.sha256('\n'.join(sorted(c['id'] for c in src['capabilities'])).encode()).hexdigest() == p['capability_id_set_sha256'], 'canonical identity set')
formal = {s['path']:s for s in rev['specifications']}
records = {}
expected_inverse = collections.defaultdict(list)
expected_groups = collections.defaultdict(set)
total_exact = total_read = total_lines = 0
types = collections.Counter()

def index_expected(f, rid, ranges, disposition, receivers, group_refs):
    check(rid not in records, 'duplicate record:' + rid)
    records[rid] = (f['path'], ranges, disposition, sorted(group_refs))
    observed_groups = set()
    for r in receivers:
        check(r['path'] in formal, 'unowned receiver:' + rid)
        if r['path'] not in formal:
            continue
        a,b = r['lines']; spec = formal[r['path']]
        check(1 <= a <= b <= spec['line_count'], 'receiver bound:' + rid)
        check(r['version'] == x['specification_baseline']['commit'], 'receiver version:' + rid)
        observed_groups.update(c['source_anchor_group_ref'] for c in spec['clause_mappings']
                               if c['lines'][0] <= b and c['lines'][1] >= a)
        expected_inverse[(r['path'], a, b)].append({
            'original_path': f['path'], 'original_version': f['version'], 'original_ranges': ranges,
            'comparison_id': rid, 'disposition': disposition})
    check(sorted(observed_groups) == sorted(group_refs), 'source group projection:' + rid)
    for g in group_refs:
        check(g in rev['source_anchor_groups'], 'missing existing source group:' + rid)
        expected_groups[g].add(rid)

for f in x['files']:
    old = Path(f['path']).read_bytes()
    new = Path(f['formal_path']).read_bytes()
    check(hashlib.sha256(old).hexdigest() == f['sha256'], 'original hash:' + f['id'])
    check(hashlib.sha256(new).hexdigest() == f['formal_sha256'], 'current hash:' + f['id'])
    old_lines = old.splitlines(keepends=True); new_lines = new.splitlines(keepends=True)
    check(len(old_lines) == f['line_count'], 'original line count:' + f['id'])
    exact = set(); actual = set()
    for pair in f['qualified_exact_reuse']:
        a,b = pair['original_lines']; c,d = pair['formal_lines']
        ob = b''.join(old_lines[a-1:b]); nb = b''.join(new_lines[c-1:d])
        check(ob == nb and hashlib.sha256(ob).hexdigest() == pair['sha256'], 'reuse bytes:' + pair['id'])
        check(1<=a<=b<=len(old_lines) and 1<=c<=d<=len(new_lines), 'reuse bounds:' + pair['id'])
        ns = points([[a,b]])
        check(not exact & ns, 'overlap exact:' + pair['id']); exact.update(ns)
        index_expected(f, pair['id'], [pair['original_lines']], 'qualified_exact_bytes_reuse',
            [{'path':f['formal_path'],'version':f['formal_version'],'lines':pair['formal_lines']}],
            pair['formal_comparison_group_refs'])
    for c in f['comparisons']:
        ns = points(c['original_ranges'])
        check(not actual & ns, 'overlap compared:' + c['id']); actual.update(ns)
        check(ns and min(ns)>=1 and max(ns)<=f['line_count'], 'comparison bound:' + c['id'])
        check(c['physical_read_mode'] == 'actual_text_read_this_followup', 'physical read mode:' + c['id'])
        check(c['execution_status'] == 'NOT_EXECUTED', 'comparison executed:' + c['id'])
        check(bool(c['comparison']), 'missing semantic disposition:' + c['id'])
        if c['disposition'] in ('received','existing_confirmed_gap'):
            check(bool(c['current_receivers']), 'missing receiver:' + c['id'])
        types[c['disposition']] += len(ns)
        index_expected(f, c['id'], c['original_ranges'], c['disposition'], c['current_receivers'],
                       c['existing_formal_comparison_group_refs'])
    check(not exact & actual, 'reuse/actual overlap:' + f['id'])
    check(exact | actual == set(range(1,f['line_count']+1)), 'unclosed original:' + f['id'])
    check(actual == points(f['physical_read_ranges_new']), 'physical ledger:' + f['id'])
    check(exact | actual == points(f['semantic_compared_ranges']), 'semantic ledger:' + f['id'])
    check(f['review_extent']=='full' and not f['unreviewed_comparison_ranges'], 'review status:' + f['id'])
    total_exact += len(exact); total_read += len(actual); total_lines += f['line_count']
    ledger = next(e for e in cov['original_specification_comparison']['files'] if e['id']==f['id'])
    check(ledger['physical_read_ranges_this_followup']==f['physical_read_ranges_new'] and
          ledger['semantic_compared_ranges']==f['semantic_compared_ranges'] and
          ledger['qualified_reuse']==f['qualified_exact_reuse'] and
          ledger['comparison_ids']==[c['id'] for c in f['comparisons']], 'coverage projection:' + f['id'])

check((len(x['files']),total_lines,total_exact,total_read)==(14,3854,935,2919), 'original navigation totals')
check(dict(types)==x['navigation_counts_only']['disposition_line_counts'], 'disposition totals')
check(not types.get('unreceived_correct_fact',0) and not x['new_findings'], 'unexpected new gap')
inverse = [{'current_path':p,'current_version':x['specification_baseline']['commit'],'current_lines':[a,b],
            'original_comparisons':v} for (p,a,b),v in sorted(expected_inverse.items())]
check(inverse==x['current_to_original'], 'reverse original/current mapping')
check(rev['original_comparison_projection']['current_to_original']==inverse, 'external inverse projection')
check(rev['original_comparison_projection']['original_to_current_and_source_groups']==x['comparison_to_existing_source_groups'], 'external forward projection')
check(len(x['comparison_to_existing_source_groups'])==len(records), 'forward record count')
for v in x['comparison_to_existing_source_groups']:
    check(records.get(v['comparison_id']) == (v['original_path'],v['original_ranges'],v['disposition'],
                                            v['existing_formal_comparison_group_refs']), 'forward record:' + v['comparison_id'])
group_inverse = [{'group_id':g,'comparison_ids':sorted(ids)} for g,ids in sorted(expected_groups.items())]
check(group_inverse==x['existing_source_group_to_original_comparisons'], 'source group inverse')
check(src['original_comparison_projection']['source_group_to_original']==group_inverse, 'external source inverse')
check([f['id'] for f in findings['findings']]==x['prior_findings_preserved'], 'prior finding identities')
check(all(f['status']=='candidate_pending_independent_counterevidence' and
          not f['review_resolution']['required_revision_signed_off'] for f in findings['findings']), 'self sign-off')
check(all(o['effective_parent_corrections']==x['effective_parent_corrections'] for o in (cov,src,rev,prog)), 'parent correction propagation')
check(findings['bounded_original_comparison_followup']['effective_parent_corrections']==x['effective_parent_corrections'], 'finding correction')
check(prog['reference_execution_count']==prog['behavior_model_execution_count']==0, 'unexpected execution')
check(x['model_request']['actual_parameter_echo']=='UNVERIFIED', 'parameter echo changed')
check(x['complete'] and x['navigation_counts_only']['unclosed_original_lines']==0, 'original incomplete')
result = {'schema_version':'gr5.review.v1','module':'M08','kind':'bounded_original_artifact_integrity_only',
          'passed':not errors,'errors':errors,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'reference_source_read_or_executed_by_this_validator':False,'behavior_model_executed':False,
          'original_files':len(x['files']),'original_lines':total_lines,'qualified_exact_reuse_lines':total_exact,
          'actual_read_difference_lines':total_read,'unclosed_lines':0,'new_findings':0,
          'prior_core_objects_unchanged':core==x['preserved_prior_core_sha256'],
          'preserved_denominators':x['preserved_denominators'],
          'counts_are_not_semantic_or_execution_proof':True}
write('original-comparison-validation.json',result)
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors:
    sys.exit(1)
