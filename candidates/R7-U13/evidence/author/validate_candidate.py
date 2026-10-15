"""Check fixed identities, exact edit boundaries and preserved historical bytes.

This is document/transport tooling, not a behavior model or reference execution.
"""
import datetime
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[4]
E=Path(__file__).parent
B='e646432c644dec04d306842cc5a559a29c718fbc'
PREFIX='candidates/R7-U13/'

def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT)

def identity(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob_content_id':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

manifest=json.loads((E/'artifact-manifest.json').read_text())
assert len(manifest['artifacts'])==4
assert git('branch','--show-current').decode().strip()=='codex/r7-u13-author-20261015-wave1'
subprocess.run(['git','merge-base','--is-ancestor',B,'HEAD'],cwd=ROOT,check=True)
assert git('rev-parse',B+':deliverables/final-specification-set').decode().strip()==manifest['base_formal_tree']
checks=[]
allowed={
 'audit/source-traceability.md':[(313,326)],
 'deliverables/final-specification-set/engine-overworld/wp15-resource-matching-and-audio.md':[(191,196),(212,214)],
 'deliverables/final-specification-set/test-catalog/engine-overworld-wp11-15-59-60.md':[(400,436)],
 'planning/feature-matrix.md':[(174,174)]
}
for row in manifest['artifacts']:
    path=row['original_path'];old=git('show',B+':'+path);new=(ROOT/row['candidate_path']).read_bytes()
    assert identity(old)==row['base']
    assert identity(new)==row['candidate']
    assert (ROOT/path).read_bytes()==old,'formal file changed: '+path
    assert row['candidate_path']==PREFIX+path
    before=old.decode().splitlines(True);after=new.decode().splitlines(True)
    ops=[]
    for tag,a,b,c,d in difflib.SequenceMatcher(None,before,after,autojunk=False).get_opcodes():
        if tag=='equal':continue
        assert tag=='insert' or (path=='planning/feature-matrix.md' and tag=='replace' and b-a==d-c==1)
        base_line=a+1
        assert any(lo<=base_line<=hi and (tag=='insert' or b<=hi) for lo,hi in allowed[path]),(path,tag,a,b)
        ops.append({'operation':tag,'base_start_line':base_line,'base_end_exclusive_line':b+1,'candidate_start_line':c+1,'candidate_end_exclusive_line':d+1})
    assert ops
    if path.endswith('/engine-overworld-wp11-15-59-60.md'):
        historical_before=[s for s in before if re.match(r'^\| B04-R\d+ \|',s)]
        historical_after=[s for s in after if re.match(r'^\| B04-R\d+ \|',s)]
        assert historical_before==historical_after and len(historical_after)==28
        assert sum(s.startswith('| GR7-D07-001-S01 |') for s in after)==1
    if path.endswith('/wp15-resource-matching-and-audio.md'):
        assert old.decode().split('## 6. 音频行为')[1].split('## 7. 默认行为')[0]==new.decode().split('## 6. 音频行为')[1].split('## 7. 默认行为')[0]
        assert old.decode().split('## 11. 未决与未验证')[1]==new.decode().split('## 11. 未决与未验证')[1]
    if path=='planning/feature-matrix.md':
        old_line=next(s for s in before if s.startswith('| F05-02 |')).split('|')
        new_line=next(s for s in after if s.startswith('| F05-02 |')).split('|')
        assert [s for i,s in enumerate(old_line) if i not in [7,9]]==[s for i,s in enumerate(new_line) if i not in [7,9]]
        assert 'Pending（GR7-D07-001' in new_line[7]
    assert b'soundfont.sf2' in new
    checks.append({'path':path,'base_and_candidate_identity':'MATCH','formal_file':'UNCHANGED','scope_opcodes':ops})

per=json.loads((E/'per-id.json').read_text())['records'][0]
assert per['author_status']=='CANDIDATE_READY_NOT_REVIEWED'
assert per['root_status_preserved']=='REQUIRED_OPEN_FOR_MANUAL_UPDATE'
assert len(per['vectors'])==15
assert all(v['behavior_result']=='NOT_EXECUTED' for v in per['vectors'])
assert {v['id'] for v in per['vectors']}=={f'C11-V{i:02}' for i in range(1,9)}|{f'D07-SF-CFG-{i:02}' for i in range(1,7)}|{'GR7-D07-001-S01'}
C=Path('/workspace/r7-context/R7-U13-author')
expected=(json.loads((C/'evidence/tasks/R7-C13/inputs/evidence/received-final-proposals/GR7-D07-001/counter-review.json').read_text())['findings'][0]['regression_vectors']+
          json.loads((C/'evidence/tasks/R7-D07/findings.json').read_text())['findings'][0]['regression_vectors'])
for old in expected:
    new=next(x for x in per['vectors'] if x['id']==old['id'])
    assert all(new[k]==v for k,v in old.items()),old['id']
assert all(x['status']=='OPEN' for x in per['open_dependencies'])
assert all(per['execution'][k]==0 for k in ['REFERENCE_OBSERVATION','independent_full_behavior_model','game_host','Demo','native_media','synthesis','sound','real_save_replay'])

reads=json.loads((E/'read-set.json').read_text())
for row in reads['reads']:
    if 'path' in row:
        data=Path(row['path']).read_bytes()
        assert all(identity(data)[k]==row[k] for k in identity(data))
tracked=git('diff','--name-only',B).decode().splitlines()
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
assert all(path.startswith(PREFIX) for path in tracked+untracked),(tracked,untracked)
allowed_files={row['candidate_path'] for row in manifest['artifacts']}
all_candidate_files=[str(p.relative_to(ROOT)) for p in (ROOT/PREFIX).rglob('*') if p.is_file()]
assert all(p in allowed_files or p.startswith(PREFIX+'evidence/author/') for p in all_candidate_files)
assert not any('__pycache__' in p for p in all_candidate_files)
for p in E.glob('*.json'):json.loads(p.read_text())
for line in (E/'commands.jsonl').read_text().splitlines():json.loads(line)
context=json.loads((E/'execution-context.json').read_text())
assert all(v=='UNVERIFIED' for v in context['effective_configuration'].values())
assert context['actual_thread_id']=='01a13f80-5248-7789-ab67-26ce7270c019'
receipts=[json.loads(p.read_text()) for p in E.glob('recovery-receipt-*.json')]
assert len(receipts)==2 and all(x['files_verified']==21 and x['bytes_verified']==16814642 for x in receipts)
assert all(x['status']=='BOUNDED_RESTORE_BYTES_VERIFIED' for x in receipts)
latest=max(receipts,key=lambda x:x['end_utc'])
assert all(x['status']=='REUSED_EXACT_BYTES' for x in latest['files'])
report={'schema':'r7-u13-author-tool-validation.v1','observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'result':'TOOL_CHECKS_OK','qualification':'Author document integrity checks only; no independent semantic PASS, acceptance or closure.',
 'mirror_checks':checks,'historical_B04_rows_preserved':28,'original_vectors_preserved':14,'new_catalog_vectors':1,'all_behavior_vectors':'NOT_EXECUTED',
 'fixed_inputs_unchanged':True,'only_authorized_write_paths':True,'all_formal_files_unchanged':True,
 'effective_configuration':'UNVERIFIED','game_host_Demo_native_media_real_save_replay':0,'candidate_files':len(all_candidate_files)}
if '--stdout-only' not in sys.argv:
    (E/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
