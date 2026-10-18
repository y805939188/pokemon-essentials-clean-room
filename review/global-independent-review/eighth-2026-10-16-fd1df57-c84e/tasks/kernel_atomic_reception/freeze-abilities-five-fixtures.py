"""Freeze all actually read five physical ability fixtures and finite manual support."""
from pathlib import Path
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
    raw=(R/path).read_bytes();assert raw==subprocess.run(['git','show',FIXED+':'+path],cwd=R,capture_output=True,check=True).stdout
    return raw,{'repo':'R','path':path,'bytes':len(raw),'sha256':sha(raw),'git_blob':subprocess.run(['git','rev-parse',FIXED+':'+path],cwd=R,capture_output=True,text=True,check=True).stdout.strip(),'fixed_R':FIXED,'lines':len(raw.decode('utf-8-sig').splitlines()),'actual_reader':'/root/kernel_atomic_reception'}
files=[]
specs=[('PBS/Gen 5 backup/abilities.txt',164,659,['pbs-abilities-gen5-001-340','pbs-abilities-gen5-341-659']),('PBS/Gen 6 backup/abilities.txt',191,767,['pbs-abilities-gen6-001-385','pbs-abilities-gen6-386-767']),('PBS/Gen 7 backup/abilities.txt',233,935,['pbs-abilities-gen7-001-470','pbs-abilities-gen7-471-935']),('PBS/Gen 8 backup/abilities.txt',267,1072,['pbs-abilities-gen8-001-540','pbs-abilities-gen8-541-1072']),('PBS/abilities.txt',267,1072,['pbs-abilities-default-001-540','pbs-abilities-default-541-1072'])]
for path,count,expected,evidence in specs:
    raw,identity=source(path);assert identity['lines']==expected
    identity.update(status='FULL_READ',reading_evidence=['io/'+e+'.json' for e in evidence])
    records=[];current=None
    for lineno,line in enumerate(raw.decode('utf-8-sig').splitlines(),1):
        prepared=line.strip()
        if not prepared or prepared.startswith('#'):continue
        if prepared.startswith('['):
            assert re.fullmatch(r'\[\w+\]',prepared)
            if current:current['source_range'][1]=lineno-1
            current={'ordinal':len(records)+1,'id_symbol_text':prepared[1:-1],'source_range':[lineno,expected],'fields':[]};records.append(current)
        else:
            match=re.fullmatch(r'(\w+)\s*=\s*(.*)',line);assert match and current
            key,value=match.groups();assert key in ('Name','Description','Flags')
            current['fields'].append({'line':lineno,'key':key,'original_value':value,'original_line':line})
    assert len(records)==count and len({r['id_symbol_text'] for r in records})==count
    for record in records:
        props={f['key']:f['original_value'] for f in record['fields']};assert set(props) in ({'Name','Description'},{'Name','Description','Flags'})
        flags=props['Flags'].split(',') if 'Flags'in props else []
        record['conditional_constructor_projection']={'id_symbol_text':record['id_symbol_text'],'real_name':props['Name'],'real_description':props['Description'],'flags':flags,'pbs_file_suffix':''}
        record['omitted_schema_fields']=['Flags'] if 'Flags'not in props else []
        record['qualification']='All original fields personally actually read; normal fixed schema/constructor projection, not target/native execution or battle-effect meaning.'
    files.append({'identity':identity,'raw_text_including_BOM_if_present':raw.decode('utf-8'),'records':records,'reading_credit':'All physical lines and every complete record actually displayed/read for this specific path; same blob alone grants no credit.'})
assert sum(len(f['records']) for f in files)==1122
assert sum(len(r['fields']) for f in files for r in f['records'])==2256
manual=load('abilities-five-fixtures.manual.json');assert len(manual['facts'])==5
units=[];identities=[]
for path,ranges,qualification in [('Data/Scripts/010_Data/002_PBS data/004_Ability.rb',None,'Own previous whole45 source'),('Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',[[4,68],[181,200]],'Own previous whole source; complete selected generic+ability methods'),('Data/Scripts/010_Data/001_GameData.rb',None,'Own previous whole283 generic source; only named ability contracts adopted'),('Data/Scripts/016_UI/001_Non-interactive UI/003_UI_EggHatching.rb',[[252,268]],'Own complete selected event registration only; parent not FULL')]:
    raw,identity=source(path);identity['qualification']=qualification;identities.append(identity);ls=raw.decode('utf-8-sig').splitlines(keepends=True)
    for lo,hi in ranges or [[1,len(ls)]]:units.append({'path':path,'range':[lo,hi],'text':''.join(ls[lo-1:hi]),'source_sha256':identity['sha256'],'qualification':qualification})
payload={'schema':'KAR-five-complete-ability-fixtures.v1','created_utc':START,'actual_reader':'/root/kernel_atomic_reception','fixed_R':FIXED,'files':files,'manual_facts':manual['facts'],'common_premise':manual['common_premise'],'source_identities':identities,'source_units':units,'open':'Other41 physical PBS remain available not yet received here; full battle/AI/hatch/render/native/save/runtime language successors not granted.','business_execution':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','new_required_contexts_votes':0}
name='five-abilities-fixtures-contribution.v1.json';assert not (BASE/name).exists();write(name,payload);raw=(BASE/name).read_bytes();packet={'path':name,'bytes':len(raw),'sha256':sha(raw)}
ledger=load('reading-ledger.json')
for file in files:
    identity=file['identity'];entry=next((e for e in ledger['records'] if e.get('repo')=='R' and e.get('path')==identity['path']),None)
    if entry is None:entry={'repo':'R','path':identity['path']};ledger['records'].append(entry)
    entry.update(identity,reader='/root/kernel_atomic_reception',actual_read_ranges=[[1,identity['lines']]],complete_record_count=len(file['records']),contribution=packet,semantic_qualification='Complete literal/scheme/default/message/flag semantics as five manually authored facts; all gameplay effects not inherited from descriptions.')
path=identities[-1]['path'];entry=next((e for e in ledger['records'] if e.get('repo')=='R' and e.get('path')==path),None)
if entry is None:ledger['records'].append(dict(identities[-1],status='PARTIAL_READ_COMPLETE_NAMED_UNITS',reader='/root/kernel_atomic_reception',actual_read_ranges=[[252,268]],reading_evidence='io/ability-hatching-flag-complete-consumer.json',contribution=packet))
elif entry['status']!='FULL_READ':entry.setdefault('actual_read_ranges',[]).append([252,268]);entry.setdefault('later_read_evidence',[]).append('io/ability-hatching-flag-complete-consumer.json')
assert len({e['path'] for e in ledger['records'] if e.get('repo')=='R' and e.get('status')=='FULL_READ' and e['path'].startswith('PBS/')})==32
ledger['updated_utc']=START;write('reading-ledger.json',ledger)
facts=load('sourcefact-consumer-receptions.json');facts['named_contributions'].append({'id':'OWN-FIVE-ABILITY-FIXTURES','complete_contribution':packet,'actual_reader':'/root/kernel_atomic_reception','complete_physical_PBS_paths':5,'complete_records':1122,'explicit_fields':2256,'manual_facts':5,'whole_domain_received':False});facts['updated_utc']=START;write('sourcefact-consumer-receptions.json',facts)
inp=load('input-identities.json');inp['five_ability_fixture_identities']=[f['identity'] for f in files];inp['updated_utc']=START;write('input-identities.json',inp)
stdout=json.dumps(dict(packet,utc=START,PBS_full=32,complete_records=1122,explicit_fields=2256,manual_facts=5),ensure_ascii=False)+'\n';io=BASE/'io';(io/'five-abilities-integration.stdout.txt').write_text(stdout);(io/'five-abilities-integration.stderr.txt').write_text('');(io/'five-abilities-integration.json').write_text(json.dumps({'id':'five-abilities-integration','started_utc':START,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'underlying_exit_code':0,'command':'python freeze-abilities-five-fixtures.py','stdout_path':str(io/'five-abilities-integration.stdout.txt'),'stderr_path':str(io/'five-abilities-integration.stderr.txt'),'reading_credit':'Actual prior4505L raw reads and five manual facts; extraction/count/schema projections alone give no semantic credit.'},indent=2)+'\n');print(stdout,end='')
