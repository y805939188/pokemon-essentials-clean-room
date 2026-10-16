"""Actual full finite payload reception and explicit17 candidate binding, no inherited sourceFULL."""
from pathlib import Path
import collections,datetime,hashlib,json
P=Path(__file__).resolve().parent;RR=P.parent.parent;R=Path('/workspace/pokemon-essentials');NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(n):return json.loads((P/n).read_text())
def write(n,o):(P/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
provider=RR/'tasks/core_atomic_reception/kernel-eor-capture-settings-consumers.v1.json';raw=provider.read_bytes();assert len(raw)==66733 and hashlib.sha256(raw).hexdigest()=='a615421b96536afe9355bb6629d7251fa5373c59dcf9ccefcad530a1baebdbd6';d=json.loads(raw)
checks=[]
for u in d['source_units']:
 b=(R/u['path']).read_bytes();a,z=u['range'];equal=len(b)==u['bytes'] and hashlib.sha256(b).hexdigest()==u['sha256'];assert equal
 text='\n'.join(b.decode().splitlines()[a-1:z])+'\n';assert text.rstrip('\n')==u['content'].rstrip('\n'),u['id']
 checks.append({'unit':u['id'],'source':u['path'],'fixed_bytes_sha_equal':True,'full_unit_text_equal_actual_range':True,'credit':'Identity/content comparison only; actual all16 completeunits were read separately in model outputs.'})
(P/'received/core-eor-capture-a615421b.v1.json').write_bytes(raw)
audio=RR/'tasks/core_atomic_reception/media-reception.mandatory-audio-caller-correction.v1.json';ar=audio.read_bytes();assert len(ar)==3905 and hashlib.sha256(ar).hexdigest()=='38544141edab159a2f388fd1abd6cfab54deab98a09cdc5263142ae9089d0e41'
(P/'received/core-audio-correction-38544141.v1.json').write_bytes(ar)
for u in json.loads(ar)['complete_source_units']:
 b=(R/u['path']).read_bytes();assert len(b)==u['file_bytes'] and hashlib.sha256(b).hexdigest()==u['file_sha256']
checks.append({'mandatory_audio_correction':'a63f17 complete allfields/2completecallers/2facts','own_prior_wrong_channel_assertions':0,'accepted':'Ordinary Wild/Trainer victory uses BGM; throw success uses ME and no-op if opponent exists. Nativepath/audio still unexecuted.'})
lib=json.loads((RR/'tasks/coverage_acceptance_incremental/dispatch/kernel_atomic_reception.readset.json').read_text())['all_fixed_R432_F131_identity_library'];ledger=read('reading-ledger.json');supp=[]
for path,ranges,units in [
 ('Data/Scripts/011_Battle/001_Battle/001_Battle.rb',[[98,174]],['initialize98–174 complete: party emptiness errors first; sendToBoxes default1 then remaining setup/AI; no constructor-wide success guarantee']),
 ('Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb',[[130,139]],['one-line complete happiness136/affection_level137/gender138/nature139; prior method130–131 tail not complete']),
 ('Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb',[[1,91]],['pbReduceHP5–20 complete; pbRecoverHP23–35 complete; pbRecoverHPFromDrain37–52 complete; pbTakeEffectDamage54–62 complete; pbFaint starts64 and cut91 NOT complete']),
]:
 x=next((x for x in ledger['records'] if x.get('repo')=='R' and x.get('path')==path),None)
 if not x:x={'repo':'R','path':path,'reader':'/root/kernel_atomic_reception','status':'PARTIAL_READ_COMPLETE_NAMED_UNITS','whole_file_read':False};ledger['records'].append(x)
 assert x['status']!='FULL_READ'
 x['actual_read_ranges']=sorted(set(tuple(v) for v in x.get('actual_read_ranges',[]))|set(tuple(v) for v in ranges));x['complete_units']=sorted(set(x.get('complete_units',[])+units));x.setdefault('later_read_evidence',[]).append('io/core-reception-complete-constructor-hp-affection-supplements.json /b18dfa')
 fixed=next(v for v in lib if v['repo']=='R' and v['path']==path);b=(R/path).read_bytes();assert hashlib.sha256(b).hexdigest()==fixed['sha256'] and len(b)==fixed['bytes'];supp.append({'fixed_identity':fixed,'actual_reading':x})
ledger['updated_utc']=NOW;write('reading-ledger.json',ledger)
binding={582:'CAR-KERNEL-EOR-01',8:'CAR-KERNEL-EOR-02',9:'CAR-KERNEL-EOR-03',10:'CAR-KERNEL-EOR-03',136:'CAR-KERNEL-EOR-04',606:'CAR-KERNEL-EOR-05',607:'CAR-KERNEL-EOR-05',608:'CAR-KERNEL-EOR-05',609:'CAR-KERNEL-EOR-05',610:'CAR-KERNEL-EOR-05',611:'CAR-KERNEL-EOR-05',613:'CAR-KERNEL-EOR-06',598:'CAR-KERNEL-EOR-06',612:'CAR-KERNEL-EOR-06',599:'CAR-KERNEL-EOR-07',179:'KAR-PREPARE-TIME',445:'KAR-PREPARE-TERRAIN'}
extra=[{'id':'KAR-PREPARE-TIME','complete_unit':'prepare209–304 from actual received16','meaning':'Cave battle_environment forces battle.time2 first. Otherwise TIME_SHADING truthy reads wallclock and maps night2/evening1/other0; false leaves previous/current constructor time rather than forcing a new day.','failure':'Earlier rule/weather/environment/backdrop assignments remain before a clock/predicate failure; no uniform rollback.'},{'id':'KAR-PREPARE-TERRAIN','complete_unit':'prepare209–304 from actual received16','meaning':'Explicit nonnil battle rule defaultTerrain wins. Only absent explicit rule plus OVERWORLD_WEATHER_SETS_BATTLE_TERRAIN truthy maps Storm→Electric/Fog→Misty. Other weather does not force a nonnil terrain here.','failure':'Rule assignments/sendToBoxes copy precede terrain branch; later Weather/metadata resolution can fail with earlier changes retained.'}]
receipt={'schema':'kernel-full-finite-core-eor-capture-reception/v1','utc':NOW,'receiver':'/root/kernel_atomic_reception','provider':'/root/core_atomic_reception','frozen_payload':'core-eor-capture-a615421b.v1.json','input_bytes':66733,'input_sha256':hashlib.sha256(raw).hexdigest(),'actual_complete_read':['00d36d allmetadata/facts/common/open','362854 units0–4 complete','e852b1 units5–9 complete','1a5e2d units10–15 complete','a63f17 mandatory3905B audio correction allfields','b18dfa actual necessary constructor/affection/HP definitions, partialsources only'],'checks':checks,'accepted':'All8 complete original facts with exact common premises/failure limits; constructor default1 and real affection getter/minimum1 HP receiver independently supplemented. Same actual reader context does not create a new independent vote.','own_partial_supplements':supp,'additional_manual_meanings':extra,'original_source_FULL_credit':'Remains actual CORE reader, except already-own Settings/Stat definitions. Receiving complete selected unit text does not grant receiver fullsource.','new_candidate_binding':binding,'open':['All transitive ability/item/ball/storage/form callbacks not universally total by this packet.','HP/type/array/getter source-specific failure prefixes preserved; copiedunit range comparison grants no target execution.','Actual native save/Marshal/battle/UI/audio remains unexecuted.'],'target_business_execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','new_finding_context_vote_required':0}
write('received/core-eor-capture-finite-reception.v1.json',receipt)
c=read('consumer-candidate-dispositions.json');byid={x['id']:x for x in c['records']};facts={x['id']:x for x in d['facts']};facts.update({x['id']:x for x in extra})
for no,fi in binding.items():
 x=byid['KAR-CONSUMER-%04d'%no];assert x['status']=='OPEN_NOT_YET_SEMANTICALLY_RECEIVED';f=facts[fi]
 x.update(status='RECEIVED_NAMED_BOUNDED_CONTRIBUTION_DOWNSTREAM_OPEN',actual_reader='/root/core_atomic_reception',contribution_reception='received/core-eor-capture-finite-reception.v1.json',meaning=f.get('meaning'),premises_and_failure_prefix=f['failure'],fact_ref=fi,raw_source_credit_to_receiver=False,pending='Exact complete finite Settings use accepted; all unlisted transitive callbacks/native/persistence remain scoped separately.')
c['summary']=dict(collections.Counter(x['status'] for x in c['records']));c['updated_utc']=NOW;write('consumer-candidate-dispositions.json',c)
print(json.dumps({'utc':NOW,'actual_original_facts':8,'complete_units':16,'new_precise_candidates':17,'summary':c['summary'],'own_FULL_added':0}))
