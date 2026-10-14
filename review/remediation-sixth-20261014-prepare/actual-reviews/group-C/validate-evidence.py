"""Review-artifact integrity only. No game/reference/vector execution."""
import datetime
import hashlib
import json
import pathlib
import subprocess

OUT=pathlib.Path(__file__).parent
ROOT=pathlib.Path('/workspace/r6-actual-c')
ACT='86bbc99b28d93db4ed9d6897daf5f3725ccd1808'
PREFIX='review/remediation-sixth-20261014-prepare/actual-reviews/group-C/'

def git(*args):return subprocess.check_output(['git','-C',str(ROOT)]+list(args))
def sha(b):return hashlib.sha256(b).hexdigest()

def main():
    data={p.name:json.loads(p.read_text()) for p in OUT.glob('*.json') if p.name not in ['validation-result.json','payload-manifest.json','core-remote-readback.json','publication-receipt.json']}
    binding=data['binding.json'];assert binding['actual_commit']==ACT
    assert binding['workspace_tree']==git('rev-parse',ACT+'^{tree}').decode().strip()
    assert binding['formal_tree']==git('rev-parse',ACT+':deliverables/final-specification-set').decode().strip()
    expected=git('diff','--full-index','--no-color','--no-ext-diff','9d5b4e99b617828690e6529b77a1e555d7c9eb1b',ACT,'--','deliverables/final-specification-set')
    assert (OUT/'final-formal-delta.patch').read_bytes()==expected
    review=data['per-id-review.json'];rows=review['rows'];assert len(rows)==19 and len({x['id'] for x in rows})==19
    assert set(review['rows'][i]['id'] for i in range(19))==set(data['merged-contribution-checks.json']['primary_ids'])
    assert all(x['actual_commit']==ACT and x['verdict']=='ACTUAL_PASS_SCOPED_STATIC' and not x['blocking_failures'] and not x['minimum_substantive_changes'] for x in rows)
    assert all(x['independent_static_acceptance_vectors'] and x['frozen_acceptance_and_regression']['static_acceptance_without_host'] for x in rows)
    assert not review['formal_acceptance'] and not review['CLOSED']
    assert 'optional' in review['AN007_optional_boundary'] and 'UNVERIFIED' in (OUT/'report.md').read_text()
    assert all(v=='UNVERIFIED' for v in binding['actual_configuration'].values())
    all_source_names={pathlib.PurePosixPath(x['path']).name for x in data['read-identities.json']['rows'] if x['commit']=='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'}
    all_source_names|={pathlib.PurePosixPath(x['path']).name for x in data['shared-full-read-reuse.json']['sources']}
    missing=[s for r in rows for s in r.get('source_context_anchors',[]) if s.split(':')[0] not in all_source_names]
    assert not missing,missing
    assert data['final-input-delta-and-preservation.json']['all53_final_input_formal_identities_checked']
    assert len(data['final-input-delta-and-preservation.json']['unchanged_group_readset'])==13
    changed=git('diff','--name-only',ACT).decode().splitlines()
    assert all(p.startswith(PREFIX) for p in changed),changed
    untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
    assert all(p.startswith(PREFIX) for p in untracked),untracked
    links=[]
    import re
    for target in re.findall(r'\]\(([^)]+)\)',(OUT/'report.md').read_text()):
        if target.startswith('https:'):continue
        links.append(target)
        # Two final publication receipts are written only after core push/readback.
        assert (OUT/target).is_file() or target in ['publication-receipt.json','payload-manifest.json','core-remote-readback.json'],target
    value={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'mode':'TOOL_ARTIFACT_INTEGRITY_ONLY',
           'actual_commit':ACT,'checks':{'all_JSON_parse':True,'binding_and_formal_tree':True,'final_patch_exact':True,
           'unique19_complete_static_dispositions':True,'all_named_new_source_anchors_have_read_identities':True,
           'all53_input_identities_preverified':True,'13_unchanged_readset':True,'relative_report_links':True,
           'scope_only_owned_directory':True,'UNVERIFIED_actual_configuration':True,'no_formal_acceptance_or_CLOSED':True},
           'static_vector_groups':sum(len(r['independent_static_acceptance_vectors']) for r in rows),
           'source_execution':0,'model_execution':0,'host_execution':0,'Demo_execution':0,
           'scope_check_tracked_paths':changed,'scope_check_untracked_paths':untracked,'blocking_failures':[]}
    (OUT/'validation-result.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'integrity':'PASS','primary_ids':len(rows),'vector_groups':value['static_vector_groups'],'owned_new_files':len(untracked)},ensure_ascii=False))

if __name__=='__main__':main()
