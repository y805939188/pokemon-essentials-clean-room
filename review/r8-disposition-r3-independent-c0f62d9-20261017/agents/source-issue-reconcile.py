#!/usr/bin/env python3
import importlib.util
import json
from pathlib import Path
import sys
sys.dont_write_bytecode=True
s=importlib.util.spec_from_file_location('source_issue_helpers',Path(__file__).with_name('source-audit.py'));a=importlib.util.module_from_spec(s);s.loader.exec_module(a)
issues=a.load(a.PACKAGE,a.PKG+'issue-status.json')['records'];batches=a.load(a.PACKAGE,a.PKG+'batch-receipts.json')['records'];author=a.read(a.INV/'revisions/r3/issue-source-reception.json')['records'];results=[];texts=[];contracts={};reports={}
for i in issues:
    ref=i['original_contract'];key=ref['commit']+':'+ref['path']
    if key not in contracts:contracts[key]=a.load(ref['commit'],ref['path'])
    value=contracts[key]
    for part in ref['pointer'].strip('/').split('/'):value=value[int(part)] if isinstance(value,list) else value[part]
    received=next(x for x in author if x['id']==i['id'])
    projection=received['original_contract_bounded_textual_fields_read']
    def paths_equal(obj,wanted,path=''):
        out=[path] if obj==wanted else []
        if isinstance(obj,dict):
            for k,v in obj.items():out+=paths_equal(v,wanted,path+'/'+k)
        elif isinstance(obj,list):
            for k,v in enumerate(obj):out+=paths_equal(v,wanted,path+'/'+str(k))
        return out
    projection_paths={k:paths_equal(value,v) for k,v in projection.items()}
    ar=i['actual_independent_review'];key=ar['commit']+':'+ar['result_path']
    if key not in reports:reports[key]=a.load(ar['commit'],ar['result_path'])
    report=reports[key];records=report.get('records',report.get('batches',[]));record=next(x for x in records if x.get('id',x.get('required_id'))==i['id'])
    verdict=record.get('actual_integrated_verdict',record.get('actual_verdict'))
    reason=record.get('actual_evidence',record.get('independent_actual_reasoning',record.get('retained_semantics',record.get('r2_method',''))))
    row={'id':i['id'],'classification':i['classification'],'batch':i['owner_batch'],'source_verdict':'PASS','original_contract_pointer':ref,'projection_exact':all(projection_paths.values()),'projection_original_paths':projection_paths,'actual_verdict':verdict,'actual_snapshot':report.get('artifact_snapshot_commit',report.get('actual_snapshot')),'actual_report_identity':a.identity(ar['commit'],ar['result_path']),'ACCEPTED':i['ACCEPTED'],'CLOSED':i['CLOSED'],'behavior_execution':i['behavior_execution'],'bounded_original_contract':projection,'actual_reasoning':reason,'scope':'Fixed existing source acceptance received; no new independent upstream acceptance vote'}
    assert row['projection_exact'] and verdict=='PASS' and i['ACCEPTED'] and not i['CLOSED'],row
    results.append(row);texts.append('\n== '+i['id']+' '+i['owner_batch']+' '+i['classification']+' ==\n'+json.dumps(projection,ensure_ascii=False,indent=2)+'\nACTUAL '+verdict+' '+str(reason)+'\n')
a.save('source-39-issue-reconciliation.json',results);(a.OUT/'source-receipt-readset.txt').write_text(''.join(texts));a.save('source-issue-command-io.json.gz',a.LOG)
print(json.dumps({'all39_fixed_contract_projections_exact':all(x['projection_exact'] for x in results),'actual_final_PASS':len(results),'CLOSED':sum(x['CLOSED'] for x in results),'readset_chars':sum(map(len,texts))},indent=2))
