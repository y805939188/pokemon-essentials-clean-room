import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_09a.json').read_text());d=base['source_dictionary'];rows=[]
d['crec_growth']={'contribution':'crec-growth-selected-input.v1.json','receipt':'crec-growth-reception.v1.json','original_reader':'/root/creature_a_atomic_reception','reception':'CGR-R001/R006 all7children/9complete units/fullGrowthRegistry/allselectedcommon actualread; no whole122064B/18record or ownFULL credit'}
d['shadow_exp_heart']={'path':'Data/Scripts/014_Pokemon/003_Pokemon_ShadowPokemon.rb','range':[1,113],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete alias/setters/heart/max/stage/predicate/happiness definitions; later wholelife not granted'}
d['scene_growth']={'path':'Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb','complete_units':[[283,293],[298,308]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete EXPBar and LevelUp methods actually read'}
d['scene_forget']={'path':'Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb','range':[447,455],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete ForgetMove only; earlier Party/Fight units separate'}
d['summary_forget']={'path':'Data/Scripts/016_UI/006_UI_Summary.rb','complete_units':[[184,207],[209,215],[740,812],[814,844],[1232,1268],[1355,1366]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE actual complete forget init/end/draw/choose/screen methods; no wholeSummary/nativeUI'}
d['persistent_move']={'path':'Data/Scripts/014_Pokemon/004_Pokemon_Move.rb','range':[1,77],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ77 actually captured request1–170 clippedEOF, not170lines'}
d['move_pp_hm_data']={'path':'Data/Scripts/010_Data/002_PBS data/005_Move.rb','complete_units':[[3,39],[41,57],[66,73],[99,104]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE declaration/schema/constructor/getters/completehidden_move predicate actuallyread; notwholeMove451'}
d['pokemon_learn_stats']={'path':'Data/Scripts/014_Pokemon/001_Pokemon.rb','complete_units':[[90,97],[646,660],[1099,1127]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE exactconstants/completelearn_move/calc_stats actuallyread, CTFcalculation prerequisites finite separately'}
d['item_growth_handlers']={'path':'Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb','complete_units':[[53,56],[158,166],[1696,1700],[1706,1746]],'actual_reader':'/root/core_atomic_reception','reading':'OwnFULL1948 plus actual complete Exp/EVdispatch and LuckyEgg/MachoBrace/sixPower registrations reread; notallItemfamilies passed'}
d['stat_windows']={'path':'Data/Scripts/013_Items/001_Item_Utilities.rb','range':[206,221],'actual_reader':'/root/core_atomic_reception','reading':'OwnFULL917 plus complete TopRightWindow actual reread; nohostwindowexecution'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(561,[
 'GainExp caller has already reached EV before GainExpOne; its first maxExp check calc_stats thenreturns. Growth maximum_exp is threshold at configuredmax100, not an arbitrary currentlevel threshold.',
 'No FindBattler/Update/sceneRefresh occurs in this maximum branch; persistent EV/stat recalculation alone doesnot guarantee current battler attack/defense/speed refresh.',
 'Calc_stats can itself fail after earlierEV/partialstatwork; no rollback or forcedlaterrefresh. Otherconcretecaller could separatelyrefresh, not this branch promise.'
],['growth','crec_growth','pokemon_learn_stats','crec_form_join'],'EV→maxExpquery→persistentcalc→return beforeactivefind/update.')
row(562,[
 'Basecalculatedexp<=0 returns beforetrainer/scaling/+1; later clampedexpFinal-oldexp<=0returns aftermodifiers beforestat/expbarloop.',
 'Both branches retain previouslycommittedEV; they do not uniformlycallcalc_stats orBattlerUpdate, unlike the distinct alreadymaxExp branch.',
 'Earlieritemmodifier callbacks/messages can haveeffects beforelaterdelta0return; zeroexperience doesnot mean allstateunchanged.'
],['growth','crec_growth','item_growth_handlers'],'EV→orderedcalculator/clamp→qualifiedzero return, preserveprefix.')
row(563,[
 'NonShadow positiveactualdelta firstincrements global total_exp_gained; finds current same-side livebattler bypartyindex, then processes eachthresholdsegment.',
 'For eachsegment tempExp2=min(nextthreshold,expFinal), writesPokemon.exp beforeSceneEXPBar; rawsetter clearscachedlevel. Scene returns fornilBattler/equalrange elseanimatesdatabox and loopsUpdate whileanimating.',
 'Aftereachthreshold-crossing segment, it snapshotsoldstats, applies currentactivePokemon leveluphappiness, recalculatespersistentstats, Update(false), RefreshOne, then levelmessage/two statwindows.',
 'Each reached newlevel scans all GetMoveList items matchingthatlevel, notonlyone or highestlevel; learned/declinedmove control returns tothisperleveliteration.',
 'Statistics/exp/earlierlevels remain ifbar/input/message/nextlearning callbackfails; no ensure completion or rollback. Nativeframe/assetwait success isNOT_EXECUTED.'
],['growth','crec_growth','b_init','scene_growth','stat_windows','pokemon_learn_stats','crec_form_join'],'actualdeltaStats→segmentedpersistentexp→blockingbar→eachlevelstats/activecopy→presentation/learning.')
row(564,[
 'Afterwriting finalsegment, curLevel increment exceeding computednewLevel triggerspersistentcalc_stats, optionalBattlerUpdate(false)/RefreshOne, thenbreak.',
 'This finalrefresh occurs evenwithno gainedlevel and also aftermultilevel path; it isdistinct from earlierperlevelupdates and doesnotcollapse toonlyhighestlevelprocessing.'
],['growth','b_init','crec_growth','pokemon_learn_stats'],'finalexpsegment→persistentrecalc→qualifiedactivecopy/refresh→break.')
row(565,[
 'Leveluphappiness iscalled onlyvia currently found battler&pokemon; anoff-field partyindividual receivesno call fromthisgrowthpath.',
 'Update(false) itselfrecalculatesattachedPokemonstats then rereadslevel/HP/totalHP. Transformflagfalse additionallycopiesfiveordinarybattlecachedstats.',
 'Transformflagtrue leavesfive transformedcachedstats intact while rereadinglevel/HP/totalHP. FullChange false neverenters its types/ability refresh block.',
 'Activeidentity lookup uses living same-side Pokemonindex; a missing/faintedactor doesnot gainfullrefresh merelybecausepersistentpartyhasthisindex.'
],['growth','b_init','battlefull','pokemon_learn_stats','crec_form_join'],'currentlivebinding→happiness→Update(false) selectivecachecopy, Transform distinct.')
row(566,[
 'Off-fieldrecipient stillgets orderedpersistentexp/calcstats/levelmessages/MoveListlearning; foundbattlernil skipsactivecopy/RefreshOne.',
 'SceneEXPBar(nil,...)returns immediately withno databoxanimation; growthstillcalledit but doesnotcreate anactivebox or waitforone.',
 'No in-fieldhappiness call ismade withoutactivePokemonref. Genericotherhappiness/evolution paths areseparate, not universalnogain.'
],['growth','scene_growth','b_init','battlefull','crec_growth'],'persistentofffieldgrowth→nilSceneEXPearlyreturn→stillmessages/learning.')
row(567,[
 'BeforeShadowbranch actualdelta/cappedexpFinal/newleveldiagnostic arecalculated. PositiveShadowbranch only heartStage<=3 calls exp+=actualdelta thenstats+=delta; heart>3 returnswithoutthese writes.',
 'Loaded Shadow exp= tests realshadowpredicate and adds newvalue-current@exp to saved_exp, leaving current@exp/ordinarycachedlevel unchanged; nonShadow calls aliasedordinarysetter.',
 'Shadowbranch returns beforeordinary segmentedbar/level/statlearningloop. Noactuallevelgain ispromised fromtemporarystorage.',
 'heartStage derives0ifnotShadow else ceil(min(gauge,maxGauge)/(maxGauge/5.0)); validpositivemaxGauge/defaultregistereddata premise iskept. Malformedsaved_exp nil/type/gauge canerror withoutstatincrement; nofakeallinputtotality.'
],['growth','crec_growth','shadow_exp_heart'],'cappedactualdelta→heartgate→Shadowsetterredirect→stats→return, currentexp distinctfromsaved.')
row(568,[
 'Growth newlevel iscomputed fromclampedexpFinal; ifbelowcurLevel raisesdiagnostic before normalexp/statincrement/segmentedloop, with earlierEV/itemcallbackprefix retained.',
 'HP/stat recalculation forwards actualcompletecalc_stats and finiteCTF calcHP/Stat/IV/base/nature definitions; thislocalclause doesnotinvent anotherformula.',
 'No transactionalrollback follows diagnosticraise. Alreadymax branch hasits separate earliercalc route and isnot thiscontradictorylevelpath.'
],['growth','crec_growth','pokemon_learn_stats','crec_form_join'],'computednewlevel sanitygate→raise beforecommit, EVprefix retained.')
row(569,[
 'Every reached newlevel traverses fullmoveList, invokes LearnMove for allsamelevelitems; existingknownmove returnsbeforeask/write.',
 'When numMoves<MAX_MOVES4, Pokemon.learn_move constructs/pushesnewpersistentMove; learnmessageoccursbeforeactiveMoveappend andmovesetchangeformhook.',
 'Fullmoves path firstasksforget; acceptance opensSceneForget with singleton[Pokemon], index0 andnewmove, bypassingpartyselection.',
 'Summaryforgetscene usesonePokemon/page4 andnewMove, drawsMAX_MOVES+1 entries:fouroldslots plusnewcancelposition. Inputreturnsselectedoldindex or−1 forBACK/newposition.',
 'Negativechoice thenasksGiveUp:Yesends onlythisLearnMove, Norepeatschooser. InitialNoForgetalsoreturnsonlythisitem; outerGetMoveListcontinues.',
 'Earlierpersistentexp/EV/levels/statsprefix isnotrolledback by cancel/decline orasset/inputfailure. Exacthidden-move gate followsC0571.'
],['growth','persistent_move','pokemon_learn_stats','movebase','scene_forget','summary_forget'],'perlevelitems→alreadyknown/space/fullbranches→singletonchooser→permovecancel→outercontinue.')
row(570,[
 'Selectedoldslot firstgetsnew Pokemon::Move, then currentactiveBattler slotgetsMove.from_pokemon_move; messagesfollow thenmovesetchangeformhook.',
 'PokemonMove initializes registeredid/ppup0/pp=total_pp; totalPP=basePP+(basePP*ppup/5), so ppup0 newmovehasfreshbasePP. BattleMove retainsrealMove andcopiesPP throughfunctionclassfactory.',
 'ThisbattlelearnerdoesnotcallgenericmachineoldPP-preservebranch and addsnoegg/Shadoweligibilityguard ofanotherinterface. Invalidnewrecord/factorycallback canfailafterpriorwrites.',
 'Cancellationofonelearningitem doesnotterminateotherMoveListentries orreturna universalbooleancertificate toGrowth.'
],['growth','persistent_move','pokemon_learn_stats','movebase','move_pp_hm_data'],'newpersistentmove→functionclassBattleMove→messages→formhook, freshPP andpartialfactoryfailure.')
row(571,[
 'Summaryscreen loopsreturnedchoice: negative ornonewmove breaks; otherwiseDEBUGshortcircuitor!oldMove.hidden_move? permits, hiddenmove givesHMrefusal thenreselect.',
 'PokemonMove.hidden_move? delegatesGameDataMove; it scansregistereditems for is_HM? ANDassociatedmove==id. Namealoneorofficialgameconvention doesnotclassifyHM.',
 'BACK/newmoveposition returns−1; cancellationmakesnooldslotreplacement butdoesnotundoalreadywrittenexp/levels/stats/EV. Afterchooserreturns SceneEnd disposesitsresources onlyonreachednormalpath.',
 'Scenelevelupinvokestwo TopRightWindows sequentially, eachwaitsInputUSE. Nativegraphics/assets/inputexperience NOT_EXECUTED; staticwaitloopdoesnotprove useractuallywaited orhostfinished.'
],['summary_forget','scene_forget','persistent_move','move_pp_hm_data','itemdata','registry_finite','growth','scene_growth','stat_windows'],'realHMpredicate→chooserloop/return→actualreplacementconsumer, precommittedgrowth distinct.')
base['source_dictionary']=d;base['rows']=rows
assert all(k in d for r in rows for k in r['source_units']if isinstance(k,str))
(P/'manual_batch_09b.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children'])for x in rows)})
