import pathlib,json,subprocess,hashlib,datetime
V=pathlib.Path(__file__).resolve().parent;R='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';B='fd1df570cad987dc3852a3b958f03916e317f7fe';NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
F=json.loads((V/'forward-mapping.json').read_text());REV=json.loads((V/'reverse-mapping.json').read_text());N=json.loads((V/'next-dispatch.json').read_text());assert len(F['atoms'])==2142
paths={'RC-MEGA-PKM':'Data/Scripts/014_Pokemon/002_Pokemon_MegaEvolution.rb','RC-ATTACK':'Data/Scripts/011_Battle/001_Battle/010_Battle_AttackPhase.rb','RC-AI-MEGA':'Data/Scripts/011_Battle/005_AI/004_AI_MegaEvolve.rb','RC-AI-COMMAND':'Data/Scripts/011_Battle/005_AI/001_Battle_AI.rb','RC-TRY':'Data/Scripts/011_Battle/002_Battler/009_Battler_UseMoveSuccessChecks.rb','RC-START':'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb','RC-REGMOVE':'Data/Scripts/011_Battle/001_Battle/004_Battle_ActionAttacksPriority.rb'}
def raw(p):return subprocess.check_output(['git','show',R+':'+p],cwd='/workspace/pokemon-essentials')
def sid(p):
 b=raw(p);return {'repo':'/workspace/pokemon-essentials','commit':R,'path':p,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'blob':subprocess.check_output(['git','rev-parse',R+':'+p],cwd='/workspace/pokemon-essentials',text=True).strip()}
for k,p in paths.items():F['source_identities'][k]=sid(p)
manual=[
 ('RC-ACTIONOTHER','Mega67–102','CanMega checksNO_MEGA switch/hasMega/wild thenDEBUG_CTRLshortcut, elseSkyDrop/ring/ownerpending−1. Ringreadsactualownerbag/items; qualificationalone doesnotregisterMega.'),
 ('RC-ACTIONOTHER','Mega104–130','Register/toggle/unregister writes per-side per-owner pendingbattlerindex/−1; registered? comparesexactindex.'),
 ('RC-COMMAND','Command171–187','Eachnewcommandphase clears nonnegativependingMega entries to−1, retainingalreadyconsumed−2 states.'),
 ('RC-COMMAND','Fight60–88','NormalmanualFight canrequesttoggle−2 beforeeventualsuccessfulmoveregistration; Palaceautomaticreturn occursbeforeopeningthisscene/togglepath.'),
 ('RC-AI-COMMAND','DefaultChoose48–70','AIreturnsafterchosenswitch/item; otherwisecallsAutoFight andreturnsiftruthy beforethe ordinaryMega registration/scoring path.'),
 ('RC-AI-MEGA','EnemyShould6–12','OrdinaryAI Mega policyreturnstruewhentheactualbattle.CanMega gatepasses, elsefalse; itdoesnotdeclineeligibleMegaonadditionalstrategycriteria here.'),
 ('RC-ATTACK','Mega92–100/Attack176–201','AttackphasecallsMegastageafterearlierCall/Switch/Itemanddecisiongates. Megastage requiresnonwild/nonfaintedUseMove andownerpendingentry==battlerindex.'),
 ('RC-ACTIONOTHER','Mega135–175','QualifiedMegaexecutor requestsPokemon.makeMega, updatesbattlerform/stats/scene, marksownerpending−2, triggersabilitycallbacksandoptionalpriorityrecalc. Successassumesallprecedingform/resource/callbackcallsnormal; noall-exitrollback.'),
 ('RC-MEGA-PKM','PokemonMega6–54/Battler145–150','BattlerhasMega rejectsTransformthenasksPokemon.hasMegaForm?; Pokemonlooksupfirstmatchingbase/unmega_formandheldstone/knownmove, makeMega writespositiveformviaordinaryformsetter. Actualvalidregistryinputisexplicitfixturepremise.'),
 ('R05','Recorded18properties/Playbackrestore+Battleconstructor98–174','Recorded18keysomitMega pending/consumedtable. PlaybackconstructsafreshownerMega tableof−1anddoesnotrestoreorrecordcommandsfortoggle; replayingFightdoesnotreconstructtheoldregistration.'),
 ('R03','Palace97–140','NochosenPalacecategorymovesregistersindex−2, storesStruggleobjectinactualchoice andrecordingwrapperwrites[0,−2]becausePalaceregistrationreturn−1istruthy.'),
 ('RC-TRY','TryUse183–297','AfterChooseMove/SkyDrop/HyperBeamearlychecks pass, choiceindex−2 requestsincapablemessageandreturnsfalse beforeaccuracy-skip/status/obedience/hitprocessing. ItdoesnotexecuteordinaryStruggleattack.'),
 ('R05','Playback198–222/class250–252','Palaceplaybackdispatchesnon−1Fightindex−2throughinheritedPalaceregistration, preservingtheindexandStrugglecarrierforthesamesuccesscheck.'),
 ('B17-SWITCH','EORSwitch142–204','Optionalplayer switch-stylequestiononopponentreplacementrequiresinternalBattletrueplusallotherlistedgates. Facilityinternalfalse skipsit anditsadditionalplayerselectionrecord; opponentselectionearliercanstillberecorded.'),
 ('RC-START','Battleconstructor98–174/Ensure16–104/Setup120–165','FreshplaybackdefaultsideSizes[1,1]; withnormalvalidsingleownertrainerpartiesEnsuredoesnotgrowthem andSetupcreatesonlypositions0/1.'),
 ('RC-REGMOVE','Register70–80/R17doublemodify/R05playback4loop','DoublelayoutappliessetBattleModewithoutaddingrecordedruleskey; playbackdoesnotreapplyfactory. Nonemptyposition2/3normalFightthenaccessesabsentbattler.movesduringregistration; slotsbeyond3notread.')]
premise='FixeddefaultR/B8/nooverride; fulloriginalcasepreconditions andnormalvalidobjects/registry/formability/UI/resource/callbacks to eachstatedobservation. W07 earlierChooseMove/SkyDrop/HyperBeam checksnormalpass. W18 validMega-readyoriginalform/owner/ring/pendingstate, ordinarymanualtoggleorAIpathasstated; noextraregistration. W20normalrecordedtrainerbattleoneownerperside/healthysetup, recordedslots2/3normalFight; caseswithextraownersorinvalidrecords mayfailinpriorstartupandarenotmovedlater. Noactualgame/Mega/playback/nativeexecution orfutureRubyAPImandate.'
new=[]
for num,(s,u,m) in enumerate(manual,2143):
 a={'id':f'FAC-A{num:04}','source':s,'unit_locator':u,'assertion':m,'formal_receivers':['RC-W07/W16/W18/W20/W28'],'premise':premise,'pending_dependencies':[],'status':'FINITE_STATIC_MEGALAYOUT_PALACE_REPLACEMENT_CHILD_RECEIVED','evidence':'SOURCE_STATIC','execution':'NOT_EXECUTED','reader':'/root/facility_atomic_completion_cloud'};new.append(a)
F['atoms'].extend(new);F['bounded_denominator']=len(F['atoms']);F['v2_increments'].append({'path':'RC-Mega-Palace-layout-five-row-reception.v2.json','count':16,'ids':[new[0]['id'],new[-1]['id']],'utc':NOW})
children=[]
def c(case,name,m,nums):children.append({'id':f'FAC-RC-{case}-{name}','case':case,'meaning':m,'source_assertions':[f'FAC-A{i:04}' for i in nums],'status':'FINITE_STATIC_CHILD_RECEIVED','premise':premise})
c('W07','record','Palacenocategorymovesproduces[0,−2], usingStruggleobjectcarrier.',[1256,1264,1462,2153])
c('W07','play','Correcttype1dispatchusesPalacePlaybackandPalaceregistrationwith−2.',[1410,1498,2155])
c('W07','fail','Onceearlierexecutiongatespass, −2firesincapablemessage/false beforeordinaryhitprocessing.',[2154])
c('W07','not-struggle','Thisisincapablesentinel, notsuccessfulordinaryStruggleattack.',[2153,2154])
c('W16','gate','FacilityinternalBattlefalseprecludesoptionalopponent-switchstyleconfirm.',[164,2156])
c('W16','no-extra','Thatabsentquestioncreatesnoextra playerSwitchInBetweenentry; doesnoteraseearlieropponentreplacemententries.',[1460,2156])
c('W16','counterpart','Internaltrue isnecessaryandnotalone sufficient; otherlistedstyle/single/opposes/healthy/bench/Outrage gatesmustalsohold.',[2156])
c('W18','manual','Tower/Arena normalFightwithvalideligibilityandexplicitMegatogglewritesactualpendingstate, thenmoveregistration.',[2143,2144,2146])
c('W18','AI','EligibleordinaryAIafterunsuccessfulswitch/item/AutoFight=false registersMega.',[2147,2148])
c('W18','execute','ReachedordinaryattackstagevalidUseMove/pendingindex invokesactualMegaexecutor.',[2149,2150,2151])
c('W18','qualification','Eligibilityalonewithouttoggle/AIregistrationdoesnotproduceMega.',[2143,2144,2149])
c('W18','record-omit','Recordedproperty/commandmechanismomitsMegastate; itdoesnotcancelactualoriginalregistration.',[2152,1456])
c('W18','replay','FreshplaybackMegaentries−1anddirectFightdispatchdo notreconstructtheoriginalMegaexecution.',[2152])
c('W20','default','Restoredregulartrainerdouble-recordstartsstilldefault1v1.',[2157])
c('W20','not-restored','18keysomitlayout; doublebattlemodifiernotrecordedruleskeyandfactorynotreapplied.',[1456,1486,2158])
c('W20','missing','Onnormalfirst2/3Fightcommandregistrationabsentbattlerreadfails, even thoughvalidoriginaldoublehadthatposition.',[1494,2158])
c('W20','beyond-four','Recordedslots≥4areignoredbyexactfour-loop.',[1494])
c('W28','clear','Commandphaseclearsoldpendingnonnegativeentriesbeforeplayers/AIchooseagain.',[2145])
c('W28','player','NoEncore+regularchoosablemove entersPalaceAutoFightbeforemanualMegatoggle, soPlayerFightaddsnonewMega.',[2146,2153])
c('W28','AI','AINoSwitch/NoItem PalaceAutoFighttrue returnsbeforeordinaryMegaregister.',[1297,2147])
c('W28','none','Withnoexternal/debugregistration, attackpendinggatefindsnoregisteredindex, soqualificationdoesnotcauseMegaexecution.',[2149,2152])
c('W28','contrast','Tower/ArenaexplicitregistrationcontrastandactualregisteredbutunrecordedMegastateremainunchanged.',[2146,2149,2152])
byid={a['id']:a for a in F['atoms']}
for ch in children:
 assert all(x in byid for x in ch['source_assertions'])
 for aid in ch['source_assertions']:
  a=byid[aid];REV['mappings'].append({'formal_clause':ch['id'],'atomic_assertion':aid,'meaning':ch['meaning'],'source':a['source'],'source_unit':a['unit_locator'],'premise':premise,'status':ch['status'],'pending_dependencies':[],'relation':'COMPLETE_RC_MEGA_PALACE_LAYOUT_CHILD'})
REV['true_bounded_assertions']=len(F['atoms']);REV['v2_new_exact_child_bindings']=len(REV['mappings'])-992
s=F['source_identities']['F07'];ss=subprocess.check_output(['git','show',B+':'+s['path']],cwd=s['repo']).decode().splitlines();groups=[]
for case in ['W07','W16','W18','W20','W28']:
 hit=[(i,t) for i,t in enumerate(ss,1) if i>=156 and t.startswith('| '+case+' |')];assert len(hit)==1;line,text=hit[0];old=f'F07-L{line:04}';h=[x for x in N['unmet_formal_seed_structures'] if x['old_locator_id']==old];assert len(h)==1;N['unmet_formal_seed_structures'].remove(h[0]);child=[x['id'] for x in children if x['case']==case];N['closed_finite_formal_seed_structures'].append(dict(h[0],case='RC-'+case,children=child,status='FINITE_STATIC_CHILD_RECEPTION_COMPLETE',receipt='RC-Mega-Palace-layout-five-row-reception.v2.json'));groups.append({'case':case,'old_locator_id':old,'line':line,'complete_original_row':text,'children':child})
assert len(N['unmet_formal_seed_structures'])==942
units=[]
for key,ranges,read in [('RC-ACTIONOTHER',[(67,175)],['a49274']),('RC-ATTACK',[(92,100),(176,201)],['a49274','30a6a5']),('RC-MEGA-PKM',[(1,83)],['a49274']),('RC-AI-MEGA',[(1,13)],['540d1b']),('RC-AI-COMMAND',[(48,70)],['e84a2f']),('B17-BATTLER',[(145,150)],['e84a2f']),('R03',[(97,140)],['e84a2f','7a3b1b','priorown245whole']),('RC-TRY',[(183,297)],['9ed391','d3c2d4','7a3b1b']),('B17-SWITCH',[(142,204)],['c6711b']),('B17-BATTLE',[(98,174),(182,211)],['635fce']),('RC-START',[(16,104),(109,118),(120,165)],['96d86a','870091','98521c']),('RC-REGMOVE',[(5,18),(20,32),(36,68),(70,80)],['efa5c1'])]:
 st=F['source_identities'][key];ll=raw(st['path']).decode().splitlines(keepends=True)
 for lo,hi in ranges:units.append({'identity':st,'range':[lo,hi],'content':''.join(ll[lo-1:hi]),'actual_read':read,'qualification':'Complete namedmethods/wholeMegaPokemon83/AI13filetextonlyasactualread. No wholeBattle867/AI/Move/Item/formdomaincallbackcredit.'})
packet={'schema':'facility-RC-Mega-Palace-layout-five-row-finite-child-reception/v2','utc':NOW,'reader':'/root/facility_atomic_completion_cloud','formal_identity':s,'common_premise':premise,'rows':groups,'explicit_case_children':children,'new_manual_source_assertions':new,'complete_supplemental_units':units,'actual_read_basis':['a49274/e84a2f/540d1b fullMegaregister/executor/AI/Pokemonneededdefs','9ed391+d3c2d4 fullTryUseMove183–297','c6711b fullEORSwitch142–204','635fce constructor98–174/defaults/mode','96d86a+870091+98521c fullEnsure/Create/Setupmethods','efa5c1 completemoveregistrationhelpers','priorwholeR03/R17/RecordedR05 andF07/F05actualread'],'counts':{'new_complete_RC_rows':5,'new_case_children':len(children),'total_RC_rows':22,'total_RC_children':77,'finite_manual_source_assertions':len(F['atoms']),'finite_reverse_bindings':len(REV['mappings']),'remaining_original_seeds':942},'qualification':'Thelistedcasegates/sourceprefixesactuallyreceived; eligibilityasactualvalidfixturedoesnotgrantallprimaryMega/callback/itemdataqualification. W16noextraquestionrecorddoesnotdenyopponentreplacementrecord. W20sourcefirstfailure scopednormaloneownertrainerstartup, notallmalformedmultitrainerrecords. CurrentB8allshownPalace/record/layoutMega distinctionsalreadycorrect; no newfinding.','OPEN':['RemainingRCW04/W10/W11/W24/W25/W26/W27 fullmeaning/callerqualification','OtherSF/PA/QC/WS942seedstructures/202external and453/649/2732primaryproofinputqualification','Allnecessaryworldprepare/ejectpack andattackreplacementprefixesstilltoconsume, noactualruntime/nativeexecution'],'new_required':0,'new_optional':0,'new_contexts':0,'new_votes':0,'business':'NOT_EXECUTED','UPDATE_NOT_STARTED':True,'wholeFAC_complete':False}
def save(n,d):(V/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
save('RC-Mega-Palace-layout-five-row-reception.v2.json',packet);save('forward-mapping.json',F);save('reverse-mapping.json',REV);N['updated_utc']=NOW;save('next-dispatch.json',N)
p=json.loads((V/'progress.json').read_text());p.update(updated_utc=NOW,manually_authored_finite_source_assertions=len(F['atoms']),source_to_formal_bindings=len(REV['mappings']),finite_new_child_bindings=len(REV['mappings'])-992,original_formal_seed_locators_still_unexhausted=942,new_RC_exact_case_children=77,new_RC_exact_rows=22);save('progress.json',p)
a=json.loads((V/'atomic-denominator.json').read_text());a['updated_utc']=NOW;a['manual_bounded_source_assertions'].update(count=len(F['atoms']),id_end=new[-1]['id']);a['finite_reverse_bindings'].update(count=len(REV['mappings']));a['full_original_atomic_denominator']['unmet_original_paragraph_table_locators']=942;a['RC_Mega_Palace_layout']=packet['counts'];save('atomic-denominator.json',a)
l=json.loads((V/'reading-ledger.json').read_text());l['updated_utc']=NOW;l['v2_exact_receptions'].append({'utc':NOW,'path':'RC-Mega-Palace-layout-five-row-reception.v2.json','actual_reads':packet['actual_read_basis'],'qualification':packet['qualification']});l.setdefault('failures',[]).append({'utc':NOW,'operation':'Guessed018/.../006_BattlePalace.rb read','result':'d4fb32 missingpath0credit; correctR03identitye84a2fused. Sourceotherfailedpathdoesnotgrantreading.'});save('reading-ledger.json',l)
b=(V/'RC-Mega-Palace-layout-five-row-reception.v2.json').read_bytes();print('source',len(F['atoms']),'routes',len(REV['mappings']),'rows',5,'children',len(children),'remaining',942,'bytes',len(b),'sha',hashlib.sha256(b).hexdigest())
