"""Independent bounded input identity, diff, raw-binding and preservation audit.

No restored program is executed. Successful checks are TOOL_VALIDATION only.
"""
import datetime
import difflib
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

OUT = Path(__file__).resolve().parents[1]
REPO = Path('/workspace/pokemon-essentials-clean-room')
CTX = Path('/workspace/r7-context/R7-U06-reviewer')
CAND = Path('/workspace/r7-review-input/R7-U06-r1-fd0c1e6f50587331846921d446d893f1c1e84f3d')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
ENTRY = '95c260d8f3fb4a171675dde877137fcd4c2f1c8d'
FREEZE = 'aa369555b0e8b6c8b077f964b54ed63d3b924f26'
COMMIT = 'fd0c1e6f50587331846921d446d893f1c1e84f3d'
PREFIX = 'review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U06/'

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def ident(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob_content_id': hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

def verify(data, expected):
    actual = ident(data)
    for k, v in actual.items():
        ek = 'git_blob' if k == 'git_blob_content_id' and 'git_blob' in expected else k
        if ek in expected:
            assert v == expected[ek], (k, expected[ek], v)
    return actual

def write(name, data):
    p = OUT / name
    with p.open('x') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')

def ptr(obj, pointer):
    for bit in pointer.split('/')[1:]:
        bit = bit.replace('~1','/').replace('~0','~')
        obj = obj[int(bit)] if isinstance(obj, list) else obj[bit]
    return obj

def walk(obj):
    yield obj
    if isinstance(obj, dict):
        for v in obj.values(): yield from walk(v)
    elif isinstance(obj, list):
        for v in obj: yield from walk(v)

def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',',':')).encode()

def main():
    frozen_files = {}
    for name in ['candidate-input.json', 'candidate-restore/R7-U06.json', 'mirror-diffs.patch', 'remote-readback.json']:
        a = git('show', FREEZE+':'+PREFIX+name)
        assert a == git('show', ENTRY+':'+PREFIX+name)
        frozen_files[name] = ident(a)
    freeze = json.loads(git('show', FREEZE+':'+PREFIX+'candidate-input.json'))
    assert git('rev-parse', FREEZE+'^{tree}').decode().strip() == '08bd0f362c74ef7645b5bbd70b557489c122ae29'
    assert git('rev-parse', COMMIT+'^{tree}').decode().strip() == freeze['candidate_tree']
    assert git('rev-parse', B+':deliverables/final-specification-set').decode().strip() == 'ebbe29f2bc88cd17de7072bf440c6fa8c8c7089c'
    raw_diff = git('diff','--name-status',B,COMMIT).decode().splitlines()
    actual_diff = [{'status': s, 'path': p} for s,p in (line.split('\t') for line in raw_diff)]
    assert actual_diff == freeze['complete_diff_against_B']
    assert all(x['status']=='A' and x['path'].startswith('candidates/R7-U06/') for x in actual_diff)
    rows = []
    for r in freeze['candidate_and_author_evidence_file_identities']:
        data = (CAND/'candidate'/r['path']).read_bytes()
        actual = verify(data, r)
        assert data == git('show', COMMIT+':'+r['path'])
        mode, kind, blob = git('ls-tree', COMMIT, '--', r['path']).decode().split('\t')[0].split()
        assert mode == r['git_mode'] == '100644' and kind == 'blob' and blob == actual['git_blob_content_id']
        rows.append({'path':r['path'],'git_mode':mode, **actual})
    assert len(rows)==43 and sum(r['bytes'] for r in rows)==597346
    restore_rows = []
    plans = [('/workspace/r7-bootstrap/R7-U06-reviewer/recovery/batches/R7-U06.json', CTX),
             ('/workspace/r7-review-bootstrap/R7-U06-r1/candidate-restore/R7-U06.json', CAND)]
    for plan_path, root in plans:
        plan=json.loads(Path(plan_path).read_bytes())
        for group in ['artifacts','evidence','fixed_read_inputs']:
            for row in plan[group]:
                restore_rows.append({'root':str(root),'path':row['local_path'],**verify((root/row['local_path']).read_bytes(),row)})
    c13=CTX/'evidence/tasks/R7-C13'
    normalized=json.loads((c13/'inputs/tasks/R7-P02/normalized-record-candidates.json').read_bytes())
    bindings=json.loads((c13/'raw-binding-manifest.json').read_bytes())
    contract=json.loads((CTX/'dispatch/delegation/contracts/R7-U06.json').read_bytes())
    binding_checks=[]
    for i in [12,13]:
        for row in walk(normalized['records'][i]):
            if not isinstance(row,dict) or not {'input_sha256','json_pointer','canonical_sha256'} <= row.keys(): continue
            paths=list(c13.rglob(row['input_sha256']+'.raw'))
            assert len(paths)==1, (row['input_sha256'], paths)
            raw=paths[0].read_bytes()
            assert hashlib.sha256(raw).hexdigest()==row['input_sha256']
            member=ptr(json.loads(raw),row['json_pointer'])
            assert hashlib.sha256(canonical(member)).hexdigest()==row['canonical_sha256']
            if 'raw_member_byte_offsets' in row:
                a,b=row['raw_member_byte_offsets']; part=raw[a:b]
                assert len(part)==row['raw_member_bytes']
                assert hashlib.sha256(part).hexdigest()==row['raw_member_sha256']
                assert json.loads(part)==member
            binding_checks.append({'record_index':i,'input_sha256':row['input_sha256'],'pointer':row['json_pointer'],'canonical_sha256':row['canonical_sha256']})
    scope=[]
    for row in freeze['candidate_and_author_evidence_file_identities']:
        if row['role']!='candidate_mirror':continue
        target=row['formal_target']; base=git('show', B+':'+target)
        verify(base,row['base_B_identity_or_explicit_new_file'])
        assert base==(CTX/'inputs/project'/target).read_bytes()
        cand=(CAND/'candidate'/row['path']).read_bytes()
        old=base.decode().splitlines(keepends=True); new=cand.decode().splitlines(keepends=True)
        blocks=[]
        for tag,a,b,c,d in difflib.SequenceMatcher(a=old,b=new,autojunk=False).get_opcodes():
            if tag!='equal':blocks.append({'operation':tag,'base_line_start':a+1,'base_line_end':b,'candidate_line_start':c+1,'candidate_line_end':d})
        if '/wp46-' in target:
            assert [x['base_line_start'] for x in blocks]==[23,54,59]
            assert all(x['operation']=='replace' and x['base_line_start']==x['base_line_end'] for x in blocks)
        else:
            assert len(blocks)==1 and blocks[0]['operation']=='insert'
            assert ''.join(x for x in new if True).encode()==cand
            a=blocks[0]['candidate_line_start']-1;b=blocks[0]['candidate_line_end']
            assert ''.join(new[:a]+new[b:]).encode()==base
        scope.append({'path':row['path'],'formal_target':target,'base':ident(base),'candidate':ident(cand),'complete_changes':blocks,'all_other_bytes_preserved':True})
    author=json.loads((CAND/'candidate/candidates/R7-U06/evidence/author/per-id.json').read_bytes())
    for i,a in zip([12,13],author['records']):
        assert a['original_accepted_verification']==normalized['records'][i]['groups']['verification']
        assert a['original_dependencies_retained']==normalized['records'][i]['groups']['dependencies']
    runtime=json.loads((CAND/'candidate/candidates/R7-U06/evidence/author/runtime-identity.json').read_bytes())
    reviewer={k:os.environ.get(k,'NOT_EXPOSED') for k in ['CODEX_THREAD_ID','CODEX_SESSION_ID','CODEX_ENVIRONMENT_ID']}
    assert reviewer['CODEX_THREAD_ID']!=runtime['actual_thread_id']==freeze['author_task_id']
    original_receipts=[]
    for root in [CTX,CAND]:
        for p in sorted(root.glob('recovery-receipt-*.json')):
            dest=OUT/'receipts'/p.name
            if dest.exists(): assert dest.read_bytes()==p.read_bytes()
            else: shutil.copyfile(p,dest)
            original_receipts.append({'path':'receipts/'+p.name,**ident(p.read_bytes())})
    write('review-input-receipt.json', {
        'schema':'r7.u06.independent-review-input-receipt.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'entry_commit':ENTRY,'entry_tree':git('rev-parse',ENTRY+'^{tree}').decode().strip(),
        'candidate_freeze_commit':FREEZE,'candidate_freeze_tree':git('rev-parse',FREEZE+'^{tree}').decode().strip(),
        'frozen_files_same_at_entry_and_freeze':frozen_files,
        'fixed_B':B,'candidate_commit':COMMIT,'candidate_tree':freeze['candidate_tree'],
        'reviewer_visible_identity':reviewer,'author_visible_identity':runtime,
        'different_actual_thread_and_environment':reviewer['CODEX_THREAD_ID']!=runtime['actual_thread_id'] and reviewer['CODEX_ENVIRONMENT_ID']!=runtime['actual_environment_id'],
        'task_id':'NOT_EXPOSED_SEPARATELY','context_id':'NOT_EXPOSED_SEPARATELY','model_process_pid':'NOT_EXPOSED',
        'requested':{'model':'gpt-6.1-sol','effort':'ultra','service_tier':'default','speed':'ordinary','Fast':'PROHIBITED'},
        'effective':{k:'UNVERIFIED_NO_EFFECTIVE_PLATFORM_RETURN' for k in ['model','effort','service_tier','speed']},
        'candidate_files':rows,'candidate_file_count':len(rows),'candidate_byte_count':sum(r['bytes'] for r in rows),
        'complete_candidate_diff_against_B':actual_diff,'candidate_scope':scope,'restore_revalidation':restore_rows,
        'original_restore_receipts':original_receipts,'binding_reference_occurrences_checked':len(binding_checks),
        'binding_results_file':'receipts/raw-bindings.json','execution':'TOOL_VALIDATION_ONLY','semantic_credit_from_exit0':False,
        'L01_L14':'RETAINED','behavior_vectors':'NOT_EXECUTED','new_reference_host_Demo_native_media_real_save_replay_full_model':0})
    write('receipts/raw-bindings.json',binding_checks)
    print(json.dumps({'candidate_files':len(rows),'candidate_bytes':sum(x['bytes'] for x in rows),'bindings':len(binding_checks),'mirrors':scope,'tool_validation_only':True},ensure_ascii=False))

if __name__=='__main__':main()
