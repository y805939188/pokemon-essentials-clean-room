#!/usr/bin/env python3
"""Prepare/apply receipt-bound cumulative source locators; preserve source and plans."""
from pathlib import Path
import argparse
import copy
import difflib
import gzip
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
INVENTORY = HERE.parents[2]
spec = importlib.util.spec_from_file_location('routing_source_backfill', INVENTORY / 'routing.py')
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def intervals(numbers):
    out = []
    for n in sorted(numbers):
        if out and n == out[-1][1] + 1:
            out[-1][1] = n
        else:
            out.append([n, n])
    return out


def normalize_receipts(refs, old_events):
    events = []
    existing = {tuple(e['batches']): e for e in old_events}
    for commit, path in sorted(refs):
        receipt = json.loads(r.blob(commit, path))
        for index, record in enumerate(receipt['records']):
            assert record['ACCEPTED'] is True and record['actual_integrated_PASS'] is True
            identities = record.get('actual_target_identities') or [record['actual_target_identity']]
            for raw in identities:
                actual = r.identity(record['actual_artifact_commit'], raw['path'])
                assert all(actual[k] == raw[v] for k, v in [('git_blob', 'blob'), ('sha256', 'sha256'), ('bytes', 'bytes')])
            event = {'event_id': record['batch'] + '-ACCEPTED-' + commit[:8], 'status': 'ACCEPTED',
                     'commit': record['actual_artifact_commit'], 'batches': [record['batch']],
                     'documents': [x['path'] for x in identities], 'required_ids': record['required_ids'],
                     'evidence': [{'commit': commit, 'path': path},
                                  {'commit': record['actual_independent_report_commit'], 'path': record['actual_independent_report_path']}],
                     'receipt_record_pointer': f'/records/{index}',
                     'qualification': 'Source batch acceptance only; no route, implementation, phase or whole-round approval'}
            prior = existing.get(tuple(event['batches']))
            if prior:
                assert prior['commit'] == event['commit'] and prior['documents'] == event['documents']
                event = copy.deepcopy(prior)
            events.append(event)
    assert len({e['event_id'] for e in events}) == len(events)
    assert len({tuple(e['batches']) for e in events}) == len(events)
    return sorted(events, key=lambda e: e['batches'])


def map_document(doc, features, snapshot):
    path = doc['source']['path']
    old_hs, old_lines = r.headings(r.blob(r.B8, path))
    new_hs, new_lines = r.headings(r.blob(snapshot, path))
    by_anchor = {h['anchor']: h for h in new_hs}
    old_owner = {}
    for f in features:
        for a, b in f['functional_scope']['line_ranges']:
            for number in range(a - 1, b):
                assert number not in old_owner
                old_owner[number] = f['feature_id']
    selected = {f['feature_id']: by_anchor[f['source']['anchor']] for f in features}
    current_owner = {}
    ambiguities = []
    for tag, a, b, c, d in difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False).get_opcodes():
        if tag == 'equal':
            for old_index in range(a, b):
                if old_index in old_owner:
                    current_owner[c + old_index - a] = old_owner[old_index]
            continue
        if tag == 'delete':
            continue
        adjacent = {old_owner[i] for i in range(a, b) if i in old_owner}
        if tag == 'insert':
            adjacent = {old_owner[i] for i in [a - 1, a] if i in old_owner}
        for new_index in range(c, d):
            candidates = {fid for fid, h in selected.items() if h['line_start'] <= new_index + 1 <= h['line_end']}
            narrowed = candidates & adjacent
            if len(narrowed) == 1:
                current_owner[new_index] = next(iter(narrowed))
            elif len(candidates) == 1:
                current_owner[new_index] = next(iter(candidates))
            elif candidates:
                ambiguities.append({'path': path, 'new_line': new_index + 1, 'operation': tag,
                                    'old_range': [a + 1, b], 'candidate_ids': sorted(candidates),
                                    'adjacent_ids': sorted(adjacent)})
    assert not ambiguities, json.dumps(ambiguities[:20], ensure_ascii=False)
    locators = {}
    changed_units = []
    actual_identity = r.identity(snapshot, path)
    for f in features:
        fid = f['feature_id']
        ranges = intervals(i + 1 for i, owner in current_owner.items() if owner == fid)
        assert ranges, f'No current source range: {fid}'
        h = selected[fid]
        assert all(h['line_start'] <= a <= b <= h['line_end'] for a, b in ranges), fid
        unit = ''.join(''.join(new_lines[a - 1:b]) for a, b in ranges).encode()
        old_unit = ''.join(''.join(old_lines[a - 1:b]) for a, b in f['functional_scope']['line_ranges']).encode()
        locators[fid] = {'heading': h['title'], 'anchor': h['anchor'], 'heading_level': h['level'],
                         'heading_sha256': h['heading_sha256'], 'line_ranges': ranges,
                         'unit_sha256': r.digest(unit), 'file_sha256': actual_identity['sha256'],
                         'file_git_blob': actual_identity['git_blob']}
        if unit != old_unit:
            changed_units.append(fid)
    return new_hs, locators, changed_units


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare', 'apply'])
    parser.add_argument('--snapshot', required=True)
    parser.add_argument('--extra-receipt', action='append', default=[], help='40-hex commit:Git-relative receipt path')
    parser.add_argument('--new-mapping', action='append', type=Path, default=[])
    args = parser.parse_args()
    input_manifest_bytes = (INVENTORY / 'routing-manifest.json').read_bytes()
    manifest = json.loads(input_manifest_bytes)
    coverage = r.read_json(INVENTORY / 'section-coverage.json')
    old_registry = r.read_json(INVENTORY / 'accepted-source-updates.json')
    intake = r.read_json(HERE / 'accepted-receipt-intake.json')
    refs = {(e['receipt_commit'], e['receipt_path']) for e in intake['events']}
    refs.update(tuple(value.split(':', 1)) for value in args.extra_receipt)
    events = normalize_receipts(refs, old_registry['events'])
    event_map = {e['event_id']: e for e in events}
    accepted_paths = {path for e in events for path in e['documents']}
    changed_paths = r.git('diff', '--name-only', r.B8, args.snapshot, '--', r.FORMAL).decode().splitlines()
    unaccepted_paths = sorted(set(changed_paths) - accepted_paths)
    actual_paths = r.git('ls-tree', '-r', '--name-only', args.snapshot, '--', r.FORMAL).decode().splitlines()
    assert sorted(p for p in actual_paths if p.endswith('.md')) == sorted(d['source']['path'] for d in manifest['documents']), 'Formal index changed: explicit scope reconciliation required'
    readings = r.read_json(INVENTORY / 'revisions/r2/accepted-source-reading.json')
    mappings = {(h['document'], h['anchor']): h for h in readings['new_heading_coverage']['accepted_mappings']}
    for path in args.new_mapping:
        additional = r.read_json(path)
        if isinstance(additional, dict):
            additional = additional['accepted_mappings']
        for h in additional:
            assert h['source_acceptance'] == 'RECEIPT_BOUND_ACCEPTED_SOURCE', 'Proposed/pending mappings are not accepted input'
            assert h.get('basis'), 'Explicit current-heading mapping needs source basis'
            mappings[(h['document'], h['anchor'])] = h
    original_sections = {(s['path'], s['anchor']): s for s in coverage['sections']}
    new_sections = []
    locators = {}
    changed_units = []
    unresolved = []
    before = copy.deepcopy(manifest)
    _, wp, batches = r.fixed_inputs()
    snapshot = {'commit': args.snapshot,
                'formal_tree': r.git('rev-parse', args.snapshot + ':' + r.FORMAL.rstrip('/')).decode().strip(),
                'upstream_calibration': 'RECEIPT_BOUND_CUMULATIVE_SOURCE; ROUTING_REVIEW_AND_WHOLE_ROUND_CLOSED_PENDING'}
    for doc in manifest['documents']:
        path = doc['source']['path']
        fs = [f for f in manifest['features'] if f['document_id'] == doc['document_id']]
        hs, mapped, changed = map_document(doc, fs, args.snapshot)
        locators.update(mapped)
        changed_units.extend(changed)
        eids = sorted(e['event_id'] for e in events if path in e['documents'])
        _, _, binding = r.effective_doc_bindings(path, wp, batches, event_map)
        binding['accepted_events'] = eids
        if binding['batches'] and set(binding['batches']) <= r.covered_batches(binding, event_map):
            binding['status'] = '已回填ACCEPTED源规格；去向待独立复审'
        doc['upstream'] = binding
        identity = r.identity(args.snapshot, path)
        changed_source = identity['sha256'] != doc['source']['sha256']
        doc['current_applicability'] = {'snapshot_commit': args.snapshot, 'path': path, 'identity': identity,
                                       'source_equivalence': ('CHANGED_ACCEPTED_SOURCE' if eids else 'CHANGED_PENDING_ACCEPTANCE_NOT_APPLIED') if changed_source else 'SAME_BYTES',
                                       'status': '已按ACCEPTED回执核对' if eids else ('待整改后核对；仅准备映射未应用' if changed_source else '后继快照同字节；保留原核对资格')}
        for f in fs:
            f['upstream'] = copy.deepcopy(binding)
            f['current_applicability'].update(snapshot_commit=args.snapshot, document=path, locator=mapped[f['feature_id']])
            if eids:
                f['current_applicability'].update(status='已按ACCEPTED回执核对', source_state='历史来源保持；当前定位与ACCEPTED实际快照单列')
        for h in hs:
            key = (path, h['anchor'])
            prior = original_sections.get(key)
            explicit = mappings.get(key)
            if prior:
                relation = {'feature_refs': copy.deepcopy(prior['feature_refs']),
                            'metadata_refs': copy.deepcopy(prior.get('metadata_refs', [])),
                            'coverage_scope': prior.get('coverage_scope', 'EXPLICIT_SOURCE_FUNCTIONS_OR_METADATA'),
                            'metadata_reason': prior.get('metadata_reason', 'Retained explicit source functional mapping')}
                basis = 'RETAIN_EXPLICIT_SOURCE_MAPPING_BY_UNCHANGED_ANCHOR; not a new source quotation'
            elif explicit:
                relation = {'feature_refs': explicit['feature_refs'], 'metadata_refs': explicit['metadata_refs'],
                            'coverage_scope': 'EXPLICIT_EXISTING_CONSUMERS', 'metadata_reason': explicit['basis']}
                basis = 'AUTHOR_EXPLICIT_NEW_HEADING_MAPPING; independent review pending'
            else:
                relation = {'feature_refs': [], 'metadata_refs': [], 'coverage_scope': 'UNRESOLVED_PENDING_ACCEPTANCE',
                            'metadata_reason': 'No accepted explicit mapping; do not infer consumers from WP numbers'}
                unresolved.append({'document': path, 'anchor': h['anchor'], 'title': h['title']})
                basis = 'PENDING'
            new_sections.append({'document_id': doc['document_id'], 'path': path,
                                 **{k: h[k] for k in ['level', 'title', 'anchor', 'line_start', 'line_end', 'heading_sha256']},
                                 **relation, 'mapping_basis': basis, 'accepted_events': eids})
    result = {'schema_version': 'routing-current-source-backfill.v1', 'command': args.command,
              'input_manifest_sha256': r.digest(input_manifest_bytes),
              'backfill_tool_sha256': r.digest(Path(__file__).read_bytes()),
              'locator_mapping_method': 'Exact line alignment and containing source-heading context; ambiguous ownership refuses, never infers destination',
              'snapshot': snapshot, 'events': events, 'unaccepted_changed_formal_paths': unaccepted_paths,
              'unresolved_new_headings': unresolved, 'historical_headings_preserved': len(coverage['sections']),
              'current_headings_observed': len(new_sections), 'accepted_receipt_batches': sorted(e['batches'][0] for e in events),
              'current_locators': locators, 'directly_changed_feature_units_vs_fixed_functional_source': sorted(changed_units),
              'scope': 'AUTHOR_SOURCE_APPLICABILITY_ONLY; no route, phase, implementation, compatibility or whole-round acceptance'}
    candidate = copy.deepcopy(manifest)
    candidate['current_snapshot'] = snapshot
    registry = {'schema_version': 'routing-accepted-source-updates.v1', 'events': events,
                'state': 'CUMULATIVE_SOURCE_ACCEPTED_ROUTING_REVIEW_PENDING',
                'instruction': 'Fixed receipt-bound source acceptance only; destination, phase, implementation and whole-round gates stay separate'}
    candidate_errors = r.errors(candidate, coverage, registry)
    result['prepared_candidate_validation_errors'] = candidate_errors
    result['all_prepared_errors_are_unaccepted_path_guards'] = all(
        any(error == path + ': false source equivalence' or error == path + ': changed current source requires accepted calibration'
            for path in unaccepted_paths) for error in candidate_errors)
    r.save_json(HERE / 'prepared-source-backfill.json', result)
    if args.command == 'apply':
        assert not unaccepted_paths, 'Refuse cumulative source switch: formal changes lack ACCEPTED receipts'
        assert not unresolved, 'Refuse incomplete current heading coverage'
        manifest['current_snapshot'] = snapshot
        assert all(f['source'] == next(x['source'] for x in before['features'] if x['feature_id'] == f['feature_id']) for f in manifest['features'])
        assert all(f['future_plan'] == next(x['future_plan'] for x in before['features'] if x['feature_id'] == f['feature_id']) for f in manifest['features'])
        assert manifest['retired_features'] == before['retired_features']
        errors = r.errors(manifest, coverage, registry)
        assert not errors, json.dumps(errors[:20], ensure_ascii=False)
        assert (INVENTORY / 'routing-manifest.json').read_bytes() == input_manifest_bytes, 'Concurrent manifest change: refuse overwrite'
        archive = HERE / ('source-backfill-input-' + r.digest(input_manifest_bytes)[:12] + '.json.gz')
        archive.write_bytes(gzip.compress(input_manifest_bytes, mtime=0))
        result['input_manifest_archive'] = str(archive.relative_to(INVENTORY))
        r.save_json(INVENTORY / 'routing-manifest.json', manifest)
        r.save_json(INVENTORY / 'accepted-source-updates.json', registry)
        r.save_json(INVENTORY / 'current-section-coverage.json', {'schema_version': 'routing-current-section-coverage.v1',
                    'snapshot': snapshot, 'source_baseline_commit': r.B8, 'sections': new_sections,
                    'qualification': 'Current source heading navigation only; fixed historical section-coverage remains untouched; source acceptance is not route validation'})
        result['applied'] = True
        result['source_and_future_plans_unchanged'] = True
        r.save_json(HERE / 'accepted-backfill-result.json', result)
    print(json.dumps({k: v for k, v in result.items() if k not in ['events', 'current_locators']}, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
