"""Verify transport, frozen input identity, and exact JSON member bindings only."""
import datetime
import gzip
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BOOT = Path('/workspace/r7-bootstrap/R7-U03-author')
CTX = Path('/workspace/r7-context/R7-U03-author')
B = 'e646432c644dec04d306842cc5a559a29c718fbc'

def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob_content_id=hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest())

def write(name, value):
    (HERE/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

plan = json.loads((BOOT/'recovery/batches/R7-U03.json').read_bytes())
contract = json.loads((BOOT/'delegation/contracts/R7-U03.json').read_bytes())
rows = plan['artifacts']+plan['evidence']+plan['fixed_read_inputs']
verified = []
for row in rows:
    actual = identity((CTX/row['local_path']).read_bytes())
    for key, value in actual.items():
        assert value == row[key], (row['local_path'], key)
    if row in plan['fixed_read_inputs'] and row['repository'].endswith('clean-room'):
        assert subprocess.check_output(['git', 'show', B+':'+row['path']], cwd=ROOT) == (CTX/row['local_path']).read_bytes()
    verified.append(dict(local_path=row['local_path'], immutable_commit=row['commit'],
                         immutable_path=row['path'], **actual))

bindings = json.loads((CTX/'evidence/tasks/R7-C13/raw-binding-manifest.json').read_bytes())
bindings = {r['binding_id']: r for r in bindings}
members = {}
supplemental_members = {}

def pointer(obj, path):
    for part in path.split('/')[1:]:
        part = part.replace('~1', '/').replace('~0', '~')
        obj = obj[int(part)] if isinstance(obj, list) else obj[part]
    return obj

def inspect(obj):
    if isinstance(obj, dict):
        if all(k in obj for k in ['binding_id', 'json_pointer', 'raw_member_byte_offsets', 'raw_member_sha256']):
            key = obj['binding_id']+obj['json_pointer']
            if key not in members:
                row = bindings[obj['binding_id']]
                path = CTX/'evidence/tasks/R7-C13'/row['c13_snapshot']
                if not path.exists():
                    sha = row['sha256']
                    path = BOOT/'supplemental'/(sha+'.raw')
                    transport_path = ('review/global-independent-review/seventh-2026-10-14-e646432-7a91/'
                                      'publication-transport/core/objects/'+sha[:2]+'/'+sha+'.gz')
                    if not path.exists():
                        encoded = subprocess.check_output(['git', 'show', '4580645dfbfec4a3c7ccbad56ae293cc619b0d25:'+transport_path], cwd=ROOT)
                        with gzip.GzipFile(fileobj=io.BytesIO(encoded)) as stream:
                            decoded = stream.read(row['bytes']+1)
                        assert identity(decoded) == dict(bytes=row['bytes'], sha256=sha, git_blob_content_id=row['content_git_blob'])
                        path.write_bytes(decoded)
                    actual = identity(path.read_bytes())
                    assert actual == dict(bytes=row['bytes'], sha256=sha, git_blob_content_id=row['content_git_blob'])
                    supplemental_members[sha] = dict(binding_id=row['binding_id'], logical_path=row['report_relative_path'],
                        fixed_publication_commit='4580645dfbfec4a3c7ccbad56ae293cc619b0d25', transport_path=transport_path, **actual,
                        qualification='Targeted concrete JSON binding supplement; no whole-index scan, no execution.')
                data = path.read_bytes()
                assert identity(data)['sha256'] == obj['input_sha256']
                start, end = obj['raw_member_byte_offsets']
                fragment = data[start:end]
                assert len(fragment) == obj['raw_member_bytes']
                assert hashlib.sha256(fragment).hexdigest() == obj['raw_member_sha256']
                value = pointer(json.loads(data), obj['json_pointer'])
                assert json.loads(fragment) == value
                canonical = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
                assert hashlib.sha256(canonical).hexdigest() == obj['canonical_sha256']
                members[key] = {**obj, 'offset_bytes_sha_pointer_and_canonical_match': True}
        for value in obj.values():
            inspect(value)
    elif isinstance(obj, list):
        for value in obj:
            inspect(value)

inspect(contract)
normalized = json.loads((CTX/'evidence/tasks/R7-C13/inputs/tasks/R7-P02/normalized-record-candidates.json').read_bytes())
for i in [6, 7]:
    inspect(normalized['records'][i])
read_set = []
for record in contract['original_full_contracts']:
    for item in record['complete_seven_groups']['六_依赖接收_精确读写集']['读取义务']['items']:
        read_set.append(dict(record_id=record['record_id'], **item,
            reading='CONTENT_INSPECTED_IN_THIS_AUTHOR_CONTEXT; SOURCE_STATIC/CONTRACT_TEXT',
            semantic_independent_acceptance=False))

supplement = BOOT/'supplemental/proposal-successor-deltas-C04-C06.json'
assert identity(supplement.read_bytes())['sha256'] == '96ced6f8253d991b19b72617b4cd74c29343ef4af1b9e6067cf9787568ea4473'
supplement_receipt = dict(logical_path='evidence/proposal-successor-deltas-C04-C06.json',
    publication_commit='4580645dfbfec4a3c7ccbad56ae293cc619b0d25',
    transport_path='review/global-independent-review/seventh-2026-10-14-e646432-7a91/publication-transport/core/objects/96/96ced6f8253d991b19b72617b4cd74c29343ef4af1b9e6067cf9787568ea4473.gz',
    recovery='git show fixed C2 object; bounded identity confirmed after gzip decode; not executed',
    **identity(supplement.read_bytes()), content_inspected=True)
history = 'review/global-independent-review/third-2026-10-12-86b4d7e-manual-a731/M03/spec-coverage.tsv'
history_data = subprocess.check_output(['git', 'show', B+':'+history], cwd=ROOT)
extras = [dict(repository='project', commit=B, path=history, lines=[1320,1320], **identity(history_data),
               purpose='WR01 residual relation only; no inherited PASS'),
          dict(repository='project', commit=B, path='deliverables/final-specification-set/engine-overworld/wp13-move-route-matrix.md', lines=[1,80], purpose='MR02/WAIT preserved'),
          dict(repository='reference', commit=plan['fixed_read_inputs'][1]['commit'], path='Data/Scripts/004_Game classes/006_Game_Character.rb', lines=[427,576], purpose='legal route/WAIT plus nonplayer blocked branch'),
          dict(repository='reference', commit=plan['fixed_read_inputs'][1]['commit'], path='Data/Scripts/004_Game classes/006_Game_Character.rb', lines=[703,825], purpose='adjacent movement/jump context'),
          dict(repository='reference', commit=plan['fixed_read_inputs'][1]['commit'], path='Data/Scripts/001_Settings.rb', lines=[1,45], purpose='default generation 8'),
          dict(repository='reference', commit=plan['fixed_read_inputs'][1]['commit'], path='Data/Scripts/004_Game classes/004_Game_Map.rb', lines=[323,394], purpose='inflight scroll task identity'),
          dict(repository='reference', commit=plan['fixed_read_inputs'][1]['commit'], path='Data/Scripts/004_Game classes/004_Game_Map.rb', lines=[439,460], purpose='inflight scroll update/nominal time')]
write('input-verification.json', dict(stage='TOOL_VALIDATION', utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    files_verified=len(verified), bytes_verified=sum(r['bytes'] for r in verified), files=verified,
    raw_member_bindings_verified=len(members), members=list(members.values()), supplement=supplement_receipt,
    targeted_supplemental_inputs=list(supplemental_members.values()),
    qualification='Byte identity and JSON membership only. Not reference execution or semantic PASS.'))
write('read-set.json', dict(contract_full_text=identity((BOOT/'delegation/contracts/R7-U03.json').read_bytes()),
    dispatch_full_text=identity((BOOT/'delegation/parallel-dispatch/authors/R7-U03-author.md').read_bytes()),
    fixed_contract_commit=plan['contract_commit'], dispatch_commit='6ec1d09e9c470954964d72761c83a760ef4f0364',
    required_read_set=read_set, additional_content_reads=extras,
    nonauthor_full_records=['p02-a5219234b1c90482616c#/records/3','p02-a5219234b1c90482616c#/records/4'],
    original_proposals=['p02-f02ac5179f6eff79e20e#/records/6/original_proposal','p02-f02ac5179f6eff79e20e#/records/7/original_proposal'],
    limits='tasks/R7-C17/limits-and-alias-reception.json full L01-L14 retained',
    skills=dict(status='NOT_PRESENT_IN_SELECTED_CONTAINER_OR_FIXED_GIT_TREE',
                checked=['/workspace/.agents', '/workspace/pokemon-essentials-clean-room/.agents', 'git ls-tree -r 6ec1d09e9c470954964d72761c83a760ef4f0364'],
                AGENTS_md='READ_FULL; identity in input-verification.json'),
    source_text_publication='No reference source copied into candidate evidence; immutable locators/ranges/identity published instead. Content tool output stays in platform transcript.',
    early_local_log_qualification='Initial reconnaissance and content reads used platform exec tool output; separate per-read UTC/stdout/stderr files were not captured. No retroactive timestamps or run claims. Later validation/publication commands have separated logs.'))
for receipt in CTX.glob('recovery-receipt-*.json'):
    shutil.copyfile(receipt, HERE/receipt.name)
print(json.dumps(dict(result='INPUT_IDENTITIES_AND_MEMBER_BINDINGS_VERIFIED', files=len(verified), bytes=sum(r['bytes'] for r in verified), member_bindings=len(members), semantic_PASS=False)))
