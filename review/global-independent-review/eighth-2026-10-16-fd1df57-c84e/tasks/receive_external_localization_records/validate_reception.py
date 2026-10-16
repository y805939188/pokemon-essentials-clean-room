"""Mechanical consistency and identity checks; no semantic or business PASS."""
from pathlib import Path
import hashlib
import json
import subprocess
import datetime

T=Path(__file__).resolve().parent
def read(name): return json.loads((T/name).read_text())
def sha(data): return hashlib.sha256(data).hexdigest()
def main():
    f=read('frozen-denominator.json');r=read('reading-ledger.json');q=read('reception-ledger.json');i=read('interfaces.json');p=read('proposal-counters.json')
    assert q['status']=='INCOMPLETE' and not q['full_task_final_ready']
    assert r['independence']['different'] and p['actual_receiver_differs_from_author']
    assert len(f['primary_objects'])==10715
    assert sum(x['literal_read_here'] for x in f['primary_objects'])==439
    assert len(r['literal_record_reads'])==433
    assert len({x['id'] for x in r['literal_record_reads']})==433
    assert sum(x['kind']=='record' and not x['literal_read_here'] for x in f['primary_objects'])==10264
    assert len(f['image_methods'])==len(q['image_callers'])==36
    assert sum(len(x['matched_lines']) for x in f['image_methods'])==63
    assert len(f['pbs35'])==35 and len(i['interfaces'])==7
    assert not any(x['full_final_acceptance'] for x in i['interfaces'])
    assert len(f['reverse125'])==125 and sum(x['subassertion_count'] for x in f['reverse125'])==398
    count=0
    for row in read('evidence/target-recovery.json')['files']:
        data=(T/row['local_path']).read_bytes()
        assert len(data)==row['bytes'] and sha(data)==row['sha256']
        count+=1
    assert count==213
    originals=T/'evidence/recovered-target/evidence/contracts'
    for name in ['AGENTS.md','eighth-global-review-prompt.md','review-SKILL.md']:
        assert (originals/name).read_bytes()==(T/'evidence/contract'/name).read_bytes()
    primary={Path(x['source']).stem:x for x in read('evidence/primary-identities.json')}
    for x in r['literal_record_reads']:
        n=x['record'];lines=(T/'evidence/primary-reference'/(x['domain']+'.txt')).read_text(encoding='utf-8-sig').splitlines()
        assert [x['raw_key'],x['raw_value']]==lines[2*n+2:2*n+4]
    root=T.parents[4]
    prefix=str(T.relative_to(root))+'/'
    staged=subprocess.check_output(['git','diff','--cached','--name-only'],cwd=root).decode().splitlines()
    assert all(x.startswith(prefix) for x in staged),staged
    out={'schema':'gr8-elr-mechanical-package-validation/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'result':'PASS_MECHANICAL_ONLY','source_semantic_credit':0,'business_execution':'NOT_EXECUTED','task_status':'INCOMPLETE','target_identity_files':213,'literal_records':433,'unread_literal_records':10264,'complete_image_methods':36,'final_interfaces_accepted':0,'UPDATE_NOT_STARTED':True}
    (T/'evidence/package-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out,ensure_ascii=False))
if __name__=='__main__':main()
