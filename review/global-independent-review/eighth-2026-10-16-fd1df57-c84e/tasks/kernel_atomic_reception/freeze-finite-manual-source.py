"""Package explicit manual meanings and only the already actually read source ranges.

This does not discover or infer semantics, coverage or full-reading from file identity.
"""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import subprocess
import sys
BASE=Path(__file__).resolve().parent
R=Path('/workspace/pokemon-essentials')
FIXED='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
START=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(raw):return hashlib.sha256(raw).hexdigest()
def load(name):return json.loads((BASE/name).read_text())
def write(name,value):(BASE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
manual=load(sys.argv[1])
assert manual['schema']=='KAR-finite-manual-source-package.v1'
output=manual['output'];assert Path(output).name==output and not (BASE/output).exists()
ledger=load('reading-ledger.json');identities=[];units=[]
for spec in manual['sources']:
    path=spec['path'];raw=(R/path).read_bytes()
    assert subprocess.run(['git','show',FIXED+':'+path],cwd=R,capture_output=True,check=True).stdout==raw
    lines=raw.decode('utf-8-sig').splitlines(keepends=True)
    identity={'repo':'R','path':path,'bytes':len(raw),'sha256':sha(raw),'git_blob':subprocess.run(['git','rev-parse',FIXED+':'+path],cwd=R,capture_output=True,text=True,check=True).stdout.strip(),'fixed_R':FIXED,'lines':len(lines),'actual_reader':'/root/kernel_atomic_reception','reading_evidence':spec['evidence']}
    ranges=[[1,len(lines)]] if spec['full'] else spec['ranges']
    entry=next((e for e in ledger['records'] if e.get('repo')=='R' and e.get('path')==path),None)
    if entry is None:entry={'repo':'R','path':path,'status':'PARTIAL_READ_COMPLETE_NAMED_UNITS'};ledger['records'].append(entry)
    previous_full=entry.get('status')=='FULL_READ'
    identity['own_read_status']='FULL_READ' if spec['full'] or previous_full else 'PARTIAL_READ_COMPLETE_NAMED_UNITS'
    identities.append(identity)
    for lo,hi in ranges:
        assert 1<=lo<=hi<=len(lines)
        units.append({'path':path,'range':[lo,hi],'text':''.join(lines[lo-1:hi]),'qualification':'Exact actually read complete unit(s) or declarations; whole parent only when explicit own FULL recorded','source_sha256':identity['sha256']})
    entry.update({k:v for k,v in identity.items() if k not in ('own_read_status','reading_evidence')})
    entry['reader']='/root/kernel_atomic_reception'
    if spec['full']:entry.update(status='FULL_READ',actual_read_ranges=ranges,reading_evidence=spec['evidence'])
    elif not previous_full:entry['actual_read_ranges']=sorted({tuple(x) for x in entry.get('actual_read_ranges',[])}|{tuple(x) for x in ranges})
    entry.setdefault('later_read_evidence',[]).extend(spec['evidence'])
facts=manual['facts'];assert len({x['id'] for x in facts})==len(facts)
mapping={}
for fact in facts:
    assert all(fact.get(k) for k in ('id','meaning','control','failure_prefix','open'))
    for n in fact['candidates']:
        key=f'KAR-CONSUMER-{n:04d}';assert key not in mapping;mapping[key]=fact
cons=load('consumer-candidate-dispositions.json')
found={e['id'] for e in cons['records'] if e['id'] in mapping}
assert found==set(mapping)
for e in cons['records']:
    if e['id'] in mapping:assert e['status']=='OPEN_NOT_YET_SEMANTICALLY_RECEIVED'
payload={'schema':'KAR-complete-finite-manual-source-contribution.v1','created_utc':START,'actual_reader':'/root/kernel_atomic_reception','fixed_R':FIXED,'manual_package':manual,'source_identities':identities,'source_units':units,'candidate_to_fact':{k:v['id'] for k,v in mapping.items()},'new_required_contexts_votes':0,'business_execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
raw=(json.dumps(payload,ensure_ascii=False,indent=2)+'\n').encode();packet={'path':output,'bytes':len(raw),'sha256':sha(raw)}
assert len({e['path'] for e in ledger['records'] if e.get('repo')=='R' and e.get('status')=='FULL_READ' and not e['path'].startswith('PBS/')})==manual['expected_nonPBS_full_after']
# All prerequisites checked before the first persistent write.
(BASE/output).write_bytes(raw)
for entry in ledger['records']:
    if entry.get('path') in {s['path'] for s in manual['sources']}:entry.setdefault('finite_contributions',[]).append(packet)
ledger['updated_utc']=START;write('reading-ledger.json',ledger)
for entry in cons['records']:
    fact=mapping.get(entry['id'])
    if fact:
        source=next(s for s in identities if s['path']==entry['path'])
        status='COMMENT_OR_INACTIVE_DEFINITION_NO_RUNTIME_CONSUMPTION_AT_THIS_LOCATION' if fact.get('purpose_only') else 'RECEIVED_LOCAL_STATIC_DOWNSTREAM_OPEN'
        entry.update(status=status,own_full_source_read=source['own_read_status']=='FULL_READ',actual_reader='/root/kernel_atomic_reception',meaning=fact['meaning'],premises_and_failure_prefix=manual['common_premise']+' '+fact['failure_prefix'],pending=fact['open'],manual_fact=fact['id'],contribution=packet)
for extra in manual.get('additional_discovered_candidates',[]):
    assert extra['manual_fact'] in {f['id'] for f in facts}
    assert not any(x['id']==extra['id'] for x in cons.get('additional_discovered_lexical_candidates',[]))
    cons.setdefault('additional_discovered_lexical_candidates',[]).append(dict(extra,actual_reader='/root/kernel_atomic_reception',status='RECEIVED_LOCAL_STATIC_DOWNSTREAM_OPEN',contribution=packet))
cons['summary']=dict(collections.Counter(e['status'] for e in cons['records']));cons['updated_utc']=START;cons.setdefault('later_finite_manual_packages',[]).append(packet);write('consumer-candidate-dispositions.json',cons)
sourcefacts=load('sourcefact-consumer-receptions.json');sourcefacts['named_contributions'].append({'id':manual['id'],'complete_contribution':packet,'actual_reader':'/root/kernel_atomic_reception','manual_facts':len(facts),'specific_lexical_candidates':len(mapping),'whole_domain_received':False});sourcefacts['updated_utc']=START;write('sourcefact-consumer-receptions.json',sourcefacts)
inp=load('input-identities.json');inp.setdefault('later_finite_manual_source_identities',[]).append({'id':manual['id'],'sources':identities});inp['updated_utc']=START;write('input-identities.json',inp)
result=dict(packet,utc=START,nonPBS_full=manual['expected_nonPBS_full_after'],manual_facts=len(facts),candidate_summary=cons['summary'])
stdout=json.dumps(result,ensure_ascii=False)+'\n';io=BASE/'io';name=manual['id']+'-integration'
(io/(name+'.stdout.txt')).write_text(stdout);(io/(name+'.stderr.txt')).write_text('')
(io/(name+'.json')).write_text(json.dumps({'id':name,'started_utc':START,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'underlying_exit_code':0,'command':'python freeze-finite-manual-source.py '+sys.argv[1],'stdout_path':str(io/(name+'.stdout.txt')),'stderr_path':str(io/(name+'.stderr.txt')),'reading_credit':'Manual facts and actual preceding source I/O only; mechanical packaging/validation adds no semantic credit.'},indent=2)+'\n')
print(stdout,end='')
