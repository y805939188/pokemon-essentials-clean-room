import pathlib,json,hashlib,datetime,subprocess
P=pathlib.Path(__file__).resolve().parent;RR=P.parent.parent;R=pathlib.Path('/workspace/pokemon-essentials');C='8c5911e4a4b07b07e832e4bb0d5d8859e88b4a9b';now=datetime.datetime.now(datetime.timezone.utc).isoformat()
patterns=['pbGetTrainerBattleBGMFromType','def pbDisplayChargeMessage','class Battle::Move::RemoveAllScreens']
census=[]
for s in patterns:
 q=subprocess.run(['git','grep','-n','-e',s,C,'--','Data/Scripts'],cwd=R,capture_output=True,text=True);assert q.returncode in [0,1]
 census.append(dict(pattern=s,argv=['git','grep','-n','-e',s,C,'--','Data/Scripts'],stdout=q.stdout,stderr=q.stderr,helper_exit=q.returncode,scope='Whole fixed tracked Data/Scripts lexical occurrences only; no reflection/plugin/defaultcompiled/native negative proof.'))
assert census[0]['stdout'].count('\n')==1
manualpath=P/'manual-atomic-clauses.json';oldpath=P/'old-locator-disposition.json';manual=json.loads(manualpath.read_text());old=json.loads(oldpath.read_text())
def identity(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(RR)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
parents=dict(manual=identity(manualpath),old_locator=identity(oldpath));records=[]
def item(n,meaning,refs):
 ident=f'CORE-C{n:04d}';o=next(x for x in old['rows']if x['id']==ident);assert not o['all_children_received'];atoms=[x for x in manual['rows']if x['old_locator']==ident];assert set(o['manual_atom_ids'])==set(x['id']for x in atoms)
 records.append(dict(old_locator=ident,complete_existing_child_ids=o['manual_atom_ids'],prior_remaining_labels=o['missing_action'],prior_atom_fields=[dict(id=a['id'],support=a['support'],pending_consumers=a.get('pending_consumers'),canonical_object_sha256=hashlib.sha256(json.dumps(a,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest())for a in atoms],new_manual_disposition=meaning,reused_actual_complete_source_or_provider=refs,actual_reread='Prior own complete source/wholeprovider/wholemanualchild evidence reused. First combined36773f truncated and grants0new whole receipt; selected whole assertion/formal/pending set884060 is complete. Fresh fixedGit census only narrows definition/call scope.',conditional_static_review_complete=True,execution_or_unrequested_extension_limits=['Target game/native Input/Graphics/Audio/Filesystem/random outcomes NOT_EXECUTED.','Unspecified future plugins/reflection/Demo events not a claim of default reachability and not an available unread current clause receiver.','No whole-domain/save-graph/recursivefamily acceptance; any actual separate missing Ruby producer stays in its own remaining row.']))
 o.update(all_children_received=True,status='RECEIVED_BOUNDED_CONDITIONAL_DEFINITION_STATIC',missing_action=[],consumer_rebinding=dict(packet='conditional-definition-remainders-finite-disposition.v1.json',meaning=meaning,utc=now,execution='NOT_EXECUTED'))
 for a in atoms:
  a['pending_consumers']=[];a['support']='SUPPORTED_BOUNDED_CONDITIONAL_DEFINITION_STATIC';a['consumer_rebinding']=dict(packet='conditional-definition-remainders-finite-disposition.v1.json',meaning=meaning,utc=now,execution_limits_separate=True)
item(151,[
 'Complete actually received UI67-U02039facts and raw BattleAudio149 identity define FromType: nextBGM clone first, then any nonnil type battle_BGM rawreturn includingempty, onlynil map/global/nonempty/default fallback.',
 'Independent fixedGit trackedScripts search in this packet has exactly one FromType occurrence, its definition105. Ordinary world and facility calls use distinct pbGetTrainerBattleBGM; no ordinary FromType caller asserted.',
 'Clause describes callable raw request/fallback only and explicitly distinguishes plugin domain. Full future plugin census and host playback are execution/extension limits, not a missing definition premise.'
],['ui67-reception.v1.json / UI67-U020 complete39facts actually received; no UI sourceFULL transfer','media-reception.v1.json finiteAudio5facts/Data9facts','Fresh fixedGit census contained here'])
item(152,[
 'Ordered ordinary trainer getter lastnonnil behavior differs from FromType; A→nil retainsA, A→empty overwritesthen ordinary empty-check fallsbackmap/global/default. Three nextbattle fields remain independent and getters do not clear.',
 'Same exact single-definition fixedGit FromType census supplies bounded noordinarycaller fact. Unknown dynamic consumers were already explicitly excluded by the clause, so they do not defeat conditional current definition review.',
 'Normal victoryBGM/captureME and raw path/systemAudio callbacks require retained mandatory correction packets; no inference emptyrequest has an audible outcome.'
],['UI67-U020 complete original received','media-reception.mandatory-audio-caller-correction.v1.json','media-audio-correction-delivery-manifest.v1.json','Fresh fixedGit census'])
item(255,[
 'Complete actually received finite UI target method and own full Targeting/Battle geometry/Command registration separate initialindex, genuine integernear text, memberhighlight, selectedbutton, USEreturn and execution filtering.',
 'Exact0live/2faintnobackup/4live3v3 witness retains initial4 due object-vs-integer near call, textnil/buttonunselected, USEregister4 then ordinary execution rejectsfar4/no nearby living allyfallback. Living2 and allnonselfalliesabsent controls retain their correct distinct initial choices.',
 'All native render/input success and unrelated target-overriding concrete move effects are outside the explicitly maintained vector premises; they are not needed to prove the conditional source behavior already personally reviewed.'
],['Own Battle867/Target185/Targeting203/Command265/UseMove762','UI67 complete finite targeting unit originally received; actual target-menu444–550 complete method subset','Prior manual atoms exact seven target witnesschildren'])
item(265,[
 'Own complete Attack102–175 invokes charge callback only living UseMove notmoved before actionloop. Empty base callback and all3 current concrete overrides were actually fully read in own Usage405/Misc693/Switching948.',
 'FixedGit census confirms three nonempty definitions plus emptybase; FocusPunch/ShellTrap/BeakBlast commit their named flags before normal animation/message. Their later use/failure reads remain the exact actually reviewed functions, chargepresentation not damage.',
 'Unspecified plugin overrides/native graphics are qualified extension/execution limits. No current source callback remains unread for this whole pre-loop claim.'
],['Own Attack202/MoveUsage405/Misc693/MoveSwitching948/UseMove762','Fresh complete default-source charge-definition census contained'])
item(270,[
 'Own complete ProcessTurn/BeginTurn/EndTurn/CancelMoves and actual Shift/Swap/flee/Run/readers bind all eight children. Faint firstreturnsfalse, wildalwaysflee displaybeforedecision, Shift bookkeepingwithoutEndTurn, nonMove Begin+Endfalse, ordinary Use via logonerr→judge→optionalrecalc true are distinct.',
 'Own PBDebug77/Errors94 complete report wrapper and dedicated Exception definitions establish StandardError diagnosticnormalreturn vs reportingfailure/otherException without runningnative printing/disk.',
 'The clause sequences a conditional effect invocation, not outcomes of every possible concrete Move effect; unselected effect families remain separate relevant rows. This row need not wait all callbacks/native logging to verify its stated call boundary.'
],['Own UseMove762/MoveUsage405/Other201/Running160/PBDebug77/Errors94','SourcefactF017/F037/F043 exact finite bindings'])
item(273,[
 'The row is explicitly ordinary selected nonStruggle usage. Actual ProcessTurn default argument yields specialUsage=false, skipAccuracyCheckfalse and ordinary prechecks; base PP deduction is reached only after its preceding gates.',
 'Stored ordinary legal AI choice and player choice converge on this same executor. Exact hypothetical AI rating that selected the move is not a premise of executor PP/control behavior.',
 'All actual ordinary command producer interfaces already received/ownFULL support the conditional registered-choice input. Remaining AI heuristics are retained in their own AI rows rather than blocking this precise row.'
],['Own UseMove762/Success595/MoveUsage405/Command265/AI001163/AI005393','SourcefactF027/F040/F041/F043 and actual AI selected interface facts'])
item(655,[
 'Own whole postbattle callback/Pickup/Honey and exact actual WORLD Pokemon.item getter/setter correction establish all eight manually split gates, formula, separate conditional rolls and reachedpersistentitemassignment.',
 'HONEY.exists first, storedability/nonnilitem notactiveBattler ability, threshold5+floor((level−1)/10)*5, strict rand100 compare, win/capture sameobject Pickup→Honey are actual complete source semantics.',
 'Clause does not claim Demo invocation, empirical randomfrequency or any plugin event ordering. Those unavailable execution observations are limits, not unread consumer definitions for this row.'
],['Own BattleStarting749/Player123/Item270','Actually full WORLD item correctionv2+metadata reception','SourcefactF057/F058 exact new bindings'])
item(658,[
 'Own ProcessTurn innerlogonerr vs three phase wrappers have distinct catch placement; before/after lastRoundMoved write is determined by actual reached EndTurn/use control, not rollback or unconditional completedaction.',
 'Current same-round Attack loop rereads eligible choice/movedflag and freshpriority after true result, so incomplete normal-diagnostic-return paths may qualify again. No assertion that every hostfault recovers is made.',
 'Native/reporting-failure/otherexception boundaries are already explicit complete Errors/PBDebug source facts; outsidecallback hostoutcomes remain declared execution limits.'
],['Own UseMove762/MoveUsage405/Attack202/StartEnd568/PBDebug77/Errors94','SourcefactF017/F043/F051'])
item(659,[
 'Own complete normal battleloop separately wraps Command/Attack/EOR and then checksdecision; logonerr bare rescue handlesStandardError, normally logs/formats/prints/flushes without explicitrethrow.',
 'BattleAbortedException extendsException outsideStandardError and reaches dedicated StartBattle rescue. Diagnostics failure/outsidewrappedblock/otherException may escape; noensure or transaction restores earlierstate.',
 'Print/input/clipboard/clock/file actualhost results are not claimed. The exact static exception-domain and normaldiagnostic-return contract is complete, so native-notexecuted is not an unread Rubyreceiver.'
],['Own StartEnd568/PBDebug77/Errors94/UseMove762','Already actual manual error-boundary atoms; no new hostexecution'])
item(660,[
 'Actually full finite complete Standby and Animation methods already bound in consumer-rebinding03 dispose/cache/framereset→yield→conditionalrecreate and in_battle/viewport/audio/fade→yield→normalrestoration→false.',
 'No ensure around yield proves only placement and absenceof universalrecovery, not crash or terminalstate after arbitrary outerrescue. Earlier writes can remain when postyield body skipped.',
 'NativeGraphics/Audio/Scene creation and every intro effect remain runtime limits; clause itself explicitly preserves those unknowns. No additional current defined receiver is needed for its normalreturn/exception boundary.'
],['consumer-rebinding-03-presentation-result.v1.json + mandatorymodegetter companion','UI67 complete units and MEDIA audio5facts actually received','Own BattleStarting749; F054 and audio mandatory companions'])
item(703,[
 'Own complete ShadowOther460 exact StartShadowSkyWeather subclass and actual weather writer/currentfield helpers supply definition-conditional class→ordinaryusegates→weather prefix contract.',
 'The row expressly denies that sourceclass existence proves optional compiled registration. It therefore does not require proving defaultoptionalSHADOWSKY load to accept this negative evidence-boundary statement.',
 'Weather commits before its own presentation/form tail; latercallbackerror keeps reachedprefix. Expiry is a different method/order and root weatherNO_REQUIRED does not alter this creation fact.'
],['Own ShadowOther460/Battle867/Success595/UseMove762','Root-weather-expiry-scope-reception.v1.json only unrelated expiryboundary, no automaticfinding'])
item(747,[
 'Actual optionalraw SHADOWSHED identity retained: status/BothSides/RemoveAllScreens; exact Move factory uses matching class identity or Unimplemented. Source defines RemoveAllScreensAndSafeguard, not shorterclass, confirmed wholefixedGit class census.',
 'Conditional statusUnimplemented failure is already actual base/factory definition review. Legal binding to longerclass gets exact eightclear contract, and reachedpostwrite callbackerror doesnotrollback.',
 'Defaultcompiled optional load/native/Demo notclaimed and unnecessary for this explicit conditional mismatch/binding distinction. No claim that all ShadowMove records/effects or factoryplugins are reviewed.'
],['Own ShadowOther460/Movebase201/MoveUsage405/UseMove762/Success595','Actual optionalraw original finite record reception; preserved full method/classes already own','Fresh exact class-name census contained'])
item(791,[
 'Complete actual event fixture in all sevenchildren supplies reachability/name/jump/overtrigger gates, interpreterrunning/doublecapacity/waiting/A-switch and singletrainerpartysize. Trigger2 passes actual event.trigger membership; trigger0 fails independently from always_on_top.',
 'Own actual GamePlayer trainer event getter and eventpage trigger assignment complete units plus Trainer wrapper/data loaders were previously read and sourcebound. Onequalifyingother saves loadedtrainer+eventid and returnsfalse under exact suppliedgates.',
 'The testcatalog expressly says static eventfixture/noDemochain. Realhost pathfinding/renderedlayer/nativeevents are not an additional unreviewed premise of this source fixture.'
],['consumer-rebinding-04-trainer-partner-data.v1.json actual complete wrapper/loader units','Prior actual Eventrefresh+GamePlayer getter completeunits and own BattleStarting749'])
item(792,[
 'Actually full UI67-U02039facts and own actual normalcallers bind independent wild battle/victory/capture getters, orderedtrainers lastnonnil/emptyfollowsfallback and cloned independentnextoverrides with noclear.',
 'Mandatory own audio correction supplies true victoryBGM/captureMEcaller; MEDIA complete sourcepath packet retains System rawprefix/existence→Audio string and conditional fallbackcanonicalize. No originalA retry inserted.',
 'Exact fixture conditions validmetadata/records/conversion and normalcallbacks; nativeaudibleoutput/resources notproven is itself stated. FullMEDIA approval/nativeplayback is not required to accept current conditional request chain.'
],['UI67-U020 complete39facts/media-reception.v1.json','media-reception.mandatory-audio-caller-correction.v1.json','media-audio-correction-delivery-manifest.v1.json'])
item(794,[
 'Legal authorrecord explicitly stores later nonnil emptyvalue; ordinary array getter overwritesA then rejects empty and choosesmapM, distinct directFromType rawemptyreturn and nil-onlyfallback.',
 'Independent fixedGit census onlydefinitionFromType supplies exact noordinarycaller bound. Dynamicpluginunknown is preserved qualification, not a demand to inspect unspecified futureconsumers.',
 'Subsequent MEDIA emptyrequest/hostoutput remains outsidefixture inference. Exact normalcaller and mandatory audio correction stay applicable; source definition doesnotchange ordinary combat behavior.'
],['Actually full UI67-U020 complete unit','Fresh fixedGit directFromType census','MEDIA source5facts + mandatory audio correction/manifest'])
out=P/'conditional-definition-remainders-finite-disposition.v1.json';packet=dict(schema='car-conditional-static-vs-execution-limit-finite-disposition/v1',utc=now,reader='/root/core_atomic_reception',prior_canonical_parent_identities=parents,records=records,fresh_fixed_source_lexical_census=census,common_boundary='15 individually authored row dispositions; not blanket native-limit clearing. Existing complete source/wholeprovider meaning and full manual children reused; exact new chain scope is stated per row. No unread Move/AI/Ability family accepted from names or sameblob.',all_CORE_complete=False,global_atomic_denominator='NOT_FROZEN',new_required=0,new_optional=0,new_contexts=0,new_votes=0,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');out.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
manual['updated_utc']=now;old['updated_utc']=now;manualpath.write_text(json.dumps(manual,ensure_ascii=False,indent=2)+'\n');oldpath.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
g=P/'coverage-gaps.json';d=json.loads(g.read_text());d['updated_utc']=now;d['decomposed_but_foreign_join_open']=[x['id']for x in old['rows']if x['manual_atom_ids']and not x['all_children_received']];g.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
q=P/'progress.json';d=json.loads(q.read_text());d['updated_utc']=now;d['old_locators_complete']=sum(x['all_children_received']for x in old['rows']);d['conditional_definition_review_completed_rows']=15;q.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
b=out.read_bytes();print(out.name,len(b),hashlib.sha256(b).hexdigest(),'rows',len(records),'remainingopen',len(json.loads(g.read_text())['decomposed_but_foreign_join_open']))
