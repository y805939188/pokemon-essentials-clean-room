"""Record actual complete finite CORE9 reception and hand-selected30 consumers."""
from pathlib import Path
import collections
import csv
import datetime
import hashlib
import json
import re
import subprocess

BASE=Path(__file__).resolve().parent
R=Path('/workspace/pokemon-essentials')
FIXED='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
START=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(raw):return hashlib.sha256(raw).hexdigest()
def read(name):return json.loads((BASE/name).read_text())
def write(name,value):(BASE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
provider=BASE.parent/'core_atomic_reception/kernel-field-settings-consumers.v1.json'
raw=provider.read_bytes()
assert len(raw)==58859 and sha(raw)=='502a0f5d7b1c06a21c3a00658bdfb9db0f5980235940aa44e570c776413a6fff'
payload=json.loads(raw)
unit_checks=[]
for unit in payload['complete_source_units']:
    parent=(R/unit['path']).read_bytes()
    a,z=unit['range']
    assert len(parent)==unit['parent_bytes'] and sha(parent)==unit['parent_sha256']
    assert ''.join(parent.decode('utf-8-sig').splitlines(keepends=True)[a-1:z])==unit['text']
    unit_checks.append({'id':unit['id'],'parent_identity_and_exact_range_text_match':True,'semantic_credit':'Actual all text personally read; structural validation does not itself grant credit.','contained_completeness':'Terrain affectedByTerrain closing end516 omitted and separately supplemented' if unit['id']=='KS-TERRAINQUERY' else 'Named supplied complete definition actually read including closure'})
rows=list(csv.DictReader((BASE/'core-field-consumer-reception.manual.tsv').open(),delimiter='\t'))
assert len(rows)==10 and all(None not in row and all(row.values()) for row in rows)
mapping={}
for row in rows:
    for number in row['candidate_numbers'].split(','):
        key=f'KAR-CONSUMER-{int(number):04d}'
        assert key not in mapping
        mapping[key]=row['fact_id']
assert len(mapping)==30
write('received/core-field-502a0f5d.v1.json',payload)
assert (BASE/'received/core-field-502a0f5d.v1.json').read_bytes()==raw

supplement=[]
identities=[]
partial_ranges={
 'Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb':[[499,516]],
 'Data/Scripts/011_Battle/001_Battle/001_Battle.rb':[[442,454],[484,494],[703,761]],
 'Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb':[[1,56],[166,174],[1748,1775]],
}
for path,ranges in partial_ranges.items():
    parent=(R/path).read_bytes()
    assert subprocess.run(['git','show',FIXED+':'+path],cwd=R,capture_output=True,check=True).stdout==parent
    identity={'path':path,'bytes':len(parent),'sha256':sha(parent),'git_blob':subprocess.run(['git','rev-parse',FIXED+':'+path],cwd=R,capture_output=True,text=True,check=True).stdout.strip(),'fixed_R':FIXED,'actual_reader':'/root/kernel_atomic_reception','status':'PARTIAL_READ_COMPLETE_NECESSARY_UNITS','actual_read_ranges':ranges,'whole_source_full_credit_added':0}
    identities.append(identity)
    lines=parent.decode('utf-8-sig').splitlines(keepends=True)
    names={'allBattlers','eachBattler','pbCheckGlobalAbility','pbStartWeather','pbEndPrimordialWeather'} if '/001_Battle/' in path else set()
    if names:
        for n,line in enumerate(lines,1):
            match=re.match(r'^  def ([^\s(;]+)',line)
            if match and match[1] in names:
                z=next(j for j in range(n,len(lines)+1) if lines[j-1].rstrip('\r\n')=='  end')
                assert any(a<=n and z<=b for a,b in ranges)
                supplement.append({'id':'OWN-'+match[1],'path':path,'range':[n,z],'text':''.join(lines[n-1:z]),'source_identity_sha256':identity['sha256'],'actual_reader':'/root/kernel_atomic_reception'})
    else:
        exact=[('OWN-TERRAIN-COMPLETE',[499,516])] if '/002_Battler/' in path else [('OWN-WEATHER-REGISTRY',[37,37]),('OWN-EFFECT-TRIGGER',[53,56]),('OWN-WEATHER-WRAPPER',[170,172]),('OWN-FOUR-WEATHER-ROCKS',[1752,1774])]
        for name,(a,z) in exact:
            assert any(s<=a and z<=e for s,e in ranges)
            supplement.append({'id':name,'path':path,'range':[a,z],'text':''.join(lines[a-1:z]),'source_identity_sha256':identity['sha256'],'actual_reader':'/root/kernel_atomic_reception'})
write('core-field-necessary-receiver-supplement.v1.json',{'schema':'KAR-core-field-necessary-receiver-supplement.v1','recorded_utc':START,'original_provider_packet_sha256':sha(raw),'preserve_original':True,'terrain_range_correction':'Original499–515 contains airborne complete but omits affectedByTerrain end516. This own actually read499–516 supplies the complete necessary method; no new finding or whole source credit.','identities':identities,'complete_units':supplement,'business':'NOT_EXECUTED','open':'Weather/form callbacks and full field/reset/lifetime domains remain separate. Only named complete source units received; no all Battle/Move/AI/Items acceptance.'})

receipt={'schema':'KAR-core-field-settings-finite-reception.v1','recorded_utc':START,'actual_receiver':'/root/kernel_atomic_reception','original_provider':'/root/core_atomic_reception','provider_packet':{'path':str(provider.relative_to(BASE.parent.parent)),'bytes':len(raw),'sha256':sha(raw),'task_local_exact_copy':'received/core-field-502a0f5d.v1.json'},'actual_full_read_evidence':['io/core-field-settings-first.json','io/core-field-settings-second.json','io/core-field-settings-third.json','io/core-field-settings-fourth.json'],'all414_lines_and_complete_metadata_read':True,'all9_original_facts_received':payload['facts'],'all_original_common_premises':payload['common_premises'],'all_original_failure_and_persistence':[payload['common_failure'],payload['persistence_reload']],'all_original_remaining_open':payload['remaining_open'],'unit_exact_validation':unit_checks,'manual_meaning_and_boundary_records':rows,'selected30_candidates':mapping,'own_necessary_receiver_supplement':'core-field-necessary-receiver-supplement.v1.json','source_credit':'Original source FULL/PARTIAL remains CORE; own additions are only complete selected necessary methods, no sourceFULL. KS-SET was already own FULL independently.','new_source_full_or_contexts_or_votes_or_findings':0,'whole_domain_received':False,'business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
write('received/core-field-settings-finite-reception.v1.json',receipt)
receipt_raw=(BASE/'received/core-field-settings-finite-reception.v1.json').read_bytes()
receipt_identity={'path':'received/core-field-settings-finite-reception.v1.json','bytes':len(receipt_raw),'sha256':sha(receipt_raw)}
consumers=read('consumer-candidate-dispositions.json')
by_id={record['id']:record for record in consumers['records']}
by_fact={row['fact_id']:row for row in rows}
for candidate,fact_id in mapping.items():
    record=by_id[candidate]
    assert record['status']=='OPEN_NOT_YET_SEMANTICALLY_RECEIVED',(candidate,record['status'])
    manual=by_fact[fact_id]
    record['status']='RECEIVED_NAMED_BOUNDED_CONTRIBUTION_DOWNSTREAM_OPEN'
    record['bounded_complete_contribution']=dict(receipt_identity,fact_id=fact_id,original_provider='/root/core_atomic_reception',actual_receiver='/root/kernel_atomic_reception')
    record['actual_finite_meaning']=manual['received_exact_meaning']
    record['pending']=manual['independent_reception_boundary']
    record['source_credit']='Original actual CORE parent FULL/PARTIAL retained. This context actually read finite complete payload and necessary own partial receivers; no own sourceFULL inferred.'
    record['whole_domain_accepted']=False
consumers['summary']=dict(collections.Counter(record['status'] for record in consumers['records']))
assert consumers['summary']['OPEN_NOT_YET_SEMANTICALLY_RECEIVED']==281
assert consumers['summary']['RECEIVED_NAMED_BOUNDED_CONTRIBUTION_DOWNSTREAM_OPEN']==227
consumers['updated_utc']=START
consumers['core_field_reception']=dict(receipt_identity,provider_complete_facts=9,own_additional_finite_meaning=1,exact_candidates=30,new_own_sourceFULL=0)
write('consumer-candidate-dispositions.json',consumers)
ledger=read('reading-ledger.json')
for identity in identities:
    entry=next((row for row in ledger['records'] if row.get('repo')=='R' and row.get('path')==identity['path']),None)
    if entry is None:
        entry={'repo':'R','path':identity['path'],'status':'PARTIAL_READ_COMPLETE_NAMED_UNITS'}
        ledger['records'].append(entry)
    old_ranges=entry.get('actual_read_ranges',[])
    entry['actual_read_ranges']=sorted({tuple(pair) for pair in old_ranges+identity['actual_read_ranges']})
    entry.setdefault('later_finite_own_read_supplements',[]).append({'path':'core-field-necessary-receiver-supplement.v1.json','source_identity_sha256':identity['sha256'],'original_whole_status_preserved':True})
assert len({row['path'] for row in ledger['records'] if row.get('repo')=='R' and row.get('status')=='FULL_READ' and not row['path'].startswith('PBS/')})==108
ledger['updated_utc']=START
write('reading-ledger.json',ledger)
facts=read('sourcefact-consumer-receptions.json')
facts['named_contributions'].append({'id':'CORE-FIELD-9','reception_path':receipt_identity['path'],'provider':'/root/core_atomic_reception','complete_finite_count':9,'extra_own_finite_critical_multiplier_meaning':1,'source_credit':'Original reader retained; own complete partial receivers explicit; no sourceFULL or whole-domain approval','whole_domain_received':False})
facts['updated_utc']=START
write('sourcefact-consumer-receptions.json',facts)
outcome=dict(receipt_identity,recorded_utc=START,provider_complete_facts=9,selected_candidates=30,remaining_candidates=281,own_nonPBS_FULL=108,own_necessary_supplement_units=len(supplement),business='NOT_EXECUTED',new_required_contexts_votes=0)
stdout=json.dumps(outcome,ensure_ascii=False)+'\n'
io=BASE/'io'
(io/'core-field-settings-reception-integration.stdout.txt').write_text(stdout)
(io/'core-field-settings-reception-integration.stderr.txt').write_text('')
(io/'core-field-settings-reception-integration.json').write_text(json.dumps({'id':'core-field-settings-reception-integration','started_utc':START,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'underlying_exit_code':0,'stdout_path':str(io/'core-field-settings-reception-integration.stdout.txt'),'stderr_path':str(io/'core-field-settings-reception-integration.stderr.txt'),'command':'python receive-core-field-settings.py','business_execution':'NOT_EXECUTED'},indent=2)+'\n')
print(stdout,end='')
