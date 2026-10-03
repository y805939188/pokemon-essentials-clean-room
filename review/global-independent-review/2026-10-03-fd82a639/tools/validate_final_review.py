"""Read-only review-artifact validation. Never executes reference code.

Git reads below inspect fixed text identities and publication boundaries only.
Line existence and record counts are not proof of behavioral correctness.
"""
import argparse
import collections
import csv
import json
from pathlib import Path
import re
import subprocess

BASE = 'e1e01bb18d824931e54f182dd61af5a9f908ba85'
REF = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
RUN = 'review/global-independent-review/2026-10-03-fd82a639'

def git(root, *args):
    return subprocess.check_output(['git', '--no-optional-locks', '-C', str(root), *args])

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--root', required=True)
    p.add_argument('--reference', required=True)
    p.add_argument('--allow-final-qa-pending', action='store_true')
    args = p.parse_args()
    root, ref = Path(args.root), Path(args.reference)
    run = root / RUN
    errors, checks = [], {}
    def check(name, value):
        checks[name] = bool(value)
        if not value:
            errors.append(name)
    def table(name):
        with (run / name).open() as f:
            return list(csv.DictReader(f, delimiter='\t'))
    def document(name):
        return json.loads((run / name).read_text())
    # Current records only; frozen independent reports keep their original schemas.
    findings = document('findings.json')
    mapping = document('root/raw-to-global-finding-map.json')
    required = [e for e in findings if e['required_revision']]
    check('233_unique_canonical_findings', len(findings) == len({e['id'] for e in findings}) == 233)
    check('229_required_200P2_29P3', len(required) == 229 and collections.Counter(e['priority'] for e in required) == {'P2': 200, 'P3': 29})
    check('no_unadjudicated_current_findings', all(e['status'] in ['CONFIRMED_REQUIRED_REVISION', 'PARTIALLY_ADDRESSED_RESIDUAL_OPEN', 'NOT_REQUIRED_HISTORICAL_CONTEXT', 'NOT_REQUIRED_AS_REPORTED'] for e in findings))
    check('251_raw_ids_once', len(mapping['mapping']) == 251 and len([r['raw_id'] for e in findings for r in e['raw_reports']]) == len({r['raw_id'] for e in findings for r in e['raw_reports']}) == 251)
    check('46_extensions_adjudicated', sum(len(e.get('extensions', [])) for e in findings) == 46 and all(not x['adjudication'].startswith('PENDING') for e in findings for x in e.get('extensions', [])))
    fields = ['id', 'priority', 'type', 'status', 'confidence', 'work_packages', 'current_claim', 'source_behavior_or_ambiguity', 'premises', 'minimum_counterexample', 'impact', 'minimum_revision', 'determinate_recheck', 'evidence', 'reviewers', 'current_qualifications']
    check('required_fields_and_reviewers_present', all(all(e.get(k) for k in fields) for e in findings))
    check('domain_feature_or_governance_exception', all(e.get('features') or e['id'] == 'WP80-INTAKE-C01' for e in findings))
    cache, location_errors = {}, []
    for e in findings:
        for v in e['evidence']:
            repo = v.get('repository')
            expected_commit = REF if repo == 'reference' else BASE
            if repo not in ['reference', 'project'] or v.get('commit') != expected_commit or not v.get('path'):
                location_errors.append([e['id'], 'identity', v])
                continue
            key = (repo, v['commit'], v['path'])
            if key not in cache:
                try:
                    cache[key] = len(git(ref if repo == 'reference' else root, 'show', v['commit'] + ':' + v['path']).decode().splitlines())
                except (subprocess.CalledProcessError, UnicodeError):
                    cache[key] = -1
            value = str(v['line_start']) + '-' + str(v.get('line_end', v['line_start'])) if 'line_start' in v else str(v.get('lines', v.get('line', '')))
            value = value.replace('–', '-').replace('—', '-')
            nums = [int(n) for n in re.findall(r'\d+', value)]
            if not re.fullmatch(r'[0-9,;\- ]+', value) or not nums or min(nums) < 1 or max(nums) > cache[key]:
                location_errors.append([e['id'], v['path'], value, cache[key]])
    check('all_canonical_evidence_identity_path_and_line_bounds', not location_errors)
    wps = table('wp-review-matrix.tsv')
    expected = {f'WP{x:02}' for x in range(1, 81)}
    for family, parts in [(47, 'AB'), (52, 'ABC'), (66, 'ABC'), (67, 'AB'), (73, 'AB')]:
        expected.remove(f'WP{family:02}')
        expected.update(f'WP{family:02}-{part}' for part in parts)
    check('87_exact_WP_identities', len(wps) == 87 and {w['wp'] for w in wps} == expected)
    check('owners_A30_B26_C28_ROOT3', collections.Counter(w['primary_agent'] for w in wps) == {'A': 30, 'B': 26, 'C': 28, 'ROOT': 3})
    check('no_family_as_executable_finding_WP', all(w in expected for e in findings for w in e['work_packages']))
    if not args.allow_final_qa_pending:
        check('87_dispositions_complete', all(w['status'] == 'REVIEW_COMPLETE' and w['decision'] in ['PASS_SCOPED', 'REQUIRES_REVISION_SCOPED'] for w in wps))
        check('run_final_statuses', document('run-manifest.json')['status'] == 'REVIEW_COMPLETE')
        check('no_active_assignments', all('PENDING' not in x['status'] and x['status'] != 'IN_PROGRESS' for x in document('assignments.json')))
    io = table('input-output-equivalence.tsv')
    feature = table('root/feature-reverse-navigation.tsv')
    sources = table('source-coverage.tsv')
    check('113_input_rows', len(io) == len({x['input'] for x in io}) == 113)
    destinations = {p for x in io for p in x['outputs'].split(';')}
    check('112_destinations_111_bodies_scope', len(destinations) == 112 and len([x for x in destinations if not x.endswith('scope-statement.md')]) == 111)
    check('113_features_125_edges', len(feature) == len({x['feature'] for x in feature}) == 113 and sum(len(x['wps'].split(';')) for x in feature) == 125)
    check('feature_expansion_complete', {p for x in feature for p in x['original_paths'].split(';')} == {x['input'] for x in io} and {p for x in feature for p in x['outputs'].split(';')} == destinations)
    check('WP47B_F0805_bidirectional', 'WP47-B' in next(x for x in feature if x['feature'] == 'F08-05')['wps'].split(';') and 'F08-05' in next(x for x in wps if x['wp'] == 'WP47-B')['features'].split(';'))
    reference_files = set(git(ref, 'ls-files', '-z').decode().rstrip('\0').split('\0'))
    check('432_inclusive_source_rows', len(sources) == 432 and {x['path'] for x in sources} == reference_files)
    check('source_limits_retained', all(x['current_scope_limit'] and x['reading_is_not_coverage'] == 'TRUE' for x in sources))
    inputs = table('input-index.tsv')
    counts = collections.Counter(x['role'] for x in inputs)
    check('input_roles_113_111_17_1', counts['original-specification-or-appendix'] == 113 and counts['sanitized-body'] == 111 and counts['static-test-family'] == 17 and counts['static-test-index'] == 1)
    queue = table('root/remediation-index.tsv')
    check('remediation_exactly_required_ids', len(queue) == 229 and {x['finding_id'] for x in queue} == {x['id'] for x in required})
    canonical = {e['id'] for e in findings}
    retired = mapping['retired_provisional_global_redirects']
    check('retired_ids_not_counted', not (set(retired) & canonical) and all(v in canonical for v in retired.values()))
    junctions = table('root/wp78-junction-recheck.tsv')
    check('54_junctions_disposed', len(junctions) == len({x['junction'] for x in junctions}) == 54 and all('PENDING' not in x['current_disposition'] for x in junctions))
    changed = git(root, 'diff', '--name-only', BASE, 'HEAD').decode().splitlines()
    check('head_diff_only_run_outputs', all(p.startswith(RUN + '/') for p in changed))
    # Explicit root-document hyperlinks, not source text, must resolve locally.
    broken = []
    for name in ['final-report.md', 'wp78-wp79-wp80-review.md', 'cross-module-review.md', 'remediation-plan.md', 'handoff.md']:
        for link in re.findall(r'\]\(([^)]+)\)', (run / name).read_text()):
            if '://' not in link and not (run / link.split('#')[0]).exists():
                broken.append([name, link])
    check('final_document_links_resolve', not broken)
    print(json.dumps(dict(status='PASS' if not errors else 'FAIL', project_base=BASE, reference_commit=REF, review_head=git(root, 'rev-parse', 'HEAD').decode().strip(), inspection='Current review files; fixed input Git objects. HEAD alone does not identify uncommitted review edits.', working_tree_status=git(root, 'status', '--porcelain=v1', '--untracked-files=all').decode().splitlines(), checks=checks, errors=errors, canonical_evidence_locations=sum(len(e['evidence']) for e in findings), distinct_evidence_objects=len(cache), location_errors=location_errors, broken_links=broken, limits='Review metadata and fixed text identity checks only; no behavioral execution or coverage percentage.'), ensure_ascii=False, indent=2))
    raise SystemExit(0 if not errors else 1)

if __name__ == '__main__':
    main()
