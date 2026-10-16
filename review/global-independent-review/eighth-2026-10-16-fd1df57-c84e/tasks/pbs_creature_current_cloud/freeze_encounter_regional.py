from pathlib import Path
import json, hashlib, subprocess, datetime, copy, re

P = Path(__file__).resolve().parent
ROOT = P.parent.parent
R = Path('/workspace/pokemon-essentials')
B = Path('/workspace/pokemon-essentials-clean-room')
RC = '8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
RT = '7589c800b61ba13a13040ed0d686979b80a84fd0'
BC = 'fd1df570cad987dc3852a3b958f03916e317f7fe'
BT = 'f292698cdd4a8e725525a9be6dc34b75faaf151e'
UTC = datetime.datetime.now(datetime.timezone.utc).isoformat()
READER = '/root/pbs_creature_current_cloud'

def load(n):
    return json.loads((P/n).read_text())

def save(n, obj):
    target = P/n
    assert not target.exists(), n
    target.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')
    raw = target.read_bytes()
    return {'path':n,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

def identity(repo, path, commit, tree):
    data = (repo/path).read_bytes()
    assert data == subprocess.check_output(['git','show',commit+':'+path],cwd=repo)
    return {'repo':str(repo),'path':path,'commit':commit,'tree':tree,
            'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
            'git_blob':subprocess.check_output(['git','rev-parse',commit+':'+path],cwd=repo,text=True).strip(),
            'lines':len(data.splitlines())}

def unit(path, a, b, label, repo=R):
    commit, tree = (RC,RT) if repo==R else (BC,BT)
    lines = (repo/path).read_text().splitlines(keepends=True)
    assert 1 <= a <= b <= len(lines)
    return {'label':label,'identity':identity(repo,path,commit,tree),'lines':[a,b],
            'complete_text':''.join(lines[a-1:b]),'actual_reader':READER,
            'credit':'Actually read complete named contained units; surrounding file FULL only where independently in reading-ledger. Integrity checks grant no reading credit.'}

ET='Data/Scripts/010_Data/001_Hardcoded data/013_EncounterType.rb'
ED='Data/Scripts/010_Data/002_PBS data/013_Encounter.rb'
C1='Data/Scripts/021_Compiler/001_Compiler.rb'
C2='Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb'
WR='Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb'
MISC='Data/Scripts/010_Data/002_PBS data/001_MiscPBSData.rb'
UTIL='Data/Scripts/019_Utilities/001_Utilities.rb'
WILD='Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb'
META='Data/Scripts/012_Overworld/002_Overworld_Metadata.rb'
PD='Data/Scripts/015_Trainers and player/005_Player_Pokedex.rb'
EDITOR='Data/Scripts/020_Debug/001_Editor screens/001_EditorScreens.rb'
DT='Data/Scripts/020_Debug/002_Editor_DataTypes.rb'
EU='Data/Scripts/020_Debug/001_Editor_Utilities.rb'
SP='Data/Scripts/010_Data/002_PBS data/008_Species.rb'
GD='Data/Scripts/010_Data/001_GameData.rb'
F36='deliverables/final-specification-set/creature-rpg/wp36-wild-encounters-and-modifiers.md'
F62='deliverables/final-specification-set/pokemon-rules/wp62-pokedex-records-regions-and-content.md'
FA='deliverables/final-specification-set/demo-dx/wp73-a-content-editors.md'
FB='deliverables/final-specification-set/demo-dx/wp73-b-world-editors.md'

# Frozen copying and serialization after actual full reading; no reference/Ruby,
# selector simulation, encounter probability audit or native editor execution.
units = [
 unit(ET,1,178,'All26 EncounterType registrations and complete constructor'),
 unit(ED,1,71,'Complete Encounter record/get/exists/each/each_of_version'),
 unit(C1,1,1117,'Compiler parser definitions already ownFULL, including strict enum and parseSpecies'),
 unit(C2,593,629,'Complete compile_regional_dexes'),
 unit(C2,658,765,'Complete compile_encounters'),
 unit(WR,364,446,'Complete write_regional_dexes, write_ribbons and write_encounters'),
 unit(MISC,1,64,'Complete MiscPBSData, especially lazy regional cache and clear'),
 unit(UTIL,378,419,'Complete current-region/number/list/length utilities'),
 unit(WILD,1,469,'Complete encounter session/trigger/selection/wild-constructor/wrapper'),
 unit(META,58,119,'Complete metadata constructor and encounter_version setter only'),
 unit(PD,1,361,'Complete Pokedex data consumer'),
 unit(EDITOR,6,124,'Complete encounter collection editor'),
 unit(EDITOR,128,252,'Complete map-version editor'),
 unit(EDITOR,256,340,'Complete encounter type/slot editor'),
 unit(EDITOR,992,1097,'Complete regional single-list editor'),
 unit(EDITOR,1099,1202,'Complete regional main editor'),
 unit(DT,56,128,'Complete LimitProperty, LimitProperty2, NonzeroLimitProperty'),
 unit(DT,448,473,'Complete SpeciesFormProperty'),
 unit(DT,1575,1619,'Complete EncounterSlotProperty'),
 unit(DT,1624,1706,'Complete property-list driver'),
 unit(EU,116,145,'Complete generic GameData selector and two Species selector entry methods'),
 unit(SP,1,455,'Complete Species source, including base/form identity and family methods'),
 unit(GD,1,283,'Complete data registry mixins'),
]

catalog = []
text=(R/ET).read_text()
blocks=list(re.finditer(r'GameData::EncounterType\.register\(\{(.*?)\}\)',text,re.S))
for i,m in enumerate(blocks,1):
    body=m.group(1)
    name=re.search(r':id\s*=>\s*:(\w+)',body).group(1)
    family=re.search(r':type\s*=>\s*:(\w+)',body).group(1)
    rate=re.search(r':trigger_chance\s*=>\s*(\d+)',body)
    catalog.append({'ordinal':i,'id':name,'real_name':name,'type':family,
                    'explicit_trigger_chance':int(rate.group(1)) if rate else None,
                    'effective_trigger_chance':int(rate.group(1)) if rate else 0,
                    'source_lines':[text[:m.start()].count('\n')+1,text[:m.end()].count('\n')+1],
                    'original_complete_registration':m.group(0),
                    'meaning':'Exact registered method identity, classification and omitted-rate constructor default; no walking trigger from a zero base rate.'})
assert len(catalog)==26
assert [(x['id'],x['effective_trigger_chance']) for x in catalog][-7:] == [('OldRod',0),('GoodRod',0),('SuperRod',0),('RockSmash',50),('HeadbuttLow',0),('HeadbuttHigh',0),('BugContest',21)]

common = [
 'Fixed R/B8, no overriding plugin/class/extra callback or concurrent mutation; stated success branches require all earlier calls to return normally.',
 'All19 Encounter and2 Regional raw sections and every authored literal/order were actually read by this context before serialization. Original typed objects are copied whole, including historical OPEN annotations; the present finite meanings qualify only their named producer/consumer flow.',
 'Primary PBS is active only through actual top-level compiler input selection and successful dependency loading. A writer, registered record, archive or caller does not by itself prove activation of backups, current-map snapshot refresh, native media or successful battle.',
 'No implementation of the reference parser/encounter selector, no business-state surrogate and no new numerical-expression audit is run by this packaging script. Git/JSON/regex here provide identity and copying only.',
 'Source units are complete named methods/groups actually read, with original reader retained. A receiver must really read the full selected record, its defaults, necessary complete source joins and shared premises; an index or digest is not semantic reception.',
 'Any raised exception/failed file/native/helper call preserves only the reached prior prefix; no universal ensure/rollback is supplied. Game/native/save-reload execution remains NOT_EXECUTED.',
]

meanings=[]
def meaning(id, statement, source_indices, formal_path, formal_lines, notes=None):
    meanings.append({'id':id,'complete_meaning':statement,'source_units':[{'index':i,'label':units[i]['label']} for i in source_indices],
      'formal':{'path':formal_path,'lines':formal_lines},'premises':common,
      'status':'FINITE_ASSERTION_MATCHED_SOURCE_STATIC','actual_reader':READER,
      'failure_and_boundary':notes or 'Only the reached exact operation is accepted; all earlier dependent calls must return normally. No execution or whole-parent/domain acceptance.'})

meaning('ER01','Encounter keys are exact integer map/version pairs formatted as symbols. exists? has no version fallback; get prefers requested version and then map version0. each sorts map then version. each_of_version uses an array fallback membership key against symbol-keyed normal data, so v>0 can yield v0 and requested version for the same map.',[1],F36,[43,48])
meaning('ER02','Encounter compile first clears registry; map/version text uses decimal-prefix conversion and defaults omitted version0. Before a new header is checked for collision, the preceding section is merged/sorted/registered. Failures preserve clear and earlier successful registrations; final archive save is reached only after all inputs.',[2,4],F36,[58,65])
meaning('ER03','A slot is recognized only with an existing current type and leading digit immediately followed by comma. Weight/minimum are positive-integer fields; species is strict registered enum; omitted maximum becomes minimum; both levels must be at most current maximum and ordered minimum<=maximum. Negative-leading weight instead reaches invalid-type handling.',[2,4],F36,[58,65])
meaning('ER04','Repeated type declarations replace its slot list. Nonempty explicit probability uses decimal-prefix conversion; otherwise existing same-section probability survives, falling back to EncounterType default only when absent. Same species+minimum+maximum slots merge by adding weight, then sort descending weight and ascending species string on ties.',[0,4],F36,[58,65])
meaning('ER05','All26 exact EncounterType IDs, six type classes and effective defaults are retained in the complete catalog. Constructor omitted trigger rate is0; omitted class is none. All three fishing methods and both Headbutt methods have effective0.',[0],F36,[91,103])
meaning('ER06','Encounter setup resets step_count, step_chances and tables, copies primitive rates and Marshal-clones selected types/slots from requested-version-or-zero record. It preserves chance_accumulator. Separate reset_step_count clears both counters; true trigger return alone never calls reset.',[8,1],F36,[67,81])
meaning('ER07','Global encounter_version constructor default is0 after earlier constructor calls. Setter validates Integer before comparing, returns on same value, otherwise stores first and runs setup only when both encounter and map contexts exist. Same-value assignment does not refresh snapshot or counters.',[9,8],F36,[43,48])
meaning('ER08','Collection editor new map/version rejects existing pair and registers empty rates/types. Whole collection copy retains suffix/all rates but copies only nonempty type arrays and clones each slot. Delete is confirmed and removes registry entry. These operations alone do not save files.',[11,1,16],FB,[69,76])
meaning('ER09','Collection exit Yes saves Encounter archive first then writes PBS; No reloads the entire Encounter registry from archive. Neither path calls setup or broadcasts current-map refresh. A later writer failure leaves the reached archive/registry prefix.',[11,5,22,8],FB,[69,76])
meaning('ER10','Map/version edit checks target collision, deletes the old registry key, mutates record identity/map/version and inserts new key. This is a record key edit, not a write to global encounter_version. Adding a type excludes every existing type key, including zero-slot arrays, but not a residual rate-only key; it installs the type default rate and an empty list before nested edit.',[12,0],FB,[78,81])
meaning('ER11','Single-type copy establishes an empty target list even when the source is empty, copies source rate rather than target default, and clones every slot. Deleting a type removes both rate and list. This differs from whole-collection copy filtering zero-slot types.',[12,11],FB,[78,81])
meaning('ER12','Type editor permits rate0..255. Renaming moves rate and the same slot list to an unused type key. New slot defaults weight20, first enumerated Species base identity and levels5/5. Editing passes a slot clone; copy inserts a clone; delete is confirmed. There is no additional type/map total-save gate.',[13,16,18],FB,[83,88])
meaning('ER13','EncounterSlotProperty offers weight1..999, registered species/form selection, levels1..current maximum; missing maximum starts at minimum and reversed min/max are swapped after property editing. It invokes property-list without a save prompt and returns data even when the property driver returns nil. SpeciesForm cancel retains old identity; ACTION defaults to original selected species for this property.',[16,17,18,19,20],FA,[29,45])
meaning('ER14','Encounter PBS writer skips nil/empty type lists. It emits probability only if truthy and>0, otherwise emits just type; equal level bounds use three-field slots. Consequently saving rate0 retains0 in archive, while successful later compile of omitted-rate Land returns default21, and omitted-rate OldRod returns0. Writer alone neither recompiles nor refreshes the current snapshot.',[5,4,0,8],FB,[90,121])
meaning('ER15','Regional compiler consumes all paths into one indexed list array: header is nonnegative decimal digits; each section may be explicitly empty and duplicate index is rejected. Nonempty species tokens use parseSpecies (uppercase/strip plus Nidoran aliases). No-section content rejects. All slots0..max must exist at final uniq pass because holes nil fail there; this is not per-file increasing-order validation.',[2,3],F62,[95,102])
meaning('ER16','Regional ordered values flatten authored line and token order. Duplicate species within the same region fail only at final cross-input pass; duplicates between different regions are allowed. Save is after all validation. Completely empty input can save an empty outer array. No current-session cache invalidation occurs in compile_regional_dexes.',[3,6],F62,[95,108])
meaning('ER17','pbLoadRegionalDexes creates Game_Temp when missing, loads Data/regional_dexes.dat only when retained cache is false/nil, and returns that exact retained object. Current-region query reads town_map_position first element or its default when map/position is absent. A separate pbClearData invalidates caches and may setup encounters; the compiler does not call it here.',[6,7,3],F62,[95,108])
meaning('ER18','Regional number returns first matching base-species position+1, or0 for missing/empty list or unknown species; the method does not guard negative region before array lookup. Member-list query rejects any negative region and returns nil for missing/empty list, else returns an outer clone. Length of negative region counts current base registry, otherwise gives list length or0.',[7,21],F62,[95,121])
meaning('ER19','Pokedex initializes only unlock index0 true, then clear resets seen/owned/form/counter tables and recomputes accessible lists without clearing unlocks. National count/seen_any use base-species iteration; other-region count/seen_any directly iterate pbAllRegionalSpecies and can fail on nil for missing/empty/negative non-national region. Counting does not require unlock.',[10,7],F62,[110,121])
meaning('ER20','Accessible lists under current-region setting select only that region/national fallback if any seen, regardless of unlock. Otherwise regional unlocked+seen lists precede national unlocked+seen. unlock/lock map all negative or too-large values to national and always refresh; unlocked? itself maps exactly-1 only. species_in_unlocked_dex? returns true immediately if national unlocked, even for unknown identity.',[10,7],F62,[110,121])
meaning('ER21','Regional writer reads the retained regional cache and writes lists in indexed order, skipping nil members and grouping adjacent family members onto lines. It does not load a fresh archive when cache already exists. Compile-to-new-archive followed by export can therefore write the old cached content back to PBS while the new archive remains distinct.',[5,6,21],F62,[95,108])
meaning('ER22','Regional main editor clones each current cached list. It can add blank, national base-species order or unique-family concatenation, swap lists, clone a list and delete without a confirmation. These work-list edits alone do not change the retained source arrays or files; nested editing operates on this main working list.',[15,6,21],FA,[158,169])
meaning('ER23','Regional single-list entry compact! occurs before the retained return clone. Refresh removes trailing nils; selecting a species removes every other occurrence by replacing it with nil. No returns the initial compacted clone, and return compact! removes all holes; main always accepts that result, so child No is not an exact restoration of holes.',[14,20,15],FA,[158,162])
meaning('ER24','Regional child Yes repeatedly slices the last element until the last element is truthy. Empty or all-cleared list reaches an empty array with no terminating condition and does not reach cleanup/return in this static branch. This is a child Yes boundary; a blank list can separately be saved directly through the main editor without entering this branch.',[14,15],FA,[158,162])
meaning('ER25','Regional main Yes writes the entire work-list archive, then invalidates regional cache, then writes PBS from lazy reload, then shows saved message and exits. Main No discards working lists without writing or clearing cache; Cancel continues. Later failure preserves earlier archive/cache/file prefix; no ensure or rollback is present.',[15,6,5],FA,[158,162])
meaning('ER26','Family fill in regional main consumes Species.get_family_species from first unseen base species in definition order, concatenating each returned family and recording seen identities. Its deeper recursive family order follows the complete Species definition rather than author edge order alone; valid acyclic context and already-read Evolution/family predicates remain necessary.',[15,21],FA,[164,169])

typed=load('typed-record-facts.v1.json')
groups=[]
for idx in [4,7]:
    g=copy.deepcopy(typed['paths'][idx])
    g['original_packet']='typed-record-facts.v1.json#/paths/'+str(idx)
    g['original_complete_record_reader']=READER
    g['complete_original_pbs_text']=(R/g['path']).read_text()
    g['current_finite_semantic_join']='ER01–ER26 as relevant, all common premises and necessary complete source units; historical record OPEN annotations are not erased and whole consumer acceptance is not inferred.'
    groups.append(g)
assert [len(g['records']) for g in groups]==[19,2]
facts=load('bounded-pbs-facts.v16.json')
selected=[x for x in facts['facts'] if x['id'] in ['PC-F013','PC-F014','PC-F015','PC-F021','PC-F022','PC-F033','PC-F034','PC-F035','PC-F036','PC-F037']]
assert len(selected)==10
formal_units=[unit(F36,1,len((B/F36).read_text().splitlines()),'Complete WP36 already ownFULL',B),
              unit(F62,1,len((B/F62).read_text().splitlines()),'Complete WP62 already ownFULL',B),
              unit(FA,29,45,'Complete property driver/numeric table finite clauses only',B),
              unit(FA,55,61,'Complete reference-selector finite clauses only',B),
              unit(FA,75,75,'Complete EncounterSlot field specification',B),
              unit(FA,158,169,'Complete regional editor and family-fill clauses',B),
              unit(FB,67,121,'Complete Encounter editor/save/roundtrip/snapshot clauses',B)]
packet={'schema':'gr8-encounter19-regional2-complete/v1','utc':UTC,'actual_reader':READER,
 'primary_complete_records':21,'complete_primary_record_groups':groups,'complete_EncounterType_catalog':catalog,
 'complete_original_source_facts':selected,'source_fact_packet':'bounded-pbs-facts.v16.json',
 'mandatory_source_fact_companion':'mandatory-encounter-trigger-counter-clarification.v1.json',
 'common_premises':common,'manual_finite_meanings':meanings,'complete_source_units':units,
 'complete_formal_units':formal_units,'raw_read_credit':'All21 complete raw sections and26 registrations actually read before packaging; not granted by this script.',
 'remaining_open':['All11 whole consumer/formal closures remain OPEN. These finite meanings do not accept every encounter event callback, movement/habitat UI, arbitrary plugin or referenced battle outcome.',
  'Host UI/native archive/Marshal/effects/battle behavior and actual save/reload were not executed.',
  'Any receiver must actually read all selected complete records and necessary definitions/premises; no automatic FULL transfer.'],
 'business':'NOT_EXECUTED','new_numeric_or_business_model_execution':0,'UPDATE_NOT_STARTED':True}
out=save('encounter19-regional2.complete.v1.json',packet)

# Root classification receipt, preserving complete decision rather than borrowing
# the root's 129071-byte exact-input/counterreview reading credit.
root_path=ROOT/'adjudication/root-egggroup-domain-reception.v1.json'
raw=root_path.read_bytes()
assert len(raw)==14620 and hashlib.sha256(raw).hexdigest()=='f7772860e1302733fb2ec9f73d57e43562e9badf01b7819644bbc5376523cf2d'
decision=json.loads(raw)
receipt={'schema':'gr8-pbs-egggroup-root-decision-reception/v1','utc':UTC,'actual_receiver':READER,
 'complete_root_decision':decision,'received_identity':{'path':str(root_path.relative_to(ROOT)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},
 'actual_full_read_IO':['e76250'],'accepted_finite_meaning':'GR8-PBS-EGGGROUP-DOMAIN-001 is root-classified required P3, limited to explicitly incorporating the15 fixed legal author IDs. Original query alias retained. Ordinary breeding algorithms and special gates remain correct.',
 'remaining_open':'Global full-history deduplication and reception of any defeating equivalent already-incorporated directory remain OPEN. This receiver did not read root exact-input129071B or Kernel counterreview16224B by reading this decision.',
 'minimal_update':'No formal changes now. Root controls unique future author/integrator and independent acceptance. No new tests/API/UI ordering/English language requirement inferred.',
 'new_contexts':0,'new_votes':0,'global_finding_count_increment_inferred':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True}
receipt_id=save('egggroup-root-decision-reception.v1.json',receipt)

l=load('reading-ledger.json')
newreads=[(META,[58,119],['metadata initialize and encounter_version=']),
 (EDITOR,[6,340],['pbEncountersEditor6–124','pbEncounterMapVersionEditor128–252','pbEncounterTypeEditor256–340']),
 (EDITOR,[992,1202],['pbRegionalDexEditor992–1097','pbRegionalDexEditorMain1099–1202']),
 (EDITOR,[1204,1247],['pbAppendEvoToFamilyArray','pbGetEvoFamilies','pbEvoFamiliesToStrings']),
 (DT,[56,128],['LimitProperty','LimitProperty2','NonzeroLimitProperty']),
 (DT,[448,473],['SpeciesFormProperty']),
 (DT,[1575,1706],['EncounterSlotProperty','pbPropertyList']),
 (EU,[1,190],['pbGetLegalMoves','pbSafeCopyFile','pbAllocateAnimation','pbMapTree','pbChooseFromGameDataList','pbChooseSpeciesList','pbChooseSpeciesFormList','pbChooseTypeList','pbChooseItemList','pbChooseAbilityList','pbChooseMoveList'])]
for path,lines,names in newreads:
    item={'path':path,'lines':lines,'complete_units':names,
     'qualification':'Actual displayed range. Only complete named units gain finite semantic credit; neighboring partial methods remain OPEN.'}
    if not any(x['path']==path and x['lines']==lines for x in l['dependencies_partial_read']): l['dependencies_partial_read'].append(item)
for lines,label in [([29,45],'property framework and numeric table'),([55,61],'reference selectors finite clauses'),([75,75],'encounter slot'),([158,169],'regional editor complete clauses')]:
    if not any(x['path']==FA and x['lines']==lines for x in l['formal_partial_read']): l['formal_partial_read'].append({'path':FA,'lines':lines,'units':label,'qualification':'Only named finite relevant clauses; whole WP73-A is not claimed read from a truncated initial display.'})
l['updated_utc']=UTC
(P/'reading-ledger.json').write_text(json.dumps(l,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'utc':UTC,'packet':out,'root_receipt':receipt_id,'source_units':len(units),'manual_meanings':len(meanings),'catalog':len(catalog),'records':21,'new_business_or_numeric_execution':0},ensure_ascii=False))
