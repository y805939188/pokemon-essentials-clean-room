import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_09g.json').read_text());d=base['source_dictionary'];rows=[]
def src(path,ran,reading='FULL_FILE_READ'):
 return dict(path=path,range=ran,actual_reader='/root/core_atomic_reception',reading=reading)
d['activefield_full']=src('Data/Scripts/011_Battle/007_Other battle code/002_Battle_ActiveField.rb',[1,88])
d['battleweather_full']=src('Data/Scripts/010_Data/001_Hardcoded data/015_BattleWeather.rb',[1,81])
d['battleterrain_full']=src('Data/Scripts/010_Data/001_Hardcoded data/016_BattleTerrain.rb',[1,58])
d['worldweather_full']=src('Data/Scripts/010_Data/001_Hardcoded data/012_Weather.rb',[1,165])
d['weather_core_complete']=src('Data/Scripts/011_Battle/001_Battle/001_Battle.rb',[694,811])
d['weather_move_parent']=src('Data/Scripts/011_Battle/003_Move/004_Move_BaseEffects.rb',[496,525],'PARTIAL_FILE_COMPLETE_CLASS_READ withall3methods/end; notwholeBaseEffects')
d['weather_terrain_moves']={'path':'Data/Scripts/011_Battle/003_Move/005_MoveEffects_Misc.rb','complete_units':[[231,236],[241,246],[251,256],[261,266],[273,285],[292,304],[311,323],[330,342],[348,370]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE all9completeclasses actuallyread; notwholeMisc/Movefamilycredit'}
d['rain_accuracy_classes']={'path':'Data/Scripts/011_Battle/003_Move/007_MoveEffects_BattlerOther.rb','complete_units':[[183,195],[618,630]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE bothcompleteThunder/Hurricaneclasses actuallyread; accuracyoverridebounded, inheritedstatusfamilyseparate'}
d['map_weather_raw']={'path':'PBS/map_metadata.txt','complete_records':[[96,103],[372,379]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE two complete rawrecords021/072; no compiled/native/fullmetadata credit'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
def layout(n,why):rows.append(dict(number=n,layout_reason=why))
layout(674,'Classification/implementation-independent contract scope; notsourcebehavior orfutureclasslayoutrequirement.')
layout(675,'Provenance/traceability, data-identity naming and staticNOT_EXECUTED qualification; doesnotcertifyallcallbacks/resource/nativeexecution.')
layout(676,'Purpose enumerates establishment/suppression/countdowns/ownership questions. Actual answers are decomposed at following clauses, not inheritedfromthisheading.')
row(677,[
 'Directoryscope includesdefaultinputs/weather-terrainestablishment/effectivequeries; specificrulesareseparatefollowingatoms.',
 'Lifecycle distinguishes temporaryoverride, suppression, naturalexpiry anddirectremoval; onegenericclearoperationcannotstandforall.',
 'ActiveField has13namednonweather/terrain effectrecords, ActiveSide22 andActivePosition9; six weather/terrain default/current/durationfields areseparate.',
 'The44record countdenotes boundedreferenceeffectscope, notproofall44effectproducer/consumerfamiliesreceived.',
 'Entryhazard/sideswap/barrierremoval/positionhealing-delayedattack areactualconsumerresponsibilities; localcounter/compute/status joins requiretheirparticularmethods.'
],['activefield_full','weather_core_complete','eor_all'],'domaincatalog→laterindividualwriter/reader/lifetimeatoms; scope count notglobalfamilyPASS.',open=['RemainingWP45specific44records/entryhazards/side-swap/positionreceiveractualchains must be independentlydecomposed afterC710; thisscopeparagraphnotcompletion.'])
layout(678,'Explicitboundedresponsibility/non-target/pointer statement: futurearrays/classes/IDs notrequired; membertemporarytypesownedbyotherWP; moneysettlementWP42; noentireWP42/46–50/AIPASS follows. Preservedeclaredscopewithoutturningitintocallbackacceptance.')
row(679,[
 'BattleweatheridentityNone isregistereddefaultno-weather.',
 'BattleweatherSun isregisteredordinarysun.',
 'BattleweatherRain isregisteredordinaryrain.',
 'BattleweatherSandstorm isregisteredsandstorm.',
 'BattleweatherHail isregisteredhail.',
 'BattleweatherHarshSun isregisteredprimordialsun.',
 'BattleweatherHeavyRain isregisteredprimordialrain.',
 'BattleweatherStrongWinds isregisteredprimordialwind.',
 'BattleweatherShadowSky isregisteredshadowweather; total9includingNone.',
 'BattleterrainNone isregisteredno-terrain.',
 'BattleterrainElectric isregistered.',
 'BattleterrainGrassy isregistered.',
 'BattleterrainMisty isregistered.',
 'BattleterrainPsychic isregistered; total5includingNone.',
 'WorldGameDataWeather IDs/categories feedpreparation; theyarenotidenticaltoBattleWeatherregistry.',
 'World/mapterrainlabels andBattleenvironment areseparateinputfromBattleterrain enum; prepareassignseparatebattle.environment/defaultTerrain.'
],['battleweather_full','battleterrain_full','worldweather_full','prepare'],'registeredidentityrecords→Battlefieldstate/query/animationmetadata; ownhardcodedFULLnotallPBS/runtimeavailability.')
row(680,[
 'FieldinitialdefaultWeatherNone.', 'FieldinitialcurrentWeatherNone.', 'FieldinitialweatherDuration0.',
 'FieldinitialdefaultTerrainNone.', 'FieldinitialcurrentTerrainNone.', 'FieldinitialterrainDuration0.',
 'defaultWeather= writesdefaultandcurrentidentical thenDuration−1.',
 'defaultTerrain= writesdefaultandcurrentidentical thenDuration−1.',
 'EOR weatherdecrementsdurationonlyif>0; EORterraindecrementsdurationonlyif>0.',
 'Duration−1 remainsundecrementedbyordinaryEORcounter; zeroallowsreachedexpirylogic, notnewpositivecount.',
 'Defaultsource isasinglefield; temporarycorestartoverwritescurrent/durationwithoutpushingpreviouscurrentontoaresumestack.',
 'Restorationchoosesdefaultsource anew with−1, notremainingdurationofprevious temporaryweather/terrain.'
],['activefield_full','weather_core_complete','eor_all'],'constructdefault/current0→defaultsetter−1 orcoretemporary5/extended8→localEORdecrement→defaultrestart; noelapsed-timeglobalclock.')
row(681,[
 'Globalfieldobject sharedbybothsides, effectsstoredonceperbattle.',
 'Sidesindexedbybattlerindexmod2; sideeffectnotmemberowned andordinaryreplacementdoesnotnewconstructActiveSide.',
 'Positioneffects stayin@positionsindexedbyinterleavedslot; battlerreplacement/residentchangesdonottransferpositionrecordwithPokemon.',
 'Pokemon/Battlerownstatus/effects followtheirexplicitinitialize/replace/reset rules; similarnameisnotproofpositionownership.'
],['activefield_full','battlefull','battlerfull','b_init','switching','other'],'constructionfield/sides/positions→battlerown/opposingside/position→replace/swapruntimeoccupants; fieldidentitynotPokemonidentity.',open=['SpecificWish/FutureSight/HealingWish/Shift detailedproducer-to-receiver clauses follow; thisboundedownershipmappingdoesnotapproveall44lifetimes.'])
row(682,[
 'prepare_battle consumescreationrulesandcurrentworldweatheratcreation, writingseparatebattleattributes.',
 'Core/Move/Ability/Item sourcesmayreadcurrentbattlerecords/membervalidity andcommittargetstate/duration.',
 'Effectivequery returnscanchangewithoutrewritingstoredweather, e.gCloudNine oractiveUmbrella.',
 'Reachedcallbacks canproduce messages/animation requests, HP/PP/status writes; absenceofanysinglemessage doesnotprovefieldorcacheunchanged.',
 'Do not substituteoneobservedoutputforcompleteinternalstate orforallcallbacksuccess.'
],['prepare','weather_core_complete','battlerfull','ability_item','use','eor_all'],'producers/world/membergates→differentquerylayers→field/memberwrites→conditionalpresentation; sideeffectsareorder-specific.')
row(683,[
 'Explicitnon-nildefaultTerrainrule winsworldderivation, includingexplicitNone.',
 'OtherwiseOVERWORLD_WEATHER_SETS_BATTLE_TERRAINmustbetrue; currentgen8defaulttrue.',
 'UnderthatgateexactworldweatherIDStorm yieldsElectricterrain.',
 'UnderthatgateexactworldweatherIDFog yieldsMistyterrain.',
 'OtherexactIDs do notestablishterrain throughthisbranch.',
 'Explicitnon-nildefaultWeatherrule winsworldcategoryderivation.',
 'Otherwise worldGameData::Weather.get(currentID).category Rain orStorm mapsBattleRain.',
 'WorldcategoryHail mapsBattleHail.',
 'WorldcategorySandstorm mapsBattleSandstorm.',
 'WorldcategorySun mapsBattleSun.',
 'Othercategories do notautomaticallysetweather throughthisbranch.',
 'DefaultStormrecord actuallyhascategoryRain; exact-IDterrainmappingandcategoryweathermappingmustnotbeconflated.'
],['prepare','rules','b_settings','worldweather_full','weather_core_complete'],'rulesnon-nilprecedence→worldIDStorm/Fogterrain ORWeather.get(ID).categoryforweather→defaultsetters; rawID/categorystaydistinct.',failure='Invalidworldlookup/datamissing mayfail beforelaterweather/environment/timepreparewrites; terrainmayalreadybeassigned. No atomicwholeprepare.')
row(684,[
 'Defaultsetters directlywritedefault/current/−1 withoutcallingnormalstartanimation/messages/callbackchain.',
 'Worldprepareconsumescreationmoment screenweather; setters/subsequentbattleoverrideswritetheBattlefield, nottheworldscreenweathervia thesemethods.',
 'Complete rawmetadata021recordcontainsWeatherRain,100.',
 'Complete rawmetadata072recordcontainsWeatherStorm,50.',
 'Theserawrecords proveauthorconfigurationtextonly; donotprovecompiledload, currentmap/weatheractivation,probabilitysample,or eventexecution.'
],['weather_core_complete','prepare','map_weather_raw'],'rawauthordata/staticworldinput→prepare→Battlefielddefault; noglobalweatherwritebythesebattlemethods.',open=['Compiledmetadata/currentGameMapactualweather event/native execution notadoptedfromtworawrecords.'])
layout(685,'Three-layer table heading only; actualstore/battle-effective/member-effective semantics separatelyauthored C686–688.')
row(686,[
 'field.weather rawcurrentvalue usedforcoreduplicateearlyreturn.',
 'WeatherMovefailurechecksrawcurrentprimal/sameweather, notsuppressedquery.',
 'Ordinaryweatherabilitywrapperrawcurrentprimal/same gates distinct.',
 'EORduration andcontinuingannouncement case readstoredweather; CloudNine doesnotbyitselfchangestoredvalue.'
],['weather_core_complete','weather_move_parent','eor_all'],'field.weather raw→start/refusal/EORduration/message; effectiveNonecannotbe substituted.')
row(687,[
 'pbWeather iteratesallBattlers nonnil/nonfainted andchecksactiveCLOUDNINE/AIRLOCK.',
 'Anyactiveone returnsNone; otherwise returnsfield.weather.',
 'Thisgetterdoesnotclearrawweather/default/duration.',
 'SuppressiondoesnotpreventweatherDurationpositiveEORdecrement orstoredcontinuingmessage.',
 'Thoseabilitychecksobeyactualfainted/GastroAcid/NeutralizingGasstate, notjustabilityname.'
],['weather_core_complete','battlefull','battlerfull','eor_all'],'allBattlers→hasActiveAbilityCloudNine/AirLock→effectiveNone; rawcounterstillruns.')
row(688,[
 'Battler.effectiveWeather firstgetsbattle.pbWeather.',
 'ActiveUTILITYUMBRELLA convertsSun toNoneforitsownmemberquery.',
 'SameactiveUmbrella convertsRain toNone.',
 'SameactiveUmbrella convertsHarshSun toNone.',
 'SameactiveUmbrella convertsHeavyRain toNone.',
 'Sandstorm/Hail/StrongWinds/ShadowSky arenotintheUmbrellafourweathermask.',
 'Inactiveitem cannotapplymask; nofield/globalqueryrewritefromthismembergetter.'
],['battlerfull','weather_core_complete'],'battleeffectivequery→ownactiveItemfourweathermask→memberreturn; distinctfrombattle-levelprimalmoveblock.')
row(689,[
 'abilityActive defaultrejectsfainted; ignore_faintedexplicittrueisanothernamedconsumerdomain.',
 'GastroAcidflagfalsegate andglobalactiveNeutralizingGasconditionalgateapplybeforeactiveabilitymatches.',
 'hasActiveAbility scalar/arrayidentitymatching followsactivitygate; storedabilityaloneisnotsufficient.',
 'itemActive rejectsfaintedwithoutignore,positiveEmbargo,positiveMagicRoom,perpartyslotCorrosiveGasandactiveKlutz.',
 'hasActiveItem scalar/arraymatchingfollowsitemActive; UmbrellacannotmaskunderMagicRoomorotheractualitemgates.',
 'DetailedAbilityfamilyqualification/producers remainWP48/49 responsibility; thisparagraphonlybindsexactquerygates,notallnegationlifecycles.'
],['battlerfull','ability_item','battlefull'],'memberstoredID+fainted/effect/globalgas→activity→scalar/arraymatch→weather/terrainconsumer.',open=['AllspecificGastroAcid/NeutralizingGas/CorrosiveGasetcproducerfamily and everyexternalmutation notapprovedmerelyfromgetterFULL; relevantfamilyreceptionsseparate.'])
row(690,[
 'Ordinarydamagemultipliersweather casequeriesuser.effectiveWeather.',
 'Thunderaccuracyoverridequeries target.effectiveWeather; sunfamily50/rainfamily0otherwiseinheritedbase.',
 'Hurricaneaccuracyoverride likewisequeriestargetweather sun50/rain0otherwisebase.',
 'Freezeprotection ordinarynewFROZENchecksrecipient.effectiveWeatherSun/HarshSun,notuserweather.',
 'PrimalFire/WatermoveblockinsidepbUseMove queriesBattle.pbWeather, onlydamagingmoves andcalculatedtypeFireinHeavyRain/WaterinHarshSun.',
 'UserUmbrelladoesnotmakethisBattle-levelprimalblockskip; suppressionatBattlelevelcan.',
 'Primalcontinuousmessage/animationabsence notproofprimalstorage/effectabsence; raw/effective/memberlayersseparate.'
],['calculations','rain_accuracy_classes','checksfull','use','battlerfull','weather_core_complete','eor_all'],'rawweather→battleeffectiveforprimaluseblock vsuserweatherdamage vsrecipientweatheraccuracy/freeze; chooseactualconsumer.',open=['InheritedThunderParalyze/HurricaneConfusefullfamilies notgrantedbyaccuracyoverrideclass; relevantstatusandmovebindings remainseparate.'])
layout(691,'Weatherentry table heading only; following four payload rows carry actualentry/guard/duration/notifying distinctions.')
row(692,[
 'FourordinaryweatherMove subclasses setSun/Rain/Sandstorm/Hailrespectively throughWeatherMovesuperconstructor.',
 'WeatherMove wholemovefailurechecksrawHarshSunandfailswithspecificmessage.',
 'LikewiserawHeavyRain fails.',
 'LikewiserawStrongWinds fails.',
 'Rawcurrent==ownweatherType fails ratherthanrefreshes.',
 'EffectiveweatherNonefromsuppressiondoesnotbypasstheserawchecks.',
 'PassedpbEffectGeneral invokespbStartWeather(user,weatherType,true,false):fixedbase5 andshowAnimsfalseforthiscorecall.',
 'Noextra genericweatheranimationfromthatcall; precedingordinarymoveanimation/messagingarenottherebycancelled.'
],['weather_move_parent','weather_terrain_moves','weather_core_complete','use'],'ordinarymovefrontgates→WeatherMovefailed?rawstorage→EffectGeneral→corefixed5/showAnimfalse; actualnormalusagePP/accuracyotherfrontsretained.')
row(693,[
 'pbStartWeather equalrawcurrent earlyreturnsbeforeduration/notification, so no refresh.',
 'Differentnewvalue writesfield.weatherfirst.',
 'fixedDurationtrue proposes5; false proposes−1.',
 'Onlypositiveproposal+nonniluser+itemActive invokeWeatherExtender; false/−1/noSource skip.',
 'Extenderdefaultreturnpreservesdurationwhenhandlerabsent/nil; matchedrockcanreturn8.',
 'WeatherDuration assignedafterextenderreturns, thenmetadataanimation conditionallyshowAnim anddata.',
 'CoredoesnotrepeatordinaryWeatherMoveprimal/same-typefailuremessages; rawprimaloverrideallowedifcallerreachescorewithdifferentnewvalue.',
 'Afterweatherwrite/duration/presentation, allBattlersweather-formchecks run thenEndPrimordial; failurecanretainnewvaluewitholdornewdurationdependingstage.'
],['weather_core_complete','item','battlerfull','b_change','battleweather_full'],'rawdifferent→weatherwrite→durationproposal→optionalactiveitemextender→durationwrite→animation/message→formeach→primalend.',failure='Core weather write precedesextendercallback; extendererrorleavesnewweather/oldduration. Lateranimation/message/formerrorleavesreachedwrites; no ensure rollback.')
row(694,[
 'Abilityweatherwrapper bydefaultrejectsanycurrentHarshSun/HeavyRain/StrongWinds rawvalue.',
 'ignore_primal=true removesonlythatouterprimalprohibition; sameweatherstillreturns.',
 'Passedwrapper showsabilitysplash/conditionalfallbackmessagebeforecallingcore.',
 'FIXED_DURATION_WEATHER_FROM_ABILITY true +nonprimalnewweather choosesfixedtrue5beforeextender.',
 'Settingfalse ordinaryabilityweatherchooses−1; primalthreenewweathertypesalwaysfixedfalse−1regardlesssetting.',
 'Explicitprimalabilitiescallignore_primaltrue; rawcurrent/defaultsourceoverridesnotastack.'
],['weather_core_complete','abilityeffects','b_settings','battlerfull'],'OnSwitchIn/damageabilityhandlers→wrappercurrentgates→splash→fixeddecision→Weathercore; fulltriggeractivityatactualcaller.',failure='Splash/messagefailuremayprecedeweatherwrite; corefailureprefixthenasC693. Doesnotpromiseabilityeffectcleanup.')
row(695,[
 'defaultWeather= directsetsdefaultandcurrenttoargument.',
 'Itsetsduration−1evenifequalpreviousvalue; nocomparisonrefreshguard.',
 'Itdoesnotinvokeordinaryweatherstartanimation/message/form/primalcheckbyitself.',
 'DefaultTerrainsetteranalogous; class/propertyimplementationnotfutureAPIrequirement.'
],['weather_core_complete'],'prepareexplicit/worldmappeddefault→directsetter3writes; distinctlaterstart/entrynotifications.')
row(696,[
 'DAMPROCK handlerextends onlyRainpositivecoreproposalto8.',
 'HEATROCK handlerextends onlySunpositivecoreproposalto8.',
 'ICYROCK handlerextends onlyHailpositivecoreproposalto8.',
 'SMOOTHROCK handlerextends onlySandstormpositivecoreproposalto8.',
 'No user/inactiveitem/no correspondingmatchedweather preservesbase; duration−1neverextendercalled.',
 'ShadowSky notamongfourrockmatchedtypes, so fixedWeathercorebase5remains5underdefaultfourhandlers.',
 'ShadowSkydataoptionalbinding/ordinaryusagefrontsseparate; classdefinedaloneisnotloadedoptionaldataevidence.'
],['item','weather_core_complete','battlerfull','shadowother'],'activeWeatherExtenderitemdispatch→specificweathercomparison→8 orfallbackproposal; ShadowSkyWeatherMoveinheritsbaseguard/fixedcall.')
row(697,[
 'Weathercore afternewvalue/duration/messageiteratesallcurrentnonfaintedBattlerspbCheckFormOnWeatherChange beforeEndPrimordial.',
 'Weatherformcheckerrejectsfainted/Transform; ForecastCASTFORM/FlowerGiftCHERRIM chooseeffectiveweatherdependentforms.',
 'ChangingmemberformcallsBattler.pbChangeForm→self.form/write-throughPokemonform setter→pbUpdate(true)/HPdifferencepreservation→scene/seen; notmerelyvisualanimation.',
 'ICEFACE/EISCUEhailpathsetsrestoreflagforlaterformphase; noimmediateformcommitpromisefromthisbranch.',
 'FullspeciesMega/forms/abilityfamiliesremainseparatereceivedfacts; genericweathercoredoesnotcertifyallformsideeffects.'
],['weather_core_complete','b_change','battlerfull','crec_form_join'],'coreweatherchange→actualweatherformchecker→conditionalrealformsetter/cache/stats/dex→primaltermination; UIaftermodelprefix.',open=['Allspecificdefaultform/data/possiblehandlers/nativeSceneoutputs beyondactualboundedCTF/CREjoins remainOPEN, notwholeWP21/49PASS.'])
row(698,[
 'EndPrimordial returnsimmediatelywhenrawcurrent==defaultWeather, includingdefaultprimal.',
 'IfdifferentcurrentHarshSun,absenceofcurrentactiveDESOLATELAND viaallBattlersglobalqueryclearsrawNoneandmessages.',
 'IfdifferentHeavyRain,absenceofactivePRIMORDIALSEAdoesanalogousclear.',
 'IfdifferentStrongWinds,absenceofactiveDELTASTREAMdoesanalogousclear.',
 'Ifrequiredactiveabilityexists, nochangefromthatcase.',
 'OnlyifrawweathervaluechangeddoesitnotifyallBattlersformchecks.',
 'Thenifdefault!=None itstartsdefaultwithnilsource/defaultfixedfalse, duration−1; otherwisekeepsNone.',
 'Defaultprimalexemptioncomesfromequaldefaultguard, notabilityexistence; nolasttemporaryweatherrestorestack.'
],['weather_core_complete','battlefull','battlerfull','b_change'],'current!=default→specificprimalrequiredabilityquery→clear/message→formeach→optionaldefaultrestart−1; errorskeepreachedprefix.')
row(699,[
 'Weathercorecallsprimalterminationafterweatherformnotification.',
 'SwitchOutabilitytail marksBattlerfaintedandchecksEndPrimordial, so departedabilityneednotcount.',
 'FormalFaint pathandabilitynegation/changehandlerscallactualEndPrimordial atrecordedpoints; notanEOR-onlypoll.',
 'ContinualAbilityChecks beginswithEndPrimordial; nestedabilitychange/neutralizinggasendcanrecheck.',
 'Newprimaloverridingoldprimal doesnotchangestoreddefaultsource; restoredsourceisdefault, notstackedtemporaryrain.'
],['weather_core_complete','ability_item','b_change','abilityeffects'],'weather/start/switch/faint/continual/abilitychange actualcallers→sameprimalterminationhelper→defaultsource; no periodic-onlyrestriction.')
row(700,[
 'ReachedEORweatherstep decrementspositiveDurationfirst; −1stays−1.',
 'Atduration0 itselectsendfeedbackfromstoredweatherthenwritescurrentNone.',
 'ThenallBattlersformchecks; defaultnonNone startswithnilsource/fixedfalse→−1.',
 'Afterexpiry ifcurrentstillNone returnsbeforecontinuousweatherreaction/damage.',
 'Ifdefaultrestartleftactualweather, thesameEORcallcontinueswithrestoredweatheranimation/message, perpriorityactiveabilityweatherreactionandweatherdamage.',
 'CloudNine/AirLock donotpausecounter orrawstoredcontinuingannouncement.',
 'PerbattlereffectiveNone canblockweather-specificdamage/reactionsdespiterawcontinuingmessage; abilityhandlergetsactualmember.effectiveWeather.',
 'Cachedpriorityarray ispassedfromEORmaster; no freshspeedresortinweatherhelperitself.'
],['eor_all','weather_core_complete','battlerfull','abilityeffects','b_change'],'EORcachedpriority→positive--→zeroexpire/message/None/forms/default→Noneearlyreturnorrestoredweathercontinuedreactions/damage.',failure='Endingmessage mayfailafterduration--beforeclear; form/defaultstart mayfailafterclear; weatherability/HP/item/faint mayfailmidpriority. No rollback/fullEORcleanupguarantee.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_10a.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
