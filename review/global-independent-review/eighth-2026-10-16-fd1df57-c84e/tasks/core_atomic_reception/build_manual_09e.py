import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_09d.json').read_text());d=base['source_dictionary'];rows=[]
d['pokemon_item_exact']={'path':'Data/Scripts/014_Pokemon/001_Pokemon.rb','range':[552,577],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete item/item_id/item=/hasItem actuallyread; preserve nil/false/unknowntruthy distinction'}
d['pokemon_pokerus']={'path':'Data/Scripts/014_Pokemon/001_Pokemon.rb','complete_units':[[791,812]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete PokerusStrain/Stage/Give actuallyread785–827'}
d['burmy_leave']={'path':'Data/Scripts/014_Pokemon/001_Pokemon-related/001_FormHandlers.rb','range':[178,200],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete BURMYcreation/leavingregistration actuallyread'}
d['money_cap_config']={'path':'Data/Scripts/001_Settings.rb','range':[48,49],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE actual MAX_MONEY scalar999999 declarationread43–52; no wholeSettingscredit'}
d['partner_array_producer']={'path':'Data/Scripts/012_Overworld/002_Battle triggering/001_Overworld_BattleStarting.rb','range':[171,202],'actual_reader':'/root/core_atomic_reception','reading':'OwnFULL749 plus actualcomplete partnergate/setup-player methods reread'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(615,[
 'EndOfBattle copies oldDecision beforeanyconversion. Old1&&wild&&caughtQueuenonempty rewritescurrent4, whilecase stillusesoldDecision.',
 'Bothrecords canthereforetemporarilydiffer; latermoney/scene/return testsreadtheir actualold/currentvariable, not oneimmutableterminalenum.'
],['start_end_full','catch_full'],'oldcopy→conditionalcurrentcaptureconversion→oldbranch/currentlaterconsumers.')
row(616,[],[],'',layout_reason='Normal-ending olddecision branch table header; concrete branches individuallydecomposed.')
row(617,[
 'Old1 trainer path SceneTrainerSuccess, defeatedopponentmessage for1/2/3trainers, theneachopponent show/lose_text fallback.../playername substitution.',
 'Moneycall hereonlyifcurrentdecision!=4. Oldwild1converted4 skipsthisearliermoneycall; capturequeueprocessing laterprecedescurrent4money.',
 'Trainer&&caughtQueuenonempty thenShowOpponent(opponent.length). Errorinlatertrainertext/presentation doesnotundoearlierstate orforcecontinue.'
],['start_end_full','money','battlefull','audio'],'oldwinpresentation→currentnon4money→qualifiedhide, preserve exactvictoryBGMcaller.')
row(618,[
 'Old2/5 internal displaysownnoablefeedback andtrainerlossnames1/2/3 iftrainer, thenLoseMoney.',
 'canLosefalse addsblacked-outmessage afterlossmoney; canLosetrue doesnotbypassmoney. Actualouterhealing/recovery remainsseparate.',
 'Noninternal branch onlycurrentdecision2 andopponentnonnil iterateswin_text fallback/playername substitution. Noninternaldraw5 doesnotinheritthoseopponentwinmessages.'
],['start_end_full','money','battlefull'],'oldlossdraw→internalmoney/message orqualifiedexternalwintext, not canLose exemption.')
row(619,[
 'Old4 capturebranch logs andSceneWildSuccess onlyif !GAIN_EXP_FOR_CAPTURE; normalfalsegate skipsaudiohere, notcapturereception.',
 'Old1converted4 stillusesold1case, cannotbereroutedinto old4-onlypresentation. CaptureSceneThrowSuccessME andordinaryvictoryBGM remaindistinct.'
],['start_end_full','b_settings','catch_full','audio'],'oldcapture/configpresentation distinctfromcurrent4conversion andcapturethrowME.')
row(620,[
 'NormalEnd invokedwith0/3 runsno old1/2/4/5 branchspecificreward/loss text butstillsharedpostbranchcleanup.',
 'ExplicitAbort exceptionbypasses entireNormalEnd andusesouterSceneEnd0; a computeddecision0doesnotaloneproveAbortorskipcleanup.'
],['start_end_full','command','running'],'entryroute notnumeric0alone determines sharednormalcleanupreachability.')
row(621,[
 'Sharednormalorder RecordAndStoreCaught→current4GainMoney→internalPokerus→SceneEnd.',
 'Then for eachnonnilbattler CancelChoice before activeOnSwitchOut(ability,b,true); Cancel returnsresidualitembeforeMegaunregister/clear. Activeability eligibilityqueriedatthattime.',
 'ThenpbParty(0) foreachnonnilPokemon withpartyindexi reads usedInBattle[0][i], PeerLeave(self,p,used,true), thenPokemon.item=initialItems[0][i]. Returns currentdecisionafterallnormalsteps.',
 'SendOutwritesused[side][slot/2], notpartyindex; normalendsreadsbyi. Samefieldreplacementwrites samepositionrecord, so readboolisnot always actualindividualparticipation (existingGR013).',
 'BURMYactualleave handler requiresend&&used thenenvironmentform1/2/0; Peer appliestruthydifferentform,capHP,changehook. Theindexmismatch canthereforeaffect thisrealconsumer, notjustanunusedlog.',
 'Onlyplayer-sideparticipatingarraygetsfinalitemrestore; currentpartymergedidentityandmutableledgerareactualinputs, notuniversalbothsideoriginalitems. Failure anypoint preserves priorqueue/money/HP/forms/refunds.'
],['start_end_full','catch_full','peer','burmy_leave','switching','command','items','ability_item','pokemon_item_exact'],'orderedsharedterminalcalls→slot-written/party-readused→actualformconsumer→Pokemonitemsetter, existingGR013protected.')
row(622,[
 'Caughtqueue eachPokemon SetCaught/Seen, firstownedset/displayperglobalhasDex/unlockedgate, ShadowownedifShadow, StorePokemon. Queueclears onlyafterfullnormaliteration.',
 'Fullpartyreceive canPeer-clean oldchosenmember/clearPOISONcount/unmega/primal→storeold→deletePlayerpartyindex→display→leftshiftinitialItems andthreeworldtemp arrays→thenStorecaught. UsedInBattle isnotamongtheseshiftwrites.',
 'ActuallyparticipatingpartnerpathcreatesnewcombinedPokemonarray fromplayerrefs thenpartnerrefs; no-partnerpathreusesplayer.partyarray. Registered-but-notparticipatingpartnerdoesnotmakecombinedarray.',
 'Thereforecapturedeletes/shiftsoncurrentplayerparty leaveoldcombinedmemberrefs andshiftedledgerindices mismatched. Normalendstillrestoresoldcombinedmemberi usingnowshiftedinitialItemsi, includingoldsent-to-boxobject. No-partneralias removesoldmemberfromendloop.',
 'Laterouterpartnerheal/current-worldPickupHoney readactualcurrentparty/item afterrestore; neitherrepairs originalitemidentitybydefinition. Sourcecapacity/UI gatescanboxratherthanparty, noallreceivealwaysparty assertion.'
],['catch_full','peer','start_end_full','partner_array_producer','battlefull','pokemon_item_exact'],'queueacquire/currentpartydelete+recordshift→possiblemergedarrayaliasseparation→endloopwrongidentity, preserveexistingcorrectqualifiedformal.',open=['Pokedex SetCaught/Seen definitions and complete storage/capacity/UI policies outside receivedCAA10factremain independentlyscoped; no allcapture/nativePASS.'])
row(623,[
 'Finalitemloop onlypbParty(0); no symmetricparty1restore. InitialItems canchangeviaConsume/Harvest/Pickup/permanenttransfer/capture partyrearrangement, notimmutableconstructorcopy.',
 'Pokemon.item= nilclears; falsewritesfalse; truthyunknownregisteredID returnswithoutchangingolditem, validtruthy normalizesid. Invalidargumenttypes mayerrorinGameData query; no universalinvalid-asnil promise.',
 'Leaveabilityacquireditem persists onlyifitsprocessor actualcurrentinitialrecord permitslaterrestore; genericleavecallbackcall doesnotguaranteekeeporloseallacquireditems.'
],['start_end_full','pokemon_item_exact','registry_finite','ability_item','eor_late_handlers','catch_full'],'mutableparty0initialrestore→actualPokemonsetter, notbothsides/unconditionalold-itemreturn.')
row(624,[
 'CancelChoice checks currentactionUseItem ANDtruthyitem, ReturnUnusedItem beforeUnregisterMega/ClearChoice; itdoesnottrackwhetherthischoicealreadyexecutedorrefunded.',
 'SuccessfulUse handlernormalreturn cleareditemidentity soEndskiprefund; rejectedCanUse itemexecutor refundedbutleftidentity soEndcanrefundagainifunchanged/reached.',
 'Playerrefund mustcurrentBagcanAdd thenadd; falsecapacityraisesbeforelaterclear/leave/restore. Existingrefund/money/HPprefix remains, noextraidempotencyledgeradded.'
],['start_end_full','items','command','bag'],'actualresidualidentity→refund-beforeclear→latercleanup, correctexistingWP28contractpreserved.')
row(625,[
 'Qualifiednormalinternalwild2v1/nopartner/liveownusers/nochoiceclear/capacity2Potion: initial2→tworegistrations0, firsthealsbenchTmissing1/clearsidentity, secondCanUsefullHPfails/refunds1/leavesidentity.',
 'SolewildregularPOISONcount0/HP1/noPoisonHeal/MagicGuard/heal, normalnondamageactions/nointerference: EORpoisonReduceHPminimum1→formalFaint.',
 'Noearlierwriterneeded: EORSwitchJudge findsfoepartyempty/ownable→1, callerpositiveexit andnormalEndreachesresidualsecondCancelChoice→inventory2.',
 'Observedconditionalend Tfull/oneactualtreatment/POTION2; neednotstartnextCommandPhase orreachfullEORtail. All vectorinputsqualifyactualsource, no runtimeclaim.'
],['items','command','bag','eor','hp_damage_heal','terrain_indirect_gate','start_end_full','switching'],'finitefailed-useidentity→EORfaint/Judge→normalendsecondrefund, staticexistingcorrectvector.')
row(626,[
 'Ifwildsurvives/nootherterminalsource andnextnormalcommandqualifiedlive&&!multiturn, directClearChoice removesresidualwithoutrefund, inventory1.',
 'IfseconduserformallyFaintsandreachescallClearChoice beforeterminal, itsresidualitemisremovedwithoutrefund, laterEndhasnone:inventory1 undernootherinventorywriter.',
 'Swap/otherCancelChoice/Abort/exception aredifferentroutes; capacitymustalloweachreachedrefund. Refusalraiseswithpriorhealing/consumption/firstrefundretained andlaterleave/restorenotguaranteed.'
],['items','command','bag','b_change','start_end_full','battlerfull'],'actualnext-phaseorfaintclear controls versusnormalendre-refund, qualifiedfailureprefix.')
row(627,[
 'Compatibilitychoiceforhistoricalrefundbehavior isfutureuserdecision; reviewdoesnotautomaticallyrepairsourceorintroduceidempotency.',
 'LocalNaturalGiftsecondhiterror mayreturnthroughdiagnostic andconditionalreselection, notautomaticallynormalterminal. Priorpersistentwrites survivebutnotnecessarilyprocesscrash/cleanuprestore.',
 'All suchcases remainNOT_EXECUTED; staticbranchfeasibilityandnativehostrecovery areseparateclaims.'
],['use','pbdebug','errors','attack','start_end_full','ng_specific_formal'],'localerror→actualdiagnostic/schedulercaller→possibleterminal, noinventedguaranteedcrash/restore.')
row(628,[
 'Gain/LoseMoney requireinternal&&moneyGain. Trainerreward sums eachopponentteammaxlevel(min1) *currentTrainerType.base_money, thenAmuletCoinflagx2 andHappyHourflagx2.',
 'Player.money settervalidatesInteger/clamps0..MAX_MONEY999999. Gainstats/message useactualnew-old difference>0, so cappedzeroadditionproducesnone.',
 'PayDaypositive fieldamount mutatesinplacex2/x2 before adding; itsseparateactualdelta stats/message onlyif>0. Capturecurrent4 callsafterRecordStore, notjusttrainerrewardcall.',
 'EarlierPayDaydoubling orfirstrewardstats canpersistiflateraddition/messagefails. Exactownersegmentmaxlevelincludesallnonnilteamlevelnotonlyliving; partnernotopponentteamunlessactuallyconfiguredthere.'
],['start_end_full','battlefull','playerfull','money_cap_config','owners','teams','config'],'qualifiedteamreward+flags→cappedplayersetter→actualdeltastats, thenmutablePayDayphase.')
row(629,[
 'Loss hasinternal&&moneyGain andswitchNO_MONEY_LOSS guard. Maxlevel onlyside0trainer0 playersegment, notpartner.',
 'BadgeCount count entries==true; factorindexmin(count,8) gives8,16,24,36,48,64,80,100,120 for0..8plus.',
 'Nominalmaxlevel*factor cappedtocurrentmoney, moneysetterwrites; actualold-new positiveonly stats and trainer/wildspecificmessage. canLose doesnotgate thismethod.',
 'ExistingGameswitchsavedtrue canblockloss; defaultswitchID33 doesnotmeanstoredvaluemustfalse. Actualconfig/switchproducer finiteKernelreception retained.'
],['start_end_full','battlefull','playerfull','config','owners','teams'],'money/configswitch→actualplayerteamlevel/badges→capdebit→actualdeltastats; partnerexcluded.')
row(630,[
 'NormalEnd internalonly aftercaughtreceiving snapshots indicescurrentglobalplayer.party wherepokerusStage1. Eachsnapshotindexthenleftneighborfirst/rightnext currentstage0andrand(3)==0.',
 'TargetGetStage0uninfected only; curedstage2 isneithersource norelEligibleTarget. Newlyinfectedtargetsarenotappendedtosourcesnapshot, thoughmayblocklaterredundanttargetchecks.',
 'PokerusStage raw0→0, nonzero low4bits0→cured2 elseinfected1; strain=encoded/16. GivePokerus skipscured, incrementsinfectionstat, usesvalidprovidedstrainornew1..15, writesduration1+strain%4 andstrainhighbits.',
 'Samevalidsourcestrain thuspassedtoqualifiedadjacenttarget; no egg/faint guardaddedinthisEndloop. Currentcapturepartyrearrangementaffectssource/neighboridentitybefore snapshot.',
 'WholeEORneednotexecute forthisnormalEndtransmission; source/targetstate/statupdatescanpartiallycommitiflatercallback/stat/RNGerror.'
],['start_end_full','pokemon_pokerus','playerfull','catch_full'],'postcapturecurrentpartyinfected-indexsnapshot→left/rightcurrentstage/RNG→encodedpersistentinfection/stat.')
base['source_dictionary']=d;base['rows']=rows
assert all(k in d for r in rows for k in r['source_units']if isinstance(k,str))
(P/'manual_batch_09e.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children'])for x in rows),'layout':sum('layout_reason'in x for x in rows)})
