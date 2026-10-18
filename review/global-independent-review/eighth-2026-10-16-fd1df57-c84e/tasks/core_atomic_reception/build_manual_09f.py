import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_09e.json').read_text());d=base['source_dictionary'];rows=[]
d['event_registry']={'path':'Data/Scripts/003_Game processing/006_Event_HandlerCollections.rb','range':[1,123],'actual_reader':'/root/core_atomic_reception','reading':'OwnFULL123 and EventHandlers42–65 actualreread; NamedEvent66–91 in separate005 source also ownFULL298'}
d['battle_intro_outer']={'path':'Data/Scripts/012_Overworld/002_Battle triggering/002_Overworld_BattleIntroAnim.rb','complete_units':[[51,57],[59,152]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete Standby/Animation actuallyread; originalWorld limitedfacts remainseparate'}
d['pokemon_heal']={'path':'Data/Scripts/014_Pokemon/001_Pokemon.rb','range':[274,306],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete heal_HP/status/PP/heal actuallyread273–310'}
d['pokemon_ability_queries']={'path':'Data/Scripts/014_Pokemon/001_Pokemon.rb','complete_units':[[428,464],[471,475]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE actual complete index/id/get/set/hasAbility methods, notwholePokemon'}
d['shadow_main']={'path':'Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb','range':[1,221],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ nowactually all1–115/116–139/140–180/181–187/188–205/206–221; no allShadowdata/nativePASS'}
d['startover']={'path':'Data/Scripts/012_Overworld/001_Overworld visuals/003_Overworld_MapTransitionAnims.rb','range':[80,138],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete StartOver method only; alternateBugContest/map/native subdomains notwholegranted'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(631,[
 'Worldcores execute BattleStart underSceneStandby insideBattleAnimation block; ifcurrentSceneMap, standby disposessprites/clearscache/frameresets beforeyield thencreatespritesafteryieldnormalreturn, notanensure.',
 'AfterBattle playercurrentparty eachPOISON statuscount0 regardlesspriorcountpositive, unmega/unprimal. Registeredpartnerpresence thenPlayerheal_party andeachpartnerPokemonheal/unmega/unprimal, independentofactualpartnerparticipation.',
 'Outcome2/5&&canLose additionallyhealseachcurrentplayerPokemon andGraphicsupdatesfor0.25s. Heal skipsEgg andsetsHP/status/PP/readyflag byitsactualdefinitions; no worldruntimewaitexecutionclaim.',
 'Then EventHandlers trigger defaultregisteredNamedEvent callbacks; onlynormalcompletedtriggerreturn reachesfinalplayerstraighten. This call animation/prelockresets, doesnot restoreorwritecurrentdirection.',
 'Currentformal finaldirectionphrase isalready same-rootCOM005 WP42propagation required/P3 under root5960B0972… receivedactual97lines; allprecedingcorrecthealing/notification/orderretained. New53986candidate onlyassociatedhistoricalsupplement, notnewroot/count.'
],['after','wild','trainer','battle_intro_outer','pokemon_heal','pokemon_mega_full','event_registry','event_dispatch','shadowother'],'normalcore→standbyreturn→actualparty/partnerheals→callbacks→animationreset, existingboundedrootfacet.',support='EXISTING_ROOT_REQUIRED_BOUNDED',open=['Only existing COM005 minimal finalphrase waitsseparatelyauthorizedamendment; globalhistory/completeforeignworlddomains remainOPEN.'])
row(632,[
 'Default evolve_and_black_out callback checks evolution iff CHECK_EVOLUTION_AFTER_ALL_BATTLES OR(decision!=2&&!=5); fixedtrue, false stillallows0/3/1/4.',
 'EvolutionCheck percurrentplayerparty index skipsnil/Egg, thenfaintedonlyifallowFaintedfalse. Ifbeforelevelrecordexistsandlowerthancurrentlevel, trieslevelup evolution; ifresultnil triesafterBattle(index), nonnil thenSceneStart/Evolution/End.',
 'Inthisdefaultcallback afterqualifiedEvolutionChecknormalreturn clears threebeforelevels/criticalhits/directdamage records; pickup/blackoutcase follows. Do notreinterpretparagraphas transactionalclear onlyaftereveryothercallbackfinished.',
 'Separate defaultShadowready callback uses recordedheartgauges indices/currentpartyidentity, skipsmissingPokemon/missingoroldzero, currentgauge0callsCheckReady; itdoesnotreadthethreeclearedrecords.',
 'CheckReady onlyifactualShadow, updatesShadowmoves thenpossiblegauge0ready-message; malformed/missingheartrecord/callbackerror canpreventlatercallback/straighten. Sourceexistingforwardedevolutionconditions/cancel/commit retainfinite CREAlifecyclefacts, notallEvolutionapproval.'
],['events','event_registry','event_dispatch','b_settings','shadowother','shadow_main','growth','pokemon_growth_qual','crec_growth'],'config/partyeligibility→levelthenafterBattlequery→scene→specificrecordclear→laterdefaultcase, plusseparateShadowconsumer.',open=['Actual per-species evolutioncondition handlers and fullEvolutionScene beyondalreadyreceived18finiteCAA lifecyclefacts remainexactforwardedconsumers; nativeGUI/compiledconditions notallPASS.'])
row(633,[
 'Defaultcallback result1/4 loopscurrentPlayer.pokemon_party (nonnilnonEgg) andperPokemon PickupthenHoneyGather.',
 'Result2/5&&!canLose unpauses BGM thenBGS beforeStartOver; canLosetrue skipsthisrecovery, otherdecisionsskipbothswitchbranches.',
 'OrdinaryStartOver outsideBugContest incrementsblacked_out_count thenheal_party; registeredcenterlocation setsvehicles/followers/switch/targetcoords/direction, conditionalSceneMaptransfer/maprefresh.',
 'No-center branch choosesPlayerMetadatahome thenMetadatahome; existinghomemapmissing canmessage(DEBUG), healagainandreturnbeforeEscapePointclear. Homepresenttransfer/currentSceneMap only; nohome justheal. BugContestearlyvariantforwarded separately.',
 'Thus invocationdoesnotguaranteemapchange. Earlierunpause/stat/heals/transfer-temp writescanpersistiflaterfailure; allnativeworld/alternate-mode behaviornotcertified.'
],['events','event_registry','event_dispatch','startover','playerfull','pokemon_heal'],'outcomecase→orderedunpause/recoveryorcurrentpartyitemreceivers, preciseearlyexitandnativeboundary.',open=['Full vehicles/followers/transfer/nativeAudio andBugContest recovery subdomains remainindependentlyforwarded, not assumed alwaysreturnhome.'])
row(634,[
 'AfterBattleblocknormalreturn BattleAnimation PopFade thenGameSystemqualified BGMresume/BGSresume using savedplayingobjects. Thispost-yieldroute isnotensure.',
 'memorized_bgm nil andmemorized_bgm_position0; nextBattleBGM nil.',
 'nextBattleVictoryBGM nil; nextBattleCaptureME nil; nextBattleBack nil.',
 'Encounterstepcount resets, viewportblack then0.4s Graphics/Input/Mapupdate fade, viewportdispose, in_battlefalse onlyatnormalend.',
 'Corethen Input.update, SetOutcome classification:1/4 chosenwild-ortrainer won++,2/3/5 lost++,0none; pbSet outcomevariableaftercounter.',
 'FailurebeforeSetOutcome meansnoitscounterwrite; failureaftercounterbeforevariable preservescounter. NativeAudio/scene/input/serialization successnotinferredfromsourcecallorPythonexit0.'
],['battle_intro_outer','wild','trainer','after','config','audio','audio_path'],'normalyieldreturn→orderedresourceclear/fade→input→stats-before-variable, no globalfinally.')
row(635,[
 'Wildnormalwrapper boolean falseonlyoutcome2/5;0/1/3/4true. Trainernormalwrapper trueonly1, capture4orabort0false.',
 'Wildsingle&&can_override wrapperposthook runsaftercore SetOutcome andmayreadactualfoeobjects; override handlednonNil beforecore isdifferententrance.',
 'Trainer waiting/facing merge anddirectexistingobjects followearlierWP39qualification; blanketordinaryEnd/resourceguarantees arenottransferred.'
],['wild','trainer','after','event_registry','event_dispatch'],'corestats/resultwrite→optionalwildposthook→mode-specificwrapperboolean, not victoryequivalence.')
row(636,[
 'WorldPickup/Honey calledinendnotificationforcurrentpersistentnonEggPokemon. EntrancestestpersistenthasAbility? andhasItem?; nofaintguard andnobattleabilityActive/NG/Embargo/MagicRoom predicate.',
 'PersistentAbilitygetter usescachedid orSpecies/ability-index/personalIDfallback thenGameDataAbility record; hasAbility comparesrecordidentity viareceivedInstanceMethods, not merelyfieldparity/owner.',
 'Noarg hasItem israwitem!=nil; false thereforecounts asoccupied andskipsacquire, while lateritemgetterwouldneedregistrytypequalification. Same-named battlePickup EORtransfer hasdifferentgates/inputs/restorewrites.'
],['events','pokemon_ability_queries','pokemon_item_exact','registry_finite','crec_form_join','eor_late_handlers'],'worldendcurrentpersistentqueries→separateworldfamily versusbattleactiveitem-transferpolicy.')
row(637,[
 'PickupfirstEgg/ability/heldgate thenrand100<10; onlyaftertriggerfiltersDynamicItemListexists preservingorder. Filteredcommonlength>=18 andrare>=11 elseabandonwithoutsecondchoice.',
 'start=max((min(100,level)-1)*10/100,0) integerarithmetic;normallevels1–10start0through91–100start9, above100capped9/belowlowerclamped0.',
 'Build9commonpositions then2rare fromfilteredtablesatstart; positionweights30/10/10/10/10/10/10/4/4/1/1 total100.',
 'Secondrand(sumweights), cumulativefirststrictlygreater selectsposition andPokemon.item=; no sorting/uniformrare-group draw. Datasettablesreplaceablebutorder/windowmathsame.',
 'Missing/typeinvaliddata canfailafterfirstdraw orfilterprefix; noItemwritebeforequalifiedselection, noautomaticdefaultbackfill.'
],['events','pokemon_item_exact','itemdata','registry_finite','pokemon_ability_queries'],'eligibility→firsttrigger→orderedfilter/length→levelwindow→cumulativeweightedsecondchoice→persistentitem.')
row(638,[
 'Defaultcommon position1 POTION.','Defaultcommon position2 ANTIDOTE.',
 'Defaultcommon position3 SUPERPOTION.','Defaultcommon position4 GREATBALL.',
 'Defaultcommon position5 REPEL.','Defaultcommon position6 ESCAPEROPE.',
 'Defaultcommon position7 FULLHEAL.','Defaultcommon position8 HYPERPOTION.',
 'Defaultcommon position9 ULTRABALL.','Defaultcommon position10 REVIVE.',
 'Defaultcommon position11 RARECANDY.','Defaultcommon position12 SUNSTONE.',
 'Defaultcommon position13 MOONSTONE.','Defaultcommon position14 HEARTSCALE.',
 'Defaultcommon position15 FULLRESTORE.','Defaultcommon position16 MAXREVIVE.',
 'Defaultcommon position17 PPUP.','Defaultcommon position18 MAXELIXIR.'
],['events','itemdata','registry_finite'],'fixed18positionorderedinputdata beforeexistencefilter/window, notall18runtimeexistenceoritemeffectsapproval.')
row(639,[
 'Defaultrare position1 HYPERPOTION.','Defaultrare position2 NUGGET.',
 'Defaultrare position3 KINGSROCK.','Defaultrare position4 FULLRESTORE.',
 'Defaultrare position5 ETHER.','Defaultrare position6 IRONBALL.',
 'Defaultrare position7 DESTINYKNOT.','Defaultrare position8 ELIXIR.',
 'Defaultrare position9 DESTINYKNOT.','Defaultrare position10 LEFTOVERS.',
 'Defaultrare position11 DESTINYKNOT.'
],['events','itemdata','registry_finite'],'fixed11positionraredata retainsduplicatedDestinyKnot7/9/11, notsetdedup.')
row(640,[
 'DynamicItemList iterates eachprovidedentry, pushesifItem.exists?; keepsoriginalorder andduplicates, excludesundefinedwithoutsortingorbackfill.',
 'DefaultDestinyKnotthreepositionssurviveindependentlyifdefined; nameidentityequalitydoesnotmergepositions.',
 'Minimum18/11 checkisAFTERfilter; tooshortreturns. Longerreplacementtablesstilluse filteredstart/window ratherthanoriginalpositionlabels.',
 'Ifallentriesexist, defaultstart0forL1–10/1for11–20/.../9for91–100, thencommon9rare2. Concreteitemeffectsemanticsnotrequiredbyselectioncontract.'
],['events','itemdata','registry_finite'],'inputentries→orderedexistsfilter→minimumlength→samelevelstart/window onfilteredarray.')
row(641,[
 'Tablepositions below are relative toselected9common+2rarewindow, notabsoluteoriginaltableindices.',
 'Secondrandomsource uses sumfixedweights100 and integer0..99 undervalidRNGcontract; first10%trigger isseparateconditionaldraw, no empiricalsamplingclaim.'
],['events'],'selectedwindow-localposition→secondintegerweightedlookup, distinct firsttrigger.')
base['source_dictionary']=d;base['rows']=rows
assert all(k in d for r in rows for k in r['source_units']if isinstance(k,str))
(P/'manual_batch_09f.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children'])for x in rows),'open_rows':sum(bool(x.get('open'))for x in rows)})
