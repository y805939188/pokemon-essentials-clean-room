from pathlib import Path
import json,datetime,hashlib
P=Path(__file__).resolve().parent;UTC=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ');v=json.loads((P/'evolution-author-edges.complete.v2.json').read_text())
# Manually transcribed, actually full-read 57-row formal table. Binding below is post-reading identity/value verification only.
s='''POLIWHIRL|POLITOED|TradeItem|KINGSROCK
KADABRA|ALAKAZAM|Trade|
MACHOKE|MACHAMP|Trade|
GRAVELER|GOLEM|Trade|
SLOWPOKE|SLOWKING|TradeItem|KINGSROCK
MAGNETON|MAGNEZONE|LocationFlag|Magnetic
HAUNTER|GENGAR|Trade|
ONIX|STEELIX|TradeItem|METALCOAT
RHYDON|RHYPERIOR|TradeItem|PROTECTOR
SEADRA|KINGDRA|TradeItem|DRAGONSCALE
SCYTHER|SCIZOR|TradeItem|METALCOAT
ELECTABUZZ|ELECTIVIRE|TradeItem|ELECTIRIZER
MAGMAR|MAGMORTAR|TradeItem|MAGMARIZER
EEVEE|LEAFEON|LocationFlag|MossRock
EEVEE|GLACEON|LocationFlag|IceRock
EEVEE|ESPEON|HappinessDay|
EEVEE|UMBREON|HappinessNight|
PORYGON|PORYGON2|TradeItem|UPGRADE
GLIGAR|GLISCOR|NightHoldItem|RAZORFANG
SNEASEL|WEAVILE|NightHoldItem|RAZORCLAW
PORYGON2|PORYGONZ|TradeItem|DUBIOUSDISC
NOSEPASS|PROBOPASS|LocationFlag|Magnetic
FEEBAS|MILOTIC|TradeItem|PRISMSCALE
DUSCLOPS|DUSKNOIR|TradeItem|REAPERCLOTH
CLAMPERL|HUNTAIL|TradeItem|DEEPSEATOOTH
CLAMPERL|GOREBYSS|TradeItem|DEEPSEASCALE
BUDEW|ROSELIA|HappinessDay|
CHINGLING|CHIMECHO|HappinessNight|
HAPPINY|CHANSEY|DayHoldItem|OVALSTONE
RIOLU|LUCARIO|HappinessDay|
MANTYKE|MANTINE|HasInParty|REMORAID
BOLDORE|GIGALITH|Trade|
GURDURR|CONKELDURR|Trade|
KARRABLAST|ESCAVALIER|TradeSpecies|SHELMET
SHELMET|ACCELGOR|TradeSpecies|KARRABLAST
PANCHAM|PANGORO|LevelDarkInParty|32
SPRITZEE|AROMATISSE|TradeItem|SACHET
SWIRLIX|SLURPUFF|TradeItem|WHIPPEDDREAM
TYRUNT|TYRANTRUM|LevelDay|39
AMAURA|AURORUS|LevelNight|39
SLIGGOO|GOODRA|LevelRain|50
PHANTUMP|TREVENANT|Trade|
PUMPKABOO|GOURGEIST|Trade|
YUNGOOS|GUMSHOOS|LevelDay|20
CHARJABUG|VIKAVOLT|LocationFlag|Magnetic
CRABRAWLER|CRABOMINABLE|LocationFlag|IceRock
FOMANTIS|LURANTIS|LevelDay|34
COSMOEM|SOLGALEO|LevelDay|53
COSMOEM|LUNALA|LevelNight|53
SNOM|FROSMOTH|HappinessNight|
KUBFU|URSHIFU|Event|1
RATTATA,1|RATICATE|LevelNight|20
FARFETCHD,1|SIRFETCHD|BattleDealCriticalHit|3
CUBONE,1|MAROWAK|LevelNight|28
LINOONE,1|OBSTAGOON|LevelNight|35
YAMASK,1|RUNERIGUS|EventAfterDamageTaken|2
ROCKRUFF,2|LYCANROC|LevelEvening|25'''
expected=[z.split('|') for z in s.splitlines()];assert len(expected)==57
counts={'LevelDay':4,'LevelNight':5,'LevelMorning':0,'LevelAfternoon':0,'LevelEvening':1,'LevelNoWeather':0,'LevelSun':0,'LevelRain':1,'LevelSnow':0,'LevelSandstorm':0,'LevelCycling':0,'LevelSurfing':0,'LevelDiving':0,'LevelDarkness':0,'LevelDarkInParty':1,'HappinessDay':3,'HappinessNight':3,'DayHoldItem':1,'NightHoldItem':2,'HasInParty':1,'Location':0,'LocationFlag':6,'Region':0,'ItemDay':0,'ItemNight':0,'Trade':8,'TradeMale':0,'TradeFemale':0,'TradeDay':0,'TradeNight':0,'TradeItem':16,'TradeSpecies':2,'BattleDealCriticalHit':1,'Event':1,'EventAfterDamageTaken':1};assert len(counts)==35 and sum(counts.values())==57
selected=[];comparisons=[]
for i,(parent,target,method,param) in enumerate(expected,1):
 matches=[(j,e) for j,e in enumerate(v['edges']) if e[2]==parent and e[10]==target and e[11]==method and (e[12] or '')==param];assert len(matches)==1,(i,parent,matches)
 j,e=matches[0];selected.append(e);comparisons.append({'formal_table_row':i,'expected_complete_four_values':[parent,target,method,param or None],'source_edge_ordinal':e[0],'source_complete_edge_pointer':f'evolution-author-edges.complete.v2.json#/edges/{j}','status':'ALL4LITERALS_MATCH_AFTER_ACTUAL_FULL_READ','meaning_qualification':'Source author edge presence/type/order only; method eligibility and actual evolution remain state/caller dependent.'})
all_actual=[e for e in v['edges'] if e[11] in counts];assert len(all_actual)==57 and {e[0] for e in all_actual}=={e[0] for e in selected}
for method,number in counts.items():assert sum(e[11]==method for e in all_actual)==number
parents=[p for p in v['parents'] if (p[1],p[2]) in {(e[1],e[2]) for e in selected}];assert len(parents)==52
packet={'schema':'gr8-pbs-current-wp32-57-author-values/v1','utc':UTC,'actual_reader':'/root/pbs_creature_current_cloud','fixed_R':v['fixed_R'],'scope':'All35formalcontextmethoddistributionrows and57completeauthor-evolutionrows inWP32 appendix; exactneededcomplete19-columnsourcevectors plus52complete9-columnparentvectors. Noeligibility/runtimewholeC/pass.','actual_read_basis':{'formal_full_appendix':'f3ef7a completealltables no truncation','formal_full_main':'5729c7','all_PBS_original_raw':'reading-ledger.json and2178completefieldpackets','all_Evolution_definitions':'ownfull676; selectedTrade563–617 additionallyc53463','post_read_binding':'This script asserts manuallytranscribedreadvalues; notparser/readproof andnever executesreference.'},'formal_path':'deliverables/final-specification-set/pokemon-rules/wp32-context-inputs-and-scenarios.md','formal_method_distribution':counts,'formal_complete_expected_table':expected,'common_complete_source_premises':v['complete_common_premises'],'parent_common_semantics':v['parent_common_semantics'],'edge_columns':v['edge_columns'],'parent_columns':v['parent_columns'],'source_packet_identities':v['source_packet_identities'],'source_units':v['source_units'],'mandatory_locator_companion_complete':json.loads((P/'mandatory-locator-clarification.v2.json').read_text()),'complete_selected_edges':selected,'complete_selected_parents':parents,'manual_literal_comparisons':comparisons,'manual_semantic_join':{'data_does_not_qualify':'Allmethodrows requireordinarySpecies/Pokemon/runtimeguard/callerpremises;day/weather/map/party predicatesreadactualcurrentcontext,notauthoreddata alone. Zero source rowsdo notmeanabsentmethod.','form_specific':'Sixformrows areexplicitnonemptyEvolution andretainownorder;noforminheritanceinference frommerebaseedge.','TradeSpecies_control':'Defaulttwo parameterscrossreferencecounterpartbutactualpredicatecomparesselfbaseSpecies. Bothdefaultfailunderunchangedownbase;customselfparam+outgoingEverstonecontrol distinct.','TradeItem_control':'All16specificItemparametersstrictlytyped;incomingselectedhelditemnormalcheckandtarget+stillheldafterhookcontrolconsumption; no outgoingbagconsumption.','target_state':'Generatedprevolution/Nonefamilymarkers excludedfromrunnableevolutions; rawonly57nonprevolution authorinputs shown.'},'remaining':'Map/world-weather metadata source values andeachothercontextconsumer/newscenario beyond bounded ownsourcefacts remainOPEN unless separatelyactuallyread/received. Noall35environmentalpredicateclosure from35counts.','business':'NOT_EXECUTED','update':'UPDATE_NOT_STARTED'}
p=P/'wp32-57-authored-evolution-values.complete.v1.json';assert not p.exists();p.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'utc':UTC,'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'rows':57,'methods':35,'parents':len(parents)},ensure_ascii=False))
