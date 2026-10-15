"""Independent bounded identity, diff, navigation and historical preservation audit.

No author or reference program is imported or executed. No game behavior model.
"""
import collections
import datetime
import difflib
import hashlib
import json
import os
from pathlib import Path
import posixpath
import re
import shutil
import subprocess
import urllib.parse

OUT = Path(__file__).resolve().parents[1]
REPO = OUT.parents[4]
BOOT = Path('/workspace/r7-review-bootstrap/R7-U12-r1')
CTX = Path('/workspace/r7-context/R7-U12-reviewer')
IN = Path('/workspace/r7-review-input/R7-U12-r1-1f33c39804d819c5a55a2b084287fc4a3a4c0919')
CAN = IN / 'candidate/candidates/R7-U12'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
C = '1f33c39804d819c5a55a2b084287fc4a3a4c0919'
F = 'aa369555b0e8b6c8b077f964b54ed63d3b924f26'
D = '95c260d8f3fb4a171675dde877137fcd4c2f1c8d'
H = 'e58486178e746273fb6fab55df00722807f1dc44'
PREFIX = 'review/remediation-seventh-20261015-prepare/candidate-freezes/R7-U12/'

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def ident(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()}

def check(data, expected):
    actual = ident(data)
    for k, v in actual.items():
        key = 'git_blob_content_id' if k == 'git_blob' and 'git_blob_content_id' in expected else k
        if key in expected:
            assert v == expected[key], (key, v, expected[key])
    return actual

def save(name, value):
    (OUT/'tool-evidence'/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

(OUT/'tool-evidence').mkdir(exist_ok=True)
freeze = json.loads((BOOT/'candidate-input.json').read_text())
contract_path = CTX/'dispatch/delegation/contracts/R7-U12.json'
contract = json.loads(contract_path.read_text())
assert freeze['candidate_tree'] == git('rev-parse', C+'^{tree}').decode().strip() == 'b97a557a2310f0e414467c81edb5984be0f1133c'
assert git('rev-parse', F+'^{tree}').decode().strip() == '08bd0f362c74ef7645b5bbd70b557489c122ae29'
check(contract_path.read_bytes(), freeze['original_contract_commit_path_identity'])
frozen_files = []
for name in ['candidate-input.json','candidate-restore/R7-U12.json','mirror-diffs.patch','remote-readback.json']:
    data = (BOOT/name).read_bytes()
    assert data == git('show', F+':'+PREFIX+name)
    frozen_files.append({'commit': F, 'path': PREFIX+name, **ident(data)})
assert (BOOT/'reviewer-dispatch.md').read_bytes() == git('show', D+':'+PREFIX+'reviewer-dispatch.md')
frozen_files.append({'commit': D, 'path': PREFIX+'reviewer-dispatch.md', **ident((BOOT/'reviewer-dispatch.md').read_bytes())})

entries = freeze['candidate_and_author_evidence_file_identities']
diff = [dict(zip(['status','path'], s.split('\t',1))) for s in git('diff','--name-status',B,C).decode().splitlines()]
assert diff == freeze['complete_diff_against_B']
assert len(diff) == len(entries) == 104
assert all(r['status']=='A' and r['path'].startswith('candidates/R7-U12/') for r in diff)
tree = {}
for line in git('ls-tree','-r',C,'candidates/R7-U12').decode().splitlines():
    head, path = line.split('\t'); mode, typ, blob = head.split()
    tree[path] = {'git_mode':mode,'type':typ,'git_blob':blob}
verified = []
for row in entries:
    actual = check((IN/'candidate'/row['path']).read_bytes(),row)
    assert tree[row['path']] == {'git_mode':'100644','type':'blob','git_blob':actual['git_blob']}
    verified.append({'path': row['path'], **actual, **tree[row['path']], 'role': row['role']})
assert sum(r['bytes'] for r in verified) == 1292206
assert len([r for r in verified if r['role']=='candidate_mirror']) == 6
manifest = json.loads((CAN/'evidence/author/artifact-manifest.json').read_text())
for row in manifest['all_new_commit_files_except_self']:
    check((IN/'candidate'/row['path']).read_bytes(),row['new'])
assert len(manifest['all_new_commit_files_except_self']) == 103
save('candidate-byte-audit.json', {'stage':'TOOL_VALIDATION','candidate_commit':C,'candidate_tree':freeze['candidate_tree'],
    'dispatch_commit':D,'freeze_commit':F,'fixed_file_bindings':frozen_files,'complete_diff_against_B':diff,
    'files':verified,'files_verified':len(verified),'bytes_verified':sum(r['bytes'] for r in verified),
    'author_manifest_nonself_declarations_verified':103,'manifest_self_binding':'Actual candidate commit/tree and exhaustive 104 file table; no recursive self hash',
    'effective_configuration':'UNVERIFIED','behavior_execution':'NOT_EXECUTED'})

plan = json.loads(Path('/workspace/r7-bootstrap/R7-U12-reviewer/recovery/batches/R7-U12.json').read_text())
restored = []
for row in plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']:
    restored.append({'local_path':row['local_path'],**check((CTX/row['local_path']).read_bytes(),row)})
assert len(restored)==26 and sum(r['bytes'] for r in restored)==7587353
save('original-input-recheck.json',{'stage':'TOOL_VALIDATION','files':restored,'count':len(restored),'bytes':sum(r['bytes'] for r in restored)})

# Check every explicit original raw slice referenced by the seven-group contract.
refs = {}
def walk(o):
    if isinstance(o,dict):
        if 'raw_member_byte_offsets' in o and 'input_sha256' in o:
            refs[(o['input_sha256'],tuple(o['raw_member_byte_offsets']))]=o
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk(contract)
rawroot=CTX/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs'
slice_results=[]
for (sha,(a,z)),row in refs.items():
    raw=(rawroot/(sha+'.raw')).read_bytes()[a:z]
    assert len(raw)==row['raw_member_bytes'] and hashlib.sha256(raw).hexdigest()==row['raw_member_sha256']
    doc=json.loads((rawroot/(sha+'.raw')).read_text())
    for part in row['json_pointer'].strip('/').split('/'):
        part=part.replace('~1','/').replace('~0','~')
        doc=doc[int(part)] if isinstance(doc,list) else doc[part]
    assert json.loads(raw)==doc
    slice_results.append({'binding_id':row['binding_id'],'pointer':row['json_pointer'],'input_sha256':sha,
                          'byte_offsets':[a,z],'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'pointer_object_matches':True})
save('original-raw-bindings.json',{'stage':'TOOL_VALIDATION','all_explicit_contract_slices':slice_results,'count':len(slice_results)})

paths=set(git('ls-tree','-r','--name-only',B).decode().splitlines())
dirs={str(Path(p).parent) for p in paths}
for p in list(dirs): dirs.update(str(a) for a in Path(p).parents)
universe=paths|dirs
three=['deliverables/final-specification-set/README.md','deliverables/final-specification-set/scope-statement.md','deliverables/final-specification-set/test-catalog/README.md']
historic='review/remediation/20261003-prepare/batches/B21/author-draft-1/'
rawprefix=f'https://raw.githubusercontent.com/y805939188/pokemon-essentials-clean-room/{H}/'
pattern=re.compile(r'\[[^\]\n]*\]\(([^)\n]+)\)')
def destinations(text,path):
    rows=[]
    for m in pattern.finditer(text):
        href=m.group(1)
        if href.startswith('#') or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',href): continue
        resolved=posixpath.normpath(posixpath.join(posixpath.dirname(path),urllib.parse.unquote(href.split('#')[0])))
        rows.append({'href':href,'resolved':resolved,'exists_in_B':resolved.rstrip('/') in universe,'line':text.count('\n',0,m.start())+1})
    return rows
nav=[]; allmissing=[]; newhrefs=[]; reverse=[]
for path in three:
    base=git('show',B+':'+path).decode(); new=(CAN/path).read_text()
    before=destinations(base,path); after=destinations(new,path)
    missing=[r for r in before if not r['exists_in_B']]
    assert len(missing)==(4 if 'test-catalog' in path else 3)
    assert all(r['resolved'].startswith(historic) for r in missing)
    assert all(r['exists_in_B'] for r in after)
    assert [r['href'] for r in before if r['exists_in_B']]==[r['href'] for r in after]
    external=[m.group(1) for m in pattern.finditer(new) if m.group(1).startswith(rawprefix)]
    assert len(external)==len(missing)
    assert collections.Counter(external)==collections.Counter(rawprefix+r['resolved'] for r in missing)
    lines=new.splitlines(keepends=True)
    notes=[s for s in lines if s.startswith('GR7-M19-001 历史导航勘误：')]
    assert len(notes)==1 and '缺少对象或档案时该检索仍不可用' in notes[0]
    reverted=new.replace('\n'+notes[0],'')
    for r in missing: reverted=reverted.replace(rawprefix+r['resolved'],r['href'])
    assert reverted==base
    reverse.append({'path':path,'baseline':ident(base.encode()),'candidate':ident(new.encode()),'all_other_bytes_restored_exactly':True})
    nav.append({'path':path,'B_local_inline_count':len(before),'B_resolved':len(before)-len(missing),'B_missing':missing,
                'candidate_local_inline_count':len(after),'candidate_all_local_resolve':True,'immutable_hrefs':external})
    allmissing+=missing;newhrefs+=external
assert sum(r['B_local_inline_count'] for r in nav)==136
assert len(allmissing)==10 and len(set(r['resolved'] for r in allmissing))==4
assert sum(r['candidate_local_inline_count'] for r in nav)==126
assert 'deliverables/final-specification-set/user-interface' in dirs
catalog=(CAN/three[2]).read_text()
family_links=[r for r in destinations(catalog,three[2]) if '/' not in r['href'] and r['href'].endswith('.md')]
# Keep original table and its ordering; the 17 family destinations are local existing files.
family_unique=list(dict.fromkeys(r['resolved'] for r in family_links))
assert len(family_unique)==17
historical=[]
for path in sorted({r['resolved'] for r in allmissing}):
    row=next(r for r in plan['fixed_read_inputs'] if r['path']==path and r['commit']==H)
    data=(CTX/row['local_path']).read_bytes();check(data,row)
    assert path not in paths and not (REPO/path).exists()
    content=data.decode()
    historical.append({'commit':H,'path':path,**ident(data),'json_top_keys':list(json.loads(content)) if path.endswith('.json') else None,
                       'qualification':'Full bytes acquired via pinned HTTP; navigation suitability only; not historical semantic approval'})
controls=[]
for path in ['README.md','CURRENT-DELIVERY.md','delivery/2026-10-14-sixth/README.md']:
    text=git('show',B+':'+path).decode()
    rows=destinations(text,path)
    controls.append({'path':path,'selected_first_15_line_links':[r for r in rows if r['line']<=15]})
    assert all(r['exists_in_B'] for r in rows if r['line']<=15)
save('navigation-regression.json',{'stage':'TOOL_VALIDATION','scope':'Only three named documents inline destinations, B paths including directories, four immutable historical targets; no browser/anchors/full131 link audit',
    'documents':nav,'reversal':reverse,'B_totals':{'local_inline':136,'resolved':126,'missing_occurrences':10,'unique_missing_targets':4},
    'candidate_totals':{'local_inline':126,'resolved':126,'immutable_history_occurrences':10},
    'directory_control':'user-interface/ exists as Git directory; original 11/5 was an unsuccessful historical attempt',
    'family_links_order':family_unique,'ordinary_controls':controls,'historical_targets':historical})

# Current projections: exactly one old/new row apiece, historical status columns unchanged.
projection=[]
for path,line in [('planning/feature-matrix.md',553),('audit/source-traceability.md',1828)]:
    base=git('show',B+':'+path).decode().splitlines(keepends=True); new=(CAN/path).read_text().splitlines(keepends=True)
    assert len(base)==len(new)
    changed=[i+1 for i,(a,b) in enumerate(zip(base,new)) if a!=b]
    assert changed==[line]
    assert 'R6-DX-DEBUG-001' in new[line-1] and 'WP72 §5.3／WP27' in new[line-1]
    assert base[line-1].split('|')[-2]==new[line-1].split('|')[-2]
    assert new[line-1].replace('WP72 §5.3／WP27（当前导航勘误：[GR7-H08-001](../review/remediation-seventh-20261015-prepare/current-navigation-errata.json)）','WP72 §5.2／WP27')==base[line-1]
    projection.append({'path':path,'only_changed_line':line,'before':base[line-1].strip(),'after':new[line-1].strip(),'status_column_unchanged':True})
errpath='review/remediation-seventh-20261015-prepare/current-navigation-errata.json'
err=json.loads((CAN/errpath).read_text())
assert err['record_id']=='GR7-H08-001' and err['subject_id']=='R6-DX-DEBUG-001'
assert err['old_label']=='WP72 §5.2／WP27' and err['current_label']=='WP72 §5.3／WP27'
orig=err['frozen_original']; check(git('show',B+':'+orig['path']),orig)
sync=json.loads(git('show',B+':'+orig['path']))
assert sync['items'][42]['id']=='R6-DX-DEBUG-001' and sync['items'][42]['actual_clause_label']==err['old_label']
check(git('show',B+':'+orig['contract_path']),orig['contract_identity'])
clause=err['current_clause']; data=git('show',B+':'+clause['path']);check(data,clause)
lines=data.splitlines(keepends=True)
assert lines[111].decode().startswith('### 5.2') and lines[121].decode().startswith('### 5.3')
assert '加道具' in lines[123].decode();check(lines[123],clause['rule_line_identity_including_LF'])
for row in err['fixed_source']['locators']:check((CTX/'inputs/reference'/row['path']).read_bytes(),row)
preserved=[]
for path in ['deliverables/final-specification-set','review/remediation-sixth-20261014-prepare']:
    bt=git('rev-parse',B+':'+path).decode().strip(); ct=git('rev-parse',C+':'+path).decode().strip()
    assert bt==ct;preserved.append({'path':path,'B_tree':bt,'candidate_commit_tree':ct,'identical':True})
assert len(git('ls-tree','-r','--name-only',B,'deliverables/final-specification-set').decode().splitlines())==131
save('current-navigation-regression.json',{'stage':'TOOL_VALIDATION','projection_changes':projection,'new_errata':ident((CAN/errpath).read_bytes()),
    'old_sync_item42_id':sync['items'][42]['id'],'old_sync_item42_label':sync['items'][42]['actual_clause_label'],
    'current_WP72_clause_identity':clause,'source_identity_fields_match':True,'frozen_contract_identity_match':True,
    'unchanged_actual_subtrees':preserved,'formal_files':131,'optional_or_policy_adopted':False,
    'behavior_vectors':'NOT_EXECUTED','candidate_scope_only':True})

context={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'actual_reviewer_thread_id':os.environ.get('CODEX_THREAD_ID'),'actual_session_id':os.environ.get('CODEX_SESSION_ID'),
    'caas_session_id':os.environ.get('CODEX_CAAS_SESSION_ID'),'delegating_source_thread_id':'01a13f49-a154-7054-9b04-ce31f924d01c',
    'identity_evidence':'Actual environment variables returned by this audit subprocess; not inferred from role or shell PID',
    'author_parent_supplied_task_id':freeze['author_task_id'],'author_internal_context':'UNVERIFIED/not exposed in author actual-context.json; original qualification preserved',
    'independence':os.environ.get('CODEX_THREAD_ID')!=freeze['author_task_id'],
    'requested':{'model':'gpt-6.1-sol','effort':'ultra','service_tier':'default','speed':'ordinary, Fast forbidden'},
    'effective':{'model':'UNVERIFIED','effort':'UNVERIFIED','service_tier':'UNVERIFIED','speed':'UNVERIFIED'},
    'model_pid':'NOT_EXPOSED','audit_pid':os.getpid(),'subagents_started':0,
    'skills':'No project .agents/skills entries in B or fixed dispatch commit; /workspace/.agents is empty; no applicable local skill was available',
    'initial_logging_gap':'Interactive reconnaissance, downloads, Git fetches and content reads (including later interactive reads) are in platform tool I/O, and the first two restorations have native receipts, but those commands are not individually wrapped with separate UTC/stdout/stderr files. Only commands explicitly recorded under logs/ have separated local I/O. No retroactive timestamps or fabricated logs; logged rechecks are new actual commands.',
    'git_transport':'First two unfiltered fetches were interrupted by this task due to large transfer; filtered fixed-commit fetch succeeded; temporary packs are not review artifacts',
    'new_reference_complete_model_host_Demo_native_media_real_save_replay':0,'L01_L14':'RETAINED'}
assert context['independence'] and context['actual_reviewer_thread_id']
save('actual-context.json',context)
print(json.dumps({'status':'INDEPENDENT_TOOL_CHECKS_PASSED','candidate_files':104,'candidate_bytes':1292206,'original_files':26,
    'raw_slices':len(slice_results),'navigation':'136 B inline local /126 resolve /10 missing /4 targets; candidate126 local resolve and10 pinned historical URLs',
    'projection_lines':[553,1828],'stage':'TOOL_VALIDATION_ONLY','semantic_verdict':'Reviewer report separately required','behavior_execution':'NOT_EXECUTED'},ensure_ascii=False))
