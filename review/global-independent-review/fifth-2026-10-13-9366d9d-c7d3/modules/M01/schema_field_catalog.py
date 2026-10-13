"""Review-only field/consumer catalogue. No reference or behavioral execution.
Source declarations are navigated as text; outputs are independent field meanings,
positions and audit links. This is not a replacement compiler/framework.
"""
import re
from collections import defaultdict
import review_state as s
F='deliverables/final-specification-set/'
P='Data/Scripts/010_Data/002_PBS data/'
files={'town_map':'002_TownMap','types':'003_Type','abilities':'004_Ability','moves':'005_Move','items':'006_Item','berry_plants':'007_BerryPlant','pokemon':'008_Species','pokemon_forms':'008_Species','pokemon_metrics':'010_SpeciesMetrics','shadow_pokemon':'011_ShadowPokemon','ribbons':'012_Ribbon','trainer_types':'014_TrainerType','trainers':'015_Trainer','metadata':'016_Metadata','player_metadata':'017_PlayerMetadata','map_metadata':'018_MapMetadata','dungeon_tilesets':'019_DungeonTileset','dungeon_parameters':'020_DungeonParameters','phone':'021_PhoneMessage'}
# All targets were materially read in this review; package ownership alone never
# upgrades a field. Primary arbitrary-input closure can remain partial.
D={
 'id':'generic-kernel/wp03-content-identity-and-schema.md §3–6; generic-kernel/wp04-pbs-lifecycle.md §§4–5',
 'text':'generic-kernel/wp08-localization.md §§3,5,6',
 'species':'creature-rpg/wp18-creature-identity-species-ownership.md §3.1–3.2',
 'stats':'pokemon-rules/wp19-attributes-ability-and-stats.md §§3–5',
 'moves':'creature-rpg/wp20-hp-status-moves-helditem.md §5',
 'growth':'creature-rpg/wp30-growth-learning-and-friendship.md',
 'breeding':'pokemon-rules/wp34-inheritance-and-offspring.md §§3–8; creature-rpg/wp33-daycare-and-breeding-session.md §5; creature-rpg/wp35-eggs-and-hatching.md §§3–4',
 'evolution':'creature-rpg/wp31-evolution-basics.md; pokemon-rules/wp32-context-inputs-and-scenarios.md',
 'types':'pokemon-rules/wp43-types-accuracy-and-damage.md §§2–3',
 'capture':'pokemon-rules/wp38-capture-and-receiving.md',
 'wild':'creature-rpg/wp36-wild-encounters-and-modifiers.md §§3–6',
 'forms':'pokemon-rules/wp21-dynamic-forms-and-display.md; pokemon-rules/wp62-pokedex-records-regions-and-content.md §§4–6',
 'mega':'pokemon-rules/wp22-mega-and-primal-reversion.md §§2–4; pokemon-rules/wp22-transformation-data.md §§1–3',
 'item':'creature-rpg/wp28-item-use-and-training.md §§3–8',
 'bag':'creature-rpg/wp27-bag-and-item-storage.md §§2–5',
 'prices':'creature-rpg/wp29-shops-and-exchanges.md §5.1',
 'resources':'engine-overworld/wp15-resource-matching-and-audio.md §§4,6',
 'region':'user-interface/wp63-pokegear-map-music-and-phone.md §3; pokemon-rules/wp62-pokedex-records-regions-and-content.md §5.3.1',
 'metadata':'creature-rpg/wp24-player-trainers-partners.md §§3,5.4; demo-dx/wp77-demo-evidence-and-capability-coverage.md §4',
 'trainer':'creature-rpg/wp24-player-trainers-partners.md §5; creature-rpg/wp18-creature-identity-species-ownership.md §4.3',
 'ribbon':'pokemon-rules/wp21-dynamic-forms-and-display.md §5.2',
 'berry':'pokemon-rules/wp60-berry-plants.md §§3–7',
 'metrics':'demo-dx/wp73-b-world-editors.md §§2,7; engine-overworld/wp15-resource-matching-and-audio.md §4.1',
 'shadow':'pokemon-rules/wp23-shadow-data-and-vectors.md §3; pokemon-rules/wp23-shadow-hyper-and-purification.md §§2–4',
 'dungeon':'engine-overworld/wp14-random-dungeons.md §§3–5',
 'weather':'engine-overworld/wp59-world-time-weather-field-moves.md §§4–5; combat-requirements/wp45-weather-terrain-side-and-position-effects.md §3',
 'map':'engine-overworld/wp11-map-topology-transfer.md §5; engine-overworld/wp12-terrain-movement-vehicles.md §5; demo-dx/wp77-demo-evidence-and-capability-coverage.md §4',
 'phone':'user-interface/wp63-pokegear-map-music-and-phone.md §5.3; demo-dx/wp77-demo-evidence-and-capability-coverage.md §5.4',
 'move_meta':'pokemon-rules/wp43-types-accuracy-and-damage.md §§2–7; combat-requirements/wp47-a-move-attributes-targeting-and-calling.md §§3–6',
 'item_flags':'combat-requirements/wp47-a-move-attributes-targeting-and-calling.md §3.1; combat-requirements/wp47-b-switching-control-and-item-changes.md §5.3; pokemon-rules/wp22-mega-and-primal-reversion.md §§3–4; creature-rpg/wp28-item-use-and-training.md §§3–8'
}
# Scope-level rules are deliberately explicit and architecture neutral.
R={}
def group(fam,keys,meaning,docs,status='supported',pending=None):
 for k in keys.split():R[(fam,k)]={'meaning':meaning,'contract_refs':[D[x] for x in docs.split()], 'status':status,'supported_boundary':'supported_static for stated field/data interface; no runtime, host, asset or full consumer-domain approval' if status=='supported' else None,'pending':pending or []}
for fam in files:group(fam,'SectionName','Record identity, separate from translated display name. Shape, composite-key handling and duplicate policy are determined by the specific family; not a universal row-number identity.','id')
for fam in ['types','abilities','moves','items','ribbons','trainer_types','town_map']:
 group(fam,'Name','Authored display text is queried by its text key in the family-specific localization domain; equal labels do not merge content identities. Missing-name constructor defaults are separate from a missing record.','text id')
for fam in ['abilities','moves','items','ribbons']:
 group(fam,'Description','Raw post-line-preprocessing text, separately localized as description. It does not specify or execute ability/item/move effects; stored text can be incomplete or differ from actual handlers.','text id')
for fam in ['types','abilities','moves','items','ribbons','town_map','pokemon','pokemon_forms','shadow_pokemon','trainer_types','map_metadata','dungeon_tilesets','dungeon_parameters']:
 group(fam,'Flags','Ordered authored string list; the generic flag predicate ignores case and tests exact whole flags. Specialized prefix/parameter readers are independent consumers. Unknown flags are retained rather than universally rejected.','id',status='partial',pending=['All specialized flag consumers mapped per family; do not infer active effects from a flag name alone'])
group('abilities','Flags','Generic case-insensitive flag predicate; actual FasterEggHatching flags add one extra step decrement after the ordinary decrement, at most once from the dynamic non-egg party. Other ability effects use identity-specific consumers.','id breeding')
group('types','IconPosition','Nonnegative icon index also sorts the Hidden Power type candidate pool; same index preserves registration order.','move_meta')
group('types','IsSpecialType','Legacy physical/special category flag read only when per-move category configuration is off; not a type-effectiveness rule.','types move_meta')
group('types','IsPseudoType','Marks pseudo types for consumers that exclude them, including Hidden Power and type-selection lists; does not itself make all attacks ineffective.','move_meta forms')
group('types','Weaknesses Resistances Immunities','Ordered type-identity references are validated after all types register; each list is deduplicated separately. Per defending type, weakness wins over resistance over immunity, yielding2,1/2,0; otherwise1. Lists do not cross-cancel conflicts.','types id')
group('moves','Type','Registered type identity; raw type is distinct from an effect-adjusted current type and is used by metadata/animation/Shadow checks.','move_meta')
group('moves','Category','Physical/Special/Status enum; compiler rejects status with positive power and warns/changes damaging zero-power entries to status. Data physical/special helpers require positive power; battle helpers are a distinct consumer.','id move_meta')
group('moves','Power Accuracy TotalPP Priority EffectChance','Base power, accuracy, PP, signed priority and additional-effect parameter are different inputs. Accuracy0 bypasses ordinary accuracy; totalPP0 is accepted and battle PP checks treat it as unlimited; chance>100 bypasses later probability modifiers; priority is signed. Values are not universally percentage-clamped.','move_meta moves')
group('moves','Target','Registered target metadata controls selectable and executed candidates, range, multi-target and foe-side flags. Dynamic effects may override it; original metadata still drives animation fallback.','move_meta')
group('moves','FunctionCode','Authored effect identity text; PBS does not reject an unknown well-formed effect name. Battle resolution has a fallback that makes status moves fail, while damaging moves keep base damage behavior. Actual optional SHADOWSHED uses the unresolved name RemoveAllScreens.','id move_meta shadow',status='partial',pending=['Current generic unknown-effect fallback contract still under complete counterevidence review'])
group('moves','Flags','All14 actual flags linked to contact/protection/mirror/calling/critical/powder/sound/pulse/punch/bite/bomb/dance/thaw/minimize consumers; relevant generations and actual-contact gates are separate from raw flag presence.','move_meta',status='partial',pending=['Complete narrow current-contract handoff for each14 flag consumer'])
group('items','NamePlural PortionName PortionNamePlural','Plural and portion names use distinct localization domains. Absent portion text falls back to the corresponding ordinary localized name; an explicitly stored empty string is not automatically absent.','text item')
group('items','Pocket','Positive authored pocket index; runtime storage uses configured pocket count/names and indexed capacities. Compiler positivity is not a proof all arbitrary positive pockets exist.','bag id')
group('items','Price SellPrice BPPrice','Nonnegative authored prices have no compiler cap. Missing purchase price0, sellprice floor(purchase/2), BPprice1; editor resource maxima and currency setters are independent restrictions.','prices')
group('items','FieldUse BattleUse Move','Independent use-context enums plus optional registered teaching move. FieldUse TM/HM/TR controls machine classification; display name such asTM57 does not. BattleUse1/2/3 require corresponding handlers at selection;4/5 do not have the same existence guard.','item')
group('items','Consumable','Missing consumption defaults to non-important; effective consumption additionally requires non-important. KeyItem/TM/HM are important, TR is not by that classification. A declared true does not make an important item consumed.','item bag')
group('items','ShowQuantity','Effective quantity visibility is explicit true OR not important. False cannot hide an ordinary item. Actual Bag additionally suppresses quantity when a registration icon is shown; PC-list and quick-menu consumers differ.','bag',status='partial',pending=['Current UI prose uses the derived predicate but its true/false default rule not yet fully counterevidence-closed'])
group('items','Flags','Allactualflags classified: KeyItem/mail/ball/berry/stone/fossil/apricorn/gem/mulch/ring predicates; first complete NaturalGift type/value and Fling number have separate prefix gates. Full67/578currentflag tables individually match. No Scent flags in optional scents, so ordinary Hyper item gates block them.','item_flags shadow',status='partial',pending=['Unused/core-unlocated category-helper consumers and all flag-context ownership ledger'])
group('berry_plants','HoursPerStage DryingPerHour Yield','Positive hours converted to stage seconds; nonnegative hourly drying; yield lower nonnegative/upperpositive, constructor swaps descending pair. Missing3/15/(2,5). Growth/yield depends on frozen mechanics and water/mulch state, not only this triple.','berry')
for fam in ['pokemon','pokemon_forms']:
 group(fam,'Name FormName Category Pokedex','Separate species/form/category/entry text domains; form names can be absent, which affects dex-form display grouping. Name is only a base-schema author field; forms inherit base name.','text species forms')
 group(fam,'Types','Registered ordered type list; compiler removes duplicates/empty elements without imposing two-type length cap. Form omission inherits a copy; runtime creature type reads copy it.','species stats types')
 group(fam,'BaseStats','Six strictly-positive authored numbers use HP/Attack/Defense/Speed/SpAtk/SpDef input columns. Constructor fills missing/nonpositive named main stats with1; input schema rejects nonpositive supplied numbers first.','species stats id',status='partial',pending=['GR5-M01-004: precise generic PBS column-order contract counterevidence'])
 group(fam,'EVs','Sequence of registered-stat/positive-value pairs; repeated stat keys take the later value. Constructor fills missing/negative main stat values0. This differs from trainer six-columnEV fields; battle reward consumers iterate main stats.','species stats id')
 group(fam,'GenderRatio GrowthRate','Registered fixed-rule identities; gender uses fixed-sex or byte thresholds, growth selects one of six declared curves and configured maximumlevel. Base-schema-only fields inherited by forms.','stats species',status='partial',pending=['Fixed GrowthRate table/formula complete current-contract closure'])
 group(fam,'BaseExp','Positive base experience yield, constructor default100; consumed with defeated/caught level and independently configured participant/scaling/reward rules.','species growth',status='partial',pending=['Complete currentWP30formula clauses plus all actual-value generation variants'])
 group(fam,'CatchRate','Nonnegative authored capture-rate base, constructor default255; capture consumer combines ball/HP/status modifiers and clamps according to its own stages, not a compiler upper bound.','species capture',status='partial',pending=['CurrentWP38capture consumer full comparison'])
 group(fam,'Happiness','Nonnegative authored starting friendship, default70; creature creation initializes it, later setters and change routines have separate caps/soft-cap policies.','species growth',status='partial',pending=['WP30 full friendship rule comparison'])
 group(fam,'Abilities HiddenAbilities','Registered ordered regular/hidden ability pools; their positions, explicit overrides and fallback rules determine selection. Compiler/data do not collapse them into a uniform list; form omission inherits respective copies.','species stats')
 group(fam,'Moves TutorMoves EggMoves','Ordered level/move pairs use nonnegativelevels, while tutor/egg lists contain registered moves. Reset selects accessible authored-order moves withkeep-latest dedup/tail slots; compatibility checks membership; breeding raw egg list differs from ancestor-aware sharing. TwoactualformTutorMoves duplicates retained.','moves breeding species')
 group(fam,'EggGroups HatchSteps Incense Offspring','Egg-group identities drive compatibility withUndiscovered rejection beforeDitto; HatchStepspositive withouteditorcap; incense gates predecessor traversal; offspring list sampled only afterbaby resolution, duplicates retainweight. Baseoffspring references deferred; form references alreadyregistered.','breeding species')
 group(fam,'Evolution Evolutions','Ordered target/method/parameter data feed family/predecessor and context-specific checks. Method parameter kind controls validation; None links family but has no triggering handler. Bothauthor aliases target samefield; singular isrepeatable andwritten, plural islegacy.','evolution id',status='partial',pending=['All current57contextsupplement sample rows and alias/output boundary comparison'])
 group(fam,'Height Weight','Unsigned restricted decimal text accepted by activecaster, then ×10 rounded and at least1 for storedtenthunits. Display/unit/weight consumers differ; malformedfloat acceptance candidate isseparate from actualvaliddecimal records.','species forms',status='partial',pending=['GR5-M01-001: active float lexical boundary current-contract counterevidence'])
 group(fam,'Color Shape Habitat Generation','Color/shape/habitat refer fixed catalogs; signed generation is metadata and doesnot selectaPBSbackup or mechanicsgeneration. Colors/shapes consumed by dexsearch; habitat/generation core gameplay use not inferred from presence.','species forms')
 group(fam,'WildItemCommon WildItemUncommon WildItemRare','Three ordered registered-item pools withindependentprobabilities; whole formgroupinherits onlyifallthreeunspecified. Wildcreation samepools specialcase andabilityprobabilities differ; pool sampling preserves multiplicity.','wild species')
 group(fam,'PokedexForm MegaStone MegaMove UnmegaForm MegaMessage','Form-only dexdisplaytarget andspecial-form conditions: sourceform match, stoneORknownmove, firstmatchingrecord, restoredefault0, message0/1presentation. All48currentMega rows andall fieldvalues match; do notuseMegaStoneflag as universaleligibility.','forms mega')
 group(fam,'Flags','Exactcase-insensitive wholeflag reads plus firstcompleteDefaultForm_N parameter; actualinheritance flags applied in species-parent thenfirsteligibleEverstoneparent order; rarityflags onlytheir specificwild/AI consumers. Nonexistentrequestedform canfall backbase, soDefaultForm_Nnot a strictformforeignkey.','species breeding wild',status='partial',pending=['AIrarityskill projection andallscalarfieldroot defaults finalcomparison'])
group('pokemon_metrics','SectionName','Registered base species plus optionalpositive form; omissioncanonicalizesform0. Querymissingpositiveform copies/registersbasevalues with emptysuffix andmaycreatebase. Doesnotrequire matchingformrecord toexist atquery.','id metrics')
group('pokemon_metrics','BackSprite FrontSprite FrontSpriteAltitude ShadowX ShadowSize','Signedposition pairs/altitude/shadowx; nonnegativesize. Defaults(0,0)/(0,0)/0/0/2. Placementscale2: even/back usesbackoffset; odd/front usesfrontoffset andsubtractsaltitude; shadowxonlyodd/foe. Sizefallbackresource selection distinctfromvisibility. Writerpathsselectedbynonzeroformrecordsuffix, equalityomissionallfivegroups.','metrics resources')
group('shadow_pokemon','GaugeSize Moves Flags','Positivegauge(default4000),orderedregisteredmoves andgenericflags(defaultempty); all131suppliedrecords matchcurrenttable. Missingformrecordfallsbackbase; no allrecordusesamegaugeassumption; activationoptional.','shadow')
group('ribbons','IconPosition','Nonnegativeatlasposition(default0); actual0..79do notsetpossessionorder. UIcropping andlocalizedselectedtext aredifferentconsumers.','ribbon resources')
group('ribbons','Flags','Genericcase-insensitive metadataflags, noactualflagfieldsin80records. Noawardworkflowinferredfromlabels/descriptions.','id ribbon')
group('trainer_types','Gender BaseMoney SkillLevel','Genderaliases mapmale0/female1/unknown2; defaultsunknown,base30,skill=base. Basevalueusedforpayout; skillusedbyAI, notalwayssameasbase; actual72records14explicitoverrides.','trainer',status='partial',pending=['AI skill bands and NPC default gender/ability/nature full counterevidence'])
group('trainer_types','IntroBGM BattleBGM VictoryBGM','Optionalresourcenames. Battle/victoryorderedtrainerarraylastnonnullwins, emptycantriggerglobal/mapfallback; directtypehelperpreservesempty. Intro request hasownmemorized/current/delayed-trackrules.','metadata resources')
group('trainer_types','Flags','Genericcase-insensitiveflags; NoName affects fulltrainerdisplay label; contentregistration andeffecthandler aliases aredistinct.','trainer id')
group('trainers','Items LoseText Pokemon','Trainerkey istype/name/optionalversion, notsectionordinal. Ordereditemlistpreserves duplicates; loseTextlocalized. Each Pokemon startsmembercontext withspecies/positivelevel; allmembersmustpassparty/levelconstraints beforefile save.','trainer id text')
group('trainers','Form Name Moves Ability AbilityIndex Item Gender Nature IV EV Happiness Shiny SuperShiny Shadow Ball','Membersubfields: formnonnegative,nicknamebounded,movesdedup,registeredability/nature/item/ball withballpredicate, IV/EVsixPBScolumns andtailrepeatfirst pluslimits, friendshipmax255. Conversionoverridesdefaultabilityindex0, gendertrainerMale?0:1, absent shiny flagsfalse anddeterministiczero-basedspecies/type-index Nature. Explicitform usesbaseidentity plusform_simple.','trainer stats item',status='partial',pending=['GR5-M01-004 sixcolumns','NPC implicitdefaultoverlay exactcurrent-contract coverage underreview'])
group('metadata','StartMoney StartItemStorage Home StorageCreator','Global0: startmoneydefault3000 copiedatplayercreation; initialitemlist addsonepervalidentryatPCstoragecreation; Home requiredbycompilerisfallbackreturnpoint, notnewgameSystemstartproof. Creatorlabel localized withBillfallback.','metadata bag text',status='partial',pending=['Constructorinitialmoney versus settercap; PC/nameconsumer clause completion'])
group('metadata','WildBattleBGM TrainerBattleBGM WildVictoryBGM TrainerVictoryBGM WildCaptureME SurfBGM BicycleBGM','Optionalaudioresource identifiers; selectionorder/surf-bike specialconsumers read. Absent andempty handledpercaller, noaudioexistenceguarantee.','metadata resources')
group('player_metadata','TrainerType WalkCharset RunCharset CycleCharset SurfCharset DiveCharset FishCharset SurfFishCharset Home','PlayercontentID record1fallback; typenameandwalkcanremainabsent atconstructor. Missingcharsets fallbackrun→walk,cycle→run,surf→cycle,dive→surf,fish→walk,surffish→fish; emptystringdoesnottriggernil-onlyfallback. Homeplayeroverridebeforeregionalglobalfallback.','metadata resources',status='partial',pending=['AllmovementcharsetselectionandHomecallerprojection alreadyreadpartly; finishcurrentWP61/65'])
group('map_metadata','Name','LocalizedMAP_NAMES value fallsbackbasicMapInfosnamewhenempty; withplayerpresent PN substitutionmutatesreturnedtextinplace. Sharedtranslationvalue/rawauthorfield/basicmapnamecanbechanged byread, dependinglookupbranch.','text map',status='partial',pending=['Exactmutation/repeatedrename current-contract counterevidence'])
group('map_metadata','Outdoor ShowArea Bicycle BicycleAlways HealingSpot Weather MapPosition DiveMap DarkMap SafariMap Dungeon BattleBack Environment MapSize Flags','All69recordsactual16fieldkinds interpreted:weatherchance,6healingtriples,regionpositions/masks,cycling/diving/darkness/safari/dungeon/contextflags. Cursorusesmasklength,habitatusesmaskchars/visiblePointunion. Individualschemaunused fieldsremainin separatecatalogrows.','map region weather dungeon',status='partial',pending=['Remaining environment/background, safari andallmapflag consumers finalcontractclosure'])
group('map_metadata','SnapEdges StillReflections','Optionalboolean cameraedge clamp andreflectionanimation gates; no actualfieldsin69maprecords. Nil/false bothfalsyfornormalconsumer,butdataabsenceisnotforeign-resourcevalidation.','map resources',status='partial',pending=['WP16 camera/reflection clauses fullcompare'])
group('map_metadata','WildBattleBGM TrainerBattleBGM WildVictoryBGM TrainerVictoryBGM WildCaptureME','Mapaudio candidates betweenpreselected/type candidate andglobaldefaults; nil/empty skippedonnormalarraypaths; logicalrequestnotplayback.','metadata resources')
group('town_map','Filename Point Flags','Regionresourcename andorderedrepeatedpoints(x,y,name,optionaldescription,flightmap,x,y,switch). Samecoordinate firstpoint governsname/details/flight; habitatvisibility usesanyvisiblepointunion; optionalhiddenislandswitch51/52. Mapregisteredstrictly beforeresourcefile lookup.','region resources')
group('dungeon_tilesets','Autotile Tile SnapToLargeGrid LargeVoidTiles LargeWallTiles LargeFloorTiles DoubleWalls FloorPatchUnderWalls ThinNorthWallOffset Flags','Repeatedsymbol/indexmapping,ordinary384+t/autotile48a,fullfourwalllayouts andparity/offsets matchWP14§5.1. Defaultsboolfalse/offset0/flagsempty. Constructoriteratesbothmappingarrays withoutnilguard; emptyregistryfallbackcannotreturna firstrecord.','dungeon id',status='partial',pending=['Actual2recordsfullyvalid; missingmappingarray andemptyregistry custominput counterevidence'])
group('dungeon_parameters','DungeonSize CellSize MinRoomSize MaxRoomSize CorridorWidth ShiftCorridors NodeLayout RoomLayout RoomChance ExtraConnections FloorPatches FloorDecorations VoidDecorations RNGSeed Flags','Allparameterdimensions/groupedtuples anddefaults feedWP14generationmath. Rawlayoutsymbolunknownfallsbackfull; densitiesallow0butmappeddecorationdivisionfails. Area/versionqueryqualified→base→freshdefaults; flagskeptthoughgeneratorconsumerunlocated.','dungeon')
group('phone','SectionName Intro IntroMorning IntroAfternoon IntroEvening Body Body1 Body2 BattleRequest BattleRemind End','Defaultspecialidentity vscontacttriple. Repeatedrawtext lists retainmultiplecandidates; per-callmessageversion fallback/timeintro/bodypair/rematch/end andTP/TEsubstitutions exactlysource-mapped. Missingmessagecollections versusemptyarraysretaintruthinessdistinctions.','phone text id')
# Discover all declared fields and preserve their exact source coordinates.
entries=[]
for fam,stem in files.items():
 path=P+stem+'.rb';raw={}
 for n,l in enumerate((s.REF/path).read_text().splitlines(),1):
  m=re.search(r'(?:"(\w+)"\s*=>|ret\["(\w+)"\]\s*=)\s*\[:\w+,\s*"([^"]+)"',l)
  if m:raw[m[1] or m[2]]=(m[3],n)
 if fam=='pokemon':
  for k in ['PokedexForm','MegaStone','MegaMove','UnmegaForm','MegaMessage']:raw.pop(k,None)
  raw['SectionName']=('m',57);raw['Offspring']=('*s',89);raw['Evolution']=('^seS',107);raw['Evolutions']=('*ses',106)
 if fam=='pokemon_forms':
  for k in ['Name','GenderRatio','GrowthRate','Incense']:raw.pop(k,None)
  raw['SectionName']=('ev',55);raw['Offspring']=('*e',86);raw['Evolution']=('^eeS',104);raw['Evolutions']=('*ees',103)
 for field,(fmt,line) in raw.items():
  review=R.get((fam,field),{'meaning':'Field not yet adjudicated','contract_refs':[],'status':'not_reviewed','supported_boundary':None,'pending':['Completefieldconsumercomparison']})
  entries.append({'field_id':fam+'.'+field,'family':fam,'field':field,'source_anchor':{'path':path,'version':s.R,'line':line},'pbs_shape_descriptor':fmt,'descriptor_contract':'WP03§5.1/WP04§4.2; exactacceptedlexicalstrings/optionals/repetition/extra-tail handling areseparate sharedprimitive contracts, notimpliedbythename',**review})
# Resolve accidental guessed WP31 title by actual basename, without assumingbody.
allformal=list((s.ROOT/F).rglob('*.md'))
for e in entries:
 e['contract_refs']=[x.replace('creature-rpg/wp31-evolution-basics.md',next((str(p.relative_to(s.ROOT/F)) for p in allformal if p.name.startswith('wp31-')),'WP31 path unresolved')) for x in e['contract_refs']]
s.write('schema-field-contracts.json',{'schema_version':'gr5.review.v1','module':'M01','source_baseline':s.R,'specification_baseline':s.B,'scope':'Everydeclaredauthorfield, includingabsentfromall73actualfiles; sourceidentity/grammarconsumerseparatefromfull-domainbehavior. Findings andpartialclausesdonotpretendnotread.', 'fields':entries})
# Attach shared field identities to every actual typed property. Do notadvance
# recordextent here: perfile semantic acceptance is aseparate reviewer decision.
lookup={e['field_id']:e for e in entries}
for f in s.read('pbs-typed-audit.json')['files']:
 name='pbs-typed-'+f['path'][4:].replace('/','--').replace(' ','_')+'.json';d=s.read(name)
 for rec in d['records']:
  for field in rec['fields']:
   ident=field['schema_family']+'.'+field['field'];review=lookup.get(ident)
   field['field_contract_ref']=ident
   field['consumer_semantic_status']=review['status'] if review else 'not_reviewed'
   field['consumer_boundary']='See schema-field-contracts.json sharedmeaning/source/currentcontract; safe literal checks alone are not semantic support.'
 s.write(name,d)
print('Declaredfieldentries',len(entries),'unmapped',[(x['family'],x['field']) for x in entries if x['status']=='not_reviewed'])
