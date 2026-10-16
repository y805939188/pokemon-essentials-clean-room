"""Record source identities and reviewed units; mechanical validation only."""
from pathlib import Path
import json,hashlib,subprocess,datetime,re
P=Path(__file__).parent
R=Path('/workspace/pokemon-essentials');B=Path('/workspace/pokemon-essentials-clean-room')
RC='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';BC='fd1df570cad987dc3852a3b958f03916e317f7fe'
RT='7589c800b61ba13a13040ed0d686979b80a84fd0';BT='751dfde81048c81390f89a65ca1d1a565ba8e1ca'
units={
'Data/Scripts/010_Data/002_PBS data/008_Species.rb':{'ranges':[[1,455]],'units':['schema/defaults/form lookup','all methods incl get_evolutions/get_baby_species and property export'],'credit':'FULL_READ'},
'Data/Scripts/010_Data/001_GameData.rb':{'ranges':[[78,155],[217,285]],'units':['ClassMethodsSymbols registry/load/save','identity equality/load-all/PBS-base-names'],'credit':'FULL_READ_SELECTED_UNITS'},
'Data/Scripts/014_Pokemon/001_Pokemon.rb':{'ranges':[[100,225],[410,580],[602,629],[890,912],[1060,1075],[1095,1230]],'units':['species/form/current data','level/egg','ability/nature/item','hasMove','height/weight/baseStats','calc_stats','initialize'],'credit':'FULL_READ_SELECTED_UNITS'},
'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb':{'ranges':[[1,715]],'units':['MultipleForms registry/call','all creation-form callbacks within range','finite UNOWN/BURMY/WORMADAM complete handlers','additional regular form handlers read as context'],'credit':'FULL_READ_SELECTED_RANGE'},
'Data/Scripts/003_Game processing/005_Event_Handlers.rb':{'ranges':[[148,204],[288,301]],'units':['HandlerHashSymbol full','SpeciesHandlerHash'],'credit':'FULL_READ_SELECTED_UNITS'},
'Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb':{'ranges':[[280,370],[380,530],[945,1022]],'units':['species validation/default and reverse edges','forms full compile/validation and reverse edges','facility list compile'],'credit':'FULL_READ_SELECTED_UNITS'},
'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/001_Challenge_BattleChallenge.rb':{'ranges':[[1,518]],'units':['all Challenge/ChallengeData/ChallengeType/FactoryData definitions'],'credit':'FULL_READ'},
'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/002_Challenge_Data.rb':{'ranges':[[1,225]],'units':['all data selectors/entry wrapper/PBPokemon compile and creation'],'credit':'FULL_READ'},
'Data/Scripts/018_Alternate battle modes/001_Battle Frontier/003_Challenge_ChooseFoes.rb':{'ranges':[[1,210]],'units':['trainer finite range, short-pool bypass, resampling, factory finite-prefix selection'],'credit':'FULL_READ'},
'Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/001_Challenge_ChallengeRules.rb':{'ranges':[[1,428]],'units':['all container and10 active factories','inactive comment examples full read but not active factory'],'credit':'FULL_READ'},
'Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/002_Challenge_Rulesets.rb':{'ranges':[[1,326]],'units':['all ruleset query/length/default/subset write/standard/direct samples'],'credit':'FULL_READ'},
'Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/003_Challenge_EntryRestrictions.rb':{'ranges':[[1,425]],'units':['all25 restrictions including cache','ordinary abilities, stat total, units, strict item/move/species','generic and nickname defined failure scope'],'credit':'FULL_READ'},
'Data/Scripts/018_Alternate battle modes/002_Battle Frontier rules/004_Challenge_LevelAdjustment.rb':{'ranges':[[1,278]],'units':['all adjustment definitions'],'credit':'FULL_READ'},
'Data/Scripts/010_Data/001_Hardcoded data/008_Stat.rb':{'ranges':[[1,133]],'units':['all stat registry/default/pbs orders'],'credit':'FULL_READ'},
'Data/Scripts/010_Data/001_Hardcoded data/001_GrowthRate.rb':{'ranges':[[1,110]],'units':['full growth-rate behavior methods1-80','Medium lookup/formula and beginning Erratic as context'],'credit':'FULL_READ_SELECTED_UNITS'},
'Data/Scripts/001_Settings.rb':{'ranges':[[131,131]],'units':['MAXIMUM_LEVEL=100 field'],'credit':'FIELD_READ'},
'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb':{'ranges':[[85,125]],'units':['complete pbGetEnvironment'],'credit':'FULL_READ_SELECTED_UNIT'},
'Data/Scripts/019_Utilities/001_Utilities.rb':{'ranges':[[1,62]],'units':['complete indexed combinations producer/next-combination'],'credit':'FULL_READ_SELECTED_UNITS'},
'PBS/battle_facility_lists.txt':{'ranges':[[1,24]],'units':['all five list sections and exact finite selected files'],'credit':'FULL_READ'},
}
# Clamp display ranges to actual file length without inventing credit beyond EOF.
for rel,v in units.items():
 n=len((R/rel).read_text(encoding='utf-8-sig').splitlines());v['ranges']=[[a,min(z,n)] for a,z in v['ranges']];v['line_count']=n
ids=[]
def identity(repo,commit,tree,rel,kind):
 p=repo/rel;raw=p.read_bytes();ls=subprocess.check_output(['git','-C',str(repo),'ls-tree',commit,'--',rel],text=True).strip()
 vals=ls.split(None,3) if ls else []
 blob=vals[2] if vals else None
 actual=subprocess.check_output(['git','-C',str(repo),'hash-object','--',str(p)],text=True).strip()
 return {'repo':str(repo),'commit':commit,'workspace_tree':tree,'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'git_mode':vals[0] if vals else None,'git_blob':blob,'actual_blob':actual,'matches_fixed':blob==actual,'purpose':kind}
for rel in units:ids.append(identity(R,RC,RT,rel,'source behavior selected units'))
cs=json.loads((P/'species-field-classes.json').read_text());projected={}
for c in cs:
 for o in c['occurrences']:projected.setdefault(o['file'],[]).append({'class':c['id'],'record_start':o['start'],'record_end':o['end'],'field_lines':o['field_lines']})
for rel in projected:ids.append(identity(R,RC,RT,rel,'finite species relevant PBS fields incl profile/forms/ancestor'))
for f in ['battle_tower_pokemon','cup_fancy_pkmn','cup_fancy_pkmn_single','cup_little_pkmn','cup_pika_pkmn','cup_poke_pkmn']:
 ids.append(identity(R,RC,RT,'PBS/'+f+'.txt','finite species collection locator; raw semantic credit delegated to parent/PBSW'))
formal=['deliverables/final-specification-set/combat-requirements/wp54-entry-rules-and-cup-data.md','deliverables/final-specification-set/combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md']
for rel in formal:ids.append(identity(B,BC,BT,rel,'WP54 predicates and explicit qualifiers, full read in this task'))
ids.append(identity(B,BC,BT,'AGENTS.md','full project instructions'))
for fn in ['inputs/eighth-global-review-prompt.md','inputs/review-SKILL.md','delegation/prompts/pbs_creature_facility.md','delegation/readsets/pbs_creature_facility.json']:
 rel='review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/'+fn;p=B/rel;raw=p.read_bytes()
 ids.append({'repo':str(B),'commit':None,'path':rel,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'type':'current R8 delegation/instructions','semantic_credit':'FULL_READ'})
(P/'identities.json').write_text(json.dumps({'frozen_B8':BC,'frozen_R':RC,'payloads':ids},ensure_ascii=False,indent=2)+'\n')
ledger={'schema':'gr8-trait-reading-ledger/v1','reviewer':'/root/pbs_creature_facility/trait_eligibility','source_units':units,'species_pbs_fields':{'credit':'FULL_READ_RELEVANT_FIELDS','occurrences':2732,'unique_exact_field_structures':649,'view':'species-fields.view.txt','view_continuous_ranges':[[1,100],[101,200],[201,300],[301,400],[401,500],[501,600],[601,649]],'raw_field_provenance':'species-field-classes.json','scope_fields':['BaseStats','Abilities','HiddenAbilities','Height','Weight','Evolution','Evolutions','Flags','Incense'],'records':projected},'formal':[{'path':p,'ranges':[[1,len((B/p).read_text().splitlines())]],'credit':'FULL_READ','target_claims':['WP54 §2 member/team/number/suggestedLevel','§3 Standard/current-form/cache/strict/team restrictions','§5 all factories/direct/mode predicates','data §1–3 finite lists and parameters']} for p in formal],'unread_within_delegated_fields':0,'acceptance':'PENDING_PARENT_INDEPENDENT_REVIEW','execution':'NOT_EXECUTED','no_credit':['full raw2770 template semantics not re-read by this child','nonqualification PBS fields not read by this child','unread portions of dependency files outside listed units','source field parsing/count does not grant semantic credit']}
(P/'reading-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
# Re-read every projected source field, validating projection losslessness of selected values.
checked=0
for c in cs:
 for o in c['occurrences']:
  lines=(R/o['file']).read_text(encoding='utf-8-sig').splitlines();found={}
  for k,lns in o['field_lines'].items():
   found[k]=[]
   for n in lns:
    kk,v=map(str.strip,lines[n-1].split('=',1));assert kk==k;found[k].append(v);checked+=1
  assert found==c['fields']
t=json.loads((P/'finite-traits.json').read_text())['records'];base=json.loads((P/'default-base-traits.json').read_text())
assert len(base)==453 and len(t)==2727
assert all(q['bst']==sum(q['base_stats']) and len(q['base_stats'])==6 for q in t)
assert base['SLAKING']['bst']==670 and base['SLAKING']['standard_non_egg']
assert base['METAGROSS']['bst']==600 and not base['METAGROSS']['standard_non_egg']
assert base['PIKACHU']['baby_species_cold']=='PICHU'
assert all(q['standard_non_egg'] for q in t if q['species']=='TYRANITAR')
assert {q['can_evolve_cold'] for q in t if q['species']=='PICHU'}=={True,False}
assert all(v['matches_fixed'] for v in ids if 'matches_fixed' in v)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(P/'validation.json').write_text(json.dumps({'evidence':'TOOL_VALIDATION_OF_STATIC_EVIDENCE_ONLY','command':'python <this-dir>/record-evidence.py','utc':now,'raw_field_values_rechecked':checked,'fixed_payload_identity_matches':sum('matches_fixed' in q for q in ids),'predicate_vectors':'NOT_EXECUTED','game_reference_model_processes':0,'checks':['all source field values round-trip projected classes','453 base and2727 direct species/form profile records','six-field sums and valid source IDs','Slaking ordinary ability early allow/Metagross600 reject','Pikachu baby Pichu','all Tyranitar forms early allowed','Pichu form valid-evolution difference','fixed identities all match'],'result':'PASS_STATIC_ARTIFACT_CHECK'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'identities':len(ids),'source_files':len(units),'field_values_verified':checked,'matches':sum('matches_fixed' in q for q in ids),'utc':now}))
