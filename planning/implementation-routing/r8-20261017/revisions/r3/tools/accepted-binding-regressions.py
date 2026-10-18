#!/usr/bin/env python3
"""Author regressions for accepted actual write-set additions and shared receivers."""
from pathlib import Path
import argparse
import copy
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
INVENTORY = HERE.parents[2]
spec = importlib.util.spec_from_file_location('routing_accepted_checks', INVENTORY / 'routing.py')
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    m = r.read_json(INVENTORY / 'routing-manifest.json')
    c = r.read_json(INVENTORY / 'section-coverage.json')
    registry = r.read_json(INVENTORY / 'accepted-source-updates.json')
    baseline = r.errors(m, c, registry)
    if baseline:
        print(json.dumps({'result': 'INVALID_BASELINE', 'errors': baseline}, ensure_ascii=False))
        return 1
    _, wp, batches = r.fixed_inputs()
    extended = next(d for d in m['documents'] if set(d['upstream']['batches']) - set(r.doc_bindings(d['source']['path'], wp, batches)[2]['batches']))
    shared = next(d for d in m['documents'] if len(d['upstream']['accepted_events']) > 1)
    changed = next(d for d in m['documents'] if d['current_applicability']['identity']['sha256'] != d['source']['sha256'])
    cases = []
    def check(name, mutate, token):
        mm, cc, rr = copy.deepcopy(m), copy.deepcopy(c), copy.deepcopy(registry)
        mutate(mm, rr)
        found = r.errors(mm, cc, rr)
        cases.append({'case': name, 'required_error_contains': token,
                      'rejected': any(token in error for error in found), 'errors': found})
    def edit_doc(mm, did, update):
        doc = next(d for d in mm['documents'] if d['document_id'] == did)
        update(doc['upstream'])
        for f in mm['features']:
            if f['document_id'] == did:
                update(f['upstream'])
    added = sorted(set(extended['upstream']['batches']) - set(r.doc_bindings(extended['source']['path'], wp, batches)[2]['batches']))[0]
    check('drop receipt-authorized actual extension gate',
          lambda mm,rr: edit_doc(mm, extended['document_id'], lambda u: u.update(batches=[b for b in u['batches'] if b != added])),
          'known conservative batch binding mismatch')
    def wrong_receipt_target(mm, rr):
        event = rr['events'][0]
        other = next(d['source']['path'] for d in mm['documents'] if d['source']['path'] not in event['documents'])
        event['documents'].append(other)
    check('claim a document outside fixed receipt record', wrong_receipt_target, 'matching fixed ACCEPTED receipt')
    removed = shared['upstream']['accepted_events'][-1]
    check('treat partial event coverage as fully received',
          lambda mm,rr: edit_doc(mm, shared['document_id'], lambda u: u.update(accepted_events=[eid for eid in u['accepted_events'] if eid != removed])),
          'unaccepted batch must retain calibration gate')
    unrelated = next(e['event_id'] for e in registry['events'] if changed['source']['path'] not in e['documents'])
    check('assign an existing but unrelated event',
          lambda mm,rr: edit_doc(mm, changed['document_id'], lambda u: u.update(accepted_events=[unrelated])),
          'unresolved or unrelated accepted event')
    check('clear changed-source acceptance but mark gate pending',
          lambda mm,rr: edit_doc(mm, changed['document_id'], lambda u: u.update(accepted_events=[], status='待整改后核对')),
          'changed current source requires accepted calibration')
    result = {'schema_version': 'routing-actual-acceptance-regressions.v1',
              'scope': 'AUTHOR_STATIC_RECEIPT_SCOPE_AND_GATE_CHECKS_ONLY; no semantic authenticity or compatibility certification',
              'manifest_sha256': r.digest((INVENTORY / 'routing-manifest.json').read_bytes()),
              'extended_receiver_document': extended['source']['path'],
              'shared_receiver_document': shared['source']['path'],
              'positive_baseline_errors': baseline, 'cases': cases,
              'all_rejected': all(case['rejected'] for case in cases)}
    r.save_json(args.output, result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(not result['all_rejected'])


if __name__ == '__main__':
    sys.exit(main())
