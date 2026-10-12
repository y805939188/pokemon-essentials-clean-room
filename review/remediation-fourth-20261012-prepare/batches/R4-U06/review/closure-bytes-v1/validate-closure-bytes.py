#!/usr/bin/env python3
"""Limited registration bytes verification. No source/specification re-review."""
import collections
import datetime
import hashlib
import json
import os
import pathlib
import subprocess

HERE=pathlib.Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').is_file())
BASE='review/remediation-fourth-20261012-prepare/'
PACK=BASE+'registration/R4-U06/'
FINAL=BASE+'batches/R4-U06/review/final-v1/'
CLOSE='2eb521fa97ff74fcc12f15e953efcaceb694f179'
TASK='b537aa973b8362d3d6984b7662133edc0d7d4a65'
SIGNED='63911d1a9ad92cc0aca267ece102351cb8d43fe8'
INPUT='1dd05964f59772886de9b808a929c168c73fa184'
PRIOR='7897037ae93af82aa9246a097c4badbd344a15b1'
THREAD='01a13183-411d-7017-93db-a79fe18bf037'

def git(*args):return subprocess.check_output(['git',*args],cwd=REPO)
def read(c,p):return git('show',c+':'+p)
def obj(c,p):return json.loads(read(c,p))
def ident(c,p):
    b=read(c,p)
    return {'path':p,'commit':c,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
            'git_blob':git('rev-parse',c+':'+p).decode().strip()}
def verify(c,expected):
    actual=ident(c,expected['path'])
    for k in ['bytes','sha256','git_blob']:
        if k in expected:assert actual[k]==expected[k],(expected['path'],k)
    return actual
def main():
    assert os.environ.get('CODEX_THREAD_ID')==THREAD
    handoff=obj(TASK,PACK+'closure-byte-review-handoff.json')
    assert git('rev-parse',CLOSE+'^{tree}').decode().strip()=='6e03b056524ea8aa98e4a2c663e1a2415a686614'
    assert git('rev-parse',TASK+'^{tree}').decode().strip()=='53fcc044061ac1e684679336fb82ca801500ac9c'
    assert git('rev-parse',SIGNED+'^{tree}').decode().strip()=='de5d97b2cddd768e482ffa989e7e1fd2c63a37f2'
    actual_delta=git('diff','--name-only',PRIOR,CLOSE).decode().splitlines()
    assert len(actual_delta)==24 and actual_delta==handoff['changed_paths_from_previous_publication']
    delta=[]
    for r in handoff['frozen_changed_file_identities']:
        checked=verify(CLOSE,r)
        assert read(CLOSE,r['path'])==read(TASK,r['path'])
        delta.append(dict(checked,unchanged_in_task_publication=True))
    assert len(delta)==24 and {r['path'] for r in delta}==set(actual_delta)
    imported=[]
    for p in git('ls-tree','-r','--name-only',SIGNED,FINAL).decode().splitlines():
        assert read(SIGNED,p)==read(CLOSE,p)==read(TASK,p),p
        imported.append(dict(ident(CLOSE,p),equal_original_independent_report=True))
    assert len(imported)==19
    formal=obj(INPUT,PACK+'formal-identities.json')['records']
    assert handoff['unchanged_formal131']['records']==formal
    formal_checks=[]
    for r in formal:
        checked=verify(CLOSE,r)
        assert git('rev-parse',INPUT+':'+r['path'])==git('rev-parse',CLOSE+':'+r['path'])==git('rev-parse',TASK+':'+r['path'])
        formal_checks.append(dict(checked,partition=r['partition'],sole_formal_owner=r['sole_formal_owner'],equal_signed_input=True))
    assert len(formal_checks)==131
    assert collections.Counter(r['partition'] for r in formal_checks)=={'GR4_scoped_accepted':28,'B_unchanged':103}
    for c in [INPUT,CLOSE,TASK,SIGNED]:
        assert git('rev-parse',c+':deliverables/final-specification-set').decode().strip()=='d5a462b4c6f8b78c3264a25d6b5495230fa265e2'
    original=obj(SIGNED,FINAL+'findings.json')['findings']
    criteria=obj(SIGNED,FINAL+'criteria-results.json')['records']
    deps=obj(SIGNED,FINAL+'dependencies-handshakes.json')
    closing=obj(CLOSE,PACK+'scoped-closure.json')
    acceptance=obj(CLOSE,PACK+'final-review-acceptance.json')
    ledger=obj(CLOSE,BASE+'registration/status-ledger.json')
    old_ledger=obj(INPUT,BASE+'registration/status-ledger.json')
    assert len(original)==len(closing['records'])==len(ledger['records'])==17
    old_byid={r['id']:r for r in old_ledger['records']}
    current_byid={r['id']:r for r in ledger['records']}
    closed_byid={r['id']:r for r in closing['records']}
    assert len(closed_byid)==17 and set(old_byid)==set(current_byid)==set(closed_byid)=={r['id'] for r in original}
    results=[]
    for i,r in enumerate(original):
        fid=r['id'];cl=closed_byid[fid];current=current_byid[fid]
        cids=[c['criterion_id'] for c in criteria if c['finding_id']==fid]
        assert r['verdict']=='FINAL_PASS_SCOPED' and r['CLOSED'] is False
        assert cl['state']=='CLOSED' and cl['CLOSED'] is True and current['state']=='CLOSED'
        assert cl['state_before']=='ACCEPTED_SCOPED' and cl['closure_kind']=='SCOPED_REQUIRED_FACT_REMEDIATION'
        assert cl['criterion_ids']==cids and cl['criteria_count']==len(cids)==r['criteria_count']
        assert cl['current_final_review']['commit']==SIGNED and cl['current_final_review']['tree']=='de5d97b2cddd768e482ffa989e7e1fd2c63a37f2'
        assert cl['current_final_review']['pointer']=='/findings/'+str(i)
        assert cl['current_final_review']['reviewer_thread_id']==THREAD
        assert cl['final_qualified_chain']==r['qualified_chain']
        assert cl['final_formal_file_identities']==r['exact_final_formal_files']
        assert cl['prior_scoped_acceptance']==old_byid[fid]['acceptance']
        assert cl['prior_actual']==old_byid[fid]['actual']
        assert {k:v for k,v in current.items() if k not in ['state','closure']}=={k:v for k,v in old_byid[fid].items() if k not in ['state','closure']}
        assert current['closure']['status']=='CLOSED_SCOPED' and current['closure']['CLOSED'] is True
        assert current['closure']['finding_id']==fid and current['closure']['final_review_commit']==SIGNED
        assert current['closure']['final_review_tree']=='de5d97b2cddd768e482ffa989e7e1fd2c63a37f2'
        assert current['closure']['reviewer_thread_id']==THREAD and current['closure']['prior_acceptance_retained_as_historical'] is True
        assert cl['new_execution']=='NOT_EXECUTED_THIS_UPDATE'
        results.append({'id':fid,'batch':r['batch'],'criterion_ids':cids,'criteria_count':len(cids),
            'current_state':'CLOSED','closure_kind':cl['closure_kind'],'byte_review_result':'PASS',
            'signed_final_verdict':'FINAL_PASS_SCOPED','signed_final_pointer':cl['current_final_review'],
            'old_acceptance_and_actual_exact_preserved':True,'final_qualified_chain_and_formal_identities_exact_preserved':True,
            'historical_final_report_CLOSED0_unchanged':True})
    assert acceptance['status']=='FINAL_PASS_SCOPED_ACCEPTED_BY_UNIQUE_REGISTRAR'
    assert acceptance['sole_registrar']==closing['sole_writer']==ledger['sole_writer']=='fourth-preparation-registrar'
    assert acceptance['accepted_findings']==[r['id'] for r in original]
    assert acceptance['criteria_accepted_scoped']==closing['criteria_covered']==76
    assert closing['entry_dependencies']==deps['entry_dependencies']
    assert closing['four_final_handshakes']==deps['four_final_handshakes']
    assert ledger['effective_CLOSED_GR4']==17 and ledger['historical_CLOSED_GR3']==23
    assert not acceptance['remaining_required_conflicts'] and not closing['remaining_required_conflicts']
    old_acceptances=[]
    for n in range(1,6):
        p=BASE+f'registration/R4-U0{n}/acceptance.json'
        assert read(INPUT,p)==read(CLOSE,p)==read(TASK,p)
        old_acceptances.append(dict(ident(CLOSE,p),historical_original_bytes_preserved=True))
    assert closing['retained_qualified_history']['GR3_CLOSED']==23
    legacy=obj(INPUT,PACK+'legacy-scoped-regression.json')
    assert closing['retained_qualified_history']['original229']==legacy['original229']
    assert closing['retained_qualified_history']['exact341']==legacy['exact341']
    assert closing['retained_qualified_history']['no_reopened_or_resigned_history'] is True
    assert closing['retained_qualified_history']['341_are_owner_contributions_not_features'] is True
    assert closing['retained_qualified_history']['old_optional_GR3_M09_001_U08']=='DEFERRED_NOT_STARTED'
    assert closing['retained_qualified_history']['GR3_M02_003']=='NO_REQUIRED_REVISION'
    assert closing['old_junction_dispositions']['count']==14
    assert closing['old_junction_dispositions']['original_supported_partial_not_reviewed_material_limits_preserved'] is True
    assert closing['old_junction_dispositions']['new_whole_chain_PASS'] is False
    limits=closing['execution_and_limits']
    assert limits==handoff['execution_boundary']
    assert limits['historical_GR4_EXECUTED_REFERENCE']==4 and limits['new_reference_model_host_Demo_behavior_execution']==0
    assert limits['runtime_criteria_PASS_means']=='Evidence boundary compliance only'
    assert all(closing[k] is False for k in ['main_merge_performed','branch_deletion_performed','Mac_modified'])
    retained=[]
    for name in ['formal-identities.json','legacy-scoped-regression.json','junction-dispositions.json','dependencies-and-shared-proposals.json','execution-and-limits.json','findings-and-criteria.json']:
        p=PACK+name
        assert read(INPUT,p)==read(CLOSE,p)==read(TASK,p)
        retained.append(dict(ident(CLOSE,p),equal_original_frozen_input=True))
    task_delta=git('diff','--name-only',CLOSE,TASK).decode().splitlines()
    assert task_delta==[PACK+'closure-byte-review-handoff.json',PACK+'closure-byte-review-task.md',PACK+'closure-publication-readback.json']
    read_entries=[ident(CLOSE,p) for p in handoff['read_entries']]
    read_entries += [ident(TASK,p) for p in task_delta]
    import_validation=obj(CLOSE,PACK+'final-review-import-validation.json')
    for r in import_validation['file_identities']:verify(CLOSE,r)
    assert import_validation['review_payload_files']==19 and import_validation['review_payload_bytes']==2418088 and not import_validation['errors']
    result={'verdict':'CLOSURE_BYTES_PASS','evidence_level':'TOOL_VALIDATION','review_kind':'REGISTRATION_BYTES_ONLY_NO_SPEC_REVIEW',
        'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer_thread_id':THREAD,
        'reviewer_thread_source':'Single CODEX_THREAD_ID echo; same as independently signed final review',
        'model_request':'sol / ultra / Standard(default) / Fast=false','actual_model_reasoning_tier_fast_echo':'UNVERIFIED','backend_or_quota_audit':False,
        'frozen_closure':handoff['frozen_closure'],'task_publication':{'commit':TASK,'tree':'53fcc044061ac1e684679336fb82ca801500ac9c'},
        'signed_final_review':handoff['already_accepted_independent_final_review'],'formal_input':handoff['final_semantic_input'],
        'counts':handoff['expected_counts'],'delta24':delta,'unchanged_original_final19':imported,
        'formal131':formal_checks,'formal_subtree':'d5a462b4c6f8b78c3264a25d6b5495230fa265e2','findings':results,
        'unchanged_old_five_acceptance_receipts':old_acceptances,'unchanged_qualification_packets':retained,
        'prior_independent_signature_reuse':'Exact byte identity and qualified scope reused. No new source/spec/GR3/229/341 review or execution.',
        'retained_history_declarations':closing['retained_qualified_history'],'retained_junction_declarations':closing['old_junction_dispositions'],
        'execution_and_limits':limits,'read_entries_full_blob_JSON_or_text_consumed':read_entries,
        'successor_only_delta':task_delta,'mandatory_blockers':[],'formal_write_paths':[],'registration_write_paths':[]}
    (HERE/'identity-and-byte-results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'verdict':result['verdict'],'closed':17,'criteria':76,'delta':24,'unchanged_report_files':19,'formal':131,'blockers':[]}))

if __name__=='__main__':main()
