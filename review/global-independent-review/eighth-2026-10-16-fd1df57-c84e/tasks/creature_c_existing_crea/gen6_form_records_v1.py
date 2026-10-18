from pathlib import Path
import json,re,hashlib,datetime,subprocess
from decimal import Decimal,ROUND_HALF_UP
C=Path(__file__).parent;R=Path('/workspace/pokemon-essentials');p='PBS/Gen 6 backup/pokemon_forms.txt';raw=(R/p).read_bytes();ls=raw.decode('utf-8-sig').splitlines();utc=datetime.datetime.now(datetime.timezone.utc).isoformat();fixed='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';assert raw==subprocess.check_output(['git','-C',str(R),'show',fixed+':'+p]);headers=[(i,re.fullmatch(r'\[([^]]+)\]',l).group(1)) for i,l in enumerate(ls,1) if re.fullmatch(r'\[([^]]+)\]',l)];g5=json.loads((C/'gen5-forms-complete-meaning.v1.json').read_text());old={x['section']:x for x in g5['complete_records']}
manual={
'KYOGRE':'Primal1 BaseStats100/150/90/90/180/160 PRIMORDIALSEA H98/W4300 Generation6; noMegaStone/MegaMove authored. BlueOrb handler condition separate, HiddenAbilities absent inherits Gen6base rather than naturaloverwrite.',
'GROUDON':'Primal1 GROUND/FIRE100/180/160/90/150/90 DESOLATELAND H50/W9997 Generation6; noMegaStone/MegaMove; RedOrb source handler independent, HiddenAbilities absent inheritedbase.',
'PICHU':'Spiky-Eared2 Generation4/PikachuNone remainsrawfamilylink, no runtimeevo target.',
'UNOWN':'27named forms1..27 B..Z/?/!;generation3only26/27. Labels only notnewstats.',
'CASTFORM':'1FIRE Red/2WATER Blue/3ICE White, eachnewPokedextext; Forecast weather battlehandler separate, baseStats inherited.',
'DEOXYS':'Attack/Defense/Speed6tuples50/180/20/150/180/20;50/70/160/90/70/160;50/95/90/180/95/90. Gen6moves at7/13/19/25/.../73 replacingGen5 9/.../97; tiedlevels at55/73 preserveorderedpairs. FullTutors includeGen6CONFIDE/DARKPULSE/POWERUPPUNCH asauthored, notsameblobG5.',
'BURMY':'Sandy1Brown/Trash2Red nowexplicitcolor vsGen5nameonly. Environmenthandlerlatercommit independent.',
'WORMADAM':'SandyBUGGROUND60/79/105/36/59/85 DEF2 Brown;TrashBUGSTEEL60/69/95/36/69/95 DEF1SPDEF1Red; allTutor lists preserveGen6CONFIDE/INFESTATION plusotheractual tokens.',
'CHERRIM':'Sunshine1Pink only, inheritedbase stats/type; FlowerGift/sourceweather dictatesfieldchange.',
'SHELLOS':'EastSea1Blue only; currentFormHandlerscopy rawstats inheritance notliteralcopythisrecord.',
'GASTRODON':'EastSea1Blue only, base inherited separately.',
'ROTOM':'Allfive appliances nowexplicitBaseStats50/65/107/86/105/107 vsGen5forms nooverride; Electric+Fire/Water/Ice/Flying/Grass, eachPokedextext. onSetFormsignatureMove substitution doesnotreset fullinheritedMoveList automatically.',
'GIRATINA':'Origin1LEVITATE naturalhidden,150/120/100/90/120/100,completeTutorsinclCONFIDE,H69/W6500tenths/Serpentine; GriseousOrb/distortionhandler separate.',
'SHAYMIN':'Sky1GRASSFLYING100/103/75/127/120/75 SPEED3 SERENEGRACE H4/W52;fulllevel/Tutor listincludingDAZZLINGGLEAM/NATUREPOWER, baseGender/Happiness unknownuntilbase read.',
'ARCEUS':'18forms includingQMARKS9 andFAIRY18Generation6; explicit17otherTypes exact1..8,10..18. Dragon16Tutorlist additionallyDIVE/CONFIDE preservingallorder. DefaultgetForm source skips9 andhas18; no claimrawtype alone callsgetForm.',
'BASCULIN':'Blue1ROCKHEAD,ADAPTABILITY andonlyUncommonDEEPSEASCALE plusnewPokedex; allthreeiteminheritance suppressed,common/rareemptyown defaults.',
'DARMANITAN':'Zen1FIREPSYCHIC105/30/105/55/140/105 SPATK2Blue plusnewPokedex; actualHP/ability/lifecycle handlergates separate.',
'DEERLING':'Summer1Green/Autumn2Red/Winter3Brown nowexplicitcolors vsG5onlylabels; runtime season liveclock notPBS-driven.',
'SAWSBUCK':'Summer1/Autumn2/Winter3 labels only, noexplicitcolors; sourcecopyDeerlinghandler notrawfieldcopy.',
'TORNADUS':'Therian1REGENERATORbothslots79/100/80/121/110/90 SPEED3H14Winged.',
'THUNDURUS':'Therian1VOLTABSORBbothslots79/105/70/101/145/80 SPATK3H30BipedalTail.',
'LANDORUS':'Therian1INTIMIDATEbothslots89/145/90/91/105/80 ATK3H13Quadruped.',
'KYUREM':'White1/TurboBlaze/SPATK3 andBlack2/Teravolt/ATK3namedPokedex;forms3/4unnamedPokedexredirect1/2 carrysamecorrespondingstats/Moves/H. DuplicateIMPRISON8/64 rawbeforelast-occurrenceMove algorithm;fusionmode/worldendconsumer source separate.',
'KELDEO':'Resolute1label+newPokedex; SECRETSWORDgetFormcondition external todata.',
'MELOETTA':'Pirouette1NORMALFIGHTING100/128/90/128/77/77 ATK1DEF1SPEED1; RelicSong battlecaller independent.',
'GENESECT':'1Shock/2Burn/3Chill/4Douse labels only noexplicitTypes; Driveformsource retainscurrentbugsteelbase unlessbase saysotherwise.',
'VIVILLON':'19namedpatterns1Continental2Elegant3Garden4HighPlains5IcySnow6Jungle7Marine8Meadow9Modern10Monsoon11Ocean12Polar13River14Sandstorm15Savanna16Sun17Tundra18Fancy19PokeBall; labelorder doesnotproveallwildcreationdraws; separateScatterbughandler/copytargets actualwhole.',
'FLABEBE':'Yellow1/Orange2/Blue3/White4 only, baseRed0 notauthoredhere; missingFields inheritedbycompiler nothardcodedcolor logic.',
'FLOETTE':'Fourflowerlabels1..4 plusEternal5:74/65/67/92/125/128,BaseExp243,fullMoves inclLIGHTOFRUIN50,EggGroupsUndiscovered,FLORGESNone. RegisteredNonefamily!=evolvingtarget, directEggGeneratorability bypassdoesnotmakeordinaryDayCarecompatible.',
'FLORGES':'Yellow1/Orange2/Blue3/White4 labels only; family/evolutionforms explicitcompilerlookup preservingmissingbase valuesOPEN.',
'FURFROU':'NineHeart/Star/Diamond/Debutante/Matron/Dandy/LaReine/Kabuki/Pharaoh labels; timedgetForm andonSetForm starttime sideeffects are actualsource, labels do notwriteclock.',
'MEOWSTIC':'Female1 COMPETITIVEhiddenonly,allcompletelevelMoves withSTOREDPOWER1and53 preserved;White color, naturalAbilities inheritedbase, no forcedgenderfield inrecord.',
'AEGISLASH':'Blade1 BaseStats60/150/50/60/150/50 EVATK2SPATK1. ThisGen6variant sourcevalues are notreplacedbycurrentgenerationnumbers; STANCECHANGEhandler actualability gate separate.',
'PUMPKABOO':'Average1 HP49/SPEED51 H4W50hiddenINSOMNIA;Large2HP54/SPEED46 H5W75 nohiddenoverride;Super3HP59/SPEED41 H8W150hiddenINSOMNIA andallthreeWildMIRACLESEED. Otherstats66/70/44/55;explicitabsence vsinheritance preserved.',
'GOURGEIST':'Average1 HP65/ATK90/SPEED84 H9W125hiddenINSOMNIA;Large2HP75ATK95SPEED69 H11W140;Super3HP85ATK100SPEED54 H17W390hiddenINSOMNIA/allthreeMIRACLESEED. DEF122/SPATK58/SPDEF75 common; fullactualtuples retained.',
'XERNEAS':'Active1labelonly, startbattleform1/end0 sources independent.',
'HOOPA':'Unbound1PSYCHICDARK80/160/60/80/170/130 H65W4900BipedalTail;complete orderedlevelMoves haspaired29Power/GuardSplit and50Wonder/TrickRoom plusHyperSpaceFury1/85; onSetForm oneMove replacement/timeditem refresh ordering distinctfromresetMoves.'}
fieldflow={
'FormName':'Own-form optional text defaultnil; localizedformlabel/Dexstructuralfilter/MegaName channel, not inheritedbase label.',
'Pokedex':'Text preprocess/localization and selectedEntrydisplay; missingform inheritsbase, explicit textstoredasgiven.',
'Generation':'Signedinteger metadata; no automaticgenerationmechanicchange from thisvalue.',
'Color':'StrictBodyColor enum→selected lastseenform search/display; not spritepixel assertion.',
'Shape':'StrictBodyShape enum→Dexshape/search/icon; not Pokemonability/geometry.',
'Types':'OrderedType enums→Pokemon(simple)copiedlist/Battlerinitialtypes; compileruniqs; noinstantcombatcallback.',
'BaseStats':'Six positivePBS columns HP/ATTACK/DEFENSE/SPEED/SPECIAL_ATTACK/SPECIAL_DEFENSE→calc_stats currentform selecteddata.',
'EVs':'RepeatedStat+positiveyieldpairs→SpeciesEVhash/Battleawardreceiver; notindividualrawEValreadyassigned.',
'BaseExp':'PositivebaseEXP rewardfield→defeated-selectedspeciesrewardformula, notownexperience.',
'Abilities':'OrderednaturalAbility symbols→PIDindex/fallback/explicitoverride; sourcecache/indexgates independentfrommetadata.',
'HiddenAbilities':'OrderedhiddenAbility symbols offset2→hiddenindex/fallback; missinginheritsbaseouterarray, notsameasnaturaloverride.',
'Moves':'Orderedunsignedlevel/Move pairs→defaultlastduplicate/final4 andlevel/evolutionlearning channels; duplicatelevels allowed.',
'TutorMoves':'OrderedstrictMove references→compatible_with_move?; declaredlist doesnotgrantallcombatfunction bodies.',
'Height':'Decimalmetres convertedround(10x),min1→Pokemon.height/Dexnumericdisplay/sizeformula.',
'Weight':'Decimalkg convertedround(10x),min1→Pokemon.weight/Dexsort/Battlerweightmodifiers.',
'WildItemCommon':'StrictItem arrayrarityCommon→wildselection; anyofthreepresent suppressesalltriplebaseinheritance.',
'WildItemUncommon':'StrictItem arrayrarityUncommon→wildselection; anyofthreepresent suppressesalltriplebaseinheritance.',
'WildItemRare':'StrictItem arrayrarityRare→wildselection; anyofthreepresent suppressesalltriplebaseinheritance.',
'Evolution':'Singularcaret orderedtriples strictmethod/typedparameter, pluralparsedbefore;Noneisregisteredfamilylinknotruntimeforwardtarget.',
'EggGroups':'StrictEggGroup array→compatibilityequality/Undiscoveredfirst/Dittogates; directgeneratornotrepeatcompatibility.',
'PokedexForm':'Ownunsigneddisplayformredirect, absentdefaultsownform; notactualstoredformoverwrite.',
'MegaStone':'StrictItem requirement matchedORknownMegaMove,sourceiterationfirsttarget; no ItemMegaStoneflag/anyheldexclusion requirement.',
'MegaMove':'StrictMove requirementknown independentofPP; OR matchingstone; no unrelatedheldMegaStone rejection.',
'MegaMessage':'Unsignedmessage selector,notformcommit; Rayquaza1field selectsmessage1notnamehardcode.'}
records=[]
for z,(lo,h) in enumerate(headers):
 hi=headers[z+1][0]-1 if z+1<len(headers) else len(ls);body=ls[lo-1:hi];fields=[];values={}
 for no,l in enumerate(body,lo):
  if not l.strip() or l.startswith(('#','[')):continue
  k,v=l.split('=',1);k=k.strip();v=v.strip();assert k in fieldflow,k;fields.append(dict(line=no,key=k,raw_value=v,manual_field_consumer_meaning=fieldflow[k]));values[k]=v
 species,form=h.split(',');mega='MegaStone' in values or 'MegaMove' in values;assert mega or species in manual,species
 semantic=dict(species=species,form=int(form),selected_explicit_values=values,own_missing_defaults=dict(FormName=None,PokedexForm=int(form),MegaStone=None,MegaMove=None,UnmegaForm=0,MegaMessage=0),missing_ordinary_fields='Conditionalinherit selectedGen6base; exactbase effectivevalues OPEN unless separatelywhole selectedread. Anythreewilditempresent suppressestripleinheritance.')
 if 'BaseStats' in values:semantic['explicit_six_stats']=dict(zip(['HP','ATTACK','DEFENSE','SPEED','SPECIAL_ATTACK','SPECIAL_DEFENSE'],map(int,values['BaseStats'].split(','))))
 for k in ['Height','Weight']:
  if k in values:semantic[k+'_stored_tenths']=max(1,int((Decimal(values[k])*10).quantize(Decimal('1'),rounding=ROUND_HALF_UP)))
 if mega:
  meaning='Gen6Mega variant '+h+': required '+('stone '+values['MegaStone'] if 'MegaStone' in values else 'knownMove '+values['MegaMove'])+'; ownUnmega0/MegaMessage'+values.get('MegaMessage','0')+'; exactBaseStats '+values.get('BaseStats','(inherit)')+'; selected natural '+values.get('Abilities','(inherit Gen6base)')+' /hidden '+values.get('HiddenAbilities','(inherit Gen6base)')+'. CorrectindividualOR only, no ring/quota/menu or forcedform unlock guarantee.'
 else:meaning=manual[species]
 delta=[]
 if h in old:
  ov={x['key']:x['raw_value'] for x in old[h]['all_ordered_explicit_fields']}
  for k in dict.fromkeys(list(ov)+list(values)):
   if ov.get(k)!=values.get(k):delta.append(dict(key=k,Gen5_explicit=ov.get(k),Gen6_explicit=values.get(k),meaning='Postreading exactliteralchange only; missingfield inherits/owndefaults accordingtocontract, notzero or automaticallyequivalent.'))
 records.append(dict(id=f'G6F-REC-{z+1:03}',section=h,range=[lo,hi],complete_raw='\n'.join(body),all_ordered_explicit_fields=fields,semantic_projection=semantic,manual_species_meaning=meaning,Gen5_corresponding_complete_record_id=old[h]['id'] if h in old else None,complete_literal_field_deltas_from_Gen5=delta,actual_reader='/root/creature_a_atomic_reception',all_fields_actually_read=True,whole_domain_acceptance=False))
megas=[x for x in records if 'MegaStone'in x['semantic_projection']['selected_explicit_values']or'MegaMove'in x['semantic_projection']['selected_explicit_values']];assert len(megas)==48;assert next(x for x in records if x['section']=='SLOWBRO,1');assert len(ls)==1123
out=dict(schema='gr8-crec-gen6-forms-complete-raw-meaning/v1',recorded_utc=utc,actual_reader='/root/creature_a_atomic_reception',source_identity=dict(path=p,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),blob=subprocess.check_output(['git','-C',str(R),'rev-parse',fixed+':'+p],text=True).strip(),lines=1123,commit=fixed,tree='7589c800b61ba13a13040ed0d686979b80a84fd0'),actual_complete_read_IO=['b827d3 full1–400','36a414 full401–800','594552 full801–1123'],complete_records=records,complete_record_count=len(records),all_explicit_field_count=sum(len(x['all_ordered_explicit_fields'])for x in records),manual_field_definition_contracts=fieldflow,nonmega_species_manual_meaning_groups=manual,Mega48_actual_meaning='All48actualGen6record fields read, notborrowedcurrentdefault48.47stone/1knownmove;Slowbroform1 notcurrentform2;MetagrossHP95 preserved butcorrespondingGen6baseHPnotassumedfromdefaultbase. No UnmegaFormauthored soowndefault0;PrimalKyogre/Groudon noMegaMetadata andseparatehandlers.',common_premises=['Backupinactive underordinarytop-level discovery; explicitpath/variant load separate.','Own Species/Compiler/Pokemon/FormHandlers definitions alreadyactualwhole, no code/game/compilerexecuted.','Gen6basewholePBS stillnotread, exactmissingfields onlyconcretewhenparticularbasefullyread; no allalternativeclosure.','Allmetadatareferences aretypedidentities, not allMove/Ability/Item/body execution ortransitiveapproval.'],mandatory_companions=['pbs-field-contracts-mandatory-mega-reception.v1.json','pbs-field-contracts-mandatory-encounter-reception.v1.json'],normal_failure_prefix='Formmuststrictpositive andbaseexist; referencedenumconversion/inheritance/finalreversevalidation precedecompletedtable/save, intermediateclear/registeredprefixnotrollback. Livearchive/cache/modelrefresh nativeunexecuted.',new_full_raw_files=1,new_primary_atoms=0,whole_domain_acceptance=False,denominator_frozen=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');o=C/'gen6-forms-complete-meaning.v1.json';assert not o.exists();o.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(dict(path=o.name,bytes=o.stat().st_size,sha256=hashlib.sha256(o.read_bytes()).hexdigest(),records=len(records),fields=out['all_explicit_field_count'],mega48=len(megas),utc=utc)))
