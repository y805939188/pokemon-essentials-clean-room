import pathlib,json
P=pathlib.Path(__file__).resolve().parent
base=json.loads((P/'manual_batch_08f.json').read_text());d=base['source_dictionary'];rows=[]
d['start_end_full']={'path':'Data/Scripts/011_Battle/001_Battle/002_Battle_StartAndEnd.rb','range':[1,568],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ previously actual; loop/end/judges freshly complete re-read'}
d['catch_full']={'path':'Data/Scripts/011_Battle/007_Other battle code/005_Battle_CatchAndStoreMixin.rb','range':[1,271],'actual_reader':'/root/core_atomic_reception','reading':'FULL_FILE_READ actually all1–140/141–271 captured this pass, not only received CAA finitefacts'}
d['pokemon_growth_qual']={'path':'Data/Scripts/014_Pokemon/001_Pokemon.rb','complete_units':[[209,212],[215,217],[220,222],[225,227],[246,250],[254,261],[264,271],[909,914]],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete named methods actually read; not Pokemon whole-file credit'}
d['caterpie_raw']={'path':'PBS/pokemon.txt','range':[237,261],'actual_reader':'/root/core_atomic_reception','reading':'PARTIAL_FILE complete CATERPIE raw record actually read; compiled import/native cache not certified'}
d['shadow']=d['shadowother'];d['pbdebug']=d['debuglog']
def row(n,c,u,chain,**kw):rows.append(dict(number=n,children=c,source_units=u,chain=chain,**kw))
row(534,[],[],'',layout_reason='Document category/domain/implementation-independent contract classification; no extra executable algorithm or shared whole-domain approval.')
row(535,[],[],'',layout_reason='Purification/history/static-evidence qualification and source-navigation policy. Fixed body actually read; historical transfer approval remains root-history scope, no new game execution or API architecture prescribed.')
row(536,[
 'This scoped document covers reached in-battle growth commits and battler feedback, ordered end-round state operations, and normalending/outer-world handoff; actual call boundaries and partial commits are individually decomposed below.',
 'Expbar/levels/learn-or-decline, residualfaint/replacement, resultmessages/money/capture and postbattleevolution are visible effect families, not a guarantee every battle reaches every one. Concrete UI/evolution/returnworld consumers remain independently scoped rather than granted by this purpose sentence.'
],['growth','start_end_full','eor','switching','catch_full'],'scope family map→later concrete reached-call contracts, not blanket closure of every named consumer.',open=['Remaining exact UI/evolution/world/individual handler joins from later clauses must be actually bound; purpose list gives no whole-domain PASS.'])
row(537,[
 'A/B/C/D/E split describes result/checkpoint, growth/sync, normalEOR, normalend, outerexception consumer domains; forwarded math/effect/capture/evolution/failure domains are not redefined here.',
 'Its own ordering, return-consumer and exit-point promises are still substantive obligations. A forward reference cannot remove an actual local ordering/exit statement from review; each such statement is independently traced below.'
],['growth','start_end_full','eor','clauses'],'document scope boundary retains its own producer/write/consumer duties while avoiding synthetic redefinition of forwardeddomains.')
row(538,[],[],'',layout_reason='Explicit non-goal: forwarded domains/rendering not redefined, reference code not executed. Scope boundary is retained without inventing a business assertion/test obligation.')
row(539,[
 'Battle decision initializes0 and exposed field can be reassigned; source-specific outcomes1win/2loss/3escape-forfeit/4capture/5draw retain actual call contexts. Abort outerrescue also writes0.',
 'Judge has no generic existingpositive guard: bothsideempty writes draw-result, ownempty2, foeempty1; bothable leaves prior decision. Checkpoints/capture/endconversion can assign separately. First positive write is therefore not an immutable resultlock.'
],['battlefull','start_end_full','clauses','running','catch_full'],'result field writers→actual conditional overwrite→caller positive/nonzero tests, distinguish stored intermediate and finalreturn.')
row(540,[
 'AbleCount scans current participating party selected by side, counting nonnil Pokemon.able?; AllFainted is count==0, not number of occupied battler seats. Able? means !egg? and persistentHP>0; egg means steps_to_hatch>0.',
 'Merged partner members can keep player side able, while growth eachInTeam(0,0) and ownershipfilter select only actual player team segment. Participating trainer identity differs from original Pokemon Owner outsider identity.'
],['battlefull','pokemon_growth_qual','growth','teams','owners','prepare'],'sideparty/able predicate→Judge versus playersegment→growth, partnerqualification and originalOwner keptdistinct.')
row(541,[
 'Growth reads defeated/captured opposing battler, its saved participants, current player recipients, global ExpAll flag/Bag, current item and mutable initialItems restore record, internal/expGain gates.',
 'Reached EV/Exp/level/statHP/moves/stats writes occur at distinct ordered steps, with Shadow paths differing; these are outputs of reached subpaths rather than simultaneous mandatory updates.'
],['growth','b_init','battlefull','item','shadow','crec_form_join'],'opponent/persistentparty/item-source inputs→EV thenExp partial outputs, different Shadow and active binding branches preserved.',open=['Exact remaining growth-rate/Shadow/stat/moves/UI consumers not yet independently bound in later clauses remainOPEN; list itself doesnot close them.'])
row(542,[
 'Runtime battler and choice/effect arrays are distinct from attached persistent Pokemon, side/field/position objects, caughtPokemonqueue and worldtemp references. Source operations cross these layers selectively.',
 'A return or displayed message is not a universal simultaneous commit/reload certificate. Error after an earlier write can retain that prefix without later layers catching up; literal fields and actual receiver setters matter.'
],['battlefull','battlerfull','b_init','growth','catch_full','start_end_full'],'layer identity→selective writes/forwarders→partial prefix, no atomicity or native save observation inferred.')
row(543,[
 'Base constructor sets internalBattle/expGain/moneyGain true; fixed mechanics generation8 is default producer. Concrete facility/prepare/rule paths may overwrite these before later consumers.',
 'Direct Battle, wild/trainer core, public wrapper, skip/override and Abort are different entrances; later result/cleanup contract uses actually reached entrance, not one universal normalend assumption.'
],['battlefull','b_settings','config','prepare','start_end_full','clauses'],'default constructor/config→possible preparationoverrides→actual internal/growth/finance/abort consumer, entrance scope retained.')
row(544,[
 'BattleLoop writes turnCount0 then Command→positivecheck→Attack→positivecheck→EOR→positivecheck. Only reaching all three without positive result increments roundcount.',
 'Normal loop exit calls EndOfBattle; immediate command escape can bypass this round attack/EOR. Debug Abort raises out before EndOfBattle and is handled by StartBattle rescue separately.',
 'Each phase is invoked under diagnostic logonerr; its actual exception policy is separately received, not assumed transactional or equivalent to completed-action stamp. Startup participant/sendout/entry details remain their earlier scopedcontracts.'
],['start_end_full','command','attack','eor','running','pbdebug'],'loopcontrol comparisons→phase reachability→normalEnd or exceptionroute, distinguish diagnostic from businesscompletion.')
row(545,[
 'Attack stage order is Call→switch→positivecheck→item→positivecheck→Mega→moves; action-loop branches check positive after each selected ProcessTurn return.',
 'ProcessTurn wraps UseMove in diagnostic helper, then Judge and conditionalpriorityrecalc on normal helper return. A failed inner operation can return without lastRoundMoved stamp; actual reselect loop tests movedThisRound rather than a generic callcompletedflag.',
 'Movecommon tail and Instruct/Dancer nested simpleuse have distinct Judge/reachability positions. Positive decision or HP0 within an arbitrary handler doesnot itself roll back earlier work or syntactically return from every outerloop.'
],['attack','use','pbdebug','battlerfull','priority'],'normal diagnosticreturn→slotJudge→actionloop checks, nested uses retain own earlyreturn and movedstamp conditions.')
row(546,[],[],'',layout_reason='Result-entry table header; all actual result writer rows decomposed individually.')
row(547,[
 'Judge queries both current sideparty AllFainted before choosing both→DecisionOnDraw/onlyown→2/onlyfoe→1; with bothable it leaves the existing record.',
 'There is no prior decisionpositive earlyreturn inside Judge. Callers may have independent guards and later Judge may overwrite a prior checkpoint intermediate; localwriter and consumergate remain separate.'
],['start_end_full','battlefull','pokemon_growth_qual','clauses'],'currentpersistentparty ablequeries→unconditional localjudge branches→possibleoverwrite, with caller-specific stopgates.')
row(548,[
 'Base drawreturns5. Loaded SelfKO rule tests lastMoveUser<0→5; else opposing lastuser→2 and own lastuser→1, preserving current snapshot direction.',
 'Absent rule falls back through aliased basedraw. This last-user policy differs from source-side Checkpoint user; rule name cannot invert recorded behavior.'
],['clauses','start_end_full','battlefull','use'],'loaded rulealias→lastMoveUser/side→drawresult, distinct from checkpointsource.')
row(549,[
 'Base Checkpoint is empty. Loaded override only enters if bothsidepartiesAllFainted. drawclause assigns opposing source→1/ownsource→2 unless provided movefunction HealUserByHalfOfDamageDone.',
 'modifiedselfdestruct is an elsif, considered only when drawclausefalse and provided function UserFaintsExplosive; otherwise priorresult stays.',
 'Perish records expired saved PerishSongUser, reducesHP/healchecks/faints, then callsCheckpoint only for nonempty collectedsources all on same side; source is battler[savedfirst], not lastmoveuser.',
 'Perishhelper positivecheckpoint return is consumed by EORmaster GainExp/return. Later reachedordinaryJudge can overwrite intermediate; checkpointwrite is not automatically finalreturn.'
],['clauses','start_end_full','eor','use','battlefull'],'bothdeadcheckpoint/savedPerishsource→intermediateassignment→actual callerchecks; keep correctR11.')
row(550,[
 'Loaded clause EOR invokes aliased basefirst. Only suddendeathtruthy ANDdecision0 compares side AbleCount, ownmore1/ownless2/equalunchanged0.',
 'This is counts-only, no HPcomparison. Baseearlyreturn still returns to wrapper; facility outerjudgments retain their distinct forwarded scope.'
],['clauses','eor','battlefull'],'baseEORreturn→rule/zeroresultgate→count-onlywriter, distinct from timeHPjudge.')
row(551,[
 'Qualified Run/alwaysflee/Teleport/EmergencyExit wild routes write3 with their own side/config/trap/livingally/level/actioncost gates.',
 'A nested write3 doesnot syntactically unwind everycaller. Actualpositivechecks decide stops; EORSwitch same-scan prefixes maycontinue and earlierwrites are not rolledback.'
],['running','use','switch_effects_full','entry_exit_handlers','switching','eor'],'specificescapewriter→actual callercheckpoint, no invented globalinterrupt.')
row(552,[
 'Shake4 message/capture success precedes RemoveFromParty, which writes participatingparty slotnil and reorders teamdisplayindices; it doesnot first faint that Pokemon.',
 'CaptureExp true surrounds GainExp with capturedtrue thenfalse; Battler.Reset follows. Current removedparty AllFainted then assigns trainer1/wild4 if that sideempty.',
 'Only afterward snagOwner/onCatch/pokeBall/unmega/primal/Shadowmoves/firstmoves/forcedform/Peer/hideball occur, then caughtPokemonqueuepush. Prior result doesnot itself skip these reachedpostwrites.',
 'Failure during GainExp can leave removedparty/capturedtrue; laterfailure can preventqueuepush. No ensure resets/reinserts. Failedcatch firstball/failureflag follows its handler.'
],['catch_full','battlefull','growth','b_init','peer','crec_form_join'],'shake4→partyremoval→temporarygrowth→Reset→countresult→metadata/form→queue, distinctfailureprefixes.',open=['Ball rate/OnCatch/ownership/pokedex/storage/native consumers outside explicitly received CAA facts remainOPEN; wholeCatchsource isnot allballhandler PASS.'])
row(553,[
 'Loopdebug&&turnCount>=100 computes DecisionOnTime: currentablecounts first, then onlythosemembers remainingHPtotals, ties5.',
 'After intermediateassignment/log it Abort-raises before ordinary EndOfBattle. StartBattle catches thisspecificexception, overwritesdecision0, Scene.EndBattle(0), returns0.',
 'Normal RecordStore/Pokerus/choiceanditemcleanup is not reached merelybecause intermediate1/2/5wascomputed. Otherexceptions/rescuefailures preserve reachedprefix; timeintermediate isnot finalreturn.'
],['start_end_full','battlefull','pokemon_growth_qual','pbdebug'],'100roundgate→counts/HPintermediate→raise→specificouterrescue0, distinct from normalending.')
row(554,[
 'Bothdead/one-dead predicates use current participatingparty including partnersegment; earliercapture slotnil can make countzero evenwithout normalfaint.',
 'Local removal→count/resultwriter remains required while capturemath/ball/receivepolicy are forwarded to separate contracts; forwards do not erase this actualprefix.'
],['battlefull','catch_full','start_end_full','pokemon_growth_qual'],'currentpartyremoval→ablecount/Judge, distinctcapture-policy obligations.')
row(555,[
 'UseMove common tail clearsMoldBreaker→GainExp→Arena skill/Hyper→EndTurn→Instruct/Dancer. Earlier TryUse failure CancelMoves/EndTurn/GainExp returns; PowderFire follows effectiveweather/damagegates thenCancel/End/GainExp return.',
 'Capturequalifiedgrowth temporarilymarkscaptured; entryhazardfaint Faint/GainExp/Judge/next. EOR has positivecheckpoint-afterexpiry GainExp/return or normalafterlatehandler GainExp; nestedreplacement mayreach entryhazardgrowth.',
 'Growth canoccur withdecision0 and lateractorscontinuing. No one-growth-per-battle or alreadyended prerequisite is inferred.'
],['use','growth','catch_full','switching','eor','entry_exit_handlers'],'concrete growthcallers→distinctpriorflags/HPstates→latercheckpoints; preserveCOM006weatherqualifieddamage.')
row(556,[
 'GainExp first calls wildVictoryScene iff wild&&opposingAllFainted&&!ownAllFainted, before internal/expGain return. Normal scene caller is BGM per mandatoryaudio correction, not ME.',
 'Noninternal or expGainfalse exits beforeExpAllscan/EV/Exp/participantsclear; earlier eligiblepresentation mayoccur and pendingparticipants stay.'
],['growth','battlefull','start_end_full','audio'],'wildcurrentpartycondition→presentation beforegrowthgate→qualifiedreturn.')
row(557,[
 'GainExp scans opposingbattlerobjects, skips emptyparticipants before fainted/capturedgate. ExpAll cannot rescueemptyrecord; nonemptyrecordwithzerovalidparticipants differs.',
 'Participantcount needs current p1[index]able and IsOwner(0,index). ExpAll uses globalplayerflag OR Bag:EXPALL. OnlywithoutExpAll collects currentable playersegment currentEXPSHARE OR recognizedinitialrestoreEXPSHARE.',
 'Allocation opens for numPartic>0 OR sharelistnonempty ORexpAll, but receiverloops still require currentable/playersegment/membership. OriginalOwner affects later outsiderboost, not battleownership.'
],['growth','battlefull','pokemon_growth_qual','bag','itemdata','registry_finite'],'record→currentownership/ablecensus→ExpAll/sharelists→qualifiedallocation.')
row(558,[
 'Firstplayersegmentloop skipsunable/nonparticipant-nonshare; each qualifiedrecipient EV thenExp, individualmessage only!Shadow. EV failure prevents itsExp/laterrecipients.',
 'ExpAll secondloop skips earliermembers/unable; collectiveprompt onlybeforefirstremainingrecipient, then sequential EV/Exp(showfalse). No remainingrecipient means noprompt.',
 'Processedopponent participants=[] even if allocationconditionfalse or currentrecipientszero. Failurebeforeclear leaves record with previousgainscommitted; no atomicexactlyonce guarantee.',
 'eachInTeam(0,0) excludespartnergrowth evenwhenpartnerkeepssideable; ExpAll doesnot override earlieremptyrecordskip.'
],['growth','battlefull','pokemon_growth_qual','b_init'],'orderedplayersegmentEV→Exp→ExpAllothers→participantsclear, retainpartialfailure/ownership.')
row(559,[
 'Share participant/share halves integerdivide separately thenadd; absentShare participantfullshare orExpAllnonparticipant half. Baseexp<=0return precedestrainerboost/scaled/+1 and leaves earlierEV.',
 'Trainerboost precedesscaling. Scaled exp integerdividesby5 before floatlevelratio^5/sqrt, multiply/floor, +1 onlyparticipant/share. Subsequent outsider/charm/item/affection gates and integerrounding retain exactorder.',
 'Qualified wild L2 base_exp39, sole L3 participant and no otherboost/share/charm/item/affection/cap gives floor(78/5)=15 then floor(15*(14/15)^2.5)+1=13. CompleteCATERPIErawrecord39 read; compiledloader/nativeoutcome not certified.',
 'EV currentitemmodifier fallsback onlyif firsttriggerfalse; Expmodifier fallback onlyfirstresult<0 and acceptedif>=0. Mutableinitialrestore item isnot automaticsecondstacking.',
 'EVyieldclone/fixedStat6order writes persistentEV orqualifiedShadow.saved_ev with perstat/totalclamps; no EVsubmethod calc_stats. ExistingCRE001252overlimitclampfailure scope retained without reopening.'
],['growth','item','stat_full','registry_finite','pokemon_growth_qual','caterpie_raw','shadowother'],'integerorderedmath→itemfallback→persistent/ShadowEVwrite; no fullgrowthrate/import/handlercertification.',open=['Exact growth_rate maximum/add_exp/level_from_exp receiver and all EV/Expitemfamilies require finitebinding; citation alone doesnot receive wholeWP30/WP19.'])
row(560,[],[],'',layout_reason='Growth commit/sync table header; subsequentrows separatelydecomposed.')
base['source_dictionary']=d;base['rows']=rows
assert all(k in d for r in rows for k in r['source_units'] if isinstance(k,str))
(P/'manual_batch_09a.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
print({'rows':len(rows),'children':sum(len(x['children'])for x in rows),'layout':sum('layout_reason'in x for x in rows),'open_rows':sum(bool(x.get('open'))for x in rows)})
