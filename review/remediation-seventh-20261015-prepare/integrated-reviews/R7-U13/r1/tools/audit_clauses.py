"""Rebuild the exact baseline-relative edits. Documentary byte checks only."""
from pathlib import Path
import json, subprocess, datetime, difflib
from run_logged import identity
W=Path('/workspace/r7-ir-R7-U13');T=Path(__file__).resolve().parent
B='e646432c644dec04d306842cc5a559a29c718fbc';MI='45c80832a41c1b56dcd7e9d93497758cbb7721de'
def git(*a):return subprocess.check_output(['git','-C',str(W/'checkout'),*a])
def check(data, expected):
    a=identity(data)
    for k,v in expected.items():
        if k in a: assert a[k]==v,(k,a[k],v)
        if k=='git_blob': assert a['git_blob_content_id']==v
    return a
J=json.loads((W/'actual-input/integration/applied-clauses.json').read_bytes())
P=json.loads((W/'actual-plans/R7-U13.json').read_bytes())
lookup={(r['commit'],r['path']):W/'actual-input'/r['local_path'] for r in P['artifacts']}
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':[],'hunks':[], 'shared_candidate_hunks':[], 'root_adjustments':[], 'semantic_scope':'Only GR7-D07-001; other edits mechanical preservation, no new semantic approval'}
for f in J['files']:
    path=f['path']
    absent=subprocess.run(['git','-C',str(W/'checkout'),'cat-file','-e',B+':'+path],capture_output=True).returncode!=0
    base=b'' if absent else git('show',B+':'+path)
    if absent: assert f['baseline_identity']['bytes']==0
    check(base,f['baseline_identity']);lines=base.decode().splitlines(keepends=True)
    final=git('show',MI+':'+path);fl=final.decode().splitlines(keepends=True)
    cursor=0;assembled=[]
    for h in sorted(f['hunks'],key=lambda h:(h['base_line_indices_half_open'][0],h['batch_order'])):
        lo,hi=h['base_line_indices_half_open'];assert lo>=cursor,(path,lo,cursor)
        rem=''.join(lines[lo:hi]).encode();add=h['added_text'].encode()
        assert rem==h['removed_text'].encode();check(rem,h['removed_identity']);check(add,h['added_identity'])
        assembled+=lines[cursor:lo];a0=len(assembled);assembled+=h['added_text'].splitlines(keepends=True);a1=len(assembled)
        assert [a0,a1]==h['actual_final_line_indices_half_open'],(path,a0,a1)
        if path!='review/remediation-seventh-20261015-prepare/current-navigation-errata.json':
            assert ''.join(fl[a0:a1]).encode()==add,(path,h['batch_id'])
        key=(h['candidate_commit'],h['candidate_path']);matched=False
        cdbytes=git('show',h['candidate_commit']+':'+h['candidate_path'])
        if key in lookup: assert cdbytes==lookup[key].read_bytes()
        if cdbytes is not None:
            cd=cdbytes.decode().splitlines(keepends=True);c0,c1=h['candidate_line_indices_half_open']
            assert ''.join(cd[c0:c1]).encode()==add
            # The independent diff must contain exactly this baseline-relative edit.
            ops=difflib.SequenceMatcher(None,lines,cd,autojunk=False).get_opcodes()
            assert any((i,j,k,l)==(lo,hi,c0,c1) for tag,i,j,k,l in ops if tag!='equal'),(path,h['batch_id'])
            matched=True
        r={'path':path,'batch':h['batch_id'],'base_zero_based_half_open':[lo,hi],'actual_zero_based_half_open':[a0,a1],'added_identity':identity(add),'removed_identity':identity(rem),'restored_candidate_slice_and_independent_diff_match':matched,'candidate_input_method':'restored plan member + exact Git blob' if key in lookup else 'exact immutable Git blob; mechanical scope only','candidate_commit':h['candidate_commit'],'candidate_path':h['candidate_path'],'candidate_full_identity':identity(cdbytes)}
        out['hunks'].append(r)
        if h['batch_id'] in ['R7-U01','R7-U02','R7-U11','R7-U12'] and path in ['audit/source-traceability.md','planning/feature-matrix.md','deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md']:
            assert matched;out['shared_candidate_hunks'].append(r)
        cursor=hi
    assembled+=lines[cursor:];data=''.join(assembled).encode();check(data,f['assembled_candidate_clauses_identity'])
    for adj in J['root_administrative_reception_adjustments']:
        if adj['path']!=path:continue
        check(data,adj['before_identity'])
        if 'added_text' in adj:data+=adj['added_text'].encode()
        else:
            before=json.loads(data);after=json.loads(final)
            def changes(a,b,p=''):
                if type(a)!=type(b): return [(p,a,b)]
                if isinstance(a,dict):
                    assert a.keys()==b.keys();return [r for k in a for r in changes(a[k],b[k],p+'/'+k)]
                if isinstance(a,list):
                    assert len(a)==len(b);return [r for i,(x,y) in enumerate(zip(a,b)) for r in changes(x,y,p+'/'+str(i))]
                return [] if a==b else [(p,a,b)]
            delta=changes(before,after)
            assert delta==[
                ('/status','CANDIDATE_READY_NOT_REVIEWED','INTEGRATED_PENDING_INDEPENDENT_ACTUAL_REVIEW'),
                ('/reception/candidate_review','PENDING different actual context ultra reviewer after R7-I candidate-input freeze','PASS_SCOPED_CANDIDATE at 28335c5d8400b6b64e53ad56ee55c572f5a3cc07; root received exact bytes'),
                ('/reception/shared_integration','PENDING R7-I clause integration; CG01/CG07 remain','R7-I clause-level CG01/CG07 integration applied; actual independent review pending')],delta
            data=final;adj=dict(adj,json_field_changes=delta)
        check(data,adj['after_identity']);out['root_adjustments'].append(adj)
    assert data==final,path
    out['files'].append({'path':path,'hunks':len(f['hunks']),'identity':identity(final),'exact_rebuilt_MI':True})
assert len(out['hunks'])==56 and len(out['files'])==24 and len(out['shared_candidate_hunks'])==9
out['same_boundary_insertions']=J['same_boundary_insertions']
out['summary']={'reconstructed_files':len(out['files']),'hunks':len(out['hunks']),'shared_preservation_checks':9,'candidate_slices_checked':sum(h['restored_candidate_slice_and_independent_diff_match'] for h in out['hunks']),'root_admin_adjustments':len(out['root_adjustments'])}
(T/'clause-byte-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out['summary']))
