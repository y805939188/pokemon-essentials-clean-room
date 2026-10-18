import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_09b.json').read_text());d=base['source_dictionary'];rows=[]
d['stages']={'path':'Data/Scripts/011_Battle/002_Battler/005_Battler_StatStages.rb','range':[1,387],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ previouslyactual'}
d['eor_weather_handlers']={'path':'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb','range':[2250,2330],'actual_reader':'/root/core_atomic_reception','reading':'OwnFULL3208 plus complete five default EORWeather registrations actuallyreread; finitefamily notallAbility'}
d['eor_heal_handlers']={'actual_reader':'/root/core_atomic_reception','complete_units':[{'path':'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb','range':[2336,2411]},{'path':'Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb','range':[1834,1859]}],'reading':'OwnFULLparent files and actual complete three ability/two item EORHealing registrations reread'}
d['eor_late_handlers']={'actual_reader':'/root/core_atomic_reception','complete_units':[{'path':'Data/Scripts/011_Battle/007_Other battle code/008_Battle_AbilityEffects.rb','range':[2417,2541]},{'path':'Data/Scripts/011_Battle/007_Other battle code/009_Battle_ItemEffects.rb','range':[1865,1888]}],'reading':'OwnFULLparentfiles and actual complete Effect/GainItem default registrations reread'}
d['weather_terrain_core']={'path':'Data/Scripts/011_Battle/001_Battle/001_Battle.rb','complete_units':[[701,775],[780,811]],'actual_reader':'/root/core_atomic_reception','reading':'OwnFULL867 plus complete effectiveWeather/start/default/primordial/terrain methods actualreread'}
d['hp_damage_heal']={'path':'Data/Scripts/011_Battle/002_Battler/003_Battler_ChangeSelf.rb','range':[5,99],'actual_reader':'/root/core_atomic_reception','reading':'OwnFULL328 plus complete HP/drain/effectdamage/faint reread'}
d['terrain_indirect_gate']={'path':'Data/Scripts/011_Battle/002_Battler/001_Battle_Battler.rb','complete_units':[[499,565],[596,600]],'actual_reader':'/root/core_atomic_reception','reading':'OwnFULL777 plus complete airborne/terrain/indirect/weatherdamage/effectiveWeather/canHeal gates reread'}
d['affection_level_receiver']={'path':'Data/Scripts/014_Pokemon/001_Pokemon.rb','range':[916,925],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete affection_level actualread916–926; wrapper Battler137 ownFULL777'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(572,[
 'EOR logs then writesendOfRoundtrue, notifiesScene, CalculatePriorityincremental and capturesone Priority(true) array.',
 'Speed-onlysort uses storedspeed andretainedtieorder, not TrickRoom reversal; unlike normalpriority it doesnot filterallfainted entries atconstruction. Eachhelper owns its laterliving/gates.',
 'Capturedarray holds actualactorobjects. Replacement reinitializes samefieldactor, so laterreads maysee newpersistentmember; cache isnot globallyfresh-sortedaftereachcallback.',
 'Innercallers that separatelycallPriority(true) gettheir own currentcacheorder. NormalfalseendOfRoundwrite isonlytail; earlierreturn/exceptioncanretaintrue.'
],['eor','priority','b_init','switching'],'EORflag→incrementalcache→singleobjectsequence→localrereads, no implicitreorder/tailensure.')
row(573,[
 'The subsequent ordinarytable fixes relativelocalstage order and explicit exitpoints, while forwarded local math/status domains remain independently scoped.',
 'This isnot a blanket guarantee everycallback returns or everylistedstage runs afterpositivewrite; actualstoplocations and priorprefixes govern.'
],['eor','battlerfull','b_change'],'scopedstage ordering→specificstop/check contracts, no forwardedwhole-domain approval.')
row(574,[],[],'',layout_reason='EOR sequence table header; every actual stage row has its own meaning children.')
row(575,[
 'Weather durationpositive decrementsfirst; atzero itmessagesoldweather, setsNone, currentliveweatherformchecks, then startsnonNone defaultweather. IfstillNone helperreturns, notwholeEOR.',
 'Currentweatheranimation/message precedes cachedmemberloop. Per member activeability weatherhandler(effectiveWeather) thenFaintifneeded, THENweatherdamage; notallabilitiesbeforeallweatherdamage.',
 'DrySkin sun/harshsun withindirectgate damages totalHP/8 andhealitemchecks; rain/heavyrain canHeal recovers/8. SolarPower sun/harshsun indirectdamages/8 andhealitemchecks.',
 'IceBody hailcanHeal recovers/16; RainDish rain/heavycanHeal recovers/16. IceFace hail&&restoreflag&&form1 callsChangeForm0 underits ownfaint/Transform/sameform gate.',
 'Weatherdamage skipsfaint, usescurrenteffectiveweather: sand/ice/shadowskyeligibility differs. Qualifiednominal totalHP/16 goesReduceHP thenhealitemcheck/Faint; cloudnine/airlock suppression andUmbrella Sun/Rain suppression are distinctfromstoredweather.',
 'Sand immunityincludes Ground/Rock/Steel, under/underground two-turn, activeOvercoat/SandForce/SandRush/SandVeil/Goggles. Hail usesIce/under-or-water/Overcoat/IceBody/SnowCloak/Goggles; ShadowSky excludesShadow andalluseindirectliving/MagicGuard.'
],['eor','eor_weather_handlers','weather_terrain_core','terrain_indirect_gate','hp_damage_heal','ability_item','b_change','shadow_exp_heart'],'duration/default/forms→memberactiveweathercallback→faint→memberweatherdamage, exactgatefamilies.',open=['Concrete weatherform and each invoked HP-item/faint-change callback joins remain exact later obligations; fullcallbacksource alone isnot allfamily semanticPASS.'])
row(576,[
 'FutureSight positionsscan inindexorder; missingposition/zero skips, othercounter decrements, positive returns; missing/faintedtarget thenreturns withotherauxfieldsretained.',
 'Atzero/live target, searchescurrentliving same-side source bysavedpartyindex; ifthatcurrentactoris target returns. Elseabsentsource retrieves savedsidepartyindex and requirespersistentable.',
 'Absentbutable source constructsnewBattler atsavedfieldindex. Its constructorInitEffects(false) canclear liveotheractors pointers tothatsavedindex BEFOREDummycopy; thisisnot a realentrantorpartyreplacement.',
 'Dummycopy takespersistentname/species/form/level/HP/types/fiveStats/status/Pokemonidentity, intentionally no ability/item/moves, setsdummytrue. A currentlyactive matchedsource isreusedwithoutthisconstructorcleanup.',
 'It snapshots userLastMoveFailed, writesfutureSighttrue, usesSimplemove(targetposition), thennormalreturn false/restoresfailure/Fainttarget/clearscounter-move-user-pastyaux. Errorbeforetailcanretainmode/failure/auxprefix.',
 'NestedSimplemove canreach normalmove growth/Judge paths. No target/no source/targetisuser earlyreturns atzero do not uniformlyclearaux; thiscorrect WP45 forwardedboundary ispreserved.'
],['eor','b_init','use','usagefull','battlerfull','battlefull','growth'],'positionexpiry→activeidentityornewdummycrosscleanup→actualSimpleuse→qualifiedrestore/clear, no fakefullentry.')
row(577,[
 'Wish scans positions indexorder; nonnilnonzero decrements, positive skips; expiredbeneficiary is currentbattleratposition andmustcanHeal.',
 'RecoverHP uses savedWishAmount oncurrentoccupant, message usesThisEx savedWishMakerpartyidentity. Missing/full/faint/HealBlock path canexpirewithouthealing, notbenefitreservedfororiginalrecipient.',
 'HPcommit precedes successmessage; helper doesnotuniversallyclearWishAmount/Maker auxiliaryfields orrequirecastercurrentlyactive.'
],['eor','battlefull','terrain_indirect_gate','hp_damage_heal'],'positioncount→currentoccupantheal→savedmakername, notoriginaloccupantbinding.')
row(578,[
 'SeaOfFire handles side0complete then1; nonzerocounterdecrementsbefore zerocheck. Exactzero skipsdamage; validnormalpositivecount premise retained ratherthannegativevalidatedduration.',
 'Stillpositive playssideanimation then cachedmemberloop same-side, indirectdamagequalified andnonFire, effectdamage nominaltotalHP/8.',
 'Later sideexpiration stage decrementsSeaOfFireagain ifpositive, so4→3/damage→2 andnextfullround2→1/damage→0 areordinarystaticsequence; a globalpositivecheck isnot insertedbetween.'
],['eor','terrain_indirect_gate','hp_damage_heal','battlerfull'],'sideindex loop/countbeforeharm→currentmembergates→latersecondcountdown.')
row(579,[
 'For eachcachedmember: Grassyterrainheal helper thenactiveabilityhealing thencurrentactiveitemhealing. Grassy requiresliving/currentGrassy/grounded-notsemiInvulnerable/canHeal andrecoversnominaltotalHP/16.',
 'Healer samplesonce<30 then allcurrentlivingallies withnonNONEstatus cure; notoneindependentdrawperally. Hydration nonNONE&&effectiveRain/HeavyRain cures. ShedSkin nonNONE draws<30tocure.',
 'Afterabilityreturn itemActive isqueriedagain, so abilitycanalteritem/status/liveness beforeitemdispatch. BlackSludge PoisoncanHeal→/16heal; nonPoisonindirect→/8effectdamage. LeftoverscanHeal→/16heal.',
 'EachsourceHPhealer/StatusCure hasactualpersistent/cache/message paths andcanfailafterpartialcommit. No allGrassypassthenallabilities orderorsharedability/itemeligibilitysnapshot.'
],['eor','eor_heal_handlers','terrain_indirect_gate','hp_damage_heal','ability_item','battlerfull','b_change'],'permemberterrain→abilitycure/heal→rereaditem→heal/harm; crossmember/allies actualstates.',open=['Default triggered HPheal/faint/status callback details outside these exact registrations remain separatelybound, not closed by this ordering row.'])
row(580,[
 'Affectionstatuscure stage occursafterability/itemheal andbeforepoisonburn. AFFECTION_EFFECTS&&internal gate; per memberliving/nonNONE/actualplayerowned/affection>=4/!mega.',
 'It skipsdraw<80, so validuniform0..99 draw80–99 cures20%; cure(false) commitsbeforeoldstatus-specificsupportmessage. Rawstepnamedaffectiondoesnotmakeanactiveabilitygate.',
 'DefaultfixedAffectionfalse disables thisstage withoutdisablingpriorheals orlaterpoisonburn. Ifenabled, curedstatuschangeslaterresidualqualification.',
 'For normalhappiness0..255, Pokemon affectioncase0/1/2/3/4 thresholds100/150/200/230/255 then5at255; currentaffection>=4 therefore230..255. Battler delegatesattachedPokemon else2, notdirectrawhappiness comparison.'
],['eor','b_settings','battlerfull','pokemon_growth_qual','ability_item','affection_level_receiver'],'config/internal→currentplayeraffectiongate→randomcure→laterresidualreread.')
row(581,[
 'Separatecompletepasses AquaRing thenIngrain thenLeechSeed, notpermemberinterleave. Firsttwo requireeffecttruthy&&canHeal, /16 recovery increasedfloor1.3 ifactiveBigRoot.',
 'LeechSeed requiresnonnegativesavedrecipientfieldindex, currentindirectdamage andcurrentnonnil/livingrecipient; recipientispositionoccupant, notnecessarilyoriginalcaster.',
 'TakeEffectDamage computesactualHP-loss andpassesit into recipientDrain. LiquidOoze checkedonvictimwithignorefaintedtrue flipsrecipienttoReduceHP anditemhealcheck; otherwisemessage/canHeal/BigRootfloor1.3→recovery.',
 'RecipientabilitiesOnDamageTaken iscalledinsidevictimdamageyield; victimthenitemHPheal/halfHPability/faint, recipientFaintafterreturn. Nestedreplacement/status/HPchanges canaffectlatersteps; staticnominalfraction isnotactualrestoredamount.'
],['eor','hp_damage_heal','terrain_indirect_gate','ability_item','battlerfull'],'effectgroup passes→actualvictimHPloss→drain/ooze→nestedrecipientreaction→victimpostdamage→recipientfaint.',open=['Concrete invoked halfHP/HP-item/faint callbacks remain individualreceivedorOPEN; no universalallreactionPASS.'])
row(582,[
 'Hyperbacklash checks actualinHyperMode ANDcurrentchoiceUseMove for eachcachedmember; no movedThisRound ornumHits-success guard isadded.',
 'NominaltotalHP/24 integerquotient goesReduceHP(false), whichrounds/clips/minimum1whenliving, thenmessage andFaintifzero; itdoesnotusegeneralTakeEffectDamage/indirectimmunity gate.',
 'Pokemon hyper_mode getter falseifheartgauge0 orHP0; Battler inHyperMode only rejectslocalfaint thenreturns attachedPokemon.hyper_mode. It addsno Shadow/wild/player-owner guard; qualifiednormalHypercreation isseparate. FullShadowlifecycle remainsindependentscope.'
],['eor','shadow_exp_heart','shadowother','battlerfull','hp_damage_heal'],'actualhyper/choicegate→directHPminimum1→message/faint, no fakeindirect/Shadow/owner gate.')
row(583,[
 'Poison completepass beforeburn. Poisonliving/statusPOISON; badpoisonstatusCount>0 firstincrementsToxic capped16 evenwhenPoisonHeal laterheals.',
 'ActivePoisonHeal canHeal recoversnominal/8, elseitsbranch doesnotpoisonharm. NonPoisonHealindirectdamage uses /8 regularor totalHP*Toxic/16 badpoison; ContinueStatuswrappedReduceHP→itemHPheal→halfHPability→Faint→halfHPflagfalse.',
 'Burn readsstatusBURN/indirecteligibility, uses generation>=7 /16 else/8 andactiveHeatproof round(dmg/2.0), thensamepostdamagechain.',
 'Earlierstatusheal/nestedcallbacks canchange laterpoison/burngates. Genericfaint/positivewrite doesnotadd anundeclaredwhole-EORstopaftereachmember.'
],['eor','terrain_indirect_gate','hp_damage_heal','b_settings','ability_item','battlerfull'],'poisoncounter/cureordamagepass→burnpass undercurrentstate, exactreactionprefix.')
row(584,[
 'Nightmare completepass first clearsNightmare when!asleep?, theneffecttruthy/indirectgate nominal/4 effectdamage.',
 'Curse separatepass requiresCursetruthy/indirectgate, nominal/4 effectdamage; eachTakeEffectDamage includesactualHPclip, messageyield, HPitem/halfability/faint andflagreset.',
 'Theirproducerfamilies areforwarded; localcurrentstate/helperorderdoesnotpromiseallNightmare/Curse creators ornativeanimationexecution.'
],['eor','hp_damage_heal','terrain_indirect_gate','battlerfull','ability_item'],'Nightmareclear/qualification→passdamage→Cursepass, no duplicateallfamilyapproval.')
row(585,[
 'Trappingliving/nonzerocount decrementsfirst, thenlooks up trappingMove name; exactzero givesfreemessageandreturnwithoutthisrounddamage.',
 'Stillnonzero choosesnamedanimation/defaultWrap BEFOREindirectgate; qualifiedgen>=6 /8 else/16. Actualsourceactor activeBindingBand changesfractionto/6 else/8.',
 'ThenDamageAnimation/effectdamage/reactionprefix. Invalidsourceindex ornonnilabsentactor canraise aftercounter/animation; noarbitrary-indexrecovery guarantee. Ordinaryleave/Shiftpointerrelations remainWP41correct.'
],['eor','switch_effects_full','hp_damage_heal','terrain_indirect_gate','ability_item','battlerfull','b_settings'],'decrement/name→zeroexit oranimation→indirect/sourceitem→damage, retaininvalidindexpartialprefix.')
row(586,[
 'Octolock stage cachedmembersrequires!faint andsavedsourceindex>=0, butcentral CanLower/Lower callsreceive NOsource; Def thenSpDef separatelyqueried/committed.',
 'Then ItemOnStatDropped. No generalmultistatMirrorArmorprecheck orimplicitMoldBreakerreset isinserted. CurrentmodecanthereforeaffectContrary/protectionsemantics underactualStagecode.',
 'ExistingECB001 completecounteracceptsrealtracebutcurrentWP40/42/44alreadycomposeit; thisrowdoesnotcreate anotherrequired/optional orforcepairednewfixture.'
],['eor','stages','ability_item','battlerfull'],'storednonnegative marker→sourcefreecentralperstat→itemreaction, retainexistingNO_REQUIREDscope.')
base['source_dictionary']=d;base['rows']=rows
assert all(k in d for r in rows for k in r['source_units']if isinstance(k,str))
(P/'manual_batch_09c.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children'])for x in rows),'layout':sum('layout_reason'in x for x in rows)})
