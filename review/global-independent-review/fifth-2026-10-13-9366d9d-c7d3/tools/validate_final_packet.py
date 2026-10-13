#!/usr/bin/env python3
"""Read-only integrity checks for the completed review packet, not behavior tests."""
import argparse, ast, collections, hashlib, json, pathlib, sys
from assemble_review import render_finding

ROOT = pathlib.Path(__file__).resolve().parents[1]
PREFIX = 'review/global-independent-review/fifth-2026-10-13-9366d9d-c7d3/'
cache = {}
errors = []
checks = {}

def read(path):
    if path not in cache:
        cache[path] = json.loads((ROOT / path).read_text())
    return cache[path]

def check(name, condition, detail=None):
    checks[name] = bool(condition)
    if not condition:
        errors.append({'check': name, 'detail': detail})

def pointer(ref):
    path = ref['path'].removeprefix(PREFIX)
    value = read(path)
    for part in ref.get('pointer', '').split('/')[1:]:
        part = part.replace('~1', '/').replace('~0', '~')
        value = value[int(part)] if isinstance(value, list) else value[part]
    return value

def identity(path):
    b = (ROOT / path).read_bytes()
    return {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(b)).encode() + b'\0' + b).hexdigest()}

def validate_syntax():
    counts = collections.Counter()
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or '__pycache__' in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        try:
            if path.suffix == '.json':
                json.loads(path.read_text()); counts['json'] += 1
            elif path.suffix == '.jsonl':
                for line in path.read_text().splitlines():
                    if line.strip(): json.loads(line)
                counts['jsonl'] += 1
            elif path.suffix == '.py':
                ast.parse(path.read_text(), filename=rel); counts['python_ast'] += 1
        except Exception as exc:
            errors.append({'check': 'artifact_syntax', 'path': rel, 'error': str(exc)})
    check('artifact_syntax', not errors)
    return dict(counts)

def validate_final():
    findings = read('findings.json')['findings']
    ids = {f['id'] for f in findings}
    check('106_unique_canonical_records', len(ids) == len(findings) == 106)
    counts = collections.Counter(f['disposition'] for f in findings)
    check('canonical_dispositions', counts == {'required': 92, 'optional': 7, 'no_required_revision': 7}, dict(counts))
    required = {f['id'] for f in findings if f['disposition'] == 'required'}
    minimum = ('id title module severity disposition status reviewer category source_baseline '
               'specification_baseline source_anchors spec_anchors expected_reference_behavior '
               'current_spec_behavior gap preconditions minimal_counterexample normal_case '
               'failure_or_boundary_case impact_on_independent_implementation negative_evidence_search '
               'proposed_spec_change affected_files shared_contracts acceptance_criteria dependencies '
               'related_capabilities related_findings root_cause_group priority history_links evidence_level '
               'execution_status confidence unknowns excluded_claims user_decision_needed review_resolution').split()
    missing = {f['id']: [k for k in minimum if k not in f] for f in findings}
    check('canonical_schema_fields', not any(missing.values()), {k:v for k,v in missing.items() if v})
    check('required_nonproposer_resolution', all(f['review_resolution'] for f in findings if f['id'] in required))
    fw = read('source-to-spec-coverage.json')
    rows = fw['rows']
    check('1460_unique_scopes', len(rows) == len({r['scope_id'] for r in rows}) == 1460)
    check('no_unreviewed_scope_status', all(r['status'] in {'supported','partial','missing','unresolved'} for r in rows))
    check('source_overlays_all_canonical', {r['id'] for r in fw['finding_scope_overlays']} == ids)
    fields = read('modules/ASM/evidence-fields.json')['fields']
    field_errors = []
    for key, value in fields.items():
        try:
            actual = pointer(value['ref'])
            if actual != value['value']:
                field_errors.append({'field_id': key, 'error': 'value differs from exact ref'})
        except Exception as exc:
            field_errors.append({'field_id': key, 'error': str(exc)})
    check('all_evidence_field_values_match_exact_refs', not field_errors, field_errors)
    flds = ('purpose','caller_override','preconditions','configuration_host','dependencies','unknowns','reviewed_scope','status_reason')
    unresolved = []
    for r in rows:
        for fld in flds:
            if fld not in r or not r[fld]:
                unresolved.append([r['scope_id'], fld, 'missing'])
            elif isinstance(r[fld], dict):
                for e in r[fld].get('evidence', []):
                    if e.get('field_id') not in fields:
                        unresolved.append([r['scope_id'], fld, e.get('field_id')])
        if r.get('missing_field_dispositions'): unresolved.append([r['scope_id'], 'remaining missing-field disposition'])
    check('matrix_fields_and_field_ids_complete', not unresolved, unresolved)
    inv = read('spec-to-source-coverage.json')
    check('25704_unique_inverse_units', len(inv['units']) == len({r['inverse_unit_id'] for r in inv['units']}) == 25704)
    check('inverse_overlays_all_canonical', {r['finding_id'] for r in inv['canonical_clause_overlays']} == ids)
    refs_failed = []
    for u in inv['units']:
        for k in ('normalized_ref','actual_record_ref'):
            try: pointer(u[k])
            except Exception as exc: refs_failed.append([u['inverse_unit_id'], k, str(exc)])
    check('all_inverse_record_pointers_resolve', not refs_failed, refs_failed)
    files = read('inventory-and-reading-coverage.json')['files']
    check('723_unique_file_identities', len(files) == len({(r['version'],r['path']) for r in files}) == 723)
    check('no_remaining_available_file_ranges', not any(r['remaining_semantic_or_context_ranges'] for r in files))
    corpus = read('corpus-inventory.json')
    known = {(r['version'], r['path']) for r in files}
    historical = {'historical_review_candidate_snapshot_or_receipt','historical_recovery_or_update_handoff','delivery_provenance_navigation','project_instructions_or_repository_metadata'}
    unmatched = [r['path'] for r in corpus['specification_repository'] if (r.get('baseline'),r['path']) not in known and r.get('currentness') not in historical]
    check('all_current_corpus_files_received', not unmatched, unmatched)
    shared = read('shared-contracts.json')
    contracts = {c['id']:c for c in shared['contracts']}
    check('unique_shared_contract_ids', len(contracts) == len(shared['contracts']))
    check('unique_shared_primary_owner', all(c.get('primary_review_owner') for c in contracts.values()))
    check('shared_named_producer_consumer_failure_fields', all(all(c.get(k) for k in ('producer','write','consumer','display','persistence','failure','source_anchors','spec_anchors','finite_comparison_ids')) for c in contracts.values()))
    check('shared_no_unreviewed_current_projection', all(c.get('status') in {'supported','partial','missing','unresolved'} and not c.get('unreviewed_assigned_scope') for c in contracts.values()))
    check('all_finding_routes_resolve', all(r['finding_id'] in ids and r['canonical_contract_id'] in contracts for r in shared['finding_label_routes']))
    check('all_canonical_findings_have_qualified_routes', {r['finding_id'] for r in shared['finding_label_routes']} == ids)
    maps = {r['id'] for r in read('modules/JXN/source-to-spec.json')['mappings']}
    check('all_shared_finite_comparisons_resolve', all(set(c.get('finite_comparison_ids', [])) <= maps for c in contracts.values()))
    routes = shared['domain_interface_join']
    check('182_domain_routes_resolve', len(routes) == 182 and all(r['canonical_id'] in contracts for r in routes))
    route_errors = []
    for r in routes:
        try:
            actual = pointer(r)
            if 'domain_record_snapshot' in r and actual != r['domain_record_snapshot']:
                route_errors.append([r['module'],r['domain_interface_id'],'source record differs from received snapshot'])
        except Exception as exc: route_errors.append([r['module'],r['domain_interface_id'],str(exc)])
    check('domain_route_record_pointers_resolve', not route_errors, route_errors)
    chains = read('junction-review.json')['chains']
    check('15_current_finite_chains_complete', len(chains) == len({r['id'] for r in chains}) == 15 and all(not r.get('unreviewed') and r['status'] in {'supported','partial','missing','unresolved'} for r in chains))
    check('chain_comparisons_and_contracts_resolve', all(set(r['finite_comparison_ids']) <= maps and set(r['shared_contract_ids']) <= set(contracts) for r in chains))
    plan = read('proposed-update-batches.json')
    batches = {b['id']:b for b in plan['batches']}
    by_finding = collections.Counter(f for b in batches.values() for f in b.get('finding_ids', []))
    check('each_required_has_one_batch', set(by_finding) == required and all(n == 1 for n in by_finding.values()), dict(by_finding))
    edges = plan['dependency_edges']; incoming = {b:set() for b in batches}
    for before, after in edges: incoming[after].add(before)
    ordered = []
    while incoming:
        ready = [b for b, deps in incoming.items() if not deps]
        if not ready: break
        ordered.extend(ready)
        for b in ready: del incoming[b]
        for deps in incoming.values(): deps.difference_update(ready)
    check('batch_dependencies_acyclic', not incoming, {k:sorted(v) for k,v in incoming.items()})
    owners = read('shared-file-owners.json')['files']
    check('unique_file_writers', len(owners) == len({r['path'] for r in owners}) and all(r['writer'] for r in owners))
    check('allowed_revision_paths_exist', all((ROOT.parents[2]/r['path']).is_file() for r in owners))
    handoff = (ROOT/'cloud-fifth-update-handoff-prompt.md').read_text()
    check('handoff_all_finding_ids', all(fid in handoff for fid in ids))
    check('handoff_expands_every_full_canonical_record', all(render_finding(f) in handoff for f in findings))
    check('handoff_static_complete_sections', all(s in handoff for s in ('完整前提','逐项验收标准','GR4、GR3及旧229/341限定关系','独立反证及最终裁决')))
    return {'findings':dict(counts), 'scope_rows':len(rows),'inverse_units':len(inv['units']),'evidence_fields':len(fields),'file_identities':len(files),'shared_contracts':len(contracts),'topological_batch_order':ordered}

def validate_manifest():
    manifest = read('cloud-fifth-update-handoff-manifest.json')
    failed = []
    for record in manifest['report_artifacts']:
        p = record['path'].removeprefix(PREFIX)
        actual = identity(p)
        if any(record[k] != v for k,v in actual.items()): failed.append(p)
    check('manifest_all_full_byte_identities', not failed, failed)
    check('handoff_has_bound_commit', 'SEMANTIC_COMMIT_BOUND_BY_PUBLICATION_SUCCESSOR' not in (ROOT/'cloud-fifth-update-handoff-prompt.md').read_text())
    return {'manifest_artifacts':len(manifest['report_artifacts'])}

if __name__ == '__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--phase',choices=['syntax','semantic','manifest'],default='semantic');parser.add_argument('--output',required=True);args=parser.parse_args()
    statistics=validate_syntax()
    try:
        if args.phase in {'semantic','manifest'}: statistics.update(validate_final())
        if args.phase == 'manifest': statistics.update(validate_manifest())
    except Exception as exc:
        errors.append({'check':'validation_interrupted','error':repr(exc)})
    result={'schema_version':'gr5.final-artifact-validation.v1','evidence_level':'TOOL_VALIDATION','behavior_execution':False,'passed':not errors,'checks':checks,'statistics':statistics,'errors':errors,'scope':'Full JSON/JSONL syntax, Python AST and current packet identities/IDs/pointers/field equality/DAG. No new semantic or runtime certification.'}
    pathlib.Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'passed':result['passed'],'statistics':statistics,'errors':errors[:10]},ensure_ascii=False))
    sys.exit(0 if result['passed'] else 1)
