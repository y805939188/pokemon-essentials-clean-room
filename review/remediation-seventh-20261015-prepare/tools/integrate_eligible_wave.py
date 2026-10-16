"""Assemble exact approved baseline-relative clauses, never replace a shared mirror."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import subprocess

ROOT=Path(__file__).resolve().parents[3]
P=ROOT/'review/remediation-seventh-20261015-prepare'
B='e646432c644dec04d306842cc5a559a29c718fbc'
PREVIOUS_MI='b0eea808887a688d52d28390ac8886fed9c10bcf'

def identity(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])

def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def main():
    ledger=json.loads((P/'ledger.json').read_text())
    selected=[b for b in ledger['batches'] if b['candidate_pass'] and not b['accepted']]
    assert [b['id'] for b in selected]==['R7-U01','R7-U02','R7-U06','R7-U08','R7-U09','R7-U11','R7-U12','R7-U13']
    output=P/'integration/wave2/v1'
    assert not (output/'applied-clauses.json').exists(), 'Do not apply a completed integration again'
    originals={}
    hunks={}
    selected_bindings=[]
    for batch_order,batch in enumerate(selected):
        frozen=json.loads((ROOT/batch['candidate_input_path']).read_text())
        eligibility=json.loads((ROOT/batch['candidate_review_result_reception']).with_name('eligibility.json').read_text())
        assert eligibility['eligible_for_next_gate'] and eligibility['root_eligibility']=='PASS_SCOPED_CANDIDATE'
        selected_bindings.append({k:batch[k] for k in ['id','required_ids','author_task_id','reviewer_context','candidate_commit','candidate_tree','candidate_freeze_commit','candidate_input_path','candidate_review_commit','candidate_review_tree']})
        for row in frozen['candidate_and_author_evidence_file_identities']:
            if row['role']!='candidate_mirror':
                continue
            target=row['formal_target']
            baseline=subprocess.run(['git','-C',str(ROOT),'show',B+':'+target],capture_output=True)
            before=baseline.stdout
            if baseline.returncode:
                assert target=='review/remediation-seventh-20261015-prepare/current-navigation-errata.json'
                assert not (ROOT/target).exists()
            else:
                assert (ROOT/target).read_bytes()==before, 'Target modified since B; require explicit prior-clause integration: '+target
            candidate=git('show',batch['candidate_commit']+':'+row['path'])
            assert identity(candidate)=={k:row[k] for k in ['bytes','sha256','git_blob']}
            originals[target]=before
            base_lines=before.decode().splitlines(True)
            candidate_lines=candidate.decode().splitlines(True)
            for kind,i,j,x,y in difflib.SequenceMatcher(None,base_lines,candidate_lines,autojunk=False).get_opcodes():
                if kind=='equal':
                    continue
                removed=''.join(base_lines[i:j]).encode()
                added=''.join(candidate_lines[x:y]).encode()
                hunks.setdefault(target,[]).append(dict(batch_id=batch['id'],batch_order=batch_order,required_ids=batch['required_ids'],candidate_commit=batch['candidate_commit'],candidate_path=row['path'],kind=kind,base_line_indices_half_open=[i,j],candidate_line_indices_half_open=[x,y],removed_identity=identity(removed),added_identity=identity(added),removed_text=removed.decode(),added_text=added.decode()))
    # Preflight all baseline spans before any formal write. Same-boundary insertions
    # concatenate in explicit batch order. Overlapping replacements are rejected.
    assembled={}
    joins=[]
    journal=[]
    for target,rows in sorted(hunks.items()):
        rows.sort(key=lambda h:(*h['base_line_indices_half_open'],h['batch_order']))
        base_lines=originals[target].decode().splitlines(True)
        result=[]
        cursor=0
        prior=None
        for row in rows:
            i,j=row['base_line_indices_half_open']
            assert cursor<=i, ('Overlapping approved clauses require manual resolution',target,row)
            result.extend(base_lines[cursor:i])
            row['actual_final_line_indices_half_open']=[len(result),len(result)+len(row['added_text'].splitlines(True))]
            result.extend(row['added_text'].splitlines(True))
            if prior and prior['base_line_indices_half_open']==[i,j] and i==j:
                joins.append(dict(path=target,base_boundary=i,first=prior['batch_id'],second=row['batch_id'],resolution='Concatenate the two independently approved insertions in this explicit order; no bytes removed or overwritten'))
            cursor=j
            prior=row
        result.extend(base_lines[cursor:])
        data=''.join(result).encode()
        assembled[target]=data
        journal.append(dict(path=target,baseline_identity=identity(originals[target]),assembled_candidate_clauses_identity=identity(data),contributors=list(dict.fromkeys(r['batch_id'] for r in rows)),hunks=rows))
    previous=json.loads((P/'integration/U04-U05/v1/integrated-input.json').read_text())
    for row in previous['actual_integrated_files']:
        assert row['path'] not in assembled
        assert identity((ROOT/row['path']).read_bytes())=={k:row[k] for k in ['bytes','sha256','git_blob']}
    # Current reception metadata is distinct from historical author-stage labels.
    reception_path='review/remediation-seventh-20261015-prepare/integration/wave2/v1/public-reception.json'
    admin=[]
    for target in ['audit/source-traceability.md','planning/feature-matrix.md']:
        link='../'+reception_path
        addition=f'\n## 第七轮累计整合的当前接收状态\n\n上列第七轮作者候选段保留各自制作时点的候选状态和原证据资格。当前独立候选审查、逐条整合及后续正式接受状态以[本轮实际接收登记]({link})为准；作者证据通过该登记的固定候选提交与精确路径读取。U01、U02、U06、U08、U09、U11、U12、U13 本次已逐条整合，等待新 context 审查实际累计字节，尚未正式接受或关闭。U04/U05 的三项已有独立实际整合 PASS 和 R7-I 正式接受，关闭仍单独登记。U03/U07/U10 保留流程资格 WAIT，未合入。所有行为向量仍 NOT_EXECUTED，宿主等运行0、有效配置 UNVERIFIED、L01–L14、旧56/92及27项/13批分母保持。\n'
        before=assembled[target]
        assembled[target]+=addition.encode()
        admin.append(dict(path=target,before_identity=identity(before),after_identity=identity(assembled[target]),reason='Current reception pointer and time-qualified preservation of author-stage labels; no new behavior or optional/policy scope',added_text=addition))
    target='review/remediation-seventh-20261015-prepare/current-navigation-errata.json'
    before=assembled[target]
    errata=json.loads(before)
    errata['status']='INTEGRATED_PENDING_INDEPENDENT_ACTUAL_REVIEW'
    errata['reception']['candidate_review']='PASS_SCOPED_CANDIDATE at 28335c5d8400b6b64e53ad56ee55c572f5a3cc07; root received exact bytes'
    errata['reception']['shared_integration']='R7-I clause-level CG01/CG07 integration applied; actual independent review pending'
    assembled[target]=(json.dumps(errata,ensure_ascii=False,indent=2)+'\n').encode()
    admin.append(dict(path=target,before_identity=identity(before),after_identity=identity(assembled[target]),reason='Administrative reception phase only; old R6 frozen payload, current label and behavior unchanged'))
    for target,data in assembled.items():
        (ROOT/target).parent.mkdir(parents=True,exist_ok=True)
        (ROOT/target).write_bytes(data)
    for row in previous['actual_integrated_files']:
        assert identity((ROOT/row['path']).read_bytes())=={k:row[k] for k in ['bytes','sha256','git_blob']}
    save(output/'applied-clauses.json',dict(schema='r7.wave2.exact-baseline-clause-integration.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),fixed_B=B,previous_actual_MI=PREVIOUS_MI,source_bindings=selected_bindings,ordered_batches=[b['id'] for b in selected],required_ids=[rid for b in selected for rid in b['required_ids']],candidate_clause_hunks=sum(len(r['hunks']) for r in journal),unique_candidate_targets=len(assembled),files=journal,same_boundary_insertions=joins,root_administrative_reception_adjustments=admin,prior_accepted_five_files_preserved_exact=True,integrated_actual_PASS=False,ACCEPTED=False,CLOSED=False,qualification='Exact approved baseline-relative hunks assembled after complete overlap preflight. Root current-reception phase annotations recorded separately. No whole shared mirror replacement, semantic self-review or runtime credit.'))
    patch=[]
    for target,data in assembled.items():
        patch.extend(difflib.unified_diff(originals[target].decode().splitlines(True),data.decode().splitlines(True),fromfile='a/'+target,tofile='b/'+target))
    (output/'actual-changes.patch').write_text(''.join(patch))
    save(output/'public-reception.json',dict(schema='r7.wave2.current-public-reception.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),fixed_B=B,source_bindings=selected_bindings,candidate_PASS_items=21,candidate_PASS_batches=10,actual_integration_applied_items=21,actual_integration_applied_batches=10,actual_independent_PASS_items=3,actual_independent_PASS_batches=2,ACCEPTED_items=3,ACCEPTED_batches=2,CLOSED_items=0,CLOSED_batches=0,denominators=dict(required_items=27,batches=13),author_evidence_read_rule='Use each exact candidate_commit plus candidates/<batch_id>/evidence/author/ paths from candidate freeze, not an assumed file on current tree',prior_acceptance='review/remediation-seventh-20261015-prepare/acceptance/U04-U05/v1/decision.json',three_procedural_waits=['R7-U03','R7-U07','R7-U10'],actual_new_review='NOT_CREATED_PENDING_PARENT_FRESH_R7IR',formal_frozen_commit='Bound by successor integrated-input and dispatch; no self-referential guessed hash',runtime='All behavioral vectors NOT_EXECUTED, host/Demo/native/save/replay0; effective model settings UNVERIFIED; L01-L14 and prior56/92 retained',nonmandatory_adoption='NONE'))
    print(json.dumps(dict(batches=len(selected),required_items=sum(len(b['required_ids']) for b in selected),targets=len(assembled),candidate_hunks=sum(len(r['hunks']) for r in journal),explicit_same_boundary_concatenations=len(joins),prior_accepted_files_preserved=5)))

if __name__=='__main__':
    main()
