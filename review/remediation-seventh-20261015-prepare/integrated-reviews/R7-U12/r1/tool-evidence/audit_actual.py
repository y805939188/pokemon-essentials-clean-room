"""Independent fixed-input and clause-assembly audit. No restored code is executed."""
from pathlib import Path
import hashlib
import json
import subprocess
import datetime
import os

BASE = 'e646432c644dec04d306842cc5a559a29c718fbc'
MI = '45c80832a41c1b56dcd7e9d93497758cbb7721de'
FI = '13d76ba61838b13925ba9d41f58a6b047564d926'
ROOT = Path('/workspace/r7-ir-R7-U12')
OUT = Path(__file__).resolve().parent
def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT/'checkout'), *args])
def identity(data):
    return dict(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                git_blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest())
def verify(data, expected):
    ident = identity(data)
    for key, value in expected.items():
        normalized = 'git_blob' if key in ['git_blob_content_id','git_blob'] else key
        if normalized in ident:
            assert ident[normalized] == value, (key, ident[normalized], value)
    return ident
def save(name, value):
    (OUT/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

verified = []
for plan_dir, dest in [('original-plans','original'),('actual-plans','actual-input')]:
    plan = json.loads((ROOT/plan_dir/'R7-U12.json').read_bytes())
    for group in ['artifacts','evidence','fixed_read_inputs']:
        for row in plan[group]:
            data = (ROOT/dest/row['local_path']).read_bytes()
            verified.append(dict(destination=dest, path=row['local_path'],
                                 **verify(data,row), repository=row['repository'],
                                 fixed_commit=row['commit'], remote_path=row['path']))
save('restored-byte-audit.json', dict(files=verified, count=len(verified),
     bytes=sum(r['bytes'] for r in verified), semantic_credit=False))

freeze = json.loads((OUT/'inputs/integrated-input.json').read_bytes())
formal = []
for line in git('ls-tree','-r','-z',MI,'deliverables/final-specification-set').split(b'\0'):
    if not line: continue
    meta,path = line.split(b'\t'); mode,kind,blob = meta.decode().split()
    path=path.decode(); data=git('show',MI+':'+path); before=git('show',BASE+':'+path)
    formal.append(dict(path=path, mode=mode, **identity(data), baseline=identity(before), changed=data!=before))
assert len(formal)==131
assert sum(r['changed'] for r in formal)==26
print('formal identity row example',json.dumps(freeze['all_formal_file_identities'][0],ensure_ascii=False))
by_path={r['path']:r for r in formal}
for row in freeze['all_formal_file_identities']:
    verify(git('show',MI+':'+row['path']),row.get('identity',row))
save('formal-131-identity-table.json',dict(files=formal, all=131, changed=26, unchanged=105,
     tree=git('rev-parse',MI+':deliverables/final-specification-set').decode().strip(), semantic_credit=False))

actual = ROOT/'actual-input'
journal=json.loads((actual/'integration/applied-clauses.json').read_bytes())
clauses=[]
for file in journal['files']:
    path=file['path']
    try: base=git('show',BASE+':'+path)
    except subprocess.CalledProcessError:
        assert path=='review/remediation-seventh-20261015-prepare/current-navigation-errata.json'
        base=b''
    verify(base,file['baseline_identity'])
    lines=base.decode().splitlines(keepends=True)
    result=[]; cursor=0
    hunks=sorted(file['hunks'],key=lambda h:(h['base_line_indices_half_open'][0],h['batch_order']))
    for h in hunks:
        a,b=h['base_line_indices_half_open']
        assert a>=cursor, (path,a,cursor)
        assert ''.join(lines[a:b])==h['removed_text']
        verify(h['removed_text'].encode(),h['removed_identity'])
        verify(h['added_text'].encode(),h['added_identity'])
        result += lines[cursor:a]+[h['added_text']]; cursor=b
        clauses.append(dict(path=path,batch=h['batch_id'],base_lines=[a,b],
                            candidate_commit=h['candidate_commit'],added_identity=h['added_identity']))
        local=actual/('candidate' if h['batch_id']=='R7-U12' else 'shared-candidate')
        local = local/h['candidate_path'] if h['batch_id']=='R7-U12' else local/h['batch_id']/path
        if local.exists():
            ca,cb=h['candidate_line_indices_half_open']
            assert ''.join(local.read_text().splitlines(keepends=True)[ca:cb])==h['added_text']
    result += lines[cursor:]
    assembled=''.join(result).encode()
    verify(assembled,file['assembled_candidate_clauses_identity'])
    change=next((r for r in journal['root_administrative_reception_adjustments'] if r['path']==path),None)
    current=git('show',MI+':'+path)
    if change:
        verify(assembled,change['before_identity']); verify(current,change['after_identity'])
        if 'added_text' in change: assert assembled+change['added_text'].encode()==current
        else:
            old=json.loads(assembled); new=json.loads(current)
            delta={k:dict(before=old[k],after=new[k]) for k in old if old[k]!=new[k]}
            assert set(delta)=={'status','reception'}
            save('root-errata-metadata-delta.json',delta)
    else: assert assembled==current,path
    restored=actual/'actual'/path
    if restored.exists(): assert restored.read_bytes()==current
save('all-56-clauses-audit.json',dict(hunks=clauses,count=len(clauses),targets=len(journal['files']),
     same_boundary_order=journal['same_boundary_insertions'],no_overwrite=True,semantic_credit=False))
prior=[]
for path in (actual/'prior-accepted/actual-at-accepted-MI').rglob('*'):
    if path.is_file():
        rel=path.relative_to(actual/'prior-accepted/actual-at-accepted-MI').as_posix()
        data=path.read_bytes(); assert data==git('show',MI+':'+rel)
        prior.append(dict(path=rel,**identity(data)))
assert len(prior)==5
history_paths=['review/remediation-sixth-20261014-prepare','review/remediation/20261003-prepare/batches/B21']
hist=[]
for path in history_paths:
    before=git('rev-parse',BASE+':'+path).decode().strip(); after=git('rev-parse',MI+':'+path).decode().strip()
    assert before==after
    hist.append(dict(path=path,baseline_tree=before,actual_tree=after))
save('prior-and-history-preservation.json',dict(prior_accepted_five=prior,unchanged_historical_subtrees=hist,semantic_credit=False))
save('fixed-git-identities.json',dict(commits={c:git('cat-file','-p',c).decode() for c in [BASE,MI,FI]},
     actual_formal_tree=git('rev-parse',MI+':deliverables/final-specification-set').decode().strip(),
     baseline_formal_tree=git('rev-parse',BASE+':deliverables/final-specification-set').decode().strip(),
     repo_skills_at_B=git('ls-tree','-r','--name-only',BASE,'.agents').decode(),
     repo_skills_at_MI=git('ls-tree','-r','--name-only',MI,'.agents').decode(),
     utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),audit_pid=os.getpid()))
print(json.dumps(dict(restored_files=len(verified),bytes=sum(r['bytes'] for r in verified),formal=131,
                     changed=26,unchanged=105,hunks=len(clauses),targets=24,prior_preserved=len(prior),
                     semantic_PASS=False)))
