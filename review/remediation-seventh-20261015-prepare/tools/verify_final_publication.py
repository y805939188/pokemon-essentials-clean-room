"""Verify final public metadata delta without granting new behavior evidence."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess

ROOT=Path(__file__).resolve().parents[3]
P=ROOT/'review/remediation-seventh-20261015-prepare'
B='e646432c644dec04d306842cc5a559a29c718fbc'
MI='94d5eb73f4508b8a8a54319040faa9aea5752059'

def git(*args):
    return subprocess.check_output(['git','-C',str(ROOT),*args])

def ident(data):
    return dict(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),git_blob=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def diff_json(before,after,pointer=''):
    if isinstance(before,dict) and isinstance(after,dict):
        result=[]
        for key in set(before)|set(after):
            path=pointer+'/'+key
            if key not in before or key not in after:
                result.append(path)
            else:
                result.extend(diff_json(before[key],after[key],path))
        return result
    return [] if before==after else [pointer]

def main():
    ledger=json.loads((P/'ledger.json').read_text())
    decision=json.loads((P/'closure/final/decision.json').read_text())
    policy=json.loads((P/'governance/current-execution-policy.json').read_text())
    formal=json.loads((P/'completion/formal-files.json').read_text())
    sync=json.loads((P/'completion/public-sync-manifest.json').read_text())
    assert ledger['counters']==dict(candidate_pass_items=27,integrated_pass_items=27,accepted_items=27,closed_items=27,candidate_pass_batches=13,integrated_pass_batches=13,accepted_batches=13,closed_batches=13)
    assert len(decision['records'])==len({r['id'] for r in decision['records']})==27
    assert all(r['CLOSED'] and r['remaining_finite_required_dependencies']==[] for r in decision['records'])
    assert decision['retained_open_limits'] and policy['main_merge_prohibited_for_this_round']
    assert not policy['main_merge_authorized'] and not ledger['main_merge_allowed_now']
    checks=[]
    for row in formal['files']:
        actual=(ROOT/row['path']).read_bytes()
        assert actual==git('show',MI+':'+row['path'])
        assert ident(actual)=={k:row[k] for k in ['bytes','sha256','git_blob']}
    assert len(formal['files'])==131 and sum(r['changed_against_B'] for r in formal['files'])==33
    for row in sync['paths']:
        before=git('show',MI+':'+row['path'])
        after=(ROOT/row['path']).read_bytes()
        assert ident(before)==row['before_identity'] and ident(after)==row['after_identity']
        if row['kind']=='EXACT_APPEND_ONLY_CURRENT_RECEIPT':
            assert after==before+row['added_text'].encode()
            checks.append(dict(path=row['path'],status='EXACT_PREFIX_PRESERVED_FINAL_RECEIPT_APPENDED',identity=ident(after)))
        else:
            changes=set(diff_json(json.loads(before),json.loads(after)))
            assert changes==set(row['allowed_changed_pointers'])
            new=json.loads(after)
            assert new['record_id']=='GR7-H08-001' and new['current_label']=='WP72 §5.3／WP27'
            assert new['reception']['ACCEPTED'] and new['reception']['CLOSED']
            checks.append(dict(path=row['path'],status='ONLY_EXPLICIT_ROOT_RECEIPT_FIELDS_CHANGED',pointers=sorted(changes),identity=ident(after)))
    r6='review/remediation-sixth-20261014-prepare'
    assert git('rev-parse','HEAD:'+r6)==git('rev-parse',B+':'+r6)
    report='review/global-independent-review/seventh-2026-10-14-e646432-7a91'
    assert git('rev-parse','HEAD:'+report).decode().strip()=='a011f74704047f11ee47c9a631914337558cb81b'
    links=[]
    for path in [P/'completion/final-report.md',ROOT/'audit/source-traceability.md',ROOT/'planning/feature-matrix.md']:
        content=path.read_text() if path.name=='final-report.md' else next(r['added_text'] for r in sync['paths'] if ROOT/r['path']==path)
        for target in re.findall(r'\]\(([^)]+)\)',content):
            if target.startswith(('http:','https:','#')):
                continue
            dest=(path.parent/target.split('#',1)[0]).resolve()
            # The binding file is created after this validation, before publication.
            if dest==P/'completion/final-delivery-binding.json' and not dest.exists():
                continue
            assert dest.exists(),(path,target)
            links.append(dict(source=str(path.relative_to(ROOT)),target=target,status='EXISTS'))
    branch=git('branch','--show-current').decode().strip()
    assert branch=='codex/remediation-seventh-20261015-cloud'
    main=git('ls-remote','origin','refs/heads/main').decode().strip()
    assert main.startswith(B+'\t')
    proof=dict(schema='r7.final-publication-validation.v1',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),functional_MI=MI,formal_tree=formal['formal_tree'],formal_files=131,changed_formal=33,unchanged_formal=98,formal_bytes_unchanged_after_independent_review=True,public_metadata_checks=checks,local_links=links,original_R7_report_tree_preserved=True,R6_frozen_tree_preserved=True,final_counters=ledger['counters'],finite_required_dependencies_remaining=[],retained_open_limits=decision['retained_open_limits'],branch=branch,main_remote=main,main_merge_prohibited=True,main_merge_performed=False,cleanup_or_local_sync_performed=False,credit='TOOL_VALIDATION of final artifact consistency and administrative-only public delta; semantic evidence remains the independent actual reports.')
    output=P/'completion/public-sync-validation.json'
    output.write_text(json.dumps(proof,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(formal=131,formal_unchanged=True,public_metadata_paths=3,local_links=len(links),finite_corrections_closed=27,retained_limits='OPEN',main_merged=False)))

if __name__=='__main__':
    main()
