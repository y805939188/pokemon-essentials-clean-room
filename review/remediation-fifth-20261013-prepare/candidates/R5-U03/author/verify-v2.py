#!/usr/bin/env python3
"""Validate only the bounded v2 document delta and exact identity reuse. No behavior execution."""
import hashlib,json,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parent
REPO=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],cwd=ROOT,text=True).strip())
REL=ROOT.relative_to(REPO).as_posix()
V1='d93776e127c1dec08fcb4297c7280e60020ced68'
FID='GR5-M01-006'
WP18='deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md'
CAT='deliverables/final-specification-set/test-catalog/creature-rpg-wp18-20-24-25-26.md'

def blob(ref,path):return subprocess.check_output(['git','show',ref+':'+path],cwd=REPO)
def previous(name):return blob(V1,REL+'/'+name)
def current(name):return (ROOT/name).read_bytes()
def js(b):return json.loads(b)
def digest(n):return hashlib.sha256(json.dumps(n,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def identity(b):return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),git_blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest())

before=js(previous('operations.json'))['operations'];after=js(current('operations.json'))['operations']
assert len(before)==len(after)==52
altered=[]
for a,b in zip(before,after):
    assert {k:v for k,v in a.items() if k!='new_text'}=={k:v for k,v in b.items() if k!='new_text'},a['label']
    if a['new_text']==b['new_text']:continue
    altered.append((b['target_path'],b['label']))
    if b['target_path']==WP18:
        assert b['label']=='npc-default-overlay-table'
        removed='先普通创建，再处理可选形态、持物和招式；'
        suffix='下表的省略值仍覆盖创建结果'
        old_prefix,old_rest=a['new_text'].split(removed,1)
        assert b['new_text'].startswith(old_prefix)
        new_rest=b['new_text'].split(suffix,1)[1]
        assert old_rest.split(suffix,1)[1]==new_rest
        for clause in ['给定形态（含 0）','简单存储形态写入','不调用形态处理器','不登记图鉴','不清特性缓存','仍重算能力','显式招式列表存在且非空','按给定顺序逐个静默学习','否则按当前等级可达学习表重建默认招式','WP20 §5.1']:
            assert clause in b['new_text'],clause
    else:
        assert b['target_path']==CAT and b['label']=='R5U03-vectors'
        assert b['new_text'].startswith(a['new_text'])
        tail=b['new_text'][len(a['new_text']):]
        assert len(tail.splitlines())==3
        assert all(line.startswith('| R5U03-M01-006-') for line in tail.splitlines())
assert set(altered)=={(WP18,'npc-default-overlay-table'),(CAT,'R5U03-vectors')}
oldv=js(previous('static-vectors.json'))['vectors'];newv=js(current('static-vectors.json'))['vectors']
assert newv[:len(oldv)]==oldv and len(oldv)==66 and len(newv)==69
assert [v['id'] for v in newv[66:]]==['R5U03-M01-006-08','R5U03-M01-006-09','R5U03-M01-006-10']
assert all(v['finding_id']==FID and v['execution_status']=='NOT_EXECUTED' and v['evidence_level']=='DERIVED_VECTOR' for v in newv[66:])
f0=js(previous('finding-responses.json'))['findings'];f1=js(current('finding-responses.json'))['findings']
for a,b in zip(f0,f1):
    if a['finding_id']!=FID:assert a==b,a['finding_id']
manifest=js(previous('candidate-manifest.json'))
changed_normative=[]
for x in manifest['artifacts']:
    if x['path'].startswith(('formal/','fragments/')) and current(x['path'])!=previous(x['path']):changed_normative.append(x['path'])
assert len(changed_normative)==2
assert set(changed_normative)=={
    'formal/'+CAT,
    'fragments/'+WP18+'.md'
}
nav=js(current('navigation-corrections.json'));assert len(nav['corrections'])==2
record_count=0
for c in nav['corrections']:
    pin=c['successor_navigation'];raw=blob(pin['commit'],pin['path'])
    assert identity(raw)=={k:pin[k] for k in ['bytes','sha256','git_blob']}
    assert c['immutable_navigation_advisory_sha256']!=pin['sha256']
    assert c['advisory_status']=='MISMATCH_RETAINED_IN_FROZEN_ORIGINAL'
    assert not c['frozen_original_modified'] and not c['whole_advisory_file_hash_PASS_granted']
    data=js(raw)
    for r in c['exact_current_records']:
        n=data
        for part in r['pointer'].strip('/').split('/'):n=n[int(part)] if isinstance(n,list) else n[part]
        assert n['id']==r['finding_id'] and digest(n)==r['expected_record_sha256']
        record_count+=1
assert record_count==4
print(json.dumps(dict(schema='r5.u03.v2-tool-validation.v1',evidence_level='TOOL_VALIDATION',status='PASS',v1_evidence=V1,changed_normative_targets=2,unchanged_other_finding_objects=10,prior_vectors_preserved=66,new_vectors=3,total_vectors=69,operation_count=52,full_navigation_file_identities_verified=2,exact_navigation_records_verified=4,old_advisory_SHA_status='2 MISMATCH RETAINED; NOT_CERTIFIED',new_behavior_executions=0,independent_006_verdict='WAIT_ORIGINAL_REVIEWER'),ensure_ascii=False,indent=2))
