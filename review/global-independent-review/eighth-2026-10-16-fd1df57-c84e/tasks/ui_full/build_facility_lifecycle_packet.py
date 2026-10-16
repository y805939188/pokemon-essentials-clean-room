import json,hashlib,subprocess,datetime
from pathlib import Path
T=Path('review/global-independent-review/eighth-2026-10-16-fd1df57-c84e/tasks/ui_full');R=Path('/workspace/pokemon-essentials');C=Path('/workspace/pokemon-essentials-clean-room');now=datetime.datetime.now(datetime.timezone.utc).isoformat()
specs=[('R','Data/Scripts/018_Alternate battle modes/001_Battle Frontier/004_Challenge_Battles.rb',None),('R','Data/Scripts/011_Battle/008_Other battle types/005_RecordedBattle.rb',None),('R','Data/Scripts/011_Battle/008_Other battle types/004_BattleArenaBattle.rb',[[1,219]]),('R','Data/Scripts/011_Battle/001_Battle/005_Battle_ActionSwitching.rb',[[95,245],[274,394]]),('R','Data/Scripts/011_Battle/003_Move/013_MoveEffects_SwitchingActing.rb',[[1,147]]),('R','Data/Scripts/011_Battle/002_Battler/010_Battler_UseMoveTriggerEffects.rb',[[87,190]]),('R','Data/Scripts/011_Battle/002_Battler/007_Battler_UseMove.rb',[[154,582]]),('B','deliverables/final-specification-set/combat-requirements/wp54-entry-eligibility-level-adjustment-and-clauses.md',[[43,50],[72,104]]),('B','deliverables/final-specification-set/combat-requirements/wp56-palace-and-arena-variants.md',[[83,128]]),('B','deliverables/final-specification-set/combat-requirements/wp58-battle-recording-and-playback.md',[[87,137]])]
sources=[]
for side,path,ranges in specs:
 repo=R if side=='R' else C;commit='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b' if side=='R' else 'fd1df570cad987dc3852a3b958f03916e317f7fe';tree='7589c800b61ba13a13040ed0d686979b80a84fd0' if side=='R' else '751dfde81048c81390f89a65ca1d1a565ba8e1ca';raw=(repo/path).read_bytes();n=len(raw.splitlines());full=ranges is None
 sources.append(dict(repo=str(repo),commit=commit,tree=tree,path=path,blob=subprocess.check_output(['git','rev-parse',commit+':'+path],cwd=repo,text=True).strip(),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),mode='100644',lines=n,reader='/root/ui_full',whole_file_read=full,status='FULL_READ' if full else 'PARTIAL_READ_COMPLETE_NAMED_UNITS',ranges=ranges or [[1,n]]))
texts=[
'Base BattleType creates ordinaryBattle; Tower/Palace/Arena create correspondingRecordedBattleclass with bothactualtrainerpartyreferences.',
'Organized CTRLheld+DEBUG branch displaysskip/won/lose_text, clearlastrecord, MEStop, true beforeheal/adjust/create; exception stops atactualprefix.',
'Normalorganized firstplayer.heal_party, nilrules defaultnewPokemonChallengeRules, thenadjustLevels andreturnedoldlevels; olditem arrayscaptured onlyafteradjustreturns.',
'Scenecreated thenrulebattlecreated theninternalBattle=false then prepare_battle. Prep canoverrideearlierlayout perexistingpreparedfieldscope, not runtimeguarantee.',
'Battle runs inpbBattleAnimation+pbSceneStandby, resultdecisioncaptured; normalreturnInput.update beforeunadjustLevels.',
'Unadjust bycurrentbothpartyindices throughreceivedFAC-R16; wholelevels originalidentitynotrematched. Missing EXP skips as sourcehelper, currentchangedEXPonlywrite/calcstats.',
'Player eachheal/unmega/unprimal/item=olditems[i], thenopponent same. Missingitemindex returnsnil andwritesnil, differentfrommissingEXPskip. A failuremidplayer leavesearlierdone/opponentnotstarted.',
'Afterrestore clear lastrecord, decisions1/2/5 dumpsrecord;statwononly1, lost2/3/5; trueonlydecision1. Noneofthese guarantees normalrecovery afterbattleexception.',
'No ensure wrapsadjustment/battle/unadjustment/heal/itemrestore; earliercompletedprefixretained atthrowpoint, no universalatomicity.',
'RecordLastBattle assigns global.lastbattle=temp.lastrecord thenclearstemp; nilalsoassignable. PlayLastBattle delegatescurrentglobalrecord.',
'PlayBattle nilreturns; nonnilcreatesabortablescene thenMarshal.restore, dispatchtype0/1/2recordplayback, choosesBGM, animation/standby/start. Unknowntype hasno fallbackplayer; no wrapperlevel/itemrestore.',
'Debugplay chooser0..500cancel-1; nonnegativechoosesBattles/Battle%03d.dat andreadsbytes viapbRgssOpen thenPlayBattle; noexecutionorfileguarantee.',
'Recordedinit randomnumbers[],rounds[],switches[],roundindex-1,properties{} thensuper. Attr randomnums differsactualrandomnumbersfield butnoassertednewissue.',
'Recordedtrainerinfo arrayeach Player4tuple type/nameclone/id/badgesclone; NPC5tuple type/nameclone/id/losetextfallback/wintextfallback. Baretrainerbranch usestrainer[i] beforeitsPlayerpredicate; not generalizedsuccess.',
'Prestartproperties filledsequentially BEFOREsuperbattle start: internalBattle/player/opponent/party1dump/party2dump/party1startsdump/party2startsdump/weather/weatherDuration/canRun/switchStyle/showAnims/itemsdump/backdrop/backdropBase/time/environment/rulesdump.',
'pbDumpRecord dumps[type,properties,rounds,randomnumbers,switches] withtypenormal0/Palace1/Arena2; fiveobjecttuple/noformatversionbuiltin.',
'Recorded pbSwitchInBetween calls super thenpushreturnedret thenreturn; negative-1andnilnotfiltered. Superexception doesnotpush, pushfailure doesnotnormalreturn.',
'RegisterMove onlysupertruthy stores[FIGHT,idxMove] andtrue; targetregistration callsuper thenwrites slot2. Run callsuperthenwrites[RUN,decision] andreturnsoriginalret.',
'AutoChoose callsuperthenwrites[FIGHT,-1] regardlessreturnedtruthiness. RegisterSwitch/Item onlysuccessfulsuperwrite; Item storesitem/target/move. No automaticcancelcleanup.',
'Commandphase incrementsroundindex thenallocatesexactfouremptyslots BEFOREsupercommandselection. Random callsuper(num),appendresultthenreturn. RecordedStorePokemonnoop.',
'Playback init borrowsarrays fromdecodedtuple, resets3indices, restoresparties/trainers then super. Start restores starts/internal/weather/duration/run/style/anims/backdrop/base/time/environment/items/rules sequentially thensuper.',
'Playbackswitch/random directlyfetchcurrentindexthenincrement andreturn; outofboundsniladvances. No localguardorrevalidation/realquery.',
'Playback commandphase onlyplayer branch incrementsround andfixed4loop; direct.length onmissinground/slot canfail. Eachnonemptyslotclearthenactiondispatch; FIGHT-1auto otherwiseRegisterMove, optionaltarget; BAG/SWITCH borrowedregistrations; RUNdecisiondirect.',
'RecordedandplaybackTower/Palace/Arena classinheritanceandmoduleinclusionareexplicit; actualfacadeBattleType factorybindsmodules. ReplaykeepsmodebaseArena/Palace behavior.',
'PlaybackHelper buildsnewPlayer4tuple orNPC5tuple bystoredlength; setsbadgesorwin/losefallbackthenid; returnsarray. BGM createsopponentfromstoredprops. Constructor failures keeppriorlocal/persistentprefix, no alltrainerdomainapproval.',
'ArenaSuccess.clear resetsnormaltype/use0/protectedfalse and skill0onlyfull; updateSkill state1unprotectedassign-2, protectedretain;state2assign2/1/-1/-2bytype; then clear(false)retainsskill.',
'Arenainit changedtrue,mind/skill/startHP[0,0],count0,partyindices[0,0], AIarenaflagtrue. pbCanSwitchIn alwaysdisplay+false; ArenaAIchooseswitchfalse.',
'ArenaEORSwitch checksdecision/favorDraws gates, pbJudge, positiveendreturn; eachfaintedsidewithnextindex increments sequentialindex, replace-message→pbReplace→singularpbOnBattlerEnteringBattle. No directcounter/mind/skill/startHPreset inthispath.',
'Arena all-entering openinghook explicitly changedtrue,resetmind/skill,capturecurrentHP,count0 then super. Separate pbRecordBattlerAsActive resetdefinition exists; thisdifferentname isnotordinaryparticipatedcallback.',
'ArenaCommand ifchanged firstsceneannouncement thenchangedfalse/count0; super; ifdecision0 addsMindonlychoiceUseMove withmove. Threeexactprotect/endure/fakeoutfunctioncodes-1,counter/mirrorcoat/bide0,status0,otherdamage1.',
'ArenaEOR callsuper first, resolveddecisionreturn. Otherwise addcurrentSuccessStates.skillonceside;count+=1; count<3return elsejudgment everylaterround withoutlocalreset.',
'Judgment cancelsbothmovestrue thenMind/Skill/Bodyratings2/0or1/1; bodyintegercurrentHP*100/[openingHP,1].max notclamped100. Sendsratingsclonestoscene beforewritingloserHP.',
'Sumratings thenmessage thenloserHP=0/pbFaint(false),tieeachside0/faintinorder; thenGainExp thenEORSwitch. FailurebeforeHPdoesnotinventfaint, failurebetweenloserskeepsfirstzero.',
'Ordinary pbReplace savesoldpartyindex, initializesnewactualpartyobject, swapscurrentpartyorderindices, sendsout, conditionallyrecalculatespriority. DoesnotcallArenaopeningorActive-resetname.',
'pbSendOut peeronEntering callbacksfirst, sceneanimationsecond, theneachresetcommands/setseen/usedInBattleflag. Sourcecallbackchain not actualpixels or allworldinvariants.',
'Ordinary all-entering hook prioritytrue→indices→singularentrylist→priority→eachcheckform. Arenaopeningoverride onlywhenall-enteringcalled, notautomaticallyeachreplacement.',
'Singularentry normalizesindexlist, optionallyresetsdropflags, loopsprioritymatchingnonfaint: participated→messages→positioneffects→hazards;faintbranchfaint/exp/judge/next;otherwiseform/primal/continuousabilities/switchinability/weather/item/held/status.',
'Afterentrypriorityscan checksEjectPackfirst thenEmergencyExit/WimpOut andbreaksonfirsttrue; finallyclearallhalf/statdropflags. Callermayalreadyhavepartialdamage/items. No countresetwithincompletebody.',
'Base pbPartyScreen capturesret-1, sceneParty callback applieslaxCanSwitchInorstrictCanSwitch andoptionalregister; normalvalidreturn storesindex. Userselection and AIstrategyareseparate.',
'Base pbSwitchInBetween playerowned&&!controlPlayer opensParty elseAIdefault. Thisisreturningquery usedbothmoveusageandEOR, notanEOR-onlyprimitive.',
'Base GetReplacement randomtrue collectsCanSwitchIn fromsameteam, empty-1 elsepbRandomchoice; randomfalse callsSwitchInBetween(idx,true), so recordedquerypathonlyownerchoice branch.',
'BaseEORhandlesfaintedopponenttrainerquery/playertrainerreplacement/wildnext-or-run; optionalswitchstyleconfirmonlyinternalbattle+single+othergates, impossibleordinaryfacilityinternalfalse. Repeatsuntilnoswitches, thenentrycallbacks.',
'Statusswitchmove Teleport trainer use checksCanChooseNonActive; postmove display→Pursuit→faintgate→GetReplacementownerquery→negativegate→recallreplace→clearchoice→moldfalse→entry→markswitched. Wildvariantescapes instead, notownerquery.',
'Damagingpivot requiresuseralive,numHits>0,opponentsnotallfaint,notalltargetsalreadyswitched,candidate; thenmessage/Pursuit/recheckfaint/query/negativeguard/replace/clearchoice/moldfalse/entry/push. No guaranteeeveryUturn invocationqueries.',
'PartingShot switcher startsuser theneligibleMagicCoat/Bounce targetmayreplaceit; requiresalive/hits/candidate/Pursuit, ownerqueryforactualswitcher; moldresetonlyiforiginaluser. Readcompleteclass, distinctfromallreflectedmoves.',
'BatonPass failedpredicate rejectsnoactivecandidate; postmove requiresalive/hits/candidate/Pursuitalive, thenownerquery, negativeguard, recallreplace batonPass=true,clearchoice,moldfalse,entry,push. Recordedqueryappendhappensbeforeguardnegative.',
'Whole pbEffectsAfterMove87–174 actualcomplete: targetdefrost, DestinyBonduserdamage/faint/judge, abilityEndUse, eligibleGreninja/Cramorantforms,RoomService,Gemconsume precedes switchingtrackarray.',
'Thenmove.SwitchOutTargetEffect, target/useritem/abilityafterMove2 unlessSheerForce+additionaleffect, THEN iforiginalusernotalready-switched move.EndOfMoveUsageEffect. AfterMove3 sameSheerForcegate thenifhits allItemEndOfMove checks. ThusownBATONPASS/recordquery sitswithinpostmovephase.',
'Whole pbUseMove154–578 actualcomplete read. BeginsSkipAccuracyderivedbeforespecialoverride,BeginTurn,forcesmulti/Encore; firstnilreturn; TryUsefailureclearslastrecords/exp/cancel/end/return; secondnilreturn distinct.',
'Ordinary PPfailure displaysuse+noPP thenclearsrecords/failtrue/cancel/end/return. Neithertryfailure norPPfailureguaranteesreachesrecordquery orArena useState1.',
'AfterPP:Stanceform,calcType,moldBreaker,twoTurnflag,usagecounters/Metronome,lastmoveuser/target/uniqueusedlist,battlesharedlastmove, Arena useState1. Thenfind/changeactualuserandtargets beforePressureextrapayment.',
'Moveblockingprioritycallbacks canmessage/ability/fail/cancel/end/return. UseMessage originalself; snatchmessage actualuser; MoveFailed earlyreturn; onStartUse andselfthaw precedePowder andprimalweatherfire/water failurebranches.',
'Powdermessage/animation andconditionalquarterdamage/exp then cancel/endreturn. HeavyRainFire/HarshSunWater failmessage/cancel/endreturn. Protean/libero gate ability+notcalled/notsnatched+othertype+nonpseudo; changes type/messages andCurseemptytargetreselect.',
'Quickcharging precedes targetbranch. Missingtargetswithrequiredtarget&&!worksNoTarget onlyfailuremessage/lastfailed, skipswholehit/postmove block; latermoldreset/exp/skill/end stillsourceflow.',
'Actualtargetbranch resetsdamage/flags, successchecks markunaffected; no-targetreflectscansopponentpriorityMagicCoat/Bounce; hitcountloopcanbreakfirstfailure/faint/sleep/frozen/alltargetsfaint; realhits increments onlysuccess.',
'Targetbranch setsArena useState2afterhitloop evenzeroactualhit; nonemptytargetstypeMod starts0thenaddsaffectedonly. Multihiteffectiveness/messages andtarget/no-targetbounce branches follow, notsameaslastMoveFailed.',
'ThenalltargetsAfterAllHits, fainttarget/user, pbEffectsAfterMove(actualuser,targets,realhits), clearsdropflags. ThusBATONPASSrecordownerquery canoccurBEFORElatermoldreset/exp/skill/end and before enclosingroundend.',
'Aftertargetbranch moldBreakerfalse→GainExp→allcurrentSuccessupdateSkill→conditionalHyperMode→EndTurn. PostendInstruct andDancer additionaluse branches separate; earlyreturnsandloggederrorhandlingdonotpromiseallprefixcleanup.',
'Instruct clearsflag beforefindpriorMove, displays/instructedtrue, mayUseMoveSimple underlogonerr, restoresround/judge onnormal, positiveendreturnbeforeflagfalse; unmatchedpriorMove skips afterclearingflag.',
'Dancer gate notDancer/lastnotfailed/hits>0/notsnatched/noMagicCoater/globalability/dancemove; buildsprioritydancers,popsloop,snapshotsround/Outrage/currentMove,targetfix,abilitymessages/flag,conditionalUseMoveSimple,restoresonlynormalandjudge; decisionreturnbeforeflagfalse. No allcallback/staticroundsuccess inferred.',
'Existingfacilitypartialentry36facts remainfrozen; nilvempty, samearrayreferences/startorder/temporarysaveposition normalrestoreandfailureprefixalreadyownproven. Thisnewpacketaddsnormalwrapper/Arena/recordownershiptemporaljoin only.',
'CurrentWP66A§4.6 tail references finite WP54 normalindexrestore, WP56continuingArena, WP58notallownerqueryEOR. These exactclaims nowboundtoactualcompleteproducer/consumerunits; not wholeWP54/55/56/58formalapproval.',
'Recordedattrfieldname/baretrainerbranch andotherreadsourcequirks retainedasfacts, no newproposal or runtimeassertion. ExistingrootCOM004/P3revision andoldfacilityfindings remain rootadjudication, notduplicated.'
]
facts=[dict(id=f'UI-FAC-LIFE-{i:03}',meaning=s) for i,s in enumerate(texts,1)]
fac=T.parent/'com_facility';forward=json.loads((fac/'forward-mapping.json').read_text());ints=json.loads((fac/'interfaces.json').read_text());interfaces=ints.get('interfaces') or ints.get('records')
packet=dict(schema='gr8-ui-facility-lifecycle-interface/v1',id='UI-FACILITY-LIFECYCLE-01',reader='/root/ui_full',utc=now,sources=sources,facts=facts,manual_fact_count=len(facts),received_complete_facility_units=[u for u in forward['facts'] if u['id'] in ['FAC-R04','FAC-R05','FAC-R10','FAC-R16']],previous_complete_entry_binding=dict(path=str(T/'facility-entry-interface.json'),bytes=(T/'facility-entry-interface.json').stat().st_size,sha256=hashlib.sha256((T/'facility-entry-interface.json').read_bytes()).hexdigest()),closure='Finite currentWP66A-A14 tail: nil/emptyandstart/restore fromfrozenentry; normalorganizedindexedrestore/failure, Arenaordinaryreplacementcounterretained, ownerquerycanpostmovebeforeEOR fromactualBatonPasschain. No fulloutsideprimaryformalcontracts/PBS/historydomainapproval.',premise='FixedR/defaultlegitbattleobjects/noexternalresethook/callbacksnormallyreturnunlessfailureatom; candidate/hit/nonfaint/ownership/sourcegatesexplicit; per-method source-static conditionalcallchain only, no actualbattle/render/native/diskrun.',business='NOT_EXECUTED',business_execution_count=0,update='UPDATE_NOT_STARTED',global_approval=False)
p=T/'facility-lifecycle-interface.json';p.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
deps=json.loads((T/'dependency-identities.json').read_text())
for rec in sources:
 if rec['repo']!=str(R):continue
 old=next((a for a in deps['records'] if a['path']==rec['path']),None)
 if old is None:deps['records'].append(rec)
 elif not old.get('whole_file_read') or rec['whole_file_read']:old.update(rec)
deps['utc']=now;(T/'dependency-identities.json').write_text(json.dumps(deps,ensure_ascii=False,indent=2)+'\n')
b=p.read_bytes();print(json.dumps(dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),facts=len(facts))))
