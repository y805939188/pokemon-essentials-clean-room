"""Integrate newly qualified clauses atop the prior exact-clause journal."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import subprocess

ROOT=Path(__file__).resolve().parents[3]
P=ROOT/'review/remediation-seventh-20261015-prepare'
B='e646432c644dec04d306842cc5a559a29c718fbc'
PREVIOUS_MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
RECEPTION='be2655f07e2565b12d15a5a9c2d15967fa5c75d7'

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])

def ident(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def main():
    output=P/'integration/wave3/v1'
    assert not (output/'applied-clauses.json').exists(), 'Completed integration cannot be reapplied'
    ledger=json.loads((P/'ledger.json').read_text())
    selected=[next(b for b in ledger['batches'] if b['id']==bid) for bid in ['R7-U07','R7-U10']]
    prior=json.loads((P/'integration/wave2/v1/applied-clauses.json').read_text())
    cumulative={r['path']:r for r in prior['files']}
    prior_admin={r['path']:r for r in prior['root_administrative_reception_adjustments']}
    updates={}
    bindings=[]
    for order,batch in enumerate(selected):
        assert batch['candidate_pass'] and batch['candidate_review_round']=='r2' and not batch.get('actual_integration_done')
        bindings.append({k:batch[k] for k in ['id','required_ids','author_task_id','reviewer_context','candidate_commit','candidate_tree','candidate_freeze_commit','candidate_input_path','candidate_review_commit','candidate_review_tree']})
        frozen=json.loads((ROOT/batch['candidate_input_path']).read_text())
        eligible=json.loads((ROOT/batch['candidate_review_result_reception']).with_name('eligibility.json').read_text())
        assert eligible['root_eligibility']=='PASS_SCOPED_CANDIDATE'
        for row in frozen['candidate_and_author_evidence_file_identities']:
            if row['role']!='candidate_mirror':
                continue
            target=row['formal_target']
            base=git('show',B+':'+target)
            current=git('show',PREVIOUS_MI+':'+target)
            assert (ROOT/target).read_bytes()==current
            candidate=git('show',batch['candidate_commit']+':'+row['path'])
            assert ident(candidate)=={k:row[k] for k in ['bytes','sha256','git_blob']}
            original=base.decode().splitlines(True)
            changed=candidate.decode().splitlines(True)
            if target not in updates:
                old=json.loads(json.dumps(cumulative.get(target,dict(path=target,baseline_identity=ident(base),hunks=[],contributors=[]))))
                for hunk in old['hunks']:
                    hunk['integration_wave_rank']=0
                updates[target]=old
            for kind,i,j,x,y in difflib.SequenceMatcher(None,original,changed,autojunk=False).get_opcodes():
                if kind=='equal':
                    continue
                removed=''.join(original[i:j])
                added=''.join(changed[x:y])
                updates[target]['hunks'].append(dict(batch_id=batch['id'],batch_order=order,integration_wave_rank=1,required_ids=batch['required_ids'],candidate_commit=batch['candidate_commit'],candidate_path=row['path'],kind=kind,base_line_indices_half_open=[i,j],candidate_line_indices_half_open=[x,y],removed_text=removed,added_text=added,removed_identity=ident(removed.encode()),added_identity=ident(added.encode())))
    assembled={}
    joins=[]
    for target,row in updates.items():
        base=git('show',B+':'+target).decode().splitlines(True)
        row['hunks'].sort(key=lambda h:(*h['base_line_indices_half_open'],h['integration_wave_rank'],h['batch_order']))
        result=[]
        cursor=0
        preceding=None
        for hunk in row['hunks']:
            i,j=hunk['base_line_indices_half_open']
            assert cursor<=i, ('Overlapping approved replacement requires manual review',target,hunk)
            assert ''.join(base[i:j])==hunk['removed_text']
            result.extend(base[cursor:i])
            hunk['actual_final_line_indices_half_open']=[len(result),len(result)+len(hunk['added_text'].splitlines(True))]
            result.extend(hunk['added_text'].splitlines(True))
            if preceding and preceding['base_line_indices_half_open']==[i,j] and i==j:
                joins.append(dict(path=target,base_boundary=i,first=preceding['batch_id'],second=hunk['batch_id'],resolution='Preserve earlier approved insertion, then append new approved insertion; neither overwritten'))
            cursor=j
            preceding=hunk
        result.extend(base[cursor:])
        data=''.join(result).encode()
        row.update(contributors=list(dict.fromkeys(h['batch_id'] for h in row['hunks'])),assembled_candidate_clauses_identity=ident(data),previous_actual_identity=ident(git('show',PREVIOUS_MI+':'+target)))
        assembled[target]=data
    # The currently accepted eight formal files are outside the new target set.
    accepted_paths={r['path'] for r in json.loads((P/'integration/U04-U05/v1/integrated-input.json').read_text())['actual_integrated_files']}
    u09=json.loads((P/'candidate-freezes/R7-U09/candidate-input.json').read_text())
    accepted_paths.update(r['formal_target'] for r in u09['candidate_and_author_evidence_file_identities'] if r['role']=='candidate_mirror')
    assert len(accepted_paths)==8 and not accepted_paths.intersection(assembled)
    for path in accepted_paths:
        assert (ROOT/path).read_bytes()==git('show',PREVIOUS_MI+':'+path)
    root_admin=[]
    pointer='review/remediation-seventh-20261015-prepare/integration/wave3/v1/public-reception.json'
    for target in ['audit/source-traceability.md','planning/feature-matrix.md']:
        before=assembled[target]
        addition=f'\n## 第七轮累计整合的当前接收状态\n\n上列第七轮作者候选段保留制作时点的原声明与证据资格。当前状态见[实际接收登记](../{pointer})，作者证据须以该登记的固定候选提交和精确路径读取。本次U07/U10的新context候选r2通过后已按条款整合，等待新的独立实际IR；旧r1辅助任务披露与WAIT完整保留，未豁免或迁移。U03候选r2尚待结果。已应用25/27项、12/13批，独立实际PASS与正式ACCEPTED5/27项、3/13批，CLOSED0；其它已应用条款仍以各自固定MI/FI接受新独立IR。U04/U05/U09已接受的八份正文逐字保持。所有行为向量NOT_EXECUTED，宿主等运行0、有效配置UNVERIFIED、L01–L14、旧56/92及27项/13批分母保持；用户授权仅在全轮所有门完成后最终普通merge main，当前未达门。\n'
        assembled[target]+=addition.encode()
        root_admin.append(dict(path=target,prior_snapshot_annotation=prior_admin[target],before_identity=ident(before),after_identity=ident(assembled[target]),added_text=addition,reason='Replace root current-phase pointer/annotation only; preserve all historical author and approved behavior clauses.'))
    for target,data in assembled.items():
        for hunk in updates[target]['hunks']:
            a,z=hunk['actual_final_line_indices_half_open']
            assert ''.join(data.decode().splitlines(True)[a:z])==hunk['added_text']
        (ROOT/target).write_bytes(data)
        updates[target]['actual_final_identity']=ident(data)
        cumulative[target]=updates[target]
    for path in accepted_paths:
        assert (ROOT/path).read_bytes()==git('show',PREVIOUS_MI+':'+path)
    new_hunks=sum(h['integration_wave_rank']==1 for r in updates.values() for h in r['hunks'])
    save(output/'applied-clauses.json',dict(schema='r7.wave3.cumulative-approved-clause-integration.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),fixed_B=B,previous_actual_MI=PREVIOUS_MI,root_candidate_reception_commit=RECEPTION,new_source_bindings=bindings,prior_source_bindings=prior['source_bindings'],new_required_ids=[i for b in bindings for i in b['required_ids']],new_batches=[b['id'] for b in bindings],new_candidate_hunks=new_hunks,new_target_files=list(updates),files=list(updates.values()),cumulative_files=list(cumulative.values()),same_boundary_insertions=joins,root_administrative_adjustments=root_admin,prior_accepted_paths_preserved_exact=sorted(accepted_paths),previous_56_candidate_hunks_preserved=True,qualification='Baseline-relative approved hunks merged with complete prior journal; no whole shared mirror replacement. Current root phase annotations separately updated, not candidate or actual semantic PASS.',actual_new_PASS=False,ACCEPTED=False,CLOSED=False))
    patch=[]
    for target,data in assembled.items():
        before=git('show',PREVIOUS_MI+':'+target)
        patch.extend(difflib.unified_diff(before.decode().splitlines(True),data.decode().splitlines(True),fromfile='a/'+target,tofile='b/'+target))
    (output/'actual-changes.patch').write_text(''.join(patch))
    save(output/'public-reception.json',dict(schema='r7.wave3.current-public-reception.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),new_source_bindings=bindings,prior_source_bindings=prior['source_bindings'],candidate_PASS_items=25,candidate_PASS_batches=12,actual_applied_items=25,actual_applied_batches=12,actual_independent_PASS_items=5,actual_independent_PASS_batches=3,ACCEPTED_items=5,ACCEPTED_batches=3,CLOSED_items=0,CLOSED_batches=0,denominators=dict(required_items=27,batches=13),prior_formal_acceptance=[dict(commit=RECEPTION,path='review/remediation-seventh-20261015-prepare/acceptance/U04-U05/v1/decision.json'),dict(commit=RECEPTION,path='review/remediation-seventh-20261015-prepare/acceptance/R7-U09/v1/decision.json')],author_evidence_rule='Use exact candidate_commit plus candidates/<batch_id>/evidence/author/; never infer files exist on current branch',new_actual_IR='Two new independent actual reviews pending preparation/parent creation; original wave2 reviews keep their exact MI/FI',old_r1_WAIT='U03/U07/U10 retained unwaived; only new U07/U10 r2 qualify current candidates',remaining_candidate_r2='R7-U03',nonmandatory_adoption='NONE',main_merge='Authorized only after every round gate, not eligible now',limits='NOT_EXECUTED behavior;host/Demo/native/save/replay0;configuration UNVERIFIED;L01-L14 retained'))
    for batch in ledger['batches']:
        if batch['id'] in ['R7-U07','R7-U10']:
            batch.update(actual_integration_done=True,state='ACTUAL_CLAUSES_APPLIED_WAIT_FRESH_INDEPENDENT_R7IR',actual_integration_journal=str((output/'applied-clauses.json').relative_to(ROOT)))
    for issue in ledger['issues']:
        if issue['primary_batch'] in ['R7-U07','R7-U10']:
            issue.update(actual_integration_done=True,state='ACTUAL_CLAUSES_APPLIED_WAIT_FRESH_INDEPENDENT_R7IR')
    ledger.update(actual_integration_done_items=25,actual_integration_done_batches=12,phase='U07_U10_ACTUAL_CLAUSES_APPLIED_WAIT_NEW_FRESH_IR')
    save(P/'ledger.json',ledger)
    print(json.dumps(dict(new_batches=2,new_required_items=4,new_targets=len(assembled),new_candidate_hunks=new_hunks,joins=joins,prior_accepted_files_preserved=8)))

if __name__=='__main__':
    main()
