import pathlib,json,hashlib,subprocess,datetime
P=pathlib.Path(__file__).resolve().parent;RR=P.parent.parent;R=pathlib.Path('/workspace/pokemon-essentials');C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';now=datetime.datetime.now(datetime.timezone.utc).isoformat();mp=P/'manual-atomic-clauses.json';op=P/'old-locator-disposition.json';m=json.loads(mp.read_text());o=json.loads(op.read_text());records=[]
def identity(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(RR)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
parents=dict(manual=identity(mp),old=identity(op));units=[]
def unit(path,start,end,reading):
 b=(R/path).read_bytes();assert b==subprocess.run(['git','show',C+':'+path],cwd=R,capture_output=True,check=True).stdout;a=b.decode().splitlines(keepends=True);text=''.join(a[start-1:end]);assert end<=len(a)
 units.append(dict(id=f'{path}:{start}-{end}',path=path,commit=C,parent_bytes=len(b),parent_sha256=hashlib.sha256(b).hexdigest(),parent_blob=subprocess.run(['git','rev-parse',C+':'+path],cwd=R,capture_output=True,text=True,check=True).stdout.strip(),range=[start,end],text=text,text_sha256=hashlib.sha256(text.encode()).hexdigest(),actual_reader='/root/core_atomic_reception',actual_read_scope=reading))
unit('Data/Scripts/003_Game processing/003_Interpreter.rb',80,82,'Whole running? method352979; parentPARTIAL.')
unit('Data/Scripts/003_Game processing/003_Interpreter.rb',183,194,'Whole get_character e8429c; parentPARTIAL.')
unit('Data/Scripts/003_Game processing/003_Interpreter.rb',200,202,'Whole get_self695224; parentPARTIAL.')
unit('Data/Scripts/004_Game classes/001_Switches and Variables/004_Game_SelfSwitches.rb',1,24,'Whole24L real read7fe0a3; new ownFULL tiny wrapper, not save/wholeWORLD.')
unit('Data/Scripts/012_Overworld/002_Battle triggering/003_Overworld_WildEncounters.rb',24,27,'Whole reset_step_count cc03b7; parentPARTIAL.')
unit('Data/Scripts/004_Game classes/002_Game_System.rb',22,22,'Whole attr_accessor declaration; parentPARTIAL.')
unit('Data/Scripts/004_Game classes/002_Game_System.rb',44,103,'Six whole BGMplay/internal2/internal/pause/unpause/resume methods1a0083; parentPARTIAL, read end103 included.')
unit('Data/Scripts/011_Battle/004_Scene/001_Battle_Scene.rb',336,349,'Whole swap-sprites215495; parentPARTIAL.')
unit('Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb',60,70,'Whole ShowPartyLineup5bb68a; parentPARTIAL.')
unit('Data/Scripts/011_Battle/004_Scene/004_Scene_PlayAnimations.rb',93,156,'Whole SendOut5bb68a plus fb43c1 complete end156; not stopped at155. ParentPARTIAL.')
unit('Data/Scripts/012_Overworld/001_Overworld.rb',340,369,'Whole FacesPlayer779b5c; parentPARTIAL.')
unit('Data/Scripts/012_Overworld/001_Overworld.rb',372,392,'Whole CanReachPlayer779b5c; parentPARTIAL; map passage predicates conditional, no whole map approval.')
unit('Data/Scripts/004_Game classes/008_Game_Player.rb',284,298,'Whole TriggeredTrainerEvents804a35 and prior own actual unit reuse; parentPARTIAL.')
unit('Data/Scripts/004_Game classes/006_Game_Character.rb',237,258,'Whole passable? dd7818; parentPARTIAL.')
unit('Data/Scripts/004_Game classes/006_Game_Character.rb',260,300,'Whole can_move_from_coordinate?7a064a; parentPARTIAL.')
unit('Data/Scripts/004_Game classes/006_Game_Character.rb',352,354,'Whole jumping?81e413; parentPARTIAL.')
unit('Data/Scripts/004_Game classes/007_Game_Event.rb',133,140,'Whole over_trigger?0a3139; parentPARTIAL.')
def bind(n,meaning,refs):
 key=f'CORE-C{n:04d}';r=next(x for x in o['rows']if x['id']==key);assert not r['all_children_received'];aa=[x for x in m['rows']if x['old_locator']==key];assert set(r['manual_atom_ids'])==set(x['id']for x in aa)
 records.append(dict(old_locator=key,prior_remaining_labels=r['missing_action'],complete_existing_children=[dict(id=a['id'],canonical_object_sha256=hashlib.sha256(json.dumps(a,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest())for a in aa],new_manual_meaning=meaning,reused_actual_evidence=refs,conditional_finite_chain_complete=True,all_recursive_domains_accepted=False))
 r.update(all_children_received=True,status='RECEIVED_BOUNDED_WORLD_UI_INTERFACE_STATIC',missing_action=[],consumer_rebinding=dict(packet='world-ui-finite-remainders.v1.json',utc=now,meaning=meaning))
 for a in aa:a.update(pending_consumers=[],support='SUPPORTED_BOUNDED_WORLD_UI_INTERFACE_STATIC',consumer_rebinding=dict(packet='world-ui-finite-remainders.v1.json',utc=now,meaning=meaning,not_native_execution=True))
bind(42,[
 'Own wrapper actual noWaiting/mapInterpreterRunning/doublecapacity gates now bind running?(!listnil), get_self→get_character(0)→currentmap.events[eventid]. Existing TrainerData213/loader124 real parsing/objectload and fullslot viability facts reused.',
 'Whole finder source explicitly trigger membership, trainer/sight regex+distance, CanReach, jumping and over_trigger exclusions. Whole Face/CanReach/move-from-coordinate/passable/jumping/overtrigger definitions now actually read; directional footprint corridor calls peredge map passage and collision checks, not rendered priority.',
 'Normal current map/events and each passage predicate are concrete supplied world-domain inputs; this clause asserts filter/fixture behavior, not all map transfer/tilemodel semantics. A-switch missing=>false/existing==true, ownself exclusion/exactone/oneTrainer/MAXPARTY thenwaitingobject+eventid andfalse occur in source order. Failure beforestore leaves no newwaiting; loader earlier state mayalreadycommit.'
],['Own BattleStarting749 and real TrainerData/loader binding04','Contained complete interpreter/selfswitch/finder/reach units','BC22 exact conditional sourcefixture already reviewed; no Demo execution'])
bind(43,[
 'Saved waitingTrainer is appended as same object, real load_args preserves it without anotherloadhook, while newdatainputs mayload. Own fullBattleStarting/data/loader+event interpreter currentmapID behavior retain exactkeys.',
 'Only normalcore result1 writes GameSelfSwitch key[currentmapid,waitedeventid,A] totrue thenneed_refresh; actual wrapper getter returns raw==true and setteronlyhashwrite. Normal continuation clears waiting, earlier core/switch/refresh error doesnotensureclear.',
 'This is conditional mutation/caller timing, not a promise every later page event/render or save reload succeeds. No whole WORLD dependency remains for these six exact write/ordering children.'
],['Own BattleStarting749; consumer-rebinding04 trainer/partner data fullbinding','Contained complete24L GameSelfSwitches/currentinterpreter methods; no entire map saveapproval'])
bind(62,[
 'Skip clearRules follows normallyreturned skipmessage; truthymemorizedBGM plus Game_Systeminstance reaches bgm_pause default0→assignsavedposition→bgm_resume before memos/4nextfields and encounterreset.',
 'Actual pause rescues Audio.bgm_pos ordinaryerror to0 thenwritespos/pausedtrue; suppliedsavedposition then resume calls internalplay onlyifpaused, resettingpos0/pausedfalse onlyafter normalplay. Internalplay cancommit playingBGM/pos before existence/Audio/Graphicsfailure; native accepted sound is not promised.',
 'Only reached latercode clearsmemo/currentpositions andnextBGM/victory/capture/background thenresetboth step_count0/chance_accumulator0. Any earlier callbackerror prevents laterclear; no ensure. Own fullskip and contained completeSystem/reset receivers close exactgap.'
],['Own BattleStarting749; KERNEL actualpbSet/mapswitch contributions','Contained GameSystem44–103/positionattr22 and Encounterreset24–27','Actual MEDIA rawprefix/existence5facts; nativeactualplay stillNOT_EXECUTED'])
bind(95,[
 'Own complete StartSendOut side[1,0], trainerarray order and playerlast joins actual pbDisplayBrief delegate/whole UI67 message gate and complete Scene SendOut93–156.',
 'SendOut waits pendingparty animation, choosesopposing/playerfade from actual firstslot, currentIllusion or suppliedPokemon sprite, refreshes, creates correctowner animations/dataBox, updates/disposes thenconditionallyShiny. Message/animation/refresh failures canstopbeforelaterparty/side; exact normalcallordering is not native displayguarantee.'
],['Own StartEnd568/AbilityItem476/Initialize325','UI67-U003/U013/U018 completefacts actually received','Contained whole SceneSendOut93–156; no parentSceneFULL'])
bind(96,[
 'Own full startup Message case count1/2/3 forfoeParty oropponentTrainer choosesexactnames; no defaultmessage invented forotherlength. WholeUI message/pausedwait facts bind realrequest/normalreturn.',
 'Graphics/Input actualdrawing/confirm native is unexecuted; claimconcerns reachednamedmessage/case selection, not a guaranteed on-screenframe. Earliermessagefailure canpreventlaterstart.'
],['Own StartEnd568/Battle867','Actual whole UI67-U003 three message/wait gate facts'])
bind(98,[
 'Own complete StartBattle main/setup→AIcreate→Scenestart→SendOut→Weather→Terrain→AllEntering→BattleLoop stages joined to whole AI001 create_ai_objects, selected complete wrapper/trainer/move constructors and actual UIinitialize/SendOut definitions.',
 'Own whole BattleWeather81/Terrain58 supply rawID-animation metadata plus current weather/terrainrecords; wholeSwitch469 AllEntering exactfullcalc/entry/incremental/postform method nowexplicitly bound. Concrete effects retain forwardWP49/individualfacts; this stage row doesnot assert their entirebehavior.',
 'Normalstage returnthenloop Command/Attack/EOR with decisionguards and failuresprefix established fromownwhole StartEnd. No promise every callback/nativeframe returned or everyAIheuristicapproved.'
],['Own StartEnd568/AI001163/AITrainer100/Switch469/BattleWeather81/BattleTerrain58','Actually received AI selected12units/7joins and UI67-U001/U013/U018','SourcefactsF033/F041–044/F051 namedinterfaces'])
bind(101,[
 'Correct known WP41 rankhole statement remains: actual sendoutpartyorder mutations give2+2double[0,1,3,2],5membertriple[0,1,4,3,2]; healthy sameowner explicit B0→B1 replacement andILLUSION/noeffectiveGas witness is conditionalchosenlegalreplacement, not proofAIwillchooseit.',
 'Own complete RecallReplace/membership/partyorder/Illusion query calls fail beforebinding afterearlier leave/lineup/messagesprefix. Actual finiteAI eligiblecandidate and UIparty/requestinterface support callablechoice without allrankings; no nodefaultopeningfailurefromhole alone.',
 'Real Scene output andAIplan remain separately limited justasformalexplicitly says. Old missingAIactualselection cannotblock an expressly userchosenhealthyvector; no newcandidate/reopeningcorrectclause.'
],['Own Switch469/StartEnd568/Battle867/AbilityItem476/AI002 completeclass','consumer-rebinding04 and actual AIU004 full candidate/result object','Actual UI67 message/party finite units; knownexistingNPC boundedscope preserved'])
bind(106,[
 'Own full Battle geometry/allBattlers/abilityqueries and Battler DirectOpposing establish readonly ordering, firstexistingfaintedbreak/fallback and independentnear predicate, no guaranteealive.',
 'Own full CatchStore271 actual Throw112 onward choosesexplicitopponentorDirectOpposing(true), theniforiginalfainted uses allAllies[0] before laterfaint/no-target/presentation. Current allAllies livingfilter canprovidealternate; nil/missingobject canraise ratherthan rawqueryaloneuniversalfailedcapture.',
 'UI initialtarget uses its own index/text/registration method andmaintained-state executionfilters. Complete actual targetresolver/body was alreadyownFULL, nowexplicitbind; allballcatchrate/effectcallbacks not needed to prove rawquery≠finaltarget distinction.'
],['Own Battle867/Battler777/Target185/Targeting203/CatchStore271','Actual freshtargetprefix97cf46 and sourcefactF028/F050 geometries','UI67-U009 wholeunit previouslyactuallyreceived'])
bind(107,[
 'Own full SwapBattlers object/index/choice writesprecede actual Sceneswap336–349; Scene sequentialswapPokemon/shadowrefs/lastCmd/lastMove, changespriteindices/positions/dataBoxbattler thenrefresh has real partialfailurepoints.',
 'OnlynormalSceneswapreturn reaches liveallBattlers10 namedpointereffectremaps; LeechSeed/Perishsource/position-owned effects retain their actual exceptions. Wholecontained method closesdirectreceiver, with nativeSprite/Graphicscalls explicitlyconditional.',
 'Formal registers interface/limits only; doesnot guarantee everyimageposition/nativeeffectafterfailure, nor implypartyslot/orderrepair. No wholeUI/runtime transfer.'
],['Own Other201/Battle867/Battler777 and allactualswappointermanualchildren','Contained wholeSceneSwap336–349; actual UI67-U001/U011/U012 finite sprites/HPfacts'])
bind(144,[
 'Whole actual UI67-U020 requestgetter and MEDIA5path/source facts cover formalcommonpremise validtypes/metadata/conversion/nooverride. Definition selectsrequest, not resourceexistence/audibleoutput.',
 'MEDIA distinguishesnormalGame_System rawprefixedstring existence→Audio from lastfallbackcanonicalize. UnreceivedcompatibilityRPG actualclass/noSystem hostexecution is a declared alternate/native boundary; normalconditionalrequestclause doesnot needits totaloutcome.'
],['Actually completeUI67-U02039facts and MEDIA5audio/9datafacts','Mandatory actual audio caller correction3905B plusmanifest7007B'])
bind(147,[
 'WholeUI getter nextVictoryclone→validmapwild→validglobalwild→default plusnonpreset../../Audio/BGMprefix joinsactual complete wildSceneSuccess408–418.',
 'Mandatory actualcaller correction provesnormalwildvictoryBGM and reachedsuccess/update code; MEDIA normalSystem/rawpath facts delimitrequest/exists/native. SourcefullremainsoriginalUIreader, no realaudioexecutioncredit.'
],['UI67-U020/actual whole correctioncaller methods3905B','media-reception.mandatory-audio-caller-correction.v1.json + deliverymanifest mandatory','MEDIA rawsource path5facts'])
bind(148,[
 'IndependentcaptureME nextclone→mapwild→globalwild→default withnonpreset../../Audio/MEprefix joinsactual completeThrowSuccess344–354, whichreturnstrainerearly.',
 'NormalnontrainercaptureME→Graphics/update3.5seconds loop→MEStop is conditionalactualsourcepath. No trainerSnag sameME andnoguaranteeeveryhostclock/update returns; partialME/waitprefix retained.'
],['UI67-U020/U015 wholefinitefacts and actualcaller correction3905B','Mandatory audio3905B/7007B completepackets','MEDIA normalSystem/rawpath5facts'])
bind(149,[
 'Ordinary trainercore getBGM strictType lookup andorderedlastnonnil/emptyfallback→map/global/default joined toactual BattleAnimation request and completeintro/standby finite wrappers.',
 'NextBattleBGM clonedreturn, failuresbeforetransition andnormalcleanupafteryield are separate. Whole actualwrapper alreadyread in consumer-rebinding03; nativeaudio/transitions notexecuted andnoensurepromise.'
],['UI67-U020complete39facts','consumer-rebinding03 completeAnimation/Standby binding','Own BattleStarting749/ChallengeBattles144; ordinarycorrectscopepreserved'])
bind(150,[
 'Whole trainerVictorygetter orderedtype/nextclone/emptyfallback/map/global/default/prefix joinsactual complete SceneTrainerSuccess and BGMchannel in mandatorycaller correction.',
 'Normalrequestpath notcanonicalizeassurance/nativeformat/playresult. Earlierclear/message/fieldprefix orlaterAudiofailure remains actualsourceorder; no newroot/ticket.'
],['UI67-U020 and actual audio caller correction3905B/manifest7007B','MEDIA completeSystem/rawprefix5facts','Own StartEnd568 actualtrainerwinreceiver'])
bind(153,[
 'Actually fullUI67-U020 introhelper suppliesstrictType/conversionbeforememo, existingmemo retain, pendingdelaynil/cue+pos0 elseplayingBGM+rescuedposition, memo-beforeplay. Directeventcalling ofdefinedhelper is conditional, not a newDemoeventreachabilityclaim.',
 'Ordinary core→Animation, realvictoryBGM/captureME plus3.5sec/trainerexception nowexplicitlyactualreceivedcorrection; skip clearswithoutcreating; wildoverride cantruncate ordinarycore. Normalyieldcleanupdistinctarbitraryfailure.',
 'NormalGame_Systempause/resume completecontained methods andown resetreceiver closeexactlocalmemcleanup. Otherdynamic event/nativeactualtiming remainqualifications, no unseen ordinarycall inserted.'
],['UI67-U020whole39facts/media-reception complete5+9facts','Own BattleStarting749/EncounterModifiers73; consumer-rebinding02/03','Mandatory F05412899B and audio3905B/7007B exactactualreceptions'])
bind(430,[
 'Own Switch fullsideSize==1 check occurs afterleavecleanup/beforemessage; contained SceneShowPartyLineup60–70 receiveswholepbParty(side)/partyStarts(side), pushesLineupAppear, normalnonfullAnimwaitspartyupdate.',
 'Actually wholeUI67-U013/U018 completefinitepartylineup definitionfacts supportwhole-party source request; nativepixels/time/input notexecuted. Multi-seat skipunaffectedbyremaininglivingcount, no partyorderrepair/registration inferred.'
],['Own Switch469/Battle867 with modegettersmandatorycompletion','Contained wholeShowPartyLineup and actual UI67-U013/U018 originalcompleteobjects'])
out=P/'world-ui-finite-remainders.v1.json';packet=dict(schema='car-world-ui-exact-finite-receiver-bindings/v1',utc=now,reader='/root/core_atomic_reception',prior_canonical_parent_identities=parents,records=records,new_or_precisely_refreshed_complete_source_units=units,actual_selected_formal_children_refresh='a72941 all16formal/remaining/childassertions untruncated; own prior complete source/provider/common premises reused exactly.',common_premise='FixedR/B8, currentvalidmap/event/trainer/registereddata objects andnormalnamedcallbackreturns onlyuntilspecifiedfailure; no plugin/concurrentmutation. Reach filter delegatesvalidmap passage; no wholecollision/tilemodel/save-domainapproval.',common_failure='Onlyreached statewrites survive; noautomaticrollback/ensure/cleanup/hostoutput. NativeGraphics/Input/Audio andmaptransfer execution NOT_EXECUTED.',all_CORE_complete=False,new_required=0,new_optional=0,new_contexts=0,new_votes=0,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');out.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
m['updated_utc']=now;o['updated_utc']=now;mp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');op.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
g=P/'coverage-gaps.json';d=json.loads(g.read_text());d['updated_utc']=now;d['decomposed_but_foreign_join_open']=[r['id']for r in o['rows']if r['manual_atom_ids']and not r['all_children_received']];g.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
ledger=P/'reading-ledger.json';d=json.loads(ledger.read_text());seen=set()
for u in units:
 if u['path']in seen:continue
 seen.add(u['path']);same=[x for x in units if x['path']==u['path']];full=u['path'].endswith('/004_Game_SelfSwitches.rb');d['entries'].append(dict(path=u['path'],ranges=[x['range']for x in same],bytes=u['parent_bytes'],sha256=u['parent_sha256'],reader='/root/core_atomic_reception',status='FULL_FILE_READ'if full else'PARTIAL_READ',semantic_pass=False,recorded_utc=now,actual_read_scope='; '.join(x['actual_read_scope']for x in same),io='Actual named untruncated tool reads contained inpacket; recordedUTC isappendtime, no backfilled readingtime.'))
ledger.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');p=P/'progress.json';d=json.loads(p.read_text());d['updated_utc']=now;d['old_locators_complete']=sum(r['all_children_received']for r in o['rows']);d['source_full_read_total']=71;d['source_support_additional_full_read']=43;d['world_ui_exact_rows_completed']=16;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');b=out.read_bytes();print(out.name,len(b),hashlib.sha256(b).hexdigest(),'rows',len(records),'newunits',len(units),'open',len(json.loads(g.read_text())['decomposed_but_foreign_join_open']))
