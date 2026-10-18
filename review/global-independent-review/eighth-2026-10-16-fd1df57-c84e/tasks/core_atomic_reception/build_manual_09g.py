import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_09f.json').read_text());d=base['source_dictionary'];rows=[]
d['move_pp_hm_data']['reading']='PARTIAL_FILE actual complete declaration/schema/constructor/getters/hidden_move predicate; parent408 lines; mandatory manual-09b-source-binding-supplement.v1.json corrects old451 metadata only'
d['battle_loop_complete']={'path':'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb','range':[322,347],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ and complete loop actuallyreread'}
d['abort_raise']={'path':'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb','range':[1,6],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ; complete exception class/pbAbort source actualreread'}
d['normal_end']={'path':'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb','range':[349,568],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ; exactnormalEnd/callees separatelybounded'}
d['growth_all']={'path':'Data/Scripts/011_Battle/001_Battle/003_Battle_ExpAndMoveLearning.rb','range':[1,271],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ; numeric/config/data joins finite CRE/KERNEL facts separately'}
d['eor_all']={'path':'Data/Scripts/011_Battle/001_Battle/011_Battle_EndOfRoundPhase.rb','range':[1,781],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ; concrete callback contracts remain separately received/bounded'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
def layout(n,why):rows.append(dict(number=n,layout_reason=why))
layout(642,'Weighted-table column heading only; local-window meaning already manually received C641. Eleven following complete payload rows receive individual semantic children, not header-as-behavior.')
row(643,['Common localposition1 has weight30 of total100.','After prior Pickup trigger/filter/window gates, integersecondrnd0 through29 selectcommonlocal1.'],['events'],'commonweight30→cumul30; rnd<30→items[0]→Pokemon.item=; tableindexiswindowlocal.')
row(644,['Common localposition2 has weight10.','Secondrnd30–39 selectscommonlocal2 afterpreviouscumulative30.'],['events'],'firstfailedthreshold30→nextcumul40→items[1] setter.')
row(645,['Common localposition3 has weight10.','Secondrnd40–49 selectscommonlocal3.'],['events'],'cumulative40 then50→items[2] setter.')
row(646,['Common localposition4 has weight10.','Secondrnd50–59 selectscommonlocal4.'],['events'],'cumulative50 then60→items[3] setter.')
row(647,['Common localposition5 has weight10.','Secondrnd60–69 selectscommonlocal5.'],['events'],'cumulative60 then70→items[4] setter.')
row(648,['Common localposition6 has weight10.','Secondrnd70–79 selectscommonlocal6.'],['events'],'cumulative70 then80→items[5] setter.')
row(649,['Common localposition7 has weight10.','Secondrnd80–89 selectscommonlocal7.'],['events'],'cumulative80 then90→items[6] setter.')
row(650,['Common localposition8 has weight4.','Secondrnd90–93 selectscommonlocal8.'],['events'],'cumulative90 then94→items[7] setter.')
row(651,['Common localposition9 has weight4.','Secondrnd94–97 selectscommonlocal9.'],['events'],'cumulative94 then98→items[8] setter.')
row(652,['Rare localposition1 has weight1.','Secondrnd98 selectsrarelocal1.'],['events'],'cumulative98 then99→items[9] setter.')
row(653,['Rare localposition2 has weight1.','Secondrnd99 selectsrarelocal2; no previousintervalmatches99.'],['events'],'cumulative99 then100→items[10] setter; breakafterwrite.')
row(654,[
 'Nine commonweights sum98; tworareweights1each; finalsum100, so validinteger0..99 partitionswithoutoverlap/gap.',
 'Conditional firstPickup10%draw passed and all originaldefaulttable IDsregistered, L1startindex0 rarewindow[HYPERPOTION,NUGGET].',
 'UnderthatL1premise seconddraw98assignsHYPERPOTION;99assignsNUGGET.',
 'Conditional sameall-IDpremise, L91startindex9 rarewindow[LEFTOVERS,DESTINYKNOT].',
 'UnderthatL91premise seconddraw98assignsLEFTOVERS;99assignsDESTINYKNOT.',
 'Chosen registeredID goes to originalPokemon.item=, a persistentobjectfield before any later caller/save; thisselection doesnotexecute its held/use effect.'
],['events','pokemon_item_exact','itemdata'],'levelclamp→orderedfilteredwindow→cumulativeweightedsecondrnd→originalPokemon.item=; itemuseeffectnotinvoked.',persistence='Pokemon helditem field remains on original object. Full native save/reload outcome not run; finite Kernel objectserialization receipt does not guarantee every dynamic field/defaultdata.')
row(655,[
 'HoneyGather firstrequiresGameData::Item.exists?(:HONEY); missingrecordreturnspreRNGandwrite.',
 'ThenEggorabsenceofstoredindividualHONEYGATHERoranynonnilhelditemblocks; no battleractive/suppression gate is substituted forPokemon.hasAbility?.',
 'Threshold=5+floor((level−1)/10)*5 atordinaryintegerlevels; L1–10threshold5,L11–20threshold10.',
 'This Honeyformula has no Pickup-style min100/max0clamp initsownmethod; do notinferPickupwindowformula.',
 'Itsownrand100 must be strictlylessthanthreshold; onlypassedgateassignsHONEY.',
 'Default on_end callback loopscurrentnonEggPokemon afterdecision1or4 and callsPickupthenHoneyon thesameindividual.',
 'Honeyrecheckshelditem afterPickup; earlierPickupsuccess canblockHoney. Eachmethodmakesitsownconditionaldraw, no single sharedsample or independence/empiricalfrequencyclaim.',
 'HONEY assignment uses Pokemon.item= persistentreference; missing/failed priorgate leavesitemunchanged, latercallbackfailuredoesnotrollbackearlierPickup/Honeywrite.'
],['events','pokemon_ability_queries','pokemon_item_exact','event_registry','event_dispatch','itemdata'],'on_end evolve_and_black_out reached→currentpokemonparty result1/4→Pickup→Honey exist/Egg/ability/item gates→threshold→rand100→item=HONEY.',open=['Demo/eventactualinvocation and native/randomsampling are NOT_EXECUTED; lexical/defaultcallback contract only, notallpluginregistrations.'])
row(656,[
 'Worldskipguard checks zeroableplayerfirst, thendebugCTRL; acceptedskipneverconstructsbattleorinitializesnormalbattle-core.',
 'Skiphelper hasitsownconditionalmessages, clear_battle_rules, optionalrememberedBGMresume, thenresetsmusicmemoranda/nextBattleoverrides andencounterstepcount.',
 'Skipoutcome defaults1; trainerwithzeroable sets0; pbSetrequestedvariable happensafterprecedingcleanup, nottheordinaryEndOfBattle result path.',
 'Wild wrapper can havealreadyconverted/speciesgeneratedPokemonbeforecore skipguard; sourceprefixmustnotberolledbackbycallingitskip.',
 'Bothnormalcorestartrecord/on_start/normalEnd/on_endpath lieafterguard; no battlepre-records ornormalterminalnotification from thisskip path.'
],['outer','wild','trainer','record_start','events'],'wrapperarguments/preparedwildprefix→coreearlyskip→skiphelper→resultvariable; noBattle.new/start/endchain. Normalcontrols WP39:113/BC09 and COM004keep; no newskipfinding.',failure='Skipmessages/BGM/cleanup can failbeforelaterclear/result; alreadycompletedprefixremains. No all-or-nothingcleanupguarantee.')
row(657,[
 'BattleAbortedException is directException subclass; pbAbort raisesit, ratherthanreturningnormaldecision.',
 'pbStartBattle beginsrescue onlyaroundpbStartBattleCore; ensureparticipants andpeerstarting hooksbeforebegin areoutsideitsdedicatedrescue.',
 'Caught explicitabort overwritesdecision0 thenrequestsScene.pbEndBattle(0); normalBattleLoop pbEndOfBattle isbypassed.',
 'Therefore itsunuseditemCancelChoice refunds, normalleavingeffects, initialItemsrestore, caughtPokemonstoreandPokerusnormalEndtailare notreach-guaranteed byabort.',
 'Ifsceneend andworldwrappersreturnnormally, worldafter_battle/on_end canstillrunwithdecision0 andpbSet0; decision0maystillallowEvolutionCheckaccordingactualconfig.',
 'CallingbareBattle.pbStartBattle suppliesnobodywithworldcoreafter_battle/resultvariableimplicitly; keepthatcallerboundary.'
],['abort_raise','start','battle_loop_complete','normal_end','outer','wild','trainer','after','events'],'pbAbortException→escapebareStandardErrorphasewrapper→startcorerescue→decision0/sceneend→conditionalworldnormalreturn→after/Set; normalEndnotcalled.',failure='A secondexceptioninabortsceneend oranyoutercallback canstoplaterworldafter/Set. Earlierpartialwritesandabortedscenechangesremain; nofinally cleanup.')
row(658,[
 'Selected-move innerdiagnosticboundary is pbProcessTurn actualcallto pbUseMove insideitsownlogonerr, distinctfromwholeCommand/Attack/EORstagewrappers.',
 'LastRoundMoved/progresswrites haveactualreachedplacement; errorsbeforethewritecannotbeassumedmarked, errorsaftercannotbeassumedunmarked.',
 'Within same round, candidate selection mayrereadactualchoices/movedflag under WP40§5.2.3; stagewrapper swallowingdoesnotitselfreplay/rollbackindividualturn.',
 'ThisreferencepreservescurrentWP40completedturn/recandidatecontract withoutclaimingwholeengineexceptionrecovery.'
],['use','success','attack','battle_loop_complete','pbdebug'],'moveinnerlogonerr andturnmarker→candidatepicker→outerAttacklogonerr; nestingisnotasingletransaction.',open=['Full externalcallbacks/nativefaultoutcome remains outsidefiniteinnercontrolflow; do not inferhostrecovery.'])
row(659,[
 'Command,Attack,EOR eachpassoneblocktoPBDebug.logonerr; afterreturnedblocktheloopchecksdecision>0 inthatorder.',
 'Bare rescue inlogonerr catchesStandardErrordomain, callsdebuglog/backtrace/log/PrintException/flush, andhasnoexplicitreraisethemainerrorafterdiagnosticnormalreturn.',
 'Afterordinarydiagnosticreturns, callercontinuesdecisioncheck/nextstage; previouslyreachedgamewritesare notrestored.',
 'BattleAbortedException directException bypassesbareStandardErrorrescue andis caughtbyitsdedicatedpbStartBattlecorerescue.',
 'Diagnosticsitselfincludesformatting/logfile/print/input/clock/nativeconsumers; ifthosedependenciesfail, orerroroutsidewrappedblock/otherExceptiondomain, thisnormalreturncontractdoesnotapply.',
 'Noensure/globalstate rollback inthesewrappers; unknownexception/nativecleanup remainsunproved.'
],['battle_loop_complete','pbdebug','errors','abort_raise','start'],'stageyield→StandardErrorrescue diagnostics→normalreturn→decisioncheck/nextphase; directExceptionabortseparate.',open=['Actualdebugfile/nativeprint/input/clipboard/systemuptime operation and outerhostrescue/finalstate NOT_EXECUTED, notsourceabsenceproof.'])
row(660,[
 'SceneStandby disposesmapSpritesets conditionally thenCache.clear/frame_reset beforeyield; recreateSpritesets isafteryield onlyonreturnandcurrentSceneMap.',
 'BattleAnimation writesin_battletrue beforeviewport/audio/intro; normalpostyield popsFade,resumesrememberedaudio,clearsoverrides/resetencounters,performsfade,disposesviewport thenin_battlefalse.',
 'NeithercompleteStandby norAnimation suppliesensurearoundyield; arbitraryraisedfailure canbypasssome/alllaterrestoration.',
 'Thisdoesnotprovehostcrashorstatesafterouterrescue; onlyactualsourcepostyieldplacement/no universalrecoverypromise.'
],['battle_intro_outer','wild','trainer'],'standby/animationprewrite→yieldworldBattle→onlynormalreturnpostcleanup; arbitraryfailuresprefixremain.',open=['Nativegraphics/audio/map scene recreation and hostouterexceptionrecovery unexecuted; allintronativecallbacksnotapproved.'])
layout(661,'Catalog navigation/coverage inventory: 13G+11R+14E+3suffix rows=41; no new source behavior asserted by listing topic names. Exact catalog case meanings reviewed at their own later locators; existence/list/fulltext is not execution or total-semantic coverage.')
row(662,[
 'Fixed defaultmechanicsgeneration8; Battle initializer internalBattle/expGain/moneyGaintrue andcanLosefalse, subjecttoactualperbattleruleoverride.',
 'SettingsdefaultcapturedEXPtrue andspeedchangerecalculate true; explicitfalse variantskeepactualgates.',
 'WorldallbattleEvolutionCheckdefaulttrue andfaintedEvolutiondefaultallowed; callbackactualdecision/config/trainer/partner gates remainseparate.',
 'Defaultaffectioneffectsfalse; noaffectionbonus inferred justbecauseindividualhappiness/affectionfields exist.',
 'Rewardbase/growththreshold/move-list/Itemregistry/currencycap/statobjects are real consumerrequirements; defaultattributesalone donot supplymissingdata orproveeveryrecord exists.',
 'Pickup9+2window usesdefault18/11orderedtables/weights; authorsreplacementtables arefilteredfirstwithnodefaultbackfill.',
 'NoDemoeventinvocation orprobability/runtime/result proof follows fromtheseconfig/sourcefacts.'
],['b_settings','battlefull','rules','prepare','events','itemdata','growth_all'], 'defaultSettings + Battleinitializer→perbattleprepareattributeoverrides→actualend/growth/eventgates; dataandruntimepremises remainexplicit.',open=['Full concretecurrencycap/defaultcontent universe and every settingsconsumer notcertifiedbythissummary; finite KERNEL/CREdata joins only, wholeinterfaces IN_PROGRESS.'])
row(663,[
 'Experienceawardhasitsownparticipants/gain/config/data writes; itisnotaliasforEORphase orterminaljudgment.',
 'Judgment scansrealparties/faintcounts atitsactualcheckpoints; stage/transientdecision maydifferfromfinaloutcome.',
 'ResidualEOR andreplacement-entrychain aredistinctorderedsteps, includingearlypositive-decisionreturns.',
 'NormalterminalBattle EndOfBattlecleanup andworldafter_battle/on_end/resultvariable areseparatecallerlevels.',
 'A boolean, onephase return ortransientdecisiondoesnotbyitselfestablishallgrowth/cleanup/persistence/worldcallbacks completed.'
],['growth_all','eor_all','normal_end','after','events'],'growth/checkpoint/residual/replacement/normalEnd/worldafter separateactualcaller/writers; noonebitallcompletion.')
row(664,[
 'Eachtemporaryfieldclear isconditionedonreachingitsactualclearconsumer; earlyreturn/abort/exceptionsretainotherprefix.',
 'Namedclearlist doesnotimplicitlyclearallPokemonpersistentfields/auxiliarybattleflags/caches.',
 'Long-livedPlayer/party/Bagobject mutationsrequiretheiractualwritepoint andsave/reload separately; scopeofclearedruntimefieldsisbounded.'
],['normal_end','after','use','eor_all'],'actualclearconsumers notuniversalobjectreset; retainfinitefieldlists and exactOPENconsumerboundaries.')
row(665,[
 'HP/EXP/level/stat/move assignmentcanprecedesuccessfulmessages/sceneanimation; UIcompletion isnotprerequisiteforalreadyreachedmodelwrites.',
 'Full-slotlearningNo/BACKonlyskipsthatlearningreplacement; experience/statprefixnotrolledback.',
 'IfnestedSummarydynamicformgettercommits, cancellationdoesnotrollbackitsownprefix; Q3currentformalWP21/15/66 scope independentlycounterreviewed NO_REQUIREDrecommendation pendingroot.'
],['growth_all','pokemon_learn_stats','persistent_move'],'exp/statwrites→learningUI→canceloldslotpreserved withoutrollbackgrowth/formprefix; no globaltransaction.',open=['Q3rootfinalclassification pending; its original source facts remain valid independent of finalscope decision.'])
row(666,[
 'initialItems restoreisamutableperparty-slotrecord; actualpermanent itemloss/consumption/updatewriterscanchangeitbeforeEndOfBattlerestoration.',
 'Restoringreadsactualrecord atterminalwritepoint, notimmutable originalBattleentryhelditem.',
 'WorldPokemon storedhasAbility/Pickup/Honey andBattleractiveability/suppression/ignorefaint gatesaredifferentconsumers; sameabilityIDdoesnotsubstituteoneforother.'
],['normal_end','events','pokemon_ability_queries','pokemon_item_exact','item'],'battlepermanentitemwriters→initialItemsrecord→terminalPokemon.item=; worldstoredidentityqueries separatebattleactiveeffects.',open=['Every concreteitemhandler/Abilityfamilyglobalclosure remains exactseparate review; thisinvariantcannotcertifyallwritersbyitself.'])
layout(667,'Own/static-execution qualification: no reference game run, probability sampling, real save/map/input checks performed. Source exception control flow provides no host tolerance guarantee; not an executable behavior claim.')
layout(668,'Upstream responsibility navigation only; these titles do not themselves prove all actual cross-domain receivers. Exact consumers remain tracked in meaning atoms/interfaces/coverage-gaps.')
layout(669,'Downstream responsibility navigation only; family/mode/UX/Demo pointers cannot serve as complete receiver acceptance. Necessary consumers continue beyond this paragraph.')
layout(670,'Explicit unresolved-scope declaration: future families/runtime/stage exits remain and no whole battle-engine PASS follows. Preserve scope without fabricating a new source atom.')
layout(671,'Explicit U01 real-event/Demo availability qualification for worldPickup/Honey; no actual game invocation claimed. Fixed source behavior remains reviewable, not a material limit for readable code.')
layout(672,'Explicit unexecuted host tolerance/abort exception boundary; no finally contract added. Actual static failure-prefix meanings are separately authored C657–660.')
layout(673,'Pure historical/current-attestation plus no-run declaration: WP42-R01 and GR-013 reported CLOSED; preserve that snapshot qualification without asserting independently completed all historical review/dedup or reopening correct closed scopes. Whole global history remains OPEN.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_09g.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('explicit authored rows',len(rows),'children',sum(len(x.get('children',[])) for x in rows),'layout',sum('layout_reason'in x for x in rows))
