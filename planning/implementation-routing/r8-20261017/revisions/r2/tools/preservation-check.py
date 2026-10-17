#!/usr/bin/env python3
"""Author conservation checks against the exact R1 candidate; not semantic review."""
from pathlib import Path
import argparse
import datetime
import gzip
import hashlib
import json
import subprocess
import sys

INVENTORY = Path(__file__).resolve().parents[3]
ROOT = INVENTORY.parents[2]
PREVIOUS = '5666b7b912e2fb79b5119283ee6a37401a7071db'


def old(name):
    path = str((INVENTORY / name).relative_to(ROOT))
    return json.loads(subprocess.check_output(['git', 'show', f'{PREVIOUS}:{path}'], cwd=ROOT))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    previous = old('routing-manifest.json')
    current_bytes = (INVENTORY / 'routing-manifest.json').read_bytes()
    current = json.loads(current_bytes)
    prior_coverage = old('section-coverage.json')
    coverage = json.loads((INVENTORY / 'section-coverage.json').read_bytes())
    checks = []
    def record(name, passed, detail=None):
        checks.append({'check': name, 'passed': bool(passed), 'detail': detail})
    record('preserve source_baseline', current['source_baseline'] == previous['source_baseline'])
    backfill_path = Path(__file__).resolve().parent / 'accepted-backfill-result.json'
    if current['current_snapshot'] == previous['current_snapshot']:
        record('preserve current snapshot before cumulative backfill', True)
    else:
        backfill = json.loads(backfill_path.read_bytes()) if backfill_path.exists() else {}
        record('bind changed current snapshot to completed accepted-source backfill',
               backfill.get('applied') is True and backfill.get('snapshot') == current['current_snapshot']
               and not backfill.get('unaccepted_changed_formal_paths') and not backfill.get('unresolved_new_headings'))
        archived = gzip.decompress((INVENTORY / backfill['input_manifest_archive']).read_bytes()) if backfill.get('input_manifest_archive') else b''
        record('preserve exact source backfill input bytes', bool(archived) and hashlib.sha256(archived).hexdigest() == backfill.get('input_manifest_sha256'))
        source_input = json.loads(archived) if archived else {'features': []}
        prior_plans = {f['feature_id']: f['future_plan'] for f in source_input['features']}
        record('source backfill preserves every R2 future plan', prior_plans == {f['feature_id']: f['future_plan'] for f in current['features']})
    old_events = {e['event_id']: e for e in old('accepted-source-updates.json')['events']}
    new_events = {e['event_id']: e for e in json.loads((INVENTORY / 'accepted-source-updates.json').read_bytes())['events']}
    record('preserve all exact earlier accepted source events', all(new_events.get(eid) == e for eid, e in old_events.items()))
    old_active = {f['feature_id']: f for f in previous['features']}
    active = {f['feature_id']: f for f in current['features']}
    old_retired = {f['feature_id']: f for f in previous['retired_features']}
    retired = {f['feature_id']: f for f in current['retired_features']}
    combined = {**retired, **active}
    record('preserve every existing stable ID', set(old_active) | set(old_retired) <= set(combined))
    source_drift = [fid for fid, f in {**old_retired, **old_active}.items()
                    if fid not in combined or f['source'] != combined[fid]['source']]
    record('preserve every existing immutable source object', not source_drift, source_drift)
    def historic_body(row):
        return {key: value for key, value in row.items() if key != 'retirement'}
    retired_drift = [fid for fid, f in old_retired.items()
                     if fid not in retired or historic_body(retired[fid]) != historic_body(f)]
    record('preserve all complete previously retired historical bodies', not retired_drift, retired_drift)
    revised_retirement_navigation = [fid for fid, f in old_retired.items()
                                     if fid in retired and retired[fid]['retirement'] != f['retirement']]
    source_docs = {d['document_id']: d['source'] for d in previous['documents']}
    current_docs = {d['document_id']: d['source'] for d in current['documents']}
    record('preserve exact source document set and identities', source_docs == current_docs)
    def source_sections(value):
        fields = ['document_id', 'path', 'level', 'title', 'anchor', 'line_start', 'line_end', 'heading_sha256']
        return [{k: s[k] for k in fields} for s in value['sections']]
    record('preserve every fixed heading field and order', source_sections(prior_coverage) == source_sections(coverage))
    category_changes = [fid for fid in sorted(set(old_active) & set(active))
                        if old_active[fid]['future_plan']['destination'] != active[fid]['future_plan']['destination']]
    record('preserve retained active destination categories', not category_changes, category_changes)
    unexpected_claims = []
    for f in current['features']:
        if (f['future_plan']['destination'] == '不纳入目标' or
                f['destination_verification']['status'] != '待验证' or
                f['future_plan']['stage'] != '待定' or
                f['implementation']['status'] != '未实现' or
                f['implementation']['acceptance_status'] != '未验收'):
            unexpected_claims.append(f['feature_id'])
    record('preserve pending route, stage, implementation and acceptance boundaries', not unexpected_claims, unexpected_claims)
    lost_gates = [fid for fid in set(old_active) & set(active)
                  if not set(old_active[fid]['upstream']['batches']) <= set(active[fid]['upstream']['batches'])
                  or not set(old_active[fid]['upstream']['required_ids']) <= set(active[fid]['upstream']['required_ids'])]
    record('preserve every original planned batch/required-ID gate', not lost_gates, lost_gates)
    changed_paths = set(subprocess.check_output(['git', 'diff', '--name-only', PREVIOUS], cwd=ROOT, text=True).splitlines())
    changed_paths.update(subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], cwd=ROOT, text=True).splitlines())
    prefix = str(INVENTORY.relative_to(ROOT)) + '/'
    record('confine all changes to independent routing directory',
           all(path.startswith(prefix) for path in changed_paths),
           sorted(path for path in changed_paths if not path.startswith(prefix)))
    result = {
        'schema_version': 'routing-r2-preservation-check.v1',
        'scope': 'AUTHOR_FIXED_BASELINE_CONSERVATION_ONLY; semantic corrections require independent review',
        'previous_candidate': PREVIOUS,
        'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'manifest_sha256': hashlib.sha256(current_bytes).hexdigest(),
        'retained_active_rows': len(set(old_active) & set(active)),
        'new_active_ids': sorted(set(active) - set(old_active)),
        'newly_retired_ids': sorted(set(retired) - set(old_retired)),
        'historical_retired_rows_preserved': len(old_retired),
        'revised_retirement_navigation_ids': sorted(revised_retirement_navigation),
        'checks': checks,
    }
    result['all_passed'] = all(c['passed'] for c in checks)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(not result['all_passed'])


if __name__ == '__main__':
    sys.exit(main())
