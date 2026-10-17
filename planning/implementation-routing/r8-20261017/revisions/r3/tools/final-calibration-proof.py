#!/usr/bin/env python3
"""Summarize author final fixed-source calibration and exact history preservation."""
from pathlib import Path
import argparse
import collections
import importlib.util
import json
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
INV = HERE.parents[2]
ROOT = INV.parents[2]
PREVIOUS = 'a32873d2860b15d9f5e27727db8f131f4ec433b6'
SNAPSHOT = '5f87743293290de2e219ecdd6c19e88280f60c9a'
TREE = '93dc967b4cdb653359afc123d3b8b318d6475fdd'


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    spec = importlib.util.spec_from_file_location('final_calibration_routing', INV / 'routing.py')
    r = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(r)
    manifest = r.read_json(INV / 'routing-manifest.json')
    coverage = r.read_json(INV / 'section-coverage.json')
    current = r.read_json(INV / 'current-section-coverage.json')
    registry = r.read_json(INV / 'accepted-source-updates.json')
    errors = r.errors(manifest, coverage, registry)
    report = r.report(manifest, coverage)
    def old(name):
        return r.git('show', PREVIOUS + ':' + str((INV / name).relative_to(ROOT)))
    previous = json.loads(old('routing-manifest.json'))
    old_docs = {d['document_id']: d for d in previous['documents']}
    old_features = {f['feature_id']: f for f in previous['features']}
    event_by_id = {e['event_id']: e for e in registry['events']}
    identities = []
    for event in registry['events']:
        for path in event['documents']:
            target = r.identity(event['commit'], path)
            actual = r.identity(SNAPSHOT, path)
            identities.append({'event_id': event['event_id'], 'path': path,
                               'accepted_target': target, 'current': actual,
                               'current_content_matches': all(target[k] == actual[k] for k in ['git_blob', 'sha256', 'bytes'])})
    # Historical U01 UI65 intentionally differs from final U04: the last exact
    # accepted target supplies current bytes; both distinct batch gates remain.
    changed_docs = [d for d in manifest['documents'] if d['source']['sha256'] != d['current_applicability']['identity']['sha256']]
    matching = {d['document_id']: [e for e in d['upstream']['accepted_events']
        if d['current_applicability']['path'] in event_by_id[e]['documents'] and
        all(d['current_applicability']['identity'][k] == r.identity(event_by_id[e]['commit'],d['current_applicability']['path'])[k]
            for k in ['git_blob','sha256','bytes'])] for d in changed_docs}
    doc_identity_ok = all(d['current_applicability']['identity'] == r.identity(SNAPSHOT, d['current_applicability']['path']) for d in manifest['documents'])
    old_keys = {(s['path'],s['anchor']) for s in coverage['sections']}
    added = [s for s in current['sections'] if (s['path'],s['anchor']) not in old_keys]
    mapping_data = r.read_json(INV/'revisions/r3/new-heading-mappings.json')
    mappings = mapping_data['accepted_mappings']
    assert mapping_data['source_identity_heading_sha256_convention']=='SHA256_UTF8_TITLE_ONLY'
    mapping_identities = []
    features_by_id = {f['feature_id']:f for f in manifest['features']}
    for mapping in mappings:
        path = mapping['document']
        hs, lines = r.headings(r.blob(SNAPSHOT,path))
        h = next(h for h in hs if h['anchor']==mapping['anchor'])
        file = r.identity(SNAPSHOT,path)
        expected = {'commit':SNAPSHOT,'document':path,'anchor':h['anchor'],'heading':h['title'],
                    'heading_level':h['level'],'heading_sha256':r.digest(h['title'].encode()),
                    'raw_markdown_heading_sha256':h['heading_sha256'],
                    'line_ranges':[[h['line_start'],h['line_end']]],
                    'unit_sha256':r.digest(''.join(lines[h['line_start']-1:h['line_end']]).encode()),
                    'file_sha256':file['sha256'],'file_git_blob':file['git_blob'],'file_bytes':file['bytes']}
        consumers = all(all(item['source'][key]==features_by_id[item['feature_id']]['source'][key]
                            for key in ['commit','document','anchor','line_ranges'])
                        for item in mapping['consumer_fixed_sources'])
        mapping_identities.append({'path':path,'anchor':h['anchor'],
                                   'source_identity_matches_actual_git':mapping['source_identity']==expected,
                                   'consumer_fixed_source_fields_match_retained_records':consumers})
    historical_files = [p for p in r.git('ls-tree','-r','--name-only',PREVIOUS,'--',str(INV.relative_to(ROOT))).decode().splitlines()
                        if '/revisions/r1/' in p or '/revisions/r2/' in p]
    history = [{'path': path, 'sha256': r.digest((ROOT/path).read_bytes()),
                'identical_to_previous': (ROOT/path).read_bytes() == r.blob(PREVIOUS,path)} for path in historical_files]
    newly_bound = [f['feature_id'] for f in manifest['features'] if not old_features[f['feature_id']]['upstream']['batches'] and f['upstream']['batches']]
    expanded_binding = [f['feature_id'] for f in manifest['features'] if set(f['upstream']['batches']) - set(old_features[f['feature_id']]['upstream']['batches'])]
    semantic_changed = [f['feature_id'] for f in manifest['features'] if any(f[k] != old_features[f['feature_id']][k] for k in ['future_plan','dependencies','differences'])]
    checks = {
        'routing_validation_errors_zero': not errors,
        'exact_final_source_commit_and_tree': manifest['current_snapshot']['commit'] == SNAPSHOT and manifest['current_snapshot']['formal_tree'] == TREE,
        'all131_current_document_identities_match_git': doc_identity_ok,
        'all_changed_current_documents_have_matching_receipt_target_content': all(matching.values()),
        'nine_distinct_accepted_batches': len(registry['events']) == 9 and len({b for e in registry['events'] for b in e['batches']}) == 9,
        'pending_and_partial_remediation_bindings_zero': report['pending_upstream_rows'] == report['partially_backfilled_upstream_rows'] == 0,
        'all_known_remediation_rows_backfilled': report['backfilled_upstream_rows'] == report['known_upstream_rows'],
        'all21_new_headings_have_explicit_existing_consumers': len(added) == 21 and all(s['feature_refs'] or s['metadata_refs'] for s in added),
        'all21_explicit_new_heading_evidence_and_consumer_source_identities_match_git': len(mapping_identities)==21
            and all(row['source_identity_matches_actual_git'] and row['consumer_fixed_source_fields_match_retained_records'] for row in mapping_identities),
        'historical_coverage_exact_bytes_preserved': old('section-coverage.json') == (INV/'section-coverage.json').read_bytes(),
        'all_historical_r1_r2_artifact_bytes_preserved': all(item['identical_to_previous'] for item in history),
        'all_stable_active_and_retired_ids_preserved': {f['feature_id'] for f in manifest['features']} == set(old_features)
            and manifest['retired_features'] == previous['retired_features'],
        'all736_routes_stages_implementation_acceptance_pending': all(f['destination_verification']['status'] == '待验证'
            and f['future_plan']['stage'] == '待定' and f['implementation']['status'] == '未实现'
            and f['implementation']['acceptance_status'] == '未验收' for f in manifest['features']),
        'no_unauthorized_exclusions': all(f['future_plan']['destination'] != '不纳入目标' for f in manifest['features']),
        'all_document_source_identities_unchanged': all(d['source'] == old_docs[d['document_id']]['source'] for d in manifest['documents']),
    }
    result = {'schema_version':'routing-r3-final-calibration-proof.v1',
              'role':'AUTHOR_FIXED_SOURCE_AND_STRUCTURE_EVIDENCE_ONLY; independent semantic review and whole-round CLOSED pending',
              'previous_candidate':PREVIOUS,'current_snapshot':manifest['current_snapshot'],
              'manifest_sha256':r.digest((INV/'routing-manifest.json').read_bytes()),
              'input_sha256':{name:r.digest((INV/name).read_bytes()) for name in [
                  'routing-manifest.json','routing.py','section-coverage.json','accepted-source-updates.json',
                  'current-section-coverage.json','revisions/r3/new-heading-mappings.json',
                  'revisions/r3/tools/final-calibration-proof.py']},
              'counts':{'formal_documents':len(manifest['documents']), 'wp_plan_rows':report['historical_count_comparison_only']['wp_plan_rows_observed'],
                        'historical_headings':len(coverage['sections']), 'current_headings':len(current['sections']), 'new_current_headings':len(added),
                        'active_features':len(manifest['features']), 'retired_features':len(manifest['retired_features']), 'metadata_records':len(manifest['metadata_records']),
                        'source_changed_documents':len(changed_docs),'accepted_target_contributions':len(identities),'accepted_events':len(registry['events']),
                        'known_bound_rows':report['known_upstream_rows'],'backfilled_rows':report['backfilled_upstream_rows'],
                        'pending_rows':report['pending_upstream_rows'],'partially_backfilled_rows':report['partially_backfilled_upstream_rows'],
                        'newly_bound_rows':len(newly_bound),'new_or_extended_binding_rows':len(expanded_binding),
                        'semantic_fields_changed_rows':len(semantic_changed),'historical_r1_r2_files_preserved':len(history)},
              'destination_counts':dict(collections.Counter(f['future_plan']['destination'] for f in manifest['features'])),
              'changed_document_matching_events':matching,'accepted_target_contributions':identities,
              'newly_bound_ids':newly_bound,'new_or_extended_binding_ids':expanded_binding,
              'semantic_fields_changed_ids':semantic_changed,'new_current_headings':added,
              'explicit_new_heading_evidence_identity_checks':mapping_identities,
              'historical_file_preservation':history,'checks':checks,'routing_errors':errors,
              'all_passed':all(checks.values()),
              'not_claimed':['Destination compatibility/prototype PASS','User approval of first-version detail','Implementation or acceptance complete','Independent review PASS','Whole-round CLOSED']}
    r.save_json(args.output,result)
    print(json.dumps({k:v for k,v in result.items() if k in ['counts','checks','all_passed','manifest_sha256']},ensure_ascii=False,indent=2))
    return int(not result['all_passed'])


if __name__ == '__main__':
    sys.exit(main())
