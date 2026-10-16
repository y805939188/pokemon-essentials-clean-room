from pathlib import Path
import json,datetime
o=Path(__file__).resolve().parent;rv=json.loads((o/'reverse-mapping.json').read_text());it=json.loads((o/'interfaces.json').read_text())
# All entries are manual finite semantic judgments after actual full catalog
# reading, complete relevant caller reads and named source-contribution receipt.
facts={
'L01':('D_SWITCHb:331–345; Battler003:64–99; receivedDRIZZLE','Entry records/position/hazards precedeability. HazardHP0 invokesfaint/EXP/judge thennext; DRIZZLEneverentered for that member.'),
'L02':('D_BATTLER6a:196–207/62–71; D_ENTERWRAPPER; D_ICEIMPOSTER','GainingandGas-end use defaultfalse switch_in; Imposterrequires true andskips, IceFaceEiscueform1/haildoesnotinspectflag andformrequest0ifeligible.'),
'L03':('D_BATTLER6a:5–28/62–71; receivedSLOWSTART/INTIMIDATE','LastGas switchout setslocalHP0/fainted beforeglobalGasrequery; persistentPokemonHPnotzeroed. FalseflagreentrystillsetsSlowStart5andcanIntimidate.'),
'L04':('receivedOnSwitchOutREGENERATOR; D_HPWRITER:23–34','Ordinaryendflagfalsecallback requestsfloor101/3=33, directRecoverwithoutcanHeal:20→53. Endflagtrue skips; outerendhealsseparate.'),
'L05':('D_BATTLER6a:30–42; receivedReceiver/SoulHeart','FirstallprioritypasschangesreceiveridentitytoSoulHeart; secondpassreadsnewidentityandrequestsSpAtk1. No fullgain/losswrapper needed.'),
'L06':('receivedBattler004statuscommit/Synchronize/sourceeligibility; D_BATTLER6b:329–336','Originalpoisonalreadywritten. Opposingsourceimmune declinesreflectedpoison; subsequentownitem/abilitycurechecksremain. No originalstatusrollback.'),
'L07':('receivedBattler005centralpositivewrite→OnStatLoss; receivedCompetitive','Two actualopposingstatlossnotifications requestSpAtk2then2:0→2→4. Same-side sourceblocked, nilsourceallowed.'),
'L08':('D_TRUANT:249–257; receivedOnFlinchSTEADFAST and fullsuccesssource','SettingFlinchonlysetseffect; speed0untilactualsuccessgatefailsfromflinch. ThatfailuretriggersSpeed1andstillfailsaction.'),
'H01':('D_HPWRITER:5–34; D_BATTLER6a:45–49; D_EMEXIT','H101half50; old50→49strictcrossflagtrue,old→50false. Recoverto50clearsflag beforeabilityconsumer; noautomaticexitfromearlierdamagealone.'),
'H02':('D_EMEXIT:382–404; D_BATTLER6a:5–28; D_EORc:700–706; D_SWITCHa:142–204','TrainerEORtruebranchrecalls+leaveslocalHP0 andreturnstruebeforechoosingreplacement. LaterEORSwitchfillsseat; returnedtrueisnotcompletedreplacement.'),
'H03':('D_EMEXIT:369–380; D_LIVINGCOUNT; receivedrunningquery','Wildopposingownerextra count>1rejects iftwoalive; otherfaintedmeanscount1andcontinuestocanRun,thenwritesdecision3andtrue. Nominalside2/reservesdonotcount; playerownerhasnoextracountgate.'),
'D01':('D_TRIGGERFULL:5–11; receivedAftermath/Damp/indirect/contactpermission','T abilityallowfaintedtrue; AftermathrequiresTfaint/contact, DampblockswhenMoldBreakerfalse. Truebreakercanallowfloor101/4=25andU100→75, thenUHPitemcheck.'),
'D02':('receivedEffectSporecompletebody and centralstatuses','r29passesfirst30%, selectedpoisonagainstSteeldeclinescentraleligibilitywithoutredraw; r30stopsbeforesecondstatusrandom.'),
'D03':('receivedMummybody; D_BATTLER6a:171–207','Contactpermissionmaypreventassignmentyetloss/gaincallbacksrunwitholdnil. CurrentSlowStartsurviveslosscleanupandnewentrysets5; noinventedassignment.'),
'D04':('D_TRIGGERFULL:112–115; receivedMoxie/ChillingNeigh','TargetdamageStatefainted2andfoereserveexists: Moxierequests2, Chillrequests1. Allopponentsfaintedgateinthehandlerblocksbothtypes.'),
'D05':('receivedBeastBoostfullbody; centralstatqualification','RawfivestatmaxwithfirstenumtiechoosesAtk. Atk+6failscanraise, nofallbackDef; no genericbestlegalstat algorithm.'),
'D06':('D_TRIGGERFULL:157–170/193–203; receivedBerserk','EffectiveSheerForce+positiveaddlEffectskipsentirelater2, soBerserknotcalled. UserOnEndUsebeforegateisstilleligible.'),
'D07':('D_TRIGGERFULL:154–198; receivedPickpocketfullbody','Targetcallbackreceivesswitched_battlers; originalsourcealreadyreplacedcausesPickpocketrefusal, notstealingfromnewoccupant.'),
'D08':('D_TRIGGERFULL:13–34; receivedBattler003formrequest','ChangeForm0precedesreadingtarget.form. Livingrequestsuccessleaves0andnoextra1branch; faintrequestrejectkeeps1andmayrequestUdeflossafterquarterdamage. Rawidentitynotordinaryactivegate.'),
'E01':('D_EORc:613–623; receivedHealercompletebody','Onehandlerdrawr29allowsloopallstatusallies; r30returnsbeforeloop. Notoneindependentrollperally.'),
'E02':('D_EORa:5–25; D_EORc:604–617; receivedHydration','RainDuration1endsbeforehealingphase, noDefaultrain=>HydrationseesnoRainanddoesnotcure. Duration2continuesandmaycure.'),
'E03':('receivedMoodycompletebody; centralcanRaise/canLower','Gen8fiveonly;precomputeddown5includesAtk0andfour+6. RaiseAtk2thenremoveAtkfromdown, forcedDefselection6→5; noacc/eva; oldsevenalternative.'),
'E04':('receivedHarvestfullbody; D_BATTLER6b:297–323/233–267','Sunnyemptycurrent/recycledberryskipRNG; otherweather r49yes/r50no. Recycledrecordclearedandinitialonlyifempty; heldtriggercanconsumeimmediately/Symbiosis.'),
'E05':('receivedPickupfullbody; D_BATTLER6bheldtrigger','StrictmaximumpositivePickupUse selects8itemY over5X; selectednilitemreturnsratherthanfallingback5. Clearselectedpickup+matchingRecycleontransfer.'),
'E06':('D_EORb:471–505; D_STARTTERRAIN:786–811; D_MIMICRY','ExpireGrassysetsNoneandnotifiesabilities; startdefaultPsychicinternallyabilities+items;outeragainabilities+items. Mimicryhasnoalreadytypeguard: resetthen2Psychicnotifications.'),
'E07':('D_EORc:684–701; receivedBadDreams/effectdamage','CurrentmemberEffectcanwritepositiveDecision. LoopstilldoescurrentitemandGainItemandlatermemberssubjectcurrentactive/alive; explicitdecisionreturnafterGainExp700. No universalpercallbackearlyexit.'),
'F01':('D_BATTLER6a:75–99; D_EORc:710–711; receivedUseendcontinualsource','EmptyeligiblefoeTracepoolkeepsTrace, latercontinualcheckcanchoosegainablefoe. Gen5commentdoesnotimposeonlyfirstentryrestriction.'),
'F02':('D_DANCER:541–577; D_PRIORITY','Collectspeedfasttoslowthenpoplast=>50before100. Dancerflagpreventsrecursiveoutercall; SimpleUsewithoutrealmoveindexdoesnotchargeoldslotPP.'),
'F03':('D_DANCER:551–575','SaveOutrage2thenincrement3beforecanChoose. Qualificationfalsebypassessuccessrestorebranch; normaltailonlyclearsDancerflag, leaving3. Nofinallyrollback.'),
'F04':('D_FOREWARN:2738–2788','PowerHigherWithUserHPfirst150thenlaterset80. Ordinary100ismaxanddisplayed; no actualdamagecalc, no150basedoncomment.'),
'F05':('D_NEUTRALGAS:2900–2932; D_BATTLER6b:390–394','GasremovesUnnerveeffectthenouterallliving3eachcallglobalberrycheck. Eachcanrevisit3butactualconsumepermission/itemstatereread; no9guaranteedeffects.')}
vectors=[]
for v in rv['vectors']:
 if not v['id'].startswith('AB-'):continue
 key=v['id'][3:];evidence,fact=facts[key]
 v['assessment']='SUPPORTED_SCOPED_SHARED_AB_STATIC_VECTOR';v['source_fact_units']=[];v['interfaces_required']=['IF-COMAI-SHARED-AB-PHASE-CATALOG'];v['manual_semantic_judgment']=fact;v['evidence_level']='SOURCE_STATIC; RECEIVED_NAMED_SOURCE_FACTS; DERIVED_VECTOR'
 vectors.append({'id':v['id'],'formal_line':v['line'],'premises':v['premise_cell'],'asserted_result':v['asserted_result_cell'],'manual_fact_and_control_assessment':fact,'source_evidence':evidence,'reviewer':'/root/com_ai','execution':'NOT_EXECUTED','receiver_scope':'This finite static catalog vector and currentWP49relevantcontract; noentireWP49formalreverseorhostPASS.'})
assert len(vectors)==31 and len(facts)==31
record={'schema':'gr8-com-ai-shared-ab-reception/v1','received_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/com_ai','primary_catalog':'combat-requirements-wp49-51-52.md entire349lines','additional_formal':'WP49main entire272lines actuallyread io/D_WP49a,b; supplementary identity ledger bindsB8','additional_own_sources':['EOR781fullcontinuous','ActionSwitching469fullcontinuous','BattlerAbilityAndItem476fullcontinuous','BattlerTriggerEffects218fullcontinuous','HPwriter1–125completeHP/drain/faint/PPunits','EmergencyExit363–408','Dancer521–578','Forewarn2738–2788','ICEFACE/IMPOSTER/Intimidate2820–2868','Gas2900–2932','Mimicry3156–3187','pbStartTerrain786–811','currentSideBattlerCount474–479'],'source_contributions':'received-source-contributions.json 12actualnamedexternalfull-source-readers,factsreceivedwithAIcallerjoin','vectors':vectors,'counts':{'vectors_read':31,'source_scoped_accepted':31,'vector_unreceived':0},'explicit_boundary':'This is sharedcatalogscopedreception, not entireWP48/49/50formalreadset reverseacceptance. NoRsourceexecution,actualgame/host/feedbackfaulttest orfrequencymeasurement.','business_execution':'NOT_EXECUTED','new_behavior_runs':0,'update_started':False}
(o/'shared-ab-reception.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
it['open_interfaces']=[x for x in it['open_interfaces'] if x['id']!='IF-COMAI-SHARED-AB-PHASE-CATALOG']
it['accepted_scoped']=[x for x in it['accepted_scoped'] if x['id']!='IF-COMAI-SHARED-AB-PHASE-CATALOG']+[{'id':'IF-COMAI-SHARED-AB-PHASE-CATALOG','status':'ACCEPTED_SCOPED_SHARED_STATIC_CATALOG','receiver':'/root/com_ai','provider_readers':['/root/com_ai','/root/com_move','/root/com_move/attributes_calling'],'evidence':'shared-ab-reception.json every31vectoractualfact/source/control; fullWP49mainread+namedsourcecallbackcontributions','facts':['All31ABfinitecatalogvectorslocallyreceivedafteractualfullrelevantphasecallerreads; exactpervectorfactsinshared-ab-reception.json.','ThisdoesnotgrantwholeWP49formalreverseacceptanceorall267familycountqualifications,defaultPBSorhostexecution.'],'execution':'NOT_EXECUTED'}]
it['accepted_scoped_count']=len(it['accepted_scoped']);it['open_interface_count']=len(it['open_interfaces']);it['updated_utc']=record['received_utc'];rv['shared_catalog_source_open_vectors']=0;rv['updated_utc']=record['received_utc']
(o/'interfaces.json').write_text(json.dumps(it,ensure_ascii=False,indent=2)+'\n');(o/'reverse-mapping.json').write_text(json.dumps(rv,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'sharedABaccepted':31,'scoped_interfaces':len(it['accepted_scoped']),'outer_reception_open':len(it['open_interfaces'])}))
