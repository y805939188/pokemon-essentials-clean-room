"""Audit candidate documents and frozen bytes. Does not execute battle behavior."""
import argparse
import difflib
import hashlib
import json
from pathlib import Path
import re
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[4])
parser.add_argument('--context', type=Path, default=Path('/workspace/r7-context/R7-U04'))
parser.add_argument('--check-manifest', action='store_true')
args = parser.parse_args()
repo = args.repo
author = repo/'candidates/R7-U04/evidence/author'
base = 'e646432c644dec04d306842cc5a559a29c718fbc'
branch = 'codex/r7-u04-author-20261015-pilot1'

def git(*argv):
    return subprocess.check_output(['git',*argv],cwd=repo)

def identity(data):
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()}

def expected(data, row):
    actual = identity(data)
    assert actual['bytes'] == row['bytes']
    assert actual['sha256'] == row['sha256']
    assert actual['git_blob'] == row.get('git_blob_content_id',row.get('git_blob'))

manifest = json.loads((author/'artifact-manifest.json').read_text())
inputs = json.loads((author/'input-identities.json').read_text())
checks = []
assert git('branch','--show-current').decode().strip() == branch
assert git('rev-parse',base+'^{tree}').decode().strip() == inputs['B_root_tree']
assert git('rev-parse',base+':deliverables/final-specification-set').decode().strip() == inputs['B_formal_tree']
assert git('merge-base','--is-ancestor',base,'HEAD') == b''
assert git('diff','--name-only',base,'--','.',':(exclude)candidates/R7-U04') == b''
untracked = git('ls-files','--others','--exclude-standard').decode().splitlines()
assert all(path.startswith('candidates/R7-U04/') for path in untracked), untracked
all_paths = git('diff','--name-only',base).decode().splitlines()+untracked
assert all(path.startswith('candidates/R7-U04/') for path in all_paths)
assert not git('ls-tree','-r','--name-only',base,'--','.agents')
assert not git('ls-tree','-r','--name-only','4bd152023b4bcb3dd5a3654deffe75aeebc40f10','--','.agents')
checks.append('Exact B root/formal tree, branch and candidate-only tracked/untracked scope; no .agents at fixed inputs.')

rows=inputs['restoration_expected_rows']
for row in rows:
    expected((args.context/row['local_path']).read_bytes(),row)
    if 'encoded_identity' in row:
        data=(args.context/'transport'/row['transport_path']).read_bytes()
        assert len(data)==row['encoded_identity']['bytes']
        assert identity(data)['git_blob']==row['encoded_identity']['git_blob_content_id']
for ref in inputs['contract_raw_bindings_rechecked']:
    data=(args.context/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs'/(ref['input_sha256']+'.raw')).read_bytes()
    a,b=ref['raw_member_byte_offsets']
    chunk=data[a:b]
    assert len(chunk)==ref['raw_member_bytes']
    assert hashlib.sha256(chunk).hexdigest()==ref['raw_member_sha256']
    value=json.loads(data)
    for token in ref['json_pointer'].split('/')[1:]:
        token=token.replace('~1','/').replace('~0','~')
        value=value[int(token)] if isinstance(value,list) else value[token]
    canonical=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    assert hashlib.sha256(canonical).hexdigest()==ref['canonical_sha256']
checks.append('29 restored files and all encoded objects rechecked; 12 contract raw/canonical bindings matched.')

assert len(manifest['mirrors'])==3
for row in manifest['mirrors']:
    original=git('show',base+':'+row['original_path'])
    candidate=(repo/row['path']).read_bytes()
    expected(original,row['base_identity'])
    expected(candidate,row['candidate_identity'])
    assert original==(repo/row['original_path']).read_bytes()
    old=original.decode().splitlines()
    new=candidate.decode().splitlines()
    assert original!=candidate
    if 'test-catalog/' in row['original_path']:
        old_rows=[line for line in old if line.startswith('|')]
        new_rows=[line for line in new if line.startswith('|')]
        assert [line for line in new_rows if line in old_rows]==old_rows
        added=[line for line in new_rows if line not in old_rows]
        assert len(added)==12
        assert all(re.match(r'\| (BC-(?:2[6-9]|3[01])|SW-3[0-5]) \|',line) for line in added)
        for tag,count in [('BC',31),('SW',35)]:
            ids=re.findall(r'^\| ('+tag+r'-\d+) \|',candidate.decode(),re.M)
            assert ids==[f'{tag}-{i:02}' for i in range(1,count+1)]
    else:
        allowed = ('- 能力查询与目标辅助：','示例场景25条见 ') if 'wp39-' in row['path'] else ('   - 玩家侧（野生战斗）：','示例场景29条见 ')
        for kind,a,b,c,d in difflib.SequenceMatcher(a=old,b=new,autojunk=False).get_opcodes():
            if kind=='equal': continue
            if kind=='replace':
                assert b-a==1 and d-c==1
                assert old[a].startswith(allowed),old[a]
            elif kind=='insert':
                assert 'wp41-' in row['path'] and a==126
                assert d-c==2
                assert new[c].startswith('- 扫描内的逃跑成功') and new[c+1].startswith('- 取消与失败分开：')
            else: raise AssertionError('Unexpected deletion or scope')
checks.append('All three fixed-B mirrors have exact recorded identities; only allowed clauses/counts changed; every old catalog row preserved in order; 12 new unique vectors.')

per_id=json.loads((author/'per-id.json').read_text())
assert [row['id'] for row in per_id['records']]==['GR7-M03-001','GR7-M03-002']
for record in per_id['records']:
    assert record['status']=='CANDIDATE_READY_NOT_REVIEWED'
    assert record['effective_model_configuration']=='UNVERIFIED'
    assert len(record['vectors'])==6
    for vector in record['vectors']:
        text=(repo/vector['path']).read_text().splitlines()[vector['line']-1]
        assert text.startswith('| '+vector['id']+' |')
        cells=text.split('|')
        assert cells[2].strip()==vector['premise'] and cells[3].strip()==vector['expected']
        assert vector['reference_execution']==vector['behavior_model_execution']=='NOT_EXECUTED'
    for gate in ['candidate_review','integrated_review','formal_acceptance','closure']:
        assert record[gate]=='NOT_REACHED'
for file in author.glob('*.json'):
    json.loads(file.read_text())
for line in (author/'public-command-log.jsonl').read_text().splitlines():
    json.loads(line)
checks.append('Per-ID vectors match candidate row bytes; all execution and review/acceptance/closure gates retain their real qualifications; public JSON parses.')

if args.check_manifest:
    recorded=manifest['evidence_inventory']
    actual=[p for p in author.rglob('*') if p.is_file() and p.name!='artifact-manifest.json']
    assert set(recorded)=={str(p.relative_to(repo)) for p in actual}
    for path, value in recorded.items(): expected((repo/path).read_bytes(),value)
    print(json.dumps({'result':'MANIFEST_BYTES_MATCH','evidence_files':len(actual),'semantic_PASS':False},ensure_ascii=False))
else:
    result={'schema':'r7.u04.author-tool-validation.v1','result':'AUTHOR_MECHANICAL_CHECKS_COMPLETE',
            'checks':checks,'restored_files':len(rows),'restored_bytes':sum(r['bytes'] for r in rows),
            'raw_binding_checks':len(inputs['contract_raw_bindings_rechecked']),
            'mirrors':3,'new_vectors':12,'domain_execution':'NOT_EXECUTED',
            'semantic_PASS':False,'independent_review':'NOT_REACHED','status':'CANDIDATE_READY_NOT_REVIEWED'}
    (author/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
