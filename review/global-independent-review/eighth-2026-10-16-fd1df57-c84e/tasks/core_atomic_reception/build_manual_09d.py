import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_09c.json').read_text());d=base['source_dictionary'];rows=[]
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(587,[
 'Battlereffectexpiry invokes Taunt→Encore→Disable→MagnetRise→Telekinesis→HealBlock→Embargo→Yawn→PerishSong, eachusingcachedpriority.',
 'Genericcountdown skipsfainted/exactzero, decrementsotherwise andyieldsonexactnewzero; normalpositiveinput qualification retained, notnegativeforever contract.',
 'Encore findsactualencoredslot; existingmove decrements thenzero-orPP0ends; missingmove clearsbothcountandEncoreMove. Disableexpiry clearsDisableMove; otherauxfieldsnotuniversallycleared.',
 'Embargoexpiry messages thenchecks currentterrainitem; Yawnexpiry rechecks dedicatedCanSleepYawn/loadedclause beforeSleep. Perishrecordsactualsavedsource andformalFaint aspreviousC0549, notuniformdraw.'
],['eor','battlerfull','ability_item','clauses','b_init'],'orderedper-effectpasses→specificauxexpiry/requery→Perishsavedsourcecheckpoint.',open=['Concrete initialproducers of eachcounter and allterrainseed/statusimmunitycallbacks remain laterexactbindings, not supplied by nameenumeration.'])
row(588,[
 'Afterallpersonalexpiry EOR testsdecision>0; iftruecallsGainExp thenunconditionallyreturns fromthisstagepath.',
 'Side/field/terrainexpiry, lateabilities/items, replacements andtailareunreached; endOfRoundtrue canpersist. EarlierFaint/HP/choice/residualwrites are notundone, eveniflatergrowthitselfchangesstate orerrors.'
],['eor','growth','b_change'],'postpersonalpositivegate→growth→return, no implicit tail/rollback.')
row(589,[
 'Side0 entireexpirygroup beforeSide1; Reflect→LightScreen→Safeguard→Mist→Tailwind→LuckyChant→Rainbow→SeaOfFire→Swamp→AuroraVeil.',
 'Eachgenerichelper ignores<=0; positivecount−1andnewzero message. SeaOfFirehere isseconddecrement afterearlierharmstage, notanotherharmcall.',
 'Teammessage formatting occurs asargument beforehelper, and canfailbeforeitscountwrite; priorcompletecounterwritesremain. Sourcebody doesnotpromiseallfieldsunchangedifdurationnonpositive.'
],['eor','battlerfull','battlefull'],'sidegrouporder→eagerteamnamearguments→positivecountdown→expiryfeedback.')
row(590,[
 'Fieldexpirygroup orderTrickRoom→Gravity→WaterSportField→MudSportField→WonderRoom→MagicRoom; eachpositiveonly decrement andzero message.',
 'MagicRoomzero aftermessage getsfreshPriority(true) andchecks eachterrainstatitem; thisinnerorder read can differ fromEORinitialcapturedarray.',
 'Noautomaticworldallitemrefresh orspeedrecalc attachedtoeveryfieldexpiry; actualconsumers rereadfieldstate later.'
],['eor','priority','ability_item','battlefull'],'fixedfieldcountdowns→MagicRoomspecialfresh-orderitemcheck.',open=['ConcreteTerrainStatBoost handlers/consumption/defaultseedrecords still require their laterboundedjoin.'])
row(591,[
 'Terrainpositive durationdecrements; onlycurrentterrain!=None&&duration0 expires, displaysoldterrain, writesNone andcurrentliveabilityterrainnotifications.',
 'NonNonedefault restartsTerrain(nil,default,false), whichitselfnotifiesabilitiesanditems; outerexpirythennotifiesabilitiesanditemsagain. IfcurrentNone remains helperreturns, notwholeEOR.',
 'Continuationanimation/message occursafterdefaultrestore; earlierGrassyhealing alreadyhappened beforethisexpiry. Directterrainremoval doesnotautomaticallyrunthisdefaultrestoreduplicatenotificationroute.'
],['eor','weather_terrain_core','ability_item','battlefull'],'duration→clear/notify→defaultStartnotify→extraouterNotify→continuation, correctduplicateboundary.',open=['IndividualonTerrainChange/seed handleroutcomes areseparate actualdefaultfamilies, not allreceived bydispatchname.'])
row(592,[
 'Eachcachedmember selfeffectshelper firstskipsfaint, thenHypercalm10% draw, thenUproarcountdown/message, thenSlowStartcountdown/message.',
 'Immediatelyafterthatmemberhelperreturn, callerrechecksabilityActive→EndRoundEffect, itemActive→EndRoundEffect, abilityActiveagain→EndRoundGainItem. Currentstate maychangebetweenallfour.',
 'BadDreams scanscurrentlivingnearopponents asleep, indirectgate, /8effectdamage. Moody buildspermittedup/down statsets, defaultgen8excludesAcc/Eva, samplesup2/removessamefromdown/down1, thenstatrestoreifdownlist anditemstatdrop.',
 'SpeedBoost requiresturnCount>0, choice!=Run andCanRaiseSpeed, thenabilityraise1; incomingmidroundturnCount0normallyskips.',
 'FlameOrb CanBurn(self,false) thenBurn(nil,...); ToxicOrb CanPoison(self,false) thenbadPoison(nil,...,true). StickyBarb indirecteligible /8effectdamage. These occurafterearliernormalpoison/burnstage, so newstatusdoesnotretroactivelyrunthatpassedstage.',
 'BallFetch nohelditem&&firstBallnonnil:currentitemassign, initialrestoreifmissing, firstBallnil, message, heldtriggercheck.',
 'Harvest nohelditem&&berryrecycle: effectiveSun/HarshSun skipsdraw, otherwise<50; assignsitem, clearsrecycle, initialrestoreifmissing, message/heldtrigger.',
 'Pickup nohelditem choosescurrentlivingothermaxpositivePickupUse, transfersfounditem, clearsdonorPickupfields/recycleifmatching; wildandmissingrecipientinitialanddonorinitialmatches additionallytransfersinitialrestoreidentity; thenmessage/heldtrigger.',
 'Latecallbacks canreplace/faint/changehelditem orrestoreledger beforelaterrechecks. No commoneligibilitysnapshot or atomic acquire-and-trigger/rollback guarantee.'
],['eor','eor_late_handlers','ability_item','stages','stat_full','shadow_exp_heart','itemdata','b_init','battlerfull'],'permembercalm/countdown→abilityeffect→itemeffect→abilityacquire withcurrentrechecks.',open=['RemainingexactHeldItemTrigger/HPhealing/statrestore/OnStatLoss nested defaultfamilies retain individuallyscoped obligations; allEORregistrationsread doesnotdeclareallItem/Ability semanticPASS.'])
row(593,[
 'Afteralllatepermemberreactions GainExp runs; onlyafteritreturns doesdecision>0causewholeEORreturn.',
 'Formchecks/replacements/movement/continual/tailskippedonthispositivepath. Ifgrowthfails earlierdelta/HP/item writesremain andcallerdiagnostic mayhandle; noimplicitendflagfalse.'
],['eor','growth','pbdebug'],'lateeffects→growth→secondpositivecheck→return orcontinue.')
row(594,[
 'EORcachedobjects eachCheckForm(true); calledmethod ownsits living/Transform/species/condition gates, no allmembersuniformformchange.',
 'Itfollowsgrowth beforeEORSwitch; a changedpersistentform canaffectlaterreplacement/worldconsumers, not universalfullattribute/abilityrefresh bytheloopalone.'
],['eor','b_change','battlerfull','crec_form_join'],'cachedactor→qualifiedspeciesformcallback→laterreplacement.',open=['Allconcrete EORform species conditions/producers and associatedrawrecords notyet individuallybound; sourceFULL doesnotclose this callbackfamily.'])
row(595,[
 'EORSwitch normalentryfirstdecision/favorDrawgate thenJudge; ifstillunresolved ititeratescurrentfaintslots withlegalbench, bindssequentiallyandgroupsEntry per scan.',
 'Newentryhazardfaint cannecessitatenextscan. Wildowneddeclinenext invokes Run(duringBattle=true), with its actual gates/counter/returnpolicy.',
 'A successfulnestedrun mayleavefurther same-scanslotwork; onlyEORcaller followingpositivecheck guaranteeslatermovement/tailareunreached inqualifiednormalnonlethalvector.'
],['eor','switching','running','priority','ai_finite'],'Judge→currentfaintreplacementscan→groupEntry/rescan→actualcallerpositiveconsumer.')
row(596,[
 'AfterEORSwitch returns, decision>0directlyreturnsEOR; noextraGainExp inthisthirdexitbranch.',
 'Automaticshift/continual/currentliveresets/side-fieldtail/endflagfalse remainunreached, while earlierswitchingandhazardprefixes survive.'
],['eor','switching'],'replacementreturn→thirdpositivecheck→skipremainingtail.')
row(597,[
 'ReacheddistantShift handlesnon1v1; allcandidatepairscollectedfrompreadjustmentlivingdistribution side0then1, withnear-foundglobalcollectionbreak.',
 'Executionusesfixedplan: totalpairs>1 skips2-sizedsourcepairs, not3-sized; actualSwapstillvalidatesendpoints/owner.',
 'No manualShiftBeginTurn/CancelMoves/movedstamp andno fullEntry chain. Exactfinitelayoutcontrols separatelydecomposedC0612–14.'
],['eor','swap','battlefull','use'],'preplan→fixedorderedexecution→Swapremaps, notmanualaction/fullentry.')
row(598,[
 'Afterautomaticshift cachedpriorityobjects eachContinualAbilityChecks withdefaultfalse; objectindex/state mayhavechangedbypriorSwap.',
 'Actualroutine triesTrace under its own gateandendsprimordialweather; nofullallSwitchIn dispatch for everymember orautomaticallability activationpromise.'
],['eor','ability_item','abilityeffects','weather_terrain_core','b_change'],'postshiftcachedobjects→qualifiedcontinualTrace/primordialchecks.',open=['Trace-specificrawcopy eligibility/nestedOnSwitchIn family outcomes retain exactlatercallbacks; genericcallee name doesnotcloseallabilities.'])
row(599,[
 'TailreachedcurrentallBattlers livingcensus isfresh, distinctfrominitialcachedsequence; per-member currenteffects/flags/history reset exactlyasC0607–09.',
 'Fainted/nilentries areexcluded, noimplicitmembershipfromearlieralive. EarlywholeEORreturns skipthistail withoutundoingearlierInit/Faint clearing.'
],['eor','battlefull','b_init','b_change'],'freshlivingcensus→boundedtailwrites; earlierfaint/initclears separate.')
row(600,[
 'Aftermembertail, side0/1 guard/round/echo state resets; unusedEchoedVoice firstclearcounter thenusedflagfalse.',
 'FieldIonDeluge/FusionBolt/FusionFlarefalse, FairyLockpositiveonly−1; negative/zero untouched. Thesewritesarecurrenttailonly, not allfielddurationexpiry.'
],['eor','field'],'membertail→bothsidetail→fieldtail, exactboundedwrites.')
row(601,[
 'OnlynormalreachedmastertailwritesendOfRoundfalse; thenloadedclausewrappermaycomparecountsundersuddendeath/decision0.',
 'OnlyafterwholeEORwrapperreturns doesBattleLoop testpositive andeitherbreaknormalend orincrementturnCount. Earlyreturndoesnotmeanendflagfalse.'
],['eor','clauses','start_end_full'],'masterfalse→wrapperresult→mainlooppositivecheck/increment.')
row(602,[
 'HP0 write, formalFaint callback, Judge resultassignment andouterexplicitexit aredifferent reachedoperations; none universallysubstitutestheothers.',
 'ResidualFaintwithoutresultwriter cancontinueotherlocalstagesuntilEORSwitchJudge; nestedcallbackpositivecanbeconsumedbyanearlierexplicitcheckpoint.',
 'No globalcheckaftereverymember/residual andno reversalofalreadycommittedHP/status/item/choicework onlaterreturn.'
],['eor','b_change','hp_damage_heal','start_end_full','switching'],'HP/faint/result/checkpoint distincteventorder, no inventedglobalinterrupt/rollback.')
row(603,[
 'Genericbattlercountdown skipsfainted/exactzero, decrementelse; normalpositivepremise doesnotverifynegativepermanentvalues.',
 'Taunt/Disable/MagnetRise/Telekinesis/HealBlock/Embargo/Yawn sharethishelper butownexpirycallbacks/auxwritesdiffer.',
 'Encoreknownmove decrements andendsatcount0 orPP0, preservingEncoreMove onthatbranch; unknownmove count0 ANDEncoreMovenil.',
 'Disableexpiry clearsDisableMove; Magnet/Tele/HealBlockonlyspecifiedmessages; Embargorechecksitem/YawnCanSleeprequery. Do notunifyallauxcleanup fromsharedcounterhelper.'
],['eor','battlerfull','ability_item','clauses'],'qualifiedcountdown→branchspecificauxclear/refresh, notallpayloadreset.')
row(604,[
 'Perishliving/nonzerocount decrements/messages; zero recordsstoredsource thenReduceHP(allcurrentHP); everyprocessedmemberthenHPitem/Faint.',
 'Collectedsourcesnonempty/alloneside causesCheckpoint(savedfirstactor), notordinarydefaultdraw. EORstage14consumespositive byGainExp/return.',
 'FormalFaintalreadyInitEffects(false), statusclear/choiceclear/etc; stage14skippedtaildoesnotrestorethem. Reflectduration/endflagcanremainasbeforeexpiry.',
 'Uproar/SlowStartcountdown occurslater selfeffects; faintskipallselfeffects, otherwiseHyper10%calm beforeUproar thenSlowStart. Noresetbasedonlyonnatural-language roundend.'
],['eor','clauses','hp_damage_heal','b_init','b_change','shadow_exp_heart'],'savedPerishsource→formalFaintprefix→positiveearlyreturn, distinctlatercalm/countdowns.')
row(605,[
 'SeaOfFirevalid4→early3/harm→sideexpiry2, nextfullround2→1/harm→0; ifearlyreturnbeforelaterexpiry thiscompletepairdoesnotapply.',
 'Weatherduration1 expiresbeforepermembercontinuationdamage; Grassyterrain1 healstageoccursbeforeterrainexpiry.',
 'Naturaldefaultterrainrestore includesStartnotifications plusouterrepeatability/itemnotifications; directremovepathnotautomaticallysame. Preserveactualcorrectlocaldifferencesratherthanharmonizingtoofficialrules.'
],['eor','weather_terrain_core','ability_item'],'qualifiedfullEORtemporalcontrols retain actualnonuniformlocalordering.')
row(606,[
 'The followingboundedmembertailwrites require reachedtail ANDcurrentlivingmembership; earliercachedpresencealoneisnot sufficient. Noensurecompletion isadded.'
],['eor','battlefull'],'currentalivecensusandtailreachability→eachlistedwrite.')
row(607,[
 'Atqualifiedtail BanefulBunker protectioneffect becomesfalse.',
 'Electrify temporarytypeoverride flag becomesfalse.',
 'Endure survivalflag becomesfalse.',
 'Flinch actionpreventionflag becomesfalse.',
 'FocusPunch charge-readinessflag becomesfalse.',
 'HelpingHand damageboostflag becomesfalse.',
 'KingsShield protectionflag becomesfalse.',
 'MagicBounce roundreflection-usedflag becomesfalse.',
 'MagicCoat temporaryreflectionflag becomesfalse.',
 'Obstruct protectionflag becomesfalse.',
 'Powder flag becomesfalse.',
 'Prankster savedaction-originflag becomesfalse.',
 'PriorityAbility savedpriority-sourceflag becomesfalse.',
 'PriorityItem savedpriority-sourceflag becomesfalse.',
 'Protect flag becomesfalse.',
 'RagePowder redirectionflag becomesfalse.',
 'Roost temporarytypingflag becomesfalse.',
 'SpikyShield protectionflag becomesfalse.',
 'Counter damagevalue becomes−1 and separatelyCounterTarget pointer−1.',
 'MirrorCoat damagevalue becomes−1 and separatelyMirrorCoatTarget pointer−1.',
 'FirstPledge savedidentity becomesnil.',
 'FollowMe redirectioncounter becomes0.',
 'Snatch orderingcounter becomes0.',
 'Spotlight redirectioncounter becomes0.'
],['eor','battlerfull','b_init','checksfull','priority'],'explicitcurrentlive-tail perfieldwrites, distinct from sourcegenerators or earlierfaintclears.',open=['Eachremaining concrete move/effect producer and after-tail consumer joins are independentlyrequired; tailwrite proof isnot wholeGuard/redirect/typing/multimove-family approval.'])
row(608,[
 'Charge positivecounter decrements1; zero/negative untouched bythisEORtail (EndTurn hasdistinct exact1clear).',
 'HyperBeam positivecounter decrements1, notuniversallycancelledbyCancelMoves.',
 'LaserFocus positivecounter decrements1.',
 'LockOn positivecounter decrements1; onlywhennewzero LockOnPos becomes−1, retainingpointerotherwise.',
 'ThroatChop positivecounter decrements1; nonpositivevalues untouched. These are actualfieldnames/countergates, not a sharedallstatusdurationexpiry.'
],['eor','use','battlerfull','b_init'],'specificpositivecounters→−1 andLockOntargetclearonlyzero, distinct EndTurn/Init lifetimes.')
row(609,[
 'lastHPLost becomes0.',
 'lastHPLostFromFoe separately becomes0.',
 'droppedBelowHalfHP becomesfalse.',
 'statsDropped becomesfalse.',
 'tookMoveDamageThisRound becomesfalse.',
 'tookDamageThisRound becomesfalse.',
 'tookPhysicalHit becomesfalse.',
 'statsRaisedThisRound becomesfalse.',
 'statsLoweredThisRound becomesfalse.',
 'canRestoreIceFace becomesfalse.',
 'lastRoundMoveFailed copies current lastMoveFailed withoutclearingcurrentfailure.',
 'lastAttacker array cleared in place.',
 'lastFoeAttacker array separately cleared in place.'
],['eor','battlerfull','hp_damage_heal','b_init','use','eor_weather_handlers'],'currentalive-tail damage/stat/history flags andinplaceattackerreset, failurecopydistinctfromclear.',open=['Specificremaining allfield producer/consumer effectfamily joins retainOPEN; existingStompingTantrum finitefailure consumers alreadybound do notcloseallhistoryuses.'])
row(610,[
 'Eachside CraftyShield becomesfalse.',
 'Eachside MatBlock becomesfalse.',
 'Eachside QuickGuard becomesfalse.',
 'Eachside WideGuard becomesfalse.',
 'Eachside Round becomesfalse.',
 'If EchoedVoiceUsed false, EchoedVoiceCounter becomes0; then EchoedVoiceUsed false unconditionally.',
 'Field IonDeluge becomesfalse.',
 'Field FusionBolt becomesfalse.',
 'Field FusionFlare becomesfalse.',
 'Field FairyLock positivecounter decrements1; zero/negative unchanged.'
],['eor','battlefull','switch_effects_full'],'bothsideguard/round/echo thenfieldtail currentwrites, preserve EchoUsed testbeforeclear.',open=['Remaining exactGuard/Round/Echo/Fusion producers and next-use readers areseparatebindings, notimplicitlyclosed by boundedtail.'])
row(611,[
 'The listedtailisbounded; itdoesnotwriteeveryeffect/status/result/runtimeflag false orzero.',
 'NextCommandPhase ClearChoice and normalInitEffects/Baton/fainting dootherqualifiedclears; earlyEORreturn cannotmanufacturetailworkmerelybecausecalledroundend.'
],['eor','command','b_init','b_change'],'specifictailversusotherlifetimeresets, no catchallcleanup.')
row(612,[
 'Distantshift onlyifreachedstageand!singleBattle?; side0then1, skipownside1. Candidatecollection usescurrentliving actors beforeanyswapexecutes.',
 'For eachsize2/3 side testsifanycurrentlivingownactornearanycurrentlivingfoe; findinganynear breaksentiresidecollectionloop, preservingalreadycollectedearlierpairs.',
 'Ifnonear, eachownlivingactor size2destination[2,3,0,1][index], size3center2/3; onlycurrent source/destinationownermatchedenqueues.',
 'No additionaldestinationcurrentlyliving requirement isadded; lowerSwap requiresnonnilestablishedobjects, notbothalive. Unsupportedlarger-than3logic isnotcertified.'
],['eor','battlefull','swap','battlerfull'],'precurrentlivingnearquery→globalcollectionbreakorownerqualifiedfixedplan.')
row(613,[
 'Aftercollection, iteratefixedpairplan inorder; skipa pair iff itssourcesideSize2 ANDtotalplanlength>1, independentofhowmanypriorpairsexecuted.',
 'Size3pairshavenothatgate; actualSwapmissing/opposite/differentownerfalse skipsitsmessage andcontinueslaterpairs.',
 'Normalsuccessshowsmove-acrossorcenter message. Itdoesnotrecompute-near tocancelremainingplannedpair, notmanualShiftcost andnotfullEntry; pointersemantics remainexactWP41ten/exceptionlist.',
 'Swapscene failure canleaveobjects/indices/choicesalreadyswapped beforepointerremap/message; no plan-leveltransactionrollback.'
],['eor','swap','battlefull','use'],'fixedplanfilter→actualSwap→conditionalmessage, no postfirst-nearreplanning.')
row(614,[
 'Valid3v3 sixactorsestablished/singleownereachside/only0and1alive/nootherablebench haspre-nearfalse andsameownercenters, collects0↔2and1↔3; bothsize3execute, liveends2/3.',
 'Valid3v2 fiveactorsestablished/singleowner/only0and1alive likewisecollectsbothpairs, buttotal2 skipssize2side1pair, so liveends2/1.',
 'Valid3v3 post-start threeplayerowners mapping0/2/4 separate, foesingleowner, only0/1alive: own0→2wrongownerrefusesenqueue, foe1→3enqueuesalone; liveends0/3.',
 'If originaldistributionalreadyhasnearown/foepair, globalnearbreakcanleaveplanempty andnothingmoves. These are conditionalstaticvectors withsourcevalidcurrentstates, notnativebattleobservations.'
],['eor','swap','battlefull','battlerfull','owners','teams'],'finiteordinaryowner/layoutcontrols through preplan+sizefilter, noactualexecution.')
base['source_dictionary']=d;base['rows']=rows
assert all(k in d for r in rows for k in r['source_units']if isinstance(k,str))
(P/'manual_batch_09d.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children'])for x in rows),'open_rows':sum(bool(x.get('open'))for x in rows)})
