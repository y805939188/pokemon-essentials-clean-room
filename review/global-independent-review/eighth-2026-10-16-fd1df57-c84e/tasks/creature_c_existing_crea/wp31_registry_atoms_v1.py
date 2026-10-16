import json, re, hashlib, datetime, subprocess
from pathlib import Path

P=Path(__file__).parent
R=Path('/workspace/pokemon-essentials')
B=Path('/workspace/pokemon-essentials-clean-room')
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
src='Data/Scripts/010_Data/001_Hardcoded data/007_Evolution.rb'
formal='deliverables/final-specification-set/pokemon-rules/wp31-basic-evolution.md'
text=(R/src).read_text(); flines=(B/formal).read_text().splitlines()
# The assertions below are manually authored after actual full reads of both
# files. The regex only binds an explicitly named complete registration unit.
rows=[]
def row(ids,needle,claims,context,param,extra=''):
    rows.append((ids.split(),needle,claims,context,param,extra))
row('Level','`Level`',['Current persistent level >= integer parameter; no requirement that this invocation just increased level.'],'level','Integer')
row('LevelMale LevelFemale','`LevelMale`',['First compare level >= integer parameter; only if true query the named male/female predicate.','Male and female variants use the checked Pokemon gender, not Trainer or Owner gender.'],'level','Integer')
row('LevelDay LevelNight LevelMorning LevelAfternoon LevelEvening','`LevelDay`',['First compare level >= parameter; only then call the corresponding no-argument PBDayNight predicate.','No time snapshot is passed from battle; each reached predicate supplies its own default time.'],'level','Integer','PBDayNight whole implementation/current host time remains separate named dependency.')
row('LevelNoWeather','`LevelNoWeather`',['First level >= parameter, then screen truthy, then exact weather_type == :None.','A missing screen is falsey; no Weather lookup is needed for this identity.'],'level','Integer')
for ident,cat in [('LevelSun',':Sun'),('LevelRain','[:Rain, :Fog]'),('LevelSnow',':Hail'),('LevelSandstorm',':Sandstorm')]:
    row(ident,'`'+ident+'`',[f'First level >= parameter, then truthy $game_screen, then current world Weather.get(weather_type).category matches {cat}.','An unknown reached weather identity can raise at registry lookup; no field-weather or remaining-turn input is read.'],'level','Integer','Weather registry and world screen setters require separately bounded consumer verification.')
for ident,field in [('LevelCycling','bicycle'),('LevelSurfing','surfing'),('LevelDiving','diving')]:
    row(ident,'`LevelCycling`',[f'First level >= parameter, then $PokemonGlobal truthy, then read its {field} field.','No map-name inference or battle field state substitutes for that global field.'],'level','Integer')
row('LevelDarkness','`LevelDarkness`',['First compare level, then directly dereference $game_map.metadata and safe-navigate dark_map.','Missing metadata is falsey; missing $game_map itself is not guarded.'],'level','Integer')
row('LevelDarkInParty','`LevelDarkInParty`',['First compare level, then invoke current global $player.has_pokemon_of_type?(:DARK).','Actual Trainer helper consumes non-egg party and can include fainted/self; no storage or merged partner roster read.'],'level','Integer')
for ident,op in [('AttackGreater','>'),('AtkDefEqual','=='),('DefenseGreater','<')]:
    row(ident,'`'+ident+'`',[f'First level >= parameter, then compare current persistent attack {op} defense.','No recomputation is requested in this registration; already stored/cached stats are consumed.'],'level','Integer')
for ident,op in [('Silcoon','<'),('Cascoon','>=')]:
    row(ident,'`'+ident+'`',[f'First level >= parameter, then ((personalID >> 16) & 0xFFFF) % 10 {op} 5.','The upper 16 PID bits are used; not low decimal digit or a new random draw.'],'level','Integer')
row('Ninjask','`Ninjask`',['Level >= parameter, with its own registered identity and no additional condition.','The sibling Shedinja row has no level-up callable and cannot be selected by this predicate.'],'level','Integer')
row('Happiness HappinessMale HappinessFemale','`Happiness`',['Threshold is 160 when APPLY_HAPPINESS_SOFT_CAP is truthy, otherwise 220.','Metadata any_level_up is true; callable itself has no level comparison.','Male/female identities additionally short-circuit on checked Pokemon male?/female? after happiness test; ordinary Happiness has no gender gate.'],'level','None')
row('HappinessDay HappinessNight','`HappinessDay`',['Threshold 160/220 follows soft-cap setting; only after it succeeds call current Day/Night predicate.','any_level_up is true; no just-levelled flag is tested inside the callable.'],'level','None')
row('HappinessMove','`HappinessMove`',['After happiness threshold, any nonnil current move with id == parameter qualifies.','Missing/insufficient happiness leaves falsey result; no persistent species commit occurs.'],'level',':Move')
row('HappinessMoveType','`HappinessMoveType`',['After happiness threshold, any nonnil current move whose type == parameter qualifies.','Reads actual Move.type; does not infer type from species or battle move copy.'],'level',':Type')
row('HappinessHoldItem','`HappinessHoldItem`',['First pkmn.item == parameter, then happiness >= soft-cap-dependent threshold.','After-evolution action compares actual evolved target with this row target and separately tests current hasItem?(parameter); only then item=nil and true.'],'level',':Item','Item lookup returns identity-comparable data; hasItem? semantics/source are in own full Pokemon.')
row('MaxHappiness','`MaxHappiness`',['Requires happiness exactly 255, rather than >= threshold.','any_level_up true supplies metadata; callable contains no level test.'],'level','None')
row('Beauty','`Beauty`',['Requires checked Pokemon beauty >= integer parameter.','any_level_up true; no beauty mutation or contest production flow is provided here.'],'level','Integer')
for ident,cond in [('HoldItem','no extra condition'),('HoldItemMale','then male?'),('HoldItemFemale','then female?'),('DayHoldItem','then PBDayNight.isDay?'),('NightHoldItem','then PBDayNight.isNight?'),('HoldItemHappiness','then happiness >= soft-cap-dependent160/220')]:
    needle='`DayHoldItem`' if ident in ['DayHoldItem','NightHoldItem'] else ('`HoldItemHappiness`' if ident=='HoldItemHappiness' else '`HoldItem`')
    row(ident,needle,[f'Level-context callable first compares pkmn.item == parameter; {cond}.','any_level_up true; no level comparison within this callable.','After-evolution action only clears item and returns true when row target == actual new target and current hasItem?(parameter); otherwise false continues action scan.'],'level',':Item')
row('HasMove','`HasMove`',['Any nonnil persistent move whose id equals parameter qualifies.','any_level_up true; no move mutation or level comparison.'],'level',':Move')
row('HasMoveType','`HasMove`',['Any nonnil persistent move whose type equals parameter qualifies.','any_level_up true; no move mutation or level comparison.'],'level',':Type')
row('HasInParty','`HasInParty`',['Calls current global $player.has_species?(parameter).','Actual Trainer helper uses current non-egg party and may include fainted/self; no storage or partner-only array.'],'level',':Species')
row('Location','`Location`',['Direct current $game_map.map_id == integer parameter.','Missing map has no local guard; no obtain_map, coordinates or target map input.'],'level','Integer')
row('LocationFlag','`LocationFlag`',['Current $game_map.metadata safe-navigation has_flag?(String parameter).','Missing metadata falsey, missing map unguarded; case semantics are in actual metadata helper.'],'level','String')
row('Region','`Region`',['Read current map metadata, require nonnil town_map_position, then first component == parameter.','No dex unlock/view region or Pokemon obtain location is queried.'],'level','Integer')
row('Item','`Item`',['Use-item callable compares supplied item identity exactly with parameter.','Does not itself consume Bag inventory, start evolution scene, or require recently gained level.'],'item',':Item')
row('ItemMale ItemFemale','`ItemMale`',['First compare supplied item == parameter; only then test checked Pokemon male?/female?.','Gender comes from Pokemon; no Owner/Trainer gender.'],'item',':Item')
row('ItemDay ItemNight','`ItemDay`',['First compare supplied item == parameter, then corresponding current Day/Night predicate.','No battle-start timestamp or time-shading option is read.'],'item',':Item')
row('ItemHappiness','`ItemHappiness`',['First compare supplied item == parameter, then happiness >= setting-dependent160/220.','No internal inventory consumption; actual item layer consumption remains a separate caller contract.'],'item',':Item')
row('Trade','`Trade`',['Trade callable unconditionally returns true after outer common guards.','No partner species, item or time condition.'],'trade','None')
row('TradeMale TradeFemale','`TradeMale`',['Trade callable checks received Pokemon male?/female?.','Does not query sent counterpart gender.'],'trade','None')
row('TradeDay TradeNight','`TradeDay`',['Trade callable invokes corresponding current Day/Night predicate at reached check.','No trade-start snapshot is passed in.'],'trade','None')
row('TradeItem','`TradeItem`',['Checks received Pokemon item == parameter.','After-evolution action checks row target == actual target and current hasItem? then clears received Pokemon item; no Bag or sent Pokemon consumption.'],'trade',':Item')
row('TradeSpecies','`TradeSpecies`',['First compares received pkmn.species == parameter; only after true checks !other_pkmn.hasItem?(:EVERSTONE).','It does not compare counterpart species; missing counterpart can fail only after self-species branch succeeds.'],'trade',':Species')
row('BattleDealCriticalHit','`BattleDealCriticalHit`',['Requires truthy $game_temp.party_critical_hits_dealt, truthy indexed slot, then indexed value >= parameter.','Ruby numeric0 passes presence guard; no initializer or total-history query is supplied here.'],'battle','Integer','Actual per-hit K producer and notification lifecycle separately required; this row accepts only definition/check receiver.')
row('Event','`Event`',['Compares explicit value == parameter.','No used-number collection or destructive number consumption occurs.'],'event','Integer')
row('EventAfterDamageTaken','`EventAfterDamageTaken`',['After-battle callable requires D container, indexed slot and indexed value >=49; if so assigns ready_to_evolve=true.','After-battle callable always returns false and never chooses evolution target; insufficient D leaves prior R unchanged.','Event callable compares explicit value == parameter then ready_to_evolve; persistent R is separate from per-battle D.'],'battle/event','Integer','Actual D producer/faint/notification and R resets separately required.')
row('Shedinja','`Shedinja`',['Has only after_evolution_proc and Integer parameter metadata; no target-check callable.','Check current party_full? first; then Bag hasPOKEBALL; either failure returns false so scan continues.','On success duplicate Pokemon using this row target, then Bag.removePOKEBALL, then true stops scan; actual evolved target is not a gate on this callback.','Duplicate operation occurs before ball removal: failures after party push/dex write can retain prefix without ball consumption.'],'after','Integer')
row('None','`None`',['Registration supplies no callable/action; all callable wrappers return nil.','Species get_evolutions omits None from ordinary forward candidates; unknown identity is a separate lookup failure rather than equivalent to None.'],'none','None')

registry=[]
for m in re.finditer(r'^GameData::Evolution\.register\(\{\n',text,re.M):
    end=text.index('\n})',m.end())+3
    body=text[m.start():end]
    ident=re.search(r':id\s*=>\s*:(\w+)',body).group(1)
    registry.append((ident,text.count('\n',0,m.start())+1,text.count('\n',0,end)+1,body))
byid={a:(b,c,d) for a,b,c,d in registry}
assert len(byid)==len(registry)
authored={i for ids,*_ in rows for i in ids}
assert authored==set(byid),(authored-set(byid),set(byid)-authored)
sourcebytes=(R/src).read_bytes()
assert subprocess.check_output(['git','-C',str(R),'show','8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b:'+src])==sourcebytes
sourceid=dict(path=src,bytes=len(sourcebytes),sha256=hashlib.sha256(sourcebytes).hexdigest(),fixed_R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b',reader='/root/creature_a_atomic_reception',full_read_chunks=['dcc0bc','354c57','e41a52'])
records=[]; units=[]
for n,(ids,needle,claims,context,param,extra) in enumerate(rows,1):
    locs=[i+1 for i,l in enumerate(flines) if needle in l]
    assert locs,(ids,needle)
    unitids=[]
    for ident in ids:
        s,e,body=byid[ident];uid='C31-REG-'+ident
        units.append(dict(id=uid,identity=sourceid,range=[s,e],text=body,complete_registration=True))
        unitids.append(uid)
    records.append(dict(id=f'C31-R{n:03}',formal=dict(path=formal,matching_lines=locs,complete_source_lines=[flines[i-1] for i in locs]),registered_identities=ids,declared_parameter_type=param,context=context,premise='Valid registered Pokemon/species/argument types and required globals until individually stated short-circuit/failure; own full Pokemon/Trainer/EvolutionUI and current Evolution registry read. Static only; source registration capability remains audited even without default PBS caller.',child_assertions=[dict(id=f'C31-R{n:03}-A{i:02}',meaning=c,source_units=unitids,source_definition_status='SUPPORTED_BY_ACTUAL_WHOLE_REGISTRATION_READ',whole_parent_acceptance=False) for i,c in enumerate(claims,1)],actual_definition_receiver=dict(path='Data/Scripts/014_Pokemon/001_Pokemon.rb',complete_units='five wrappers976–1021, action_after_evolution1025–1029, internal1035–1045, trigger1047–1059; entire file prior own FULL',dispatch='family wrapper calls only that family callable; internal egg/shadow thenEverstone thenBattleBond; Species forward list in order, first truthy target; after-action separate scan before species change'),normal_cancel_failure='Predicate does not run scene commit. Registration short-circuits left-to-right; exceptions retain previously reached cache/persistent writes. Scene cancellation does not retroactively erase prior caller growth or R. Shedinja and item after-actions have explicit mutation prefixes above.',remaining=extra or 'Default/backup actual PBS values, full transitive environment producers and caller lifecycle must be separately bound; not inferred from this definition packet.',accepted=False))
payload=dict(schema='gr8-cre-c-wp31-registry-meaning-atoms/v1',recorded_utc=utc,actual_reader=sourceid['reader'],manual_assertion_authoring=True,source_units=units,records=records,complete_registry_identity_count=len(byid),manual_assertion_count=sum(len(x['child_assertions']) for x in records),qualification='All registry identities manually distinguished and source-complete. This finite packet is not entire WP31/C acceptance; consumers/default PBS/persistence remain separately audited. No new independent context/reviewer/vote.',business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
(P/'wp31-registry-meaning-atoms.v1.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
d=json.loads((P/'reverse-mapping.json').read_text());assert not any(x['id'].startswith('C31-R') for x in d['records']);d['records']+=records;d['utc']=utc;d['status']='RUNNING_MANUAL_MEANING_ATOMS';(P/'reverse-mapping.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
pr=json.loads((P/'progress.json').read_text());pr['updated_utc']=utc;pr['primary_clause_atoms']=sum(len(x.get('child_assertions',[])) for x in d['records']);(P/'progress.json').write_text(json.dumps(pr,ensure_ascii=False,indent=2)+'\n')
b=(P/'wp31-registry-meaning-atoms.v1.json').read_bytes();print(json.dumps(dict(utc=utc,identities=len(byid),groups=len(records),manual_atoms=payload['manual_assertion_count'],bytes=len(b),sha256=hashlib.sha256(b).hexdigest())))
