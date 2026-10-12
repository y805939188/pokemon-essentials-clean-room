from pathlib import Path
import json, re, subprocess

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
R = Path('/Users/dingshinn/Desktop/pokemon-framework-reference/reference/pokemon-essentials')
READ = {
 'Data/Scripts/001_Settings.rb': '1–28,130–169,414–460; all setting declarations and generation-derived definitions searched',
 'Data/Scripts/002_BattleSettings.rb': '1–140',
 'Data/Scripts/010_Data/001_GameData.rb': '1–283',
 'Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb': '1–91',
 'Data/Scripts/010_Data/001_Hardcoded data/011_TerrainTag.rb': '25–47',
 'Data/Scripts/010_Data/002_PBS data/005_Move.rb': '1–94',
 'Data/Scripts/010_Data/002_PBS data/006_Item.rb': '1–137 (schema/defaults/resource naming; editor descriptions not independently checked)',
 'Data/Scripts/010_Data/002_PBS data/008_Species.rb': '48–231',
 'Data/Scripts/010_Data/002_PBS data/009_Species_files.rb': '1–246 (resource naming/fallback; actual playback not tested)',
 'Data/Scripts/010_Data/002_PBS data/010_SpeciesMetrics.rb': '1–72',
 'Data/Scripts/010_Data/002_PBS data/011_ShadowPokemon.rb': '1–58',
 'Data/Scripts/010_Data/002_PBS data/013_Encounter.rb': '1–71',
 'Data/Scripts/010_Data/002_PBS data/014_TrainerType.rb': '1–100',
 'Data/Scripts/010_Data/002_PBS data/016_Metadata.rb': '18–66',
 'Data/Scripts/010_Data/002_PBS data/017_PlayerMetadata.rb': '9–56',
 'Data/Scripts/010_Data/002_PBS data/020_DungeonParameters.rb': '50–90',
 'Data/Scripts/010_Data/002_PBS data/021_PhoneMessage.rb': '1–100',
 'Data/Scripts/021_Compiler/001_Compiler.rb': '1–483,690–841,921–1117; deprecated helpers 486–689 only distinguished as inactive, not reviewed as a separate compatibility API',
 'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb': '1–75,211–230,388–449,646–765,809–1029,1040–1155,1233–1282',
 'Data/Scripts/021_Compiler/003_Compiler_WritePBS.rb': '1–68,291–354,403–445',
 'Data/Scripts/021_Compiler/004_Compiler_MapsAndEvents.rb': '40–81,1683–1751; conversion predicates and template bodies not checked',
 'Data/Scripts/001_Technical/003_Intl_Messages.rb': '1–823; text collection event variants inspected statically, actual maps unavailable',
 'Data/Scripts/001_Technical/002_Files/001_FileTests.rb': '1–80',
 'Data/Scripts/020_Debug/003_Debug menus/002_Debug_MenuCommands.rb': '1420–1482',
 'Data/Scripts/007_Objects and windows/002_MessageConfig.rb': '778–814 (fallback definitions only)',
 'Data/Scripts/013_Items/004_Item_Phone.rb': '437–465',
 'Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb': '96–160',
 'Data/Scripts/016_UI/013_UI_Load.rb': '300–344',
 'Data/Scripts/999_Main/999_Main.rb': '17–45',
 'Data/Scripts/003_Game processing/001_StartGame.rb': '14–40',
}
SAMPLES = {}
for directory, move_line, species_line in [('',5326,893),('Gen 5 backup/',3637,893),('Gen 6 backup/',4344,892),('Gen 7 backup/',4768,893),('Gen 8 backup/',5326,893)]:
 SAMPLES['PBS/'+directory+'moves.txt'] = f'TACKLE: {move_line}–{move_line+4}; Type/Category/Power'
 SAMPLES['PBS/'+directory+'pokemon.txt'] = f'CLEFAIRY: {species_line} and Types/Abilities/Evolution in that section'
 SAMPLES['PBS/'+directory+'types.txt'] = 'STEEL:54–59; resistance list generation boundary'
SAMPLES.update({
 'PBS/battle_facility_lists.txt':'1–25; explicit Trainers/Pokemon references enumerated',
 'PBS/metadata.txt':'1–16; global section/default starter resources and player boundary',
 'PBS/phone.txt':'1–16; Default and repeated Intro properties',
 'PBS/Shadow Pokémon backup/types_shadow_pkmn.txt':'1–7; SHADOW identity and own-type resistance',
 'PBS/Shadow Pokémon backup/shadow_pokemon.txt':'1–16; species identity, gauge and move references',
 'Text_english_core/TYPE_NAMES.txt':'1–16; named domain and key/translation pairs',
 'Text_english_core/ITEM_PORTION_NAMES.txt':'1–16; natural-language hash keys',
 'Text_english_core/SPECIES_FORM_NAMES.txt':'1–16; short nonnumeric key and form-name keys',
 'Text_english_core/SCRIPT_TEXTS.txt':'1–16,139–142; named domain, control-marker encoding and placeholders'
})

def entry(p, samples=False):
 rel=str(p.relative_to(R)); raw=p.read_bytes(); ranges=(SAMPLES if samples else READ).get(rel)
 return {'path':rel,'lines':len(raw.splitlines()),'bytes':len(raw),'material_availability':'available_readable',
         'inspection':'read_semantically' if ranges else 'inventoried_only','checked_range':ranges,
         'not_checked':'All remaining content/records and runtime behavior; lexical inventory is not parse/compile validation.'}

source_paths=set((R/'Data/Scripts/010_Data').rglob('*.rb')) | set((R/'Data/Scripts/021_Compiler').rglob('*.rb'))
source_paths |= {R/p for p in READ}
searches=[]
for pattern in ['MECHANICS_GENERATION|SCALED_EXP_FORMULA|MOVE_CATEGORY_PER_MOVE','Settings::LANGUAGES|load_message_files|Translator\\.(compile_text|extract_text)','def .*compile_text|def .*stringToKey|def _INTL|def _MAPINTL']:
 p=subprocess.run(['rg','-l',pattern,str(R/'Data/Scripts')],capture_output=True,text=True)
 paths=sorted(str(Path(x).relative_to(R)) for x in p.stdout.splitlines())
 searches.append({'pattern':pattern,'search_root':'Data/Scripts','exit_code':p.returncode,'matched_files':paths,'meaning':'Candidate/caller inventory only; individual semantic reads are separately recorded.'})

formal=ROOT/'deliverables/final-specification-set'
primary={'generic-kernel/wp02-rule-configuration-and-data-variants.md','generic-kernel/wp03-content-identity-and-schema.md','generic-kernel/wp04-pbs-lifecycle.md','generic-kernel/wp08-localization.md','test-catalog/generic-kernel-wp02-03-04.md','test-catalog/generic-kernel-wp05-06-07-08-09-10.md'}
projection={'engine-overworld/wp15-resource-matching-and-audio.md','test-catalog/engine-overworld-wp11-15-59-60.md','user-interface/wp17-messages-windows-input.md','scope-statement.md'}
formal_inventory=[]
for p in sorted(formal.rglob('*.md')):
 rel=str(p.relative_to(formal)); role='primary' if rel in primary else 'projection_or_context' if rel in projection else 'counterevidence_search_only'
 formal_inventory.append({'path':str(p.relative_to(ROOT)),'role':role,'inspection':'See spec-coverage.json; no whole-file PASS' if role!='counterevidence_search_only' else 'Text search only, not semantic coverage'})

pbs=[entry(p,True) for p in sorted((R/'PBS').rglob('*.txt'))]
translations=[entry(p,True) for p in sorted((R/'Text_english_core').rglob('*.txt'))]
materials=[]
for rel in ['Data/Scripts.rxdata','Data/messages_core.dat','knownpoint.bmp','selpoint.bmp']:
 p=R/rel; materials.append({'path':rel,'material_availability':'present' if p.exists() else 'absent','inspection':'not_reviewed','reason':'Shared readiness only; no deserialize/image/media validation.'})
payload={'schema_version':'1.0','module':'M01','reference_root':str(R),'reference_commit':'8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b','formal_commit':'1f36475d22120a0d1175967d5b17d71fe8311d88','baseline_source':'../../baseline.json','sources':[entry(p) for p in sorted(source_paths)],'PBS':pbs,'translations':translations,'materials':materials,'consumer_searches':searches,'formal_files':formal_inventory,'counts':{'010_Data':len(list((R/'Data/Scripts/010_Data').rglob('*.rb'))),'021_Compiler':4,'source_files_listed':len(source_paths),'PBS':len(pbs),'translation_files':len(translations),'formal_files':len(formal_inventory),'PBS_semantic_samples':sum(x['inspection']=='read_semantically' for x in pbs),'translation_semantic_samples':sum(x['inspection']=='read_semantically' for x in translations)},'scope_meaning':'All files under the named source/data roots inventoried, only declared ranges reviewed semantically. Counts are bounded sample/inventory counts, not completeness denominators. Data/Scripts consumer search is not all-consumer review.','not_reviewed':['Unlisted ranges in inventoried source files; all deprecated CSV API behavior.','All PBS records outside named samples, all cross-generation full dependency/compile combinations.','18 translation files fully inventoried but 14 have no semantic pair sample; no all-corpus import/export execution.','Map/event conversion internals, facility species/trainer pools, full Nature table and all other hardcoded rule registrations.','Binary messages and scripts, fonts, media, actual map/Demo and host execution; plugins/dynamic overrides.']}
(OUT/'source-scope.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(payload['counts'],ensure_ascii=False))
