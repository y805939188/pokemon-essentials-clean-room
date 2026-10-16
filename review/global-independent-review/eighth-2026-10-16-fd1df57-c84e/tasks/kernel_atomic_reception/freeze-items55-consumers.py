"""Freeze manually reconstructed item consumers and exact complete definitions."""
from pathlib import Path
import collections
import csv
import datetime
import hashlib
import json
import re
import subprocess

BASE = Path(__file__).resolve().parent
R = Path('/workspace/pokemon-essentials')
FIXED = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
START = datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(raw): return hashlib.sha256(raw).hexdigest()
def load(name): return json.loads((BASE/name).read_text())
def write(name, obj): (BASE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def source(path):
    raw = (R/path).read_bytes()
    fixed = subprocess.run(['git','show',FIXED+':'+path],cwd=R,capture_output=True,check=True).stdout
    assert raw == fixed
    identity = {'path':path,'bytes':len(raw),'sha256':sha(raw),'git_blob':subprocess.run(['git','rev-parse',FIXED+':'+path],cwd=R,capture_output=True,text=True,check=True).stdout.strip(),'fixed_commit':FIXED,'lines':len(raw.decode('utf-8-sig').splitlines()),'actual_reader':'/root/kernel_atomic_reception'}
    return raw.decode('utf-8-sig').splitlines(keepends=True), identity

rows = list(csv.DictReader((BASE/'items55-consumer-facts.manual.tsv').open(), delimiter='\t'))
assert len(rows) == 15 and len({row['id'] for row in rows}) == 15
candidate_to_fact = {}
for row in rows:
    assert None not in row and all(row.values())
    for number in row['candidate_numbers'].split(','):
        key = f'KAR-CONSUMER-{int(number):04d}'
        assert key not in candidate_to_fact
        candidate_to_fact[key] = row['id']
assert len(candidate_to_fact) == 55

own_full = {
 'Data/Scripts/013_Items/001_Item_Utilities.rb':['items-utilities-001-310','items-utilities-311-620','items-utilities-621-917'],
 'Data/Scripts/013_Items/002_Item_Effects.rb':['items-effects-001-330','items-effects-331-660','items-effects-661-990','items-effects-991-1260','items-effects-1261-1524'],
 'Data/Scripts/013_Items/003_Item_BattleEffects.rb':['items-battle-effects-001-360','items-battle-effects-361-712'],
 'Data/Scripts/013_Items/005_Item_PokeRadar.rb':['items-radar-001-267'],
 'Data/Scripts/014_Pokemon/004_Pokemon_Move.rb':['items-receiver-move77'],
}
identities = []
units = []
for path, evidence in own_full.items():
    lines, identity = source(path)
    identity['reading_evidence'] = ['io/'+key+'.json' for key in evidence]
    identity['own_read_status'] = 'FULL_READ'
    identities.append(identity)
    units.append({'id':'ITEM-SOURCE-'+str(len(units)+1),'path':path,'range':[1,len(lines)],'complete_unit':'Whole fixed source personally actually read; finite semantic acceptance only for named facts','text':''.join(lines),'identity_sha256':identity['sha256']})

pokemon_path = 'Data/Scripts/014_Pokemon/001_Pokemon.rb'
lines, pokemon_identity = source(pokemon_path)
pokemon_identity['own_read_status'] = 'PARTIAL_READ_COMPLETE_NAMED_METHODS'
pokemon_identity['actual_read_ranges'] = [[1,104],[108,117],[188,309],[497,538],[552,581],[599,671],[923,981],[1028,1060],[1062,1147],[1159,1226]]
pokemon_identity['reading_evidence'] = ['io/items-receiver-pokemon-health-level.json','io/items-receiver-pokemon-happiness-stats.json','io/items-receiver-pokemon-identity-nature-moves-evo.json']
identities.append(pokemon_identity)
selected = {'level','level=','exp=','egg?','growth_rate','hp=','status=','able?','fainted?','heal_HP','heal_status','heal_PP','heal','baseStats','calcIV','calcHP','calcStat','calc_stats','nature','nature=','nature_for_stats','nature_for_stats=','initialize','changeHappiness','item','item=','hasItem?','numMoves','hasMove?','getMoveList','reset_moves','learn_move','forget_move','species_data','check_evolution_on_level_up','check_evolution_internal'}
method_ranges = {}
for start, line in enumerate(lines,1):
    match = re.match(r'^  def ([^ (;\s]+)', line)
    if not match or match[1] not in selected: continue
    end = next(j for j in range(start,len(lines)+1) if lines[j-1].rstrip('\r\n') == '  end')
    assert any(a <= start and end <= z for a,z in pokemon_identity['actual_read_ranges']), (match[1],start,end)
    method_ranges[match[1]] = [start,end]
    units.append({'id':'POKEMON-'+match[1],'path':pokemon_path,'range':[start,end],'complete_unit':'This named method only; whole Pokemon source remains PARTIAL','text':''.join(lines[start-1:end]),'identity_sha256':pokemon_identity['sha256']})
assert selected == set(method_ranges)
units.append({'id':'POKEMON-DECLARATIONS','path':pokemon_path,'range':[1,98],'complete_unit':'Actual attr/constant declarations; class and following methods not claimed complete by this slice','text':''.join(lines[:98]),'identity_sha256':pokemon_identity['sha256']})

for path, ranges in [('Data/Scripts/001_Settings.rb',[[17,17],[135,146],[233,253],[405,411]]),('Data/Scripts/002_BattleSettings.rb',[[1,140]])]:
    config_lines, identity = source(path)
    identity['own_read_status'] = 'FULL_READ_PREVIOUSLY; selected declarations included for finite use'
    identities.append(identity)
    for a,z in ranges:
        assert z <= len(config_lines)
        units.append({'id':'CONFIG-'+str(len(units)+1),'path':path,'range':[a,z],'complete_unit':'Whole BattleSettings or complete declaration statements exactly as labelled; source whole-read credit was previously recorded','text':''.join(config_lines[a-1:z]),'identity_sha256':identity['sha256']})

receiver = load('items-receiver-facts.manual.json')
payload = {
 'schema':'KAR-items55-consumers.v1','created_utc':START,'actual_reader':'/root/kernel_atomic_reception','fixed_R':FIXED,
 'manual_facts':rows,'receiver_facts':receiver['facts'],'source_identities':identities,'source_units':units,
 'candidate_to_fact':candidate_to_fact,'necessary_receiver_method_ranges':method_ranges,
 'common_premises':['Fixed unmodified R and B8; default Settings declarations evaluate at loading, callbacks excluded from override unless explicitly named.','All four Items sources and Move77 were personally actually read in full in the listed I/O windows; Pokemon only the selected complete methods/declarations was read here.','Generic GameData and concrete Stat/Nature/Move/Species/Item definitions, HandlerHashSymbol/EventHandlers and SaveData default17 mechanism were already personally actually read; their existing finite facts remain scoped.','Native RNG uniform legal integer offsets is a conditional WP06 premise, never a measured distribution.','Calls to native scene/audio/animation/battle APIs are requests with prefixes; success of downstream work is not inferred from a caller reaching the request.'],
 'persistence':'Stats and Global metadata persist through their existing registered outer objects; GameTemp Radar chain is not among17 saved registrations. Full SaveData source mechanism and failure prefixes remain in creature-save-events-contribution.json SAVE01–07/core-stats-variables-save-contribution.v1.json; these named units do not certify native roundtrip, all old save shapes or inner compatibility.',
 'open':['All other original lexical candidates and dynamic/transitive consumers retain their explicit ledger states.','Radar animation renderer, WildEncounter/flute/repel/rod receiver domains and every arbitrary evolution/ability callback not fully received by these item units.','55 local static candidates now have exact finite meanings and failures; no whole Settings/Stats/Items/Creature/UI domain approval.','Target business/game/Ruby/native NOT_EXECUTED; UPDATE_NOT_STARTED.'],
 'original_providers_retained':'Existing CRE lifecycle/evolution and UI finite receptions keep their original actual reader and receipt; no sourceFULL transferred by alias or same blob.',
 'new_required_contexts_votes':0,
}
write('items55-consumers-contribution.v1.json',payload)

packet_raw = (BASE/'items55-consumers-contribution.v1.json').read_bytes()
packet_identity = {'path':'items55-consumers-contribution.v1.json','bytes':len(packet_raw),'sha256':sha(packet_raw)}
ledger = load('reading-ledger.json')
for identity in identities[:5]:
    path = identity['path']
    matched = next((entry for entry in ledger['records'] if entry.get('repo')=='R' and entry.get('path')==path),None)
    if matched is None:
        matched = {'repo':'R','path':path}
        ledger['records'].append(matched)
    matched.update(identity)
    matched['status'] = 'FULL_READ'
    matched['reader'] = '/root/kernel_atomic_reception'
    matched['actual_read_ranges'] = [[1,identity['lines']]]
    matched['full_read_credit'] = 'Own actual contiguous full I/O outputs; source identity checked against fixed Git. Does not grant all consumer semantics.'
matched = next((entry for entry in ledger['records'] if entry.get('repo')=='R' and entry.get('path')==pokemon_path),None)
if matched is None:
    matched = {'repo':'R','path':pokemon_path,'status':'PARTIAL_READ_COMPLETE_NAMED_UNITS'}
    ledger['records'].append(matched)
assert matched['status'] != 'FULL_READ', 'Do not silently overwrite an independent whole-source status'
old_ranges = matched.get('actual_read_ranges',[])
matched.update(pokemon_identity)
matched['status'] = 'PARTIAL_READ_COMPLETE_NAMED_UNITS'
matched['actual_read_ranges'] = sorted({tuple(pair) for pair in old_ranges+pokemon_identity['actual_read_ranges']})
matched['complete_units'] = sorted(set(matched.get('complete_units',[]))|set(method_ranges))
matched['whole_file_read'] = False
full_non_pbs = {entry['path'] for entry in ledger['records'] if entry.get('repo')=='R' and entry.get('status')=='FULL_READ' and not entry['path'].startswith('PBS/')}
assert len(full_non_pbs) == 108, len(full_non_pbs)
ledger['own_reference_full_read_non_PBS'] = 108
ledger['updated_utc'] = START
write('reading-ledger.json',ledger)

consumers = load('consumer-candidate-dispositions.json')
record_by_id = {record['id']:record for record in consumers['records']}
fact_by_id = {row['id']:row for row in rows}
expected_paths = set(own_full)-{'Data/Scripts/014_Pokemon/004_Pokemon_Move.rb'}
for candidate, fact_id in candidate_to_fact.items():
    record = record_by_id[candidate]
    assert record['status']=='OPEN_NOT_YET_SEMANTICALLY_RECEIVED', (candidate,record['status'])
    assert record['path'] in expected_paths
    fact = fact_by_id[fact_id]
    record['status'] = 'RECEIVED_LOCAL_STATIC_DOWNSTREAM_OPEN'
    record['own_full_source_read'] = True
    record['actual_receiver'] = '/root/kernel_atomic_reception'
    record['complete_contribution'] = dict(packet_identity,fact_id=fact_id)
    record['actual_finite_meaning'] = fact['meaning']
    record['read_time_and_default'] = fact['read_time_and_default']
    record['failure_prefix_and_normal_cancel'] = fact['failure_prefix_and_normal_cancel']
    record['pending'] = fact['remaining_scope']
    record['whole_domain_accepted'] = False
consumers['summary'] = dict(collections.Counter(record['status'] for record in consumers['records']))
assert consumers['summary']['OPEN_NOT_YET_SEMANTICALLY_RECEIVED'] == 311
assert consumers['summary']['RECEIVED_LOCAL_STATIC_DOWNSTREAM_OPEN'] == 197
consumers['updated_utc'] = START
consumers['items55_local_reception'] = dict(packet_identity,manual_facts=15,receiver_facts=4,unique_candidate_count=55,new_own_full_sources=5,whole_domain_approvals_added=0)
write('consumer-candidate-dispositions.json',consumers)

facts = load('sourcefact-consumer-receptions.json')
facts.setdefault('named_contributions',[]).append({'id':'OWN-ITEMS-55','provider':'/root/kernel_atomic_reception','complete_contribution':packet_identity,'manual_complete_facts':15,'receiver_facts':4,'source_credit':'Own full five sources and own complete selected Pokemon methods only; provider CRE/UI finite credit unchanged.','whole_domain_received':False})
facts['updated_utc'] = START
write('sourcefact-consumer-receptions.json',facts)
inp = load('input-identities.json')
inp.setdefault('items55_own_full_and_partial_identities',[]).extend(identities)
inp['updated_utc'] = START
write('input-identities.json',inp)

outcome = dict(packet_identity,utc=START,manual_facts=15,receiver_facts=4,complete_source_units=len(units),whole_new_source_files=5,partial_Pokemon_methods=len(method_ranges),candidates=55,remaining_candidates=311,own_nonPBS_full=108,business_execution='NOT_EXECUTED',new_required_contexts_votes=0)
stdout = json.dumps(outcome,ensure_ascii=False)+'\n'
io = BASE/'io'
(io/'items55-freeze-integration.stdout.txt').write_text(stdout)
(io/'items55-freeze-integration.stderr.txt').write_text('')
(io/'items55-freeze-integration.json').write_text(json.dumps({'id':'items55-freeze-integration','started_utc':START,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'underlying_exit_code':0,'stdout_path':str(io/'items55-freeze-integration.stdout.txt'),'stderr_path':str(io/'items55-freeze-integration.stderr.txt'),'command':'python freeze-items55-consumers.py','business_execution':'NOT_EXECUTED','credit':'Only previously actually read complete I/O outputs and hand-authored exact meanings; no semantic acceptance from counting or identity validation.'},indent=2)+'\n')
print(stdout,end='')
