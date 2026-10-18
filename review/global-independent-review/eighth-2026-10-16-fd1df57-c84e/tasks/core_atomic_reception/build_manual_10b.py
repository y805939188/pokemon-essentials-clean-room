import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_10a.json').read_text());d=base['source_dictionary'];rows=[]
d['statuses_full']={'path':'Data/Scripts/011_Battle/002_Battler/004_Battler_Statuses.rb','range':[1,575],'actual_reader':'/root/core_atomic_reception','reading':'OwnpriorFULL575; freeze/terrain/confusion actualconsumerbinding, notSuccessChecksfile'}
d['defog_complete']={'path':'Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb','range':[1217,1312],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE completeDefogclass with all4methods actuallyread; normalstat/successfamily separate'}
d['targetstatdown_parent']={'path':'Data/Scripts/011_Battle/003_Move/004_Move_BaseEffects.rb','range':[173,193],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE completeTargetStatDownMoveclass actualread; notwholeBaseEffects orincidentalTargetMultiStats tail'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(701,[
 'EORWeatherDamage rejectsfaintedbeforeweathertypequery.',
 'Onlymember.effectiveWeatherSandstorm/Hail/ShadowSky enterslistedweatherdamagecase; otherweathertypesamt−1→return.',
 'Eachlistedweatherrequiresitsown takesXXXDamage gate beforemessage/amount.',
 'Sandstormnominalamountinteger totalhp/16.', 'Hailnominalamountinteger totalhp/16.', 'ShadowSkynominalamountinteger totalhp/16.',
 'LivingpbReduceHP rounds/clipsatcurrentHP andensuresnominalbelow1becomes1; scalarwritebeforeHPscene/report.',
 'Weatherhelperactualorder weatherdamagefeedback→SceneDamageAnimation→ReduceHP(amt,false)→ItemHPHealCheck→Faintifstillfainted; do notsubstitutegenericTakeEffectDamageadditional-halfabilitychain.',
 'Sandstormgroundtypeexcluded.', 'Sandstormrocktypeexcluded.', 'Sandstormsteeltypeexcluded.',
 'SandstormandHail exclude underground/underwater specificTwoTurnfunctioncodes, notallsemivulnerablemoves.',
 'SandstormexcludesactiveOVERCOAT/SANDFORCE/SANDRUSH/SANDVEIL.',
 'SandstormandHail excludeactiveSAFETYGOGGLES.',
 'HailexcludesICEtypeandactiveOVERCOAT/ICEBODY/SNOWCLOAK.',
 'ShadowSky excludesShadowPokemonbyitsactualquery.',
 'Allthree inherittakesIndirectDamage fainted/activeMAGICGUARD exclusions; noall-weather-damages inference.'
],['eor_all','battlerfull','b_change','ability_item','shadow_main'],'effectiveweathertype→specifictype/two-turn/ability/item/Shadowgate→floorHPfraction→feedback/animation→writeHP→itemcheck/faint.',failure='Weathertext/animation failures canprecedeHPwrite; HPscene/item/faint failure canfollowHPwrite. Earlierduration/form/reactiveprefixretained; no fullcleanup guarantee.')
row(702,[
 'StartShadowSkyWeather completeconstructorinheritsWeatherMove andsetsweatherTypeShadowSky.',
 'WhenfunctionactuallyboundtoregisteredmoveandordinaryPP/usefrontspassed, wholemovefailurechecksrawcurrentShadowSkyduplicate.',
 'InheritedWeatherMove rawHarshSun/HeavyRain/StrongWinds rejectsregardlesssuppressedbattleweather.',
 'RawNoneorordinarydifferentweatherpassesinheritedwholemovecheck; otherordinaryfrontsmustalsopass.',
 'SuccessEffectGeneral passesfixedtrue/showAnimfalse toweathercore, currentShadowSky/baseDuration5.',
 'DefaultfourrocksnevermatchShadowSky, so no8extensionfromthem.',
 'Noadditionalcoregenericweatheranimationforfalseflag; ShadowSky-specificmessage/formchecks/primalend stillactualcoretail.',
 'EORpositivecounter/suppression/memberShadowSkyindirectdamage remain samegeneric/specifichelpers, notnewalternateclock.'
],['shadowother','weather_move_parent','weather_core_complete','item','use','eor_all'],'boundShadowSkyclass→ordinaryfronts→rawWeatherMoveguard→fixedcore→actualweather/form/EORconsumers.')
row(703,[
 'Definitionexistencealone doesnotproveoptionalSHADOWSKYcontentcurrentlyloaded/registered orDemoable.',
 'Onlyactualbinding/reachedordinaryusegatesactivatethisfunctioncontract.',
 'Coreweatherwriteprecedesitsduration/item/presentation/formtail; laterfailurekeepsactuallyreachedprefix ratherthanpromisingnormalwholemovecompletion.'
],['shadowother','weather_move_parent','weather_core_complete','use'],'definition→conditionalboundmovelookup→frontgates→writebeforetail; no optionaldata/fullsuccess inference.',open=['DefaultoptionalShadowcontentregistration/loadedcompileddata/Demoevent notclaimed by sourceclass; no targetexecution.'])
row(704,[
 'Terraincore rawequalcurrent returnswithoutdurationrefresh/animation/callback.',
 'Differentterrainwritescurrentbeforeextensiondurationlogic.',
 'fixedDurationdefaulttrue proposes5; explicitfalse proposes−1.',
 'Positiveproposal+nonnilsource+activeitem invokesTerrainExtender; defaultregisteredTERRAINEXTENDERreturns8, othersfallbackoriginalproposal.',
 'Durationwritecomesafterhandler, thenregisteredanimation/abilitysplashhide/specificterrainmessage.',
 'Core firstallBattlerspbAbilityOnTerrainChange, thenseparateallBattlerspbItemTerrainStatBoostCheck; nointerleavingperbattlerbetweenbothloops.',
 'FourordinaryterrainMoves eachrejectrawsameElectric/Grassy/Misty/Psychic beforeEffectGeneral→StartTerrain.',
 'FourSurgeOnSwitchInhandlersalsorejectrawsamebeforeSplash/StartTerrain; activeabilityeligibilityatcallerretained.',
 'AbilityOnTerrainChange checksabilityActive; ItemTerrainStatBoostCheck checksitemActive andhandlertruebeforeHeldItemTriggered. Methodcallcountnotpromiseeveryspecificcallbackeffect.'
],['weather_core_complete','weather_terrain_moves','item','abilityeffects','ability_item','battlerfull'],'differentrawterrain→currentwrite→activeitemextension→duration→presentation→allabilityloop→allitemloop, exactsame-state front.',failure='Extendererrorcanleavecurrentnewwitholdduration; lateranimation/message/firstloop/secondlooperrorsretainearlierpartialwrites/checks. No transaction.')
row(705,[
 'affectedByTerrain rejectsairbornefirst, thenanysemiInvulnerable; otherwise true.',
 'airborne falseforactiveIRONBALLbeforeotherflightreasons.',
 'airborne falseforIngrainflag.', 'airborne falseforSmackDownflag.', 'airborne falseforpositiveglobalGravity.',
 'Absentearliergrounding, FLYINGtypeisairborne.',
 'Absentearliergrounding, activeLEVITATEisairborne onlywhenbattle.moldBreakerfalse.',
 'Absentearliergrounding, activeAIRBALLOON isairborne.',
 'Absentearliergrounding,positiveMagnetRise isairborne.',
 'Absentearliergrounding,positiveTelekinesis isairborne.',
 'Noearlierground/flightreasonreturnsfalseairborne; beinggroundedstillnotguaranteedterrainaffectedbecausepositiveTwoTurnsemiInvulnerablemayreject.',
 'semiInvulnerable usesactualTwoTurnMovefunctionlookup for6namedsky/underground/underwater/Bounce/PhantomForce/SkyDropfunctioncodes, notjusttype/visualheight.'
],['battlerfull','weather_core_complete'],'orderedgroundingoverrides→flightquery/moldbreak→semiInvulnerableexactfunctionlookup→terrainrecipienteligibility; activeitemgatesstayactual.')
row(706,[
 'ElectricpowerboostrequiresElectrictypeanduseraffectedByTerrain; gen8multiplier1.3vsolder1.5.',
 'GrasspowerboostrequiresGrasstypeanduseraffected; samegenerationmultiplier.',
 'PsychicpowerboostrequiresPsychictypeanduseraffected; samegenerationmultiplier.',
 'MistyDragonpowerhalvingusestargetaffectedByTerrain, notuserqualification.',
 'ElectricnewSleep/preventdrowsysleepconsumerterraingatesreadrecipientaffected; notanunqualifiedglobalstatusban.',
 'Mistyordinarynewstatuschecksaffectedrecipient; confusionadditionalMistyguardrequiresgen>=7.',
 'PsychicTerrain targetsuccessgate requirescurrentPsychic +recipientaffected +opposinguser +choices[user.index][4]>0savedpriority.',
 'Positiveprioritysavedfield ratherthanrecomputedmovebasepriority isactualsource; same-side/ownrecipientnotopponentblockedbythisgate.',
 'EORGrassyheal rejectsfainted, thenrequirescurrentGrassy+affectedByTerrain+canHeal.',
 'Grassyamountinteger totalhp/16 thenRecoverHP clipdeficit/min1; HPwritebeforehealthmessage.',
 'A healingmessagefailure afterwrite doesnotrollbackHP; callback/restofEORexecutionnotguaranteed.'
],['calculations','statuses_full','checksfull','priority','eor_all','battlerfull','b_change'],'currentterrain→actualuser/recipientquery+savedpriority/HP/statusgate→specificmultiplier/protection/healwrite, sharedterrainnotsharedqualification.')
row(707,[
 'EORTerrainEnding decreasesdurationonlyifpositive inlaterphase.',
 'Expirybranchrequirescurrentterrain!=None andduration==0; countzeroalonewithoutcurrentdoesnotrestore.',
 'Expiryproducescurrentterrain-specificendmessage thenwritescurrentNone.',
 'ThenallBattlersabilitychangechecks observeNone.',
 'IfdefaultnonNone, StartTerrain(nil,default,false) writescurrent/defaultduration−1andperformsownallabilitythenallitemloops.',
 'Afterthatcore returns, EORcallerseparatelyaddsallabilitythenallitemloopsagain.',
 'Thus successfulrestorationcallsabilitycheck3waves:clearNone/coreestablish/afterestablish; itemcheck2waves:coreestablish/afterestablish.',
 'Thoseareactualentrymethodcalls conditionalonallBattlersmembershipandnormalreturn; activegates/handlercanavoiddouble-effect orproduceeffects; noforcedduplicate-sideeffect claim.',
 'Ifnoactualcurrentafterexpiryreturns; otherwiserestoredterraincontinuesanimation/message inthesameEORstep.'
],['eor_all','weather_core_complete','ability_item','battlerfull','abilityeffects','item'],'laterpositive--→nonNonezeroexpiry→clear/abilitywave1→defaultcoreability2/item1→extraability3/item2→continue; normalreturnrequiredbetweenwaves.',open=['Everyterrainability/itemhandlerrepeated-sideeffect outcome requiresitsactualcompletehandler/data; fullregistryreadaloneisnotallsemanticPASS.'])
row(708,[
 'SteelRollerMove failswholemoveifrawcurrentterrainNone.',
 'WhenitsEffectGeneralreached withterrain, sendspecificendmessage thenwritesfield.terrainNone.',
 'SteelRollerdoesnotwriteterrainDuration norcallTerraincore/terrainability/defaultrestart inthatcompleteclass.',
 'DefogTargetStatDownclass>=gen8 targetfailuregate canpassbecauseanyterrainpresent, beforeordinarylowerstatfailurefallback.',
 'DefogsuccessfultargeteffectmayfirstlowerEVASION/clearlistedwalls/hazards, then>=gen8presentterrainmessage→currentNone.',
 'Defogalsodoesnotresetduration/callnaturalexpiryability/defaultrestart fromitsdirectterrainclearbranch.',
 'LaterEORTerrainhelperstilldecrementspositiveoldduration, butcurrentNonefailsnonNonezeroexpiryguard; cannotguaranteedefaultrestoreafterdirectclear.',
 'Defogotherfronts/target/generation/clearance/statresultcanindependentlydeterminesuccess; no equivalenceSteelRollerNonegateallDefogfails.'
],['weather_terrain_moves','defog_complete','targetstatdown_parent','stages','checksfull','eor_all','weather_core_complete'],'directEffectGeneral/AgainstTarget→optionalpreexistingstat/wall/hazardwrites→terrainNoneonly→laterpositive--withoutnonNoneexpiry; distinctnaturalexpiry.',failure='Terrainendmessage mayfailbeforeNoneassignment; Defogearlierstat/sideclearwritesmayalreadyexist. Notautomaticall-or-noneeffect.')
row(709,[
 'EORmaster callsGrassyhealing inearlypriorityhealpass whileterrainDuration1/currentGrassy stillactive.',
 'SamecompletedroundlaterEndTerrain decreases1→0 andremovescurrent; earlierhealingnotretroactivelycancelled.',
 'WeatherDuration1 handledinearlyweatherstepfirstdecreases→0/ends; withnodefaultnooldSandstormdamage thatcall.',
 'Therefore remainingcounter1isnotauniformno-effectrule acrossweatherandterrain; orderinganddefaultrestorationmustbeaccounted.',
 'Earlydecision/exceptionbeforelatersteps maypreventcountdown; staticfull-EORvectorrequiresactualremainingphaseexecution.'
],['eor_all','weather_core_complete','battlerfull','b_change'],'weatherend/damageearly vsGrassyhealingearly/laterterrainexpire; samecounterdifferentprocessingpoint.')
row(710,[
 'Field13+Side22+Position9=44effectrecords; auxiliaryFutureSight4/Wish3 countedasrecordswithin9position, notseparatefeaturepackages.',
 'Weather/Terrain default/current/duration6fields remainseparatefrom44effects.',
 'Directoryinitialvalues andlifetimesareactualboundedperrecordcontracts, notfuturearrays/classes/implementationAPIorwhole44callbackapproval.'
],['activefield_full','weather_core_complete','eor_all'],'actualnamedrecordinitializers→perrecordproducer/consumer/lifetime directory; semanticreceiptforeachrecordcontinues.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_10b.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x['children'])for x in rows))
