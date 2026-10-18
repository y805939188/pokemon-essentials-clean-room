#!/usr/bin/env python3
"""Apply only the two explicit accepted receipts to routing applicability, not specs."""
from pathlib import Path
import copy
import importlib.util
import json
import re
import sys

sys.dont_write_bytecode = True
HOME = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('routing_accepted_backfill', HOME/'routing.py')
routing = importlib.util.module_from_spec(spec)
spec.loader.exec_module(routing)
RECEIPT_COMMIT = '861f7a44a6f763c265a11761ab17a8ec3b55f304'
RECEIPT_PATH = 'review/remediation-eighth-20261016-prepare/acceptance/U02-U03/receipt.json'
receipt = json.loads(routing.blob(RECEIPT_COMMIT,RECEIPT_PATH))
records = receipt['records']
assert {r['batch'] for r in records} == {'R8-U02','R8-U03'}
assert all(r['ACCEPTED'] and not r['CLOSED'] and r['actual_integrated_PASS'] for r in records)
snapshot = records[0]['actual_artifact_commit']
assert all(r['actual_artifact_commit'] == snapshot for r in records)
manifest = routing.read_json(HOME/'routing-manifest.json')
source_before = {f['feature_id']:copy.deepcopy(f['source']) for f in manifest['features']}
events, by_path = [], {}
for r in records:
    path = r['actual_target_identity']['path']
    actual = routing.identity(snapshot,path)
    expected = r['actual_target_identity']
    assert actual['sha256'] == expected['sha256'] and actual['git_blob'] == expected['blob'] and actual['bytes'] == expected['bytes']
    eid = r['batch']+'-ACCEPTED-861f7a44'
    event = {'event_id':eid,'status':'ACCEPTED','commit':snapshot,'batches':[r['batch']],
        'documents':[path],'required_ids':r['required_ids'],
        'evidence':[{'commit':RECEIPT_COMMIT,'path':RECEIPT_PATH},
            {'commit':r['actual_independent_report_commit'],'path':r['actual_independent_report_path']}],
        'receipt_record_pointer':'/records/'+str(records.index(r)),
        'qualification':'Source-spec batch acceptance only; no routing or implementation acceptance'}
    events.append(event);by_path[path]=event
actual_paths = routing.git('ls-tree','-r','--name-only',snapshot,'--',routing.FORMAL).decode().splitlines()
assert sorted(p for p in actual_paths if p.endswith('.md')) == sorted(d['source']['path'] for d in manifest['documents'])
changed = routing.git('diff','--name-only',routing.B8,snapshot,'--',routing.FORMAL).decode().splitlines()
assert set(changed) == set(by_path), 'Unexpected unaccepted formal change'
manifest['current_snapshot']={'commit':snapshot,'formal_tree':routing.git('rev-parse',snapshot+':'+routing.FORMAL.rstrip('/')).decode().strip(),
    'upstream_calibration':'PARTIAL_ACCEPTED_U02_U03; OTHER_BATCHES_AND_FINAL_ROUTING_REVIEW_PENDING'}
doc_by_id = {}
changed_lines = {}
for d in manifest['documents']:
    path = d['source']['path'];doc_by_id[d['document_id']]=d
    current_identity = routing.identity(snapshot,path)
    source_hs,_ = routing.headings(routing.blob(d['source']['commit'],path))
    current_hs,_ = routing.headings(routing.blob(snapshot,path))
    fields = ['anchor','title','level','line_start','line_end']
    assert [[h[k] for k in fields] for h in source_hs] == [[h[k] for k in fields] for h in current_hs], 'Needs manual locator remap'
    is_changed = path in by_path
    d['current_applicability']={'snapshot_commit':snapshot,'path':path,'identity':current_identity,
        'source_equivalence':'CHANGED_ACCEPTED_SOURCE' if is_changed else 'SAME_BYTES',
        'status':'已按ACCEPTED回执核对' if is_changed else '后继快照同字节；保留原核对资格'}
    if is_changed:
        d['upstream']['accepted_events']=[by_path[path]['event_id']]
        d['upstream']['status']='已回填ACCEPTED源规格；去向待独立复审'
        diff=routing.git('diff','--no-ext-diff','--unified=0',routing.B8,snapshot,'--',path).decode()
        changed_lines[path]=set()
        for start,count in re.findall(r'^@@ -(\d+)(?:,(\d+))? ',diff,re.M):
            changed_lines[path].update(range(int(start),int(start)+int(count or '1')))
directly_changed=[];document_checked=[]
for f in manifest['features']:
    d=doc_by_id[f['document_id']];path=d['source']['path'];current=f['current_applicability']
    current.update(snapshot_commit=snapshot,document=path)
    hs,lines=routing.headings(routing.blob(snapshot,path))
    heading=next(h for h in hs if h['anchor']==f['source']['anchor'])
    ranges=copy.deepcopy(f['functional_scope']['line_ranges'])
    current['locator']={'heading':heading['title'],'anchor':heading['anchor'],'heading_level':heading['level'],
        'heading_sha256':heading['heading_sha256'],'line_ranges':ranges,
        'unit_sha256':routing.digest(''.join(''.join(lines[a-1:b]) for a,b in ranges).encode()),
        'file_sha256':d['current_applicability']['identity']['sha256'],'file_git_blob':d['current_applicability']['identity']['git_blob']}
    if path in by_path:
        event=by_path[path];f['upstream']['accepted_events']=[event['event_id']]
        f['upstream']['status']='已回填ACCEPTED源规格；去向待独立复审'
        current['status']='已按ACCEPTED回执核对'
        current['source_state']='历史来源保持；当前定位与ACCEPTED实际快照单列'
        document_checked.append(f['feature_id'])
        unit_lines={n for a,b in ranges for n in range(a,b+1)}
        if unit_lines.intersection(changed_lines[path]):
            directly_changed.append(f['feature_id'])
            note=('U02当前§5.2移除特定提示承诺；其他输出按各自到达前提保留。' if event['batches']==['R8-U02'] else 'U03当前§3.3明确五果样本；不从构造缺省或个别反例推导记录多数。')
            f['differences'].append(event['event_id']+'：'+note+' 历史source不回写；去向与阶段资格不升级。')
assert all(f['source']==source_before[f['feature_id']] for f in manifest['features'])
routing.save_json(HOME/'routing-manifest.json',manifest)
routing.save_json(HOME/'accepted-source-updates.json',{'schema_version':'routing-accepted-source-updates.v1',
    'events':events,'state':'PARTIAL_ACCEPTED_BACKFILL_PENDING_FINAL_BASELINE',
    'instruction':'Only U02/U03 accepted receipts applied. Remaining batches and final cumulative baseline must arrive from coordinator; routing review pending.'})
routing.save_json(HOME/'revisions/r1/tools/accepted-backfill-result.json',{'receipt':{'commit':RECEIPT_COMMIT,'path':RECEIPT_PATH},
    'current_snapshot':manifest['current_snapshot'],'source_objects_unchanged':True,'formal_document_identities_checked':len(manifest['documents']),
    'accepted_events':[e['event_id'] for e in events],'directly_changed_feature_ids':directly_changed,
    'accepted_document_feature_ids':document_checked,'retired_rows_unchanged':True,
    'scope':'Author applicability backfill only; no routing approval, no implementation/acceptance elevation, no unaccepted batch applied'})
print(json.dumps({'accepted_events':len(events),'document_feature_rows_checked':len(document_checked),'directly_changed_features':directly_changed,'current_snapshot':snapshot},ensure_ascii=False))
