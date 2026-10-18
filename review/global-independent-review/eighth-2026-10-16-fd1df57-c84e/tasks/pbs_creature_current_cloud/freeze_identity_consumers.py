from pathlib import Path
import json,datetime,hashlib,re
P=Path(__file__).resolve().parent;R=Path('/workspace/pokemon-essentials');B=Path('/workspace/pokemon-essentials-clean-room')
U=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ');C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';T='7589c800b61ba13a13040ed0d686979b80a84fd0'
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def unit(path,lo,hi):return dict(repo=str(R),commit=C,tree=T,path=path,lines=[lo,hi])
BS='Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb';PK='Data/Scripts/014_Pokemon/001_Pokemon.rb';SP='Data/Scripts/010_Data/002_PBS data/008_Species.rb'
l=json.loads((P/'reading-ledger.json').read_text())
for path in [BS,'Data/Scripts/003_Game processing/005_Event_Handlers.rb']:
 if path not in l['dependencies_full_read']:l['dependencies_full_read'].append(path)
l['updated_utc']=U;save('reading-ledger.json',l)
f=json.loads((P/'bounded-pbs-facts.v7.json').read_text())
def add(title,meaning,sources):
 i=len(f['facts'])+1;f['facts'].append(dict(id=f'PC-F{i:03d}',title=title,fact=meaning,actual_reader='/root/pbs_creature_current_cloud',source_units=sources,premises=['FixedR/no overrides; allrequired priorcalls normally return except named failureroutes.','Valid usualobjects; sourceprefixes are conditional static observations, not executed state.'],evidence='SOURCE_STATIC',business='NOT_EXECUTED',qualification='Named complete sourceunits only; all external host, callbacks and unreceived body predicates remain separately OPEN.'))
add('Actual trainer-load producers',
    'TrainerBattle.generate_foes accepts existingNPCTrainer without on_trainer_load callback; Array route loads tuple type/name/version, missing feedback then retry then raises if stillnil, triggers actualtrainer callback, then applies optional speech, appends trainer/items/partystart/memberobjects. Scalar route validates type/name, optional nextInteger version else default0; successful constructedtrainer callback precedes appending sameobjects. Source doesnot make tupleversionnil equivalent to missing scalar version. Later failure preserves construction/random/callback prefix, no transaction.',[unit(BS,1,749)])
add('Actual normal trainer battle caller prefix',
    'TrainerBattle.start may store first spottedNPC aswaiting andreturnfalse; secondcall merges waitingtrainer object and only win marks its selfswitch before clearingwaiting. start_core skip gate occurs before on_start_battle; otherwise start-event precedes foeconstruction, player/partner assembly, scene/Battle construction, partystarts/items, defaultsize andprepare; clearsrules before animation/corebattle callback, after_battle thenInput/outcome write. Missing helper/media/callback can stoplaterprefix; no allnormalhost success promise.',[unit(BS,1,749)])
add('Actual wild creation and override callers',
    'WildBattle.start generates foes before optional singlefoe override event and before core skip gate. Any handled[0] nonnil returns directly, includingfalse; no normal battle/endwrapper afterward. Ordinary path passes Pokemon objects tostart_core, so generationdoesnotrepeat creation for thoseobjects. start_core skip occurs before start-event and coreassembly; wrapper end-event onlysinglefoe can_override after normalcore. Scalar generation validates identity/Integer1..maxlevel; Array goes throughpbGenerateWildPokemon; existingPokemon reused. Failures keeppriorgeneratedobject/callback prefixes.',[unit(BS,1,749)])
add('Ordinary battle cleanup before evolution receivers',
    'after_battle resets badpoison count then eachplayer makeUnmega/makeUnprimal; partnerpresence healsplayer andeachpartner thenrevertsboth; loss/drawcanLose healsplayer again before end-event. Onlythen triggers on_end_battle andstraightensplayer. End-evolve callback runs conditional evolutioncheck first, clears three trackingarrays onlyafteritreturns, thenPickup/Honey forwin/capture orblackout foruncancelledloss. A later exception doesnotundo earlierreverts/heals/evolution ortrackingprefix.',[unit(BS,1,749),unit(BS,1,749)])
add('Actual postbattle evolution selector',
    'pbEvolutionCheck iteratespartyorder, skipsnil/egg andconfiguredfainted. Onlyactualtrackedlevelincrease checkslevel-up first; ifnil result thenafter-battle callback bypartyindex. Nonniltarget constructsScene,starts,evolves,ends before nextmember. CancelhandledinsideEvolutionScene doesnot globallyundo priorparty entries; exceptionprevents laterparty/outertrackingclear. This isactualproducer→Pokemonchecks→EvolutionUI chain.',[unit(BS,1,749),unit(PK,976,1044),unit('Data/Scripts/016_UI/001_Non-interactive UI/004_UI_Evolution.rb',1,276)])
add('Own full primitive event dispatch reception',
    'Own complete298 Event/NamedEvent/HandlerHash/HandlerHashSymbol nowread inaddition to originalkernel finitefacts. Event trigger hasarity-dependent sender/restarray behavior; NamedEvent spreadsargs inhashorder. HandlerHash trigger doesnotprependid, Symbolvariant normalizesid lookup andprependsnormalizedsymbol; exacttruthyhandler precedesconditions, copysharesresolvedhandler. ConcreteFormHandlers/Item/Wild/Trainer producers therefore keepactualargumentshape, never one universalautomatic eventmodel. Exceptions stoplatercallbacks without rollback.',[unit('Data/Scripts/003_Game processing/005_Event_Handlers.rb',1,298)])
f['schema']='gr8-bounded-pbs-source-facts/v8';f['utc']=U;f['supersedes_finite_source_packet']='bounded-pbs-facts.v7.json retained';f['mandatory_companions']=['mandatory-locator-clarification.v2.json','mandatory-item-schema-clarification.v1.json'];save('bounded-pbs-facts.v8.json',f)

old=json.loads((P/'reverse-mapping.json').read_text());save('reverse-mapping.v5.frozen.json',old);new=[]
F18='deliverables/final-specification-set/creature-rpg/wp18-creature-identity-species-ownership.md';F19='deliverables/final-specification-set/pokemon-rules/wp19-attributes-ability-and-stats.md'
def atom(id,formal,line,text,sources,refs):new.append(dict(id=id,formal=dict(path=formal,lines=[line,line]),assertion=text,sourcefact_ids=refs,source_units=sources,actual_reader='/root/pbs_creature_current_cloud',status='FINITE_ASSERTION_MATCHED_SOURCE_STATIC',qualification='Exact stated attribute/predicate only; defaultconstructor isnotauthorPBSacceptance andneitherother paragraphpredicates nor execution are inferred.'))
# Full tableN and Nature173 were actually read, including every coordinate;
# this direct manual value table is not recovered from hashes or an oldPASS.
N=[('HARDY',None,None),('LONELY','ATTACK','DEFENSE'),('BRAVE','ATTACK','SPEED'),('ADAMANT','ATTACK','SPECIAL_ATTACK'),('NAUGHTY','ATTACK','SPECIAL_DEFENSE'),('BOLD','DEFENSE','ATTACK'),('DOCILE',None,None),('RELAXED','DEFENSE','SPEED'),('IMPISH','DEFENSE','SPECIAL_ATTACK'),('LAX','DEFENSE','SPECIAL_DEFENSE'),('TIMID','SPEED','ATTACK'),('HASTY','SPEED','DEFENSE'),('SERIOUS',None,None),('JOLLY','SPEED','SPECIAL_ATTACK'),('NAIVE','SPEED','SPECIAL_DEFENSE'),('MODEST','SPECIAL_ATTACK','ATTACK'),('MILD','SPECIAL_ATTACK','DEFENSE'),('QUIET','SPECIAL_ATTACK','SPEED'),('BASHFUL',None,None),('RASH','SPECIAL_ATTACK','SPECIAL_DEFENSE'),('CALM','SPECIAL_DEFENSE','ATTACK'),('GENTLE','SPECIAL_DEFENSE','DEFENSE'),('SASSY','SPECIAL_DEFENSE','SPEED'),('CAREFUL','SPECIAL_DEFENSE','SPECIAL_ATTACK'),('QUIRKY',None,None)]
NP='Data/Scripts/010_Data/001_Hardcoded data/009_Nature.rb';ns=(R/NP).read_text().splitlines();fl=(B/F19).read_text().splitlines();zh={None:'无','ATTACK':'攻击','DEFENSE':'防御','SPEED':'速度','SPECIAL_ATTACK':'特攻','SPECIAL_DEFENSE':'特防'}
for i,(name,up,down) in enumerate(N):
 line=89+i;cells=[v.strip() for v in fl[line-1].split('|')[1:-1]];assert cells==[str(i),name,zh[up],zh[down]]
 si=next(j for j,s in enumerate(ns) if re.search(r':id\s*=>\s*:'+name+r',?$',s.strip()));lo=si;hi=si+1
 while hi<len(ns) and ns[hi]!='})':hi+=1
 for key,val in [('index',i),('identity',name),('up',up),('down',down)]:atom(f'PCR-NATURE-{name}-{key}',F19,line,f'{name} {key}={val}',[unit(NP,lo,hi+1),unit(PK,497,539)],['PC-F028'])

defaults=[(88,'species','id'),(88,'form',0),(89,'real_name','Unnamed'),(89,'real_category','???'),(89,'real_pokedex_entry','???'),(90,'real_form_name',None),(91,'pokedex_form','own_form'),(92,'types',['NORMAL']),(92,'base_stats_nonpositive_or_missing_each_main',1),(92,'evs_negative_or_missing_each_main',0),(93,'base_exp',100),(93,'growth_rate','Medium'),(93,'gender_ratio','Female50Percent'),(94,'catch_rate',255),(94,'happiness',70),(94,'egg_groups',['Undiscovered']),(94,'hatch_steps',1),(95,'height',1),(95,'weight',1),(95,'color','Red'),(95,'shape','Head'),(95,'habitat','None'),(95,'generation',0)]
for key in ['moves','tutor_moves','egg_moves','abilities','hidden_abilities']:defaults.append((96,key,[]))
for key in ['wild_item_common','wild_item_uncommon','wild_item_rare','offspring','evolutions','flags']:defaults.append((97,key,[]))
for key in ['incense','mega_stone','mega_move']:defaults.append((98,key,None))
for key,val in [('unmega_form',0),('mega_message',0),('pbs_file_suffix','')]:defaults.append((99,key,val))
for line,key,val in defaults:atom('PCR-SPECIES-DEFAULT-'+key,F18,line,f'Givenvalidid/mainstatregistry, absent {key}→{val!r}',[unit(SP,175,221)],['PC-F004','PC-F005'])

for id,line,text,refs in [
 ('SPECIES-BASE-KEY',51,'Base id=species symbol,form0; positiveform compoundid retainsseparatebasespecies/form',['PC-F004','PC-F005']),
 ('SPECIES-LOOKUP-TRIAL',52,'get_species_form triescompoundkey beforebasekey',['PC-F004','PC-F005']),
 ('SPECIES-LOOKUP-MISS',52,'Bothcompound/baseabsent→nil',['PC-F004','PC-F005']),
 ('SPECIES-EACH-BASE',53,'each_species yields onlyform0',['PC-F004','PC-F005']),
 ('SPECIES-COUNT-BASE',53,'species_count counts onlyeach_species',['PC-F004','PC-F005']),
 ('SPECIES-FORM-SCALARS',54,'Undefined listedscalar fields inheritbase values; notform_name/PokedexForm/Megafields',['PC-F005']),
 ('SPECIES-FORM-COLLECTIONS',54,'Undefined listedcollections clonebaseoutercontainer',['PC-F005']),
 ('SPECIES-FORM-MOVES',54,'Missingorempty Moves copieseachbasemoveentry',['PC-F005']),
 ('SPECIES-FORM-EVOS',54,'Missingorempty Evolutions copieseachbaseentry',['PC-F005','PC-F006']),
 ('SPECIES-FORM-WILDTRIPLE',54,'Wilditemtriple inherits onlyallthreerawhashfieldsnil; explicitonepreventswholetripleinheritance',['PC-F005']),
 ('SPECIES-BASEFORM',101,'base_form takesDefaultForm_N elseownform',['PC-F023']),
 ('SPECIES-FLAG-CASE',101,'has_flag? comparesdowncasedstrings',['PC-F023']),
 ('SPECIES-STAT-TOTAL',101,'base_stat_total sumsmainstatvalues',['PC-F028']),
]:atom('PCR-'+id,F18,line,text,[unit(SP,154,221),unit(SP,243,265),unit('Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',448,485)],refs)

for id,line,text in [
 ('TYPES-COPY',34,'Pokemon.types returns fullselectedrecordtypes.clone'),('TYPES-FIRST',35,'type1 firstentry'),('TYPES-SECOND',35,'type2 secondentry elsefirst'),('TYPES-RESOLVE',36,'hasType? strictType.get normalization thenfull include?'),('TYPES-NOHARD2',37,'Compileruniq/compact andPokemonclone donottruncate2'),
 ('GENDER-VALUES',41,'gender returns0male/1female/2genderless'),('GENDER-CACHE',43,'Unfilledgender cachecomputed once; storedgender reused'),('GENDER-LOWBYTE',44,'Mixedratio usesPID&0xFF'),('GENDER-LESS',45,'Femaleonlywhenlowbyte<femalechance; equalitymale'),('GENDER-SET',47,'Mixedgender setter accepts0/1/nil; invalidignored'),('GENDER-SINGLE',48,'Single-gender setter no-op'),
 ('ABILITY-PARITY',64,'Uncachedability_index PID&1'),('ABILITY-CACHE',66,'Existingability cache wins'),('ABILITY-HIDDEN',67,'Index>=2 reads hidden[index-2], absent fallsback localparity'),('ABILITY-NATURAL',68,'Natural[index] elseNatural0'),('ABILITY-EMPTY',69,'Noavailableability returnsnil'),('ABILITY-SET',70,'Registeredoverride accepted evenoutsidespecies; unknownignored;nilclears'),('ABILITY-INDEX',71,'Setter writes indexandclearsresolvedcache; Integerdomain unrestricted'),('ABILITY-HIDDENQUERY',72,'Hiddenqueryusesstoredindex>=2 independentlyofresolvedfallback'),('ABILITY-CANDIDATES',73,'Allnatural nonnilindices thenallhidden nonnilposition+2; noindexcollisionmerge'),
 ('NATURE-PID',79,'Uncachednature indexes orderedNature byPID%count andcaches'),('NATURE-SET',81,'Nature setter registered/nilonly;calc_stats onlywhenno calculationoverride'),('NATURE-CALC',82,'Calculationoverride setter registered/nil thenalwaysrecalc'),('NATURE-HASNATURE',83,'hasNature? noargcheckscurrentcache withoutforcingderive')]:
 atom('PCR-'+id,F19,line,text,[unit(PK,313,539),unit('Data/Scripts/021_Compiler/002_Compiler_CompilePBS.rb',283,331)],['PC-F026','PC-F027','PC-F028'])
for chance,line in [(32,46),(64,46),(128,46),(192,46),(224,46)]:atom(f'PCR-GENDER-CHANCE-{chance}',F19,line,f'CorrespondingFemaleRatioregistrationfemale_chance={chance}',[unit('Data/Scripts/010_Data/001_Hardcoded data/002_GenderRatio.rb',55,83),unit(PK,341,357)],['PC-F026'])
for key,value in [('AlwaysMale',0),('AlwaysFemale',1),('Genderless',2)]:atom('PCR-GENDER-FIXED-'+key,F19,42,f'{key} fixedgender={value}',[unit('Data/Scripts/010_Data/001_Hardcoded data/002_GenderRatio.rb',40,54),unit(PK,341,357)],['PC-F026'])
assert len(new)==185,len(new)
old['schema']='gr8-pbs-current-reverse/v6';old['utc']=U;old['clauses'].extend(new);old['identity_attribute_addendum_atoms']=len(new);old['atom_denominator_frozen_so_far']=len(old['clauses']);old['supersedes']='reverse-mapping.v5.frozen.json retained';save('reverse-mapping.json',old)
for n in ['bounded-pbs-facts.v8.json','reverse-mapping.json']:
 b=(P/n).read_bytes();print(n,len(b),hashlib.sha256(b).hexdigest())
print('utc',U,'facts',len(f['facts']),'newatoms',len(new),'allatoms',len(old['clauses']),'fullsources',len(l['dependencies_full_read']))
