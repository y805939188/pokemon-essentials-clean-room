import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_07f.json').read_text());d=base['source_dictionary'];rows=[]
d['switch_effects_full']={'path':'Data/Scripts/011_Battle/003_Move/013_MoveEffects_SwitchingActing.rb','range':[1,948],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ in actual five contiguous output intervals; no allclass semanticPASS'}
d['scene_party']={'path':'Data/Scripts/011_Battle/004_Scene/003_Scene_ChooseCommands.rb','range':[141,191],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE_COMPLETE_PARTYSCREEN_METHOD_READ141–190 plus187–195'}
d['crec_form_join']={'contribution':'crec-transformation-selected-complete-input.json','receipt':'crec-transformation-reception.v1.json','original_reader':'/root/creature_a_atomic_reception','reception':'All fivecomplete CTF-R001/003/004/006/007 records+37sourceunits+12raw/9identity/premises/failure actualreceived; not whole477963B/fullsource transfer'}
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
for n,reason in [(399,'Classification/implementation-independent scope label; no additional switchbehavior beyond subsequent contract.'),(400,'Clean-document/source-traceability/static-only administrative statement. Currentunrun evidence preserved; doesnot impose sourcepaths/futureAPI.'),(401,'Purpose taxonomy points to qualification/order/state/escape/boundaries defined in body; complete compoundbehavior is decomposed at concrete subsequent clauses, not inferred from completeness adjective.'),(402,'Scope index for switch qualification/cancellation/registration; actual gates below are separate behavioral children.'),(403,'Scope index for recall/replacement/entryeffects; no behavior result beyond body requirements.'),(404,'Scope index for faint/EOR replacement/opponent confirmation; actual loop/order below separatelyread.'),(405,'Scope index for positionmovement versusreplacement/targetmapping; actual swap source bound below.'),(406,'Scope index for run/trapping/probability/count; actual threeentry/guard/number rules below.'),(407,'Scope index for bounded force-switch movefamilies; full concrete classes now actually read, body assertions receive separate mapping.'),(408,'Explicit non-target/dependency routing to command/ending/effectfamilies/growth/capture/formdomains; no whole-domain acceptance from citation.'),(409,'Explicit partyUI scope routing; finite actual Scene method and originalUI contribution received separately.'),(410,'Term table columnheader only.')]:row(n,[],[],'',layout_reason=reason)
row(411,[
 'Replacement candidate uses party-array index into same-side participating party, including owner segments; it is distinct from Battlerfieldindex or UI displayedrank.',
 'Eligibility checks current persistent Pokemon object and owner mapping before binding; partyorder/UI translation changes are separate from underlying participatingarray position.'
],['switching','battlefull','scene_party'],'candidate persistentarray identity→ownersegment→UIrank translation/battlebinding; no indexdomain conflation.')
row(412,['Switchout means the old activeobject leaving with its own recall/ability/peer/form/bookkeeping chain; persistent Pokemon stays in party. Runtime effectreset and baton subset depend on actual replacement initialization below.'],['switching','b_init','ability_item','peer'],'term routes oldactive cleanup and persistentobject distinction, not blanketHP/statusclearing.')
row(413,['Replacement is common category for resending a partyPokemon into position after faint or forcedeffect; qualification/choice/random/cancel and entrynotifications remain different concrete caller paths, not one uniformbranch.'],['switching','switch_effects_full','attack'],'term unifies role, not gates; EOR and forcedmove consumers separately below.')
row(414,[
 'Normal Shift qualification requires computed same-owner destination; actual swap additionally rejects missingactors/opposition/differentowner.',
 'Swap exchanges activeBattler objects/indexfields/choicearrays and sprites, then remaps specified effect targetindices; itdoesnot bind newPokemon or exchange partyorder.'
],['other','swap','use'],'ownerqualifiedactivepositions→object/choice/index exchange; no recalledPokemon replacement.')
row(415,[
 'Nonwild force-switch effect builds randomlegalbench candidate through replacementIndex(random=true), recalls/replaces at mostone target then clearChoice/entrynotify.',
 'Read with full§8 explicitclearChoice and source comment replacementdoesnothingthisround: no separate chosen SwitchOut action/PP is charged to target, but its former registeredcommand is removed and incomingPokemon doesnot get a freecurrentround action.',
 'Wild terminal branches instead set decision3 under ownlevel/canRun/solewild gates, without randomreplacement; this term is not a universal wilddrag promise.'
],['switch_effects_full','switching','command','attack'],'forcedmove→candidate random→replacement→choiceNone→entry; preserve noextraaction and exactwildterminal scope.')
row(416,[
 'Trapping aggregate includes positiveTrapping/MeanLook>=0/ownJawLock>=0/anylivingotherJawLockpointsatself/Octolock>=0/Ingrain/NoRetreat/positivefieldFairyLock.',
 'Certain switching/escape and activeopposing ability/itemtrap are separate callerlayers. A raw aggregate true can be bypassed by earlier Ghost/ShedShell rule in switchout path.',
 'Move producers Bind/MeanLook/Octolock/JawLock/FairyLock write distinctduration/identity fields; no alltraps share same expiry or damagecounter.'
],['battlerfull','switching','running','switch_effects_full','abilityeffects','item'],'state producerfamily→aggregatequery→caller-specific earlyescape/otherbearer traps; not single universalblocker.')
row(417,[
 'Constructor initializes @runCommand0; it is battle-wide accumulatedattempt count, not peractor field.',
 'Run execution increments only reached probabilitycalculation and !duringBattle; earlydeterministic escape/refusal and replacementduringBattle do not add.',
 'Calculation uses existingcount*30 then bound/rand comparison; replacementrun can benefit existingcount without increment. Getter/query doesnot itself increase attempts.'
],['battlefull','running'],'battleinit→reachedrun calculation→conditionalcountwrite→rateconsumer; no countfor everyrequest.')
row(418,[
 'Swap remaps actualliveBattlers effects Attract/BideTarget/CounterTarget/JawLock/LockOnPos/MeanLook/MirrorCoatTarget/Octolock/SkyDrop/TrappingUser if equalidxA/B.',
 'LeechSeed deliberately positionbound and not remapped; PerishSongUser only sideidentity needed so same-side swap leaves it. Not everyfieldcontaining an index musttrack same targetobject.',
 'Actor/choice/index/sprite swaps occur before remapping. Scene exception can leave object exchange with oldtarget references; no transactionalatomic guarantee.'
],['swap','battlerfull'],'actualindexwrite/sprites→specifiedeffecttarget remap; explicit positionversusidentity exceptions.')
row(419,[
 'Nonnegative candidate: first out-of-range or nilpartyentry refuses without later egg/owner/status/active work.',
 'Then egg refuses with optionalpartyScene message; next wrongowner refuses and optionalownername lookup/message; owner check precedes fainted.',
 'Then persistent fainted refuses with optional message, then current same-side activePokemonindex refuses. Pass returns true without registeringchoice.',
 'Owner mismatch is actual participatingownersegment, not Pokemons originalOwner/foreign flag. Prior messages/query callbacks may raise; no newchoice commit from query.'
],['switching','battlefull','battlerfull'],'bounds/nil→egg→currenttrainersegment→persistentfaint→active lookup→true; optionalfeedback only.')
row(420,[
 'CanSwitchIn negative index returns true before partyarrayaccess, representing laxquery/cancel sentinel and no candidate selected.',
 'Combined CanSwitch still checks same-side registered SwitchOutduplicate and CanSwitchOut even for negativeindex; no automaticcombinedtrue.',
 'UI shouldRegister path explicitly rejects negative before RegisterSwitch; directbare register has no separate negativeguard beyond combinedmethod, so read query/UI/bare layers distinctly.',
 'Negative duplicate with optionalpartyScene can reach party[negative].name feedback according actualarraystate; no invented safety of everymalformed negativequery.'
],['switching','scene_party','command'],'negative laxsentinel→combinedlatergates→UIregistration guard; not legalconcretePokemon certificate.')
row(421,[
 'CanSwitchOut first returns true if currentBattler.fainted, without trappinghandlers.',
 'Then activeability CertainSwitching callbacktrue, activeitem CertainSwitching callbacktrue, then MORE_TYPE_EFFECTS&&Ghost each returntrue beforeaggregate trap.',
 'Default ability CertainSwitching registry empty; ShedShell itemhandler simplytrue when caller itemactive. Callbackabsence not idealized newhandler.',
 'Aggregate trap true refuses, else allOtherSideBattlers visits currentlivingopponents activeabilitytrap before secondloop activeitemtrap. Optional message names actualbearer/name.',
 'Default abilitytraps ArenaTrap ifswitcher!airborne, MagnetPull ifSteel, ShadowTag ifswitcher!activeShadowTag; itemtrap registry empty under fixeddefaults. No MoldBreaker bypass added by this caller.'
],['switching','battlerfull','abilityeffects','item','ability_item','b_settings'],'faint→certainability/item→Ghost→aggregate→opposingabilitythenitem→pass; defaultspecific callbacks and active gates retained.')
row(422,[
 'CanSwitch first invokes CanSwitchIn; false stops beforeduplicate/out test.',
 'Then currentliving allSameSideBattlers includes anymatching registered SwitchOutpartyindex, refuses; optionalmessage dereferences candidate name.',
 'Then CanSwitchOut determines finalqualification. Query doesnot writechoice.',
 'RegisterSwitch repeats same combinedquery withoutscene, and ontrue sequentially writes actionSwitchOut,partyindex,movenil; targetslot notreset here.'
],['switching','battlefull','command'],'qualificationin→duplicate→qualificationout→separate repeatedregister→threewrites; no queryregistration equivalence.')
row(423,[
 'Random replacement candidates and lax PartyScreen route onlyCanSwitchIn; strict PartyScreen route CanSwitch combined even shouldRegisterfalse.',
 'Scene SwitchIn button requires mode0,candidate.able?, and(canSwitch OR !canCancel); canSwitch is UIpermission and not read by direct CanSwitch/CanSwitchIn.',
 'shouldRegistertrue rejects negative then RegisterSwitch invokes combinedagain. Qualifyingquery and UIpermission remain independent.',
 'RecallAndReplace actualchain never calls combinedquery; caller must establish own eligibility and interrupt/decision/liveness conditions.'
],['switching','scene_party','attack','switch_effects_full'],'lax/strict/permission/register/executor five layers; no inferred commonguard.')
row(424,['Duplicate check only current same-side liveactors with choices actionSwitchOut and samepartyindex, regardless whether queryingactor itself owns previousmatchingregistration. It is before CanSwitchOut and doesnot reserve a candidate onquerysuccess.'],['switching','battlefull'],'same-sidechoice census→refusal orlateroutguard; no registration from query.')
row(425,[
 'Scene negativepartychoice repeats when !canCancel, otherwise breakswithout yieldingcandidate; no qualification/register oncancel itself.',
 'Mode0 candidate.able? plus(canSwitch OR !canCancel) exposes SwitchIn; Summary alwaysavailable and performs summaryview without yielding or selecting.',
 'Chosen displayedrank maps via partyorder to participatingarray index; no mapping leaves−1 and passes it to yielded battlequalification layer.',
 'Scene exit calls endScene then fadeIn; no ensure around exceptions guaranteesvisualrestore. UI permission precedes later actual qualification and cannotreplace it.'
],['scene_party','switching','battlefull','ui_command'],'displayparty/order→inputpermission→ranktranslation→battlecallback→normalclose/fade; no Summaryselection.')
row(426,[
 'Battle PartyScreen receives threeindependentflags checkLaxOnly/canCancel/shouldRegister. Callback chooses in-only versuscombined qualification first.',
 'Onqualificationpass, shouldRegisterfalse setsreturncandidate only; true refusesnegative or failedRegisterSwitch, then setsreturn. Strictmode can therefore querywithoutregister.',
 'SwitchInBetween routes actualplayerowned&&!controlPlayer to PartyScreen withflags anddefaultshouldRegisterfalse; otherwiseAI newenemychooser. This choiceproducer is separate fromlater RecallAndReplace.',
 'Command PartyMenu uses strict/cancelable/registertrue; failed/canceledmenu returns to commandloop, forcedreplacement uses actualspecifiedcancelpolicy.',
 'AI candidate legality/internalcontrol paths have not all been completelyreceived in current pass; direct delegation is bounded, not allAI returnvalid proof.'
],['switching','command','scene_party','battlefull'],'flagorthogonality→qualification→optionalregistration/return→playerUI versusAI producer.',open=['Complete AI.pbDefaultChooseNewEnemy legality/return/cancel consumers remain OPEN for delegated branch; original963129B AI input available, not materiallimit.'])
row(427,[
 'Command selected SwitchOut is executed only attackphase, not while partyUI registers. Stage uses currentpriority/livingregisteredactor and storedcandidate.',
 'It writes successfailurefalse/lastMoveUser, recallsmessage then invokesPursuit; positive decisionreturnsphase; actorfaint skips replacement.',
 'No actualcombinedrecheck in subsequent recall/replace, so newlyentered opponenttrap doesnot by itself veto alreadyregistered switch.',
 'All other actualoldactor/newcandidate validity, callbackerror and Pursuit result remain concrete sourceorder; not guarantee successfulreplacement afterarbitrarymidroundmutation.'
],['attack','switching','priority','use','switch_effects_full'],'selectionregistration→laterattack/Pursuit→replacement withoutcombinedrecheck, ordinarygates retained.')
base['source_dictionary']=d;base['rows']=rows
(P/'manual_batch_08a.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x.get('children',[]))for x in rows),'layout':sum('layout_reason'in x for x in rows)})
