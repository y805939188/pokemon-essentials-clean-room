"""Audit finite required-correction closure gates; never merge or mutate status."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import subprocess

ROOT=Path(__file__).resolve().parents[3]
P=ROOT/'review/remediation-seventh-20261015-prepare'
B='e646432c644dec04d306842cc5a559a29c718fbc'
MI='94d5eb73f4508b8a8a54319040faa9aea5752059'
FI='6a02773d62e36a295e9701a8d0ba5b5cb6441614'
C='f622356f3beb9e84ea8cff9db07c7fb382565d3f'

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])

def ident(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def main():
    ledger=json.loads((P/'ledger.json').read_text())
    registry=json.loads((P/'delegation/task-registry/current.json').read_text())
    policy=json.loads((P/'governance/current-execution-policy.json').read_text())
    projection=json.loads((P/'closure/preflight/final-static-projection.json').read_text())
    assert policy['main_merge_prohibited_for_this_round'] and not policy['main_merge_authorized']
    assert projection['MI']==MI and projection['all36_actual_targets_reconstructed']
    assert projection['cumulative_exact_candidate_hunks']==85
    assert len(projection['cumulative_recorded_phase_exception'])==1
    assert projection['initial_exact_hunks']==11
    assert ledger['counters']['accepted_items']==27 and ledger['counters']['accepted_batches']==13
    assert ledger['pending_reviewer_results']==0
    assert len(registry['entries'])==len({r['task_id'] for r in registry['entries']})==42
    batches={b['id']:b for b in ledger['batches']}
    issues={r['id']:r for r in ledger['issues']}
    records=[]
    severities=collections.Counter()
    actual_contexts=set()
    required_seen=set()
    for bid,batch in batches.items():
        assert all(batch[k] for k in ['candidate_pass','integrated_pass','accepted','actual_integration_done'])
        contract_path=f'review/remediation-seventh-20261015-prepare/delegation/contracts/{bid}.json'
        fixed_contract=git('show',C+':'+contract_path)
        assert (ROOT/contract_path).read_bytes()==fixed_contract
        contract=json.loads(fixed_contract)
        assert contract['blocking_author_dependencies']==[]
        candidate_review=next(r for r in registry['entries'] if r['role']=='independent_candidate_reviewer' and r.get('result_commit')==batch['candidate_review_commit'])
        actual_review=next(r for r in registry['entries'] if 'integrated' in r['role'] and r.get('result_commit')==batch['actual_integration_review_commit'])
        assert actual_review['root_eligibility']=='PASS_SCOPED_ACTUAL_INTEGRATION'
        assert candidate_review['task_id']!=batch['author_task_id']
        assert actual_review['task_id'] not in {batch['author_task_id'],candidate_review['task_id'],'01a13eb7-10b9-7663-a1ea-fe4792373029','01a13f49-a154-7054-9b04-ce31f924d01c'}
        actual_contexts.add(actual_review['task_id'])
        acceptance_path=P/('acceptance/U04-U05/v1/decision.json' if bid in ['R7-U04','R7-U05'] else f'acceptance/{bid}/v1/decision.json')
        acceptance_bytes=acceptance_path.read_bytes()
        acceptance=json.loads(acceptance_bytes)
        actual_folder=ROOT/actual_review['result_reception']
        actual_per=json.loads((actual_folder.parent/'per-id.json').read_text())
        actual_records={r.get('id',r.get('record_id')):r for r in actual_per['records']}
        for index,original in enumerate(contract['original_full_contracts']):
            rid=original['record_id']
            assert rid not in required_seen and rid in issues
            required_seen.add(rid)
            severities[original['severity']]+=1
            current=issues[rid]
            assert current['candidate_pass'] and current['integrated_pass'] and current['accepted']
            original_groups=original['complete_seven_groups']
            assert len(original_groups)==7
            receipt=next(r for r in acceptance['records'] if r['id']==rid)
            assert receipt['formal_state']=='ACCEPTED'
            assert receipt['candidate_commit']==batch['candidate_commit']
            assert receipt['candidate_review_commit']==batch['candidate_review_commit']
            assert receipt['independent_actual_review_commit']==batch['actual_integration_review_commit']
            assert receipt['independent_actual_reviewer']==actual_review['task_id']
            assert receipt['semantic_receiver']['status'].startswith('RECEIVED')
            shared=receipt.get('shared_receiver',receipt.get('shared_catalog_receiver'))
            assert shared and shared['status'].startswith('RECEIVED')
            dependency=receipt.get('dependency_and_historical_receiver',receipt.get('dependency_receiver',receipt.get('dependencies')))
            assert dependency
            primary=actual_records[rid]
            verdict=primary.get('verdict',primary.get('conclusion',primary.get('decision')))
            assert verdict=='PASS_SCOPED_ACTUAL_INTEGRATION'
            groups6=original_groups['六_依赖接收_精确读写集']
            groups7=original_groups['七_执行与未知']
            group6_bytes=json.dumps(groups6,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
            primary_bytes=json.dumps(primary,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
            record=dict(id=rid,batch_id=bid,severity=original['severity'],scope='Only the original narrowed mandatory static correction and its finite named source/consumer/shared/historical obligations',original_complete_contract=dict(commit=C,path=contract_path,pointer=f'/original_full_contracts/{index}/complete_seven_groups',file_identity=ident(fixed_contract)),required_dependency_contract=dict(pointer=f'/original_full_contracts/{index}/complete_seven_groups/六_依赖接收_精确读写集',canonical_identity=ident(group6_bytes),required_receivers=groups6.get('必要同步与接收者'),write_scope=groups6.get('精确中文写入边界'),read_obligation_qualification=groups6.get('读取义务',{}).get('qualification'),named_author_scheduling_edges=[],scheduling_qualification='Empty original ordering edges are not evidence of absent domain dependencies'),candidate=dict(commit=batch['candidate_commit'],freeze_commit=batch['candidate_freeze_commit'],independent_review_commit=batch['candidate_review_commit'],independent_reviewer=candidate_review['task_id']),actual=dict(commit=batch['actual_integration_review_commit'],reviewer=actual_review['task_id'],MI=receipt['actual_MI'],FI=receipt['actual_FI'],per_id_primary_canonical_identity=ident(primary_bytes),root_reception=actual_review['result_reception']),root_responsibility_receipt=dict(path=str(acceptance_path.relative_to(ROOT)),file_identity=ident(acceptance_bytes),semantic=receipt['semantic_receiver'],shared=shared,dependency_and_history=dependency),finite_required_closure_gates=dict(complete_original_seven_groups=True,qualified_current_candidate_review=True,clause_level_actual_integration=True,fresh_actual_independent_scoped_PASS=True,root_semantic_receiver=True,root_shared_receiver=True,root_finite_direct_transitive_domain_and_named_history_receiver=True,final_cumulative_exact_projection=True,unmet_finite_required_gate=False),retained_open_boundaries=dict(original_group7=groups7,scope='Original runtime, model attestation, wider native/host/global coverage and future policy boundaries remain unverified/open. They are not marked satisfied or closed by closing this narrowed required correction.',old56_92='UNCHANGED',optional_policy='NOT_ADOPTED'),eligible_for_scoped_required_closure=True)
            records.append(record)
    assert len(records)==27 and len(batches)==13 and len(actual_contexts)==12
    assert severities==dict(P2=10,P3=17)
    groups=json.loads((P/'delegation/conflict-groups.json').read_text())['groups']
    shared_receivers=[]
    for group in groups:
        assert set(group['batches_including_conditional'])<=set(batches)
        assert all(batches[b]['accepted'] for b in group['required_batches'])
        shared_receivers.append(dict(group_id=group['id'],path=group['path'],all_including_conditional=group['batches_including_conditional'],required_contributors=group['required_batches'],status='RECEIVED_SCOPED_CURRENT_CONTRIBUTIONS',owner='R7-I',proof='Exact final projection plus the relevant scoped independent actual reviews; conditional non-writes retain their independently reviewed non-trigger reasoning.',latest_cumulative_scope_review='4ea7ea5d0fc4854503a1548994322548da020e3f' if group['id'] in ['CG04','CG05'] else 'de582c1e56f60cc2e8c688646595dd354e89bf97' if group['id'] in ['CG01','CG02','CG03','CG07'] else '12eb77bde80c7ff256254b93704a8eb5bc6263dd'))
    # No old evidence or non-target baseline file was modified/deleted.
    diff=git('diff','--name-status','--no-renames',B,'HEAD').decode().splitlines()
    modifications=[]
    unexpected=[]
    allowed=set(r['path'] for r in projection['cumulative_checks']+projection['initial_checks'])
    for line in diff:
        status,path=line.split('\t',1)
        if status=='M':
            modifications.append(path)
            if path not in allowed:
                unexpected.append(dict(status=status,path=path))
        elif status!='A':
            unexpected.append(dict(status=status,path=path))
        elif not (path.startswith('review/remediation-seventh-20261015-prepare/') or path.startswith('review/global-independent-review/seventh-2026-10-14-e646432-7a91/')):
            unexpected.append(dict(status=status,path=path))
    assert not unexpected,unexpected
    assert len(modifications)==35
    reference_head=subprocess.check_output(['git','-C','/workspace/r7-reference','rev-parse','HEAD']).decode().strip()
    assert reference_head=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
    assert not subprocess.check_output(['git','-C','/workspace/r7-reference','status','--porcelain'])
    main=git('ls-remote','origin','refs/heads/main').decode().strip()
    assert main.startswith(B+'\t')
    decision=dict(schema='r7.final-finite-dependency-history-and-closure-audit.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),audited_HEAD=git('rev-parse','HEAD').decode().strip(),B=B,final_functional_MI=MI,FI=FI,records=records,severities=dict(severities),required_items=27,batches=13,independent_actual_contexts=12,shared_receivers=shared_receivers,scoped_required_unmet_gates=[],all27_eligible_for_scoped_required_closure=True,closure_scope='Narrowed required static specification corrections only; not whole-engine/runtime/global-coverage certification',retained_open_limits=['L01-L14','Effective model/effort/tier/speed UNVERIFIED','All new behavioral vectors NOT_EXECUTED; host/Demo/native media/real save/replay/full independent model0','CC04 registration/device bridge and broader native/SF2 loading/guards/synthesis/audio evidence remain unverified','Future compatibility policies and nonmandatory proposals not adopted'],history=dict(no_deleted_paths=True,no_non_target_baseline_modifications=True,modified_baseline_target_count=35,original_R7_report_tree='a011f74704047f11ee47c9a631914337558cb81b',old56_92='UNCHANGED',prior_WAIT_and_U06_process_noncompliance='RETAINED_UNWAIVED_OR_EXPLICITLY_ADJUDICATED_WITH_NEW_SIGNED_CONTENT_VERDICT'),reference_read_only_HEAD=reference_head,main_remote=main,main_merge_prohibited=True,no_cleanup_or_local_sync=True,CLOSED_granted_by_audit=False,qualification='This audit verifies root receipts and finite gate coverage/projection. The independent reports supply semantic PASS; only a separate explicit root decision can close the scoped required corrections.')
    save(P/'closure/final/dependency-and-history-reception.json',decision)
    print(json.dumps(dict(required=27,batches=13,actual_contexts=12,shared_groups=len(groups),finite_unmet=0,eligible_for_scoped_closure=True,retained_limits='OPEN',main_merge='PROHIBITED',closure_granted_by_audit=False)))

if __name__=='__main__':
    main()
