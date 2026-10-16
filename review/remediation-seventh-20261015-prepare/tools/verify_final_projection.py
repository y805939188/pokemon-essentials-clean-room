"""Bounded static projection audit. It grants no semantic PASS or closure."""
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

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])

def identity(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def json_diff(before,after,pointer=()):
    if isinstance(before,dict) and isinstance(after,dict):
        result=[]
        for key in set(before)|set(after):
            if key not in before or key not in after:
                result.append(pointer+(key,))
            else:
                result.extend(json_diff(before[key],after[key],pointer+(key,)))
        return result
    return [] if before==after else [pointer]

def main():
    frozen=json.loads(git('show',FI+':review/remediation-seventh-20261015-prepare/integration/wave4/v1/integrated-input.json'))
    journal=json.loads(git('show',MI+':review/remediation-seventh-20261015-prepare/integration/wave4/v1/applied-clauses.json'))
    ledger=json.loads((P/'ledger.json').read_text())
    registry=json.loads((P/'delegation/task-registry/current.json').read_text())
    batches={b['id']:b for b in ledger['batches']}
    required={r['id'] for r in ledger['issues']}
    assert len(required)==27 and len(batches)==13
    severities=collections.Counter()
    approved_targets=set()
    required_from_contracts=set()
    for bid,batch in batches.items():
        contract=json.loads((P/'delegation/contracts'/f'{bid}.json').read_text())
        assert contract['required_ids']==batch['required_ids']
        assert contract['blocking_author_dependencies']==[]
        required_from_contracts.update(contract['required_ids'])
        severities.update(r['severity'] for r in contract['original_full_contracts'])
        candidate=json.loads((ROOT/batch['candidate_input_path']).read_text())
        permitted={r['candidate_path'] for r in contract['paths']}
        for row in candidate['candidate_and_author_evidence_file_identities']:
            if row['role']=='candidate_mirror':
                assert row['path'] in permitted
                assert row['formal_target']==row['path'].removeprefix('candidates/'+bid+'/')
                approved_targets.add(row['formal_target'])
    assert required_from_contracts==required
    assert severities==dict(P2=10,P3=17)
    formal=[]
    expected_paths={row['path'] for row in frozen['all_formal_file_identities']}
    tracked_paths=set(git('ls-tree','-r','--name-only',MI,'deliverables/final-specification-set').decode().splitlines())
    assert tracked_paths==expected_paths and len(tracked_paths)==131
    for row in frozen['all_formal_file_identities']:
        path=row['path']
        fixed=git('show',MI+':'+path)
        base=git('show',B+':'+path)
        mode=git('ls-tree',MI,path).decode().split()[0]
        assert mode=='100644'
        assert identity(fixed)=={k:row[k] for k in ['bytes','sha256','git_blob']}
        assert identity(base)==row['base_B_identity']
        assert (ROOT/path).read_bytes()==fixed, 'Current formal bytes must equal reviewed final MI'
        assert (fixed!=base)==row['changed_against_B']
        if fixed!=base:
            assert path in approved_targets
        formal.append(dict(path=path,changed=fixed!=base,identity=identity(fixed)))
    assert sum(r['changed'] for r in formal)==33
    cumulative_checks=[]
    phase_exception=[]
    admin={r['path']:r['added_text'] for r in journal['root_administrative_adjustments']}
    exact_hunks=0
    for row in journal['cumulative_files']:
        path=row['path']
        raw_base=subprocess.run(['git','-C',str(ROOT),'show',B+':'+path],capture_output=True)
        base=raw_base.stdout
        if raw_base.returncode:
            assert path=='review/remediation-seventh-20261015-prepare/current-navigation-errata.json'
        assert identity(base)==row['baseline_identity']
        actual=git('show',MI+':'+path)
        assert (ROOT/path).read_bytes()==actual
        base_lines=base.decode().splitlines(True)
        actual_lines=actual.decode().splitlines(True)
        for hunk in row['hunks']:
            assert hunk['candidate_commit']==batches[hunk['batch_id']]['candidate_commit']
            candidate=git('show',hunk['candidate_commit']+':'+hunk['candidate_path'])
            a,z=hunk['candidate_line_indices_half_open']
            inserted=''.join(candidate.decode().splitlines(True)[a:z])
            i,j=hunk['base_line_indices_half_open']
            removed=''.join(base_lines[i:j])
            assert inserted==hunk['added_text'] and removed==hunk['removed_text']
            assert identity(inserted.encode())==hunk['added_identity']
            assert identity(removed.encode())==hunk['removed_identity']
            if path.endswith('current-navigation-errata.json'):
                differences=set(json_diff(json.loads(inserted),json.loads(actual)))
                assert differences=={('status',),('reception','candidate_review'),('reception','shared_integration')}
                phase_exception.append(dict(path=path,fields=['/'+('/'.join(v)) for v in sorted(differences)],qualification='One candidate JSON hunk is not literal whole-text identity; precisely three previously recorded root reception-phase strings differ. All other fields match.'))
            else:
                a,z=hunk['actual_final_line_indices_half_open']
                assert ''.join(actual_lines[a:z])==inserted
                exact_hunks+=1
        if not path.endswith('current-navigation-errata.json'):
            assembled=[]
            cursor=0
            # Final line coordinates establish explicit ties for common EOF.
            ordered=sorted(row['hunks'],key=lambda h:(*h['base_line_indices_half_open'],h['actual_final_line_indices_half_open'][0]))
            for hunk in ordered:
                i,j=hunk['base_line_indices_half_open']
                assert cursor<=i, 'Overlapping approved replacement'
                assembled.extend(base_lines[cursor:i])
                assembled.extend(hunk['added_text'].splitlines(True))
                cursor=j
            assembled.extend(base_lines[cursor:])
            body=''.join(assembled).encode()
            assert identity(body)==row['assembled_candidate_clauses_identity']
            assert body+admin.get(path,'').encode()==actual
        cumulative_checks.append(dict(path=path,hunks=len(row['hunks']),actual_identity=identity(actual),whole_actual_reconstructed_or_exact_phase_exception=True))
    assert exact_hunks==85 and len(phase_exception)==1
    initial=json.loads((P/'integration/U04-U05/v1/applied-clauses.json').read_text())
    initial_checks=[]
    initial_hunks=0
    for row in initial['operations']:
        actual=git('show',MI+':'+row['path'])
        candidate=git('show',row['source_candidate_commit']+':'+row['source_candidate_path'])
        base=git('show',B+':'+row['path'])
        assert actual==candidate and (ROOT/row['path']).read_bytes()==actual
        assert identity(base)==row['before'] and identity(actual)==row['after']
        for hunk in row['hunks']:
            a,z=hunk['base_lines_zero_half_open']
            i,j=hunk['candidate_lines_zero_half_open']
            assert identity(''.join(base.decode().splitlines(True)[a:z]).encode())==hunk['removed_identity']
            assert identity(''.join(candidate.decode().splitlines(True)[i:j]).encode())==hunk['inserted_identity']
            initial_hunks+=1
        initial_checks.append(dict(path=row['path'],whole_actual_equals_independently_accepted_candidate=True,identity=identity(actual)))
    assert initial_hunks==11
    expected_changed={r['path'] for r in formal if r['changed']}
    expected_changed|={'audit/source-traceability.md','planning/feature-matrix.md','review/remediation-seventh-20261015-prepare/current-navigation-errata.json'}
    assert expected_changed=={r['path'] for r in cumulative_checks+initial_checks}
    assert expected_changed<=approved_targets
    assert git('rev-parse',MI+':review/global-independent-review/seventh-2026-10-14-e646432-7a91').decode().strip()=='a011f74704047f11ee47c9a631914337558cb81b'
    assert len(registry['entries'])==len({r['task_id'] for r in registry['entries']})
    proof=dict(schema='r7.final-static-clause-projection-audit.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),B=B,MI=MI,FI=FI,formal_files=131,changed_formal=33,unchanged_formal=98,required_items=27,batches=13,severities=dict(severities),candidate_and_authorized_target_scope='MATCH',cumulative_exact_candidate_hunks=exact_hunks,cumulative_recorded_phase_exception=phase_exception,initial_exact_hunks=initial_hunks,cumulative_checks=cumulative_checks,initial_checks=initial_checks,all36_actual_targets_reconstructed=True,nonmandatory_adoption='NONE',current_counters=ledger['counters'],unique_registered_task_IDs=len(registry['entries']),CLOSED_granted=False,main_merge_allowed_now=False,limits='All behavior NOT_EXECUTED;runtime0;configuration UNVERIFIED;L01-L14 retained',credit='TOOL_VALIDATION of identities, scope and exact preservation only. It is not independent semantic review, acceptance, closure or runtime-equivalence proof.')
    output=P/'closure/preflight/final-static-projection.json'
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(formal=131,changed=33,unchanged=98,exact_candidate_hunks=85,recorded_phase_exception=1,initial_exact_hunks=11,actual_targets=36,semantic_PASS_granted=False,closure_granted=False)))

if __name__=='__main__':
    main()
