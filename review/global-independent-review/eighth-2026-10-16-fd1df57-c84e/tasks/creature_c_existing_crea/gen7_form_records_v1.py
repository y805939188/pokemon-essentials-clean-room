from pathlib import Path
import json,re,hashlib,datetime,subprocess
from decimal import Decimal,ROUND_HALF_UP
C=Path(__file__).parent
R=Path('/workspace/pokemon-essentials')
source_path='PBS/Gen 7 backup/pokemon_forms.txt'
raw=(R/source_path).read_bytes()
lines=raw.decode('utf-8-sig').splitlines()
fixed='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b'
assert raw==subprocess.check_output(['git','-C',str(R),'show',fixed+':'+source_path])
utc=datetime.datetime.now(datetime.timezone.utc).isoformat()
prior=json.loads((C/'gen6-forms-complete-meaning.v1.json').read_text())
prior_records={x['section']:x for x in prior['complete_records']}
flows=dict(prior['manual_field_definition_contracts'])
flows.update(EggMoves='Ordered knownMove array→specific species EggGenerator currentrawEggMoves versus Species.get_egg_moves fallback; female/Ditto/machine channels andcompatibility gates separate.',Flags='Arbitrary text tokens case-insensitive species.has_flag?; InheritFormWithEverstone/InheritFormFromMother qualify exact DayCare branches, noautomaticbreed/formcommit from mereflag.')
manual={
'RATTATA':'Alolan1 DARK/NORMAL,GLUTTONY/HUSTLE naturalTHICKFAThidden,Weight38,Black,Everstoneflag,onlyUncommonPECHABERRY andRATICATE LevelNight20. No ownBaseStats/Moves means inherit selectedGen7base; explicitTutor/Egglists replace base. Sourcecreationcopy selectsregion, actualnight predicate live; raritytripleinheritance suppressed.',
'RATICATE':'Alolan1 DARK/NORMAL75/71/70/77/40/80,GLUTTONY/HUSTLE THICKFAT,W255Black,Everstoneflag,onlyUncommonPECHA;actualfullTutorlist notfullMoveclassdict.',
'RAICHU':'Alolan1 ELECTRIC/PSYCHIC60/85/50/110/95/85SURGESURFERbothslots,H7W210Brown;explicit0PSYCHIC then1SPEEDSWAP/THUNDERSHOCK/TAILWHIP/QUICKATTACK/THUNDERBOLT. Noheritageflag inthisform; sourcePikachuonEvolution region separate.',
'SANDSHREW':'AlolanICE/STEEL50/75/90/40/10/35SNOWCLOAK/SLUSHRUSH H7W400White,Everstoneflag,ICESTONE→Sandslash;completeMoves/Tutors/Eggmoves notinherited.',
'SANDSLASH':'AlolanICE/STEEL75/100/120/65/25/65SNOWCLOAK/SLUSHRUSH H12W550Blue,Everstoneflag;0IcicleSpear precedeslevel1list.',
'VULPIX':'AlolanICE,SNOWCLOAK/SNOWWARNING,White,Everstone,onlyUncommonSNOWBALL andICESTONE→Ninetales; noownBaseStats/H/W defaults fromselectedbase;fulllevel/Tutor/Egg order retained.',
'NINETALES':'AlolanICE/FAIRY73/67/75/109/81/100 SPEED2 SNOWCLOAK/SNOWWARNING Blue/FlagEverstone/UncommonSnowball,0DazzlingGleam+1list; noarea/towergate fromlabel.',
'DIGLETT':'AlolanGROUND/STEEL10/55/30/90/35/45SANDVEIL/TANGLINGHAIR,W10Everstone;hiddenability absent inherits selectedbase, doesnotcopysecondnatural automatically; fullownmoves/tutor/egg.',
'DUGTRIO':'AlolanGROUND/STEEL35/100/60/110/50/70ATK2SANDVEIL/TANGLINGHAIR W666Everstone,0SandTomb1Rototiller/NightSlash/TriAttack…ordered; hiddenbaseinheritance.',
'MEOWTH':'AlolanDARK40/35/35/90/50/40 hiddenRATTLED,BlueEverstone,Happiness→Persian, naturalabsentinheritGen7base; allthreeownmovechannels exact.',
'PERSIAN':'AlolanDARK65/60/60/115/75/65FURCOAT/TECHNICIAN hiddenRATTLED,H11W330BlueEverstone,0Swift then1/6/…exactlist; sourceevolutionfromMeowth readsselecteddata.',
'GEODUDE':'AlolanROCK/ELECTRIC MAGNETPULL/STURDY hiddenGALVANIZE W203GrayEverstone onlyUncommonCELLBATTERY;noownBaseStats→Gen7base; alllevel/Tutor/Egglists explicit.',
'GRAVELER':'AlolanROCK/ELECTRIC MAGNETPULL/STURDY GALVANIZE W1100GrayEverstone UncommonCellBattery; ownmoves/Tutors vsinheritedEgglist separate, baseEvolutionnotreadhere.',
'GOLEM':'AlolanROCK/ELECTRIC MAGNETPULL/STURDY GALVANIZE H17W3160GrayEverstone onlyCommonCELLBATTERY; onlycommonpresent disablesuncommon/rarebaseinheritance. CompleteMoves0none1HeavySlam…60HeavySlam retainduplicates.',
'GRIMER':'AlolanPOISON/DARK POISONTOUCH/GLUTTONY POWEROFALCHEMY H7W420GreenEverstone; ownMoves/Tutors/Eggcomplete, nostat6override baseunknown.',
'MUK':'AlolanPOISON/DARK POISONTOUCH/GLUTTONY POWEROFALCHEMY H10W520GreenEverstone;0VenomDrench andcompleteordinarylist, ownTutor butnoEggMovesoverride.',
'EXEGGUTOR':'AlolanGRASS/DRAGON95/105/85/45/125/75 FRISK H109W4156;0DragonHammer andcompleteTutors;noEverstoneflag here, sourceExeggcutevolutionregion stillindependent.',
'CUBONE':'Form1unnamedGeneration7 withMAROWAK LevelNight28 only. ItusesownPokedexForm1/nilFormName defaults, otherwisebaseinheritance; artificialpre-evolutionform runtimeonEvolution rule inspectedseparately.',
'MAROWAK':'AlolanFIRE/GHOST CURSEDBODY/LIGHTNINGROD ROCKHEAD W340Purple;completeMoves/Tutors butnostat6override/NoEverstoneflaghere. 0notauthored inMoves;sourceCuboneonEvolution usesmapregion independent.',
'GRENINJA':'1unnamedBATTLEBONDnaturalhidden/EggGroupsUndiscovered;2Ashnamed72/145/67/132/153/71 BaseExp288/BattleBondbothslots/Generation7, noexplicitEggGroups2 thusbaseinheritance ratherthanautomaticcopyform1. SourceBattleBondguard blocksordinaryevo andbattlechangingseparate.',
'ZYGARDE':'10%1stats54/100/71/115/61/85 Exp219H12W335BlackQuadruped;Complete2stats216/100/121/85/91/95 Exp319POWERCONSTRUCTboth H45W6100BlackBipedalTail;3unnamedPokedex2samecompletefields. Handler2→0/3→1 arithmetic andHPcalc separate, no rawform aliases.',
'ORICORIO':'1PomPomELECTRICFLYINGYellow/2PauPSYCHICFLYINGPink/3SensuGHOSTFLYINGPurple withownPokedex;otherstats/moves inheritselectedbase. Nectaritemcaller notencoded bylabel.',
'ROCKRUFF':'OwnTempoform2unnamed bothabilityslotsOWNTEMPO,InheritFormFromMother,LYCANROC LevelEvening25. No numericgenerationgate oranylevelcondition beyondactualevo proc/caller.',
'LYCANROC':'Midnight1stats85/115/75/82/55/75 KEENEYE/VITALSPIRIT NOGUARD H11RedBipedalTail,0Counter andownMoves/Tutors. Dusk2stats75/117/65/110/55/65TOUGHCLAWSboth,0Thrash with1AccelRock/Counter… andmotherflag;currentformhandler onEvolution mapping independent.',
'WISHIWASHI':'School1stats45/140/130/30/140/135 Exp217H82W786MultiBodyPokedex;SCHOOLING>=20/HPthresholdbattlehandlerdeterminestransition, notmetadataauto.',
'SILVALLY':'18typeforms1..18inclQMARKS9andFAIRY18;Dragon16owncompleteTutorlist. ActualRKSSYSTEMfirst/Memorydispatch skips9, dataType/labels do notwritehelditem/type automatically.',
'MINIOR':'SevenCoreforms7..13allstats60/100/60/120/100/60 Exp175 EVATK1SPATK1 W3 andmotherflag;Red7/Orange8 bothColorRed,Yellow9,Green10,Blue11+Indigo12ColorBlue,Violet13Purple. Noauthoredshell1..6rows inthisfile;currentgetForm creation/enter/leave/endmod7callbacks mustnotbeconflatedwithrawabsence.',
'MIMIKYU':'Busted1namedPokedexonly; noHP/stat/type override. ActualDisguisesavedHP/eventcallbacks separate.',
'NECROZMA':'DuskMane1PSYCHICSTEEL97/157/127/77/113/109Exp306ATK3H38W4600YellowQuadruped;Dawn2PSYCHICGHOST97/113/109/77/157/127Exp306SPATK3H42W3500Blue. Ultra3PSYCHICDRAGON97/167/97/129/167/97Exp339ATK1SPATK1SPEED1NEUROFORCE H75Yellow,4unnamedPokedex3samefields. NoMegaStone/MoveMetadata supplied: these areformdata+separatehandlers, notindividualMega target.',
'MAGEARNA':'OriginalColor1RedwithPokedex only;baseTypes/stats/abilityinheritanceunknownunlesscorrespondingGen7base read.',
'KYUREM':'Gen7White1/3andBlack2/4Moves replacelevel64IMPRISONwithNOBLEROAR, remainingfulltuple/type/ability/H asliteralrecord;BaseExp315explicit,1/2namedPokedex3/4unnamedredirect1/2. Fusedfield/onSetForm callbacks areseparatesourcewriters.',
'WORMADAM':'Gen7Sandy/TrashfullMovesadd0QUIVERDANCE,1SUCKERPUNCH/TrashMETALBURST and50BUGBUZZ,rawtiedlevels/order retained;completeTutors additionallyAllySwitch/Telekinesis. Stat6/Types/EV/Colororiginaltuples exactinrecord.',
'FLOETTE':'Eternal5same74/65/67/92/125/128 Exp243Undiscovered/None→Florges butnow1FAIRYWIND plus6FAIRYWIND;defaulteligiblemovesdedupbylasteligibleoccurrence,notacrossunreachedlevels. Fourflowerformsonlylabels.',
'MEOWSTIC':'Female1COMPETITIVEhidden,White,owncompleteMovesnowextra1COVET/1CONFUSION before5/9duplicates; PPnewmove/defaultreset/learnexistingobject channels remainseparate.',
'DARMANITAN':'Gen7Zen1FIREPSYCHIC105/30/105/55/140/105 Exp189 SPATK2Blue;ownPokedex, no abilityoverrideinheritGen7base.',
'ROTOM':'AllfiveGen7appliance explicitstats50/65/107/86/105/107 Exp182 plusElectric/secondary type,Pokedex;notGen5baseinheritedstats. SignatureonSetFormrule independentofrawfulllearnsetinheritance.'}
# Existing Gen6 family branches remain useful source-flow context. New Gen7 literals
# and all exact deltas below are authoritative for this file, never the old values.
headers=[(i,re.fullmatch(r'\[([^]]+)\]',line).group(1)) for i,line in enumerate(lines,1) if re.fullmatch(r'\[([^]]+)\]',line)]
assert len(headers)==250
records=[]
for ordinal,(lo,header) in enumerate(headers,1):
 hi=headers[ordinal][0]-1 if ordinal<len(headers) else len(lines)
 body=lines[lo-1:hi]
 fields=[]
 values={}
 for line_no,line in enumerate(body,lo):
  if not line.strip() or line.startswith(('#','[')):
   continue
  key,value=line.split('=',1)
  key=key.strip();value=value.strip()
  assert key in flows,key
  fields.append(dict(line=line_no,key=key,raw_value=value,manual_consumer_meaning=flows[key]))
  values[key]=value
 species,form_text=header.split(',')
 form=int(form_text)
 is_mega='MegaStone' in values or 'MegaMove' in values
 if is_mega:
  meaning=f"Gen7{header}: exactcandidate requirement "+('held '+values['MegaStone'] if 'MegaStone' in values else 'known '+values['MegaMove'])+f"; own Unmega0 and MegaMessage{values.get('MegaMessage','0')}; exactstats {values.get('BaseStats','inherit')}; BaseExp{values.get('BaseExp','inherit')}; natural{values.get('Abilities','inheritGen7base')}/hidden{values.get('HiddenAbilities','inheritGen7base')}. OR no unrelatedheldstone exclusion; battlepermission separate."
 else:
  meaning=manual.get(species,'Gen7 wholeexplicitrecord fields andsourceflow: '+prior['nonmega_species_manual_meaning_groups'].get(species,''))
  assert meaning.strip() and (species in manual or species in prior['nonmega_species_manual_meaning_groups']),species
 projection=dict(species=species,form=form,explicit_values=values,own_missing_defaults=dict(FormName=None,PokedexForm=form,MegaStone=None,MegaMove=None,UnmegaForm=0,MegaMessage=0),missing_ordinary_fields='SelectedGen7baseconditionalinheritance, exactconcretebasevalueOPENuntilactualbase read. Anywildraritypresent preventsalltripleinheritance.')
 if 'BaseStats' in values:
  projection['six_stats']=dict(zip(['HP','ATTACK','DEFENSE','SPEED','SPECIAL_ATTACK','SPECIAL_DEFENSE'],map(int,values['BaseStats'].split(','))))
 for key in ['Height','Weight']:
  if key in values:
   projection[key+'_tenths']=max(1,int((Decimal(values[key])*10).quantize(Decimal('1'),rounding=ROUND_HALF_UP)))
 deltas=[]
 if header in prior_records:
  old_values=prior_records[header]['semantic_projection']['selected_explicit_values']
  for key in dict.fromkeys(list(old_values)+list(values)):
   if old_values.get(key)!=values.get(key):
    deltas.append(dict(key=key,Gen6_explicit=old_values.get(key),Gen7_explicit=values.get(key),meaning='Bothrawsactuallyread; exactdeltaofexplicitfield, absence not0/concreteeffectiveinheritance.'))
 records.append(dict(id=f'G7F-REC-{ordinal:03}',section=header,range=[lo,hi],complete_raw='\n'.join(body),all_ordered_explicit_fields=fields,semantic_projection=projection,manual_specific_meaning=meaning,Gen6_corresponding_record=prior_records[header]['id'] if header in prior_records else None,all_literal_Gen6_Gen7_deltas=deltas,actual_reader='/root/creature_a_atomic_reception',all_raw_fields_actually_read=True,whole_domain_acceptance=False))
mega_records=[x for x in records if 'MegaStone' in x['semantic_projection']['explicit_values'] or 'MegaMove' in x['semantic_projection']['explicit_values']]
assert len(mega_records)==48 and len(lines)==1745
out=dict(schema='gr8-crec-gen7-forms-complete-raw-meaning/v1',recorded_utc=utc,actual_reader='/root/creature_a_atomic_reception',source_identity=dict(path=source_path,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),blob=subprocess.check_output(['git','-C',str(R),'rev-parse',fixed+':'+source_path],text=True).strip(),lines=1745,commit=fixed,tree='7589c800b61ba13a13040ed0d686979b80a84fd0'),actual_complete_read_IO=['a2da99 1–175','435397 176–350','80ca0b 351–700','c2a325 701–875','6a2687 876–1050','f0d57d1051–1225','19bd491226–1400','946c741401–1575','28aa771576–1745'],truncated_attempts_no_FULL_credit=['c239c7 mixed1–350','9f7fb9 mixed701–1050'],complete_records=records,complete_record_count=250,all_explicit_field_count=sum(len(x['all_ordered_explicit_fields']) for x in records),manual_species_specific_meanings=manual,complete_field_definition_contracts=flows,common_premises=['Everyoriginalrawfield actuallyread andartifactnotparser-successcredit.','Backupinactive bydefaulttop-leveldiscovery;explicitselectedvariant knownregistries/earliernormalcompile required.','Gen7base whole rawunread; no239? inventedglobalcount or concreteinheritance fromgenericrule.','Own whole Species/Pokemon/Compiler/FormHandlers sourcecredit separate; metadataIDs no blanketMove/Ability/Itemhandleracceptance.','PreviousGen6familycontext references are sourceflowonly; Gen7 exactexplicitvalues/deltas authoritative.'],manual_particular_controls=['MegaAlakazamSpDef105 here vsGen6 95;MegaSlowbrostill1;all48Expdefaultfields actualvalues retained.','RattataNight20/MeowthHappiness/SandshrewVulpixIceStone/CuboneNight28/RockruffEvening25 exactparameters no officialreplacement.','Greninja1Undiscovered cannotassumeGreninja2inheritsform1; it inheritsbase accordingtoselectedcompiledflow.','MiniorOrangeColorRed/IndigoColorBlue retainliteraldata;noauthoredshell1..6rows readingdoesnotinventregistration.','Zygarde3/Pokedex2 andNecrozma4/Pokedex3 unnameddata distinctfromordinaryformgetter/dexvisibility.'],mandatory_companions=['pbs-field-contracts-mandatory-mega-reception.v1.json','pbs-field-contracts-mandatory-encounter-reception.v1.json'],normal_failure_prefix='Strictformbase/positiveindex/enumvalidation/conditionalinheritance→register/finalreverse/save in actualcompiler order; earlierclear/registrationprefix notatomicrollback. ModelgetForm readcancommit beforelaterdisplay failure;actualtarget/nativeexecutionNOT_EXECUTED.',new_full_raw_files=1,new_primary_atoms=0,whole_domain_acceptance=False,denominator_frozen=False,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED')
p=C/'gen7-forms-complete-meaning.v1.json'
assert not p.exists()
p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(path=p.name,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),records=250,fields=out['all_explicit_field_count'],mega48=len(mega_records),utc=utc)))
