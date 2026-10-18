import pathlib,json,subprocess,hashlib,datetime
V=pathlib.Path(__file__).resolve().parent;R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';B='fd1df570cad987dc3852a3b958f03916e317f7fe';NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
F=json.loads((V/'forward-mapping.json').read_text());REV=json.loads((V/'reverse-mapping.json').read_text());N=json.loads((V/'next-dispatch.json').read_text());assert len(F['atoms'])==2127
manual=[
 ('R10','DebugPlay133–140','Debugplaynumberparams range0..500/default0/cancel−1; fileplayonlyifreturnednumber≥0. Normalcanceldoesnotopenfileorplay.'),
 ('R10','PlayBattle111–128','Unknownrecordtag leaves battleplayernil; withnormalremainingmetadata/BGM/animationprefix, blockfailsatnil.pbStartBattle. Earlierprefixerrorsremainpossibleandarenotmovedtothispoint.'),
 ('RC-COMMAND','Command60–98','OrdinaryFight registersvalidmovebeforechoosingtarget onlyif!singleBattle?; negativechosentarget returnsfalsewithouttargetregister. Singlebattleomitsmanualtargetselection.'),
 ('RC-COMMAND','Command5–23,60–98','CancelChoice clearsactualchoice/Megapending andmayreturnactualunuseditem, butfullRecordedmoduleprovidesnocancel/clearchoice recordoverride; oldrecordedslotremainsuntilsuccessfullyoverwritten.'),
 ('RC-ACTIONOTHER','RegisterShift21–26/RegisterCall31–36','BaseShift/Call registration writesactualchoicewithtag/0/nil andtrue; fullRecordedmodulehasneitherregistrationoverride, soitsoldrecordedslotisretained.'),
 ('RC-COMMAND','Command171–265','Basecommandphase handlesplayerloopthendecisiongate/AIloop; eachrecordingphasehasalreadyappendedits4emptyrecordslots. ActualnormalAI/player successfulmove registrations shareRecordedwrapper.')]
def sid(p):
 b=subprocess.check_output(['git','show',R+':'+p],cwd='/workspace/pokemon-essentials');return {'repo':'/workspace/pokemon-essentials','commit':R,'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':subprocess.check_output(['git','rev-parse',R+':'+p],cwd='/workspace/pokemon-essentials',text=True).strip()}
F['source_identities']['RC-COMMAND']=sid('Data/Scripts/011_Battle/001_Battle/009_Battle_CommandPhase.rb');F['source_identities']['RC-ACTIONOTHER']=sid('Data/Scripts/011_Battle/001_Battle/008_Battle_ActionOther.rb')
premise='FixedR/B8/nooverride; exactcaseinputwithvalidinitializedrecording/playbackstate, normalreachedregistry/serialization/scene/animation/commanddependenciesunlessnamedfailure. Absentrecordmeansnil/false, notemptytruthybyteString/Array. Meaningofunknown-tagfailureassumesearlierBGM/animationprefixnormal. SourcehelperfixturesdonotmandateadditionalfuturepublicAPI/layout/eventreachability. Native/realplayback/saveNOT_EXECUTED.'
new=[]
for num,(s,u,m) in enumerate(manual,2128):
 a={'id':f'FAC-A{num:04}','source':s,'unit_locator':u,'assertion':m,'formal_receivers':['F07 RC finite selectedrows'],'premise':premise,'pending_dependencies':[],'status':'FINITE_STATIC_RC_NAMED_CHILD_RECEIVED','evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','reader':'/root/facility_atomic_completion_cloud'};new.append(a)
F['atoms'].extend(new);F['bounded_denominator']=len(F['atoms']);F['v2_increments'].append({'path':'RC14-selected-row-complete-child-reception.v2.json','count':6,'ids':[new[0]['id'],new[-1]['id']],'utc':NOW})
children=[]
def c(case,name,meaning,nums,extra=None):
 refs=[f'FAC-A{x:04}' for x in nums];children.append({'id':f'FAC-RC-{case}-{name}','case':case,'meaning':meaning,'source_assertions':refs,'extra_premises':extra or [],'status':'FINITE_STATIC_CHILD_RECEIVED'})
c('W01','round','Onenormalcommandphase incrementsrecordindexandappendsonefour-slotround.',[1475,1476,2133])
c('W01','player','Playerchosensuccessfulmove m records[0,m]; normalsingleFightdoesnotaddtargetslot.',[1392,1462,2130])
c('W01','opponent','NormalopponentAIselectedmove mprime records[0,mprime]anditsoptionalAI-registeredtarget.',[1462,1465,2133],['Case explicitlystatesopponentAIchoosesmove; no genericAIquality/successguarantee.'])
c('W01','random','AnyexecutioncallsreachingrecordedpbRandomappendinthatorder.',[1479,1480])
c('W02','four','Withvalid2v2battlersallfourrecordpositionsareusable.',[1476,1462])
c('W02','empty','Unselected/forcedunwrittenpositionsretaintheirinitializedemptyarrays.',[1476])
c('W03','zero','Normalorganizedwrapperresult0clearsoldtemporaryrecordanddoesnotdump.',[172,173,174,175])
c('W03','three','Normalresult3likewiseclearsanddoesnotdump.',[172,173,174,175])
c('W03','four','Ordinaryfacilitytrainerbattlecapture4isnotordinaryreachable; recordwrapperwouldnotexport4ifexternallysupplied.',[164,172,173,174,175],['Recordedstorageoverridenotisreachabilityproof; capturerestrictions/normaltrainerbattlepremiseascurrentWP58.'])
c('W05','success','AthenBsuccessreplaceswholeslotwith[0,B].',[1462,1464])
c('W05','failure','FailedBregistrationdoesnotreplacepriorAslot.',[1463])
c('W06','replace','Afterinheritedautomaticlogicreturns, wrapperreplaceswholeslotwith[0,−1].',[1470])
c('W06','target','Nestedearliertargetisdiscardedbythatreplacement.',[1471])
c('W06','play','Playback−1usesautomaticmove(false), rederivingdefaultlogic.',[1498])
c('W08','cancel','NegativechosentargetreturnsbeforeRecordedtargetwrite.',[2130])
c('W08','confirm','Successfulfinaltargetsetsrecordelement2afteractualtargetregistration;laterwritesoverwriteit.',[1465])
c('W08','no-target','Singlefightorunwritten/cancelledtargetcanleave[0,move]withoutthirdentry.',[2130,1464])
c('W09','incomplete','Targetgiveninitialemptyslotexpands[nil,nil,target].',[1466])
c('W09','dispatch','Playbacknonemptyincompleteslotclearsactualchoice, butnilcommandtagmatchesnocommandbranch.',[1497,1504])
c('W12','random','Exhaustedrandomentryreturnsnil; randomindexstillincrements.',[1489,1490])
c('W12','switch','Exhaustedswitchentryreturnsnil; switchindexstillincrements.',[1487,1488])
c('W12','downstream','Noimmediateboundsrepair; downstreamconsumerdefineslaterdivergence/failure.',[1488,1490,1504])
c('W13','absent','Absentnil/falserecordreturnsbeforescenecreation.',[227],['Catalog空recordinterpretedasabsentlastbattlefield(defaultnil); truthyemptybytesnotacceptedbysourceguard.'])
c('W13','cancel','Debugnumbercancel−1skipsfilecallandplayback.',[2128])
c('W14','dispatch','Unknownrecordtypehitsnoneofthreeconstructionbranches.',[230,231,232,233])
c('W14','failure','Ifearliermetadata/BGM/animationcallsnormal, startupblockcallsnil.pbStartBattleandfails.',[2129])
c('W14','prefix','Scenecreation/abortable/deserializationprecededispatch; nofulltransactionorwholegamefailureclaimed.',[228,229,2129])
c('W15','assign','Promotionassignstemporarybytesvalueasglobal.lastbattle.',[225])
c('W15','clear','Promotionthen sets temporarynil.',[226])
c('W15','persistence','Globalmetadatapersistentobjectcontainslastbattle; gametempisnotthatpersistentvalue. Nativewritesuccessnotinferred.',[225,226],['CompleteKERNELFAC-SAVE01–13/globalwholeobjectregistrationandGlobalMetadata183sourceactuallyreceivedinv1; notnewwholeSave/nativecredit.'])
c('W15','unpromoted','Withoutpromotionthisparticulartemporaryrecordisnotmovedinto global.lastbattle.',[225,226])
c('W17','version','Record5tupleaddsnoexplicitformatversionfield.',[1458,1459])
c('W17','objects','Party/items/rulescontainruntimeobjectserialization; replaydependscurrentclass/registry/getter/fieldassumptions.',[1426,1428,1444,1454,1485,1515,1516,1517])
c('W17','boundary','Nocrossimplementation/versionequivalenceguarantee followsfromsamerecordedarrays; onlythedefinedsequenceconsumermechanismaccepted.',[1459,1481,1486,1504])
c('W19','actual','Aftercancellingoldactualmove, successfulShift/Callwritesactualactiontag.',[2131,2132])
c('W19','record','Nocancel/Shift/CallrecordinghookclearsorreplacespriorrecordedFight, sooldslotpersists.',[2131,2132,1504],['ValidfixturelayoutforShift; notanordinarysingle/doublefacilityShiftavailabilityclaim.'])
c('W21','index','Playbackplayerphaseadvancesroundindexbeforefirstrecordaccess.',[1492,1493])
c('W21','round','Absentroundfailsatindexread; nilslotfailsat.lengthatitsvisit.',[1496])
c('W21','boundary','Malformedround/slotfirstfailureisdistinctfromsequenceexhaustionreturnnil+increment; earliercompletedslotscanretainprefixeffects.',[1496,1488,1490,1497],['Firstslotnil/earlieremptywhencomparingfailurepriorityagainstfirstownrandom/switchconsumer; no claimallprevioussideeffectsrollback.'])
byid={a['id']:a for a in F['atoms']}
for ch in children:
 assert all(x in byid for x in ch['source_assertions'])
 for aid in ch['source_assertions']:
  a=byid[aid];REV['mappings'].append({'formal_clause':ch['id'],'atomic_assertion':aid,'meaning':ch['meaning'],'source':a['source'],'source_unit':a['unit_locator'],'premise':premise+' '+' '.join(ch['extra_premises']),'status':ch['status'],'pending_dependencies':[],'relation':'EXPLICIT_COMPLETE_SELECTED_RC_ROW_CHILD'})
REV['true_bounded_assertions']=len(F['atoms']);REV['v2_new_exact_child_bindings']=len(REV['mappings'])-992
s=F['source_identities']['F07'];fb=subprocess.check_output(['git','show',B+':'+s['path']],cwd=s['repo']).decode().splitlines();selected=['W01','W02','W03','W05','W06','W08','W09','W12','W13','W14','W15','W17','W19','W21'];groups=[]
for case in selected:
 hits=[(i,l) for i,l in enumerate(fb,1) if l.startswith('| '+case+' |') and i>=156];assert len(hits)==1;line,text=hits[0];old=f'F07-L{line:04}';hit=[x for x in N['unmet_formal_seed_structures'] if x['old_locator_id']==old];assert len(hit)==1;N['unmet_formal_seed_structures'].remove(hit[0]);closed=dict(hit[0],case='RC-'+case,children=[x['id'] for x in children if x['case']==case],status='FINITE_STATIC_CHILD_RECEPTION_COMPLETE',receipt='RC14-selected-row-complete-child-reception.v2.json');N['closed_finite_formal_seed_structures'].append(closed);groups.append({'case':case,'old_locator_id':old,'line':line,'complete_original_row':text,'children':closed['children'],'status':'FINITE_STATIC_ROW_CHILD_RECEPTION_COMPLETE'})
assert len(N['unmet_formal_seed_structures'])==950
units=[]
for k,ranges in [('RC-COMMAND',[(1,265)]),('RC-ACTIONOTHER',[(5,36)]),('R10',[(102,144)])]:
 ss=F['source_identities'][k];bb=subprocess.check_output(['git','show',R+':'+ss['path']],cwd=ss['repo']).decode().splitlines(keepends=True)
 for lo,hi in ranges:units.append({'identity':ss,'range':[lo,hi],'content':''.join(bb[lo-1:hi]),'actual_read':['257ff0 R10whole144','69ccc9+9e7296 Commandall265','ee7e01 Other1–66fullnamedmethods'],'qualification':'Ownactualcompletecontainedsourceunits; noallUI/AI/Move/Abilitycallbacks transferred.'})
packet={'schema':'facility-selected-RC14-full-row-child-reception/v2','utc':NOW,'actual_reader':'/root/facility_atomic_completion_cloud','formal_identity':s,'common_premise':premise,'rows':groups,'explicit_children':children,'new_source_assertions':new,'complete_supplemental_units':units,'counts':{'complete_selected_RC_rows':14,'explicit_case_children':len(children),'new_source_assertions':6,'all_source_assertions':len(F['atoms']),'finite_reverse_bindings':len(REV['mappings']),'remaining_original_seed_structures':950},'qualification':'FullRC29formaltextactuallyread70f935; only14listedrowsnowfullyfinitechildaccepted. Allnamedextra/prefix/inputinterpretationsabovearepartofthereceipt. NoW04actionorderingchoiceorW10failed-attempt-vscancel ambiguitysilentlyclosed, remaining15RCrowsnotacceptedbyregionproximity. SourcefullhelperauditdoesnotcreatefutureAPI/supportmandates. NOT_EXECUTED.','OPEN':['RemainingRCW04/W07/W10/W11/W16/W18/W20/W22/W22b/W23/W24/W25/W26/W27/W28needexactrequiredcallee/producer/meaningchildren; alreadyreceivedCOREterminal/commandfactsarereusablebutnotautomaticrowclosure.','OtherSF/PA/QC/WSseedchildexhaustiveness,202external;453/649/2732primaryeligibilityproofinputs remainOPEN.','W04debugmessage/clearwordorderandW10run-returnscopewillbereviewedagainstwholeWP58/sourcebeforeanygapclaim; 0newfinding/classificationbythisreceipt.'],'new_required':0,'new_optional':0,'new_contexts':0,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'wholeFAC_complete':False}
def save(n,x):(V/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
save('RC14-selected-row-complete-child-reception.v2.json',packet);save('forward-mapping.json',F);save('reverse-mapping.json',REV);N['updated_utc']=NOW;save('next-dispatch.json',N)
p=json.loads((V/'progress.json').read_text());p.update(updated_utc=NOW,manually_authored_finite_source_assertions=len(F['atoms']),source_to_formal_bindings=len(REV['mappings']),finite_new_child_bindings=len(REV['mappings'])-992,original_formal_seed_locators_still_unexhausted=950,new_RC_exact_case_children=len(children),new_RC_exact_rows=14);save('progress.json',p)
a=json.loads((V/'atomic-denominator.json').read_text());a['updated_utc']=NOW;a['manual_bounded_source_assertions'].update(count=len(F['atoms']),id_end=new[-1]['id']);a['finite_reverse_bindings'].update(count=len(REV['mappings']),qualification=f"992historicalregion+{len(REV['mappings'])-992}explicitfinite source/audit/casechildroutes; notfullformaldenominator.");a['RC14_finite']=packet['counts'];save('atomic-denominator.json',a)
l=json.loads((V/'reading-ledger.json').read_text());l['updated_utc']=NOW;l['v2_exact_receptions'].append({'utc':NOW,'path':'RC14-selected-row-complete-child-reception.v2.json','actual_reads':['70f935 fullRC29formalrows','fdbd22 fullWP58L1–98','257ff0 R10whole144','69ccc9+9e7296 Commandwhole265','ee7e01 Other1–66'],'qualification':packet['qualification']});l.setdefault('failures',[]).append({'utc':NOW,'operation':'Read guessed006_Battle_ActionOther.rb','result':'PathnotinfixedR;8aba34failedandgave0credit. Correct008pathlocated98607dandactualcompleteunitreadee7e01.'});save('reading-ledger.json',l)
b=(V/'RC14-selected-row-complete-child-reception.v2.json').read_bytes();print('source',len(F['atoms']),'routes',len(REV['mappings']),'rows',14,'children',len(children),'remainingseeds',950,'bytes',len(b),'sha',hashlib.sha256(b).hexdigest())
