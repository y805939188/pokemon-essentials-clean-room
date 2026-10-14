"""Repair-only documentation controls; no reference behavior execution."""
from pathlib import Path
from collections import Counter
import ast, datetime, hashlib, json, re, subprocess

OUT=Path(__file__).resolve().parent
EVIDENCE=OUT.parent
REPO=OUT.parents[5]
PRIOR='00b45de642f07cee9953e42f04cce9c35d77346f'
REVIEW='3ef4854ef43eac92fd1dc57350e4cf6aa160082b'
PREFIX='review/remediation-sixth-20261014-prepare/candidates/R6-U13/'
PT='mirror/deliverables/final-specification-set/test-catalog/pokemon-rules-wp53-60-61-62-69-70.md'

def git(*args):
    return subprocess.check_output(['git',*args],cwd=REPO)

def digest(b):
    return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
            'git_blob':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()}

# Load only the two pure document-check helpers, not the script's I/O entry.
module=ast.parse((EVIDENCE/'verify_candidate.py').read_text())
nodes=[n for n in module.body if isinstance(n,ast.FunctionDef) and n.name in {'catalogue_rows','sf30_subcase_presence'}]
assert len(nodes)==2
ns={'re':re,'Counter':Counter}
exec(compile(ast.Module(body=nodes,type_ignores=[]),'<document-check-helpers>','exec'),ns)
index_rows=ns['catalogue_rows'];subcases=ns['sf30_subcase_presence']
old=git('show',PRIOR+':'+PREFIX+PT).decode()
new=(REPO/PREFIX/PT).read_text()
oldrows,_=index_rows(old,r'^\| SF\d','old FAIL catalogue')
newrows,audit=index_rows(new,r'^\| SF\d','repaired catalogue')
old_check=subcases(oldrows['SF30']);new_check=subcases(newrows['SF30'])
assert not any(old_check.values()) and all(new_check.values())
try:
    index_rows(new+'\n'+newrows['SF30'],r'^\| SF\d','injected duplicate')
except AssertionError as err:
    duplicate_detected='SF30' in str(err)
else:
    duplicate_detected=False
assert duplicate_detected
assert new.splitlines()[39]==newrows['SF30']
expected=old.replace(oldrows['SF30'],newrows['SF30'])
assert new==expected,'Only SF30 may differ in the mirror'
mirrors=git('ls-tree','-r','--name-only',PRIOR,PREFIX+'mirror/').decode().splitlines()
unchanged=[]
for p in mirrors:
    if p!=PREFIX+PT:
        assert git('show',PRIOR+':'+p)==(REPO/p).read_bytes()
        unchanged.append(p)
assert len(unchanged)==7

history=json.loads((EVIDENCE/'historical-regression.json').read_text())
old_history=json.loads(git('show',PRIOR+':'+PREFIX+'evidence/historical-regression.json'))
for before,after in zip(old_history['R5_exact_scopes_read'],history['R5_exact_scopes_read']):
    assert before['id']==after['id']
    assert before['qualified_scope']==after['qualified_scope']
    assert before['binding_blob']==after['binding_blob']
    assert after['retrieval_transition']['fixed_path_exists'] is True
    assert 'did not establish path absence' in after['retrieval_note']
    data=git('show',after['source_commit']+':'+after['source_path'])
    assert all(digest(data)[k]==after[k] for k in ['bytes','sha256','git_blob'])
assert 'Original contract path was not present' not in (EVIDENCE/'bind_history.py').read_text()

review_inputs=[]
RPATH='review/remediation-sixth-20261014-prepare/reviews/R6-U13-R/'
for p in ['review-report.md','R5-path-correction.json','recording-save/conversion-negative-evidence.json','wp66-a-required-receiving-delta.md','facility/wp66-a-receiver-payload.json','history-payload/report.md','history-payload/bytes-audit/bytes-and-author-tools-report.md','recording-save/report.md']:
    b=git('show',REVIEW+':'+RPATH+p)
    review_inputs.append({'commit':REVIEW,'path':RPATH+p,**digest(b),'lines':len(b.splitlines()),'full_text_presented_and_read':True})

result={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cwd':str(REPO),
 'argv':['python',str(Path(__file__).relative_to(REPO))],'exit':0,'stderr':'',
 'prior_candidate':PRIOR,'fixed_FAIL_report':REVIEW,'review_inputs':review_inputs,
 'mirror_delta':'ONE_PHYSICAL_SF30_LINE_ONLY','seven_other_mirrors_byte_equal':unchanged,
 'catalogue_raw_audit':audit,'old_FAIL_SF30_presence':old_check,'new_SF30_presence':new_check,
 'injected_duplicate_SF30_rejected_before_indexing':duplicate_detected,
 'R5_three_qualified_scope_payloads_unchanged':True,'R5_exact_commit_paths_local_full_bytes_match':True,
 'checks_limit':'Raw IDs, exact byte preservation, textual subcase presence and fixed input identities only. SF30 meaning is separately author-static compared in report.md. No arbitrary subcase preservation or probability behavior proof.',
 'source_execution':False,'host_execution':False,'real_save_load':False,
 'independent_recheck':'PENDING_SAME_PARENT_ASSIGNED_REVIEWER','WP66_A_actual_receiving':'PENDING_R6_I_BLOCKS_INTEGRATED_ACCEPTANCE'}
(OUT/'checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'AUTHOR_REPAIR_DOCUMENT_CHECKS_PASS','mirror_delta':'SF30_ONLY','counts_SF':audit['raw_row_count'],'duplicates_detectable':duplicate_detected,'old_FAIL_case_rejected':True,'seven_mirrors_unchanged':len(unchanged)},ensure_ascii=False))
