"""Mechanical identities and clause assembly only; never semantic or runtime PASS."""
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path('/workspace/r7-ir-R7-U01')
REPO = '/workspace/pokemon-essentials-clean-room'
B = 'e646432c644dec04d306842cc5a559a29c718fbc'
MI = '45c80832a41c1b56dcd7e9d93497758cbb7721de'
FI = '13d76ba61838b13925ba9d41f58a6b047564d926'
def git(*args):
    return subprocess.check_output(['git',*args],cwd=REPO)
def identity(b):
    return {'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),
            'git_blob':hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()}
def check(b, row):
    a=identity(b)
    for k,v in a.items():
        if k in row: assert row[k]==v,(k,row,a)
        if k=='git_blob' and 'git_blob_content_id' in row:assert row['git_blob_content_id']==v
    return a
f=json.loads((ROOT/'bootstrap/integrated-input.json').read_bytes())
j=json.loads((ROOT/'actual-input/integration/applied-clauses.json').read_bytes())
commits={c:git('rev-parse',c+'^{tree}').decode().strip() for c in [B,MI,FI,'a3938bbb8f8c2294465b75363a39fd4598b82a15','2e1b1fb6dd638757436b7292949b3ba0012cafec']}
assert commits[MI]==f['actual_MI_tree']
assert commits[FI]=='6747a584b91c86acd4771c1a6dee93260602106f'
assert git('rev-parse',MI+':deliverables/final-specification-set').decode().strip()==f['actual_formal_subtree']
formal=[]
for r in f['all_formal_file_identities']:
    b=git('show',MI+':'+r['path']);a=check(b,r)
    old=git('show',B+':'+r['path']);check(old,r['base_B_identity'])
    assert (old!=b)==r['changed_against_B']
    formal.append({'path':r['path'],**a,'changed_against_B':old!=b})
tree_paths=git('ls-tree','-r','--name-only',MI,'--','deliverables/final-specification-set').decode().splitlines()
assert sorted(tree_paths)==sorted(x['path'] for x in formal)
assert len(formal)==131 and sum(x['changed_against_B'] for x in formal)==26
restored=[]
for kind,dest in [('original','original'),('actual','actual-input')]:
    plan=json.loads((ROOT/(kind+'-plans/R7-U01.json')).read_bytes())
    rows=sum([plan.get(k,[]) for k in ('artifacts','evidence','fixed_read_inputs')],[])
    for row in rows:
        b=(ROOT/dest/row['local_path']).read_bytes();a=check(b,row)
        if row['repository']=='y805939188/pokemon-essentials-clean-room':
            remote=git('show',row['commit']+':'+row['path'])
            if 'transport_path' in row: remote=gzip.decompress(remote)
            assert remote==b,row['local_path']
        restored.append({'set':kind,'path':row['local_path'],**a})
hunks=[];assemblies=[]
for r in j['files']:
    p=r['path']
    if r['baseline_identity']['bytes']==0:
        assert subprocess.run(['git','cat-file','-e',B+':'+p],cwd=REPO,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode!=0
        base=b''
    else:base=git('show',B+':'+p)
    check(base,r['baseline_identity']);lines=base.decode().splitlines(keepends=True)
    ordered=sorted(r['hunks'],key=lambda h:(h['base_line_indices_half_open'][0],h['batch_order']))
    result=[];cursor=0
    for h in ordered:
        a,z=h['base_line_indices_half_open'];c,d=h['candidate_line_indices_half_open']
        candidate=git('show',h['candidate_commit']+':'+h['candidate_path']).decode().splitlines(keepends=True)
        removed=''.join(lines[a:z]);added=''.join(candidate[c:d])
        assert removed==h['removed_text'] and added==h['added_text']
        check(removed.encode(),h['removed_identity']);check(added.encode(),h['added_identity'])
        assert a>=cursor,(p,a,cursor)
        result.extend(lines[cursor:a]);result.append(added);cursor=z
        hunks.append({'path':p,'batch':h['batch_id'],'base':h['base_line_indices_half_open'],'actual':h['actual_final_line_indices_half_open'],
                      'candidate_commit':h['candidate_commit'],'added':identity(added.encode()),'exact_B_and_candidate':True})
    result.extend(lines[cursor:]);assembled=''.join(result).encode();check(assembled,r['assembled_candidate_clauses_identity'])
    current=git('show',MI+':'+p)
    admin=next((x for x in j['root_administrative_reception_adjustments'] if x['path']==p),None)
    if admin:
        check(assembled,admin['before_identity']);check(current,admin['after_identity'])
        if 'added_text' in admin:assert current==assembled+admin['added_text'].encode()
        else:
            old=json.loads(assembled);new=json.loads(current)
            assert old.keys()==new.keys()
    else:assert current==assembled
    assemblies.append({'path':p,'contributors':r['contributors'],'hunks':len(r['hunks']),'actual':identity(current),'admin':bool(admin),'exact_assembly':True})
prior=[]
for path in sorted((ROOT/'actual-input/prior-accepted/actual-at-accepted-MI').rglob('*')):
    if not path.is_file():continue
    rel=str(path.relative_to(ROOT/'actual-input/prior-accepted/actual-at-accepted-MI'))
    b=git('show',MI+':'+rel);assert b==path.read_bytes();prior.append({'path':rel,**identity(b),'preserved':True})
skills={c:git('ls-tree','-r','--name-only',c,'--','.agents').decode().splitlines() for c in [B,MI]}
out={'schema':'r7.u01.actual.mechanical.v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'commits':commits,'formal':formal,'formal_counts':{'all':131,'changed':26,'unchanged':105},'restored':restored,
     'candidate_hunks':hunks,'assemblies':assemblies,'prior_five':prior,'tracked_agents_files':skills,
     'qualification':'TOOL_VALIDATION only. No content acceptance, independent identity or runtime evidence inferred.'}
(ROOT/'tool-evidence/mechanical-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'commits':commits,'formal':out['formal_counts'],'restored':len(restored),'hunks':len(hunks),'assembled_targets':len(assemblies),'prior_preserved':len(prior),'skills':skills},ensure_ascii=False,indent=2))
