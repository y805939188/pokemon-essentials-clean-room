"""Freeze actually read literals and twelve manual meanings, without target execution."""
from pathlib import Path
import collections
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
def load(name):return json.loads((BASE/name).read_text())
def write(name,value):(BASE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def source(path):
    raw=(R/path).read_bytes()
    assert subprocess.run(['git','show',FIXED+':'+path],cwd=R,capture_output=True,check=True).stdout==raw
    identity={'repo':'R','path':path,'bytes':len(raw),'sha256':sha(raw),'git_blob':subprocess.run(['git','rev-parse',FIXED+':'+path],cwd=R,capture_output=True,text=True,check=True).stdout.strip(),'fixed_R':FIXED,'lines':len(raw.decode('utf-8-sig').splitlines()),'actual_reader':'/root/kernel_atomic_reception'}
    return raw,identity

files=[]
for path,evidence in [('PBS/encounters.txt','pbs-encounters-default-full'),('PBS/Gen 5 backup/encounters.txt','pbs-encounters-gen5-gen6-full'),('PBS/Gen 6 backup/encounters.txt','pbs-encounters-gen5-gen6-full'),('PBS/Gen 7 backup/encounters.txt','pbs-encounters-gen7-full'),('PBS/Gen 8 backup/encounters.txt','pbs-encounters-gen8-full')]:
    raw,identity=source(path)
    assert identity['lines']==311
    identity.update(status='FULL_READ',reading_evidence='io/'+evidence+'.json')
    records=[]
    current=None
    method=None
    for lineno,line in enumerate(raw.decode('utf-8-sig').splitlines(),1):
        prepared=line.split('#',1)[0].strip()
        if not prepared:continue
        header=re.fullmatch(r'\[(\d+)(?:,(\d+))?\]',prepared)
        if header:
            if current:current['source_range'][1]=lineno-1
            current={'ordinal':len(records)+1,'header_literal':prepared,'map':int(header[1]),'version':int(header[2] or 0),'source_range':[lineno,311],'methods':[]}
            records.append(current)
            method=None
        elif prepared[0].isdigit():
            assert current and method
            parts=prepared.split(',');assert len(parts) in (3,4)
            weight=int(parts[0]);minimum=int(parts[2]);maximum=int(parts[3]) if len(parts)==4 else minimum
            assert weight>0 and 1<=minimum<=maximum<=100
            method['slots'].append({'ordinal':len(method['slots'])+1,'line':lineno,'original_line':line,'weight':weight,'species_symbol_text':parts[1],'minimum_level':minimum,'maximum_level':maximum,'maximum_was_omitted':len(parts)==3,'reference_resolution':'REGISTERED_SPECIES_REQUIRED_NOT_GRANTED_BY_LITERAL'})
        else:
            assert current
            parts=prepared.split(',');assert len(parts) in (1,2)
            default={'OldRod':0,'GoodRod':0,'SuperRod':0,'HeadbuttLow':0,'HeadbuttHigh':0}.get(parts[0])
            chance=int(parts[1]) if len(parts)==2 else default
            assert chance is not None
            method={'ordinal':len(current['methods'])+1,'line':lineno,'original_line':line,'type_symbol_text':parts[0],'explicit_probability':int(parts[1]) if len(parts)==2 else None,'conditional_compiled_probability':chance,'slots':[]}
            current['methods'].append(method)
    assert len(records)==19 and sum(len(x['methods']) for x in records)==52
    methods=[m for x in records for m in x['methods']]
    assert sum(len(m['slots']) for m in methods)==220
    assert sum(m['explicit_probability'] is None for m in methods)==19
    for method in methods:
        assert sum(s['weight'] for s in method['slots'])==100
        groups={}
        for slot in method['slots']:
            key=(slot['species_symbol_text'],slot['minimum_level'],slot['maximum_level'])
            groups[key]=groups.get(key,0)+slot['weight']
        method['conditional_compiled_merged_slots']=[{'weight':weight,'species_symbol_text':species,'minimum_level':minimum,'maximum_level':maximum} for (species,minimum,maximum),weight in sorted(groups.items(),key=lambda kv:(-kv[1],kv[0][0]))]
        method['compiled_order_qualification']='Weight descending then Species text ascending; equal comparator groups have no additional native stable-order promise.'
    files.append({'identity':identity,'raw_text_including_BOM_if_present':raw.decode('utf-8'),'records':records,'qualification':'All311 physical lines and complete ordered records actually read for this path; extraction/projection comparison only tool validation. Backup activation explicit, lookup success/native compile unexecuted.'})

wild='Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb'
specs=[(wild,None,['wild-encounters-001-240','wild-encounters-241-469'],'FULL_READ'),('Data/Scripts/010_Data/002_PBS data/013_Encounter.rb',None,[],'FULL_READ_PREVIOUS'),('Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb',None,[],'FULL_READ_PREVIOUS'),('Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',[[658,765]],[],'FULL_READ_PREVIOUS_SELECTED_COMPLETE_METHOD'),('Data/Scripts/015_Trainers and player/001_Trainer.rb',[[57,63],[75,79],[94,100]],['wild-lead-party-receiver-complete','wild-pokemon-party-filter-complete'],'PARTIAL_READ_COMPLETE_NECESSARY_METHODS'),('Data/Scripts/016_UI/004_UI_Pokedex_Entry.rb',[[302,352]],['wp03-dex-necessary-complete-area-methods'],'PARTIAL_READ_COMPLETE_NECESSARY_METHODS'),('Data/Scripts/001_Settings.rb',[[135,146],[358,370]],[],'FULL_READ_PREVIOUS_SELECTED_DECLARATIONS')]
identities=[]
units=[]
for path,ranges,evidence,status in specs:
    raw,identity=source(path)
    identity.update(status=status,reading_evidence=['io/'+e+'.json' for e in evidence])
    identities.append(identity)
    lines=raw.decode('utf-8-sig').splitlines(keepends=True)
    for lo,hi in ranges or [[1,len(lines)]]:
        assert hi<=len(lines)
        units.append({'path':path,'range':[lo,hi],'text':''.join(lines[lo-1:hi]),'source_sha256':identity['sha256'],'qualification':status})
manual=load('encounter-fixtures-consumers.manual.json')
assert len(manual['facts'])==12 and len({f['id'] for f in manual['facts']})==12
mapping={f'KAR-CONSUMER-{n:04d}':fact for fact in manual['facts'] for n in fact['candidates']}
assert len(mapping)==10
payload={'schema':'KAR-five-encounter-fixtures-consumers.v1','created_utc':START,'actual_reader':'/root/kernel_atomic_reception','fixed_R':FIXED,'files':files,'source_identities':identities,'source_units':units,'manual_facts':manual['facts'],'common_premise':manual['common_premise'],'candidate_to_fact':{k:v['id'] for k,v in mapping.items()},'root_bounded_counter_receipt':'received/root-encounter-finite-reception.v1.json','history':'GR7-M04-001 now accurately navigated as emergency-save optional, not encounter alias; full canonical54870B not yet received here. All-history dedup OPEN.','business_execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','new_required_contexts_votes':0,'remaining':'Other46 physical PBS and all unreceived callbacks/native/domain consumers remain explicit OPEN; no whole global Settings or encounter-domain PASS.'}
write('five-encounter-fixtures-consumers-contribution.v1.json',payload)
raw=(BASE/'five-encounter-fixtures-consumers-contribution.v1.json').read_bytes()
packet={'path':'five-encounter-fixtures-consumers-contribution.v1.json','bytes':len(raw),'sha256':sha(raw)}
ledger=load('reading-ledger.json')
for identity in [f['identity'] for f in files]+[identities[0]]:
    entry=next((x for x in ledger['records'] if x.get('repo')=='R' and x.get('path')==identity['path']),None)
    if entry is None:entry={'repo':'R','path':identity['path']};ledger['records'].append(entry)
    entry.update(identity,reader='/root/kernel_atomic_reception',status='FULL_READ',actual_read_ranges=[[1,identity['lines']]],contribution=packet,semantic_qualification='Finite complete literal/source meanings in twelve manual facts; no downstream/domain/native global approval.')
assert len({e['path'] for e in ledger['records'] if e.get('repo')=='R' and e.get('status')=='FULL_READ' and e['path'].startswith('PBS/')})==27
assert len({e['path'] for e in ledger['records'] if e.get('repo')=='R' and e.get('status')=='FULL_READ' and not e['path'].startswith('PBS/')})==109
ledger['updated_utc']=START
write('reading-ledger.json',ledger)
cons=load('consumer-candidate-dispositions.json')
for entry in cons['records']:
    fact=mapping.get(entry['id'])
    if fact:
        assert entry['status']=='OPEN_NOT_YET_SEMANTICALLY_RECEIVED'
        entry.update(status='RECEIVED_LOCAL_STATIC_DOWNSTREAM_OPEN',own_full_source_read=True,actual_reader='/root/kernel_atomic_reception',meaning=fact['meaning'],premises_and_failure_prefix=manual['common_premise']+' '+fact['failure_prefix'],pending=fact['open'],manual_fact=fact['id'],contribution=packet)
cons['summary']=dict(collections.Counter(e['status'] for e in cons['records']))
cons['updated_utc']=START
cons['encounter10_local_reception']=packet
write('consumer-candidate-dispositions.json',cons)
facts=load('sourcefact-consumer-receptions.json')
facts['named_contributions'].append({'id':'OWN-ENCOUNTER-FIVE-FIXTURES-10CONSUMERS','complete_contribution':packet,'actual_reader':'/root/kernel_atomic_reception','complete_physical_PBS_paths':5,'records':95,'methods':260,'slots':1100,'manual_facts':12,'specific_lexical_consumers':10,'whole_domain_received':False})
facts['updated_utc']=START
write('sourcefact-consumer-receptions.json',facts)
inp=load('input-identities.json');inp['five_encounter_fixture_identities']=[f['identity'] for f in files];inp['wild_encounter_source_identity']=identities[0];inp['updated_utc']=START;write('input-identities.json',inp)
result=dict(packet,utc=START,PBS_full=27,nonPBS_full=109,manual_facts=12,records=95,methods=260,slots=1100,candidate_summary=cons['summary'])
stdout=json.dumps(result,ensure_ascii=False)+'\n';io=BASE/'io'
(io/'encounter-fixtures-integration.stdout.txt').write_text(stdout)
(io/'encounter-fixtures-integration.stderr.txt').write_text('')
(io/'encounter-fixtures-integration.json').write_text(json.dumps({'id':'encounter-fixtures-integration','started_utc':START,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'underlying_exit_code':0,'stdout_path':str(io/'encounter-fixtures-integration.stdout.txt'),'stderr_path':str(io/'encounter-fixtures-integration.stderr.txt'),'command':'python freeze-encounter-fixtures-consumers.py','reading_credit':'Already actually read raw files and manually authored meanings only; counts/reconstruction tool validation.'},indent=2)+'\n')
print(stdout,end='')
