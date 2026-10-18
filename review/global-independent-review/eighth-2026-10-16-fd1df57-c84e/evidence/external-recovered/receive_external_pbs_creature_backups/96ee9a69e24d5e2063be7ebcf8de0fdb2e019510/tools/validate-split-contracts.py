"""Independent complete-set and identity validation of the four dispatch contracts."""
from pathlib import Path
import ast
import hashlib
import json
import subprocess

T=Path(__file__).resolve().parents[1]
OUT=T/'delegation/remaining-v1'
REPO=Path.cwd()

def load(path):
    return json.loads(path.read_text())

def identity(path):
    data=path.read_bytes()
    return dict(path=str(path.relative_to(REPO)),mode='100644',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),
                blob=hashlib.sha1(('blob '+str(len(data))+'\0').encode()+data).hexdigest())

def main():
    index=load(OUT/'index.json')
    prior=load(T/'reception-ledger.json')
    original={r['section_id']:r for r in load(T/'recovered-target/forward-mapping.json')['records']}
    pending={r['id'] for r in prior['records'] if r['literal_status']=='AVAILABLE_UNREAD_NOT_RECEIVED'}
    pending_atoms={a['id'] for a in prior['atoms'] if a['receiver_status']!='FINITE_PREDICATE_RECEIVED_FOR_ROOT'}
    remaining_ifs={x['id'] for x in load(T/'interfaces.json')['interfaces'] if x['status']=='INCOMPLETE_NOT_SIGNED'}
    seen_records=set();seen_atoms=set();seen_ifs=set();seen_heads=set();counts=[]
    for a in index['assignments']:
        path=OUT/a['id']
        rs=load(path/'readset.complete.json')
        prompt=(path/'prompt.md').read_text()
        assert 'NOT_STARTED' in rs['status'] and rs['independence']['actual_shard_context']=='NOT_STARTED_NOT_ASSIGNED'
        assert rs['exclusive_write_set']==a['exclusive_write_set']
        assert rs['exclusive_write_set'].startswith(str(T.relative_to(REPO))+'/shards/')
        assert rs['exclusive_write_set'] in prompt
        assert str((path/'readset.complete.json').relative_to(REPO)) in prompt
        assert identity(path/'prompt.md')==a['prompt']
        assert identity(path/'readset.complete.json')==a['readset']
        for norm in rs['normative_inputs']:
            actual=identity(REPO/norm['path'])
            assert all(actual[k]==norm[k] for k in actual)
            if 'source_commit' in norm:
                source=subprocess.check_output(['git','show',norm['source_commit']+':'+norm['source_path']])
                assert source==(REPO/norm['path']).read_bytes()
        ids={x['complete_target_forward_object']['section_id'] for x in rs['owned_records']}
        atoms={x['id'] for x in rs['owned_atoms']}
        interfaces={x['id'] for x in rs['owned_interfaces']}
        headers={x['id'] for x in rs['owned_header']}
        assert not (ids&seen_records or atoms&seen_atoms or interfaces&seen_ifs or headers&seen_heads)
        seen_records|=ids;seen_atoms|=atoms;seen_ifs|=interfaces;seen_heads|=headers
        raw={x['id']:(Path(x['repo'])/x['path']).read_bytes() for x in rs['owned_primary_files']}
        for x in rs['owned_records']:
            record=x['complete_target_forward_object']
            assert record==original[record['section_id']]
            start,end=x['frozen']['byte_offsets_half_open']
            assert hashlib.sha256(raw[record['identity_id']][start:end]).hexdigest()==x['source_unit_sha256']
        assert len(ids)==rs['counts']['records']
        assert sum(len(x['complete_target_forward_object']['fields']) for x in rs['owned_records'])==rs['counts']['fields']
        assert sum(len(x['complete_target_forward_object']['omitted']) for x in rs['owned_records'])==rs['counts']['omissions']
        assert len(atoms)==rs['counts']['atoms'] and len(interfaces)==rs['counts']['interfaces']
        counts.append(dict(id=a['id'],**rs['counts']))
    assert seen_records==pending and len(seen_records)==3940
    assert seen_atoms==pending_atoms and len(seen_atoms)==192
    assert seen_ifs==remaining_ifs and len(seen_ifs)==10
    assert len(seen_heads)==4
    assert sum(x['fields'] for x in counts)==77195 and sum(x['omissions'] for x in counts)==72617
    assert index['new_contexts_started_by_this_task']==0
    for p in (T/'tools').glob('*.py'):
        ast.parse(p.read_text())
    result=dict(schema='r8-disjoint-dispatch-independent-validation/v1',status='PASS_CONTRACT_SET_AND_IDENTITY_ONLY',
                record_union_exact=True,records_pairwise_disjoint=True,atom_union_exact=True,atoms_pairwise_disjoint=True,
                interface_union_exact=True,interfaces_pairwise_disjoint=True,header_ownership_exact=True,
                all_original_forward_objects_exact=True,all_source_units_exact=True,normative_full_text_copies_exact=True,
                counts=counts,new_contexts=0,semantic_reading_added=0,behavior_execution='NOT_EXECUTED',task_status='INCOMPLETE')
    (OUT/'validation.independent.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    files=[identity(p) for p in sorted(OUT.rglob('*')) if p.is_file() and p!=OUT/'payload-manifest.json']
    (OUT/'payload-manifest.json').write_text(json.dumps(dict(schema='r8-dispatch-payload-manifest/v1',files=files,count=len(files),bytes=sum(x['bytes'] for x in files),
        excluded_self='Bound externally by actual immutable commit/tree and full remote readback',semantic_credit=0),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],counts=counts,payloads=len(files),new_contexts=0,semantic_reading_added=0)))

if __name__=='__main__':
    main()
