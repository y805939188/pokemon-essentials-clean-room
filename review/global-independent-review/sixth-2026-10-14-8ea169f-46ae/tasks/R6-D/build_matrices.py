"""Join complete data units to manually reviewed rules; never synthesize PASS."""
import hashlib
import json
import pathlib
import re
from read_range import ROOT, OUT, verify

verify()
R = 'reference/pokemon-essentials/'
F = 'deliverables/final-specification-set/'
S = R+'Data/Scripts/'
compiler = S+'021_Compiler/002_Compiler_CompilePBS.rb'
base = S+'021_Compiler/001_Compiler.rb'
schema = S+'010_Data/002_PBS data/'
challenge = S+'018_Alternate battle modes/001_Battle Frontier/'
denominator = json.loads((ROOT/'review/global-independent-review/sixth-2026-10-14-8ea169f-46ae/inventory/formal-block-denominator.json').read_text())

def loc(path, first, last):
    return dict(path=path,start_line=first,end_line=last)

def formal(file, first, last):
    result=loc(F+file,first,last)
    result['clauses']=[d['id'] for d in denominator if d['path']==result['path'] and d['start_line']<=last and d['end_line']>=first]
    return result

rules = {
 'facility_pokemon': dict(note=2, fact='Five authored fields are consumed permissively; unknown item→none, unknown moves omitted, nature/species missing are not generic enum errors.',
   consumers=[loc(challenge+'002_Challenge_Data.rb',113,139),loc(challenge+'002_Challenge_Data.rb',154,217)],
   formal=[formal('combat-requirements/wp55-facility-session-and-restoration.md',97,99),formal('demo-dx/wp76-facility-content-generation-and-simulation.md',229,232)]),
 'facility_trainers': dict(note=3, fact='Physical header is not a trainer identity lookup; row ordinal and six fields are consumed. Candidate duplicates remain entries and sampling is with replacement.',
   consumers=[loc(compiler,1024,1062),loc(challenge+'003_Challenge_ChooseFoes.rb',39,81)],
   formal=[formal('combat-requirements/wp55-facility-session-and-restoration.md',91,99),formal('demo-dx/wp76-facility-content-generation-and-simulation.md',221,225)]),
 'battle_facility_lists': dict(note=1, fact='Five section occurrences; explicit file references; first non-default match then first default fallback; unreferenced fancy files remain available data.',
   consumers=[loc(compiler,951,1021),loc(challenge+'002_Challenge_Data.rb',21,32)],
   formal=[formal('generic-kernel/wp02-rule-configuration-and-data-variants.md',223,236),formal('combat-requirements/wp55-facility-session-and-restoration.md',95,97),formal('demo-dx/wp76-facility-content-generation-and-simulation.md',262,262)]),
 'encounters': dict(note=5, fact='Map/version and method/slot data; optional maximum defaults to minimum; known species/form, strictly positive slot fields; method chance follows dedicated handling. Profile activation is separate.',
   consumers=[loc(compiler,658,765),loc(schema+'013_Encounter.rb',17,69),loc(S+'010_Data/001_Hardcoded data/013_EncounterType.rb',29,178)],
   formal=[formal('generic-kernel/wp04-pbs-lifecycle.md',122,135),formal('test-catalog/generic-kernel-wp02-03-04.md',20,21),formal('test-catalog/generic-kernel-wp02-03-04.md',70,72)]),
 'regional_dexes': dict(note=6, fact='Authored order flattens to one-based regional number, duplicate members rejected per region; regions0/1 have151/256 existing identities. No historical official numbering assumption.',
   consumers=[loc(compiler,593,628),loc(S+'019_Utilities/001_Utilities.rb',389,418),loc(schema+'001_MiscPBSData.rb',28,33)],
   formal=[formal('pokemon-rules/wp62-pokedex-records-regions-and-content.md',95,102),formal('test-catalog/generic-kernel-wp02-03-04.md',151,154)]),
 'trainers': dict(note=7, fact='Versioned trainer headers; Pokemon starts a member, later subfields apply to it; ordinary enum references are strict; IV/EV and required-member validation precede registration.',
   consumers=[loc(schema+'015_Trainer.rb',18,43),loc(schema+'015_Trainer.rb',86,177),loc(compiler,791,945)],
   formal=[formal('creature-rpg/wp24-player-trainers-partners.md',149,158),formal('generic-kernel/wp04-pbs-lifecycle.md',156,156),formal('test-catalog/generic-kernel-wp02-03-04.md',27,27),formal('test-catalog/generic-kernel-wp02-03-04.md',93,96),formal('test-catalog/generic-kernel-wp02-03-04.md',104,105),formal('test-catalog/generic-kernel-wp02-03-04.md',155,158)]),
 'trainer_types': dict(note=8, fact='Type identity, named gender aliases, nonnegative base money/skill and optional BGM names; absent skill follows base money. Resource output still needs native/media evidence.',
   consumers=[loc(schema+'014_TrainerType.rb',18,30),loc(schema+'014_TrainerType.rb',52,116)],
   formal=[formal('creature-rpg/wp24-player-trainers-partners.md',149,149),formal('engine-overworld/wp15-resource-matching-and-audio.md',69,78),formal('test-catalog/generic-kernel-wp02-03-04.md',101,101),formal('test-catalog/generic-kernel-wp02-03-04.md',119,119)]),
 'ribbons': dict(note=8, fact='Names/descriptions are translated separately, positions0..79 address64px cells in eight-column atlas. Content data does not prove contest gameplay or asset availability.',
   consumers=[loc(schema+'012_Ribbon.rb',14,41),loc(compiler,634,652),loc(S+'016_UI/006_UI_Summary.rb',850,896)],
   formal=[formal('user-interface/wp66-a-party-and-summary-ui.md',164,164),formal('user-interface/wp66-a-party-and-summary-ui.md',176,178),formal('test-catalog/generic-kernel-wp02-03-04.md',114,114)]),
 'metadata': dict(note=7, fact='Global0 requires Home and terminal checks require player1; player records supply movement resources with chained fallback. Current values satisfy data prerequisites, not map/media availability.',
   consumers=[loc(schema+'016_Metadata.rb',21,78),loc(schema+'017_PlayerMetadata.rb',12,87),loc(compiler,1070,1167)],
   formal=[formal('creature-rpg/wp24-player-trainers-partners.md',73,79),formal('creature-rpg/wp24-player-trainers-partners.md',100,100),formal('generic-kernel/wp04-pbs-lifecycle.md',148,148),formal('test-catalog/generic-kernel-wp02-03-04.md',103,103),formal('test-catalog/generic-kernel-wp02-03-04.md',109,115)]),
 'map_metadata': dict(note=9, fact='Present named map metadata supplies typed switches, weather chance, map position/size, environment, links and extension flags. Real serialized map geometry is unavailable.',
   consumers=[loc(schema+'018_MapMetadata.rb',33,57),loc(schema+'018_MapMetadata.rb',92,129),loc(compiler,1173,1190)],
   formal=[formal('user-interface/wp63-pokegear-map-music-and-phone.md',40,50),formal('engine-overworld/wp14-random-dungeons.md',25,29),formal('test-catalog/generic-kernel-wp02-03-04.md',117,117)]),
 'town_map': dict(note=9, fact='Regions and ordered Point tuples; optional location detail/healing/switch fields stay distinct. Current switch51/52 entries have no healing triple.',
   consumers=[loc(schema+'002_TownMap.rb',14,40),loc(compiler,73,98)],
   formal=[formal('user-interface/wp63-pokegear-map-music-and-phone.md',38,50),formal('test-catalog/generic-kernel-wp02-03-04.md',119,119)]),
 'map_connections': dict(note=9, fact='Six components, directed opposite edges and integer offsets; every present map ID has metadata. Actual maps are missing; geometry/connectivity is not proved.',
   consumers=[loc(compiler,104,137)],
   formal=[formal('generic-kernel/wp04-pbs-lifecycle.md',154,154),formal('test-catalog/generic-kernel-wp02-03-04.md',148,150)]),
 'phone': dict(note=9, fact='Whole record current/start/default fallback; repeated ^q texts and PN/TN/TP/TE/TM/m controls; one TP/TE sample per call. No event registration or actual phone runtime proved.',
   consumers=[loc(schema+'021_PhoneMessage.rb',15,26),loc(schema+'021_PhoneMessage.rb',32,87),loc(compiler,1237,1268),loc(S+'013_Items/004_Item_Phone.rb',414,535)],
   formal=[formal('user-interface/wp63-pokegear-map-music-and-phone.md',148,156),formal('generic-kernel/wp04-pbs-lifecycle.md',89,90),formal('test-catalog/generic-kernel-wp02-03-04.md',25,25),formal('test-catalog/generic-kernel-wp02-03-04.md',33,36)]),
 'dungeon_parameters': dict(note=11, fact='Area/version defaults and parameters supply dimensions, room/corridor/layout/chance/decorations. Present even dimensions and positive densities avoid separately documented conditional failures.',
   consumers=[loc(schema+'020_DungeonParameters.rb',33,117),loc(compiler,1211,1231),loc(S+'012_Overworld/008_Overworld_RandomDungeons.rb',51,215),loc(S+'012_Overworld/008_Overworld_RandomDungeons.rb',347,475),loc(S+'012_Overworld/008_Overworld_RandomDungeons.rb',747,809),loc(S+'012_Overworld/008_Overworld_RandomDungeons.rb',862,975)],
   formal=[formal('engine-overworld/wp14-random-dungeons.md',52,104),formal('engine-overworld/wp14-random-dungeons.md',110,141),formal('engine-overworld/wp14-random-dungeons.md',198,218)]),
 'dungeon_tilesets': dict(note=11, fact='Both Autotile and Tile groups exist; index base transforms, wall layouts, booleans and north offset feed layout rendering. No actual host tileset/media verified.',
   consumers=[loc(schema+'019_DungeonTileset.rb',19,196),loc(compiler,1196,1206),loc(S+'012_Overworld/008_Overworld_RandomDungeons.rb',1063,1076)],
   formal=[formal('generic-kernel/wp04-pbs-lifecycle.md',150,150),formal('engine-overworld/wp14-random-dungeons.md',87,96),formal('engine-overworld/wp14-random-dungeons.md',222,243),formal('test-catalog/generic-kernel-wp02-03-04.md',127,132)])
}
extra_vectors = {
 'facility_pokemon': [('test-catalog/demo-dx-wp72-73-74-75-76-77.md',194,194),('test-catalog/demo-dx-wp72-73-74-75-76-77.md',243,245),('test-catalog/creature-rpg-wp35-36-57-64-68.md',75,79),('test-catalog/creature-rpg-wp35-36-57-64-68.md',86,90)],
 'facility_trainers': [('test-catalog/combat-requirements-wp54-55-56-58.md',65,71),('test-catalog/combat-requirements-wp54-55-56-58.md',88,88),('test-catalog/combat-requirements-wp54-55-56-58.md',95,95),('test-catalog/demo-dx-wp72-73-74-75-76-77.md',211,212)],
 'phone': [('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',77,80),('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',97,98)],
 'town_map': [('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',89,94)],
 'map_metadata': [('test-catalog/user-interface-wp17-63-65-66-67-68-69-70-71.md',91,94)],
 'dungeon_parameters': [('test-catalog/engine-overworld-wp11-15-59-60.md',253,260),('test-catalog/engine-overworld-wp11-15-59-60.md',268,279),('test-catalog/engine-overworld-wp11-15-59-60.md',284,289),('test-catalog/engine-overworld-wp11-15-59-60.md',293,295)],
 'dungeon_tilesets': [('test-catalog/engine-overworld-wp11-15-59-60.md',269,274),('test-catalog/engine-overworld-wp11-15-59-60.md',291,292)]
}
for family, spans in extra_vectors.items():
    rules[family]['formal'].extend(formal(*span) for span in spans)
rules['town_map']['consumers'].extend([loc(S+'016_UI/009_UI_RegionMap.rb',73,117),loc(S+'016_UI/009_UI_RegionMap.rb',183,230)])
rules['map_metadata']['consumers'].extend([
    loc(S+'016_UI/009_UI_RegionMap.rb',73,117),loc(S+'012_Overworld/001_Overworld.rb',224,314),
    loc(S+'013_Items/001_Item_Utilities.rb',531,550),loc(S+'013_Items/004_Item_Phone.rb',330,366),
    loc(S+'012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',89,107),
    loc(S+'012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb',268,297),
    loc(S+'012_Overworld/004_Overworld_FieldMoves.rb',277,306),loc(S+'012_Overworld/003_Overworld_Time.rb',116,124),
    loc(S+'018_Alternate battle modes/001_SafariZone.rb',63,71),
    loc(S+'010_Data/001_Hardcoded data/007_Evolution.rb',490,497),
    loc(S+'014_Pokemon/001_Pokemon-related/001_FormHandlers.rb',267,272),
    loc(S+'012_Overworld/002_Battle triggering/004_Overworld_EncounterModifiers.rb',51,59),
    loc(S+'016_UI/005_UI_Party.rb',1204,1213)])
rules['map_metadata']['formal'].append(formal('engine-overworld/wp59-world-time-weather-field-moves.md',145,156))
for key, rule in rules.items():
    rule['id']='D-'+key
    rule['review_method']='manual static consumer/formal comparison plus complete inert field/reference predicates'
    rule['semantic_note']='semantic-notes.md item'+str(rule['note'])
    rule['evidence_level']='STATIC_READ_AND_DERIVED_DATA_RELATIONS'
    rule['not_proved']=['actual compiler run','actual host or Demo','full combat effect behavior outside data contract','complete variant compatibility']
(OUT/'manual-rule-catalog.json').write_text(json.dumps(rules,ensure_ascii=False,indent=2)+'\n')

rows=[]
def add(d, record, line, field, value, part=None):
    rule=rules[d['family']]
    identity=record['identity'] if record else 'row:'+str(part)
    rows.append(dict(unit=f"{d['path']}:{line}:{field}",source=loc(R+d['path'],line,line),
        file_sha256=d['sha256'],record_identity=identity,record_ordinal=record['ordinal'] if record else part,
        field=field,value_sha256=hashlib.sha256(value.encode()).hexdigest(),rule=rule['id'],
        fact=rule['fact'],consumer_locations=rule['consumers'],formal_locations=rule['formal'],
        status='RULE_MAPPED_NO_AUTOMATIC_PASS',independent_field_semantic_note=rule['semantic_note'],
        premise='Fixed current schema/default consumers; registered dependencies; ordinary host calls succeed; no plugin override. Backups require explicit selection and remain compatibility-unproved.'))

for path in sorted(OUT.glob('structure-*.json')):
    d=json.loads(path.read_text())
    for rec in d['records']:
        add(d,rec,rec['start_line'],'record_header',rec['identity'])
        for field in rec['fields']:
            add(d,rec,field['line'],field['key'],field['value'])
        for row in rec['rows']:
            if d['family']=='regional_dexes':
                for index,value in enumerate(row['value'].split(',')):
                    add(d,rec,row['line'],'ordered_member:'+str(index),value.strip())
            else:
                add(d,rec,row['line'],'encounter_method_or_slot',row['value'])
    for index,row in enumerate(d['unsectioned']):
        if d['family']=='facility_pokemon':
            for field,value in zip(['species','item','nature','effort_list','move_list'],row['atoms']):
                add(d,None,row['line'],field,value,index)
        else:
            for field,value in zip(['mapA','edgeA','coordinateA','mapB','edgeB','coordinateB'],row['value'].split(',')):
                add(d,None,row['line'],field,value,index)

with (OUT/'source-to-spec-matrix.jsonl').open('w') as stream:
    for row in rows:stream.write(json.dumps(row,ensure_ascii=False)+'\n')
reverse=[]
for family,rule in rules.items():
    for dest in rule['formal']:
        for clause in denominator:
            if clause['id'] not in dest['clauses']:continue
            reverse.append(dict(formal_clause=clause,owned_subrange=dest,rule=rule['id'],
                source=rule['consumers'],data_units_pattern=family,
                prerequisites='manual-rule-catalog.json '+rule['id'],
                status='DATA_CONTRACT_PORTION_REVIEWED; unrelated mechanics not approved',
                vector_execution='NOT_EXECUTED'))
(OUT/'spec-to-source-matrix.json').write_text(json.dumps(reverse,ensure_ascii=False,indent=2)+'\n')
inventory=json.loads((OUT/'pbs-special-structure.json').read_text())['files']
(OUT/'special-coverage.json').write_text(json.dumps(dict(files=len(inventory),record_field_units=len(rows),
    manually_reviewed_rule_families=len(rules),reverse_rows=len(reverse),
    all_record_field_structure_covered=True,raw_facility_prose_scope='Delimiter/control and text-consumption semantics, not literary quality',
    no_automatic_pass=True,semantic_notes='semantic-notes.md',rules='manual-rule-catalog.json',
    source_units='source-to-spec-matrix.jsonl',formal_units='spec-to-source-matrix.json',inventory=inventory),ensure_ascii=False,indent=2)+'\n')
with (OUT/'command-log.jsonl').open('a') as stream:
    stream.write(json.dumps(dict(operation='build_matrices.py',input='current structure files plus authored manual rule map and fixed formal clause denominator',
        output='all within R6-D',forward_rows=len(rows),reverse_rows=len(reverse),exit=0,semantic_pass_inferred=False))+'\n')
print(json.dumps(dict(forward_units=len(rows),reverse_rows=len(reverse),manual_rules=len(rules),status='NO_AUTOMATIC_PASS')))
