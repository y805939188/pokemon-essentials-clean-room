"""Record actually read complete sources with eight manually authored finite facts."""
from pathlib import Path
import collections
import datetime
import hashlib
import json
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
identities=[]
units=[]
sources=[('Data/Scripts/005_Sprites/004_Sprite_Reflection.rb',89,'reflection-and-wild-modifiers-full'),('Data/Scripts/012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb',73,'reflection-and-wild-modifiers-full'),('Data/Scripts/005_Sprites/006_Spriteset_Global.rb',56,'spritesets-global-map-full'),('Data/Scripts/005_Sprites/007_Spriteset_Map.rb',131,'spritesets-global-map-full')]
for path,expected,evidence in sources:
    raw,identity=source(path);assert identity['lines']==expected
    identity.update(status='FULL_READ',reading_evidence='io/'+evidence+'.json')
    identities.append(identity)
    units.append({'path':path,'range':[1,expected],'text':raw.decode('utf-8-sig'),'qualification':'Own actual whole source read; semantic acceptance limited to named manual facts and exact downstream OPEN'})
for path,ranges,status in [('Data/Scripts/010_Data/001_Hardcoded data/008_Stat.rb',None,'FULL_READ_PREVIOUS'),('Data/Scripts/014_Pokemon/001_Pokemon.rb',[[1,104],[113,115],[390,400],[1099,1127]],'PARTIAL_READ_COMPLETE_NECESSARY_UNITS'),('Data/Scripts/001_Settings.rb',[[17,17],[69,74],[135,141],[377,383],[431,440]],'FULL_READ_PREVIOUS_SELECTED_DECLARATIONS')]:
    raw,identity=source(path);identity['status']=status;identities.append(identity);lines=raw.decode('utf-8-sig').splitlines(keepends=True)
    for lo,hi in ranges or [[1,len(lines)]]:
        assert hi<=len(lines)
        units.append({'path':path,'range':[lo,hi],'text':''.join(lines[lo-1:hi]),'qualification':status})
manual=load('visual-wild12.manual.json');assert len(manual['facts'])==8
mapping={f'KAR-CONSUMER-{n:04d}':fact for fact in manual['facts'] for n in fact['candidates']};assert len(mapping)==12
payload={'schema':'KAR-visual-wild12-contribution.v1','created_utc':START,'actual_reader':'/root/kernel_atomic_reception','fixed_R':FIXED,'source_identities':identities,'source_units':units,'manual_facts':manual['facts'],'common_premise':manual['common_premise'],'candidate_to_fact':{k:v['id'] for k,v in mapping.items()},'persistence':'These classes/callbacks do not save files. Generated Pokemon fields persist only through existing selected party/storage/player outer-object registration and actual later save/load, whose complete contracts were received separately; no inner/native roundtrip certified. Reflection/viewport objects are native/transient, no saved registration inferred.','open':'Full renderer/resource/other callback universe and dynamic/transitive consumer denominator remain OPEN. All native execution unperformed.','business_execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','new_required_contexts_votes':0}
write('visual-wild12-contribution.v1.json',payload)
raw=(BASE/'visual-wild12-contribution.v1.json').read_bytes();packet={'path':'visual-wild12-contribution.v1.json','bytes':len(raw),'sha256':sha(raw)}
ledger=load('reading-ledger.json')
for identity in identities[:4]:
    entry=next((e for e in ledger['records'] if e.get('repo')=='R' and e.get('path')==identity['path']),None)
    if entry is None:entry={'repo':'R','path':identity['path']};ledger['records'].append(entry)
    entry.update(identity,reader='/root/kernel_atomic_reception',actual_read_ranges=[[1,identity['lines']]],contribution=packet,semantic_qualification='Eight finite manual facts and exact candidate bindings only; no native/global domain acceptance.')
pokemon=next(e for e in ledger['records'] if e.get('repo')=='R' and e.get('path')=='Data/Scripts/014_Pokemon/001_Pokemon.rb')
assert pokemon['status']!='FULL_READ'
pokemon.setdefault('actual_read_ranges',[]).append([390,400]);pokemon.setdefault('later_read_evidence',[]).append('io/pokemon-shiny-complete-receiver.json')
assert len({e['path'] for e in ledger['records'] if e.get('repo')=='R' and e.get('status')=='FULL_READ' and not e['path'].startswith('PBS/')})==113
ledger['updated_utc']=START;write('reading-ledger.json',ledger)
cons=load('consumer-candidate-dispositions.json')
for entry in cons['records']:
    fact=mapping.get(entry['id'])
    if fact:
        assert entry['status']=='OPEN_NOT_YET_SEMANTICALLY_RECEIVED'
        entry.update(status='RECEIVED_LOCAL_STATIC_DOWNSTREAM_OPEN',own_full_source_read=True,actual_reader='/root/kernel_atomic_reception',meaning=fact['meaning'],premises_and_failure_prefix=manual['common_premise']+' '+fact['failure_prefix'],pending=fact['open'],manual_fact=fact['id'],contribution=packet)
cons['summary']=dict(collections.Counter(e['status'] for e in cons['records']));cons['updated_utc']=START;cons['visual_wild12_local_reception']=packet;write('consumer-candidate-dispositions.json',cons)
facts=load('sourcefact-consumer-receptions.json');facts['named_contributions'].append({'id':'OWN-VISUAL-WILD12','complete_contribution':packet,'actual_reader':'/root/kernel_atomic_reception','manual_facts':8,'specific_lexical_candidates':12,'own_full_sources':4,'whole_domain_received':False});facts['updated_utc']=START;write('sourcefact-consumer-receptions.json',facts)
inp=load('input-identities.json');inp['visual_wild12_source_identities']=identities;inp['updated_utc']=START;write('input-identities.json',inp)
stdout=json.dumps(dict(packet,utc=START,nonPBS_full=113,candidate_summary=cons['summary']),ensure_ascii=False)+'\n';io=BASE/'io'
(io/'visual-wild12-integration.stdout.txt').write_text(stdout);(io/'visual-wild12-integration.stderr.txt').write_text('')
(io/'visual-wild12-integration.json').write_text(json.dumps({'id':'visual-wild12-integration','started_utc':START,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'underlying_exit_code':0,'command':'python freeze-visual-wild12.py','stdout_path':str(io/'visual-wild12-integration.stdout.txt'),'stderr_path':str(io/'visual-wild12-integration.stderr.txt'),'reading_credit':'Actual preceding full I/O and manual facts; extraction/count tools do not supply semantic credit.'},indent=2)+'\n')
print(stdout,end='')
