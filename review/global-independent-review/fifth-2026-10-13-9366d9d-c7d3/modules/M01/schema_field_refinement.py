"""Audit metadata only. Does not execute reference code or a behavior model."""
import review_state as s

d=s.read('schema-field-contracts.json')
details={}
def put(family, mapping):
 for key,value in mapping.items():details[(family,key)]=value
put('town_map',{
 'SectionName':('Nonnegative region identity; independent from map ID and regional dex ID.','required identity'),
 'Name':('Region display name; REGION_NAMES dictionary key.','???'),
 'Filename':('Regional map image resource name used by map and dex Area consumers; no file existence validation in PBS compilation.','null'),
 'Point':('Ordered tuple x,y,location name,optional location description,optional flight map,x,y,visibility switch. Labels and flight use first same-coordinate row; habitat visibility uses union of eligible rows.','empty list'),
 'Flags':('Authored region metadata flags; case-insensitive exact whole-flag query. This declaration does not itself assign a gameplay effect to arbitrary flags.','empty list')})
put('moves',{
 'Power':('Nonnegative base power; zero-power damaging category is normalized to Status by compilation, while positive-power Status is rejected. Effect-specific variable power is a separate consumer.','0'),
 'Accuracy':('Nonnegative base accuracy parameter; zero bypasses ordinary accuracy checks, not all target/use qualifications.','100'),
 'TotalPP':('Nonnegative base PP; zero means unlimited at the documented PP consumers, not missing move identity.','5'),
 'Priority':('Signed base move priority, before ability and dynamic priority adjustments.','0'),
 'EffectChance':('Nonnegative additional-effect parameter; ordinary effect probability and specialized overrides are distinct. Compiler does not cap it at100.','0'),
 'FunctionCode':('Effect identity string resolved at battle construction; unknown well-formed effect identity uses the unimplemented fallback. Unknown Status fails locally; a damaging fallback retains ordinary damage with no special effect.','None'),
 'Type':('Registered authored type, distinct from computed use-time type; per-type physical/special fallback is independently configured.','NONE'),
 'Category':('Exact Physical/Special/Status tokens map to0/1/2; data predicates for damaging/status use this category even when old type-based classification is selected.','Status'),
 'Target':('Registered target-kind identity supplies target count, range and foe-side/all flags. Effects may change the actual target kind at use time.','None')})
put('items',{
 'NamePlural':('Plural ordinary display text, separately looked up in ITEM_NAMES_PLURAL. It is not inferred from Name during ordinary record construction.','Unnamed'),
 'PortionName':('Optional singular portion text; null falls back to localized ordinary name, while explicit empty text remains an empty result.','null'),
 'PortionNamePlural':('Optional plural portion text; null falls back to localized ordinary plural, not to singular portion text.','null'),
 'Price':('Nonnegative purchase-price data; editor maximum and currency setter bounds are different constraints.','0'),
 'SellPrice':('Nonnegative full sale-price data; absent value is integer half of purchase price. Explicit zero remains zero.','floor(Price/2)'),
 'BPPrice':('Nonnegative BP purchase-price data, independent from monetary Price.','1'),
 'Pocket':('Positive 1-based bag pocket number. Text validation does not prove the configured pocket exists or has capacity.','1'),
 'FieldUse':('Exact enum OnPokemon1,Direct2,TM3,HM4,TR5; absence0 means no ordinary field use. Machine classification follows these values.','0'),
 'BattleUse':('Exact enum OnPokemon1,OnMove2,OnBattler3,OnFoe4,Direct5; absence0. Target-selection and execution contracts differ by this context.','0'),
 'Move':('Optional registered teaching move; independent from the item name or apparent TM number.','null'),
 'Consumable':('Absent value is inverse importance; effective consumption also requires nonimportance. Explicit true cannot make KeyItem/TM/HM effectively consumable.','not important'),
 'ShowQuantity':('Effective quantity predicate is true when explicit true OR nonimportant. Explicit false cannot suppress ordinary-item quantities. Bag registered-icon display can separately suppress the number.','null; effective predicate depends on importance')})
put('berry_plants',{
 'HoursPerStage':('Strictly positive hours per growth stage; plant consumer converts hours to seconds.','3'),
 'DryingPerHour':('Nonnegative moisture loss per hour; actual drying is gated by plant mode and timers.','15'),
 'Yield':('Two values: nonnegative lower yield and strictly positive upper yield; constructor swaps descending endpoints. Actual yield additionally depends on mode/watering/moisture.','[2,5]')})
species={
 'Name':('Base-species name, localized in SPECIES_NAMES; form schema does not declare it.','Unnamed'),
 'FormName':('Optional localized form label; absent/empty affects dex grouping and omission, not numeric form existence.','null'),
 'Category':('Localized species category label; independent from move Category.','???'),
 'Pokedex':('Raw post-preprocessing species-description text, localized in POKEDEX_ENTRIES. It does not generate game mechanics.','???'),
 'GenderRatio':('One of eight fixed identities; three fixed-sex/genderless records have no threshold, the five mixed ratios use byte thresholds32,64,128,192,224.','Female50Percent'),
 'GrowthRate':('One of six fixed growth identities; level-table lookup precedes the separately registered out-of-table formula after configured maximum-level clamping.','Medium'),
 'BaseExp':('Strictly positive defeated/captured experience-yield input; participant, scaling, foreign-owner and other multipliers belong to the consumer.','100'),
 'CatchRate':('Nonnegative capture base. Its unsigned text grammar does not impose a255 cap; ball and capture calculation apply their own gates/bounds.','255'),
 'Happiness':('Nonnegative authored initial friendship copied by creature creation; later friendship setters/modifiers have separate0..255 and optional soft-cap behavior.','70'),
 'Types':('Ordered registered type list; compiler deduplicates. No general two-type cap in data/query.','[NORMAL]'),
 'BaseStats':('Six positive text columns are HP,Attack,Defense,Speed,SpAtk,SpDef. Record construction fills missing/nonpositive named main stats with1.','each main stat1'),
 'EVs':('Repeated registered stat/positive yield pairs; later occurrence of a stat overwrites its prior yield. Missing/negative main-stat values are filled0 during construction.','each main stat0'),
 'Abilities':('Ordered regular ability identities; position determines ordinary ability slot, with explicit individual overrides and unavailable-slot fallback handled by WP19.','empty list'),
 'HiddenAbilities':('Ordered hidden ability identities; logical slots start after the two ordinary slots. Not randomly selected merely by this declaration.','empty list'),
 'Moves':('Ordered level/move pairs; level0 is permitted and used for evolution learning. Default-move reset follows authored order and current level/capacity.','empty list'),
 'TutorMoves':('Ordered teaching-compatibility identities; no automatic deduplication inferred from input-list syntax.','empty list'),
 'EggMoves':('Ordered egg-move identities; direct family query may fall back to preceding species/form. Not equivalent to the current known-move list.','empty list'),
 'EggGroups':('Registered breeding-group identities; Undiscovered rejection and Ditto treatment occur in compatibility consumers.','[Undiscovered]'),
 'HatchSteps':('Strictly positive initial hatch-step count, with no PBS maximum; editor99999 ceiling is not a compiler invariant.','1'),
 'Incense':('Optional registered breeding-incense item used when resolving which pre-evolution may be produced.','null'),
 'Offspring':('Allowed alternative offspring species; base text references are deferred to final validation, form references require current registry identities. Consumer intersects permitted family relationships.','empty list'),
 'Height':('Restricted decimal input converted to rounded tenths of a meter with minimum stored1. Display and individual size calculations consume that stored unit.','stored1 (0.1m)'),
 'Weight':('Restricted decimal input converted to rounded tenths of a kilogram with minimum stored1. Battle effective weight can differ through form, temporary change, abilities and items.','stored1 (0.1kg)'),
 'Color':('Fixed body-color identity used in dex search/display metadata.','Red'),
 'Shape':('Fixed body-shape identity; icon index and search identity are separate.','Head'),
 'Habitat':('Fixed habitat identity. Does not replace encounter-table-based Area highlighting.','None'),
 'Generation':('Signed content-generation metadata; does not select mechanics configuration or activate a PBS backup.','0'),
 'WildItemCommon':('Ordered common wild-held-item pool; used by wild generation, not by every creature constructor.','empty list'),
 'WildItemUncommon':('Ordered uncommon wild-held-item pool, distinct from the common/rare branches.','empty list'),
 'WildItemRare':('Ordered rare wild-held-item pool. Forms inherit all three pools together only when all are unspecified.','empty list'),
 'Evolutions':('Legacy plural list of target/method/parameter triples; shares destination with singular Evolution and is consumed according to schema order. Export suppresses this old spelling.','empty list'),
 'Evolution':('Repeatable target/method/optional-parameter records. Parameter requirements depend on the registered method; reverse links are generated after forward definitions. None is a declared non-evolving relation.','empty list'),
 'PokedexForm':('Display-form grouping number; absent takes record form. Actual listability also depends on name and self-display mapping.','record form'),
 'MegaStone':('Registered held-item condition for this form; checks coexist with the alternative MegaMove condition.','null'),
 'MegaMove':('Registered known-move condition for this form; it is not itself a command to learn the move.','null'),
 'UnmegaForm':('Ordinary source/restored form number for the Mega relation.','0'),
 'MegaMessage':('Nonnegative presentation variant; default standard message, Rayquaza-style variant is a distinct configured input.','0')}
for fam in ['pokemon','pokemon_forms']:put(fam,species)
put('pokemon_metrics',{
 'SectionName':('Registered species plus optional positive form, with omitted form0 canonicalized to base identity.','base form0'),
 'BackSprite':('Signed x/y offsets for the player/back side, applied at twice stored scale.','[0,0]'),
 'FrontSprite':('Signed x/y offsets for the foe/front side, applied at twice stored scale.','[0,0]'),
 'FrontSpriteAltitude':('Signed vertical lift of front sprite, separate from its position pair and ground shadow.','0'),
 'ShadowX':('Signed foe shadow horizontal offset; player shadow does not use this offset.','0'),
 'ShadowSize':('Nonnegative generic shadow resource selector; a species-specific shadow resource can take precedence.','2')})
put('shadow_pokemon',{'GaugeSize':('Strictly positive maximum heart gauge for Shadow creation.','4000'),'Moves':('Ordered registered Shadow move identities; limited display/known-move slots and restoration are consumer rules.','empty list'),'Flags':('Case-insensitive exact metadata flags, without an effect inferred merely from presence.','empty list')})
put('trainer_types',{'Gender':('Exact aliases Male/male/M/m/0→0; Female/female/F/f/1→1; Unknown/unknown/Other/other/Mixed/mixed/X/x/2→2. All-uppercase full words are not implicit aliases.','2'),'BaseMoney':('Unsigned payout coefficient multiplied by the highest party level before subsequent rewards/bounds.','30'),'SkillLevel':('Unsigned AI skill; absence takes BaseMoney, not always30. Editor9999 is not the PBS maximum.','BaseMoney'),'IntroBGM':('Optional encounter-introduction audio; valid nonempty input participates in prior-music memory selection before request.','null'),'BattleBGM':('Optional trainer battle track; ordinary trainer arrays take last nonnull value then empty fallback, direct-type helper differs.','null'),'VictoryBGM':('Optional trainer victory track with analogous ordered candidate and fallback rules.','null')})
put('trainers',{
 'Items':('Ordered registered trainer item resources; duplicates retained. Battle/AI use depends on item contexts.','empty list'),
 'LoseText':('Raw defeated-trainer speech, localized in TRAINER_SPEECHES_LOSE.','...'),
 'Pokemon':('Starts a member record with registered species and strictly positive bounded level; compile requires nonempty team but no MAX_PARTY_SIZE team cap.','no member'),
 'Form':('Nonnegative explicit form applied through the simple form assignment after normalized-base species creation.','no override'),
 'Name':('Nonempty explicit nickname is localized in POKEMON_NICKNAMES and applied after friendship; compiler checks nickname length.','no nickname override'),
 'Moves':('Explicit nonempty moves learned in order; compiler removes duplicate moves. Missing/empty list resets to the default level-learned list.','default moves'),
 'Ability':('Explicit ability override; absent clears the ability cache after selecting AbilityIndex.','null override'),
 'AbilityIndex':('Unsigned ability slot; absent becomes ordinary slot0 for NPC construction.','0'),
 'Item':('Optional registered initial held item, directly applied to constructed member.','null'),
 'Gender':('Only exact male/female aliases; absent requests male iff trainer type is male, otherwise female, subject to immutable species-sex setter. Unknown trainer type therefore does not mean random member sex.','trainer male ? male : female'),
 'Nature':('Explicit registered nature, else index=(zero-based base-species registration index+zero-based trainer-type registration index) modulo Nature count; index fallback1 only for an absent key.','deterministic registration-order choice'),
 'IV':('One to six unsigned text values in PBS stat order; omitted trailing components repeat the first value at compilation, each capped by validation31. Direct partial record hashes instead fill absent stat keys0.','if entire field absent: min(floor(level/2),31) each'),
 'EV':('One to six unsigned text values in PBS stat order; trailing components repeat first, each<=252 and total<=510. Direct partial hashes fill0.','if entire field absent: min(floor(3*level/2),85) each'),
 'Happiness':('Explicit nonnegative value must be<=255 at compile and overrides species-derived friendship.','no override'),
 'Shiny':('Boolean ordinary shininess is explicitly false when absent, rather than leaving the creature random result. Omitted on export when SuperShiny true.','false'),
 'SuperShiny':('Boolean super-shiny state explicitly false when absent; independent display toggle applies later.','false'),
 'Shadow':('True invokes Shadow creation after other attributes, then clears ordinary shininess; false/absent does not invoke it.','false'),
 'Ball':('Registered item additionally validated as a ball; applies after Shadow handling.','ordinary constructed ball')})
put('metadata',{'StartMoney':('Initial player money copied directly at construction; unsigned PBS field has no configured-currency-maximum check.','3000'),'StartItemStorage':('Ordered item identities, each occurrence adds one when PC item storage is first created.','empty list'),'Home':('Required global fallback return destination map,x,y,direction; map positive, other components nonnegative, not automatically valid map geometry.','null in constructor; compiler requires global Home'),'StorageCreator':('Localized storage-author display name; null/empty translated result falls back to script-localized Bill.','Bill display fallback')})
for k,kind in [('WildBattleBGM','wild battle'),('TrainerBattleBGM','trainer battle'),('WildVictoryBGM','wild victory'),('TrainerVictoryBGM','trainer victory'),('WildCaptureME','capture success'),('SurfBGM','surfing'),('BicycleBGM','cycling')]:
 put('metadata',{k:(f'Optional global {kind} audio candidate; selection and fallback occur at the corresponding consumer, not in the data declaration.','null')})
put('player_metadata',{'TrainerType':('Registered trainer type of this player content identity. Unknown player content lookup falls back to record1.','null'),'WalkCharset':('Walking character resource base name; no constructor fallback if absent.','null'),'RunCharset':('Running resource; absence falls back to effective walking resource.','WalkCharset'),'CycleCharset':('Cycling resource; absence falls back to effective running resource.','RunCharset'),'SurfCharset':('Surfing resource; absence falls back to effective cycling resource.','CycleCharset'),'DiveCharset':('Diving resource; absence falls back to effective surfing resource.','SurfCharset'),'FishCharset':('Fishing resource; absence falls back to effective walking resource.','WalkCharset'),'SurfFishCharset':('Surf-fishing resource; absence falls back to effective fishing resource.','FishCharset'),'Home':('Player-specific return destination; consumers prefer it over global Home.','null')})
map_rules={'Name':'Localized map name; empty result falls back to raw MapInfos name. PN replacement mutates the returned shared text in place when a player exists.','Outdoor':'Outdoor environment gate for tint and several movement/field abilities.','ShowArea':'Permission to request location announcement on actual map change, still subject to same-name and blocked-pair suppression.','Bicycle':'Allows bicycle usage where the ordinary movement consumer checks it.','BicycleAlways':'Forces bicycle during map entry and blocks ordinary surfing qualifications.','HealingSpot':'Return destination map,x,y written to the current healing spot on entry; no direction component.','Weather':'Registered world weather plus unsigned chance; entry samples0..99<chance and has no100 cap in compiler.','MapPosition':'Regional-map identity plus base grid x,y; region is not the game map ID.','DiveMap':'Positive linked underwater map ID; reverse surfacing searches maps referencing the current map.','DarkMap':'Creates darkness presentation and qualifies Flash; state lifecycle is separate.','SafariMap':'Includes a map in an active Safari region; does not start a Safari session.','SnapEdges':'Clamps camera display coordinates to map/screen bounds at the actual assignment consumer.','StillReflections':'Suppresses horizontal reflection ripple, independent from global reflection switch and raised-water tint hiding.','Dungeon':'Requests random dungeon layout at map creation. Does not prove bundled source map geometry exists.','BattleBack':'Optional battle-background resource stem used after rule/preselection/surfing candidates.','MapSize':'Unsigned width plus shape text. Region cursor uses length; dex habitat uses actual occupied characters, so these projections differ.','Environment':'Registered default battle environment; tile context can refine it and explicit battle rule can override it.'}
put('map_metadata',{k:(v,'null') for k,v in map_rules.items()})
for k in ['WildBattleBGM','TrainerBattleBGM','WildVictoryBGM','TrainerVictoryBGM','WildCaptureME']:put('map_metadata',{k:(f'Map-specific {k} resource candidate before global fallback; null/empty handling belongs to audio consumer.','null')})
tiles={'Autotile':'Repeated nonnegative autotile index and symbolic purpose; stored tile identity uses48*index, with specialized walls expansion.','Tile':'Repeated nonnegative regular index and symbolic purpose; normal stored identity384+index, with specialized walls expansion.','SnapToLargeGrid':'Snaps generated room placement to the larger tile grid.','LargeVoidTiles':'Uses2x2 void variants/parity.','LargeWallTiles':'Uses larger wall offset layouts; combined independently with DoubleWalls.','LargeFloorTiles':'Uses2x2 floor variants/parity.','DoubleWalls':'Selects double-height wall offset family, independently from large walls.','FloorPatchUnderWalls':'Permits floor patches to affect cells beneath relevant walls.','ThinNorthWallOffset':'Signed offset used for thin north-wall placement.'}
put('dungeon_tilesets',{k:(v,'required list at constructor' if k in ['Autotile','Tile'] else '0' if k=='ThinNorthWallOffset' else 'false') for k,v in tiles.items()})
put('dungeon_parameters',{'DungeonSize':('Positive cell-grid width,height.','[5,5]'),'CellSize':('Positive cell width,height in map tiles.','[10,10]'),'MinRoomSize':('Positive minimum room width,height.','[5,5]'),'MaxRoomSize':('Positive maximum room width,height; random-size helper uses minimum if maximum<=minimum, else inclusive interval.','[cell width-1,cell height-1]'),'CorridorWidth':('Positive corridor width in tiles.','2'),'ShiftCorridors':('Optional random corridor-shift switch.','null/falsy'),'NodeLayout':('Symbolic active-node layout; not a fixed enum validation. Unknown layout handled by generation fallback.','full'),'RoomLayout':('Symbolic room-eligible-node layout, distinct from active graph nodes.','full'),'RoomChance':('Positive room generation chance; no compiler100 cap.','70'),'ExtraConnections':('Nonnegative additional graph connections requested.','2'),'FloorPatches':('Positive radius,positive patch chance,nonnegative smoothing rate.','[3,75,25]'),'FloorDecorations':('Nonnegative ordinary/large floor decoration density pair. Zero can reach a consumer division boundary, not guaranteed empty decoration.','[50,200]'),'VoidDecorations':('Nonnegative ordinary/large void decoration density pair.','[50,200]'),'RNGSeed':('Optional unsigned configured random seed; temporary requested seed has its own priority/clearing consumer.','null')})
phone={'Intro':'Generic opening candidates.','IntroMorning':'Nonempty morning alternatives during05:00–09:59.','IntroAfternoon':'Nonempty afternoon alternatives during14:00–16:59.','IntroEvening':'Nonempty evening alternatives during17:00–19:59; not nighttime.','Body':'Whole-body candidates used outside the split-body choice.','Body1':'First part of the two-part body choice.','Body2':'Second part; with Body1 participates in75% split-body choice, or mandatory when whole Body absent.','BattleRequest':'Rematch request used when rematches enabled and flag1; generation advances flag to2.','BattleRemind':'Rematch reminder forflag2; absent falls back to request.','End':'Optional closing candidates appended when nonempty.'}
put('phone',{k:(v+' Repeated post-preprocessing raw strings; each selected string is localized and playback splits/replaces tokens separately.','null') for k,v in phone.items()})

domains={'town_map':'REGION_NAMES','types':'TYPE_NAMES','abilities':'ABILITY_NAMES','moves':'MOVE_NAMES','items':'ITEM_NAMES','ribbons':'RIBBON_NAMES','trainer_types':'TRAINER_TYPE_NAMES'}
for f in d['fields']:
 key=(f['family'],f['field'])
 if key in details:
  f['specific_field_rule'],f['construction_default']=details[key]
 elif f['field']=='Flags':
  f['specific_field_rule']='Ordered string flags with case-insensitive exact whole-flag predicate. Specialized parameter/prefix readers retain their separately reviewed rules; arbitrary flag names do not themselves create effects.'
  f['construction_default']='empty list'
 elif f['field']=='SectionName':
  f['specific_field_rule']=f['meaning']+' This family uses the exact descriptor shown; family-specific conversion and duplicate policy are linked by its capability references.'
  f['construction_default']='identity supplied by input; special default identities only where stated'
 elif f['field']=='Name':
  f['specific_field_rule']='Authored name is a key in '+domains.get(f['family'],'the separately documented family text domain')+'; separate from registry identity.'
  f['construction_default']='Unnamed'
 elif f['field']=='Description':
  f['specific_field_rule']='Post-preprocessing raw description string, queried in the family description dictionary; it is not executed as an effect.'
  f['construction_default']='???'
 elif f['family']=='types':
  f['specific_field_rule']=f['meaning']
  f['construction_default']='0' if f['field']=='IconPosition' else 'false' if f['field'] in ['IsSpecialType','IsPseudoType'] else 'empty list'
 elif f['family']=='ribbons' and f['field']=='IconPosition':
  f['specific_field_rule']='Unsigned atlas icon position, independent of acquired-ribbon order.';f['construction_default']='0'
 else:raise ValueError('Unrefined declared field '+str(key))
 if f['family']=='pokemon_forms':f['construction_default_boundary']='Form compilation may first inherit a base value; listed constructor default applies only after that separate compilation rule.'
 if f['family']=='player_metadata':f['construction_default_boundary']='Charset fallback is for absent/null values; an explicit empty string does not take that fallback.'
 f['semantic_review_scope']='Declaration, default, compile/export and shared consumer projection reviewed; status denotes present-spec coverage, not whether the field was read.'
s.write('schema-field-contracts.json',d)
c=s.read('source-to-spec.json')
for x in c['capabilities']:
 if x['capability_id']=='M01-DATA-Item-1':x['comparison']=x['comparison'].replace('All 18 schema keys','All 16 schema keys')
 if x['capability_id']=='M01-DATA-Move-1':x['comparison']=x['comparison'].replace('Explicit 14 schema keys','Explicit 13 schema keys')
s.write('source-to-spec.json',c)
print('Refined',len(d['fields']),'declared fields; metadata only, no source/model execution')
