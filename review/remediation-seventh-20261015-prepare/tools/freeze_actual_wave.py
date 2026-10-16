"""Freeze actual cumulative spec bytes and bounded per-batch IR transports."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess

ROOT=Path(__file__).resolve().parents[3]
P=ROOT/'review/remediation-seventh-20261015-prepare'
MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
B='e646432c644dec04d306842cc5a559a29c718fbc'
RECEPTION='71ccd38aeefcc12d01e1362e825bd82f251037f5'
REPO='y805939188/pokemon-essentials-clean-room'

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])

def identity(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def tree(commit,prefix=''):
    result={}
    for entry in git('ls-tree','-r',commit,*([prefix] if prefix else [])).decode().splitlines():
        info,path=entry.split('\t',1)
        mode,kind,blob=info.split()
        result[path]=dict(mode=mode,kind=kind,blob=blob)
    return result

def main():
    output=P/'integration/wave2/v1'
    journal=json.loads((output/'applied-clauses.json').read_text())
    bindings={x['id']:x for x in journal['source_bindings']}
    actual_tree=tree(MI)
    base_tree=tree(B)
    formal_prefix='deliverables/final-specification-set/'
    files=[]
    for path,row in actual_tree.items():
        if not path.startswith(formal_prefix):
            continue
        before=git('show',B+':'+path)
        actual=git('show',MI+':'+path)
        assert row['mode']=='100644' and row['kind']=='blob'
        files.append(dict(path=path,**identity(actual),git_mode=row['mode'],base_B_identity=identity(before),changed_against_B=actual!=before))
    assert len(files)==131 and sum(x['changed_against_B'] for x in files)==26
    assert git('rev-parse',MI+':review/global-independent-review/seventh-2026-10-14-e646432-7a91').decode().strip()=='a011f74704047f11ee47c9a631914337558cb81b'
    old=json.loads((P/'integration/U04-U05/v1/integrated-input.json').read_text())
    for row in old['actual_integrated_files']:
        assert identity(git('show',MI+':'+row['path']))=={k:row[k] for k in ['bytes','sha256','git_blob']}
    actual_paths=[x['path'] for x in journal['files']]
    current_files=[dict(path=path,**identity(git('show',MI+':'+path)),contributors=next(x['contributors'] for x in journal['files'] if x['path']==path)) for path in actual_paths]
    frozen=dict(schema='r7.wave2.frozen-actual-integration-input.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),actual_MI=MI,actual_MI_tree=git('rev-parse',MI+'^{tree}').decode().strip(),actual_formal_subtree=git('rev-parse',MI+':deliverables/final-specification-set').decode().strip(),fixed_B=B,fixed_R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',covered_new_batches=journal['ordered_batches'],covered_new_required_ids=journal['required_ids'],new_actual_target_files=current_files,all_formal_file_identities=files,formal_counts=dict(all=131,changed_against_B=26,unchanged_against_B=105,prior_accepted_files_preserved_exact=5),source_bindings=journal['source_bindings'],shared_integration=dict(candidate_hunks=56,root_administrative_adjustments=journal['root_administrative_reception_adjustments'],same_boundary_insertions=journal['same_boundary_insertions'],rule='All approved baseline-relative spans are disjoint except two same-boundary append pairs, explicitly concatenated U01 then U02. Read full current shared files, not just mirrors or hunk hashes.',root_owner='R7-I sole semantic/shared receiver',formal_acceptance_for_new18='PENDING_FRESH_ACTUAL_REVIEWS_AND_ROOT_DEPENDENCY_RECEPTION'),previous_actual_MI=old['actual_integration_commit'],previous_actual_IR='357f917bb449e1f597678af5515662e6822e91d9',previous_formal_acceptance_commit=RECEPTION,previous_formal_acceptance_path='review/remediation-seventh-20261015-prepare/acceptance/U04-U05/v1/decision.json',excluded_procedural_wait_batches=['R7-U03','R7-U07','R7-U10'],nonmandatory_adoption='NONE',denominators=dict(required_items=27,batches=13),state=dict(candidate_PASS_items=21,actual_independent_PASS_items=3,ACCEPTED_items=3,CLOSED_items=0),execution='All behavior NOT_EXECUTED; reference/independent full model/host/Demo/native/save/replay0, configuration UNVERIFIED, L01-L14 retained',self_binding='This file and eight IR plans are pinned by successor FI commit/tree in exact dispatch; no self-referential hash guessed.')
    save(output/'integrated-input.json',frozen)
    plans=[]
    review_tasks={x['batch_id']:x for x in json.loads((P/'intake/20261015-review-wave/parent-receipt.json').read_text())['entries']}
    for bid,binding in bindings.items():
        artifacts={}
        def add(commit,path,local):
            data=git('show',commit+':'+path)
            row=dict(repository=REPO,commit=commit,path=path,local_path=local,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob_content_id=identity(data)['git_blob'])
            if local in artifacts:
                assert artifacts[local]==row
            artifacts[local]=row
        own_freeze=json.loads((ROOT/binding['candidate_input_path']).read_text())
        candidate_plan_path=str(Path(binding['candidate_input_path']).with_name('candidate-restore')/f'{bid}.json')
        own_plan=json.loads(git('show',binding['candidate_freeze_commit']+':'+candidate_plan_path))
        for row in own_plan['artifacts']:
            artifacts[row['local_path']]=row
        add(binding['candidate_freeze_commit'],binding['candidate_input_path'],'freeze/candidate-input.json')
        add(binding['candidate_freeze_commit'],str(Path(binding['candidate_input_path']).with_name('mirror-diffs.patch')),'freeze/mirror-diffs.patch')
        task=review_tasks[bid]
        reception=json.loads((P/'review-receptions'/task['label']/'reception.json').read_text())
        for row in reception['files']:
            add(task['result_commit'],row['path'],'candidate-review/'+row['path'])
        for name in ['reception.json','eligibility.json']:
            path='review/remediation-seventh-20261015-prepare/review-receptions/'+task['label']+'/'+name
            add(RECEPTION,path,'root-reception/'+name)
        for path in ['applied-clauses.json','actual-changes.patch','public-reception.json']:
            add(MI,'review/remediation-seventh-20261015-prepare/integration/wave2/v1/'+path,'integration/'+path)
        add(RECEPTION,'review/remediation-seventh-20261015-prepare/acceptance/U04-U05/v1/decision.json','prior-accepted/decision.json')
        for name in ['report.md','per-id.json','review-input-receipt.json']:
            add('357f917bb449e1f597678af5515662e6822e91d9','review/remediation-seventh-20261015-prepare/integrated-reviews/U04-U05/r1/'+name,'prior-accepted/independent-ir/'+name)
        own_targets={row['formal_target'] for row in own_freeze['candidate_and_author_evidence_file_identities'] if row['role']=='candidate_mirror'}
        contract=json.loads((P/'delegation/contracts'/f'{bid}.json').read_text())
        read_targets=set(own_targets)
        for row in contract['paths']:
            path=row['candidate_path'].removeprefix('candidates/'+bid+'/')
            if path in actual_tree:
                read_targets.add(path)
        original_plan=json.loads(git('show','658488c81f1f3181a488298ab27850c8af951d73:review/remediation-seventh-20261015-prepare/recovery/batches/'+bid+'.json'))
        for row in original_plan['fixed_read_inputs']:
            if row['repository']==REPO and row['path'] in actual_tree:
                read_targets.add(row['path'])
        for row in old['actual_integrated_files']:
            read_targets.add(row['path'])
            add(old['actual_integration_commit'],row['path'],'prior-accepted/actual-at-accepted-MI/'+row['path'])
        for path in sorted(read_targets):
            add(MI,path,'actual/'+path)
            if path in base_tree:
                add(B,path,'baseline/'+path)
        shared=[]
        for target in sorted(own_targets):
            contributors=next((x['contributors'] for x in journal['files'] if x['path']==target),[])
            for other in contributors:
                if other==bid:
                    continue
                other_binding=bindings[other]
                add(other_binding['candidate_commit'],'candidates/'+other+'/'+target,'shared-candidate/'+other+'/'+target)
                other_task=review_tasks[other]
                for name in ['report.md','per-id.json','review-input-receipt.json']:
                    add(other_task['result_commit'],other_task['prefix']+name,'shared-candidate-review/'+other+'/'+name)
                add(RECEPTION,'review/remediation-seventh-20261015-prepare/review-receptions/'+other_task['label']+'/eligibility.json','shared-root-reception/'+other+'/eligibility.json')
                shared.append(dict(path=target,other_batch=other,candidate_commit=other_binding['candidate_commit'],candidate_review_commit=other_task['result_commit']))
        plan=dict(schema='r7.wave2.bounded-actual-IR-transport.v1',batch_id=bid,required_ids=binding['required_ids'],contract_commit='f622356f3beb9e84ea8cff9db07c7fb382565d3f',evidence_publication_commit=MI,unresolved_reference_fields=[],artifacts=list(artifacts.values()),evidence=[],fixed_read_inputs=[],future_paths_not_downloaded=[],qualification='Immutable own complete candidate/current and necessary old-version history, own full independent candidate result, actual full target/consumer/shared-file bytes, B baselines, all prior five accepted actual files, scoped other shared candidates/review receipts and exact clause journal. Original source/counterproof recovery separately required; no program execution or semantic PASS.',shared_preservation_checks=shared)
        save(output/'integrated-restore'/f'{bid}.json',plan)
        plans.append(dict(batch_id=bid,required_ids=binding['required_ids'],plan_path='review/remediation-seventh-20261015-prepare/integration/wave2/v1/integrated-restore/'+bid+'.json',files=len(artifacts),bytes=sum(x['bytes'] for x in artifacts.values()),actual_read_targets=sorted(read_targets),shared_checks=shared))
    save(output/'transport-index.json',dict(schema='r7.wave2.actual-IR-plan-index.v1',MI=MI,plans=plans,created_tasks=0,all_behavior='NOT_EXECUTED'))
    print(json.dumps(dict(MI=MI,formal_subtree=frozen['actual_formal_subtree'],formal_counts=frozen['formal_counts'],plans=[{k:x[k] for k in ['batch_id','files','bytes']} for x in plans])))

if __name__=='__main__':
    main()
