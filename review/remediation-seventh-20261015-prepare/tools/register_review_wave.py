"""Record root reception decisions and fresh-review requests; no AI tasks."""
from pathlib import Path
import datetime
import importlib.util
import json
import subprocess
import sys
sys.dont_write_bytecode = True
P = Path(__file__).resolve().parents[1]
ROOT = P.parents[1]
NOW = datetime.datetime.now(datetime.timezone.utc).isoformat()
spec = importlib.util.spec_from_file_location('bounded_receiver', P/'tools/receive_author_wave.py')
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

def relative(path):
    return str(path.relative_to(ROOT))

def main():
    ledger = json.loads((P/'ledger.json').read_text())
    batches = {x['id']:x for x in ledger['batches']}
    registry = json.loads((P/'delegation/task-registry/current.json').read_text())
    tasks = json.loads((P/'intake/20261015-review-wave/parent-receipt.json').read_text())['entries']
    summary = []
    for task in tasks:
        folder = P/'review-receptions'/task['label']
        receipt = json.loads((folder/'reception.json').read_text())
        per = json.loads((folder/'per-id.json').read_text())
        inp = json.loads((folder/'review-input-receipt.json').read_text())
        manifest = json.loads((folder/'artifact-manifest.json').read_text())
        known = {x['path']:x for x in receipt['files']}
        if task['batch_id'] == 'R7-U02':
            for row in manifest['files']:
                row['path'] = task['prefix']+row['path']
        matched = set()
        for path, records in M.manifest_records(manifest, known).items():
            for record in records:
                identity = M.candidate_identity(record)
                if identity:
                    assert identity == {k:known[path][k] for k in ['bytes','sha256','git_blob']}, path
                    matched.add(path)
        assert set(known)-matched == {task['prefix']+'artifact-manifest.json'}
        encoded = json.dumps(per,ensure_ascii=False)+json.dumps(inp,ensure_ascii=False)+(folder/'report.md').read_text()
        assert task['reviewer_task_id'] in encoded
        records = []
        for row in per['records']:
            rid = row.get('id',row.get('record_id'))
            assert rid
            verdict = next((row[k] for k in ['verdict','conclusion','decision','result','content_verdict'] if k in row),None)
            records.append(dict(id=rid,reported_content_verdict=row.get('candidate_content_assessment',verdict),reported_record_verdict=verdict))
        if not task['batch_id'].startswith('IR'):
            batch = batches[task['batch_id']]
            for field in ['candidate_commit','candidate_tree','candidate_freeze_commit','author_task_id']:
                assert batch[field] in encoded, (task['label'],field)
            assert {r['id'] for r in records} == set(batch['required_ids'])
            qualified = task['batch_id'] not in ['R7-U03','R7-U07','R7-U10']
            eligible = qualified and all(r['reported_record_verdict']=='PASS_SCOPED_CANDIDATE' for r in records)
            assert qualified == eligible
            state = 'PASS_SCOPED_CANDIDATE' if eligible else 'WAIT_INPUT_OR_INDEPENDENCE'
            batch.update(candidate_pass=eligible,reviewer_context=task['reviewer_task_id'],candidate_review_commit=task['result_commit'],candidate_review_tree=task['result_tree'],candidate_review_round=task['round'],state='CANDIDATE_PASS_PENDING_ACTUAL_INTEGRATION' if eligible else state,candidate_review_result_reception=relative(folder/'reception.json'))
            batch['candidate_review_verdicts'] = {r['id']:state for r in records}
            batch['reported_content_verdicts'] = {r['id']:r['reported_content_verdict'] for r in records}
            for issue in ledger['issues']:
                if issue['primary_batch'] == task['batch_id']:
                    issue.update(candidate_pass=eligible,state=batch['state'],candidate_review_commit=task['result_commit'])
                    if relative(folder/'eligibility.json') not in issue['evidence']:
                        issue['evidence'].append(relative(folder/'eligibility.json'))
            deviation = ('One prohibited AI helper created before contract reading; stopped and not used for candidate content. Root does not waive; fresh independent r2 required.' if not qualified else
                         'U01r2 discloses early gh auth status before full contract; no credential values/model proof claimed; no AI child or independence delegation. Preserve operational deviation, no claim of perfect process compliance.' if task['batch_id']=='R7-U01' else
                         'No prohibited AI child or independence blocker found in received identity, report and per-ID disclosures; retain log and configuration qualifications.')
        else:
            assert per['MI']=='b0eea808887a688d52d28390ac8886fed9c10bcf' and per['FI']=='d9021aa2d704476f644ef15f1a3b8291653ff8f1'
            assert per['reviewer']['subtasks_created']==0 and per['reviewer']['different_from_excluded_contexts']
            for key in ['MI','FI']:
                assert subprocess.check_output(['git','-C',str(ROOT),'rev-parse',per[key]+'^{tree}']).decode().strip()==per[key+'_tree']
            def visit(value):
                if isinstance(value,dict):
                    if all(k in value for k in ['commit','path','file_identity','byte_offsets_half_open','span_identity']):
                        data=M.git('show',value['commit']+':'+value['path'])
                        a,z=value['byte_offsets_half_open']
                        assert M.ident(data)==value['file_identity'] and M.ident(data[a:z])==value['span_identity']
                    for child in value.values():
                        visit(child)
                elif isinstance(value,list):
                    for child in value:
                        visit(child)
            visit(per)
            assert all(r['reported_record_verdict']=='PASS_SCOPED_ACTUAL_INTEGRATION' for r in records)
            eligible=True
            state='PASS_SCOPED_ACTUAL_INTEGRATION'
            deviation='Zero child tasks; new actual context differs from both authors/candidate reviewers. U04 unexposed internal opaque ID qualification retained.'
        entry=next(x for x in registry['entries'] if x['task_id']==task['reviewer_task_id'])
        entry.update(status='COMPLETED_ACTUAL_REVIEW_RECEIVED',result_commit=task['result_commit'],result_tree=task['result_tree'],actual_execution='IMMUTABLE_ARTIFACTS_RECEIVED_NOT_BEHAVIOR_EXECUTION',root_eligibility=state,result_reception=relative(folder/'reception.json'))
        save(folder/'eligibility.json',dict(schema='r7.root-review-eligibility.v1',utc=NOW,task=task,records=records,root_eligibility=state,eligible_for_next_gate=eligible,manifest_nonself_identities_matched=len(matched),manifest_self_binding='Exact immutable result commit/tree plus exhaustive root HTTP/Git table',identity_binding='Actual reported runtime ID matches parent-created task mapping; required immutable candidate/freezes and authors cross-checked in report/per-ID/input',process_qualification=deviation,effective_configuration='UNVERIFIED',behavior_vectors='NOT_EXECUTED',host_Demo_native_media_real_save_replay=0,L01_L14='RETAINED',no_ACCEPTED_or_CLOSED_from_candidate_PASS=True))
        summary.append(dict(batch_id=task['batch_id'],round=task['round'],result_commit=task['result_commit'],eligibility=state,records=records))
    ir=next(t for t in tasks if t['batch_id'].startswith('IR'))
    irper=json.loads((P/'review-receptions'/ir['label']/'per-id.json').read_text())
    frozen=json.loads((P/'integration/U04-U05/v1/integrated-input.json').read_text())
    for row in frozen['actual_integrated_files']:
        assert M.ident((ROOT/row['path']).read_bytes())=={k:row[k] for k in ['bytes','sha256','git_blob']}
    accepted=[]
    for row in irper['records']:
        bid=row['batch']
        batch=batches[bid]
        assert batch['candidate_pass']
        assert row['dependencies']['named_direct_record_edges']==[] and row['dependencies']['named_transitive_record_edges']==[]
        contract=json.loads((P/'delegation/contracts'/f'{bid}.json').read_text())
        assert contract['blocking_author_dependencies']==[]
        dependencies=dict(row['dependencies'])
        dependencies.update(formal_reception='SATISFIED_ROOT_EXACT_BYTE_RECEPTION_AND_RESPONSIBILITY_REGISTRATION',closure='OPEN_SEPARATE_ROOT_CLOSURE_DECISION_NOT_YET_RECORDED',global_dependencies='NOT_ASSERTED_SATISFIED')
        accepted.append(dict(id=row['id'],batch_id=bid,formal_state='ACCEPTED',candidate_commit=batch['candidate_commit'],candidate_review_commit=batch['candidate_review_commit'],actual_MI=irper['MI'],actual_FI=irper['FI'],independent_actual_review_commit=ir['result_commit'],independent_actual_reviewer=ir['reviewer_task_id'],scope='Exact narrowed mandatory static behavioral specification at frozen MI; no runtime equivalence or broader/global acceptance',semantic_receiver=dict(owner='R7-I sole integrator',status='RECEIVED',responsibility='Accept exact changed clauses and finite source/consumer correctness after independent actual-byte review',checks=row['independent_content_checks']),shared_catalog_receiver=dict(owner='R7-I sole integrator',status='RECEIVED',catalogs=[x['path'] for x in frozen['actual_integrated_files'] if x['source_batch']==bid and '/test-catalog/' in x['path']],qualification='No CG group for these two batches; shared intra-batch catalog contributions and unchanged older rows explicitly received without wholesale replacement'),dependencies=dependencies,historical_receiver=dict(owner='R7-I',status='RECEIVED_SCOPED_STATIC',basis=row['independent_content_checks'],qualification='Only named finite regressions; old global56/92 status and wider domains not re-signed'),CLOSED=False,remaining=['Separate explicit closure decision after checking dependency receipt and preservation at the next cumulative integration checkpoint. This is an unmade root decision, not an invented dependency on an unrelated batch or host run.'],execution='All behavior NOT_EXECUTED, host/Demo/native/save/replay0; L01-L14 and effective configuration UNVERIFIED retained'))
        batch.update(integrated_pass=True,accepted=True,closed=False,state='ACCEPTED_PENDING_SEPARATE_CLOSURE_DECISION',actual_integration_reviewer_task_id=ir['reviewer_task_id'],actual_integration_review_commit=ir['result_commit'])
        for issue in ledger['issues']:
            if issue['id']==row['id']:
                issue.update(integrated_pass=True,accepted=True,closed=False,state='ACCEPTED_PENDING_SEPARATE_CLOSURE_DECISION',actual_integration_review_commit=ir['result_commit'])
                evidence=relative(P/'acceptance/U04-U05/v1/decision.json')
                if evidence not in issue['evidence']:
                    issue['evidence'].append(evidence)
    save(P/'acceptance/U04-U05/v1/decision.json',dict(schema='r7.root-formal-acceptance.v1',utc=NOW,authorizer='User explicitly authorizes formal acceptance after actual independent re-review',records=accepted,counts=dict(accepted_items=3,accepted_batches=2,closed_items=0),no_main_merge=True))
    ready=[]
    for bid in ['R7-U03','R7-U07','R7-U10']:
        batch=batches[bid]
        old=next(t for t in tasks if t['batch_id']==bid)
        folder=P/'review-rechecks'/bid/'r2'
        folder.mkdir(parents=True,exist_ok=True)
        text=(P/'candidate-freezes'/bid/'reviewer-dispatch.md').read_text().replace('r1','r2')
        intro=f'''从现在起，包括读取任何合同、侦察仓库或检查连接之前，禁止创建任何辅助 AI 子任务、子会话、agent 或模型调用；仅父会话可创建本次唯一审者，普通 shell/rg/HTTP 工具允许。

# {bid} r2：新 context 完整独立重审，同一作者候选不重写

本次是 R7-I 明确要求的新审者。与作者 **{batch['author_task_id']}**、原r1审者 **{old['reviewer_task_id']}**、父会话及R7-I实际context均不同，记录实际可见thread/context；无真实独立身份则WAIT，不自行另建任务。请求GPT6.1 sol ultra/default普通速度，禁Fast；有效回参仍UNVERIFIED。

旧r1成果固定 **{old['result_commit']}** / tree **{old['result_tree']}**，精确路径 `{old['prefix']}report.md`、`per-id.json`、`review-input-receipt.json`、`artifact-manifest.json`。可从固定raw URL定向读取。旧报告内容PASS与“合同前创建一次只读AI辅助”披露全部保留；R7-I最终资格为WAIT_INPUT_OR_INDEPENDENCE，未豁免，也不把流程问题归为作者语义错误。旧PASS不能代替本次完整内容审查，不沿用其语义判断。

唯一新成果分支 `codex/{bid.lower()}-reviewer-20261015-r2`，唯一写集 `candidates/{bid}/evidence/reviewer/r2/`，从固定B创建；不覆盖旧r1、不改候选/正文/公共台账，不force。作者候选、冻结aa369555和原七组合同均保持原版本。以下完整合同仅将审者轮次/输出路径改为r2，其余最小范围、反证、保留、消费者/回归门完整适用。没有新的作者任务。

'''
        (folder/'reviewer-dispatch.md').write_text(intro+text)
        ready.append(dict(batch_id=bid,round='r2',prompt_path=relative(folder/'reviewer-dispatch.md'),required_ids=batch['required_ids'],candidate_commit=batch['candidate_commit'],candidate_freeze_commit=batch['candidate_freeze_commit'],previous_review_commit=old['result_commit'],excluded_author=batch['author_task_id'],excluded_r1_reviewer=old['reviewer_task_id'],requested_model='gpt-6.1-sol',requested_effort='ultra',service_tier='default',speed='normal; Fast forbidden',task_id=None,creation='PARENT_ONLY_NOT_CREATED_HERE',unique_output_branch=f'codex/{bid.lower()}-reviewer-20261015-r2'))
        batch['fresh_r2_review_ready']=ready[-1]
    save(P/'review-rechecks/ready.json',dict(schema='r7.fresh-independent-rechecks-ready.v1',entries=ready,created_here=0,qualification='All three are same-candidate fresh-context full reviews, not author repair; immutable publication commit supplied outside this self-referential file.'))
    for scope,rows in [('items',ledger['issues']),('batches',ledger['batches'])]:
        for key in ['candidate_pass','integrated_pass','accepted','closed']:
            ledger['counters'][key+'_'+scope]=sum(bool(x[key]) for x in rows)
    ledger.update(utc=NOW,phase='ALL_REVIEWS_RECEIVED_THREE_PROCEDURAL_WAITS_FIRST_THREE_FORMALLY_ACCEPTED',candidate_reviewers_ready=3,reviewer_results_received=15,candidate_reviewer_results_received=14,execution_confirmed_reviewer_tasks=15,pending_reviewer_results=0,candidate_reviewers_awaiting_results=0,active_reviewer_tasks=0,candidate_reviewers_with_frozen_inputs=14,runtime_counts_qualification='13 author/14 candidate-review/1 actual-IR result bundles received, not model configuration or behavior execution. Three fresh r2 candidate reviews requested but not created here.')
    registry['counts'].update(candidate_reviewer_results_received=14,candidate_reviewer_results_pending=0,actual_integrated_reviewer_results_received=1,new_candidate_reviewers_ready_not_created=3)
    registry['requests_not_created']=ready
    registry['utc']=NOW
    save(P/'ledger.json',ledger)
    save(P/'delegation/task-registry/current.json',registry)
    save(P/'intake/20261015-review-wave/eligibility-summary.json',dict(schema='r7.root-review-wave-eligibility.v1',utc=NOW,entries=summary,counters=ledger['counters'],reviewer_tasks_created_here=0))
    print(ledger['counters'])
    print('Ready:',[r['batch_id'] for r in ready])

if __name__=='__main__':
    main()
