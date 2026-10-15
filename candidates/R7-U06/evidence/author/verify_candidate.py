"""Identity, binding, scope and document preservation audit; no behavior engine."""
from pathlib import Path
import datetime
import difflib
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
CONTEXT = Path('/workspace/r7-context/R7-U06-author')
BOOT = Path('/workspace/r7-bootstrap/R7-U06-author')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())
def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)
def write(name, obj):
    (HERE/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

contract = json.loads((BOOT/'delegation/contracts/R7-U06.json').read_bytes())
plan = json.loads((BOOT/'recovery/batches/R7-U06.json').read_bytes())
verified=[]
for row in plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']+json.loads((HERE/'supplemental-plan.json').read_bytes()):
    actual=identity((CONTEXT/row['local_path']).read_bytes())
    assert all(actual[k]==row[k] for k in actual), row['local_path']
    if row in plan['fixed_read_inputs'] and row['repository'].endswith('clean-room'):
        assert identity(git('show',B+':'+row['path']))==actual
    verified.append(dict(local_path=row['local_path'], **actual))
write('restored-identities.json', {'stage':'TOOL_VALIDATION', 'files':verified,
    'count':len(verified),'bytes':sum(r['bytes'] for r in verified), 'semantic_credit':False})

rawdir=CONTEXT/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/evidence/inputs'
normalized=json.loads((CONTEXT/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_bytes())
refs=[]
def walk(obj):
    if isinstance(obj,dict):
        if all(k in obj for k in ['input_sha256','raw_member_byte_offsets','raw_member_sha256','canonical_sha256','json_pointer']):
            sha=obj['input_sha256']; data=(rawdir/(sha+'.raw')).read_bytes()
            assert hashlib.sha256(data).hexdigest()==sha
            a,b=obj['raw_member_byte_offsets']; member=data[a:b]
            assert len(member)==obj['raw_member_bytes']
            assert hashlib.sha256(member).hexdigest()==obj['raw_member_sha256']
            value=json.loads(data)
            for part in obj['json_pointer'].split('/')[1:]:
                part=part.replace('~1','/').replace('~0','~')
                value=value[int(part)] if isinstance(value,list) else value[part]
            canonical=json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()
            assert hashlib.sha256(canonical).hexdigest()==obj['canonical_sha256'],obj['json_pointer']
            refs.append(obj)
        for v in obj.values():walk(v)
    elif isinstance(obj,list):
        for v in obj:walk(v)
walk(contract)
for i in [12,13]:walk(normalized['records'][i]['groups'])
write('binding-verification.json',{'stage':'TOOL_VALIDATION','references_checked_including_repeats':len(refs),
    'references':refs,'qualification':'Raw bytes/pointers/canonical identity only; no semantic acceptance.'})

formal=[]; patch=''; scope=[]; table_ids={}
for row in contract['paths']:
    p=ROOT/row['candidate_path']; old=git('show',B+':'+row['path'])
    if row['classification']!='required':
        assert not p.exists()
        continue
    new=p.read_bytes(); a=old.decode().splitlines(keepends=True); b=new.decode().splitlines(keepends=True)
    operations=[op for op in difflib.SequenceMatcher(a=a,b=b,autojunk=False).get_opcodes() if op[0]!='equal']
    if 'wp46-damage-multihit' in row['path']:
        changed=[i+1 for tag,i,j,k,l in operations for i in range(i,j)]
        assert changed==[23,54,59], changed
        assert all(tag=='replace' and j-i==l-k==1 for tag,i,j,k,l in operations)
    else:
        assert len(operations)==1 and operations[0][0]=='insert', operations
        # All original text, table identities and ordering survive byte-for-byte.
        _,i,j,k,l=operations[0]
        assert b[:k]+b[l:]==a
    if '/test-catalog/' in row['path']:
        added=[line.strip().split('|')[1].strip() for tag,i,j,k,l in operations for line in b[k:l]
               if line.startswith('| ') and not line.startswith('| ID ') and not line.startswith('| ---')]
        assert len(added)==len(set(added))==15
        table_ids[row['path']]=added
    formal.append(dict(original_path=row['path'], candidate_path=row['candidate_path'],
                       original_B=identity(old), candidate=identity(new)))
    scope.append(dict(path=row['path'],opcodes=operations))
    patch+=''.join(difflib.unified_diff(a,b,fromfile='B/'+row['path'],tofile=row['candidate_path'],n=0))
(HERE/'changes.patch').write_text(patch)
wp46=ROOT/'candidates/R7-U06/deliverables/final-specification-set/pokemon-rules/wp46-damage-multihit-and-healing.md'
wp49=ROOT/'candidates/R7-U06/deliverables/final-specification-set/combat-requirements/wp49-ability-phase-triggers.md'
assert '#611-蒸汽机的直接每击速度请求' in wp46.read_text()
assert '### 6.1.1 蒸汽机的直接每击速度请求' in wp49.read_text()
assert git('branch','--show-current').decode().strip()=='codex/r7-u06-author-20261015-wave1'
assert git('rev-parse','HEAD').decode().strip()==B
assert all(p.startswith('candidates/R7-U06/') for p in git('diff','--name-only',B).decode().splitlines())
untracked=git('ls-files','--others','--exclude-standard').decode().splitlines()
assert all(p.startswith('candidates/R7-U06/') for p in untracked)
write('scope-validation.json',{'stage':'TOOL_VALIDATION', 'result':'CHECKS_COMPLETED',
    'formal_mirrors':formal,'scope':scope,'new_vector_ids':table_ids,
    'conditional_WP43':'NOT_WRITTEN_NO_CONTRADICTION', 'all_original_catalog_rows':'BYTE_PRESERVED',
    'branch':'codex/r7-u06-author-20261015-wave1', 'reference_execution':0,
    'independent_review':'NOT_PERFORMED_BY_AUTHOR', 'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
print(json.dumps({'restored_files':len(verified),'restored_bytes':sum(r['bytes'] for r in verified),
    'binding_references_checked':len(refs),'complete_mirrors':len(formal),'added_static_vectors':sum(map(len,table_ids.values())),
    'original_text_scope':'WP46 only original lines 23/54/59 replaced; other three files insert only',
    'behavior_vectors':'NOT_EXECUTED','result':'TOOL_VALIDATION_COMPLETED'},ensure_ascii=False))
