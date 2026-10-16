"""Preserve all three actually read literal fixtures and finite manual meanings."""
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
files=[]
for path,evidence,expected_records,expected_fields in [('PBS/ribbons.txt','pbs-ribbons-full',80,240),('PBS/trainer_types.txt','pbs-trainer-types-full',72,256),('PBS/trainers.txt','pbs-trainers-full',20,77)]:
    raw=(R/path).read_bytes()
    assert subprocess.run(['git','show',FIXED+':'+path],cwd=R,capture_output=True,check=True).stdout==raw
    identity={'repo':'R','path':path,'bytes':len(raw),'sha256':sha(raw),'git_blob':subprocess.run(['git','rev-parse',FIXED+':'+path],cwd=R,capture_output=True,text=True,check=True).stdout.strip(),'fixed_R':FIXED,'lines':len(raw.decode('utf-8-sig').splitlines()),'actual_reader':'/root/kernel_atomic_reception','status':'FULL_READ','reading_evidence':'io/'+evidence+'.json'}
    records=[]
    current=None
    member=None
    for lineno,line in enumerate(raw.decode('utf-8-sig').splitlines(),1):
        stripped=line.strip()
        if not stripped or stripped.startswith('#'):continue
        if stripped.startswith('[') and stripped.endswith(']'):
            if current:current['source_range'][1]=lineno-1
            current={'ordinal':len(records)+1,'id_literal':stripped[1:-1],'source_range':[lineno,identity['lines']],'fields':[]}
            records.append(current)
            member=None
            if path=='PBS/trainers.txt':
                header=current['id_literal'].split(',')
                assert len(header) in (2,3)
                current['compound_id']=[header[0],header[1],int(header[2]) if len(header)==3 else 0]
                current['pokemon_members']=[]
            continue
        match=re.fullmatch(r'\s*(\w+)\s*=\s*(.*)',line)
        assert current is not None and match,(path,lineno,line)
        key,value=match.groups()
        field={'line':lineno,'key':key,'original_value':value,'original_line':line}
        if path=='PBS/trainers.txt':
            if key=='Pokemon':
                parts=value.split(',');assert len(parts)==2
                member={'ordinal':len(current['pokemon_members'])+1,'pokemon_source_line':lineno,'species_literal':parts[0],'level':int(parts[1]),'fields':[]}
                current['pokemon_members'].append(member)
            elif key not in ('Items','LoseText'):
                assert member is not None
                member['fields'].append(dict(field))
            field['member_ordinal']=member['ordinal'] if key not in ('Items','LoseText') else None
        current['fields'].append(field)
    assert len(records)==expected_records and sum(len(record['fields']) for record in records)==expected_fields
    assert len({record['id_literal'] for record in records})==len(records)
    for record in records:
        props={field['key']:field['original_value'] for field in record['fields']}
        if path=='PBS/ribbons.txt':
            assert set(props)=={'Name','IconPosition','Description'}
            record['constructor_projection']={'id_symbol_text':record['id_literal'],'real_name':props['Name'],'icon_position':int(props['IconPosition']),'real_description':props['Description'],'flags':[],'pbs_file_suffix':''}
        elif path=='PBS/trainer_types.txt':
            money=int(props['BaseMoney'])
            record['constructor_projection']={'id_symbol_text':record['id_literal'],'real_name':props['Name'],'gender':{'Male':0,'Female':1,'Unknown':2}[props['Gender']],'base_money':money,'skill_level':int(props['SkillLevel']) if 'SkillLevel' in props else money,'flags':[],'intro_BGM':None,'battle_BGM':props.get('BattleBGM'),'victory_BGM':props.get('VictoryBGM'),'pbs_file_suffix':''}
        else:
            record['outer_constructor_projection']={'id':record['compound_id'],'trainer_type_symbol_text':record['compound_id'][0],'real_name':record['compound_id'][1],'version':record['compound_id'][2],'items_symbol_texts':props['Items'].split(',') if 'Items' in props else [],'real_lose_text':props['LoseText'],'pbs_file_suffix':''}
            for member in record['pokemon_members']:
                properties={field['key']:field['original_value'] for field in member['fields']}
                projections={}
                for key,value in properties.items():
                    if key in ('Form','AbilityIndex','Happiness'):projections[key]=int(value)
                    elif key in ('Shiny','SuperShiny','Shadow'):projections[key]=value.lower()=='true'
                    elif key=='Gender':projections[key]={'male':0,'female':1}[value]
                    elif key in ('IV','EV'):projections[key]=[int(token) for token in value.split(',')]
                    elif key in ('Moves',):projections[key]={'ordered_reference_symbol_texts':value.split(','),'lookup_success_not_granted':True}
                    elif key in ('Ability','Item','Nature','Ball'):projections[key]={'reference_symbol_text':value,'lookup_success_not_granted':True}
                    else:projections[key]=value
                member['conditional_parser_field_projections']=projections
                member['all_omitted_subschema_keys']=[key for key in ['Form','Name','Moves','Ability','AbilityIndex','Item','Gender','Nature','IV','EV','Happiness','Shiny','SuperShiny','Shadow','Ball'] if key not in properties]
                member['conditional_factory_fallbacks']={'IV_each_when_omitted':min(member['level']//2,31) if 'IV' not in properties else None,'EV_each_when_omitted':min(member['level']*3//2,85) if 'EV' not in properties else None,'moves_when_omitted':'Pokemon.reset_moves using exact Species move list; literal list remains unreceived here','gender_when_omitted':'trainer.male? ? 0 : 1; source receiver/loaded trainer type precondition','nature_when_omitted':'(Species.keys.index(base_species) + TrainerType.keys.index(type)) % Nature.count, each missing index fallback1; whole species order not received'}
    if path=='PBS/ribbons.txt':assert [record['constructor_projection']['icon_position'] for record in records]==list(range(80))
    if path=='PBS/trainers.txt':assert sum(len(record['pokemon_members']) for record in records)==39
    files.append({'identity':identity,'raw_text_including_BOM_if_present':raw.decode('utf-8'),'records':records,'literal_read_qualification':'All raw physical lines and every complete record personally actually read; extraction/count/projection validation itself grants no semantic credit.'})

manual=load('ribbon-trainer-fixtures.manual.json')
packet={'schema':'KAR-three-ribbon-trainer-fixtures.v1','recorded_utc':START,'actual_reader':'/root/kernel_atomic_reception','fixed_R':FIXED,'files':files,'complete_manual_facts':manual['facts'],'common_premise':manual['common_premise'],'source_definition_support':'Own prior full Generic/Ribbon/TrainerType/Trainer and Compiler1–4 sources; current complete definition rereads retain same reader, not extra sourceFULL. Exact schemas/defaults/parse/write/messages belong named manual facts.','business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED','open':'All51 other physical PBS files remain available unreceived here. Full species/move/item literal corpus, current loaded compiled data and complete native/domain consumers are not granted by these three author fixtures.'}
write('three-ribbon-trainer-fixtures-contribution.v1.json',packet)
packet_raw=(BASE/'three-ribbon-trainer-fixtures-contribution.v1.json').read_bytes()
packet_identity={'path':'three-ribbon-trainer-fixtures-contribution.v1.json','bytes':len(packet_raw),'sha256':sha(packet_raw)}
ledger=load('reading-ledger.json')
for file in files:
    identity=file['identity']
    record=next((entry for entry in ledger['records'] if entry.get('repo')=='R' and entry.get('path')==identity['path']),None)
    if record is None:
        record={'repo':'R','path':identity['path']};ledger['records'].append(record)
    record.update(identity)
    record['reader']='/root/kernel_atomic_reception'
    record['actual_read_ranges']=[[1,identity['lines']]]
    record['complete_record_count']=len(file['records'])
    record['semantic_qualification']='All explicit literals, ordering and omitted-field distinctions personally read; conditional source transformations and exact consumer dependencies remain finite and open as stated in manual facts.'
    record['contribution']=dict(packet_identity)
pbs_full={entry['path'] for entry in ledger['records'] if entry.get('repo')=='R' and entry.get('status')=='FULL_READ' and entry['path'].startswith('PBS/')}
assert len(pbs_full)==22
ledger['updated_utc']=START
write('reading-ledger.json',ledger)
inp=load('input-identities.json')
inp['three_ribbon_trainer_fixtures_identities']=[file['identity'] for file in files]
inp['updated_utc']=START
write('input-identities.json',inp)
facts=load('sourcefact-consumer-receptions.json')
facts['named_contributions'].append({'id':'OWN-THREE-RT-FIXTURES','complete_contribution':packet_identity,'complete_physical_PBS_paths':3,'complete_records':172,'complete_trainer_members':39,'manual_facts':6,'actual_reader':'/root/kernel_atomic_reception','whole_domain_received':False,'qualification':'Literal complete source fixtures; no full referenced Species/Move/Item corpus or actual native compiler/factory success.'})
facts['updated_utc']=START
write('sourcefact-consumer-receptions.json',facts)
stdout=json.dumps(dict(packet_identity,utc=START,PBS_full=22,PBS_remaining=51,records=172,trainer_members=39,manual_facts=6,business='NOT_EXECUTED',new_required_contexts_votes=0),ensure_ascii=False)+'\n'
io=BASE/'io'
(io/'three-rt-fixtures-integration.stdout.txt').write_text(stdout)
(io/'three-rt-fixtures-integration.stderr.txt').write_text('')
(io/'three-rt-fixtures-integration.json').write_text(json.dumps({'id':'three-rt-fixtures-integration','started_utc':START,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'underlying_exit_code':0,'stdout_path':str(io/'three-rt-fixtures-integration.stdout.txt'),'stderr_path':str(io/'three-rt-fixtures-integration.stderr.txt'),'command':'python integrate-ribbon-trainer-fixtures.py','reading_credit':'Only the already actually read920L raw text and six manually authored finite meanings; reconstruction checks are tool validation, not semantic credit.','business_execution':'NOT_EXECUTED'},indent=2)+'\n')
print(stdout,end='')
