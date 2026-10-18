import pathlib,json,hashlib,datetime
P=pathlib.Path(__file__).resolve().parent;RR=P.parent.parent;now=datetime.datetime.now(datetime.timezone.utc).isoformat();mp=P/'manual-atomic-clauses.json';op=P/'old-locator-disposition.json';m=json.loads(mp.read_text());o=json.loads(op.read_text());records=[]
def ident(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(RR)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
parents=dict(manual=ident(mp),old=ident(op))
def bind(n,meaning,refs):
 key=f'CORE-C{n:04d}';r=next(x for x in o['rows']if x['id']==key);assert not r['all_children_received'];aa=[x for x in m['rows']if x['old_locator']==key];assert set(r['manual_atom_ids'])==set(x['id']for x in aa)
 records.append(dict(old_locator=key,original_canonical_parent_pointer='/rows/'+str(n-1),prior_remaining_labels=r['missing_action'],complete_existing_children=[dict(id=a['id'],canonical_object_sha256=hashlib.sha256(json.dumps(a,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest())for a in aa],new_manual_consumer_meaning=meaning,reused_actual_evidence=refs,review_scope='Exact conditional command/query/register/call/return consumer, not all downstream strategy/effect outcomes.',remaining_extensions_and_execution='Native UI/Input, unspecified plugin/score/effect callbacks and complete save graph are not approved. Any actually asserted concrete unreceived effect remains in its own precise row.',new_sourceFULL=0))
 r.update(all_children_received=True,status='RECEIVED_BOUNDED_COMMAND_INTERFACE_STATIC',missing_action=[],consumer_rebinding=dict(packet='command-interface-remainders-finite-disposition.v1.json',utc=now,meaning=meaning))
 for a in aa:a.update(pending_consumers=[],support='SUPPORTED_BOUNDED_COMMAND_INTERFACE_STATIC',consumer_rebinding=dict(packet='command-interface-remainders-finite-disposition.v1.json',utc=now,meaning=meaning,all_downstream_effects=False))
bind(70,[
 'Complete own constructor867 binds all13 initial-value children; Item.each generic symbols registry iterates DATA.each_value, Item.has_flag downcase comparison accepts MegaRing and collects actual current IDs. Clause never promises a fixed default ring list, so every Item raw record is not a premise.',
 'Actual AI001 initialize8–10 onlystores suppliedBattle. Later create_ai_objects/start and wrappers use their separately actually received complete constructor/setup units; constructor context doesnot imply all AI choice strategies.',
 'Current full Item270, actual MEDIA9registry facts and own AI001163 resolve the two real oldlabels; raw invalid registry/native/plugin mutation remains outside normal premise.'
],['Own Battle867/Item270/AI001163/AITrainer100','Actual media data-getter9 complete facts','Actual AI finite interface12units/7joins; fresh precise registry124–126/flags167–169 rereads'])
bind(204,[
 'All nine children define action intents and saved selected priority, not promised effect success. Actual Clear/RegisterMove/Target/Switch/Item/Call/Run/Shift and Priority producers plus their direct executors are whole personally read.',
 'UseItem choice precedes actual Bag consumption and SwitchOut identity precedes laterreplace; same source enum doesnot impose futureimplementation array slots. Item lifecycle and priority exactstoredfields already bound.',
 'All concrete ItemHandlers/AI targets were an overbroad residual for this data-definition row; they remain exact separate effect/target clauses rather than blocking verified enum/intention meaning.'
],['Own Command265/UseItem149/Switch469/Other201/Running160/Priority279/Attack202','sourcefact-consumer-bindings31–50 exact interfaces; PBS itemlifecycle actual receiver packet navigation only'])
bind(205,[
 'Command playerpass/controlPlayer then nonplayerpass route exactAI default method; own whole main chooses wrappedSwitch, wrappedItem, AutoFight intercept, Mega, scores/finalselection in that order.',
 'Actually received complete AIU001/003/004 etc and own Palace245 establish callbackoverride/delegation prefix. Scores and real executed obedience are explicitly outside this control-interface row; no legal-choice invariant follows from route alone.'
],['Own Command265/AI001163/AI003220/AI005393/Palace245','ai-interface-reception.v1.json CAR-AI-CORE-J01/J03/J04 full actual original objects received'])
bind(206,[
 'Registration writes intent; SwitchRecallReplace doesnot rerun command combinedqualification; item families1/2/3/5 recheck eligibility while ball4 directdispatch; move shared execution legality is distinct from native menu.',
 'Own complete dispatchers/Bag/current ownerlists and actually received finite UI/itemlifecycle support exact generic call semantics. All concrete callbacks neednot agree in outcome to prove register≠execute; failures keep reachedprefix.'
],['Own Switch469/UseItem149/UseMove762/Success595/Bag301/Command265','SourcefactF027/F030/F035/F040 exact full interfaces; mandatory item lifecycle/status companions'])
bind(209,[
 'Own complete priority producer and all actual currently registered bracket handlers in full Ability3208/Item1948 were personally read; movepriority, abilitybracket, itembracket, effectivebracket and saved flags have separate real domains.',
 'Comparison movepriority first then effectivebracket establishes within-priority microadjustment. Actual active/Use gates, Stall/QuickDraw/QuickClaw/Custap/Lagging/FullIncense and normalfailedprefix already finitely bound; this definition doesnot require every score/native caller.'
],['Own Priority279/Ability3208/Item1948/AbilityItem476','Actual MEDIA priority producer supplemental9105B and manual complete bracket atoms','RootCOM001 limited Stall vsTruant identity correction preserved'])
bind(212,[
 'Direct command reset uses actual canShowCommands current existingalive&&!multiturn, calls Clear without ReturnUnusedItem. This resolves retainedpreviouslyrefunded identity with no secondrefund on that path.',
 'Own full Bag301/UseItem149 and actual PBS finite lifecycle consequence bind returned-item capacity/refund/clear prefix. Potion effect detail is not a premise of this row after an explicitly previously-refunded choice; current state is the fixture.'
],['Own Command265/UseItem149/Bag301/MoveUsage405','pbs-item-choice-lifecycle-binding.v1.json and actual complete direct ending/command/faint source units','SourcefactF035/F040 with mandatoryC0122 where faint context used'])
bind(214,[
 'Own complete CommandPhaseLoop ascendsindex, stopsdecision, skipsnotown/nonNone/cannotshow, records player actioned beforemenu. controlPlayer delegates AI then skipsplayer bookkeeping.',
 'Actually whole AI main/set_up and complete finite providerJ01 bind actual delegation. Callback score effects and normalcommand-return success are not promised by this seven-child scan.'
],['Own Command265/AI001163 and actual selected AI interfaceobjects','SourcefactF041 complete finite loop and AI producer semantics'])
bind(215,[
 'Complete received UIcommand unit and own Command loop bind numberedreturn meanings including ShadowCall4, firstRun3/laterCancel−1, DEBUGF9−2. Native keypress output is conditioned as suppliedreturn.',
 'The row names debugmenu entry only; it doesnot assert its whole editing effect catalog. Actual editor downstream remains developer domain, so old full-editor/native requirement was broader than the eight statedchildren.'
],['Actually full finite UI67 menu objects/Command265','Own Running160/Command265 separatesF9editing from debugRun results'])
bind(216,[
 'firstAction is selected actioned length1, not fixedglobalindex0. Actual immediate Run→RunMenu nonzero closescommandselection while0 cancelscurrentchoice/continues; debug−1 canleave decision0.',
 'Own Run160 exact query/executor and all active trap/escape callbackdefinitions personally full read support conditional resultdomain. No specific trap grant is inferred; native menu/input is explicit executionlimit.'
],['Own Command265/Running160/Ability3208/Item1948/AbilityItem476','SourcefactF036 and actual finiteUIcommand/menu records'])
bind(219,[
 'Successful menu branch preserves registeredchoice and exitsinnerloop; failure reaches currentCancelChoice. Backtracking separately pops currentrecord, selects priorindex−1, cancels onlypreviouschoice, popspriorrecord/breaks without extra currentcancel.',
 'Actual CancelChoice refunds retained UseItem then unregistersMega then directclears. Own Bag301 and exact TrainerData213/loader124 owneritemclone establish real inventoryreceiver. Failedrefund stops laterMega/choiceclears and doesnotrollback priorwrites.'
],['Own Command265/UseItem149/Bag301/Other201','consumer-rebinding-04-trainer-partner-data.v1.json actual ownerlist producer','Original full item-choice lifecycle provider facts and exactsourceunits'])
bind(220,[
 'Complete own Running DebugRun has actual resultmenu choices/writes, CTRL/DEBUG guard, trainercapture refusal/Cancel−1unchangeddecision and RunMenu nonzero consumer.',
 'F9−2editor is separate path with no result-menu mutation guarantee. Full battleediting effects and native CTRL execution are outside this six-child returnvalue contract.'
],['Own Running160/Command265/Other201','Actual complete UI67 native-facing command return fact, no whole developer transfer'])
bind(222,[
 'Own nonplayer scan and actual AI main/set_up/ownerwrapper/autoFight override bind exact delegation and next-scan behavior. Playercontrol mode shares interface but executor stilluses actual actorowner.',
 'Full selected AI finite facts include voluntaryswitch/item/move/Palace sequencing. This row expressly excludes scorepolicy, so all strategyhandlers/Arena scorevalues cannot block proof of its four interfacechildren.'
],['Own Command265/AI001163/AI003220/AI005393/Palace245/Arena366','Actual ai-interface-reception.v1.json complete12unit/7join original content'])
bind(224,[
 'Own Fight direct autoEncore/Struggle gate precedes actual Palace AutoFight intercept; fullPalace special registration/partialeligibility/sourcecategory is already own245, no ordinaryeligibility assumption replaces it.',
 'Normal chosenindex/object/id→RegisterMove→nonSingle Scene target→negativecontinue/nonnegativeRegisterTarget and −2Mega toggle/−1cancel are actual complete directmethod/finiteUImethods. Concrete later effects are separate from suppliedtargetmetadata query.'
],['Own Command265/Palace245/Success595/Targeting203/Target185','Actual UI67 fight/target complete records plus samecaller finite sourcefactsF027/F040'])
bind(225,[
 'Bag internal gate, familytarget/eligibility, choicewrite-before-consume, consumed_after_use? important/consumable semantics and playerremovefalse raise are actual own complete UseItem/Item/Bag definitions.',
 'Nonplayer owneritems originates current trainerDATA itemsclone through real loader/partysetup; consume deletesfirstmatching entry and no equivalentplayerBagremove failurepromise. Ballflag only afternormal successfulmenureturn endsturnselection.',
 'Exact selected handlerexistence/use interface is complete; generic claim doesnot assert every item effect success. Unknown itemfamilydata and individual effects retain separate PBS/item scope.'
],['Own UseItem149/Item270/Bag301/ItemUtilities917/BattleItem712/Command265','consumer-rebinding04 complete TrainerData/loader owneritemproducer','Actual UI67 bagmenu finite complete objects'])
bind(226,[
 'Own PartyMenu normalPartyScreen vs debugreplacement chooser directreceiver are complete finite UI/AI definitions. Its command returnpredicate >=0 records success, distinct future RecallReplace execution and entry.',
 'Actually received AIU004 full replacementcandidatefilter/sort/result contract and own complete class4–172 support directnormalreturn. Ratinghelpers mayraise and no result/replacecommit guaranteed; unrelated forcedmove/abilitypaths are not this menuclaim.'
],['Own Command265/Switch469/AI002 complete4–172, notwhole705','Actual AI finiteJ02/J03 and UIparty complete record; no ratingpolicyallfamilycredit'])
bind(227,[
 'Own complete Run command/executor defines player immediate0/−1/1 consumer vs opposingwild callable Runregistration earlybranch and traineropposing0. Wildalwaysflee ProcessTurn is a separateactual sourcepath.',
 'No assertion exists that every AI default invokes opposing pbRun; readable opposingdirectdefinition is reviewed without inventing a defaultcall. Roaming/Safari special modes do not alter exact conditional generic actionidentity result.'
],['Own Running160/Command265/UseMove762','SourcefactF036/F043 and exact registeredmodifier finitefacts; no whole alternative mode grant'])
bind(229,[
 'Actually complete received UIFight Special−3 gate uses passedshiftMode; own CanShift owner/layout query then Command unregisterMega→RegisterShift are complete actual methods.',
 'Clause onlymanualFight choice; hypothetical AIShift/defaultcaller and nativekey event are not premises. Actual Swap mayrefuse, and registration doesnotguarantee laterpositionstate.'
],['Own Other201/Command265/UseMove762/Target185/Battle867','Actual UI67 fight record and sourcefactF037/F040; no allAIShiftclaim'])
bind(242,[
 'Own complete CanShowFightMenu, AutoChoose and CanChooseAny distinguishEncore/full slot scan/Struggle. RealAny caller in ownAI002 current ShouldSwitch handler and Palace AI override uses its actual return at real stage.',
 'Own fullPalace245 plus AI002 completeclass/selectedhandler source alreadyread through220 supplies namednochoose interface. Score/strategy downstream doesnotchange existenceofthis shared query; futureimplementation free toseparatehelper remains formaldesignscope.'
],['Own Success595/Command265/Palace245/AI005393','AI002 onlyactual partial through220, complete selectedhandler objects; no whole tailFULL'])
bind(397,[
 'Actual obedience owner/internal/action/multiturn predicates in whole Success595 establish normal nonplayerAI exemption and controlPlayer-owned AI stillsubject; no actualscore policy premise.',
 'Parenthetical player-sideAI unrun is retained evidence boundary. This row doesnot assert allAIchoiceslegal or interactionruntime, so unknownstrategies are not needed; stronger C0336 remains explicitlyOPEN.'
],['Own Success595/Command265/AI001163/AI005393/Shadow221','ai-interface-reception.v1.json finiteproducer facts and sourcefactF041'])
out=P/'command-interface-remainders-finite-disposition.v1.json';packet=dict(schema='car-exact-command-interface-consumer-rebinding/v1',utc=now,reader='/root/core_atomic_reception',prior_canonical_parent_identities=parents,records=records,actual_complete_selected_formal_assertion_refresh='All20 rows/allchildassertions/currentformal/pending labels untruncated8adad5. Wholeoriginalmanualchildren/commonpremises alreadyactuallyreviewed; selected actualAI/source method rereads49b35c/03ca38/1b72cd/e593c0/a23955 add0parentFULL.',explicit_remaining='CORE-C0336 stronger AI onlylegalchoice assertion stays OPEN. Ordinary finalfilter/registration vs Palace partialCanChoose/overridingRegisterMove and any actual generic legality quantifier require exact combinedcontext assessment; no newfinding/classification yet.',all_CORE_complete=False,global_atomic_denominator='NOT_FROZEN',new_required=0,new_optional=0,new_contexts=0,new_votes=0,business='NOT_EXECUTED',update='UPDATE_NOT_STARTED');out.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n')
m['updated_utc']=now;o['updated_utc']=now;mp.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n');op.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
g=P/'coverage-gaps.json';d=json.loads(g.read_text());d['updated_utc']=now;d['decomposed_but_foreign_join_open']=[r['id']for r in o['rows']if r['manual_atom_ids']and not r['all_children_received']];g.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=P/'progress.json';d=json.loads(p.read_text());d['updated_utc']=now;d['old_locators_complete']=sum(r['all_children_received']for r in o['rows']);d['exact_command_interface_rows_completed']=19;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');b=out.read_bytes();print(out.name,len(b),hashlib.sha256(b).hexdigest(),'rows',len(records),'open',len(json.loads(g.read_text())['decomposed_but_foreign_join_open']))
