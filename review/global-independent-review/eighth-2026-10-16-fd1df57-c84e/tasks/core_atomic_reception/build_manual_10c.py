import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_10b.json').read_text());d=base['source_dictionary'];rows=[]
d['misc_full']={'path':'Data/Scripts/011_Battle/003_Move/005_MoveEffects_Misc.rb','range':[1,693],'actual_reader':'/root/core_atomic_reception','reading':'OwnFULL693 nowactualread1–226/227–363/348–381/375–520/521–693; oldpartialcreditkeptseparate, notallclasssemanticsPASS'}
def partial(k,path,ranges):d[k]={'path':path,'complete_units':ranges,'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE actual complete named classes/methods including closingend; no wholefilegrant'}
partial('gravity_producer','Data/Scripts/011_Battle/003_Move/007_MoveEffects_BattlerOther.rb',[[1299,1333]])
partial('wonderroom_producer','Data/Scripts/011_Battle/003_Move/006_MoveEffects_BattlerStats.rb',[[1942,1957]])
partial('magicroom_producer','Data/Scripts/011_Battle/003_Move/011_MoveEffects_Items.rb',[[274,289]])
partial('sport_ion_producers','Data/Scripts/011_Battle/003_Move/008_MoveEffects_MoveAttributes.rb',[[696,718],[723,745],[1604,1620]])
partial('fusion_producers','Data/Scripts/011_Battle/003_Move/012_MoveEffects_ChangeMoveEffect.rb',[[381,401],[406,426]])
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
def layout(n,why):rows.append(dict(number=n,layout_reason=why))
layout(711,'Fieldrecord tableheading; 13actualrecordpayloadsareinC712–722 withmulti-recordrows separatelysplit. Noheadingfullcallbackcredit.')
row(712,[
 'Gravityinitialfieldcounter0; movefailsifalready>0withoutrefresh.',
 'PassedEffectGeneralsetsGravity5 beforeannouncement andper-battleradjustment.',
 'PositiveGravitygroundsairbornequery beforeFlying/Levitate/Balloon/MagnetRise/Telekinesis reasons.',
 'Accuracycalculationmultiplier *=5/3.0 whilepositive; notguaranteedabsolutehit.',
 'CanChooseMovecheckspositiveGravity+actualmove.unusableInGravity? atcommand/actioneligibility; falseblockswithappropriatepaused/nonpausedmessage.',
 'Establishmentallcurrentnonfaintedbattlers checksTwoTurnfunctioncodesInSky/InSkyParalyzeTarget/InSkyTargetCannotAct only.',
 'MatchedThreeTwoturnstatesclearTwoTurnAttacknil; ifnotmovedThisRound ClearChoice direct, notuniversalrefund/replay.',
 'IfanyofMagnetRisepositive/Telekinesispositive/SkyDrop>=0, clearsMagnetRise0/Telekinesis0/SkyDrop−1 andqueuesfeedback.',
 'NoothersemiInvulnerabletype e.gUnderground/Underwater/RemoveProtections iscancelledbythatThreecodecheck.',
 'ReachedEndFieldEffectspositivecounter decrements1andmessagesat0; earlyEORexitcanpreventthistick.'
],['activefield_full','gravity_producer','battlerfull','checksfull','calculations','command','eor_all','movebase'],'Gravityproducer5→ground/accuracy/eligibilityqueries→specificsky-choice/levitationcleanup→laterfieldcountdown.',failure='Gravity5beforemessage; failureinmessage/per-battlerclearleavesnewfieldandprefixofstatechanges, notall-battleratomicestablishment.')
row(713,[
 'TrickRoominitialcounter0; movewhen<=0 sets5.',
 'Movealreadypositive sets0ratherthanrefreshing5; bothbranchescounterwritebeforemessage.',
 'PriorityfullcalccapturespositiveTrickRoom; partialrecalcdetectschangedpositivityandrequestsreordering.',
 'Within equalmovepriority/equalbracket, TrickRoomsortslowerspeedfirst; movepriority/subprioritytiersnotreversed.',
 'Tie-breakerretainedfor equalspeed, notdeterministicalltiesbyslot.',
 'Reachedfieldcountdownreducespositive; 0endmessage, notnewstack/restoration.',
 'Actualrecalctiming remainsWP40/WP41 caller/config, notimplicitrecalconceverycounterwrite.'
],['activefield_full','switch_effects_full','priority','attack','eor_all'],'TrickRoomtoggle→prioritysnapshot/recalc→withinbracketspeedreverse→latecountdown; timingactualcallersseparate.')
row(714,[
 'WonderRoominitial0; movewhenabsentsets5.',
 'Movewhenpositivecancels0, doesnotrefresh.',
 'Battler.defense getterreturnsrawspdef whilepositive.',
 'Battler.spdef getterreturnsrawdefense whilepositive.',
 'Underlying@defense/@spdefandPokemonpersistentstatsnotexchangedbythesetoggle/gettermethods.',
 'DamageDefenseStats stillpairsphysicalwithDEFENSEstage andspecialwithSPECIAL_DEFENSEstage; stagesnotexchangedbyWonderRoom.',
 'Naturalpositivecountdownthen0endmessage; rawstatsdonotneedrestorewritesbecausereadselectionchanges.'
],['activefield_full','wonderroom_producer','battlerfull','calculations','eor_all'],'fieldtoggle→read-timebaseDefense/SpDefswap +originalnamedstages→fieldexpiry; notpersistentstatrewrite.')
row(715,[
 'MagicRoominitial0; movewhenabsentsets5.',
 'Movewhenpositivecancels0andmessages, notrefresh.',
 'Battler.itemActive returnsfalsewhileMagicRoompositivebeforeCorrosiveGas/Klutz checks; helditemIDnotdeletedbyquery.',
 'NaturalFieldCountdown whenpositive decrements; at0 sendsendmessage thenpbPriority(true).eachItemTerrainStatBoostCheck.',
 'ThatitemrecheckstilltestsitemActive/terrainhandler eligibility, notautomaticseedconsumptionforall.',
 'Directtogglecancelcompleteclassdoesnotexplicitlyperformthatnaturalexpiryextraitemloop.',
 'Otherlatercommoncallbacksmaystillcheckitems; absenceofthisexplicitloopnotproofallitemcallbacksneverrun.',
 'Explicitconsumption/usingberryexceptionsaredifferentMove/Itemfamilycontracts, noterasingphysicalitemjustbecauseMagicRoompositive.'
],['activefield_full','magicroom_producer','battlerfull','ability_item','eor_all','priority'],'MagicRoom5→activeitemfalse(noidentitydelete)→natural0message+extraTerrainStatCheck ORdirectcancel0withoutthatloop.',open=['Fullitemexceptionfamilies/persistentitemallwriters remainseparateWP50/Movebindingsemantics; thisrecordnotfullHeldItemfamilyPASS.'])
row(716,[
 'MudSportFieldinitial0; gen>=6Movefailsifglobalpositive, successfulEffectsets5.',
 'WaterSportFieldinitial0; gen>=6Movefailsifglobalpositive, successfulEffectsets5.',
 'OlderMudSportMovechecksanyallBattlersmemberMudSporttrue, failsifone; otherwisewritesuserMudSporttrue.',
 'OlderWaterSportMovechecksanyallBattlersmemberWaterSporttrue, failsifone; otherwisewritesuserWaterSporttrue.',
 'BotholdmemberbooleansresetfalsebyactualBattlerinit; currentglobalfieldcounter isnotresetbyordinarymemberreplacement.',
 'Electricpower divides3ifanymemberMudSport, andseparatelydivides3ifMudSportFieldpositive.',
 'Firepower divides3ifanymemberWaterSport, andseparatelydivides3ifWaterSportFieldpositive.',
 'Theseareseparatetwoguards, so deliberatelycoexistingold+newfieldswouldeachapply; defaultgenerationproducerchoosesonefamily.',
 'NaturalfieldcountdownreducesMudSportField/WaterSportFieldpositiveandmessagesat0, notoldmemberboolean-countdown.'
],['activefield_full','sport_ion_producers','b_init','battlerfull','calculations','eor_all','b_settings'],'genbranchselectsglobal5/membertrue→actualdamagemultiplierguards→memberinit ORglobalcountdown; replacementscopeexplicit.')
row(717,[
 'FairyLockinitial0; movespecificalreadypositivefails.',
 'SuccessfulEffectsets2 beforemessage.',
 'trappedInBattle includespositiveFairyLock afterothermembertrappingchecks.',
 'Voluntaryswitch/runeligibilityappliesitsownforced/Ghost/ShedShell/RunAway/etcactualorderedexemptions; fieldflagnotabsoluteeverydepartureban.',
 'CompleteEORtaildecrementspositiveFairyLockoncewithoutmessage; iftailnotreachedcounterretained.',
 'Replacement/forcedswitch entryseparatefromcommandnormaltrapquery; notalllegalexitsblockedbyflag.'
],['activefield_full','switch_effects_full','battlerfull','switching','running','eor_all'],'FairyLock2→normaltrappedquerywithcallerexemptions→fulltail--, notuniversalexitinterceptor.')
row(718,[
 'IonDelugeinitialfalse; NormalMoveBecomeElectricstatusMovefailswhenalreadytrue.',
 'StatusversionalsofailsifnootherunmovedbattlerwithUseMove/Shiftchoice; allBattlersphysicalpresencealoneinsufficient.',
 'Damagingversionreturnsfalsebeforebothstatus-onlychecks, so thosefrontsnotuniversalforthisfunction.',
 'EffectGeneralwhenflagalreadytrue returnswithoutduplicateestablishmentmessage; otherwisewritestruebeforefeedback.',
 'Typecalculationnormal-type ret becomesElectricwhileIonDelugetrue atactualtype-changeorder; notallmoveTypesconverted.',
 'CompleteEORtailclearsfalse; missedtailretainsflagprefixratherthan“automaticallyonwallclockroundchange”.'
],['activefield_full','sport_ion_producers','usagefull','calculations','eor_all'],'status/damagingfrontdifference→fieldtrue→Normaltypecalculationconsumer→completeEORtailfalse.')
row(719,[
 'FusionBoltinitialfalse; FusionFlareinitialfalse.',
 'FusionBoltfunction usage-counteroverride capturesoldFusionFlareintoitsmoveinstance@doublePowerbeforecallingparentcounterreset.',
 'FusionFlarefunctioncapturesoldFusionBoltanalogouslybeforeparent.',
 'ParentgenericpbChangeUsageCounters resetsbothglobalFusionflagsfalse; normalinterveningmoveusingparentcanthereforebreakchain.',
 'OwnEffectGeneralsetsitscorrespondingBolt/Flareflagtrueifthatphaseactuallyreached.',
 'BaseDamageMultiplier doublesonlycaptured@doublePower; laterflagclearingdoesnotretroactivelychangethecapturedflagforthatuse.',
 'CompleteEORtailclearsbothfalseagain.',
 'Thisisnotindefiniteever-used-this-roundhistoryacrossanyinterposednormalmove; earlyfailure/overriddencountertimingactualUseMoveorderretained.'
],['activefield_full','fusion_producers','usagefull','use','eor_all'],'oppositeflagcapture→superclearboth→actualeffectsetown→nextcounterreader/capture→tailclear; no persistentbattlehistory.')
row(720,[
 'AmuletCoinfieldinitialfalse.',
 'RecordBattlerAsParticipated uses!opposesandstoreditem_idAMULETCOINorLUCKINCENSE tosettrue.',
 'ThiswriterdoesnotrequireitemActivebeforematchingID, so suppressingitembyMagicRoomdoesnotbyitselfpreventthisrecord.',
 'Oncefieldtrue ordinaryswitchingoutdoesnotclearit; ActiveFieldpersistsuntilbattleobjectlifecycle.',
 'Actualrewardsconsumefieldflaginmoneycalculation onlywhenitsowninternal/money/victory/playercapgatesreach; noautomaticimmediatemoneymutationatrecording.'
],['activefield_full','switching','money','normal_end','battlerfull'],'ownsideparticipationrecordstoredID→fieldflagtrue→laterGainMoneymultiplier, notactiveitemtrigger here.')
row(721,[
 'HappyHourfieldinitialfalse.',
 'DoubleMoneyMove EffectGeneral writestrueonlyifusernotopposesownplayerside.',
 'Opponentuserstillproducescommonhappymessage butdoesnotsetthisownsidebonusflag.',
 'FlaghasnoordinaryEORcountdown/reset; repeatedtrueisnotacounterincrement.',
 'Endrewardcalculationsconsumeactualflagwithothermoneyconditions; noimmediatemoneywritebythisMove.'
],['activefield_full','misc_full','money','normal_end','eor_all'],'ownsideHappyHourEffect→persistentbattleflagtrue→latermoneybonus; feedbackalsopossiblewithoutflagwrite.')
row(722,[
 'PayDayfieldinitial0.',
 'AddMoneyMoveonlyincrementswhenuser.pbOwnedByPlayer?true, notmerely!opposespartnerorotherownside.',
 'EachreachedEffectGeneral adds5*user.levelatthatmoment.',
 'Messagecoinsscatteroccursalsofornonowneduserwithoutincrement.',
 'BattlePayDayrecordnotclearedeachroundinEORtail; multipleownusesaccumulate.',
 'Laterlevelchangesdonotrevisetheexistingnumericrecord; endmoneycollectionusesactualrecordwithmultiplier/cap/messagegates.',
 'ActionfailuresbeforeEffectGeneraladdnothing; latermessagefailurecanleaveincrement; no globalrollback.'
],['activefield_full','misc_full','battlerfull','money','normal_end','eor_all'],'playerowneduser→levelnow*5accumulate→message→laterendcollectrecord; partnerownershipseparate.')
base['rows']=rows;base['source_dictionary']=d
(P/'manual_batch_10c.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print('authoredrows',len(rows),'children',sum(len(x.get('children',[]))for x in rows),'layout',sum('layout_reason'in x for x in rows))
